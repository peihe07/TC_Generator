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
    className="modern-workflow-bottom-bar modern-configure-bottom-bar flex justify-between items-center pt-2 mt-1"
  >
    <Button className="flex items-center gap-1" onClick={onBack}>
      <RiArrowLeftLine className="size-4" /> Back
    </Button>
    <div className="modern-configure-estimates">
      <span>Calls <strong>{estimatedCalls}</strong></span>
      <span>Cost <strong>${estimatedBudget.toFixed(2)}</strong></span>
      <span>Validation <strong>{strictValidation ? 'strict' : 'warn only'}</strong></span>
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
