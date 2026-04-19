import React from 'react';
import {
  RiAlertFill,
  RiCheckboxCircleFill,
  RiDownload2Line,
  RiErrorWarningFill,
} from '@remixicon/react';
import { TcRow } from '../../../lib/types';
import { Button } from '../../ui';

export interface ValidationPanelProps {
  selectedRow: TcRow | null;
  onExport: () => void;
}

/**
 * Right-hand panel: shows validation results for the currently active row
 * plus the primary "Export All" call-to-action.
 */
export const ValidationPanel: React.FC<ValidationPanelProps> = ({ selectedRow, onExport }) => (
  <div className="w-64 flex flex-col gap-2">
    <fieldset className="flex-1 flex flex-col overflow-hidden">
      <legend className="font-bold text-sm">Validation Results</legend>
      <div className="flex-1 overflow-auto p-2 flex flex-col gap-2">
        {!selectedRow ? (
          <div className="sys-log-entry" style={{ color: 'var(--win95-gray-dark)' }}>
            <span className="sys-log-tag info">INFO</span>
            Expand a row to view validation.
          </div>
        ) : selectedRow.validationErrors && selectedRow.validationErrors.length > 0 ? (
          selectedRow.validationErrors.map((err, i) => (
            <div key={i} className="sys-log-entry selectable">
              <div className="flex items-start gap-2">
                {err.severity === 'error' ? (
                  <RiErrorWarningFill
                    className="size-4 shrink-0 mt-0.5"
                    style={{ color: 'var(--status-reject)' }}
                  />
                ) : (
                  <RiAlertFill
                    className="size-4 shrink-0 mt-0.5"
                    style={{ color: 'var(--status-warn)' }}
                  />
                )}
                <div className="flex-1 min-w-0">
                  <div>
                    <span
                      className={`sys-log-tag ${err.severity === 'error' ? 'critical' : 'warn'}`}
                    >
                      {err.severity === 'error' ? 'CRITICAL' : 'WARNING'}
                    </span>
                    <span className="font-bold text-[11px]">
                      {err.severity === 'error' ? 'Logic Conflict' : 'Quality Warning'}
                    </span>
                  </div>
                  <div className="text-[11px] mt-1" style={{ color: '#303030' }}>
                    {err.message}
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="sys-log-entry selectable">
            <div className="flex items-start gap-2">
              <RiCheckboxCircleFill
                className="size-4 shrink-0 mt-0.5"
                style={{ color: 'var(--status-accept)' }}
              />
              <div className="flex-1">
                <div>
                  <span className="sys-log-tag info">PASS</span>
                  <span className="font-bold text-[11px]">All Checks Passed</span>
                </div>
                <div className="text-[11px] mt-1" style={{ color: '#303030' }}>
                  This test case meets all AI quality standards.
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </fieldset>

    <Button
      className="w-full py-3 flex items-center justify-center gap-2 font-bold default"
      onClick={onExport}
    >
      <RiDownload2Line className="size-5" /> Export All
    </Button>
  </div>
);

export default ValidationPanel;
