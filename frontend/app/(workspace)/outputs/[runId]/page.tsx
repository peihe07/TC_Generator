import OutputPreviewView from "../../../../src/components/outputs/OutputPreviewView";

export default async function OutputPreviewPage({
  params,
}: {
  params: Promise<{ runId: string }>;
}) {
  const { runId } = await params;
  return <OutputPreviewView runId={runId} />;
}
