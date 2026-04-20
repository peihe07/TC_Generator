'use client';

import React from 'react';
import { RiRobot2Line, RiRobot2Fill, RiAlertFill } from '@remixicon/react';
import { useAgentStore } from '../../../store/useAgentStore';
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

  // When `pendingConfirm` is set (e.g. restored from a persisted session
  // history with a still-unresolved confirm) treat the button as
  // waiting_confirm even if streamState has already moved on. Uses the
  // same class name as StreamState's own waiting_confirm, so the CSS
  // rule in win95.css fires either way.
  const state = pendingConfirm ? 'waiting_confirm' : streamState;
  const isWaitingConfirm = state === 'waiting_confirm';

  return (
    <Button
      className={`agent-taskbar-btn agent-taskbar-btn--${state}`}
      onClick={handleClick}
      title={
        isWaitingConfirm
          ? 'Agent Co-pilot — confirmation needed'
          : 'Agent Co-pilot'
      }
    >
      {isWaitingConfirm ? (
        // Phase 4 follow-up: visual reinforcement for waiting_confirm.
        // Pulse cadence is 1s (canonical) same as streaming, so the
        // state is distinguished by the chunky alert glyph + amber bg.
        <RiAlertFill size={16} />
      ) : state === 'idle' || state === 'error' ? (
        <RiRobot2Line size={16} />
      ) : (
        <RiRobot2Fill size={16} />
      )}
      <span>Agent</span>
    </Button>
  );
}
