// Client-only event tracking. 後端尚無 collector endpoint，所以這層只做：
// 1. console.debug 方便本地觀察
// 2. 推到 window.__tcEvents（dev/test mode）給 Playwright 斷言
// 3. 預留 transport 接口以便後續接後端 / 分析工具
//
// Event 命名沿用 blueprint §13.2。新增事件請：
// - 在 EventName union 加上 literal
// - 在 KnownEvents map 補欄位限制（強型別 props）

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
