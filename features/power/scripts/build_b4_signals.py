"""B4 — G28 `SIGNALS` 正則調校報告（R-P57 / G35）。

自 037 之 `Verification Criteria` / `Verification Method` 兩欄抽取全部 token，
統計命名形態分布，據此說明調校內容與覆寫率變化。

調校後之識別式本體位於 `build_vcvm.py`（`SIGNALS` / `DOMAIN_ONLY_ACRONYMS`）；
本腳本只產出佐證報告，不重複定義判準。

用法：
    python features/power/scripts/build_b4_signals.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_vcvm import DOMAIN_ONLY_ACRONYMS, OVERRIDES  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

TOKEN_RE = re.compile(r"\$[A-Za-z_]+\$|[A-Za-z][A-Za-z0-9_.$]*\d*")

# R-P55 回歸斷言
EXPECTED_OVERRIDE_COUNT = 0


def classify(token: str) -> str | None:
    if re.fullmatch(r"\$[A-Za-z_]+\$", token):
        return "`$SIGNAL$`"
    if re.search(r"\.\d", token):
        return "點號後接數字（如 `CS.00244`）"
    if "." in token:
        return "點號分隔識別式"
    if "_" in token:
        return "底線識別式"
    if re.fullmatch(r"[A-Z]{2,3}", token):
        return "全大寫 2–3 字"
    if re.fullmatch(r"[A-Z]{4,}", token):
        return "全大寫 4+ 字"
    if re.fullmatch(r"[A-Za-z]{3,}\d+", token):
        return "字母尾接數字（如 `Timeout1`）"
    if re.fullmatch(r"[A-Z][a-z]+(?:[A-Z][a-z]+)+", token):
        return "CamelCase"
    return None


def main() -> None:
    path_037 = next(f for f in IN.iterdir() if "FSM-037" in f.name)
    wb = openpyxl.load_workbook(path_037, data_only=True, read_only=True)
    ws = wb["SWE1 Requirements"]
    rows = [
        (str(r[16] or "").strip(), str(r[17] or "").strip())
        for r in ws.iter_rows(min_row=8, max_row=145, values_only=True)
        if r[0] and str(r[0]).strip()
    ]
    wb.close()

    forms: Counter = Counter()
    samples: dict[str, Counter] = {}
    for vc, vm in rows:
        for token in TOKEN_RE.findall(f"{vc} {vm}"):
            kind = classify(token)
            if not kind:
                continue
            forms[kind] += 1
            samples.setdefault(kind, Counter())[token] += 1

    print("B4 命名形態分布（母體：%d leaf 之 VC + VM）" % len(rows))
    for kind, n in forms.most_common():
        top = "、".join(f"{t}×{c}" for t, c in samples[kind].most_common(4))
        print(f"  {kind:26} {n:>4}  {top}")
    print(f"\n  DOMAIN_ONLY_ACRONYMS（排除規則）：{sorted(DOMAIN_ONLY_ACRONYMS)}")
    print(f"  G35 人工覆寫率：{len(OVERRIDES)} / {len(rows)} = "
          f"{100 * len(OVERRIDES) / len(rows):.1f}%（調校前 6 / 115 = 5.2%）")
    print(f"\n  報告全文見 {(DATA / 'b4_signals_calibration.md').relative_to(ROOT)}"
          f"（本腳本產出佐證數字，報告本體隨包撰寫）")

    if len(OVERRIDES) != EXPECTED_OVERRIDE_COUNT:
        print(f"\n**回歸斷言失敗（R-P55）**：覆寫筆數 {len(OVERRIDES)} "
              f"≠ 期望 {EXPECTED_OVERRIDE_COUNT}")
        raise SystemExit(1)
    print("\n回歸斷言（R-P55）：PASS")


if __name__ == "__main__":
    main()
