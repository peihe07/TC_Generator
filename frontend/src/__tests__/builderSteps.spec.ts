import { describe, expect, it } from "vitest";
import {
  BUILDER_STEPS,
  isBuilderStep,
  nextStep,
  prevStep,
  STEP_DEFINITIONS,
} from "../components/builder/types";

describe("builder step navigation", () => {
  it("BUILDER_STEPS 順序固定", () => {
    expect(BUILDER_STEPS).toEqual([
      "data",
      "configure",
      "validate",
      "execute",
      "review",
    ]);
  });

  it("isBuilderStep guard", () => {
    expect(isBuilderStep("data")).toBe(true);
    expect(isBuilderStep("review")).toBe(true);
    expect(isBuilderStep("nope")).toBe(false);
  });

  it("nextStep 走到最後回 null", () => {
    expect(nextStep("data")).toBe("configure");
    expect(nextStep("configure")).toBe("validate");
    expect(nextStep("validate")).toBe("execute");
    expect(nextStep("execute")).toBe("review");
    expect(nextStep("review")).toBeNull();
  });

  it("prevStep 走回頭回 null", () => {
    expect(prevStep("review")).toBe("execute");
    expect(prevStep("execute")).toBe("validate");
    expect(prevStep("validate")).toBe("configure");
    expect(prevStep("configure")).toBe("data");
    expect(prevStep("data")).toBeNull();
  });

  it("STEP_DEFINITIONS 每個 step 都有 label/description", () => {
    for (const step of BUILDER_STEPS) {
      expect(STEP_DEFINITIONS[step].label).toBeTruthy();
      expect(STEP_DEFINITIONS[step].description).toBeTruthy();
    }
  });
});
