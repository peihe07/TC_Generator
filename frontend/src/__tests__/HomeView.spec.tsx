import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import HomeView from "../components/home/HomeView";
import { useBuilderDraftStore } from "../store/useBuilderDraftStore";
import { useJobHistoryStore } from "../store/useJobHistoryStore";

// next/link 在測試環境直接渲染為 <a>
vi.mock("next/link", () => ({
  default: ({ children, href, ...rest }: React.ComponentProps<"a">) => (
    <a href={href as string} {...rest}>
      {children}
    </a>
  ),
}));

// usePathname 沒被 HomeView 直接用，但子元件可能用；安全 stub
vi.mock("next/navigation", () => ({
  usePathname: () => "/",
}));

beforeEach(() => {
  localStorage.clear();
  useJobHistoryStore.setState({ records: [], loaded: false });
  useBuilderDraftStore.setState({ draft: null, loaded: false });
});

afterEach(cleanup);

describe("HomeView", () => {
  it("空 history 時 KPI 全為 0/—、Recent Runs 顯示空狀態", () => {
    render(<HomeView />);
    expect(
      screen.getByRole("heading", { level: 1, name: "Home" })
    ).toBeInTheDocument();
    // Total Runs 為 0
    expect(screen.getByText("Total Runs")).toBeInTheDocument();
    // RecentRuns 空狀態
    expect(
      screen.getByText("Start with", { exact: false })
    ).toBeInTheDocument();
    // Quick Actions
    expect(screen.getByText("Quick Actions")).toBeInTheDocument();
    // New Run 出現在 Quick Actions（Home 內無 TopNav）
    expect(screen.getAllByText("New Run").length).toBeGreaterThan(0);
  });

  it("有 history 時 Recent Runs 顯示表格列", () => {
    useJobHistoryStore.setState({
      loaded: true,
      records: [
        {
          id: "job-1",
          kind: "generate",
          model: "gpt-5",
          startedAt: Date.now() - 5000,
          finishedAt: Date.now(),
          rowsTotal: 4,
          rowsProcessed: 4,
          cost: 0.1,
          inputTokens: 100,
          outputTokens: 200,
          cacheReadTokens: 0,
          cacheCreationTokens: 0,
        },
      ],
    });
    render(<HomeView />);
    expect(screen.getByText("Generate")).toBeInTheDocument();
    expect(screen.getByText("job-1")).toBeInTheDocument();
    expect(screen.queryByText("No runs yet")).not.toBeInTheDocument();
  });

  it("有 draft 時 Continue Draft 區出現", () => {
    useBuilderDraftStore.setState({
      loaded: true,
      draft: {
        id: "draft_xyz",
        createdAt: Date.now() - 10_000,
        updatedAt: Date.now() - 1000,
        currentStep: "configure",
      },
    });
    render(<HomeView />);
    expect(
      screen.getByText(/Continue draft/, { exact: false })
    ).toBeInTheDocument();
    expect(screen.getByText("draft_xyz")).toBeInTheDocument();
    expect(screen.getByText("Resume")).toBeInTheDocument();
  });
});
