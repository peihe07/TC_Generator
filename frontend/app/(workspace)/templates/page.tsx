import PagePlaceholder from "../../../src/components/shell/PagePlaceholder";

export default function TemplatesPage() {
  return (
    <PagePlaceholder
      title="Templates"
      description="Reusable, versioned generation rules. Powered by spec-library."
      upcoming={[
        "Create / clone / version / deprecate templates",
        "Changelog per version",
        "Usage analytics (runs created by template)",
      ]}
    />
  );
}
