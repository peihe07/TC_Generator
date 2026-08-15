#!/usr/bin/env python3
"""Verify Part N (Layer 2 Test Sets) against the Layer 3 map — handoff 12 §2.

Part N is SIGNED (Pei, 2026-08-14). This script does not derive it, propose
it, or adjust it: the 15 Test Sets, their section lists and their declared
leaf counts are transcribed from handoff 12 §2 and hard-coded below. The job
here is to prove the signed partition actually describes the surveyed
population — that it covers every section exactly once and adds up.

Both halves of each Test Set are hard-coded on purpose: the section list AND
the leaf count the handoff declares. Measuring the count from the sections
alone would only prove the arithmetic is self-consistent; comparing it to the
independently-stated figure is what catches a mis-expanded range. Handoff 12
writes several groups as ranges (`7.2 ~ 7.10`, `13.2 ~ 13.6`); those are
expanded explicitly here, and a wrong expansion fails against the declared
count rather than silently redefining the group.

Emits data/test_set_map.tsv (section -> Test Set) for Phase 4. That file is a
LOOKUP, not workbook content: per §4.1.5 Layer 3 never enters the workbook
and is never concatenated into a Test Set name.

Usage:
    python3 features/comfort/scripts/verify_partn.py
"""

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
LAYER3 = FEATURE / "data" / "layer3_map.tsv"
OUT = FEATURE / "data" / "test_set_map.tsv"

TEST_GROUP = "Comfort"          # Layer 1 (R-C6)

# Layer 2 — transcribed from handoff 12 §2. (name, sections, declared leaves)
PART_N = [
    ("Front Climate Anatomy",
     ["2.1", "2.2", "6.3"], 12),
    ("Climate Modes",
     ["2.3", "2.3.1", "2.4", "2.5", "2.5.1", "2.10", "2.11", "2.13", "2.14",
      "2.16"], 41),
    ("Temperature and Fan",
     ["2.6", "2.6.1", "2.7", "2.7.1"], 17),
    ("Airflow and Defrost",
     ["2.8", "2.9", "2.12", "2.12.1", "2.12.2", "2.15"], 23),
    ("Tri-Mode Climate",
     ["3.1", "3.2", "3.3", "3.4"], 14),
    ("Rear Climate",
     ["7.1", "7.1.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9",
      "7.10", "9.1", "9.2", "9.3", "9.4", "9.4.1"], 46),
    ("ECO HVAC",
     ["10.1", "10.2", "10.3", "10.4", "10.5", "10.6", "10.7", "10.8", "10.9",
      "10.9.1"], 15),
    ("Heated Vented Seats",
     ["11.1", "11.2", "11.3", "11.4", "11.5", "11.6", "11.6.1", "11.7",
      "11.8", "11.9", "11.10", "11.11", "11.11.1",
      "12.1", "12.2", "12.3", "12.4", "12.5", "12.6", "12.7", "12.8",
      "12.9"], 59),
    ("Seat Control Tab",
     ["13.2", "13.2.1", "13.3", "13.3.1", "13.4", "13.5", "13.6"], 14),
    ("Climate Popups",
     ["14.1", "14.1.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7",
      "14.8", "14.9", "14.10", "14.10.1", "14.11", "14.12", "14.13", "14.14",
      "14.15", "14.16", "14.16.1", "14.17", "14.18", "14.19", "15.1"], 42),
    ("ICS Anatomy",
     ["16.2", "16.16"], 14),
    ("ICS Climate Modes",
     ["16.3", "16.4", "16.5", "16.10", "16.11", "16.13", "16.14", "16.17"], 40),
    ("ICS Temperature and Fan",
     ["16.6", "16.6.1", "16.7"], 16),
    ("ICS Airflow and Defrost",
     ["16.8", "16.9", "16.12", "16.12.1", "16.15"], 29),
    ("Home Screen Widget",
     ["17.1", "17.2", "17.3", "17.4", "17.5", "18.1"], 21),
]

EXPECTED_TOTAL = 403
EXPECTED_SECTIONS = 129
# Handoff 10 §4.1 / upstream 01 §3 — restated here, not recomputed.
EXPECTED_CHAPTERS = {
    "2": 92, "3": 14, "6": 1, "7": 38, "9": 8, "10": 15, "11": 37,
    "12": 22, "13": 14, "14": 40, "15": 2, "16": 99, "17": 18, "18": 3,
}
BANNED_WORDS = ("Misc", "General", "Unclassified")


def outline_key(s: str) -> tuple:
    return tuple(int(p) for p in s.split("."))


class Checks:
    def __init__(self) -> None:
        self.rows: list = []

    def add(self, name, expected, actual, note="") -> None:
        self.rows.append((name, expected, actual, expected == actual, note))

    @property
    def failed(self) -> int:
        return sum(1 for r in self.rows if not r[3])

    def report(self) -> None:
        print("assertions:")
        for name, expected, actual, ok, note in self.rows:
            print(f"- {'PASS' if ok else '**FAIL**'} — {name}: "
                  f"expected `{expected}`, measured `{actual}`"
                  + (f" — {note}" if note else ""))


def main() -> None:
    layer3 = {r["outline"]: r for r in
              csv.DictReader(LAYER3.open(encoding="utf-8"), delimiter="\t")}
    leaves = {o: int(r["leaf_count"]) for o, r in layer3.items()}
    c = Checks()

    # --- 1. per-Test-Set totals, then the grand total ------------------
    measured_per_set, unknown = {}, {}
    for name, sections, declared in PART_N:
        missing = [s for s in sections if s not in leaves]
        if missing:
            unknown[name] = missing
        measured_per_set[name] = sum(leaves.get(s, 0) for s in sections)
    bad = {n: (d, measured_per_set[n]) for n, _, d in PART_N
           if measured_per_set[n] != d}
    c.add("each Test Set's leaf_count matches handoff 12 §2",
          "all 15 equal",
          "all 15 equal" if not bad else f"mismatch {bad}",
          "declared vs measured, per set")
    c.add("Test Set leaf totals sum to 403", EXPECTED_TOTAL,
          sum(measured_per_set.values()),
          "、".join(f"{n}:{measured_per_set[n]}" for n, _, _ in PART_N))

    # --- 2. every section assigned exactly once ------------------------
    assigned = Counter(s for _, secs, _ in PART_N for s in secs)
    dupes = {s: n for s, n in assigned.items() if n > 1}
    orphans = sorted(set(layer3) - set(assigned), key=outline_key)
    phantom = sorted(set(assigned) - set(layer3), key=outline_key)
    c.add("all 129 mapped sections assigned", EXPECTED_SECTIONS, len(assigned),
          f"unassigned: {orphans or 'none'}; not in layer3_map: "
          f"{phantom or 'none'}")
    c.add("no section assigned to two Test Sets", {}, dupes,
          "a duplicated section would double-count its leaves")

    # --- 3. per-chapter round-trip ------------------------------------
    got = Counter()
    for _, sections, _ in PART_N:
        for s in sections:
            got[s.split(".")[0]] += leaves.get(s, 0)
    ch_bad = {ch: (EXPECTED_CHAPTERS.get(ch), got.get(ch))
              for ch in set(EXPECTED_CHAPTERS) | set(got)
              if EXPECTED_CHAPTERS.get(ch) != got.get(ch)}
    c.add("per-chapter round-trip (ch2==92, ch16==99, +12 others)",
          "all 14 chapters equal",
          "all 14 chapters equal" if not ch_bad else f"mismatch {ch_bad}",
          "、".join(f"{ch}:{got.get(ch, 0)}"
                   for ch in sorted(EXPECTED_CHAPTERS, key=int)))

    # --- 4. naming rules (§4.2 / §4.1.3) -------------------------------
    names = [n for n, _, _ in PART_N]
    offences, group_word = [], []
    for n in names:
        if n != n.strip():
            offences.append(f"{n!r}: leading/trailing whitespace")
        for w in BANNED_WORDS:
            if w.lower() in n.lower():
                offences.append(f"{n!r}: contains banned bucket word {w!r}")
        if n.lower().startswith(TEST_GROUP.lower() + " "):
            group_word.append(n)
    dup_names = [n for n, k in Counter(names).items() if k > 1]
    if dup_names:
        offences.append(f"duplicate Test Set names: {dup_names}")
    c.add("Test Set names: no Misc/General/Unclassified, no stray "
          "whitespace, no duplicates", [], offences,
          f"{len(names)} names checked")

    # §4.2 bans the Test Group as a name prefix. This is REPORTED as its own
    # line rather than folded into the offence list, because that is what
    # surfaced the one case there was: "Comfort Widget" was signed in handoff
    # 12, reported here rather than exempted in a condition, and renamed to
    # "Home Screen Widget" by handoff 13 §2. Had the exemption stayed buried
    # in an `and n != "Comfort Widget"`, the check would have passed and the
    # rename would never have happened — the PASS would have covered it up.
    # Expected to be empty from handoff 13 onward; a non-empty list means the
    # rename did not reach every place, or a new name reintroduced the shape.
    c.add("no Test Set name starts with the Test Group word (§4.2)",
          [], group_word,
          f"{len(names)} names checked against prefix {TEST_GROUP!r}")

    c.report()

    # --- emit the lookup ----------------------------------------------
    lines = ["test_group\ttest_set\toutline\tleaf_count\tsection_title"]
    for name, sections, _ in PART_N:
        for s in sorted(sections, key=outline_key):
            row = layer3.get(s, {})
            lines.append("\t".join([TEST_GROUP, name, s,
                                    str(leaves.get(s, 0)),
                                    row.get("section_title", "(not mapped)")]))
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n{len(lines) - 1} section rows written to {OUT.relative_to(ROOT)}")
    print(f"Test Sets: {len(PART_N)}; leaf range "
          f"{min(measured_per_set.values())}–{max(measured_per_set.values())}; "
          f"largest = {max(measured_per_set.values()) / EXPECTED_TOTAL:.1%}")

    if c.failed:
        sys.exit(f"\nFAILED: {c.failed} assertion(s). Part N is signed, so a "
                 "failure here means the transcription or the Layer 3 map is "
                 "wrong — not that the partition should be adjusted.")


if __name__ == "__main__":
    main()
