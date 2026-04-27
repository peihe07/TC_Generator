'use client';

import React, { useEffect, useRef, useState } from 'react';
import { useWorkspaceStore } from '../../store/useWorkspaceStore';
import { useJobStore } from '../../store/useJobStore';
import { useWindowStore } from '../../store/useWindowStore';
import { Button, IconButton, Win95Dialog } from '../ui';

const WorkspaceMenu: React.FC = () => {
  const {
    workspaces, activeId, loaded,
    loadFromStorage, saveCurrentAs, overwriteActive, loadWorkspace, deleteWorkspace, renameWorkspace,
    exportWorkspace, importWorkspace, importIntoCurrentJob,
  } = useWorkspaceStore();
  const resetJob = useJobStore((s) => s.resetJob);
  const currentJobId = useJobStore((s) => s.jobMetadata?.jobId);
  const closeWindow = useWindowStore((s) => s.closeWindow);
  const openWindow = useWindowStore((s) => s.openWindow);
  const [open, setOpen] = useState(false);
  const [resetDialogOpen, setResetDialogOpen] = useState(false);
  const [resetPending, setResetPending] = useState(false);
  const [importMode, setImportMode] = useState<'new' | 'merge'>('new');
  const popRef = useRef<HTMLDivElement>(null);
  const fileRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  useEffect(() => {
    const h = (e: MouseEvent) => {
      if (popRef.current && !popRef.current.contains(e.target as Node)) setOpen(false);
    };
    if (open) document.addEventListener('mousedown', h);
    return () => document.removeEventListener('mousedown', h);
  }, [open]);

  const handleSaveAs = () => {
    const name = window.prompt('Workspace name:');
    if (!name) return;
    saveCurrentAs(name);
  };

  const handleOverwrite = () => {
    if (!activeId) return;
    if (!window.confirm('Overwrite current workspace with latest state?')) return;
    overwriteActive();
  };

  const handleNew = () => {
    const ok = window.confirm(
      '開始新的 job？\n\n' +
      '會清除：目前 job 的 rows / logs / 成本統計 + 流程視窗\n' +
      '會保留：Job History、已儲存 workspace、Config、已匯出檔案\n\n' +
      '（若要徹底清光所有資料，請改用下方的「Reset All Data…」）',
    );
    if (!ok) return;
    resetJob();
    useWorkspaceStore.setState({ activeId: null });
    // 關掉所有流程視窗（避免殘留舊 job 畫面），重開 Upload 當作新 job 起點。
    (['configure', 'generate', 'review', 'export', 'quickGenerate'] as const).forEach(closeWindow);
    openWindow('upload', 'Upload Files');
    setOpen(false);
  };

  const handleRename = (id: string, current: string) => {
    const name = window.prompt('Rename workspace:', current);
    if (!name) return;
    renameWorkspace(id, name);
  };

  const handleDelete = (id: string, name: string) => {
    if (!window.confirm(`Delete workspace "${name}"?`)) return;
    deleteWorkspace(id);
  };

  const handleExport = (id: string, name: string) => {
    const json = exportWorkspace(id);
    if (!json) return;
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${name.replace(/[^\w-]+/g, '_')}.tcw.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleResetConfirm = async () => {
    if (resetPending) return;
    setResetPending(true);
    try {
      const res = await fetch('/api/admin/reset', { method: 'DELETE' });
      if (!res.ok) {
        const detail = await res.text();
        throw new Error(detail || `HTTP ${res.status}`);
      }
      // Wipe only DATA keys (current job / history / workspaces). UI layout
      // keys like desktop icon positions and panel widths are preserved so
      // the user doesn't have to re-arrange the desktop after a reset.
      const DATA_KEYS = [
        'tc-job-session',              // useJobStore (persist middleware)
        'tc-generator-job-history',    // useJobHistoryStore
        'tc-generator-workspaces',     // useWorkspaceStore list
        'tc-generator-active-workspace', // useWorkspaceStore active id
      ];
      try {
        for (const key of DATA_KEYS) localStorage.removeItem(key);
        sessionStorage.clear();
      } catch {
        // storage disabled / private mode — reload is still useful
      }
      window.location.reload();
    } catch (err) {
      setResetPending(false);
      setResetDialogOpen(false);
      window.alert(`Reset failed: ${(err as Error).message}`);
    }
  };

  const handleImportClick = () => {
    setImportMode('new');
    fileRef.current?.click();
  };

  const handleMergeClick = () => {
    if (!currentJobId) {
      window.alert('請先 Upload 原始 Excel 建立 job，再執行 Merge。');
      return;
    }
    setImportMode('merge');
    fileRef.current?.click();
  };

  const handleImportFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    e.target.value = ''; // 允許重複選擇同一個檔案
    if (!file) return;
    try {
      const text = await file.text();
      if (importMode === 'merge') {
        const { mergedRows } = importIntoCurrentJob(text);
        openWindow('review', 'Review');
        window.alert(`Merged ${mergedRows} tcRows into current job. 可直接 Export 使用原始 Excel 範本。`);
      } else {
        const ws = importWorkspace(text);
        loadWorkspace(ws.id); // 直接套用到 Review，不用再手動點 Load
        openWindow('review', 'Review');
        window.alert(`Imported "${ws.name}" 並載入到 Review。`);
      }
    } catch (err) {
      window.alert(`Import failed: ${(err as Error).message}`);
    }
  };

  const active = workspaces.find((w) => w.id === activeId);

  return (
    <div ref={popRef} style={{ position: 'relative' }}>
      <Button
        style={{ height: 22, padding: '0 8px', maxWidth: 180, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}
        onClick={() => setOpen((v) => !v)}
        title="Workspace manager"
      >
        {active ? `📂 ${active.name}` : '📂 Workspace'}
      </Button>

      {open && (
        <div
          className="workspace-menu"
          style={{
            position: 'absolute',
            bottom: 26,
            right: 0,
            minWidth: 280,
            maxHeight: 320,
            background: 'var(--win95-gray)',
            border: '2px solid',
            borderColor: 'var(--win95-white) var(--win95-gray-mid) var(--win95-gray-mid) var(--win95-white)',
            boxShadow: '2px 2px 0 var(--win95-black)',
            padding: 4,
            zIndex: 10000,
            display: 'flex',
            flexDirection: 'column',
            gap: 4,
          }}
        >
          <div style={{ display: 'flex', gap: 4 }}>
            <Button onClick={handleSaveAs} style={{ flex: 1 }}>Save As…</Button>
            <Button onClick={handleOverwrite} disabled={!activeId} style={{ flex: 1 }}>Save</Button>
            <Button onClick={handleNew} style={{ flex: 1 }} title="清除目前 job（不動歷史與已存 workspace）">New Job</Button>
          </div>
          <div style={{ display: 'flex', gap: 4 }}>
            <Button onClick={handleImportClick} style={{ flex: 1 }}>Import…</Button>
            <Button
              onClick={handleMergeClick}
              disabled={!currentJobId}
              style={{ flex: 1 }}
              title={currentJobId ? '將 .tcw.json 的 tcRows 合併到目前 job，保留原始 Excel 範本' : '請先 Upload 原始 Excel'}
            >
              Merge…
            </Button>
            <input
              ref={fileRef}
              type="file"
              accept=".json,application/json"
              style={{ display: 'none' }}
              onChange={handleImportFile}
            />
          </div>

          <div style={{ fontSize: 11, fontWeight: 'bold', padding: '2px 4px', borderTop: '1px solid var(--win95-gray-mid)', marginTop: 2 }}>
            Saved Workspaces ({workspaces.length})
          </div>

          <div
            style={{
              display: 'flex',
              justifyContent: 'flex-end',
              borderTop: '1px solid var(--win95-gray-mid)',
              paddingTop: 4,
              marginTop: 2,
            }}
          >
            <Button
              onClick={() => {
                setOpen(false);
                setResetDialogOpen(true);
              }}
              title="Clear every job, trace, and browser cache"
              style={{ fontSize: 11, color: 'var(--status-reject-dark)' }}
            >
              Reset All Data…
            </Button>
          </div>

          <div style={{ overflowY: 'auto', maxHeight: 220, background: 'var(--win95-white)', border: '1px solid var(--win95-gray-mid)' }}>
            {workspaces.length === 0 && (
              <div style={{ padding: 8, fontSize: 11, color: 'var(--text-muted)', textAlign: 'center' }}>
                No saved workspaces yet.
              </div>
            )}
            {workspaces
              .slice()
              .sort((a, b) => b.updatedAt - a.updatedAt)
              .map((w) => (
                <div
                  key={w.id}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 4,
                    padding: '3px 4px',
                    background: w.id === activeId ? 'var(--win95-navy)' : undefined,
                    color: w.id === activeId ? 'var(--win95-white)' : undefined,
                    fontSize: 11,
                  }}
                >
                  <Button
                    onClick={() => loadWorkspace(w.id)}
                    style={{ flex: 1, textAlign: 'left', minWidth: 0, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}
                    title={`Load "${w.name}" (${w.snapshot.tcRows.length} TCs)`}
                  >
                    {w.name}
                    <span style={{ marginLeft: 4, opacity: 0.7, fontSize: 10 }}>
                      ({w.snapshot.tcRows.length} TCs)
                    </span>
                  </Button>
                  <IconButton label="Rename" onClick={() => handleRename(w.id, w.name)}>✎</IconButton>
                  <IconButton label="Export to JSON" onClick={() => handleExport(w.id, w.name)}>⤓</IconButton>
                  <IconButton label="Delete" onClick={() => handleDelete(w.id, w.name)}>✕</IconButton>
                </div>
              ))}
          </div>
        </div>
      )}

      <Win95Dialog
        open={resetDialogOpen}
        variant="error"
        title="Reset All Data"
        message={
          <>
            這會永久刪除以下資料，且無法復原：
            <ul style={{ margin: '6px 0 0 18px', padding: 0 }}>
              <li>所有 parse / generate / export job</li>
              <li>決策 trace</li>
              <li>瀏覽器暫存（目前 job、workspace layout、job history）</li>
            </ul>
            <div style={{ marginTop: 8 }}>
              已匯出的 <code>*_generated.xlsx</code> 檔不會被刪除。
            </div>
          </>
        }
        actions={[
          {
            label: 'Cancel',
            variant: 'default',
            onClick: () => setResetDialogOpen(false),
          },
          {
            label: resetPending ? 'Resetting…' : 'Reset',
            variant: 'cancel',
            onClick: handleResetConfirm,
          },
        ]}
        onClose={() => {
          if (!resetPending) setResetDialogOpen(false);
        }}
      />
    </div>
  );
};

export default WorkspaceMenu;
