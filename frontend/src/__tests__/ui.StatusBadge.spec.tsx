import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import React from 'react';

import { StatusBadge } from '../components/ui';

describe('StatusBadge', () => {
  it('renders uppercase status as default label', () => {
    const { container } = render(<StatusBadge status="accepted" />);
    expect(container.textContent).toBe('ACCEPTED');
  });

  it('applies both base and status-specific classes', () => {
    const { container } = render(<StatusBadge status="rejected" />);
    const badge = container.firstElementChild;
    expect(badge).toHaveClass('status-badge');
    expect(badge).toHaveClass('rejected');
  });

  it('renders custom children instead of default label', () => {
    render(<StatusBadge status="flagged">已標記</StatusBadge>);
    expect(screen.getByText('已標記')).toBeInTheDocument();
  });

  it.each([
    'accepted',
    'rejected',
    'flagged',
    'pending',
    'reviewing',
    'generating',
  ] as const)('supports %s variant', (status) => {
    const { container } = render(<StatusBadge status={status} />);
    expect(container.firstElementChild).toHaveClass(status);
  });

  it('merges custom className', () => {
    const { container } = render(
      <StatusBadge status="pending" className="ml-2">
        wait
      </StatusBadge>,
    );
    const badge = container.firstElementChild;
    expect(badge).toHaveClass('status-badge');
    expect(badge).toHaveClass('pending');
    expect(badge).toHaveClass('ml-2');
  });
});
