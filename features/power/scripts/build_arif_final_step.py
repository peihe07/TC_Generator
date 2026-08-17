"""B5 —— Arif 之 144 列 done region 末步素材（15 §B5）。

**本腳本僅備妥素材，不改動任何實作。** Q3（Final Step 措詞之 canon 與
實務衝突）屬 Pei 之裁定，15 §I 明令「不得依 B5 之素材自行改動 G77 或任何 TC」。

母體：Home feature 工作簿之 done region —— Z 欄（Author）== `ArifChen`。
依 Comfort profile §3.1 之 G-1 量測，該區為 **144 列**；本腳本以 assertion
擋下母體選取錯誤（A-CF14 之教訓：以 `Arif` 選取得 0 列，而 0 列會產出
「全數不含驗證措詞」之空集合結論）。

依 **R-P80**，僅用其「末步為驗證步驟」之結構性事實，不引用內容裁決。
**`read_only=True`，不呼叫 `save()`**（15 §I）。

用法：
    python features/power/scripts/build_arif_final_step.py
"""

from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_er_restatement import steps, _stem  # noqa: E402
from lint_tcs import FINAL_STEP_INTENT_RE  # noqa: E402

HOME = Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
            "Core HMI/HomeHMI/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
            "STLA Test Case Specification & Result_SWQT_Home_20260809.xlsx")
SHEET = "Test Case Specification&Result"
AUTHOR_COL, PROC_COL = 26, 12          # Z 欄 Test Case Author、L 欄 Test procedure
# （已於 r9 標頭實測確認：Home 之欄位配置與 Power 不同 —— 無 estimated time 欄，
#   P priority / Q design method / R functional safety / Z author。）
AUTHOR_VALUE = "ArifChen"
EXPECTED_ROWS = 144

PROBE = ["check", "verify", "confirm", "ensure", "validate", "observe",
         "read", "count", "wait", "compare", "measure"]


def main() -> None:
    digest = hashlib.sha256(HOME.read_bytes()).hexdigest()
    wb = openpyxl.load_workbook(HOME, data_only=True, read_only=True)
    ws = wb[SHEET]
    rows = []
    for row in ws.iter_rows(min_row=10, values_only=True):
        author = row[AUTHOR_COL - 1]
        if author and str(author).strip() == AUTHOR_VALUE:
            rows.append(row[PROC_COL - 1])
    wb.close()

    assert len(rows) == EXPECTED_ROWS, (
        f"母體列數 {len(rows)} ≠ {EXPECTED_ROWS} —— 選取器可能有誤（A-CF14）")

    last = [steps(p)[-1] for p in rows if p and steps(p)]
    n = len(last)
    hits = {kw: sum(1 for s in last if re.search(r"\b" + kw, s, re.I)) for kw in PROBE}
    intent = [s for s in last if FINAL_STEP_INTENT_RE.search(s)]
    lead = Counter(_stem(re.match(r"[A-Za-z]+", s).group(0).lower())
                   for s in last if re.match(r"[A-Za-z]+", s))

    out = [
        "# B5 —— Arif 144 列 done region 之末步素材（15 §B5）\n",
        "\n> **本檔僅為裁定素材。Q3 屬 Pei 之裁定，執行層未據此改動 G77 或任何 TC。**\n",
        f"\n> 母體檔：`{HOME.name}`\n",
        f"> SHA256：`{digest}`\n",
        f"> 選取器：Z 欄（Author）== `{AUTHOR_VALUE}`；"
        f"母體列數 assertion **{len(rows)} == {EXPECTED_ROWS}** PASS\n",
        f"> `read_only=True`，**未呼叫 `save()`**。\n",
        f"> 產生指令：`python features/power/scripts/build_arif_final_step.py`\n",
        f"\n## 1. 母體\n\n done region **{len(rows)}** 列，"
        f"其中 `test_procedure` 非空且可拆出末步者 **{n}** 條。\n",
        "\n## 2. 驗證意圖措詞之命中\n\n| 詞 | Arif 末步命中 | 佔比 |\n|---|---|---|\n",
    ]
    for kw in PROBE:
        out.append(f"| `{kw}` | **{hits[kw]}** | {100*hits[kw]/max(1,n):.1f}% |\n")
    out.append(f"\n**§5.2B 之完整措詞（`check that` / `to verify` / `and check` …）"
               f"命中 {len(intent)} / {n}（{100*len(intent)/max(1,n):.1f}%）。**\n")

    out.append("\n## 3. 三個母體之並列比較\n\n"
               "| 母體 | 末步條數 | §5.2B 措詞命中 | 佔比 |\n|---|---|---|---|\n"
               f"| **Arif done region（Home）** | {n} | **{len(intent)}** | "
               f"{100*len(intent)/max(1,n):.1f}% |\n"
               "| Comfort + Privacy 已交付（14 包 B4） | 472 | **0** | 0.0% |\n")

    out.append("\n## 4. Arif 末步之行首動詞（前 10）\n\n| 動詞 | 次數 | 佔比 |\n|---|---|---|\n")
    for v, c in lead.most_common(10):
        out.append(f"| `{v}` | {c} | {100*c/max(1,n):.1f}% |\n")

    forms = Counter(" ".join(s.split()[:3]) for s in last)
    out.append("\n## 4.1 典型措詞形態（前 10 種，取前三字）\n\n"
               "| 形態 | 次數 |\n|---|---|\n")
    for f_, c in forms.most_common(10):
        out.append(f"| `{f_}` | {c} |\n")
    out.append("\n**關鍵區別（供裁定）**：`check` 出現於 **%d / %d（%.1f%%）**，"
               "其中 **%d** 條以 `Check` 起首 —— 即驗證意圖確為 Arif 之慣例。\n"
               "惟 §5.2B 所列之**完整措詞**（`check that` / `to check` / `and check`）"
               "僅命中 **%d（%.1f%%）** —— 多數為祈使句 `Check the ...`，非 `check that ...`。\n"
               "**現行 G77 之正則要求完整措詞，故對 Arif 之 %d 條祈使式末步亦會判 FAIL。**\n"
               "此點為素材，**執行層未據以改動 G77**（15 §I）。\n"
               % (hits["check"], n, 100*hits["check"]/max(1, n),
                  lead.get("check", 0), len(intent), 100*len(intent)/max(1, n),
                  lead.get("check", 0) - len(intent)))

    out.append(f"\n## 5. Arif 末步全文（{n} 條，逐條列出，不節錄）\n\n")
    for i, s in enumerate(last, 1):
        mark = " **[含 §5.2B 措詞]**" if FINAL_STEP_INTENT_RE.search(s) else ""
        out.append(f"{i}. {s}{mark}\n")

    path = DATA / "b5_arif_final_step.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"SHA256 {digest}")
    print(f"母體 {len(rows)} 列（assertion PASS）；末步 {n} 條；"
          f"§5.2B 措詞命中 {len(intent)}（{100*len(intent)/max(1,n):.1f}%）")
    for kw in PROBE:
        print(f"  {kw:10}{hits[kw]:5}")
    print("行首動詞前 10：", lead.most_common(10))


if __name__ == "__main__":
    main()
