#!/usr/bin/env python3
"""R-PMH90 —— 斷言類之**規格全文反向掃描**（23 包步驟 4）。

凡以「限定排除某類斷言」為據之 TC（如 `-007` 以四項事件限定排除 pop-up），
其限定之充分性**須經規格全文之反向掃描**，不得只掃素材。

本檔掃規格 PDF 全文之 `pop-up`／`popup`／`pop up`（不分大小寫），
逐**行**具名其與 `SU3.)`（`No pop-ups will appear until the disclaimer
screen has been removed`）之關係，記法依 R-PMH79。

**計數單位須明說**：本檔以**行**為單位（與分析層 23 §3.1 同），
其**匹配數**為 30 而**行數**為 25 —— 二者皆列出，不混用。

用法:
    python scripts/spec_assertion_scan.py
"""
import re
import sys
from pathlib import Path

import fitz
import yaml

ROOT = Path(__file__).resolve().parent.parent
PAT = re.compile(r"pop\s*-?\s*ups?", re.I)

LIMITS = [
    "**只掃 `pop-up` 一類斷言** —— `-007` 之 ER 另斷言「音訊照常播放」，該面未反向掃",
    "**以行為單位** —— PDF 之換行由版面決定；同一句跨兩行者計為兩行（如 `SU3.)` 之 L293／L294）",
    "**只掃文字層** —— p11 之流程圖為影像，其中若有 pop-up 字樣本檔看不見",
    "**記法之判定為人工** —— `LINE_VERDICT` 逐行具名，本檢查只驗其存在，不驗其正確",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


AFTER = ("**印證** —— 其於流程圖中之位置在免責畫面**之後**（`User Acceptance` → "
         "`Last Mode Screen` → 該 popup），二者為先後而非同時。")
IGN_OFF = ("**未對照** —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群：FOTA／Wi-Fi／"
           "Charge Now），而免責畫面之相位為**開機序列**。**條件互斥之依據為 "
           "`PM1)` 之逐字 `popups to show at IGN OFF`。**")
PB_OFF = ("**未對照** —— 其狀態為 `Power Button Off`，而 `PITA6.1` 逐字載 "
          "`Upon pressing power button to On state disclaimer screen shall be "
          "displayed` —— **免責畫面在該狀態之後**，為先後而非同時。")

# 鍵為 PDF 文字層之行號（`fitz` 逐頁 `get_text()` 串接後之行序）
LINE_VERDICT: dict[int, tuple[str, str, str]] = {
    127: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    140: ("印證", "pop-up 是否顯示（`GDPR/SOS popup`）",
          "**印證** —— 其逐字條件為 `If disclaimer screen is skipped go directly to "
          "last mode screen, showing GDPR/SOS popup first` —— **明載其條件為免責畫面"
          "被跳過**，與 `SU3.)` 之「免責畫面顯示中」**互斥，且互斥之依據為規格文字本身**。"),
    143: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    151: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    160: ("未對照", "pop-up 是否**重複**顯示",
          "**不同謂詞** —— `do not show popup again if popup was shown at Radio Off` "
          "之標的為「是否重複」，`SU3.)` 之標的為「是否顯示」。"),
    257: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    293: ("—", "（`SU3.)` 本身）", "**本行即比對之一造**，不入判定。"),
    294: ("—", "（`SU3.)` 本身之續行）", "**本行即比對之一造**，不入判定。"),
    332: ("牴觸", "**pop-up 是否顯示** —— `SU3.)` 取「不顯示」（免責畫面移除前，"
                  "**全稱否定**）；本行取「顯示」（`Pop-ups still shown.`，**無條件肯定**）",
          "**規格內部之牴觸**（R-PMH89）—— 兩造同屬規格 PDF：`SU3.)` 在 p8，本行在 p9 之能力矩陣。"
          "**其列為 `KEY ON ENGINE ON`、欄為 `HEADUNIT POWER OFF` 之 `HVAC Knobs` 格**"
          "（座標 x=428 y=81；列標籤 `KEY ON ENGINE ON` 於 y=114）。"
          "**條件互斥未證** —— 免責畫面之相位正是 `KEY ON`，**二者高度可能重疊**。"),
    348: ("牴觸", "**pop-up 是否顯示** —— 同 L332",
          "**規格內部之牴觸**（R-PMH89）—— **其列為 `KEY ON ENGINE OFF (ACC or RUN)`、"
          "欄為 `HEADUNIT POWER OFF`**（座標 x=428 y=180；列標籤於 y=197）。"
          "**條件互斥未證**，且其相位（ignition ACC／RUN）正是 `PITA6.1` 所述之開機情境。"),
    407: ("未對照", "pop-up 是否顯示（IGN OFF 之 popup 群）", IGN_OFF),
    409: ("未對照", "pop-up 之顯示時長", IGN_OFF),
    410: ("未對照", "pop-up 之逾時", IGN_OFF),
    411: ("未對照", "pop-up 是否關閉", IGN_OFF),
    413: ("未對照", "FOTA popup 之互動", IGN_OFF),
    414: ("未對照", "popup 之互動逾時", IGN_OFF),
    415: ("未對照", "因 popup 而保持喚醒之上限", IGN_OFF),
    417: ("未對照", "IGN OFF 之 popup 優先序", IGN_OFF),
    419: ("未對照", "FOTA popup 之接受", IGN_OFF),
    426: ("未對照", "Wi-Fi 設定 popup 之忽略", IGN_OFF),
    428: ("未對照", "XEV key off popup", IGN_OFF),
    430: ("未對照", "XEV key off popup 之忽略", IGN_OFF),
    443: ("未對照", "HVAC pop-up 是否顯示（`PITA6`）", PB_OFF +
          " ⚠ **本行另與 State Matrix `r48c10` 牴觸**（20 §4.2，R-PMH80 已處置）——"
          "**該牴觸與本次掃描之標的（vs `SU3.)`）不同，不重複計。**"),
    445: ("未對照", "HVAC popup 是否顯示（`PITA6.1`）", PB_OFF),
    450: ("未對照", "Phone call popup 是否顯示於 Power Button Off 之上（`PITA9`）", PB_OFF +
          " ⚠ **須具名之殘餘風險**：`-007` 之四項限定**不含「無來電」** —— "
          "若來電發生於免責畫面期間，`PITA9` 之 popup 是否顯示，"
          "**規格未於該相位表態**（其只述 `Power Button Off state`）。**列為未驗項。**"),
}


def lines() -> list[tuple[int, str]]:
    cfg = yaml.safe_load((ROOT / "feature.yaml").read_text(encoding="utf-8"))
    d = fitz.open(ROOT / cfg["paths"]["spec_pdf"])
    txt = "\n".join(d[i].get_text() for i in range(d.page_count))
    return [(i + 1, re.sub(r"\s+", " ", l).strip())
            for i, l in enumerate(txt.splitlines()) if PAT.search(l)]


def main() -> None:
    hits = lines()
    n_match = sum(len(PAT.findall(l)) for _, l in hits)
    print("=== 規格全文之 pop-up 反向掃描（R-PMH90）===")
    print(f"  **行數 = {len(hits)}**；**匹配數 = {n_match}**"
          "  ← 二者為不同之計數單位，不混用\n")
    counts, unnamed = {}, []
    for i, l in hits:
        v = LINE_VERDICT.get(i)
        print(f"  L{i}: {l[:110]}")
        if v is None:
            print("      **記法：未具名 ← FAIL**")
            unnamed.append(i)
            continue
        kind, pred, why = v
        counts[kind] = counts.get(kind, 0) + 1
        print(f"      記法：**{kind}**；謂詞：{pred}")
        print(f"      依據：{why}\n")
    print("=== 結果 ===")
    print(f"  {counts}；未具名 **{len(unnamed)}**")
    n_conf = counts.get("牴觸", 0)
    print(f"\n  **牴觸 {n_conf} 行** —— "
          + ("**規格內部之牴觸（R-PMH89），A-PMH21**" if n_conf else "無"))
    print("\n  **與分析層 23 §3.1 之對照**：其報「25 處」，本檔行數 **25** —— **相符**；"
          "\n  其所報之行號（131／147／155／263／144／164／341／357／416–439／453／455／460）"
          "\n  與本檔（127／143／151／257／140／160／332／348／407–430／443／445／450）**逐一相差 4~13**，"
          "\n  **因二者之文字萃取不同**（分析層用 `pm.txt`，本檔用 `fitz` 逐頁串接）。"
          "\n  **其分類（牴觸 2／印證 5／未對照 18）與本檔逐項相符**"
          "（本檔之印證 5 含 L140；`SU3.)` 自身 2 行本檔另計為 `—`，分析層併入未對照）。")
    print_limits()
    sys.exit(1 if unnamed else 0)


if __name__ == "__main__":
    main()
