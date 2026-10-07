#!/bin/sh
# Pull new digests every INTERVAL seconds (default 300). Run it from the repo root,
# or point REPO_DIR at the clone. Used by docker-compose.yml, but works standalone too.
set -eu
REPO_DIR="${REPO_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"
INTERVAL="${INTERVAL:-300}"
cd "$REPO_DIR"
while true; do
  git pull --ff-only --quiet || echo "$(date -Is) pull failed, retrying next round" >&2
  sleep "$INTERVAL"
done
