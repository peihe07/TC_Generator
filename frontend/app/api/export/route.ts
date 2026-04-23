import { NextResponse } from "next/server";

import { proxyJsonResponse } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  try {
    const payload = await request.json();
    return await proxyJsonResponse(
      "/api/export",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      },
      (data) => {
        if (
          typeof data === "object" &&
          data !== null &&
          "jobId" in data &&
          typeof data.jobId === "string"
        ) {
          return {
            ...data,
            downloadUrl: `/api/export/download/${encodeURIComponent(data.jobId)}`,
          };
        }
        return data;
      },
    );
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
