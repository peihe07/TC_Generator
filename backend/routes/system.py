"""System/support FastAPI routes kept outside the main generation server."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Callable

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse

from tools import ToolError, aggregate_metrics_tool


def register_system_routes(
    app: FastAPI,
    *,
    job_store,
    job_usage: Callable[[dict | None], dict],
    tool_error_to_http: Callable[[ToolError], HTTPException],
) -> None:
    @app.get("/api/health")
    def healthcheck() -> dict:
        return {
            "status": "ok",
            "openai_configured": bool(os.environ.get("OPENAI_API_KEY")),
        }

    @app.delete("/api/admin/reset")
    def reset_all_state(request: Request) -> dict:
        """Wipe every SQLite job row — no recovery."""
        client_host = request.client.host if request.client else None
        if client_host not in {"127.0.0.1", "::1", "localhost", "testclient"}:
            raise HTTPException(status_code=403, detail="reset only allowed from localhost")

        jobs_removed = job_store.clear_all()
        job_store.vacuum()

        return {
            "status": "ok",
            "jobsRemoved": jobs_removed,
        }

    @app.get("/api/jobs/{job_id}/usage")
    def get_job_usage(job_id: str) -> dict:
        job = job_store.get(job_id)
        if not job:
            raise HTTPException(status_code=404, detail="job not found")
        usage = job_usage(job)
        return {"jobId": job_id, **usage}

    @app.get("/api/metrics/aggregate")
    def metrics_aggregate(job_ids: str | None = None) -> dict:
        selected: list[str] | None = None
        if job_ids:
            selected = [jid.strip() for jid in job_ids.split(",") if jid.strip()]
        try:
            return aggregate_metrics_tool(job_ids=selected, job_store=job_store)
        except ToolError as exc:
            raise tool_error_to_http(exc) from exc

    @app.get("/api/spec-library")
    async def list_spec_library() -> dict:
        manifest_path = Path(__file__).resolve().parent.parent.parent / "spec-index" / "manifest.json"
        if not manifest_path.is_file():
            return {"specs": []}
        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"specs": []}
        raw_specs = data.get("specs") or []
        specs = [
            {
                "name": item.get("name"),
                "sourceFile": item.get("source_file"),
                "entriesCount": item.get("entries_count"),
                "embeddingModel": item.get("embedding_model"),
                "updatedAt": item.get("updated_at"),
            }
            for item in raw_specs
            if isinstance(item, dict) and item.get("name")
        ]
        return {"specs": specs}

    @app.get("/api/jobs/{job_id}/source-status")
    async def get_source_status(job_id: str) -> dict:
        job = job_store.get(job_id)
        has_source = bool(job and job.get("rawBytes") and job.get("rawFileName"))
        return {
            "jobId": job_id,
            "hasSource": has_source,
            "rawFileName": (job or {}).get("rawFileName") if has_source else None,
        }

    @app.get("/api/export/download/{jobId}", name="download_export")
    async def download_export(jobId: str) -> FileResponse:
        job = job_store.get(jobId)
        if not job or not job.get("exportPath") or not os.path.exists(job["exportPath"]):
            raise HTTPException(status_code=404, detail="export file not found")

        return FileResponse(
            job["exportPath"],
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=os.path.basename(job["exportPath"]),
        )
