import React from 'react';
import { RiArrowLeftLine, RiPlayFill } from '@remixicon/react';
import { Button } from '../../ui';

export interface ConfigureBottomBarProps {
  estimatedCalls: number;
  estimatedBudget: number;
  strictValidation: boolean;
  canStartGenerate: boolean;
  onBack: () => void;
  onStartGenerate: () => void;
}

/**
 * Bottom action bar pinned at the foot of the Configure module. Shows
 * derived totals (calls / cost ceiling / validation mode) and the two
 * navigation actions.
 */
export const ConfigureBottomBar: React.FC<ConfigureBottomBarProps> = ({
  estimatedCalls,
  estimatedBudget,
  strictValidation,
  canStartGenerate,
  onBack,
  onStartGenerate,
}) => (
  <div
    className="flex justify-between items-center pt-2 mt-1"
    style={{ borderTop: '1px solid var(--win95-gray-mid)' }}
  >
    <Button className="flex items-center gap-1" onClick={onBack}>
      <RiArrowLeftLine className="size-4" /> Back
    </Button>
    <div style={{ color: 'var(--text-muted)', fontSize: 11 }}>
      Est. calls: <strong>{estimatedCalls}</strong>
      {' | '}Est. cost ceiling: <strong>${estimatedBudget.toFixed(2)}</strong>
      {' | '}Validation: <strong>{strictValidation ? 'strict' : 'warn only'}</strong>
    </div>
    <Button
      className="flex items-center gap-1 default"
      onClick={onStartGenerate}
      disabled={!canStartGenerate}
    >
      Start Generate{' '}
      <RiPlayFill className="size-4" style={{ color: 'var(--status-accept-dark)' }} />
    </Button>
  </div>
);

export default ConfigureBottomBar;
