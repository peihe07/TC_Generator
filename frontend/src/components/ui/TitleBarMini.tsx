'use client';

import React from 'react';

export type TitleBarMiniVariant = 'default' | 'edit';

export interface TitleBarMiniProps
  extends Omit<React.HTMLAttributes<HTMLDivElement>, 'title'> {
  /** Leading icon (pre-sized, typically `size-3`). Rendered verbatim. */
  icon?: React.ReactNode;
  /**
   * Title text / node rendered as the flex-1 middle slot. Most call
   * sites pass a plain string; React nodes also work (e.g. conditional
   * "— EDIT MODE" suffixes).
   */
  title: React.ReactNode;
  /**
   * Visual variant:
   * - `default` — Win95 navy title bar (read-only card headers)
   * - `edit` — orange edit-accent bar (RegenDiff staging, active edit)
   */
  variant?: TitleBarMiniVariant;
  /**
   * Optional trailing content — badges, buttons, secondary labels.
   * Rendered after the title; no implicit styling, so callers keep full
   * control over spacing and layout.
   */
  children?: React.ReactNode;
}

const variantClass: Record<TitleBarMiniVariant, string> = {
  default: '',
  edit: 'edit',
};

/**
 * Miniature Win95 title bar used above "paper-card" content blocks
 * (TcCard, ReviewRow content cells, RegenDiff staging banner).
 *
 * Renders `<div class="title-bar-mini [edit]">` with an optional leading
 * icon, a flex-1 title slot, and any trailing children. Styling lives in
 * win95.css — this component only assembles the standard DOM shape.
 */
export const TitleBarMini = React.forwardRef<HTMLDivElement, TitleBarMiniProps>(
  function TitleBarMini(
    { icon, title, variant = 'default', className, children, ...rest },
    ref,
  ) {
    const merged = ['title-bar-mini', variantClass[variant], className]
      .filter(Boolean)
      .join(' ');
    return (
      <div ref={ref} className={merged} {...rest}>
        {icon}
        <span className="flex-1">{title}</span>
        {children}
      </div>
    );
  },
);
