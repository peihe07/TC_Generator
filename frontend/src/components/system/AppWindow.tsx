"use client";

import { useRef } from "react";
import {
  RiCheckboxBlankLine,
  RiCloseLine,
  RiSubtractLine,
} from "@remixicon/react";

import type { WindowId, WindowState } from "@/src/lib/types";
import { useWindowStore } from "@/src/store/useWindowStore";

type AppWindowProps = {
  windowState: WindowState;
  children: React.ReactNode;
};

export function AppWindow({ windowState, children }: AppWindowProps) {
  const focusWindow = useWindowStore((state) => state.focusWindow);
  const minimizeWindow = useWindowStore((state) => state.minimizeWindow);
  const closeWindow = useWindowStore((state) => state.closeWindow);
  const updatePosition = useWindowStore((state) => state.updatePosition);
  const focusedWindowId = useWindowStore((state) => state.focusedWindowId);
  const dragState = useRef<{
    id: WindowId;
    offsetX: number;
    offsetY: number;
  } | null>(null);

  if (!windowState.isOpen || windowState.isMinimized) {
    return null;
  }

  return (
    <section
      className="window app-window"
      style={{
        width: windowState.size.width,
        height: windowState.size.height,
        left: windowState.position.x,
        top: windowState.position.y,
        zIndex: windowState.zIndex,
      }}
      onMouseDown={() => focusWindow(windowState.id)}
    >
      <div
        className={`title-bar ${windowState.id === focusedWindowId ? "is-focused" : "is-muted"}`}
        onMouseDown={(event) => {
          focusWindow(windowState.id);
          dragState.current = {
            id: windowState.id,
            offsetX: event.clientX - windowState.position.x,
            offsetY: event.clientY - windowState.position.y,
          };

          const onMove = (moveEvent: MouseEvent) => {
            if (!dragState.current) {
              return;
            }

            updatePosition(windowState.id, {
              x: Math.max(8, moveEvent.clientX - dragState.current.offsetX),
              y: Math.max(8, moveEvent.clientY - dragState.current.offsetY),
            });
          };

          const onUp = () => {
            dragState.current = null;
            globalThis.window.removeEventListener("mousemove", onMove);
            globalThis.window.removeEventListener("mouseup", onUp);
          };

          globalThis.window.addEventListener("mousemove", onMove);
          globalThis.window.addEventListener("mouseup", onUp);
        }}
      >
        <div className="title-bar-text">{windowState.title}</div>
        <div className="title-bar-controls">
          <button
            aria-label={`Minimize ${windowState.title}`}
            onClick={() => minimizeWindow(windowState.id)}
          >
            <RiSubtractLine size={12} />
          </button>
          <button
            aria-label={`Focus ${windowState.title}`}
            onClick={() => focusWindow(windowState.id)}
          >
            <RiCheckboxBlankLine size={12} />
          </button>
          <button
            aria-label={`Close ${windowState.title}`}
            onClick={() => closeWindow(windowState.id)}
          >
            <RiCloseLine size={12} />
          </button>
        </div>
      </div>
      <div className="window-body window-body-shell">{children}</div>
    </section>
  );
}
