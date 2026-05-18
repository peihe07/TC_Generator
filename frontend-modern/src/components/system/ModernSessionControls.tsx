'use client';

import React, { useEffect, useRef, useState } from 'react';
import {
  RiAddLine,
  RiArrowDownSLine,
  RiDownload2Line,
  RiFlaskLine,
  RiFolderOpenLine,
  RiGitMergeLine,
  RiSave3Line,
  RiUpload2Line,
} from '@remixicon/react';
import { useJobStore } from '../../store/useJobStore';
import { useWindowStore } from '../../store/useWindowStore';
import { useWorkspaceStore } from '../../store/useWorkspaceStore';

export default function ModernSessionControls() {
  const {
    workspaces,
    activeId,
    loaded,
    loadFromStorage,
    saveCurrentAs,
    overwriteActive,
    loadWorkspace,
    exportWorkspace,
    importWorkspace,
    importIntoCurrentJob,
  } = useWorkspaceStore();
  const resetJob = useJobStore((s) => s.resetJob);
  const currentJobId = useJobStore((s) => s.jobMetadata?.jobId);
  const { openWindow, closeWindow } = useWindowStore();
  const [importMode, setImportMode] = useState<'new' | 'merge'>('new');
  const [menuOpen, setMenuOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);
  const fileRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (!loaded) loadFromStorage();
  }, [loaded, loadFromStorage]);

  useEffect(() => {
    if (!menuOpen) return;
    const handlePointerDown = (event: MouseEvent) => {
      if (!menuRef.current?.contains(event.target as Node)) {
        setMenuOpen(false);
      }
    };
    document.addEventListener('mousedown', handlePointerDown);
    return () => document.removeEventListener('mousedown', handlePointerDown);
  }, [menuOpen]);

  const active = workspaces.find((workspace) => workspace.id === activeId);

  const handleNewJob = () => {
    const ok = window.confirm('開始新的 job？目前 rows / logs / job progress 會清除，已儲存 workspace 與 history 會保留。');
    if (!ok) return;
    resetJob();
    useWorkspaceStore.setState({ activeId: null });
    (['configure', 'generate', 'review', 'export', 'quickGenerate'] as const).forEach(closeWindow);
    openWindow('upload', 'Upload Files');
    setMenuOpen(false);
  };

  const handleSaveAs = () => {
    const name = window.prompt('Workspace name:', active?.name ?? '');
    if (!name) return;
    saveCurrentAs(name);
    setMenuOpen(false);
  };

  const handleSave = () => {
    if (!activeId) {
      handleSaveAs();
      return;
    }
    overwriteActive();
    setMenuOpen(false);
  };

  const handleImportClick = () => {
    setImportMode('new');
    fileRef.current?.click();
    setMenuOpen(false);
  };

  const handleMergeClick = () => {
    if (!currentJobId) {
      window.alert('請先 Upload 原始 Excel 建立 job，再執行 Merge。');
      return;
    }
    setImportMode('merge');
    fileRef.current?.click();
    setMenuOpen(false);
  };

  const handleImportFile = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    event.target.value = '';
    if (!file) return;

    try {
      const text = await file.text();
      if (importMode === 'merge') {
        const { mergedRows } = importIntoCurrentJob(text);
        openWindow('review', 'Review');
        window.alert(`Merged ${mergedRows} tcRows into current job. 可直接 Export 使用目前 job 的原始 Excel 範本。`);
        return;
      }

      const workspace = importWorkspace(text);
      loadWorkspace(workspace.id);
      openWindow('review', 'Review');
      window.alert(`Imported "${workspace.name}" 並載入到 Review。`);
    } catch (error) {
      window.alert(`Import failed: ${(error as Error).message}`);
    }
  };

  const handleLoadWorkspace = (id: string) => {
    loadWorkspace(id);
    openWindow('review', 'Review');
    setMenuOpen(false);
  };

  const handleExportActive = () => {
    if (!activeId || !active) return;
    const json = exportWorkspace(activeId);
    if (!json) return;
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = `${active.name.replace(/[^\w-]+/g, '_')}.tcw.json`;
    anchor.click();
    URL.revokeObjectURL(url);
    setMenuOpen(false);
  };

  const handleLoadSampleRun = async () => {
    try {
      const existing = workspaces.find((workspace) => workspace.id === 'sample-projection-run');
      if (existing) {
        loadWorkspace(existing.id);
        openWindow('review', 'Review');
        setMenuOpen(false);
        return;
      }
      const response = await fetch('/samples/projection-sample-run.tcw.json');
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      const text = await response.text();
      const workspace = importWorkspace(text);
      loadWorkspace(workspace.id);
      openWindow('review', 'Review');
      setMenuOpen(false);
    } catch (error) {
      window.alert(`Load sample failed: ${(error as Error).message}`);
    }
  };

  const sortedWorkspaces = workspaces
    .slice()
    .sort((a, b) => b.updatedAt - a.updatedAt);

  return (
    <div ref={menuRef} className="modern-session-controls" aria-label="Job session controls">
      <button
        type="button"
        className="modern-session-trigger"
        aria-haspopup="menu"
        aria-expanded={menuOpen}
        onClick={() => setMenuOpen((open) => !open)}
      >
        <span className="modern-session-current">
          <span className="modern-session-label">Job Session</span>
          <strong>{active?.name ?? 'Unsaved workspace'}</strong>
        </span>
        <span className="modern-session-trigger-meta">
          <span>{workspaces.length} saved</span>
          <RiArrowDownSLine />
        </span>
      </button>

      {menuOpen && (
        <div className="modern-session-menu" role="menu">
          <div className="modern-session-menu-header">
            <span>Session Actions</span>
            <strong>{currentJobId ? 'Parsed job ready' : 'No parsed job'}</strong>
          </div>

          <div className="modern-session-action-grid">
            <button type="button" className="modern-session-menu-item" onClick={handleNewJob} role="menuitem">
              <RiAddLine />
              <span>
                <strong>New Job</strong>
                <small>Clear current rows and start upload</small>
              </span>
            </button>
            <button type="button" className="modern-session-menu-item" onClick={handleSave} role="menuitem">
              <RiSave3Line />
              <span>
                <strong>Save</strong>
                <small>{activeId ? 'Overwrite active workspace' : 'Create a named workspace'}</small>
              </span>
            </button>
            <button type="button" className="modern-session-menu-item" onClick={handleSaveAs} role="menuitem">
              <RiFolderOpenLine />
              <span>
                <strong>Save As</strong>
                <small>Store a separate snapshot</small>
              </span>
            </button>
            <button type="button" className="modern-session-menu-item item-teal" onClick={handleImportClick} role="menuitem">
              <RiUpload2Line />
              <span>
                <strong>Import</strong>
                <small>Open a .tcw.json workspace</small>
              </span>
            </button>
            <button
              type="button"
              className="modern-session-menu-item item-gold"
              onClick={handleMergeClick}
              disabled={!currentJobId}
              title={currentJobId ? 'Merge .tcw.json rows into the current parsed job' : '請先 Upload 原始 Excel 建立 job'}
              role="menuitem"
            >
              <RiGitMergeLine />
              <span>
                <strong>Merge</strong>
                <small>Keep current Excel source, replace rows</small>
              </span>
            </button>
            <button
              type="button"
              className="modern-session-menu-item"
              onClick={handleExportActive}
              disabled={!activeId}
              role="menuitem"
            >
              <RiDownload2Line />
              <span>
                <strong>Export JSON</strong>
                <small>Download active workspace</small>
              </span>
            </button>
            <button
              type="button"
              className="modern-session-menu-item item-sample"
              onClick={handleLoadSampleRun}
              role="menuitem"
            >
              <RiFlaskLine />
              <span>
                <strong>Load sample run</strong>
                <small>Projection workbook, 4 generated TCs</small>
              </span>
            </button>
          </div>

          <div className="modern-session-list-header">
            <span>Saved Workspaces</span>
            <small>{sortedWorkspaces.length}</small>
          </div>
          <div className="modern-session-list">
            {sortedWorkspaces.length === 0 && (
              <div className="modern-session-empty">No saved workspace yet.</div>
            )}
            {sortedWorkspaces.map((workspace) => (
              <button
                key={workspace.id}
                type="button"
                className="modern-session-workspace"
                data-active={workspace.id === activeId}
                onClick={() => handleLoadWorkspace(workspace.id)}
                role="menuitem"
              >
                <span>
                  <strong>{workspace.name}</strong>
                  <small>{new Date(workspace.updatedAt).toLocaleString()}</small>
                </span>
                <em>{workspace.snapshot.tcRows.length} TCs</em>
              </button>
            ))}
          </div>
        </div>
      )}

      <input
        ref={fileRef}
        type="file"
        accept=".json,application/json"
        style={{ display: 'none' }}
        onChange={handleImportFile}
      />
    </div>
  );
}
