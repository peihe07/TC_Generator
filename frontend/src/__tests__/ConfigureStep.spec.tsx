import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { cleanup, render, screen, fireEvent } from "@testing-library/react";
import ConfigureStep from "../components/builder/steps/ConfigureStep";
import { useBuilderDraftStore } from "../store/useBuilderDraftStore";
import { useJobStore } from "../store/useJobStore";
import type { TcRow } from "../lib/types";

// jobAdapter SpecMatching 在 mount 時會 fetch；mock 掉避免網路呼叫
vi.mock("../services/jobAdapter", async (orig) => {
  const real = await orig<typeof import("../services/jobAdapter")>();
  return {
    ...real,
    fetchMatchPreview: vi.fn().mockResolvedValue({
      summary: {
        total: 0,
        exact: 0,
        fuzzy: 0,
        unmatched: 0,
        hasReferenceWorkbook: false,
      },
      matches: [],
    }),
    fetchGroupingPreview: vi.fn(),
  };
});

const baseRow = (id: string): TcRow => ({
  id,
  reqId: `REQ-${id}`,
  testGroup: "G",
  testSet: "Alpha",
  testItem: `Item ${id}`,
  preConditions: "",
  inputTestData: "",
  steps: "",
  expectedResults: "",
  status: "pending",
});

beforeEach(() => {
  localStorage.clear();
  useJobStore.setState({
    jobMetadata: { jobId: "j1", projectName: "P", createdAt: "2026-04-29", totalRows: 2 },
    tcRows: [baseRow("r1"), baseRow("r2")],
    config: {
      model: "gpt-5",
      batchSize: 5,
      budgetLimit: 10,
      creditBalance: 0,
      strictValidation: false,
      targetColumns: ["preConditions", "steps"],
    },
  });
  useBuilderDraftStore.setState({
    loaded: true,
    draft: {
      id: "draft_1",
      createdAt: 1,
      updatedAt: 1,
      currentStep: "configure",
      completed: {},
    },
  });
});

afterEach(cleanup);

describe("ConfigureStep", () => {
  it("renders 三個區段 + summary 反映目前 config", () => {
    render(<ConfigureStep />);
    expect(screen.getByText("Configure Rules")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /Options/ })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /Grouping/ })).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /Spec Matching/ })
    ).toBeInTheDocument();
    // Summary
    expect(screen.getByText("Rows loaded")).toBeInTheDocument();
    // Strict mode default off
    expect(screen.getByText("Off")).toBeInTheDocument();
    // 2 rows 可能在 row count + batchSize 都出現，至少一個
    expect(screen.getAllByText("2").length).toBeGreaterThan(0);
  });

  it("mount 後 markStepComplete('configure', true)", () => {
    render(<ConfigureStep />);
    expect(
      useBuilderDraftStore.getState().draft?.completed?.configure
    ).toBe(true);
  });

  it("Strict toggle 切換更新 config", () => {
    render(<ConfigureStep />);
    // 整個 Configure step 只有一個 toggle (Strict)
    const toggle = screen.getByRole("switch");
    fireEvent.click(toggle);
    expect(useJobStore.getState().config.strictValidation).toBe(true);
  });
});
