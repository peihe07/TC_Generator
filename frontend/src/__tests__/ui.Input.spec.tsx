import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

import { Input } from '../components/ui';

describe('Input', () => {
  it('defaults to type="text" with the sunken border class', () => {
    render(<Input aria-label="q" />);
    const el = screen.getByRole('textbox', { name: 'q' }) as HTMLInputElement;
    expect(el.type).toBe('text');
    expect(el).toHaveClass('border-2');
    expect(el).toHaveClass('border-sunken');
  });

  it('omits sunken border when inputStyle="flat"', () => {
    render(<Input aria-label="q" inputStyle="flat" />);
    const el = screen.getByRole('textbox', { name: 'q' });
    expect(el).not.toHaveClass('border-sunken');
  });

  it('forwards custom className alongside sunken class', () => {
    render(<Input aria-label="q" className="w-full" />);
    const el = screen.getByRole('textbox', { name: 'q' });
    expect(el).toHaveClass('border-sunken');
    expect(el).toHaveClass('w-full');
  });

  it('respects type override (e.g. number)', () => {
    render(<Input aria-label="n" type="number" defaultValue={5} />);
    const el = screen.getByRole('spinbutton', { name: 'n' }) as HTMLInputElement;
    expect(el.type).toBe('number');
  });

  it('fires onChange when the user types', () => {
    const handle = vi.fn();
    render(<Input aria-label="q" onChange={handle} />);
    fireEvent.change(screen.getByRole('textbox', { name: 'q' }), {
      target: { value: 'hello' },
    });
    expect(handle).toHaveBeenCalledTimes(1);
  });

  it('forwards ref to the underlying input element', () => {
    const ref = React.createRef<HTMLInputElement>();
    render(<Input ref={ref} aria-label="q" />);
    expect(ref.current).toBeInstanceOf(HTMLInputElement);
  });
});
