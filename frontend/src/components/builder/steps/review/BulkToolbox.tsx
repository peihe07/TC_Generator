"use client";

import {
  RiCloseLine,
  RiDeleteBin6Line,
  RiLoader4Line,
  RiRefreshLine,
  RiSparklingLine,
} from "@remixicon/react";
import { useState } from "react";
import {
  regenerateRows,
  rerunRows,
  type RerunSummary,
} from "../../../../services/jobAdapter";
import { useJobStore } from "../../../../store/useJobStore";
import type { TcRow } from "../../../../lib/types";

export default function BulkToolbox({
  selectedIds,
  rows,
  onClear,
}: {
  selectedIds: string[];
  rows: TcRow[];
  onClear: () => void;
}) {
  const config = useJobStore((s) => s.config);
  const jobMetadata = useJobStore((s) => s.jobMetadata);
  const deleteTcRows = useJobStore((s) => s.deleteTcRows);
  const setAwaitingApply = useJobStore((s) => s.setAwaitingApply);
  const updateTcRow = useJobStore((s) => s.updateTcRow);
  const addTcRowAfter = useJobStore((s) => s.addTcRowAfter);
  const isRegenerating = useJobStore((s) => s.isRegenerating);
  const setRegenerating = useJobStore((s) => s.setRegenerating);

  const [showRegenDialog, setShowRegenDialog] = useState(false);
  const [reason, setReason] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isRerunning, setIsRerunning] = useState(false);
  const [rerunSummary, setRerunSummary] = useState<RerunSummary | null>(null);

  const selectedRows = rows.filter((r) => selectedIds.includes(r.id));
  const count = selectedRows.length;

  const onDelete = () => {
    if (
      window.confirm(
        `Delete ${count} row(s)? This cannot be undone.`
      )
    ) {
      deleteTcRows(selectedIds);
      onClear();
    }
  };

  const startBulkRegen = async () => {
    if (!jobMetadata?.jobId) {
      setError("No backend job. Run generation first.");
      return;
    }
    if (!reason.trim()) {
      setError("Please provide a reason.");
      return;
    }
    setShowRegenDialog(false);
    setError(null);
    setRegenerating(true);
    selectedIds.forEach((id) => updateTcRow(id, { status: "generating" }));

    await regenerateRows(
      {
        jobId: jobMetadata.jobId,
        rowIds: selectedIds,
        rows: selectedRows,
        config,
        regenerateReason: reason.trim(),
      },
      {
        onRow: (rowId, fields) => setAwaitingApply(rowId, fields),
        onFail: (rowId, message) => {
          updateTcRow(rowId, { status: "fail" });
          setError(`${rowId}: ${message}`);
        },
        onComplete: () => {
          setRegenerating(false);
          selectedIds.forEach((id) => {
            const cur = useJobStore
              .getState()
              .tcRows.find((r) => r.id === id);
            if (cur && cur.status === "generating") {
              updateTcRow(id, { status: "success" });
            }
          });
        },
        onError: (message) => {
          setRegenerating(false);
          setError(message);
        },
      }
    );
  };

  const startBulkRerun = async () => {
    if (!jobMetadata?.jobId) {
      setError("No backend job. Run generation first.");
      return;
    }
    if (
      !window.confirm(
        `Re-run ${count} row(s)? Each will be overwritten directly without preview.`
      )
    )
      return;

    setError(null);
    setRerunSummary(null);
    setIsRerunning(true);
    selectedIds.forEach((id) => updateTcRow(id, { status: "generating" }));

    await rerunRows(
      {
        jobId: jobMetadata.jobId,
        rowIds: selectedIds,
        rows: selectedRows,
        config,
        project: jobMetadata.projectName ?? null,
      },
      {
        onPrimary: (newRow) => updateTcRow(newRow.id, newRow),
        onRowAdded: (newRow, parentId) => addTcRowAfter(parentId, newRow),
        onFail: (rowId, message) => {
          updateTcRow(rowId, { status: "fail" });
          setError(`${rowId}: ${message}`);
        },
        onComplete: (summary) => {
          setIsRerunning(false);
          setRerunSummary(summary);
        },
        onError: (message) => {
          setIsRerunning(false);
          setError(message);
        },
      }
    );
  };

  if (count === 0) return null;

  return (
    <div
      className="sticky bottom-4 z-30 surface-floating px-4 py-3 space-y-2"
      style={{ borderRadius: 16 }}
    >
      <div className="flex items-center justify-between gap-3 flex-wrap">
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={onClear}
            className="flex items-center justify-center w-7 h-7 rounded-full focus-ring transition-all"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
            aria-label="Clear selection"
          >
            <RiCloseLine size={16} />
          </button>
          <span className="text-sm text-primary font-bold">
            {count} selected
          </span>
        </div>

        <div className="flex items-center gap-2 flex-wrap">
          <button
            type="button"
            onClick={() => {
              setShowRegenDialog(true);
              setError(null);
            }}
            disabled={isRegenerating || isRerunning || !jobMetadata?.jobId}
            className="cta inline-flex items-center gap-1 text-xs px-3 py-1.5 disabled:opacity-50"
          >
            {isRegenerating ? (
              <>
                <RiLoader4Line size={12} className="animate-spin" />
                Regenerating...
              </>
            ) : (
              <>
                <RiSparklingLine size={12} />
                Regenerate
              </>
            )}
          </button>
          <button
            type="button"
            onClick={() => void startBulkRerun()}
            disabled={isRegenerating || isRerunning || !jobMetadata?.jobId}
            className="inline-flex items-center gap-1 text-xs px-3 py-1.5 rounded-md font-bold focus-ring disabled:opacity-50 transition-all"
            style={{
              backgroundColor: "rgba(21, 97, 109, 0.12)",
              color: "var(--color-teal)",
            }}
          >
            {isRerunning ? (
              <>
                <RiLoader4Line size={12} className="animate-spin" />
                Re-running...
              </>
            ) : (
              <>
                <RiRefreshLine size={12} />
                Re-run
              </>
            )}
          </button>
          <button
            type="button"
            onClick={onDelete}
            disabled={isRegenerating || isRerunning}
            className="inline-flex items-center gap-1 text-xs px-3 py-1.5 rounded-md font-bold focus-ring disabled:opacity-50 transition-all"
            style={{
              backgroundColor: "rgba(120, 41, 15, 0.1)",
              color: "var(--color-brandy)",
            }}
          >
            <RiDeleteBin6Line size={12} />
            Delete
          </button>
        </div>
      </div>

      {showRegenDialog && (
        <div className="space-y-2 pt-2">
          <label className="text-[10px] uppercase tracking-wider text-muted font-bold">
            Reason (applied to all {count} rows)
          </label>
          <textarea
            value={reason}
            onChange={(e) => setReason(e.target.value)}
            placeholder="e.g. Add negative test cases for invalid input."
            rows={2}
            className="w-full bg-transparent text-sm py-2 px-3 rounded-md text-primary focus-ring resize-y"
            style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.25)" }}
          />
          <div className="flex items-center justify-end gap-2">
            <button
              type="button"
              onClick={() => setShowRegenDialog(false)}
              className="text-xs px-3 py-1.5 rounded-md focus-ring"
              style={{
                backgroundColor: "rgba(21, 97, 109, 0.12)",
                color: "var(--color-teal)",
              }}
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={() => void startBulkRegen()}
              className="cta inline-flex items-center text-xs px-3 py-1.5"
            >
              Send to AI
            </button>
          </div>
        </div>
      )}

      {error && (
        <div
          className="text-xs px-3 py-2 rounded-md"
          style={{
            color: "var(--color-brandy)",
            backgroundColor: "rgba(120, 41, 15, 0.08)",
          }}
        >
          {error}
        </div>
      )}

      {rerunSummary && (
        <div
          className="text-xs px-3 py-2 rounded-md"
          style={{
            color: "var(--color-teal)",
            backgroundColor: "rgba(21, 97, 109, 0.08)",
          }}
        >
          Re-run finished: {rerunSummary.rowsUpdated} updated,{" "}
          {rerunSummary.rowsAdded} added, {rerunSummary.rowsFailed} failed.
        </div>
      )}
    </div>
  );
}
