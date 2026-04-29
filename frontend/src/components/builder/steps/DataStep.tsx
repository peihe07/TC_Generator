"use client";

import {
  RiFileExcel2Line,
  RiFileLine,
  RiFileSearchLine,
  RiCheckLine,
} from "@remixicon/react";
import { useEffect, useRef, useState } from "react";
import { createJobLog } from "../../../lib/logging";
import {
  fetchSpecLibrary,
  parseJobFiles,
  type SpecLibraryEntry,
} from "../../../services/jobAdapter";
import { useBuilderDraftStore } from "../../../store/useBuilderDraftStore";
import { useJobStore } from "../../../store/useJobStore";
import { formatSpecLibraryLabel } from "../../modules/upload/UploadModule";

type Slot = "tc" | "referenceWorkbook" | "spec";

export default function DataStep({ onAdvance }: { onAdvance: () => void }) {
  const setJobMetadata = useJobStore((s) => s.setJobMetadata);
  const setTcRows = useJobStore((s) => s.setTcRows);
  const updateStats = useJobStore((s) => s.updateStats);
  const appendLog = useJobStore((s) => s.appendLog);

  const updateDraft = useBuilderDraftStore((s) => s.update);
  const markStepComplete = useBuilderDraftStore((s) => s.markStepComplete);

  const [files, setFiles] = useState<{
    tc?: File;
    referenceWorkbook?: File;
    spec?: File;
  }>({});
  const [draggingZone, setDraggingZone] = useState<Slot | null>(null);
  const [specLibrary, setSpecLibrary] = useState<SpecLibraryEntry[]>([]);
  const [selectedSpecName, setSelectedSpecName] = useState("");
  const [libraryError, setLibraryError] = useState("");
  const [parseError, setParseError] = useState("");
  const [isParsing, setIsParsing] = useState(false);

  const tcInputRef = useRef<HTMLInputElement | null>(null);
  const refInputRef = useRef<HTMLInputElement | null>(null);
  const specInputRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetchSpecLibrary()
      .then((list) => {
        if (!cancelled) setSpecLibrary(list);
      })
      .catch((err) => {
        if (!cancelled) {
          setLibraryError(
            err instanceof Error ? err.message : "Failed to load spec library."
          );
        }
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const handleDrop = (e: React.DragEvent, slot: Slot) => {
    e.preventDefault();
    setDraggingZone(null);
    const file = e.dataTransfer.files[0];
    if (file) {
      setParseError("");
      setFiles((prev) => ({ ...prev, [slot]: file }));
    }
  };

  const handlePick = (
    e: React.ChangeEvent<HTMLInputElement>,
    slot: Slot
  ) => {
    const file = e.target.files?.[0];
    if (file) {
      setParseError("");
      setFiles((prev) => ({ ...prev, [slot]: file }));
    }
  };

  const onParse = async () => {
    if (!files.tc || isParsing) return;
    setIsParsing(true);
    setParseError("");
    appendLog(
      createJobLog("info", `Parsing ${files.tc.name} via job adapter.`)
    );

    try {
      const result = await parseJobFiles({
        rawFile: files.tc,
        referenceWorkbookFile: selectedSpecName
          ? undefined
          : files.referenceWorkbook,
        specFile: files.spec,
        selectedSpecName: selectedSpecName || undefined,
      });

      setJobMetadata(result.jobMetadata);
      setTcRows(result.rows);
      updateStats({
        total: result.stats.total,
        processed: 0,
        success: 0,
        fail: 0,
      });
      appendLog(
        createJobLog(
          "success",
          `Loaded ${result.rows.length} row(s) for ${result.jobMetadata.projectName}.`
        )
      );

      updateDraft({
        data: {
          datasetId: result.jobMetadata.jobId,
          fileName: files.tc.name,
          rowCount: result.rows.length,
        },
      });
      markStepComplete("data", true);
      onAdvance();
    } catch (error) {
      const msg =
        error instanceof Error
          ? error.message
          : "Failed to parse the workbook.";
      setParseError(msg);
      appendLog(createJobLog("error", msg));
    } finally {
      setIsParsing(false);
    }
  };

  return (
    <div className="space-y-4">
      <DropZone
        slot="tc"
        title="TC Specification"
        hint=".xlsx / .xlsm — required"
        Icon={RiFileExcel2Line}
        file={files.tc}
        accept=".xlsx,.xlsm"
        dragging={draggingZone === "tc"}
        inputRef={tcInputRef}
        onDrop={handleDrop}
        onDragEnter={() => setDraggingZone("tc")}
        onDragLeave={() => setDraggingZone((z) => (z === "tc" ? null : z))}
        onPick={handlePick}
      />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="space-y-2">
          <label className="block text-xs uppercase tracking-wider text-secondary">
            Reference Workbook (Optional)
          </label>
          <select
            value={selectedSpecName}
            onChange={(e) => {
              setSelectedSpecName(e.target.value);
              setParseError("");
            }}
            className="w-full bg-transparent text-sm py-2 px-3 rounded-md text-primary focus-ring"
            style={{ boxShadow: "inset 0 0 0 1px rgba(21, 97, 109, 0.25)" }}
          >
            <option value="">— None (use upload below) —</option>
            {specLibrary.map((spec) => (
              <option key={spec.name} value={spec.name}>
                {formatSpecLibraryLabel(spec.name)}
                {spec.entriesCount != null ? ` (${spec.entriesCount})` : ""}
              </option>
            ))}
          </select>
          {libraryError && (
            <p
              className="text-xs"
              style={{ color: "var(--color-brandy)" }}
            >
              {libraryError}
            </p>
          )}
          <DropZone
            slot="referenceWorkbook"
            title="Or drop a reference workbook"
            hint=".xlsx / .xlsm"
            Icon={RiFileSearchLine}
            file={selectedSpecName ? undefined : files.referenceWorkbook}
            accept=".xlsx,.xlsm"
            dragging={draggingZone === "referenceWorkbook"}
            disabled={!!selectedSpecName}
            disabledLabel="Library spec selected"
            inputRef={refInputRef}
            onDrop={handleDrop}
            onDragEnter={() => setDraggingZone("referenceWorkbook")}
            onDragLeave={() =>
              setDraggingZone((z) => (z === "referenceWorkbook" ? null : z))
            }
            onPick={handlePick}
            compact
          />
        </div>

        <div className="space-y-2">
          <label className="block text-xs uppercase tracking-wider text-secondary">
            Reference PDF / DOCX (Optional)
          </label>
          <DropZone
            slot="spec"
            title="Drop a reference document"
            hint=".pdf / .docx / .xlsx"
            Icon={RiFileLine}
            file={files.spec}
            accept=".pdf,.docx,.xlsx"
            dragging={draggingZone === "spec"}
            inputRef={specInputRef}
            onDrop={handleDrop}
            onDragEnter={() => setDraggingZone("spec")}
            onDragLeave={() => setDraggingZone((z) => (z === "spec" ? null : z))}
            onPick={handlePick}
          />
        </div>
      </div>

      {parseError && (
        <div
          className="surface p-3 text-sm"
          style={{ color: "var(--color-brandy)" }}
          role="alert"
        >
          <span className="font-bold">Parse error:</span> {parseError}
        </div>
      )}

      <div className="flex items-center justify-end">
        <button
          type="button"
          onClick={() => void onParse()}
          disabled={!files.tc || isParsing}
          className="cta inline-flex items-center gap-1.5 text-sm disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isParsing ? "Parsing..." : "Parse & Continue"}
        </button>
      </div>
    </div>
  );
}

function DropZone({
  title,
  hint,
  Icon,
  file,
  accept,
  dragging,
  inputRef,
  onDrop,
  onDragEnter,
  onDragLeave,
  onPick,
  slot,
  disabled,
  disabledLabel,
  compact,
}: {
  title: string;
  hint: string;
  Icon: typeof RiFileLine;
  file?: File;
  accept: string;
  dragging: boolean;
  inputRef: React.RefObject<HTMLInputElement | null>;
  onDrop: (e: React.DragEvent, slot: Slot) => void;
  onDragEnter: (e: React.DragEvent) => void;
  onDragLeave: (e: React.DragEvent) => void;
  onPick: (e: React.ChangeEvent<HTMLInputElement>, slot: Slot) => void;
  slot: Slot;
  disabled?: boolean;
  disabledLabel?: string;
  compact?: boolean;
}) {
  return (
    <div
      onClick={() => !disabled && inputRef.current?.click()}
      onDragOver={(e) => e.preventDefault()}
      onDragEnter={(e) => {
        e.preventDefault();
        if (!disabled) onDragEnter(e);
      }}
      onDragLeave={(e) => {
        e.preventDefault();
        if (e.currentTarget === e.target) onDragLeave(e);
      }}
      onDrop={(e) => {
        if (disabled) return;
        onDrop(e, slot);
      }}
      role="button"
      tabIndex={disabled ? -1 : 0}
      className="surface flex flex-col items-center justify-center gap-2 cursor-pointer transition-all px-4 text-center"
      style={{
        minHeight: compact ? 96 : 120,
        opacity: disabled ? 0.5 : 1,
        cursor: disabled ? "not-allowed" : "pointer",
        boxShadow: dragging
          ? "inset 0 0 0 2px var(--color-tangerine), 0 6px 20px var(--shadow-tint)"
          : undefined,
      }}
    >
      <Icon
        size={compact ? 28 : 32}
        style={{
          color: file
            ? "var(--color-tangerine)"
            : "var(--color-teal)",
        }}
      />
      <div className="space-y-0.5 max-w-full">
        <div className="text-sm font-bold text-primary truncate">
          {disabled
            ? disabledLabel ?? "Disabled"
            : file
            ? file.name
            : title}
        </div>
        <div className="text-xs text-muted">
          {file ? (
            <span
              className="inline-flex items-center gap-1"
              style={{ color: "var(--color-teal)" }}
            >
              <RiCheckLine size={12} /> Ready
            </span>
          ) : (
            hint
          )}
        </div>
      </div>
      <input
        ref={inputRef}
        hidden
        type="file"
        accept={accept}
        onChange={(e) => onPick(e, slot)}
      />
    </div>
  );
}
