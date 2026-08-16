#!/usr/bin/env python3
"""Cross-Test-Set sibling candidate generator (handoff 37 §6).

Whether two sections are siblings cannot be decided mechanically. What CAN be
mechanised is producing candidates and making that production a required step
at the moment a Test Set completes — so "remember to check" stops being a
memory and becomes a run.

Method: two sections in DIFFERENT Test Sets whose full_text share at least one
of the spec's own upper-case vocabulary tokens (SYNC, MAX DEF, RECIRC, AUTO …).

  !! This list is NOT a completeness proof (R-C37). It is produced by lexical
  !! overlap and cannot find a sibling pair that shares no vocabulary — e.g.
  !! two sections describing the same behaviour in different words. Every run
  !! prints that limit; do not quote a clean run as "no siblings remain".

`data/pending_sibling.tsv` records each judgement and the `reviewed_at` state
(the feature's section count when the review ran), so "which round was this
table last checked in" is answerable from the file rather than from memory.

Usage:
    python3 features/comfort/scripts/sibling_candidates.py            # report
    python3 features/comfort/scripts/sibling_candidates.py --for "Climate Modes"
"""

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
FRAMEWORK = FEATURE / "framework.md"
TABLE = FEATURE / "data" / "pending_sibling.tsv"

# The spec's own screaming-case names. Deliberately not a general keyword
# extractor: these are the tokens the clauses use as proper names for
# functions, which is what makes two sections about the same thing.
# 40 §4 — case-INSENSITIVE. 3.2 writes "turns on Sync" where 2.11 writes
# "SYNC"; a case-sensitive literal was silently splitting them, exactly as
# MAX DEFROST vs MAX DEF did. Measured counts across the 129 sections:
# SYNC 20, Sync 8, sync 6 — the split was real, not hypothetical.
VOCAB = re.compile(
    r"\b(SYNC|MAX A/?C|MAX DEFROST|MAX DEF|RECIRC\w*|AUTO ECO|ECO HVAC|"
    r"AUTO|REAR DEFROST|REAR DEF|FRONT ?/? ?MAX DEFROST|FRONT DEF|DEFROST|"
    r"CLIMATE OFF|HVAC|MODE|TEMPERATURE|FAN|A/?C|LO|HI|ICS)\b", re.I)
# 39 §4.1 — these pair almost everything with everything. They used to be
# DROPPED, and that silent drop is what produced Front Climate Anatomy's "0
# candidates". They are now MARKED instead: a marked candidate still gets
# read, a dropped one never does.
HIGH_FREQUENCY = {"FAN", "MODE", "TEMPERATURE", "HI", "LO", "HVAC", "AUTO"}
# 39 §4.2 — measured from the corpus, not from memory: a scan of
# MAX */REAR */FRONT * forms over all 129 sections. 2.10 writes MAX DEFROST
# where 3.3 writes MAX DEF, and that one difference hid a sibling pair we
# already knew about.
# Measured over all 129 sections (40 §4.2), counts in comments. Keys are
# upper-cased before lookup, so case variants collapse first.
SYNONYMS = {
    "MAX DEFROST": "MAX DEF",          # 2 vs 32
    "FRONT /MAX DEFROST": "MAX DEF",   # 1
    "FRONT/MAX DEFROST": "MAX DEF",
    "REAR DEFROST": "REAR DEF",        # 7 vs 1
    "MAX AC": "MAX A/C",               # MAX A/C 23
    "AC": "A/C",                       # AC 11 vs A/C 44
    "RECIRCULATION": "RECIRC",         # RECIRC 7
}


def normalise(tokens: set) -> set:
    """Upper-case first, then map onto the canonical member of each group."""
    out = set()
    for tok in tokens:
        key = " ".join(tok.upper().split())
        out.add(SYNONYMS.get(key, key))
    return out


def test_set_of_section() -> dict:
    """Read Part N's group table — the framework is the authority, not a copy.

    A section listed under two groups used to be resolved by last-wins, which
    made an injected mis-grouping invisible: the later, correct row simply
    overwrote it. Duplicates now abort (38 §4).
    """
    mapping, seen = {}, {}
    for line in FRAMEWORK.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*\*?\*?\d",
                     line)
        if not m:
            continue
        name, spec = m.group(1), m.group(2)
        for part in spec.split(","):
            part = part.strip().strip("*` ")
            if "~" in part:                      # "7.1 ~ 7.10" style ranges
                lo, hi = (p.strip() for p in part.split("~"))
                mapping.setdefault(("range", name), []).append((lo, hi))
            elif part:
                if part in seen and seen[part] != name:
                    raise SystemExit(
                        f"ABORT — framework.md lists {part} under both "
                        f"{seen[part]!r} and {name!r}; a section belongs to "
                        "exactly one Test Set (§4.1)")
                seen[part] = name
                mapping[part] = name
    return mapping


def resolve(outline: str, mapping: dict) -> str:
    if outline in mapping:
        return mapping[outline]
    head = outline.split(".")[0]
    for key, ranges in mapping.items():
        if not (isinstance(key, tuple) and key[0] == "range"):
            continue
        for lo, hi in ranges:
            if lo.split(".")[0] == head == hi.split(".")[0]:
                a = [int(x) for x in outline.split(".")]
                l = [int(x) for x in lo.split(".")]
                h = [int(x) for x in hi.split(".")]
                if l <= a <= h:
                    return key[1]
    return ""


def verify_parse(sections: dict, group: dict) -> None:
    """38 §4 — the parse fails silently, so it is checked before it is used.

    framework.md is parsed with a regex over a markdown table; a damaged or
    reformatted table would quietly drop a group and change which pairs count
    as cross-set. The check is against test_set_map.tsv, which was derived
    independently at Phase 3, so an error has to occur in both to pass.
    """
    with (FEATURE / "data" / "test_set_map.tsv").open(encoding="utf-8") as fh:
        expected = {r["outline"]: r["test_set"]
                    for r in csv.DictReader(fh, delimiter="\t")}

    problems = []
    if len(group) != 129:
        problems.append(f"parsed {len(group)} sections, expected 129")
    unassigned = sorted(o for o, g in group.items() if not g)
    if unassigned:
        problems.append(f"{len(unassigned)} section(s) resolved to no Test "
                        f"Set: {unassigned}")
    mismatched = sorted(o for o in group
                        if o in expected and group[o] != expected[o])
    if mismatched:
        problems.append("disagrees with test_set_map.tsv for "
                        + ", ".join(f"{o} (framework={group[o]!r} vs "
                                    f"map={expected[o]!r})" for o in mismatched))
    missing = sorted(set(expected) - set(group))
    if missing:
        problems.append(f"test_set_map has sections the parse never saw: {missing}")

    if problems:
        raise SystemExit("ABORT — framework.md group parse is unusable:\n  "
                         + "\n  ".join(problems))
    print(f"parse check: 129 sections, each in exactly one Test Set, "
          f"agreeing with test_set_map.tsv")


def load_table() -> list:
    if not TABLE.exists():
        return []
    with TABLE.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


# 42 §1 — `provisional` marks a verdict whose evidence is weaker than what it
# will be compared against. A pair judged while one side has no TCs was judged
# against that side's CLAUSE; the day that side is generated, the thing to
# compare against is a TC. Same verdict, different object. The flag says "look
# again", not "you were wrong" — re-confirmation may keep the verdict.
FIELDS = ["outline", "sibling_outline", "verdict", "provisional",
          "reviewed_at", "reason"]
DEFERRED_REASON = (
    "**依 41 §3 規則三入表（42 §2 之全量重建）。** 兩節皆未生成，現在判無處可用 —— "
    "sibling 判定之用途是寫 TC 時決定 `duplicate_of`／`distinguishing_axis`（§4.6）。"
    "其所屬組生成之日連同其他候選一併判定。**`deferred` 不是 `not-sibling`**：前者是"
    "「尚未問」，後者是「問過了，答案是否」")


def generated_outlines() -> set:
    """Sections with at least one emitted TC — read from generated/, which is
    the only place that fact exists. A hand-kept list would drift."""
    return {json.loads(p.read_text(encoding="utf-8"))["outline"]
            for p in sorted((FEATURE / "generated").glob("*.json"))}


def key(a: str, b: str) -> tuple:
    """Order-independent pair key. The table was written by two different
    rounds with the two sides in different orders; merging on a directed key
    would duplicate rows that are the same pair (42 §2)."""
    return tuple(sorted((a, b), key=lambda o: [int(t) for t in o.split(".")]))


# Verdicts that have never been judged pair-by-pair. `deferred` says so on
# its face; `not-broken-by-3-samples (class)` says so in its name (41 §4 —
# three samples break a class, they do not establish one). Neither may ever
# be non-provisional, whatever is generated.
NEVER_FINAL = {"deferred", "not-broken-by-3-samples (class)"}


def provisional_of(k: tuple, rec: dict, gen: set) -> str:
    """42 §1. Monotone in one direction only: once a human clears a row by
    writing `false`, a later rebuild must not set it back to `true` — the
    clearing IS the re-confirmation the gate asked for. Recomputing it would
    make the gate un-satisfiable and the work invisible."""
    if rec["verdict"] in NEVER_FINAL:
        return "true"
    if rec.get("provisional") == "false":
        return "false"
    return "false" if (k[0] in gen and k[1] in gen) else "true"


def rebuild(pairs: dict, group: dict, gen: set, n_sections: int) -> None:
    """42 §2 — full rebuild with key merge. The table is machine-maintained:
    every candidate pair appears, judged or not, so that "not in the table"
    stops meaning "not yet reachable" and starts meaning "not a candidate".

    Existing verdicts survive: a key already judged (verdict != deferred)
    keeps its verdict and reason. Only `provisional` is recomputed, because
    it is a function of what is generated TODAY, not of when the row was
    written.
    """
    existing = {}
    for r in load_table():
        existing[key(r["outline"], r["sibling_outline"])] = r

    def emit(k, rec, tally):
        rows.append({"outline": k[0], "sibling_outline": k[1],
                     "verdict": rec["verdict"],
                     "provisional": provisional_of(k, rec, gen),
                     "reviewed_at": rec["reviewed_at"],
                     "reason": rec["reason"]})
        stats[tally] += 1

    rows, stats = [], Counter()
    for (a, b) in sorted(pairs, key=lambda p: key(*p)):
        k = key(a, b)
        old = existing.pop(k, None)
        if old and old["verdict"] != "deferred":
            emit(k, old, "kept")
        else:
            emit(k, {"verdict": "deferred", "reviewed_at": str(n_sections),
                     "reason": DEFERRED_REASON}, "new deferred")

    # A judged row whose pair is no longer a candidate is NOT dropped — the
    # judgement was human work and its disappearance would be silent. It is
    # carried over and reported (R-C24's shape: exemptions are named lines).
    for k, old in sorted(existing.items()):
        emit(k, old, "carried over (no longer a candidate)")

    rows.sort(key=lambda r: key(r["outline"], r["sibling_outline"]))
    with TABLE.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t",
                           lineterminator="\n", quoting=csv.QUOTE_NONE,
                           quotechar="", escapechar=None)
        w.writeheader()
        w.writerows(rows)

    print(f"\nrebuilt {TABLE.name}: {len(rows)} rows")
    for k2, v in sorted(stats.items()):
        print(f"  {k2:38} {v}")
    print("  verdict distribution:")
    for v, n in sorted(Counter(r["verdict"] for r in rows).items()):
        print(f"    {v:34} {n}")
    print("  provisional:")
    for v, n in sorted(Counter(r["provisional"] for r in rows).items()):
        print(f"    {v:34} {n}")
    if stats["carried over (no longer a candidate)"]:
        print("  !! carried-over rows are judgements the current vocabulary no")
        print("  !! longer reproduces; they are kept, not dropped (R-C37)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--for", dest="group", default=None,
                    help="restrict one side to this Test Set (use when that "
                         "set has just completed)")
    ap.add_argument("--rebuild", action="store_true",
                    help="42 §2 — full rebuild of pending_sibling.tsv with "
                         "key merge. Refuses to run with --for, because a "
                         "restricted run would write a TRUNCATED table and "
                         "the truncation would look like 'no candidate'")
    args = ap.parse_args()
    if args.rebuild and args.group:
        raise SystemExit("ABORT — --rebuild is whole-corpus by definition; "
                         "--for would write a truncated table (42 §2)")

    with FULLTEXT.open(encoding="utf-8") as fh:
        sections = {r["outline"]: r["full_text"].replace("\\n", "\n")
                    for r in csv.DictReader(fh, delimiter="\t")}
    mapping = test_set_of_section()
    group = {o: resolve(o, mapping) for o in sections}
    verify_parse(sections, group)

    tokens = {o: normalise(set(VOCAB.findall(txt)))
              for o, txt in sections.items()}

    pairs = defaultdict(set)
    outlines = sorted(sections)
    for i, a in enumerate(outlines):
        for b in outlines[i + 1:]:
            if not group[a] or not group[b] or group[a] == group[b]:
                continue
            if args.group and args.group not in (group[a], group[b]):
                continue
            shared = tokens[a] & tokens[b]
            if shared:
                pairs[(a, b)] = shared

    judged = {(r["outline"], r["sibling_outline"]): r for r in load_table()}

    print(f"sections: {len(sections)}   candidate pairs: {len(pairs)}"
          + (f"   restricted to: {args.group}" if args.group else ""))
    print(f"high-frequency tokens are MARKED, not excluded (39 §4.1): "
          f"{sorted(HIGH_FREQUENCY)}")
    print(f"synonym groups applied (measured from the corpus, 39 §4.2): "
          f"{ {k: v for k, v in SYNONYMS.items() if k != v} }\n")

    unjudged = []
    for (a, b), shared in sorted(pairs.items()):
        rec = judged.get((a, b)) or judged.get((b, a))
        mark = rec["verdict"] if rec else "UNJUDGED"
        if not rec:
            unjudged.append((a, b, sorted(shared)))
        hf = " high-frequency" if shared <= HIGH_FREQUENCY else ""
        print(f"- {a:8} [{group[a]:22}] <-> {b:8} [{group[b]:22}] "
              f"{sorted(shared)}  {mark}{hf}")

    print(f"\n{len(pairs) - len(unjudged)} judged, {len(unjudged)} unjudged")
    print("\n!! NOT a completeness proof (R-C37): this list comes from lexical")
    print("!! overlap (including the measured synonym groups) and cannot")
    print("!! surface a sibling pair that shares none of the vocabulary above")
    print("!! and is not in an equivalence group. A clean run means 'no")
    print("!! candidate by this method', never 'no siblings remain'.")

    if args.rebuild:
        rebuild(pairs, group, generated_outlines(), len(sections))
        return

    for r in load_table():
        print(f"\ntable: {r['outline']} <-> {r['sibling_outline']} "
              f"verdict={r['verdict']} provisional={r.get('provisional', '?')} "
              f"reviewed_at={r['reviewed_at']} sections — {r['reason']}")


if __name__ == "__main__":
    main()
