#!/usr/bin/env python3
"""107 候選之粗篩（下放包 30 §二，T158）。

`ledger_xref` 之輸出是**材料**不是結論：107 為「跨檔提及同一標的」，
其中多數應為正常（同一 leaf 在 RULINGS 與 ANOMALIES 各被提及一次，本該如此）。
**逐一讀 107 個，成本會全花在確認正常上。**

A-VC20 之特徵：**同一標的、二處皆有內容性描述、而其一說「無」另一說「有」**。
可機械化者為前二項：

  第一層 —— 剔除純引用型（不描述標的之內容者）
  第二層 —— 保留者中，同一標的之二處分別含「無」語彙與「有」語彙者，
            另出高優先清單

**本檔不判定牴觸** —— 只把「該讀的」縮到可讀之數。

self-test 前置（PLAYBOOK §7.1.1）：不過即非零碼退出、不輸出正式結果。

Usage:
    python features/vehicle_category/scripts/xref_triage.py
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
XREF = ROOT / "data/ledger_xref.tsv"
OUT_PRUNED = ROOT / "data/xref_triage_pruned.tsv"
OUT_REVIEW = ROOT / "data/xref_triage_review.tsv"
OUT_PRIORITY = ROOT / "data/xref_triage_priority.tsv"

# ── 第一層之三個剔除類（下放包 30 §2.1 逐字）────────────────────────
# (a) 純編號引用：該行只是指向該標的，不說它是什麼
PURE_REF = re.compile(
    r"(見|依|同|沿|承|據|參|按|援|引|其(?:依據|由來)為|"
    r"見\s*§|R-TM13|待\s*|→)\s*$")
# (b) 清單成員：表格列、項目符號之列舉，其欄位為編號而非描述
LIST_ROW = re.compile(r"^\|[^|]*\|")          # markdown 表格列
BULLET_ID = re.compile(r"^[-*]\s*[`\[]?(§?[\d.]+|[A-Z]-VC\d+|DR-VC\d+)[`\]]?\s*[—:：]?\s*$")
# (c) 交叉指涉：「其標的為 X」「見 X」形態之整行
XREF_LINE = re.compile(r"^\s*[>＞]?\s*(見|參見|詳見|另見|同上|同前)")

# 內容性斷言之標記 —— 該行對標的之**內容**有所說
CONTENT = re.compile(
    r"(逐字|原文|內容|Description|含|載|存|為\s*[「『\"`]|"
    r"僅|只|無|未|不含|沒有|空|文字|摘要|實測|量測|全文)")

# ── 第二層之對立語彙（下放包 30 §2.1 逐字）──────────────────────────
NEG = re.compile(r"(無|未帶|未載|僅存|不含|沒有|零|空|未涵蓋|不存在)")
POS = re.compile(r"(含|有|載|逐字為|存有|寫著|記著|實測.*為|其內容為)")

# ── `resolved` 欄（執行層增設，下放包未列）────────────────────────────
# **R-TM13（既交付者不改原文，加註保留）保證每一個已解之牴觸永遠留在台帳裡** ——
# 舊斷言與其反駁並存，二者之語彙必然對立。故第二層**必然**收進已解案：
# `§3.3`（A-VC5 RESOLVED／REV-01 作廢）即為一例，其對立完全真實而早已了結。
# 本欄不判定「是否已解」—— 只標記該行**是否帶有解決標記**，讓讀表者先看未帶者。
RESOLVED = re.compile(
    r"(RESOLVED|已解|作廢|撤銷|已結|正解|更正|修訂|REV-\d+|見\s*R-VC27)")


def prune_reason(text: str):
    """回傳 (是否剔除, 類別)。保留者類別為空。"""
    t = text.strip()
    if XREF_LINE.match(t):
        return True, "c 交叉指涉"
    if BULLET_ID.match(t):
        return True, "b 清單成員"
    if LIST_ROW.match(t) and not CONTENT.search(t):
        return True, "b 清單成員"
    if not CONTENT.search(t):
        return True, "a 純編號引用"
    if PURE_REF.search(t) and len(t) < 40:
        return True, "a 純編號引用"
    return False, ""


def load():
    rows = []
    with XREF.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            rows.append(r)
    return rows


def triage(rows):
    by_key = defaultdict(list)
    for r in rows:
        by_key[(r["kind"], r["target"])].append(r)
    pruned, review, priority = [], [], []
    for key, rs in by_key.items():
        keep = []
        for r in rs:
            drop, why = prune_reason(r["text"])
            (pruned if drop else keep).append({**r, "prune_class": why})
        # 跨 ≥2 個台帳且**保留者亦跨 ≥2 個台帳**者才需人讀 ——
        # 保留只剩一檔者，其跨檔性來自被剔除的純引用，不構成 A-VC20 之形態。
        files = {r["file"] for r in keep}
        if len(files) >= 2:
            review.extend(keep)
            neg = {r["file"] for r in keep if NEG.search(r["text"])}
            pos = {r["file"] for r in keep if POS.search(r["text"])}
            # 對立須**跨檔**：同一檔內之「有」與「無」多為同一段之正反陳述
            if neg and pos and (neg - pos or pos - neg):
                res_hit = sum(1 for r in keep if RESOLVED.search(r["text"]))
                for r in keep:
                    priority.append({
                        **r,
                        "neg": "yes" if NEG.search(r["text"]) else "",
                        "pos": "yes" if POS.search(r["text"]) else "",
                        "resolved_marks": res_hit,
                    })
    return pruned, review, priority


def self_test(rows):
    ok = True
    # (b) 已知標的 §10.1 —— DR-VC6 之實測佐證欄與 R-VC12 二(a) 二處
    #     皆須落入第一層保留，且該標的須落入第二層高優先
    _, review, priority = triage(rows)
    r101 = [r for r in review if r["target"] == "10.1"]
    files = {r["file"] for r in r101}
    a1 = any("DATA_REQUESTS" in f for f in files) and \
        any("RULINGS" in f for f in files)
    print(f"  self-test 1  (b) §10.1 之二處皆落入第一層保留            "
          f"{'PASS' if a1 else '**FAIL**'}  保留 {len(r101)} 處，檔 {sorted(files)}")
    ok &= a1
    p101 = [r for r in priority if r["target"] == "10.1"]
    a2 = bool(p101)
    print(f"  self-test 2  (b) §10.1 須落入第二層高優先               "
          f"{'PASS' if a2 else '**FAIL**'}  高優先 {len(p101)} 處")
    ok &= a2
    # (a) 反向 —— 一個純編號引用行須被第一層剔除
    probe = "- 其依據為 R-VC12"
    drop, why = prune_reason(probe)
    a3 = drop
    print(f"  self-test 3  (a) 反向 純編號引用行須被剔除              "
          f"{'PASS' if a3 else '**FAIL**'}  {probe!r} → "
          f"{'剔除（' + why + '）' if drop else '**保留**'}")
    ok &= a3
    return ok


def write(path, rows, cols):
    with path.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r.get(c, "")) for c in cols) + "\n")


def main():
    rows = load()
    print("xref_triage —— self-test 前置（PLAYBOOK §7.1.1）")
    if not self_test(rows):
        print("\n**self-test 未全過 —— 不輸出正式結果，非零碼退出。**")
        return 2
    print("  → 三個斷言全過，開始跑正式母體\n")

    pruned, review, priority = triage(rows)
    cols = ["kind", "target", "file", "line", "text"]
    write(OUT_PRUNED, pruned, cols + ["prune_class"])
    write(OUT_REVIEW, review, cols)
    write(OUT_PRIORITY, priority, cols + ["neg", "pos", "resolved_marks"])

    n_rev_t = len({(r["kind"], r["target"]) for r in review})
    n_pri_t = len({(r["kind"], r["target"]) for r in priority})
    print(f"母體：`ledger_xref.tsv` {len(rows)} 處提及")
    print(f"  第一層剔除 {len(pruned)} 處 → {OUT_PRUNED.name}")
    print(f"  第一層保留 {len(review)} 處／**{n_rev_t} 個標的** → {OUT_REVIEW.name}")
    print(f"  第二層高優先 {len(priority)} 處／**{n_pri_t} 個標的** → "
          f"{OUT_PRIORITY.name}")
    from collections import Counter
    print(f"  剔除之類別分布 {dict(Counter(r['prune_class'] for r in pruned))}")
    keys = {(r["kind"], r["target"]): int(r["resolved_marks"]) for r in priority}
    clean = [k for k, v in keys.items() if v == 0]
    print(f"\n  高優先中**無任何解決標記**者 **{len(clean)} 個標的** —— 先讀這些：")
    for k, t in sorted(clean):
        print(f"    [{k}] {t}")
    print(f"  其餘 {n_pri_t - len(clean)} 個標的帶有解決標記"
          f"（RESOLVED／作廢／REV-nn 等）—— R-TM13 使已解案永遠留在台帳裡，"
          f"其對立為真而早已了結。")
    print("\n**本檔不判定牴觸** —— 只把該讀的縮到可讀之數。判斷由人做。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
