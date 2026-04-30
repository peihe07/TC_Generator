import { afterEach, describe, expect, it } from "vitest";
import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import DataTable, { type DataTableColumn } from "../components/ui/DataTable";

afterEach(cleanup);

interface Row {
  id: string;
  name: string;
  cost: number;
}

const rows: Row[] = [
  { id: "a", name: "Alpha", cost: 3 },
  { id: "b", name: "Bravo", cost: 1 },
  { id: "c", name: "Charlie", cost: 2 },
];

const columns: DataTableColumn<Row>[] = [
  { id: "name", header: "Name", cell: (r) => r.name, sortBy: (r) => r.name },
  {
    id: "cost",
    header: "Cost",
    cell: (r) => r.cost.toFixed(2),
    sortBy: (r) => r.cost,
    align: "right",
  },
];

describe("DataTable", () => {
  it("renders rows with cell content", () => {
    render(<DataTable rows={rows} columns={columns} rowKey={(r) => r.id} />);
    expect(screen.getByText("Alpha")).toBeInTheDocument();
    expect(screen.getByText("Bravo")).toBeInTheDocument();
    expect(screen.getByText("3.00")).toBeInTheDocument();
  });

  it("empty state when rows empty", () => {
    render(
      <DataTable
        rows={[]}
        columns={columns}
        empty={<span>nothing here</span>}
      />,
    );
    expect(screen.getByText("nothing here")).toBeInTheDocument();
  });

  it("clicking sortable header toggles sort direction", () => {
    render(
      <DataTable
        rows={rows}
        columns={columns}
        rowKey={(r) => r.id}
        defaultSort={{ columnId: "cost", direction: "asc" }}
      />,
    );
    // 預設 cost asc → row 順序為 Bravo (1), Charlie (2), Alpha (3)
    const tbodyRows = screen.getAllByRole("row").slice(1); // skip header
    expect(tbodyRows[0]).toHaveTextContent("Bravo");
    expect(tbodyRows[2]).toHaveTextContent("Alpha");

    fireEvent.click(screen.getByRole("button", { name: /Cost/ }));
    const after = screen.getAllByRole("row").slice(1);
    expect(after[0]).toHaveTextContent("Alpha");
    expect(after[2]).toHaveTextContent("Bravo");
  });
});
