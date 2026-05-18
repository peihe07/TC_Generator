import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, cleanup } from '@testing-library/react';
import { afterEach } from 'vitest';
import React from 'react';
import { Win95Dialog } from '../components/ui/Dialog';

afterEach(cleanup);

/**
 * Win95Dialog — unit tests covering a11y + keyboard + focus behavior.
 */

function setup(overrides: Partial<React.ComponentProps<typeof Win95Dialog>> = {}) {
  const onClose = vi.fn();
  const onOk = vi.fn();
  const onCancel = vi.fn();
  render(
    <Win95Dialog
      open
      title="Confirm Action"
      message="Continue with this action?"
      actions={[
        { label: 'OK', variant: 'default', onClick: onOk },
        { label: 'Cancel', variant: 'cancel', onClick: onCancel },
      ]}
      onClose={onClose}
      {...overrides}
    />,
  );
  return { onClose, onOk, onCancel };
}

describe('Win95Dialog', () => {
  it('renders title and message when open', () => {
    setup();
    expect(screen.getByText('Confirm Action')).toBeInTheDocument();
    expect(screen.getByText('Continue with this action?')).toBeInTheDocument();
  });

  it('does not render anything when open is false', () => {
    render(
      <Win95Dialog
        open={false}
        title="Hidden"
        message="Not shown"
        actions={[{ label: 'OK', onClick: vi.fn() }]}
        onClose={vi.fn()}
      />,
    );
    expect(screen.queryByText('Hidden')).not.toBeInTheDocument();
  });

  it('has correct a11y roles and labels', () => {
    setup();
    const dialog = screen.getByRole('alertdialog');
    expect(dialog).toHaveAttribute('aria-modal', 'true');
    expect(dialog).toHaveAttribute('aria-labelledby');
    expect(dialog).toHaveAttribute('aria-describedby');
  });

  it('calls onClose when Escape is pressed', () => {
    const { onClose } = setup();
    fireEvent.keyDown(document, { key: 'Escape' });
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('calls action.onClick when the corresponding button is clicked', () => {
    const { onOk, onCancel } = setup();
    fireEvent.click(screen.getByRole('button', { name: 'OK' }));
    expect(onOk).toHaveBeenCalledTimes(1);
    fireEvent.click(screen.getByRole('button', { name: 'Cancel' }));
    expect(onCancel).toHaveBeenCalledTimes(1);
  });

  it('applies .default class to the default action button', () => {
    setup();
    expect(screen.getByRole('button', { name: 'OK' })).toHaveClass('default');
    expect(screen.getByRole('button', { name: 'Cancel' })).not.toHaveClass('default');
  });

  it('focuses the default action on open', () => {
    setup();
    // jsdom focus is synchronous; default-ok should be the active element
    expect(document.activeElement).toBe(screen.getByRole('button', { name: 'OK' }));
  });

  it('renders the variant glyph (warning / error / info)', () => {
    cleanup();
    const { rerender } = render(
      <Win95Dialog
        open
        variant="warning"
        title="T"
        message="M"
        actions={[{ label: 'OK', onClick: vi.fn() }]}
        onClose={vi.fn()}
      />,
    );
    expect(screen.getAllByText('!').length).toBe(2); // title-bar mini + body chunky

    rerender(
      <Win95Dialog
        open
        variant="error"
        title="T"
        message="M"
        actions={[{ label: 'OK', onClick: vi.fn() }]}
        onClose={vi.fn()}
      />,
    );
    expect(screen.getAllByText('×').length).toBe(2);

    rerender(
      <Win95Dialog
        open
        variant="info"
        title="T"
        message="M"
        actions={[{ label: 'OK', onClick: vi.fn() }]}
        onClose={vi.fn()}
      />,
    );
    expect(screen.getAllByText('i').length).toBe(2);
  });

  it('title-bar Close button triggers onClose', () => {
    const { onClose } = setup();
    fireEvent.click(screen.getByRole('button', { name: 'Close' }));
    expect(onClose).toHaveBeenCalledTimes(1);
  });
});
