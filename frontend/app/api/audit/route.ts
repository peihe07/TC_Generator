import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    return await proxyJsonResponse("/api/audit", {
      method: "POST",
      body: formData,
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
