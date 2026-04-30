export const metadata = {
  title: "Diagrams · TC Generator",
};

export default function DiagramsPage() {
  return (
    <div className="space-y-4">
      <header className="space-y-1">
        <h1 className="text-3xl font-bold text-primary">Workflow Diagrams</h1>
        <p className="text-secondary text-sm">
          Architecture & process flow charts (sourced from public/diagrams.html).
        </p>
      </header>

      <div
        className="surface overflow-hidden"
        style={{ height: "calc(100vh - 200px)", minHeight: 480 }}
      >
        <iframe
          src="/diagrams.html"
          title="Workflow Diagrams"
          style={{
            width: "100%",
            height: "100%",
            border: "none",
            display: "block",
          }}
        />
      </div>
    </div>
  );
}
