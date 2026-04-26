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
  regenerateReason: string;
  onRegenerateReasonChange: (value: string) => void;
}

/**
 * Floating bulk-action toolbox at the bottom of the Review module.
 * Renders only when at least one row is selected.
 */
export const ReviewToolbox: React.FC<ReviewToolboxProps> = ({
  selectedCount,
  isRegenerating,
  onClear,
  onBulkStatus,
  onBulkDelete,
  onRegenerate,
  onRerun,
  regenerateReason,
  onRegenerateReasonChange,
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
      <input
        className="border-2 border-sunken"
        style={{ width: 220, fontSize: 11, padding: '2px 4px' }}
        value={regenerateReason}
        onChange={(event) => onRegenerateReasonChange(event.target.value)}
        placeholder="Reason for regenerate"
        title="Reason sent to AI for regenerate"
        disabled={isRegenerating}
      />
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
        title="Re-generate TC text only (keep existing split)"
      >
        <RiRefreshLine className={`size-3 ${isRegenerating ? 'animate-spin' : ''}`} />
        {isRegenerating ? 'Regenerating...' : 'Regenerate'}
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
