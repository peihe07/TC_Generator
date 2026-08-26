#!/usr/bin/env python3
"""IN §9 self-check, mechanised subset, run over the pilot batch.

Only the items a machine can decide are here. The rest of §9 (is the ER
really observable, does the TC really trace to the requirement) is a reading
task and stays with the pilot review -- this script does NOT report those as
passing, it reports them as not covered, because a green run that silently
omits half the checklist is the failure mode R-G11 is about.
"""
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
BATCH = FEAT / "batches" / "pilot" / "pilot_tcs.json"

TEXT_FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
               "expected_result"]
REQUIRED = ["tc_title", "pre_conditions", "input_test_data", "test_procedure",
            "expected_result", "specification_reference", "design_method",
            "priority", "split_flag", "split_reason"]
METHODS = {"Negative / Invalid", "Fault Injection", "State Transition",
           "Decision Table", "Equivalence Partitioning",
           "Boundary Value Analysis", "Combinatorial", "Scenario / Use Case",
           "Functional Based"}
MODALS = re.compile(r"\b(shall|will|should|would)\b", re.I)
CJK = re.compile(r"[一-鿿]")
NUMBERED = re.compile(r"^\d+\.\s")

fails: list[str] = []


def fail(rid: str, item: str, detail: str) -> None:
    fails.append(f"{rid}  [{item}] {detail}")


def main() -> int:
    data = json.loads(BATCH.read_text(encoding="utf-8"))
    tcs = data["tcs"]
    const = None
    lower_halves: dict[str, list[str]] = {}

    for tc in tcs:
        rid = tc.get("req_id", "?")

        for k in REQUIRED:                                    # §10.1
            if k not in tc:
                fail(rid, "10.1", f"missing key {k}")

        if tc.get("priority") not in {"P0", "P1", "P2", "P3"}:   # §10.2
            fail(rid, "10.2", f"priority {tc.get('priority')!r}")

        if tc.get("design_method") not in METHODS:               # §12
            fail(rid, "12", f"design_method {tc.get('design_method')!r}")

        # §4.3.1 two-part test_item
        title = tc.get("tc_title", "")
        parts = title.split("\n")
        if len(parts) != 2:
            fail(rid, "4.3.1", f"test_item is not two lines ({len(parts)})")
        else:
            upper, lower = parts
            if not (lower.startswith("(") and lower.endswith(")")):
                fail(rid, "4.3.1", "lower half is not wrapped in ( )")
            if CJK.search(lower):
                fail(rid, "4.3.1", "lower half contains CJK -- must be English")
            if len(upper.split()) > 50:
                fail(rid, "R-3", f"upper half {len(upper.split())} tokens > 50")
            head = rid.rsplit("-", 1)[0]
            lower_halves.setdefault(head, []).append(lower)

        # §11 formatting + §6 1:1
        for f in TEXT_FIELDS:
            v = tc.get(f, "")
            for line in v.split("\n"):
                if line != line.strip():
                    fail(rid, "11", f"{f}: leading/trailing whitespace {line!r}")
                if line.rstrip().endswith((".", "。")):
                    fail(rid, "11", f"{f}: trailing period {line!r}")
                if "[" in line or "]" in line:
                    fail(rid, "11", f"{f}: square bracket {line!r}")
                if re.search(r"(?<!\w)'[^']+'(?!\w)", line):
                    fail(rid, "11", f"{f}: single-quoted label {line!r}")

        proc = [l for l in tc.get("test_procedure", "").split("\n") if l.strip()]
        er = [l for l in tc.get("expected_result", "").split("\n") if l.strip()]
        if len(proc) < 2:                                        # §10.5
            fail(rid, "10.5", f"only {len(proc)} procedure step(s)")
        if len(proc) != len(er):                                 # §6
            fail(rid, "6", f"procedure {len(proc)} vs ER {len(er)} -- not 1:1")
        for l in proc + er:
            if not NUMBERED.match(l):
                fail(rid, "11", f"unnumbered item {l!r}")
        for l in er:                                             # §6 no modals
            if MODALS.search(l):
                fail(rid, "6", f"modal verb in ER {l!r}")

        ref = tc.get("specification_reference", "")
        if const is None:
            const = ref
        elif ref != const:                                       # R-BLM5
            fail(rid, "R-BLM5", "spec_reference differs from the batch constant")

    # §4.3 sibling distinction: lower halves unique within one heading
    for head, lows in lower_halves.items():
        if len(set(lows)) != len(lows):
            fail(head, "4.3.1", "sibling lower halves are not distinct")

    print(f"TC 數 {len(tcs)}")
    print(f"N 欄相異值數 {len({t['specification_reference'] for t in tcs})}"
          f"  (R-BLM5 預期 1)")
    print(f"priority 分布 {dict((p, sum(1 for t in tcs if t['priority'] == p)) for p in sorted({t['priority'] for t in tcs}))}")
    print(f"design_method 分布 {dict((m, sum(1 for t in tcs if t['design_method'] == m)) for m in sorted({t['design_method'] for t in tcs}))}")
    print(f"Input Test Data == NA 之比例 "
          f"{sum(1 for t in tcs if t['input_test_data'] == 'NA')}/{len(tcs)}")
    print()
    print("--- 機檢覆蓋之 §9 項次：1(部分) 2(部分) 4 5(部分) 10(計數) 13 14 15 16 ---")
    print("--- 機檢「不」覆蓋，留 pilot 人審：3 5(可執行性) 6 7 8 9 11 12 17 ---")
    print()
    if fails:
        print(f"FAIL {len(fails)}")
        for f in fails:
            print("  " + f)
        return 1
    print("機檢項全數 PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
