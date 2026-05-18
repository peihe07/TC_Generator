import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

import { IconButton } from '../components/ui';

describe('IconButton', () => {
  it('sets both title and aria-label from the required label prop', () => {
    render(<IconButton label="Close">✕</IconButton>);
    const btn = screen.getByRole('button', { name: 'Close' });
    expect(btn).toHaveAttribute('title', 'Close');
    expect(btn).toHaveAttribute('aria-label', 'Close');
  });

  it('always applies btn-icon base class', () => {
    render(<IconButton label="Add">+</IconButton>);
    expect(screen.getByRole('button', { name: 'Add' })).toHaveClass('btn-icon');
  });

  it('applies accept and reject variant classes on top of btn-icon', () => {
    const { rerender } = render(
      <IconButton label="Accept" variant="accept">
        ✓
      </IconButton>,
    );
    const accept = screen.getByRole('button', { name: 'Accept' });
    expect(accept).toHaveClass('btn-icon');
    expect(accept).toHaveClass('btn-accept');

    rerender(
      <IconButton label="Reject" variant="reject">
        ✕
      </IconButton>,
    );
    const reject = screen.getByRole('button', { name: 'Reject' });
    expect(reject).toHaveClass('btn-icon');
    expect(reject).toHaveClass('btn-reject');
  });

  it('fires onClick when enabled, not when disabled', () => {
    const handleClick = vi.fn();
    const { rerender } = render(
      <IconButton label="Run" onClick={handleClick}>
        ▶
      </IconButton>,
    );
    fireEvent.click(screen.getByRole('button', { name: 'Run' }));
    expect(handleClick).toHaveBeenCalledTimes(1);

    rerender(
      <IconButton label="Run" onClick={handleClick} disabled>
        ▶
      </IconButton>,
    );
    fireEvent.click(screen.getByRole('button', { name: 'Run' }));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('merges custom className without losing variant classes', () => {
    render(
      <IconButton label="X" variant="reject" className="extra">
        ✕
      </IconButton>,
    );
    const btn = screen.getByRole('button', { name: 'X' });
    expect(btn).toHaveClass('btn-icon');
    expect(btn).toHaveClass('btn-reject');
    expect(btn).toHaveClass('extra');
  });
});
