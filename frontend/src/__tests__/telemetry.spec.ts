import { afterEach, beforeEach, describe, expect, it } from "vitest";
import {
  clearRecordedEvents,
  getRecordedEvents,
  track,
} from "../lib/telemetry";

beforeEach(() => clearRecordedEvents());
afterEach(() => clearRecordedEvents());

describe("telemetry", () => {
  it("track 把事件推到 buffer", () => {
    track("home_new_run_click", { source: "test" });
    const events = getRecordedEvents();
    expect(events).toHaveLength(1);
    expect(events[0].name).toBe("home_new_run_click");
    expect(events[0].props.source).toBe("test");
    expect(typeof events[0].ts).toBe("number");
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
