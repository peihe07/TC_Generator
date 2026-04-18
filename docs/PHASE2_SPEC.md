# Phase 2 — Frontend ChatModule 實作規格

**版本**：v1
**日期**：2026-04-18
**狀態**：待實作
**上游文件**：[ROADMAP.md](ROADMAP.md) section 5（ChatModule 元件樹與風格規範）

本文件補齊 ROADMAP Phase 2 未鎖死的技術細節，讓實作者（人或 AI agent）不用猜。

---

## 0. Backend 實際契約（從 `backend/routes/agent.py` + `agent_dispatcher.py` 摘出）

### 0.1 Turn-based model（關鍵認知）

**每次 `POST /api/agent/chat` = 一個 turn**。一個 turn 會跑完一串 LLM ↔ tool 迴圈，直到以下之一：

- LLM 不再 call tool → emit `done` → 連線結束
- LLM call 了需確認的 tool → emit `require_confirm` → 連線提早結束（不是中斷，是正常結束）
- 發生例外 → emit `error` → 連線結束
- `max_steps=8` 用完 → emit `error: max_steps_exceeded`

**沒有「對話中」的持續連線**。不是 WebSocket。

### 0.2 Confirm flow（關鍵認知）

**Confirm 不是新 endpoint**。使用者點 Accept 後，前端**用同一個 `POST /api/agent/chat`** 重送：

```jsonc
// 第一次 POST：觸發 require_confirm
{ "session_id": null, "message": "幫我 generate 這個 job" }
// SSE: tool_call(list_jobs) → tool_result → require_confirm(call_xxx, est=$1.23) → [連線結束]

// 使用者按 Accept → 第二次 POST：重送帶 approved_call_ids
{ "session_id": "<server-returned>", "message": "", "approved_call_ids": ["call_xxx"] }
// SSE: tool_call(generate_tc) → tool_result → done
```

**Message 可以空字串**（重送時）。Backend 會看 history 最後一個 tool 訊息是 `requires_confirmation`，重跑迴圈時帶 approved_call_ids。

### 0.3 Session ID 來源

- 第一次 request：`session_id: null` → backend `get_or_create` 產 UUID
- 所有 SSE event payload **都會帶 `session_id`**（由 route 層注入）
- 前端從**第一個 event 的 `session_id`** 擷取並保存
- 後續 request 都要帶這個 session_id

### 0.4 歷史 resume

- `GET /api/agent/sessions/{session_id}` 回 `{history, totalCostUsd, createdAt, updatedAt}`
- `history` 是 **OpenAI messages 格式**（role + content / tool_calls / tool_call_id），不是 UI message 格式
- 前端需要**自己把 OpenAI history 轉成 UI message**（見 §3.3）

### 0.5 Session 列表

- `GET /api/agent/sessions?limit=20` 回 `{sessions: [{sessionId, totalCostUsd, createdAt, updatedAt, messageCount}]}`
- 沒有 title，前端可用「第一則 user message 前 40 字」當 preview

---

## 1. SSE Event Schema（TypeScript）

放在 `frontend/src/services/agentEvents.ts`：

```typescript
// 所有事件都帶 session_id（backend 在 route 層 setdefault 注入）
export interface BaseAgentEvent {
  session_id: string;
}

export interface MessageEvent extends BaseAgentEvent {
  type: "message";
  text: string;
}

export interface ToolCallEvent extends BaseAgentEvent {
  type: "tool_call";
  call_id: string;
  tool: string;
  args: Record<string, unknown>;
}

export interface ToolResultEvent extends BaseAgentEvent {
  type: "tool_result";
  call_id: string;
  tool: string;
  duration_ms: number;
  result: unknown; // tool-specific; 見 §1.1
}

export interface ToolErrorEvent extends BaseAgentEvent {
  type: "tool_error";
  call_id: string;
  tool: string;
  error: { code: string; message: string; details?: unknown };
}

export interface RequireConfirmEvent extends BaseAgentEvent {
  type: "require_confirm";
  call_id: string;
  tool: string;
  args: Record<string, unknown>;
  est_cost_usd: number;
}

export interface DoneEvent extends BaseAgentEvent {
  type: "done";
  step_count: number;
}

export interface ErrorEvent extends BaseAgentEvent {
  type: "error";
  code: string;    // "internal" | "max_steps_exceeded" | ...
  message: string;
}

export type AgentEvent =
  | MessageEvent
  | ToolCallEvent
  | ToolResultEvent
  | ToolErrorEvent
  | RequireConfirmEvent
  | DoneEvent
  | ErrorEvent;
```

### 1.1 ToolResult payload 形狀（已對照 backend 實作）

**命名慣例**：tool result 一律 **camelCase**。唯一例外是 `get_job_validation` 的 `perRow[].tc_id / test_item / pre_conditions / test_procedure / expected_result / design_method / priority` — 這裡保留 snake_case 因為要直接餵進 `validate_tc` 的 input（該 tool input schema 就是 snake_case）。

```typescript
// 對應 backend/tools/*.py 的 return dict（2026-04-18 實地核對）

// ----- parse_workbook -----
export interface ParseWorkbookResult {
  jobId: string;
  project: string;
  testGroup: string;
  rowCount: number;
  previewHeaders: string[];
  previewRows: Array<Record<string, unknown>>;
  rows: ParsedRow[];
  columnFillStatus: Record<string, number>;
  files: {
    rawFileName: string;
    referenceWorkbookName: string | null;
    specFileName: string | null;
    specFormat: string | null;
  };
}
export interface ParsedRow {
  id: string;              // "row-<num>"
  rowNum: number;
  tcId: string;
  reqId: string;
  testItem: string;
  originalRequirement: string;
  testSet: string;
  specReference: string | null;
  priority: string;
  status: "draft";
  reviewStatus: "pending";
  generated: unknown | null;
  validation: unknown[];
}

// ----- group_tests -----
export interface GroupTestsResult {
  groups: Array<{ testSet: string; count: number; reqIds: string[] }>;
  framework: Record<string, string[]>;
  assignments: Array<{
    id: string | null;
    reqId: string | null;
    testSet: string;
    source: "existing" | "derived";
  }>;
}

// ----- match_spec -----
export interface MatchSpecResult {
  summary: {
    total: number;
    exact: number;
    fuzzy: number;
    unmatched: number;
    hasReferenceWorkbook: boolean;
  };
  matches: Array<{
    id: string | null;
    reqId: string | null;
    testItem: string | null;
    specReference: string | null;
    matchType: string | null;     // "exact" | "fuzzy" | "unmatched" | null
    matchScore: number | null;
  }>;
}

// ----- generate_tc (WRITE_COSTLY) -----
export interface GenerateTcResult {
  tcData: unknown[];           // 生成結果 list；UI 層不直接解析，交給 review module
  cost: number;
  inputTokens: number;
  outputTokens: number;
  cacheCreationTokens: number;
  cacheReadTokens: number;
  model: string;
}

// ----- validate_tc (單筆) -----
export interface ValidateTcResult {
  issues: Array<{
    id: string;
    severity: "warning" | "passing";
    field: string;
    message: string;
  }>;
  hasWarnings: boolean;
}

// ----- write_excel (DESTRUCTIVE) -----
export interface WriteExcelResult {
  outputPath: string;
  rowsWritten: number;
  frameworkSheetWritten: boolean;
}

// ----- inspect_workbook -----
export interface InspectWorkbookResult {
  path: string;
  fileName: string;
  fileSizeBytes: number;
  sheets: string[];
  testGroup: string | null;
  rowsEstimate: number;
  hasTcSheet: boolean;
}

// ----- list_jobs -----
export interface ListJobsResult {
  jobs: Array<{
    jobId: string;
    fileName: string;
    status: string;            // "parsed" | "generating" | "completed" | ...
    rowCount: number;
    testGroup: string | null;
    project: string | null;
  }>;
  total: number;
}

// ----- estimate_cost -----
export interface EstimateCostResult {
  jobId: string;
  rowCount: number;
  model: string;
  batchSize: number;
  estCostUsd: number;          // 4 位小數
}

// ----- get_job_validation -----
// 注意：perRow 欄位是 snake_case（因為餵進 validate_tc）
export interface GetJobValidationResult {
  total: number;
  pass: number;
  warnings: number;
  errors: 0;                   // 目前恆為 0（validator 不丟 error）
  perRow: Array<{
    tc_id: string;
    test_item: string;
    pre_conditions: string;
    test_procedure: string;
    expected_result: string;
    design_method: string;
    priority: string;
  }>;
}

// ----- 匯總 type -----
export type ToolResultByName = {
  parse_workbook: ParseWorkbookResult;
  group_tests: GroupTestsResult;
  match_spec: MatchSpecResult;
  generate_tc: GenerateTcResult;
  validate_tc: ValidateTcResult;
  write_excel: WriteExcelResult;
  inspect_workbook: InspectWorkbookResult;
  list_jobs: ListJobsResult;
  estimate_cost: EstimateCostResult;
  get_job_validation: GetJobValidationResult;
};
```

### 1.2 為什麼要做這份對照

前端 `ToolCallCard` 展開顯示 `result` 時，不同 tool 需要不同渲染：

| Tool | UI 渲染提示 |
|------|----------|
| `parse_workbook` | 顯示 `jobId` + `rowCount` + `files.rawFileName` |
| `list_jobs` | Table：jobId / fileName / status / rowCount |
| `estimate_cost` | 「預估 $X.XX，{rowCount} rows, {model}」一句話 |
| `generate_tc` | 不展開（內容太多），顯示「已生成 N 筆，花費 $X」並放 Open in Review 按鈕 |
| `validate_tc` | Table：severity / field / message |
| `get_job_validation` | 「總數 {total}：通過 {pass}、警告 {warnings}」+ 可展開 perRow |
| `match_spec` | summary 四數字 + 可展開 matches |
| `inspect_workbook` | 檔案摘要 |
| `group_tests` | Table：testSet / count |
| `write_excel` | 顯示 `outputPath` + 下載連結（若是本機路徑可選擇不做下載，只複製路徑） |

---

## 2. Confirm Flow 協定（不漏)

### 2.1 UI 狀態機

```
idle
  ↓ user send message
sending → streaming → [done] → idle
                  ↓
                  [require_confirm] → waiting_confirm
                                        ↓ accept
                                        resuming → streaming → ...
                                        ↓ decline
                                        idle（在 UI 顯示 "已取消"）
```

### 2.2 Accept 實作

```typescript
async function acceptConfirm(event: RequireConfirmEvent) {
  await agentClient.sendTurn({
    session_id: event.session_id,
    message: "",  // 空字串，backend 會繼續 loop
    approved_call_ids: [event.call_id],
  });
}
```

### 2.3 Decline 實作

Decline 不用打 backend。直接在 UI 上標記 call_id 為 declined，顯示「已取消此動作」。下次使用者發新 message 時，backend 看到 history 裡最後是 `requires_confirmation` tool message，LLM 會自然繼續對話（通常會問「要改別的嗎？」）。

**重要**：decline 後 history 裡那筆 `requires_confirmation` 不會被清掉，LLM 下一輪看得到。

---

## 3. `useAgentStore` Zustand Store

檔案：`frontend/src/store/useAgentStore.ts`

### 3.1 State shape

```typescript
interface AgentState {
  // 當前 session
  sessionId: string | null;
  messages: UIMessage[];         // 見 §3.2
  pendingConfirm: RequireConfirmEvent | null;
  streamState: "idle" | "sending" | "streaming" | "waiting_confirm" | "error";
  lastError: { code: string; message: string } | null;

  // Session 列表（側邊 recent sessions）
  recentSessions: SessionSummary[];
  recentSessionsLoadedAt: number | null;

  // 成本追蹤
  currentSessionCost: number;

  // Actions
  sendMessage: (text: string) => Promise<void>;
  acceptConfirm: () => Promise<void>;
  declineConfirm: () => void;
  loadSession: (sessionId: string) => Promise<void>;
  newSession: () => void;
  deleteSession: (sessionId: string) => Promise<void>;
  refreshRecentSessions: () => Promise<void>;
  clearError: () => void;
}
```

### 3.2 UIMessage shape

UI 層專用，非 OpenAI 格式。在 `agentClient.ts` 裡把 events 累積成這個 shape：

```typescript
export type UIMessage =
  | { kind: "user"; id: string; text: string; ts: number }
  | {
      kind: "agent";
      id: string;
      // 一個 agent turn 可能混合 text 和 tool calls，依時序排列
      parts: Array<UITextPart | UIToolPart | UIConfirmPart>;
      ts: number;
    };

interface UITextPart { kind: "text"; text: string; }
interface UIToolPart {
  kind: "tool";
  callId: string;
  tool: string;
  args: Record<string, unknown>;
  status: "running" | "ok" | "error";
  result?: unknown;
  error?: { code: string; message: string };
  durationMs?: number;
}
interface UIConfirmPart {
  kind: "confirm";
  callId: string;
  tool: string;
  args: Record<string, unknown>;
  estCostUsd: number;
  status: "pending" | "accepted" | "declined";
}
```

### 3.3 Resume 時轉換 OpenAI history → UIMessage[]

```typescript
function historyToMessages(history: OpenAIMessage[]): UIMessage[] {
  // role=user → UIMessage kind=user
  // role=assistant 若有 content 且無 tool_calls → 新 agent message 加 text part
  // role=assistant 有 tool_calls → 新 agent message，每個 tool_call 加 tool part（status=ok，沒 result）
  // role=tool → 找對應 tool_call_id 的 part，把 content 的 result 填進去
  // Note: Resume 的 tool part 沒有 durationMs（trace 裡才有，不從 session history 取）
}
```

**Trade-off**：resume 畫面會少了一些細節（duration、部分 reasoning），但主要對話流完整。可接受。

---

## 4. agentClient.ts SSE Wrapper

檔案：`frontend/src/services/agentClient.ts`

### 4.1 關鍵設計決策

- **用 `fetch` + `ReadableStream`，不用 `EventSource`**。原因：`EventSource` 不支援 POST body；我們需要 POST JSON。
- **每個 turn 開一條 stream**，turn 結束（done/require_confirm/error）stream 自然 close。
- **同一時刻最多一條 in-flight stream**。`sendMessage` 期間重入 → reject。

### 4.2 API

```typescript
export class AgentClient {
  async sendTurn(req: {
    session_id: string | null;
    message: string;
    approved_call_ids?: string[];
  }, onEvent: (event: AgentEvent) => void): Promise<void>;

  async getSession(sessionId: string): Promise<SessionDetail>;
  async listSessions(limit?: number): Promise<SessionSummary[]>;
  async deleteSession(sessionId: string): Promise<void>;
  async downloadTrace(sessionId: string): Promise<Blob>;  // for File menu → Export Trace
}
```

### 4.3 SSE 解析

每個 event 長這樣（backend 實際輸出）：
```
event: tool_call
data: {"call_id":"...","tool":"...","args":{...},"session_id":"..."}

```

解析：按 `\n\n` 切 event；每個 event 抽 `event:` 和 `data:` 兩行；`data` 做 `JSON.parse`。

### 4.4 斷線處理

**不做自動重連**。原因：SSE 是 turn 結束就關，真正「異常斷線」的情境只有網路抖動，此時前端：

1. 拋 error part 到該 agent message，標記 `streamState = "error"`
2. 顯示「連線中斷，請重新發送訊息」
3. 使用者重發 = 新 turn；history 已經存到 backend，下次 `sendMessage` 送過去的 `session_id` 不變，LLM 能從 history 接續

**不嘗試 resume 同一個 turn** — turn 語意是 atomic，中斷就視同放棄這個 turn。

---

## 5. ChatModule 元件樹（對照 ROADMAP §5.1.1）

檔案 layout：

```
frontend/src/components/modules/
├── ChatModule.tsx                   # 外殼、訂閱 store、佈局
└── chat/
    ├── MessageList.tsx              # scroll container + auto-scroll-to-bottom
    ├── UserMessageBubble.tsx
    ├── AgentMessageBubble.tsx       # 內含 TextPart / ToolCard / ConfirmCard
    ├── ToolCallCard.tsx             # 展開/收合、狀態 icon、Open in * 按鈕
    ├── ConfirmCard.tsx              # Accept / Decline
    ├── InspectorPanel.tsx           # 右側
    ├── CurrentJobBox.tsx            # 用 useJobStore
    ├── ToolTraceList.tsx            # 最近 20 筆 tool_call
    ├── RecentSessionsList.tsx
    └── InputArea.tsx                # FileDropzone + textarea + SendButton
```

### 5.1 CurrentJobBox 顯示欄位（具體）

從 `useJobStore` 取，若無 current job 顯示「無作用中 Job」：

- Job ID
- 檔名
- 狀態（parsed / generating / reviewed / exported）
- Row 數
- 總成本（若已生成）

### 5.2 ToolTraceList 規則

- 只顯示**當前 session** 的 tool calls（從 `messages` reduce 出所有 `UIToolPart`）
- 最多 20 筆，超過隱藏並顯示「... 另有 N 筆」
- 點擊跳到對話該 tool card（scroll into view）

### 5.3 RecentSessionsList 規則

- 顯示 `recentSessions`（從 store），最多 10 筆
- 每筆顯示：preview（第一則 user message 前 40 字）+ 相對時間 + 成本
- 點擊 → `loadSession(sessionId)`
- 右鍵 / 三點選單 → Delete

---

## 6. Taskbar 按鈕

檔案：`frontend/src/components/system/AgentTaskbarButton.tsx`

### 6.1 狀態映射

| Store 狀態 | 按鈕視覺 | Icon |
|-----------|---------|------|
| `streamState === "idle"` + 無 pendingConfirm | 灰底 | `ri-robot-2-line` |
| `streamState === "sending" \|\| "streaming"` | 藍底，CSS 動畫閃爍 | 同上 |
| `streamState === "waiting_confirm"` | 黃底，CSS 脈動 | `ri-robot-2-fill` |
| `streamState === "error"` | 紅底 | `ri-robot-2-fill` |

### 6.2 點擊行為

- 若 ChatModule window 未開啟 → 開啟
- 若已開啟但未 focus → focus
- 若 `pendingConfirm` 不為 null → 額外 scroll 到該 ConfirmCard

---

## 7. Multi-session UI

ChatModule 標題列放三個按鈕（用 win95 風格）：
- `[New]` → `newSession()`：清掉當前 session 的 state，`sessionId = null`，下次 send 會產新 UUID
- `[Sessions ▼]` → 下拉顯示 `RecentSessionsList`
- `[Export Trace]` → 若有 sessionId，打 `downloadTrace`，用 `<a download>` 觸發下載

**不做**：session rename、session search、session pin。

---

## 8. File upload（chat 裡附件）

ROADMAP 寫「FileDropzone」但沒定協定。簡化設計：

1. 使用者拖檔到 InputArea → 呼叫**既有** `POST /api/parse`，回傳 jobId
2. 把這個 jobId 的資訊預填進輸入框：「附件：{fileName} (job={jobId})，{N} rows」
3. 使用者按 send 時把這段文字一併送進 message

**Rationale**：不需新後端機制。Agent 看到 jobId 會用 `get_job_detail` 或 `list_jobs` 繼續。

---

## 9. 測試矩陣（取代 ROADMAP 的「覆蓋訊息渲染、tool card 展開」）

### 9.1 Unit — `ChatModule.spec.tsx`（Vitest）

| # | 場景 | 斷言 |
|---|------|------|
| 1 | 空 session render | 顯示 empty state 提示 |
| 2 | UIMessage 渲染（user + agent text） | 順序 / 樣式正確 |
| 3 | Agent message 有 tool part（status=running） | Tool card 顯示 spinner |
| 4 | Tool part 完成（status=ok） | 顯示 duration + 可展開 result |
| 5 | Tool part 失敗（status=error） | 顯示 error code + message，不展開 result |
| 6 | ConfirmCard pending 狀態 | Accept / Decline 按鈕可點 |
| 7 | ConfirmCard accepted 後 | 按鈕變 disabled，顯示「已確認」 |
| 8 | Error event 渲染 | 最後加一個系統 error banner |

### 9.2 Integration — `agentClient.spec.ts`

| # | 場景 | 斷言 |
|---|------|------|
| 1 | 解析多事件 stream | onEvent 被呼叫次數 = 事件數 |
| 2 | 事件 data 跨行（`data: {...}\n\n` 邊界） | 解析正確 |
| 3 | Stream 斷線（abort） | 拋 error，不 crash |
| 4 | Accept confirm 流程 | 第二次 POST 帶 `approved_call_ids` |

### 9.3 Store — `useAgentStore.spec.ts`

| # | 場景 | 斷言 |
|---|------|------|
| 1 | sendMessage 流程 | streamState 依序 idle → sending → streaming → idle |
| 2 | require_confirm 中斷 | streamState = waiting_confirm，pendingConfirm 不為 null |
| 3 | loadSession 轉換 OpenAI history | messages 正確還原（user / assistant / tool parts） |
| 4 | newSession 清空 | sessionId = null、messages = [] |

### 9.4 E2E — `agent.spec.ts`（Playwright，mock backend）

| # | 場景 | 斷言 |
|---|------|------|
| 1 | 打開 Agent、發一則訊息、看到回覆 | Message bubble 出現 |
| 2 | Confirm 流程（Accept） | 第二批 tool_call 正確執行 |
| 3 | Taskbar 狀態色切換（idle → streaming → idle） | CSS class 正確 |
| 4 | 切換 session | 前一 session messages 消失，新 session 載入 |
| 5 | Export trace 觸發下載 | 下載請求正確 |

### 9.5 Workspace round-trip（擴充既有 E2E）

在現有 workspace JSON export / import 測試裡，加 agent session 當前狀態應**不**進 workspace（session 獨立儲存在 backend）。驗證：

- Export workspace 不含 agent state
- Import workspace 後 ChatModule 保持原 session 不受影響

---

## 10. 實作順序建議

1. **agentEvents.ts** + **agentClient.ts**（純邏輯，先寫測試）
2. **useAgentStore.ts** + 單元測試
3. **ChatModule 靜態版**：`UIMessage` mock 資料渲染，確認樣式
4. **接 store**：sendMessage / ConfirmCard
5. **InspectorPanel**：接 useJobStore
6. **AgentTaskbarButton**：接 store、window manager
7. **Multi-session UI**：New / Sessions / Export Trace
8. **FileDropzone**：只呼叫現有 parse endpoint，不動後端
9. **E2E**

**checkpoint**：做完 3 後先給一次 demo（靜態 UI），對齊視覺後再往下。

---

## 11. 明確不做

- WebSocket（維持 SSE）
- 自動重連（turn 中斷 = 使用者重送）
- Session title / search / pin
- Markdown 完整渲染（text part 先用 `white-space: pre-wrap`，需求出現再升級）
- 中斷 in-flight turn（Cancel button — 先不做，等使用者回報才補）
- 多 session 平行跑（UI 只開一個 ChatModule window）

---

## 12. 對 ROADMAP 的勘誤

1. ROADMAP §4.3.1 的 `attachments` 欄位 backend 沒實作，本文件 §8 改走「用既有 parse endpoint」
2. ROADMAP §5.3.1 的 `state_update` event 目前 backend 沒 emit；前端接收邏輯先不寫，等 Phase 3 補
3. ROADMAP 宣稱 ChatModule 有「斷線重連」— 本文件 §4.4 降級為「不重連」

這三點都**不阻塞 Phase 2 完成**，記錄在此供未來檢視。
