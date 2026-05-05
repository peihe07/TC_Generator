import { proxyGetJsonRoute } from "../../../_lib/backend";

export const runtime = "nodejs";

export async function GET(
  _request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  const { jobId } = await context.params;
  return proxyGetJsonRoute(`/api/jobs/${encodeURIComponent(jobId)}/usage`);
}
