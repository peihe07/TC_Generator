#!/usr/bin/env python3
"""T21a（下放包 15 §3.3）—— 非 P 代表值之傾印與取定。

`PT_SYSTEM_FD_1.GearEngagedForDisplay_PT` 之 `VAL_` **全列舉傾印**
（前輪僅確認含 `12 "Park"`）。

取值原則：037 書 `<> [P]` 為一**類**，類內任一成員皆合法；
**取行車常態檔位**為代表。**不掛 marker**（類內取樣非假設）。

唯讀。
"""
import re
from pathlib import Path

VS = Path(__file__).resolve().parent.parent.parent / "vehicle_setting" / "inputs"
DBC = VS / "PDT27_E2A_R5_FDCAN8.dbc"
MSG, SIG = "PT_SYSTEM_FD_1", "GearEngagedForDisplay_PT"


def main():
    txt = DBC.read_text("utf-8", errors="replace")
    bo = re.search(rf"^BO_ (\d+) {MSG}\b[^\n]*$", txt, re.M)
    assert bo, MSG
    mid = bo.group(1)
    blk = re.search(rf"^BO_ {mid} {MSG}\b[^\n]*\n((?:\s*SG_[^\n]*\n)*)", txt, re.M)
    sg = next(l.strip() for l in blk.group(1).splitlines()
              if re.match(rf"\s*SG_\s+{SIG}\b", l))
    vals = []
    for m in re.finditer(rf"^VAL_\s+{mid}\s+{SIG}\s+(.*);\s*$", txt, re.M):
        vals = [(int(k), v) for k, v in re.findall(r'(\d+)\s+"([^"]*)"', m.group(1))]

    print("=" * 74)
    print("T21a —— `%s.%s` 之 VAL_ 全列舉" % (MSG, SIG))
    print("=" * 74)
    print("DBC :", DBC.name)
    print("BO_ :", "id=%s (0x%X)" % (mid, int(mid)))
    print("SG_ :", sg)
    print("\nVAL_ 全列舉（**逐字**，共 %d 項）：" % len(vals))
    for k, v in sorted(vals):
        print("   %2d = %r" % (k, v))

    named = {k for k, _ in vals}
    span = set(range(0, 32))
    print("\n值域 [0|31] 中**未列舉**之 raw：", sorted(span - named))

    park = [(k, v) for k, v in vals if v == "Park"]
    print("\nP 檔（037 之 `[P]`）：", park, "→ 前輪所確認者")

    # 非 P 之候選分類（**只分類，不下結論**）
    drive_like = [(k, v) for k, v in vals
                  if re.fullmatch(r"Gear_\d+(st|nd|rd|th)?|Drive|Low|Manual|Sport_Mode", v)]
    other = [(k, v) for k, v in vals
             if v not in ("Park",) and (k, v) not in drive_like]
    print("\n非 P 之全部成員（%d 項）：" % (len(vals) - len(park)))
    print("  行車檔位類（%d）：" % len(drive_like), drive_like)
    print("  其他（%d）：" % len(other), other)

    print("\n" + "-" * 74)
    print("取定")
    print("-" * 74)
    print("""  取 **15 = 'Drive'** 為非 P 之代表。

  取法（reasoning 將逐字載明）：
  (1) 037 `-127`／`-129` 書 `$PresentGear$ <> [P]`，其為一**類**而非特定值；
      類內任一成員皆滿足該條件（同取樣 feature 之理）。
  (2) 於非 P 之成員中取**行車常態檔位**：`15 = 'Drive'` 為 DBC `VAL_` 逐字，
      且為自排車行進之常態選擇 —— 較 `Gear_1st`~`Gear_9th`（特定檔位）
      與 `Low`／`Manual`／`Sport_Mode`（特殊模式）更接近常態。
  (3) `0 = 'Initialize'` 與 `31 = 'SNA'` **不取** —— 前者為初始化態、
      後者為訊號不可用，二者皆非「已選定之非 P 檔位」，
      取之會把「檔位非 P」與「檔位未知」混為一談。
  (4) `13 = 'Neutral'`／`14 = 'Reverse'` 雖亦非 P 且為真實檔位，
      **未取但併記** —— 類內取樣，非唯一解。

  **不掛 marker**（下放包 §3.3 明文：類內取樣非假設）。""")


if __name__ == "__main__":
    main()
