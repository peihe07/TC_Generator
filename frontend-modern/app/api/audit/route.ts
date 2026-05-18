import { proxyFormBodyRoute } from "../_lib/backend";

export const runtime = "nodejs";

export async function POST(request: Request) {
  return proxyFormBodyRoute(request, "/api/audit");
}
