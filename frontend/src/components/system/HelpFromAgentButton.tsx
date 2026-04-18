'use client';

import React from 'react';
import { RiQuestionAnswerLine } from '@remixicon/react';
import { useAgentStore } from '../../store/useAgentStore';
import { useWindowStore } from '../../store/useWindowStore';

interface Props {
  contextPrompt: string;
  title?: string;
}

export default function HelpFromAgentButton({ contextPrompt, title }: Props) {
  const openWindow = useWindowStore((s) => s.openWindow);
  const focusWindow = useWindowStore((s) => s.focusWindow);
  const chatOpen = useWindowStore((s) => s.windows.chat?.isOpen ?? false);
  const streamState = useAgentStore((s) => s.streamState);

  const handleClick = () => {
    window.dispatchEvent(new CustomEvent('agent-prefill', { detail: contextPrompt }));

    if (!chatOpen) {
      openWindow('chat', 'Agent Co-pilot');
    } else {
      focusWindow('chat');
    }
  };

  const disabled = streamState === 'sending' || streamState === 'streaming';

  return (
    <button
      className="btn-help-agent"
      onClick={handleClick}
      disabled={disabled}
      title={disabled ? 'Agent 正在處理中…' : (title ?? '求助 AI')}
    >
      <RiQuestionAnswerLine size={14} />
    </button>
  );
}
