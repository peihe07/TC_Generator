"use client";

import {
  RiArrowLeftLine,
  RiDownload2Line,
  RiLoader4Line,
} from "@remixicon/react";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import DataTable, { type DataTableColumn } from "../ui/DataTable";

interface PreviewRow {
  reqId?: string | null;
  tc_id?: string | null;
  test_set?: string | null;
  pre_conditions?: string | null;
  input_test_data?: string | null;
  test_procedure?: string | null;
  expected_result?: string | null;
  priority?: string | null;
  design_method?: string | null;
}

interface PreviewResponse {
  jobId: string;
  fileName: string;
  totalRows: number;
  limit: number;
  rows: PreviewRow[];
}

export default function OutputPreviewView({ runId }: { runId: string }) {
  const [data, setData] = useState<PreviewResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetch(`/api/jobs/${encodeURIComponent(runId)}/output-preview`)
      .then(async (res) => {
        if (!res.ok) {
          const body = await res.json().catch(() => ({}));
          throw new Error(body.detail ?? `Status ${res.status}`);
        }
        return (await res.json()) as PreviewResponse;
      })
      .then((d) => {
        if (!cancelled) setData(d);
      })
      .catch((err) => {
        if (!cancelled)
          setError(err instanceof Error ? err.message : "Preview failed");
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [runId]);

  return (
    <div className="space-y-6">
      <Link
        href="/outputs"
        className="inline-flex items-center gap-1.5 text-sm text-secondary hover:text-primary focus-ring rounded"
      >
        <RiArrowLeftLine size={16} />
        Back to outputs
      </Link>

      <header className="flex items-end justify-between gap-3 flex-wrap">
        <div className="space-y-1">
          <h1 className="text-3xl font-bold text-primary">Output Preview</h1>
          <code className="text-xs text-muted">{runId}</code>
        </div>
        <a
          href={`/api/export/download/${encodeURIComponent(runId)}`}
          className="cta inline-flex items-center gap-1.5 text-sm"
        >
          <RiDownload2Line size={16} />
          Download xlsx
        </a>
      </header>

      {loading && (
        <div className="surface p-6 flex items-center gap-2 text-sm text-secondary">
          <RiLoader4Line size={14} className="animate-spin" />
          Loading workbook…
        </div>
      )}

      {error && (
        <div
          className="surface p-4 text-sm"
          style={{ color: "var(--color-brandy)" }}
        >
          {error}
        </div>
      )}

      {data && (
        <>
          <div className="surface px-4 py-3 text-xs text-secondary flex items-center gap-3 flex-wrap">
            <span>
              <strong className="text-primary">{data.fileName}</strong>
            </span>
            <span className="text-muted">·</span>
            <span>
              Showing {data.rows.length} of {data.totalRows} TCs
              {data.totalRows > data.rows.length
                ? ` (capped at ${data.limit})`
                : ""}
            </span>
          </div>

          <PreviewTable rows={data.rows} />
        </>
      )}
    </div>
  );
}

function PreviewTable({ rows }: { rows: PreviewRow[] }) {
  const columns = useMemo<DataTableColumn<PreviewRow>[]>(
    () => [
      {
        id: "tc_id",
        header: "TC ID",
        sortBy: (r) => r.tc_id ?? "",
        cell: (r) => (
          <span className="text-primary font-bold align-top">
            {r.tc_id || "—"}
          </span>
        ),
      },
      {
        id: "reqId",
        header: "Req",
        sortBy: (r) => r.reqId ?? "",
        cell: (r) => (
          <span className="text-secondary align-top">{r.reqId || "—"}</span>
        ),
      },
      {
        id: "test_set",
        header: "Test Set",
        sortBy: (r) => r.test_set ?? "",
        cell: (r) => (
          <span className="text-secondary align-top">
            {r.test_set || "—"}
          </span>
        ),
      },
      {
        id: "pre",
        header: "Pre-Conditions",
        cell: (r) => (
          <span
            className="text-secondary align-top whitespace-pre-wrap"
            style={{ display: "block", maxWidth: 220 }}
          >
            {r.pre_conditions || "—"}
          </span>
        ),
      },
      {
        id: "proc",
        header: "Procedure",
        cell: (r) => (
          <span
            className="text-secondary align-top whitespace-pre-wrap"
            style={{ display: "block", maxWidth: 260 }}
          >
            {r.test_procedure || "—"}
          </span>
        ),
      },
      {
        id: "expected",
        header: "Expected",
        cell: (r) => (
          <span
            className="text-secondary align-top whitespace-pre-wrap"
            style={{ display: "block", maxWidth: 220 }}
          >
            {r.expected_result || "—"}
          </span>
        ),
      },
      {
        id: "priority",
        header: "Priority",
        cell: (r) => (
          <span className="text-secondary align-top">
            {r.priority || "—"}
          </span>
        ),
      },
    ],
    [],
  );

  return (
    <DataTable
      rows={rows}
      columns={columns}
      rowKey={(r, i) => r.tc_id ?? `row-${i}`}
    />
  );
}
