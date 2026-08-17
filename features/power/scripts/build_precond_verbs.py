"""B4 — G51 動詞判準之經驗導出（R-P83 / G60）。

現行 20 個動詞為執行層自行列舉，無來源佐證。改為：

  取已交付 TC 之 `test_procedure` 欄（依定義即為動作）之行首動詞聯集
  → 動作動詞之經驗基礎
  再以已交付之 `pre_conditions` 欄（依定義不含動作）量測偽陽性率

來源為 Comfort 與 Privacy 之已交付件。依 **R-P80**，此處僅用其
「procedure 欄含動作、pre_conditions 欄不含動作」之**結構性事實**，
不引用其任何內容裁決。

**三份工作簿皆 `read_only=True`，不呼叫 `save()`**（11 §I）。

用法：
    python features/power/scripts/build_precond_verbs.py
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

# (path, sheet, procedure 欄, pre_conditions 欄, 末列)
SOURCES = [
    ("Comfort",
     Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
          "Climate Control Interface/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
          "STLA Test Case Specification & Result_SWQT_Comfort_20260817.xlsx"),
     "Test Case Specification 測試用例規範", 12, 10, 601),
    ("Privacy",
     Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
          "Privacy Mode/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
          "STLA Test Case Specification & Result_SWQT_Privacy_20260813.xlsx"),
     "Test Case Specification 測試用例規範", 12, 10, 20),
]

# 09 包所用之人工清單，供對照
MANUAL = {
    "insert", "press", "connect", "disconnect", "check", "confirm", "verify",
    "open", "select", "start", "send", "set", "launch", "navigate", "enter",
    "tap", "click", "read", "record", "compare", "inject", "trigger",
}

# 行首之編號與 source-class 標記
LEAD_RE = re.compile(r"^\s*\d+[.)]\s*(?:\[[a-z-]+\]\s*)?")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")


def lead_verb(line: str) -> str | None:
    body = LEAD_RE.sub("", line).strip()
    if not body:
        return None
    m = WORD_RE.match(body)
    return m.group(0).lower() if m else None


def main() -> None:
    proc_leads: Counter = Counter()
    pre_lines: list[tuple[str, str]] = []
    counts = {}
    for name, path, sheet, proc_col, pre_col, last in SOURCES:
        wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        ws = wb[sheet]
        n_proc = n_pre = 0
        for row in ws.iter_rows(min_row=10, max_row=last, values_only=True):
            proc, pre = row[proc_col - 1], row[pre_col - 1]
            if proc:
                n_proc += 1
                for line in str(proc).split("\n"):
                    v = lead_verb(line)
                    if v:
                        proc_leads[v] += 1
            if pre:
                n_pre += 1
                for line in str(pre).split("\n"):
                    if line.strip():
                        pre_lines.append((name, line))
        wb.close()
        counts[name] = (n_proc, n_pre)

    # 經驗動詞：procedure 行首出現 >= MIN_FREQ 次者
    MIN_FREQ = 3
    empirical = {v for v, c in proc_leads.items() if c >= MIN_FREQ}

    # 以已交付 pre_conditions 量偽陽性
    def flags(vocab: set[str]) -> list[tuple[str, str, str]]:
        out = []
        for src, line in pre_lines:
            v = lead_verb(line)
            if v and v in vocab:
                out.append((src, v, line.strip()))
        return out

    fp_emp = flags(empirical)
    fp_man = flags(MANUAL)

    missing = sorted(empirical - MANUAL)
    extra = sorted(MANUAL - set(proc_leads))

    out = [
        "# B4 — G51 動詞判準之經驗導出（R-P83 / G60）\n",
        "\n> 來源：Comfort 與 Privacy 之已交付件。依 **R-P80**，僅用其\n",
        "> 「procedure 欄含動作、pre_conditions 欄不含動作」之**結構性事實**，\n",
        "> 不引用其任何內容裁決。三份皆 `read_only=True`，未呼叫 `save()`。\n",
        "> 產生指令：`python features/power/scripts/build_precond_verbs.py`\n",
        f"\n## 1. 語料\n\n| 來源 | `test_procedure` 非空列 | `pre_conditions` 非空列 |\n|---|---|---|\n",
    ]
    for name, (a, b) in counts.items():
        out.append(f"| {name} | {a} | {b} |\n")
    out.append(f"| **合計** | **{sum(a for a, _ in counts.values())}** | "
               f"**{sum(b for _, b in counts.values())}** |\n")
    out.append(f"\n`pre_conditions` 之行數合計 **{len(pre_lines)}**。\n")

    out.append(f"\n## 2. 經驗動詞（procedure 行首，出現 ≥ {MIN_FREQ} 次）\n\n"
               f"共 **{len(empirical)}** 個。\n\n| 動詞 | 出現次數 |\n|---|---|\n")
    for v, c in sorted(proc_leads.items(), key=lambda kv: -kv[1]):
        if c >= MIN_FREQ:
            out.append(f"| `{v}` | {c} |\n")

    out.append(f"\n## 3. 與 09 包人工清單之對照\n\n"
               f"| | 數量 | 內容 |\n|---|---|---|\n"
               f"| 人工清單 | {len(MANUAL)} | — |\n"
               f"| 經驗清單 | {len(empirical)} | — |\n"
               f"| **人工漏列**（經驗有而人工無） | **{len(missing)}** | "
               f"{', '.join('`' + v + '`' for v in missing) or '無'} |\n"
               f"| **人工誤列**（人工有而 procedure 從未出現） | **{len(extra)}** | "
               f"{', '.join('`' + v + '`' for v in extra) or '無'} |\n")

    out.append(f"\n## 4. G60 —— 對已交付 `pre_conditions` 之偽陽性\n\n"
               f"| 判準 | 誤觸發行數 | 佔 {len(pre_lines)} 行 |\n|---|---|---|\n"
               f"| 09 包人工清單 | **{len(fp_man)}** | {100*len(fp_man)/max(1,len(pre_lines)):.1f}% |\n"
               f"| 本包經驗清單 | **{len(fp_emp)}** | {100*len(fp_emp)/max(1,len(pre_lines)):.1f}% |\n")
    for label, fp in [("人工清單", fp_man), ("經驗清單", fp_emp)]:
        out.append(f"\n### {label}之誤觸發明細（前 20）\n\n")
        if not fp:
            out.append("（無）\n")
        else:
            out.append("| 來源 | 動詞 | 行 |\n|---|---|---|\n")
            for src, v, line in fp[:20]:
                out.append(f"| {src} | `{v}` | {line[:76]} |\n")

    path = DATA / "b4_precond_verbs.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"G60 經驗動詞 {len(empirical)} 個（≥{MIN_FREQ} 次）；"
          f"人工漏列 {len(missing)}、人工誤列 {len(extra)}")
    print(f"  偽陽性：人工清單 {len(fp_man)} / {len(pre_lines)} 行；"
          f"經驗清單 {len(fp_emp)} / {len(pre_lines)} 行")
    print(f"  漏列：{missing}")
    print(f"  誤列：{extra}")
    for src, v, line in fp_emp[:8]:
        print(f"   FP {src} `{v}`: {line[:70]}")


if __name__ == "__main__":
    main()
