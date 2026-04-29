import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  _resetForTest,
  clearRecordedEvents,
  flushNow,
  getRecordedEvents,
  track,
} from "../lib/telemetry";

beforeEach(() => {
  localStorage.clear();
  clearRecordedEvents();
  _resetForTest();
});
afterEach(() => {
  localStorage.clear();
  clearRecordedEvents();
  _resetForTest();
  vi.restoreAllMocks();
  vi.unstubAllEnvs();
});

describe("telemetry", () => {
  it("track 把事件推到 buffer", () => {
    track("home_new_run_click", { source: "test" });
    const events = getRecordedEvents();
    expect(events).toHaveLength(1);
    expect(events[0].name).toBe("home_new_run_click");
    expect(events[0].props.source).toBe("test");
    expect(events[0].experiments).toEqual({});
    expect(typeof events[0].ts).toBe("number");
  });

  it("track 附帶目前 experiment assignment", () => {
    localStorage.setItem(
      "tc:experiments:v1",
      JSON.stringify({
        home_layout_emphasis: {
          key: "home_layout_emphasis",
          variant: "action_first",
          assignedAt: 1000,
          source: "override",
        },
      })
    );

    track("experiment_exposure", {
      experiment: "home_layout_emphasis",
      variant: "action_first",
    });

    expect(getRecordedEvents()[0].experiments).toEqual({
      home_layout_emphasis: "action_first",
    });
  });

  it("buffer 上限為 200，溢出時移除最舊的", () => {
    for (let i = 0; i < 210; i++) {
      track("builder_step_next", { from: "data", to: "configure" });
    }
    expect(getRecordedEvents()).toHaveLength(200);
  });

  it("clearRecordedEvents 清空 buffer", () => {
    track("home_new_run_click", {});
    clearRecordedEvents();
    expect(getRecordedEvents()).toEqual([]);
  });

  it("非 test 環境下批次 flush 到 /api/events", async () => {
    vi.stubEnv("NODE_ENV", "development");
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ ok: true, count: 10 }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      })
    );
    vi.stubGlobal("fetch", fetchMock);

    // 10 個事件達到 FLUSH_THRESHOLD → 立即 flush
    for (let i = 0; i < 10; i++) {
      track("builder_step_next", { from: "data", to: "configure" });
    }
    await flushNow();

    expect(fetchMock).toHaveBeenCalledTimes(1);
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe("/api/events");
    expect((init as RequestInit).method).toBe("POST");
    const body = JSON.parse((init as RequestInit).body as string);
    expect(body.events).toHaveLength(10);
    expect(body.events[0].name).toBe("builder_step_next");
  });

  it("test 環境下不送出（避免污染外部 fetch mock）", async () => {
    const fetchMock = vi.fn();
    vi.stubGlobal("fetch", fetchMock);
    track("home_new_run_click", { source: "x" });
    await flushNow();
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it("不同 event 的 props 都被保留", () => {
    track("run_execute_start", { jobId: "j1", rowCount: 5 });
    track("run_execute_success", {
      jobId: "j1",
      rowCount: 5,
      durationMs: 1234,
    });
    track("run_execute_fail", { jobId: "j1", reason: "boom" });

    const events = getRecordedEvents();
    expect(events.map((e) => e.name)).toEqual([
      "run_execute_start",
      "run_execute_success",
      "run_execute_fail",
    ]);
    expect(events[1].props.durationMs).toBe(1234);
    expect(events[2].props.reason).toBe("boom");
  });
});
