import { beforeEach, describe, expect, it } from "vitest";
import { useCommandPaletteStore } from "../store/useCommandPaletteStore";

beforeEach(() => {
  useCommandPaletteStore.setState({ open: false });
});

describe("useCommandPaletteStore", () => {
  it("初始為關閉", () => {
    expect(useCommandPaletteStore.getState().open).toBe(false);
  });

  it("setOpen 設定狀態", () => {
    useCommandPaletteStore.getState().setOpen(true);
    expect(useCommandPaletteStore.getState().open).toBe(true);
    useCommandPaletteStore.getState().setOpen(false);
    expect(useCommandPaletteStore.getState().open).toBe(false);
  });

  it("toggle 翻轉狀態", () => {
    useCommandPaletteStore.getState().toggle();
    expect(useCommandPaletteStore.getState().open).toBe(true);
    useCommandPaletteStore.getState().toggle();
    expect(useCommandPaletteStore.getState().open).toBe(false);
  });
});
