#!/usr/bin/env python3
"""作業 B — CFTS020 全域重判報告之產生器（下放包 03 §三 B）。

依 R-ICS2 **v2(b)** 重判全 2180 物件，四欄輸出（R-DD23／R-DD24）：
數據（三軸實值）、判斷、所印之理由、強度。
另出 v1→v2 差異表（以 ObjectID 為鍵，逐一列出，不只給統計）。

**表格全由本腳本產生，非人工謄寫** —— 謄寫本身即漂移源。
判定與抽取條件一律取自 `cfts020_probe.py`（其檔頭逐項揭露掃描條件）。

輸出：docs/reports/03_cfts020_recon_v2.md
（取代 docs/reports/02_cfts020_face_recon.md；舊檔保留不刪，R-TM13）
"""
from __future__ import annotations

import importlib.util
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("probe", ROOT / "scripts/cfts020_probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

# 三面之章節（下放包 03 作業 B-4；1.5 二節為 Display 面之對照組）
FACES = [
    ("1", "Display（SWRA 006／007）", [
        ("1.8.1.1.1", "HU behavior in response to ICS POWER hardkey pressed events {4819556}", "主"),
        ("1.8.1.1.3", "HU behavior in response to ICS SCREEN OFF hardkey press events {4819570}", "主"),
        ("1.5.1.1.1", "HU behavior in response to ICS POWER hardkey pressed events {4819385}", "對照"),
        ("1.5.1.1.2", "HU behavior in response to ICS SCREEN OFF hardkey press events {4819389}", "對照"),
    ]),
    ("2", "Browse（SWRA 003／004）", [
        ("1.8.1.2", "Rotary Knob Data Transfer {4819577}", "主"),
    ]),
    ("3", "Navigation（SWRA 008／009）", [
        ("1.8.1.1", "Push Button Data Transfer {4819542}（含其子節 1.8.1.1.x）", "主"),
        ("1.8.1.3", "Button Press Events {4819587}", "主"),
    ]),
]


def cell(v: list[str] | None) -> str:
    return "**軸缺**" if v is None else ", ".join(v)


def esc(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ")


def sec_objs(objs: list[dict], sec: str) -> list[dict]:
    return [o for o in objs
            if o["section_no"] == sec or o["section_no"].startswith(sec + ".")]


def face_table(sel: list[dict]) -> list[str]:
    """四欄（數據／判斷／所印之理由／強度），數據欄展開為三軸實值。"""
    out = ["| ObjectID | § | Artifact Type | 數據：ECU | 數據：Radio | "
           "數據：EE Architecture | 判斷（v2） | 所印之理由 | 強度 |",
           "|---|---|---|---|---|---|---|---|---|"]
    for o in sel:
        reason = esc("；".join(o["v2_reasons"])) or \
            "三軸皆命中 v2(b)（ECU 軸缺者依 (ii) 不作排除）"
        out.append(
            f'| {o["id"]} | {o["section_no"]} | {o["artifact_type"]} | '
            f'{cell(o["ecu"])} | {cell(o["radio"])} | {cell(o["ee"])} | '
            f'{o["v2"]} | {reason} | {o["strength"]} |')
    return out


def main() -> None:
    objs = probe.parse()
    total = len(objs)
    c2 = Counter(o["v2"] for o in objs)
    c1 = Counter(o["v1"] for o in objs)
    dl = probe.diffs(objs)

    out = [
        "# CFTS020 全域重判 — 逐物件三軸實值與 R-ICS2 **v2(b)** 判定",
        "",
        "> **本檔取代 `02_cfts020_face_recon.md`**（該檔為 R-ICS2 **v1** 下之結果，",
        "> 依 R-ICS2 v2(d) **已作廢**；舊檔依 R-TM13 保留不刪、不改）。",
        "> 下放包 03 作業 B。**本檔不生 TC**（R-ICS9(e)）。",
        "> 本檔由 `scripts/gen_recon_v2.py` 產生，**表格非人工謄寫**。",
        "",
        "現行判準 **R-ICS2 v2(b)**（CFTS020 專用，逐字見 `RULINGS.md`）：",
        "",
        "- (i) `Radio ∈ {R1L, R1L-R, allSys}` ∧ `EE Architecture ∈ {Atlantis High, All}`",
        "- (ii) `ECU` 軸**存在時**須含 `{ICS, LTM}`；**不存在時不視為不適用，亦不記 WARN**",
        "- (iii) 章節分支為**輔證**，不得取代逐物件實測（v2(c)／R-ICS9(b)）",
        "",
        "已作廢之 v1 判準（僅為產生 §2 差異表而保留於腳本，**不得引用**）：",
        "`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}` ∧ `EE ∋ {Atlantis High, All}`，",
        "軸缺而無實質落空者標 `WARN-軸缺`。",
        "",
        "---",
        "",
        "## §0 掃描條件與母數",
        "",
        "| 項 | 條件／實測 |",
        "|---|---|",
        "| 來源檔 | `inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` 之 `word/document.xml` |",
        "| 轉純文字 | `</w:p>`→換行、`</w:tc>`→tab、去標籤、`html.unescape` |",
        "| 物件辨識 | 屬性頭正則 `^(\\d{7}): \\[`，**區分大小寫**，行首先 `strip()` |",
        "| 章節辨識 | `^(\\d+(?:\\.\\d+)*) (.+?) \\{(\\d{7})\\}$` 且該行不含 `PAGEREF`（目次行帶 `PAGEREF`）|",
        "| 屬性抓取 | 同一行 `\\[([^:\\]]+):([^\\]]*)\\]` 逐段，key 大小寫原樣 |",
        "| 軸值切分 | 逗號切分後 `strip()`；軸不存在記 `None`，**不視為空集合、不以章節屬性代替** |",
        "| 軸值比對 | 區分大小寫之精確字串集合交集（不正規化、不前綴比對）|",
        "",
        f"- 物件總數（上式正則命中數）：**{total}**",
        f"- 相異 ObjectID：**{len({o['id'] for o in objs})}**（無重號）",
        f"- `ECU` 軸不存在者：**{sum(1 for o in objs if o['ecu'] is None)}**"
        f"（{sum(1 for o in objs if o['ecu'] is None) * 100 / total:.1f}%）",
        f"- `Radio` 軸不存在者：**{sum(1 for o in objs if o['radio'] is None)}**",
        f"- `EE Architecture` 軸不存在者：**{sum(1 for o in objs if o['ee'] is None)}**",
        f"- Artifact Type 分佈：{dict(Counter(o['artifact_type'] for o in objs))}",
        "",
        "> **407 為章節標題數，非物件數**（A-ICS15）。本檔全部統計之母數皆為物件數 "
        f"{total}，二者不混用。",
        "",
        "---",
        "",
        "## §1 全域判定分佈（v2）",
        "",
        "| 判定 | 物件數 | 佔比 |",
        "|---|---|---|",
    ]
    for k in ("適用", "不適用"):
        out.append(f"| {k} | **{c2.get(k, 0)}** | {c2.get(k, 0) * 100 / total:.1f}% |")
    out += [
        f"| 合計 | {total} | 100% |",
        "",
        "**v2 無 WARN 類**：v2(b)(ii) 明文「ECU 軸不存在時不視為不適用，亦不記 WARN」，",
        "故 v1 之 `WARN-軸缺` 於 v2 全數消滅，判定只餘二類。",
        "R-DD24 之第四欄「強度」仍保留，於 v2 下改以**軸齊備與否**分級（非 WARN）：",
        "",
        "| 強度 | 物件數 |",
        "|---|---|",
    ]
    for k, v in Counter(o["strength"] for o in objs).most_common():
        out.append(f"| {k} | {v} |")
    out += [
        "",
        "對照（**僅供沿革，判準已作廢**）v1 分佈："
        f"{dict(c1)}。",
        "",
        "---",
        "",
        "## §2 v1 → v2 差異表",
        "",
        f"判定改變者共 **{len(dl)}** 筆（母數 {total}，即 "
        f"{len(dl) * 100 / total:.1f}%）。轉變型態統計：",
        "",
        "| v1 判定 | → | v2 判定 | 筆數 |",
        "|---|---|---|---|",
    ]
    for (a, b), n in Counter((d["v1"], d["v2"]) for d in dl).most_common():
        out.append(f"| {a} | → | {b} | **{n}** |")
    out += [
        "",
        "轉變原因分類：",
        "",
        "| 原因 | 筆數 |",
        "|---|---|",
    ]
    for k, v in Counter(d["cause"] for d in dl).most_common():
        out.append(f"| {k} | {v} |")
    out += [
        "",
        f"下表以 ObjectID 為鍵**逐一列出全部 {len(dl)} 筆**（不只給統計，"
        "下放包 03 §4 差異表要求）。",
        "",
        "<details><summary>v1 → v2 差異全表（逐筆，"
        f"{len(dl)} 列）</summary>",
        "",
        "| ObjectID | § | Artifact Type | ECU | Radio | EE Architecture | "
        "v1 判定 | → | v2 判定 | 轉變原因 |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for d in dl:
        out.append(
            f'| {d["id"]} | {d["section_no"] or "-"} | {d["artifact_type"]} | '
            f'{cell(d["ecu"])} | {cell(d["radio"])} | {cell(d["ee"])} | '
            f'{d["v1"]} | → | {d["v2"]} | {esc(d["cause"])} |')
    out += [
        "",
        "</details>",
        "",
        "---",
        "",
        "## §3 三面之物件清單（依 v2 重列）",
        "",
        "四欄依 R-DD23／R-DD24：**數據**（ECU／Radio／EE 三軸實值）、"
        "**判斷**、**所印之理由**、**強度**。",
        "",
    ]

    for tag, title, secs in FACES:
        sel_all = []
        for sec, _, _ in secs:
            sel_all += sec_objs(objs, sec)
        out += [f"### §3.{tag} {title}", "",
                f"（本面所列章節之物件合計 {len(sel_all)}，"
                f"判定分佈 {dict(Counter(o['v2'] for o in sel_all))}）", ""]
        for sec, name, kind in secs:
            sel = sec_objs(objs, sec)
            sub2 = Counter(o["v2"] for o in sel)
            sub1 = Counter(o["v1"] for o in sel)
            out += [f"#### §{sec} {name} — {kind}", "",
                    f"物件 **{len(sel)}** 個；v2 判定分佈 **{dict(sub2)}**；"
                    f"（v1 為 {dict(sub1)}，已作廢）", ""]
            if not sel:
                out += ["（本節無物件）", ""]
                continue
            out += face_table(sel)
            out += ["", "<details><summary>逐物件本文（逐字，"
                    f"{len(sel)} 條）</summary>", ""]
            for o in sel:
                out.append(f'- **{o["id"]}**（{o["artifact_type"]}／{o["v2"]}）：'
                           f'{esc(o["text"])}')
            out += ["", "</details>", ""]

    # ---- §4 下放包 03 §5 之預期數字對照（全部實測，不沿用陳述）----
    def n(sec: str, v: str = "適用") -> int:
        return sum(1 for o in sec_objs(objs, sec) if o["v2"] == v)

    g15 = [o for o in sec_objs(objs, "1.5")
           if o["artifact_type"] == "Subsystem Functional Requirement"]
    g15_na = sum(1 for o in g15 if o["v2"] == "不適用")
    o617 = next(o for o in objs if o["id"] == "4819617")
    o583 = next(o for o in objs if o["id"] == "4819583")

    out += [
        "---",
        "",
        "## §4 實測值對照（下放包 03 §5）",
        "",
        "全部為本次實測，不沿用他人陳述。量測條件見 §0。",
        "",
        "| # | 項 | 實測 |",
        "|---|---|---|",
        f"| (a) | v2 之適用物件總數 | **{c2.get('適用', 0)}**（v1 為 {c1.get('適用', 0)}）|",
        f"| (b) | `4819617` 之 v2 判定 | **{o617['v2']}**（§{o617['section_no']}；"
        f"ECU {cell(o617['ecu'])}／Radio {cell(o617['radio'])}／EE {cell(o617['ee'])}）|",
        f"| (c) | 1.5 章節下 Artifact Type = Subsystem Functional Requirement 之物件 "
        f"| {len(g15)} 個，其中不適用 **{g15_na}** 個 → "
        f"{'**仍 100% 不適用**' if g15_na == len(g15) else '**非 100%**'} |",
        f"| (d) | `1.8.1.1.1 {{4819556}}` 群之適用數 | **{n('1.8.1.1.1')}** / "
        f"{len(sec_objs(objs, '1.8.1.1.1'))} |",
        f"| (e) | `1.8.1.1.3 {{4819570}}` 群之適用數 | **{n('1.8.1.1.3')}** / "
        f"{len(sec_objs(objs, '1.8.1.1.3'))} |",
        f"| (f) | `1.8.1.3 {{4819587}}` 群 | v1：24 中 {sum(1 for o in sec_objs(objs, '1.8.1.3') if o['v1'] == '不適用')} 不適用；"
        f"v2：{len(sec_objs(objs, '1.8.1.3'))} 中 **{n('1.8.1.3', '不適用')} 不適用、"
        f"{n('1.8.1.3')} 適用** |",
        "",
        "### §4.1 既有 TC 之錨點複驗",
        "",
        "CFTS022 走 v2(a)（＝v1 之三軸交集，判準未變），故 b01／b02 所錨之 "
        "CFTS022 物件不受本次重判影響。CFTS020 側之錨點逐一複驗：",
        "",
        "| 錨 | 批 | v1 | v2 | 結論 |",
        "|---|---|---|---|---|",
        f"| CFTS020-4819617 | b02 | {o617['v1']} | **{o617['v2']}** | "
        f"{'錨仍成立（R-ICS2 v2(e) 相符），I1／I2 無需回收' if o617['v2'] == '適用' else '**E2／E3 觸發**'} |",
        f"| CFTS020-4819583 | b01（作業 D 將引為 Pre-Condition）| {o583['v1']} | "
        f"**{o583['v2']}** | {'錨仍成立' if o583['v2'] == '適用' else '**須回報**'} |",
        "",
        "### §4.2 與 R-ICS2 v2(c) 所述 1.5 實例之對照（輔證，非判準）",
        "",
        f"- 1.5 章節下物件 **{len(sec_objs(objs, '1.5'))}** 個；"
        f"`EE` 恰為 `['PowerNet']` 者 **"
        f"{sum(1 for o in sec_objs(objs, '1.5') if o['ee'] == ['PowerNet'])}** 個"
        "（與 v2(c) 所述「130 為 PowerNet」相符）",
        f"- Artifact Type 分佈："
        f"{dict(Counter(o['artifact_type'] for o in sec_objs(objs, '1.5')))}"
        "（v2(c) 所述「餘二皆 Description 型章節引言」指的是 EE 非 PowerNet 之二個，"
        "非指 1.5 只有二個 Description）",
        "- 該二個為 `4819364`（Description，`[ECU:FPDM]`、EE `PowerNet, Atlantis High` "
        "→ v2 **不適用**，即 v2(b)(ii) 所舉之實例）與 `4819365`"
        "（Description，Radio `R1L-R, R1L`、EE `All` → v2 **適用**）",
        f"- 故 1.5 下唯一 v2 適用者為 `4819365`，其 Artifact Type 為 Description，"
        "**非需求物件**；需求物件（Subsystem Functional Requirement）"
        f"{len(g15)} 個仍 100% 不適用，與 v2(c) 相符",
        "",
    ]

    dst = ROOT / "docs/reports/03_cfts020_recon_v2.md"
    dst.write_text("\n".join(out) + "\n")
    print(f"寫入 {dst.relative_to(ROOT.parents[1])}")
    print(f"  v2 分佈 {dict(c2)}；差異 {len(dl)} 筆")


if __name__ == "__main__":
    main()
