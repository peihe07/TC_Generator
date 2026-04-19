import { NextResponse } from "next/server";

import { getBackendBaseUrl } from "../../_lib/backend";

export const runtime = "nodejs";

export async function GET(request: Request) {
  try {
    const url = new URL(request.url);
    const qs = url.searchParams.toString();
    const suffix = qs ? `?${qs}` : "";
    const response = await fetch(
      `${getBackendBaseUrl()}/api/metrics/aggregate${suffix}`,
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
