#!/usr/bin/env python3
"""PreToolUse hook: block a Linear issue create that's missing a required field.

Registered in ~/.claude/settings.json on mcp__claude_ai_Linear__save_issue and
reached through the ~/.claude/skills symlink. global CLAUDE.md says every issue
gets an assignee, a project, a priority and a label in the creating call; this
makes that a gate instead of a remembered rule.

A call with an `id` is an update and passes. A create (no `id`) missing any of
assignee, project, priority (1 to 4; 0 is Linear's "No priority") or labels
(`labels` or `addLabels`, non-empty) exits 2, and Claude Code shows stderr to
the model so it can fix the call. Input it can't read also exits 2, since a
check that couldn't run is a failure, never a pass.

Test: echo '{"tool_name":"mcp__claude_ai_Linear__save_issue","tool_input":{"team":"My Team","title":"x"}}' | python3 -I linear-issue-fields.py
"""
import json
import sys


def filled(value):
    if isinstance(value, str):
        return value.strip() != ""
    return value is not None


def missing_fields(tool_input):
    missing = []
    if not filled(tool_input.get("assignee")):
        missing.append('assignee ("me" for the user)')
    if not filled(tool_input.get("project")):
        missing.append("project")
    priority = tool_input.get("priority")
    if isinstance(priority, bool) or not isinstance(priority, (int, float)) or priority not in (1, 2, 3, 4):
        missing.append("priority (1 Urgent, 2 High, 3 Medium, 4 Low; 0 is no priority)")
    labels = tool_input.get("labels") or tool_input.get("addLabels")
    if not isinstance(labels, list) or not any(filled(l) for l in labels):
        missing.append("labels (list the team's labels first)")
    return missing


def main():
    try:
        payload = json.load(sys.stdin)
        tool_input = payload.get("tool_input")
        if not isinstance(tool_input, dict):
            raise ValueError("no tool_input object")
    except Exception as exc:  # noqa: BLE001, any unreadable input blocks
        print(f"linear-issue-fields hook couldn't read the tool input ({exc}), so the create is blocked. "
              "Check ~/.claude/skills/authoring-skills/scripts/linear-issue-fields.py.", file=sys.stderr)
        return 2

    if filled(tool_input.get("id")):
        return 0

    missing = missing_fields(tool_input)
    if not missing:
        return 0

    print("Linear create blocked: every new issue needs an assignee, a project, a priority and a label "
          "in the creating call (global CLAUDE.md). Missing: " + "; ".join(missing) + ". "
          "Add them and call save_issue again. If the team has no project for this work, create one "
          "or ask the user which project it belongs to.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
