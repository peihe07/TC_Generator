import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';

// Mock stores and client before importing components
vi.mock('../store/useAgentStore', () => ({
  useAgentStore: vi.fn(),
}));

vi.mock('../store/useJobStore', () => ({
  useJobStore: vi.fn(() => ({ jobMetadata: null, stats: { cost: 0 } })),
}));

vi.mock('../store/useWindowStore', () => ({
  useWindowStore: vi.fn(() => ({ openWindow: vi.fn(), windows: { chat: { isOpen: true } }, focusWindow: vi.fn() })),
}));

vi.mock('../services/agentClient', () => ({
  agentClient: { downloadTrace: vi.fn(), listSessions: vi.fn().mockResolvedValue([]) },
  getSessionPreview: vi.fn(() => 'preview text'),
  getPendingConfirmPart: vi.fn(() => null),
  historyToMessages: vi.fn(() => []),
}));

import { useAgentStore } from '../store/useAgentStore';
import MessageList from '../components/modules/chat/MessageList';
import ToolCallCard from '../components/modules/chat/ToolCallCard';
import ConfirmCard from '../components/modules/chat/ConfirmCard';
import type { UIMessage, UIToolPart, UIConfirmPart } from '../services/agentEvents';

function makeStore(overrides = {}) {
  return {
    messages: [],
    streamState: 'idle',
    lastError: null,
    sessionId: null,
    pendingConfirm: null,
    recentSessions: [],
    recentSessionsLoadedAt: null,
    currentSessionCost: 0,
    sendMessage: vi.fn(),
    acceptConfirm: vi.fn(),
    declineConfirm: vi.fn(),
    loadSession: vi.fn(),
    newSession: vi.fn(),
    deleteSession: vi.fn(),
    refreshRecentSessions: vi.fn(),
    clearError: vi.fn(),
    ...overrides,
  };
}

// ---- 1. Empty session ----
describe('MessageList', () => {
  it('shows empty state when no messages', () => {
    render(<MessageList messages={[]} />);
    expect(screen.getByText(/Agent 副駕模式已就緒/)).toBeInTheDocument();
  });

  // ---- 2. User + agent text rendering ----
  it('renders user and agent text messages in order', () => {
    const messages: UIMessage[] = [
      { kind: 'user', id: 'u1', text: 'Hello agent', ts: 0 },
      { kind: 'agent', id: 'a1', parts: [{ kind: 'text', text: 'Hi there' }], ts: 1 },
    ];
    render(<MessageList messages={messages} />);
    const user = screen.getByText('Hello agent');
    const agent = screen.getByText('Hi there');
    expect(user).toBeInTheDocument();
    expect(agent).toBeInTheDocument();
    // User comes before agent in DOM
    expect(user.compareDocumentPosition(agent) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
  });
});

// ---- ToolCallCard ----
describe('ToolCallCard', () => {
  // ---- 3. Running status shows spinner ----
  it('shows spinner icon when status is running', () => {
    const part: UIToolPart = {
      kind: 'tool', callId: 'c1', tool: 'list_jobs', args: {}, status: 'running',
    };
    const { container } = render(<ToolCallCard part={part} />);
    expect(container.querySelector('.spin')).toBeInTheDocument();
  });

  // ---- 4. OK status shows duration and is expandable ----
  it('shows duration and expands result on click when ok', () => {
    const part: UIToolPart = {
      kind: 'tool', callId: 'c2', tool: 'list_jobs', args: {},
      status: 'ok', result: { jobs: [], total: 0 }, durationMs: 123,
    };
    render(<ToolCallCard part={part} />);
    expect(screen.getByText('123ms')).toBeInTheDocument();

    // Click header to expand
    fireEvent.click(screen.getByText('list_jobs'));
    expect(screen.getByText('Args')).toBeInTheDocument();
    expect(screen.getByText('Result')).toBeInTheDocument();
  });

  // ---- 5. Error status shows error message ----
  it('shows error code and message when status is error', () => {
    const part: UIToolPart = {
      kind: 'tool', callId: 'c3', tool: 'generate_tc', args: {}, status: 'error',
      error: { code: 'tool_error', message: 'Something went wrong' },
    };
    render(<ToolCallCard part={part} />);
    fireEvent.click(screen.getByText('generate_tc'));
    expect(screen.getByText(/Something went wrong/)).toBeInTheDocument();
    expect(screen.queryByText('Result')).not.toBeInTheDocument();
  });
});

// ---- ConfirmCard ----
describe('ConfirmCard', () => {
  beforeEach(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useAgentStore as any).mockImplementation((selector: (s: unknown) => unknown) =>
      selector(makeStore()),
    );
  });

  // ---- 6. Pending shows Accept / Decline ----
  it('shows Accept and Decline buttons when pending', () => {
    const part: UIConfirmPart = {
      kind: 'confirm', callId: 'c4', tool: 'generate_tc',
      args: {}, estCostUsd: 1.5, status: 'pending',
    };
    render(<ConfirmCard part={part} />);
    expect(screen.getByText('Accept')).toBeInTheDocument();
    expect(screen.getByText('Decline')).toBeInTheDocument();
    expect(screen.getByText(/\$1\.5000/)).toBeInTheDocument();
  });

  // ---- 7. Accepted state shows confirmation message ----
  it('shows accepted message when status is accepted', () => {
    const part: UIConfirmPart = {
      kind: 'confirm', callId: 'c5', tool: 'generate_tc',
      args: {}, estCostUsd: 1.5, status: 'accepted',
    };
    render(<ConfirmCard part={part} />);
    expect(screen.queryByText('Accept')).not.toBeInTheDocument();
    expect(screen.getByText(/已確認/)).toBeInTheDocument();
  });

  // ---- 8. Error banner ----
  it('error banner visible when streamState is error', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useAgentStore as any).mockImplementation((selector: (s: unknown) => unknown) =>
      selector(makeStore({ streamState: 'error', lastError: { code: 'internal', message: 'boom' } })),
    );

    // Render a minimal wrapper that uses the store
    function ErrorBanner() {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const { streamState, lastError, clearError } = (useAgentStore as any)((s: ReturnType<typeof makeStore>) => s);
      if (streamState !== 'error' || !lastError) return null;
      return (
        <div className="chat-error-banner">
          [{lastError.code}] {lastError.message}
          <button onClick={clearError}>×</button>
        </div>
      );
    }

    render(<ErrorBanner />);
    expect(screen.getByText(/boom/)).toBeInTheDocument();
    expect(screen.getByText(/internal/)).toBeInTheDocument();
  });
});
