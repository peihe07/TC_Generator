import { proxyJsonBodyRoute } from "../../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  return proxyJsonBodyRoute(request, "/api/review/suggest-fix");
}
