import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

import { Button } from '../components/ui';

describe('Button', () => {
  it('renders children and is a <button type="button"> by default', () => {
    render(<Button>Save</Button>);
    const btn = screen.getByRole('button', { name: 'Save' });
    expect(btn).toBeInTheDocument();
    // Default type should prevent accidental form submission
    expect(btn).toHaveAttribute('type', 'button');
  });

  it('applies accept variant class', () => {
    render(<Button variant="accept">Accept</Button>);
    expect(screen.getByRole('button', { name: 'Accept' })).toHaveClass(
      'btn-accept',
    );
  });

  it('applies reject variant class', () => {
    render(<Button variant="reject">Reject</Button>);
    expect(screen.getByRole('button', { name: 'Reject' })).toHaveClass(
      'btn-reject',
    );
  });

  it('forwards custom className alongside variant', () => {
    render(
      <Button variant="accept" className="flex-1">
        Go
      </Button>,
    );
    const btn = screen.getByRole('button', { name: 'Go' });
    expect(btn).toHaveClass('btn-accept');
    expect(btn).toHaveClass('flex-1');
  });

  it('fires onClick and respects disabled', () => {
    const handleClick = vi.fn();
    const { rerender } = render(<Button onClick={handleClick}>Click</Button>);
    fireEvent.click(screen.getByRole('button', { name: 'Click' }));
    expect(handleClick).toHaveBeenCalledTimes(1);

    rerender(
      <Button onClick={handleClick} disabled>
        Click
      </Button>,
    );
    fireEvent.click(screen.getByRole('button', { name: 'Click' }));
    // Still only called once — disabled button should not fire onClick.
    expect(handleClick).toHaveBeenCalledTimes(1);
    expect(screen.getByRole('button', { name: 'Click' })).toBeDisabled();
  });

  it('forwards ref to the underlying button element', () => {
    const ref = React.createRef<HTMLButtonElement>();
    render(<Button ref={ref}>Ref</Button>);
    expect(ref.current).toBeInstanceOf(HTMLButtonElement);
  });

  it('allows type override (e.g. submit)', () => {
    render(<Button type="submit">Submit</Button>);
    expect(screen.getByRole('button', { name: 'Submit' })).toHaveAttribute(
      'type',
      'submit',
    );
  });
});
