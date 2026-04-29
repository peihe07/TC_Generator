import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { cleanup, render, screen, fireEvent } from "@testing-library/react";
import ReviewStep from "../components/builder/steps/ReviewStep";
import { useBuilderDraftStore } from "../store/useBuilderDraftStore";
import { useJobStore } from "../store/useJobStore";
import type { TcRow } from "../lib/types";

vi.mock("next/link", () => ({
  default: ({ children, href, ...rest }: React.ComponentProps<"a">) => (
    <a href={href as string} {...rest}>
      {children}
    </a>
  ),
}));

const baseRow = (id: string, overrides: Partial<TcRow> = {}): TcRow => ({
  id,
  reqId: `REQ-${id}`,
  testGroup: "G",
  testSet: "Alpha",
  testItem: `Item ${id}`,
  tcTitle: `TC ${id}`,
  preConditions: "",
  inputTestData: "",
  steps: "",
  expectedResults: "",
  status: "success",
  ...overrides,
});

beforeEach(() => {
  localStorage.clear();
  useBuilderDraftStore.setState({
    loaded: true,
    draft: {
      id: "draft_1",
      createdAt: 1,
      updatedAt: 1,
      currentStep: "review",
      completed: {},
    },
  });
  useJobStore.setState({
    jobMetadata: { jobId: "j1", projectName: "P", createdAt: "2026-04-29", totalRows: 0 },
    tcRows: [],
    config: {
      model: "gpt-5",
      batchSize: 5,
      budgetLimit: 10,
      creditBalance: 0,
      strictValidation: false,
      targetColumns: ["preConditions", "steps"],
    },
  });
});

afterEach(cleanup);

describe("ReviewStep", () => {
  it("無 row 時 prompt 使用者去 Execute", () => {
    render(<ReviewStep />);
    expect(
      screen.getByText(/No rows to review/i)
    ).toBeInTheDocument();
  });

  it("有 rows 時顯示 filter pills 與 row list", () => {
    useJobStore.setState({
      tcRows: [
        baseRow("r1", {
          validationErrors: [{ severity: "error", message: "missing steps" }],
        }),
        baseRow("r2", {
          validationErrors: [
            { severity: "warning", message: "soft warning" },
          ],
        }),
        baseRow("r3"),
      ],
    });
    render(<ReviewStep />);

    expect(screen.getByRole("button", { name: /All \(3\)/ })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /Errors \(1\)/ })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /Warnings \(1\)/ })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /OK \(1\)/ })).toBeInTheDocument();
    // 三列都在
    expect(screen.getByText(/REQ-r1.*TC r1/)).toBeInTheDocument();
    expect(screen.getByText(/REQ-r2.*TC r2/)).toBeInTheDocument();
    expect(screen.getByText(/REQ-r3.*TC r3/)).toBeInTheDocument();
  });

  it("Errors filter 只留下 error 列", () => {
    useJobStore.setState({
      tcRows: [
        baseRow("r1", {
          validationErrors: [{ severity: "error", message: "boom" }],
        }),
        baseRow("r2"),
      ],
    });
    render(<ReviewStep />);

    fireEvent.click(screen.getByRole("button", { name: /Errors \(1\)/ }));
    // 用 button accessible name 鎖定 row list 裡的列（避免命中 detail panel 的 reqId）
    expect(
      screen.getByRole("button", { name: /REQ-r1/ })
    ).toBeInTheDocument();
    expect(
      screen.queryByRole("button", { name: /REQ-r2/ })
    ).not.toBeInTheDocument();
  });

  it("有 rows 時 mount 即 markStepComplete review=true", () => {
    useJobStore.setState({
      tcRows: [baseRow("r1")],
    });
    render(<ReviewStep />);
    expect(
      useBuilderDraftStore.getState().draft?.completed?.review
    ).toBe(true);
  });

  it("Bulk select all 顯示 selected count", () => {
    useJobStore.setState({
      tcRows: [baseRow("r1"), baseRow("r2")],
    });
    render(<ReviewStep />);

    // header bulk checkbox（label='Select all visible rows'）
    const selectAll = screen.getByRole("checkbox", {
      name: /Select all visible rows/,
    });
    fireEvent.click(selectAll);
    // Bulk toolbox 出現（用 toolbox 內的 Delete 按鈕辨識；row list 沒這顆按鈕）
    expect(
      screen.getByRole("button", { name: /^Delete$/ })
    ).toBeInTheDocument();
    // 兩處都顯示 "2 selected"（header + toolbox）
    expect(screen.getAllByText(/2 selected/).length).toBeGreaterThanOrEqual(2);
  });
});
