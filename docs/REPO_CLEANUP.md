# Repo Cleanup Guide

最後更新：2026-04-19

這份文件把目前 repo 內容分成三類：

- `保留且已歸類`：屬於正式專案內容，應留在目前位置
- `保留但不該 commit`：本機執行/快取/測試產物
- `可刪除候選`：目前看起來沒有正式用途，刪掉不影響系統執行

## 1. 保留且已歸類

### 核心程式碼

- `backend/`：FastAPI、tool layer、agent、parser、generator、writer
- `frontend/app/`：Next.js app shell 與 proxy routes
- `frontend/src/`：UI components、stores、services、tests
- `tests/`：backend pytest
- `frontend/e2e/`：Playwright E2E
- `frontend/public/icons/desktop/`：桌面 icon，`Desktop.tsx` 直接使用

### 專案文件

- `docs/`：正式文件主目錄
- `docs/design-system/`：設計系統 handoff / migration / preview / UI kit 圖
- `docs/mockups/`：早期 GUI flow 與 chat mockup
- `docs/API_CONTRACT.md`
- `docs/RULES.md`
- `docs/STATUS.md`
- `docs/ROADMAP.md`

### 執行時目錄

- `output/`：runtime 匯出與 SQLite job/trace/session 資料
- `framework/`：保留作為 framework mapping 輸入目錄
- `spec-index/`：保留作為 spec index / reference 輸入目錄

## 2. 保留但不該 commit

這些通常應該存在本機，但不應進版本控制：

- `.env`
- `frontend/.env.local`
- `.venv/`
- `frontend/.next/`
- `frontend/test-results/`
- `.pytest_cache/`
- `.playwright-mcp/`
- `output/*.db`
- `output/*.xlsx`
- `*.tsbuildinfo`
- `__pycache__/`
- `.coverage`
- `docs/temp/`

## 3. 可刪除候選

以下檔案/目錄目前看起來沒有正式用途，且不影響系統執行：

- `do_commits.sh`
  - 一次性手動 commit 腳本
  - 內容已過時，還引用不存在的 `docs/TC Generator Design System/`
- `frontend/tests/__init__.py`
  - `frontend/tests/` 目前沒有實際 Python 測試內容
- 所有 `.DS_Store`
  - 例如：`./.DS_Store`、`docs/.DS_Store`、`frontend/.DS_Store`
- 所有 `__pycache__/` 與 `.pyc`
  - 例如：`backend/__pycache__/`、`tests/__pycache__/`
- 所有本機測試暫存
  - `frontend/test-results/.last-run.json`
  - `.playwright-mcp/*`

## 4. 目前建議的目錄角色

### App code

- `backend/`
- `frontend/app/`
- `frontend/src/`
- `frontend/public/`

### Project docs

- `docs/`
- `docs/design-system/`
- `docs/mockups/`

### Local runtime data

- `output/`
- `framework/`
- `spec-index/`
- `docs/temp/`

### Tests

- `tests/`
- `frontend/e2e/`
- `frontend/src/__tests__/`

## 5. 建議的下一步

如果要繼續實際清理 repo，建議順序如下：

1. 刪掉 `do_commits.sh`
2. 刪掉所有 `.DS_Store`、`__pycache__/`、`.pytest_cache/`、`.playwright-mcp/`
3. 刪掉 `frontend/tests/__init__.py`
4. 保留 `frontend/public/icons/desktop/` 並納入版本控制
5. 不要再把 mockup / design assets 放回 `output/`，統一放 `docs/`
