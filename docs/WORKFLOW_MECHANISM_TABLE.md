# TC Generator — 使用機制總表

更新：2026-04-27。這份是開發 / 維護用，不是給終端使用者看的文案。

## 主流程總表

| 階段 | 使用者做什麼 | 前端指令 / function | Browser API | Backend API | Backend 做什麼 | AI 連接 | 結果 / 狀態 |
|---|---|---|---|---|---|---|---|
| Upload: 載入 spec library | 打開 Upload | `fetchSpecLibrary()` | `GET /api/spec-library` | `GET /api/spec-library` | 讀 `spec-index/manifest.json` | 無 | dropdown 顯示可選 spec index |
| Upload: Parse | 上傳 raw Excel，可選 reference/spec | `parseJobFiles()` | `POST /api/parse` | `POST /api/parse` | `parse_workbook_tool` 解析 workbook，建立 `jobId`，保存 raw bytes | 無 | `jobMetadata`、rows、preview rows 進 store |
| Configure: Fill Blank | 按 `Fill Blank` | `fetchGroupingPreview(forceRegroup=false)` | `POST /api/group` | `POST /api/group` | `group_tests_tool` 只補空白 Test Set | 需要時呼叫 `classify_test_sets`；model 固定 `gpt-5-mini` | 回 preview assignments；不直接改 rows |
| Configure: Regroup All | 按 `Regroup All` | `fetchGroupingPreview(forceRegroup=true)` | `POST /api/group` | `POST /api/group` | 全部 row 重新分類；既有 Test Set 當 hint | `classify_test_sets`；model 固定 `gpt-5-mini` | 回 preview；AI 漏 row 時 fallback 到 PDMxx / `Unclassified` |
| Configure: Apply grouping | 按 `Apply` | `applyGroupingPreview()` | 無 | 無 | 無 backend 寫入 | 無 | preview 寫回 frontend rows |
| Configure: Match spec | 按 spec matching / 進 tab | `fetchMatchPreview()` | `POST /api/match` | `POST /api/match` | `match_spec_tool` 做 PDM exact / fuzzy / semantic matching | semantic match 可能用 embeddings；若 cached index 已有 embeddings 則不重算 | 回 match preview，可手動覆寫 |
| Configure: Start Generate | 按 `Start Generate` | `handleStartGenerate()` | 無 | 無 | 若有 grouping preview，先 auto-apply | 無 | 開 Generate 視窗；避免忘記 Apply |
| Generate: Queue | 按 `Generate` | `startGeneration()` 第一步 | `POST /api/generate` | `POST /api/generate` | job 設為 queued，保存 rows/config | 無 | 回 `streamUrl` |
| Generate: Stream | Generate 自動連線 | `EventSource(streamUrl)` | `GET /api/generate/stream?jobId=...` | `GET /api/generate/stream?jobId=...` | 逐 row 執行 decompose/generate/validate；每 batch persist usage | `decompose_requirement` + `generate_tcs_for_row`；model 用使用者選的 `gpt-5` / `gpt-5.4` | SSE: `job.started`、`req.split`、`row.completed`、`row.added`、`job.completed` |
| Generate: Stop | 按 `Stop` | runner `.stop()` | 關閉 EventSource | backend 可能仍跑完當前 sync call | 前端停止接收 | AI 呼叫已送出時不能保證取消 | UI 停止更新；已成功 batch 的 usage 已 persist |
| Generate: Resume | SSE disconnect 後按 `Resume` | `startGeneration(pendingRows)` | 同 Generate | 同 Generate | 只送未完成 rows | 同 Generate | 接續產生 pending rows |
| Review: Select rows | 勾選 / 篩選 row | local store actions | 無 | 無 | 無 | 無 | selectedIds / filter 更新 |
| Review: Accept / Reject | 按 `Accept` / `Reject` | `updateRowStatus()` | 無 | 無 | 無 | 無 | row 狀態改成 accepted / rejected |
| Review: Edit | 展開 row 後改欄位、Save | `updateRow()` | 無 | 無 | 無 | 無 | row 欄位直接更新 |
| Review: AI fix suggestion | 在 ValidationPanel 按詢問 AI | `requestReviewFixSuggestion()` | `POST /api/review/suggest-fix` | `POST /api/review/suggest-fix` | `suggest_review_fix` 產結構化修正建議 | OpenAI chat；預設 `gpt-5` | 回 root cause / fields / proposed change / suggested reason |
| Review: Apply suggested reason | 按 `套用為 Regenerate Reason` | set local `regenerateReason` | 無 | 無 | 無 | 無 | 只填入 reason 草稿，不自動送 AI |
| Review: Regenerate | 按 `Regenerate`，dialog 填 reason 後確認 | `regenerateRows()` | `POST /api/jobs/[jobId]/regenerate/stream` | `POST /api/jobs/{job_id}/regenerate/stream` | 依 reason 重生 selected rows；primary 走 diff preview | `generate_tcs_for_row`；model 用目前 config | SSE: `regen.started`、`row.regenerated`、`row.added`、`row.regen_failed` |
| Review: Apply regen diff | 在 diff 卡按 `Apply Selected` | `applyRegenerated()` | 無 | 無 | 無 | 無 | 選定欄位從 `awaitingApply` 寫回 row |
| Review: Discard regen diff | 按 discard | `clearAwaitingApply()` | 無 | 無 | 無 | 無 | 清掉 diff preview |
| Review: Re-run | 按 `Re-run` | `rerunRows()` | `POST /api/jobs/[jobId]/rerun/stream` | `POST /api/jobs/{job_id}/rerun/stream` | 重走完整 decompose + generate pipeline | `decompose_requirement` + `generate_tcs_for_row`；model 用目前 config | primary 直接覆蓋；sub-TC 以 `row.added` 插入；完成顯示 summary dialog |
| Export: Source check | 按 Export 前自動檢查 | `fetchSourceStatus()` | `GET /api/jobs/[jobId]/source-status` | `GET /api/jobs/{job_id}/source-status` | 確認 job 是否還有 raw workbook bytes | 無 | 若缺原檔，前端可要求補上傳 |
| Export: Attach raw | 選擇原始 Excel 補回 job | `attachRawWorkbook()` | `POST /api/jobs/[jobId]/attach-raw` | `POST /api/jobs/{job_id}/attach-raw` | 保存 raw bytes / rawFileName | 無 | 後續 export 可沿用原 Excel |
| Export: Export to Excel | 選 scope / columns 後按 Export | `exportJob()` | `POST /api/export` | `POST /api/export` | 篩 rows、補 Test Set、TC ID resequence、`write_excel_tool` 寫檔 | 若 row 缺 Test Set，呼叫 `classify_test_sets`；model `gpt-5-mini` | 回 `downloadUrl`、fileName、exportedRows、classifyUsage |
| Export: Download | 按 download link | browser navigation | `GET /api/export/download/[jobId]` | `GET /api/export/download/{jobId}` | 回傳 xlsx file stream | 無 | 下載產出的 workbook |
| Quick Generate: Generate | 填 requirement 後按 Generate | `QuickGenerateModule` stream fetch | `POST /api/quick-generate/stream` | `POST /api/quick-generate/stream` | 建 synthetic row，auto-split，再串流 TC | `generate_tcs_for_row`；model 用 Quick Generate 選擇 | SSE: `job.started`、`decompose.analysis`、`tc.generating`、`tc.completed`、`job.completed` |
| Quick Generate: Stop | 按 Stop | `AbortController.abort()` | 中止 `/api/quick-generate/stream` | request disconnect check | backend 偵測 disconnect 後不再送 success events | 已送出的 OpenAI sync call 不保證取消 | 前端停止，結果丟棄 |
| CostMeter: per-job usage | 打開成本面板 / 顯示細項 | job usage fetch | `GET /api/jobs/[jobId]/usage` | `GET /api/jobs/{job_id}/usage` | 讀 job usage breakdown | 無 | 顯示 per-kind / per-model 成本 |
| Cost dashboard | 打開 dashboard | metrics fetch | `GET /api/metrics/aggregate?job_ids=...` | `GET /api/metrics/aggregate?job_ids=...` | `aggregate_metrics_tool` 聚合 jobs | 無 | 顯示總成本、平均 rows、match rate |
| Workspace: Save / Load | 存取 workspace snapshot | localStorage store | 無 | 無 | 無 | 無 | 保存 frontend snapshot；不等於 backend job DB 備份 |
| Workspace: Export / Import JSON | 匯出 / 匯入 `.tcw.json` | local file APIs | 無 | 無 | 無 | 無 | 匯入後若 backend 缺 raw bytes，export 需 attach raw |
| Dev health check | 開發者檢查 backend | curl / smoke check | N/A | `GET /api/health` | 回 backend status / OpenAI key configured flag | 無 | 確認 backend 活著 |
| Admin reset | Workspace menu 確認 reset | reset action | `DELETE /api/admin/reset` | `DELETE /api/admin/reset` | 清空 SQLite job registry，vacuum | 無 | destructive；localhost only |
| Audit: Upload + Run | 在 AuditModule 上傳 workbook 後按「開始審核」 | `runAudit()` | `POST /api/audit` | `POST /api/audit` | `review_engine.review_workbook` 跑 Tier 1/2/3，套用 mutual exclusion / suppression / severity ceiling | `dry_run=false` 時走 `_run_llm_pipeline`（§6.1/§6.3/§7.1/§7.2/§7.3/§8.2.4/§8.4.2/§8.5.3）；預設 `dry_run=true` 不呼叫 AI | 回 §9 schema 的 findings JSON；前端顯示 batch summary + Per Req / Per TC tabs；可下載 `findings.json` |
| Audit: Filter / Download | 切 tab、調最低嚴重度、下載 JSON | local component state | 無 | 無 | 無 | 無 | 純前端篩選 / 序列化下載 |

## AI 連接總表

| AI 功能 | 何時觸發 | Backend function | Model | 輸入 | 輸出 | 成本記錄 |
|---|---|---|---|---|---|---|
| Test Set 分類 | Configure grouping、Export 補缺 Test Set | `classify_test_sets` | 固定 `gpt-5-mini` | row id / reqId / test item / existing Test Set hints | row id → test set assignment | 累加到 job usage；frontend history 記 classify / export delta |
| Requirement 拆分判斷 | Generate / Re-run | `decompose_requirement` / generation path | 使用者選的 `gpt-5` 或 `gpt-5.4` | requirement、sibling rows、rules、context | split reasoning、keywords、scenario count | 累加到 generate / rerun usage |
| TC 正文生成 | Generate / Regenerate / Re-run / Quick Generate | `generate_tcs_for_row` | 使用者選的 model | row context、rules、spec reference、review reason（regen only） | TC 欄位：title/pre-cond/input/proc/ER/method/priority 等 | 累加到對應 job / quick history |
| Review 修正建議 | ValidationPanel 有 error 時使用者按詢問 AI | `suggest_review_fix` | 預設 `gpt-5` | 單筆 TC + validation errors + rules | root cause、affected fields、proposed change、suggested reason | 可記為 `suggest-fix` 類型 |
| ASPICE SWE.6 Audit (LLM rules) | AuditModule `dry_run=false` | `review_engine._run_llm_pipeline` → `review_prompt_builder` | 預設 `gpt-5`，可由 form `model` 覆寫 | 批次 TC（每批 5 筆）+ 該批要評估的 rule 集合 + Req spec 索引 | per_req_findings + per_tc_findings（§9 schema） | audit endpoint 同步呼叫，目前不持久化到 job DB |
| Semantic spec match | Configure match，且需要 semantic matching | `spec_matcher` embeddings | embedding model 依 spec index / matcher 設定 | spec text / requirement text | cosine match score | 不走 chat cost history；cached spec index 優先 |

## 寫入點

| 寫入目標 | 由誰觸發 | 寫入內容 | 位置 |
|---|---|---|---|
| Frontend rows | 使用者 Apply / Generate events / Review actions | testSet、generated fields、status、split rows、awaitingApply | Zustand `useJobStore` |
| Job DB | Parse / Generate / Regenerate / Re-run / Export | parsed rows、raw bytes、config、usage、exportPath | SQLite `output/jobs.db` via `job_store.py` |
| Job History | Generate / Regenerate / Re-run / Quick / Export classify | 每次操作的 delta cost / tokens / model / row count | frontend localStorage `useJobHistoryStore` |
| Workbook file | Export | 依 scope 寫回 TC rows、framework sheet、resequenced TC IDs | backend output path，下載走 `/api/export/download/{jobId}` |
| Workspace snapshot | 使用者 Save / Export JSON | frontend state snapshot | browser localStorage 或 `.tcw.json` |

## 重要邊界

- Browser code 一律呼叫 `/api/*` same-origin Next.js route；不要直接打 Python backend。
- Generate / Regenerate / Export 需要 active backend job；沒有 job 不走 local mock。
- Grouping preview 不直接改 rows；只有 Apply 或 Start Generate auto-apply 才寫回。
- Regenerate 不直接覆蓋 row；先放 `awaitingApply`，使用者選欄位後才套用。
- Re-run 會直接覆蓋 primary row，並可插入 sub-TC rows。
- Export 是唯一寫 workbook 的步驟。
- Agent routes / ChatModule / trace/session store 已移除；不要新增依賴。
