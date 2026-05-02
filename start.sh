#!/bin/bash
# Start TC Generator — backend (FastAPI) + frontend (Next.js)

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"
ENV_FILE="$ROOT_DIR/.env"
FRONTEND_ENV="$FRONTEND_DIR/.env.local"
BACKEND_PORT=8000
FRONTEND_PORT=3333
BACKEND_BASE="http://127.0.0.1:${BACKEND_PORT}"

# --- Colour helpers ---
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

info()    { echo -e "${GREEN}[TC]${NC} $1"; }
warn()    { echo -e "${YELLOW}[TC]${NC} $1"; }
error()   { echo -e "${RED}[TC]${NC} $1"; }

# --- Check .env ---
if [ ! -f "$ENV_FILE" ]; then
  warn ".env not found. AI generation will be unavailable."
  warn "Create $ENV_FILE with: OPENAI_API_KEY=sk-proj-..."
else
  info ".env found."
  set -a
  source "$ENV_FILE"
  set +a
  if [ -z "${OPENAI_API_KEY:-}" ]; then
    warn "OPENAI_API_KEY is not set in .env. AI generation and Agent chat will fail."
  else
    info "OPENAI_API_KEY detected."
  fi
fi

# --- Sync frontend .env.local ---
cat > "$FRONTEND_ENV" <<EOF
PYTHON_API_BASE=$BACKEND_BASE
EOF
info "Synced $FRONTEND_ENV"

# --- Activate Python venv ---
if [ ! -d "$ROOT_DIR/.venv" ]; then
  error ".venv not found. Run: python -m venv .venv && pip install -e .[dev]"
  exit 1
fi

source "$ROOT_DIR/.venv/bin/activate"

# --- Start backend ---
info "Starting backend on port $BACKEND_PORT..."
cd "$ROOT_DIR"
uvicorn api_server:app --app-dir "$BACKEND_DIR" --host 127.0.0.1 --port "$BACKEND_PORT" --reload --reload-dir "$BACKEND_DIR" &
BACKEND_PID=$!

# --- Start frontend ---
info "Starting frontend on port $FRONTEND_PORT..."
cd "$FRONTEND_DIR"
npm run dev -- --hostname 127.0.0.1 --port "$FRONTEND_PORT" &
FRONTEND_PID=$!

info "---"
info "Backend:  ${BACKEND_BASE}/docs"
info "Frontend: http://127.0.0.1:${FRONTEND_PORT}"
info "Press Ctrl+C to stop both."

# --- Cleanup on exit ---
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; info 'Stopped.'" EXIT INT TERM

wait
