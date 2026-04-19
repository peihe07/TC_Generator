import React from 'react';
import HelpFromAgentButton from '../../system/HelpFromAgentButton';

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
  <div className="flex justify-between items-center mb-2 bg-gray-200 p-1 border border-sunken">
    <div className="flex gap-2 items-center">
      <div className="field-row">
        <label htmlFor="filter" className="text-xs font-bold">
          Show:
        </label>
        <select id="filter" value={filter} onChange={(e) => onFilterChange(e.target.value)}>
          <option value="all">All TCs</option>
          <option value="flagged">Flagged Only</option>
          <option value="pending">Pending Review</option>
          <option value="regen">Awaiting Apply</option>
        </select>
      </div>
      <div className="field-row">
        <label htmlFor="test-set-filter" className="text-xs font-bold">
          Test Set:
        </label>
        <select
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
        </select>
      </div>
      <span className="text-xs text-gray-600 ">
        Total: {totalCount} | Accepted: {acceptedCount} | Expanded: {expandedCount}
      </span>
    </div>
    <HelpFromAgentButton contextPrompt={helpContextPrompt} title="求助 AI" />
  </div>
);

export default ReviewToolbar;
