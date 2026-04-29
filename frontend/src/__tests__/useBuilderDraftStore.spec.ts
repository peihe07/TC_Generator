import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { useBuilderDraftStore } from "../store/useBuilderDraftStore";

const LS_KEY = "tc-generator-builder-draft";

function reset() {
  localStorage.clear();
  useBuilderDraftStore.setState({ draft: null, loaded: false });
}

beforeEach(reset);
afterEach(reset);

describe("useBuilderDraftStore", () => {
  it("loadFromStorage 沒有資料時設為 loaded 但 draft 為 null", () => {
    useBuilderDraftStore.getState().loadFromStorage();
    const { draft, loaded } = useBuilderDraftStore.getState();
    expect(loaded).toBe(true);
    expect(draft).toBeNull();
  });

  it("startNew 產生 id、currentStep=data 並寫入 localStorage", () => {
    const draft = useBuilderDraftStore.getState().startNew();
    expect(draft.id).toMatch(/^draft_/);
    expect(draft.currentStep).toBe("data");
    expect(useBuilderDraftStore.getState().draft).toEqual(draft);
    const persisted = JSON.parse(localStorage.getItem(LS_KEY) ?? "null");
    expect(persisted?.id).toBe(draft.id);
  });

  it("update 會 patch 欄位並更新 updatedAt", () => {
    const a = useBuilderDraftStore.getState().startNew();
    const before = a.updatedAt;
    // 等到不同 timestamp
    const t0 = Date.now();
    while (Date.now() === t0) {
      // spin
    }
    useBuilderDraftStore.getState().update({
      data: { fileName: "tc.xlsx", rowCount: 12 },
    });
    const next = useBuilderDraftStore.getState().draft!;
    expect(next.data?.fileName).toBe("tc.xlsx");
    expect(next.data?.rowCount).toBe(12);
    expect(next.updatedAt).toBeGreaterThan(before);
  });

  it("markStepComplete 寫入 completed flag", () => {
    useBuilderDraftStore.getState().startNew();
    useBuilderDraftStore.getState().markStepComplete("data", true);
    expect(useBuilderDraftStore.getState().draft?.completed?.data).toBe(true);
    useBuilderDraftStore.getState().markStepComplete("data", false);
    expect(useBuilderDraftStore.getState().draft?.completed?.data).toBe(false);
  });

  it("clear 清空 draft 與 localStorage", () => {
    useBuilderDraftStore.getState().startNew();
    expect(localStorage.getItem(LS_KEY)).not.toBeNull();
    useBuilderDraftStore.getState().clear();
    expect(useBuilderDraftStore.getState().draft).toBeNull();
    expect(localStorage.getItem(LS_KEY)).toBeNull();
  });

  it("loadFromStorage 從 localStorage 還原既有 draft", () => {
    const seeded = {
      id: "draft_seed",
      createdAt: 1,
      updatedAt: 2,
      currentStep: "configure",
    };
    localStorage.setItem(LS_KEY, JSON.stringify(seeded));
    useBuilderDraftStore.getState().loadFromStorage();
    expect(useBuilderDraftStore.getState().draft?.id).toBe("draft_seed");
    expect(useBuilderDraftStore.getState().draft?.currentStep).toBe(
      "configure"
    );
  });
});
