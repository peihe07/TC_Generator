"use client";

import {
  RiDownload2Line,
  RiLoader4Line,
  RiCheckLine,
  RiAlertLine,
  RiUpload2Line,
} from "@remixicon/react";
import { useEffect, useRef, useState } from "react";
import {
  attachRawWorkbook,
  exportJob,
  fetchSourceStatus,
} from "../../../../services/jobAdapter";
import { useBuilderDraftStore } from "../../../../store/useBuilderDraftStore";
import { useJobStore } from "../../../../store/useJobStore";

const SCOPE_OPTIONS: Array<{ value: "all" | "accepted"; label: string }> = [
  { value: "all", label: "All rows" },
  { value: "accepted", label: "Accepted only" },
];

const OUTPUT_OPTIONS: Array<{ value: "new-file" | "overwrite"; label: string }> =
  [
    { value: "new-file", label: "New file" },
    { value: "overwrite", label: "Overwrite source workbook" },
  ];

const COLUMN_OPTIONS = [
  { key: "preConditions", label: "Pre-Conditions" },
  { key: "inputTestData", label: "Input Test Data" },
  { key: "steps", label: "Test Procedure" },
  { key: "expectedResults", label: "Expected Result" },
  { key: "designMethod", label: "Design Method" },
  { key: "priority", label: "Priority" },
];

interface ExportResult {
  downloadUrl: string;
  exportedRows: number;
  fallbackTemplate?: boolean;
  tcIdsRenumbered?: number;
}

export default function ReviewExportPanel() {
  const tcRows = useJobStore((s) => s.tcRows);
  const jobMetadata = useJobStore((s) => s.jobMetadata);
  const config = useJobStore((s) => s.config);
  const markStepComplete = useBuilderDraftStore((s) => s.markStepComplete);

  const [scope, setScope] = useState<"all" | "accepted">("all");
  const [outputMode, setOutputMode] = useState<"new-file" | "overwrite">(
    "new-file"
  );
  const [includeFramework, setIncludeFramework] = useState(false);
  const [selectedColumns, setSelectedColumns] = useState<string[]>(() => [
    ...config.targetColumns,
  ]);

  const [state, setState] = useState<
    | { kind: "idle" }
    | { kind: "running" }
    | { kind: "done"; result: ExportResult }
    | { kind: "error"; message: string }
  >({ kind: "idle" });

  // Source workbook attach status — when the job lost rawBytes (e.g. server
  // restart), overwrite mode + framework sheet rebuild can't run without it.
  const [sourceStatus, setSourceStatus] = useState<{
    hasSource: boolean;
    rawFileName: string | null;
  } | null>(null);
  const [attaching, setAttaching] = useState(false);
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    if (!jobMetadata?.jobId) {
      setSourceStatus(null);
      return;
    }
    let cancelled = false;
    void fetchSourceStatus(jobMetadata.jobId)
      .then((s) => {
        if (!cancelled) setSourceStatus(s);
      })
      .catch(() => {
        if (!cancelled) setSourceStatus(null);
      });
    return () => {
      cancelled = true;
    };
  }, [jobMetadata?.jobId]);

  const handleAttach = async (file: File) => {
    if (!jobMetadata?.jobId) return;
    setAttaching(true);
    try {
      const res = await attachRawWorkbook(jobMetadata.jobId, file);
      setSourceStatus({
        hasSource: res.hasSource,
        rawFileName: res.rawFileName,
      });
    } catch (err) {
      setState({
        kind: "error",
        message:
          err instanceof Error
            ? err.message
            : "Failed to attach raw workbook.",
      });
    } finally {
      setAttaching(false);
    }
  };

  const onExport = async () => {
    if (!jobMetadata?.jobId) {
      setState({
        kind: "error",
        message: "No backend jobId. Run generation first.",
      });
      return;
    }
    setState({ kind: "running" });
    try {
      const result = (await exportJob({
        jobId: jobMetadata.jobId,
        rows: tcRows,
        scope,
        outputMode,
        includeFrameworkSheet: includeFramework,
        selectedColumns,
      })) as ExportResult;
      setState({ kind: "done", result });
      markStepComplete("review", true);
    } catch (err) {
      setState({
        kind: "error",
        message: err instanceof Error ? err.message : "Export failed.",
      });
    }
  };

  const toggleColumn = (key: string) => {
    setSelectedColumns((prev) =>
      prev.includes(key) ? prev.filter((c) => c !== key) : [...prev, key]
    );
  };

  return (
    <section className="surface p-5 space-y-4">
      <header className="space-y-1">
        <h3 className="text-base font-bold text-primary">Export</h3>
        <p className="text-xs text-secondary">
          Build the final xlsx and download it.
        </p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="space-y-2">
          <SubLabel>Scope</SubLabel>
          <PillGroup
            value={scope}
            options={SCOPE_OPTIONS}
            onChange={setScope}
          />
        </div>
        <div className="space-y-2">
          <SubLabel>Output</SubLabel>
          <PillGroup
            value={outputMode}
            options={OUTPUT_OPTIONS}
            onChange={setOutputMode}
          />
        </div>
      </div>

      <div className="space-y-2">
        <SubLabel>Columns to include</SubLabel>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-1.5">
          {COLUMN_OPTIONS.map(({ key, label }) => (
            <button
              key={key}
              type="button"
              onClick={() => toggleColumn(key)}
              className="text-left px-2.5 py-1.5 rounded-md text-xs font-bold focus-ring transition-all"
              style={{
                backgroundColor: selectedColumns.includes(key)
                  ? "var(--color-tangerine)"
                  : "transparent",
                color: selectedColumns.includes(key)
                  ? "var(--color-ink)"
                  : "var(--color-teal)",
                boxShadow: selectedColumns.includes(key)
                  ? "0 1px 4px var(--shadow-tint)"
                  : "inset 0 0 0 1px rgba(21, 97, 109, 0.2)",
              }}
            >
              {label}
            </button>
          ))}
        </div>
      </div>

      <label className="flex items-center gap-2 text-sm cursor-pointer">
        <input
          type="checkbox"
          checked={includeFramework}
          onChange={(e) => setIncludeFramework(e.target.checked)}
          className="sr-only"
        />
        <span
          className="flex items-center justify-center w-4 h-4 rounded transition-all"
          style={{
            backgroundColor: includeFramework
              ? "var(--color-tangerine)"
              : "transparent",
            boxShadow: includeFramework
              ? "0 1px 2px var(--shadow-tint)"
              : "inset 0 0 0 1.5px var(--color-teal)",
            color: "var(--color-ink)",
          }}
        >
          {includeFramework && (
            <svg width="10" height="10" viewBox="0 0 12 12" fill="none">
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
        <span className="text-secondary">
          Include framework / instructions sheet
        </span>
      </label>

      {sourceStatus && !sourceStatus.hasSource && jobMetadata?.jobId && (
        <div
          className="text-sm px-3 py-2 rounded-md flex items-start gap-2 flex-wrap"
          style={{
            color: "var(--color-brandy)",
            backgroundColor: "rgba(120, 41, 15, 0.08)",
          }}
        >
          <RiAlertLine size={16} className="shrink-0 mt-0.5" />
          <div className="flex-1 space-y-1 min-w-0">
            <div>
              Original raw workbook is missing on the server (likely cleared
              after a restart).
              {outputMode === "overwrite" || includeFramework
                ? " Re-attach it before exporting."
                : " New-file export will still work; re-attach is required for overwrite mode and framework sheet rebuild."}
            </div>
            <input
              ref={fileInputRef}
              type="file"
              accept=".xlsx,.xlsm"
              className="hidden"
              onChange={(e) => {
                const file = e.target.files?.[0];
                if (file) void handleAttach(file);
                e.target.value = "";
              }}
            />
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              disabled={attaching}
              className="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-md font-bold focus-ring disabled:opacity-50"
              style={{
                color: "var(--color-brandy)",
                backgroundColor: "rgba(120, 41, 15, 0.12)",
              }}
            >
              {attaching ? (
                <RiLoader4Line size={12} className="animate-spin" />
              ) : (
                <RiUpload2Line size={12} />
              )}
              {attaching ? "Attaching…" : "Re-attach raw workbook"}
            </button>
          </div>
        </div>
      )}

      {sourceStatus?.hasSource && sourceStatus.rawFileName && (
        <div className="text-[10px] uppercase tracking-wider text-muted">
          Source: <code className="text-secondary">{sourceStatus.rawFileName}</code>
        </div>
      )}

      {state.kind === "error" && (
        <div
          className="text-sm px-3 py-2 rounded-md flex items-start gap-2"
          style={{
            color: "var(--color-brandy)",
            backgroundColor: "rgba(120, 41, 15, 0.08)",
          }}
        >
          <RiAlertLine size={16} className="shrink-0 mt-0.5" />
          <span>{state.message}</span>
        </div>
      )}

      {state.kind === "done" && (
        <div
          className="text-sm px-3 py-2 rounded-md flex items-center gap-2"
          style={{
            color: "var(--color-teal)",
            backgroundColor: "rgba(21, 97, 109, 0.08)",
          }}
        >
          <RiCheckLine size={16} className="shrink-0" />
          <span className="flex-1">
            Exported {state.result.exportedRows} row(s)
            {state.result.fallbackTemplate
              ? " (fallback template used)"
              : ""}
            .
          </span>
          <a
            href={state.result.downloadUrl}
            className="cta inline-flex items-center gap-1 text-xs px-3 py-1.5"
          >
            <RiDownload2Line size={12} />
            Download
          </a>
        </div>
      )}

      <div className="flex items-center justify-between gap-3 pt-1">
        <span className="text-xs text-muted">
          {tcRows.length} row(s) · jobId{" "}
          <code>{jobMetadata?.jobId ?? "—"}</code>
        </span>
        <button
          type="button"
          onClick={() => void onExport()}
          disabled={
            state.kind === "running" ||
            !jobMetadata?.jobId ||
            tcRows.length === 0 ||
            selectedColumns.length === 0
          }
          className="cta inline-flex items-center gap-1.5 text-sm disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {state.kind === "running" ? (
            <>
              <RiLoader4Line size={14} className="animate-spin" />
              Building xlsx...
            </>
          ) : (
            <>
              <RiDownload2Line size={14} />
              Build & Export
            </>
          )}
        </button>
      </div>
    </section>
  );
}

function SubLabel({ children }: { children: React.ReactNode }) {
  return (
    <div className="text-[10px] uppercase tracking-wider text-muted font-bold">
      {children}
    </div>
  );
}

function PillGroup<T extends string>({
  value,
  options,
  onChange,
}: {
  value: T;
  options: Array<{ value: T; label: string }>;
  onChange: (v: T) => void;
}) {
  return (
    <div className="flex items-center gap-1">
      {options.map((o) => {
        const active = o.value === value;
        return (
          <button
            key={o.value}
            type="button"
            onClick={() => onChange(o.value)}
            className="px-3 py-1.5 text-xs font-bold rounded-md focus-ring transition-all"
            style={{
              backgroundColor: active
                ? "var(--color-tangerine)"
                : "transparent",
              color: active ? "var(--color-ink)" : "var(--color-teal)",
              boxShadow: active
                ? "0 1px 4px var(--shadow-tint)"
                : "inset 0 0 0 1px rgba(21, 97, 109, 0.2)",
            }}
          >
            {o.label}
          </button>
        );
      })}
    </div>
  );
}
