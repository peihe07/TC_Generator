#!/usr/bin/env python3
"""CFTS020 物件抽取與適用性判定（下放包 03 作業 B／§4 掃描條件）。

抽取條件（逐項揭露）：
  - 來源檔：`inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and
    DCSD _20260310-1533.docx` 之 `word/document.xml`
  - 轉純文字：`</w:p>`→換行、`</w:tc>`→tab、去標籤、`html.unescape`
  - 章節行：`^(\\d+(?:\\.\\d+)*) (.+?) \\{(\\d{7})\\}$`，且該行不含 `PAGEREF`
    （目次行帶 `PAGEREF`，正文行不帶 —— 以此區分，非以行號）。
    章節行數 407 為**章節標題數**，非物件數，二者不得混用（A-ICS15）
  - 物件屬性頭：`^(\\d{7}): \\[`（區分大小寫；`re.match`，行首先 `strip()`）。
    此正則之命中數即物件母數，實測 **2180**
  - 屬性：同一行以 `\\[([^:\\]]+):([^\\]]*)\\]` 逐段抓取，key 大小寫原樣
    （`ECU` / `Radio` / `EE Architecture` / `Artifact Type` / `State`）
  - 物件本文：屬性頭之次一行（原檔即為一段一行）
  - 軸值：逗號切分後去頭尾空白；**軸不存在時記為 `None`**
    （不視為空集合，亦不以章節標題之屬性代替，R-ICS9(b)）
  - 軸值比對：**區分大小寫之精確字串**集合交集（不作正規化、不作前綴比對）

判準：
  * **v2（預設，R-ICS2 v2(b) —— CFTS020 專用）**
      (i)  `Radio ∋ {R1L, R1L-R, allSys}` ∧ `EE Architecture ∋ {Atlantis High, All}`
      (ii) `ECU` 軸**存在時**須含 `{ICS, LTM}`；**不存在時不視為不適用，
           亦不記 WARN** —— 該軸於本文件本不作區別之用
      故 v2 只有二類判定：`適用` / `不適用`，無 WARN 類。
      強度欄（R-DD24 之「正面命中／WARN」）於 v2 下之取值見 `strength()`。
  * **v1（`--v1`，已作廢，僅供產生 v1→v2 差異表）**
      `ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}`
      ∧ `EE ∋ {Atlantis High, All}`；任一軸缺而無實質落空者標 `WARN-軸缺`。
      **其判準不得引用**（R-ICS2 v1 之作廢註）。

章節分支（1.5 = PowerNet-only、1.8 = PNet & AtlHi & AtlMi）為**輔證**，
不得取代逐物件實測（R-ICS2 v2(c)、R-ICS9(b)）。

用法：
  python3 features/ics_management/scripts/cfts020_probe.py --stats
  python3 features/ics_management/scripts/cfts020_probe.py --stats --v1
  python3 features/ics_management/scripts/cfts020_probe.py --object 4819617
  python3 features/ics_management/scripts/cfts020_probe.py --section 1.8.1.3 --diff
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / ("inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and "
              "DCSD _20260310-1533.docx")

ECU_OK = {"ICS", "LTM"}
# 變體層之分支表：由頂層節標題字面歸類（b11 作業 C 實測，見檔頭）
DUT_VARIANT = "Disassociated"          # R-ICS37(a)，b10 量測
SCOPE_RULED_IN = {"1.18"}              # R-ICS39：§1.18 算數（裁決，非推導）
RADIO_OK = {"R1L", "R1L-R", "allSys"}
EE_OK = {"Atlantis High", "All"}

SEC_RE = re.compile(r"^(\d+(?:\.\d+)*) (.+?) \{(\d{7})\}\s*$")


def variant_of(title: str) -> str:
    """變體層：由頂層節標題字面歸類。不涉軸層、不涉裁決。"""
    if "Silver Box" in title or "Disassociated" in title:
        return "Disassociated"
    if re.search(r"(?<!Dis)Associated", title):
        return "Associated"
    return "未分類"
VARIANT_FIT = {"Disassociated": "Disassociated",
               "Associated": "Associated",
               "未分類": "Unclassified"}


def variant_fit(variant: str) -> str:
    """變體層對 DUT 之關係，**三值**（R-ICS42(b)；b13 作業 A 改此處）。

    b11~b12 此欄為布林 `variant == DUT_VARIANT`，使「未分類」與「Associated」
    同落 `False` 而被併為一桶 —— upstream-11 §4-3 之「87 個 Associated 分支物件」
    因此而誤，實為 §1.4（Common Between Architectures）× 86 ＋ §1.5 × 1（A-ICS81）。

    `Unclassified` 不是「不適用」，而是**無變體歸屬**（架構共通節）；
    其去留與 `Associated` 不同問，不得再合桶。
    """
    return VARIANT_FIT[variant]


OBJ_RE = re.compile(r"^(\d{7}): \[")
ATTR_RE = re.compile(r"\[([^:\]]+):([^\]]*)\]")


def doc_lines() -> list[str]:
    xml = zipfile.ZipFile(DOC).read("word/document.xml").decode("utf8")
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"</w:tc>", "\t", xml)
    return html.unescape(re.sub(r"<[^>]+>", "", xml)).split("\n")


def axis(attrs: dict[str, str], key: str) -> list[str] | None:
    if key not in attrs:
        return None
    return [t.strip() for t in attrs[key].split(",") if t.strip()]


def verdict_v1(o: dict) -> tuple[str, list[str]]:
    """R-ICS2 **v1**（已作廢）之三軸交集判定。僅供 v1→v2 差異表。"""
    miss = []
    if o["ecu"] is None:
        miss.append("ECU 軸不存在於本物件（不以章節屬性代替，R-ICS9(b)）")
    elif not (set(o["ecu"]) & ECU_OK):
        miss.append(f"ECU {o['ecu']} ∩ {sorted(ECU_OK)} = ∅")
    if o["radio"] is None:
        miss.append("Radio 軸不存在")
    elif not (set(o["radio"]) & RADIO_OK):
        miss.append(f"Radio ∩ {sorted(RADIO_OK)} = ∅")
    if o["ee"] is None:
        miss.append("EE 軸不存在")
    elif not (set(o["ee"]) & EE_OK):
        miss.append(f"EE {o['ee']} ∩ {sorted(EE_OK)} = ∅")
    if not miss:
        return "適用", []
    if any("不存在" in m for m in miss) and not any("∅" in m for m in miss):
        return "WARN-軸缺", miss          # R-DD24：落 fallback 者標 WARN
    return "不適用", miss


def verdict_v2(o: dict) -> tuple[str, list[str]]:
    """R-ICS2 **v2(b)**（現行，CFTS020 專用）。

    只有 `適用` / `不適用` 二類，無 WARN 類：ECU 軸不存在時
    依 v2(b)(ii) 明文「不視為不適用，亦不記 WARN」。
    """
    miss = []
    if o["ecu"] is not None and not (set(o["ecu"]) & ECU_OK):
        miss.append(f"ECU {o['ecu']} ∩ {sorted(ECU_OK)} = ∅（v2(b)(ii)：軸存在故須命中）")
    if o["radio"] is None:
        miss.append("Radio 軸不存在（v2(b)(i) 之必要軸，缺即不成立）")
    elif not (set(o["radio"]) & RADIO_OK):
        miss.append(f"Radio {o['radio']} ∩ {sorted(RADIO_OK)} = ∅")
    if o["ee"] is None:
        miss.append("EE 軸不存在（v2(b)(i) 之必要軸，缺即不成立）")
    elif not (set(o["ee"]) & EE_OK):
        miss.append(f"EE {o['ee']} ∩ {sorted(EE_OK)} = ∅")
    return ("適用", []) if not miss else ("不適用", miss)


def strength(o: dict, v: str) -> str:
    """R-DD24 之第四欄「強度」。v2 下無 WARN 類，故以軸齊備與否分級。"""
    if v != "適用":
        return "—"
    if o["ecu"] is not None:
        return "正面命中（三軸齊備且全命中）"
    return "正面命中（ECU 軸缺，依 R-ICS2 v2(b)(ii) 不記 WARN）"


def verdict(o: dict, use_v1: bool = False) -> tuple[str, list[str]]:
    return verdict_v1(o) if use_v1 else verdict_v2(o)


def parse(use_v1: bool = False) -> list[dict]:
    lines = doc_lines()
    objs, section = [], ("", "")
    top_titles: dict[str, str] = {}
    for i, line in enumerate(lines):
        s = line.strip()
        if "PAGEREF" not in s:
            m = SEC_RE.match(s)
            if m:
                section = (m.group(1), f"{m.group(2)} {{{m.group(3)}}}")
                if m.group(1).count(".") == 1:
                    top_titles[m.group(1)] = m.group(2)
                continue
        if OBJ_RE.match(s):
            attrs = dict(ATTR_RE.findall(s))
            body = lines[i + 1].strip() if i + 1 < len(lines) else ""
            o = {
                "id": s[:7],
                "section_no": section[0],
                "section": section[1],
                "artifact_type": attrs.get("Artifact Type", ""),
                "state": attrs.get("State", ""),
                "ecu": axis(attrs, "ECU"),
                "radio": axis(attrs, "Radio"),
                "ee": axis(attrs, "EE Architecture"),
                "text": body,
            }
            o["v1"], o["v1_reasons"] = verdict_v1(o)
            o["v2"], o["v2_reasons"] = verdict_v2(o)
            o["verdict"], o["reasons"] = (
                (o["v1"], o["v1_reasons"]) if use_v1 else (o["v2"], o["v2_reasons"]))
            o["strength"] = strength(o, o["verdict"])
            # ── 三層分列（b11 作業 C；不得合併為單一旗標）──────────
            top = ".".join(o["section_no"].split(".")[:2]) if o["section_no"] else ""
            o["variant"] = variant_of(top_titles.get(top, ""))
            o["variant_fits_dut"] = variant_fit(o["variant"])
            o["scope"] = ("算數（R-ICS39，裁決）" if top in SCOPE_RULED_IN
                          else "隨變體層")
            objs.append(o)
    return objs


def diffs(objs: list[dict]) -> list[dict]:
    """v1 → v2 判定改變者，附轉變原因分類。"""
    out = []
    for o in objs:
        if o["v1"] == o["v2"]:
            continue
        if o["ecu"] is None and o["v2"] == "適用":
            cause = "軸缺（ECU 軸不存在；v1 判不適用/WARN，v2(b)(ii) 不再以此排除）"
        elif o["ecu"] is None:
            cause = "軸缺（ECU 軸不存在；v1 之 WARN 類於 v2 併入實質判定）"
        else:
            cause = "軸值（ECU 軸存在，v1/v2 對其餘軸之處置差異）"
        out.append({**o, "cause": cause})
    return out


def show(o: dict, full: bool) -> None:
    print(f'{o["id"]}  §{o["section_no"] or "-"}  {o["artifact_type"]:32} {o["verdict"]}')
    print(f'    ECU={o["ecu"]}')
    print(f'    Radio={o["radio"]}')
    print(f'    EE={o["ee"]}')
    for r in o["reasons"]:
        print(f'    ! {r}')
    print(f'    v1={o["v1"]}  v2={o["v2"]}  強度={o["strength"]}')
    print(f'    {o["text"] if full else o["text"][:150]}')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--section")
    ap.add_argument("--object")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--v1", action="store_true",
                    help="改用 R-ICS2 v1（已作廢）之判準，僅供差異表對照")
    ap.add_argument("--diff", action="store_true",
                    help="只列 v1→v2 判定改變者")
    a = ap.parse_args()

    objs = parse(use_v1=a.v1)
    print(f"# 判準：R-ICS2 {'v1（已作廢）' if a.v1 else 'v2(b)（現行）'}", file=sys.stderr)
    if a.stats:
        print(f"物件總數 {len(objs)}，相異 id {len({o['id'] for o in objs})}")
        for k in ("ecu", "radio", "ee"):
            print(f"  {k} 軸不存在者 {sum(1 for o in objs if o[k] is None)}")
        from collections import Counter
        print("  v2 判定分佈", dict(Counter(o["v2"] for o in objs)))
        print("  v1 判定分佈", dict(Counter(o["v1"] for o in objs)))
        print(f"  v1→v2 改變者 {len(diffs(objs))}")
        print("  強度分佈", dict(Counter(o["strength"] for o in objs)))
        print("  Artifact Type", dict(Counter(o["artifact_type"] for o in objs)))
        return 0

    sel = objs
    if a.section:
        sel = [o for o in objs if o["section_no"] == a.section
               or o["section_no"].startswith(a.section + ".")]
    if a.object:
        sel = [o for o in objs if o["id"] == a.object]
    if a.diff:
        ids = {d["id"] for d in diffs(objs)}
        sel = [o for o in sel if o["id"] in ids]
    if a.json:
        print(json.dumps(sel, ensure_ascii=False, indent=1))
        return 0
    if not sel:
        print("查無")
        return 1
    for o in sel:
        show(o, a.full)
    return 0


if __name__ == "__main__":
    sys.exit(main())
