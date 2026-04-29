import { describe, expect, it } from "vitest";
import {
  aggregate,
  deriveStatus,
  formatCost,
  formatDuration,
  formatPercent,
  toRun,
} from "../services/runAdapter";
import type { JobRecord } from "../store/useJobHistoryStore";

function makeRecord(overrides: Partial<JobRecord> = {}): JobRecord {
  return {
    id: "j1",
    kind: "generate",
    model: "claude-opus",
    startedAt: 1_000,
    finishedAt: 5_000,
    rowsTotal: 10,
    rowsProcessed: 10,
    cost: 0.5,
    inputTokens: 100,
    outputTokens: 200,
    cacheReadTokens: 0,
    cacheCreationTokens: 0,
    ...overrides,
  };
}

describe("deriveStatus", () => {
  it("running 當 finishedAt 為 0", () => {
    expect(deriveStatus(makeRecord({ finishedAt: 0 }))).toBe("running");
  });

  it("completed 當所有 row 都處理完", () => {
    expect(deriveStatus(makeRecord())).toBe("completed");
  });

  it("partial 當 processed 少於 total", () => {
    expect(
      deriveStatus(makeRecord({ rowsTotal: 10, rowsProcessed: 4 }))
    ).toBe("partial");
  });

  it("failed 當 processed 為 0 但 total > 0", () => {
    expect(
      deriveStatus(makeRecord({ rowsTotal: 10, rowsProcessed: 0 }))
    ).toBe("failed");
  });
});

describe("toRun", () => {
  it("把 JobRecord 包成 Run view-model", () => {
    const run = toRun(makeRecord());
    expect(run.id).toBe("j1");
    expect(run.kindLabel).toBe("Generate");
    expect(run.status).toBe("completed");
    expect(run.durationMs).toBe(4_000);
    expect(run.progress).toBe(1);
    expect(run.tokens.input).toBe(100);
  });

  it("running run 沒有 duration", () => {
    const run = toRun(makeRecord({ finishedAt: 0 }));
    expect(run.durationMs).toBeNull();
    expect(run.status).toBe("running");
  });
});

describe("aggregate", () => {
  it("計算 KPI 數據", () => {
    const runs = [
      toRun(makeRecord({ id: "1" })),
      toRun(makeRecord({ id: "2", rowsProcessed: 5 })),
      toRun(makeRecord({ id: "3", rowsProcessed: 0 })),
      toRun(makeRecord({ id: "4", finishedAt: 0 })),
    ];
    const a = aggregate(runs, 10_000);
    expect(a.total).toBe(4);
    expect(a.finishedCount).toBe(3);
    expect(a.successCount).toBe(1);
    expect(a.failCount).toBe(1);
    expect(a.partialCount).toBe(1);
    expect(a.issueCount).toBe(2);
    expect(a.runningCount).toBe(1);
    expect(a.successRate).toBeCloseTo(1 / 3); // 排除 running
    expect(a.avgDurationMs).toBe(4_000);
    expect(a.completedAvgDurationMs).toBe(4_000);
    expect(a.recent7dTotal).toBe(4);
    expect(a.recent7dSuccessRate).toBeCloseTo(1 / 3);
  });

  it("7 day KPI window excludes older runs", () => {
    const now = 8 * 86_400_000;
    const runs = [
      toRun(makeRecord({ id: "old", finishedAt: 1_000 })),
      toRun(makeRecord({ id: "recent", startedAt: now - 10_000, finishedAt: now })),
    ];

    const a = aggregate(runs, now);

    expect(a.total).toBe(2);
    expect(a.recent7dTotal).toBe(1);
    expect(a.recent7dSuccessRate).toBe(1);
  });
});

describe("formatters", () => {
  it("formatDuration", () => {
    expect(formatDuration(null)).toBe("—");
    expect(formatDuration(500)).toBe("500ms");
    expect(formatDuration(2_500)).toBe("2.5s");
    expect(formatDuration(125_000)).toBe("2m 5s");
  });

  it("formatCost", () => {
    expect(formatCost(0)).toBe("$0");
    expect(formatCost(0.0001)).toBe("$0.0001");
    expect(formatCost(1.234)).toBe("$1.23");
  });

  it("formatPercent", () => {
    expect(formatPercent(0.756)).toBe("76%");
  });
});
