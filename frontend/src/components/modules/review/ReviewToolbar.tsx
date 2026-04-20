import React from 'react';
import HelpFromAgentButton from '../../system/HelpFromAgentButton';
import { Select } from '../../ui';

const SHOW_OPTIONS = [
  { value: 'all', label: 'All TCs' },
  { value: 'flagged', label: 'Flagged Only' },
  { value: 'pending', label: 'Pending Review' },
  { value: 'regen', label: 'Awaiting Apply' },
];

export interface ReviewToolbarProps {
  filter: string;
  onFilterChange: (v: string) => void;
  testSetFilter: string;
  onTestSetFilterChange: (v: string) => void;
  testSetOptions: string[];
  totalCount: number;
  acceptedCount: number;
  expandedCount: number;
  helpContextPrompt: string;
}

/**
 * Top toolbar of the Review module: status filter + test-set filter +
 * counts summary + "Help from AI" button.
 */
export const ReviewToolbar: React.FC<ReviewToolbarProps> = ({
  filter,
  onFilterChange,
  testSetFilter,
  onTestSetFilterChange,
  testSetOptions,
  totalCount,
  acceptedCount,
  expandedCount,
  helpContextPrompt,
}) => (
  <div
    // §P10: Toolbar is "app chrome", not content — should be raised bezel
    // (matches Win95 File Explorer / app toolbar convention, and preview/
    // taskbar.html raised pattern). Was .border-sunken which is for
    // content/input surfaces; visual direction was inconsistent with role.
    className="flex justify-between items-center mb-2 p-1 bezel-raised"
    style={{ backgroundColor: 'var(--win95-gray)' }}
  >
    <div className="flex gap-2 items-center">
      <div className="field-row">
        <label htmlFor="filter" className="text-xs font-bold">
          Show:
        </label>
        <Select
          id="filter"
          value={filter}
          onChange={(e) => onFilterChange(e.target.value)}
          options={SHOW_OPTIONS}
        />
      </div>
      <div className="field-row">
        <label htmlFor="test-set-filter" className="text-xs font-bold">
          Test Set:
        </label>
        <Select
          id="test-set-filter"
          value={testSetFilter}
          onChange={(e) => onTestSetFilterChange(e.target.value)}
        >
          <option value="all">All Sets</option>
          {testSetOptions.map((testSet) => (
            <option key={testSet} value={testSet}>
              {testSet}
            </option>
          ))}
        </Select>
      </div>
      <span className="text-xs" style={{ color: 'var(--text-muted)' }}>
        Total: {totalCount} | Accepted: {acceptedCount} | Expanded: {expandedCount}
      </span>
    </div>
    <HelpFromAgentButton contextPrompt={helpContextPrompt} title="求助 AI" />
  </div>
);

export default ReviewToolbar;
