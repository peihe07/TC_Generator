'use client';

import React from 'react';

export interface CheckboxProps
  extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type'> {
  /**
   * Visible label rendered to the right of the native checkbox. Required
   * for a11y — when you really need a bare checkbox (e.g. table row
   * selection), pass `label={null}` and use `aria-label` instead.
   */
  label: React.ReactNode;
  /**
   * Optional wrapper className — applied to the outer `<label>` so it
   * still participates in `.field-row` / `.flex gap-*` layouts.
   * Defaults to `"field-row"` which matches 98.css conventions.
   */
  wrapperClassName?: string;
}

/**
 * Win95-themed checkbox bundled with its `<label>`. Renders the standard
 * `.field-row` layout so callers drop-in without rewriting wrappers.
 *
 * The component is stateless — controlled via `checked` / `onChange`, or
 * uncontrolled via `defaultChecked`, exactly like the native element.
 */
export const Checkbox = React.forwardRef<HTMLInputElement, CheckboxProps>(
  function Checkbox(
    { label, id, wrapperClassName = 'field-row', className, ...rest },
    ref,
  ) {
    // Generate a stable id when the caller didn't pass one so `<label htmlFor>`
    // still pairs with the right input (required for native checkbox behaviour).
    const reactId = React.useId();
    const inputId = id ?? `cb-${reactId}`;

    return (
      <div className={wrapperClassName}>
        <input
          ref={ref}
          type="checkbox"
          id={inputId}
          className={className}
          {...rest}
        />
        {label !== null && label !== undefined && (
          <label htmlFor={inputId}>{label}</label>
        )}
      </div>
    );
  },
);
