import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import OutputsView from "../components/outputs/OutputsView";
import { useJobHistoryStore } from "../store/useJobHistoryStore";

vi.mock("next/link", () => ({
  default: ({ children, href, ...rest }: React.ComponentProps<"a">) => (
    <a href={href as string} {...rest}>
      {children}
    </a>
  ),
}));

vi.mock("next/navigation", () => ({
  usePathname: () => "/outputs",
}));

beforeEach(() => {
  localStorage.clear();
  useJobHistoryStore.setState({ records: [], loaded: false });
});

afterEach(cleanup);

describe("OutputsView", () => {
  it("空時顯示 EmptyState + Start New Run CTA", () => {
    render(<OutputsView />);
    expect(
      screen.getByRole("heading", { level: 3, name: /No outputs yet/ })
    ).toBeInTheDocument();
    expect(
      screen.getByRole("link", { name: /Start New Run/i })
    ).toBeInTheDocument();
  });

  it("選 1 row 時 Compare disabled；選 2 row 時 enable", () => {
    useJobHistoryStore.setState({
      loaded: true,
      records: [
        baseRow("job-1"),
        baseRow("job-2"),
      ],
    });

    render(<OutputsView />);
    const checkboxes = screen.getAllByRole("checkbox");
    // 兩列各一個 select checkbox
    expect(checkboxes.length).toBe(2);

    fireEvent.click(checkboxes[0]);
    const compareLink = screen.getByRole("link", { name: /Compare/ });
    expect(compareLink.getAttribute("aria-disabled")).toBe("true");

    fireEvent.click(checkboxes[1]);
    expect(compareLink.getAttribute("aria-disabled")).toBe("false");
    expect(compareLink.getAttribute("href")).toContain("a=job-1");
    expect(compareLink.getAttribute("href")).toContain("b=job-2");
  });
});

function baseRow(id: string) {
  return {
    id,
    kind: "generate" as const,
    model: "gpt-5",
    startedAt: Date.now() - 5000,
    finishedAt: Date.now(),
    rowsTotal: 5,
    rowsProcessed: 5,
    cost: 0.1,
    inputTokens: 100,
    outputTokens: 200,
    cacheReadTokens: 0,
    cacheCreationTokens: 0,
  };
}
