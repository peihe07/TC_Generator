import { NextResponse } from "next/server";

import { proxyJsonResponse ,  workspaceHeaderFrom } from "../../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const payload = await request.json();
    return await proxyJsonResponse("/api/review/suggest-fix", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...workspaceHeaderFrom(request),
      },
      body: JSON.stringify(payload),
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
