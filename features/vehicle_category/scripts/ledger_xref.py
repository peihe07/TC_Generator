#!/usr/bin/env python3
"""台帳交叉索引（下放包 29 §4.1，T155）。

**由來**：A-VC20 —— `DATA_REQUESTS.md` 之 DR-VC6「實測佐證（T17）」欄
自始逐字記著 §10.1／§10.2 存有二句文字，而 R-VC12 二(a) 與表 B 同期
寫成「未帶文字」。**同一 repo 內，正解與錯解並存了 24 個包**，
而被引用的是錯的那一份。

**教訓不是「要重測」**（那是 R-VC12 之教訓，且 REV-14 已證條文攔不住）——
是**既有台帳之互相牴觸也要有人看見，而現在沒有東西在看**。

**本檔不偵測矛盾** —— 那需要語意判斷。
它做的是**把同一標的的所有記載並列**（檔名＋行號＋該行原文），
使判斷不再需要靠記性去拼。判斷仍由人做。

**⚠ 盲區（下放包 31 §4.3，逐字）**：

本工具與其粗篩之偵測範圍為**跨檔**。
同一檔內、尤其同一條目內之牴觸，**全盲**。
R-VC12 二(a) 之所以被發現，是因其恰好跨檔（DR-VC6 記對、RULINGS 記錯）；
同型而不跨檔者不會被發現。其補網為 PLAYBOOK 之加註內款複核（紀律，無承載者）。


self-test 前置（PLAYBOOK §7.1.1）：不過即非零碼退出、不輸出正式結果。

Usage:
    python features/vehicle_category/scripts/ledger_xref.py
    python features/vehicle_category/scripts/ledger_xref.py --target §10.1
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGERS = [
    ROOT / "RULINGS.md",
    ROOT / "ANOMALIES.md",
    ROOT / "DATA_REQUESTS.md",
    ROOT / "DECISIONS.md",
    ROOT / "docs/REVISIONS.md",
    ROOT / "framework.md",
    ROOT / "data/tableB_draft.md",
    ROOT / "docs/TABLE_A_frop_crossdomain.md",
    ROOT.parent.parent / "docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md",
]
OUT_XREF = ROOT / "data/ledger_xref.tsv"
OUT_CAND = ROOT / "data/ledger_conflicts_candidates.tsv"

# 標的之四類。**節號須避免吃到版本號與日期** —— `R1_SR24`、`2026-08-27`
# 之類不是節號，故要求其前為 `§` 或行首之列表記號。
# `§n` 之前若有 `IN`／`FO`／`PLAYBOOK`／`下放包 29` 之類的擁有者，那是
# **他文件之節號**，非本 feature 之規格節。
#
# ⚠ **改為剔除（下放包 31 §三，T162）。** 上一版只記 `owner` 欄而不剔除
# —— 於是噪音照樣進候選表。**上繳包 30 §4(3) 把成因寫成「正則吃不到」，
# 那是錯的**：正則一直吃得到（`A-VC21` 之行實測 `owner=下放包`），
# **是標了而未用**。該誤述之形態同 PLAYBOOK §7.4：看到症狀就推因，沒去驗。
#
# 本次**只動這一個變數**（下放包 31 §3.2）：owner 命中之 section 提及**不記錄**。
# `NEG`／`POS` 語彙表與第一層剔除類別**一律不動**，否則差異表歸因不明。
OWNER = re.compile(r"(IN|FO|PLAYBOOK|canon|下放包|上繳包|包)\s*(?:\d+\s*)?§\s*$")
PATS = {
    "section": re.compile(r"§(\d+(?:\.\d+)*)"),
    "leaf": re.compile(r"\b(SWE1-HMI-VC-\d{3}(?:-\d{2})?)\b"),
    "dr": re.compile(r"\b(DR-VC\d+)\b"),
    "anomaly": re.compile(r"\b(A-VC\d+)\b"),
    "ruling": re.compile(r"\b(R-VC\d+)\b"),
    "revision": re.compile(r"\b(REV-\d+)\b"),
}


def scan():
    """(kind, target) -> [(檔名, 行號, 該行原文, owner), …]

    第二回傳值為**被 owner 剔除者**（他文件之節號），供差異表列名。
    """
    hits = defaultdict(list)
    excluded = []
    for p in LEDGERS:
        if not p.exists():
            continue
        try:
            rel = str(p.relative_to(ROOT))
        except ValueError:
            rel = str(p.relative_to(ROOT.parent.parent))
        for i, line in enumerate(p.read_text("utf-8").splitlines(), 1):
            for kind, pat in PATS.items():
                for m in pat.finditer(line):
                    key = (kind, m.group(1))
                    own = ""
                    if kind == "section":
                        mo = OWNER.search(line[:m.start() + 1])
                        if mo:
                            excluded.append((rel, i, m.group(1), mo.group(1)))
                            continue          # ← 剔除，不記錄

                    # 同一行同一標的重複出現只記一次
                    if hits[key] and hits[key][-1][:2] == (rel, i):
                        continue
                    hits[key].append((rel, i, line.strip(), own))
    return hits, excluded


def self_test(hits, excluded):
    """(b) 已知標的 §10.1 —— 應同時列出 DR-VC6 之實測佐證欄與 R-VC12 二(a)。
       (a) 反向 —— 一個不存在之節號應零命中。"""
    ok = True
    rows = hits.get(("section", "10.1"), [])
    files = {r[0] for r in rows}
    has_dr = any("DATA_REQUESTS" in f for f in files)
    has_rul = any("RULINGS" in f for f in files)
    a1 = has_dr and has_rul
    print(f"  self-test 1  (b) §10.1 應同時出現於 DATA_REQUESTS 與 RULINGS  "
          f"{'PASS' if a1 else '**FAIL**'}  命中 {len(rows)} 處，檔 {sorted(files)}")
    ok &= a1
    ghost = hits.get(("section", "99.99"), [])
    a2 = not ghost
    print(f"  self-test 2  (a) 反向 §99.99 應零命中                        "
          f"{'PASS' if a2 else '**FAIL**'}  命中 {len(ghost)} 處")
    ok &= a2
    # (a) 反向之二：本檔若把「並列」誤寫成「只取第一處」，斷言 1 仍會過。
    # 故另驗一個已知多處者之筆數 —— R-VC12 至少出現於 RULINGS 與 ANOMALIES。
    r12 = hits.get(("ruling", "R-VC12"), [])
    a3 = len({r[0] for r in r12}) >= 2
    print(f"  self-test 3  (b) R-VC12 應跨 ≥2 個台帳                       "
          f"{'PASS' if a3 else '**FAIL**'}  檔 {sorted({r[0] for r in r12})}")
    ok &= a3
    # ── T162 之二個斷言（下放包 31 §三）────────────────────────────
    # (b) 已知標的：A-VC21 正文之「下放包 29 §3.3」須被判為 owner 並剔除
    a4 = any(f.endswith("ANOMALIES.md") and t == "3.3" and o == "下放包"
             for f, _, t, o in excluded)
    print(f"  self-test 4  (b) 「下放包 29 §3.3」須被判 owner 並剔除      "
          f"{'PASS' if a4 else '**FAIL**'}  剔除總數 {len(excluded)}")
    ok &= a4
    # (a) 反向：ANOMALIES 中之裸 `§3.3`（A-VC5 之本文）須**保留**
    kept = [r for r in hits.get(("section", "3.3"), [])
            if r[0].endswith("ANOMALIES.md")]
    a5 = bool(kept)
    print(f"  self-test 5  (a) 反向 裸 §3.3（A-VC5 本文）須保留          "
          f"{'PASS' if a5 else '**FAIL**'}  保留 {len(kept)} 處")
    ok &= a5
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--target", help="只看單一標的，如 §10.1 或 R-VC12")
    args = ap.parse_args()

    hits, excluded = scan()
    print("ledger_xref —— self-test 前置（PLAYBOOK §7.1.1）")
    if not self_test(hits, excluded):
        print("\n**self-test 未全過 —— 不輸出正式結果，非零碼退出。**")
        return 2
    print("  → 五個斷言全過，開始跑正式母體\n")

    if args.target:
        t = args.target.lstrip("§")
        for (kind, key), rows in sorted(hits.items()):
            if key == t:
                print(f"=== [{kind}] {key} —— {len(rows)} 處")
                for f, i, line, own in rows:
                    tag = f"[{own} §]" if own else "[裸 §]"
                    print(f"  {f}:{i} {tag}\n    {line[:200]}")
        return 0

    with OUT_XREF.open("w", encoding="utf-8") as fh:
        fh.write("kind\ttarget\towner\tfile\tline\ttext\n")
        for (kind, key), rows in sorted(hits.items()):
            for f, i, line, own in rows:
                fh.write(f"{kind}\t{key}\t{own}\t{f}\t{i}\t{line[:400]}\n")

    # 候選 = 同一標的**跨二個以上台帳**被提及者。
    # 同一檔內之多次提及不入候選 —— 那通常是同一段落之上下文，
    # 而 A-VC20 之形態是**跨檔**（DR 檔記對、RULINGS 記錯）。
    cand = {k: v for k, v in hits.items() if len({r[0] for r in v}) >= 2}
    with OUT_CAND.open("w", encoding="utf-8") as fh:
        fh.write("kind\ttarget\tbare_section\tn_files\tn_mentions\tfiles\n")
        for (kind, key), rows in sorted(
                cand.items(), key=lambda x: (-len({r[0] for r in x[1]}), x[0])):
            files = sorted({r[0] for r in rows})
            # owner 命中者已於 scan() 剔除，故此欄恆為 yes；保留欄位以免下游改格式。
            bare = "yes"
            fh.write(f"{kind}\t{key}\t{bare}\t{len(files)}\t{len(rows)}\t"
                     f"{'; '.join(files)}\n")

    from collections import Counter
    kinds = Counter(k for k, _ in hits)
    from collections import Counter as _C2
    print(f"標的 {len(hits)} 個（{dict(kinds)}）；提及 "
          f"{sum(len(v) for v in hits.values())} 處")
    print(f"**owner 剔除（他文件之節號）{len(excluded)} 處** —— "
          f"擁有者分布 {dict(_C2(o for _, _, _, o in excluded))}")
    print(f"→ {OUT_XREF.relative_to(ROOT)}")
    print(f"**跨 ≥2 個台帳之候選 {len(cand)} 個** → "
          f"{OUT_CAND.relative_to(ROOT)}")
    print("\n**本檔不判斷是否牴觸** —— 只並列。判斷由人做。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
