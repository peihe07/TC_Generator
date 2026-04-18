# Phase 2 Validation + Phase 3 — 交付規格

**版本**：v1
**日期**：2026-04-18
**狀態**：待 Sonnet 4.6 實作
**上游文件**：[ROADMAP.md](ROADMAP.md)、[PHASE2_SPEC.md](PHASE2_SPEC.md)

本文件分兩個 Part：
- **Part A**：Phase 2 煙霧測試與缺陷修正（0.5 天）
- **Part B**：Phase 3 剩餘工作（1 天）

兩者建議依序執行：先完成 A 再進 B，因為 B 的 E2E 需要 A 的驗證做過。

---

# Part A — Phase 2 煙霧測試

## A.1 目的

Phase 2 完成 TypeScript typecheck（0 error）+ Vitest 23 pass，但**從未用真實 backend 跑過完整 Chat 流程**。這一步的目的是發現單元測試覆蓋不到的整合問題。

## A.2 前置需求

1. Backend 能跑：`uvicorn api_server:app --app-dir backend --host 127.0.0.1 --port 8000`
2. Frontend 能跑：`cd frontend && npm run dev`
3. `OPENAI_API_KEY` 環境變數已設定（`/api/agent/chat` 需要真實 LLM）

如果沒有 API key，跳過 scenario 1-5 的 LLM 互動部分，只驗證 SSE 解析與前端狀態流轉（用 `curl` 直打 backend，mock LLM response 不容易，可先做 scenarios 6-9 的前端邊界）。

## A.3 測試腳本（命令列版）

先不依賴 UI，用 `curl` 直打 backend 驗 SSE 協定對前端的假設是否成立。

### Scenario 1 — 基本 message

```bash
curl -N -X POST http://127.0.0.1:8000/api/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": null, "message": "Hello"}'
```

**應看到**（SSE 格式）：
```
event: message
data: {"text":"...","session_id":"<uuid>"}

event: done
data: {"step_count":1,"session_id":"<uuid>"}
```

**失敗徵兆與對應**：
- 沒有 `session_id` 欄位 → backend bug，檢查 `routes/agent.py` 的 `payload_data.setdefault`
- `event:` 後面沒有空格 → 前端 `parseSSEEvent` 要改 `line.startsWith('event:')`
- Done 事件跟 message 之間沒有空白行 → 協定實作有誤

### Scenario 2 — Tool call + result

```bash
curl -N -X POST http://127.0.0.1:8000/api/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": null, "message": "List recent jobs"}'
```

**應看到**：
```
event: tool_call
data: {"call_id":"call_xxx","tool":"list_jobs","args":{...},"session_id":"..."}

event: tool_result
data: {"call_id":"call_xxx","tool":"list_jobs","duration_ms":N,"result":{"jobs":[],"total":0},"session_id":"..."}

event: message
data: {"text":"...","session_id":"..."}

event: done
data: {...}
```

**驗證**：`tool_result.result` 的 shape 是否符合 `PHASE2_SPEC.md §1.1` 的 `ListJobsResult` interface。若不符，更新 `frontend/src/services/agentEvents.ts`。

### Scenario 3 — Budget gate（require_confirm）

需要先有 parsed job 才能觸發。先走 scenario 4 parse 一個檔，拿到 jobId 後：

```bash
curl -N -X POST http://127.0.0.1:8000/api/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": null, "message": "Generate TC for job <JOB_ID> with rows from 1 to 20"}'
```

**應看到**（可能在幾輪 tool call 後）：
```
event: require_confirm
data: {"call_id":"...","tool":"generate_tc","args":{...},"est_cost_usd":0.XX,"session_id":"..."}
```

**然後** stream 就結束了（這是 Phase 2 spec §0.1 的 turn-based 語意）。

### Scenario 4 — Confirm resume

用 scenario 3 拿到的 `session_id` 和 `call_id`：

```bash
curl -N -X POST http://127.0.0.1:8000/api/agent/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"<SID>","message":"","approved_call_ids":["<CALL_ID>"]}'
```

**應看到** 真正的 tool_call → tool_result → done。

### Scenario 5 — Session resume

```bash
curl http://127.0.0.1:8000/api/agent/sessions/<SID>
```

回應應為 JSON：`{"sessionId":"...","history":[...],"totalCostUsd":N,"createdAt":T,"updatedAt":T}`。

**驗證**：`history` 是 OpenAI messages 陣列。拿去餵 `frontend/src/services/agentClient.ts` 的 `historyToMessages()` 應該能正常轉成 UIMessage。

## A.4 UI 手動測試（dev server）

跑 `npm run dev` 後開 `http://localhost:3000`：

### Scenario 6 — 開啟 Chat Window

- 桌面雙擊 Agent 圖示 → 應開啟 Agent Co-pilot 視窗
- Start Menu 也能開
- Taskbar 右側機器人按鈕也能開
- 關閉後重開應記得位置（`useWindowStore` persist）

### Scenario 7 — 基本對話

- 輸入「Hello」→ Enter → 使用者 bubble 立即出現（optimistic）
- Agent 回覆應串流顯示
- Taskbar button 在 streaming 期間應變藍色並閃爍
- 完成後回灰色

### Scenario 8 — Tool call 卡片展開

- 要 agent「list recent jobs」
- ToolCallCard 出現，status=running → ok
- 展開 → Args + Result 顯示
- 對於 `parse_workbook` / `list_jobs` 等應看到 `Open in *` 按鈕

### Scenario 9 — Budget gate

- 觸發需確認的動作（或手動改 `backend/tools/_budget.py` 門檻到 $0.01）
- ConfirmCard 出現
- Taskbar 按鈕變黃色脈動
- 按 Accept → 執行
- 按 Decline → 顯示「已取消」

### Scenario 10 — FileDropzone

- 拖一個 `.xlsx` 到輸入框
- 應顯示 spinner，完成後輸入框預填「附件：xxx.xlsx (job=xxx，N rows)」
- 按 Send → agent 應能理解 jobId

### Scenario 11 — Session 管理

- 建 session A → 送訊息
- 按 header 的 `+` (New Session) → 應清空進 session 新狀態
- 按 InspectorPanel 的 session A → 應還原歷史
- 按 trash icon → 應刪除

### Scenario 12 — 重新整理

- 對話中重新整理頁面
- Session 應能從 backend resume（檢查 sessionId 是否持久化）
- 或者變回空 session 也可接受（看目前設計），但應該一致

**當前設計**：session 不持久化到 localStorage，重載 = 新 session。若後續想要持久化，需改 `useAgentStore`。

## A.5 常見問題排查清單

| 徵兆 | 可能原因 | 修正位置 |
|------|---------|---------|
| SSE 解析壞掉（看不到訊息） | `parseSSEEvent` 對空行處理 | `agentClient.ts:parseSSEEvent` |
| Tool result 欄位 undefined | camelCase/snake_case 不符 | `agentEvents.ts` 對應的 `*Result` interface |
| ConfirmCard 點 Accept 後卡住 | `approved_call_ids` 沒送對 | `useAgentStore.ts:acceptConfirm` |
| Session resume 後對話亂掉 | `historyToMessages` 邏輯有漏 | `agentClient.ts:historyToMessages` |
| Taskbar button 顏色沒切換 | streamState 沒更新 | `useAgentStore.ts` 狀態轉換 |
| 拖檔無反應 | `dataTransfer.files` 拿不到 | `InputArea.tsx:handleDrop` |

## A.6 完成標準

- [ ] 12 個 scenario 全部跑過
- [ ] 有 bug 的寫進 `docs/PHASE2_SMOKE_ISSUES.md`（包含：symptom、repro steps、fix commit）
- [ ] 所有 bug 修完
- [ ] 最後再跑一次 `npm run test:unit` + `npm run typecheck`，全綠

## A.7 交付物

- 若無 bug：一個 report commit `docs: add phase 2 smoke test report` 記錄跑過的 scenarios
- 若有 bug：多個 fix commits + 一個 report

---

# Part B — Phase 3 剩餘工作

**目的**：完成 GUI ↔ Agent 雙向 handoff，收尾合規相關 UX。

**範圍**：原 ROADMAP Phase 3 扣掉 Phase 2 已做的部分，只剩 2 項。

## B.1 「求助 AI」按鈕（5 個 GUI module）

### B.1.1 需求

在每個 GUI module 的右上角工具列加一個 Remix Icon `ri-question-answer-line` 按鈕。點擊：
1. 開啟 ChatModule（若未開）並 focus
2. 預填 context prompt 到輸入框

### B.1.2 Context prompt 模板

每個 module 的 context 不一樣。規則：

| Module | Context prompt 模板 |
|--------|---------------------|
| Upload | `[context: 目前在 Upload Module]\n[目前檔案: {fileName or "未上傳"}]\n` |
| Configure | `[context: 目前在 Configure Module, job={jobId}]\n[Test Sets: {count} 個]\n` |
| Generate | `[context: 目前在 Generate Module, job={jobId}]\n[進度: {processed}/{total} rows, 成本 ${cost}]\n` |
| Review | `[context: 目前在 Review Module, job={jobId}]\n[Validator: {warningCount} warnings]\n` |
| Export | `[context: 目前在 Export Module, job={jobId}]\n` |

**取值來源**：`useJobStore`（jobMetadata、stats、tcRows）。沒有 job 時 fallback 成 `未開啟 job`。

### B.1.3 實作步驟

#### 建共用元件
新增 `frontend/src/components/system/HelpFromAgentButton.tsx`：

```tsx
'use client';

import React from 'react';
import { RiQuestionAnswerLine } from '@remixicon/react';
import { useAgentStore } from '../../store/useAgentStore';
import { useWindowStore } from '../../store/useWindowStore';

interface Props {
  contextPrompt: string;  // 由各 module 傳入
  title?: string;
}

export default function HelpFromAgentButton({ contextPrompt, title }: Props) {
  const openWindow = useWindowStore((s) => s.openWindow);
  const focusWindow = useWindowStore((s) => s.focusWindow);
  const chatWindow = useWindowStore((s) => s.windows.chat);

  const handleClick = () => {
    // Prefill input area via a custom event OR extend useAgentStore with a draft field
    window.dispatchEvent(new CustomEvent('agent-prefill', { detail: contextPrompt }));

    if (!chatWindow.isOpen) {
      openWindow('chat', 'Agent Co-pilot');
    } else {
      focusWindow('chat');
    }
  };

  return (
    <button
      className="btn-help-agent"
      onClick={handleClick}
      title={title ?? '求助 AI'}
    >
      <RiQuestionAnswerLine size={14} />
    </button>
  );
}
```

#### 更新 InputArea 聽 prefill 事件

在 `frontend/src/components/modules/chat/InputArea.tsx`：

```tsx
useEffect(() => {
  const handler = (e: Event) => {
    const prompt = (e as CustomEvent<string>).detail;
    setText((prev) => prompt + prev);
    textareaRef.current?.focus();
  };
  window.addEventListener('agent-prefill', handler);
  return () => window.removeEventListener('agent-prefill', handler);
}, []);
```

#### 在 5 個 module 加按鈕

找每個 module 的 header / toolbar 區（通常是 `*Module.tsx` 的最上方 div），插入：

```tsx
<HelpFromAgentButton
  contextPrompt={buildContext()}
  title="求助 AI"
/>
```

`buildContext()` 各 module 自己定義，從 `useJobStore()` 取值。

#### CSS（加到 `win95.css`）

```css
.btn-help-agent {
  width: 22px;
  height: 22px;
  padding: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.btn-help-agent:hover {
  background: var(--win95-select-bg);
  color: var(--win95-select-text);
}
```

### B.1.4 驗收

- 5 個 module 都有按鈕
- 每個按鈕點擊：
  - ChatModule 開啟 / focus
  - InputArea 自動 focus
  - 輸入框最前面出現對應 context prompt
- Context 變數正確取值（用 console.log 確認一輪）
- Typecheck 0 error

## B.2 混用劇本 E2E

### B.2.1 Scenario（對照 ROADMAP §7.3 劇本 B）

**Setup**：
- Mock `/api/agent/chat` 吐出固定劇本
- Mock `/api/parse`、`/api/generate/stream` 等 GUI 流程的 endpoint

**步驟**：
1. GUI 流程：Upload xlsx → Configure → Generate (mock, 假設 5 個 warnings)
2. 開 Review，看到 warnings
3. 點 Review 的「求助 AI」按鈕 → ChatModule 開啟，context 預填
4. 在 Chat 送「幫我重跑這 5 個 warning rows」
5. Agent 回一個 `regenerate_tc` tool_call（mock response）→ tool_result
6. 按 ToolCallCard 的 `Open in Review` 跳回 Review
7. Review 畫面應仍是原本的 job（state 一致）
8. 回到 Export → 匯出成功

### B.2.2 檔案

新增 `frontend/e2e/handoff.spec.ts`。

### B.2.3 實作重點

- 大量 mock `page.route()`，不依賴真實 backend
- 驗證 `useJobStore` 的 `jobMetadata` 在 chat 期間沒被誤動
- 驗證 context prompt 真的出現在輸入框

### B.2.4 驗收

- `npx playwright test e2e/handoff.spec.ts` pass
- 劇本執行中間沒 console error

## B.3 衝突處理 toast — 延後

**原因**：backend 目前沒 emit `state_update` event（`routes/agent.py` 和 `agent_dispatcher.py` 都沒推）。實作完整衝突 toast 需要先做 backend：

1. `dispatch_tool` 完成後判斷該 tool 是否影響 job state（例如 `parse_workbook` / `generate_tc`）
2. 若是，load 最新 job state
3. 從 SSE 推 `state_update: {jobId, delta}`
4. 前端 `agentClient.ts` 加 `state_update` handler
5. `useJobStore` 比對 revision 決定是否顯示 toast

**工作量**：2-3 天（含 backend + frontend）。

**決策**：Phase 3 不做，放到 Phase 4 或更後面。原因：
- 實務上雙邊同時改同一個 job 的頻率極低
- 使用者不在意時，靜默以 server 端資料為準即可
- Phase 2 spec §12 已記錄此 known limitation

## B.4 Phase 3 完成標準

- [ ] B.1 全部 5 個 module 都有「求助 AI」按鈕，context 正確
- [ ] B.2 `handoff.spec.ts` E2E pass
- [ ] `npm run test:unit` + `npm run test:e2e` + `npx tsc --noEmit` 全綠
- [ ] 一個 commit `feat(frontend): add Help from Agent buttons to GUI modules (Phase 3)`
- [ ] 一個 commit `test(frontend): add GUI-Agent handoff E2E scenario (Phase 3)`
- [ ] 更新 `docs/STATUS.md` 標記 Phase 3 完成

---

# 時程估算

| Part | 工作 | 估時 |
|------|------|------|
| A | 12 個 smoke test scenario + 修 bug | 0.5 天 |
| B.1 | 5 個 Help-from-Agent 按鈕 | 0.5 天 |
| B.2 | 混用劇本 E2E | 0.5 天 |
| **合計** | | **1.5 天** |

---

# 給 Sonnet 4.6 的指示

1. **先做 Part A，再做 Part B**
2. Part A 若發現 bug，寫進 `docs/PHASE2_SMOKE_ISSUES.md`，每修一個 bug 一個 commit（`fix(frontend): ...` 或 `fix(backend): ...`）
3. Part B 照 B.1 → B.2 順序
4. 每完成一個 commit，先 stage 但不要執行 `git commit`，讓使用者確認後自己執行（參照專案 CLAUDE.md 的規則）
5. 遇到需要決策的地方（例如 scenario 5 的 session 持久化要不要做），先停下來問，不要自行決定
6. 每個 commit 之前必跑：`npx tsc --noEmit` + `npx vitest run`
7. 如果要改 backend，動到 `routes/agent.py` 或 `agent_dispatcher.py` 之外的檔案前先問
