"""VF230：DBC 解析器（W-VF84；R-VF127 之 DBC 換本所需）。

**其所以須新寫**：`data/_dbc_parsed.json` 為快取，**而其產生腳本不在 repo**
（W-VF77 已具名）。`R-VF127` 令改引 `forms/` 之二本，
**而無解析器則換本無從施行** —— 故本檔為該條之載體。

**其正確性之驗證方式（R-VF92 一：獨立確認）**：
以本解析器重建**舊二本**之結構，與現行 `_dbc_parsed.json` 逐鍵比對；
**全等方採信其對新二本之解析**。不全等即停 —— 其表示本解析器與原產生者不等價。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
ROOT = FEAT.parents[1]

BO = re.compile(r"^BO_\s+(\d+)\s+(\S+?)\s*:\s*(\d+)\s+(\S+)", re.M)
SG = re.compile(
    r"^\s*SG_\s+(\S+)\s*(?:M|m\d+)?\s*:\s*(\d+)\|(\d+)@(\d)([-+])\s*"
    r"\(([^,]+),([^)]+)\)\s*\[[^\]]*\]\s*\"([^\"]*)\"", re.M)
VAL = re.compile(r'^VAL_\s+(\d+)\s+(\S+)\s+(.*?);\s*$', re.M)
PAIR = re.compile(r'(-?\d+)\s+"([^"]*)"')


# ---- 與原產生者對齊：剝除度數符號 `°` ----
# **自驗攔下之差異全為 `°`**（`°C`／`°F` vs `C`／`F`）：
# 89 個訊號（`Temp_Unit`／`HVBatModuleTemp_*` 等）之 `unit`／`vals` 有此差。
# **DBC 為 ISO-8859，以 latin-1 讀則 `°` 逐字保留**；而現行快取無之
# —— 即**原產生者剝除了它**。
# **本層不自行判定何者為對** —— 其對現行 438 條之產出**零影響**
# （89 個有異之訊號，438 條一個都沒用到；產出中無任何 `°`）。
# **故取「與原產生者對齊」以使自驗可全等**，並以本註記與 `DEG_ANCHORS`
# 固定其行為 —— **不使其成為一個隱形之假定**。
# 若日後之條文觸及該 89 個訊號之任一，**其單位之逐字形須先裁定**。
DEG = re.compile("[\u00b0\ufffd]")


def _deg(s: str) -> str:
    return DEG.sub("", s)


DEG_ANCHORS = [("\u00b0C", "C", "度數符號須剝除（與原產生者對齊）"),
               ("C", "C", "**假陽之防**：無 `\u00b0` 者不得改動"),
               ("\u00b0F", "F", "另一單位之同型"),
               ("Not_Used", "Not_Used", "**假陽之防**：一般標籤不受影響")]


def verify_deg() -> None:
    bad = [k for a, b, k in DEG_ANCHORS if _deg(a) != b]
    for a, b, k in DEG_ANCHORS:
        print(f"  {'✅' if _deg(a) == b else '❌'} {k}：{a!r} → {_deg(a)!r}（期望 {b!r}）")
    if bad:
        raise SystemExit("`°` 剝除之錨點不符，停")


def parse(path: Path) -> dict:
    txt = path.read_text(encoding="latin-1", errors="replace")
    msgs, sigs, vals = {}, {}, {}
    cur = None
    for line in txt.splitlines():
        m = BO.match(line)
        if m:
            cur = (int(m.group(1)), m.group(2))
            msgs[m.group(2)] = {"id": int(m.group(1)), "dlc": int(m.group(3)),
                                "tx": m.group(4)}
            continue
        s = SG.match(line)
        if s and cur:
            sigs.setdefault(s.group(1), []).append({
                "msg": cur[1], "msg_id": cur[0], "start": int(s.group(2)),
                "length": int(s.group(3)), "order": s.group(4), "sign": s.group(5),
                "factor": s.group(6).strip(), "offset": s.group(7).strip(),
                "unit": _deg(s.group(8))})
            continue
        if not line.strip():
            cur = None
    for m in VAL.finditer(txt):
        d = {r: _deg(lab) for r, lab in PAIR.findall(m.group(3))}
        if d:
            vals.setdefault(m.group(2), {}).update(d)
    return {"msgs": msgs, "sigs": sigs, "vals": vals}


def build(files: list[Path]) -> dict:
    return {f.name: parse(f) for f in files}


def main() -> None:
    args = sys.argv[1:]
    old = [FEAT / "inputs" / n for n in
           ("PDT27_E2A_R4_BHCAN.dbc", "PDT27_E2A_R5_FDCAN8.dbc")]
    new = [ROOT / "forms" / n for n in
           ("PDT27_E2A_R1_BHCAN2.dbc", "PDT27_E2A_R1_FDCAN8.dbc")]

    # ---- 自驗：以本解析器重建舊二本，與現行快取逐鍵比對 ----
    cur = json.loads((FEAT / "data/_dbc_parsed.json").read_text())
    mine = build(old)
    ok = True
    print("=== `\u00b0` 剝除之錨點 ===")
    verify_deg()
    print("\n=== 自驗（R-VF92 一）：本解析器 vs 現行快取（舊二本）===")
    for k in sorted(set(cur) | set(mine)):
        if k not in cur or k not in mine:
            print(f"  ❌ {k}: 僅一側有"); ok = False; continue
        for sub in ("sigs", "vals"):
            a, b = cur[k].get(sub, {}), mine[k].get(sub, {})
            same = a == b
            print(f"  {'✅' if same else '❌'} {k[:26]:28} {sub:5} "
                  f"{len(a):>5} vs {len(b):>5}  {'全等' if same else '**不等**'}")
            if not same:
                ok = False
                da = set(a) - set(b)
                db = set(b) - set(a)
                print(f"       僅快取有 {len(da)}：{sorted(da)[:4]}")
                print(f"       僅本檔有 {len(db)}：{sorted(db)[:4]}")
                diff = [x for x in set(a) & set(b) if a[x] != b[x]]
                print(f"       同鍵而值異 {len(diff)}：{diff[:4]}")
    if not ok:
        raise SystemExit("**自驗不等 —— 本解析器與原產生者不等價，停。**"
                         "不得以其解析新二本。")
    print("\n**自驗全等，得據以解析新二本。**")

    if "--write" in args:
        out = build(new)
        (FEAT / "data/_dbc_parsed_new.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\n新二本 → data/_dbc_parsed_new.json")
        for k, v in out.items():
            print(f"  {k[:34]:36} sigs {len(v['sigs']):>5}｜vals {len(v['vals']):>5}")


if __name__ == "__main__":
    main()
