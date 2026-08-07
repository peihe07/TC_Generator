# Repo Layout — 每個目錄是什麼、能不能動

最後更新：2026-08-07

分三種標記：
**[code]** 程式碼，路徑被設定檔綁死 · **[data]** 資料/產出 · **[rebuild]** 可重建，砍掉不心疼

---

## 頂層目錄

| 目錄 | 類型 | 內容 | 動它之前要知道 |
|---|---|---|---|
| `backend/` | code | FastAPI + CLI + 生成/審查/寫回核心 | `pyproject.toml` 的 `package-dir = {"" = "backend"}` 與 `pythonpath = ["backend"]` 綁死；模組是扁平 py-modules 清單，新增檔案要同步 `py-modules` |
| `tests/` | code | backend 測試（基線 618 collected） | `testpaths = ["tests"]` |
| `frontend/` | code | Win95 風格 legacy 桌面 UI（Next.js） | README 的啟動指令直接指這個路徑 |
| `frontend-modern/` | code | 現代 UI 變體，獨立 package / ports / Docker | 與 `frontend/` 刻意隔離，不共用 node_modules |
| `docker/` | code | dev / prod / modern 三組 compose | `.dockerignore` 在 root |
| `config/` | data | `budget.json`、`kpi_thresholds.json`、`domain_packs/` | `scorecard.py` 預設讀 `config/kpi_thresholds.json` |
| `docs/` | data | 文件；分類見 `docs/README.md` | 五份 runtime 規則文件被 `rules_loader.py` 硬編路徑，不可搬 |
| `scripts/` | code | 離線工具：`build_spec_index.py`、`translate_xlsx.py` 等 | — |
| `M1/` | data | M0–M2 里程碑的工作區：設計文件、domain pack、SWE1 需求 JSON、覆蓋率腳本 | **路徑被 code 引用**，詳見 `M1/README.md` |
| `tcgen_package/` | data | FW036 remaining TC 的一次性生成包（RUNBOOK / scripts / batches / generated / ANOMALIES） | RD-1 裁決尚未全部落地，隨時要能重跑 write-back；自帶 `.gitignore` |
| `output/` | data | CLI / job 的執行產物 | `*.xlsx`、`*.db`、`.workspaces/` 已 ignore；`dealer/` `player/` 下有刻意 commit 的樣本 |
| `spec-index/` | data + rebuild | spec 索引（約 **440 MB**）。`cache/*.xlsx`（2 MB）是 SYS1 匯出**輸入檔**、`sources/*.pdf`（93 MB）是原始 spec —— 兩者都**不是**快取；`cache/*.json`（348 MB）才是 embedding 產物 | 全部 gitignore（含客戶機敏資料）。重建 `*.json` 要跑 `scripts/build_spec_index.py`，**會產生 OpenAI embedding API 費用**，不要當一般快取刪 |
| `_to_delete/` | rebuild | 待手動刪除的暫存區（已 ignore） | 這個環境的工具不能直接刪檔，只能搬進來，由人清空 |

## 磁碟大戶（都可重建）

| 位置 | 大小 | 重建方式 |
|---|---|---|
| `frontend/node_modules` | ~680 MB | `cd frontend && npm install` |
| `frontend-modern/node_modules` | ~440 MB | `cd frontend-modern && npm install` |
| `spec-index/cache/*.json` | ~348 MB | `python scripts/build_spec_index.py` — **需付 embedding API 費用**，非零成本 |
| `.venv/` | — | `pip install -e ".[dev]"` |

## 不可搬動清單（搬了會壞）

1. `docs/runtime/ASPICE_SWE6_AI_Instruction.md`、`docs/runtime/TEST_CASE_DESIGN_METHOD.md`、
   `docs/runtime/TEST_CASE_PRIORITY.md` — `backend/rules_loader.py` 以常數路徑載入
2. `docs/runtime/ASPICE_SWE6_AI_Review.md` — review engine 引用
3. `docs/runtime/profiles/<stem>.md` — `rules_loader.py` 以 stem 組路徑
4. `M1/domain_pack_*.json`、`M1/swe1_*_reqs.json`、`M1/spec_coverage_*.json`、
   `M1/spec_coverage_analysis.py` — `backend/main.py` 的 CLI 說明與
   `docs/dev/PIPELINE_DESIGN.md` 的指令範例都指這些路徑
5. `backend/` 底下的模組檔名 — `pyproject.toml` 的 `py-modules` 逐一列名
6. root 的 `start.sh` / `start-modern.sh` / `reset-state.sh` — README 的啟動段落

## 一次性 vs 可複用

這個 repo 同時裝了「產品」與「某次專案的工地」，兩者不要混：

- **產品**：`backend/` `frontend*/` `tests/` `config/` `docs/`（runtime + dev）
- **工地**：`tcgen_package/`（FW036）、`M1/`（里程碑實驗）、`output/`、`refinement/`（2026-05 一次性腳本，已無人引用）

新專案要開新的工地目錄，不要把 FW036 的假設（column map、保護區列號、
Test Set 清單）搬進產品層 —— 這正是 `docs/plans/TCGEN_INTEGRATION_PLAN.md`
W4 要解決的事。


## 已知的假快取（看起來可刪、其實不能）

- `spec-index/cache/*.xlsx` — 名字在 cache 底下，但它是 SYS1 Polarion 匯出的**輸入檔**，
  `build_spec_index.py` 靠它產生索引。刪了要重新跟上游要檔案
- `spec-index/cache/*.json` — embedding 產物，重建要付 API 費用
- `spec-index/cache/*.pkl` — **這個才是真的可刪**：現行程式碼只讀寫 `.json`
  （`spec_matcher.save_spec_index` / `load_spec_index`），`manifest.json` 也沒登記 pkl。
  37 個檔共 161 MB 已於 2026-08-07 移入 `_to_delete/spec-index-legacy-pkl/`
