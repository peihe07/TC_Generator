import { proxyJsonBodyRoute } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  return proxyJsonBodyRoute(request, "/api/generate", (data) => {
    if (
      typeof data === "object" &&
      data !== null &&
      "jobId" in data &&
      typeof data.jobId === "string"
    ) {
      return {
        ...data,
        streamUrl: `/api/generate/stream?jobId=${encodeURIComponent(data.jobId)}`,
      };
    }
    return data;
  });
}
