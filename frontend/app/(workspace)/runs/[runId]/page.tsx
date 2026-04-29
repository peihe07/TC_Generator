import RunDetailView from "../../../../src/components/runs/RunDetailView";

export default async function RunDetailPage({
  params,
}: {
  params: Promise<{ runId: string }>;
}) {
  const { runId } = await params;
  return <RunDetailView runId={runId} />;
}
