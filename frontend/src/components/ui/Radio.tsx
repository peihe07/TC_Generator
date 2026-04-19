'use client';

import React from 'react';

export interface RadioProps
  extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type'> {
  /** Visible label rendered to the right of the native radio. */
  label: React.ReactNode;
  /**
   * Radio group name. Multiple `<Radio>` with the same `name` form a
   * single exclusive group (inherited native behaviour).
   */
  name: string;
  /** Optional wrapper className; defaults to `"field-row"`. */
  wrapperClassName?: string;
}

/**
 * Win95-themed radio bundled with its `<label>`. Use inside a `<fieldset>`
 * or `role="radiogroup"` container, with every option sharing the same
 * `name` prop.
 *
 * Controlled via `checked` / `onChange`, or uncontrolled via `defaultChecked`.
 */
export const Radio = React.forwardRef<HTMLInputElement, RadioProps>(
  function Radio(
    { label, id, name, wrapperClassName = 'field-row', className, ...rest },
    ref,
  ) {
    const reactId = React.useId();
    const inputId = id ?? `radio-${reactId}`;

    return (
      <div className={wrapperClassName}>
        <input
          ref={ref}
          type="radio"
          id={inputId}
          name={name}
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
