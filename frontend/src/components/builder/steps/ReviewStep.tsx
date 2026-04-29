"use client";

import {
  RiAlertFill,
  RiCheckboxCircleFill,
  RiErrorWarningFill,
  RiSparklingLine,
  RiDeleteBin6Line,
} from "@remixicon/react";
import { useEffect, useMemo, useState } from "react";
import {
  requestReviewFixSuggestion,
  type ReviewFixSuggestion,
} from "../../../services/jobAdapter";
import { useBuilderDraftStore } from "../../../store/useBuilderDraftStore";
import { useJobStore } from "../../../store/useJobStore";
import type { TcRow } from "../../../lib/types";
import ReviewExportPanel from "./review/ReviewExportPanel";

type Filter = "all" | "error" | "warn" | "ok";

const FIELDS: Array<{ key: keyof EditableFields; label: string }> = [
  { key: "preConditions", label: "Pre-Conditions" },
  { key: "inputTestData", label: "Input Test Data" },
  { key: "steps", label: "Test Procedure" },
  { key: "expectedResults", label: "Expected Result" },
  { key: "designMethod", label: "Design Method" },
  { key: "priority", label: "Priority" },
];

interface EditableFields {
  preConditions: string;
  inputTestData: string;
  steps: string;
  expectedResults: string;
  designMethod: string;
  priority: string;
}

export default function ReviewStep() {
  const tcRows = useJobStore((s) => s.tcRows);
  const updateTcRow = useJobStore((s) => s.updateTcRow);
  const deleteTcRows = useJobStore((s) => s.deleteTcRows);
  const markStepComplete = useBuilderDraftStore((s) => s.markStepComplete);

  const [filter, setFilter] = useState<Filter>("all");
  const [selectedId, setSelectedId] = useState<string | null>(null);

  useEffect(() => {
    if (tcRows.length > 0) markStepComplete("review", true);
  }, [tcRows.length, markStepComplete]);

  // 自動選第一筆
  useEffect(() => {
    if (selectedId && tcRows.find((r) => r.id === selectedId)) return;
    setSelectedId(tcRows[0]?.id ?? null);
  }, [tcRows, selectedId]);

  const counts = useMemo(() => {
    let err = 0,
      warn = 0,
      ok = 0;
    for (const row of tcRows) {
      const sev = severity(row);
      if (sev === "error") err += 1;
      else if (sev === "warn") warn += 1;
      else ok += 1;
    }
    return { all: tcRows.length, err, warn, ok };
  }, [tcRows]);

  const filtered = useMemo(() => {
    if (filter === "all") return tcRows;
    return tcRows.filter((r) => severity(r) === filter);
  }, [tcRows, filter]);

  const selected = tcRows.find((r) => r.id === selectedId) ?? null;

  if (tcRows.length === 0) {
    return (
      <div className="surface p-8 text-center space-y-2">
        <p className="text-sm text-secondary">
          No rows to review. Run generation in the Execute step first.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h2 className="text-xl font-bold text-primary">Review</h2>
        <p className="text-sm text-secondary">
          Inspect each TC, fix issues, then export.
        </p>
      </header>

      <div className="flex items-center gap-2 flex-wrap">
        <FilterPill
          active={filter === "all"}
          onClick={() => setFilter("all")}
          tone="info"
        >
          All ({counts.all})
        </FilterPill>
        <FilterPill
          active={filter === "error"}
          onClick={() => setFilter("error")}
          tone="error"
        >
          Errors ({counts.err})
        </FilterPill>
        <FilterPill
          active={filter === "warn"}
          onClick={() => setFilter("warn")}
          tone="warn"
        >
          Warnings ({counts.warn})
        </FilterPill>
        <FilterPill
          active={filter === "ok"}
          onClick={() => setFilter("ok")}
          tone="ok"
        >
          OK ({counts.ok})
        </FilterPill>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-4">
        <div className="lg:col-span-3">
          <RowList
            rows={filtered}
            selectedId={selectedId}
            onSelect={setSelectedId}
            onDelete={(id) => {
              deleteTcRows([id]);
              if (selectedId === id) setSelectedId(null);
            }}
          />
        </div>
        <div className="lg:col-span-2">
          {selected ? (
            <RowDetail
              key={selected.id}
              row={selected}
              onChange={(patch) => updateTcRow(selected.id, patch)}
            />
          ) : (
            <div className="surface p-8 text-center text-muted text-sm">
              Pick a row to review.
            </div>
          )}
        </div>
      </div>

      <ReviewExportPanel />
    </div>
  );
}

function severity(row: TcRow): "error" | "warn" | "ok" {
  const errs = row.validationErrors ?? [];
  if (errs.some((e) => e.severity === "error")) return "error";
  if (errs.some((e) => e.severity === "warning")) return "warn";
  return "ok";
}

function FilterPill({
  active,
  onClick,
  tone,
  children,
}: {
  active: boolean;
  onClick: () => void;
  tone: "info" | "error" | "warn" | "ok";
  children: React.ReactNode;
}) {
  const colors = {
    info: "var(--color-teal)",
    error: "var(--color-brandy)",
    warn: "var(--color-tangerine)",
    ok: "var(--color-teal)",
  };
  return (
    <button
      type="button"
      onClick={onClick}
      className="px-3 py-1.5 text-xs font-bold rounded-md focus-ring transition-all"
      style={{
        backgroundColor: active ? colors[tone] : "transparent",
        color: active ? "var(--color-papaya)" : colors[tone],
        boxShadow: active
          ? "0 2px 6px var(--shadow-tint)"
          : `inset 0 0 0 1px ${colors[tone]}33`,
      }}
    >
      {children}
    </button>
  );
}

function RowList({
  rows,
  selectedId,
  onSelect,
  onDelete,
}: {
  rows: TcRow[];
  selectedId: string | null;
  onSelect: (id: string) => void;
  onDelete: (id: string) => void;
}) {
  if (rows.length === 0) {
    return (
      <div className="surface p-8 text-center text-muted text-sm">
        No rows match the current filter.
      </div>
    );
  }

  return (
    <div
      className="surface p-2 overflow-y-auto"
      style={{ maxHeight: 600 }}
    >
      <ul className="space-y-1">
        {rows.map((row) => {
          const sev = severity(row);
          const active = row.id === selectedId;
          return (
            <li key={row.id}>
              <button
                type="button"
                onClick={() => onSelect(row.id)}
                className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left transition-all focus-ring row-hover"
                style={{
                  backgroundColor: active
                    ? "rgba(255, 125, 0, 0.12)"
                    : undefined,
                  boxShadow: active
                    ? "inset 0 0 0 2px var(--color-tangerine)"
                    : undefined,
                }}
              >
                <SeverityIcon severity={sev} />
                <div className="flex-1 min-w-0">
                  <div className="text-sm text-primary font-bold truncate">
                    {row.reqId} · {row.tcTitle || row.testItem}
                  </div>
                  <div className="text-xs text-muted truncate">
                    {row.testSet || "—"}
                  </div>
                </div>
                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    if (window.confirm(`Delete ${row.reqId}?`)) onDelete(row.id);
                  }}
                  className="text-muted hover:text-[var(--color-brandy)] focus-ring rounded p-1"
                  aria-label="Delete row"
                >
                  <RiDeleteBin6Line size={14} />
                </button>
              </button>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

function SeverityIcon({ severity: sev }: { severity: "error" | "warn" | "ok" }) {
  if (sev === "error")
    return (
      <RiErrorWarningFill
        size={16}
        style={{ color: "var(--color-brandy)" }}
      />
    );
  if (sev === "warn")
    return (
      <RiAlertFill size={16} style={{ color: "var(--color-tangerine)" }} />
    );
  return (
    <RiCheckboxCircleFill
      size={16}
      style={{ color: "var(--color-teal)" }}
    />
  );
}

function RowDetail({
  row,
  onChange,
}: {
  row: TcRow;
  onChange: (patch: Partial<TcRow>) => void;
}) {
  const [edits, setEdits] = useState<EditableFields>({
    preConditions: row.preConditions || "",
    inputTestData: row.inputTestData || "",
    steps: row.steps || "",
    expectedResults: row.expectedResults || "",
    designMethod: row.designMethod || "",
    priority: row.priority || "",
  });
  const [dirty, setDirty] = useState(false);

  const errors = row.validationErrors ?? [];
  const errorCount = errors.filter((e) => e.severity === "error").length;
  const warnCount = errors.filter((e) => e.severity === "warning").length;

  const save = () => {
    onChange({ ...edits });
    setDirty(false);
  };

  const reset = () => {
    setEdits({
      preConditions: row.preConditions || "",
      inputTestData: row.inputTestData || "",
      steps: row.steps || "",
      expectedResults: row.expectedResults || "",
      designMethod: row.designMethod || "",
      priority: row.priority || "",
    });
    setDirty(false);
  };

  return (
    <div className="surface p-5 space-y-4">
      <header className="space-y-1">
        <div className="text-xs text-muted">{row.reqId}</div>
        <h3 className="text-base font-bold text-primary">
          {row.tcTitle || row.testItem}
        </h3>
        <div className="text-xs text-secondary">{row.testSet || "—"}</div>
      </header>

      {errors.length > 0 && (
        <ValidationSummary
          row={row}
          errorCount={errorCount}
          warnCount={warnCount}
        />
      )}

      <div className="space-y-3">
        {FIELDS.map(({ key, label }) => (
          <div key={key} className="space-y-1">
            <label className="text-[10px] uppercase tracking-wider text-muted font-bold">
              {label}
            </label>
            <textarea
              value={edits[key]}
              onChange={(e) => {
                setEdits((prev) => ({ ...prev, [key]: e.target.value }));
                setDirty(true);
              }}
              rows={key === "steps" || key === "expectedResults" ? 3 : 1}
              className="w-full bg-transparent text-sm py-2 px-3 rounded-md text-primary focus-ring resize-y"
              style={{
                boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.2)",
                minHeight: 32,
              }}
            />
          </div>
        ))}
      </div>

      <div className="flex items-center justify-end gap-2 pt-2">
        <button
          type="button"
          onClick={reset}
          disabled={!dirty}
          className="text-xs px-3 py-1.5 rounded-md focus-ring disabled:opacity-40"
          style={{
            backgroundColor: "rgba(21, 97, 109, 0.12)",
            color: "var(--color-teal)",
          }}
        >
          Reset
        </button>
        <button
          type="button"
          onClick={save}
          disabled={!dirty}
          className="cta inline-flex items-center text-xs px-4 py-1.5 disabled:opacity-50"
        >
          Save changes
        </button>
      </div>
    </div>
  );
}

function ValidationSummary({
  row,
  errorCount,
  warnCount,
}: {
  row: TcRow;
  errorCount: number;
  warnCount: number;
}) {
  const errors = row.validationErrors ?? [];
  const [suggestState, setSuggestState] = useState<{
    kind: "idle" | "loading" | "ok" | "error";
    data?: ReviewFixSuggestion;
    message?: string;
  }>({ kind: "idle" });

  const askAi = async () => {
    setSuggestState({ kind: "loading" });
    try {
      const data = await requestReviewFixSuggestion({
        tc: { ...row },
        errors: errors.map((e) => ({
          severity: e.severity,
          field: e.column,
          message: e.message,
        })),
      });
      setSuggestState({ kind: "ok", data });
    } catch (err) {
      setSuggestState({
        kind: "error",
        message: err instanceof Error ? err.message : "Suggest failed.",
      });
    }
  };

  return (
    <div
      className="space-y-2 px-3 py-2.5 rounded-md"
      style={{
        backgroundColor:
          errorCount > 0
            ? "rgba(120, 41, 15, 0.06)"
            : "rgba(255, 125, 0, 0.06)",
      }}
    >
      <div className="flex items-center justify-between gap-2">
        <div className="text-xs font-bold text-primary">
          {errorCount > 0
            ? `${errorCount} error${errorCount > 1 ? "s" : ""}`
            : ""}
          {errorCount > 0 && warnCount > 0 && " · "}
          {warnCount > 0
            ? `${warnCount} warning${warnCount > 1 ? "s" : ""}`
            : ""}
        </div>
        <button
          type="button"
          onClick={() => void askAi()}
          disabled={suggestState.kind === "loading"}
          className="text-xs font-bold inline-flex items-center gap-1 focus-ring rounded px-2 py-1 disabled:opacity-50"
          style={{ color: "var(--color-tangerine)" }}
        >
          <RiSparklingLine size={12} />
          {suggestState.kind === "loading" ? "Asking..." : "Ask AI"}
        </button>
      </div>
      <ul className="space-y-1 text-xs">
        {errors.map((e, i) => (
          <li key={i} className="flex gap-2">
            <span
              style={{
                color:
                  e.severity === "error"
                    ? "var(--color-brandy)"
                    : "var(--color-tangerine)",
              }}
            >
              {e.severity === "error" ? "✕" : "⚠"}
            </span>
            <span className="text-secondary">
              {e.column ? <strong>{e.column}: </strong> : null}
              {e.message}
            </span>
          </li>
        ))}
      </ul>
      {suggestState.kind === "ok" && suggestState.data && (
        <div
          className="text-xs space-y-1 px-3 py-2 rounded mt-2"
          style={{ backgroundColor: "rgba(21, 97, 109, 0.08)" }}
        >
          <div className="font-bold text-primary">AI suggestion</div>
          <div className="text-secondary">
            <strong>Cause:</strong> {suggestState.data.problemRootCause}
          </div>
          <div className="text-secondary">
            <strong>Proposed:</strong> {suggestState.data.proposedChange}
          </div>
        </div>
      )}
      {suggestState.kind === "error" && (
        <div
          className="text-xs"
          style={{ color: "var(--color-brandy)" }}
        >
          {suggestState.message}
        </div>
      )}
    </div>
  );
}
