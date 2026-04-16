"use client";

import { useMemo, useState } from "react";
import {
  RiCheckboxCircleLine,
  RiDownload2Line,
  RiFileExcel2Line,
  RiFolderZipLine,
} from "@remixicon/react";

import { useJobStore } from "@/src/store/useJobStore";

const columnOptions = [
  "TC ID",
  "Requirement ID",
  "Test Set",
  "Original Requirement",
  "Test Item Rewrite",
  "Pre-Conditions",
  "Test Procedure",
  "Expected Result",
  "Priority",
  "Validation Summary",
] as const;

type ExportScope = "all" | "accepted" | "flagged";
type OutputMode = "new-file" | "overwrite";

export function ExportWindow() {
  const tcRows = useJobStore((state) => state.tcRows);
  const logs = useJobStore((state) => state.logs);
  const [scope, setScope] = useState<ExportScope>("accepted");
  const [outputMode, setOutputMode] = useState<OutputMode>("new-file");
  const [includeFrameworkSheet, setIncludeFrameworkSheet] = useState(true);
  const [selectedColumns, setSelectedColumns] = useState<string[]>([
    "TC ID",
    "Requirement ID",
    "Test Item Rewrite",
    "Expected Result",
    "Validation Summary",
  ]);
  const [downloadReady, setDownloadReady] = useState(false);

  const scopedRows = useMemo(() => {
    if (scope === "all") {
      return tcRows;
    }
    if (scope === "accepted") {
      return tcRows.filter((row) => row.reviewStatus === "accepted");
    }
    return tcRows.filter((row) => row.reviewStatus === "flagged");
  }, [scope, tcRows]);

  const toggleColumn = (column: string) => {
    setSelectedColumns((current) =>
      current.includes(column)
        ? current.filter((item) => item !== column)
        : [...current, column],
    );
  };

  return (
    <div className="window-content-grid">
      <div className="sunken-panel accent-panel">
        <div>
          <p className="eyebrow">Phase 1 / Export</p>
          <h2>Package the reviewed rows like a release artifact.</h2>
          <p>
            This cabinet models export scope, output mode, and column selection
            so the backend handoff can later plug into a stable desktop workflow.
          </p>
        </div>
        <div className="metric-strip">
          <div className="metric-card">
            <span className="metric-label">Rows queued</span>
            <strong>{scopedRows.length}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Columns</span>
            <strong>{selectedColumns.length}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Package</span>
            <strong>{downloadReady ? "ready" : "draft"}</strong>
          </div>
        </div>
      </div>

      <div className="window-columns">
        <div className="sunken-panel">
          <h3>Export Scope</h3>
          <div className="radio-stack">
            <label>
              <input
                type="radio"
                name="scope"
                checked={scope === "all"}
                onChange={() => setScope("all")}
              />
              <span>All generated rows</span>
            </label>
            <label>
              <input
                type="radio"
                name="scope"
                checked={scope === "accepted"}
                onChange={() => setScope("accepted")}
              />
              <span>Accepted only</span>
            </label>
            <label>
              <input
                type="radio"
                name="scope"
                checked={scope === "flagged"}
                onChange={() => setScope("flagged")}
              />
              <span>Flagged only</span>
            </label>
          </div>

          <h3 className="subheading">Output Mode</h3>
          <div className="radio-stack">
            <label>
              <input
                type="radio"
                name="output-mode"
                checked={outputMode === "new-file"}
                onChange={() => setOutputMode("new-file")}
              />
              <span>Create `{`{input}_generated.xlsx`}`</span>
            </label>
            <label>
              <input
                type="radio"
                name="output-mode"
                checked={outputMode === "overwrite"}
                onChange={() => setOutputMode("overwrite")}
              />
              <span>Overwrite original workbook</span>
            </label>
          </div>

          <label className="checkbox-row export-toggle">
            <input
              type="checkbox"
              checked={includeFrameworkSheet}
              onChange={(event) => setIncludeFrameworkSheet(event.target.checked)}
            />
            <span>Include framework sheet</span>
          </label>
        </div>

        <div className="sunken-panel">
          <h3>Column Selection</h3>
          <div className="checkbox-grid">
            {columnOptions.map((column) => (
              <label key={column} className="checkbox-row export-column">
                <input
                  type="checkbox"
                  checked={selectedColumns.includes(column)}
                  onChange={() => toggleColumn(column)}
                />
                <span>{column}</span>
              </label>
            ))}
          </div>

          <div className="sunken-subpanel export-preview">
            <h4>Payload Preview</h4>
            <ul>
              <li>{scopedRows.length} row(s) selected</li>
              <li>{selectedColumns.length} column(s) included</li>
              <li>{includeFrameworkSheet ? "Framework sheet included" : "Framework sheet skipped"}</li>
              <li>{outputMode === "new-file" ? "New workbook" : "Overwrite mode"}</li>
            </ul>
          </div>
        </div>
      </div>

      <div className="sunken-panel export-footer">
        <div className="export-actions">
          <button
            type="button"
            onClick={() => setDownloadReady(true)}
            disabled={!scopedRows.length}
          >
            <RiFolderZipLine size={14} />
            Prepare package
          </button>
          <button type="button" disabled={!downloadReady}>
            <RiDownload2Line size={14} />
            Download workbook
          </button>
        </div>

        <div className="export-summary">
          {downloadReady ? (
            <>
              <RiCheckboxCircleLine size={16} />
              <span>
                Package prepared. Backend wiring can later replace this button with a signed download URL.
              </span>
            </>
          ) : (
            <>
              <RiFileExcel2Line size={16} />
              <span>
                Waiting for an export package. Latest desktop activity: {logs.at(-1)?.message ?? "No logs yet."}
              </span>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
