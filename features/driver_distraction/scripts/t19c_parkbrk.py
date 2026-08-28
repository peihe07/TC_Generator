#!/usr/bin/env python3
"""T19c（下放包 13 §七）—— `LID CAN Mapping r1310` 全列傾印與 DBC 驗證。

(1) 回核 A 欄 `Logical Identifier` = `PARK_BRK_EDG`（R-DD18(b) 明文：
    施加名之 CAN 對應仍須自 LID 該列實測查得，不因勘誤成立而略過查證）
(2) 全列逐欄傾印，欄名依 R-DD10(a) 書 Excel 欄名，架構帶自 r2 讀取
(3) 取 **Atlantis High 欄**之訊號名（R-DD6 v2(a)(b)），對二 DBC 驗存在性
(4) `VAL_` 逐字（R-DD9(a)）

唯讀。**profile §3 之 PARK_BRK 列由分析層回填，本檔不寫 profile。**
"""
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
VS = ROOT.parent / "vehicle_setting" / "inputs"
LID = VS / "Logical Identifiers and CAN Mapping v1_76.xlsx"
DBC = [VS / "PDT27_E2A_R4_BHCAN.dbc", VS / "PDT27_E2A_R5_FDCAN8.dbc"]
SHEET, ROW = "CAN Mapping", 1310
EXPECT = "PARK_BRK_EDG"


def cn(j):
    s, j = "", j + 1
    while j:
        j, r = divmod(j - 1, 26)
        s = chr(65 + r) + s
    return s


def dbc_probe(qualified):
    """`MESSAGE.Signal` → 於二 DBC 驗 BO_／SG_ 存在性與 VAL_ 逐字。"""
    msg, sig = qualified.split(".", 1)
    out = []
    for p in DBC:
        txt = p.read_text("utf-8", errors="replace")
        bo = re.search(rf"^BO_ (\d+) {re.escape(msg)}\b[^\n]*$", txt, re.M)
        sg = None
        if bo:
            blk = re.search(rf"^BO_ {bo.group(1)} {re.escape(msg)}\b[^\n]*\n"
                            rf"((?:\s*SG_[^\n]*\n)*)", txt, re.M)
            if blk:
                for l in blk.group(1).splitlines():
                    if re.match(rf"\s*SG_\s+{re.escape(sig)}\b", l):
                        sg = l.strip()
        vals = []
        if bo:
            for m in re.finditer(rf"^VAL_\s+{bo.group(1)}\s+{re.escape(sig)}\s+(.*);\s*$",
                                 txt, re.M):
                vals = re.findall(r'(\d+)\s+"([^"]*)"', m.group(1))
        out.append((p.name, bo, sg, vals))
    return out


def main():
    wb = openpyxl.load_workbook(LID, read_only=True, data_only=True)
    rows = [list(r) for r in wb[SHEET].iter_rows(values_only=True)]
    wb.close()
    bands = {j: str(v).strip() for j, v in enumerate(rows[1]) if v not in (None, "")}
    names = [str(v) if v is not None else "" for v in rows[2]]

    def band(j):
        cur = None
        for s in sorted(bands):
            if j >= s:
                cur = bands[s]
        return cur

    row = rows[ROW - 1]
    print("=" * 78)
    print(f"T19c —— `LID {SHEET} r{ROW}`")
    print("=" * 78)
    print("架構帶（自 r2 讀取）：" + "／".join(f"{cn(j)}={v}" for j, v in sorted(bands.items())))

    got = str(row[0])
    ok_a = (got == EXPECT)
    print(f"\n[回核] A 欄 `Logical Identifier` = {got!r}　期待 {EXPECT!r}　"
          f"→ {'相符 ✓' if ok_a else '**不符 ✗**'}")

    # 唯一性（同 T14b 之閘）
    hits = [i for i, r in enumerate(rows[3:], 4)
            if r[0] not in (None, "") and str(r[0]) == EXPECT]
    near = sorted({str(r[0]) for r in rows[3:]
                   if r[0] not in (None, "") and "park_brk" in str(r[0]).lower()
                   and str(r[0]) != EXPECT})
    print(f"[回核] `{EXPECT}` 完全相等之列：{hits} → "
          f"{'唯一 ✓' if len(hits) == 1 else '**非唯一 ✗**'}")
    print(f"[回核] 含 `PARK_BRK` 而不等於 `{EXPECT}` 之 A 欄值：{near or '無'}")

    print(f"\n-- r{ROW} 全欄逐字")
    for j, v in enumerate(row):
        if v not in (None, ""):
            nm = names[j] if j < len(names) else "?"
            print(f"   {cn(j):>3} [{band(j)} 帶 · {nm}] = {v!r}")

    # Atlantis High 欄之訊號名（R-DD6 v2(a)(b)）
    zi = next(j for j, v in bands.items() if v == "Atlantis High")
    pi = next(j for j, v in bands.items() if v == "Atlantis")
    ah, at = row[zi], row[pi]
    print(f"\n[取欄] Atlantis 欄（{cn(pi)}）= {at!r}")
    print(f"[取欄] Atlantis High 欄（{cn(zi)}）= {ah!r}")
    print(f"       二欄{'同字 → R-DD6 v2(b) 無差別' if str(at) == str(ah) else '不同字 → 取 Atlantis High'}")

    cands = [x.strip() for x in re.split(r"[\n\r]+", str(ah)) if x.strip()]
    print(f"[取欄] Atlantis High 欄所載之名：{cands}"
          + ("　（一格多名 → R-DD13）" if len(cands) > 1 else ""))

    print("\n" + "-" * 78)
    print("DBC 驗證（存在性 ＋ VAL_ 逐字）")
    print("-" * 78)
    ok_dbc = False
    for c in cands:
        print(f"\n候選 `{c}`")
        if "." not in c:
            print("   （非 `MESSAGE.Signal` 形，略）")
            continue
        for fn, bo, sg, vals in dbc_probe(c):
            if bo:
                print(f"   [{fn}] BO_ id={bo.group(1)} ✓")
                print(f"        SG_ : {sg if sg else '**該訊息內無此 SG_ ✗**'}")
                if sg:
                    ok_dbc = True
                print(f"        VAL_: {vals if vals else '（無列舉）'}")
                for k, v in vals:
                    print(f"              {k} = {v!r}")
            else:
                print(f"   [{fn}] BO_ `{c.split('.')[0]}` **不在** ✗")
    print("\n" + "=" * 78)
    print(f"T19c 判定：A 欄回核 {'✓' if ok_a else '✗'}／"
          f"Atlantis High 名於綁定 DBC {'查得 ✓' if ok_dbc else '**查無 ✗**'}")
    print("**profile §3 之 PARK_BRK 列由分析層回填；本檔不寫 profile。**")


if __name__ == "__main__":
    main()
