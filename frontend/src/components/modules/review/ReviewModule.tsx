'use client';

import React, { useState, useCallback } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { TcRow } from '../../../lib/types';
import { createJobLog } from '../../../lib/logging';
import { regenerateRows } from '../../../services/jobAdapter';
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
} from '@remixicon/react';

// --- Field-level diff comparison for a regenerated row ---
interface RegenDiffProps {
  row: TcRow;
  onApply: (fields: ('steps' | 'expectedResults' | 'preConditions')[]) => void;
  onDiscard: () => void;
}

const DIFF_FIELDS: { key: 'preConditions' | 'steps' | 'expectedResults'; label: string }[] = [
  { key: 'preConditions', label: 'Pre-Conditions' },
  { key: 'steps', label: 'Steps' },
  { key: 'expectedResults', label: 'Expected Results' },
];

const RegenDiff: React.FC<RegenDiffProps> = ({ row, onApply, onDiscard }) => {
  const [selected, setSelected] = useState<Set<'steps' | 'expectedResults' | 'preConditions'>>(
    new Set(['steps', 'expectedResults', 'preConditions'])
  );

  const toggle = (field: 'steps' | 'expectedResults' | 'preConditions') => {
    setSelected((prev) => {
      const next = new Set(prev);
      next.has(field) ? next.delete(field) : next.add(field);
      return next;
    });
  };

  return (
    <div className="border-2 border-orange-400 bg-orange-50 p-3 mt-2">
      <div className="flex items-center justify-between mb-2">
        <span className="text-xs font-bold text-orange-800 uppercase">New Version Ready — Select fields to apply</span>
        <div className="flex gap-1">
          <button
            className="text-xs px-2 py-0.5 text-gray-700"
            onClick={onDiscard}
          >
            <RiArrowGoBackLine className="size-3 inline mr-1" />Discard
          </button>
          <button
            className="text-xs px-3 py-0.5 font-bold default"
            onClick={() => onApply([...selected])}
            disabled={selected.size === 0}
          >
            <RiCheckFill className="size-3 inline mr-1" />Apply Selected
          </button>
        </div>
      </div>

      <div className="flex flex-col gap-3">
        {DIFF_FIELDS.map(({ key, label }) => {
          const oldVal = row[key] || '';
          const newVal = row.pendingRegenerated?.[key] || '';
          const changed = oldVal !== newVal;
          const isSelected = selected.has(key);

          return (
            <div key={key} className={`border ${isSelected ? 'border-orange-300 bg-white' : 'border-gray-200 bg-gray-50 opacity-60'}`}>
              <div
                className="flex items-center gap-2 px-2 py-1 bg-gray-100 border-b border-gray-200 cursor-pointer select-none"
                onClick={() => toggle(key)}
              >
                {isSelected
                  ? <RiCheckboxLine className="size-4 text-orange-600 shrink-0" />
                  : <RiCheckboxBlankLine className="size-4 text-gray-400 shrink-0" />}
                <span className="text-[10px] font-bold uppercase text-gray-700">{label}</span>
                {changed && (
                  <span className="ml-auto text-[9px] px-1 py-0.5 bg-orange-200 text-orange-800 font-bold uppercase">Changed</span>
                )}
                {!changed && (
                  <span className="ml-auto text-[9px] px-1 py-0.5 bg-gray-200 text-gray-500 uppercase">Unchanged</span>
                )}
              </div>
              <div className="grid grid-cols-2 divide-x divide-gray-200">
                <div className="p-2">
                  <div className="text-[9px] font-bold text-gray-400 uppercase mb-1">Current</div>
                  <div className="text-[11px] whitespace-pre-wrap text-gray-700 leading-relaxed">{oldVal || '—'}</div>
                </div>
                <div className="p-2 bg-green-50">
                  <div className="text-[9px] font-bold text-green-600 uppercase mb-1">New</div>
                  <div className="text-[11px] whitespace-pre-wrap text-green-900 leading-relaxed">{newVal || '—'}</div>
                </div>
              </div>
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
    updateTcRow, deleteTcRows,
    setPendingRegenerated, applyRegenerated, clearPendingRegenerated,
    isRegenerating, setRegenerating, config, appendLog,
  } = useJobStore();
  const { openWindow } = useWindowStore();

  const [expandedRow, setExpandedRow] = useState<string | null>('TC-003');
  const [editingId, setEditingRowId] = useState<string | null>(null);
  const [editValues, setEditValues] = useState<{ steps: string; expected: string; preConditions: string }>({
    steps: '', expected: '', preConditions: '',
  });
  const [filter, setFilter] = useState('all');
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());

  const selectedRow = tcRows.find((r) => r.id === expandedRow);

  const handleStatusChange = (id: string, status: TcRow['status']) => {
    updateTcRow(id, { status });
  };

  const startEditing = (row: TcRow) => {
    setEditingRowId(row.id);
    setEditValues({ steps: row.steps, expected: row.expectedResults, preConditions: row.preConditions });
  };

  const saveEdit = (id: string) => {
    updateTcRow(id, {
      steps: editValues.steps,
      expectedResults: editValues.expected,
      preConditions: editValues.preConditions,
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
    if (expandedRow === id) setExpandedRow(null);
    setSelectedIds((prev) => { const next = new Set(prev); next.delete(id); return next; });
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

  const filteredRows = tcRows.filter((r) => {
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
          <div className="flex gap-4 items-center">
            <div className="field-row">
              <label htmlFor="filter" className="text-xs font-bold">Show:</label>
              <select id="filter" value={filter} onChange={(e) => setFilter(e.target.value)}>
                <option value="all">All TCs</option>
                <option value="flagged">Flagged Only</option>
                <option value="pending">Pending Review</option>
                <option value="regen">Awaiting Apply</option>
              </select>
            </div>
            <span className="text-xs text-gray-600 font-sans">
              Total: {tcRows.length} | Accepted: {tcRows.filter((r) => r.status === 'accepted').length}
            </span>
          </div>
        </div>

        {/* Table */}
        <div className="flex-1 overflow-auto border-2 border-sunken bg-white">
          <table className="w-full text-sm border-collapse">
            <thead className="sticky top-0 bg-gray-200 shadow-sm z-10">
              <tr className="border-b border-gray-400">
                <th className="w-8 p-1 text-center">
                  <button
                    className="flex items-center justify-center w-full"
                    title={allVisibleSelected ? 'Deselect all' : 'Select all'}
                    onClick={toggleSelectAll}
                  >
                    {allVisibleSelected
                      ? <RiCheckboxLine className="size-4 text-blue-700" />
                      : <RiCheckboxBlankLine className="size-4 text-gray-500" />}
                  </button>
                </th>
                <th className="w-6"></th>
                <th className="text-left p-2 border-r">TC ID</th>
                <th className="text-left p-2 border-r">Req ID</th>
                <th className="text-left p-2 border-r">Status</th>
                <th className="text-center p-2 w-28">Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredRows.map((row) => (
                <React.Fragment key={row.id}>
                  <tr
                    className={`border-b hover:bg-blue-50 cursor-pointer
                      ${expandedRow === row.id ? 'bg-blue-100' : ''}
                      ${row.status === 'flagged' ? 'bg-orange-50' : ''}
                      ${row.pendingRegenerated ? 'bg-yellow-50' : ''}
                      ${selectedIds.has(row.id) ? 'outline outline-1 outline-blue-400' : ''}
                    `}
                  >
                    {/* Checkbox */}
                    <td className="text-center p-1" onClick={(e) => e.stopPropagation()}>
                      <button
                        className="flex items-center justify-center w-full"
                        onClick={() => toggleSelectRow(row.id)}
                      >
                        {selectedIds.has(row.id)
                          ? <RiCheckboxLine className="size-4 text-blue-700" />
                          : <RiCheckboxBlankLine className="size-4 text-gray-400" />}
                      </button>
                    </td>

                    {/* Expand toggle */}
                    <td
                      className="text-center"
                      onClick={() => setExpandedRow(expandedRow === row.id ? null : row.id)}
                    >
                      {expandedRow === row.id
                        ? <RiArrowUpSLine className="size-4" />
                        : <RiArrowDownSLine className="size-4" />}
                    </td>

                    <td
                      className="p-2 border-r font-mono text-xs"
                      onClick={() => setExpandedRow(expandedRow === row.id ? null : row.id)}
                    >
                      <span className="flex items-center gap-1">
                        {row.status === 'flagged' && <RiFlagFill className="size-3 text-orange-600" />}
                        {row.pendingRegenerated && <RiRefreshLine className="size-3 text-yellow-600" />}
                        {row.id}
                      </span>
                    </td>
                    <td
                      className="p-2 border-r font-mono text-xs"
                      onClick={() => setExpandedRow(expandedRow === row.id ? null : row.id)}
                    >
                      {row.reqId}
                    </td>
                    <td
                      className="p-2 border-r"
                      onClick={() => setExpandedRow(expandedRow === row.id ? null : row.id)}
                    >
                      <span className={`px-2 py-0.5 rounded-full text-[10px] uppercase font-bold ${
                        row.status === 'accepted' ? 'bg-green-100 text-green-800' :
                        row.status === 'rejected' ? 'bg-red-100 text-red-800' :
                        row.status === 'flagged' ? 'bg-orange-100 text-orange-800' :
                        row.status === 'generating' ? 'bg-blue-100 text-blue-800 animate-pulse' :
                        row.pendingRegenerated ? 'bg-yellow-100 text-yellow-800' :
                        'bg-gray-100 text-gray-700'
                      }`}>
                        {row.pendingRegenerated ? 'awaiting apply' : row.status}
                      </span>
                    </td>

                    {/* Actions */}
                    <td className="p-0 border-r cell-center" onClick={(e) => e.stopPropagation()}>
                      <div className="flex justify-center items-center gap-1 h-full min-h-[32px]">
                        <button
                          className="btn-icon btn-accept"
                          title="Accept"
                          onClick={() => handleStatusChange(row.id, 'accepted')}
                        >
                          <RiCheckFill className="size-4" />
                        </button>
                        <button
                          className="btn-icon btn-reject"
                          title="Reject"
                          onClick={() => handleStatusChange(row.id, 'rejected')}
                        >
                          <RiCloseFill className="size-4" />
                        </button>
                        <button
                          className="btn-icon"
                          title="Delete"
                          style={{ color: '#7f1d1d' }}
                          onClick={() => handleDelete(row.id)}
                        >
                          <RiDeleteBinLine className="size-4" />
                        </button>
                      </div>
                    </td>
                  </tr>

                  {/* Expanded detail */}
                  {expandedRow === row.id && (
                    <tr>
                      <td colSpan={6} className="bg-gray-50 p-4 border-b-2 border-gray-300 shadow-inner">
                        {/* Regen diff takes priority when pending */}
                        {row.pendingRegenerated ? (
                          <RegenDiff
                            row={row}
                            onApply={(fields) => applyRegenerated(row.id, fields)}
                            onDiscard={() => clearPendingRegenerated(row.id)}
                          />
                        ) : (
                          <div className="grid grid-cols-2 gap-4">
                            {/* Left: Original */}
                            <div className="flex flex-col gap-1">
                              <span className="text-xs font-bold text-gray-500 uppercase">Original Requirement</span>
                              <div className="p-3 bg-white border border-gray-300 min-h-[120px] text-xs leading-relaxed overflow-auto">
                                {row.testItem}
                              </div>
                            </div>

                            {/* Right: Generated / Editable */}
                            <div className="flex flex-col gap-1">
                              <span className="text-xs font-bold text-blue-600 uppercase flex justify-between">
                                <span>Generated Test Case</span>
                                {editingId === row.id && (
                                  <span className="text-orange-600 text-[10px]">EDIT MODE</span>
                                )}
                              </span>
                              <div className={`p-3 bg-white border min-h-[120px] text-xs leading-relaxed flex flex-col ${
                                editingId === row.id ? 'border-orange-400 ring-1 ring-orange-200' : 'border-blue-300'
                              }`}>
                                {editingId === row.id ? (
                                  <>
                                    <label className="font-bold text-[10px] mb-1">PRE-CONDITIONS:</label>
                                    <textarea
                                      className="mb-2 p-1 text-xs font-sans min-h-[40px]"
                                      value={editValues.preConditions}
                                      onChange={(e) => setEditValues({ ...editValues, preConditions: e.target.value })}
                                    />
                                    <label className="font-bold text-[10px] mb-1">STEPS:</label>
                                    <textarea
                                      className="flex-1 mb-2 p-1 text-xs font-sans min-h-[60px]"
                                      value={editValues.steps}
                                      onChange={(e) => setEditValues({ ...editValues, steps: e.target.value })}
                                    />
                                    <label className="font-bold text-[10px] mb-1">EXPECTED RESULTS:</label>
                                    <textarea
                                      className="p-1 text-xs font-sans"
                                      value={editValues.expected}
                                      onChange={(e) => setEditValues({ ...editValues, expected: e.target.value })}
                                    />
                                  </>
                                ) : (
                                  <>
                                    <div className="font-bold mb-1">Pre-Conditions:</div>
                                    <div className="whitespace-pre-wrap mb-2 text-gray-600">{row.preConditions}</div>
                                    <div className="font-bold mb-1">Steps:</div>
                                    <div className="whitespace-pre-wrap flex-1">{row.steps}</div>
                                    <div className="font-bold mt-2 mb-1">Expected:</div>
                                    <div className="text-green-800 font-bold">{row.expectedResults}</div>
                                  </>
                                )}
                              </div>
                            </div>
                          </div>
                        )}

                        {/* Detail action buttons (not shown in regen diff mode) */}
                        {!row.pendingRegenerated && (
                          <div className="mt-3 flex justify-end gap-2">
                            {editingId === row.id ? (
                              <>
                                <button
                                  className="flex items-center gap-1 text-xs px-3 py-1"
                                  onClick={() => setEditingRowId(null)}
                                >
                                  <RiArrowGoBackLine className="size-3" /> Cancel
                                </button>
                                <button
                                  className="flex items-center gap-1 text-xs px-3 py-1 font-bold default"
                                  onClick={() => saveEdit(row.id)}
                                >
                                  <RiSaveLine className="size-3" /> Save Changes
                                </button>
                              </>
                            ) : (
                              <>
                                <button
                                  className="flex items-center gap-1 text-xs px-3 py-1"
                                  onClick={() => startEditing(row)}
                                >
                                  <RiEditLine className="size-3" /> Manual Edit
                                </button>
                                <button
                                  className={`flex items-center gap-1 text-xs px-3 py-1 ${
                                    row.status === 'flagged'
                                      ? 'bg-orange-100 text-orange-900 font-bold border-orange-400'
                                      : 'text-orange-700'
                                  }`}
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
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Right Validation Panel */}
      <div className="w-64 flex flex-col gap-2">
        <fieldset className="flex-1 flex flex-col overflow-hidden">
          <legend className="font-bold text-sm">Validation Results</legend>
          <div className="flex-1 overflow-auto p-2 flex flex-col gap-3">
            {selectedRow?.validationErrors && selectedRow.validationErrors.length > 0 ? (
              selectedRow.validationErrors.map((err, i) => (
                <div
                  key={i}
                  className={`flex items-start gap-2 p-2 border ${
                    err.severity === 'error'
                      ? 'bg-red-50 border-red-200'
                      : 'bg-yellow-50 border-yellow-200'
                  }`}
                >
                  {err.severity === 'error'
                    ? <RiErrorWarningFill className="size-5 text-red-600 shrink-0" />
                    : <RiAlertFill className="size-5 text-yellow-600 shrink-0" />}
                  <div>
                    <div className={`text-xs font-bold ${err.severity === 'error' ? 'text-red-800' : 'text-yellow-800'}`}>
                      {err.severity === 'error' ? 'Logic Conflict' : 'Quality Warning'}
                    </div>
                    <div className={`text-[10px] ${err.severity === 'error' ? 'text-red-700' : 'text-yellow-700'}`}>
                      {err.message}
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="flex items-start gap-2 p-2 bg-green-50 border border-green-200">
                <RiCheckboxCircleFill className="size-5 text-green-600 shrink-0" />
                <div>
                  <div className="text-xs font-bold text-green-800">Checks Passed</div>
                  <div className="text-[10px] text-green-700">This test case meets all AI quality standards.</div>
                </div>
              </div>
            )}
          </div>
        </fieldset>

        <button
          className="w-full py-3 flex items-center justify-center gap-2 font-bold default"
          onClick={() => openWindow('export', 'TC Generator - Export')}
        >
          <RiDownload2Line className="size-5" /> Export All
        </button>
      </div>

      {/* Floating action bar — shown when rows are selected */}
      {selectedIds.size > 0 && (
        <div className="absolute bottom-4 left-1/2 -translate-x-1/2 z-20 flex items-center gap-3 px-4 py-2 bg-gray-900 text-white shadow-lg border border-gray-600 min-w-[360px] justify-between">
          <span className="text-xs font-bold text-gray-300">
            {selectedIds.size} row{selectedIds.size > 1 ? 's' : ''} selected
          </span>
          <div className="flex gap-2">
            <button
              className="text-xs px-3 py-1 text-gray-400 hover:text-white"
              onClick={() => setSelectedIds(new Set())}
            >
              Clear
            </button>
            <button
              className="text-xs px-4 py-1 bg-blue-600 hover:bg-blue-500 font-bold flex items-center gap-1 disabled:opacity-50 disabled:cursor-not-allowed"
              onClick={handleRegenerate}
              disabled={isRegenerating}
            >
              <RiRefreshLine className={`size-4 ${isRegenerating ? 'animate-spin' : ''}`} />
              {isRegenerating ? 'Regenerating...' : `Regenerate ${selectedIds.size} Selected`}
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ReviewModule;
