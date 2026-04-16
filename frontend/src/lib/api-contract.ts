import type { TcPreviewRow, TcRow } from "@/src/lib/types";

export type ParseResponse = {
  jobId: string;
  project: string | null;
  testGroup: string | null;
  rowCount: number;
  previewHeaders: string[];
  previewRows: TcPreviewRow[];
  rows: TcRow[];
  columnFillStatus: Record<string, number>;
  files: {
    rawFileName: string | null;
    specFileName: string | null;
    specFormat: string | null;
  };
};

export type GenerateRequest = {
  jobId?: string | null;
  rows: TcRow[];
  config: {
    model: string;
    batchSize: number;
    budget: number;
    strictValidation: boolean;
  };
};

export type GenerateResponse = {
  jobId: string;
  status: "queued";
  totalRows: number;
  streamUrl: string;
};

export type GenerateStreamEvent =
  | {
      type: "job.started" | "job.completed";
      jobId: string;
      stats: {
        total: number;
        processed: number;
        currentCost: number;
      };
      message: string;
    }
  | {
      type: "row.completed";
      jobId: string;
      row: TcRow;
      stats: {
        total: number;
        processed: number;
        currentCost: number;
      };
      message: string;
    };

export type ExportRequest = {
  jobId: string;
  scope: "all" | "accepted" | "flagged";
  outputMode: "new-file" | "overwrite";
  includeFrameworkSheet: boolean;
  selectedColumns: string[];
  rows: TcRow[];
};

export type ExportResponse = {
  jobId: string;
  status: "ready";
  exportedRows: number;
  fileName: string;
  downloadUrl: string;
  selectedColumns: string[];
};
