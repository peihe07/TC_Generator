#!/bin/bash
# Reset all TC Generator runtime state.
#
# Clears the three SQLite databases under output/:
#   - jobs.db           (parse / generate / export jobs)
#   - agent_sessions.db (agent chat history)
#   - traces.db         (agent tool-call decision trace)
#
# Does NOT touch any *.xlsx files under output/ — those are exported
# results and are kept. Pass `--all` to also remove generated xlsx files.
#
# Browser localStorage (current job, workspace layout, job history) is
# NOT reachable from a shell script; see the reminder printed at the end.

set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="$ROOT_DIR/output"

RED='\033[0;31m'; YELLOW='\033[1;33m'; GREEN='\033[0;32m'; NC='\033[0m'
info()  { echo -e "${GREEN}[reset]${NC} $1"; }
warn()  { echo -e "${YELLOW}[reset]${NC} $1"; }

if [ ! -d "$OUTPUT_DIR" ]; then
  warn "output/ does not exist — nothing to reset."
  exit 0
fi

# Warn if backend appears to be running — SQLite handles concurrent access
# but deleting a file the server has open is racy.
if pgrep -f "uvicorn api_server:app" > /dev/null; then
  echo -e "${RED}[reset]${NC} uvicorn is running. Stop it first (Ctrl+C on start.sh) before resetting."
  exit 1
fi

REMOVED=0
for db in jobs.db agent_sessions.db traces.db; do
  target="$OUTPUT_DIR/$db"
  if [ -f "$target" ]; then
    rm -f "$target"
    info "removed $db"
    REMOVED=$((REMOVED + 1))
  fi
done

if [ "${1:-}" = "--all" ]; then
  COUNT=$(find "$OUTPUT_DIR" -maxdepth 1 -name "*.xlsx" -type f | wc -l | tr -d ' ')
  if [ "$COUNT" -gt 0 ]; then
    find "$OUTPUT_DIR" -maxdepth 1 -name "*.xlsx" -type f -delete
    info "removed $COUNT exported .xlsx file(s)"
  fi
fi

info "backend state cleared ($REMOVED db files)."
warn "Browser localStorage was not touched. To clear it:"
warn "  1. open http://127.0.0.1:3000 in browser"
warn "  2. DevTools (F12) → Application → Local Storage → right-click → Clear"
warn "  or run in the browser Console:  localStorage.clear()"
