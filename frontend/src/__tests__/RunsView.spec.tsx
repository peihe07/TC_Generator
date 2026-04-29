import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import RunsView from "../components/runs/RunsView";
import { useJobHistoryStore } from "../store/useJobHistoryStore";

vi.mock("next/link", () => ({
  default: ({ children, href, ...rest }: React.ComponentProps<"a">) => (
    <a href={href as string} {...rest}>
      {children}
    </a>
  ),
}));

const mockReplace = vi.fn();
let searchParamsValue = new URLSearchParams();
vi.mock("next/navigation", () => ({
  useRouter: () => ({ replace: mockReplace, push: vi.fn() }),
  useSearchParams: () => searchParamsValue,
  usePathname: () => "/runs",
}));

beforeEach(() => {
  mockReplace.mockClear();
  searchParamsValue = new URLSearchParams();
  localStorage.clear();
  useJobHistoryStore.setState({ records: [], loaded: false });
});

afterEach(cleanup);

const seed = (
  partial: Partial<Parameters<typeof useJobHistoryStore.getState>[0]> = {}
) => {
  void partial;
};

describe("RunsView", () => {
  it("空 history 時顯示空狀態 + 0 of 0 runs", () => {
    render(<RunsView />);
    expect(
      screen.getByRole("heading", { level: 1, name: "Runs" })
    ).toBeInTheDocument();
    expect(
      screen.getByText("0 of 0 runs", { exact: false })
    ).toBeInTheDocument();
  });

  it("有 history 時表格顯示列；filter pill 點擊更新 URL", () => {
    useJobHistoryStore.setState({
      loaded: true,
      records: [
        {
          id: "job-A",
          kind: "generate",
          model: "gpt-5",
          startedAt: Date.now() - 5000,
          finishedAt: Date.now(),
          rowsTotal: 4,
          rowsProcessed: 4,
          cost: 0.2,
          inputTokens: 100,
          outputTokens: 200,
          cacheReadTokens: 0,
          cacheCreationTokens: 0,
        },
        {
          id: "job-B",
          kind: "rerun",
          model: "gpt-5.4",
          startedAt: Date.now() - 4000,
          finishedAt: Date.now(),
          rowsTotal: 0, // 預期 status='completed' 因為 total=0 不會落入 partial/failed 分支
          rowsProcessed: 0,
          cost: 0.5,
          inputTokens: 50,
          outputTokens: 100,
          cacheReadTokens: 0,
          cacheCreationTokens: 0,
        },
      ],
    });

    render(<RunsView />);
    expect(screen.getByText("job-A")).toBeInTheDocument();
    expect(screen.getByText("job-B")).toBeInTheDocument();

    // Filter pill: Failed (從 0 開始 → 沒人是 failed)
    fireEvent.click(screen.getByRole("button", { name: /^Failed$/ }));
    expect(mockReplace).toHaveBeenCalled();
    const lastCall = mockReplace.mock.calls.at(-1)?.[0] as string;
    expect(lastCall).toContain("status=failed");
  });
});

// keep tsc happy: seed unused but typed
void seed;
