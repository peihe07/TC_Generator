'use client';

import React from 'react';

export type ButtonVariant = 'default' | 'accept' | 'reject';

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /**
   * 視覺樣式變體。
   * - `default`：一般 Win95 按鈕（預設）。
   * - `accept`：深綠色文字，用於確認/接受操作。
   * - `reject`：深紅色文字，用於拒絕/刪除操作。
   */
  variant?: ButtonVariant;
}

const variantClass: Record<ButtonVariant, string> = {
  default: '',
  accept: 'btn-accept',
  reject: 'btn-reject',
};

/**
 * Win95 風格基礎按鈕，套用 98.css `.window button` 樣式與
 * 專案擴充的 `:focus-visible` / `:active` 視覺。
 *
 * 支援所有原生 `<button>` attributes（包含 `disabled`、`onClick`、
 * `aria-*` 等），並將 `className` 與變體 class 合併。
 */
export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  function Button(
    { variant = 'default', className, type = 'button', children, ...rest },
    ref,
  ) {
    const merged = [variantClass[variant], className].filter(Boolean).join(' ');
    return (
      <button ref={ref} type={type} className={merged || undefined} {...rest}>
        {children}
      </button>
    );
  },
);
