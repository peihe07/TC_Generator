import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

import { Select } from '../components/ui';

describe('Select', () => {
  it('renders options from the `options` prop', () => {
    render(
      <Select
        aria-label="filter"
        defaultValue="all"
        options={[
          { value: 'all', label: 'All TCs' },
          { value: 'flagged', label: 'Flagged Only' },
        ]}
      />,
    );
    const select = screen.getByRole('combobox', { name: 'filter' }) as HTMLSelectElement;
    expect(select.value).toBe('all');
    const opts = Array.from(select.options).map((o) => o.value);
    expect(opts).toEqual(['all', 'flagged']);
  });

  it('renders children verbatim when provided (options ignored)', () => {
    render(
      <Select aria-label="test-set" defaultValue="alpha" options={[{ value: 'x', label: 'X' }]}>
        <option value="alpha">Alpha</option>
        <option value="beta">Beta</option>
      </Select>,
    );
    const select = screen.getByRole('combobox', { name: 'test-set' }) as HTMLSelectElement;
    const opts = Array.from(select.options).map((o) => o.value);
    expect(opts).toEqual(['alpha', 'beta']);
  });

  it('marks disabled options as unselectable', () => {
    render(
      <Select
        aria-label="m"
        defaultValue="a"
        options={[
          { value: 'a', label: 'A' },
          { value: 'b', label: 'B', disabled: true },
        ]}
      />,
    );
    const b = screen.getByRole('option', { name: 'B' }) as HTMLOptionElement;
    expect(b.disabled).toBe(true);
  });

  it('fires onChange on selection change', () => {
    const handle = vi.fn();
    render(
      <Select
        aria-label="m"
        defaultValue="a"
        onChange={handle}
        options={[
          { value: 'a', label: 'A' },
          { value: 'b', label: 'B' },
        ]}
      />,
    );
    fireEvent.change(screen.getByRole('combobox', { name: 'm' }), {
      target: { value: 'b' },
    });
    expect(handle).toHaveBeenCalledTimes(1);
  });

  it('forwards ref to the underlying select', () => {
    const ref = React.createRef<HTMLSelectElement>();
    render(<Select ref={ref} aria-label="m" options={[{ value: 'a', label: 'A' }]} />);
    expect(ref.current).toBeInstanceOf(HTMLSelectElement);
  });
});
