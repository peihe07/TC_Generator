"""B2 v2 — A-PW16 九章判定素材，判讀單位改為「被引用之錨點 vs leaf」（R-P38）。

R-P41(a)：本檔之**事實部分全部由本腳本產生** ——
章節全文、該章全部需求錨點、其中被引用者及引用之 leaf、未被引用者、
引用 leaf 之 Requirement Description。

**判讀欄為人工**，以 JUDGEMENTS 常數保存於本檔（人工撰寫、隨腳本版控），
腳本本身不做任何判讀，也不產生處置建議（R-P27 / 05 §I）。

用法：
    python features/power/scripts/build_b2.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_textlayer import REQ_RE, SEC_RE, paragraphs  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

# A-PW16 之九章（03 包 G14 所查出）
NINE = [
    "1.6.2.1", "1.6.2.1.4", "1.6.2.1.9", "1.6.2.1.10", "1.6.2.1.11",
    "1.6.2.1.14", "1.6.2.1.15.1", "1.6.3.1.1", "1.8.1.1.1",
]

PM_RE = re.compile(r"Sys-RA-PM-\d{4}")
PD_RE = re.compile(r"Sys-RA-PD[_-]\d+")

# ── 人工判讀欄（R-P38：須針對被引用之錨點，非整章）────────────────────
# 格式：章節號 -> (判定, 逐字依據)
JUDGEMENTS: dict[str, tuple[str, str]] = {
    "1.6.2.1": (
        "無法判定",
        "被引用之兩個錨點 `4941354`、`4941355` 之文字層內容各只有一行 "
        "`CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource` 與 "
        "`CFTSMV009_CIP_R4_O1584_5_inline.rtf WrapperResource`，"
        "即其實質內容為嵌入之 inline RTF 物件，**不在 R-P17 之文字層內**。"
        "既無可判讀之行為敘述，即無從與任何 leaf 之 Description 比對。"
        "（此即 R-P39 所要清點之情形。）",
    ),
    "1.6.2.1.4": (
        "未涵蓋",
        "本章兩個錨點中**僅 `4941400` 被引用**（`SWE-PM-003` 經 `Sys-RA-PM-0031`）；"
        "`4941399` 未被任何 leaf 引用。`4941400` 逐字為「the R1 HU shall not enter "
        "stolen vehicle mode under any condition」，`Radio` 欄含本專案車型 `R1L`。"
        "`SWE-PM-003`（Partial Operation）之 Description 全文無 stolen vehicle 相關敘述。"
        "**判讀單位訂正後之結論**：未涵蓋者為一條**否定需求**（不得進入該模式），"
        "非「防盜功能」——A-PW16 稱本章為「實質功能章節」不準確。"
        "未被引用之 `4941399`（描述進入條件，`Radio` 欄 `VP4R7, VP4R84` 不含 R1L）"
        "不在本 feature 範圍內。",
    ),
    "1.6.2.1.9": (
        "部分涵蓋",
        "四個錨點中 `4941426` / `4941427` / `4941428` 被引用（皆 `SWE-PM-008`），"
        "`4941429`（`$Telematic_Power$` = [Logistic_On]）**未被引用，不在判讀範圍內**。"
        "`SWE-PM-008` Description 逐字列出三個狀態名"
        "「Logistic Idle/ Logistic Standby / Lgistic Sleep」——**狀態名稱涵蓋**。"
        "但被引用錨點之實質內容 —— `4941426` 之「In the following \"Ignition Working "
        "Conditions\": Ignition On, Ignition Pre_Start, Ignition Start, Ignition "
        "Cranking, Ignition On Engine On」、`4941427` 之「related to TLM, FPDM AMP, "
        "ICS, and DTV OFF with Logistic Mode active」、`4941428` 之「TLM and AMP has "
        "not to reproduce any audio source and the user can\'t do any setting」——"
        "在 Description 中皆無對應文字。",
    ),
    "1.6.2.1.10": (
        "部分涵蓋",
        "狀態名稱涵蓋（同 §1.6.2.1.9）。被引用錨點之區辨條件「Ignition Pre Off, "
        "Ignition Off」＋「Logistic Mode active **AND network active**」"
        "在 Description 中無對應；Description 僅有「subcomponents shall ensure no "
        "features are availabel and prepare to shutdown」，未區分 network 狀態。",
    ),
    "1.6.2.1.11": (
        "部分涵蓋",
        "狀態名稱涵蓋（同上）。被引用錨點之區辨條件為「Ignition Pre Off, Ignition Off」"
        "＋「Logistic Mode active **AND network off**」。"
        "**§1.6.2.1.10 與 §1.6.2.1.11 之唯一差異即 network active / off**，"
        "而 `SWE-PM-008` Description 不含 `network` 一詞，故無法據以區分此二章。",
    ),
    "1.6.2.1.14": (
        "部分涵蓋",
        "**八個錨點中僅 `4941453` 被引用**（九條 leaf 共同引用），其餘七個"
        "（`4941452`、`4941454`–`4941459`）未被任何 leaf 引用，不在判讀範圍內。"
        "`4941453` 之內容為該章之 TLM 狀態 × 模組對照表。"
        "`SWE-PM-001`–`009` 之 Description 逐條列舉各狀態下之模組狀態"
        "（`Display is on` / `Audio un-muted` / `BT on` / `Tuner on` / `USB on` / `AUX on`），"
        "與表中 Source／Audio Power amplifier／Display／tuner／USB／AUX 各欄可對應。"
        "但 **BoosterOUT**、**Antenna 之 Analog / Digital 分列**，"
        "以及 `Display / Illumination` 欄所引之「as defined in CFTS020 and VF668」"
        "與 DCSD touch coordinate 行為，在九條 Description 中皆無對應文字。",
    ),
    "1.6.2.1.15.1": (
        "涵蓋",
        "**判讀單位訂正後結論改變。** 本章三個錨點中**僅 `4941663` 被引用**"
        "（`SWE-PM-004`）；`4941661`、`4941662` 未被任何 leaf 引用。"
        "`4941663` 之內文全文為「In \u201cTimed Mode\u201d the Customer setting screens "
        "shall be disabled.」，其 `Radio` 欄為 `R1L-R, R1L`（本專案車型專屬）。"
        "`SWE-PM-004`（Timed）Description 末句「User settings option shall be disable "
        "in Timed power state」與之**逐句對應**。"
        "v1 以「章 vs leaf」比對時，據未被引用之 `4941661`（ICS POWER 按鍵 wakeup 路徑、"
        "CAN 喚醒、`CLIMATIC_PANEL.Radio_Btn0`、250 ms、`ActiveLoadSlave`）"
        "與 `4941662` 判為「部分涵蓋」——**該二錨點不在本 feature 範圍內**，"
        "其未涵蓋不構成 coverage hole。此為 R-P38 訂正單位後之實質差異。",
    ),
    "1.6.3.1.1": (
        "涵蓋（一分支例外）",
        "`SWE-PM-057` Description 與被引用錨點 `4941708`（「user can set "
        "SwitchOff_Timeout_Setting.Req to \"00 minutes\" OR to \"20 minutes\" IF PROXI "
        "parameter \"Switch_Off_Time\" is equal to \"20 minutes\"」）逐句對應；"
        "其 Case1/2/3 亦對應 `4941707` 之 Timeout1 設定。"
        "**例外**：`4941706` 之分支「For case of LTM High Radio present, see "
        "Auto_SwitchOn_Setting.Req management section」指向另一章節，Description 無對應。",
    ),
    "1.8.1.1.1": (
        "涵蓋",
        "五個錨點中 `4941814` / `4941815` / `4941817` 被引用（皆 `SWE-PM-057`）；"
        "`4941813`（`Switch_Off_Time` 由 PROXI 於 TLM node 定義）與 `4941816` 未被引用。"
        "被引用者逐條為 `Switch_Off_Time` = 20 / 60 / 180 分鐘時之 "
        "`SwitchOff_Timeout_Setting.Req` 可選值。`SWE-PM-057` 之 Verification Method "
        "逐字列出 Case1（00 或 20 min）、Case2（00 或 60 min）、Case3（00 或 180 min），"
        "Verification Criteria 為「\"Switch_Off_Time\" parameter is set to "
        "\"20 or 60 or 180 minutes\" in PROXI」。三個 case 完全對應。",
    ),
}
# ────────────────────────────────────────────────────────────────


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def chapter_anchors() -> dict[str, dict]:
    """CFTS009 之九章：標題、章節 id、本文全文、其下全部需求錨點及**逐錨點內文**。

    錨點行本身只有 metadata（`[Artifact Type:…] [Radio:…]` 等），
    需求文字在其後之段落，至下一個錨點或下一個章節錨點止。
    """
    out: dict[str, dict] = {}
    current = None
    anchor = None
    for plain, bold in paragraphs(find("CFTS_009_Wake-up")):
        m = SEC_RE.match(plain)
        if m:
            current = m.group(1) if m.group(1) in NINE else None
            anchor = None
            if current:
                out[current] = {"title": m.group(2), "sid": m.group(3),
                                "lines": [], "anchors": [], "text": {}, "meta": {}}
            continue
        if not current:
            continue
        if plain.strip():
            out[current]["lines"].append(plain.strip())
        found = REQ_RE.findall(bold)
        if found:
            anchor = found[0]
            out[current]["anchors"].append(anchor)
            out[current]["text"][anchor] = []
            out[current]["meta"][anchor] = plain.strip()
        elif anchor and plain.strip():
            out[current]["text"][anchor].append(plain.strip())
    return out


def leaf_records() -> dict[str, dict]:
    wb = openpyxl.load_workbook(find("FSM-037"), data_only=True, read_only=True)
    ws = wb["SWE1 Requirements"]
    out = {}
    for r in ws.iter_rows(min_row=8, max_row=145, values_only=True):
        if r[0] and str(r[0]).strip():
            out[str(r[0]).strip()] = {
                "title": str(r[2] or "").strip(),
                "desc": str(r[3] or "").strip(),
                "vc": str(r[16] or "").strip(),
                "vm": str(r[17] or "").strip(),
                "src": str(r[1] or ""),
            }
    wb.close()
    return out


def main() -> None:
    chapters = chapter_anchors()
    leaves = leaf_records()

    # item id -> 引用它的 leaf（經 layer3_full.tsv 之 item_ids 欄）
    cited: dict[str, list[str]] = defaultdict(list)
    for line in (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        leaf, _cfts, _num, _title, _n, items, _toks = line.split("\t")
        for item in items.split(","):
            if leaf not in cited[item]:
                cited[item].append(leaf)

    out = [
        "# B2 v2 — A-PW16 九章判定素材（R-P38：被引用之錨點 vs leaf）\n",
        "\n> 取代 `b2_uncovered_chapters.md`（該檔以「章 vs leaf」比對，單位有誤）。\n",
        "> 依 R-P27 與 05 §I：本檔**不建議任何處置**。\n",
        "> 依 R-P41(a)：事實部分全部由 `scripts/build_b2.py` 產生；\n",
        "> 判讀欄為人工，以該腳本之 `JUDGEMENTS` 常數保存並隨腳本版控。\n",
        "\n## 判定總表\n",
        "\n| 章節 | 標題 | 錨點總數 | 被引用 | 未被引用 | 引用之 leaf | 判定 |\n",
        "|---|---|---|---|---|---|---|\n",
    ]
    detail = []
    for num in NINE:
        ch = chapters[num]
        anchors = ch["anchors"]
        used = [a for a in anchors if cited.get(a)]
        unused = [a for a in anchors if not cited.get(a)]
        who = sorted({l for a in used for l in cited[a]},
                     key=lambda x: int(re.match(r"SWE-PM-(\d+)", x).group(1)))
        verdict, basis = JUDGEMENTS[num]
        out.append(
            f"| §{num} | {ch['title']} | {len(anchors)} | **{len(used)}** | "
            f"{len(unused)} | {', '.join(f'`{w}`' for w in who) or '**無**'} | **{verdict}** |\n"
        )

        detail.append(f"\n---\n\n## §{num} — {ch['title']}　`{{{ch['sid']}}}`\n")
        detail.append(f"\n### 該章之全部需求錨點（{len(anchors)} 個）\n\n")
        detail.append("| 錨點 id | 是否被引用 | 引用之 leaf | 內文首 120 字元 |\n|---|---|---|---|\n")
        for a in anchors:
            refs = cited.get(a, [])
            body = " / ".join(ch["text"].get(a, [])).replace("|", "\\|")[:120]
            detail.append(
                f"| `{a}` | {'**是**' if refs else '否'} | "
                f"{', '.join(f'`{r}`' for r in refs) or '—'} | {body or '（無內文）'} |\n"
            )
        detail.append(f"\n**被引用之錨點**（{len(used)}）："
                      f"{', '.join(f'`{a}`' for a in used) or '**無**'}\n")
        detail.append(f"\n**未被引用之錨點**（{len(unused)}）："
                      f"{', '.join(f'`{a}`' for a in unused) or '**無**'}\n")

        detail.append(f"\n### 被引用錨點之全文（判讀單位，R-P38）\n")
        if not used:
            detail.append("\n（本章無任何錨點被引用）\n")
        for a in used:
            detail.append(f"\n#### `{a}`　引用者：{', '.join(f'`{r}`' for r in cited[a])}\n")
            detail.append(f"\nmetadata：`{ch['meta'].get(a, '')}`\n")
            detail.append("\n```\n" + ("\n".join(ch["text"].get(a, [])) or "（無內文 —— 內容可能在嵌入物件內）") + "\n```\n")

        detail.append(f"\n### 引用本章之 leaf 之 Requirement Description（全文）\n")
        if not who:
            detail.append("\n（無 leaf 引用本章之任何錨點）\n")
        for w in who:
            rec = leaves[w]
            detail.append(f"\n#### `{w}` — {rec['title']}\n\n```\n{rec['desc']}\n```\n")
            if rec["vc"]:
                detail.append(f"\nVerification Criteria：\n\n```\n{rec['vc']}\n```\n")
            if rec["vm"]:
                detail.append(f"\nVerification Method：\n\n```\n{rec['vm']}\n```\n")

        detail.append(f"\n### 判讀（人工）\n\n**判定：{verdict}**\n\n{basis}\n")
        detail.append(f"\n### 本章全文（不截斷，{sum(len(x) for x in ch['lines'])} 字元）\n\n"
                      f"```\n" + "\n".join(ch["lines"]) + "\n```\n")

    path = DATA / "b2_v2_uncovered_chapters.md"
    path.write_text("".join(out + detail), encoding="utf-8")

    missing = [n for n in NINE if n not in JUDGEMENTS]
    print(f"wrote {path.relative_to(ROOT)} — {len(NINE)} 章，{path.stat().st_size} bytes")
    print(f"G23 錨點必填欄：{len(NINE)} / {len(NINE)} 章皆列出被引用錨點欄"
          f"（含「無」之明示）；缺判讀者 {missing or '無'}")
    for num in NINE:
        ch = chapters[num]
        used = [a for a in ch["anchors"] if cited.get(a)]
        print(f"  §{num:12} 錨點 {len(ch['anchors']):>3} 被引用 {len(used):>2} "
              f"未引用 {len(ch['anchors']) - len(used):>3}")


if __name__ == "__main__":
    main()
