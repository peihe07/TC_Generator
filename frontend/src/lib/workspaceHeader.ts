import { useWorkspaceStore } from "../store/useWorkspaceStore";

/** Build a `{ "X-Workspace-Id": ... }` object for fetch headers. */
export function buildWorkspaceHeader(): Record<string, string> {
  if (typeof window === "undefined") return {};
  try {
    const id = useWorkspaceStore.getState().currentId;
    return id ? { "X-Workspace-Id": id } : {};
  } catch {
    return {};
  }
}
