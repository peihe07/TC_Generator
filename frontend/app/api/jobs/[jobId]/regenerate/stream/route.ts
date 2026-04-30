import { proxyStream ,  workspaceHeaderFrom } from "../../../../_lib/backend";

export const runtime = "nodejs";

export async function POST(
  request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  try {
    const { jobId } = await context.params;
    const payload = await request.text();
    return await proxyStream(`/api/jobs/${encodeURIComponent(jobId)}/regenerate/stream`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "text/event-stream",
      },
      body: payload,
    });
  } catch (error) {
    return Response.json(
      {
        detail:
          error instanceof Error ? error.message : "Proxy request failed.",
      },
      { status: 503 },
    );
  }
}
