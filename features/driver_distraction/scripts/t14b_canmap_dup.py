#!/usr/bin/env python3
"""T14b（下放包 09 §五）—— pilot 前置閘。

`LID CAN Mapping` 分頁之重複 Logical Identifier 掃描（母體判準比照 T13a），
**特別確認 `Speedometer` 與 `PresentGear` 是否唯一**。
非唯一即逐列全欄傾印並停止 pilot（r420／r421 同型失效模式）。

引用格式依 R-DD10：Excel 欄名、LID 列標架構欄、計數書母體判準、列號 1-based。
"""
import re
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
LID = ROOT.parent / "vehicle_setting" / "inputs" / "Logical Identifiers and CAN Mapping v1_76.xlsx"
SHEET = "CAN Mapping"
WATCH = ["Speedometer", "PresentGear"]
CITED = {1738: "Speedometer", 1397: "PresentGear"}   # 下放包 09 §四-4


def cn(j):
    s, j = "", j + 1
    while j:
        j, r = divmod(j - 1, 26)
        s = chr(65 + r) + s
    return s


def main():
    wb = openpyxl.load_workbook(LID, read_only=True, data_only=True)
    rows = [list(r) for r in wb[SHEET].iter_rows(values_only=True)]
    wb.close()

    # 架構帶與欄名：比照 T13a，自 r2／r3 讀取，不硬編
    bands = {j: str(v).strip() for j, v in enumerate(rows[1]) if v not in (None, "")}
    names = [str(v) if v is not None else "" for v in rows[2]]

    def band_of(j):
        cur = None
        for s in sorted(bands):
            if j >= s:
                cur = bands[s]
        return cur

    print("=" * 72)
    print(f"T14b —— LID `{SHEET}` 重複 Logical Identifier 掃描")
    print(f"母體判準：r4 起至 r{len(rows)}（r1 表題／r2 架構帶／r3 欄名，排除）；")
    print("          A 欄 `Logical Identifier` 非空者計入；空白列排除。")
    print("架構帶（自 r2 讀取）：" + "／".join(f"{cn(j)}={v}" for j, v in sorted(bands.items())))

    groups = defaultdict(list)
    for i, row in enumerate(rows[3:], 4):
        if row[0] not in (None, ""):
            groups[str(row[0])].append(i)
    total = sum(len(v) for v in groups.values())
    dups = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"\n非空 Logical Identifier 列數 = {total}；unique = {len(groups)}；"
          f"重複之 LID 名 = {len(dups)}，佔 {sum(len(v) for v in dups.values())} 列")
    if dups:
        dist = defaultdict(int)
        for v in dups.values():
            dist[len(v)] += 1
        print("重複組之列數分布：" + "／".join(f"{k} 列 × {dist[k]} 組" for k in sorted(dist)))

    # === 閘：二訊號之唯一性 ===
    print("\n" + "-" * 72)
    print("閘 —— `Speedometer` 與 `PresentGear` 之唯一性")
    verdict = True
    for w in WATCH:
        exact = groups.get(w, [])
        # 另查「含該字串但非完全相等」者，避免只看完全相等而漏掉變體
        near = sorted({i for i, row in enumerate(rows[3:], 4)
                       if row[0] not in (None, "")
                       and w.lower() in str(row[0]).lower()
                       and str(row[0]) != w})
        ok = len(exact) == 1
        verdict &= ok
        print(f"\n  [{w}] 完全相等之列：{exact or '（無）'} → "
              f"{'唯一 ✓' if ok else '**非唯一 ✗**' if len(exact) > 1 else '**查無 ✗**'}")
        if near:
            print(f"      含該字串但不相等之 A 欄值（量測，非代換）：")
            for i in near:
                print(f"        r{i} A = {rows[i-1][0]!r}")
        else:
            print(f"      含該字串但不相等者：無")

    # === 下放包所引之列，回頭核 A 欄（§九 之 ACV_FailType 案例）===
    print("\n" + "-" * 72)
    print("下放包 09 §四-4 所引之列 —— 回核其 A 欄 `Logical Identifier`")
    for r, want in CITED.items():
        got = rows[r - 1][0] if r <= len(rows) else None
        print(f"  r{r}: A = {got!r}  期待 {want!r} → {'相符 ✓' if str(got) == want else '**不符 ✗**'}")
        verdict &= (str(got) == want)

    # === 二訊號所在列之全欄傾印（無論通過與否都印，供 profile 覆核）===
    print("\n" + "-" * 72)
    print("二訊號所在列之全欄逐字")
    for w in WATCH:
        for i in groups.get(w, []):
            print(f"\n-- [{w}] r{i}")
            for j, v in enumerate(rows[i - 1]):
                if v not in (None, ""):
                    nm = names[j] if j < len(names) else "?"
                    print(f"   {cn(j):>3} [{band_of(j)} 帶 · {nm}] = {v!r}")

    print("\n" + "=" * 72)
    print("T14b 判定：" + ("**清白 —— pilot 得開**" if verdict
                          else "**不清白 —— 停止 pilot，回報待裁**"))
    return 0 if verdict else 1


if __name__ == "__main__":
    raise SystemExit(main())
