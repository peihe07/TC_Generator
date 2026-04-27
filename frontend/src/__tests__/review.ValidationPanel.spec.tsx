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

  it('shows structured fix proposal and applies reason via callback', async () => {
    requestReviewFixSuggestionMock.mockResolvedValue({
      problemRootCause: 'tc_title 為裸動作，違反 §6.1 sibling-distinction。',
      affectedFields: ['tc_title', 'pre_conditions'],
      proposedChange: 'tc_title 補上 with iPhone connected via USB；pre_conditions 加 BT pairing 完成。',
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

    // 三個結構化區塊都要顯示
    await waitFor(() =>
      expect(
        screen.getByText('tc_title 為裸動作，違反 §6.1 sibling-distinction。'),
      ).toBeInTheDocument(),
    );
    expect(screen.getByText('問題根源：')).toBeInTheDocument();
    expect(screen.getByText('建議改法：')).toBeInTheDocument();
    expect(
      screen.getByText(/tc_title 補上 with iPhone connected via USB/),
    ).toBeInTheDocument();
    // affected_fields 渲染為 inline code badges
    expect(screen.getByText('tc_title')).toBeInTheDocument();
    expect(screen.getByText('pre_conditions')).toBeInTheDocument();

    fireEvent.click(screen.getByText('套用為 Regenerate Reason'));
    expect(onApply).toHaveBeenCalledWith('Add precondition to tc_title trigger.');
  });

  it('lets the reviewer edit the suggested reason (Chinese or English) before applying', async () => {
    requestReviewFixSuggestionMock.mockResolvedValue({
      problemRootCause: '建議內容',
      affectedFields: [],
      proposedChange: '建議改法',
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

    const textarea = (await screen.findByPlaceholderText(
      /可改寫或自由描述問題/,
    )) as HTMLTextAreaElement;
    expect(textarea.value).toBe('Add precondition to tc_title trigger.');

    fireEvent.change(textarea, {
      target: { value: '請補上 BT off 前置條件並把它寫進 tc_title' },
    });
    fireEvent.click(screen.getByText('套用為 Regenerate Reason'));
    expect(onApply).toHaveBeenCalledWith(
      '請補上 BT off 前置條件並把它寫進 tc_title',
    );
  });

  it('disables apply when the editable reason is empty after trimming', async () => {
    requestReviewFixSuggestionMock.mockResolvedValue({
      problemRootCause: '建議內容',
      affectedFields: [],
      proposedChange: '建議改法',
      suggestedReason: 'Add precondition.',
      model: 'gpt-test',
      cost: 0,
    });

    render(
      <ValidationPanel
        selectedRow={rowWithError}
        onExport={() => {}}
        onApplySuggestedReason={() => {}}
      />,
    );
    fireEvent.click(screen.getByText('詢問 AI'));

    const textarea = (await screen.findByPlaceholderText(
      /可改寫或自由描述問題/,
    )) as HTMLTextAreaElement;
    fireEvent.change(textarea, { target: { value: '   ' } });

    const apply = screen.getByText('套用為 Regenerate Reason') as HTMLButtonElement;
    expect(apply.disabled).toBe(true);
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
      problemRootCause: '建議內容 A',
      affectedFields: [],
      proposedChange: '改法 A',
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
