import TemplateDetailView from "../../../../src/components/templates/TemplateDetailView";

export default async function TemplateDetailPage({
  params,
}: {
  params: Promise<{ templateId: string }>;
}) {
  const { templateId } = await params;
  return <TemplateDetailView templateId={decodeURIComponent(templateId)} />;
}
