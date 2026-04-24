import { describe, it, expect, vi, beforeEach } from 'vitest';
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';

const exportJobMock = vi.fn();
const appendLogMock = vi.fn();
const resetJobMock = vi.fn();
const advanceWindowMock = vi.fn();

vi.mock('../store/useJobStore', () => ({
  useJobStore: vi.fn(() => ({
    tcRows: [
      {
        id: 'TC-001',
        rowNum: 10,
        tcId: 'PROJ-GRP-001',
        reqId: 'REQ-1',
        testGroup: 'Group',
        testSet: 'Set A',
        testItem: 'Test item',
        preConditions: 'NA',
        inputTestData: 'NA',
        steps: '1. Step',
        expectedResults: '1. Result',
        status: 'accepted',
      },
    ],
    jobMetadata: { jobId: 'job-1', projectName: 'ProjectA', createdAt: '', totalRows: 1 },
    appendLog: appendLogMock,
    resetJob: resetJobMock,
    config: {
      model: 'gpt-5',
      batchSize: 5,
      budgetLimit: 10,
      creditBalance: 0,
      strictValidation: false,
      targetColumns: ['preConditions', 'inputTestData', 'steps', 'expectedResults'],
    },
  })),
}));

vi.mock('../store/useWindowStore', () => ({
  useWindowStore: vi.fn(() => ({
    advanceWindow: advanceWindowMock,
  })),
}));

vi.mock('../services/jobAdapter', () => ({
  exportJob: (...args: unknown[]) => exportJobMock(...args),
}));

vi.mock('../lib/logging', () => ({
  createJobLog: vi.fn((level: string, message: string) => ({ level, message })),
}));

vi.mock('../components/system/HelpFromAgentButton', () => ({
  default: () => null,
}));

import ExportModule from '../components/modules/export/ExportModule';

describe('ExportModule', () => {
  beforeEach(() => {
    exportJobMock.mockReset();
    appendLogMock.mockReset();
    resetJobMock.mockReset();
    advanceWindowMock.mockReset();
    exportJobMock.mockResolvedValue({
      fileName: 'ProjectA_generated.xlsx',
      downloadUrl: '/api/export/download/job-1',
      exportedRows: 1,
      simulated: false,
    });
  });

  it('uses output setting toggles when building export payload', async () => {
    render(<ExportModule />);

    fireEvent.click(screen.getByLabelText('Include Steps'));
    fireEvent.click(screen.getByLabelText('Update Framework Sheet'));
    fireEvent.click(screen.getByRole('button', { name: /Export to Excel/i }));

    await waitFor(() => expect(exportJobMock).toHaveBeenCalledTimes(1));

    expect(exportJobMock).toHaveBeenCalledWith(
      expect.objectContaining({
        includeFrameworkSheet: false,
        selectedColumns: ['TC Title', 'TC ID', 'Test Set', 'Pre-Conditions', 'Input Test Data', 'Expected Result', 'Priority', 'Design Method'],
      }),
    );
  });
});
