'use client';

import React, { useEffect, useMemo, useRef, useState } from 'react';
import {
  RiCheckboxCircleLine,
  RiDownload2Line,
  RiErrorWarningLine,
  RiFlagLine,
  RiInformationLine,
  RiRefreshLine,
} from '@remixicon/react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { DESIGN_METHODS, TcRow, TcStatus } from '../../../lib/types';

type ReviewFilter = 'all' | 'reviewing' | 'accepted' | 'flagged' | 'warnings';

const FILTERS: Array<{ id: ReviewFilter; label: string }> = [
  { id: 'all', label: 'All' },
  { id: 'reviewing', label: 'Reviewing' },
  { id: 'accepted', label: 'Accepted' },
  { id: 'flagged', label: 'Flagged' },
  { id: 'warnings', label: 'Warnings' },
];

function statusLabel(status: TcStatus): string {
  if (status === 'accepted') return 'Accepted';
  if (status === 'flagged') return 'Flagged';
  if (status === 'rejected') return 'Rejected';
  if (status === 'fail') return 'Failed';
  if (status === 'generating') return 'Generating';
  return 'Reviewing';
}

function firstLine(value: string, fallback = 'No content'): string {
  const trimmed = value.trim();
  if (!trimmed) return fallback;
  return trimmed.split('\n')[0];
}

function splitLabel(row: TcRow): string | null {
  const decision = row.splitDecision;
  if (!decision || decision.tcCount <= 1) return null;
  return `Split ${(decision.subIndex ?? 0) + 1}/${decision.tcCount}`;
}

function splitGroupLabel(row: TcRow): string | null {
  const decision = row.splitDecision;
  if (!decision || decision.tcCount <= 1) return null;
  return `Original req ${decision.reqId || row.reqId}`;
}

function FieldBlock({ label, value }: { label: string; value: string }) {
  return (
    <section className="modern-review-field">
      <div className="modern-review-field-label">{label}</div>
      <div className="modern-review-field-value">{value || '-'}</div>
    </section>
  );
}

type EditValues = {
  preConditions: string;
  inputTestData: string;
  steps: string;
  expectedResults: string;
  priority: string;
  designMethod: string;
};

function EditField({
  label,
  value,
  onChange,
  minRows = 3,
}: {
  label: string;
  value: string;
  onChange: (value: string) => void;
  minRows?: number;
}) {
  return (
    <label className="modern-review-edit-field">
      <span>{label}</span>
      <textarea
        value={value}
        onChange={(event) => onChange(event.target.value)}
        rows={minRows}
      />
    </label>
  );
}

function GeneratedEditForm({
  values,
  onChange,
}: {
  values: EditValues;
  onChange: (values: Partial<EditValues>) => void;
}) {
  return (
    <div className="modern-review-edit-stack">
      <div className="modern-review-edit-inline">
        <label>
          <span>Priority</span>
          <input
            value={values.priority}
            onChange={(event) => onChange({ priority: event.target.value })}
          />
        </label>
        <label>
          <span>Design method</span>
          <select
            value={values.designMethod}
            onChange={(event) => onChange({ designMethod: event.target.value })}
          >
            <option value="">Select method...</option>
            {values.designMethod &&
            !DESIGN_METHODS.includes(values.designMethod as typeof DESIGN_METHODS[number]) ? (
              <option value={values.designMethod}>
                Custom: {values.designMethod}
              </option>
            ) : null}
            {DESIGN_METHODS.map((method) => (
              <option key={method} value={method}>
                {method}
              </option>
            ))}
          </select>
        </label>
      </div>
      <EditField
        label="Pre-conditions"
        value={values.preConditions}
        onChange={(value) => onChange({ preConditions: value })}
      />
      <EditField
        label="Input test data"
        value={values.inputTestData}
        onChange={(value) => onChange({ inputTestData: value })}
        minRows={2}
      />
      <EditField
        label="Test procedure"
        value={values.steps}
        onChange={(value) => onChange({ steps: value })}
        minRows={7}
      />
      <EditField
        label="Expected result"
        value={values.expectedResults}
        onChange={(value) => onChange({ expectedResults: value })}
        minRows={7}
      />
    </div>
  );
}

function DecisionButton({
  children,
  onClick,
  variant = 'default',
}: {
  children: React.ReactNode;
  onClick: () => void;
  variant?: 'default' | 'accept' | 'flag' | 'reject';
}) {
  return (
    <button type="button" className={`modern-review-action ${variant}`} onClick={onClick}>
      {children}
    </button>
  );
}

export default function ModernReviewModule() {
  const { tcRows, updateTcRow, jobMetadata, stats } = useJobStore();
  const { advanceWindow } = useWindowStore();
  const [filter, setFilter] = useState<ReviewFilter>('all');
  const [query, setQuery] = useState('');
  const [activeId, setActiveId] = useState<string | null>(tcRows[0]?.id ?? null);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editValues, setEditValues] = useState<EditValues>({
    preConditions: '',
    inputTestData: '',
    steps: '',
    expectedResults: '',
    priority: '',
    designMethod: '',
  });
  const editorPanelRef = useRef<HTMLElement | null>(null);

  const filteredRows = useMemo(() => {
    const needle = query.trim().toLowerCase();
    return tcRows.filter((row) => {
      if (filter === 'reviewing' && row.status !== 'reviewing' && row.status !== 'pending') return false;
      if (filter === 'accepted' && row.status !== 'accepted') return false;
      if (filter === 'flagged' && row.status !== 'flagged') return false;
      if (filter === 'warnings' && !(row.validationErrors?.length)) return false;
      if (!needle) return true;
      return [row.tcId, row.reqId, row.tcTitle, row.testItem]
        .filter(Boolean)
        .some((value) => String(value).toLowerCase().includes(needle));
    });
  }, [filter, query, tcRows]);

  const activeRow = tcRows.find((row) => row.id === activeId) ?? filteredRows[0] ?? tcRows[0] ?? null;
  const isEditing = Boolean(activeRow && editingId === activeRow.id);
  const activeSplitLabel = activeRow ? splitLabel(activeRow) : null;
  const activeSplitGroupLabel = activeRow ? splitGroupLabel(activeRow) : null;
  const acceptedCount = tcRows.filter((row) => row.status === 'accepted').length;
  const warningCount = tcRows.filter((row) => row.validationErrors?.length).length;
  const flaggedCount = tcRows.filter((row) => row.status === 'flagged').length;

  const setStatus = (status: TcStatus) => {
    if (!activeRow) return;
    updateTcRow(activeRow.id, { status });
  };

  const startEdit = () => {
    if (!activeRow) return;
    setEditingId(activeRow.id);
    setEditValues({
      preConditions: activeRow.preConditions,
      inputTestData: activeRow.inputTestData,
      steps: activeRow.steps,
      expectedResults: activeRow.expectedResults,
      priority: activeRow.priority ?? '',
      designMethod: activeRow.designMethod ?? '',
    });
  };

  const cancelEdit = () => {
    setEditingId(null);
  };

  const saveEdit = () => {
    if (!activeRow) return;
    updateTcRow(activeRow.id, {
      preConditions: editValues.preConditions,
      inputTestData: editValues.inputTestData,
      steps: editValues.steps,
      expectedResults: editValues.expectedResults,
      priority: editValues.priority || undefined,
      designMethod: editValues.designMethod || undefined,
      status: 'reviewing',
    });
    setEditingId(null);
  };

  const updateEditValues = (values: Partial<EditValues>) => {
    setEditValues((current) => ({ ...current, ...values }));
  };

  useEffect(() => {
    if (!isEditing) return;
    editorPanelRef.current?.scrollIntoView({ block: 'start', behavior: 'smooth' });
  }, [isEditing, activeRow?.id]);

  return (
    <div className="modern-review">
      <aside className="modern-review-list-pane">
        <div className="modern-review-summary">
          <div>
            <span>Review Queue</span>
            <strong>{tcRows.length} TCs</strong>
          </div>
          <div>
            <span>Accepted</span>
            <strong>{acceptedCount}</strong>
          </div>
          <div>
            <span>Warnings</span>
            <strong>{warningCount}</strong>
          </div>
        </div>

        <div className="modern-review-filters" role="tablist" aria-label="Review filters">
          {FILTERS.map((item) => (
            <button
              key={item.id}
              type="button"
              data-active={filter === item.id}
              onClick={() => setFilter(item.id)}
            >
              {item.label}
            </button>
          ))}
        </div>

        <input
          className="modern-review-search"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search TC ID, Req ID, title..."
        />

        <div className="modern-review-card-list">
          {filteredRows.map((row) => {
            const rowSplitLabel = splitLabel(row);
            const warningCount = row.validationErrors?.length ?? 0;
            return (
              <button
                key={row.id}
                type="button"
                className="modern-review-card"
                data-active={activeRow?.id === row.id}
                data-split={Boolean(rowSplitLabel)}
                onClick={() => setActiveId(row.id)}
              >
                {rowSplitLabel ? (
                  <div className="modern-review-split-ribbon">
                    <span>{rowSplitLabel}</span>
                    <small>{splitGroupLabel(row)}</small>
                  </div>
                ) : null}
                <div className="modern-review-card-top">
                  <strong title={row.tcId || row.id}>{row.tcId || row.id}</strong>
                  <span className={`modern-review-status ${row.status}`}>{statusLabel(row.status)}</span>
                </div>
                <div className="modern-review-card-title">
                  {row.tcTitle || firstLine(row.testItem)}
                </div>
                <div className="modern-review-card-meta">
                  <span className="req" title={row.reqId}>{row.reqId}</span>
                  {row.priority ? <span>{row.priority}</span> : null}
                  {warningCount > 0 ? (
                    <span className="warn">{warningCount} warning{warningCount > 1 ? 's' : ''}</span>
                  ) : null}
                </div>
              </button>
            );
          })}
        </div>
      </aside>

      <main className="modern-review-detail-pane">
        {!activeRow ? (
          <div className="modern-review-empty">No test cases loaded.</div>
        ) : (
          <>
            <header className="modern-review-detail-header">
              <div>
                <div className="modern-review-eyebrow">{activeRow.reqId}</div>
                <h2>{activeRow.tcTitle || 'Untitled test case'}</h2>
                <div className="modern-review-title-meta">
                  <span>{activeRow.tcId || activeRow.id}</span>
                  <span>{activeRow.testSet || 'No test set'}</span>
                  {activeRow.specReference ? <span>{activeRow.specReference}</span> : null}
                  {activeSplitLabel ? <span className="split">{activeSplitLabel}</span> : null}
                </div>
                {activeSplitGroupLabel ? (
                  <div className="modern-review-split-note">
                    {activeSplitGroupLabel} {'->'} {activeSplitLabel}
                  </div>
                ) : null}
              </div>
              <span className={`modern-review-status large ${activeRow.status}`}>
                {statusLabel(activeRow.status)}
              </span>
            </header>

            {isEditing ? (
              <section ref={editorPanelRef} className="modern-review-editor-panel">
                <div>
                  <div className="modern-review-section-title">Editing generated test case</div>
                  <p>Make review changes here, then save from the decision panel.</p>
                </div>
                <GeneratedEditForm values={editValues} onChange={updateEditValues} />
              </section>
            ) : null}

            {activeRow.splitDecision ? (
              <section className="modern-review-analysis">
                <div className="modern-review-section-title">
                  <RiInformationLine />
                  {activeSplitLabel ? `AI split interpretation - ${activeSplitLabel}` : 'AI requirement interpretation'}
                </div>
                <p>{activeRow.splitDecision.reasoning || 'No split reasoning provided for this sub TC.'}</p>
                {activeRow.splitDecision.keywords?.length ? (
                  <div className="modern-review-keywords">
                    {activeRow.splitDecision.keywords.map((keyword, index) => (
                      <span key={`${keyword.keyword}-${index}`}>
                        <strong>{keyword.keyword}</strong>
                        {(keyword.coveredBy ?? []).length ? ` -> TC ${(keyword.coveredBy ?? []).join(', ')}` : ''}
                      </span>
                    ))}
                  </div>
                ) : null}
              </section>
            ) : null}

            <div className="modern-review-content-grid">
              <section className="modern-review-source">
                <div className="modern-review-section-title">Original requirement</div>
                <p>{activeRow.testItem || '-'}</p>
              </section>
              <section className="modern-review-generated">
                <div className="modern-review-section-title">Generated test case</div>
                <FieldBlock label="Pre-conditions" value={activeRow.preConditions} />
                <FieldBlock label="Input test data" value={activeRow.inputTestData} />
                <FieldBlock label="Test procedure" value={activeRow.steps} />
                <FieldBlock label="Expected result" value={activeRow.expectedResults} />
              </section>
            </div>
          </>
        )}
      </main>

      <aside className="modern-review-inspector">
        <section className="modern-review-inspector-card">
          <div className="modern-review-section-title">
            <RiErrorWarningLine />
            Validation
          </div>
          {!activeRow ? (
            <p className="modern-review-muted">Select a TC to inspect validation.</p>
          ) : activeRow.validationErrors?.length ? (
            <div className="modern-review-issues">
              {activeRow.validationErrors.map((error, index) => (
                <div key={`${error.message}-${index}`} className="modern-review-issue">
                  <strong>{error.severity.toUpperCase()}</strong>
                  <span>{error.message}</span>
                </div>
              ))}
            </div>
          ) : (
            <div className="modern-review-pass">
              <RiCheckboxCircleLine />
              No blocking validation issues.
            </div>
          )}
        </section>

        <section className="modern-review-inspector-card">
          <div className="modern-review-section-title">Decision</div>
          <div className="modern-review-actions">
            {isEditing ? (
              <>
                <DecisionButton variant="accept" onClick={saveEdit}>
                  Save changes
                </DecisionButton>
                <DecisionButton onClick={cancelEdit}>
                  Cancel edit
                </DecisionButton>
              </>
            ) : (
              <>
                <DecisionButton onClick={startEdit}>
                  Edit fields
                </DecisionButton>
                <DecisionButton variant="accept" onClick={() => setStatus('accepted')}>
                  <RiCheckboxCircleLine /> Accept
                </DecisionButton>
                <DecisionButton variant="flag" onClick={() => setStatus('flagged')}>
                  <RiFlagLine /> Flag
                </DecisionButton>
                <DecisionButton variant="reject" onClick={() => setStatus('rejected')}>
                  Reject
                </DecisionButton>
                <DecisionButton onClick={() => setStatus('reviewing')}>
                  <RiRefreshLine /> Back to review
                </DecisionButton>
              </>
            )}
          </div>
        </section>

        <section className="modern-review-inspector-card">
          <div className="modern-review-section-title">Run summary</div>
          <dl className="modern-review-run-summary">
            <div>
              <dt>Job</dt>
              <dd>{jobMetadata?.jobId ?? '-'}</dd>
            </div>
            <div>
              <dt>Cost</dt>
              <dd>${stats.cost.toFixed(4)}</dd>
            </div>
            <div>
              <dt>Flagged</dt>
              <dd>{flaggedCount}</dd>
            </div>
          </dl>
          <button
            type="button"
            className="modern-review-export"
            onClick={() => advanceWindow('review', 'export', 'TC Generator - Export')}
          >
            <RiDownload2Line />
            Export all
          </button>
        </section>
      </aside>
    </div>
  );
}
