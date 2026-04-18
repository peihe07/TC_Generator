'use client';

import React, { useCallback, useMemo, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { TcRow } from '../../../lib/types';
import { createJobLog } from '../../../lib/logging';
import { regenerateRows } from '../../../services/jobAdapter';
import HelpFromAgentButton from '../../system/HelpFromAgentButton';
import {
  RiCheckFill,
  RiCloseFill,
  RiFlagLine,
  RiFlagFill,
  RiEditLine,
  RiSaveLine,
  RiArrowDownSLine,
  RiArrowUpSLine,
  RiErrorWarningFill,
  RiCheckboxCircleFill,
  RiAlertFill,
  RiDownload2Line,
  RiArrowGoBackLine,
  RiDeleteBinLine,
  RiRefreshLine,
  RiCheckboxLine,
  RiCheckboxBlankLine,
  RiFileTextLine,
  RiEditBoxLine,
} from '@remixicon/react';

// --- Word-level diff (LCS) used by RegenDiff ---
type DiffToken = { type: 'same' | 'add' | 'del'; text: string };

function tokenize(text: string): string[] {
  // 以空白/換行/標點為分隔並保留分隔符，讓差異可 word-level 呈現
  return text.split(/(\s+|[,.;:!?()\[\]])/).filter((t) => t !== '');
}

function diffTokens(oldText: string, newText: string): { left: DiffToken[]; right: DiffToken[] } {
  const a = tokenize(oldText);
  const b = tokenize(newText);
  const m = a.length, n = b.length;
  // LCS table
  const dp: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }
  const left: DiffToken[] = [];
  const right: DiffToken[] = [];
  let i = 0, j = 0;
  while (i < m && j < n) {
    if (a[i] === b[j]) {
      left.push({ type: 'same', text: a[i] });
      right.push({ type: 'same', text: b[j] });
      i++; j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) {
      left.push({ type: 'del', text: a[i] });
      i++;
    } else {
      right.push({ type: 'add', text: b[j] });
      j++;
    }
  }
  while (i < m) left.push({ type: 'del', text: a[i++] });
  while (j < n) right.push({ type: 'add', text: b[j++] });
  return { left, right };
}

const DiffText: React.FC<{ tokens: DiffToken[] }> = ({ tokens }) => (
  <span className="whitespace-pre-wrap">
    {tokens.map((t, i) =>
      t.type === 'same'
        ? <span key={i}>{t.text}</span>
        : t.type === 'add'
          ? <span key={i} className="diff-add">{t.text}</span>
          : <span key={i} className="diff-del">{t.text}</span>
    )}
  </span>
);

// --- Stacked field (Excel-column style) used in expanded detail ---
const StackedReadField: React.FC<{
  label: string;
  value: string;
  muted?: boolean;
}> = ({ label, value, muted }) => (
  <div style={{ borderTop: '1px solid #e0e0e0' }}>
    <div
      className="px-2 py-1 font-bold uppercase"
      style={{
        background: '#e8e8e8',
        borderBottom: '1px solid #d0d0d0',
        fontSize: 10,
        color: '#444',
        letterSpacing: 0.5,
      }}
    >
      {label}
    </div>
    <div
      className="selectable px-3 py-2 text-xs whitespace-pre-wrap"
      style={{
        color: muted ? '#808080' : '#000000',
        wordBreak: 'break-word',
        lineHeight: 1.5,
      }}
    >
      {value || '—'}
    </div>
  </div>
);

const StackedEditField: React.FC<{
  label: string;
  value: string;
  onChange: (v: string) => void;
  minHeight?: number;
}> = ({ label, value, onChange, minHeight = 50 }) => (
  <div style={{ borderTop: '1px solid #fdba74' }} className="memo-edit">
    <div
      className="px-2 py-1 font-bold uppercase"
      style={{
        background: '#fed7aa',
        borderBottom: '1px solid #fdba74',
        fontSize: 10,
        color: '#7c2d12',
        letterSpacing: 0.5,
      }}
    >
      {label}
    </div>
    <textarea
      className="w-full px-3 py-2 text-xs"
      style={{ minHeight, resize: 'vertical', lineHeight: 1.5 }}
      value={value}
      onChange={(e) => onChange(e.target.value)}
    />
  </div>
);

// --- Field-level diff comparison for a regenerated row ---
type DiffFieldKey = 'preConditions' | 'inputTestData' | 'steps' | 'expectedResults';

interface RegenDiffProps {
  row: TcRow;
  onApply: (fields: DiffFieldKey[]) => void;
  onDiscard: () => void;
}

const DIFF_FIELDS: { key: DiffFieldKey; label: string }[] = [
  { key: 'preConditions', label: 'Pre-Conditions' },
  { key: 'inputTestData', label: 'Input Test Data' },
  { key: 'steps', label: 'Test Procedure' },
  { key: 'expectedResults', label: 'Expected Result' },
];

const RegenDiff: React.FC<RegenDiffProps> = ({ row, onApply, onDiscard }) => {
  const [selected, setSelected] = useState<Set<DiffFieldKey>>(
    new Set(['preConditions', 'inputTestData', 'steps', 'expectedResults'])
  );

  const toggle = (field: DiffFieldKey) => {
    setSelected((prev) => {
      const next = new Set(prev);
      next.has(field) ? next.delete(field) : next.add(field);
      return next;
    });
  };

  return (
    <div className="paper-card p-3 mt-2" style={{ borderColor: '#fb923c #fb923c #fb923c #fb923c' }}>
      <div className="title-bar-mini edit -mx-3 -mt-3 mb-3" style={{ padding: '4px 10px' }}>
        <RiRefreshLine className="size-3" />
        <span className="flex-1">New Version Ready — Select fields to apply</span>
        <button
          className="text-xs"
          style={{ minHeight: 20, padding: '1px 8px' }}
          onClick={onDiscard}
        >
          <RiArrowGoBackLine className="size-3 inline mr-1" />Discard
        </button>
        <button
          className="text-xs font-bold default"
          style={{ minHeight: 20, padding: '1px 10px' }}
          onClick={() => onApply([...selected])}
          disabled={selected.size === 0}
        >
          <RiCheckFill className="size-3 inline mr-1" />Apply Selected
        </button>
      </div>

      <div className="flex flex-col gap-2">
        {DIFF_FIELDS.map(({ key, label }) => {
          const oldVal = row[key] || '';
          const newVal = row.pendingRegenerated?.[key] || '';
          const changed = oldVal !== newVal;
          const isSelected = selected.has(key);
          const { left, right } = changed ? diffTokens(oldVal, newVal) : { left: [], right: [] };

          return (
            <div
              key={key}
              style={{
                border: '2px solid',
                borderColor: isSelected
                  ? '#808080 #ffffff #ffffff #808080'
                  : '#c0c0c0 #e0e0e0 #e0e0e0 #c0c0c0',
                background: '#ffffff',
                opacity: isSelected ? 1 : 0.55,
              }}
            >
              <div
                className="flex items-center gap-2 px-2 py-1 cursor-pointer"
                style={{ background: '#e8e8e8', borderBottom: '1px solid #c0c0c0' }}
                onClick={() => toggle(key)}
              >
                {isSelected
                  ? <RiCheckboxLine className="size-4 text-orange-600 shrink-0" />
                  : <RiCheckboxBlankLine className="size-4 text-gray-400 shrink-0" />}
                <span className="text-[10px] font-bold uppercase text-gray-700">{label}</span>
                {changed ? (
                  <span className="ml-auto text-[9px] px-1 font-bold uppercase" style={{ background: '#fed7aa', color: '#7c2d12', border: '1px solid #fb923c' }}>Changed</span>
                ) : (
                  <span className="ml-auto text-[9px] px-1 uppercase" style={{ background: '#e0e0e0', color: '#606060', border: '1px solid #c0c0c0' }}>Unchanged</span>
                )}
              </div>
              {changed ? (
                <div className="grid grid-cols-2" style={{ borderTop: '1px solid #e0e0e0' }}>
                  <div className="p-2 text-[11px] leading-relaxed selectable" style={{ borderRight: '1px solid #e0e0e0', background: '#faf6f4' }}>
                    <div className="text-[9px] font-bold uppercase mb-1" style={{ color: '#991b1b' }}>
                      <RiFileTextLine className="size-3 inline mr-1" />Current (strikethrough = removed)
                    </div>
                    <DiffText tokens={left} />
                  </div>
                  <div className="p-2 text-[11px] leading-relaxed selectable" style={{ background: '#f4faf4' }}>
                    <div className="text-[9px] font-bold uppercase mb-1" style={{ color: '#166534' }}>
                      <RiEditBoxLine className="size-3 inline mr-1" />New (highlighted = added)
                    </div>
                    <DiffText tokens={right} />
                  </div>
                </div>
              ) : (
                <div className="p-2 text-[11px] text-gray-600 selectable whitespace-pre-wrap" style={{ borderTop: '1px solid #e0e0e0' }}>
                  {oldVal || '—'}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

// --- Main ReviewModule ---
const ReviewModule: React.FC = () => {
  const {
    tcRows, jobMetadata,
    updateTcRow, deleteTcRows, renumberTcRows,
    setPendingRegenerated, applyRegenerated, clearPendingRegenerated,
    isRegenerating, setRegenerating, config, appendLog,
  } = useJobStore();
  const { openWindow } = useWindowStore();

  // 允許同時展開多列
  const [expandedRows, setExpandedRows] = useState<Set<string>>(new Set());
  const [activeRowId, setActiveRowId] = useState<string | null>(null);
  const [editingId, setEditingRowId] = useState<string | null>(null);
  const [editValues, setEditValues] = useState<{ steps: string; expected: string; preConditions: string; inputTestData: string }>({
    steps: '', expected: '', preConditions: '', inputTestData: '',
  });
  const [filter, setFilter] = useState('all');
  const [testSetFilter, setTestSetFilter] = useState('all');
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());

  // Validation panel 顯示最後一個被展開/聚焦的列
  const selectedRow = tcRows.find((r) => r.id === activeRowId) ?? null;

  const toggleExpand = (id: string) => {
    setExpandedRows((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
        if (activeRowId === id) {
          setActiveRowId(next.size > 0 ? [...next][next.size - 1] : null);
        }
      } else {
        next.add(id);
        setActiveRowId(id);
      }
      return next;
    });
  };

  const collapseOne = (id: string) => {
    setExpandedRows((prev) => {
      if (!prev.has(id)) return prev;
      const next = new Set(prev);
      next.delete(id);
      return next;
    });
    if (activeRowId === id) setActiveRowId(null);
  };

  const handleStatusChange = (id: string, status: TcRow['status']) => {
    updateTcRow(id, { status });
  };

  const startEditing = (row: TcRow) => {
    setEditingRowId(row.id);
    setActiveRowId(row.id);
    setEditValues({
      steps: row.steps,
      expected: row.expectedResults,
      preConditions: row.preConditions,
      inputTestData: row.inputTestData ?? '',
    });
  };

  const saveEdit = (id: string) => {
    updateTcRow(id, {
      steps: editValues.steps,
      expectedResults: editValues.expected,
      preConditions: editValues.preConditions,
      inputTestData: editValues.inputTestData,
      status: 'accepted',
    });
    setEditingRowId(null);
  };

  const toggleFlag = (id: string, currentStatus: string) => {
    updateTcRow(id, { status: currentStatus === 'flagged' ? 'reviewing' : 'flagged' });
  };

  const handleDelete = (id: string) => {
    if (!confirm('Delete this test case?')) return;
    deleteTcRows([id]);
    renumberTcRows();
    collapseOne(id);
    if (editingId === id) setEditingRowId(null);
    setSelectedIds(new Set());
  };

  const toggleSelectRow = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      next.has(id) ? next.delete(id) : next.add(id);
      return next;
    });
  };

  const toggleSelectAll = () => {
    const visible = filteredRows.map((r) => r.id);
    const allSelected = visible.every((id) => selectedIds.has(id));
    if (allSelected) {
      setSelectedIds((prev) => { const next = new Set(prev); visible.forEach((id) => next.delete(id)); return next; });
    } else {
      setSelectedIds((prev) => { const next = new Set(prev); visible.forEach((id) => next.add(id)); return next; });
    }
  };

  const handleBulkStatus = (status: TcRow['status']) => {
    if (selectedIds.size === 0) return;
    selectedIds.forEach((id) => updateTcRow(id, { status }));
    appendLog(createJobLog('info', `Marked ${selectedIds.size} row(s) as ${status}.`));
    setSelectedIds(new Set());
  };

  const handleBulkDelete = () => {
    if (selectedIds.size === 0) return;
    if (!confirm(`Delete ${selectedIds.size} selected test case(s)?`)) return;
    const ids = [...selectedIds];
    deleteTcRows(ids);
    renumberTcRows();
    appendLog(createJobLog('info', `Deleted ${ids.length} row(s).`));
    setExpandedRows((prev) => { const next = new Set(prev); ids.forEach((i) => next.delete(i)); return next; });
    if (ids.includes(activeRowId ?? '')) setActiveRowId(null);
    setEditingRowId(null);
    setSelectedIds(new Set());
  };

  const handleRegenerate = useCallback(async () => {
    if (selectedIds.size === 0) return;
    setRegenerating(true);

    const ids = [...selectedIds];
    ids.forEach((id) => updateTcRow(id, { status: 'generating' }));

    try {
      appendLog(createJobLog('info', `Re-generating ${ids.length} selected row(s).`));
      await regenerateRows(
        {
          jobId: jobMetadata?.jobId ?? null,
          rowIds: ids,
          rows: tcRows,
          config,
        },
        {
          onRow: (id, data) => {
            setPendingRegenerated(id, data);
            updateTcRow(id, { status: 'reviewing' });
          },
          onFail: (id, message) => {
            updateTcRow(id, { status: 'fail' });
            appendLog(createJobLog('error', `${id}: ${message}`));
          },
          onComplete: () => {
            appendLog(createJobLog('success', 'Re-generation complete. Review highlighted rows before applying.'));
          },
          onError: (message) => {
            appendLog(createJobLog('warn', message));
          },
        },
      );
    } catch {
      ids.forEach((id) => updateTcRow(id, { status: 'fail' }));
      appendLog(createJobLog('error', 'Re-generation failed.'));
    } finally {
      setRegenerating(false);
      setSelectedIds(new Set());
    }
  }, [selectedIds, jobMetadata, setRegenerating, updateTcRow, setPendingRegenerated, tcRows, config, appendLog]);

  const testSetOptions = useMemo(
    () => [...new Set(tcRows.map((row) => row.testSet).filter(Boolean))].sort(),
    [tcRows],
  );

  const filteredRows = tcRows.filter((r) => {
    if (testSetFilter !== 'all' && r.testSet !== testSetFilter) return false;
    if (filter === 'flagged') return r.status === 'flagged';
    if (filter === 'pending') return r.status === 'pending';
    if (filter === 'regen') return !!r.pendingRegenerated;
    return true;
  });

  const allVisibleSelected = filteredRows.length > 0 && filteredRows.every((r) => selectedIds.has(r.id));

  return (
    <div className="flex h-full gap-2 overflow-hidden relative">
      {/* Main Table Area */}
      <div className="flex-1 flex flex-col min-w-0">
        {/* Toolbar */}
        <div className="flex justify-between items-center mb-2 bg-gray-200 p-1 border border-sunken">
          <div className="flex gap-2 items-center">
            <div className="field-row">
              <label htmlFor="filter" className="text-xs font-bold">Show:</label>
              <select id="filter" value={filter} onChange={(e) => setFilter(e.target.value)}>
                <option value="all">All TCs</option>
                <option value="flagged">Flagged Only</option>
                <option value="pending">Pending Review</option>
                <option value="regen">Awaiting Apply</option>
              </select>
            </div>
            <div className="field-row">
              <label htmlFor="test-set-filter" className="text-xs font-bold">Test Set:</label>
              <select
                id="test-set-filter"
                value={testSetFilter}
                onChange={(e) => setTestSetFilter(e.target.value)}
              >
                <option value="all">All Sets</option>
                {testSetOptions.map((testSet) => (
                  <option key={testSet} value={testSet}>
                    {testSet}
                  </option>
                ))}
              </select>
            </div>
            <span className="text-xs text-gray-600 ">
              Total: {tcRows.length} | Accepted: {tcRows.filter((r) => r.status === 'accepted').length} | Expanded: {expandedRows.size}
            </span>
          </div>
          <HelpFromAgentButton
            contextPrompt={`[context: 目前在 Review Module, job=${jobMetadata?.jobId ?? '未開啟 job'}]\n[Validator: ${tcRows.filter(r => (r.validationErrors ?? []).length > 0).length} warnings]\n`}
            title="求助 AI"
          />
        </div>

        {/* Table */}
        <div className="flex-1 overflow-auto border-2 border-sunken bg-white">
          <table className="w-full text-sm border-collapse">
            <thead className="sticky top-0 z-10">
              <tr>
                <th className="win95-th center" style={{ width: 32 }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <input
                      type="checkbox"
                      id="select-all"
                      checked={allVisibleSelected}
                      onChange={toggleSelectAll}
                      title={allVisibleSelected ? 'Deselect all' : 'Select all'}
                    />
                    <label htmlFor="select-all" style={{ margin: 0 }} />
                  </div>
                </th>
                <th className="win95-th center" style={{ width: 24 }}></th>
                <th className="win95-th">TC ID</th>
                <th className="win95-th">Req ID</th>
                <th className="win95-th">Status</th>
                <th className="win95-th center" style={{ width: 112 }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredRows.map((row) => {
                const isExpanded = expandedRows.has(row.id);
                const isSelected = selectedIds.has(row.id);
                const isActive = activeRowId === row.id;
                const isEditing = editingId === row.id;
                return (
                  <React.Fragment key={row.id}>
                    <tr
                      className={`border-b cursor-pointer win95-row
                        ${isActive || isSelected ? 'selected' : ''}
                        ${row.status === 'flagged' && !isActive && !isSelected ? 'bg-orange-50' : ''}
                        ${row.pendingRegenerated && !isActive && !isSelected ? 'bg-yellow-50' : ''}
                      `}
                    >
                      <td
                        style={{ cursor: 'pointer', width: 32, textAlign: 'center', verticalAlign: 'middle' }}
                        onClick={(e) => { e.stopPropagation(); toggleSelectRow(row.id); }}
                      >
                        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', pointerEvents: 'none' }}>
                          <input
                            type="checkbox"
                            id={`row-${row.id}`}
                            checked={isSelected}
                            onChange={() => {}}
                          />
                          <label htmlFor={`row-${row.id}`} style={{ margin: 0 }} />
                        </div>
                      </td>

                      <td className="text-center py-2" onClick={() => toggleExpand(row.id)}>
                        {isExpanded
                          ? <RiArrowUpSLine className="size-4" />
                          : <RiArrowDownSLine className="size-4" />}
                      </td>

                      <td className="px-3 py-2 border-r font-mono text-xs" onClick={() => toggleExpand(row.id)}>
                        <span className="flex items-center gap-1">
                          {row.status === 'flagged' && <RiFlagFill className="size-3 text-orange-600" />}
                          {row.pendingRegenerated && <RiRefreshLine className="size-3 text-yellow-600" />}
                          {row.id}
                        </span>
                      </td>
                      <td className="px-3 py-2 border-r font-mono text-xs" onClick={() => toggleExpand(row.id)}>
                        {row.reqId}
                      </td>
                      <td className="px-3 py-2 border-r" onClick={() => toggleExpand(row.id)}>
                        <span className={`status-badge ${
                          row.pendingRegenerated ? 'reviewing' :
                          row.status === 'generating' ? 'generating' :
                          row.status
                        } ${row.status === 'generating' ? 'animate-pulse' : ''}`}>
                          {row.pendingRegenerated ? 'awaiting apply' : row.status}
                        </span>
                      </td>

                      <td className="p-0 border-r cell-center" onClick={(e) => e.stopPropagation()}>
                        <div className="flex justify-center items-center gap-1 h-full min-h-[32px]">
                          <button className="btn-icon btn-accept" title="Accept" onClick={() => handleStatusChange(row.id, 'accepted')}>
                            <RiCheckFill className="size-4" />
                          </button>
                          <button className="btn-icon btn-reject" title="Reject" onClick={() => handleStatusChange(row.id, 'rejected')}>
                            <RiCloseFill className="size-4" />
                          </button>
                          <button className="btn-icon" title="Delete" style={{ color: '#7f1d1d' }} onClick={() => handleDelete(row.id)}>
                            <RiDeleteBinLine className="size-4" />
                          </button>
                        </div>
                      </td>
                    </tr>

                    {isExpanded && (
                      <tr>
                        <td
                          colSpan={6}
                          className="p-4"
                          style={{
                            background: '#9a9a9a',
                            boxShadow: 'inset 2px 2px 0 #606060, inset -2px -2px 0 #d0d0d0',
                            borderBottom: '2px solid #404040',
                          }}
                          onClick={() => setActiveRowId(row.id)}
                        >
                          {row.pendingRegenerated ? (
                            <RegenDiff
                              row={row}
                              onApply={(fields) => {
                                applyRegenerated(row.id, fields);
                                renumberTcRows();
                                collapseOne(row.id);
                                setEditingRowId(null);
                                setSelectedIds(new Set());
                              }}
                              onDiscard={() => clearPendingRegenerated(row.id)}
                            />
                          ) : (
                            <div className="grid grid-cols-5 gap-3">
                              {/* Left: Original (40%) */}
                              <div className="col-span-2 flex flex-col">
                                <div className="title-bar-mini">
                                  <RiFileTextLine className="size-3" />
                                  <span className="flex-1">Original Requirement</span>
                                </div>
                                <div className="paper-card flex-1 p-3 text-xs leading-relaxed overflow-auto whitespace-pre-wrap break-words selectable" style={{ minHeight: 140 }}>
                                  {row.testItem}
                                </div>
                              </div>

                              {/* Right: Generated / Editable (60%) */}
                              <div className="col-span-3 flex flex-col">
                                <div className={`title-bar-mini ${isEditing ? 'edit' : ''}`}>
                                  <RiEditBoxLine className="size-3" />
                                  <span className="flex-1">
                                    {isEditing ? 'Generated Test Case — EDIT MODE' : 'Generated Test Case'}
                                  </span>
                                </div>
                                <div className={`paper-card ${isEditing ? 'edit-mode' : ''}`}>
                                  {isEditing ? (
                                    <div className="flex flex-col">
                                      <StackedEditField
                                        label="Pre-Conditions"
                                        value={editValues.preConditions}
                                        onChange={(v) => setEditValues({ ...editValues, preConditions: v })}
                                      />
                                      <StackedEditField
                                        label="Input Test Data"
                                        value={editValues.inputTestData}
                                        onChange={(v) => setEditValues({ ...editValues, inputTestData: v })}
                                      />
                                      <StackedEditField
                                        label="Test Procedure"
                                        value={editValues.steps}
                                        onChange={(v) => setEditValues({ ...editValues, steps: v })}
                                        minHeight={80}
                                      />
                                      <StackedEditField
                                        label="Expected Result"
                                        value={editValues.expected}
                                        onChange={(v) => setEditValues({ ...editValues, expected: v })}
                                      />
                                    </div>
                                  ) : (
                                    <div className="flex flex-col">
                                      <StackedReadField label="Pre-Conditions" value={row.preConditions} />
                                      <StackedReadField label="Input Test Data" value={row.inputTestData} muted />
                                      <StackedReadField label="Test Procedure" value={row.steps} />
                                      <StackedReadField label="Expected Result" value={row.expectedResults} />
                                      {row.specReference && (
                                        <StackedReadField label="Spec Reference" value={row.specReference} muted />
                                      )}
                                    </div>
                                  )}
                                </div>
                              </div>
                            </div>
                          )}

                          {!row.pendingRegenerated && (
                            <div className="mt-3 flex justify-end gap-2">
                              {isEditing ? (
                                <>
                                  <button className="flex items-center gap-1 text-xs px-3 py-1" onClick={() => setEditingRowId(null)}>
                                    <RiArrowGoBackLine className="size-3" /> Cancel
                                  </button>
                                  <button className="flex items-center gap-1 text-xs px-3 py-1 font-bold default" onClick={() => saveEdit(row.id)}>
                                    <RiSaveLine className="size-3" /> Save Changes
                                  </button>
                                </>
                              ) : (
                                <>
                                  <button className="flex items-center gap-1 text-xs px-3 py-1" onClick={() => startEditing(row)}>
                                    <RiEditLine className="size-3" /> Manual Edit
                                  </button>
                                  <button
                                    className={`flex items-center gap-1 text-xs px-3 py-1 ${
                                      row.status === 'flagged' ? 'font-bold' : ''
                                    }`}
                                    style={row.status === 'flagged' ? { background: '#e0a000', color: '#000000' } : { color: '#7c2d12' }}
                                    onClick={() => toggleFlag(row.id, row.status)}
                                  >
                                    {row.status === 'flagged'
                                      ? <RiFlagFill className="size-3" />
                                      : <RiFlagLine className="size-3" />}
                                    {row.status === 'flagged' ? 'Unflag' : 'Flag for Human'}
                                  </button>
                                </>
                              )}
                            </div>
                          )}
                        </td>
                      </tr>
                    )}
                  </React.Fragment>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Right Validation Panel */}
      <div className="w-64 flex flex-col gap-2">
        <fieldset className="flex-1 flex flex-col overflow-hidden">
          <legend className="font-bold text-sm">Validation Results</legend>
          <div className="flex-1 overflow-auto p-2 flex flex-col gap-2">
            {!selectedRow ? (
              <div className="sys-log-entry" style={{ color: '#606060' }}>
                <span className="sys-log-tag info">INFO</span>
                Expand a row to view validation.
              </div>
            ) : selectedRow.validationErrors && selectedRow.validationErrors.length > 0 ? (
              selectedRow.validationErrors.map((err, i) => (
                <div key={i} className="sys-log-entry selectable">
                  <div className="flex items-start gap-2">
                    {err.severity === 'error'
                      ? <RiErrorWarningFill className="size-4 shrink-0 mt-0.5" style={{ color: '#c00000' }} />
                      : <RiAlertFill className="size-4 shrink-0 mt-0.5" style={{ color: '#e0a000' }} />}
                    <div className="flex-1 min-w-0">
                      <div>
                        <span className={`sys-log-tag ${err.severity === 'error' ? 'critical' : 'warn'}`}>
                          {err.severity === 'error' ? 'CRITICAL' : 'WARNING'}
                        </span>
                        <span className="font-bold text-[11px]">
                          {err.severity === 'error' ? 'Logic Conflict' : 'Quality Warning'}
                        </span>
                      </div>
                      <div className="text-[11px] mt-1" style={{ color: '#303030' }}>
                        {err.message}
                      </div>
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="sys-log-entry selectable">
                <div className="flex items-start gap-2">
                  <RiCheckboxCircleFill className="size-4 shrink-0 mt-0.5" style={{ color: '#00a000' }} />
                  <div className="flex-1">
                    <div>
                      <span className="sys-log-tag info">PASS</span>
                      <span className="font-bold text-[11px]">All Checks Passed</span>
                    </div>
                    <div className="text-[11px] mt-1" style={{ color: '#303030' }}>
                      This test case meets all AI quality standards.
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </fieldset>

        <button className="w-full py-3 flex items-center justify-center gap-2 font-bold default" onClick={() => openWindow('export', 'TC Generator - Export')}>
          <RiDownload2Line className="size-5" /> Export All
        </button>
      </div>

      {/* Floating toolbox — shown when rows are selected */}
      {selectedIds.size > 0 && (
        <div
          className="win95-toolbox absolute bottom-4 left-1/2 z-20"
          style={{ transform: 'translateX(-50%)', padding: '6px 4px' }}
        >
          <div className="win95-toolbox-handle" />
          <div className="win95-toolbox-group">
            <span className="font-bold" style={{ fontSize: 11, padding: '0 4px' }}>
              {selectedIds.size} row{selectedIds.size > 1 ? 's' : ''} selected
            </span>
            <button onClick={() => setSelectedIds(new Set())}>Clear</button>
          </div>
          <div className="win95-toolbox-group">
            <button className="flex items-center gap-1" title="Accept selected" onClick={() => handleBulkStatus('accepted')}>
              <RiCheckFill className="size-3 text-green-700" /> Accept
            </button>
            <button className="flex items-center gap-1" title="Reject selected" onClick={() => handleBulkStatus('rejected')}>
              <RiCloseFill className="size-3 text-red-700" /> Reject
            </button>
          </div>
          <div className="win95-toolbox-group">
            <button className="flex items-center gap-1" title="Delete selected" onClick={handleBulkDelete}>
              <RiDeleteBinLine className="size-3" /> Delete
            </button>
            <button className="font-bold flex items-center gap-1" onClick={handleRegenerate} disabled={isRegenerating}>
              <RiRefreshLine className={`size-3 ${isRegenerating ? 'animate-spin' : ''}`} />
              {isRegenerating ? 'Regenerating...' : `Regenerate`}
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ReviewModule;
