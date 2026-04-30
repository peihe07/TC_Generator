"use client";

import {
  RiDownload2Line,
  RiArrowLeftRightLine,
  RiInboxLine,
} from "@remixicon/react";
import Link from "next/link";
import EmptyState from "../shell/EmptyState";
import { useMemo, useState } from "react";
import { track } from "../../lib/telemetry";
import {
  formatCost,
  formatDuration,
  formatRelativeTime,
  STATUS_COLOR,
  STATUS_LABEL,
  toRuns,
  type Run,
} from "../../services/runAdapter";
import { useWorkspaceFilteredRecords } from "../../lib/useWorkspaceFiltered";

const OUTPUT_KINDS = new Set(["generate", "quick", "rerun", "regenerate"]);

export default function OutputsView() {
  const records = useWorkspaceFilteredRecords();

  const outputs = useMemo<Run[]>(() => {
    return toRuns(records).filter(
      (r) => OUTPUT_KINDS.has(r.kind) && r.status !== "running"
    );
  }, [records]);

  const [selected, setSelected] = useState<string[]>([]);

  const toggleSelect = (id: string) => {
    setSelected((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]
    );
  };

  const [bulkLoading, setBulkLoading] = useState(false);
  const [bulkError, setBulkError] = useState<string | null>(null);

  const downloadBulk = async () => {
    if (selected.length === 0) return;
    setBulkLoading(true);
    setBulkError(null);
    try {
      const res = await fetch("/api/outputs/bulk-download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ jobIds: selected }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail ?? `Status ${res.status}`);
      }
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download =
        res.headers
          .get("content-disposition")
          ?.match(/filename="?([^";]+)"?/)?.[1] ?? "tc-outputs-bundle.zip";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    } catch (err) {
      setBulkError(err instanceof Error ? err.message : "Download failed");
    } finally {
      setBulkLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <header className="flex items-end justify-between gap-3 flex-wrap">
        <div className="space-y-1">
          <h1 className="text-3xl font-bold text-primary">Outputs</h1>
          <p className="text-secondary text-sm">
            Output management and iterative quality checks.
          </p>
        </div>
        <span className="text-xs text-muted">{outputs.length} outputs</span>
      </header>

      {outputs.length === 0 ? (
        <EmptyState
          Icon={RiInboxLine}
          title="No outputs yet"
          description="Outputs appear after a run completes."
          action={{ label: "Start New Run", href: "/run-builder" }}
        />
      ) : (
        <div className="surface p-2 overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="text-left text-xs uppercase tracking-wider text-muted">
                <th className="font-normal px-3 py-2 w-8" aria-label="select" />
                <th className="font-normal px-3 py-2">Output</th>
                <th className="font-normal px-3 py-2">Status</th>
                <th className="font-normal px-3 py-2">Duration</th>
                <th className="font-normal px-3 py-2">Cost</th>
                <th className="font-normal px-3 py-2">Completed</th>
                <th className="font-normal px-3 py-2 text-right">Actions</th>
              </tr>
            </thead>
            <tbody>
              {outputs.map((r) => (
                <tr key={r.id} className="row-hover">
                  <td className="px-3 py-2.5">
                    <input
                      type="checkbox"
                      checked={selected.includes(r.id)}
                      onChange={() => toggleSelect(r.id)}
                      aria-label={`Select ${r.id}`}
                    />
                  </td>
                  <td className="px-3 py-2.5">
                    <Link
                      href={`/runs/${r.id}`}
                      className="text-primary font-bold hover:underline"
                    >
                      {r.kindLabel}
                    </Link>
                    <div className="text-xs text-muted truncate max-w-[260px]">
                      {r.id}
                    </div>
                  </td>
                  <td className="px-3 py-2.5">
                    <span
                      className="inline-flex items-center gap-1.5 text-xs font-bold"
                      style={{ color: STATUS_COLOR[r.status] }}
                    >
                      <span
                        className="inline-block w-1.5 h-1.5 rounded-full"
                        style={{ backgroundColor: STATUS_COLOR[r.status] }}
                      />
                      {STATUS_LABEL[r.status]}
                    </span>
                  </td>
                  <td className="px-3 py-2.5 text-secondary">
                    {formatDuration(r.durationMs)}
                  </td>
                  <td className="px-3 py-2.5 text-secondary">
                    {formatCost(r.cost)}
                  </td>
                  <td className="px-3 py-2.5 text-muted text-xs">
                    {r.finishedAt ? formatRelativeTime(r.finishedAt) : "—"}
                  </td>
                  <td className="px-3 py-2.5 text-right">
                    <div className="inline-flex items-center gap-2">
                      <Link
                        href={`/outputs/${encodeURIComponent(r.id)}`}
                        className="text-xs font-bold focus-ring rounded px-2 py-1"
                        style={{ color: "var(--color-tangerine)" }}
                      >
                        Preview
                      </Link>
                      <a
                        href={`/api/export/download/${encodeURIComponent(r.id)}`}
                        className="inline-flex items-center gap-1 text-xs font-bold focus-ring rounded px-2 py-1 text-secondary"
                      >
                        <RiDownload2Line size={12} />
                        Download
                      </a>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {selected.length > 0 && (
        <div
          className="sticky bottom-4 surface-floating px-5 py-3 space-y-2"
          style={{ borderRadius: 16 }}
        >
          <div className="flex items-center justify-between gap-3 flex-wrap">
            <span className="text-sm text-secondary">
              {selected.length === 2
                ? "2 outputs selected — ready to compare"
                : `${selected.length} selected`}
            </span>
            <div className="flex items-center gap-2 flex-wrap">
              <button
                type="button"
                onClick={() => setSelected([])}
                className="text-xs px-3 py-1.5 rounded-md focus-ring"
                style={{
                  backgroundColor: "rgba(21, 97, 109, 0.12)",
                  color: "var(--color-teal)",
                }}
              >
                Clear
              </button>
              <button
                type="button"
                onClick={() => void downloadBulk()}
                disabled={bulkLoading}
                className="inline-flex items-center gap-1.5 text-sm px-3 py-1.5 rounded-md font-bold focus-ring disabled:opacity-40"
                style={{
                  backgroundColor: "rgba(21, 97, 109, 0.12)",
                  color: "var(--color-teal)",
                }}
              >
                <RiDownload2Line size={14} />
                {bulkLoading ? "Bundling…" : "Download zip"}
              </button>
              <Link
                href={`/outputs/compare?a=${encodeURIComponent(
                  selected[0]
                )}&b=${encodeURIComponent(selected[1] ?? "")}`}
                aria-disabled={selected.length !== 2}
                onClick={() => {
                  if (selected.length === 2) {
                    track("output_compare_open", {
                      a: selected[0],
                      b: selected[1],
                    });
                  }
                }}
                className="cta inline-flex items-center gap-1.5 text-sm"
                style={{
                  pointerEvents: selected.length === 2 ? "auto" : "none",
                  opacity: selected.length === 2 ? 1 : 0.5,
                }}
              >
                <RiArrowLeftRightLine size={16} />
                Compare
              </Link>
            </div>
          </div>
          {bulkError && (
            <p
              className="text-xs"
              style={{ color: "var(--color-brandy)" }}
            >
              {bulkError}
            </p>
          )}
        </div>
      )}
    </div>
  );
}
