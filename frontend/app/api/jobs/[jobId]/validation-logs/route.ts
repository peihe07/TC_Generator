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
      `/api/jobs/${encodeURIComponent(jobId)}/validation-logs`,
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

export async function POST(
  request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  try {
    const { jobId } = await context.params;
    const body = await request.text();
    return await proxyJsonResponse(
      `/api/jobs/${encodeURIComponent(jobId)}/validation-logs`,
      {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        ...workspaceHeaderFrom(request),
      },
        body,
      },
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
