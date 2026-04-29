import { afterEach, beforeEach, describe, expect, it } from "vitest";
import {
  useJobHistoryStore,
  type JobRecord,
} from "../store/useJobHistoryStore";

const LS_KEY = "tc-generator-job-history";

function makeRec(id: string, overrides: Partial<JobRecord> = {}): JobRecord {
  const now = Date.now();
  return {
    id,
    kind: "generate",
    model: "gpt-5",
    startedAt: now,
    finishedAt: now + 1000,
    rowsTotal: 5,
    rowsProcessed: 5,
    cost: 0.1,
    inputTokens: 100,
    outputTokens: 200,
    cacheReadTokens: 0,
    cacheCreationTokens: 0,
    ...overrides,
  };
}

function reset() {
  localStorage.clear();
  useJobHistoryStore.setState({ records: [], loaded: false });
}

beforeEach(reset);
afterEach(reset);

describe("useJobHistoryStore", () => {
  it("appendRecord 把最新放最前", () => {
    useJobHistoryStore.getState().appendRecord(makeRec("r1"));
    useJobHistoryStore.getState().appendRecord(makeRec("r2"));
    const ids = useJobHistoryStore.getState().records.map((r) => r.id);
    expect(ids).toEqual(["r2", "r1"]);
  });

  it("appendRecord 持久化到 localStorage", () => {
    useJobHistoryStore.getState().appendRecord(makeRec("r1"));
    const saved = JSON.parse(localStorage.getItem(LS_KEY) ?? "[]");
    expect(saved).toHaveLength(1);
    expect(saved[0].id).toBe("r1");
  });

  it("totalCost 累計", () => {
    useJobHistoryStore
      .getState()
      .appendRecord(makeRec("r1", { cost: 0.5 }));
    useJobHistoryStore
      .getState()
      .appendRecord(makeRec("r2", { cost: 1.25 }));
    expect(useJobHistoryStore.getState().totalCost()).toBeCloseTo(1.75);
  });

  it("loadFromStorage 過濾超過 90 天的舊紀錄", () => {
    const tooOld = Date.now() - 95 * 24 * 60 * 60 * 1000;
    localStorage.setItem(
      LS_KEY,
      JSON.stringify([
        makeRec("old", { startedAt: tooOld, finishedAt: tooOld + 1 }),
        makeRec("fresh"),
      ])
    );
    useJobHistoryStore.getState().loadFromStorage();
    const ids = useJobHistoryStore.getState().records.map((r) => r.id);
    expect(ids).toEqual(["fresh"]);
  });

  it("clearHistory 清空", () => {
    useJobHistoryStore.getState().appendRecord(makeRec("r1"));
    useJobHistoryStore.getState().clearHistory();
    expect(useJobHistoryStore.getState().records).toEqual([]);
    expect(localStorage.getItem(LS_KEY)).toBe("[]");
  });
});
