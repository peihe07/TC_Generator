'use client';

import React, { useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';

/**
 * Win95Dialog — reusable confirm / warning / info dialog.
 * Matches design-system `preview/dialog.html`:
 *   360px wide · raised 2px bezel · heavy 4×4 drop shadow · navy title
 *   bar with chunky warning glyph · body flex-gap 14 · right-aligned
 *   action row · default action bolded via `.default` (98.css).
 *
 * a11y:
 *   - role="alertdialog", aria-labelledby, aria-describedby
 *   - Esc closes (via onClose)
 *   - Focus trap within dialog while open
 *   - Previous focus restored on close
 *   - Default action auto-focused on open
 *
 * Motion: none. Per design-system + MIGRATION.md Phase 4 rules,
 * dialog appears/disappears instantly — no fade, no slide.
 */

export type Win95DialogVariant = 'warning' | 'error' | 'info';

export interface Win95DialogAction {
  label: string;
  onClick: () => void;
  variant?: 'default' | 'cancel';
}

export interface Win95DialogProps {
  open: boolean;
  variant?: Win95DialogVariant;
  title: string;
  message: React.ReactNode;
  actions: Win95DialogAction[];
  /** Called on Esc key or title-bar close button. */
  onClose: () => void;
}

const GLYPH_STYLE: Record<Win95DialogVariant, { background: string; color: string; glyph: string }> = {
  warning: { background: 'var(--status-warn)', color: 'var(--win95-black)', glyph: '!' },
  error:   { background: 'var(--status-reject)', color: 'var(--win95-white)', glyph: '×' },
  info:    { background: 'var(--win95-navy)', color: 'var(--win95-white)', glyph: 'i' },
};

export const Win95Dialog: React.FC<Win95DialogProps> = ({
  open,
  variant = 'warning',
  title,
  message,
  actions,
  onClose,
}) => {
  const dialogRef = useRef<HTMLDivElement>(null);
  const defaultButtonRef = useRef<HTMLButtonElement>(null);
  const previousFocusRef = useRef<HTMLElement | null>(null);
  const titleId = React.useId();
  const messageId = React.useId();

  // Save + restore focus on open/close.
  useEffect(() => {
    if (!open) return;
    previousFocusRef.current = document.activeElement as HTMLElement | null;
    // Focus the default action first (or first action if no default).
    const target = defaultButtonRef.current ?? dialogRef.current?.querySelector('button');
    (target as HTMLElement | null)?.focus();
    return () => {
      previousFocusRef.current?.focus?.();
    };
  }, [open]);

  // Esc to close + Tab focus trap.
  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
        return;
      }
      if (e.key !== 'Tab') return;
      const node = dialogRef.current;
      if (!node) return;
      const focusables = node.querySelectorAll<HTMLElement>(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])',
      );
      if (focusables.length === 0) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, [open, onClose]);

  if (!open || typeof document === 'undefined') return null;

  const glyph = GLYPH_STYLE[variant];
  const defaultIdx = actions.findIndex((a) => a.variant === 'default');

  return createPortal(
    <div
      // Transparent overlay blocks clicks under the dialog without a
      // visible backdrop (Win95 dialogs don't dim the desktop).
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 10000,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'rgba(0, 0, 0, 0.1)',
      }}
      role="presentation"
    >
      <div
        ref={dialogRef}
        role="alertdialog"
        aria-modal="true"
        aria-labelledby={titleId}
        aria-describedby={messageId}
        style={{
          width: 360,
          background: 'var(--win95-gray)',
          border: '2px solid',
          borderColor:
            'var(--win95-white) var(--win95-gray-mid) var(--win95-gray-mid) var(--win95-white)',
          boxShadow: '4px 4px 0 rgba(0, 0, 0, 0.35)',
        }}
      >
        <div className="title-bar">
          <div
            id={titleId}
            className="title-bar-text"
            style={{ display: 'flex', alignItems: 'center', gap: 6 }}
          >
            <span
              aria-hidden="true"
              style={{
                width: 14,
                height: 14,
                background: glyph.background,
                color: glyph.color,
                border: '1px solid var(--win95-black)',
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 'bold',
                fontSize: 10,
              }}
            >
              {glyph.glyph}
            </span>
            {title}
          </div>
          <div className="title-bar-controls">
            <button aria-label="Close" onClick={onClose} />
          </div>
        </div>

        <div
          style={{
            padding: 16,
            display: 'flex',
            gap: 14,
            alignItems: 'flex-start',
          }}
        >
          <div
            aria-hidden="true"
            style={{
              width: 40,
              height: 40,
              background: glyph.background,
              color: glyph.color,
              border: '2px solid var(--win95-black)',
              fontWeight: 'bold',
              fontSize: 26,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              flexShrink: 0,
            }}
          >
            {glyph.glyph}
          </div>
          <div id={messageId} style={{ fontSize: 'var(--font-md)' }}>
            {message}
          </div>
        </div>

        <div
          style={{
            padding: '4px 12px 12px',
            display: 'flex',
            gap: 6,
            justifyContent: 'flex-end',
          }}
        >
          {actions.map((action, i) => (
            <button
              key={i}
              ref={i === defaultIdx ? defaultButtonRef : undefined}
              className={action.variant === 'default' ? 'default' : undefined}
              style={{ minWidth: 72 }}
              onClick={action.onClick}
            >
              {action.label}
            </button>
          ))}
        </div>
      </div>
    </div>,
    document.body,
  );
};

export default Win95Dialog;
