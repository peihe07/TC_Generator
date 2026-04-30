import { afterEach, beforeEach, describe, expect, it } from "vitest";
import {
  DEFAULT_WORKSPACE_ID,
  useWorkspaceStore,
} from "../store/useWorkspaceStore";

const LS_KEY = "tc-generator-workspaces";

function reset() {
  localStorage.clear();
  useWorkspaceStore.setState({
    workspaces: [
      { id: DEFAULT_WORKSPACE_ID, name: "Default", createdAt: 0 },
    ],
    currentId: DEFAULT_WORKSPACE_ID,
    loaded: false,
  });
}

beforeEach(reset);
afterEach(reset);

describe("useWorkspaceStore", () => {
  it("loadFromStorage 沒資料時 seed default workspace 並 persist", () => {
    useWorkspaceStore.getState().loadFromStorage();
    const s = useWorkspaceStore.getState();
    expect(s.loaded).toBe(true);
    expect(s.workspaces).toHaveLength(1);
    expect(s.currentId).toBe(DEFAULT_WORKSPACE_ID);
    const persisted = JSON.parse(localStorage.getItem(LS_KEY) ?? "{}");
    expect(persisted.workspaces).toHaveLength(1);
  });

  it("createWorkspace 自動切到新 workspace", () => {
    useWorkspaceStore.getState().loadFromStorage();
    const ws = useWorkspaceStore.getState().createWorkspace("Project Alpha");
    expect(ws.name).toBe("Project Alpha");
    expect(useWorkspaceStore.getState().currentId).toBe(ws.id);
    expect(useWorkspaceStore.getState().workspaces).toHaveLength(2);
  });

  it("switchWorkspace 換到既有 workspace", () => {
    useWorkspaceStore.getState().loadFromStorage();
    const ws = useWorkspaceStore.getState().createWorkspace("Beta");
    useWorkspaceStore.getState().switchWorkspace(DEFAULT_WORKSPACE_ID);
    expect(useWorkspaceStore.getState().currentId).toBe(DEFAULT_WORKSPACE_ID);
    useWorkspaceStore.getState().switchWorkspace(ws.id);
    expect(useWorkspaceStore.getState().currentId).toBe(ws.id);
  });

  it("removeWorkspace 不允許刪到只剩 0 個", () => {
    useWorkspaceStore.getState().loadFromStorage();
    useWorkspaceStore.getState().removeWorkspace(DEFAULT_WORKSPACE_ID);
    expect(useWorkspaceStore.getState().workspaces).toHaveLength(1);
  });

  it("removeWorkspace 移除當前 workspace 時跳到第一個", () => {
    useWorkspaceStore.getState().loadFromStorage();
    const a = useWorkspaceStore.getState().createWorkspace("A");
    useWorkspaceStore.getState().createWorkspace("B");
    useWorkspaceStore.getState().switchWorkspace(a.id);
    useWorkspaceStore.getState().removeWorkspace(a.id);
    const remaining = useWorkspaceStore.getState().workspaces.map((w) => w.id);
    expect(remaining).not.toContain(a.id);
    expect(useWorkspaceStore.getState().currentId).toBe(remaining[0]);
  });

  it("renameWorkspace 改名持久化", () => {
    useWorkspaceStore.getState().loadFromStorage();
    useWorkspaceStore.getState().renameWorkspace(DEFAULT_WORKSPACE_ID, "Workspace X");
    expect(
      useWorkspaceStore.getState().workspaces[0].name
    ).toBe("Workspace X");
    const persisted = JSON.parse(localStorage.getItem(LS_KEY) ?? "{}");
    expect(persisted.workspaces[0].name).toBe("Workspace X");
  });

  it("loadFromStorage 對壞掉 currentId fallback 到第一個", () => {
    localStorage.setItem(
      LS_KEY,
      JSON.stringify({
        workspaces: [
          { id: "ws-1", name: "First", createdAt: 1 },
          { id: "ws-2", name: "Second", createdAt: 2 },
        ],
        currentId: "non-existent",
      })
    );
    useWorkspaceStore.getState().loadFromStorage();
    expect(useWorkspaceStore.getState().currentId).toBe("ws-1");
  });
});
