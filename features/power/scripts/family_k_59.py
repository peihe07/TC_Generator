"""B7 —— 家族 K 三分法與 G251 判準（R-P366 / R-P360(b)）。

家族 K：Procedure / ER / Pre-Condition 以 `listed in Input Test Data` 回指
ITD 欄，違 IN §4.5 SWC 基準與 R-1 v2「ITD 以 `NA` 為常態」。

R-P366 之三分，(c) 之判準由 **R-P373** 改「多行」為「性質」：
  (a) 可內聯          → 內聯至 Procedure 該步，ITD 改 `NA`
  (b) 單行 > 60 字元  → 逐條檢；內聯後末步逾 §5.2B 18 字者改拆步，
                        **不得刪減資料以合字數**（資料完整性勝）
  (c) IN §4.5 第 3 類獨立資料集 → 保留於 ITD，Remarks 說明

R-P373(a)：第 3 類之特徵為「**一步多值、值間為並列**」（邊界值／批次值／
列舉全體）。多行而每行為**一訊號一賦值**、彼此為前置關係者**非資料集**，
依 (a) 內聯（每一賦值一步 `Send the signal $MESSAGE.Signal$ = <raw> (<label>)`，
起始音量等非訊號值入 Pre-Condition）。

用法：
    python features/power/scripts/family_k_59.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "features/power/data/family_k_disposition_55.tsv"

BACKREF_RE = re.compile(r"listed in Input Test Data", re.I)
SCAN_FIELDS = ("pre_conditions", "test_procedure", "expected_result")
LIMIT = 60          # R-P366(a)/(b) 之分界
LAST_STEP_WORDS = 18  # IN §5.2B


def last_step(text: str) -> str:
    steps = [ln for ln in (text or "").splitlines() if ln.strip()]
    return steps[-1] if steps else ""


def backref_steps(text: str) -> list[tuple[int, str, bool]]:
    """回指 ITD 之步驟：(序位, 原文, 是否為末步)。"""
    steps = [ln for ln in (text or "").splitlines() if ln.strip()]
    return [(i + 1, ln, i == len(steps) - 1)
            for i, ln in enumerate(steps) if BACKREF_RE.search(ln)]


def words(step: str) -> int:
    """去掉行首之 `N.` 序號後計字。"""
    return len(re.sub(r"^\s*\d+\.\s*", "", step).split())


# R-P373(a)：第 3 類資料集之語言標記 —— 一步多值、值間並列。
DATASET_RE = re.compile(
    r"\bone at a time\b|\bin turn\b|\beach of\b|\bboundary values\b"
    r"|\ball listed\b|\bfor every\b|\bevery listed\b"
    # 67 包補：`Repeat … N times` 亦為「一步多輪、輪間並列」之第 3 類
    # （66 包 §1 表對 `-218` 明示此寫法），原式看不到。
    r"|\brepeat\b[^\n]{0,60}\b\d+\s+times\b", re.I)


def is_dataset(tc: dict) -> bool:
    """R-P373(a)：同一步驟須逐一代入多個值者，方為第 3 類。

    多行而每行為「一訊號一賦值」者為前置關係，非並列值集 —— 依 (b) 非資料集。
    """
    itd = (tc.get("input_test_data") or "").strip()
    lines = [ln.strip() for ln in itd.splitlines() if ln.strip()]
    if len(lines) <= 1:
        return bool(DATASET_RE.search(tc.get("test_procedure") or ""))
    # 每行皆為「<名> = <值>」或「<名>: <值>」形態 → 一訊號一賦值，非並列值集
    assign = sum(1 for ln in lines if re.match(r"^[^=:]+[=:]\s*\S", ln))
    if assign == len(lines):
        return bool(DATASET_RE.search(tc.get("test_procedure") or ""))
    return True


def classify(tc: dict) -> tuple[str, str]:
    itd = (tc.get("input_test_data") or "").strip()
    if is_dataset(tc):
        return "c", "IN §4.5 第 3 類獨立資料集 → 保留 ITD，Remarks 說明"
    # R-P373(b)：多行而每行一訊號一賦值者依性質內聯，**與長度無關**
    if "\n" in itd:
        return "a", "多行，每行一訊號一賦值（R-P373(b)）→ 每一賦值一步內聯"
    if len(itd) > LIMIT:
        return "b", "單行逾 60 字元，逐條檢；逾 18 字則拆步，不得刪資料"
    return "a", "內聯至 Procedure 該步，ITD 改 NA"


def main() -> None:
    cur = rm.load_current()
    hits = [t for t in cur
            if any(BACKREF_RE.search(t.get(f) or "") for f in SCAN_FIELDS)]

    rows = ["tc_id\tclass\titd_len\titd_lines\tlast_step_words\t"
            "inline_words_est\tdisposition"]
    counts = {"a": 0, "b": 0, "c": 0}
    over18 = []
    for tc in sorted(hits, key=lambda t: t["tc_id"]):
        cls, note = classify(tc)
        counts[cls] += 1
        itd = (tc.get("input_test_data") or "").strip()
        proc = tc.get("test_procedure") or ""
        ls = last_step(proc)
        # 內聯之標的為**回指該欄之步驟**，非必為末步。
        # §5.2B 之 18 字上限只約束末步，故僅當回指步即末步時才會撞上限。
        est = 0
        for _, step, is_last in backref_steps(proc):
            # 內聯後字數 ＝ 該步原字數 ＋ ITD 字數 − 回指片語 5 字
            w = words(step) + len(itd.split()) - 5
            est = max(est, w)
            if cls == "a" and is_last and w > LAST_STEP_WORDS:
                over18.append((tc["tc_id"], w))
        rows.append(f"{tc['tc_id']}\t{cls}\t{len(itd)}\t"
                    f"{itd.count(chr(10)) + 1}\t{words(ls)}\t{est}\t{note}")

    OUT.write_text("\n".join(rows) + "\n")
    print(f"家族 K：{len(hits)} / {len(cur)} 條")
    print(f"  (a) 內聯（R-P373(b) 含多行一訊號一賦值）: {counts['a']}")
    print(f"  (b) 單行 >{LIMIT} 字元，逐條檢          : {counts['b']}")
    print(f"  (c) IN §4.5 第 3 類獨立資料集          : {counts['c']}")
    print(f"\n(a) 類中內聯後末步估逾 §5.2B {LAST_STEP_WORDS} 字者："
          f"{len(over18)} 條 —— 依 R-P366(b) 轉拆步，不得刪資料")
    for tid, n in over18[:12]:
        print(f"   {tid[-3:]}  估 {n} 字")
    print(f"\n→ {OUT.relative_to(ROOT)}")

    # G251 現況（施作前之基線）
    nonna = [t for t in cur
             if (t.get("input_test_data") or "").strip() not in ("NA", "")]
    print(f"\nG251 基線：`listed in Input Test Data` 殘留 {len(hits)}（期望 0）；"
          f"ITD 非 NA 者 {len(nonna)}（施作後應為 {counts['b'] + counts['c']}）")


if __name__ == "__main__":
    main()
