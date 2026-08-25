#!/usr/bin/env python3
"""LID v1.78 vs v1.76 diff on the Atlantis High column group (handoff 05 step 7).

v1_76 lives in features/vehicle_setting/inputs/ and is READ ONLY here — it is
opened, never written, never moved (handoff 05 step 7).

Comparison face: sheet `CAN Mapping`, `Atlantis High` group's `Signal Name`,
keyed by the `Logical Identifier` column. Both files locate the group from
their OWN r2/r3 rows rather than assuming a fixed column index — the two
versions need not lay out identically.

Values are compared after whitespace normalisation of each newline-separated
entry, as an ORDERED-INSENSITIVE SET: a cell holding several MESSAGE.Signal
values is the same content regardless of the order they are written in.
Nothing is compared by similarity.
"""
from pathlib import Path

import openpyxl

from tsv_meta import write_meta

ROOT = Path(__file__).resolve().parents[3]
V178 = ROOT / "forms" / "Logical Identifiers and CAN Mapping v1_78.xlsx"
V176 = (ROOT / "features" / "vehicle_setting" / "inputs"
        / "Logical Identifiers and CAN Mapping v1_76.xlsx")


def norm(s):
    return " ".join(str(s or "").split())


def load(path):
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    grid = [list(r) for r in wb["CAN Mapping"].iter_rows(values_only=True)]
    wb.close()
    groups = {norm(v): i for i, v in enumerate(grid[1]) if v is not None}
    labels = [norm(v) for v in grid[2]]
    ah = groups["Atlantis High"]
    assert labels[ah] == "Signal Name", labels[ah]
    out = {}
    for i, r in enumerate(grid[3:], start=4):
        k = norm(r[0])
        if not k:
            continue
        cell = str(r[ah] or "") if len(r) > ah else ""
        vals = frozenset(norm(x) for x in cell.splitlines() if x.strip())
        out.setdefault(k, []).append((i, vals, norm(r[ah + 1])
                                      if len(r) > ah + 1 else ""))
    return grid, groups, labels, out


def _verify_bindings():
    """R-G23: refuse to measure against unbound reference material.

    Every figure this script produces is only as true as the DBC/LID/PROXI
    revision it was computed from. Checking at the entry point means a
    swapped file stops the run instead of quietly changing the numbers.
    """
    import subprocess
    import sys as _sys
    r = subprocess.run(
        [_sys.executable, str(Path(__file__).with_name(
            "verify_reference_binding.py"))],
        capture_output=True, text=True)
    if r.returncode != 0:
        _sys.stderr.write(r.stdout + r.stderr)
        _sys.exit("reference binding check FAILED — refusing to run "
                  "(R-G23). Do not update the declared sha256; report it.")


def main():
    _verify_bindings()
    g8, gr8, lb8, a = load(V178)
    g6, gr6, lb6, b = load(V176)
    print("# LID v1.78 vs v1.76 — Atlantis High `Signal Name` 比對")
    print(f"v1_78: {V178}")
    print(f"       CAN Mapping {len(g8)} 列；Atlantis High 起於 c{gr8['Atlantis High'] + 1}"
          f"；資料列 {sum(len(v) for v in a.values())}；相異 LID {len(a)}")
    print(f"v1_76: {V176}")
    print(f"       CAN Mapping {len(g6)} 列；Atlantis High 起於 c{gr6['Atlantis High'] + 1}"
          f"；資料列 {sum(len(v) for v in b.values())}；相異 LID {len(b)}")
    print(f"v1_78 架構分組: {sorted(gr8, key=gr8.get)}")
    print(f"v1_76 架構分組: {sorted(gr6, key=gr6.get)}")

    both = set(a) & set(b)
    only8, only6 = set(a) - set(b), set(b) - set(a)
    same = [k for k in both if {v for _, v, _ in a[k]} == {v for _, v, _ in b[k]}]
    diff = sorted(both - set(same))
    print()
    print("## 三分（以 Logical Identifier 為鍵，Signal Name 為值）")
    print(f"  皆有且 Signal Name 相同 : {len(same)}")
    print(f"  皆有但 Signal Name 不同 : **{len(diff)}**")
    print(f"  僅 v1_78 有             : {len(only8)}")
    print(f"  僅 v1_76 有             : {len(only6)}")

    print()
    print("## Signal Name 相異者 —— 逐筆")
    if not diff:
        print("  （無）")
    for k in diff:
        va = sorted(x for _, v, _ in a[k] for x in v)
        vb = sorted(x for _, v, _ in b[k] for x in v)
        print(f"\n### {k}")
        print(f"  v1_78 (r{','.join(str(i) for i, _, _ in a[k])}): {va or '（空）'}")
        print(f"  v1_76 (r{','.join(str(i) for i, _, _ in b[k])}): {vb or '（空）'}")
        print(f"  僅 v1_78: {sorted(set(va) - set(vb)) or '—'}")
        print(f"  僅 v1_76: {sorted(set(vb) - set(va)) or '—'}")

    print()
    print("## 本 feature 之 15 個 $Signal$ 在兩版之一致性")
    sigs = ['Back_Button', 'CCDMF_RQ_DISP_INTS', 'CM_TCH_STAT',
            'DCSD_DISP_STAT', 'Enter_Button', 'ICSMuteButton',
            'ICSPowerButton', 'ICSScreenOffButton', 'ICS_KNOB1_DIR',
            'ICS_KNOB1_VAL', 'ICS_KNOB2_DIR', 'ICS_KNOB2_VAL',
            'RQ_DISP_INTS', 'TGW_DISP_STAT', 'Telematic_Power']
    for s in sigs:
        if s in diff:
            state = "**相異**"
        elif s in same:
            state = "相同"
        elif s in only8:
            state = "僅 v1_78 有"
        elif s in only6:
            state = "僅 v1_76 有"
        else:
            state = "兩版皆無"
        print(f"  {s}: {state}")
    hit = [s for s in sigs if s in diff]
    print(f"\n  -> 本 feature 受影響之訊號: {hit or '無'}")

    out = ROOT / "features" / "display" / "data" / "lid_v178_vs_v176.tsv"
    with out.open("w", encoding="utf-8") as fh:
        fh.write("logical_identifier\tverdict\tv178_rows\tv178_signal_names\t"
                 "v176_rows\tv176_signal_names\n")
        for k in sorted(set(a) | set(b)):
            if k in diff:
                verdict = "DIFFERENT"
            elif k in same:
                verdict = "SAME"
            elif k in only8:
                verdict = "ONLY_v178"
            else:
                verdict = "ONLY_v176"
            fh.write("\t".join([
                k, verdict,
                " ¦ ".join(str(i) for i, _, _ in a.get(k, [])),
                " ¦ ".join(sorted(x for _, v, _ in a.get(k, []) for x in v)),
                " ¦ ".join(str(i) for i, _, _ in b.get(k, [])),
                " ¦ ".join(sorted(x for _, v, _ in b.get(k, []) for x in v)),
            ]) + "\n")
    write_meta(out, ["logical_identifier", "verdict", "v178_rows", "v178_signal_names", "v176_rows", "v176_signal_names"], len(set(a) | set(b)),
               generated_by="features/display/scripts/lid_version_diff.py",
               rulings=["R-G15"],
               measurement_conditions="比對面＝CAN Mapping 之 Atlantis High Signal Name，鍵為 Logical Identifier；多值以 frozenset 比對（順序無關）",
               notes="v1_76 全程唯讀，未搬動。")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
