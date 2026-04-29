// Client-side event tracking。每個 track() 呼叫：
// 1. console.debug（dev/test only）
// 2. 推到 window.__tcEvents（dev/test only，給 Playwright 斷言）
// 3. 排入 send queue，定期 batched flush 到 POST /api/events
//
// 失敗 silent — telemetry 不能拖累主功能；網路錯誤就丟掉，避免堆積記憶體。

export type EventName =
  | "home_new_run_click"
  | "builder_step_next"
  | "builder_validation_fail"
  | "run_execute_start"
  | "run_execute_success"
  | "run_execute_fail"
  | "run_retry_click"
  | "template_use_click"
  | "output_compare_open";

interface KnownEvents {
  home_new_run_click: { source?: string };
  builder_step_next: { from: string; to: string };
  builder_validation_fail: { criticalCount: number };
  run_execute_start: { jobId?: string | null; rowCount: number };
  run_execute_success: {
    jobId?: string | null;
    rowCount: number;
    durationMs?: number;
  };
  run_execute_fail: { jobId?: string | null; reason: string };
  run_retry_click: { runId: string; mode: "rerun" | "edit" };
  template_use_click: { templateId: string };
  output_compare_open: { a: string; b: string };
}

export type EventProps<T extends EventName> = T extends keyof KnownEvents
  ? KnownEvents[T]
  : Record<string, unknown>;

interface RecordedEvent {
  name: EventName;
  props: Record<string, unknown>;
  ts: number;
}

const BUFFER_LIMIT = 200;
const FLUSH_INTERVAL_MS = 5000;
const FLUSH_THRESHOLD = 10;
const MAX_QUEUE = 500;

let pendingQueue: RecordedEvent[] = [];
let flushTimer: ReturnType<typeof setTimeout> | null = null;

function pushBuffer(event: RecordedEvent) {
  if (typeof window === "undefined") return;
  if (process.env.NODE_ENV === "production") return;
  const w = window as unknown as { __tcEvents?: RecordedEvent[] };
  if (!Array.isArray(w.__tcEvents)) w.__tcEvents = [];
  w.__tcEvents.push(event);
  if (w.__tcEvents.length > BUFFER_LIMIT) {
    w.__tcEvents.splice(0, w.__tcEvents.length - BUFFER_LIMIT);
  }
}

function scheduleFlush() {
  if (typeof window === "undefined") return;
  if (flushTimer) return;
  flushTimer = setTimeout(() => {
    flushTimer = null;
    void flush();
  }, FLUSH_INTERVAL_MS);
}

async function flush() {
  if (pendingQueue.length === 0) return;
  const batch = pendingQueue.splice(0, pendingQueue.length);
  try {
    await fetch("/api/events", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ events: batch }),
      keepalive: true,
    });
  } catch {
    // silent — telemetry 不重要到要 retry
  }
}

export function track<T extends EventName>(name: T, props: EventProps<T>): void {
  const event: RecordedEvent = {
    name,
    props: props as Record<string, unknown>,
    ts: Date.now(),
  };
  pushBuffer(event);
  if (typeof window !== "undefined" && process.env.NODE_ENV !== "production") {
    // eslint-disable-next-line no-console
    console.debug("[telemetry]", name, props);
  }

  if (typeof window === "undefined") return;
  // 測試環境（NODE_ENV='test'）跳過實際送出，避免污染外部 fetch mock
  if (process.env.NODE_ENV === "test") return;

  pendingQueue.push(event);
  if (pendingQueue.length > MAX_QUEUE) {
    pendingQueue.splice(0, pendingQueue.length - MAX_QUEUE);
  }
  if (pendingQueue.length >= FLUSH_THRESHOLD) {
    void flush();
  } else {
    scheduleFlush();
  }
}

// 測試 / 工具：拿目前 buffer 快照
export function getRecordedEvents(): RecordedEvent[] {
  if (typeof window === "undefined") return [];
  const w = window as unknown as { __tcEvents?: RecordedEvent[] };
  return w.__tcEvents ? [...w.__tcEvents] : [];
}

export function clearRecordedEvents(): void {
  if (typeof window === "undefined") return;
  const w = window as unknown as { __tcEvents?: RecordedEvent[] };
  w.__tcEvents = [];
}

// 暫停應用前主動 flush（如 beforeunload）；keepalive fetch 也會嘗試送出。
export function flushNow(): Promise<void> {
  return flush();
}

// 測試專用：清掉 pending queue
export function _resetForTest(): void {
  pendingQueue = [];
  if (flushTimer) {
    clearTimeout(flushTimer);
    flushTimer = null;
  }
}
