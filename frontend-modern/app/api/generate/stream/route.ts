import { proxyErrorResponse, proxyStream } from "../../_lib/backend";

export const runtime = "nodejs";

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const jobId = searchParams.get("jobId");
    if (!jobId) {
      return Response.json({ detail: "jobId is required." }, { status: 400 });
    }

    return await proxyStream(
      `/api/generate/stream?jobId=${encodeURIComponent(jobId)}`,
      {
        method: "GET",
        headers: {
          Accept: "text/event-stream",
        },
      },
    );
  } catch (error) {
    return proxyErrorResponse(error);
  }
}
