import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import React from 'react';

import { TitleBarMini } from '../components/ui';

describe('TitleBarMini', () => {
  it('renders the title inside a flex-1 span', () => {
    render(<TitleBarMini title="Original Requirement" />);
    const span = screen.getByText('Original Requirement');
    expect(span.tagName).toBe('SPAN');
    expect(span).toHaveClass('flex-1');
  });

  it('applies the default variant (no "edit" class) unless asked', () => {
    const { container } = render(<TitleBarMini title="X" />);
    const root = container.firstChild as HTMLElement;
    expect(root).toHaveClass('title-bar-mini');
    expect(root).not.toHaveClass('edit');
  });

  it('adds the edit class for variant="edit"', () => {
    const { container } = render(<TitleBarMini title="Staging" variant="edit" />);
    const root = container.firstChild as HTMLElement;
    expect(root).toHaveClass('title-bar-mini');
    expect(root).toHaveClass('edit');
  });

  it('renders leading icon and trailing children in order', () => {
    render(
      <TitleBarMini
        icon={<span data-testid="icon">★</span>}
        title="Title"
      >
        <span data-testid="trail">Extra</span>
      </TitleBarMini>,
    );
    expect(screen.getByTestId('icon')).toBeInTheDocument();
    expect(screen.getByText('Title')).toBeInTheDocument();
    expect(screen.getByTestId('trail')).toBeInTheDocument();
  });

  it('merges caller className alongside the base class', () => {
    const { container } = render(
      <TitleBarMini title="X" className="-mx-3 -mt-3 mb-3" />,
    );
    const root = container.firstChild as HTMLElement;
    expect(root).toHaveClass('title-bar-mini');
    expect(root).toHaveClass('-mx-3');
    expect(root).toHaveClass('mb-3');
  });

  it('passes through style and aria props', () => {
    const { container } = render(
      <TitleBarMini title="X" style={{ padding: 10 }} aria-label="bar" />,
    );
    const root = container.firstChild as HTMLElement;
    expect(root.style.padding).toBe('10px');
    expect(root).toHaveAttribute('aria-label', 'bar');
  });
});
