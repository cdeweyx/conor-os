"""First-look availability checks for a shortlist of names. A collision count, never a clearance.

Usage:
  python check_name.py <name> [<name> ...] [--category software|regulated] [--tlds com,app,io,ai,so,co]
                       [--prefixes get,use,try] [--ships-package] [--json out.json]

Per name, prior art first (a free handle can hide a taken name), then the rest. PASS / WARN / FAIL per line:
  prior art   GitHub: exact-name repos by stars and the github.com/<name> owner (needs an authenticated `gh`).
  app store   iTunes Search API, exact or prefix title match.
  domains     registry RDAP (Verisign, Google, Identity Digital, nic.so), whois for .co; 404 = free. "taken" is
              registered with no real site, "parked" sits on aftermarket nameservers or a for-sale page
              (expect $500 to $5,000), "live" serves a site. A live .com with no free prefix variant is FAIL.
              Prefix variants are checked only when the bare .com isn't free.
  registries  npm and PyPI (WARN only with --ships-package).
  handles     X and Instagram page titles with a browser UA (can break any day; treat as a hint).
  words       Wiktionary entry (a real word: check crowding); for --category regulated, words regulators and
              app stores flag (bet, win, guaranteed, risk-free, free, lock, sure) are FAIL.
  web search  queries printed for the agent's search tool.
  trademark   USPTO has no public search API: open the printed link in a browser, search the wordmark, and
              report live exact marks in classes 9 and 42 (plus 28 and 41 for regulated). Live exact mark in
              those classes = fail; other classes or dead marks = warn; none = "no exact hit on <date>".
Linguistics (IPA, heard-spellings, meanings in other languages, slang) is a model call in SKILL step 7.
"""

import argparse
import concurrent.futures
import datetime
import json
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request

RDAP = {
    "com": "https://rdap.verisign.com/com/v1/domain/{}",
    "net": "https://rdap.verisign.com/net/v1/domain/{}",
    "app": "https://pubapi.registry.google/rdap/domain/{}",
    "dev": "https://pubapi.registry.google/rdap/domain/{}",
    "ai": "https://rdap.identitydigital.services/rdap/domain/{}",
    "io": "https://rdap.identitydigital.services/rdap/domain/{}",
    "bet": "https://rdap.identitydigital.services/rdap/domain/{}",
    "so": "https://rdap.nic.so/domain/{}",
}
PARKING = ("afternic", "sedo", "bodis", "parkingcrew", "hugedomains", "dan.com", "above.com", "uniregistry")
REGULATED_WORDS = ("bet", "win", "guaranteed", "riskfree", "free", "lock", "sure")
BROWSER = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"}


def fetch(url, headers=None, timeout=15):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "product-naming-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(3_000_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return None, ""


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return ""


def domain(fqdn):
    tld = fqdn.rsplit(".", 1)[1]
    if tld == "co":
        out = run(["whois", fqdn])
        if not out:
            return "unknown"
        if re.search(r"not found|no match|available", out, re.I):
            return "free"
    else:
        code, _ = fetch(RDAP.get(tld, "https://rdap.org/domain/{}").format(fqdn))
        if code == 404:
            return "free"
        if code != 200:
            return f"unknown ({code})"
    ns = run(["dig", "+short", "NS", fqdn]).lower()
    if any(p in ns for p in PARKING):
        return "parked"
    _, body = fetch(f"https://{fqdn}", BROWSER, timeout=8)
    if re.search(r"for sale|buy this domain|under construction|coming soon|domain is parked", body, re.I):
        return "parked"
    return "live" if len(body) > 2000 else "taken"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("names", nargs="+")
    p.add_argument("--category", default="software")
    p.add_argument("--tlds", default="com,app,io,ai,so,co")
    p.add_argument("--prefixes", default="get,use,try")
    p.add_argument("--ships-package", action="store_true")
    p.add_argument("--json")
    a = p.parse_args()

    stamp = datetime.datetime.now().isoformat(timespec="minutes")
    report = {}

    def one(raw):
        name = re.sub(r"[^a-z0-9-]", "", raw.lower())
        lines, data = [], {"checked": stamp}

        repos = run(["gh", "api", "-X", "GET", "search/repositories", "-f", f"q={name} in:name", "-f", "sort=stars",
                     "-f", "per_page=10", "--jq", '.items[] | [.full_name, .stargazers_count, (.description // "")] | @tsv'])
        exact = [r.split("\t") for r in repos.splitlines() if r and r.split("\t")[0].split("/")[-1].lower() == name]
        top = max((int(r[1]) for r in exact), default=0)
        owner = run(["gh", "api", f"users/{name}", "--jq", "[.type, .public_repos, .followers] | @tsv"]).strip().split("\t")
        owner = owner if len(owner) == 3 else None
        busy = owner and owner[0] == "Organization" and (int(owner[1]) >= 10 or int(owner[2]) >= 100)
        data["github"] = {"exact_repos": exact, "owner": owner}
        lines.append(("FAIL" if top >= 1000 or busy else "WARN" if top >= 100 or owner else "PASS",
                      f"prior art: {len(exact)} exact repo(s), top {top} stars"
                      + (f" ({exact[0][0]}: {exact[0][2][:70]})" if exact else "")
                      + (f"; github.com/{name} is a {owner[0]} ({owner[1]} repos, {owner[2]} followers)" if owner else f"; github.com/{name} free")))

        _, body = fetch(f"https://itunes.apple.com/search?term={urllib.parse.quote(raw)}&entity=software&limit=25")
        try:
            titles = [r.get("trackName", "") for r in json.loads(body).get("results", [])]
        except ValueError:
            titles = []
        hits = [t for t in titles if t.lower() == raw.lower() or t.lower().startswith(raw.lower() + " ") or t.lower().startswith(raw.lower() + ":")]
        data["app_store"] = hits
        lines.append(("WARN" if hits else "PASS", "app store: " + (", ".join(hits[:4]) if hits else "no exact title")))

        doms = {f"{name}.{t}": domain(f"{name}.{t}") for t in a.tlds.split(",") if t}
        if doms.get(f"{name}.com") != "free":
            doms.update({f"{pre}{name}.com": domain(f"{pre}{name}.com") for pre in a.prefixes.split(",") if pre})
        data["domains"] = doms
        com = doms.get(f"{name}.com")
        prefix_free = [d for d, st in doms.items() if st == "free" and d.endswith(".com") and d != f"{name}.com"]
        lines.append(("PASS" if com == "free" else "FAIL" if com == "live" and not prefix_free else "WARN",
                      "domains: " + ", ".join(f"{d} {s}" for d, s in doms.items())
                      + (" (parked: expect $500 to $5,000, ask)" if com == "parked" else "")))

        npm, _ = fetch(f"https://registry.npmjs.org/{name}")
        pypi, _ = fetch(f"https://pypi.org/pypi/{name}/json")
        taken = [r for r, c in (("npm", npm), ("PyPI", pypi)) if c == 200]
        lines.append(("WARN" if taken and a.ships_package else "PASS", "registries: " + (", ".join(taken) + " taken" if taken else "npm and PyPI free")))

        handles = []
        for site, url, free_title in (("X", f"https://x.com/{name}", None), ("Instagram", f"https://www.instagram.com/{name}/", "Instagram")):
            code, body = fetch(url, BROWSER, timeout=10)
            title = (re.search(r"<title>(.*?)</title>", body, re.S) or [None, ""])[1].strip()
            handles.append(f"{site} {'free' if code == 404 or title == free_title else 'taken' if title else 'unknown'}")
        data["handles"] = handles
        lines.append(("WARN" if any("taken" in h for h in handles) else "PASS", "handles: " + ", ".join(handles) + " (hint only)"))

        _, wk = fetch(f"https://en.wiktionary.org/w/api.php?action=query&format=json&titles={urllib.parse.quote(name)}")
        real_word = bool(wk) and '"-1"' not in wk
        flagged = [w for w in REGULATED_WORDS if w in name] if a.category == "regulated" else []
        lines.append(("FAIL" if flagged else "WARN" if real_word else "PASS",
                      ("words: contains " + ", ".join(flagged) + " (regulators and app stores flag these in a regulated category)" if flagged
                       else "words: a dictionary word, so expect crowding" if real_word else "words: not a dictionary entry")))

        data["search"] = [f'"{raw}" {a.category}', f'"{raw}" app', f'"{raw}" software', f'"{raw}" company']
        lines.append(("TODO", "web search: " + " | ".join(data["search"])))
        classes = "9, 42, 28, 41" if a.category == "regulated" else "9, 42"
        data["uspto"] = "https://tmsearch.uspto.gov/search/search-information"
        lines.append(("TODO", f"trademark: search the wordmark at {data['uspto']}; report live exact marks in classes {classes}. Not legal advice."))

        return raw, {**data, "lines": lines}

    # Names run in parallel (each check is network-bound); output keeps the input order.
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for raw, data in pool.map(one, a.names):
            report[raw] = data
            print(f"\n{raw}  (checked {stamp})")
            for st, msg in data["lines"]:
                print(f"  {st:<4}  {msg}")

    if a.json:
        json.dump(report, open(a.json, "w"), indent=2)


if __name__ == "__main__":
    main()
