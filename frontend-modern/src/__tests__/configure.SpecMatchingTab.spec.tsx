import { describe, expect, it, vi } from 'vitest';
import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';

import { SpecMatchingTab } from '../components/modules/configure/SpecMatchingTab';

describe('SpecMatchingTab', () => {
  it('fires refresh from the toolbar button', () => {
    const onRefresh = vi.fn();
    render(
      <SpecMatchingTab
        preview={null}
        isLoading={false}
        error={null}
        onRefresh={onRefresh}
      />,
    );

    fireEvent.click(screen.getByRole('button', { name: /refresh/i }));
    expect(onRefresh).toHaveBeenCalledTimes(1);
  });

  it('disables refresh while loading and shows loading state', () => {
    const onRefresh = vi.fn();
    render(
      <SpecMatchingTab
        preview={null}
        isLoading
        error={null}
        onRefresh={onRefresh}
      />,
    );

    const button = screen.getByRole('button', { name: /refresh/i });
    expect(button).toBeDisabled();
    expect(screen.getByText('Loading spec matching preview...')).toBeInTheDocument();
  });
});
