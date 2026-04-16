"use client";

import { useEffect, useMemo, useState } from "react";
import {
  RiAlertLine,
  RiCheckboxCircleLine,
  RiCloseCircleLine,
  RiEdit2Line,
  RiFlagLine,
} from "@remixicon/react";

import type { TcRow, ValidationIssue, ValidationSeverity } from "@/src/lib/types";
import { useJobStore } from "@/src/store/useJobStore";

function getSeverityWeight(severity: ValidationSeverity) {
  switch (severity) {
    case "critical":
      return 3;
    case "warning":
      return 2;
    default:
      return 1;
  }
}

function buildInlineDiff(original: string, generated: string) {
  if (!generated) {
    return { originalHtml: original, generatedHtml: generated };
  }

  const originalTokens = original.split(/(\s+)/);
  const generatedTokens = generated.split(/(\s+)/);

  const originalSet = new Set(originalTokens.filter(Boolean));
  const generatedSet = new Set(generatedTokens.filter(Boolean));

  const originalHtml = originalTokens
    .map((token) =>
      token.trim() && !generatedSet.has(token)
        ? `<del>${token}</del>`
        : token,
    )
    .join("");

  const generatedHtml = generatedTokens
    .map((token) =>
      token.trim() && !originalSet.has(token)
        ? `<ins>${token}</ins>`
        : token,
    )
    .join("");

  return { originalHtml, generatedHtml };
}

function summarizeValidation(issues: ValidationIssue[] | undefined) {
  const counts = {
    critical: 0,
    warning: 0,
    passing: 0,
  };

  (issues ?? []).forEach((issue) => {
    counts[issue.severity] += 1;
  });

  return counts;
}

function ValidationBadge({ issues }: { issues: ValidationIssue[] | undefined }) {
  const counts = summarizeValidation(issues);
  if (counts.critical) {
    return <span className="review-badge critical">{counts.critical} critical</span>;
  }
  if (counts.warning) {
    return <span className="review-badge warning">{counts.warning} warning</span>;
  }
  return <span className="review-badge passing">passing</span>;
}

export function ReviewWindow() {
  const tcRows = useJobStore((state) => state.tcRows);
  const updateRow = useJobStore((state) => state.updateRow);
  const [selectedRowId, setSelectedRowId] = useState<string | null>(null);
  const [statusFilter, setStatusFilter] = useState<"all" | TcRow["reviewStatus"]>("all");
  const [validationFilter, setValidationFilter] = useState<"all" | ValidationSeverity>("all");
  const [isEditing, setIsEditing] = useState(false);
  const [draftFields, setDraftFields] = useState({
    preConditions: "",
    testProcedure: "",
    expectedResult: "",
  });

  const sortedRows = useMemo(() => {
    return [...tcRows].sort((a, b) => {
      const aSeverity = Math.max(
        ...(a.validation?.map((issue) => getSeverityWeight(issue.severity)) ?? [0]),
      );
      const bSeverity = Math.max(
        ...(b.validation?.map((issue) => getSeverityWeight(issue.severity)) ?? [0]),
      );
      return bSeverity - aSeverity;
    });
  }, [tcRows]);

  const filteredRows = useMemo(() => {
    return sortedRows.filter((row) => {
      const statusMatch =
        statusFilter === "all" ? true : row.reviewStatus === statusFilter;
      const validationMatch =
        validationFilter === "all"
          ? true
          : (row.validation ?? []).some((issue) => issue.severity === validationFilter);
      return statusMatch && validationMatch;
    });
  }, [sortedRows, statusFilter, validationFilter]);

  const selectedRow =
    filteredRows.find((row) => row.id === selectedRowId) ??
    filteredRows[0] ??
    null;

  useEffect(() => {
    setDraftFields({
      preConditions: selectedRow?.generated?.preConditions ?? "",
      testProcedure: selectedRow?.generated?.testProcedure ?? "",
      expectedResult: selectedRow?.generated?.expectedResult ?? "",
    });
    setIsEditing(false);
  }, [selectedRow?.id]);

  const originalText = selectedRow?.originalRequirement ?? selectedRow?.testItem ?? "";
  const generatedText =
    selectedRow?.generated?.testItemRewrite ??
    "No generated rewrite yet. Start a mock run in the Generate window first.";
  const diff = buildInlineDiff(originalText, generatedText);

  const acceptAllPassing = () => {
    filteredRows.forEach((row) => {
      if (!(row.validation ?? []).some((issue) => issue.severity === "critical")) {
        updateRow(row.id, { reviewStatus: "accepted" });
      }
    });
  };

  const saveEdits = () => {
    if (!selectedRow?.generated) {
      return;
    }

    updateRow(selectedRow.id, {
      generated: {
        ...selectedRow.generated,
        preConditions: draftFields.preConditions,
        testProcedure: draftFields.testProcedure,
        expectedResult: draftFields.expectedResult,
      },
      reviewStatus: "pending",
    });
    setIsEditing(false);
  };

  return (
    <div className="window-content-grid">
      <div className="sunken-panel accent-panel">
        <div>
          <p className="eyebrow">Phase 1 / Review</p>
          <h2>Inspect every generated row before it becomes an artifact.</h2>
          <p>
            The review desk now lets you filter rows, inspect a compact diff,
            and stamp each row as accepted, rejected, or flagged for human follow-up.
          </p>
        </div>
        <div className="metric-strip">
          <div className="metric-card">
            <span className="metric-label">Rows in scope</span>
            <strong>{filteredRows.length}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Accepted</span>
            <strong>{tcRows.filter((row) => row.reviewStatus === "accepted").length}</strong>
          </div>
          <div className="metric-card">
            <span className="metric-label">Flagged</span>
            <strong>{tcRows.filter((row) => row.reviewStatus === "flagged").length}</strong>
          </div>
        </div>
      </div>

      <div className="review-toolbar sunken-panel">
        <label>
          <span>Review status</span>
          <select
            value={statusFilter}
            onChange={(event) =>
              setStatusFilter(event.target.value as "all" | TcRow["reviewStatus"])
            }
          >
            <option value="all">All</option>
            <option value="pending">Pending</option>
            <option value="accepted">Accepted</option>
            <option value="rejected">Rejected</option>
            <option value="flagged">Flagged</option>
          </select>
        </label>
        <label>
          <span>Validation</span>
          <select
            value={validationFilter}
            onChange={(event) =>
              setValidationFilter(event.target.value as "all" | ValidationSeverity)
            }
          >
            <option value="all">All</option>
            <option value="critical">Critical</option>
            <option value="warning">Warning</option>
            <option value="passing">Passing</option>
          </select>
        </label>
        <button type="button" onClick={acceptAllPassing}>
          <RiCheckboxCircleLine size={14} />
          Accept all passing
        </button>
      </div>

      <div className="review-layout">
        <div className="sunken-panel review-list-panel">
          <h3>Generated Rows</h3>
          <div className="review-row-list">
            {filteredRows.length ? (
              filteredRows.map((row) => (
                <button
                  key={row.id}
                  type="button"
                  className={`review-row-card ${selectedRow?.id === row.id ? "selected" : ""}`}
                  onClick={() => setSelectedRowId(row.id)}
                >
                  <div className="review-row-head">
                    <strong>{row.reqId}</strong>
                    <ValidationBadge issues={row.validation} />
                  </div>
                  <p>{row.testItem || "No test item text."}</p>
                  <div className="review-row-foot">
                    <span>{row.reviewStatus ?? "pending"}</span>
                    <span>{row.generated?.priority ?? row.priority ?? "NA"}</span>
                  </div>
                </button>
              ))
            ) : (
              <div className="empty-state">
                <p>No rows match the current filters.</p>
              </div>
            )}
          </div>
        </div>

        <div className="sunken-panel review-main-panel">
          <h3>Diff View</h3>
          {selectedRow ? (
            <div className="review-main-grid">
              <div className="diff-column">
                <h4>Original Requirement</h4>
                <div
                  className="diff-box"
                  dangerouslySetInnerHTML={{ __html: diff.originalHtml || "No source text." }}
                />
              </div>
              <div className="diff-column">
                <h4>Generated Rewrite</h4>
                <div
                  className="diff-box"
                  dangerouslySetInnerHTML={{ __html: diff.generatedHtml }}
                />
              </div>
              <div className="sunken-subpanel review-generated-fields">
                <h4>Generated Fields</h4>
                {isEditing ? (
                  <div className="edit-field-stack">
                    <label>
                      <span>Pre-conditions</span>
                      <textarea
                        value={draftFields.preConditions}
                        onChange={(event) =>
                          setDraftFields((current) => ({
                            ...current,
                            preConditions: event.target.value,
                          }))
                        }
                      />
                    </label>
                    <label>
                      <span>Procedure</span>
                      <textarea
                        value={draftFields.testProcedure}
                        onChange={(event) =>
                          setDraftFields((current) => ({
                            ...current,
                            testProcedure: event.target.value,
                          }))
                        }
                      />
                    </label>
                    <label>
                      <span>Expected</span>
                      <textarea
                        value={draftFields.expectedResult}
                        onChange={(event) =>
                          setDraftFields((current) => ({
                            ...current,
                            expectedResult: event.target.value,
                          }))
                        }
                      />
                    </label>
                  </div>
                ) : (
                  <dl>
                    <dt>Pre-conditions</dt>
                    <dd>{selectedRow.generated?.preConditions ?? "Not generated yet."}</dd>
                    <dt>Procedure</dt>
                    <dd>{selectedRow.generated?.testProcedure ?? "Not generated yet."}</dd>
                    <dt>Expected</dt>
                    <dd>{selectedRow.generated?.expectedResult ?? "Not generated yet."}</dd>
                  </dl>
                )}
              </div>
            </div>
          ) : (
            <div className="empty-state">
              <p>No generated rows available.</p>
              <small>Start a mock run first so the review desk has data to inspect.</small>
            </div>
          )}
        </div>

        <div className="sunken-panel review-sidebar">
          <h3>Validation Panel</h3>
          {selectedRow ? (
            <>
              <div className="review-action-row">
                <button
                  type="button"
                  onClick={() => updateRow(selectedRow.id, { reviewStatus: "accepted" })}
                >
                  <RiCheckboxCircleLine size={14} />
                  Accept
                </button>
                <button
                  type="button"
                  onClick={() => updateRow(selectedRow.id, { reviewStatus: "rejected" })}
                >
                  <RiCloseCircleLine size={14} />
                  Reject
                </button>
                <button
                  type="button"
                  onClick={() => updateRow(selectedRow.id, { reviewStatus: "flagged" })}
                >
                  <RiFlagLine size={14} />
                  Flag
                </button>
                <button
                  type="button"
                  onClick={() => {
                    if (isEditing) {
                      saveEdits();
                      return;
                    }
                    setIsEditing(true);
                  }}
                >
                  <RiEdit2Line size={14} />
                  {isEditing ? "Save" : "Edit"}
                </button>
                {isEditing ? (
                  <button type="button" onClick={() => setIsEditing(false)}>
                    Cancel
                  </button>
                ) : null}
              </div>

              <div className="validation-list">
                {(selectedRow.validation ?? []).length ? (
                  selectedRow.validation?.map((issue) => (
                    <div key={issue.id} className={`validation-item ${issue.severity}`}>
                      {issue.severity === "critical" ? (
                        <RiCloseCircleLine size={14} />
                      ) : issue.severity === "warning" ? (
                        <RiAlertLine size={14} />
                      ) : (
                        <RiCheckboxCircleLine size={14} />
                      )}
                      <div>
                        <strong>{issue.field}</strong>
                        <p>{issue.message}</p>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="empty-state">
                    <p>No validation results for this row.</p>
                  </div>
                )}
              </div>
            </>
          ) : (
            <div className="empty-state">
              <p>Select a row to inspect details.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
