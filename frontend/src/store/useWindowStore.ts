"use client";

import { create } from "zustand";

import { WINDOW_DEFINITIONS } from "@/src/lib/constants";
import type { WindowId, WindowPosition, WindowState } from "@/src/lib/types";

type WindowStore = {
  windows: Record<WindowId, WindowState>;
  focusedWindowId: WindowId | null;
  nextZIndex: number;
  openWindow: (id: WindowId) => void;
  closeWindow: (id: WindowId) => void;
  focusWindow: (id: WindowId) => void;
  minimizeWindow: (id: WindowId) => void;
  toggleWindow: (id: WindowId) => void;
  updatePosition: (id: WindowId, position: WindowPosition) => void;
};

const initialWindows = Object.fromEntries(
  Object.entries(WINDOW_DEFINITIONS).map(([id, definition], index) => [
    id,
    {
      ...definition,
      isOpen: id === "upload",
      isMinimized: false,
      zIndex: id === "upload" ? 10 : index + 1,
    },
  ]),
) as Record<WindowId, WindowState>;

export const useWindowStore = create<WindowStore>((set, get) => ({
  windows: initialWindows,
  focusedWindowId: "upload",
  nextZIndex: 20,
  openWindow: (id) =>
    set((state) => ({
      windows: {
        ...state.windows,
        [id]: {
          ...state.windows[id],
          isOpen: true,
          isMinimized: false,
          zIndex: state.nextZIndex,
        },
      },
      focusedWindowId: id,
      nextZIndex: state.nextZIndex + 1,
    })),
  closeWindow: (id) =>
    set((state) => ({
      windows: {
        ...state.windows,
        [id]: {
          ...state.windows[id],
          isOpen: false,
          isMinimized: false,
        },
      },
      focusedWindowId: state.focusedWindowId === id ? null : state.focusedWindowId,
    })),
  focusWindow: (id) => {
    const { windows } = get();
    if (!windows[id].isOpen) {
      get().openWindow(id);
      return;
    }

    set((state) => ({
      windows: {
        ...state.windows,
        [id]: {
          ...state.windows[id],
          isMinimized: false,
          zIndex: state.nextZIndex,
        },
      },
      focusedWindowId: id,
      nextZIndex: state.nextZIndex + 1,
    }));
  },
  minimizeWindow: (id) =>
    set((state) => ({
      windows: {
        ...state.windows,
        [id]: {
          ...state.windows[id],
          isMinimized: true,
        },
      },
      focusedWindowId: state.focusedWindowId === id ? null : state.focusedWindowId,
    })),
  toggleWindow: (id) => {
    const windowState = get().windows[id];
    if (!windowState.isOpen || windowState.isMinimized) {
      get().focusWindow(id);
      return;
    }

    get().minimizeWindow(id);
  },
  updatePosition: (id, position) =>
    set((state) => ({
      windows: {
        ...state.windows,
        [id]: {
          ...state.windows[id],
          position,
        },
      },
    })),
}));
