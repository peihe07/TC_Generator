"use client";

import {
  RiCheckLine,
  RiCloseLine,
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
import type { TcRow } from "../../../../lib/types";
import { useJobStore } from "../../../../store/useJobStore";

type FieldKey = "preConditions" | "inputTestData" | "steps" | "expectedResults";

const FIELDS: Array<{ key: FieldKey; label: string }> = [
  { key: "preConditions", label: "Pre-Conditions" },
  { key: "inputTestData", label: "Input Test Data" },
  { key: "steps", label: "Test Procedure" },
  { key: "expectedResults", label: "Expected Result" },
];

export default function RegeneratePanel({ row }: { row: TcRow }) {
  const config = useJobStore((s) => s.config);
  const jobMetadata = useJobStore((s) => s.jobMetadata);
  const setAwaitingApply = useJobStore((s) => s.setAwaitingApply);
  const applyRegenerated = useJobStore((s) => s.applyRegenerated);
  const clearAwaitingApply = useJobStore((s) => s.clearAwaitingApply);
  const updateTcRow = useJobStore((s) => s.updateTcRow);
  const isRegenerating = useJobStore((s) => s.isRegenerating);
  const setRegenerating = useJobStore((s) => s.setRegenerating);
  const addTcRowAfter = useJobStore((s) => s.addTcRowAfter);

  const [reason, setReason] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [showDialog, setShowDialog] = useState(false);
  const [isRerunning, setIsRerunning] = useState(false);
  const [rerunSummary, setRerunSummary] = useState<RerunSummary | null>(null);

  const awaiting = row.awaitingApply;

  const start = async () => {
    if (!jobMetadata?.jobId) {
      setError("No backend job. Run generation first.");
      return;
    }
    if (!reason.trim()) {
      setError("Please provide a reason — it guides the AI's revision.");
      return;
    }
    setShowDialog(false);
    setError(null);
    setRegenerating(true);
    updateTcRow(row.id, { status: "generating" });

    await regenerateRows(
      {
        jobId: jobMetadata.jobId,
        rowIds: [row.id],
        rows: [row],
        config,
        regenerateReason: reason.trim(),
      },
      {
        onRow: (rowId, fields) => {
          if (rowId === row.id) setAwaitingApply(rowId, fields);
        },
        onFail: (rowId, message) => {
          if (rowId === row.id) {
            updateTcRow(rowId, { status: "fail" });
            setError(message);
          }
        },
        onComplete: () => {
          setRegenerating(false);
          updateTcRow(row.id, { status: "success" });
        },
        onError: (message) => {
          setRegenerating(false);
          setError(message);
        },
      }
    );
  };

  const apply = (selectedKeys: FieldKey[]) => {
    applyRegenerated(row.id, selectedKeys);
  };

  const reject = () => {
    clearAwaitingApply(row.id);
  };

  const startRerun = async () => {
    if (!jobMetadata?.jobId) {
      setError("No backend job. Run generation first.");
      return;
    }
    setError(null);
    setRerunSummary(null);
    setIsRerunning(true);
    updateTcRow(row.id, { status: "generating" });

    await rerunRows(
      {
        jobId: jobMetadata.jobId,
        rowIds: [row.id],
        rows: [row],
        config,
        project: jobMetadata.projectName ?? null,
      },
      {
        onPrimary: (newRow) => updateTcRow(newRow.id, newRow),
        onRowAdded: (newRow, parentId) => addTcRowAfter(parentId, newRow),
        onFail: (rowId, message) => {
          if (rowId === row.id) {
            updateTcRow(rowId, { status: "fail" });
            setError(message);
          }
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

  return (
    <section className="surface p-4 space-y-3">
      <header className="flex items-center justify-between gap-2">
        <h3 className="text-xs uppercase tracking-wider text-secondary font-bold">
          Regenerate with AI
        </h3>
        {awaiting ? (
          <span
            className="text-[10px] font-bold uppercase tracking-wider"
            style={{ color: "var(--color-tangerine)" }}
          >
            Awaiting your decision
          </span>
        ) : null}
      </header>

      {!awaiting && (
        <div className="space-y-2">
          <div className="flex items-center gap-2 flex-wrap">
            <button
              type="button"
              onClick={() => {
                setShowDialog(true);
                setError(null);
              }}
              disabled={
                isRegenerating || isRerunning || !jobMetadata?.jobId
              }
              className="cta inline-flex items-center gap-1.5 text-xs px-3 py-1.5 disabled:opacity-50"
            >
              {isRegenerating ? (
                <>
                  <RiLoader4Line size={12} className="animate-spin" />
                  Regenerating...
                </>
              ) : (
                <>
                  <RiSparklingLine size={12} />
                  Regenerate (with reason)
                </>
              )}
            </button>
            <button
              type="button"
              onClick={() => {
                if (
                  window.confirm(
                    "Re-run will overwrite this row directly without a preview. Continue?"
                  )
                )
                  void startRerun();
              }}
              disabled={
                isRegenerating || isRerunning || !jobMetadata?.jobId
              }
              className="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-md font-bold focus-ring transition-all disabled:opacity-50"
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
                  Re-run (overwrite)
                </>
              )}
            </button>
            {!jobMetadata?.jobId && (
              <span className="text-xs text-muted">
                Run generation first to enable
              </span>
            )}
          </div>
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
      )}

      {error && !awaiting && (
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

      {showDialog && (
        <div className="space-y-2">
          <label className="text-[10px] uppercase tracking-wider text-muted font-bold">
            Reason for regeneration
          </label>
          <textarea
            value={reason}
            onChange={(e) => setReason(e.target.value)}
            placeholder="e.g. Steps are missing the negative case for invalid input."
            rows={3}
            className="w-full bg-transparent text-sm py-2 px-3 rounded-md text-primary focus-ring resize-y"
            style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.25)" }}
          />
          <div className="flex items-center justify-end gap-2">
            <button
              type="button"
              onClick={() => setShowDialog(false)}
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
              onClick={() => void start()}
              className="cta inline-flex items-center text-xs px-3 py-1.5"
            >
              Send to AI
            </button>
          </div>
          {error && (
            <p
              className="text-xs"
              style={{ color: "var(--color-brandy)" }}
            >
              {error}
            </p>
          )}
        </div>
      )}

      {awaiting && (
        <AwaitingApplyView row={row} onApply={apply} onReject={reject} />
      )}
    </section>
  );
}

function AwaitingApplyView({
  row,
  onApply,
  onReject,
}: {
  row: TcRow;
  onApply: (keys: FieldKey[]) => void;
  onReject: () => void;
}) {
  const awaiting = row.awaitingApply;
  if (!awaiting) return null;

  // 預設全選所有變更欄位
  const initiallyChanged = FIELDS.filter(
    ({ key }) => normalize(awaiting[key]) !== normalize(row[key])
  ).map(({ key }) => key);

  const [selected, setSelected] = useState<FieldKey[]>(initiallyChanged);

  const toggle = (key: FieldKey) =>
    setSelected((prev) =>
      prev.includes(key) ? prev.filter((k) => k !== key) : [...prev, key]
    );

  return (
    <div className="space-y-3">
      {FIELDS.map(({ key, label }) => {
        const before = String(row[key] ?? "");
        const after = String(awaiting[key] ?? "");
        const changed = normalize(before) !== normalize(after);
        return (
          <div
            key={key}
            className="space-y-1.5"
            style={{
              opacity: changed ? 1 : 0.5,
            }}
          >
            <label className="flex items-center gap-2 text-xs">
              <input
                type="checkbox"
                checked={selected.includes(key)}
                onChange={() => toggle(key)}
                disabled={!changed}
                className="sr-only"
              />
              <span
                className="flex items-center justify-center w-3.5 h-3.5 rounded transition-all"
                style={{
                  backgroundColor: selected.includes(key)
                    ? "var(--color-tangerine)"
                    : "transparent",
                  boxShadow: selected.includes(key)
                    ? "0 1px 2px var(--shadow-tint)"
                    : "inset 0 0 0 1.5px var(--color-teal)",
                  color: "var(--color-ink)",
                  cursor: changed ? "pointer" : "not-allowed",
                }}
                onClick={() => changed && toggle(key)}
              >
                {selected.includes(key) && (
                  <svg width="9" height="9" viewBox="0 0 12 12" fill="none">
                    <path
                      d="M2 6.5L5 9.5L10 3.5"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                )}
              </span>
              <span className="font-bold text-primary">{label}</span>
              {!changed && (
                <span className="text-muted text-[10px]">(no change)</span>
              )}
            </label>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              <div
                className="p-2 rounded text-secondary"
                style={{
                  backgroundColor: "rgba(120, 41, 15, 0.06)",
                  whiteSpace: "pre-wrap",
                }}
              >
                <div
                  className="text-[9px] uppercase tracking-wider mb-1 font-bold"
                  style={{ color: "var(--color-brandy)" }}
                >
                  Before
                </div>
                {before || <span className="text-muted">—</span>}
              </div>
              <div
                className="p-2 rounded text-secondary"
                style={{
                  backgroundColor: "rgba(21, 97, 109, 0.08)",
                  whiteSpace: "pre-wrap",
                }}
              >
                <div
                  className="text-[9px] uppercase tracking-wider mb-1 font-bold"
                  style={{ color: "var(--color-teal)" }}
                >
                  After
                </div>
                {after || <span className="text-muted">—</span>}
              </div>
            </div>
          </div>
        );
      })}

      <div className="flex items-center justify-end gap-2 pt-1">
        <button
          type="button"
          onClick={onReject}
          className="inline-flex items-center gap-1 text-xs px-3 py-1.5 rounded-md focus-ring"
          style={{
            backgroundColor: "rgba(120, 41, 15, 0.1)",
            color: "var(--color-brandy)",
          }}
        >
          <RiCloseLine size={12} />
          Reject
        </button>
        <button
          type="button"
          onClick={() => onApply(selected)}
          disabled={selected.length === 0}
          className="cta inline-flex items-center gap-1 text-xs px-3 py-1.5 disabled:opacity-50"
        >
          <RiCheckLine size={12} />
          Apply {selected.length > 0 ? `${selected.length} field(s)` : ""}
        </button>
      </div>
    </div>
  );
}

function normalize(v: unknown): string {
  return String(v ?? "").trim();
}
