"""W-131（72 包 §6；承 71 包 §5 之 W-127＋W-128）—— R-VS67 之訊號名改寫。

R-VS67：訊號名、message、值域**一律取 LID `Atlantis High` 欄組**，
不依條文之架構標籤（R-VS19″ 已定該標籤為來源沿革）。

對映（LID `Atlantis High` 欄組逐字，`lid_pairs.tsv` 列 763／783／769／789／937）：

    TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm    → TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm
    TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm    → TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm
    TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm   → TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm
    TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm   → TELEMATIC_VEHICLE_SETUP3.FR_VS_Tlm
    TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm      → TELEMATIC_VEHICLE_SETUP3.HSW_Tlm

**五者皆為 1 bit**（`0 = Not_Pressed`／`1 = Pressed`）——
故 `= 2 (Heated_seat_medium)`／`= 3 (Heated_seat_high)` 之類斷言**無法成立**，
其為 **DR-15′ 之標的**，依 R-VS67(d) 逐條標 `dr15_exposed = yes`。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]

MAP = {
    "TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm": "TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm",
    "TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm": "TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm",
    "TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm": "TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm",
    "TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm": "TELEMATIC_VEHICLE_SETUP3.FR_VS_Tlm",
    "TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm": "TELEMATIC_VEHICLE_SETUP3.HSW_Tlm",
}
BIT = {"0": "Not_Pressed", "1": "Pressed"}
ASSERT = re.compile(r"(TELEMATIC_VEHICLE_SETUP3\.\w+_Tlm)\s*=\s*(\d+)\s*\(([^)]+)\)")


def latest():
    groups: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    return [(k, max(v)[0], max(v)[1]) for k, v in sorted(groups.items())]


def main() -> None:
    renames, broken = collections.Counter(), []
    ntc = 0
    for name, ver, path in latest():
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for tc in d["tcs"]:
            ntc += 1
            hit = False
            for k in ("test_procedure", "expected_result", "tc_title"):
                v = tc[k]
                for old, new in MAP.items():
                    if old in v:
                        v = v.replace(old, new)
                        renames[f"{old} → {new}"] += 1
                        hit = True
                tc[k] = v
            if not hit:
                continue
            changed = True
            # (3) 1 bit 訊號上之非 0/1 斷言 —— 無法成立
            bad = []
            for k in ("test_procedure", "expected_result"):
                for m in ASSERT.finditer(tc[k]):
                    if m.group(2) not in BIT or BIT[m.group(2)] != m.group(3):
                        bad.append(f"{m.group(1)} = {m.group(2)} ({m.group(3)})")
            if bad:
                tc["dr15_exposed"] = "yes"
                tc["remarks"] = ((str(tc.get("remarks", "")) + "；") if tc.get("remarks") else "") \
                    + ("BLOCKED: DR-15′ —— 改依 R-VS67 取 `*_Tlm`（1 bit，"
                       "`0 = Not_Pressed`／`1 = Pressed`），"
                       "而本列之斷言為四階值，其於 1 bit 訊號上無法成立")
                broken.append((name, tc["leaf_id"], sorted(set(bad))))
            tc["signal_source"] = "LID `Atlantis High` 欄組（R-VS67）"
        if changed:
            d["revision"] = ("W-131（46 輪）：依 R-VS67 將訊號名改取 LID "
                             "`Atlantis High` 欄組；1 bit 上無法成立之斷言標 "
                             "`dr15_exposed = yes`")
            (FEAT / "generated" / f"{name}_v{ver + 1}.json").write_text(
                json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"母體 {ntc} 條\n")
    print("## (2) 訊號名之改寫（原名 → 新名）\n")
    print("| 原名 | 新名 | 處數 |")
    print("|---|---|---:|")
    for k, n in sorted(renames.items(), key=lambda x: -x[1]):
        o, nw = k.split(" → ")
        print(f"| `{o}` | `{nw}` | {n} |")
    print(f"\n改寫合計 **{sum(renames.values())}** 處\n")
    print(f"## (3) 改寫後無法成立之斷言 —— **{len(broken)} 條**\n")
    print("| batch | leaf_id | 無法成立之斷言 |")
    print("|---|---|---|")
    for b, l, a in broken:
        print(f"| `{b}` | `{l}` | {'；'.join(f'`{x}`' for x in a)} |")


if __name__ == "__main__":
    main()
