"""Cached, budgeted twitterapi.io client.

Key and ledger live in ~/.config/xapi/ (twitterapi.env, ledger.jsonl), so they
outlive any workspace. Responses are cached under $XAPI_RUN/x-cache, so a repeat query is free.

CLI:
  python xapi.py search '<query>' [--pages N]
  python xapi.py timeline <userName> --since YYYY-MM-DD [--pages N]
  python xapi.py user <userName>
  python xapi.py budget
Env: XAPI_RUN (run folder, default cwd), XAPI_BUDGET (credits this run may spend, default 35000).
Images: tweet['extendedEntities']['media'][i]['media_url_https'].
"""

import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CONF = Path.home() / ".config/xapi"
LEDGER = CONF / "ledger.jsonl"
RUN = Path(os.environ.get("XAPI_RUN", ".")).resolve()
CACHE = RUN / "x-cache"
BASE = "https://api.twitterapi.io"
RUN_BUDGET = int(os.environ.get("XAPI_BUDGET", "35000"))
CREDITS_PER_TWEET = 15  # $0.15 per 1k tweets; the trial account was 100k credits
CREDITS_PER_USER = 18
MIN_CREDITS_PER_CALL = 15
ACCOUNT_CREDITS = 100_000


def _key():
    for line in (CONF / "twitterapi.env").read_text().splitlines():
        if line.startswith("TWITTERAPI_IO_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no TWITTERAPI_IO_KEY in ~/.config/xapi/twitterapi.env")


def _rows():
    if not LEDGER.exists():
        return []
    return [json.loads(x) for x in LEDGER.read_text().splitlines() if x.strip()]


def budget():
    rows = _rows()
    run = sum(r["credits"] for r in rows if r.get("run") == str(RUN))
    total = sum(r["credits"] for r in rows)
    return {"run": str(RUN), "run_spent_est": run, "run_budget": RUN_BUDGET,
            "account_spent_est": total, "account_left_est": ACCOUNT_CREDITS - total}


def _get(path, params):
    CACHE.mkdir(parents=True, exist_ok=True)
    ident = path + "?" + urllib.parse.urlencode(sorted(params.items()))
    f = CACHE / (hashlib.sha1(ident.encode()).hexdigest() + ".json")
    if f.exists():
        return json.loads(f.read_text())
    b = budget()
    if b["run_spent_est"] >= RUN_BUDGET:
        raise SystemExit(f"run budget spent ({b}); raise XAPI_BUDGET only if the user says so")
    req = urllib.request.Request(BASE + ident, headers={"X-API-Key": _key()})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(2 ** attempt * 5)
                continue
            raise
    if "tweets" not in data and isinstance(data.get("data"), dict) and "tweets" in data["data"]:
        data = {**data["data"], "has_next_page": data.get("has_next_page"), "next_cursor": data.get("next_cursor")}
    n = len(data.get("tweets") or [])
    time.sleep(1)  # one caller, one page a second: the key throttles parallel callers
    credits = CREDITS_PER_USER if "user/info" in path else max(MIN_CREDITS_PER_CALL, n * CREDITS_PER_TWEET)
    CONF.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a") as fh:
        fh.write(json.dumps({"t": time.time(), "run": str(RUN), "call": ident, "tweets": n, "credits": credits}) + "\n")
    f.write_text(json.dumps(data))
    return data


def search(query, pages=1, qtype="Latest"):
    """Advanced search. Operators: from:, since:YYYY-MM-DD_HH:MM:SS_UTC, until:, -filter:retweets, OR, quotes."""
    out, cursor = [], ""
    for _ in range(pages):
        data = _get("/twitter/tweet/advanced_search", {"query": query, "queryType": qtype, "cursor": cursor})
        out += data.get("tweets") or []
        if not data.get("has_next_page") or not data.get("next_cursor"):
            break
        cursor = data["next_cursor"]
    return out


def timeline(user, since, until=None, pages=4):
    """A user's posts in a window, via search (window-complete; last_tweets isn't)."""
    q = f"from:{user} since:{since}_00:00:00_UTC -filter:retweets"
    if until:
        q += f" until:{until}_00:00:00_UTC"
    return search(q, pages=pages)


def user(name):
    return _get("/twitter/user/info", {"userName": name}).get("data")


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d: a[a.index(k) + 1] if k in a else d  # noqa: E731
    cmd = a[0] if a else "budget"
    if cmd == "search":
        res = search(a[1], pages=int(opt("--pages", 1)))
    elif cmd == "timeline":
        res = timeline(a[1], since=opt("--since", None), pages=int(opt("--pages", 4)))
    elif cmd == "user":
        res = user(a[1])
    else:
        res = budget()
    print(json.dumps(res, indent=1))
