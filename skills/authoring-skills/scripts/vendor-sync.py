#!/usr/bin/env python3
"""Install the third-party skills pinned in vendor.json into skills/<name>.

Run from anywhere with:  python3 -I skills/authoring-skills/scripts/vendor-sync.py [--check] [name ...]

For each manifest entry it fetches the pinned commit (shallow, sparse, blobs
only for the paths it needs), copies the upstream path into skills/<name>
minus `exclude`, copies the repo-root `notices` (LICENSE, NOTICE.md) into the
folder, applies the `frontmatter` overrides to SKILL.md, and copies any
upstream `agents` into ~/.claude/agents. It writes nothing else. Paths in
`keep` (a downloaded binary, say) survive a reinstall.

Idempotent: an installed skill that already matches prints "ok". One that
differs prints a file summary, then is replaced. --check only reports and
exits 1 on any drift, so it doubles as "does this folder still match upstream?".
A skill folder that's a symlink is left alone.

Stdlib only. Needs git 2.25+ (sparse-checkout) on PATH.
"""

import filecmp
import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
MANIFEST = REPO / "vendor.json"
SKILLS = REPO / "skills"
AGENTS = Path.home() / ".claude" / "agents"


def git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def fetch(repo, commit, paths, into):
    """Sparse, shallow checkout of `paths` at `commit` into `into`."""
    into.mkdir(parents=True)
    git(into, "init", "-q")
    git(into, "remote", "add", "origin", repo)
    git(into, "sparse-checkout", "set", "--no-cone", *["/" + p.strip("/") for p in paths])
    git(into, "fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", commit)
    git(into, "-c", "advice.detachedHead=false", "checkout", "-q", "FETCH_HEAD")


def render(key, value):
    if key == "description":
        lines = textwrap.wrap(value, width=76, break_long_words=False, break_on_hyphens=False)
        return [f"{key}: >-"] + ["  " + l for l in lines]
    return [f"{key}: {value}"]


def override_frontmatter(skill_md, overrides):
    """Replace or add top-level frontmatter keys; leave every other line as upstream wrote it."""
    if not overrides:
        return
    lines = skill_md.read_text(encoding="utf-8").split("\n")
    if lines[0].strip() != "---":
        sys.exit(f"{skill_md}: no frontmatter to override")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    head, rest = lines[1:end], lines[end:]
    # Split the frontmatter into top-level keys, each with its continuation lines.
    blocks = []
    for line in head:
        if line and not line[0].isspace() and ":" in line:
            blocks.append([line.split(":", 1)[0], [line]])
        elif blocks:
            blocks[-1][1].append(line)
        else:
            blocks.append([None, [line]])
    pending = dict(overrides)
    for block in blocks:
        if block[0] in pending:
            block[1] = render(block[0], pending.pop(block[0]))
    # New keys go after description, so name and description stay on top.
    at = next((i + 1 for i, b in enumerate(blocks) if b[0] == "description"), len(blocks))
    for key, value in pending.items():
        blocks.insert(at, [key, render(key, value)])
        at += 1
    out = ["---"] + [l for b in blocks for l in b[1]] + rest
    skill_md.write_text("\n".join(out), encoding="utf-8")


def stage(entry, src, into):
    """Build the installed folder for one entry under `into`."""
    exclude = set(entry.get("exclude", []))
    shutil.copytree(src / entry["path"], into,
                    ignore=lambda d, names: [n for n in names if Path(d) == src / entry["path"] and n in exclude])
    for notice in entry.get("notices", []):
        shutil.copy2(src / notice, into / notice)
    override_frontmatter(into / "SKILL.md", entry.get("frontmatter"))


def files(root, keep=()):
    out = {}
    for p in root.rglob("*"):
        rel = p.relative_to(root).as_posix()
        if p.is_file() and not any(rel == k or rel.startswith(k + "/") for k in keep):
            out[rel] = p
    return out


def compare(new, old, keep):
    a, b = files(new), files(old, keep) if old.exists() else {}
    added = sorted(set(a) - set(b))
    removed = sorted(set(b) - set(a))
    changed = sorted(f for f in set(a) & set(b) if not filecmp.cmp(a[f], b[f], shallow=False))
    return added, removed, changed


def install(staged, dest, keep):
    held = Path(tempfile.mkdtemp(prefix="vendor-keep-"))
    for k in keep:
        if (dest / k).exists():
            (held / k).parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(dest / k), str(held / k))
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(staged, dest)
    for k in keep:
        if (held / k).exists():
            (dest / k).parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(held / k), str(dest / k))
    shutil.rmtree(held)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    entries = json.loads(MANIFEST.read_text(encoding="utf-8"))["skills"]
    if args:
        unknown = set(args) - {e["name"] for e in entries}
        if unknown:
            sys.exit(f"not in vendor.json: {', '.join(sorted(unknown))}")
        entries = [e for e in entries if e["name"] in args]

    drift = False
    with tempfile.TemporaryDirectory(prefix="vendor-sync-") as tmp:
        tmp = Path(tmp)
        checkouts = {}
        for e in entries:
            name, dest, keep = e["name"], SKILLS / e["name"], e.get("keep", [])
            if dest.is_symlink():
                print(f"{name}: skipped, skills/{name} is a symlink")
                continue
            key = (e["repo"], e["commit"])
            if key not in checkouts:
                group = [x for x in entries if (x["repo"], x["commit"]) == key]
                paths = {p for x in group for p in [x["path"], *x.get("notices", []), *([x["agents"]] if x.get("agents") else [])]}
                checkouts[key] = tmp / f"src{len(checkouts)}"
                try:
                    fetch(e["repo"], e["commit"], sorted(paths), checkouts[key])
                except subprocess.CalledProcessError as err:
                    sys.exit(f"{name}: fetch of {e['repo']}@{e['commit'][:7]} failed: {err.stderr.decode().strip()}")
            src = checkouts[key]
            staged = tmp / "staged" / name
            stage(e, src, staged)
            added, removed, changed = compare(staged, dest, keep)
            pin = f"{e['commit'][:7]}"
            if not (added or removed or changed):
                print(f"{name}: ok @ {pin}")
            else:
                drift = True
                print(f"{name}: {'would change' if check else 'installed'} @ {pin} "
                      f"(+{len(added)} -{len(removed)} ~{len(changed)})")
                for tag, group in (("+", added), ("-", removed), ("~", changed)):
                    for f in group:
                        print(f"  {tag} {f}")
                if not check:
                    install(staged, dest, keep)
            if e.get("agents"):
                for agent in sorted((src / e["agents"]).glob("*.md")):
                    target = AGENTS / agent.name
                    if target.is_file() and filecmp.cmp(agent, target, shallow=False):
                        continue
                    drift = True
                    print(f"  {'would copy' if check else 'copied'} agent {agent.name} -> {target}")
                    if not check:
                        AGENTS.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(agent, target)
    return 1 if (check and drift) else 0


if __name__ == "__main__":
    sys.exit(main())
