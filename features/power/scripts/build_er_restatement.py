"""B3/B4 —— G73 複述判準與 G64 詞彙之經驗導出（R-P96 / R-P99(a)）。

R-P96 要求 G73 之判準「詞彙基礎須有經驗來源，不得憑印象列舉」，
比照 R-P83（G51 動詞）／ R-P88（G64 詞彙）之作法。

作法：

  取 Comfort 與 Privacy 之**已交付** TC，逐條將 `test_procedure` 拆為
  編號步驟、`expected_result` 拆為編號行；**僅取二者行數相等者**
  （即 1:1 對齊者）作為語料，逐對量測：

    overlap = |ER 實詞 ∩ proc 實詞| / |ER 實詞|

  該分佈之高尾即為「複述」之經驗門檻。同時取 ER 有而 proc 無之實詞
  聯集，作為「可觀察標的」之經驗詞庫（G73 判準之第二項）。

  另以同一語料量測 G64 之偽陽性與完備性（R-P99(a)）：
  對已交付之 `pre_conditions` 逐行套用 `ENV_STABILITY_RE`。

依 **R-P80**，此處僅用其「procedure 欄含動作、ER 欄含結果、
pre_conditions 欄不含環境穩定性前提」之**結構性事實**，
不引用其任何內容裁決。

**三份工作簿皆 `read_only=True`，不呼叫 `save()`**（R-G3）。

用法：
    python features/power/scripts/build_er_restatement.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import ENV_STABILITY_RE  # noqa: E402  經驗量測之對象

# (name, path, sheet, pre 欄, proc 欄, er 欄, 末列)
SOURCES = [
    ("Comfort",
     Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
          "Climate Control Interface/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
          "STLA Test Case Specification & Result_SWQT_Comfort_20260817.xlsx"),
     "Test Case Specification 測試用例規範", 10, 12, 13, 601),
    ("Privacy",
     Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
          "Privacy Mode/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
          "STLA Test Case Specification & Result_SWQT_Privacy_20260813.xlsx"),
     "Test Case Specification 測試用例規範", 10, 12, 13, 20),
]

NUM_RE = re.compile(r"^\s*\d+[.)]\s*(?:\[[a-z-]+\]\s*)?")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_.$'-]*")

# 功能詞（無語義負載，不計入重疊）—— 標準停用詞，非本判準之發明
STOP = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "and", "or",
    "of", "to", "in", "on", "at", "for", "from", "with", "by", "that", "this",
    "it", "its", "as", "into", "until", "while", "then", "again", "still",
    "no", "not", "all", "any", "each", "every", "both", "same", "other",
    "shall", "should", "will", "can", "may", "must", "has", "have", "had",
    "there", "which", "when", "if", "so", "than", "up", "out", "over",
}


def steps(text: str) -> list[str]:
    """拆為編號項；無編號者以非空行為單位。"""
    return [NUM_RE.sub("", ln).strip()
            for ln in str(text).split("\n") if ln.strip()]


def _stem(w: str) -> str:
    """輕量字尾正規化 —— 使 `start` 與 `starts`、`record` 與 `recorded` 對齊。
    僅去 -ing / -ed / -es / -s，長度 > 4 者方去，不做詞形還原。"""
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: -len(suf)]
    return w

def words(line: str) -> set[str]:
    ws = {w.lower() for w in WORD_RE.findall(line)} - STOP
    return {_stem(w) for w in ws}


def main() -> None:
    pairs: list[tuple[str, str, str, float]] = []
    pre_lines: list[tuple[str, str]] = []
    new_targets: Counter = Counter()
    counts = {}

    for name, path, sheet, pre_c, proc_c, er_c, last in SOURCES:
        wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
        ws = wb[sheet]
        n_tc = n_aligned = 0
        for row in ws.iter_rows(min_row=10, max_row=last, values_only=True):
            proc, er, pre = row[proc_c - 1], row[er_c - 1], row[pre_c - 1]
            if pre:
                for ln in str(pre).split("\n"):
                    if ln.strip():
                        pre_lines.append((name, ln.strip()))
            if not (proc and er):
                continue
            n_tc += 1
            ps, es = steps(proc), steps(er)
            if len(ps) != len(es):
                continue
            n_aligned += 1
            for p_line, e_line in zip(ps, es):
                pw, ew = words(p_line), words(e_line)
                if not ew:
                    continue
                ov = len(ew & pw) / len(ew)
                pairs.append((name, p_line, e_line, ov))
                for w in ew - pw:
                    new_targets[w] += 1
        wb.close()
        counts[name] = (n_tc, n_aligned)

    ovs = sorted(p[3] for p in pairs)

    def pct(q: float) -> float:
        return ovs[min(len(ovs) - 1, int(q * len(ovs)))] if ovs else 0.0

    # G64 經驗量測（R-P99(a)）
    fp = [(s, ln) for s, ln in pre_lines if ENV_STABILITY_RE.search(ln)]

    out = [
        "# B3 / B4 —— G73 複述判準與 G64 詞彙之經驗導出\n",
        "\n> R-P96：G73 之詞彙基礎須有經驗來源，比照 R-P83 / R-P88。\n",
        "> R-P99(a)：G64 須以 Comfort / Privacy 已交付之 `pre_conditions` 補測。\n",
        "> 依 **R-P80** 僅用其結構性事實，不引用任何內容裁決。\n",
        "> 三份皆 `read_only=True`，**未呼叫 `save()`**。\n",
        "> 產生指令：`python features/power/scripts/build_er_restatement.py`\n",
        "\n## 1. 語料\n\n| 來源 | proc 與 ER 皆非空之 TC | 其中 1:1 對齊者 | `pre_conditions` 行數 |\n|---|---|---|---|\n",
    ]
    for name, (a, b) in counts.items():
        n_pre = sum(1 for s, _ in pre_lines if s == name)
        out.append(f"| {name} | {a} | **{b}** | {n_pre} |\n")
    out.append(f"| **合計** | {sum(a for a, _ in counts.values())} | "
               f"**{sum(b for _, b in counts.values())}** | {len(pre_lines)} |\n")
    out.append(f"\n對齊語料共 **{len(pairs)}** 組 (procedure 步驟, ER 行)。\n")

    out.append("\n## 2. 重疊率之經驗分佈\n\n"
               "`overlap = |ER 實詞 ∩ proc 實詞| / |ER 實詞|`（實詞 = 去停用詞）\n\n"
               "| 分位 | overlap |\n|---|---|\n")
    for q, lab in [(0.50, "P50"), (0.75, "P75"), (0.90, "P90"),
                   (0.95, "P95"), (0.99, "P99")]:
        out.append(f"| {lab} | {pct(q):.3f} |\n")
    out.append(f"| 最大 | {ovs[-1]:.3f} |\n" if ovs else "")
    for thr in (0.60, 0.70, 0.80, 0.90, 1.00):
        n = sum(1 for p in pairs if p[3] >= thr)
        out.append(f"\n- overlap ≥ {thr:.2f} 者 **{n}** 組"
                   f"（{100*n/max(1,len(pairs)):.1f}%）")
    out.append("\n\n### overlap 最高之 12 組（已交付件中最接近複述者）\n\n"
               "| 來源 | overlap | procedure 步驟 | ER 行 |\n|---|---|---|---|\n")
    for name, p_line, e_line, ov in sorted(pairs, key=lambda x: -x[3])[:12]:
        out.append(f"| {name} | {ov:.2f} | {p_line[:56]} | {e_line[:56]} |\n")

    out.append(f"\n## 3. 可觀察標的之經驗詞庫\n\n"
               f"ER 行有而其對應 procedure 步驟無之實詞，共 **{len(new_targets)}** 個相異詞。\n\n"
               f"出現 ≥ 5 次者：\n\n| 詞 | 次數 |\n|---|---|\n")
    for w, c in sorted(new_targets.items(), key=lambda kv: -kv[1]):
        if c >= 5:
            out.append(f"| `{w}` | {c} |\n")

    out.append(f"\n## 4. G64 之經驗量測（R-P99(a)）\n\n"
               f"| 項目 | 實測 |\n|---|---|\n"
               f"| 語料行數（已交付 `pre_conditions`） | **{len(pre_lines)}** |\n"
               f"| `ENV_STABILITY_RE` 觸發行數 | **{len(fp)}** |\n"
               f"| 偽陽性率 | {100*len(fp)/max(1,len(pre_lines)):.2f}% |\n")
    out.append("\n### 觸發明細（全列，供判別真偽陽性）\n\n")
    if not fp:
        out.append("（無觸發）\n")
    else:
        out.append("| 來源 | 行 |\n|---|---|\n")
        for s, ln in fp:
            out.append(f"| {s} | {ln[:100]} |\n")

    # 5. 以實際閘門邏輯套用於已交付語料與本批十條（R-P99：真實實測）
    from lint_tcs import (ER_ACTOR_RE, ER_OVERLAP_P50,
                          check_s6_er_restatement, check_s841_time_equality)
    t1 = [p for p in pairs if ER_ACTOR_RE.search(p[2]) and p[3] >= ER_OVERLAP_P50]
    t2 = [p for p in pairs if p[3] >= 1.0]
    out.append(f"\n## 5. 閘門邏輯對已交付語料之實測（R-P99）\n\n"
               f"| 分支 | 判準 | 觸發 / {len(pairs)} | 比率 |\n|---|---|---|---|\n"
               f"| tier 1 | 動作述語 ＋ overlap ≥ {ER_OVERLAP_P50:.2f} | **{len(t1)}** | "
               f"{100*len(t1)/len(pairs):.1f}% |\n"
               f"| tier 2 | overlap = 1.00 | **{len(t2)}** | "
               f"{100*len(t2)/len(pairs):.1f}% |\n")
    out.append("\n**該等觸發於已交付件中屬合法之狀態回讀**"
               "（§6「prove condition established」），形如\n"
               "「Select the rear Feet mode → The rear Feet mode is selected」。\n"
               "**故 G73 全部列為待人工裁決類，不阻斷** —— 比照 R-P76 之 R-P42(b)。\n")
    out.append("\n### tier 1 觸發之前 15 例（已交付件）\n\n"
               "| 來源 | overlap | procedure 步驟 | ER 行 |\n|---|---|---|---|\n")
    for name, p_line, e_line, ov in t1[:15]:
        out.append(f"| {name} | {ov:.2f} | {p_line[:52]} | {e_line[:52]} |\n")

    import json as _json
    out.append("\n## 6. 對本批十條之真實實測（R-P99(c)：證據為「合成＋真實」）\n\n"
               "| 版本 | G73 tier 1 | G73 tier 2 | G74 |\n|---|---|---|---|\n")
    for lab, f in [("12 包修正後（本包修正前）", ROOT / "features/power/data/b2_before13.json"),
                   ("13 包再修正後", ROOT / "features/power/generated/batch_001_power_down.json")]:
        if not f.exists():
            continue
        tcs_ = _json.loads(f.read_text(encoding="utf-8"))["tcs"]
        r = check_s6_er_restatement(tcs_)
        out.append(f"| {lab} | **{len([x for x in r if x['rule']=='R-P96(a)'])}** | "
                   f"**{len([x for x in r if x['rule']=='R-P96(b)'])}** | "
                   f"**{len(check_s841_time_equality(tcs_))}** |\n")

    path = DATA / "b3_er_restatement.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"語料 {len(pairs)} 組；P90={pct(0.90):.3f} P95={pct(0.95):.3f} "
          f"P99={pct(0.99):.3f} max={ovs[-1] if ovs else 0:.3f}")
    for thr in (0.6, 0.7, 0.8, 0.9, 1.0):
        print(f"  overlap>={thr:.2f}: {sum(1 for p in pairs if p[3]>=thr)}")
    print(f"新標的詞 {len(new_targets)} 個")
    print(f"G64 語料 {len(pre_lines)} 行，觸發 {len(fp)} 行")
    for s, ln in fp[:10]:
        print(f"   {s}: {ln[:88]}")


if __name__ == "__main__":
    main()
