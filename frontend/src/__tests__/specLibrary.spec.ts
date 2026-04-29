import { describe, expect, it } from "vitest";
import { formatSpecLibraryLabel } from "../lib/specLibrary";

describe("formatSpecLibraryLabel", () => {
  it("沒有 HMI 標記時回原字串", () => {
    expect(formatSpecLibraryLabel("Project_X")).toBe("Project_X");
    expect(formatSpecLibraryLabel("hello world")).toBe("hello world");
  });

  it("抽出第一個 HMI 後內容直到下個 HMI", () => {
    expect(
      formatSpecLibraryLabel("Project_HMI_RegionA_HMI_OldName")
    ).toBe("RegionA");
  });

  it("抽出第一個 HMI 後內容直到 _Rn 標記", () => {
    expect(formatSpecLibraryLabel("Project_HMI_RegionA_R1")).toBe("RegionA");
  });

  it("抽出 HMI 後內容直到尾端括號標記", () => {
    expect(
      formatSpecLibraryLabel("Project_HMI_RegionA_(latest)")
    ).toBe("RegionA");
  });

  it("把底線換成空白並去掉前後空白", () => {
    expect(
      formatSpecLibraryLabel("X_HMI_Multi_Word_Region_R2")
    ).toBe("Multi Word Region");
  });

  it("HMI 後直接接到 _Rn 標記時抽出尾段（非空 fallback 條件）", () => {
    // 該情境 contentEnd <= contentStart，slice 回到尾端 "_R1" → "R1"
    expect(formatSpecLibraryLabel("X_HMI_R1")).toBe("R1");
  });
});
