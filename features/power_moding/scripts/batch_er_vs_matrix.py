#!/usr/bin/env python3
"""23 包步驟 5 —— batch 1 之**逐條 ER 斷言** × 規範性素材／規格他處。

22 §12 第 6 項（執行層自陳）：ch 7 × 矩陣之 30 列判定為**章**層，
**不等於逐條 TC 之 ER 都被對照過**。

本檔以 **ER 斷言**為單位：對 `generated/batch01.json` 之每一條 TC 之
每一行 `expected_result`，逐一具名其與 State Matrix 某格或規格他處之關係，
記法依 **R-PMH79**（牴觸／印證／未對照）＋ **R-PMH84**（條件互斥須被證明）。

**每一 ER 斷言皆須於 `ER_VERDICT` 具名**，未具名 → FAIL。
**發現任一牴觸 → 退出碼 1**（23 包停止條件 7）。

用法:
    python scripts/batch_er_vs_matrix.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH = ROOT / "generated" / "batch01.json"

LIMITS = [
    "**只對照 `expected_result`** —— `pre_conditions` 與 `test_procedure` 之斷言不入母體",
    "**謂詞之認定為人工** —— `ER_VERDICT` 逐條具名，本檢查只驗其存在，不驗其正確",
    "素材側只看 **State Matrix**；規格側只看 **SYS1 之 outline 文字與 PDF 文字層** —— "
    "**PDF 之圖表（p9 能力矩陣以文字層存在故有看，p11 流程圖無）不在此列**",
    "**`-007` 不入母體** —— 其已於 22 包依 R-PMH87 單獨處置",
    "**「未對照」之依據多為「素材無對應列」** —— 其證明的是素材之沉默，"
    "非二者條件互斥；凡以條件互斥為由者已逐條具名其依據（R-PMH84）",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


NO_ROW = ("**素材無對應列**：State Matrix 全 362 非空格中，"
          "`disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` "
          "**全數 0 命中**（21 包 §3.1、23 包複驗）。**無共同謂詞。**")

# 鍵為 (tc_id 之末三碼, ER 之序號)
ER_VERDICT: dict[tuple[str, int], tuple[str, str, str]] = {
    ("001", 1): ("未對照", "`\"loading...\"` 是否顯示／`\"Accept\"` 按鈕是否顯示", NO_ROW),
    ("001", 2): ("未對照", "系統是否回報 ready", NO_ROW + " 矩陣之列軸為事件，無「系統就緒」之列。"),
    ("001", 3): ("未對照", "`\"Loading...\"` 是否移除／`\"Accept\"` 是否顯示", NO_ROW),
    ("002", 1): ("未對照", "免責畫面與 `\"Accept\"` 按鈕是否顯示", NO_ROW),
    ("002", 2): ("未對照", "按 Accept 後是否顯示 last mode screen",
                 "**共同名詞 `Last state`**（矩陣 `r33` = `Recall Last state of VP`），"
                 "**惟其觸發為 `Key-on` 事件，本 ER 之觸發為按 `\"Accept\"` 按鈕** —— "
                 "矩陣全簿無 `Accept`（0 命中）。**不同謂詞（回復何狀態 vs 按鍵後之畫面）。**"),
    ("003", 1): ("未對照", "免責畫面與 `\"Accept\"` 按鈕是否顯示", NO_ROW),
    ("003", 2): ("未對照", "逾時期間是否有使用者輸入", NO_ROW + " 矩陣無 `timeout`（0 命中）；"
                 "其 `Timer` 8 處**全為 `Radio Off Delay`**，非 splash／disclaimer 之逾時。"),
    ("003", 3): ("未對照", "逾時後是否顯示 last mode screen", NO_ROW),
    ("004", 1): ("未對照", "是否有使用者輸入", NO_ROW),
    ("004", 2): ("未對照", "Maserati 之免責畫面是否仍顯示且未逾時", NO_ROW +
                 " 矩陣無 `Maserati`（0 命中）。"),
    ("004", 3): ("未對照", "按 Accept 後是否顯示 last mode screen", "同 `-002` 之 ER 2。"),
    ("005", 1): ("未對照", "comfort controls 是否顯示於免責畫面", NO_ROW +
                 " 矩陣無 `comfort`（0 命中）；其 `HVAC Knobs` 為**硬體旋鈕**，"
                 "非畫面上之 comfort controls。**不同謂詞。**"),
    ("005", 2): ("未對照", "被操作之 comfort control 是否有回應", "同上。"),
    ("006", 1): ("未對照", "免責畫面上所顯示之控制項（記錄步）", NO_ROW),
    ("006", 2): ("未對照", "配備 lower comfort screen 時 comfort controls 是否**不**顯示",
                 NO_ROW + " 矩陣無 `lower comfort`（0 命中）。"),
    ("008", 1): ("未對照", "radio 是否處於 Power Button Off 狀態（記錄步）",
                 "**共同名詞 `Power Button OFF`**（矩陣之欄軸），惟本 ER 為**記錄前提狀態**，"
                 "非斷言某事件之後果。**無可相反之值。**"),
    ("008", 2): ("印證", "**按 ON/OFF 鍵後 head unit 之電源狀態** —— "
                 "`PITA6.1`／本 ER 取「轉為 On」；矩陣 `r6` c12／c13 取 `Head Unit Power ON`",
                 "**同一謂詞取相同值。** 矩陣 `r6`（`Key-on` 區塊 × `ON/OFF button Pressed`）"
                 "之 c12／c13（`Power Button OFF` × `Call Not Active` × `Door Open`／`Closed`）"
                 "逐字為 **`Head Unit Power ON`**，與本 ER 之 `The radio changes to On state` 相同。"
                 "**條件亦相符**：`-008` 之 pre-condition 已含「無通話情境進行中」"
                 "（`PITA6.1` 之 `unless certain phone call scenarios have occurred`），"
                 "恰對應 `Call Not Active` 欄。**矩陣為本 ER 之獨立佐證。**"),
    ("008", 3): ("未對照", "轉 On 後免責畫面是否顯示", NO_ROW +
                 " `PITA6.1` 之 `disclaimer screen shall be displayed (see SU6.)` "
                 "於矩陣無對應（`disclaimer` 0 命中）。"),
}


def main() -> None:
    d = json.loads(BATCH.read_text(encoding="utf-8"))
    tcs = [t for t in d["tcs"] if not t["tc_id"].endswith("007")]
    counts = {"牴觸": 0, "印證": 0, "未對照": 0, "待定義": 0}
    unnamed = []
    print("=== batch 1 之逐條 ER 斷言 × 規範性素材／規格他處（23 包步驟 5）===")
    print(f"母體：{len(tcs)} 條 TC（**`-007` 已於 22 包單獨處置，不入母體**）\n")
    n = 0
    for t in tcs:
        key3 = t["tc_id"][-3:]
        ers = [x for x in t["expected_result"].split("\n") if x.strip()]
        print(f"## {t['tc_id']}（leaf {t['leaf_id']}，outline "
              f"{t['specification_reference'].split('_')[-1]}）—— ER {len(ers)} 條\n")
        for i, er in enumerate(ers, 1):
            n += 1
            v = ER_VERDICT.get((key3, i))
            print(f"  ER{i}: {er}")
            if v is None:
                print("      **記法：未具名 ← FAIL**")
                unnamed.append((t["tc_id"], i))
                continue
            kind, pred, why = v
            counts[kind] += 1
            print(f"      記法：**{kind}**；謂詞：{pred}")
            print(f"      依據：{why}\n")
    print("=== 結果 ===")
    print(f"  ER 斷言 **{n}** 條；牴觸 **{counts['牴觸']}**／印證 **{counts['印證']}**／"
          f"未對照 **{counts['未對照']}**／待定義 **{counts['待定義']}**；"
          f"未具名 **{len(unnamed)}**")
    if counts["牴觸"]:
        print("  ← **停止條件 7 觸發**：發現牴觸，須上呈，不得自行調和")
    for tid, i in unnamed:
        print(f"    未具名：{tid} ER{i}")
    print_limits()
    sys.exit(1 if (counts["牴觸"] or unnamed) else 0)


if __name__ == "__main__":
    main()
