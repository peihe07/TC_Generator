'use client';

import React, { useEffect, useRef, useState } from 'react';
import Draggable, { DraggableData, DraggableEvent } from 'react-draggable';
import { useWindowStore } from '../../store/useWindowStore';
import WindowManager from './WindowManager';
import Taskbar from './Taskbar';
import CostMeter from './CostMeter';
import { WindowID } from '../../store/useWindowStore';
import { TASKBAR_HEIGHT } from './layout';

const ICON_PX = 48;

const DESKTOP_ICONS: { id: WindowID; label: string }[] = [
  { id: 'upload',        label: 'Upload' },
  { id: 'configure',     label: 'Configure' },
  { id: 'generate',      label: 'Generate' },
  { id: 'review',        label: 'Review' },
  { id: 'export',        label: 'Export' },
  { id: 'quickGenerate', label: 'Quick TC' },
  { id: 'diagrams',      label: 'Diagrams' },
  { id: 'rules',         label: 'TC Rules' },
];

const WINDOW_TITLES: Record<WindowID, string> = {
  upload:        'TC Generator - Upload Files',
  configure:     'TC Generator - Configure',
  generate:      'TC Generator - Generate',
  review:        'TC Generator - Review',
  export:        'TC Generator - Export',
  quickGenerate: 'Quick TC Generator',
  diagrams:      'Workflow Diagrams',
  rules:         'TC Writing Rules',
};

// Default icon grid positions — laid out as a 5-per-column grid so the
// later icons stay above the fold on 13-14" laptops.
const ICON_W = 80;
const ICON_H = 92;
const ICON_GAP = 8;
const ICON_START_X = 12;
const ICON_START_Y = 12;
const ICONS_PER_COLUMN = 5;
const COLUMN_STEP_X = ICON_W + 12;

function defaultPositions(): Record<WindowID, { x: number; y: number }> {
  const pos: Partial<Record<WindowID, { x: number; y: number }>> = {};
  DESKTOP_ICONS.forEach(({ id }, i) => {
    const col = Math.floor(i / ICONS_PER_COLUMN);
    const row = i % ICONS_PER_COLUMN;
    pos[id] = {
      x: ICON_START_X + col * COLUMN_STEP_X,
      y: ICON_START_Y + row * (ICON_H + ICON_GAP),
    };
  });
  return pos as Record<WindowID, { x: number; y: number }>;
}

const LS_KEY = 'desktop-icon-positions';

/**
 * Snap any icon whose persisted position falls outside the current
 * viewport back to its default slot.
 */
function rescueOffscreenIcons(
  saved: Record<WindowID, { x: number; y: number }>,
  defaults: Record<WindowID, { x: number; y: number }>,
): Record<WindowID, { x: number; y: number }> {
  if (typeof window === 'undefined') return saved;
  const maxX = window.innerWidth - ICON_W;
  const maxY = window.innerHeight - ICON_H - 28; // leave room for taskbar
  const fixed = { ...saved };
  for (const { id } of DESKTOP_ICONS) {
    const p = fixed[id];
    if (!p || p.x < 0 || p.y < 0 || p.x > maxX || p.y > maxY) {
      fixed[id] = defaults[id];
    }
  }
  return fixed;
}

function loadPositions(): Record<WindowID, { x: number; y: number }> {
  const defaults = defaultPositions();
  try {
    const raw = localStorage.getItem(LS_KEY);
    if (raw) {
      const merged = { ...defaults, ...JSON.parse(raw) };
      return rescueOffscreenIcons(merged, defaults);
    }
  } catch {
    // ignore
  }
  return defaults;
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
              <img
                src={`/icons/desktop/${id}.svg`}
                width={ICON_PX}
                height={ICON_PX}
                style={{ imageRendering: 'pixelated' }}
                alt={label}
                draggable={false}
              />
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
