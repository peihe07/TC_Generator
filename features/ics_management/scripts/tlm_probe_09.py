#!/usr/bin/env python3
"""下放包 09 作業 A —— `TLM` 於 CFTS020 之指涉量測。

問題：CFTS020 §1.18 所稱之 `TLM`，是否即本 DUT（即 §1.8 所稱之 `HU`）？

掃描條件（逐項揭露，見報告 §0）：
  - 物件結構：`importlib` 載入同目錄 `cfts020_probe.py` 之 `parse()`（未改該檔）
  - CFTS022 另以同一 docx 抽取法自行解析（`</w:p>`→換行、`</w:tc>`→tab、
    去 XML 標籤、`html.unescape`）
  - 詞界：`(?<![A-Za-z0-9_])TLM(?![A-Za-z0-9_])`，**區分大小寫**。
    此詞界排除 `HTML`（前接 `M`? 實為 `HTM`+`L`，`TLM` 子字串不存在）、
    排除 `LTM`／`ETM`（字面不同）、排除 `TLM_xxx`／`xxxTLM` 之複合詞
  - `HU` 同法：`(?<![A-Za-z0-9_])HU(?![A-Za-z0-9_])`，排除 `HUD`、`HU_`、`SHU`

本腳本**只列不裁**（R-ICS33(b)）：不寫任何 TC JSON、不改任何錨。

用法：
  python3 features/ics_management/scripts/tlm_probe_09.py            # 全部量測項
  python3 features/ics_management/scripts/tlm_probe_09.py --m1       # 單項
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import re
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

CFTS022 = ROOT / ("inputs/R1LR_Atl-H_26PI2.5 Jun Release-Privacy_CFTS_022 "
                  "Functional Specification_20260608-1205.docx")

# 詞界：不得誤抓 HTML／LTM／ETM／TLM_x 等
TLM_RE = re.compile(r"(?<![A-Za-z0-9_])TLM(?![A-Za-z0-9_])")
HU_RE = re.compile(r"(?<![A-Za-z0-9_])HU(?![A-Za-z0-9_])")
# 寬鬆版：僅供「詞界處理之對照」，證明詞界確有濾掉東西
TLM_LOOSE = re.compile(r"TLM")
HU_LOOSE = re.compile(r"HU")


def load_probe():
    """載入既有 cfts020_probe.py（唯讀使用其 parse()）。"""
    spec = importlib.util.spec_from_file_location(
        "cfts020_probe", HERE / "cfts020_probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def docx_lines(path: Path) -> list[str]:
    """同 cfts020_probe.doc_lines 之抽取法，用於 CFTS022。"""
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf8")
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"</w:tc>", "\t", xml)
    return html.unescape(re.sub(r"<[^>]+>", "", xml)).split("\n")


def sec_top(o: dict) -> str:
    """物件所屬之頂層節（如 1.18.1.2 → 1.18）。"""
    n = o["section_no"]
    parts = n.split(".")
    return ".".join(parts[:2]) if len(parts) >= 2 else (n or "-")


# ----------------------------------------------------------------- 量測項 1
def m1(objs):
    print("=" * 78)
    print("§1 全文出現面：TLM / HU 之出現次數與章節分佈")
    print("=" * 78)
    for name, strict, loose in (("TLM", TLM_RE, TLM_LOOSE), ("HU", HU_RE, HU_LOOSE)):
        hits = [(o, len(strict.findall(o["text"]))) for o in objs]
        hits = [(o, n) for o, n in hits if n]
        loose_n = sum(len(loose.findall(o["text"])) for o in objs)
        strict_n = sum(n for _, n in hits)
        print(f"\n--- `{name}`：帶詞界命中 {strict_n} 次於 {len(hits)} 個物件"
              f"；無詞界（寬鬆）命中 {loose_n} 次 —— 詞界濾掉 {loose_n - strict_n} 次")
        dist = {}
        for o, n in hits:
            dist.setdefault(sec_top(o), [0, 0])
            dist[sec_top(o)][0] += n
            dist[sec_top(o)][1] += 1
        for sec in sorted(dist, key=lambda s: [int(x) for x in s.split(".")]):
            print(f"    §{sec:<8} 次數 {dist[sec][0]:<5} 物件 {dist[sec][1]}")

    # 併現：同一物件內 TLM 與 HU 皆出現
    both = [o for o in objs if TLM_RE.search(o["text"]) and HU_RE.search(o["text"])]
    print(f"\n--- 同一物件內 `TLM` 與 `HU` 併現者：{len(both)} 個")
    for o in both:
        print(f"\n  {o['id']}  §{o['section_no']}  [{o['verdict']}]  "
              f"ECU={o['ecu']}")
        print(f"    逐字：{o['text']}")

    # 併現（寬鬆詞界，供複核詞界是否漏抓）
    both_loose = [o for o in objs
                  if TLM_LOOSE.search(o["text"]) and HU_LOOSE.search(o["text"])]
    print(f"\n--- （對照）寬鬆詞界下併現者：{len(both_loose)} 個"
          f" —— 差 {len(both_loose) - len(both)} 個，逐字如下")
    for o in both_loose:
        if o not in both:
            print(f"  {o['id']} §{o['section_no']}：{o['text'][:200]}")


# ----------------------------------------------------------------- 量測項 2
KEY_FUNCS = [
    ("按鍵訊號之接收/處理", r"[Bb]utton"),
    ("旋鈕訊號之接收/處理", r"[Kk]nob|KNOB"),
    ("畫面/HMI 之決定或管理", r"screen|Screen|HMI"),
    ("browsing list 之管理", r"browsing"),
    ("音量輸出", r"[Vv]olume"),
    ("Mute", r"Mute|mute"),
    ("Screen Off 模式", r'"Screen Off"|Screen Off|Screen On'),
]


def subject(text: str) -> str:
    """粗略主詞判別：取本文中最先出現之 `TLM`／`HU`／`ICS` 詞界命中者。"""
    pos = {}
    for name, rx in (("TLM", TLM_RE), ("HU", HU_RE),
                     ("ICS", re.compile(r"(?<![A-Za-z0-9_])ICS(?![A-Za-z0-9_])"))):
        m = rx.search(text)
        if m:
            pos[name] = m.start()
    if not pos:
        return "-"
    return min(pos, key=pos.get)


def m2(objs):
    print("\n" + "=" * 78)
    print("§2 職能對位：§1.8.1.1／§1.8.1.2（HU 側）vs §1.18.1.2（TLM 側）")
    print("=" * 78)
    hu_side = [o for o in objs
               if o["section_no"].startswith(("1.8.1.1", "1.8.1.2"))]
    tlm_side = [o for o in objs if o["section_no"].startswith("1.18.1.2")]
    print(f"§1.8.1.1+§1.8.1.2 物件 {len(hu_side)} 個"
          f"（主詞 HU {sum(1 for o in hu_side if subject(o['text']) == 'HU')}）")
    print(f"§1.18.1.2 物件 {len(tlm_side)} 個"
          f"（主詞 TLM {sum(1 for o in tlm_side if subject(o['text']) == 'TLM')}）")

    print("\n| 職能 | §1.8 HU 側物件 | §1.18.1.2 TLM 側物件 | 配對 |")
    paired = unpaired = 0
    for label, rx in KEY_FUNCS:
        r = re.compile(rx)
        a = [o["id"] for o in hu_side
             if r.search(o["text"]) and subject(o["text"]) == "HU"]
        b = [o["id"] for o in tlm_side
             if r.search(o["text"]) and subject(o["text"]) == "TLM"]
        ok = "同職能不同主詞名" if (a and b) else ("僅一側" if (a or b) else "皆無")
        if a and b:
            paired += 1
        elif a or b:
            unpaired += 1
        print(f"| {label} | {', '.join(a) or '無'} | {', '.join(b) or '無'} | {ok} |")
    print(f"\n配對數 {paired}；未配對數 {unpaired}")

    print("\n--- §1.18.1.2 全物件逐字（主詞標註）")
    for o in tlm_side:
        print(f"\n  {o['id']} §{o['section_no']} [{o['verdict']}] 主詞={subject(o['text'])}")
        print(f"    {o['text']}")


# ----------------------------------------------------------------- 量測項 3
HOST_FUNCS = [
    ("畫面（screen）", re.compile(r"screen", re.I)),
    ('"Screen Off" 模式', re.compile(r"Screen Off")),
    ("browsing lists", re.compile(r"browsing", re.I)),
    ("音量輸出（volume）", re.compile(r"volume", re.I)),
    ("HMI", re.compile(r"HMI")),
    ("audio/media 來源", re.compile(r"audio|media|source", re.I)),
]


def m3(objs):
    print("\n" + "=" * 78)
    print("§3 主機專屬職能之持有：TLM 是否具備畫面/Screen Off/browsing/音量")
    print("=" * 78)
    tlm_objs = [o for o in objs if TLM_RE.search(o["text"])]
    for label, rx in HOST_FUNCS:
        hit = [o for o in tlm_objs if rx.search(o["text"])]
        print(f"\n--- {label}：TLM 物件中 {len(hit)} 個命中")
        for o in hit:
            print(f"  {o['id']} §{o['section_no']} [{o['verdict']}]：{o['text']}")


# ----------------------------------------------------------------- 量測項 4
def m4(objs):
    print("\n" + "=" * 78)
    print("§4 ECU 屬性面：CFTS020／CFTS022 之 ECU 值域中是否有 TLM")
    print("=" * 78)
    vals = {}
    for o in objs:
        for v in (o["ecu"] or []):
            vals[v] = vals.get(v, 0) + 1
    print("CFTS020 ECU 值域（值：帶該值之物件數）：")
    for v in sorted(vals, key=lambda k: -vals[k]):
        print(f"    {v:<20} {vals[v]}")
    print(f"  → `TLM` 是否於 CFTS020 之 ECU 值域出現："
          f"{'是' if 'TLM' in vals else '否（查無）'}")

    # CFTS022
    lines = docx_lines(CFTS022)
    attr_re = re.compile(r"\[([^:\]]+):([^\]]*)\]")
    obj_re = re.compile(r"^(\d{7}): \[")
    vals22 = {}
    n22 = 0
    for line in lines:
        s = line.strip()
        if obj_re.match(s):
            n22 += 1
            attrs = dict(attr_re.findall(s))
            for v in [t.strip() for t in attrs.get("ECU", "").split(",") if t.strip()]:
                vals22[v] = vals22.get(v, 0) + 1
    print(f"\nCFTS022 物件數 {n22}；ECU 值域：")
    for v in sorted(vals22, key=lambda k: -vals22[k]):
        print(f"    {v:<20} {vals22[v]}")
    print(f"  → `TLM` 是否於 CFTS022 之 ECU 值域出現："
          f"{'是' if 'TLM' in vals22 else '否（查無）'}")

    # CFTS022 全文之 TLM 詞界命中
    t22 = sum(len(TLM_RE.findall(l)) for l in lines)
    h22 = sum(len(HU_RE.findall(l)) for l in lines)
    print(f"\nCFTS022 全文（含目次與表格）：`TLM` 詞界命中 {t22} 次；"
          f"`HU` 詞界命中 {h22} 次")
    for l in lines:
        if TLM_RE.search(l):
            print(f"    逐字：{l.strip()[:300]}")


# ----------------------------------------------------------------- 量測項 5
def m5(objs):
    print("\n" + "=" * 78)
    print("§5 反向查核：§1.18 是否有任何物件之主詞為 HU")
    print("=" * 78)
    s118 = [o for o in objs if o["section_no"].startswith("1.18")]
    print(f"§1.18 物件總數 {len(s118)}（適用 "
          f"{sum(1 for o in s118 if o['verdict'] == '適用')}）")
    hu_hit = [o for o in s118 if HU_RE.search(o["text"])]
    print(f"§1.18 內含詞界 `HU` 之物件：{len(hu_hit)} 個")
    for o in hu_hit:
        print(f"  {o['id']} §{o['section_no']} [{o['verdict']}] "
              f"主詞={subject(o['text'])}：{o['text']}")
    # 反向：§1.8 內含 TLM 者
    s18 = [o for o in objs if o["section_no"].startswith("1.8")]
    tlm_hit = [o for o in s18 if TLM_RE.search(o["text"])]
    print(f"\n（反向）§1.8 內含詞界 `TLM` 之物件：{len(tlm_hit)} 個")
    for o in tlm_hit:
        print(f"  {o['id']} §{o['section_no']} [{o['verdict']}] "
              f"主詞={subject(o['text'])}：{o['text'][:300]}")


def main() -> int:
    ap = argparse.ArgumentParser()
    for k in ("m1", "m2", "m3", "m4", "m5"):
        ap.add_argument(f"--{k}", action="store_true")
    a = ap.parse_args()
    sel = [k for k in ("m1", "m2", "m3", "m4", "m5") if getattr(a, k)]
    objs = load_probe().parse()
    print(f"CFTS020 物件母數：{len(objs)}")
    for k in (sel or ["m1", "m2", "m3", "m4", "m5"]):
        globals()[k](objs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
