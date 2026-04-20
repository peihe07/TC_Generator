'use client';

import React, { useCallback, useMemo, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { TcRow } from '../../../lib/types';
import { createJobLog } from '../../../lib/logging';
import { regenerateRows } from '../../../services/jobAdapter';
import { ReviewRow, type EditValues } from './ReviewRow';
import { ReviewToolbar } from './ReviewToolbar';
import { ReviewToolbox } from './ReviewToolbox';
import { ValidationPanel } from './ValidationPanel';
import type { DiffFieldKey } from './RegenDiff';

/**
 * Review module orchestrator.
 *
 * 職責切分：
 *   - ReviewModule (此檔)：state + data flow + store interaction
 *   - ReviewToolbar     : 頂部 filter + help
 *   - ReviewRow         : 單列 (含展開編輯 / regen diff)
 *   - ValidationPanel   : 右側驗證結果
 *   - ReviewToolbox     : 浮動 bulk action
 */
const ReviewModule: React.FC = () => {
  const {
    tcRows,
    jobMetadata,
    updateTcRow,
    deleteTcRows,
    renumberTcRows,
    setAwaitingApply,
    applyRegenerated,
    clearAwaitingApply,
    isRegenerating,
    setRegenerating,
    config,
    appendLog,
  } = useJobStore();
  const { openWindow } = useWindowStore();

  // 允許同時展開多列
  const [expandedRows, setExpandedRows] = useState<Set<string>>(new Set());
  const [activeRowId, setActiveRowId] = useState<string | null>(null);
  const [editingId, setEditingRowId] = useState<string | null>(null);
  const [editValues, setEditValues] = useState<EditValues>({
    steps: '',
    expected: '',
    preConditions: '',
    inputTestData: '',
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

  const testSetOptions = useMemo(
    () => [...new Set(tcRows.map((row) => row.testSet).filter(Boolean))].sort(),
    [tcRows],
  );

  const filteredRows = tcRows.filter((r) => {
    if (testSetFilter !== 'all' && r.testSet !== testSetFilter) return false;
    if (filter === 'flagged') return r.status === 'flagged';
    if (filter === 'pending') return r.status === 'pending';
    if (filter === 'regen') return !!r.awaitingApply;
    return true;
  });

  const toggleSelectAll = () => {
    const visible = filteredRows.map((r) => r.id);
    const allSelected = visible.every((id) => selectedIds.has(id));
    if (allSelected) {
      setSelectedIds((prev) => {
        const next = new Set(prev);
        visible.forEach((id) => next.delete(id));
        return next;
      });
    } else {
      setSelectedIds((prev) => {
        const next = new Set(prev);
        visible.forEach((id) => next.add(id));
        return next;
      });
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
    setExpandedRows((prev) => {
      const next = new Set(prev);
      ids.forEach((i) => next.delete(i));
      return next;
    });
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
            setAwaitingApply(id, data);
            updateTcRow(id, { status: 'reviewing' });
          },
          onFail: (id, message) => {
            updateTcRow(id, { status: 'fail' });
            appendLog(createJobLog('error', `${id}: ${message}`));
          },
          onComplete: () => {
            appendLog(
              createJobLog(
                'success',
                'Re-generation complete. Review highlighted rows before applying.',
              ),
            );
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
  }, [
    selectedIds,
    jobMetadata,
    setRegenerating,
    updateTcRow,
    setAwaitingApply,
    tcRows,
    config,
    appendLog,
  ]);

  const handleApplyRegen = (id: string, fields: DiffFieldKey[]) => {
    applyRegenerated(id, fields);
    renumberTcRows();
    collapseOne(id);
    setEditingRowId(null);
    setSelectedIds(new Set());
  };

  const allVisibleSelected =
    filteredRows.length > 0 && filteredRows.every((r) => selectedIds.has(r.id));

  const helpContextPrompt =
    `[context: 目前在 Review Module, job=${jobMetadata?.jobId ?? '未開啟 job'}]\n` +
    `[Validator: ${tcRows.filter((r) => (r.validationErrors ?? []).length > 0).length} warnings]\n`;

  return (
    <div className="flex h-full gap-2 overflow-hidden relative">
      {/* Main Table Area */}
      <div className="flex-1 flex flex-col min-w-0">
        <ReviewToolbar
          filter={filter}
          onFilterChange={setFilter}
          testSetFilter={testSetFilter}
          onTestSetFilterChange={setTestSetFilter}
          testSetOptions={testSetOptions}
          totalCount={tcRows.length}
          acceptedCount={tcRows.filter((r) => r.status === 'accepted').length}
          expandedCount={expandedRows.size}
          helpContextPrompt={helpContextPrompt}
        />

        {/* Table */}
        <div className="flex-1 overflow-auto border-sunken bg-white">
          <table className="w-full text-sm border-collapse">
            <thead className="sticky top-0 z-10">
              <tr>
                <th className="win95-th center" style={{ width: 32 }}>
                  <div
                    style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                  >
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
                <th className="win95-th center" style={{ width: 112 }}>
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {filteredRows.map((row) => (
                <ReviewRow
                  key={row.id}
                  row={row}
                  isExpanded={expandedRows.has(row.id)}
                  isSelected={selectedIds.has(row.id)}
                  isActive={activeRowId === row.id}
                  isEditing={editingId === row.id}
                  editValues={editValues}
                  onToggleExpand={toggleExpand}
                  onToggleSelect={toggleSelectRow}
                  onSetActive={setActiveRowId}
                  onStatusChange={handleStatusChange}
                  onDelete={handleDelete}
                  onStartEdit={startEditing}
                  onEditValuesChange={setEditValues}
                  onSaveEdit={saveEdit}
                  onCancelEdit={() => setEditingRowId(null)}
                  onToggleFlag={toggleFlag}
                  onApplyRegen={handleApplyRegen}
                  onDiscardRegen={clearAwaitingApply}
                />
              ))}
            </tbody>
          </table>
        </div>
      </div>

      <ValidationPanel
        selectedRow={selectedRow}
        onExport={() => openWindow('export', 'TC Generator - Export')}
      />

      {selectedIds.size > 0 && (
        <ReviewToolbox
          selectedCount={selectedIds.size}
          isRegenerating={isRegenerating}
          onClear={() => setSelectedIds(new Set())}
          onBulkStatus={handleBulkStatus}
          onBulkDelete={handleBulkDelete}
          onRegenerate={handleRegenerate}
        />
      )}
    </div>
  );
};

export default ReviewModule;
