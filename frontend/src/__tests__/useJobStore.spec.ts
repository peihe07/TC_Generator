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
});
