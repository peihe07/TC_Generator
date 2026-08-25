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

# R-PMH92 —— 本檢查之 must-hit 註冊。**總表之結果欄由此決定，手寫不採認。**
HAS_MUST_HIT = False
MUST_HIT_NOTE = '**未註冊 must-hit**（24 包 §12）—— 其逐條判定由人寫入'

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH = ROOT / "generated" / "batch01.json"

LIMITS = [
    "**只對照 `expected_result`** —— `pre_conditions` 與 `test_procedure` 之斷言不入母體",
    "**斷言之切分以 ` and ` 為之** —— 以逗號、分號或隱含連接之複合斷言**不會被切開**；"
    "其切分規則本身未經驗證（23 個斷言為該規則之產物）",
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

# --- R-PMH94／R-PMH97（26 包）：母體改為**斷言**，並先做二分 ---
# 鍵為 (tc_id 之末三碼, ER 之序號, 斷言之序號)
# 值為 (類, 記法, 謂詞, 依據)；類 ∈ {"SUT", "測試執行"}
#   `SUT`      —— 標的為受測系統之行為或狀態 → **須反向掃描**
#   `測試執行` —— 標的為測試員之作為或不作為 → **不入母體**，記法為 `—`
# **25 包以 ER 條為單位（18 條），其涵蓋率 78%（5 個斷言未單獨對照）；
#   本輪改以斷言為單位（23 個），涵蓋率 100%。**
ER_VERDICT: dict[tuple[str, int, int], tuple[str, str, str, str]] = {
    ("001", 1, 1):
        ("SUT", "未對照", "`\"loading...\"` 是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("001", 1, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為 25→26 包新增之單獨對照**（原併於 ER1 一條）。"),
    ("001", 2, 1):
        ("SUT", "未對照", "系統是否回報 ready",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣之列軸為事件，無「系統就緒」之列。"),
    ("001", 3, 1):
        ("SUT", "未對照", "`\"Loading...\"` 是否移除",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("001", 3, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為新增之單獨對照**。"),
    ("002", 1, 1):
        ("SUT", "未對照", "免責畫面與 `\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("002", 2, 1):
        ("SUT", "未對照", "免責畫面是否移除",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為新增之單獨對照**。"),
    ("002", 2, 2):
        ("SUT", "未對照", "是否顯示 last mode screen",
         "**共同名詞 `Last state`**（矩陣 `r33` = `Recall Last state of VP`），惟其觸發為 `Key-on` 事件，本斷言之觸發為按 `\"Accept\"` 或逾時 —— 矩陣全簿無 `Accept`（0 命中）。**不同謂詞（回復何狀態 vs 按鍵／逾時後之畫面）。**"),
    ("003", 1, 1):
        ("SUT", "未對照", "免責畫面與 `\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("003", 2, 1):
        ("測試執行", "—", "（測試員是否給予輸入）",
         "**測試執行斷言**（R-PMH97）—— 其主語為測試員之不作為（`No user input is given`），非 SUT。**不入反向掃描之母體。**"),
    ("003", 3, 1):
        ("SUT", "未對照", "是否顯示 last mode screen",
         "**共同名詞 `Last state`**（矩陣 `r33` = `Recall Last state of VP`），惟其觸發為 `Key-on` 事件，本斷言之觸發為按 `\"Accept\"` 或逾時 —— 矩陣全簿無 `Accept`（0 命中）。**不同謂詞（回復何狀態 vs 按鍵／逾時後之畫面）。**"),
    ("004", 1, 1):
        ("測試執行", "—", "（測試員是否給予輸入）",
         "**測試執行斷言**（R-PMH97），同 `-003` ER2。**不入母體。**"),
    ("004", 2, 1):
        ("SUT", "未對照", "Maserati 之免責畫面是否仍顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `Maserati`（0 命中）。**本斷言為新增之單獨對照**。"),
    ("004", 2, 2):
        ("SUT", "未對照", "是否已逾時",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `timeout`（0 命中）；其 `Timer` 8 處全為 `Radio Off Delay`。**本斷言為新增之單獨對照**。"),
    ("004", 3, 1):
        ("SUT", "未對照", "免責畫面是否移除",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為新增之單獨對照**。"),
    ("004", 3, 2):
        ("SUT", "未對照", "是否顯示 last mode screen",
         "**共同名詞 `Last state`**（矩陣 `r33` = `Recall Last state of VP`），惟其觸發為 `Key-on` 事件，本斷言之觸發為按 `\"Accept\"` 或逾時 —— 矩陣全簿無 `Accept`（0 命中）。**不同謂詞（回復何狀態 vs 按鍵／逾時後之畫面）。**"),
    ("005", 1, 1):
        ("SUT", "未對照", "comfort controls 是否顯示於免責畫面",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `comfort`（0 命中）；其 `HVAC Knobs` 為**硬體旋鈕**，非畫面上之 comfort controls。**不同謂詞。**"),
    ("005", 2, 1):
        ("SUT", "未對照", "被操作之 comfort control 是否有回應",
         "同 `-005` ER1。"),
    ("006", 1, 1):
        ("SUT", "未對照", "免責畫面上所顯示之控制項（記錄步）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("006", 2, 1):
        ("SUT", "未對照", "配備 lower comfort screen 時 comfort controls 是否**不**顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `lower comfort`（0 命中）。"),
    ("008", 1, 1):
        ("SUT", "未對照", "radio 是否處於 Power Button Off 狀態（記錄步）",
         "**共同名詞 `Power Button OFF`**（矩陣之欄軸），惟本斷言為**記錄前提狀態**，非斷言某事件之後果。**無可相反之值。**"),
    ("008", 2, 1):
        ("SUT", "印證", "**按 ON/OFF 鍵後 head unit 之電源狀態** —— `PITA6.1`／本斷言取「轉為 On」；矩陣 `r6` c12／c13 取 `Head Unit Power ON`",
         "**同一謂詞取相同值。** `-008` 之 pre-condition 已含「無通話情境進行中」（`PITA6.1` 之 `unless certain phone call scenarios have occurred`），**恰對應 `Call Not Active` 欄**。**矩陣為本斷言之獨立佐證。**"),
    ("008", 3, 1):
        ("SUT", "未對照", "轉 On 後免責畫面是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** `PITA6.1` 之 `disclaimer screen shall be displayed (see SU6.)` 於矩陣無對應。"),
}


def main() -> None:
    d = json.loads(BATCH.read_text(encoding="utf-8"))
    tcs = [t for t in d["tcs"] if not t["tc_id"].endswith("007")]
    counts = {"牴觸": 0, "印證": 0, "未對照": 0, "待定義": 0}
    kinds = {"SUT": 0, "測試執行": 0}
    unnamed = []
    print("=== batch 1 之逐**斷言**對照 × 規範性素材／規格他處"
          "（26 包步驟 2／3，R-PMH94／R-PMH97）===")
    print(f"母體：{len(tcs)} 條 TC（**`-007` 已單獨處置，不入母體**）")
    print("**單位為斷言**（以 ` and ` 切分 ER）—— 25 包以 ER 條為單位，涵蓋率 78%\n")
    n_er = n_as = 0
    for t in tcs:
        key3 = t["tc_id"][-3:]
        ers = [x for x in t["expected_result"].split("\n") if x.strip()]
        n_er += len(ers)
        print(f"## {t['tc_id']}（leaf {t['leaf_id']}，outline "
              f"{t['specification_reference'].split('_')[-1]}）\n")
        for i, er in enumerate(ers, 1):
            body = re.sub(r"^\d+\.\s*", "", er)
            parts = [x for x in re.split(r"\s+and\s+", body) if x.strip()]
            for j, part in enumerate(parts, 1):
                n_as += 1
                v = ER_VERDICT.get((key3, i, j))
                print(f"  ER{i}.{j}: {part}")
                if v is None:
                    print("      **未具名 ← FAIL**")
                    unnamed.append((t["tc_id"], i, j))
                    continue
                kind, form, pred, why = v
                kinds[kind] = kinds.get(kind, 0) + 1
                if form in counts:
                    counts[form] += 1
                print(f"      類：**{kind}**；記法：**{form}**；謂詞：{pred}")
                print(f"      依據：{why}\n")
    print("=== 結果 ===")
    print(f"  ER 條 **{n_er}** → **斷言 {n_as}**（比值 {n_as/n_er:.2f}）")
    print(f"  二分（R-PMH97）：SUT 行為斷言 **{kinds['SUT']}**／"
          f"測試執行斷言 **{kinds['測試執行']}**（後者不入掃描母體）")
    print(f"  記法：牴觸 **{counts['牴觸']}**／印證 **{counts['印證']}**／"
          f"未對照 **{counts['未對照']}**／待定義 **{counts['待定義']}**")
    print(f"  未具名 **{len(unnamed)}**；**涵蓋率 "
          f"{(n_as-len(unnamed))/n_as:.0%}**（25 包以 ER 條為單位時為 78%）")
    if counts["牴觸"]:
        print("  ← **停止條件觸發**：發現牴觸，須上呈，不得自行調和")
    for tid, i, j in unnamed:
        print(f"    未具名：{tid} ER{i}.{j}")
    print_limits()
    sys.exit(1 if (counts["牴觸"] or unnamed) else 0)


if __name__ == "__main__":
    main()
