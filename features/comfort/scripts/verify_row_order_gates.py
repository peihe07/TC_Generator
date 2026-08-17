#!/usr/bin/env python3
"""96 §6 之三道 gate 之反向驗證。

96 §6 立三道，並要求「三者皆須反向驗證」：

    row-order-by-reqid   D 欄自上而下須為 037 之 leaf 序，不符即指名首個逆序之列
    all-leaves-present   037 之 403 個 leaf 每一個皆須於該欄出現至少一次
    blank-row-shape      留空列除 D 欄外各欄皆須為空

**一道只會通過的檢查證明不了任何事**（R-C41 之同一理由）：三道現皆綠，
而綠燈只在「它會為壞資料轉紅」時才有意義。本檔對每一道各注入一個壞資料，
斷言它轉紅；再以乾淨資料斷言它轉綠。

**注入之對象是 gate 之判準函式，不是產出檔** —— 產出檔由 `xlsx_surgical.py`
單一路徑寫出（R18-3），不得為了測試而繞過它。故本檔把 `write_back` 之
判準各抽成一個純函式，兩邊共用同一段邏輯：**測到的與跑到的是同一個判準。**

`all-leaves-present` 之必要性由語料自證（96 §6）：交付前之覆蓋率
（383 / 403、434 / 403…）**來自我方之統計，不來自交付物本身** ——
從來沒有一道檢查問過「403 個是不是都在表上」。

Usage:
    python3 features/comfort/scripts/verify_row_order_gates.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_back as W


# --- 三道 gate 之判準，抽為純函式（write_back §3.3 讀回產出檔後套用同一組）--
def g_row_order(col_d: list) -> str:
    """回傳首個**倒退**之列之描述；無則 None。

    判準為 `<` 而非 `<=`：一個 leaf 拆出多條 TC 時，那幾列之 D 欄相同，
    那是規則所要的形態，不是違規。
    """
    for i in range(1, len(col_d)):
        if W.leaf_sort_key(col_d[i]) < W.leaf_sort_key(col_d[i - 1]):
            return f"row{W.FIRST_ROW + i}: {col_d[i]} 在 {col_d[i - 1]} 之後"
    return None


def g_all_leaves(col_d: list, universe: list) -> list:
    return sorted(set(universe) - set(col_d), key=W.leaf_sort_key)


def g_blank_shape(rows: list) -> list:
    """rows：[(是否留空列, {欄: 值})]，回傳違規之欄。"""
    bad = []
    for i, (is_blank, cells) in enumerate(rows):
        if not is_blank:
            continue
        for col, v in cells.items():
            if col != "D" and v not in (None, ""):
                bad.append(f"row{W.FIRST_ROW + i}.{col}")
    return bad


def main() -> int:
    ok = True

    def case(name, fired, expected):
        nonlocal ok
        p = bool(fired) == expected
        ok &= p
        print(f"  {'PASS' if p else '**FAIL**'} — {name}: "
              f"fired={bool(fired)}, expected={expected}")

    plan = W.row_plan(W.load_tcs())
    universe = W.leaf_universe()
    col_d = [r["req_id"] for r in plan]

    print("## row-order-by-reqid\n")
    case("乾淨之列序 -> 不觸發", g_row_order(col_d), False)
    swapped = col_d[:]
    swapped[3], swapped[4] = swapped[4], swapped[3]
    case("相鄰兩列對調 -> 觸發", g_row_order(swapped), True)
    batch_order = sorted(col_d, key=lambda r: r[-2:])   # 一個非 leaf 序之排法
    case("依批次順序（現行 434 列之排法）-> 觸發",
         g_row_order(batch_order), True)
    # 同一 leaf 之多條 TC 佔連續數列 —— 這是規則所要的形態，不得觸發。
    # 第一版之判準寫 `<=`，此向即是抓出它的那一向。
    runs = [i for i in range(1, len(col_d)) if col_d[i] == col_d[i - 1]]
    case(f"同一 leaf 之多條 TC 佔連續列（實測 {len(runs)} 處）-> 不觸發",
         g_row_order(col_d), False)
    dup = col_d[:]
    dup[40] = dup[3]          # 一個早先之 leaf 再度出現於後方 -> 其後即倒退
    case("同一 leaf 於他處再現（非連續）-> 觸發", g_row_order(dup), True)
    print(f"  首個逆序之列可具名：{g_row_order(swapped)}\n")

    print("## all-leaves-present\n")
    case("403 leaf 全在 -> 不觸發", g_all_leaves(col_d, universe), False)
    case("抽掉留空列之 leaf（即 96 之前之做法）-> 觸發",
         g_all_leaves([d for d in col_d if d != "SWE1-HVAC-019-03"], universe),
         True)
    case("抽掉任一有 TC 之 leaf -> 觸發",
         g_all_leaves([d for d in col_d if d != "SWE1-HVAC-001-01"], universe),
         True)
    missing20 = [d for d in col_d if d not in {
        "SWE1-HVAC-016-01", "SWE1-HVAC-018-01", "SWE1-HVAC-039",
        "SWE1-HVAC-099", "SWE1-HVAC-129-01"}]
    case("抽掉本包補產之五個 leaf -> 觸發（且具名）",
         g_all_leaves(missing20, universe), True)
    print(f"  具名之缺者：{g_all_leaves(missing20, universe)}\n")

    print("## blank-row-shape\n")
    clean = [(bool(r.get(W.BLANK)),
              {"D": r["req_id"], "F": "", "I": "", "L": "", "AH": ""})
             for r in plan]
    case("留空列僅 D 有值 -> 不觸發", g_blank_shape(clean), False)
    dirty = [(b, dict(c)) for b, c in clean]
    idx = next(i for i, (b, _) in enumerate(dirty) if b)
    dirty[idx][1]["I"] = "something"
    case("留空列之 I 欄有值 -> 觸發", g_blank_shape(dirty), True)
    dirty2 = [(b, dict(c)) for b, c in clean]
    dirty2[idx][1]["F"] = "NR1L-ComfortHMI-999"
    case("留空列被發了一個 tc_id -> 觸發", g_blank_shape(dirty2), True)
    nonblank = [(False, dict(c)) for _, c in dirty]
    case("同樣髒之列若不是留空列 -> 不觸發（本道只管留空列）",
         g_blank_shape(nonblank), False)

    n = 13
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"live plan: {len(plan)} 列 = "
          f"{sum(1 for r in plan if not r.get(W.BLANK))} TC ＋ "
          f"{sum(1 for r in plan if r.get(W.BLANK))} 留空列；"
          f"037 leaf {len(universe)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
