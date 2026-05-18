'use client';

import React from 'react';
import type { ButtonVariant } from './Button';

export interface IconButtonProps
  extends Omit<React.ButtonHTMLAttributes<HTMLButtonElement>, 'aria-label'> {
  /**
   * 視覺樣式變體（同 Button）。
   */
  variant?: ButtonVariant;
  /**
   * 按鈕說明文字。同時套用到 `title`（滑鼠懸停提示）與
   * `aria-label`（screen reader 念出），**不可省略**——icon-only
   * 按鈕若缺少 aria-label 將無法被輔助科技使用。
   */
  label: string;
}

const variantClass: Record<ButtonVariant, string> = {
  default: 'btn-icon',
  accept: 'btn-icon btn-accept',
  reject: 'btn-icon btn-reject',
};

/**
 * 22×22 的方形 icon 按鈕（套用 `.btn-icon` class）。
 *
 * 與 Button 的差別：`label` 為必填，強制每顆 icon button 都有
 * 可及性名稱——避免 screen reader 只念出「button」而無語意。
 */
export const IconButton = React.forwardRef<HTMLButtonElement, IconButtonProps>(
  function IconButton(
    { variant = 'default', label, className, type = 'button', children, ...rest },
    ref,
  ) {
    const merged = [variantClass[variant], className].filter(Boolean).join(' ');
    return (
      <button
        ref={ref}
        type={type}
        title={label}
        aria-label={label}
        className={merged}
        {...rest}
      >
        {children}
      </button>
    );
  },
);
