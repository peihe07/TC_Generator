import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import React from 'react';

import { ValidationPanel } from '../components/modules/review/ValidationPanel';
import { TcRow } from '../lib/types';

const requestReviewFixSuggestionMock = vi.fn();

vi.mock('../services/jobAdapter', () => ({
  requestReviewFixSuggestion: (...args: unknown[]) =>
    requestReviewFixSuggestionMock(...args),
}));

const rowWithError: TcRow = {
  id: 'r1',
  tcId: 'TC-001',
  reqId: 'REQ-1',
  testGroup: 'G1',
  testSet: 'Set A',
  testItem: 'requirement text',
  tcTitle: 'Select X',
  preConditions: '1. precondition',
  inputTestData: 'NA',
  steps: '1. step',
  expectedResults: '1. expected',
  status: 'reviewing',
  validationErrors: [
    { severity: 'error', message: 'Trigger missing precondition.', column: 'tc_title' },
  ],
};

describe('ValidationPanel — AI fix suggestion', () => {
  beforeEach(() => {
    requestReviewFixSuggestionMock.mockReset();
  });

  it('hides the AI assist block when the row has no validation errors', () => {
    render(
      <ValidationPanel
        selectedRow={{ ...rowWithError, validationErrors: [] }}
        onExport={() => {}}
      />,
    );
    expect(screen.queryByText(/AI 修法建議/)).not.toBeInTheDocument();
  });

  it('shows suggestion + reason and applies reason via callback', async () => {
    requestReviewFixSuggestionMock.mockResolvedValue({
      suggestion: 'tc_title 缺少前置條件，請補上。',
      suggestedReason: 'Add precondition to tc_title trigger.',
      model: 'gpt-test',
      cost: 0,
    });

    const onApply = vi.fn();
    render(
      <ValidationPanel
        selectedRow={rowWithError}
        onExport={() => {}}
        onApplySuggestedReason={onApply}
      />,
    );

    fireEvent.click(screen.getByText('詢問 AI'));

    expect(requestReviewFixSuggestionMock).toHaveBeenCalledWith(
      expect.objectContaining({
        tc: expect.objectContaining({ tc_id: 'TC-001', tc_title: 'Select X' }),
        errors: [
          expect.objectContaining({
            severity: 'error',
            field: 'tc_title',
            message: 'Trigger missing precondition.',
          }),
        ],
      }),
    );

    await waitFor(() =>
      expect(screen.getByText('tc_title 缺少前置條件，請補上。')).toBeInTheDocument(),
    );
    expect(
      screen.getByText('Add precondition to tc_title trigger.'),
    ).toBeInTheDocument();

    fireEvent.click(screen.getByText('套用為 Regenerate Reason'));
    expect(onApply).toHaveBeenCalledWith('Add precondition to tc_title trigger.');
  });

  it('renders the error message when the request fails', async () => {
    requestReviewFixSuggestionMock.mockRejectedValue(new Error('network down'));

    render(
      <ValidationPanel selectedRow={rowWithError} onExport={() => {}} />,
    );
    fireEvent.click(screen.getByText('詢問 AI'));

    await waitFor(() =>
      expect(screen.getByText('network down')).toBeInTheDocument(),
    );
  });

  it('resets suggestion state when the active row changes', async () => {
    requestReviewFixSuggestionMock.mockResolvedValue({
      suggestion: '建議內容 A',
      suggestedReason: 'reason A',
      model: 'gpt-test',
      cost: 0,
    });

    const { rerender } = render(
      <ValidationPanel selectedRow={rowWithError} onExport={() => {}} />,
    );
    fireEvent.click(screen.getByText('詢問 AI'));
    await waitFor(() =>
      expect(screen.getByText('建議內容 A')).toBeInTheDocument(),
    );

    rerender(
      <ValidationPanel
        selectedRow={{ ...rowWithError, id: 'r2', tcId: 'TC-002' }}
        onExport={() => {}}
      />,
    );

    expect(screen.queryByText('建議內容 A')).not.toBeInTheDocument();
  });
});
