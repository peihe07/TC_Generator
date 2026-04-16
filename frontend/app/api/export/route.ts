import { NextResponse } from "next/server";

import { getBackendBaseUrl } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const payload = await request.json();
    const response = await fetch(`${getBackendBaseUrl()}/api/export`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    if (response.ok && data?.jobId) {
      data.downloadUrl = `/api/export/download/${encodeURIComponent(data.jobId)}`;
    }
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
