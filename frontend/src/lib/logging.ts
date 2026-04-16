import type { JobLog } from "@/src/lib/types";

export function createJobLog(
  level: JobLog["level"],
  message: string,
): JobLog {
  return {
    timestamp: new Date().toLocaleTimeString(),
    level,
    message,
  };
}
