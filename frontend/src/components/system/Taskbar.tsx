'use client';

import React, { useEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { useWindowStore, WindowID } from '../../store/useWindowStore';
import { TASKBAR_HEIGHT } from './layout';
import WorkspaceMenu from './WorkspaceMenu';
import JobHistoryMenu from './JobHistoryMenu';
import AgentTaskbarButton from '../modules/chat/AgentTaskbarButton';

const START_MENU_ITEMS: { label: string; icon: string; id: WindowID | null }[] = [
  { label: 'Upload',     icon: '📁', id: 'upload' },
  { label: 'Configure',  icon: '⚙',  id: 'configure' },
  { label: 'Generate',   icon: '▶',  id: 'generate' },
  { label: 'Review',     icon: '📋', id: 'review' },
  { label: 'Export',     icon: '💾', id: 'export' },
  { label: 'Quick TC',   icon: '⚡', id: 'quickGenerate' },
  { label: 'Diagrams',   icon: '📊', id: 'diagrams' },
  { label: 'TC Rules',   icon: '📖', id: 'rules' },
  { label: 'Agent',      icon: '🤖', id: 'chat' },
];

const WINDOW_TITLES: Record<WindowID, string> = {
  upload:        'TC Generator - Upload Files',
  configure:     'TC Generator - Configure',
  generate:      'TC Generator - Generate',
  review:        'TC Generator - Review',
  export:        'TC Generator - Export',
  quickGenerate: 'Quick TC Generator',
  diagrams:      'Architecture Diagrams',
  rules:         'TC Writing Rules',
  chat:          'Agent Co-pilot',
};

const Taskbar: React.FC = () => {
  const { windows, focusedWindowId, focusWindow, openWindow } = useWindowStore();
  const [time, setTime] = useState('');
  const [showStart, setShowStart] = useState(false);
  const [isMounted, setIsMounted] = useState(false);
  const startRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setIsMounted(true);
  }, []);

  useEffect(() => {
    const update = () => {
      const now = new Date();
      setTime(
        now.toLocaleString([], {
          year: 'numeric',
          month: '2-digit',
          day: '2-digit',
          hour: '2-digit',
          minute: '2-digit',
        })
      );
    };
    update();
    const timer = setInterval(update, 1000);
    return () => clearInterval(timer);
  }, []);

  // Close start menu when clicking outside
  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (startRef.current && !startRef.current.contains(e.target as Node)) {
        setShowStart(false);
      }
    };
    if (showStart) document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, [showStart]);

  const openWindows = Object.values(windows).filter(win => win.isOpen);

  const handleTaskbarClick = (id: WindowID) => {
    const win = windows[id];
    if (win.isMinimized || focusedWindowId !== id) {
      focusWindow(id);
    } else {
      // Click focused non-minimized window → minimize it
      useWindowStore.getState().minimizeWindow(id);
    }
  };

  const handleStartItemClick = (id: WindowID) => {
    setShowStart(false);
    openWindow(id, WINDOW_TITLES[id]);
  };

  if (!isMounted) return null;

  return createPortal(
    <div
      role="contentinfo"
      className="fixed z-[9999]"
      style={{ left: 0, right: 0, bottom: 0, height: TASKBAR_HEIGHT, zIndex: 9999 }}
    >
      {/* Start Menu */}
      {showStart && (
        <div ref={startRef} className="start-menu" style={{ bottom: TASKBAR_HEIGHT }}>
          <div style={{ display: 'flex', minHeight: 240 }}>
            {/* Side stripe */}
            <div className="start-menu-side">TC Generator</div>
            {/* Items */}
            <div style={{ flex: 1 }}>
              {START_MENU_ITEMS.map(({ label, icon, id }) => (
                <div
                  key={label}
                  className="start-menu-item"
                  onClick={() => id && handleStartItemClick(id)}
                >
                  <span style={{ fontSize: 16, lineHeight: 1 }}>{icon}</span>
                  <span>{label}</span>
                </div>
              ))}
              <hr className="start-menu-separator" />
              <div
                className="start-menu-item"
                onClick={() => setShowStart(false)}
              >
                <span style={{ fontSize: 16, lineHeight: 1 }}>🔒</span>
                <span>Close Menu</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Taskbar bar */}
      <div
        className="w-full h-full flex items-center px-1 gap-1"
        style={{
          background: '#c0c0c0',
          borderTop: '2px solid #ffffff',
          boxShadow: 'inset 1px 1px 0 #ffffff',
        }}
      >
        {/* Start button */}
        <button
          className={`flex items-center gap-1 font-bold px-2 ${showStart ? 'border-inset' : ''}`}
          style={{ height: 22, fontWeight: 'bold' }}
          onClick={() => setShowStart(v => !v)}
        >
          {/* Windows flag icon */}
          <svg width="14" height="14" viewBox="0 0 14 14" style={{ imageRendering: 'pixelated' }}>
            <rect x="0" y="0" width="6" height="6" fill="#ff0000"/>
            <rect x="8" y="0" width="6" height="6" fill="#00aa00"/>
            <rect x="0" y="8" width="6" height="6" fill="#0000ff"/>
            <rect x="8" y="8" width="6" height="6" fill="#ffff00"/>
          </svg>
          <span>Start</span>
        </button>

        {/* Separator */}
        <div style={{ width: 1, height: 18, background: '#808080', boxShadow: '1px 0 0 #fff', margin: '0 2px' }} />

        {/* Window tabs */}
        <div className="flex-1 flex gap-1 overflow-x-auto" style={{ minWidth: 0 }}>
          {openWindows.map((win) => {
            const isActive = focusedWindowId === win.id && !win.isMinimized;
            return (
              <button
                key={win.id}
                onClick={() => handleTaskbarClick(win.id as WindowID)}
                style={{
                  height: 22,
                  minWidth: 100,
                  maxWidth: 180,
                  padding: '0 6px',
                  textAlign: 'left',
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  whiteSpace: 'nowrap',
                  fontWeight: isActive ? 'bold' : 'normal',
                  borderStyle: isActive ? 'inset' : undefined,
                  opacity: win.isMinimized ? 0.75 : 1,
                }}
              >
                {win.isMinimized ? `[${win.title}]` : win.title}
              </button>
            );
          })}
        </div>

        {/* Separator */}
        <div style={{ width: 1, height: 18, background: '#808080', boxShadow: '1px 0 0 #fff', margin: '0 2px' }} />

        {/* Workspace manager */}
        <WorkspaceMenu />

        {/* Separator */}
        <div style={{ width: 1, height: 18, background: '#808080', boxShadow: '1px 0 0 #fff', margin: '0 2px' }} />

        {/* Job history */}
        <JobHistoryMenu />

        {/* Separator */}
        <div style={{ width: 1, height: 18, background: '#808080', boxShadow: '1px 0 0 #fff', margin: '0 2px' }} />

        {/* Agent Co-pilot */}
        <AgentTaskbarButton />

        {/* Separator */}
        <div style={{ width: 1, height: 18, background: '#808080', boxShadow: '1px 0 0 #fff', margin: '0 2px' }} />

        {/* Clock */}
        <div
          className="status-bar-field ml-auto flex items-center justify-end px-2"
          style={{ height: 22, minWidth: 150, textAlign: 'right', whiteSpace: 'nowrap' }}
        >
          {time}
        </div>
      </div>
    </div>,
    document.body
  );
};

export default Taskbar;
