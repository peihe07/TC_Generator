# TC Generator Modern Frontend

This package is a separate UI variant. It does not replace the existing
`frontend/` Win95-style application.

## Local Development

From the repository root:

```bash
./start-modern.sh
```

Modern UI ports:

- Frontend: `http://127.0.0.1:3433`
- Backend: `http://127.0.0.1:8013`

## Docker

Development:

```bash
docker compose -f docker-compose.modern.dev.yml up --build
```

Production:

```bash
docker compose -f docker-compose.modern.yml up --build
```

Modern Docker names are intentionally labeled and separated:

- Project: `tc-generator-modern` / `tc-generator-modern-dev`
- Frontend containers: `tc_generator_modern_frontend`,
  `tc_generator_modern_dev_frontend`
- Backend containers: `tc_generator_modern_backend`,
  `tc_generator_modern_dev_backend`
- Frontend images: `tc-generator-modern-frontend:*`
- Backend images: `tc-generator-modern-backend:*`

The modern backend writes to `output-modern/` so it does not share the legacy
runtime output directory.
