import { useEffect, useRef, useState, useCallback } from 'react';

/**
 * Hook for a horizontally-resizable panel pinned to the **right side** of a
 * parent flex row. The panel width is controlled state; the caller renders
 * a splitter element and spreads the returned `separatorProps` onto it.
 *
 * Contract:
 * - Dragging the splitter LEFT grows the panel; RIGHT shrinks it.
 * - ← / → keys step by `step` px (default 16), same semantic as drag.
 * - Width is clamped to `[minWidth, maxWidth]`.
 * - Width persists to `localStorage[storageKey]`; read once on mount,
 *   written on every change (cheap — string of a small int).
 *
 * a11y: Splitter element receives `role="separator"`, `aria-orientation`,
 * `aria-valuenow/min/max`, and `tabIndex=0`, so screen readers announce it
 * as an interactive resizer and keyboard users can focus + adjust it.
 *
 * Touch/pen: implementation uses Pointer Events, so the same code path
 * handles mouse, touch, and stylus. `touch-action: none` on the splitter
 * element is recommended (set by `.splitter-v` CSS class).
 */
export interface UseResizablePanelOptions {
  storageKey: string;
  defaultWidth: number;
  minWidth: number;
  maxWidth: number;
  step?: number;
}

export interface SeparatorProps {
  role: 'separator';
  'aria-orientation': 'vertical';
  'aria-valuenow': number;
  'aria-valuemin': number;
  'aria-valuemax': number;
  tabIndex: 0;
  onPointerDown: (e: React.PointerEvent<HTMLElement>) => void;
  onKeyDown: (e: React.KeyboardEvent<HTMLElement>) => void;
}

export interface UseResizablePanelResult {
  width: number;
  separatorProps: SeparatorProps;
}

export function useResizablePanel({
  storageKey,
  defaultWidth,
  minWidth,
  maxWidth,
  step = 16,
}: UseResizablePanelOptions): UseResizablePanelResult {
  const clamp = useCallback(
    (n: number) => Math.min(maxWidth, Math.max(minWidth, n)),
    [minWidth, maxWidth],
  );

  const [width, setWidth] = useState<number>(() => clamp(defaultWidth));

  // Restore persisted width on mount. localStorage isn't available during
  // SSR, so we guard for that; Next.js App Router may render this hook in
  // a client-only module ("use client" in caller), but the guard is cheap.
  useEffect(() => {
    if (typeof window === 'undefined') return;
    const stored = window.localStorage.getItem(storageKey);
    if (stored === null) return;
    const parsed = parseInt(stored, 10);
    if (!Number.isNaN(parsed)) setWidth(clamp(parsed));
  }, [storageKey, clamp]);

  // Persist width (trailing write on every change — cheap for a small int).
  useEffect(() => {
    if (typeof window === 'undefined') return;
    window.localStorage.setItem(storageKey, String(width));
  }, [storageKey, width]);

  const dragRef = useRef<{ startX: number; startWidth: number } | null>(null);

  const onPointerDown = useCallback(
    (e: React.PointerEvent<HTMLElement>) => {
      e.preventDefault();
      dragRef.current = { startX: e.clientX, startWidth: width };
      // Capture pointer so we keep receiving move/up even if cursor leaves.
      e.currentTarget.setPointerCapture(e.pointerId);
    },
    [width],
  );

  // Global move/up handlers attached only while a drag is in progress. We
  // attach to window (not the splitter) so the drag can continue even if
  // the pointer drifts off the 4px splitter onto adjacent flex children.
  useEffect(() => {
    const onMove = (ev: PointerEvent) => {
      const drag = dragRef.current;
      if (!drag) return;
      // Splitter sits to the left of the panel: dragging LEFT (clientX
      // decreases) should GROW the panel.
      const delta = drag.startX - ev.clientX;
      setWidth(clamp(drag.startWidth + delta));
    };
    const onUp = () => {
      dragRef.current = null;
    };
    window.addEventListener('pointermove', onMove);
    window.addEventListener('pointerup', onUp);
    window.addEventListener('pointercancel', onUp);
    return () => {
      window.removeEventListener('pointermove', onMove);
      window.removeEventListener('pointerup', onUp);
      window.removeEventListener('pointercancel', onUp);
    };
  }, [clamp]);

  const onKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLElement>) => {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        setWidth((w) => clamp(w + step));
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        setWidth((w) => clamp(w - step));
      }
    },
    [clamp, step],
  );

  const separatorProps: SeparatorProps = {
    role: 'separator',
    'aria-orientation': 'vertical',
    'aria-valuenow': width,
    'aria-valuemin': minWidth,
    'aria-valuemax': maxWidth,
    tabIndex: 0,
    onPointerDown,
    onKeyDown,
  };

  return { width, separatorProps };
}
