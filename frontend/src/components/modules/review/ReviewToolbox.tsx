import React from 'react';
import {
  RiCheckFill,
  RiCloseFill,
  RiDeleteBinLine,
  RiPlayLine,
  RiRefreshLine,
} from '@remixicon/react';
import { TcRow } from '../../../lib/types';
import { Button } from '../../ui';

export interface ReviewToolboxProps {
  selectedCount: number;
  isRegenerating: boolean;
  onClear: () => void;
  onBulkStatus: (status: TcRow['status']) => void;
  onBulkDelete: () => void;
  onRegenerate: () => void;
  onRerun: () => void;
  /**
   * True when a Regenerate Reason has been pre-filled (e.g. via the
   * ValidationPanel "套用為 Regenerate Reason" flow). Used to mark the
   * Regenerate button so the reviewer knows there's pending context.
   */
  hasPendingReason?: boolean;
}

/**
 * Floating bulk-action toolbox at the bottom of the Review module.
 * Renders only when at least one row is selected.
 *
 * Regenerate no longer carries an inline reason input — clicking the
 * button opens a Win95Dialog (owned by ReviewModule) where the reviewer
 * fills in the reason and confirms. This makes the act of regenerating
 * an explicit, gated action instead of "type and pray you remembered to
 * click the right button".
 */
export const ReviewToolbox: React.FC<ReviewToolboxProps> = ({
  selectedCount,
  isRegenerating,
  onClear,
  onBulkStatus,
  onBulkDelete,
  onRegenerate,
  onRerun,
  hasPendingReason = false,
}) => (
  <div
    className="win95-toolbox absolute bottom-4 left-1/2 z-20"
    style={{ transform: 'translateX(-50%)', padding: '6px 4px' }}
  >
    <div className="win95-toolbox-handle" />
    <div className="win95-toolbox-group">
      <span className="font-bold" style={{ fontSize: 11, padding: '0 4px' }}>
        {selectedCount} row{selectedCount > 1 ? 's' : ''} selected
      </span>
      <Button onClick={onClear}>Clear</Button>
    </div>
    <div className="win95-toolbox-group">
      <Button
        className="flex items-center gap-1"
        title="Accept selected"
        onClick={() => onBulkStatus('accepted')}
      >
        <RiCheckFill className="size-3" style={{ color: 'var(--status-accept-dark)' }} /> Accept
      </Button>
      <Button
        className="flex items-center gap-1"
        title="Reject selected"
        onClick={() => onBulkStatus('rejected')}
      >
        <RiCloseFill className="size-3" style={{ color: 'var(--status-reject-dark)' }} /> Reject
      </Button>
    </div>
    <div className="win95-toolbox-group">
      <Button
        className="flex items-center gap-1"
        title="Delete selected"
        onClick={onBulkDelete}
      >
        <RiDeleteBinLine className="size-3" /> Delete
      </Button>
      <Button
        className="flex items-center gap-1"
        onClick={onRegenerate}
        disabled={isRegenerating}
        title={
          hasPendingReason
            ? '已有 ValidationPanel 套用的 Regenerate Reason 草稿，按下會跳出對話框讓你確認 / 編輯後送出。'
            : '按下後會跳出對話框讓你填寫 Regenerate Reason 再送出。'
        }
      >
        <RiRefreshLine className={`size-3 ${isRegenerating ? 'animate-spin' : ''}`} />
        {isRegenerating
          ? 'Regenerating...'
          : `Regenerate${hasPendingReason ? ' •' : ''}…`}
      </Button>
      <Button
        className="font-bold flex items-center gap-1"
        onClick={onRerun}
        disabled={isRegenerating}
        title="Re-run full pipeline (AI re-evaluates split & decomposition)"
      >
        <RiPlayLine className={`size-3 ${isRegenerating ? 'animate-spin' : ''}`} />
        {isRegenerating ? 'Re-running...' : 'Re-run'}
      </Button>
    </div>
  </div>
);

export default ReviewToolbox;
