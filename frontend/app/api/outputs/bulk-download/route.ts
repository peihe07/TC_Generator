import { NextResponse } from "next/server";

import { getBackendBaseUrl } from "../../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const body = await request.text();
    const upstream = await fetch(
      `${getBackendBaseUrl()}/api/outputs/bulk-download`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body,
      },
    );
    return new Response(upstream.body, {
      status: upstream.status,
      statusText: upstream.statusText,
      headers: upstream.headers,
    });
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
