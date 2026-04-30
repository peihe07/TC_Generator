import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  cleanup,
  fireEvent,
  render,
  screen,
} from "@testing-library/react";
import WorkspaceSwitcher from "../components/shell/WorkspaceSwitcher";
import {
  DEFAULT_WORKSPACE_ID,
  useWorkspaceStore,
} from "../store/useWorkspaceStore";

beforeEach(() => {
  localStorage.clear();
  useWorkspaceStore.setState({
    workspaces: [
      { id: DEFAULT_WORKSPACE_ID, name: "Default", createdAt: 0 },
    ],
    currentId: DEFAULT_WORKSPACE_ID,
    loaded: true,
  });
});

afterEach(() => {
  cleanup();
  vi.restoreAllMocks();
});

describe("WorkspaceSwitcher", () => {
  it("顯示當前 workspace 名稱", () => {
    render(<WorkspaceSwitcher />);
    expect(screen.getByText("Default")).toBeInTheDocument();
  });

  it("展開後列出 workspaces 並可切換", () => {
    // 從 Default 開始，建一個新的（會自動切過去），點 trigger 開 dropdown，再點 Default 切回去
    useWorkspaceStore.getState().createWorkspace("Project Alpha");
    expect(useWorkspaceStore.getState().currentId).not.toBe(
      DEFAULT_WORKSPACE_ID,
    );

    render(<WorkspaceSwitcher />);
    // Trigger button 顯示當前 workspace 名稱（Project Alpha）
    fireEvent.click(screen.getByText("Project Alpha"));
    // Dropdown 中的 Default 列項
    fireEvent.click(screen.getByText("Default"));
    expect(useWorkspaceStore.getState().currentId).toBe(
      DEFAULT_WORKSPACE_ID,
    );
  });

  it("New workspace 表單建立並切過去", () => {
    render(<WorkspaceSwitcher />);
    fireEvent.click(screen.getByText("Default"));
    fireEvent.click(screen.getByText("New workspace"));
    fireEvent.change(screen.getByPlaceholderText("Workspace name"), {
      target: { value: "Beta" },
    });
    fireEvent.click(screen.getByText("Create"));
    const state = useWorkspaceStore.getState();
    expect(state.workspaces.find((w) => w.name === "Beta")).toBeDefined();
    expect(
      state.workspaces.find((w) => w.id === state.currentId)?.name,
    ).toBe("Beta");
  });

  it("Remove 按鈕只在 >1 workspace 時出現", () => {
    render(<WorkspaceSwitcher />);
    fireEvent.click(screen.getByText("Default"));
    expect(
      screen.queryByLabelText(/Remove workspace/),
    ).not.toBeInTheDocument();
  });

  it("有多個 workspace 時可移除非當前 entry", () => {
    useWorkspaceStore.getState().createWorkspace("Beta");
    // currentId 變為 Beta；切回 Default 確保 remove 不是 self
    useWorkspaceStore.getState().switchWorkspace(DEFAULT_WORKSPACE_ID);
    vi.spyOn(window, "confirm").mockReturnValue(true);

    render(<WorkspaceSwitcher />);
    fireEvent.click(screen.getByText("Default"));
    const removeButtons = screen.getAllByLabelText(/Remove workspace/);
    // 找名為 Beta 的那個 remove 按鈕
    const betaRemove = removeButtons.find((btn) =>
      btn.getAttribute("aria-label")?.includes("Beta"),
    );
    expect(betaRemove).toBeDefined();
    if (betaRemove) fireEvent.click(betaRemove);

    expect(
      useWorkspaceStore.getState().workspaces.find((w) => w.name === "Beta"),
    ).toBeUndefined();
  });
});
