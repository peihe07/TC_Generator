import { proxyStream ,  workspaceHeaderFrom } from "../../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const payload = await request.text();
    return await proxyStream("/api/quick-generate/stream", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "text/event-stream",
      },
      signal: request.signal,
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
