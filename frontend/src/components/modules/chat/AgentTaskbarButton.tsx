'use client';

import React from 'react';
import { RiRobot2Line, RiRobot2Fill } from '@remixicon/react';
import { useAgentStore, StreamState } from '../../../store/useAgentStore';
import { useWindowStore } from '../../../store/useWindowStore';
import { Button } from '../../ui';

export default function AgentTaskbarButton() {
  const streamState = useAgentStore((s) => s.streamState);
  const pendingConfirm = useAgentStore((s) => s.pendingConfirm);
  const { windows, openWindow, focusWindow } = useWindowStore();
  const chatWindow = windows['chat'];

  const handleClick = () => {
    if (!chatWindow.isOpen) {
      openWindow('chat', 'Agent Co-pilot');
    } else {
      focusWindow('chat');
    }
  };

  const state = pendingConfirm ? 'need_confirm' : streamState;

  return (
    <Button
      className={`agent-taskbar-btn agent-taskbar-btn--${state}`}
      onClick={handleClick}
      title="Agent Co-pilot"
    >
      {state === 'idle' || state === 'error' ? (
        <RiRobot2Line size={16} />
      ) : (
        <RiRobot2Fill size={16} />
      )}
      <span>Agent</span>
    </Button>
  );
}
