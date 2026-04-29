import PagePlaceholder from "../../../src/components/shell/PagePlaceholder";

export default function OutputsPage() {
  return (
    <PagePlaceholder
      title="Outputs"
      description="Output management and iterative quality checks."
      upcoming={[
        "Search / filter by run, tag, date, owner",
        "Output preview",
        "Compare two outputs (diff view)",
        "Export bundle and metadata",
      ]}
    />
  );
}
