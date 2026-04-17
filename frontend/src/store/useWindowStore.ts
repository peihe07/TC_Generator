import { create } from 'zustand';

export type WindowID = 'upload' | 'configure' | 'generate' | 'review' | 'export' | 'quickGenerate' | 'diagrams' | 'rules';

interface WindowState {
  id: WindowID;
  title: string;
  isOpen: boolean;
  isMinimized: boolean;
  isMaximized: boolean;
  zIndex: number;
  position: { x: number; y: number };
  size: { width: number; height: number };
}

interface WindowStore {
  windows: Record<WindowID, WindowState>;
  focusedWindowId: WindowID | null;
  maxZIndex: number;

  openWindow: (id: WindowID, title: string, defaultSize?: { width: number; height: number }) => void;
  closeWindow: (id: WindowID) => void;
  minimizeWindow: (id: WindowID) => void;
  maximizeWindow: (id: WindowID) => void;
  focusWindow: (id: WindowID) => void;
  updatePosition: (id: WindowID, pos: { x: number; y: number }) => void;
  updateSize: (id: WindowID, size: { width: number; height: number }) => void;
}

const DEFAULT_WINDOWS: Record<WindowID, WindowState> = {
  upload: { id: 'upload', title: 'Upload Files', isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 50, y: 50 }, size: { width: 500, height: 400 } },
  configure: { id: 'configure', title: 'Configuration', isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 80, y: 80 }, size: { width: 600, height: 500 } },
  generate: { id: 'generate', title: 'Generation Progress', isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 150, y: 100 }, size: { width: 600, height: 480 } },
  review: { id: 'review', title: 'Review Results', isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 100, y: 50 }, size: { width: 900, height: 650 } },
  export: { id: 'export', title: 'Export', isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 200, y: 150 }, size: { width: 500, height: 450 } },
  quickGenerate: { id: 'quickGenerate', title: 'Quick TC Generator', isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 120, y: 80 }, size: { width: 860, height: 620 } },
  diagrams:      { id: 'diagrams',      title: 'Architecture Diagrams',  isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 160, y: 60 }, size: { width: 900, height: 680 } },
  rules:         { id: 'rules',         title: 'TC Writing Rules',        isOpen: false, isMinimized: false, isMaximized: false, zIndex: 10, position: { x: 180, y: 70 }, size: { width: 820, height: 640 } },
};

export const useWindowStore = create<WindowStore>((set) => ({
  windows: DEFAULT_WINDOWS,
  focusedWindowId: 'export',
  maxZIndex: 100,

  openWindow: (id, title, defaultSize) => set((state) => {
    const newMaxZ = state.maxZIndex + 1;
    return {
      windows: {
        ...state.windows,
        [id]: {
          ...state.windows[id],
          title,
          isOpen: true,
          isMinimized: false,
          zIndex: newMaxZ,
          ...(defaultSize ? { size: defaultSize } : {}),
        },
      },
      focusedWindowId: id,
      maxZIndex: newMaxZ,
    };
  }),

  closeWindow: (id) => set((state) => ({
    windows: {
      ...state.windows,
      [id]: { ...state.windows[id], isOpen: false },
    },
    focusedWindowId: state.focusedWindowId === id ? null : state.focusedWindowId,
  })),

  minimizeWindow: (id) => set((state) => ({
    windows: {
      ...state.windows,
      [id]: { ...state.windows[id], isMinimized: true },
    },
    focusedWindowId: state.focusedWindowId === id ? null : state.focusedWindowId,
  })),

  maximizeWindow: (id) => set((state) => ({
    windows: {
      ...state.windows,
      [id]: { ...state.windows[id], isMaximized: !state.windows[id].isMaximized },
    },
    focusedWindowId: id,
  })),

  focusWindow: (id) => set((state) => {
    const newMaxZ = state.maxZIndex + 1;
    return {
      windows: {
        ...state.windows,
        [id]: { ...state.windows[id], zIndex: newMaxZ, isMinimized: false },
      },
      focusedWindowId: id,
      maxZIndex: newMaxZ,
    };
  }),

  updatePosition: (id, pos) => set((state) => ({
    windows: {
      ...state.windows,
      [id]: { ...state.windows[id], position: pos },
    },
  })),

  updateSize: (id, size) => set((state) => ({
    windows: {
      ...state.windows,
      [id]: { ...state.windows[id], size },
    },
  })),
}));
