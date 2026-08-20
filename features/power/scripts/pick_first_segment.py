"""R-P337 —— `test_item` 首段之取句（B1 之前半）。

R-P333(a) 令首段「逐字自 `source_clause` 取」而未給取哪一句；
R-P337 補之：取該 TC 之 `expected_result` 所斷言之行為在 `source_clause`
中之對應句，一句為度，不足則取最小完整句組（連續、不跳接），
取後不得改寫、不得補字、不得省略中間文字。

## 本檔之取句法及其性質

候選 = `source_clause` 依 **`. ` / `; ` / 換行** 切出之句，
**切點兩側皆保留原字**，故任一候選皆為 `source_clause` 之**連續子字串**
（G237(d) 之要件由構造保證，非由事後檢查保證）。

計分 = 候選與「`tc_title` ＋ `expected_result` ＋ `test_procedure`」之
**內容詞覆蓋率** —— 即該 TC 所斷言之行為有多少落在該句內。
相鄰候選之合併（最小完整句組）於單句覆蓋率低於 `MERGE_BELOW` 時才嘗試，
且只合併**相鄰**者（不跳接，R-P337(b)）。

**其為機械取句，非人讀裁決。** 依 R-P250 須以已知應命中之實例驗證 ——
見 `--self-test`，其取本 feature 真實之六條，逐條載明應取之句。

用法：
    python features/power/scripts/pick_first_segment.py --self-test
    python features/power/scripts/pick_first_segment.py --report
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"

# R-P338(b)：上限自 Comfort 465 列實測導出（P95），**不得憑印象訂**
FIRST_SEG_MAX = 282

MERGE_BELOW = 0.55          # 單句覆蓋率低於此值才嘗試合併相鄰句
STOP = set("""a an the is are was were be been being of to in on at by for with
from as and or not no if then this that these those it its shall must has have
had do does did will would can could may might been which when while after
before only also into out up down over under such per each any all both same
other another there their his her they them we you i""".split())


def content_words(text: str) -> set[str]:
    return {w for w in re.findall(r"[A-Za-z_$][A-Za-z0-9_$.]*", text.lower())
            if w not in STOP and len(w) > 2}


def candidates(clause: str) -> list[str]:
    """切句；每個候選皆為 `clause` 之連續子字串（切點兩側保留原字）。"""
    out, buf = [], []
    for line in clause.split("\n"):
        # `. ` 與 `; ` 為句界；用 lookbehind 保留標點於前句
        for part in re.split(r"(?<=[.;])\s+", line):
            part = part.strip()
            if part:
                out.append(part)
        buf.append(line)
    # 去重但保序
    seen, uniq = set(), []
    for c in out:
        if c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq


def score(cand: str, target: set[str], idf: dict[str, float]) -> float:
    """覆蓋率以 IDF 加權 —— 於該 leaf 之候選集內罕見之詞更具鑑別力。

    未加權時，泛用詞（`season`／`ignition`）與**該 TC 唯一之區辨詞**
    （`december`／`Switch_Off_Time`）等值，於是引導句常勝過真正的規定句。
    """
    cw = content_words(cand)
    if not cw or not target:
        return 0.0
    tot = sum(idf.get(w, 1.0) for w in target)
    return sum(idf.get(w, 1.0) for w in cw & target) / tot if tot else 0.0


def pick(clause: str, tc: dict) -> tuple[str, float, bool]:
    """回傳（首段、覆蓋率、是否為合併句組）。"""
    target = content_words(" ".join(
        (tc.get("tc_title", ""), tc.get("expected_result", ""),
         tc.get("test_procedure", ""))))
    all_cands = candidates(clause)
    # R-P338(b)：上限於**選句時**即生效 —— 否則會選中超限句再回頭截斷，
    # 而截斷必然違反 R-P337(d)（不得省略中間文字）。
    cands = [c for c in all_cands if len(c) <= FIRST_SEG_MAX]
    if not cands:
        return "", 0.0, False
    df = {}
    for c in all_cands:
        for w in content_words(c):
            df[w] = df.get(w, 0) + 1
    n = len(all_cands)
    idf = {w: (n / k) ** 0.5 for w, k in df.items()}
    scored = [(score(c, target, idf), i, c) for i, c in enumerate(cands)]
    best_s, best_i, best_c = max(scored, key=lambda x: (x[0], -len(x[2])))

    merged = False
    # R-P337(b)：**一句不足以承載該 TC 所驗之完整行為時**才取句組。
    # 「不足」以語義條件判，不以門檻數字判 —— 即：**某一 ER 行之區辨詞
    # 完全不落在所選句內**，而某相鄰句涵蓋之。相鄰者才可（不跳接）。
    er_lines = [l for l in str(tc.get("expected_result", "")).split("\n") if l.strip()]

    def key_terms(line: str) -> set[str]:
        ws = content_words(line) & set(idf)
        if not ws:
            return set()
        top = max(idf[w] for w in ws)
        return {w for w in ws if idf[w] >= top * 0.8}   # 該行之最具鑑別力者

    uncovered = [l for l in er_lines
                 if key_terms(l) and not (key_terms(l) & content_words(best_c))]
    if uncovered:
        for j in (best_i - 1, best_i + 1):
            if not 0 <= j < len(cands):
                continue
            lo, hi = min(best_i, j), max(best_i, j)
            joined = " ".join(cands[lo:hi + 1])
            if len(joined) > FIRST_SEG_MAX:
                continue
            still = [l for l in uncovered
                     if not (key_terms(l) & content_words(joined))]
            if len(still) < len(uncovered):
                best_s, best_c, merged = score(joined, target, idf), joined, True
                break
    return best_c, best_s, merged


def load() -> list[tuple[dict, dict, str]]:
    """(tc, leaf, batch_file) —— req_id == leaf['parent']。"""
    rows = []
    for f in sorted(GENERATED.glob("batch_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        by_parent = {l["parent"]: l for l in d["leaves"]}
        for tc in d["tcs"]:
            rows.append((tc, by_parent[tc["req_id"]], f.name))
    return rows


# ── R-P250：以已知應命中之實例驗證 ──────────────────────────────
# 六條皆取自本 feature 之現行語料；「應取之句」為人讀 `source_clause`
# 與該 TC 之 ER 後所定，**先寫期望再跑**。
# 判斷以**候選索引**表達 —— 判斷之內容是「取哪一句」，
# 而非我對該句之轉錄；手打原句會引入來源之 NBSP 等不可見字之誤差
# （首版即因此二條假 FAIL）。索引於**跑之前**依人讀 `source_clause` 與 ER 判定。
EXPECTED = {
    "NR1L-PowerManagement-001": (0,),      # 唯一含 SplashScreen_Time 之句
    "NR1L-PowerManagement-020": (0,),      # LTM/ETM 一句；other Radios 一句為對照非本條
    "NR1L-PowerManagement-060": (5,),      # Phone_Call.Info == Active 之規定；
                                           # [6] 相鄰而合併後 316 > 282，依 R-P338(b) 取單句
    "NR1L-PowerManagement-120": (3,),      # 唯一載 "Switch_Off_Time" PROXI 值之句
    "NR1L-PowerManagement-200": (1, 2),    # ER 二行分屬相鄰二句，合併 108 ≤ 282
    "NR1L-PowerManagement-255": (2,),      # 「Summer 已開始」只在此句；與 [0] 不相鄰
}


def self_test() -> int:
    rows = {tc["tc_id"]: (tc, leaf) for tc, leaf, _ in load()}
    bad = 0
    for tid, idx in EXPECTED.items():
        tc, leaf = rows[tid]
        cs = candidates(leaf["source_clause"])
        want = " ".join(cs[i] for i in idx)
        got, s, m = pick(leaf["source_clause"], tc)
        ok = got == want
        bad += not ok
        print(f"{'PASS' if ok else '**FAIL**'} {tid}  覆蓋率={s:.2f}{' 合併' if m else ''}")
        if not ok:
            print(f"    期望: {want[:150]}")
            print(f"    實得: {got[:150]}")
    print(f"\n自驗：{len(EXPECTED) - bad} / {len(EXPECTED)} 相符")
    return 1 if bad else 0


def report() -> int:
    rows = load()
    over = low = merged_n = 0
    for tc, leaf, _ in rows:
        seg, s, m = pick(leaf["source_clause"], tc)
        over += len(seg) > FIRST_SEG_MAX
        low += s < 0.30
        merged_n += m
    print(f"母體 {len(rows)} 條")
    print(f"超過首段上限 {FIRST_SEG_MAX} 字元：{over}")
    print(f"覆蓋率 < 0.30（取句可疑，須人讀）：{low}")
    print(f"以相鄰句組取得：{merged_n}")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    raise SystemExit(report())
