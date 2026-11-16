#!/usr/bin/env python3
"""PostToolUse hook: tell a long main session to hand off at its next clean break.

Registered in ~/.claude/settings.json with no matcher, reached through the
~/.claude/skills symlink. Every call re-reads the whole context, so a lead
session at 700k costs several times one at 150k per turn. In one week,
18 main sessions went past 400k.

It reads the session's transcript tail for the last API call's context
(input + cache read + cache write). Past 400k it adds one line to the model's
context, then again at each further 100k, once per threshold per session.
Subagents are skipped: they're sized by their brief, not handed off.

It never blocks: any error exits 0 with no output, since a missed nudge costs
tokens, not correctness.

Test: echo '{"session_id":"t","transcript_path":"<a main .jsonl>"}' | python3 -I context-nudge.py
"""
import json
import os
import sys

FIRST = 400_000
STEP = 100_000
TAIL_BYTES = 2_000_000
STATE_DIR = os.path.expanduser("~/.claude/state/context-nudge")


def last_context(path):
    with open(path, "rb") as f:
        f.seek(0, os.SEEK_END)
        f.seek(max(0, f.tell() - TAIL_BYTES))
        lines = f.read().decode("utf-8", "ignore").splitlines()
    for line in reversed(lines):
        try:
            usage = json.loads(line)["message"]["usage"]
        except (ValueError, KeyError, TypeError):
            continue
        return (usage.get("input_tokens", 0)
                + usage.get("cache_read_input_tokens", 0)
                + usage.get("cache_creation_input_tokens", 0))
    return 0


def main():
    data = json.load(sys.stdin)
    path = data.get("transcript_path") or ""
    if data.get("agent_id") or "/subagents/" in path or not os.path.isfile(path):
        return
    ctx = last_context(path)
    if ctx < FIRST:
        return
    threshold = FIRST + (ctx - FIRST) // STEP * STEP
    os.makedirs(STATE_DIR, exist_ok=True)
    state = os.path.join(STATE_DIR, str(data.get("session_id", "unknown")))
    try:
        done = int(open(state).read().strip() or 0)
    except (OSError, ValueError):
        done = 0
    if threshold <= done:
        return
    with open(state, "w") as f:
        f.write(str(threshold))
    note = (f"Context is at {ctx // 1000}k tokens, and every call re-reads all of it. "
            "At the next clean break (no agent mid-run, a merge batch landed, a thread "
            "finished), run the skill pause and write the handoff for a fresh session "
            "as one copyable block. Don't stop work mid-step for this.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                             "additionalContext": note}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
