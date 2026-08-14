#!/usr/bin/env python3
"""Scaffold a new FW036 feature directory per FEATURE_ONBOARDING.md.

Creates the standard feature layout at `features/<name>/` (mirroring
features/media and features/home), copies the
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

# RULINGS.md and DATA_REQUESTS.md were previously left for the operator to
# create by hand, so a feature could reach Phase 2 with its signed rulings
# living only in a chat log (the AMFM/Projection gap recorded in their
# docs/INDEX.md). Both are scaffolded now — an empty register is a visible
# state, an absent file is not.
RULINGS_SKELETON = """\
# RULINGS — {feature} (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 {feature} 之裁決權威；
跨 feature 條文承接時註明來源包。

---

(no rulings recorded yet)
"""

DATA_REQUESTS_SKELETON = """\
# DATA REQUESTS — {feature} (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/{slug}/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| — | (none known at scaffold time) | — | — | — | — | — |
"""


def scaffold(feature: str, root: Path, adopt_existing: bool = False) -> None:
    # Directory naming convention (2026-08-11 reorg): all features live under
    # features/, lowercase, without the HMI suffix. The feature NAME keeps its
    # own casing — it is what feature.yaml and the profile filename carry.
    feat_dir = root / "features" / feature.lower()
    if feat_dir.exists() and not adopt_existing:
        sys.exit(f"refusing to scaffold: {feat_dir} already exists")

    templates = root / "docs" / "fw036" / "templates"
    decisions_tpl = (templates / "DECISIONS.md").read_text(encoding="utf-8")
    yaml_tpl = (templates / "feature.yaml").read_text(encoding="utf-8")
    playbook_tpl = (templates / "PLAYBOOK.md").read_text(encoding="utf-8")

    for d in DIRS:
        (feat_dir / d).mkdir(parents=True, exist_ok=adopt_existing)

    abbr = feature[:2].upper()
    files = {
        "RUNBOOK.md": RUNBOOK_SKELETON.format(feature=feature),
        "ANOMALIES.md": ANOMALIES_SKELETON.format(feature=feature, abbr=abbr),
        "RULINGS.md": RULINGS_SKELETON.format(feature=feature),
        "DATA_REQUESTS.md": DATA_REQUESTS_SKELETON.format(
            feature=feature, slug=feature.lower()),
        "DECISIONS.md": decisions_tpl.replace("{FEATURE}", feature),
        "feature.yaml": yaml_tpl.replace("{FEATURE}", feature),
        "PLAYBOOK.md": (playbook_tpl.replace("{FEATURE}", feature)
                        .replace("{abbr}", abbr)),
        ".gitignore": GITIGNORE,
    }
    # --adopt-existing exists for the case where the analysis layer has already
    # delivered docs/handoff/ into an otherwise-empty feature dir. It fills the
    # gaps and NEVER overwrites: a scaffold that clobbered a signed handoff
    # would destroy the only copy of a ruling.
    skipped = []
    for name, body in files.items():
        target = feat_dir / name
        if target.exists():
            skipped.append(name)
            continue
        target.write_text(body, encoding="utf-8")

    print(f"scaffolded {feat_dir}")
    if skipped:
        print(f"  kept existing (not overwritten): {', '.join(sorted(skipped))}")
    print("next steps:")
    print(f"  1. drop source files into {feat_dir / 'inputs'}")
    print(f"  2. fill {feat_dir / 'feature.yaml'} (spec_mode, paths)")
    print("  3. run Phase 1 recon (Claude Code, Tier 1)")
    print("  4. review DECISIONS.md [PROPOSED] items and sign (Tier 2)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("feature", help="feature name, e.g. Climate")
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--adopt-existing", action="store_true",
                    help="fill gaps in an existing feature dir; never "
                         "overwrites a file that is already there")
    args = ap.parse_args()
    scaffold(args.feature, Path(args.root).resolve(), args.adopt_existing)


if __name__ == "__main__":
    main()
