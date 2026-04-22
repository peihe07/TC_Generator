"""Pytest fixtures：把所有 SQLite store 指到 tmp 路徑，避免 test 跑下去污染或
清空 production `output/` 下的真實 DB。

之前發生過：`test_admin_reset_wipes_stores_from_localhost` 直接打
`/api/admin/reset`，觸發 `JOB_REGISTRY.clear_all()` — 因為沒有 DB 隔離，
production `output/jobs.db` 整份被清空，user 上傳的 job 被連坐刪除。

解法：在 pytest 收集任何測試模組之前，先把三個 DB env var 設到 tmp 檔。
`api_server` import 時呼叫 `default_db_path()` 才會讀這幾個變數，所以一定要在
任何 `from api_server import ...` 之前完成設定 — conftest.py 的 top-level
程式碼是執行這件事的最早點。
"""
import os
import tempfile
from pathlib import Path

# 用 mkdtemp 拿一個 session 級別的 tmp 目錄；同 session 內所有測試共用，
# 行為和原本 production DB 一致（測試之間可看到彼此寫入），只是檔案落在 tmp。
_TEST_DB_DIR = Path(tempfile.mkdtemp(prefix="tc-generator-test-dbs-"))

os.environ.setdefault("TC_JOBS_DB", str(_TEST_DB_DIR / "jobs.db"))
os.environ.setdefault("TC_AGENT_SESSION_DB", str(_TEST_DB_DIR / "agent_sessions.db"))
os.environ.setdefault("TC_TRACE_DB", str(_TEST_DB_DIR / "traces.db"))
