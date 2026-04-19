'use client';

import React from 'react';
import { RiMoneyDollarCircleLine } from '@remixicon/react';
import type { UIConfirmPart } from '../../../services/agentEvents';
import { useAgentStore } from '../../../store/useAgentStore';
import { Button } from '../../ui';

interface Props {
  part: UIConfirmPart;
}

export default function ConfirmCard({ part }: Props) {
  const acceptConfirm = useAgentStore((s) => s.acceptConfirm);
  const declineConfirm = useAgentStore((s) => s.declineConfirm);

  return (
    <div className="confirm-card" data-status={part.status}>
      <div className="confirm-card-header">
        <RiMoneyDollarCircleLine size={16} />
        <span>需要確認：{part.tool}</span>
      </div>
      <div className="confirm-card-cost">
        預估費用：<strong>${part.estCostUsd.toFixed(4)}</strong>
      </div>

      {part.status === 'pending' && (
        <div className="confirm-card-actions">
          <Button className="btn-confirm-accept" onClick={acceptConfirm}>
            Accept
          </Button>
          <Button className="btn-confirm-decline" onClick={declineConfirm}>
            Decline
          </Button>
        </div>
      )}

      {part.status === 'accepted' && (
        <div className="confirm-card-result accepted">已確認，執行中…</div>
      )}

      {part.status === 'declined' && (
        <div className="confirm-card-result declined">已取消此動作</div>
      )}
    </div>
  );
}
