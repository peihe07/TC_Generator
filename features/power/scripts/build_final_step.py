"""B4 —— G77 判準詞彙之經驗導出（R-P101）。

R-P101 要求 G77 之判準「以 Comfort / Privacy 已交付之 `test_procedure`
**末步**為語料導出」，不得憑印象列舉。

依 **R-P80**，僅用其「末步為驗證步驟」之**結構性事實**，
不引用其任何內容裁決。

**二份工作簿皆 `read_only=True`，不呼叫 `save()`**（R-G3）。

用法：
    python features/power/scripts/build_final_step.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_er_restatement import SOURCES, steps, _stem, WORD_RE  # noqa: E402
from lint_tcs import (FINAL_STEP_INTENT_RE,  # noqa: E402
                      check_s52b_final_step_intent)

# §5.2B 所列之驗證意圖措詞，逐一於語料中計數（含近義者以求完整）
PROBE = ["check", "verify", "confirm", "ensure", "validate", "observe",
         "look", "note", "measure", "compare", "read", "count", "wait"]


def main() -> None:
    last_steps: list[tuple[str, str]] = []
    for name, path, sheet, _pre, proc_c, _er, last in SOURCES:
        wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        for row in wb[sheet].iter_rows(min_row=10, max_row=last, values_only=True):
            proc = row[proc_c - 1]
            if proc and steps(proc):
                last_steps.append((name, steps(proc)[-1]))
        wb.close()

    n = len(last_steps)
    hits = {kw: sum(1 for _, s in last_steps if re.search(r"\b" + kw, s, re.I))
            for kw in PROBE}
    intent = [s for _, s in last_steps if FINAL_STEP_INTENT_RE.search(s)]
    lead = Counter(_stem(re.match(r"[A-Za-z]+", s).group(0).lower())
                   for _, s in last_steps if re.match(r"[A-Za-z]+", s))
    lens = sorted(len(s.split()) for _, s in last_steps)

    out = [
        "# B4 —— G77 判準詞彙之經驗導出（R-P101）\n",
        "\n> 語料：Comfort + Privacy 已交付之 `test_procedure` **末步**。\n",
        "> 依 **R-P80** 僅用其「末步為驗證步驟」之結構性事實，不引用內容裁決。\n",
        "> 二份皆 `read_only=True`，**未呼叫 `save()`**。\n",
        "> 產生指令：`python features/power/scripts/build_final_step.py`\n",
        f"\n## 1. 語料\n\n末步共 **{n}** 條"
        f"（Comfort {sum(1 for s, _ in last_steps if s == 'Comfort')}、"
        f"Privacy {sum(1 for s, _ in last_steps if s == 'Privacy')}）。\n",
        f"\n末步字數：中位 {lens[n//2]}、P90 {lens[int(n*0.9)]}、最長 {lens[-1]}。\n",
        "\n## 2. 驗證意圖措詞之出現次數\n\n| 詞 | 末步命中 | 佔比 |\n|---|---|---|\n",
    ]
    for kw in PROBE:
        out.append(f"| `{kw}` | **{hits[kw]}** | {100*hits[kw]/n:.1f}% |\n")
    out.append(f"\n**§5.2B 之完整措詞（`check that` / `to verify` / `and check` …）"
               f"於語料命中 {len(intent)} / {n}。**\n")

    out.append("\n## 3. 已交付末步之行首動詞\n\n| 動詞 | 次數 |\n|---|---|\n")
    for v, c in lead.most_common(12):
        out.append(f"| `{v}` | {c} |\n")

    out.append("""
## 4. 結論 —— 一項須回報之衝突

**§5.2B 之措詞在已交付實務中 0 / %d attested。**
已交付件之末步慣例為「Read <具體可觀察標的>」——
以「所讀之標的」滿足 §5.5「Final Step 自身即揭示所檢查者」，不另加子句。
Privacy 之末步全數為此形態（例：`Read the state of the speed controlled volume on the HU`）。

**執行層之判別**：R-P101 所指之缺陷**成立** —— 13 包之末步
「Read the TLM display through SplashScreen_Time」所讀者為**載體**（display）
而非**標的**（splash screen），連已交付慣例之標準都未達到。
故本閘依 R-P101 之明令實作並列為阻斷類。

**惟須明載**：採 §5.2B 措詞後，Power 之末步慣例將與 Comfort / Privacy
**分歧**（A-PW67）。此與 G73 之情形不同 ——
G73 是判準無法與合法回讀區分（故不阻斷），
G77 是判準明確而**交付慣例與 canon 條文不一致**（故阻斷，但須登記）。
""" % n)

    out.append("\n## 5. 對本批十條之真實實測（R-P99(c)：證據為「合成＋真實」）\n\n"
               "| 版本 | G77 findings |\n|---|---|\n")
    for lab, f in [("13 包版（修正前）", DATA / "b3_before14.json"),
                   ("14 包版（修正後）", ROOT / "features/power/generated"
                                          / "batch_001_power_down.json")]:
        if not f.exists():
            continue
        tcs_ = json.loads(f.read_text(encoding="utf-8"))["tcs"]
        out.append(f"| {lab} | **{len(check_s52b_final_step_intent(tcs_))}** |\n")

    path = DATA / "b4_final_step.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"末步語料 {n} 條；§5.2B 措詞命中 {len(intent)}")
    for kw in PROBE:
        print(f"  {kw:10}{hits[kw]:5}")


if __name__ == "__main__":
    main()
