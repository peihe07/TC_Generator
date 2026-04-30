import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../../_lib/backend";

export const runtime = "nodejs";

export async function GET(request: Request) {
  try {
    const url = new URL(request.url);
    const qs = url.searchParams.toString();
    const suffix = qs ? `?${qs}` : "";
    return await proxyJsonResponse(`/api/events/aggregate${suffix}`, {
      method: "GET",
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
