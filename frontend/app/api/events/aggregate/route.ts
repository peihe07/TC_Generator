import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../../_lib/backend";

export const runtime = "nodejs";

export async function GET(request: Request) {
  try {
    const url = new URL(request.url);
    const qs = url.searchParams.toString();
    const suffix = qs ? `?${qs}` : "";
    const wsId = request.headers.get("x-workspace-id");
    return await proxyJsonResponse(`/api/events/aggregate${suffix}`, {
      method: "GET",
      headers: wsId ? { "X-Workspace-Id": wsId } : undefined,
    });
  } catch (error) {
    return NextResponse.json(
      {
        detail:
          error instanceof Error ? error.message : "Proxy request failed.",
      },
      { status: 503 }
    );
  }
}
