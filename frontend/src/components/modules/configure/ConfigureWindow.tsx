"use client";

import { RiFolderSettingsLine, RiShieldCheckLine } from "@remixicon/react";

import { useBackendBaseUrl } from "@/src/hooks/usePythonAPI";
import { useJobStore } from "@/src/store/useJobStore";

export function ConfigureWindow() {
  const config = useJobStore((state) => state.config);
  const files = useJobStore((state) => state.files);
  const tcRows = useJobStore((state) => state.tcRows);
  const updateConfig = useJobStore((state) => state.updateConfig);
  const backendBaseUrl = useBackendBaseUrl();

  const estimatedCalls = tcRows.length
    ? Math.ceil(tcRows.length / Math.max(config.batchSize, 1))
    : 0;

  return (
    <div className="window-content-grid">
      <div className="sunken-panel accent-panel">
        <div>
          <p className="eyebrow">Phase 1 / Configure</p>
          <h2>Shape the job before you spend tokens.</h2>
          <p>
            This board centralizes the operational knobs that will later drive
            the real Python backend, without forcing the operator back into the
            upload window.
          </p>
        </div>
        <div className="metric-strip">
          <div className="metric-card">
            <span className="metric-label">Queued rows</span>
            <strong>{tcRows.length}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">API calls</span>
            <strong>{estimatedCalls}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Backend</span>
            <strong>{backendBaseUrl ? "bound" : "unset"}</strong>
          </div>
        </div>
      </div>

      <div className="window-columns">
        <div className="sunken-panel">
          <h3>Execution Controls</h3>
          <div className="config-grid stacked">
            <label>
              <span>Anthropic model</span>
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
              <span>Budget ceiling</span>
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
              <span>Strict validation gate</span>
            </label>
          </div>
        </div>

        <div className="sunken-panel">
          <h3>Job Readiness</h3>
          <div className="checklist-panel">
            <div className="checklist-row">
              <RiFolderSettingsLine size={16} />
              <div>
                <strong>Raw workbook</strong>
                <p>{files.raw?.name ?? "Not staged yet"}</p>
              </div>
            </div>
            <div className="checklist-row">
              <RiFolderSettingsLine size={16} />
              <div>
                <strong>Supplementary spec</strong>
                <p>{files.spec?.name ?? "Optional and currently empty"}</p>
              </div>
            </div>
            <div className="checklist-row">
              <RiShieldCheckLine size={16} />
              <div>
                <strong>Validation mode</strong>
                <p>
                  {config.strictValidation
                    ? "Blocking invalid rows before export."
                    : "Warnings only. Invalid rows can still be written."}
                </p>
              </div>
            </div>
          </div>

          <div className="sunken-subpanel">
            <h4>Backend binding</h4>
            <p>
              {backendBaseUrl
                ? backendBaseUrl
                : "Set NEXT_PUBLIC_PYTHON_API_BASE to bind this desktop to the Python service."}
            </p>
          </div>

          <div className="sunken-subpanel">
            <h4>Throughput preview</h4>
            <p>
              {tcRows.length
                ? `${tcRows.length} rows will be split into ${estimatedCalls} call(s) at the current batch size.`
                : "Load a workbook first to estimate runtime and cost cadence."}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
