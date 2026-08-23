"""W-133(4)（73 包 §5）—— 依 R-VS67′ 回復 44 條之斷言並標 `impl_gap`。

46 輪 W-131 依 R-VS67 將訊號名改取 `Atlantis High` 欄組之 `*_Tlm`（1 bit），
致四階斷言無法成立（44 條）。R-VS67′ 令**不能承載者取能承載之欄組**
（`Atlantis` → `*_Cmd_Tlm`，四階）並依 **R-VS66(a)** 標 `impl_gap`。

`dr15_exposed` 之標記**保留**（R-VS67′(a)）—— DR-15′ 之答覆仍可能改其形態。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]

BACK = {  # `Atlantis High`（1 bit）→ `Atlantis`（四階），R-VS67′(2)
    "TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm": "TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm",
    "TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm": "TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm",
    "TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm": "TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm",
    "TELEMATIC_VEHICLE_SETUP3.FR_VS_Tlm": "TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm",
    "TELEMATIC_VEHICLE_SETUP3.HSW_Tlm": "TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm",
}
BIT = {"0": "Not_Pressed", "1": "Pressed"}
ASSERT = re.compile(r"(TELEMATIC_VEHICLE_SETUP3?\.\w+_Tlm)\s*=\s*(\d+)\s*\(([^)]+)\)")


def latest():
    g: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            g[m.group(1)].append((int(m.group(2) or 1), f))
    return [(k, max(v)[0], max(v)[1]) for k, v in sorted(g.items())]


def main() -> None:
    rows, gap = [], 0
    for name, ver, path in latest():
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for tc in d["tcs"]:
            blob = tc["test_procedure"] + tc["expected_result"]
            # 只回復「四階斷言落在 1 bit 訊號上」者
            broken = [m for m in ASSERT.finditer(blob)
                      if m.group(1) in BACK
                      and (m.group(2) not in BIT or BIT[m.group(2)] != m.group(3))]
            if not broken:
                continue
            sigs = sorted({m.group(1) for m in broken})
            for k in ("test_procedure", "expected_result", "tc_title"):
                v = tc[k]
                for old, new in BACK.items():
                    v = v.replace(old, new)
                tc[k] = v
            tc["impl_gap"] = "；".join(BACK[s] for s in sigs)
            tc["signal_source"] = ("LID `Atlantis` 欄組（R-VS67′(2)：`Atlantis High` "
                                   "之 1 bit 承載不了四階語義）")
            tc["remarks"] = re.sub(r"BLOCKED: DR-15′[^；]*；?", "",
                                   str(tc.get("remarks", "")))
            tc["remarks"] = ((tc["remarks"] + "；") if tc["remarks"].strip("；") else "") \
                + (f"IMPL_GAP: {tc['impl_gap']} —— 依 R-VS66(a) 照寫，"
                   f"該訊號不在基線 DBC，開 issue 予 RD")
            tc["remarks"] = tc["remarks"].strip("；")
            gap += 1
            rows.append((name, tc["leaf_id"], sigs, tc.get("dr15_exposed")))
            changed = True
        if changed:
            d["revision"] = ("W-133(4)（47 輪）：依 R-VS67′ 取能承載之 `Atlantis` 欄組，"
                             "標 `impl_gap`（R-VS66(a)）；`dr15_exposed` 保留")
            (FEAT / "generated" / f"{name}_v{ver + 1}.json").write_text(
                json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"**回復並標 `impl_gap` 者：{gap} 條**\n")
    print("| batch | leaf_id | 回復之訊號 | `dr15_exposed` |")
    print("|---|---|---|---|")
    for b, l, s, e in rows:
        print(f"| `{b}` | `{l}` | {'；'.join(f'`{BACK[x]}`' for x in s)} | {e} |")


if __name__ == "__main__":
    main()
