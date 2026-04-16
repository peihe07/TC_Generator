#!/bin/bash
# Start TC Generator — backend (FastAPI) + frontend (Next.js)

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$ROOT_DIR/src"
FRONTEND_DIR="$ROOT_DIR/frontend"
ENV_FILE="$ROOT_DIR/.env"
FRONTEND_ENV="$FRONTEND_DIR/.env.local"
BACKEND_PORT=8000
FRONTEND_PORT=3000

# --- Colour helpers ---
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

info()    { echo -e "${GREEN}[TC]${NC} $1"; }
warn()    { echo -e "${YELLOW}[TC]${NC} $1"; }
error()   { echo -e "${RED}[TC]${NC} $1"; }

# --- Check .env ---
if [ ! -f "$ENV_FILE" ]; then
  warn ".env not found. AI generation will be unavailable."
  warn "Create $ENV_FILE with: ANTHROPIC_API_KEY=sk-ant-api03-..."
else
  info ".env found."
fi

# --- Write frontend .env.local if missing ---
if [ ! -f "$FRONTEND_ENV" ]; then
  echo "NEXT_PUBLIC_PYTHON_API_BASE=http://localhost:${BACKEND_PORT}" > "$FRONTEND_ENV"
  info "Created $FRONTEND_ENV"
fi

# --- Activate Python venv ---
if [ ! -d "$ROOT_DIR/.venv" ]; then
  error ".venv not found. Run: python -m venv .venv && pip install -e .[dev]"
  exit 1
fi

source "$ROOT_DIR/.venv/bin/activate"

# --- Start backend ---
info "Starting backend on port $BACKEND_PORT..."
cd "$ROOT_DIR"
uvicorn src.api_server:app --reload --port "$BACKEND_PORT" &
BACKEND_PID=$!

# --- Start frontend ---
info "Starting frontend on port $FRONTEND_PORT..."
cd "$FRONTEND_DIR"
npm run dev -- --port "$FRONTEND_PORT" &
FRONTEND_PID=$!

info "---"
info "Backend:  http://localhost:${BACKEND_PORT}/docs"
info "Frontend: http://localhost:${FRONTEND_PORT}"
info "Press Ctrl+C to stop both."

# --- Cleanup on exit ---
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; info 'Stopped.'" EXIT INT TERM

wait
