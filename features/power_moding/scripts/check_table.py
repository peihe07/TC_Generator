#!/usr/bin/env python3
"""R-PMH92 —— 檢查總表**由程式產生**，手寫之結果欄不予採認。

各檢查於其模組頂端註冊 `HAS_MUST_HIT` 與 `MUST_HIT_NOTE`；
本檔逐一執行並依下表定其結果欄：

    已註冊 must-hit 且通過        → `PASS`
    已註冊 must-hit 而未通過      → `FAIL`
    **未註冊 must-hit**           → **`未實測`**（不得為 `PASS`）

依據：「新增程式無 must-hit 而總表標 PASS」於 21、22、23 三包連續出現，
**三次皆由執行層自行更正**（R-PMH35(c) 之重複違反）。
**自行更正三次，即應改為不必自行更正。**

用法:
    python scripts/check_table.py            # 產生 Markdown 表
"""
import importlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

HAS_MUST_HIT = False          # 本檔自身無 must-hit —— 依 R-PMH92 其列標「未實測」
MUST_HIT_NOTE = "**未註冊 must-hit** —— 本檔只彙整他檢查之結果"

# (顯示名, 模組名, 引數)；**退出碼之含意於此具名**
CHECKS = [
    ("lint_batch.py generated/batch01.json", "lint_batch", ["generated/batch01.json"], "0"),
    ("lint_batch.py generated/batch02.json", "lint_batch", ["generated/batch02.json"], "0"),
    # 30 包（R-PMH107）：batch 3 之納入 —— **既有檢查對新資料之適用**
    ("lint_batch.py generated/batch03.json", "lint_batch", ["generated/batch03.json"], "0"),
    ("lint_batch.py generated/batch04.json", "lint_batch", ["generated/batch04.json"], "0"),
    ("lint_batch.py <fixture prerework>", "lint_batch", ["tests/fixtures/batch01_prerework.json"], "1"),
    ("lint_batch.py <fixture r2>", "lint_batch", ["tests/fixtures/batch01_r2.json"], "1"),
    ("lint_batch.py --limit-must-hit", "lint_batch", ["--limit-must-hit"], "0"),
    # 31 包（R-PMH116）：Final Step 檢查之錨點 —— **解凍所產生之唯一新旗標**
    ("lint_batch.py --final-step-must-hit", "lint_batch", ["--final-step-must-hit"], "0"),
    ("check_granularity.py --self-test", "check_granularity", ["--self-test"], "0"),
    ("check_granularity.py --check-doc-sync", "check_granularity", ["--check-doc-sync"], "0"),
    ("check_granularity.py --doc-sync-must-hit", "check_granularity", ["--doc-sync-must-hit"], "0"),
    ("check_write_back.py --self-test", "check_write_back", ["--self-test"], "0"),
    ("marker_coverage.py --self-test", "marker_coverage", ["--self-test"], "0"),
    ("marker_coverage.py --verify-extraction", "marker_coverage",
     ["--verify-extraction", "sandbox/spec_pymupdf.txt"], "0"),
    ("marker_coverage.py --window-compare", "marker_coverage", ["--window-compare"], "0"),
    ("canon_coverage.py", "canon_coverage", [], "0"),
    ("check_state_consistency.py", "check_state_consistency", [], "0"),
    ("challenge_rulings.py", "challenge_rulings", [], "0"),
    ("tsv_vs_pdf.py --truncation", "tsv_vs_pdf", ["--truncation"], "0"),
    ("chapter_bidirectional.py 7..12", "chapter_bidirectional", ["7"], "0"),
    ("chapter_bidirectional.py --partition", "chapter_bidirectional", ["--partition"], "0"),
    ("chapter_bidirectional.py --source-must-hit", "chapter_bidirectional", ["--source-must-hit"], "0"),
    ("chapter_bidirectional.py --export-residue", "chapter_bidirectional", ["--export-residue"], "0"),
    ("matrix_vs_chapter.py --must-hit", "matrix_vs_chapter", ["--must-hit"], "0"),
    ("matrix_vs_chapter.py 8", "matrix_vs_chapter", ["8"], "0"),
    ("matrix_vs_chapter.py 11", "matrix_vs_chapter", ["11"], "0"),
    ("matrix_vs_chapter.py 12", "matrix_vs_chapter", ["12"], "0"),
    ("matrix_vs_chapter.py 7", "matrix_vs_chapter", ["7"], "1"),
    ("matrix_vs_chapter.py 10", "matrix_vs_chapter", ["10"], "1"),
    # 29b（R-PMH107）：章 9 解凍後首次對照 —— **既有檢查對新資料之適用**
    ("matrix_vs_chapter.py 9", "matrix_vs_chapter", ["9"], "1"),
    ("spec_assertion_scan.py --assertion popup_ignoff", "spec_assertion_scan",
     ["--assertion", "popup_ignoff"], "0"),
    ("spec_assertion_scan.py --assertion splash_anim", "spec_assertion_scan",
     ["--assertion", "splash_anim"], "0"),
    ("spec_assertion_scan.py --assertion animation", "spec_assertion_scan",
     ["--assertion", "animation"], "1"),
    ("spec_assertion_scan.py --assertion popup", "spec_assertion_scan", ["--assertion", "popup"], "0"),
    ("spec_assertion_scan.py --assertion audio", "spec_assertion_scan", ["--assertion", "audio"], "1"),
    ("spec_assertion_scan.py --assertion announcement", "spec_assertion_scan",
     ["--assertion", "announcement"], "0"),
    ("spec_assertion_scan.py --assertion popup_after", "spec_assertion_scan",
     ["--assertion", "popup_after"], "0"),
    ("spec_assertion_scan.py --cell-must-hit", "spec_assertion_scan",
     ["--cell-must-hit"], "0"),
    ("spec_assertion_scan.py --spec-population", "spec_assertion_scan",
     ["--spec-population"], "0"),
    ("batch_er_vs_matrix.py", "batch_er_vs_matrix", [], "0"),
    ("verdict_form.py", "verdict_form", [], "0"),
    ("verdict_form.py --must-hit", "verdict_form", ["--must-hit"], "0"),
]

# 退出碼 != 0 而**設計如此**者，其原因具名於此
BY_DESIGN = {
    "lint_batch.py <fixture prerework>": "must-hit fixture —— 其 FAIL 即其通過",
    "lint_batch.py <fixture r2>": "must-hit fixture —— 其 FAIL 即其通過",
    "lint_batch.py --final-step-must-hit": "R-PMH116 —— 本批五條修正前之 Final Step 須 FAIL／batch 1-2 之 15 條須 PASS／`Compare` 邊界二例",
    "matrix_vs_chapter.py 7": "含**牴觸 1**（`r48` × `SU3.)`）→ 退出碼 1 為設計",
    "matrix_vs_chapter.py 10": "含**牴觸 1**（`10.3` × `r48c10`，已登記 R-PMH80）→ 退出碼 1 為設計",
    "matrix_vs_chapter.py 9": "含**牴觸 2**（`r31`／`r32` × `PM1)`，29b 步驟 8）→ 退出碼 1 為設計",
    "spec_assertion_scan.py --assertion animation": "含**牴觸 3**（L299／L300／L301 × `-009`，29 步驟 3）→ 退出碼 1 為設計",
    "spec_assertion_scan.py --assertion audio": "**查出牴觸 1**（`r45` × `-007` ER4(b)，24 包）"
                                                "—— **25 包已以第 5～7 項限定排除之，其牴觸記錄保留**",
}


def main() -> None:
    print("| 檢查 | must-hit | 退出碼 | 期望 | **結果** | 備註 |")
    print("|---|---|---:|---:|---|---|")
    n_untested = 0
    for name, mod, args, want in CHECKS:
        m = importlib.import_module(mod)
        has = bool(getattr(m, "HAS_MUST_HIT", False))
        note = getattr(m, "MUST_HIT_NOTE", "")
        r = subprocess.run([sys.executable, str(SCRIPTS / f"{mod}.py"), *args],
                           capture_output=True, text=True, cwd=ROOT)
        rc = r.returncode
        ok = str(rc) == want
        if not has:
            result = "**未實測**"
            n_untested += 1
        else:
            result = "**PASS**" if ok else "**FAIL**"
        extra = BY_DESIGN.get(name, "")
        print(f"| `{name}` | {'✅' if has else '**否**'} | {rc} | {want} | {result} | "
              f"{extra or note} |")
    print(f"\n**未註冊 must-hit 而標「未實測」者 = {n_untested}**"
          "  ← R-PMH92：其不得標 PASS")
    print("\n> 本表由 `python scripts/check_table.py` 產生。**手寫之結果欄不予採認**（R-PMH92）。")


if __name__ == "__main__":
    main()
