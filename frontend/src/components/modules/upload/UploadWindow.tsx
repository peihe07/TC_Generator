"use client";

import { ChangeEvent, useRef, useState, useTransition } from "react";
import * as XLSX from "xlsx";
import { RiDeleteBinLine, RiUploadCloud2Line } from "@remixicon/react";

import { useBackendBaseUrl, useTriggerParse } from "@/src/hooks/usePythonAPI";
import type { TcPreviewRow } from "@/src/lib/types";
import { useJobStore } from "@/src/store/useJobStore";

const ACCEPTED_RAW_FILES = ".xlsx,.xlsm";
const ACCEPTED_SPEC_FILES = ".pdf,.docx,.xlsx";

function readWorkbookPreview(file: File): Promise<{
  headers: string[];
  rows: TcPreviewRow[];
}> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onerror = () => reject(new Error("Failed to read workbook."));
    reader.onload = (event) => {
      try {
        const data = event.target?.result;
        const workbook = XLSX.read(data, { type: "array" });
        const worksheet = workbook.Sheets[workbook.SheetNames[0]];
        const table = XLSX.utils.sheet_to_json<(string | number | null)[]>(worksheet, {
          header: 1,
          defval: null,
        });
        const [headerRow = [], ...bodyRows] = table;
        const headers = headerRow.map((cell, index) =>
          String(cell ?? `Column ${index + 1}`),
        );
        const rows = bodyRows.slice(0, 5).map((row, rowIndex) =>
          headers.reduce<TcPreviewRow>((acc, header, columnIndex) => {
            acc[header] = row[columnIndex] ?? null;
            acc.__row = rowIndex + 1;
            return acc;
          }, {}),
        );

        resolve({ headers, rows });
      } catch (error) {
        reject(error instanceof Error ? error : new Error("Invalid workbook."));
      }
    };

    reader.readAsArrayBuffer(file);
  });
}

export function UploadWindow() {
  const rawFile = useJobStore((state) => state.files.raw);
  const specFile = useJobStore((state) => state.files.spec);
  const setJobId = useJobStore((state) => state.setJobId);
  const previewHeaders = useJobStore((state) => state.previewHeaders);
  const previewRows = useJobStore((state) => state.previewRows);
  const logs = useJobStore((state) => state.logs);
  const stats = useJobStore((state) => state.stats);
  const config = useJobStore((state) => state.config);
  const setFiles = useJobStore((state) => state.setFiles);
  const setPreview = useJobStore((state) => state.setPreview);
  const setRows = useJobStore((state) => state.setRows);
  const updateConfig = useJobStore((state) => state.updateConfig);
  const appendLog = useJobStore((state) => state.appendLog);
  const resetJob = useJobStore((state) => state.resetJob);
  const backendBaseUrl = useBackendBaseUrl();
  const triggerParse = useTriggerParse();
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();
  const rawInputRef = useRef<HTMLInputElement | null>(null);
  const specInputRef = useRef<HTMLInputElement | null>(null);

  const handleRawFile = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) {
      return;
    }

    if (!file.name.toLowerCase().endsWith(".xlsx") && !file.name.toLowerCase().endsWith(".xlsm")) {
      setError("Raw workbook must be an .xlsx or .xlsm file.");
      return;
    }

    setError(null);
    setFiles({ raw: file, parsed: false });
    appendLog({
      level: "info",
      message: backendBaseUrl
        ? `Loaded ${file.name}. Sending workbook to backend parse endpoint.`
        : `Loaded ${file.name}. Parsing the first five rows locally for preview.`,
    });

    startTransition(async () => {
      try {
        if (backendBaseUrl) {
          const payload = new FormData();
          payload.append("raw_file", file);
          if (specFile) {
            payload.append("spec_file", specFile);
          }

          const response = await triggerParse.mutateAsync(payload);
          setJobId(response.jobId);
          setPreview(response.previewHeaders, response.previewRows);
          setRows(response.rows);
          setFiles({ raw: file, parsed: true });
          appendLog({
            level: "info",
            message: `Backend parse complete: ${response.rowCount} rows, project ${response.project ?? "N/A"}, group ${response.testGroup ?? "N/A"}.`,
          });
          return;
        }

        const preview = await readWorkbookPreview(file);
        setPreview(preview.headers, preview.rows);
        setFiles({ raw: file, parsed: true });
        const reqKey =
          preview.headers.find((header) => /requirement|req id/i.test(header)) ??
          preview.headers[0] ??
          "Column 1";
        const itemKey =
          preview.headers.find((header) => /test item/i.test(header)) ??
          preview.headers[1] ??
          reqKey;
        setRows(
          preview.rows.map((row, index) => ({
            id: `preview-${index + 1}`,
            rowNum: index + 1,
            reqId: String(row[reqKey] ?? `ROW-${index + 1}`),
            testItem: String(row[itemKey] ?? ""),
            originalRequirement: String(row[itemKey] ?? ""),
            status: "draft",
            reviewStatus: "pending",
          })),
        );
        appendLog({
          level: "info",
          message: `Preview ready: ${preview.rows.length} rows from ${file.name}.`,
        });
      } catch (previewError) {
        setError(
          previewError instanceof Error
            ? previewError.message
            : "Failed to parse workbook preview.",
        );
        appendLog({
          level: "error",
          message: backendBaseUrl
            ? "Backend parse failed. Check API availability and workbook validity."
            : "Workbook preview failed. Check whether the selected file is a valid Excel document.",
        });
      }
    });
  };

  const handleSpecFile = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) {
      return;
    }

    setFiles({ spec: file });
    appendLog({
      level: "info",
      message: `Attached supplementary spec: ${file.name}.`,
    });
  };

  return (
    <div className={`window-content-grid ${isPending ? "is-busy" : ""}`}>
      <div className="sunken-panel accent-panel">
        <div>
          <p className="eyebrow">Phase 1 / Upload</p>
          <h2>Work like a desktop operator, not a wizard.</h2>
          <p>
            Stage the raw workbook, inspect a five-row preview, then carry the
            session into setup and generation windows without leaving the desktop.
          </p>
        </div>
        <div className="metric-strip">
          <div className="metric-card">
            <span className="metric-label">Rows</span>
            <strong>{previewRows.length || stats.total}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Batch</span>
            <strong>{config.batchSize}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Budget</span>
            <strong>${config.budget.toFixed(2)}</strong>
          </div>
        </div>
      </div>

      <div className="window-columns">
        <div className="sunken-panel">
          <h3>Source Cabinet</h3>
          <div className="upload-stack">
            <label className="upload-dropzone" htmlFor="raw-file-input">
              <RiUploadCloud2Line size={28} />
              <span>Raw workbook</span>
              <small>{rawFile?.name ?? "Choose .xlsx / .xlsm"}</small>
            </label>
            <input
              ref={rawInputRef}
              id="raw-file-input"
              type="file"
              accept={ACCEPTED_RAW_FILES}
              onChange={handleRawFile}
              hidden
            />

            <label className="upload-dropzone secondary" htmlFor="spec-file-input">
              <RiUploadCloud2Line size={24} />
              <span>Supplementary spec</span>
              <small>{specFile?.name ?? "Optional .pdf / .docx / .xlsx"}</small>
            </label>
            <input
              ref={specInputRef}
              id="spec-file-input"
              type="file"
              accept={ACCEPTED_SPEC_FILES}
              onChange={handleSpecFile}
              hidden
            />
          </div>

          <div className="config-grid">
            <label>
              <span>Model</span>
              <select
                value={config.model}
                onChange={(event) => updateConfig({ model: event.target.value })}
              >
                <option value="claude-sonnet-4-6">claude-sonnet-4-6</option>
                <option value="claude-haiku-4-5-20251001">
                  claude-haiku-4-5-20251001
                </option>
              </select>
            </label>
            <label>
              <span>Batch size</span>
              <input
                type="number"
                min={1}
                max={20}
                value={config.batchSize}
                onChange={(event) =>
                  updateConfig({ batchSize: Number(event.target.value) || 1 })
                }
              />
            </label>
            <label>
              <span>Budget</span>
              <input
                type="number"
                min={0.1}
                step={0.1}
                value={config.budget}
                onChange={(event) =>
                  updateConfig({ budget: Number(event.target.value) || 0.1 })
                }
              />
            </label>
            <label className="checkbox-row">
              <input
                type="checkbox"
                checked={config.strictValidation}
                onChange={(event) =>
                  updateConfig({ strictValidation: event.target.checked })
                }
              />
              <span>Strict validation</span>
            </label>
          </div>

          <div className="button-row">
            <button type="button" onClick={() => rawInputRef.current?.click()}>
              Pick workbook
            </button>
            <button type="button" onClick={() => specInputRef.current?.click()}>
              Attach spec
            </button>
            <button type="button" onClick={resetJob}>
              <RiDeleteBinLine size={14} />
              Reset
            </button>
          </div>

          {error ? <p className="error-line">{error}</p> : null}
        </div>

        <div className="sunken-panel">
          <h3>Workbook Preview</h3>
          {previewRows.length ? (
            <div className="preview-table-wrapper">
              <table className="preview-table">
                <thead>
                  <tr>
                    {previewHeaders.map((header) => (
                      <th key={header}>{header}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {previewRows.map((row, index) => (
                    <tr key={`${row.__row ?? "row"}-${index}`}>
                      {previewHeaders.map((header) => (
                        <td key={`${index}-${header}`}>
                          {row[header] === null ? "—" : String(row[header])}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="empty-state">
              <p>No workbook preview yet.</p>
              <small>
                Once you select an Excel file, the first five rows appear here
                before any backend round-trip.
              </small>
            </div>
          )}
        </div>
      </div>

      <div className="sunken-panel">
        <h3>Session Console</h3>
        <div className="log-list">
          {logs.slice(-6).map((log, index) => (
            <div key={`${log.timestamp}-${index}`} className={`log-entry ${log.level}`}>
              <span>[{log.timestamp}]</span>
              <span>{log.message}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
