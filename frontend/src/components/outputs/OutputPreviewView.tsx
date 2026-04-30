"use client";

import {
  RiArrowLeftLine,
  RiDownload2Line,
  RiLoader4Line,
} from "@remixicon/react";
import Link from "next/link";
import { useEffect, useState } from "react";

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

          <div className="surface p-2 overflow-x-auto">
            <table className="w-full text-xs">
              <thead>
                <tr className="text-left text-[10px] uppercase tracking-wider text-muted">
                  <th className="font-normal px-3 py-2">TC ID</th>
                  <th className="font-normal px-3 py-2">Req</th>
                  <th className="font-normal px-3 py-2">Test Set</th>
                  <th className="font-normal px-3 py-2">Pre-Conditions</th>
                  <th className="font-normal px-3 py-2">Procedure</th>
                  <th className="font-normal px-3 py-2">Expected</th>
                  <th className="font-normal px-3 py-2">Priority</th>
                </tr>
              </thead>
              <tbody>
                {data.rows.map((row, i) => (
                  <tr key={`${row.tc_id ?? i}`} className="row-hover">
                    <td className="px-3 py-2 align-top text-primary font-bold">
                      {row.tc_id || "—"}
                    </td>
                    <td className="px-3 py-2 align-top text-secondary">
                      {row.reqId || "—"}
                    </td>
                    <td className="px-3 py-2 align-top text-secondary">
                      {row.test_set || "—"}
                    </td>
                    <td className="px-3 py-2 align-top text-secondary max-w-[220px] whitespace-pre-wrap">
                      {row.pre_conditions || "—"}
                    </td>
                    <td className="px-3 py-2 align-top text-secondary max-w-[260px] whitespace-pre-wrap">
                      {row.test_procedure || "—"}
                    </td>
                    <td className="px-3 py-2 align-top text-secondary max-w-[220px] whitespace-pre-wrap">
                      {row.expected_result || "—"}
                    </td>
                    <td className="px-3 py-2 align-top text-secondary">
                      {row.priority || "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}
    </div>
  );
}
