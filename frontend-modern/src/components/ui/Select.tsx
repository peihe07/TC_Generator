'use client';

import React from 'react';

export interface SelectOption {
  value: string;
  label: string;
  disabled?: boolean;
}

export interface SelectProps
  extends React.SelectHTMLAttributes<HTMLSelectElement> {
  /**
   * Option list. Mutually exclusive with passing `<option>` children —
   * prefer this prop when options come from data. When `children` is
   * provided it is rendered as-is and `options` is ignored.
   */
  options?: SelectOption[];
}

/**
 * Win95-themed select wrapper over the native `<select>`. Accepts either
 * a declarative `options` prop or raw `<option>` children for cases that
 * need groups (`<optgroup>`) or conditional rendering.
 *
 * 98.css styles the native element directly, so this primitive only
 * exists to make call sites type-safe and consistent.
 */
export const Select = React.forwardRef<HTMLSelectElement, SelectProps>(
  function Select({ options, children, ...rest }, ref) {
    return (
      <select ref={ref} {...rest}>
        {children ??
          options?.map((opt) => (
            <option key={opt.value} value={opt.value} disabled={opt.disabled}>
              {opt.label}
            </option>
          ))}
      </select>
    );
  },
);
