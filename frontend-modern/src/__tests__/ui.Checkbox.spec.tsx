import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

import { Checkbox } from '../components/ui';

describe('Checkbox', () => {
  it('renders a label bound to the underlying checkbox', () => {
    render(<Checkbox id="agree" label="I agree" defaultChecked />);
    const cb = screen.getByRole('checkbox', { name: 'I agree' }) as HTMLInputElement;
    expect(cb).toBeChecked();
    expect(cb).toHaveAttribute('id', 'agree');
  });

  it('pairs auto-generated id with label when no id prop is passed', () => {
    render(<Checkbox label="Strict mode" />);
    const cb = screen.getByRole('checkbox', { name: 'Strict mode' });
    expect(cb).toBeInTheDocument();
    // Clicking the label should toggle the checkbox via htmlFor wiring.
    fireEvent.click(screen.getByText('Strict mode'));
    expect(cb).toBeChecked();
  });

  it('fires onChange when toggled', () => {
    const handleChange = vi.fn();
    render(<Checkbox label="Opt in" onChange={handleChange} />);
    fireEvent.click(screen.getByRole('checkbox', { name: 'Opt in' }));
    expect(handleChange).toHaveBeenCalledTimes(1);
  });

  it('propagates disabled to the underlying input', () => {
    render(<Checkbox label="Opt in" disabled />);
    expect(screen.getByRole('checkbox', { name: 'Opt in' })).toBeDisabled();
  });

  it('forwards ref to the underlying input element', () => {
    const ref = React.createRef<HTMLInputElement>();
    render(<Checkbox label="R" ref={ref} />);
    expect(ref.current).toBeInstanceOf(HTMLInputElement);
    expect(ref.current?.type).toBe('checkbox');
  });

  it('uses custom wrapperClassName when supplied', () => {
    const { container } = render(
      <Checkbox label="X" wrapperClassName="custom-row" />,
    );
    expect(container.querySelector('.custom-row')).not.toBeNull();
  });
});
