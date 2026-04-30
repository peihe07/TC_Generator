import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../../../_lib/backend";

export const runtime = "nodejs";

export async function GET(
  request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  try {
    const { jobId } = await context.params;
    const url = new URL(request.url);
    const qs = url.searchParams.toString();
    const path = `/api/jobs/${encodeURIComponent(jobId)}/output-preview${
      qs ? `?${qs}` : ""
    }`;
    return await proxyJsonResponse(path, { method: "GET" });
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
