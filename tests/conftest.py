"""Pytest fixtures：把 SQLite job store 指到 tmp 路徑，避免 test 跑下去污染
或清空 production `output/` 下的真實 DB。

之前發生過：`test_admin_reset_wipes_stores_from_localhost` 直接打
`/api/admin/reset`，觸發 `JOB_REGISTRY.clear_all()` — 因為沒有 DB 隔離，
production `output/jobs.db` 整份被清空，user 上傳的 job 被連坐刪除。

解法：在 pytest 收集任何測試模組之前，先把 DB env var 設到 tmp 檔。
`api_server` import 時呼叫 `default_db_path()` 才會讀這個變數，所以一定要在
任何 `from api_server import ...` 之前完成設定 — conftest.py 的 top-level
程式碼是執行這件事的最早點。
"""
import os
import tempfile
from pathlib import Path

_TEST_DB_DIR = Path(tempfile.mkdtemp(prefix="tc-generator-test-dbs-"))

os.environ.setdefault("TC_JOBS_DB", str(_TEST_DB_DIR / "jobs.db"))
