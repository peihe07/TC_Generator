import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  cleanup,
  fireEvent,
  render,
  screen,
  waitFor,
} from "@testing-library/react";
import TemplateDetailView from "../components/templates/TemplateDetailView";
import type {
  SpecChangelogEntry,
  SpecLibraryEntry,
} from "../services/jobAdapter";

vi.mock("next/link", () => ({
  default: ({ children, href, ...rest }: React.ComponentProps<"a">) => (
    <a href={href as string} {...rest}>
      {children}
    </a>
  ),
}));

vi.mock("next/navigation", () => ({
  usePathname: () => "/templates/tpl-A",
}));

const seedEntry = (
  overrides: Partial<SpecLibraryEntry> = {}
): SpecLibraryEntry => ({
  name: "tpl-A",
  sourceFile: "a.xlsx",
  entriesCount: 5,
  embeddingModel: "text-embedding-3-large",
  updatedAt: "2026-04-29T12:00:00Z",
  version: "1.0.0",
  changelog: [],
  ...overrides,
});

beforeEach(() => {
  vi.restoreAllMocks();
});

afterEach(cleanup);

function mockEndpoints({
  entry,
  usage,
  changelogResponse,
}: {
  entry: SpecLibraryEntry;
  usage?: object;
  changelogResponse?: object;
}) {
  const fetchMock = vi.fn(
    async (input: RequestInfo | URL, _init?: RequestInit) => {
    void _init;
    const url = typeof input === "string" ? input : input.toString();
    if (url.endsWith("/api/spec-library")) {
      return new Response(JSON.stringify({ specs: [entry] }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
    }
    if (url.includes("/usage")) {
      return new Response(
        JSON.stringify(
          usage ?? {
            name: entry.name,
            usageCount: 0,
            lastUsedAt: null,
            recentRunIds: [],
          }
        ),
        { status: 200, headers: { "Content-Type": "application/json" } }
      );
    }
    if (url.includes("/changelog")) {
      return new Response(
        JSON.stringify(
          changelogResponse ?? {
            ok: true,
            entry: {
              version: "1.1.0",
              message: "added boundary cases",
              ts: 1714000000000,
            },
            spec: {
              ...entry,
              version: "1.1.0",
              changelog: [
                ...(entry.changelog ?? []),
                {
                  version: "1.1.0",
                  message: "added boundary cases",
                  ts: 1714000000000,
                },
              ],
            },
          }
        ),
        { status: 200, headers: { "Content-Type": "application/json" } }
      );
    }
    return new Response("not found", { status: 404 });
    }
  );
  vi.stubGlobal("fetch", fetchMock);
  return fetchMock;
}

describe("TemplateDetailView changelog", () => {
  it("渲染既有 changelog entries（最新優先）", async () => {
    const entry = seedEntry({
      version: "2.0.0",
      changelog: [
        { version: "1.0.0", message: "initial", ts: 1700000000000 },
        { version: "2.0.0", message: "rule overhaul", ts: 1714000000000 },
      ] as SpecChangelogEntry[],
    });
    mockEndpoints({ entry });

    render(<TemplateDetailView templateId="tpl-A" />);

    await waitFor(() => {
      expect(screen.getByText("Changelog")).toBeInTheDocument();
    });
    expect(screen.getByText("v1.0.0")).toBeInTheDocument();
    expect(screen.getByText("rule overhaul")).toBeInTheDocument();
    // 表頭也帶 v2.0.0（current version），加上 entry 列表中也有一筆
    expect(screen.getAllByText("v2.0.0").length).toBeGreaterThanOrEqual(2);
  });

  it("空 changelog 顯示 fallback 文案", async () => {
    mockEndpoints({ entry: seedEntry() });
    render(<TemplateDetailView templateId="tpl-A" />);
    await waitFor(() => {
      expect(
        screen.getByText("No changelog entries yet.")
      ).toBeInTheDocument();
    });
  });

  it("提交表單時 POST 到 /changelog 並把回傳的 entry 加進列表", async () => {
    const fetchMock = mockEndpoints({ entry: seedEntry() });
    render(<TemplateDetailView templateId="tpl-A" />);

    await waitFor(() => {
      expect(screen.getByText("Changelog")).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText("+ Add entry"));
    fireEvent.change(screen.getByPlaceholderText(/Version/), {
      target: { value: "1.1.0" },
    });
    fireEvent.change(screen.getByPlaceholderText("What changed?"), {
      target: { value: "added boundary cases" },
    });
    fireEvent.click(screen.getByText("Save entry"));

    await waitFor(() => {
      expect(screen.getByText("added boundary cases")).toBeInTheDocument();
    });

    const changelogCall = fetchMock.mock.calls.find(([url]) =>
      String(url).includes("/changelog")
    );
    expect(changelogCall).toBeTruthy();
    const init = changelogCall?.[1] as RequestInit | undefined;
    const body = JSON.parse((init?.body as string) ?? "{}");
    expect(body).toEqual({
      version: "1.1.0",
      message: "added boundary cases",
    });
  });

  it("空訊息時顯示 client-side 錯誤、不打 API", async () => {
    const fetchMock = mockEndpoints({ entry: seedEntry() });
    render(<TemplateDetailView templateId="tpl-A" />);

    await waitFor(() => {
      expect(screen.getByText("Changelog")).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText("+ Add entry"));
    fireEvent.click(screen.getByText("Save entry"));

    await waitFor(() => {
      expect(screen.getByText("Message required.")).toBeInTheDocument();
    });
    const changelogCalls = fetchMock.mock.calls.filter(([url]) =>
      String(url).includes("/changelog")
    );
    expect(changelogCalls).toHaveLength(0);
  });
});
