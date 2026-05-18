import { beforeEach, describe, expect, it } from 'vitest';

import { useJobStore } from '../store/useJobStore';
import type { TcRow } from '../lib/types';

const baseRow = (id: string): TcRow => ({
  id,
  reqId: `REQ-${id}`,
  testGroup: 'DeviceManager',
  testSet: 'Core',
  testItem: `Requirement ${id}`,
  preConditions: '',
  inputTestData: '',
  steps: '',
  expectedResults: '',
  status: 'pending',
});

const rowWithTcId = (id: string, tcId: string, testGroup = 'DeviceManager'): TcRow => ({
  ...baseRow(id),
  testGroup,
  tcId,
});

describe('useJobStore row identity', () => {
  beforeEach(() => {
    useJobStore.setState({
      jobMetadata: null,
      tcRows: [],
      logs: [],
      isProcessing: false,
      isRegenerating: false,
    });
  });

  it('keeps stable row ids when deleting split rows', () => {
    useJobStore.getState().setTcRows([
      baseRow('row-10'),
      {
        ...baseRow('row-10__tc2'),
        splitDecision: {
          reqId: 'REQ-row-10',
          tcCount: 2,
          subIndex: 1,
          parentId: 'row-10',
          reasoning: '',
          keywords: [],
        },
      },
      baseRow('row-11'),
    ]);

    useJobStore.getState().deleteTcRows(['row-11']);

    expect(useJobStore.getState().tcRows.map((row) => row.id)).toEqual([
      'row-10',
      'row-10__tc2',
    ]);
    expect(useJobStore.getState().tcRows[1].splitDecision?.parentId).toBe('row-10');
  });

  it('keeps stable row ids after applying regenerated content', () => {
    useJobStore.getState().setTcRows([
      {
        ...baseRow('row-10'),
        awaitingApply: {
          preConditions: '1. Ready',
          inputTestData: 'NA',
          steps: '1. Execute',
          expectedResults: '1. Result',
        },
      },
      baseRow('row-11'),
    ]);

    useJobStore.getState().applyRegenerated('row-10', ['steps']);

    expect(useJobStore.getState().tcRows.map((row) => row.id)).toEqual([
      'row-10',
      'row-11',
    ]);
    expect(useJobStore.getState().tcRows[0].steps).toBe('1. Execute');
  });

  it('resequences TC IDs after deleting rows so the review table stays contiguous', () => {
    useJobStore.getState().setTcRows([
      rowWithTcId('row-1', 'PRJ-DM-001'),
      rowWithTcId('row-2', 'PRJ-DM-002'),
      rowWithTcId('row-3', 'PRJ-DM-003'),
      rowWithTcId('row-4', 'PRJ-DM-004'),
    ]);

    useJobStore.getState().deleteTcRows(['row-2']);

    expect(useJobStore.getState().tcRows.map((row) => row.id)).toEqual([
      'row-1',
      'row-3',
      'row-4',
    ]);
    expect(useJobStore.getState().tcRows.map((row) => row.tcId)).toEqual([
      'PRJ-DM-001',
      'PRJ-DM-002',
      'PRJ-DM-003',
    ]);
  });

  it('resequences TC IDs independently per project and group bucket', () => {
    useJobStore.getState().setTcRows([
      rowWithTcId('dm-1', 'PRJ-DM-001', 'DeviceManager'),
      rowWithTcId('bt-1', 'PRJ-BT-001', 'Bluetooth'),
      rowWithTcId('dm-2', 'PRJ-DM-002', 'DeviceManager'),
      rowWithTcId('bt-2', 'PRJ-BT-002', 'Bluetooth'),
      rowWithTcId('dm-3', 'PRJ-DM-003', 'DeviceManager'),
    ]);

    useJobStore.getState().deleteTcRows(['dm-2', 'bt-1']);

    expect(useJobStore.getState().tcRows.map((row) => row.tcId)).toEqual([
      'PRJ-DM-001',
      'PRJ-BT-001',
      'PRJ-DM-002',
    ]);
  });

  it('clears duplicate badges when the referenced duplicate row was deleted', () => {
    useJobStore.getState().setTcRows([
      {
        ...rowWithTcId('am-1', 'PRJ-RAD-001'),
        rowNum: 10,
        splitDecision: {
          reqId: 'SWE-RA-RAD-001',
          tcCount: 2,
          subIndex: 0,
          reasoning: '',
          keywords: [],
        },
      },
      {
        ...rowWithTcId('am-2', 'PRJ-RAD-002'),
        rowNum: 11,
        splitDecision: {
          reqId: 'SWE-RA-RAD-001',
          tcCount: 2,
          subIndex: 1,
          parentId: 'am-1',
          duplicateOf: '10',
          distinguishingAxis: { axis: 'none', delta: 'same behavior' },
          reasoning: '',
          keywords: [],
        },
      },
    ]);

    useJobStore.getState().deleteTcRows(['am-1']);

    expect(useJobStore.getState().tcRows).toHaveLength(1);
    expect(useJobStore.getState().tcRows[0].splitDecision?.duplicateOf).toBeUndefined();
    expect(useJobStore.getState().tcRows[0].splitDecision?.distinguishingAxis).toBeUndefined();
  });
});
