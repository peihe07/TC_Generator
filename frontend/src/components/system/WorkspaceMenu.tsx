'use client';

import React, { useEffect, useRef, useState } from 'react';
import { useWorkspaceStore } from '../../store/useWorkspaceStore';
import { useJobStore } from '../../store/useJobStore';
import { Button, IconButton } from '../ui';

const WorkspaceMenu: React.FC = () => {
  const {
    workspaces, activeId, loaded,
    loadFromStorage, saveCurrentAs, overwriteActive, loadWorkspace, deleteWorkspace, renameWorkspace,
    exportWorkspace, importWorkspace,
  } = useWorkspaceStore();
  const resetJob = useJobStore((s) => s.resetJob);
  const [open, setOpen] = useState(false);
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
    if (!window.confirm('Start a new workspace? Current unsaved state will be cleared.')) return;
    resetJob();
    useWorkspaceStore.setState({ activeId: null });
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

  const handleImportClick = () => fileRef.current?.click();

  const handleImportFile = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    e.target.value = ''; // 允許重複選擇同一個檔案
    if (!file) return;
    try {
      const text = await file.text();
      const ws = importWorkspace(text);
      window.alert(`Imported "${ws.name}".`);
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
            <Button onClick={handleNew} style={{ flex: 1 }}>New</Button>
          </div>
          <div style={{ display: 'flex', gap: 4 }}>
            <Button onClick={handleImportClick} style={{ flex: 1 }}>Import…</Button>
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
    </div>
  );
};

export default WorkspaceMenu;
