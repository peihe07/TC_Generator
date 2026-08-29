#!/usr/bin/env python3
"""作業 D — CFTS020 三面偵察報告之產生器（下放包 02 §三 D）。

逐物件輸出 ObjectID／Artifact Type／ECU／Radio／EE 三軸實值與 R-ICS2 判定，
判定與理由取自 `cfts020_probe.py`（R-DD23 三欄、R-DD24 WARN）。
**表格由本腳本產生，非人工謄寫** —— 謄寫本身即漂移源。

輸出：docs/reports/02_cfts020_face_recon.md
"""
from __future__ import annotations

import importlib.util
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("probe", ROOT / "scripts/cfts020_probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

FACES = [
    ("A", "Display Control（SWRA 006／007／(011)）", [
        ("1.5.1.1.1", "HU behavior in response to ICS POWER hardkey pressed events {4819385}"),
        ("1.5.1.1.2", "HU behavior in response to ICS SCREEN OFF hardkey press events {4819389}"),
        ("1.8.1.1.1", "HU behavior in response to ICS POWER hardkey pressed events {4819556}"),
        ("1.8.1.1.3", "HU behavior in response to ICS SCREEN OFF hardkey press events {4819570}"),
    ]),
    ("B", "Browse Control（SWRA 003／004）", [
        ("1.8.1.2", "Rotary Knob Data Transfer {4819577}"),
    ]),
    ("C", "Menu Navigation（SWRA 008／009）", [
        ("1.8.1.1", "Push Button Data Transfer {4819542}（僅 Enter／Back 相關物件另標）"),
        ("1.8.1.3", "Button Press Events {4819587}"),
    ]),
]


def cell(v: list[str] | None) -> str:
    return "**軸缺**" if v is None else ", ".join(v)


def esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def main() -> None:
    objs = probe.parse()
    by_sec: dict[str, list[dict]] = {}
    for o in objs:
        by_sec.setdefault(o["section_no"], []).append(o)

    out = ["# CFTS020 三面偵察 — 逐物件三軸實值與 R-ICS2 判定",
           "",
           "> 下放包 02 作業 D。**不生 TC**（R-ICS9(e)）。",
           "> 本檔由 `scripts/gen_face_recon.py` 產生，表格非人工謄寫。",
           "> 抽取與判定條件見 `scripts/cfts020_probe.py` 檔頭。",
           "> 判準（R-ICS2）：`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}`",
           "> ∧ `EE ∋ {Atlantis High, All}`。軸不存在者標 **WARN-軸缺**，",
           "> 不以章節標題之屬性代替（R-ICS9(b)）。",
           ""]

    total = len(objs)
    c = Counter(o["verdict"] for o in objs)
    out += ["## §0 全文件母數（掃描條件見上）", "",
            f"- 物件總數 **{total}**，相異 ObjectID **{len({o['id'] for o in objs})}**",
            f"- `ECU` 軸不存在者 **{sum(1 for o in objs if o['ecu'] is None)}**"
            f"（{sum(1 for o in objs if o['ecu'] is None) * 100 // total}%）",
            f"- `Radio` 軸不存在 **{sum(1 for o in objs if o['radio'] is None)}**、"
            f"`EE Architecture` 軸不存在 **{sum(1 for o in objs if o['ee'] is None)}**",
            f"- 判定分佈：{dict(c)}",
            f"- Artifact Type：{dict(Counter(o['artifact_type'] for o in objs))}",
            ""]

    for tag, title, secs in FACES:
        out += [f"## §{tag} {title}", ""]
        for sec, name in secs:
            sel = [o for o in objs if o["section_no"] == sec
                   or o["section_no"].startswith(sec + ".")]
            sub = Counter(o["verdict"] for o in sel)
            out += [f"### §{sec} {name}", "",
                    f"物件 {len(sel)} 個，判定分佈 {dict(sub)}", ""]
            if not sel:
                out += ["（本節無物件）", ""]
                continue
            out += ["| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | 判定 | 未命中之判準 |",
                    "|---|---|---|---|---|---|---|---|"]
            for o in sel:
                out.append(
                    f'| {o["id"]} | {o["section_no"]} | {o["artifact_type"]} | '
                    f'{cell(o["ecu"])} | {cell(o["radio"])} | {cell(o["ee"])} | '
                    f'{o["verdict"]} | {esc("；".join(o["reasons"])) or "—"} |')
            out += ["", "<details><summary>逐物件本文（逐字）</summary>", ""]
            for o in sel:
                out.append(f'- **{o["id"]}**（{o["artifact_type"]}）：{esc(o["text"])}')
            out += ["", "</details>", ""]

    Path(ROOT / "docs/reports/02_cfts020_face_recon.md").write_text("\n".join(out) + "\n")
    print("寫入 docs/reports/02_cfts020_face_recon.md，"
          f"共 {sum(len([o for o in objs if o['section_no']==s or o['section_no'].startswith(s+'.')]) for _,_,ss in FACES for s,_ in ss)} 物件列")


if __name__ == "__main__":
    main()
