import PagePlaceholder from "../../../src/components/shell/PagePlaceholder";

export default function DataPage() {
  return (
    <PagePlaceholder
      title="Data"
      description="Ingestion reliability and schema visibility."
      upcoming={[
        "Dataset upload registry",
        "Schema preview and compatibility hints",
        "Data quality alerts",
      ]}
    />
  );
}
