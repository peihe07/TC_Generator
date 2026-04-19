'use client';

import React from 'react';

export interface InputProps
  extends React.InputHTMLAttributes<HTMLInputElement> {
  /**
   * Visual treatment. `sunken` applies the Win95 inset border used in
   * textareas and filter boxes; `flat` keeps the 98.css default (used
   * inside table cells where a full 3D border would be visually noisy).
   */
  inputStyle?: 'sunken' | 'flat';
}

/**
 * Win95-themed text input. Sensible default is `type="text"` + sunken
 * 3D border (matches the rest of the app's input surfaces).
 *
 * Prefer `<Input>` over raw `<input>` for anything user-facing so that
 * styling / a11y changes can land in one place.
 */
export const Input = React.forwardRef<HTMLInputElement, InputProps>(
  function Input(
    { type = 'text', inputStyle = 'sunken', className, ...rest },
    ref,
  ) {
    const sunken = inputStyle === 'sunken' ? 'border-2 border-sunken' : '';
    const merged = [sunken, className].filter(Boolean).join(' ');
    return (
      <input
        ref={ref}
        type={type}
        className={merged || undefined}
        {...rest}
      />
    );
  },
);
