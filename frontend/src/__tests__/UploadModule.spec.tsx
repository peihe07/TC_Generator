import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

const parseJobFilesMock = vi.fn();
const fetchSpecLibraryMock = vi.fn();
const appendLogMock = vi.fn();
const setJobMetadataMock = vi.fn();
const setTcRowsMock = vi.fn();
const updateStatsMock = vi.fn();
const advanceWindowMock = vi.fn();

vi.mock('../services/jobAdapter', () => ({
  fetchSpecLibrary: (...args: unknown[]) => fetchSpecLibraryMock(...args),
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
    fetchSpecLibraryMock.mockReset();
    fetchSpecLibraryMock.mockResolvedValue([]);
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

  it('shows concise spec library labels between HMI markers while preserving full values', async () => {
    fetchSpecLibraryMock.mockResolvedValue([
      {
        name: 'SYS1_HMI_Announcements_HMI_Logic_and_Flow_R1_SR24_1A(May_3_2021)',
        sourceFile: 'SYS1_HMI_Announcements_HMI_Logic_and_Flow_R1_SR24_1A(May_3_2021).xlsx',
        entriesCount: 8,
        embeddingModel: null,
        updatedAt: null,
      },
      {
        name: 'SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7',
        sourceFile: 'SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7.xlsx',
        entriesCount: 1044,
        embeddingModel: null,
        updatedAt: null,
      },
      {
        name: 'SYS1_HMI_Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023)',
        sourceFile: 'SYS1_HMI_Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023).xlsx',
        entriesCount: 78,
        embeddingModel: null,
        updatedAt: null,
      },
      {
        name: 'SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)',
        sourceFile: 'SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021).xlsx',
        entriesCount: 64,
        embeddingModel: null,
        updatedAt: null,
      },
    ]);

    render(<UploadModule />);

    const announcementsOption = await screen.findByRole('option', {
      name: 'Announcements (8)',
    });
    const cameraOption = await screen.findByRole('option', {
      name: 'HeadUnitCameraSystems (1044)',
    });
    const deviceManagerOption = await screen.findByRole('option', {
      name: 'Device Manager (78)',
    });
    const rvcOption = await screen.findByRole('option', {
      name: 'RVC+PAM (64)',
    });

    expect(announcementsOption).toHaveValue(
      'SYS1_HMI_Announcements_HMI_Logic_and_Flow_R1_SR24_1A(May_3_2021)',
    );
    expect(cameraOption).toHaveValue(
      'SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7',
    );
    expect(deviceManagerOption).toHaveValue(
      'SYS1_HMI_Device_Manager_HMI Logic_and_Flow_R1_SR24_Post_2A_(March_13_2023)',
    );
    expect(rvcOption).toHaveValue(
      'SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)',
    );
  });
});
