#!/usr/bin/env python3
"""Measure every skill's always-on and on-invoke cost against the house caps.

Run from anywhere with:  python3 -I skills/authoring-skills/scripts/skill-budget.py [skills_dir]

Stdlib only. Frontmatter is parsed by hand (descriptions use folded `>` YAML
and PyYAML isn't installed). Tokens are estimated as body words * 1.4.

Fails (exit 1) when, for any skill not in vendor.json (vendored skills report
only, except a description we override, which still has to fit the cap):
  - the description is over 1,024 chars (the spec cap),
  - the body is over 4,000 words (the hard cap; 3,500 words, ~5k tokens, is the
    compaction slice and the target, flagged but not failed),
  - the body carries more than 5 dated parentheticals like "(2026-",
  - the frontmatter or description can't be read (a check that can't run fails),
  - a role in agents/ pins an alias instead of a full model ID, or a model the
    "Sweep filed for" line in model-routing.md doesn't list (a model shipped:
    file the sweep ticket, authoring-skills "When a model ships"),
  - an always-read reference is over 1,500 words. A reference is always-read
    when SKILL.md writes "every run" (or "every <unit>" for a per-unit loop:
    "every surface", "every issue") right after its backticked path, as in
    "Read `references/learnings.md` every run" (authoring-skills, Size and
    frontmatter). A marked path that doesn't resolve fails too,
  - a skill folder has no row in README.md, or its `name` isn't its folder name,
  - a non-vendored skill .md file has an em dash (Claude echoes the punctuation it
    reads; research/ excepted),
  - a reference over 100 lines has no "Contents" line in its first 12 lines,
  - an agents/*.md frontmatter isn't strict YAML (each top-level line a
    `key: value`, a value with ": " or a leading YAML indicator quoted, name,
    description and model present, name matching the file),
  - a line that spawns an agent (a fresh, helper or numbered agent, or a
    backticked role followed by "agent") has no `Model:` on it,
  - a skill file carries a British spelling (writing-style) or a home-directory
    path like a file:// URL into a home folder (it breaks in a worktree, on
    another machine, and in a cloud run). research/ folders are raw sources and aren't checked.
Descriptions over the 550-char target are flagged but don't fail.
Also fails when a vendor.json skill isn't on disk (run vendor-sync.py).
Skips skills/synced/ and symlinked skills that aren't real directories.

ALLOWED lists known failures another change owns (empty when nothing is owed). Each entry has the date it
was added and who empties it; an allowed failure prints as ALLOWED, and an
entry that no longer matches anything prints as STALE so it gets deleted.
"""

import json
import re
import sys
from pathlib import Path

DESC_CAP = 1024
DESC_TARGET = 550
BODY_WORDS_TARGET = 3500
BODY_WORDS_CAP = 4000
DATED_CAP = 5
ALWAYS_READ_CAP = 1500
TOKENS_PER_WORD = 1.4
SKIP_DIRS = {"synced"}
DATED = re.compile(r"\(20\d\d-\d\d")

# A backticked .md path, an optional (aside), optional "in full" / "end to end",
# then "every run" or "every <unit>". An optional "<skill>'s " before the path
# points at another skill's file.
ALWAYS_READ = re.compile(
    r"(?:\b(?P<owner>[a-z0-9-]+)'s\s+)?`(?P<path>[^`\s]+\.md)`(?:\s*\([^)]*\))?"
    r"[\s,]+(?:(?:in full|end to end)[\s,]+)?every (?P<unit>run|surface|issue|milestone|round)\b")

ROLE = r"`(?:worker|critic|researcher|planner)`"
SPAWN = re.compile(
    r"\b(?:one|two|three|four|five|six|a|an|each|every|fresh|fresh-context|new|separate)\s+(?:[\w-]+\s+){0,3}" + ROLE
    + r"|" + ROLE + r"(?:'s)?\s+(?:agents?|subagents?|per)\b"
    + r"|\b(?:helper|fresh|fresh-context|new|separate)\s+(?:sub)?agents?\b"
    + r"|\bsub-?agents?\s+(?:from|per|for each|in parallel)\b",
    re.I)
# The routing legend names every role by design; learnings files quote history.
SPAWN_EXEMPT = {"model-routing.md"}

BRITISH = {
    "colour": "color", "colours": "colors", "coloured": "colored", "favourite": "favorite",
    "favourites": "favorites", "favour": "favor", "favoured": "favored", "flavour": "flavor",
    "behaviour": "behavior", "behaviours": "behaviors", "honour": "honor", "honoured": "honored",
    "neighbour": "neighbor", "neighbours": "neighbors", "centre": "center", "centred": "centered",
    "licence": "license", "licences": "licenses", "judgement": "judgment", "catalogue": "catalog",
    "grey": "gray", "greys": "grays", "greying": "graying", "cosy": "cozy", "labelled": "labeled",
    "labelling": "labeling", "cancelled": "canceled", "modelling": "modeling",
    "summarise": "summarize", "summarised": "summarized", "generalise": "generalize",
    "generalises": "generalizes", "generalised": "generalized", "capitalised": "capitalized",
    "emphasise": "emphasize", "emphasised": "emphasized", "organise": "organize",
    "organised": "organized", "organisation": "organization", "recognise": "recognize",
    "realise": "realize", "prioritise": "prioritize", "optimise": "optimize", "customise": "customize",
    "minimise": "minimize", "maximise": "maximize", "normalise": "normalize", "visualise": "visualize",
    "analyse": "analyze", "analysed": "analyzed", "practise": "practice", "artefact": "artifact",
    "ageing": "aging", "sceptical": "skeptical", "programme": "program", "fulfil": "fulfill",
}
BRITISH_RE = re.compile(r"\b(" + "|".join(sorted(BRITISH, key=len, reverse=True)) + r")\b", re.I)
HOME_PATH = re.compile(r"file:///Users/|(?<![\w~.])/Users/[\w.-]+/")
TEXT_SUFFIXES = {".md", ".py", ".mjs", ".js", ".html", ".css", ".sh"}

# Known failures another change owns: (check, path, needle in the message) ->
# (date added, who empties it). Delete an entry once it prints STALE.
ALLOWED = {}


def strip_frontmatter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[i + 1:]), i + 1
    return text, 0


def check_always_read(root, skill_dirs):
    """Return (rows, failures) for references SKILL.md marks as read every run."""
    rows, failures = [], []
    for d in skill_dirs:
        body, _ = strip_frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
        seen = set()
        for m in ALWAYS_READ.finditer(body):
            owner = m.group("owner")
            base = root / owner if owner and (root / owner / "SKILL.md").is_file() else d
            target = (base / m.group("path")).resolve()
            key = str(target)
            if key in seen:
                continue
            seen.add(key)
            try:
                rel = target.relative_to(root.resolve()).as_posix()
            except ValueError:
                rel = m.group("path")
            if not target.is_file():
                failures.append(("always-read", rel, f"{d.name}: always-read `{m.group('path')}` doesn't resolve"))
                continue
            words = len(target.read_text(encoding="utf-8").split())
            rows.append((d.name, rel, m.group("unit"), words))
            if words > ALWAYS_READ_CAP:
                failures.append(("always-read", rel, f"{rel}: {words} words, read every {m.group('unit')} > {ALWAYS_READ_CAP}"))
    return rows, failures


def check_readme(repo, names):
    try:
        readme = (repo / "README.md").read_text(encoding="utf-8")
    except OSError:
        return [("readme", "README.md", "README.md: unreadable")]
    return [("readme", f"{n}/", f"{n}: no row in README.md") for n in names if f"[{n}](" not in readme]


def skill_files(d):
    for f in sorted(d.rglob("*")):
        if f.is_file() and f.suffix in TEXT_SUFFIXES and "research" not in f.relative_to(d).parts:
            yield f


def check_text(root, skill_dirs):
    """Spawn lines without Model:, British spellings, home-directory paths."""
    failures = []
    me = Path(__file__).resolve()
    for d in skill_dirs:
        for f in skill_files(d):
            if f.resolve() == me:  # holds the word list and the patterns
                continue
            rel = f.relative_to(root).as_posix()
            text = f.read_text(encoding="utf-8", errors="replace")
            offset = 0
            if f.suffix == ".md":
                text, offset = strip_frontmatter(text)
            quiet = f.name in SPAWN_EXEMPT or "learnings" in f.name or "failed-prompts" in f.name
            for i, line in enumerate(text.splitlines(), offset + 1):
                if f.suffix == ".md" and not quiet and SPAWN.search(line) and "Model:" not in line:
                    failures.append(("model-line", rel, f"{rel}:{i}: spawns an agent with no `Model:` line"))
                for m in BRITISH_RE.finditer(line):
                    w = m.group(0)
                    failures.append(("spelling", rel, f"{rel}:{i}: '{w}', write '{BRITISH[w.lower()]}'"))
                if f.suffix == ".md" and EM_DASH in line:
                    failures.append(("em-dash", rel, f"{rel}:{i}: em dash; use a comma, period, or parentheses"))
                if HOME_PATH.search(line):
                    failures.append(("home-path", rel, f"{rel}:{i}: home-directory path; point at the skill's file instead"))
    return failures


EM_DASH = "\u2014"
YAML_INDICATOR = tuple("[]{}&*!|>'\"%@`#,?:-")


def check_name(root, skill_dirs):
    failures = []
    for d in skill_dirs:
        fields, _ = parse_frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
        name = (fields or {}).get("name", "")
        if name != d.name:
            failures.append(("name", f"{d.name}/", f"{d.name}: frontmatter name '{name}' doesn't match the folder"))
    return failures


def check_contents(root, skill_dirs):
    """A reference over 100 lines needs a contents line near the top."""
    failures = []
    for d in skill_dirs:
        for f in skill_files(d):
            if f.suffix != ".md" or f.name == "SKILL.md":
                continue
            lines = f.read_text(encoding="utf-8").splitlines()
            if len(lines) > 100 and not any("contents" in l.lower() for l in lines[:12]):
                rel = f.relative_to(root).as_posix()
                failures.append(("contents", rel, f"{rel}: {len(lines)} lines and no Contents line in the first 12"))
    return failures


def check_agent_yaml(repo):
    """Strict frontmatter for agents/*.md: Claude Code drops an agent whose YAML doesn't parse."""
    failures = []
    for f in sorted((repo / "agents").glob("*.md")):
        rel = f"agents/{f.name}"
        lines = f.read_text(encoding="utf-8").split("\n")
        if not lines or lines[0].strip() != "---" or "---" not in [l.strip() for l in lines[1:]]:
            failures.append(("agent-yaml", rel, f"{rel}: no frontmatter fenced by ---"))
            continue
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        keys = set()
        for i, line in enumerate(lines[1:end], 2):
            if not line.strip() or line.startswith((" ", "\t")):
                if line.startswith("\t"):
                    failures.append(("agent-yaml", rel, f"{rel}:{i}: tab indentation"))
                continue
            m = re.match(r"^([A-Za-z0-9_-]+):(?: (.*))?$", line)
            if not m:
                failures.append(("agent-yaml", rel, f"{rel}:{i}: not a 'key: value' line"))
                continue
            key, value = m.group(1), (m.group(2) or "").strip()
            if key in keys:
                failures.append(("agent-yaml", rel, f"{rel}:{i}: duplicate key '{key}'"))
            keys.add(key)
            quoted = len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'"
            if value and not quoted and value not in (">", "|", ">-", "|-"):
                if ": " in value or " #" in value or value.startswith(YAML_INDICATOR):
                    failures.append(("agent-yaml", rel, f"{rel}:{i}: '{key}' value needs quotes (': ', ' #' or a leading indicator)"))
        fields, _ = parse_frontmatter("\n".join(lines))
        for k in ("name", "description", "model"):
            if k not in keys:
                failures.append(("agent-yaml", rel, f"{rel}: missing '{k}'"))
        if (fields or {}).get("name") and fields["name"] != f.stem:
            failures.append(("agent-yaml", rel, f"{rel}: name '{fields['name']}' doesn't match the file"))
    return failures


def apply_allowed(failures):
    """Split (check, path, message) failures into (failing, allowed, stale entries)."""
    failing, allowed, used = [], [], set()
    for check, path, msg in failures:
        hit = next((k for k in ALLOWED if k[0] == check and path.startswith(k[1]) and k[2] in msg), None)
        if hit:
            used.add(hit)
            allowed.append(f"{msg}  [allowed {ALLOWED[hit][0]}: {ALLOWED[hit][1]}]")
        else:
            failing.append(msg)
    stale = [f"{k[0]} {k[1]} {k[2]}".strip() for k in ALLOWED if k not in used]
    return failing, allowed, stale


def parse_frontmatter(text):
    """Return (fields, body). fields maps top-level keys to strings."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, text
    fields = {}
    i = 1
    while i < end:
        line = lines[i]
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, value = m.group(1), m.group(2).strip()
        if value[:1] in (">", "|"):
            folded = value.startswith(">")
            block = []
            i += 1
            while i < end and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                block.append(lines[i].strip())
                i += 1
            if folded:
                # Folded scalar: lines join with spaces, blank lines become newlines.
                paras, cur = [], []
                for b in block:
                    if b:
                        cur.append(b)
                    elif cur:
                        paras.append(" ".join(cur))
                        cur = []
                if cur:
                    paras.append(" ".join(cur))
                fields[key] = "\n".join(paras)
            else:
                fields[key] = "\n".join(block).strip()
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key] = value
        i += 1
    body = "\n".join(lines[end + 1:])
    return fields, body


def check_model_pins(repo):
    """Return failures for role pins that are aliases or that no sweep covers."""
    agents = repo / "agents"
    routing = repo / "skills" / "authoring-skills" / "references" / "model-routing.md"
    if not agents.is_dir():
        return []
    try:
        line = next(l for l in routing.read_text(encoding="utf-8").splitlines()
                    if l.startswith("Sweep filed for:"))
    except (OSError, StopIteration):
        return [f"model pins: no 'Sweep filed for:' line in {routing}"]
    swept = set(re.findall(r"claude-[a-z0-9-]+", line))
    failures = []
    for f in sorted(agents.glob("*.md")):
        fields, _ = parse_frontmatter(f.read_text(encoding="utf-8"))
        model = (fields or {}).get("model", "")
        if not model.startswith("claude-"):
            failures.append(f"agents/{f.name}: model '{model}' is an alias or missing; pin the full ID")
        elif model not in swept:
            failures.append(f"agents/{f.name}: {model} has no model sweep filed; see authoring-skills, When a model ships")
    return failures


def load_vendored(repo):
    """Map each vendor.json skill name to its entry."""
    try:
        return {e["name"]: e for e in json.loads((repo / "vendor.json").read_text())["skills"]}
    except (OSError, ValueError, KeyError):
        return {}


def load_overrides():
    path = Path.home() / ".claude" / "settings.json"
    try:
        return json.loads(path.read_text()).get("skillOverrides", {}) or {}
    except OSError:
        print(f"warning: {path} not found; listing totals assume no skillOverrides", file=sys.stderr)
    except ValueError as e:
        print(f"warning: {path} isn't valid JSON ({e}); listing totals assume no skillOverrides", file=sys.stderr)
    return {}


def main():
    default = Path(__file__).resolve().parents[2]
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 1
    overrides = load_overrides()
    vendored_skills = load_vendored(root.parent)

    rows, failures, ours_dirs = [], [], []
    for d in sorted(root.iterdir()):
        if d.name in SKIP_DIRS or d.is_symlink() or not d.is_dir():
            continue
        skill_md = d / "SKILL.md"
        if not skill_md.is_file():
            continue
        fields, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        name = d.name
        vendored = name in vendored_skills
        if fields is None or not fields.get("description"):
            failures.append(f"{name}: frontmatter or description unreadable")
            continue
        desc = len(fields["description"])
        words = len(body.split())
        dated = len(DATED.findall(body))
        disabled = fields.get("disable-model-invocation", "").lower() == "true"
        override = overrides.get(name, "on")
        rows.append((name, desc, words, round(words * TOKENS_PER_WORD), dated, disabled, override, vendored))
        if vendored:
            ours = "description" in vendored_skills[name].get("frontmatter", {})
            if ours and desc > DESC_CAP:
                failures.append(f"{name}: description {desc} chars > {DESC_CAP} (override in vendor.json)")
            continue
        ours_dirs.append(d)
        if desc > DESC_CAP:
            failures.append(f"{name}: description {desc} chars > {DESC_CAP}")
        if words > BODY_WORDS_CAP:
            failures.append(f"{name}: body {words} words > {BODY_WORDS_CAP}")
        if dated > DATED_CAP:
            failures.append(f"{name}: {dated} dated parentheticals > {DATED_CAP}")

    hdr = f"{'skill':<26}{'desc':>6}{'words':>7}{'tok(w*1.4)':>12}{'dated':>7}  {'dmi':<4}{'override':<11}notes"
    print(hdr)
    print("-" * len(hdr))
    listed_total = 0
    for name, desc, words, tok, dated, disabled, override, vendored in rows:
        listed = not disabled and override == "on"
        if listed:
            listed_total += desc
        notes = []
        if vendored:
            notes.append("vendored, report only")
        if listed and desc > DESC_TARGET:
            notes.append(f"desc over {DESC_TARGET} target")
        if not vendored and BODY_WORDS_TARGET < words <= BODY_WORDS_CAP:
            notes.append(f"body over {BODY_WORDS_TARGET} target")
        print(f"{name:<26}{desc:>6}{words:>7}{tok:>12}{dated:>7}  {'yes' if disabled else '-':<4}{override:<11}{', '.join(notes)}")

    missing = sorted(set(vendored_skills) - {r[0] for r in rows})
    if missing:
        # A fresh worktree has none of them: vendored skills are gitignored.
        failures.append(f"vendored skills not installed in this worktree ({', '.join(missing)}). "
                        f"Run vendor-sync.py in this worktree: python3 -I skills/authoring-skills/scripts/vendor-sync.py")
    failures += check_model_pins(root.parent)

    read_rows, keyed = check_always_read(root, ours_dirs)
    keyed += check_readme(root.parent, [r[0] for r in rows])
    keyed += check_text(root, ours_dirs)
    keyed += check_name(root, ours_dirs)
    keyed += check_contents(root, ours_dirs)
    keyed += check_agent_yaml(root.parent)
    failing, allowed, stale = apply_allowed(keyed)
    failures += failing

    print()
    print(f"Always-read references (marked 'every run' or 'every <unit>' in SKILL.md), cap {ALWAYS_READ_CAP} words:")
    for _, rel, unit, words in read_rows:
        print(f"  {rel:<52}{words:>6}  every {unit}{'  OVER' if words > ALWAYS_READ_CAP else ''}")

    print()
    print(f"Skills measured: {len(rows)}. Tokens estimated as body words * {TOKENS_PER_WORD}.")
    print(f"Description chars, listed skills only (not disable-model-invocation, override 'on'): {listed_total} (~{listed_total // 4} tokens)")
    if allowed:
        print(f"\nALLOWED ({len(allowed)}, owned by another change; see ALLOWED in this script):")
        for a in allowed:
            print(f"  {a}")
    if stale:
        print("\nSTALE allowlist entries (nothing matches them now; delete them):")
        for s in stale:
            print(f"  {s}")
    if failures:
        print(f"\nFAIL ({len(failures)}):")
        for f in failures:
            print(f"  {f}")
        return 1
    print("\nPASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
