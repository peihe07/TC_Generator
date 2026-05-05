import { proxyTextStreamRoute } from "../../../../_lib/backend";

export const runtime = "nodejs";

export async function POST(
  request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  const { jobId } = await context.params;
  return proxyTextStreamRoute(
    request,
    `/api/jobs/${encodeURIComponent(jobId)}/regenerate/stream`,
  );
}
