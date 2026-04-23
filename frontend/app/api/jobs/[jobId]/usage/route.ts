import { NextResponse } from "next/server";

import { getBackendBaseUrl } from "../../../_lib/backend";

export const runtime = "nodejs";

export async function GET(
  _request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  try {
    const { jobId } = await context.params;
    const response = await fetch(
      `${getBackendBaseUrl()}/api/jobs/${encodeURIComponent(jobId)}/usage`,
      { method: "GET" },
    );
    const data = await response.json();
    return NextResponse.json(data, { status: response.status });
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
