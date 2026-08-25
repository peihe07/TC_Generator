#!/usr/bin/env python3
"""21 包步驟 3 —— State Matrix × 規格章之對照（R-PMH79 之三種記法）。

**R-PMH79**：對照結果只得記為三者之一 ——
  `牴觸`   二者就**同一謂詞取相反值**。須具名該謂詞，並上呈，不得自行調和。
  `印證`   二者就同一謂詞取相同值，或素材補上同一命題之另一半。須具名謂詞。
  `未對照` 二者**無共同謂詞**，或素材中**無對應列**。

**「無對應列」不得記為「無矛盾」；「不同謂詞」不得記為「非牴觸」。**

矩陣為規範性文件（PDF p10：`Power Moding behavior shall not be developed
without following the Power Moding State Matrix`），故其與規格章之牴觸
即為「TC 之 ER 可能與規範性文件相反」之來源。

用法:
    python scripts/matrix_vs_chapter.py 7
    python scripts/matrix_vs_chapter.py 7 --vocab      # 只跑詞彙探針
"""
import argparse
import re
import sys
from pathlib import Path

import openpyxl
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

MATRIX = ("inputs/Power Moding HMI State Matrix R1 SR24 Post 2A "
          "DCR21421 (August 3 2022).xlsx")
SHEET = "State Matrix"

# 三個區塊之（起列, 標題列, 軸列）—— 由 §2.1 之合併儲存格實測而得
BLOCKS = [(1, 16, (2, 3, 4, 5)), (19, 33, (20, 21, 22, 23)), (37, 48, (37, 38, 39))]

# ch 7 之關鍵名詞 —— 用於**範圍向**：其於矩陣之命中數
VOCAB_CH7 = ["animation", "splash", "disclaimer", "comfort", "Maserati",
             "lower comfort", "traffic announcement", "CAN BUS", "ignition",
             "driver door", "black", "timeout", "3 sec", "1.5", "10s",
             "last mode", "Radio OFF"]

LIMITS = [
    "**只對照矩陣之「事件列 × 有值之格」** —— 空格與 `-` 一律不入母體；"
    "其「無值」是否本身有意義（不適用 vs 未定義），本檢查不判",
    "**謂詞之認定為人工** —— `VERDICT` 逐列具名，本檢查只驗其存在，不驗其正確",
    "**只比對 SYS1 側之 outline 文字** —— 規格 PDF 之圖表（p9 能力矩陣、p11 流程圖）不看",
    "詞彙探針為**大小寫敏感之字面**比對 —— 不敏感之比對會使 `Radio OFF` 誤命中 `Radio Off Delay`（15 次），二者為不同之詞",
    "詞彙探針為**字面**比對 —— 同義改寫（如 `VP` vs `screen`）不會命中，"
    "**故『詞彙 0 命中』不等於『語意無交集』**，僅為 `未對照` 之支持證據而非其證明",
    "**矩陣之三個區塊各有一組軸** —— 跨區塊之同名事件（如 `ON/OFF button Pressed` "
    "於 r6／r24／r40）其軸不同，本檢查逐列判，不合併",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def n(v) -> str:
    return re.sub(r"\s+", " ", str(v)).strip() if v is not None else ""


def load_sheet():
    cfg = yaml.safe_load((ROOT / "feature.yaml").read_text(encoding="utf-8"))  # noqa: F841
    wb = openpyxl.load_workbook(ROOT / MATRIX, data_only=True)   # **不 save**
    return wb, wb[SHEET]


def merged_val(ws, r, c) -> str:
    for m in ws.merged_cells.ranges:
        if m.min_row <= r <= m.max_row and m.min_col <= c <= m.max_col:
            return n(ws.cell(m.min_row, m.min_col).value)
    return n(ws.cell(r, c).value)


def event_rows(ws) -> list[tuple[int, int, str, list]]:
    """回傳 [(區塊起列, 列, 事件標籤, [(欄, 軸, 值)])] —— 只取有值之格。"""
    out = []
    for lo, hi, axr in BLOCKS:
        for r in range(lo, hi + 1):
            lbl = n(ws.cell(r, 1).value)
            cells = []
            for c in range(2, 14):
                v = n(ws.cell(r, c).value)
                if v in ("", "-", "'-"):
                    continue
                ax = " / ".join(x for x in (merged_val(ws, a, c) for a in axr) if x)
                cells.append((c, ax, v))
            if lbl and cells:
                out.append((lo, r, lbl, cells))
    return out


# --- R-PMH79：逐列之記法、謂詞與依據。**每一事件列皆須在此具名**，未具名 → FAIL ---
# 鍵為 (區塊起列, 列)。
VERDICT: dict[tuple[int, int], tuple[str, str, str]] = {
    (1, 6):
        ("未對照", "按 Power 鍵之後果（電源狀態／pop-up）vs 開機動畫是否顯示",
         "章 7 之 `SU6.)`（7.7）載 `When Power Button is pressed On do not show Start Up Animation.` —— 其謂詞為**動畫是否顯示**；本列之格為 `Head Unit Power ON`／`Power OFF state`／`Pop-up: Cannot Power Off System`，其謂詞為**電源狀態**與 **pop-up**。**不同謂詞**。另 `SU1.1)`（7.1.1）雖提 power button 之轉移，惟其值為「依車輛架構」，**未斷言具體值**，故無可相反者。"),
    (1, 7):
        ("未對照", "門開啟之後果（電源／VP 狀態）vs 動畫觸發",
         "章 7 之觸發一律為**駕駛門關閉**（`SU1.)`／`SU4.)`／`SU5.)`／`SU6.)`）；本列為門**開啟**。且矩陣之 `Door` 軸**未區分駕駛門與其他門**（`driver door` 於矩陣 0 命中）。**不同謂詞且情境不同。**"),
    (1, 8):
        ("未對照", "門關閉之後果（`Event ignored`／`Power Button remains off`）vs 動畫是否播放",
         "**最接近之一列** —— `SU1.)`（7.1）以駕駛門關閉為觸發、`SU6.)`（7.7）載「last state 為 Radio OFF 時關門播放動畫後螢幕維持黑」。惟本列之格所斷言者為**電源按鈕狀態不變**（`Power Button remains off`）／**事件被忽略**，**未提動畫是否播放**；且矩陣之 `Door` 軸未區分駕駛門。**不同謂詞。** ⚠ 須人讀：`Event ignored`（HU on 時）與 `SU5.)`「每個 CAN BUS wake up 只播一次」在意圖上相容，惟該相容為推論而非量測。"),
    (1, 9):
        ("未對照", "來電之後果（電源）vs pop-up 抑制",
         "`SU3.)`（7.4）之謂詞為 **pop-up 是否顯示**；本列之格為 `Head Unit Power ON`，謂詞為**電源**。**不同謂詞**（20 §4.3 之 `10.6` 同型，依 R-PMH79 改記為未對照）。"),
    (1, 10):
        ("未對照", "Projection 之後果",
         "章 7 全文無 `Projection` —— **規格側無對應敘述**。"),
    (1, 11):
        ("未對照", "VR 長按（無 Projection）之後果",
         "章 7 全文無 VR 長按 —— 其屬 ch 11（`VRLP1`）。**章 7 側無對應敘述**。"),
    (1, 12):
        ("未對照", "VR 長按（Projection 中）之後果",
         "同上，且 Projection 於章 7 無敘述。"),
    (1, 13):
        ("未對照", "通話結束之後果",
         "章 7 全文無通話結束之敘述（`SU3.)` 只提 traffic announcement 之音訊）。**規格側無對應敘述**。"),
    (1, 14):
        ("未對照", "Projection 通話結束之後果",
         "同 r13，且 Projection 於章 7 無敘述。"),
    (1, 15):
        ("未對照", "Key-off 之後果（VP on/off、pop-up）vs 關機動畫之觸發",
         "`SU4.)`（7.5）載 `Begin shut down animation only when you have the combination of a KEY OFF and radio UI shut down.` —— 其謂詞為**關機動畫何時開始**；本列之格為 `VP Turns OFF`／`VP Stays ON`／pop-up，謂詞為**VP 電源**與 **pop-up**。**不同謂詞。** ⚠ pop-up 面同 r48 之高風險註記（軸不含 disclaimer 狀態）。"),
    (1, 16):
        ("未對照", "Off Road+ 按鍵之後果",
         "本列屬 **ch 12**（`OFF1.)`／`OFF3.)`，已於 20 包 §3 對照並判為互補）。**章 7 側無對應敘述**。"),
    (19, 24):
        ("未對照", "Key-off 狀態下按 Power 鍵之後果 vs 開機動畫是否顯示",
         "同 r6：`SU6.)` 之謂詞為動畫，本列為 VP 電源與 pop-up。**不同謂詞。**"),
    (19, 25):
        ("未對照", "門開啟之後果 vs 動畫觸發",
         "同 r7 —— 章 7 之觸發為駕駛門**關閉**，且矩陣之 `Door` 軸未區分駕駛門。"),
    (19, 26):
        ("未對照", "來電之後果（`Head Unit remains ON untill the Timer is done`）vs pop-up 抑制",
         "同 r9 —— 不同謂詞（電源／計時 vs pop-up 是否顯示）。⚠ `Timer` 於矩陣 8 命中而章 7 之 `timeout` 0 命中：**二者為不同之計時**（前者為 Radio Off Delay，後者為 splash／disclaimer 之逾時）。"),
    (19, 27):
        ("未對照", "Projection 之後果",
         "章 7 全文無 Projection。"),
    (19, 28):
        ("未對照", "VR 長按（無 Projection）之後果",
         "屬 ch 11。"),
    (19, 29):
        ("未對照", "VR 長按（Projection 中）之後果",
         "同上。"),
    (19, 30):
        ("未對照", "門關閉之後果（`Event ignored`／HU off 時亦忽略）vs 動畫是否播放",
         "**與 r8 同型且更值得看**：本列為 **Key-off** 區塊，其 `HU off` 欄（c12）亦為 `Event ignored`。而 `SU1.)`（7.1）之情境即「駕駛門關閉→播放開機動畫」。惟本列之謂詞為**事件是否被處理**，未提動畫；且矩陣之 `Door` 軸未區分駕駛門。**不同謂詞。** ⚠ **本列為 ch 7 × 矩陣中最接近牴觸者，須人讀。**"),
    (19, 31):
        ("未對照", "通話結束之後果",
         "章 7 全文無通話結束之敘述。"),
    (19, 32):
        ("未對照", "Projection 通話結束之後果",
         "同上。"),
    (19, 33):
        ("未對照", "Key-on 之後果（`Recall Last state of VP`）vs 開機序列",
         "**共同名詞 `Last state`** —— `SU6.)`（7.7）載 `If last state is Radio OFF, play startup animation and show applicable splash screens…`。惟本列之格為 `Recall Last state of VP`（**回復上次 VP 狀態**），其謂詞為**回復何狀態**；`SU6.)` 之謂詞為**是否播放動畫／顯示 splash**。**不同謂詞**，且矩陣未言回復過程中是否播放動畫。⚠ 須人讀。"),
    (37, 40):
        ("未對照", "按 Power 鍵之後果（Mute／Screen Off）vs 開機動畫",
         "同 r6／r24 —— 不同謂詞。章 7 全文無 Mute 與 Screen Off 之敘述。"),
    (37, 41):
        ("未對照", "來電之後果（Screen on／unmute／HU Powers on）vs pop-up 抑制",
         "同 r9 —— 不同謂詞（20 §4.3 之 `10.6` 即此列，依 R-PMH79 由「非牴觸」改記為「未對照」）。"),
    (37, 42):
        ("未對照", "切入 R 檔之後果",
         "章 7 全文無 gear、無倒車影像。**規格側無對應敘述**。"),
    (37, 43):
        ("未對照", "切出 R 檔之後果",
         "同上。"),
    (37, 44):
        ("未對照", "Screen Off 鍵之後果",
         "章 7 全文無 Screen Off 鍵。其屬 ch 10（`PITA4`）。"),
    (37, 45):
        ("未對照", "Mute 鍵之後果",
         "章 7 全文無 Mute。"),
    (37, 46):
        ("未對照", "Headunit Mode 鍵之後果",
         "章 7 全文無 Headunit Mode 鍵。"),
    (37, 47):
        ("未對照", "以 VR 切換 Headunit Mode 之後果",
         "同上；VR 屬 ch 11。"),
    (37, 48):
        ("未對照", "HVAC 硬控調整之後果（pop-up 是否顯示）vs `SU3.)` 之 pop-up 抑制",
         "**共同名詞 `pop-up`，惟軸不含 disclaimer 狀態** —— 章 7 之 `SU3.)`（7.4）為全稱否定（`No pop-ups will appear until the disclaimer screen has been removed`），本列為無條件之肯定，**二者之條件互不涵蓋**，故非同一命題之相反值。**⚠ 高風險項，須人讀**：若本列之情境可發生於 disclaimer 顯示期間，即成牴觸；矩陣之軸無法回答此問。"),
}


def vocab_probe(ws) -> list[tuple[str, int]]:
    cells = [n(v) for row in ws.iter_rows(values_only=True) for v in row if n(v)]
    blob = " || ".join(cells)
    # **大小寫敏感** —— 不敏感之比對會使 `Radio OFF` 命中 `Radio Off Delay`
    # 15 次（二者為不同之詞：前者為「最後狀態為關機」，後者為延時參數）。
    return [(p, blob.count(p)) for p in VOCAB_CH7], len(cells)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("chapter", type=int)
    ap.add_argument("--vocab", action="store_true")
    a = ap.parse_args()
    wb, ws = load_sheet()
    import chapter_bidirectional as cb

    probes, n_cells = vocab_probe(ws)
    print(f"=== State Matrix × 規格章 {a.chapter} 之對照（R-PMH79）===")
    print(f"素材：`{MATRIX}`（唯讀，未 save）；非空格 = **{n_cells}**\n")

    print(f"--- 範圍向：章 {a.chapter} 之關鍵名詞於矩陣之命中 ---")
    hit = [(p, k) for p, k in probes if k]
    for p, k in probes:
        print(f"  {k:>3}  {p}")
    print(f"\n  命中之名詞 = **{len(hit)}/{len(probes)}**"
          + ("" if hit else " —— **全部 0 命中**"))
    print("  ⚠ 字面比對；`0 命中` 為 `未對照` 之**支持證據**，非其證明（見 LIMITS）。")
    if a.vocab:
        print_limits()
        wb.close()
        sys.exit(0)

    rows = event_rows(ws)
    outs = cb.sys1_chapter(a.chapter)
    print(f"\n--- 逐列對照：矩陣事件列 **{len(rows)}**"
          f" × 章 {a.chapter} 之 outline **{len(outs)}** ---\n")
    counts = {"牴觸": 0, "印證": 0, "未對照": 0}
    unnamed = []
    for lo, r, lbl, cells in rows:
        v = VERDICT.get((lo, r))
        print(f"  [區塊 r{lo}] r{r:<3} {lbl}（{len(cells)} 格）")
        if v is None:
            print("      **記法：未具名 ← FAIL（R-PMH79）**")
            unnamed.append((lo, r, lbl))
            continue
        kind, pred, why = v
        counts[kind] = counts.get(kind, 0) + 1
        print(f"      記法：**{kind}**；謂詞：{pred}")
        print(f"      依據：{why}")
    print(f"\n=== 結果 ===")
    print(f"  牴觸 **{counts['牴觸']}**／印證 **{counts['印證']}**／"
          f"未對照 **{counts['未對照']}**；未具名 **{len(unnamed)}**")
    if counts["牴觸"]:
        print("  ← **停止條件觸發**：發現牴觸，須上呈，不得自行調和（R-PMH79）")
    for lo, r, lbl in unnamed:
        print(f"    未具名：r{r} {lbl}")
    print_limits()
    wb.close()
    sys.exit(1 if (counts["牴觸"] or unnamed) else 0)


if __name__ == "__main__":
    main()
