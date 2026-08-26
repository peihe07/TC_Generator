#!/usr/bin/env python3
"""CONT 表之二層防護（下放包 20a）。

`CONT` 表（`data/cont_table.tsv`）記「037 之片段出自 SYS1 之完整句」者，
供收斂條件第 16 項比對。上繳包 16 §9 已揭露其二個風險：

  1. **該進表的沒進表** —— 新批次之續行型／指涉型 leaf 未登記，
     第 16 項對其 N/A，片段上半無人攔。
  2. **表之內容錯** —— 登記之 SYS1 節指錯，第 16 項拿錯的來源比對。

本檔以二層解之：第一層候選偵測（風險 1）、第二層內容驗證（風險 2）。

**self-test 前置**（PLAYBOOK §7.1.1，下放包 20 §1.1）——
main 先跑四個斷言，任一不過即非零碼退出且**不輸出正式結果**。
「先」由紀律變為程式結構。
"""
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"
S1 = ROOT / ("inputs/SYS1_HMI_Vehicle_Category_HMI_Logic_and_Flow_"
             "R1_SR24_Post_2A_(December_27_2023).xlsx")
CONT = ROOT / "data/cont_table.tsv"
EXCL = ROOT / "data/cont_exclusions.tsv"
# 列冊 —— 候選已被看見且歸屬於未來批次，其判定隨該批勘查為之。
# 與排除清單之別：排除者為「已判定非此類」，列冊者為「已看見、待判定」。
# 二者皆使「已考慮過」與「沒看到」可區分（20a §2.1）。
DEFER = ROOT / "data/cont_deferred.tsv"

# 條號前綴樣式表 —— **第一層 (a) 與第二層共用同一張**（20a §2.2 註：
# 二處不得分歧，承機讀行之同一原則）。
PREFIX = re.compile(r"^\s*(?:[A-Z]{1,4}\d[\d.]*\s*\)|\d[\d.]*\s*\))\s*")
PRONOUN = re.compile(r"^(It|They|This|These|That|Those)\b")
# `short` 已自 CONT 候選移除（下放包 21 §三）——
# 其對 CONT 而言是偽陽性（完整短句非片段），對 profile §8 才是真陽性候選。
# 本檔仍掃它，但**輸出至 `data/short_source_leaves.tsv`**，不進候選判定。
# 60 字元之耦合隨之解除：CONT 不再用該數字，該清單即 §8 之清單。
SHORT = 60
SHORT_OUT = ROOT / "data/short_source_leaves.tsv"


def strip_prefix(s):
    return PREFIX.sub("", s.strip()).strip()


def norm(s):
    """**沿用第 7b 項之同一正規化**（下放包 21 §二，丁案）：
    去條號前綴 ＋ 小寫 ＋ 去標點 ＋ 壓縮空白。

    全案自此只有一套正規化 —— 第二層原本自帶「首字母正規化」，
    與第 7b 之定義是二套；丁之後合一（承機讀行與前綴樣式表之同一原則：
    單一來源，二處必分歧）。

    `013-02` 之改寫（`, and` → `.`）**恰好全落在標點層** ——
    去標點後其片段回復為 SYS1 之純前段，子串成立。
    """
    s = strip_prefix(s).lower()
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load_037():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    out = {}
    for r in list(wb["Analysis Report"].iter_rows(values_only=True))[7:]:
        if r[0] not in (None, ""):
            out[str(r[0]).strip()] = (str(r[2]).split("\n")[0].strip(),
                                      str(r[4]).strip())
    return out


def load_sys1():
    wb = openpyxl.load_workbook(S1, read_only=True, data_only=True)
    rows = list(wb["Basic Report"].iter_rows(values_only=True))
    h = [str(c).strip() if c else "" for c in rows[0]]
    oi, di = h.index("Outline Number"), h.index("Description")
    out = {}
    for r in rows[1:]:
        o = str(r[oi]).strip() if r[oi] else ""
        if o:
            out[o] = ((str(r[di]) if r[di] else "")
                      .replace("_x000D_\n", "\n").replace("_x000D_", " "))
    return out


def read_tsv(p):
    if not p.exists():
        return []
    lines = p.read_text("utf-8").splitlines()
    if len(lines) < 2:
        return []
    head = lines[0].split("\t")
    return [dict(zip(head, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def classify(desc):
    """回傳命中之候選特徵（可多個），空 list 表非候選。"""
    s = strip_prefix(desc)
    hits = []
    if s and s[0].islower():
        hits.append("continuation")
    if PRONOUN.match(s):
        hits.append("reference")
    return hits                      # `short` 已移出（下放包 21 §三）


def layer1(src, cont_leaves, excl_leaves, defer_leaves=frozenset()):
    """候選偵測 —— 候選 ∉ CONT ∧ ∉ 排除清單 ∧ ∉ 列冊 → 未處置。"""
    unhandled, all_cand = [], []
    for lid, (_, desc) in sorted(src.items()):
        hits = classify(desc)
        if not hits:
            continue
        all_cand.append((lid, hits, strip_prefix(desc)[:70]))
        if (lid not in cont_leaves and lid not in excl_leaves
                and lid not in defer_leaves):
            unhandled.append((lid, hits, strip_prefix(desc)[:70]))
    return all_cand, unhandled


def layer2(src, sys1, cont_rows):
    """內容驗證 —— 037 片段（正規化）須為登記節之子串。"""
    bad = []
    for row in cont_rows:
        lid, sec = row["leaf"], row["sys1_section"]
        frag = norm(src.get(lid, ("", ""))[1])
        target = norm(sys1.get(sec, ""))
        if not frag or not target or frag not in target:
            bad.append((lid, sec, frag[:48], "節不存在" if not target
                        else "片段非該節之子串"))
    return bad


def self_test(src, sys1):
    """四個斷言（20a §2.4）。任一不過即非零碼退出。"""
    ok = True
    # 第一層 (b) 已知標的：019-02 為指涉型，未登記時應被列為候選
    h = classify(src["SWE1-HMI-VC-019-02"][1])
    a1 = "reference" in h
    print(f"  self-test 1  第一層(b) 已知標的 019-02 應為候選  "
          f"{'PASS' if a1 else '**FAIL**'}  命中={h}")
    ok &= a1
    # 第一層 (a) 反向：017 為完整句，不應成候選
    h = classify(src["SWE1-HMI-VC-017"][1])
    a2 = not h
    print(f"  self-test 2  第一層(a) 反向 017 不應為候選        "
          f"{'PASS' if a2 else '**FAIL**'}  命中={h or '無'}")
    ok &= a2
    # 第二層 (b) 已知標的：第 1 批四筆之既有登記應全過
    rows = read_tsv(CONT)
    base = [r for r in rows if r["leaf"].startswith(
        ("SWE1-HMI-VC-012", "SWE1-HMI-VC-013"))]
    bad = layer2(src, sys1, base)
    a3 = base and not bad
    print(f"  self-test 3  第二層(b) 第 1 批四筆登記應全過      "
          f"{'PASS' if a3 else '**FAIL**'}  母體={len(base)} 不符={bad}")
    ok &= a3
    # 第二層 (a) 反向：把 012-03 之登記改指 2.5 → 應 FAIL
    probe = [{"leaf": "SWE1-HMI-VC-012-03", "sys1_section": "2.5"}]
    a4 = bool(layer2(src, sys1, probe))
    print(f"  self-test 4  第二層(a) 反向 012-03→§2.5 應 FAIL   "
          f"{'PASS' if a4 else '**FAIL**'}")
    ok &= a4
    return ok


def main():
    src, sys1 = load_037(), load_sys1()
    print("cont_guard —— self-test 前置（PLAYBOOK §7.1.1）")
    if not self_test(src, sys1):
        print("\n**self-test 未全過 —— 不輸出正式結果，非零碼退出。**")
        return 2
    print("  → 四個斷言全過，開始跑正式母體\n")

    cont_rows = read_tsv(CONT)
    excl_rows = read_tsv(EXCL)
    cont_leaves = {r["leaf"] for r in cont_rows}
    excl_leaves = {r["leaf"] for r in excl_rows}
    defer_rows = read_tsv(DEFER)
    defer_leaves = {r["leaf"] for r in defer_rows}

    # `short` 清單（profile §8 之適用對象；不參與 CONT 候選判定）
    shorts = sorted((lid, len(strip_prefix(d)), strip_prefix(d))
                    for lid, (_, d) in src.items()
                    if len(strip_prefix(d)) < SHORT)
    SHORT_OUT.write_text(
        "leaf\tlen\tdescription\n"
        + "".join(f"{a}\t{b}\t{c}\n" for a, b, c in shorts), encoding="utf-8")

    all_cand, unhandled = layer1(src, cont_leaves, excl_leaves, defer_leaves)
    bad2 = layer2(src, sys1, cont_rows)

    print(f"第一層 —— 候選偵測（母體 {len(src)} 列 / 全 117 leaf 之 037）")
    print(f"  候選 {len(all_cand)} 筆；已處置 {len(all_cand) - len(unhandled)}；"
          f"**未處置 {len(unhandled)}**")
    for lid, hits, d in all_cand:
        state = ("CONT" if lid in cont_leaves
                 else "排除" if lid in excl_leaves
                 else f"列冊(第{next(r['batch'] for r in defer_rows if r['leaf'] == lid)}批)"
                 if lid in defer_leaves else "**未處置**")
        print(f"    {lid.replace('SWE1-HMI-VC-', ''):<10}{','.join(hits):<26}"
              f"{state:<12}{d}")
    print(f"\nprofile §8 短來源清單（< {SHORT} 字元）：{len(shorts)} 筆 → "
          f"{SHORT_OUT.relative_to(ROOT)}")
    print(f"\n第二層 —— 內容驗證（CONT 表 {len(cont_rows)} 條）")
    print(f"  不符 {len(bad2)} 條 {bad2 or '無'}")

    failed = bool(unhandled) or bool(bad2)
    print(f"\n{'**FAIL**' if failed else 'PASS'} —— "
          f"未處置候選 {len(unhandled)}；內容不符 {len(bad2)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
