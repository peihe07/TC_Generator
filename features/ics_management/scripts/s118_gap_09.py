#!/usr/bin/env python3
"""下放包 09 作業 B —— §1.18 獨有行為面之覆蓋缺口清點（實測層）。

只做**可機器複現之量測**，不作裁決、不生成任何 TC。
輸出供 `docs/reports/09_s118_coverage_gap.md` §1／§2 之表格覆核。

量測內容
--------
1. §1.18 全節物件數／判適用數（R-ICS2 v2(b)，載 `cfts020_probe.parse()`，不改該檔）
2. 現有 TC 之母數與其 `specification_reference` 之相異錨集合
3. 每一判適用物件之「行為 token」與其在 27 條 TC 驗證文字中之命中情形
   - 行為 token 抽取（逐項揭露，全為正則，不作語意判讀）：
       · `\\$[A-Za-z0-9_<>]+\\$`            —— LID／訊號符號
       · `\\b[A-Z][A-Z0-9_]{4,}\\b`          —— 全大寫訊息／狀態名（如 CLIMATIC_PANEL）
       · `"([^"]+)"`                        —— 逐字定值（如 "Pressed"）
       · `\\bT[A-Za-z][A-Za-z0-9_]*\\b`      —— 時間符號（如 Tbutton）
     去除停用詞（見 `STOP`），避免 ICS／TLM／CAN 等泛用大寫詞污染比對
4. TC 驗證文字 = `test_item` + `test_procedure` + `expected_result` 三欄串接
   （**不含** `reasoning`／`pre_conditions`／`tc_title` —— 覆蓋須「實際驗到」，
     前置條件與理由欄不算驗證行為，判準見報告 §0）

用法：
  python3 features/ics_management/scripts/s118_gap_09.py            # 摘要
  python3 features/ics_management/scripts/s118_gap_09.py --objects  # 逐物件表
  python3 features/ics_management/scripts/s118_gap_09.py --tcs      # TC 清單
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "scripts" / "cfts020_probe.py"

# 泛用大寫詞：出現於幾乎每個物件，作為比對 token 無鑑別力，故排除
STOP = {
    "CFTS", "ICS", "TLM", "HMI", "LIDS", "CSTACK", "BHCAN", "CLIMATIC",
    "PANEL", "PLEASE", "SHALL", "SIGNAL", "SIGNALS", "SCREEN", "SCREENS",
}

TOK_PATTERNS = [
    re.compile(r"\$[A-Za-z0-9_<>]+\$"),
    re.compile(r"\b[A-Z][A-Z0-9_]{4,}\b"),
    re.compile(r'"([^"]+)"'),
    re.compile(r"\bT[A-Za-z][A-Za-z0-9_]{3,}\b"),
]


def load_probe():
    spec = importlib.util.spec_from_file_location("cfts020_probe", PROBE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def tokens(text: str) -> set[str]:
    out: set[str] = set()
    for pat in TOK_PATTERNS:
        for m in pat.finditer(text):
            tok = m.group(1) if m.lastindex else m.group(0)
            if tok.upper().strip("$_") in STOP:
                continue
            out.add(tok)
    return out


def norm(sig: str) -> str:
    """訊號符號之比對正規化：去 `$`、去 `<n>` 索引、轉小寫。

    §1.18 母條寫 `$ICS_KNOB<n>_DIR$`，TC 逐字寫 `$ICS_KNOB2_DIR$`／
    `Radio_Knob2_DIR`；`<n>`→`` 後以 `knob_dir` 之片段比對可對上。
    """
    s = sig.strip("$").replace("<n>", "").replace("<N>", "")
    return re.sub(r"[^a-z0-9]", "", s.lower())


def load_tcs() -> list[dict]:
    tcs = []
    for f in sorted((ROOT / "generated").glob("b0*/b0*_tcs.json")):
        data = json.loads(f.read_text(encoding="utf8"))
        for i, t in enumerate(data["tcs"], 1):
            tcs.append({
                "batch": data["batch"],
                "no": f'{data["batch"]}-{i:02d}',
                "req_id": t["req_id"],
                "title": t["tc_title"],
                "anchors": [a.strip() for a in
                            str(t.get("specification_reference", "")).split("\n") if a.strip()],
                "verify_text": "\n".join([
                    t.get("test_item", ""),
                    t.get("test_procedure", ""),
                    t.get("expected_result", ""),
                ]),
            })
    return tcs


def hits(obj_toks: set[str], tcs: list[dict]) -> dict[str, list[str]]:
    """每個 token 命中之 TC 編號（正規化後之子字串比對）。"""
    res = {}
    for tok in sorted(obj_toks):
        n = norm(tok)
        if len(n) < 4:
            continue
        res[tok] = [t["no"] for t in tcs if n in norm(t["verify_text"])]
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--objects", action="store_true")
    ap.add_argument("--tcs", action="store_true")
    args = ap.parse_args()

    probe = load_probe()
    objs = probe.parse()
    s118 = [o for o in objs if o["section_no"].startswith("1.18")]
    app = [o for o in s118 if o["verdict"] == "適用"]
    tcs = load_tcs()

    anchors = sorted({a for t in tcs for a in t["anchors"]})
    s118_ids = {o["id"] for o in s118}
    anchored_s118 = [a for a in anchors if a.split("-")[-1] in s118_ids]

    print(f"§1.18 物件數={len(s118)}  判適用={len(app)}  判不適用={len(s118) - len(app)}")
    print(f"現有 TC 數={len(tcs)}  相異錨={len(anchors)}  其中指向 §1.18 物件者={len(anchored_s118)}")
    print(f"不適用之 §1.18 物件：{sorted(s118_ids - {o['id'] for o in app})}")

    if args.tcs:
        print("\n== TC 清單 ==")
        for t in tcs:
            print(f'{t["no"]}  {t["req_id"]}  {t["title"]}  錨={",".join(t["anchors"])}')

    if args.objects:
        print("\n== 逐物件 token 命中 ==")
        for o in app:
            toks = tokens(o["text"])
            h = hits(toks, tcs)
            full = [t["no"] for t in tcs
                    if h and all(t["no"] in v for v in h.values() if v is not None)]
            covered = sorted({n for v in h.values() for n in v})
            print(f'\n{o["id"]}  §{o["section_no"]}  {o["artifact_type"]}')
            print(f'  text: {o["text"][:180]}')
            print(f'  tokens: {sorted(toks)}')
            for tok, v in h.items():
                print(f'    {tok:36} -> {v if v else "無 TC 命中"}')
            print(f'  任一 token 命中之 TC: {covered}')
            print(f'  全 token 同時命中之 TC: {full}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
