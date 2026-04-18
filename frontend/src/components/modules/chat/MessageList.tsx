'use client';

import React, { useEffect, useRef } from 'react';
import type { UIMessage, UIPart } from '../../../services/agentEvents';
import ToolCallCard from './ToolCallCard';
import ConfirmCard from './ConfirmCard';

interface Props {
  messages: UIMessage[];
}

export default function MessageList({ messages }: Props) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  if (messages.length === 0) {
    return (
      <div className="chat-empty">
        <p>Agent 副駕模式已就緒。</p>
        <p>輸入指令，例如：「列出最近的 jobs」或「幫我 parse 這份檔案」</p>
      </div>
    );
  }

  return (
    <div className="message-list">
      {messages.map((msg) => (
        <div key={msg.id} className={`message-row message-row--${msg.kind}`}>
          {msg.kind === 'user' && (
            <div className="user-bubble">{msg.text}</div>
          )}
          {msg.kind === 'agent' && (
            <div className="agent-bubble">
              {msg.parts.map((part, i) => (
                <Part key={i} part={part} />
              ))}
            </div>
          )}
        </div>
      ))}
      <div ref={bottomRef} />
    </div>
  );
}

function Part({ part }: { part: UIPart }) {
  if (part.kind === 'text') {
    return <div className="agent-text" style={{ whiteSpace: 'pre-wrap' }}>{part.text}</div>;
  }
  if (part.kind === 'tool') {
    return <ToolCallCard part={part} />;
  }
  if (part.kind === 'confirm') {
    return <ConfirmCard part={part} />;
  }
  return null;
}
