'use client';

import React, { useCallback, useMemo, useState } from 'react';
import { useJobStore } from '../../../store/useJobStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { TcRow } from '../../../lib/types';
import { createJobLog } from '../../../lib/logging';
import {
  regenerateRows,
  rerunRows,
  type RerunSummary,
} from '../../../services/jobAdapter';
import { ReviewRow, type EditValues } from './ReviewRow';
import { ReviewToolbar } from './ReviewToolbar';
import { ReviewToolbox } from './ReviewToolbox';
import { ValidationPanel } from './ValidationPanel';
import type { DiffFieldKey } from './RegenDiff';
import { useResizablePanel } from '../../../hooks/useResizablePanel';
import { Win95Dialog } from '../../ui';

type PendingDelete = { kind: 'single'; id: string } | { kind: 'bulk' } | null;

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
    setAwaitingApply,
    applyRegenerated,
    clearAwaitingApply,
    isRegenerating,
    setRegenerating,
    addTcRowAfter,
    config,
    updateStats,
    appendLog,
  } = useJobStore();
  const { advanceWindow } = useWindowStore();

  // 允許同時展開多列
  const [expandedRows, setExpandedRows] = useState<Set<string>>(new Set());
  const [activeRowId, setActiveRowId] = useState<string | null>(null);
  const [editingId, setEditingRowId] = useState<string | null>(null);
  const [editValues, setEditValues] = useState<EditValues>({
    steps: '',
    expected: '',
    preConditions: '',
    inputTestData: '',
    designMethod: '',
    priority: '',
  });
  const [filter, setFilter] = useState('all');
  const [testSetFilter, setTestSetFilter] = useState('all');
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [pendingDelete, setPendingDelete] = useState<PendingDelete>(null);
  const [regenerateReason, setRegenerateReason] = useState('');
  // Re-run 完成後顯示一個明顯的摘要 dialog，讓 reviewer 不會懷疑「跑完沒？」
  const [rerunSummary, setRerunSummary] = useState<RerunSummary | null>(null);

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
      designMethod: row.designMethod ?? '',
      priority: row.priority ?? '',
    });
  };

  const saveEdit = (id: string) => {
    updateTcRow(id, {
      steps: editValues.steps,
      expectedResults: editValues.expected,
      preConditions: editValues.preConditions,
      inputTestData: editValues.inputTestData,
      designMethod: editValues.designMethod || undefined,
      priority: editValues.priority || undefined,
      status: 'accepted',
    });
    setEditingRowId(null);
  };

  const toggleFlag = (id: string, currentStatus: string) => {
    updateTcRow(id, { status: currentStatus === 'flagged' ? 'reviewing' : 'flagged' });
  };

  // Delete flows are confirm-dialog driven so destructive actions get a
  // Win95-style prompt rather than a native browser confirm(). See also
  // handleBulkDelete below; both funnel into `confirmDelete()` once the
  // user OKs in the dialog.
  const handleDelete = (id: string) => {
    setPendingDelete({ kind: 'single', id });
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
    setPendingDelete({ kind: 'bulk' });
  };

  /** Commit the pending delete action once the Win95Dialog is confirmed. */
  const confirmDelete = () => {
    if (!pendingDelete) return;
    if (pendingDelete.kind === 'single') {
      const id = pendingDelete.id;
      deleteTcRows([id]);
      collapseOne(id);
      if (editingId === id) setEditingRowId(null);
      setSelectedIds(new Set());
    } else {
      const ids = [...selectedIds];
      deleteTcRows(ids);
      appendLog(createJobLog('info', `Deleted ${ids.length} row(s).`));
      setExpandedRows((prev) => {
        const next = new Set(prev);
        ids.forEach((i) => next.delete(i));
        return next;
      });
      if (ids.includes(activeRowId ?? '')) setActiveRowId(null);
      setEditingRowId(null);
      setSelectedIds(new Set());
    }
    setPendingDelete(null);
  };

  const cancelDelete = () => setPendingDelete(null);

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
          regenerateReason: regenerateReason.trim(),
        },
        {
          onProgress: (usage) => {
            updateStats(usage);
          },
          onRow: (id, data) => {
            setAwaitingApply(id, data);
            updateTcRow(id, { status: 'reviewing' });
          },
          onFail: (id, message) => {
            updateTcRow(id, { status: 'fail' });
            appendLog(createJobLog('error', `${id}: ${message}`));
          },
          onRowAdded: (row, parentId) => {
            addTcRowAfter(parentId, row);
          },
          onReqSplit: (info) => {
            if (info.tcCount > 1) {
              appendLog(createJobLog('info', info.message || `${info.reqId}: split into ${info.tcCount} TC(s).`));
            }
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
      setRegenerateReason('');
    }
  }, [
    selectedIds,
    jobMetadata,
    setRegenerating,
    updateTcRow,
    setAwaitingApply,
    tcRows,
    config,
    regenerateReason,
    appendLog,
    updateStats,
    addTcRowAfter,
  ]);

  const handleRerun = useCallback(async () => {
    if (selectedIds.size === 0) return;
    setRegenerating(true);

    const ids = [...selectedIds];
    ids.forEach((id) => updateTcRow(id, { status: 'generating' }));

    try {
      appendLog(createJobLog('info', `Re-running ${ids.length} selected row(s) through the full pipeline.`));
      await rerunRows(
        {
          jobId: jobMetadata?.jobId ?? null,
          rowIds: ids,
          rows: tcRows,
          config,
          project: jobMetadata?.projectName ?? null,
        },
        {
          onProgress: (usage) => {
            updateStats(usage);
          },
          onPrimary: (row) => {
            // 覆蓋原列，保留 id / tcId。Re-run 不走 diff preview。
            updateTcRow(row.id, {
              ...row,
              awaitingApply: undefined,
            });
          },
          onRowAdded: (row, parentId) => {
            addTcRowAfter(parentId, row);
          },
          onReqSplit: (info) => {
            if (info.tcCount > 1) {
              appendLog(createJobLog('info', info.message));
            }
          },
          onFail: (id, message) => {
            updateTcRow(id, { status: 'fail' });
            appendLog(createJobLog('error', `${id}: ${message}`));
          },
          onComplete: (summary) => {
            const detail =
              `${summary.rowsUpdated} updated, ` +
              `${summary.rowsAdded} added, ` +
              `${summary.rowsFailed} failed`;
            appendLog(
              createJobLog('success', `Re-run complete (${detail}).`),
            );
            setRerunSummary(summary);
          },
          onError: (message) => {
            appendLog(createJobLog('warn', message));
          },
        },
      );
    } catch {
      ids.forEach((id) => updateTcRow(id, { status: 'fail' }));
      appendLog(createJobLog('error', 'Re-run failed.'));
    } finally {
      setRegenerating(false);
      setSelectedIds(new Set());
    }
  }, [
    selectedIds,
    jobMetadata,
    setRegenerating,
    updateTcRow,
    addTcRowAfter,
    tcRows,
    config,
    appendLog,
    updateStats,
  ]);

  const handleApplyRegen = (id: string, fields: DiffFieldKey[]) => {
    applyRegenerated(id, fields);
    collapseOne(id);
    setEditingRowId(null);
    setSelectedIds(new Set());
  };

  const allVisibleSelected =
    filteredRows.length > 0 && filteredRows.every((r) => selectedIds.has(r.id));

  // Map siblings (row uuid → tcId) for the "重複於" badge in ReviewRow.
  // Recomputed only when tcRows reference changes (cheap O(N) scan).
  const tcIdByRowId = React.useMemo(() => {
    const map = new Map<string, string>();
    for (const r of tcRows) {
      if (r.tcId) map.set(r.id, r.tcId);
    }
    return map;
  }, [tcRows]);
  const resolveSiblingTcId = React.useCallback(
    (rowId: string) => tcIdByRowId.get(rowId),
    [tcIdByRowId],
  );

  const { width: panelWidth, separatorProps } = useResizablePanel({
    storageKey: 'review-validation-panel-width',
    defaultWidth: 320,
    minWidth: 200,
    maxWidth: 500,
  });

  return (
    <div className="flex h-full overflow-hidden relative">
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
                  resolveSiblingTcId={resolveSiblingTcId}
                />
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Splitter — drag to resize ValidationPanel. See useResizablePanel. */}
      <div
        className="splitter-v"
        {...separatorProps}
        title="拖曳調整 Validation 面板寬度（← → 方向鍵 16px）"
        aria-label="Resize validation panel"
      />

      <ValidationPanel
        selectedRow={selectedRow}
        onExport={() => advanceWindow('review', 'export', 'TC Generator - Export')}
        onApplySuggestedReason={(reason) => {
          setRegenerateReason(reason);
          if (selectedRow) {
            setSelectedIds(new Set([selectedRow.id]));
          }
        }}
        width={panelWidth}
      />

      {selectedIds.size > 0 && (
        <ReviewToolbox
          selectedCount={selectedIds.size}
          isRegenerating={isRegenerating}
          onClear={() => setSelectedIds(new Set())}
          onBulkStatus={handleBulkStatus}
          onBulkDelete={handleBulkDelete}
          onRegenerate={handleRegenerate}
          onRerun={handleRerun}
          regenerateReason={regenerateReason}
          onRegenerateReasonChange={setRegenerateReason}
        />
      )}

      <Win95Dialog
        open={pendingDelete !== null}
        variant="warning"
        title="Confirm Delete"
        message={
          pendingDelete?.kind === 'bulk'
            ? `Delete ${selectedIds.size} selected test case(s)? This cannot be undone.`
            : 'Delete this test case? This cannot be undone.'
        }
        actions={[
          { label: 'Delete', variant: 'default', onClick: confirmDelete },
          { label: 'Cancel', variant: 'cancel', onClick: cancelDelete },
        ]}
        onClose={cancelDelete}
      />

      <Win95Dialog
        open={rerunSummary !== null}
        variant={
          rerunSummary && rerunSummary.rowsFailed > 0 ? 'warning' : 'info'
        }
        title="Re-run Complete"
        message={
          rerunSummary ? (
            <>
              <div style={{ marginBottom: 6 }}>
                AI 已完成 Re-run，結果如下：
              </div>
              <ul style={{ margin: '0 0 0 18px', padding: 0 }}>
                <li>
                  <strong>{rerunSummary.rowsUpdated}</strong> 筆原列被覆寫更新
                </li>
                <li>
                  <strong>{rerunSummary.rowsAdded}</strong> 筆新 TC 由 AI 拆出加入
                </li>
                <li>
                  <strong>{rerunSummary.rowsFailed}</strong> 筆失敗
                  {rerunSummary.rowsFailed > 0 ? '（請查看 row 狀態）' : ''}
                </li>
              </ul>
              {rerunSummary.rowsUpdated === 0 &&
                rerunSummary.rowsAdded === 0 &&
                rerunSummary.rowsFailed === 0 && (
                  <div
                    style={{
                      marginTop: 6,
                      color: 'var(--status-warn-dark, #7a5200)',
                    }}
                  >
                    沒有任何 row 被處理 — 可能是後端 stream 中斷或 selection
                    為空。請檢查 Generation log。
                  </div>
                )}
            </>
          ) : null
        }
        actions={[
          {
            label: 'OK',
            variant: 'default',
            onClick: () => setRerunSummary(null),
          },
        ]}
        onClose={() => setRerunSummary(null)}
      />
    </div>
  );
};

export default ReviewModule;
