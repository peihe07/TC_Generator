import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { cleanup, render, screen, waitFor } from "@testing-library/react";
import OutputPreviewView from "../components/outputs/OutputPreviewView";

vi.mock("next/link", () => ({
  default: ({ children, href, ...rest }: React.ComponentProps<"a">) => (
    <a href={href as string} {...rest}>
      {children}
    </a>
  ),
}));

beforeEach(() => {
  vi.restoreAllMocks();
});

afterEach(cleanup);

describe("OutputPreviewView", () => {
  it("成功時渲染 row 表格與 metadata", async () => {
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          jobId: "job-1",
          fileName: "preview.xlsx",
          totalRows: 2,
          limit: 200,
          rows: [
            {
              tc_id: "T-001",
              reqId: "REQ-1",
              test_set: "Set A",
              pre_conditions: "pre",
              test_procedure: "step",
              expected_result: "ok",
              priority: "P1",
            },
            {
              tc_id: "T-002",
              reqId: "REQ-2",
              test_set: "Set A",
              pre_conditions: "",
              test_procedure: "",
              expected_result: "",
              priority: "",
            },
          ],
        }),
        { status: 200, headers: { "Content-Type": "application/json" } }
      )
    );
    vi.stubGlobal("fetch", fetchMock);

    render(<OutputPreviewView runId="job-1" />);

    await waitFor(() => {
      expect(screen.getByText("T-001")).toBeInTheDocument();
    });
    expect(screen.getByText("T-002")).toBeInTheDocument();
    expect(screen.getByText("preview.xlsx")).toBeInTheDocument();
    expect(
      screen.getByText(/Showing 2 of 2 TCs/)
    ).toBeInTheDocument();
    expect(fetchMock).toHaveBeenCalledWith(
      "/api/jobs/job-1/output-preview"
    );
  });

  it("409 時顯示錯誤訊息", async () => {
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({ detail: "no exported workbook (run Export first)" }),
        { status: 409, headers: { "Content-Type": "application/json" } }
      )
    );
    vi.stubGlobal("fetch", fetchMock);

    render(<OutputPreviewView runId="job-no-export" />);

    await waitFor(() => {
      expect(
        screen.getByText(/no exported workbook/)
      ).toBeInTheDocument();
    });
  });

  it("超過 limit 時顯示 'capped at N'", async () => {
    const fetchMock = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          jobId: "job-big",
          fileName: "big.xlsx",
          totalRows: 500,
          limit: 200,
          rows: Array.from({ length: 200 }).map((_, i) => ({
            tc_id: `T-${i.toString().padStart(3, "0")}`,
            reqId: `REQ-${i}`,
          })),
        }),
        { status: 200, headers: { "Content-Type": "application/json" } }
      )
    );
    vi.stubGlobal("fetch", fetchMock);

    render(<OutputPreviewView runId="job-big" />);

    await waitFor(() => {
      expect(
        screen.getByText(/capped at 200/)
      ).toBeInTheDocument();
    });
    expect(
      screen.getByText(/Showing 200 of 500 TCs/)
    ).toBeInTheDocument();
  });
});
