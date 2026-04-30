import AutoSizingIframe from "../AutoSizingIframe";

export default function DiagramsView() {
  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h1 className="text-3xl font-bold text-primary">Workflow Diagrams</h1>
        <p className="text-secondary text-sm">
          Architecture & process flow charts.
        </p>
      </header>

      <div className="surface overflow-hidden">
        <AutoSizingIframe src="/diagrams.html" title="Workflow Diagrams" />
      </div>
    </div>
  );
}
