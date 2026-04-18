# TC Generator — Roadmap

版本：v1.0
日期：2026-04-18
狀態：**下一步規劃（尚未開工）**

目前已完成的內容請看 [STATUS.md](STATUS.md)。

---

## 主題：Agent 副駕模式（Agent Integration）

在現有 TC Generator 專案上，疊加「Agent 副駕」模式，與現行 GUI 雙模並存。

---

## 1. 目標與非目標

### 1.1 目標
- **不砍掉現有 GUI**。現行 Upload / Configure / Generate / Review / Export 五個 module 保留並繼續作為 ASPICE SWE.6 合規的主要交付路徑。
- **新增 Agent 副駕模式**。讓使用者可以用自然語言、跨 job、批次操作，解決現有 GUI 做不到或做得慢的需求。
- **單一事實來源**。GUI 和 Agent 共用同一組 backend tool、同一個 job store、同一份前端 state。任何一邊的動作另一邊立即看得到。
- **ASPICE 稽核保證**。Agent 每個決策寫入 trace log，可以 replay 與審閱。
- **漸進式交付**。分四個 Phase，每個 Phase 獨立可用、可停、可 rollback。

### 1.2 非目標
- 不取代 GUI。不會把 5 個 module 重寫成 chat。
- 不改 `backend/core/` 的任何生成邏輯。Agent 只是決策層。
- 不引入新的 LLM 供應商依賴。Agent 可以用現有 OpenAI function calling，或選配 Anthropic；二選一都能實作。
- 不做「自主執行」預設行為。所有寫入類 / 有成本類 tool 都要人工確認或有 budget gate。

---

## 2. 現況基線（2026-04-18 snapshot）

| 項目 | 狀態 |
|---|---|
| Backend 核心模組 | `parser / spec_matcher / grouper / prompt_builder / generator / validator / writer / job_manager / job_store` 共 9 個 |
| FastAPI endpoints | 8 個：health / parse / group / match / generate / generate-stream / regenerate-stream / export / download |
| Backend 測試 | 225 pass（pytest） |
| Frontend 架構 | Next.js desktop，active modules 為 `*Module.tsx`；`jobAdapter.ts` 為單一 adapter |
| Frontend 測試 | TypeScript typecheck 通過；workspace round-trip E2E 通過 |
| 真實基準 | 44 rows / $0.125 / cache hit 90.9% / spec match rate 100% |

**結論**：基礎穩固，可以直接疊加 Agent 層，不需要先做大規模 refactor。

---

## 3. 架構總覽

### 3.1 分層
```
┌──────────────────────────────────────────────────────────┐
│ Frontend (Next.js Desktop)                                │
│                                                            │
│   GUI Modules (現有 5 個)          ChatModule (新增)      │
│   Upload / Configure / Generate /  - 對話流               │
│   Review / Export                  - Tool call 卡片       │
│                                    - Inspector 面板       │
│              └────┬────┘                  │               │
│                   │                       │               │
│              useJobStore (Zustand) ← 共用單一 store       │
│                   │                       │               │
│         jobAdapter.ts          agentClient.ts             │
│              │                       │                    │
│         /api/parse ...        /api/agent/chat (SSE)       │
└───────────────┼───────────────────────┼──────────────────┘
                │                       │
┌───────────────▼───────────────────────▼──────────────────┐
│ Backend (FastAPI)                                          │
│                                                            │
│   routes/                     routes/agent.py              │
│   parse.py generate.py ...    └─ LLM loop + dispatcher    │
│           │                              │                 │
│           └─── backend/tools/ (新增) ────┘                 │
│                每個 tool = 純 function + JSON schema       │
│                          │                                 │
│                backend/core/ (現有，不動)                  │
│                parser / generator / validator / ...        │
│                          │                                 │
│                job_store.py (SQLite, 單一資料源)           │
│                trace_store.py (新增, agent 決策 log)       │
└────────────────────────────────────────────────────────────┘
```

### 3.2 關鍵設計原則
1. **Tool layer 是唯一的業務動作介面**。REST route 變成薄 wrapper，Agent dispatcher 也是薄 wrapper，兩者呼叫同一份 function。
2. **Job state 是單一事實來源**。Agent 跑完 tool 更新 SQLite → SSE 推前端 → `useJobStore` 接收 → 所有 open 的 GUI module 自動刷新。
3. **Trace 與 Job 分離但關聯**。`jobs.db` 保留生成結果（可重現性），新增 `traces.db` 保留 Agent 決策歷程（稽核）。
4. **Agent 不能繞過 tool**。System prompt 禁止 code execution / shell / 任意 HTTP；只能呼叫白名單 tool。

---

## 4. Backend 設計

### 4.1 Tool Layer 抽取（Phase 0）

#### 4.1.1 目標目錄結構
```
backend/
  tools/
    __init__.py
    schemas.py          # JSON schema 定義（openai / anthropic 格式）
    registry.py         # tool 註冊表 + 安全分級
    _budget.py          # budget gate helper
    inspect.py          # inspect_workbook_tool
    parse.py            # parse_workbook_tool
    group.py            # group_tests_tool
    match.py            # match_spec_tool
    generate.py         # generate_tc_tool / regenerate_tc_tool
    validate.py         # validate_tc_tool
    write.py            # write_excel_tool
    jobs.py             # list_jobs_tool / get_job_detail_tool / estimate_cost_tool
  core/                 # 現有模組改放這裡，視情況
    parser.py
    generator.py
    ...
```

> **若不想動現有 `backend/` 扁平結構**：也可以不建 `core/` 資料夾，直接把 `tools/` 建起來，裡面 import 現有的 `parser / generator / ...`。對測試影響小，建議先走這條。

#### 4.1.2 Tool function 規範
每個 tool：
```python
def parse_workbook_tool(
    path: str,
    sys1_path: str | None = None,
    spec_path: str | None = None,
) -> dict:
    """Pure function; idempotent given the same input."""
    # 1. 呼叫現有 core 模組
    # 2. 寫入 job_store
    # 3. 回傳 {"job_id": ..., "rows": N, "warnings": [...]}
```

規範：
- **純函式**：同樣輸入永遠同樣輸出（除了 timestamp / job_id）
- **不做 HTTP 解析**：不接受 `Request`、不丟 `HTTPException`；改丟 `ToolError` 自訂 exception
- **回傳 JSON-serializable dict**
- **寫入 job_store 在 tool 內部做**，route / dispatcher 都不用管
- **有 side-effect 的 tool 加 `@requires_confirmation` 裝飾器**（write / generate / export 類）

#### 4.1.3 REST route 改寫
```python
# routes/parse.py (改後)
@router.post("/api/parse")
async def parse_endpoint(file: UploadFile) -> dict:
    path = save_temp(file)
    try:
        return parse_workbook_tool(path=str(path))
    except ToolError as e:
        raise HTTPException(status_code=400, detail=str(e))
```

Route 只做：參數驗證 → tool 呼叫 → 例外翻譯成 HTTP。

### 4.2 Tool 清單（Phase 1 開始實作）

#### 4.2.1 Read-only tools（安全，agent 可自由使用）
| Tool | 用途 | args | 回傳 |
|---|---|---|---|
| `inspect_workbook` | 看檔案結構，不解析內容 | `path` | `{sheets, rows_estimate, test_group, file_size}` |
| `list_jobs` | 列歷史 job | `filter?, limit?` | `[{job_id, created_at, file_name, state, rows}]` |
| `get_job_detail` | 取某 job 的完整資料 | `job_id` | 完整 job 資料 |
| `get_job_validation` | 取 validator 結果 | `job_id` | `{pass, warnings, errors}` |
| `estimate_cost` | 估算生成成本 | `job_id, model, batch_size` | `{est_cost_usd, rows, tokens_estimate}` |
| `diff_jobs` | 比對兩個 job | `job_a, job_b` | diff 內容 |

#### 4.2.2 Write tools（要 budget gate 或確認）
| Tool | 用途 | 確認門檻 |
|---|---|---|
| `parse_workbook` | 解析 xlsx | 無（成本 0） |
| `match_spec` | 跑 spec match | 無 |
| `group_tests` | 分組 | 無 |
| `generate_tc` | 生成 | `est_cost > $0.50` 需確認 |
| `regenerate_tc` | 重生 | 同上 |
| `validate_tc` | 驗證 | 無 |
| `write_excel` | 寫 Excel | 覆寫既有檔才確認 |

#### 4.2.3 Composite tools（批次類，一定要確認）
| Tool | 用途 |
|---|---|
| `regenerate_failed` | 重跑所有 validator fail 的 row |
| `export_and_archive` | 匯出並歸檔 |
| `apply_framework` | 套用 framework.json |

#### 4.2.4 JSON Schema 範例
```python
# tools/schemas.py
PARSE_WORKBOOK_SCHEMA = {
    "name": "parse_workbook",
    "description": "Parse an ASPICE SWE.6 TC workbook (.xlsx) into structured rows. "
                   "Returns job_id for downstream tools.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Absolute path to the .xlsx"},
            "sys1_path": {"type": "string", "description": "Optional SYS1 spec for traceability"},
            "spec_path": {"type": "string", "description": "Optional supplementary doc (.pdf/.docx/.xlsx)"},
        },
        "required": ["path"],
    },
}
```

完整 schemas 在 Phase 1 實作時逐一定義。

### 4.3 Agent Endpoint（Phase 1）

#### 4.3.1 API 規格
```
POST /api/agent/chat
Content-Type: application/json
Body: {
  "session_id": "uuid",        # 首次為空，由 server 產生
  "message": "string",
  "attachments": [{"path": "..."}],  # 由前端 upload route 先產出的 tmp path
}

Response: SSE stream
  event: message         → text chunk
  event: tool_call       → {tool, args, call_id}
  event: tool_result     → {call_id, result, duration_ms}
  event: state_update    → {job_id, delta: {...}}    ← 同步到 useJobStore
  event: require_confirm → {call_id, tool, args, est_cost}
  event: done            → {session_id, total_cost}
  event: error           → {message}
```

#### 4.3.2 Session 管理
- Session 資料存在 `agent_sessions` SQLite table
- 每 session 包含：`session_id, created_at, message_history[], tool_trace[], total_cost_usd`
- Session 預設保留 7 天（env `TC_AGENT_SESSION_MAX_AGE_DAYS`）

#### 4.3.3 System Prompt 設計
核心規則：
1. 你是 TC Generator 的操作副駕，只能透過白名單 tool 完成工作。
2. 遇到 spec match rate 低 → 主動建議掛 spec 或 fuzzy threshold 調整。
3. 遇到 validator warning → 先分類（soft/hard），soft 列選項讓使用者選，hard 自動 retry。
4. 任何 `est_cost > $0.50` 的動作必須先出 require_confirm event。
5. 絕不編造 job_id 或 row 內容；不確定就先 `list_jobs` 或 `get_job_detail`。
6. 回答用繁體中文，技術關鍵字保留英文。

#### 4.3.4 Dispatcher 骨架
```python
async def run_agent_loop(session_id, user_message, stream):
    history = load_session(session_id)
    history.append({"role": "user", "content": user_message})

    while True:
        response = await llm.chat(
            messages=history,
            tools=ALL_TOOL_SCHEMAS,
            tool_choice="auto",
        )

        if response.text:
            await stream.send("message", response.text)

        if not response.tool_calls:
            break

        for call in response.tool_calls:
            if needs_confirmation(call):
                await stream.send("require_confirm", call)
                if not await wait_for_confirm(call.id):
                    history.append({"role": "tool", "content": "user_declined"})
                    continue

            await stream.send("tool_call", call)
            result = await dispatch(call.tool, call.args)
            write_trace(session_id, call, result)
            await stream.send("tool_result", {"call_id": call.id, "result": result})

            # 狀態同步推前端
            if affects_job_state(call.tool):
                state = load_job_state(result.get("job_id"))
                await stream.send("state_update", state)

            history.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})

        save_session(session_id, history)

    await stream.send("done", {"total_cost": cost_so_far})
```

### 4.4 Trace 與稽核

#### 4.4.1 Trace store
新增 `backend/trace_store.py`：
```python
class SqliteTraceStore:
    def record(self, session_id, event_type, payload)
    def replay(self, session_id) -> list[TraceEvent]
    def export(self, session_id, format="jsonl") -> bytes
```

每筆 trace event：
```json
{
  "ts": "2026-04-18T14:05:23.117Z",
  "session_id": "...",
  "type": "tool_call",
  "tool": "generate_tc",
  "args": {...},
  "result_hash": "sha256:...",
  "duration_ms": 12403,
  "llm_reasoning": "..."
}
```

#### 4.4.2 Replay 機制
```python
# CLI: python -m backend.tools.replay SESSION_ID --to output/replay.xlsx
# 照 trace 順序重跑所有 tool，驗證結果一致（result_hash 比對）
```

這支 CLI 會成為 ASPICE 稽核員的關鍵工具。

---

## 5. Frontend 設計

### 5.1 ChatModule

#### 5.1.1 元件樹
```
ChatModule.tsx
├── ChatHeader                 # 視窗標題列 + session 切換
├── ChatScroll
│   └── MessageList
│       ├── UserMessage
│       ├── AgentMessage
│       │   ├── TextBlock
│       │   ├── ToolCallCard   # tool 執行狀態卡
│       │   └── ChoiceButtons  # agent 給的選項按鈕
│       └── ConfirmCard        # require_confirm 的互動卡
├── InspectorPanel             # 右側面板
│   ├── CurrentJobBox
│   ├── CostMeter
│   ├── ToolTraceList
│   └── RecentSessionsList
└── InputArea
    ├── FileDropzone
    ├── PromptTextarea
    └── SendButton
```

#### 5.1.2 實作要點
- **視窗化**：`ChatModule` 註冊為一種 `WindowType`，走現有 `useWindowStore` 的 open / close / focus / drag / resize
- **預設開啟尺寸**：960 x 640，最小 640 x 480
- **記憶位置**：關閉時存最後位置，下次開啟還原
- **快捷鍵**：`Cmd+K` / `Ctrl+K` 開啟並 focus 到輸入框
- **多 session**：File menu → New Session / Switch Session

### 5.2 Taskbar 整合

在 `frontend/src/components/system/Taskbar.tsx` 的右側新增 `AgentTaskbarButton.tsx`：
- 圖示：Remix Icon `ri-robot-2-line`
- 狀態：
  - idle：灰底
  - running：藍底閃爍（agent 正在跑 tool）
  - need_confirm：黃底脈動（等使用者確認）
  - error：紅底
- 點擊：open / focus ChatModule；若有 pending confirm 則直接捲到該 message

### 5.3 State 同步契約

#### 5.3.1 單向原則
```
Agent tool 完成
  ↓ backend 寫 job_store
  ↓ SSE state_update event
  ↓ agentClient.ts 收到
  ↓ useJobStore.applyDelta(payload)
  ↓ 所有訂閱的 module 自動 re-render
```

#### 5.3.2 衝突處理
- **Agent 跑期間使用者動 GUI**：允許。GUI 寫 state 會觸發 optimistic update；若 agent 也剛好寫，以 server 回來的 version 為準。
- **同一個 job 兩邊同時編輯**：使用 job 的 `revision` 欄位做 optimistic concurrency check，有衝突時 ChatModule 顯示 toast「使用者已修改此 job，agent 將讀取最新版本」。

#### 5.3.3 jobAdapter.ts 新增方法
```typescript
// 既有
jobAdapter.parse(file)
jobAdapter.generate(jobId, config)
// 新增
jobAdapter.applyAgentDelta(payload: StateUpdateEvent)
jobAdapter.getJobRevision(jobId: string): number
```

### 5.4 Handoff UI

#### 5.4.1 Agent → GUI（常見）
`ToolCallCard` 在完成態且 tool 屬於「有對應 GUI module」的類別時，顯示跳轉按鈕：

| Tool | 對應 GUI 按鈕 |
|---|---|
| `parse_workbook` | `Open in Upload` |
| `group_tests` / `match_spec` | `Open in Configure` |
| `generate_tc` / `regenerate_tc` | `Open in Review` |
| `validate_tc` | `Open in Review` |
| `write_excel` | `Open in Export` |

按鈕實作：
```typescript
onClick={() => {
  useWindowStore.getState().openWindow('review', { jobId });
  // 可選：把焦點帶到該 row
  useJobStore.getState().focusRow(jobId, rowId);
}}
```

#### 5.4.2 GUI → Agent
在每個 GUI Module 的右上角工具列加一個「求助 AI」按鈕（Remix Icon `ri-question-answer-line`）：
- 點擊時開啟 ChatModule
- 預填 context prompt，例如：
  ```
  [context: 目前在 Review Module，job=job_20260418_140310]
  [context: 有 2 筆 validator warning: row 17, row 23]
  （使用者的問題）
  ```
- 使用者補充自然語言後送出

### 5.5 樣式遵循
- 維持現有 `win95.css` 風格（sharp corners、raised borders、pixelated font）
- Tool card 用新增的 `.tool-card` class（已在 mockup 定義，搬進 `win95.css`）
- 不使用 emoji；所有 icon 一律用 `@remixicon/react`

---

## 6. 分階段實作計畫

### Phase 0 — Tool Layer 抽取（2–3 天）

**目標**：把現有 FastAPI route 裡的業務邏輯抽出到 `backend/tools/`，route 變薄。

| 任務 | 驗收 |
|---|---|
| 建 `backend/tools/` 資料夾與 `registry.py` 骨架 | import 成功、pytest 仍 225 pass |
| 抽 `parse_workbook_tool` | `test_api_server::test_parse` 仍 pass；新增 `test_tool_parse` |
| 抽 `match_spec_tool` / `group_tests_tool` | 同上 |
| 抽 `generate_tc_tool` / `regenerate_tc_tool` | 同上，含 SSE stream 行為維持 |
| 抽 `validate_tc_tool` / `write_excel_tool` | 同上 |
| 新增 `ToolError` 例外與 HTTP 對應表 | 現有 API 回應 status code 不變 |

**不做的事**：不改 API shape、不改前端。這個 Phase 結束時 GUI 使用者完全無感。

### Phase 1 — Agent Endpoint（3–4 天）

| 任務 | 驗收 |
|---|---|
| `tools/schemas.py` 完整 schema（全部 tools） | JSON schema validate 通過 |
| `routes/agent.py` SSE endpoint | 對話能跑、tool_call 事件正確 |
| `dispatcher.py` 實作 | 能呼叫所有 tool，錯誤處理完整 |
| Session store（`agent_sessions` table） | 重啟後能 resume |
| `trace_store.py` + replay CLI | 能完整 replay 一個 session |
| System prompt 第一版 | CLI 整合測試：5 個 golden scenario 能跑完 |
| `test_agent_dispatcher.py`（新增） | 覆蓋每個 tool 的 agent 呼叫路徑 |

**Golden scenarios**（整合測試素材）：
1. 「parse 這份檔」→ parse_workbook → 回報結構
2. 「跑完整個 pipeline」→ parse → group → generate → validate → 回報
3. 「上週那個 job 補 REQ-045」→ list_jobs → regenerate_tc
4. 「跨 job 查 match rate」→ list_jobs → 迴圈 get_job_validation
5. 「estimate 這個檔多少錢」→ inspect_workbook → estimate_cost

### Phase 2 — Frontend ChatModule（4–5 天）

| 任務 | 驗收 |
|---|---|
| `ChatModule.tsx` + 子元件 | 能顯示對話、能發送訊息 |
| `agentClient.ts` SSE wrapper | 所有 event type 能解析、斷線重連 |
| `InspectorPanel` 接 useJobStore | 實時反映 job 狀態 |
| Taskbar 整合 `AgentTaskbarButton` | 4 個狀態顏色正確 |
| 多 session UI | 能切換、能清除 |
| `ChatModule.spec.ts` 單元測試 | 覆蓋訊息渲染、tool card 展開 |
| workspace round-trip E2E 擴充 | 涵蓋 Agent tool 結果也能存入 workspace |

### Phase 3 — Handoff & 合規（2–3 天）

| 任務 | 驗收 |
|---|---|
| Tool card 的 `Open in *` 跳轉按鈕 | 5 種 tool 對應 5 個 module 都能跳 |
| GUI Module 的「求助 AI」按鈕 | context prompt 正確預填 |
| Trace export UI（File → Export Trace） | 能產 `.jsonl` 稽核檔 |
| Budget gate UX | `require_confirm` 卡片能正確 Accept/Decline |
| 衝突處理 toast | 雙邊同時改時有明確提示 |
| E2E：混用劇本 | Playwright 腳本 run 劇本 B（GUI + Agent 混用）|

### Phase 4 — 進階 & 觀察（選配，1–2 週）

- Cross-job 分析 tool 擴充（`diff_jobs`、`aggregate_metrics`）
- 排程執行（與 `scheduled-tasks` MCP 整合）
- Cost 觀測面板（過去 30 天花費 / cache hit 趨勢）
- A/B：比較 GUI-only 使用者 vs 混用使用者的平均完成時間

---

## 7. 測試策略

### 7.1 Backend
| 層級 | 測試 |
|---|---|
| Tool unit | 每個 tool 一個 `test_tool_*.py`，covering golden input、error cases |
| Dispatcher | `test_agent_dispatcher.py`：mock LLM，assert tool 呼叫順序、confirm 機制 |
| REST compat | 現有 `test_api_server.py` 全數保留，確保 Phase 0 refactor 無行為變化 |
| Trace replay | `test_trace_replay.py`：產生 trace → replay → result_hash 一致 |

目標：整體 pytest ≥ 250 cases（現行 225 + 新增 ≥ 25）。

### 7.2 Frontend
| 層級 | 測試 |
|---|---|
| Component | Vitest + Testing Library：`ChatModule`、`ToolCallCard`、`InspectorPanel` |
| Integration | mock SSE stream，驗證 state 同步 |
| E2E | Playwright 新增 `agent.spec.ts`、`handoff.spec.ts` |

### 7.3 手動驗收劇本
- 劇本 A：純 GUI 跑完一份 DeviceManager（現行基線） → 結果與 Agent 版完全一致
- 劇本 B：GUI 到 Review 卡關 → 切 Agent → 改完切回 Review → Export
- 劇本 C：純 Agent 批次補生成 → Review → Export

---

## 8. ASPICE 合規保證

### 8.1 可重現性
- Tool 為純函式：同 input → 同 output（除 timestamp / id）
- LLM 呼叫在 tool 內部也鎖定 `temperature=0`、固定 seed（模型支援的話）
- Trace 可 replay：`python -m backend.tools.replay SESSION_ID` 能完整重跑

### 8.2 可追溯性
- 每個 job 保留：parse 原始檔 hash、tool 呼叫序列、LLM 回應 raw、validator 結果
- 每個 agent session 保留：對話完整歷史、tool_call + result pairs、使用者 confirm 記錄

### 8.3 可審閱性
- Trace export：一鍵匯出 `.jsonl` + `.md` 摘要
- Job export：Excel 匯出檔裡內嵌 trace_id（metadata sheet）
- 稽核員只要給一個 job_id，可以 100% 還原出「當時是誰、用什麼 prompt、跑了哪些 tool、吃了多少 token」

### 8.4 防誤動
- 白名單 tool only（agent 不能執行任意 code）
- 有成本動作全部 budget gate（預設 $0.50 門檻）
- 覆寫現有 Excel 檔要確認
- 刪除類動作禁用（只支援歸檔、不支援 delete）

---

## 9. 風險與緩解

| 風險 | 影響 | 緩解 |
|---|---|---|
| Agent 理解錯意圖、跑錯 tool | 中。成本浪費 + 使用者挫折 | System prompt 要求模糊時先 `list_jobs` 確認；budget gate；replay CLI 可審閱 |
| LLM reasoning token 成本失控 | 中。長對話累積 | session 強制 summarize（每 10 輪壓縮一次 history）；context window guard |
| GUI 與 Agent 同時改 job 衝突 | 低–中 | `revision` 欄位 + toast 提示；衝突時保守讓 GUI 贏 |
| Agent 成為主入口、GUI 被冷落 | 低 | 刻意不做「自動生成完成就匯出」類的 shortcut，需要 GUI 人工 Review |
| ASPICE 稽核員不接受 Agent 結果 | 中。合規風險 | Phase 4 前不把 Agent 放在主要交付路徑；稽核員教育訓練 + replay demo |
| Refactor 破壞 225 tests | 高。blocker | Phase 0 每抽一個 tool 立刻跑全套 pytest；不合併 PR 除非全綠 |

---

## 10. 成功指標

### 10.1 技術指標
| 指標 | 目標 |
|---|---|
| pytest pass | 維持 100%（≥ 250 cases） |
| TypeScript typecheck | 0 error |
| Agent endpoint p95 latency | < 200ms（不含 tool 執行時間） |
| Trace replay 成功率 | 100% |
| Refactor 後 REST API 行為 | 100% 相容 |

### 10.2 產品指標（Phase 4 觀察）
| 指標 | 目標 |
|---|---|
| 混用劇本（B+C）佔比 | 2 個月內 ≥ 20% |
| 跨 job 查詢類操作月頻次 | 從 0 提升到 ≥ 10 |
| 增量補生成平均完成時間 | 從「純 GUI ~5 min」降到「Agent ~45 sec」 |
| 平均單 session agent 成本 | ≤ $0.05 |
| 使用者回報的 Agent 「誤動作」次數 | < 3 次/月 |

---

## 11. 檔案異動清單

### 11.1 新增
```
backend/
  tools/__init__.py
  tools/schemas.py
  tools/registry.py
  tools/_budget.py
  tools/inspect.py
  tools/parse.py
  tools/group.py
  tools/match.py
  tools/generate.py
  tools/validate.py
  tools/write.py
  tools/jobs.py
  tools/replay.py                    # CLI
  routes/__init__.py
  routes/agent.py
  agent_dispatcher.py
  trace_store.py

tests/
  test_tool_parse.py
  test_tool_generate.py
  test_tool_validate.py
  ... (每個 tool 一個)
  test_agent_dispatcher.py
  test_trace_store.py
  test_trace_replay.py

frontend/src/
  components/modules/ChatModule.tsx
  components/modules/chat/MessageList.tsx
  components/modules/chat/ToolCallCard.tsx
  components/modules/chat/ConfirmCard.tsx
  components/modules/chat/InspectorPanel.tsx
  components/modules/chat/ChoiceButtons.tsx
  components/system/AgentTaskbarButton.tsx
  components/system/HelpFromAgentButton.tsx
  services/agentClient.ts
  store/useAgentStore.ts               # agent session state

frontend/e2e/
  agent.spec.ts
  handoff.spec.ts

docs/
  ROADMAP.md                            # 本文件
  AGENT_TOOL_SCHEMAS.md                 # Phase 1 完成後產出
```

### 11.2 改動
```
backend/
  api_server.py                         # route 改成薄 wrapper（或拆進 routes/*.py）

frontend/src/
  store/useWindowStore.ts               # 註冊 chat window type
  store/useJobStore.ts                  # 新增 applyAgentDelta / revision 欄位
  services/jobAdapter.ts                # 新增 agent delta apply 方法
  styles/win95.css                      # 新增 .tool-card 系列樣式
  components/system/Taskbar.tsx         # 加上 AgentTaskbarButton
  components/modules/ReviewModule.tsx   # 加「求助 AI」按鈕（所有現有 module 同理）
  components/modules/UploadModule.tsx
  components/modules/ConfigureModule.tsx
  components/modules/GenerateModule.tsx
  components/modules/ExportModule.tsx
```

### 11.3 完全不動
```
backend/parser.py
backend/spec_matcher.py
backend/spec_parser.py
backend/grouper.py
backend/prompt_builder.py
backend/generator.py
backend/validator.py
backend/writer.py
backend/id_generator.py
backend/job_manager.py
backend/job_store.py
backend/main.py                         # CLI 入口維持

frontend/src/components/modules/*Module.tsx  # 5 個 GUI module 的核心邏輯不動
frontend/app/api/*                       # 既有 proxy route 不動
```

---

## 12. 時程總覽

| Phase | 工作 | 人天 | 併行可能 |
|---|---|---|---|
| 0 | Tool layer 抽取 | 2–3 | 不可（blocker） |
| 1 | Agent endpoint + dispatcher + trace | 3–4 | 部分（Phase 2 可同時啟動） |
| 2 | Frontend ChatModule | 4–5 | 可與 Phase 1 部分重疊 |
| 3 | Handoff + 合規 UX | 2–3 | 不可（blocker）|
| 4 | 進階 + 觀察 | 5–10（選配） | 全部 |

**關鍵路徑總計約 12–16 工作天（2.5–3 週）**，不含 Phase 4。

---

## 13. 下一步決策點

在開始 Phase 0 前，需要先確認以下三件事：

1. **LLM 供應商**：沿用 OpenAI function calling，還是引入 Anthropic？
   - 建議：Phase 1 先用 OpenAI（專案已經在用），Phase 4 再評估 Anthropic 的長 context 優勢。
2. **資料夾重構**：是否要建 `backend/core/` 子目錄？
   - 建議：不要。現行扁平結構 + 新增 `backend/tools/` 衝擊最小。
3. **Trace 寫入粒度**：每個 event 都寫，還是只寫 tool call？
   - 建議：tool call + LLM response 都寫。LLM chunk 不寫（太雜）。

確認後，Phase 0 第一天就可以開工。
