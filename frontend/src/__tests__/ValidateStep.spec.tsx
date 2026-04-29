import { afterEach, beforeEach, describe, expect, it } from "vitest";
import { cleanup, render, screen } from "@testing-library/react";
import ValidateStep from "../components/builder/steps/ValidateStep";
import { useBuilderDraftStore } from "../store/useBuilderDraftStore";
import { useJobStore } from "../store/useJobStore";
import type { TcRow } from "../lib/types";

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
  useBuilderDraftStore.setState({
    loaded: true,
    draft: {
      id: "draft_1",
      createdAt: 1,
      updatedAt: 1,
      currentStep: "validate",
      completed: {},
    },
  });
});

afterEach(cleanup);

describe("ValidateStep", () => {
  it("無 row 時 Dataset loaded 為 fail (blocking) → markStepComplete validate=false", () => {
    useJobStore.setState({
      jobMetadata: null,
      tcRows: [],
      config: {
        model: "gpt-5",
        batchSize: 5,
        budgetLimit: 10,
        creditBalance: 0,
        strictValidation: false,
        targetColumns: ["preConditions"],
      },
    });
    render(<ValidateStep />);

    expect(screen.getByText("Dataset loaded")).toBeInTheDocument();
    // critical issue banner
    expect(
      screen.getByText(/critical issue/, { exact: false })
    ).toBeInTheDocument();
    // Validate step 標記為 false
    expect(
      useBuilderDraftStore.getState().draft?.completed?.validate
    ).toBe(false);
  });

  it("有 rows + target columns 時所有 critical 都過 → markStepComplete=true", () => {
    useJobStore.setState({
      jobMetadata: { jobId: "j1", projectName: "P", createdAt: "2026-04-29", totalRows: 1 },
      tcRows: [{ ...baseRow("r1"), testSet: "Alpha" }],
      config: {
        model: "gpt-5",
        batchSize: 5,
        budgetLimit: 10,
        creditBalance: 0,
        strictValidation: false,
        targetColumns: ["preConditions", "steps"],
      },
    });
    render(<ValidateStep />);

    // 沒有 critical issue banner
    expect(
      screen.queryByText(/critical issue/, { exact: false })
    ).not.toBeInTheDocument();
    expect(
      useBuilderDraftStore.getState().draft?.completed?.validate
    ).toBe(true);
  });

  it("缺 target columns 時 critical fail (blocking)", () => {
    useJobStore.setState({
      jobMetadata: { jobId: "j1", projectName: "P", createdAt: "2026-04-29", totalRows: 1 },
      tcRows: [baseRow("r1")],
      config: {
        model: "gpt-5",
        batchSize: 5,
        budgetLimit: 10,
        creditBalance: 0,
        strictValidation: false,
        targetColumns: [],
      },
    });
    render(<ValidateStep />);

    expect(screen.getByText("Target columns")).toBeInTheDocument();
    expect(
      useBuilderDraftStore.getState().draft?.completed?.validate
    ).toBe(false);
  });
});
