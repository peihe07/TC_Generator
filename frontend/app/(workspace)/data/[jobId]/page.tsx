import DatasetDetailView from "../../../../src/components/data/DatasetDetailView";

export default async function DatasetDetailPage({
  params,
}: {
  params: Promise<{ jobId: string }>;
}) {
  const { jobId } = await params;
  return <DatasetDetailView jobId={jobId} />;
}
