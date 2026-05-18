import { describe, it, expect, beforeEach, vi } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useResizablePanel } from '../hooks/useResizablePanel';

/**
 * useResizablePanel — unit tests for the resizable panel hook.
 *
 * Coverage:
 *   - default width is the clamped `defaultWidth`
 *   - initial read from localStorage honors stored value
 *   - stored value outside [min, max] is clamped
 *   - each width change persists to localStorage
 *   - keyboard ArrowLeft / ArrowRight step by `step`, clamped
 *   - separatorProps have correct a11y attributes
 */

const STORAGE_KEY = 'test-panel-width';

beforeEach(() => {
  window.localStorage.clear();
});

describe('useResizablePanel', () => {
  it('starts at defaultWidth when storage is empty', () => {
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 320,
        minWidth: 200,
        maxWidth: 500,
      }),
    );
    expect(result.current.width).toBe(320);
  });

  it('restores persisted width on mount (within range)', () => {
    window.localStorage.setItem(STORAGE_KEY, '400');
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 320,
        minWidth: 200,
        maxWidth: 500,
      }),
    );
    expect(result.current.width).toBe(400);
  });

  it('clamps persisted width to minWidth', () => {
    window.localStorage.setItem(STORAGE_KEY, '50');
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 320,
        minWidth: 200,
        maxWidth: 500,
      }),
    );
    expect(result.current.width).toBe(200);
  });

  it('clamps persisted width to maxWidth', () => {
    window.localStorage.setItem(STORAGE_KEY, '9999');
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 320,
        minWidth: 200,
        maxWidth: 500,
      }),
    );
    expect(result.current.width).toBe(500);
  });

  it('persists width changes via keyboard', () => {
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 320,
        minWidth: 200,
        maxWidth: 500,
        step: 16,
      }),
    );
    const fakeEvent = {
      key: 'ArrowLeft',
      preventDefault: vi.fn(),
    } as unknown as React.KeyboardEvent<HTMLElement>;
    act(() => {
      result.current.separatorProps.onKeyDown(fakeEvent);
    });
    expect(result.current.width).toBe(336);
    expect(window.localStorage.getItem(STORAGE_KEY)).toBe('336');
  });

  it('ArrowLeft grows the panel, ArrowRight shrinks', () => {
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 320,
        minWidth: 200,
        maxWidth: 500,
        step: 16,
      }),
    );
    const leftEvent = {
      key: 'ArrowLeft',
      preventDefault: vi.fn(),
    } as unknown as React.KeyboardEvent<HTMLElement>;
    const rightEvent = {
      key: 'ArrowRight',
      preventDefault: vi.fn(),
    } as unknown as React.KeyboardEvent<HTMLElement>;
    act(() => {
      result.current.separatorProps.onKeyDown(leftEvent);
    });
    expect(result.current.width).toBe(336);
    act(() => {
      result.current.separatorProps.onKeyDown(rightEvent);
      result.current.separatorProps.onKeyDown(rightEvent);
    });
    expect(result.current.width).toBe(304);
  });

  it('keyboard changes are clamped to [min, max]', () => {
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 208,
        minWidth: 200,
        maxWidth: 500,
        step: 16,
      }),
    );
    const rightEvent = {
      key: 'ArrowRight',
      preventDefault: vi.fn(),
    } as unknown as React.KeyboardEvent<HTMLElement>;
    // 208 - 16 = 192, below min; should clamp to 200.
    act(() => {
      result.current.separatorProps.onKeyDown(rightEvent);
    });
    expect(result.current.width).toBe(200);
  });

  it('separatorProps carry correct a11y attributes', () => {
    const { result } = renderHook(() =>
      useResizablePanel({
        storageKey: STORAGE_KEY,
        defaultWidth: 320,
        minWidth: 200,
        maxWidth: 500,
      }),
    );
    const p = result.current.separatorProps;
    expect(p.role).toBe('separator');
    expect(p['aria-orientation']).toBe('vertical');
    expect(p['aria-valuenow']).toBe(320);
    expect(p['aria-valuemin']).toBe(200);
    expect(p['aria-valuemax']).toBe(500);
    expect(p.tabIndex).toBe(0);
  });
});
