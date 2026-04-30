import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const body = await request.text();
    const wsId = request.headers.get("x-workspace-id");
    return await proxyJsonResponse("/api/events", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(wsId ? { "X-Workspace-Id": wsId } : {}),
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
