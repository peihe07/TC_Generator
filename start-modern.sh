#!/bin/bash
# Start TC Generator Modern UI — separate ports and visible process labels.

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend-modern"
ENV_FILE="$ROOT_DIR/.env"
FRONTEND_ENV="$FRONTEND_DIR/.env.local"
BACKEND_PORT=8013
FRONTEND_PORT=3433
BACKEND_BASE="http://127.0.0.1:${BACKEND_PORT}"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

info()    { echo -e "${GREEN}[TC-MODERN]${NC} $1"; }
warn()    { echo -e "${YELLOW}[TC-MODERN]${NC} $1"; }
error()   { echo -e "${RED}[TC-MODERN]${NC} $1"; }

if [ ! -f "$ENV_FILE" ]; then
  warn ".env not found. AI generation will be unavailable."
else
  info ".env found."
  set -a
  source "$ENV_FILE"
  set +a
  if [ -z "${OPENAI_API_KEY:-}" ]; then
    warn "OPENAI_API_KEY is not set in .env."
  else
    info "OPENAI_API_KEY detected."
  fi
fi

cat > "$FRONTEND_ENV" <<EOF
PYTHON_API_BASE=$BACKEND_BASE
NEXT_PUBLIC_TC_GENERATOR_VARIANT=modern-local
EOF
info "Synced $FRONTEND_ENV"

if [ ! -d "$ROOT_DIR/.venv" ]; then
  error ".venv not found. Run: python -m venv .venv && pip install -e .[dev]"
  exit 1
fi

source "$ROOT_DIR/.venv/bin/activate"

info "Starting MODERN backend on port $BACKEND_PORT..."
cd "$ROOT_DIR"
uvicorn api_server:app --app-dir "$BACKEND_DIR" --host 127.0.0.1 --port "$BACKEND_PORT" --reload --reload-dir "$BACKEND_DIR" &
BACKEND_PID=$!

info "Starting MODERN frontend on port $FRONTEND_PORT..."
cd "$FRONTEND_DIR"
npm run dev -- --hostname 127.0.0.1 --port "$FRONTEND_PORT" &
FRONTEND_PID=$!

info "---"
info "Modern Backend:  ${BACKEND_BASE}/docs"
info "Modern Frontend: http://127.0.0.1:${FRONTEND_PORT}"
info "Docker dev: docker compose -f docker-compose.modern.dev.yml up --build"
info "Docker prod: docker compose -f docker-compose.modern.yml up --build"
info "Press Ctrl+C to stop both."

trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; info 'Stopped MODERN UI.'" EXIT INT TERM

wait
