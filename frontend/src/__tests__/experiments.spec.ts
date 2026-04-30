import { beforeEach, describe, expect, it } from "vitest";
import {
  EXPERIMENT_DEFINITIONS,
  clearExperimentAssignments,
  clearExperimentDecision,
  getExperimentAssignment,
  getExperimentAssignments,
  getExperimentDecision,
  resolveExperimentVariant,
  setExperimentDecision,
} from "../lib/experiments";

beforeEach(() => {
  localStorage.clear();
});

describe("experiments", () => {
  it("resolves a deterministic variant from subject id", () => {
    const a = resolveExperimentVariant("home_layout_emphasis", "workspace-a");
    const b = resolveExperimentVariant("home_layout_emphasis", "workspace-a");
    expect(a).toBe(b);
    expect(EXPERIMENT_DEFINITIONS.home_layout_emphasis.variants).toContain(a);
  });

  it("persists assignment once selected", () => {
    const first = getExperimentAssignment("home_layout_emphasis", {
      subjectId: "workspace-a",
    });
    const second = getExperimentAssignment("home_layout_emphasis", {
      subjectId: "workspace-b",
    });

    expect(second).toEqual(first);
    expect(getExperimentAssignments()).toEqual({
      home_layout_emphasis: first,
    });
  });

  it("allows explicit override for local validation", () => {
    const assignment = getExperimentAssignment("home_layout_emphasis", {
      override: "action_first",
    });
    expect(assignment.variant).toBe("action_first");
    expect(assignment.source).toBe("override");
  });

  it("clears stored assignments", () => {
    getExperimentAssignment("home_layout_emphasis", { subjectId: "x" });
    clearExperimentAssignments();
    expect(getExperimentAssignments()).toEqual({});
  });

  describe("decisions (promote / resume)", () => {
    it("once concluded, every subject receives the winner with source=concluded", () => {
      setExperimentDecision("home_layout_emphasis", "action_first");
      const a = getExperimentAssignment("home_layout_emphasis", {
        subjectId: "subject-a",
      });
      const b = getExperimentAssignment("home_layout_emphasis", {
        subjectId: "subject-b",
      });
      expect(a.variant).toBe("action_first");
      expect(a.source).toBe("concluded");
      expect(b.variant).toBe("action_first");
    });

    it("decision overrides existing bucket assignment", () => {
      const before = getExperimentAssignment("home_layout_emphasis", {
        subjectId: "stable-subject",
      });
      const otherVariant =
        before.variant === "kpi_first" ? "action_first" : "kpi_first";
      setExperimentDecision("home_layout_emphasis", otherVariant);
      const after = getExperimentAssignment("home_layout_emphasis", {
        subjectId: "stable-subject",
      });
      expect(after.variant).toBe(otherVariant);
      expect(after.source).toBe("concluded");
    });

    it("clearing a decision returns bucketed assignment", () => {
      setExperimentDecision("home_layout_emphasis", "action_first");
      clearExperimentDecision("home_layout_emphasis");
      expect(getExperimentDecision("home_layout_emphasis")).toBeNull();
      const a = getExperimentAssignment("home_layout_emphasis", {
        subjectId: "subject-a",
      });
      expect(a.source).toBe("bucket");
    });

    it("rejects an invalid winner variant", () => {
      expect(() =>
        setExperimentDecision(
          "home_layout_emphasis",
          // @ts-expect-error — intentional invalid variant for guard
          "not_a_real_variant"
        )
      ).toThrow();
    });
  });
});
