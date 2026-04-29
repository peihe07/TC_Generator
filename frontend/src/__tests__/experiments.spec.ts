import { beforeEach, describe, expect, it } from "vitest";
import {
  EXPERIMENT_DEFINITIONS,
  clearExperimentAssignments,
  getExperimentAssignment,
  getExperimentAssignments,
  resolveExperimentVariant,
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
});
