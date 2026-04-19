import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

import { Radio } from '../components/ui';

describe('Radio', () => {
  it('renders label paired with the underlying radio input', () => {
    render(<Radio id="m-gpt5" name="model" value="gpt-5" label="GPT-5" defaultChecked />);
    const radio = screen.getByRole('radio', { name: 'GPT-5' }) as HTMLInputElement;
    expect(radio).toBeChecked();
    expect(radio).toHaveAttribute('name', 'model');
    expect(radio).toHaveAttribute('value', 'gpt-5');
  });

  it('forms an exclusive group when two radios share a name', () => {
    const onA = vi.fn();
    const onB = vi.fn();
    render(
      <>
        <Radio id="a" name="g" value="a" label="A" defaultChecked onChange={onA} />
        <Radio id="b" name="g" value="b" label="B" onChange={onB} />
      </>,
    );
    const a = screen.getByRole('radio', { name: 'A' }) as HTMLInputElement;
    const b = screen.getByRole('radio', { name: 'B' }) as HTMLInputElement;

    fireEvent.click(b);
    expect(b).toBeChecked();
    expect(a).not.toBeChecked();
    expect(onB).toHaveBeenCalledTimes(1);
  });

  it('auto-generates an id so the label toggles the input', () => {
    render(<Radio name="g" value="v" label="Pick me" />);
    fireEvent.click(screen.getByText('Pick me'));
    expect(screen.getByRole('radio', { name: 'Pick me' })).toBeChecked();
  });

  it('forwards ref to the underlying input', () => {
    const ref = React.createRef<HTMLInputElement>();
    render(<Radio name="g" value="v" label="R" ref={ref} />);
    expect(ref.current).toBeInstanceOf(HTMLInputElement);
    expect(ref.current?.type).toBe('radio');
  });
});
