#!/usr/bin/env python3
"""Scaffold a new FW036 feature directory per FEATURE_ONBOARDING.md.

Creates the standard feature layout (mirroring mediaHMI/HomeHMI), copies the
DECISIONS.md and feature.yaml templates with the feature name substituted,
and writes RUNBOOK/ANOMALIES skeletons pointing at the canon.

Usage:
    python scripts/new_feature.py Climate
    python scripts/new_feature.py Bluetooth --root /path/to/TC_Generator

This script only scaffolds (Tier 1). Phase 1 recon, Phase 2 rulings, and
everything after are driven from the generated RUNBOOK.
"""

import argparse
import sys
from pathlib import Path

DIRS = ["inputs", "data", "batches", "generated", "scripts", "docs"]

# Written on scaffold, not left for the operator to remember: inputs/ holds
# customer source documents and data/ holds regenerable artefacts. A feature
# dir created without this commits several MB of customer material on the
# first `git add`. The per-feature data/ exclusions are added by that
# feature's Step 1 as its artefacts appear — only the always-true rules and
# the one deliberate exception are stated here.
GITIGNORE = """\
# Customer source files - never commit
inputs/

# Regenerable artifacts (rebuilt by the Step 1 scripts). Add this feature's
# own data/*.json artefacts here as Step 1 starts emitting them.
data/recon.json
batches/
lint_report.json

# data/spec_id_to_outline.tsv IS tracked on purpose where a feature builds
# one: it is the traceability lookup every spec_reference is linted against,
# and a diff on it is the signal that the spec export moved underneath us.

# Local noise
__pycache__/
*.pyc
output/
.DS_Store
"""

RUNBOOK_SKELETON = """\
# FW036 {feature} HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to {feature}.

## Phase 0 — Intake
- [ ] Source files placed in `inputs/` (workbook, 037, spec, popup list)
- [ ] spec_mode classified: ___  (FEATURE_ONBOARDING §3)
- [ ] `feature.yaml` filled from `docs/fw036/templates/feature.yaml`

## Phase 1 — Recon (Tier 1, fully delegable)
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [ ] workbook_state: ___
- [ ] Coverage: ___ leaves total / ___ done / ___ regen targets

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_{feature}_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
"""

ANOMALIES_SKELETON = """\
# ANOMALIES — FW036 {feature} HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-{abbr}nn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

(no entries yet)

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-{abbr}nn]`.
"""


def scaffold(feature: str, root: Path) -> None:
    feat_dir = root / f"{feature}HMI"
    if feat_dir.exists():
        sys.exit(f"refusing to scaffold: {feat_dir} already exists")

    templates = root / "docs" / "fw036" / "templates"
    decisions_tpl = (templates / "DECISIONS.md").read_text(encoding="utf-8")
    yaml_tpl = (templates / "feature.yaml").read_text(encoding="utf-8")
    playbook_tpl = (templates / "PLAYBOOK.md").read_text(encoding="utf-8")

    for d in DIRS:
        (feat_dir / d).mkdir(parents=True)

    abbr = feature[:2].upper()
    (feat_dir / "RUNBOOK.md").write_text(
        RUNBOOK_SKELETON.format(feature=feature), encoding="utf-8")
    (feat_dir / "ANOMALIES.md").write_text(
        ANOMALIES_SKELETON.format(feature=feature, abbr=abbr), encoding="utf-8")
    (feat_dir / "DECISIONS.md").write_text(
        decisions_tpl.replace("{FEATURE}", feature), encoding="utf-8")
    (feat_dir / "feature.yaml").write_text(
        yaml_tpl.replace("{FEATURE}", feature), encoding="utf-8")
    (feat_dir / "PLAYBOOK.md").write_text(
        playbook_tpl.replace("{FEATURE}", feature)
        .replace("{abbr}", abbr), encoding="utf-8")
    (feat_dir / ".gitignore").write_text(GITIGNORE, encoding="utf-8")

    print(f"scaffolded {feat_dir}")
    print("next steps:")
    print(f"  1. drop source files into {feat_dir / 'inputs'}")
    print(f"  2. fill {feat_dir / 'feature.yaml'} (spec_mode, paths)")
    print("  3. run Phase 1 recon (Claude Code, Tier 1)")
    print("  4. review DECISIONS.md [PROPOSED] items and sign (Tier 2)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("feature", help="feature name, e.g. Climate")
    ap.add_argument("--root", default=".", help="repo root")
    args = ap.parse_args()
    scaffold(args.feature, Path(args.root).resolve())


if __name__ == "__main__":
    main()
