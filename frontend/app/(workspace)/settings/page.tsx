import PagePlaceholder from "../../../src/components/shell/PagePlaceholder";

export default function SettingsPage() {
  return (
    <PagePlaceholder
      title="Settings"
      description="Workspace settings and preferences."
      upcoming={["Workspace info", "Members and access", "Integrations"]}
    />
  );
}
