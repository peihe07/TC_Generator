'use client';

import React, { useEffect, useRef, useState } from 'react';
import Draggable, { DraggableData, DraggableEvent } from 'react-draggable';
import { useWindowStore } from '../../store/useWindowStore';
import WindowManager from './WindowManager';
import Taskbar from './Taskbar';
import CostMeter from './CostMeter';
import { WindowID } from '../../store/useWindowStore';
import { TASKBAR_HEIGHT } from './layout';

// Pixel-art icons — 64x64 (2x integer scale of 32x32 grid) + crispEdges for sharp pixels
const ICON_PX = 48;
const ICONS: Record<WindowID, React.ReactNode> = {
  upload: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="4" y="20" width="24" height="8" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="6" y="22" width="20" height="4" fill="#ffffff"/>
      <polygon points="16,4 8,16 13,16 13,20 19,20 19,16 24,16" fill="#ffff00" stroke="#000" strokeWidth="1"/>
    </svg>
  ),
  configure: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="13" y="2"  width="6" height="4" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="13" y="26" width="6" height="4" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="2"  y="13" width="4" height="6" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="26" y="13" width="4" height="6" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <circle cx="16" cy="16" r="6" fill="#008080" stroke="#000" strokeWidth="1"/>
      <circle cx="16" cy="16" r="3" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
    </svg>
  ),
  generate: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="3" y="4" width="26" height="24" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="4" y="5" width="24" height="14" fill="#000080"/>
      <polygon points="12,9 12,17 22,13" fill="#00ff00"/>
      <rect x="6" y="22" width="6" height="2" fill="#808080"/>
      <rect x="14" y="22" width="12" height="2" fill="#808080"/>
    </svg>
  ),
  review: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="4" y="3" width="24" height="26" fill="#ffffff" stroke="#000" strokeWidth="1"/>
      <rect x="4" y="3" width="24" height="4" fill="#000080"/>
      <rect x="7" y="11" width="18" height="2" fill="#000080"/>
      <rect x="7" y="15" width="18" height="2" fill="#000080"/>
      <rect x="7" y="19" width="12" height="2" fill="#000080"/>
      <polyline points="7,24 10,27 16,21" fill="none" stroke="#008000" strokeWidth="2"/>
    </svg>
  ),
  export: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="4" y="20" width="24" height="8" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="6" y="22" width="20" height="4" fill="#ffffff"/>
      <polygon points="16,28 8,16 13,16 13,4 19,4 19,16 24,16" fill="#00aa00" stroke="#000" strokeWidth="1"/>
    </svg>
  ),
  quickGenerate: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <polygon points="18,2 10,18 15,18 14,30 22,14 17,14" fill="#ffff00" stroke="#000" strokeWidth="1"/>
    </svg>
  ),
  diagrams: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="2"  y="2"  width="10" height="7" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="20" y="2"  width="10" height="7" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
      <rect x="11" y="23" width="10" height="7" fill="#008080" stroke="#000" strokeWidth="1"/>
      <line x1="7"  y1="9"  x2="7"  y2="16" stroke="#000" strokeWidth="1"/>
      <line x1="25" y1="9"  x2="25" y2="16" stroke="#000" strokeWidth="1"/>
      <line x1="7"  y1="16" x2="16" y2="16" stroke="#000" strokeWidth="1"/>
      <line x1="25" y1="16" x2="16" y2="16" stroke="#000" strokeWidth="1"/>
      <line x1="16" y1="16" x2="16" y2="23" stroke="#000" strokeWidth="1"/>
    </svg>
  ),
  rules: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="4" y="2" width="20" height="28" fill="#ffffff" stroke="#000" strokeWidth="1"/>
      <rect x="4" y="2" width="20" height="5" fill="#000080"/>
      <rect x="7" y="10" width="14" height="2" fill="#000080"/>
      <rect x="7" y="14" width="14" height="2" fill="#000080"/>
      <rect x="7" y="18" width="10" height="2" fill="#000080"/>
      <rect x="7" y="22" width="12" height="2" fill="#000080"/>
      <rect x="26" y="6" width="2" height="22" fill="#c0c0c0" stroke="#000" strokeWidth="1"/>
    </svg>
  ),
  chat: (
    <svg width={ICON_PX} height={ICON_PX} viewBox="0 0 32 32" shapeRendering="crispEdges">
      <rect x="4" y="4" width="24" height="18" fill="#000080" stroke="#000" strokeWidth="1"/>
      <rect x="6" y="6" width="20" height="14" fill="#0000cc"/>
      <rect x="8" y="9" width="4" height="4" fill="#00ff00"/>
      <rect x="14" y="9" width="4" height="4" fill="#00ff00"/>
      <rect x="20" y="9" width="4" height="4" fill="#00ff00"/>
      <polygon points="10,22 14,22 12,28" fill="#000080"/>
    </svg>
  ),
};

const DESKTOP_ICONS: { id: WindowID; label: string }[] = [
  { id: 'upload',        label: 'Upload' },
  { id: 'configure',     label: 'Configure' },
  { id: 'generate',      label: 'Generate' },
  { id: 'review',        label: 'Review' },
  { id: 'export',        label: 'Export' },
  { id: 'quickGenerate', label: 'Quick TC' },
  { id: 'diagrams',      label: 'Diagrams' },
  { id: 'rules',         label: 'TC Rules' },
  { id: 'chat',          label: 'Agent' },
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

// Default icon grid positions (left column, top-to-bottom)
const ICON_W = 80;
const ICON_H = 92;
const ICON_GAP = 8;
const ICON_START_X = 12;
const ICON_START_Y = 12;

function defaultPositions(): Record<WindowID, { x: number; y: number }> {
  const pos: Partial<Record<WindowID, { x: number; y: number }>> = {};
  DESKTOP_ICONS.forEach(({ id }, i) => {
    pos[id] = {
      x: ICON_START_X,
      y: ICON_START_Y + i * (ICON_H + ICON_GAP),
    };
  });
  return pos as Record<WindowID, { x: number; y: number }>;
}

const LS_KEY = 'desktop-icon-positions';

function loadPositions(): Record<WindowID, { x: number; y: number }> {
  try {
    const raw = localStorage.getItem(LS_KEY);
    if (raw) return { ...defaultPositions(), ...JSON.parse(raw) };
  } catch {
    // ignore
  }
  return defaultPositions();
}

const Desktop: React.FC = () => {
  const { openWindow } = useWindowStore();
  const [hasMounted, setHasMounted] = useState(false);
  const [selectedIcon, setSelectedIcon] = useState<WindowID | null>(null);
  const [positions, setPositions] = useState<Record<WindowID, { x: number; y: number }>>(defaultPositions);
  // Track dragged distance to distinguish click vs drag
  const dragMovedRef = useRef<Record<string, boolean>>({});
  // nodeRefs for react-draggable (avoids findDOMNode warning)
  const nodeRefs = useRef<Partial<Record<WindowID, React.RefObject<HTMLDivElement | null>>>>({});
  DESKTOP_ICONS.forEach(({ id }) => {
    if (!nodeRefs.current[id]) {
      nodeRefs.current[id] = React.createRef<HTMLDivElement>();
    }
  });

  useEffect(() => {
    setHasMounted(true);
    setPositions(loadPositions());
  }, []);

  const handleDragStop = (id: WindowID, _e: DraggableEvent, data: DraggableData) => {
    const next = { ...positions, [id]: { x: data.x, y: data.y } };
    setPositions(next);
    try { localStorage.setItem(LS_KEY, JSON.stringify(next)); } catch { /* ignore */ }
  };

  const handleDesktopClick = (e: React.MouseEvent) => {
    if ((e.target as HTMLElement).closest('.desktop-icon')) return;
    setSelectedIcon(null);
  };

  if (!hasMounted) return null;

  return (
    <div
      className="desktop-bg relative w-screen h-dvh overflow-hidden select-none"
      style={{ paddingBottom: TASKBAR_HEIGHT }}
      onClick={handleDesktopClick}
    >
      {/* Draggable desktop icons */}
      {DESKTOP_ICONS.map(({ id, label }) => (
        <Draggable
          key={id}
          nodeRef={nodeRefs.current[id] as React.RefObject<HTMLElement>}
          position={positions[id]}
          onStart={() => { dragMovedRef.current[id] = false; }}
          onDrag={() => { dragMovedRef.current[id] = true; }}
          onStop={(e, data) => handleDragStop(id, e, data)}
          bounds="parent"
        >
          <div
            ref={nodeRefs.current[id]}
            className={`desktop-icon absolute ${selectedIcon === id ? 'selected' : ''}`}
            style={{ width: ICON_W, zIndex: 1 }}
            onClick={(e) => {
              e.stopPropagation();
              if (!dragMovedRef.current[id]) setSelectedIcon(id);
            }}
            onDoubleClick={() => {
              if (!dragMovedRef.current[id]) openWindow(id, WINDOW_TITLES[id]);
            }}
          >
            <div className="desktop-icon-img flex items-center justify-center" style={{ width: ICON_PX, height: ICON_PX }}>
              {ICONS[id]}
            </div>
            <span className="desktop-icon-label">{label}</span>
          </div>
        </Draggable>
      ))}

      {/* Cost meter — top right corner */}
      <CostMeter />

      <WindowManager />
      <Taskbar />
    </div>
  );
};

export default Desktop;
