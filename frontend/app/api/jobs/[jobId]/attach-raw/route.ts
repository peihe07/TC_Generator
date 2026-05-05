import { proxyErrorResponse, proxyJsonResponse } from "../../../_lib/backend";

export const runtime = "nodejs";

export async function POST(
  request: Request,
  context: { params: Promise<{ jobId: string }> },
) {
  try {
    const { jobId } = await context.params;
    const formData = await request.formData();
    return await proxyJsonResponse(
      `/api/jobs/${encodeURIComponent(jobId)}/attach-raw`,
      {
        method: "POST",
        body: formData,
      },
    );
  } catch (error) {
    return proxyErrorResponse(error);
  }
}
