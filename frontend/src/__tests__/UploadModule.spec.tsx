import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

const parseJobFilesMock = vi.fn();
const appendLogMock = vi.fn();
const setJobMetadataMock = vi.fn();
const setTcRowsMock = vi.fn();
const updateStatsMock = vi.fn();
const advanceWindowMock = vi.fn();

vi.mock('../services/jobAdapter', () => ({
  parseJobFiles: (...args: unknown[]) => parseJobFilesMock(...args),
}));

vi.mock('../store/useJobStore', () => ({
  useJobStore: vi.fn(() => ({
    setJobMetadata: setJobMetadataMock,
    setTcRows: setTcRowsMock,
    updateStats: updateStatsMock,
    appendLog: appendLogMock,
  })),
}));

vi.mock('../store/useWindowStore', () => ({
  useWindowStore: vi.fn(() => ({
    advanceWindow: advanceWindowMock,
  })),
}));

vi.mock('../lib/logging', () => ({
  createJobLog: vi.fn((level: string, message: string) => ({ level, message })),
}));

vi.mock('../components/system/HelpFromAgentButton', () => ({
  default: () => null,
}));

import UploadModule from '../components/modules/upload/UploadModule';

describe('UploadModule', () => {
  beforeEach(() => {
    parseJobFilesMock.mockReset();
    appendLogMock.mockReset();
    setJobMetadataMock.mockReset();
    setTcRowsMock.mockReset();
    updateStatsMock.mockReset();
    advanceWindowMock.mockReset();
  });

  it('shows parse errors inline when backend parsing fails', async () => {
    parseJobFilesMock.mockRejectedValue(new Error('raw_file must be .xlsx or .xlsm'));
    render(<UploadModule />);

    const input = document.querySelector('input[accept=".xlsx,.xlsm"]') as HTMLInputElement;
    fireEvent.change(input, {
      target: {
        files: [new File(['bad'], 'bad.xlsx', { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' })],
      },
    });
    fireEvent.click(screen.getByRole('button', { name: /Parse & Next/i }));

    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('raw_file must be .xlsx or .xlsm');
    });
    expect(advanceWindowMock).not.toHaveBeenCalled();
  });
});
