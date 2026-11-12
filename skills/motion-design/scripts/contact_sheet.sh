#!/usr/bin/env bash
# Tile a motion recording into one contact sheet so a single look covers the timeline.
# Usage: contact_sheet.sh input.webm [fps] [cols] [rows] [width]
set -euo pipefail
in="${1:?input video}"; fps="${2:-10}"; cols="${3:-8}"; rows="${4:-3}"; width="${5:-480}"
out="${in%.*}-sheet.png"
ffmpeg -loglevel error -y -i "$in" -vf "fps=${fps},scale=${width}:-1,tile=${cols}x${rows}" "$out"
echo "$out"
