"use client";

import { useEffect, useMemo } from "react";
import {
  filterRecordsByWorkspace,
  useJobHistoryStore,
  type JobRecord,
} from "../store/useJobHistoryStore";
import { useWorkspaceStore } from "../store/useWorkspaceStore";

/** Returns the job records visible in the current workspace. */
export function useWorkspaceFilteredRecords(): JobRecord[] {
  const records = useJobHistoryStore((s) => s.records);
  const loaded = useJobHistoryStore((s) => s.loaded);
  const loadFromStorage = useJobHistoryStore((s) => s.loadFromStorage);

  const wsId = useWorkspaceStore((s) => s.currentId);
  const wsLoaded = useWorkspaceStore((s) => s.loaded);
  const loadWs = useWorkspaceStore((s) => s.loadFromStorage);

  useEffect(() => {
    if (!loaded) loadFromStorage();
    if (!wsLoaded) loadWs();
  }, [loaded, loadFromStorage, wsLoaded, loadWs]);

  return useMemo(
    () => filterRecordsByWorkspace(records, wsId),
    [records, wsId],
  );
}
