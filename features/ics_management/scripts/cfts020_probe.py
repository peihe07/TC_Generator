#!/usr/bin/env python3
"""CFTS020 物件抽取與三軸判定（下放包 02 作業 D／§4 掃描條件）。

抽取條件（逐項揭露）：
  - 自 `inputs/R1LR_Atl-H_26PI1.5 … CFTS_020 ICS and DCSD_20260310-1533.docx`
    之 `word/document.xml`：`</w:p>`→換行、`</w:tc>`→tab、去標籤、`html.unescape`
  - 章節行：`^(\\d+(?:\\.\\d+)*) (.+?) \\{(\\d{7})\\}$`，且不含 `PAGEREF`
    （目次行帶 `PAGEREF`，正文行不帶 —— 以此區分，非以行號）
  - 物件屬性頭：`^(\\d{7}): \\[(.*)\\]$` 之變形，實作以 `^(\\d{7}): \\[` 起判；
    屬性以 `[key:value]` 逐段抓取
  - 物件本文：屬性頭之次一行（原檔即為一段一行）
  - 三軸：`ECU` / `Radio` / `EE Architecture`，逗號切分後去頭尾空白；
    **軸不存在時記為 `None`（不視為空集合，亦不以章節屬性代替，R-ICS9(b)）**

判準（R-ICS2）：`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}`
            ∧ `EE ∋ {Atlantis High, All}`

用法：
  python3 features/ics_management/scripts/cfts020_probe.py --section 1.8.1.4
  python3 features/ics_management/scripts/cfts020_probe.py --object 4819617
  python3 features/ics_management/scripts/cfts020_probe.py --stats
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
RADIO_OK = {"R1L", "R1L-R", "allSys"}
EE_OK = {"Atlantis High", "All"}

SEC_RE = re.compile(r"^(\d+(?:\.\d+)*) (.+?) \{(\d{7})\}\s*$")
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


def verdict(o: dict) -> tuple[str, list[str]]:
    """R-DD23 三欄：判定 + 所印之理由（未命中之判準逐項列出）。"""
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


def parse() -> list[dict]:
    lines = doc_lines()
    objs, section = [], ("", "")
    for i, line in enumerate(lines):
        s = line.strip()
        if "PAGEREF" not in s:
            m = SEC_RE.match(s)
            if m:
                section = (m.group(1), f"{m.group(2)} {{{m.group(3)}}}")
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
            o["verdict"], o["reasons"] = verdict(o)
            objs.append(o)
    return objs


def show(o: dict, full: bool) -> None:
    print(f'{o["id"]}  §{o["section_no"] or "-"}  {o["artifact_type"]:32} {o["verdict"]}')
    print(f'    ECU={o["ecu"]}')
    print(f'    Radio={o["radio"]}')
    print(f'    EE={o["ee"]}')
    for r in o["reasons"]:
        print(f'    ! {r}')
    print(f'    {o["text"] if full else o["text"][:150]}')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--section")
    ap.add_argument("--object")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true")
    a = ap.parse_args()

    objs = parse()
    if a.stats:
        print(f"物件總數 {len(objs)}，相異 id {len({o['id'] for o in objs})}")
        for k in ("ecu", "radio", "ee"):
            print(f"  {k} 軸不存在者 {sum(1 for o in objs if o[k] is None)}")
        from collections import Counter
        print("  判定分佈", dict(Counter(o["verdict"] for o in objs)))
        print("  Artifact Type", dict(Counter(o["artifact_type"] for o in objs)))
        return 0

    sel = objs
    if a.section:
        sel = [o for o in objs if o["section_no"] == a.section
               or o["section_no"].startswith(a.section + ".")]
    if a.object:
        sel = [o for o in objs if o["id"] == a.object]
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
