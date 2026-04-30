import { NextResponse } from "next/server";

import { proxyJsonResponse ,  workspaceHeaderFrom } from "../../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const body = await request.text();
    return await proxyJsonResponse("/api/outputs/compare", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...workspaceHeaderFrom(request),
      },
      body,
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
