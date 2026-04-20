import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, within } from '@testing-library/react';
import React from 'react';

import { ReviewRow, type EditValues, type ReviewRowProps } from '../components/modules/review/ReviewRow';
import { TcRow } from '../lib/types';

/**
 * ReviewRow is pure props-driven — no store, no API. These tests cover:
 *   - accept / reject / delete callbacks
 *   - flag toggle callback with correct argument
 *   - entering edit mode → changing textarea → save
 *   - pendingRegenerated renders <RegenDiff/> and hides row-level actions
 *
 * The component returns a React fragment of <tr> elements, so we mount it
 * inside a minimal <table><tbody/></table> host to keep the DOM valid.
 */

const baseRow: TcRow = {
  id: 'TC-001',
  reqId: 'REQ-1',
  testGroup: 'G1',
  testSet: 'Set A',
  testItem: 'Original requirement text',
  preConditions: 'pre',
  inputTestData: 'input',
  steps: 'step 1',
  expectedResults: 'expected',
  status: 'reviewing',
};

const blankEditValues: EditValues = {
  steps: '',
  expected: '',
  preConditions: '',
  inputTestData: '',
};

/** Build a fresh set of mock callbacks + a partial override for the row. */
function renderRow(overrides: Partial<ReviewRowProps> = {}, row: Partial<TcRow> = {}) {
  const handlers = {
    onToggleExpand: vi.fn(),
    onToggleSelect: vi.fn(),
    onSetActive: vi.fn(),
    onStatusChange: vi.fn(),
    onDelete: vi.fn(),
    onStartEdit: vi.fn(),
    onEditValuesChange: vi.fn(),
    onSaveEdit: vi.fn(),
    onCancelEdit: vi.fn(),
    onToggleFlag: vi.fn(),
    onApplyRegen: vi.fn(),
    onDiscardRegen: vi.fn(),
  };

  const props: ReviewRowProps = {
    row: { ...baseRow, ...row },
    isExpanded: false,
    isSelected: false,
    isActive: false,
    isEditing: false,
    editValues: blankEditValues,
    ...handlers,
    ...overrides,
  };

  const utils = render(
    <table>
      <tbody>
        <ReviewRow {...props} />
      </tbody>
    </table>,
  );

  return { ...utils, handlers, props };
}

describe('ReviewRow — collapsed state', () => {
  beforeEach(() => {
    vi.restoreAllMocks();
  });

  it('renders TC id and Req id', () => {
    renderRow();
    expect(screen.getByText('TC-001')).toBeInTheDocument();
    expect(screen.getByText('REQ-1')).toBeInTheDocument();
  });

  it('shows awaiting review label for pending rows', () => {
    renderRow({}, { status: 'pending' });
    expect(screen.getByText('awaiting review')).toBeInTheDocument();
  });

  it('shows failure reason for failed rows', () => {
    renderRow({}, {
      status: 'fail',
      validationErrors: [{ severity: 'warning', message: 'Budget exceeded for this row.' }],
    });
    expect(screen.getByText('failed')).toBeInTheDocument();
    expect(screen.getByText('Budget exceeded for this row.')).toBeInTheDocument();
  });

  it('fires onStatusChange("accepted") when Accept icon button clicked', () => {
    const { handlers } = renderRow();
    fireEvent.click(screen.getByRole('button', { name: 'Accept' }));
    expect(handlers.onStatusChange).toHaveBeenCalledWith('TC-001', 'accepted');
  });

  it('fires onStatusChange("rejected") when Reject icon button clicked', () => {
    const { handlers } = renderRow();
    fireEvent.click(screen.getByRole('button', { name: 'Reject' }));
    expect(handlers.onStatusChange).toHaveBeenCalledWith('TC-001', 'rejected');
  });

  it('fires onDelete when Delete icon button clicked', () => {
    const { handlers } = renderRow();
    fireEvent.click(screen.getByRole('button', { name: 'Delete' }));
    expect(handlers.onDelete).toHaveBeenCalledWith('TC-001');
  });

  it('fires onToggleSelect when checkbox cell clicked', () => {
    const { handlers, container } = renderRow();
    const checkbox = container.querySelector('input[type="checkbox"]');
    expect(checkbox).not.toBeNull();
    // td wraps the checkbox and handles the click with stopPropagation
    fireEvent.click(checkbox!.closest('td')!);
    expect(handlers.onToggleSelect).toHaveBeenCalledWith('TC-001');
  });

  it('does not render the expanded detail panel', () => {
    renderRow();
    expect(screen.queryByText('Original Requirement')).not.toBeInTheDocument();
  });
});

describe('ReviewRow — expanded read mode', () => {
  it('shows Original Requirement + Generated Test Case panels', () => {
    renderRow({ isExpanded: true });
    expect(screen.getByText('Original Requirement')).toBeInTheDocument();
    expect(screen.getByText('Generated Test Case')).toBeInTheDocument();
    expect(screen.getByText('Original requirement text')).toBeInTheDocument();
  });

  it('shows Manual Edit + Flag buttons when not editing', () => {
    renderRow({ isExpanded: true });
    expect(screen.getByRole('button', { name: /manual edit/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /flag for human/i })).toBeInTheDocument();
  });

  it('calls onStartEdit with the row when Manual Edit clicked', () => {
    const { handlers, props } = renderRow({ isExpanded: true });
    fireEvent.click(screen.getByRole('button', { name: /manual edit/i }));
    expect(handlers.onStartEdit).toHaveBeenCalledWith(props.row);
  });

  it('calls onToggleFlag with current status when Flag clicked', () => {
    const { handlers } = renderRow({ isExpanded: true });
    fireEvent.click(screen.getByRole('button', { name: /flag for human/i }));
    expect(handlers.onToggleFlag).toHaveBeenCalledWith('TC-001', 'reviewing');
  });

  it('renders Unflag button when status is already flagged', () => {
    renderRow({ isExpanded: true }, { status: 'flagged' });
    expect(screen.getByRole('button', { name: /unflag/i })).toBeInTheDocument();
  });
});

describe('ReviewRow — edit mode flow', () => {
  it('shows Save + Cancel buttons and 4 textareas in edit mode', () => {
    renderRow({
      isExpanded: true,
      isEditing: true,
      editValues: {
        steps: 'step body',
        expected: 'expected body',
        preConditions: 'pre body',
        inputTestData: 'data body',
      },
    });

    expect(screen.getByRole('button', { name: /save changes/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /cancel/i })).toBeInTheDocument();
    // 4 StackedEditField textareas
    expect(screen.getAllByRole('textbox')).toHaveLength(4);
  });

  it('calls onEditValuesChange with merged object when a textarea changes', () => {
    const initial: EditValues = {
      steps: 'original step',
      expected: 'original expected',
      preConditions: 'original pre',
      inputTestData: 'original data',
    };
    const { handlers } = renderRow({
      isExpanded: true,
      isEditing: true,
      editValues: initial,
    });

    // Find the Test Procedure textarea by looking up its label node's sibling.
    const label = screen.getByText('Test Procedure', { selector: 'div' });
    const wrapper = label.parentElement!;
    const textarea = within(wrapper).getByRole('textbox') as HTMLTextAreaElement;

    fireEvent.change(textarea, { target: { value: 'new step body' } });

    expect(handlers.onEditValuesChange).toHaveBeenCalledTimes(1);
    expect(handlers.onEditValuesChange).toHaveBeenCalledWith({
      ...initial,
      steps: 'new step body',
    });
  });

  it('calls onSaveEdit(id) when Save Changes clicked', () => {
    const { handlers } = renderRow({ isExpanded: true, isEditing: true });
    fireEvent.click(screen.getByRole('button', { name: /save changes/i }));
    expect(handlers.onSaveEdit).toHaveBeenCalledWith('TC-001');
  });

  it('calls onCancelEdit when Cancel clicked', () => {
    const { handlers } = renderRow({ isExpanded: true, isEditing: true });
    fireEvent.click(screen.getByRole('button', { name: /cancel/i }));
    expect(handlers.onCancelEdit).toHaveBeenCalledTimes(1);
  });
});

describe('ReviewRow — pendingRegenerated state', () => {
  const rowWithPending: Partial<TcRow> = {
    pendingRegenerated: {
      steps: 'new step',
      expectedResults: 'new expected',
      preConditions: 'new pre',
      inputTestData: 'new data',
    },
  };

  it('renders the RegenDiff panel instead of Original/Generated grid', () => {
    renderRow({ isExpanded: true }, rowWithPending);
    expect(screen.getByText(/new version ready/i)).toBeInTheDocument();
    expect(screen.queryByText('Original Requirement')).not.toBeInTheDocument();
  });

  it('hides Manual Edit and Flag buttons while awaiting apply', () => {
    renderRow({ isExpanded: true }, rowWithPending);
    expect(screen.queryByRole('button', { name: /manual edit/i })).not.toBeInTheDocument();
    expect(screen.queryByRole('button', { name: /flag for human/i })).not.toBeInTheDocument();
  });

  it('calls onDiscardRegen(id) when Discard clicked', () => {
    const { handlers } = renderRow({ isExpanded: true }, rowWithPending);
    fireEvent.click(screen.getByRole('button', { name: /discard/i }));
    expect(handlers.onDiscardRegen).toHaveBeenCalledWith('TC-001');
  });

  it('calls onApplyRegen(id, fields) when Apply Selected clicked', () => {
    const { handlers } = renderRow({ isExpanded: true }, rowWithPending);
    fireEvent.click(screen.getByRole('button', { name: /apply selected/i }));
    expect(handlers.onApplyRegen).toHaveBeenCalledTimes(1);
    const [idArg, fieldsArg] = handlers.onApplyRegen.mock.calls[0];
    expect(idArg).toBe('TC-001');
    // By default all 4 fields are pre-selected.
    expect(new Set(fieldsArg)).toEqual(
      new Set(['preConditions', 'inputTestData', 'steps', 'expectedResults']),
    );
  });
});
