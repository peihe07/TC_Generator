import { describe, it, expect, beforeEach } from 'vitest';
import { render, screen, cleanup } from '@testing-library/react';
import React from 'react';

import AppWindow from '../components/system/AppWindow';
import { useWindowStore, WindowID } from '../store/useWindowStore';

const WINDOW_IDS: WindowID[] = [
  'upload',
  'configure',
  'generate',
  'review',
  'export',
  'quickGenerate',
  'diagrams',
  'rules',
];

beforeEach(() => {
  const current = useWindowStore.getState();
  useWindowStore.setState({
    windows: Object.fromEntries(
      WINDOW_IDS.map((id) => [
        id,
        {
          ...current.windows[id],
          isOpen: false,
          isMinimized: false,
          isMaximized: false,
          zIndex: 10,
        },
      ]),
    ) as typeof current.windows,
    focusedWindowId: null,
    maxZIndex: 100,
  });
});

describe('AppWindow', () => {
  it('keeps maximized content scrollable without pushing title controls offscreen', () => {
    useWindowStore.setState((state) => ({
      windows: {
        ...state.windows,
        upload: {
          ...state.windows.upload,
          title: 'Upload Files',
          isOpen: true,
          isMaximized: true,
        },
      },
      focusedWindowId: 'upload',
    }));

    render(
      <AppWindow id="upload">
        <div style={{ height: 5000 }}>Tall content</div>
      </AppWindow>,
    );

    const outer = screen.getByTestId('app-window-upload-maximized');
    expect(outer).toHaveClass('min-h-0', 'overflow-hidden');
    expect(outer).toHaveStyle({ height: 'calc(100dvh - 28px)' });

    const body = screen.getByTestId('app-window-upload-body');
    expect(body).toHaveClass('min-h-0', 'overflow-hidden');

    const scroller = screen.getByTestId('app-window-upload-scroller');
    expect(scroller).toHaveClass('min-h-0', 'overflow-auto');

    expect(screen.getByRole('button', { name: 'Minimize' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Maximize' })).toBeInTheDocument();

    cleanup();
  });
});
