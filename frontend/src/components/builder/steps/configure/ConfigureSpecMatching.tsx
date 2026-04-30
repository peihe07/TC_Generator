"use client";

import { RiLoader4Line, RiRefreshLine } from "@remixicon/react";
import { useEffect, useMemo, useState } from "react";
import { fetchMatchPreview } from "../../../../services/jobAdapter";
import { useJobStore } from "../../../../store/useJobStore";
import type { MatchPreviewState } from "../../../../lib/configurePreviewTypes";
import { Section, StatusPill } from "./shared";

export default function ConfigureSpecMatching({
  defaultOpen = false,
}: {
  defaultOpen?: boolean;
}) {
  const tcRows = useJobStore((s) => s.tcRows);
  const jobMetadata = useJobStore((s) => s.jobMetadata);

  const [preview, setPreview] = useState<MatchPreviewState | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const load = async () => {
    if (!tcRows.length) {
      setPreview(null);
      return;
    }
    setIsLoading(true);
    setError(null);
    try {
      const result = await fetchMatchPreview({
        jobId: jobMetadata?.jobId ?? null,
        rows: tcRows,
      });
      setPreview(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Match request failed.");
    } finally {
      setIsLoading(false);
    }
  };

  // 進入時自動帶一次（與舊行為一致）
  useEffect(() => {
    void load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [jobMetadata?.jobId]);

  const exactRatio = useMemo(() => {
    if (!preview?.summary.total) return 0;
    return Math.round((preview.summary.exact / preview.summary.total) * 100);
  }, [preview]);

  return (
    <Section
      title="Spec Matching"
      hint="Traceability from rows to the optional reference workbook."
      defaultOpen={defaultOpen}
    >
      <div className="space-y-3">
        <div className="flex items-center justify-between gap-3 flex-wrap">
          <div className="text-sm text-secondary">
            {preview ? (
              <>
                Exact: <strong className="text-primary">{preview.summary.exact}</strong>{" "}
                / {preview.summary.total} ({exactRatio}%) · Fuzzy:{" "}
                <strong className="text-primary">{preview.summary.fuzzy}</strong> · Unmatched:{" "}
                <strong className="text-primary">
                  {preview.summary.unmatched}
                </strong>
              </>
            ) : (
              "No preview loaded yet."
            )}
          </div>
          <button
            type="button"
            onClick={() => void load()}
            disabled={isLoading || !tcRows.length}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-bold focus-ring disabled:opacity-40 transition-all"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            {isLoading ? (
              <RiLoader4Line size={12} className="animate-spin" />
            ) : (
              <RiRefreshLine size={12} />
            )}
            Refresh
          </button>
        </div>

        {error && (
          <div
            className="text-sm px-3 py-2 rounded-md"
            style={{
              color: "var(--color-brandy)",
              backgroundColor: "rgba(120, 41, 15, 0.08)",
            }}
          >
            {error}
          </div>
        )}

        {preview && !preview.summary.hasReferenceWorkbook && (
          <div
            className="text-xs px-3 py-2 rounded-md text-secondary"
            style={{ backgroundColor: "rgba(21, 97, 109, 0.08)" }}
          >
            No reference workbook loaded. Upload one in Select Data step to
            enable matching.
          </div>
        )}

        {preview && preview.matches.length > 0 && (
          <div
            className="overflow-y-auto rounded-md"
            style={{
              maxHeight: 320,
              boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.15)",
            }}
          >
            <table className="w-full text-xs">
              <thead className="sticky top-0 z-10">
                <tr
                  className="text-left text-[10px] uppercase tracking-wider text-muted"
                  style={{
                    backgroundColor: "rgba(255, 236, 209, 0.95)",
                    backdropFilter: "blur(8px)",
                  }}
                >
                  <th className="font-normal px-3 py-2 w-28">Req ID</th>
                  <th className="font-normal px-3 py-2">Test Item</th>
                  <th className="font-normal px-3 py-2 w-32">Matched Spec</th>
                  <th className="font-normal px-3 py-2 w-24">Status</th>
                </tr>
              </thead>
              <tbody>
                {preview.matches.map((row) => (
                  <tr key={row.id} className="row-hover">
                    <td className="px-3 py-1.5 text-secondary">{row.reqId}</td>
                    <td
                      className="px-3 py-1.5 text-primary truncate max-w-0"
                      title={row.testItem}
                    >
                      {row.testItem}
                    </td>
                    <td className="px-3 py-1.5 text-secondary truncate">
                      {row.specReference || "—"}
                    </td>
                    <td className="px-3 py-1.5">
                      {row.matchType === "exact" ? (
                        <StatusPill tone="ok">Exact</StatusPill>
                      ) : row.matchType === "fuzzy" ? (
                        <StatusPill tone="warn">
                          Fuzzy{" "}
                          {row.matchScore != null
                            ? `${(row.matchScore * 100).toFixed(0)}%`
                            : ""}
                        </StatusPill>
                      ) : (
                        <span className="text-xs text-muted">Unmatched</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </Section>
  );
}
