import { proxyJsonBodyRoute } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  return proxyJsonBodyRoute(request, "/api/export", (data) => {
    if (
      typeof data === "object" &&
      data !== null &&
      "jobId" in data &&
      typeof data.jobId === "string"
    ) {
      return {
        ...data,
        downloadUrl: `/api/export/download/${encodeURIComponent(data.jobId)}`,
      };
    }
    return data;
  });
}
