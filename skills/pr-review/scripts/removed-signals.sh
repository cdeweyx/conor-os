#!/usr/bin/env bash
# Prints deleted lines in a unified diff that carry an interface signal, one
# "path: line" each. Empty output means the interface lens doesn't run.
# Usage: removed-signals.sh <diff.patch>
# Exit 0 either way; exit 2 only when the diff can't be read, which is a failure, never a pass.
set -u
diff_file="${1:-}"
if [ -z "$diff_file" ] || [ ! -r "$diff_file" ]; then
  echo "removed-signals: can't read diff: ${diff_file:-<none>}" >&2
  exit 2
fi

awk '
  /^diff --git / {
    path = $4; sub(/^b\//, "", path)
    skip = (path ~ /(^|\/)(package-lock\.json|pnpm-lock\.yaml|yarn\.lock|bun\.lockb?)$/ ||
            path ~ /(__snapshots__|(^|\/)(dist|build|\.next|\.build|vendor|node_modules)\/)/ ||
            path ~ /\.(snap|min\.js|min\.css|map|lock)$/)
    next
  }
  /^--- / || /^\+\+\+ / { next }
  skip { next }
  /^-/ {
    if ($0 ~ /aria-|role=|alt=|<label|htmlFor|[[:space:]]for=|scope=|focus|outline|tab[iI]ndex|prefers-(reduced-motion|contrast)|[[:space:]]lang=|[[:space:]]dir=|text-wrap|line-clamp|overflow-wrap|tabular-nums|font-variant-numeric|<(button|nav|main|ul)[[:space:]>]|<a[[:space:]]/)
      print path ": " substr($0, 2)
  }
' "$diff_file"
