import { NextResponse } from "next/server";

import { proxyJsonResponse ,  workspaceHeaderFrom } from "../../../_lib/backend";

export const runtime = "nodejs";

export async function GET(
  request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  try {
    const { jobId } = await context.params;
    return await proxyJsonResponse(
      `/api/jobs/${encodeURIComponent(jobId)}/timeline`,
      { method: "GET", headers: workspaceHeaderFrom(request)  },
    );
  } catch (error) {
    return NextResponse.json(
      {
        detail:
          error instanceof Error ? error.message : "Proxy request failed.",
      },
      { status: 503 },
    );
  }
}
