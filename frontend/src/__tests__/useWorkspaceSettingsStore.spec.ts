import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { useWorkspaceSettingsStore } from "../store/useWorkspaceSettingsStore";

const LS_KEY = "tc-generator-workspace-settings";

const FALLBACK = {
  defaultModel: "gpt-5",
  defaultBatchSize: 5,
  defaultBudgetLimit: 10,
  defaultCreditBalance: 0,
  defaultStrictValidation: false,
};

function reset() {
  localStorage.clear();
  useWorkspaceSettingsStore.setState({
    settings: { ...FALLBACK },
    loaded: false,
  });
}

beforeEach(reset);
afterEach(reset);

describe("useWorkspaceSettingsStore", () => {
  it("初始值套 FALLBACK", () => {
    expect(useWorkspaceSettingsStore.getState().settings).toEqual(FALLBACK);
  });

  it("loadFromStorage 沒資料只翻 loaded", () => {
    useWorkspaceSettingsStore.getState().loadFromStorage();
    expect(useWorkspaceSettingsStore.getState().loaded).toBe(true);
    expect(useWorkspaceSettingsStore.getState().settings).toEqual(FALLBACK);
  });

  it("update 持久化並覆蓋", () => {
    useWorkspaceSettingsStore.getState().update({
      defaultBatchSize: 8,
      defaultStrictValidation: true,
    });
    const s = useWorkspaceSettingsStore.getState().settings;
    expect(s.defaultBatchSize).toBe(8);
    expect(s.defaultStrictValidation).toBe(true);
    // 未動的欄位仍是 FALLBACK
    expect(s.defaultModel).toBe(FALLBACK.defaultModel);
    const persisted = JSON.parse(localStorage.getItem(LS_KEY) ?? "{}");
    expect(persisted.defaultBatchSize).toBe(8);
  });

  it("loadFromStorage 從既有資料還原（且補齊缺失欄位）", () => {
    localStorage.setItem(
      LS_KEY,
      JSON.stringify({ defaultBudgetLimit: 25 })
    );
    useWorkspaceSettingsStore.getState().loadFromStorage();
    const s = useWorkspaceSettingsStore.getState().settings;
    expect(s.defaultBudgetLimit).toBe(25);
    // 缺失欄位用 FALLBACK 補齊
    expect(s.defaultModel).toBe(FALLBACK.defaultModel);
  });

  it("reset 還原為 FALLBACK 並寫入", () => {
    useWorkspaceSettingsStore.getState().update({ defaultBudgetLimit: 99 });
    useWorkspaceSettingsStore.getState().reset();
    expect(useWorkspaceSettingsStore.getState().settings).toEqual(FALLBACK);
    const persisted = JSON.parse(localStorage.getItem(LS_KEY) ?? "{}");
    expect(persisted).toEqual(FALLBACK);
  });

  it("loadFromStorage 對壞掉的 JSON 容錯", () => {
    localStorage.setItem(LS_KEY, "{not-json}");
    useWorkspaceSettingsStore.getState().loadFromStorage();
    expect(useWorkspaceSettingsStore.getState().loaded).toBe(true);
    expect(useWorkspaceSettingsStore.getState().settings).toEqual(FALLBACK);
  });
});
