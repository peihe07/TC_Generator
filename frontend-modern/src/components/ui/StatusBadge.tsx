'use client';

import React from 'react';

export type StatusVariant =
  | 'accepted'
  | 'rejected'
  | 'flagged'
  | 'fail'
  | 'pending'
  | 'reviewing'
  | 'generating';

export interface StatusBadgeProps
  extends Omit<React.HTMLAttributes<HTMLSpanElement>, 'children'> {
  /**
   * 狀態語意。對應到 win95.css 中 `.status-badge.<status>` 樣式。
   */
  status: StatusVariant;
  /**
   * 顯示的標籤文字。若省略，預設用大寫後的 `status` 字串
   * （例如 `accepted` → `ACCEPTED`）。
   */
  children?: React.ReactNode;
}

/**
 * 狀態徽章，套用 win95.css 的 `.status-badge` sunken 視覺。
 *
 * 注意：為了色盲可及性，徽章同時用顏色與**文字**表達狀態，
 * 避免純色彩依賴（例如綠色=accepted）。
 */
export const StatusBadge = React.forwardRef<HTMLSpanElement, StatusBadgeProps>(
  function StatusBadge({ status, className, children, ...rest }, ref) {
    const merged = ['status-badge', status, className].filter(Boolean).join(' ');
    return (
      <span ref={ref} className={merged} {...rest}>
        {children ?? status.toUpperCase()}
      </span>
    );
  },
);
