#!/usr/bin/env python3
"""驗 `feature.yaml` 之 `reference:` 綁定與實體檔相符（R-G23／R-G40）。

**移植自 `features/display/scripts/verify_reference_binding.py`**（R-G40 五：
逐鍵對照後移植，非默默沿用）。移植檢查表見 `docs/upstream/16_binding_and_backfill_exec.md` §2。

R-G15 使綁定可見。可見不等於受檢：一個宣告了卻無人比對的 sha256，
其失效方式與根本沒有綁定完全相同 —— 只是讀起來像素材受到保護。

本 feature 之情形尤其如此：b14 實測本 feature 之 10 個 sha **無任何程式在比對**
（`verify_reference_binding.py` 當時只存在於 `display` 與 `bed_lowering`）。
R-ICS46 綁入 BHCAN2 後，b03 之 12 處回填、31 條之每一個訊號欄，
全都繫於這 11 個檔就是被量測過的那幾個。

不符時以非零退出並**同時印出二值**。**永不回寫宣告值** ——
那會默默採納一個無人裁定過的資料庫版本（R-G23）。
"""

import hashlib
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
FEATURE_YAML = Path(__file__).resolve().parents[1] / "feature.yaml"


def sha256_of(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    cfg = yaml.safe_load(FEATURE_YAML.read_text(encoding="utf-8"))
    ref = cfg.get("reference") or {}
    if not ref:
        print(f"{FEATURE_YAML}: no `reference:` section — nothing to verify")
        return 0

    print("# reference binding check (R-G23)")
    print(f"feature.yaml: {FEATURE_YAML}")
    print(f"entries: {len(ref)}\n")
    print("| key | file | declared | actual | verdict |")
    print("|---|---|---|---|---|")

    bad = []
    for key in sorted(ref):
        entry = ref[key] or {}
        rel = entry.get("file", "")
        declared = str(entry.get("sha256", "")).strip().lower()
        path = ROOT / rel
        if not rel:
            verdict, actual = "**NO FILE DECLARED**", "—"
            bad.append((key, "no file declared"))
        elif not path.is_file():
            verdict, actual = "**MISSING**", "—"
            bad.append((key, f"file not found: {path}"))
        elif not declared:
            verdict, actual = "**NO SHA DECLARED**", sha256_of(path)[:16] + "…"
            bad.append((key, "no sha256 declared"))
        else:
            actual_full = sha256_of(path)
            actual = actual_full[:16] + "…"
            if actual_full == declared:
                verdict = "MATCH"
            else:
                verdict = "**MISMATCH**"
                bad.append((key, f"declared {declared} / actual {actual_full}"))
        print(f"| {key} | `{Path(rel).name if rel else '—'}` "
              f"| `{(declared[:16] + '…') if declared else '—'}` "
              f"| `{actual}` | {verdict} |")

    print()
    if bad:
        print(f"**{len(bad)} of {len(ref)} FAILED.** Full values:")
        for key, why in bad:
            print(f"  {key}: {why}")
        print("\nR-G23: stop and report. Do NOT update the declared value in "
              "feature.yaml — that would adopt an unruled revision of the "
              "reference database.")
        return 1
    print(f"**{len(ref)} of {len(ref)} match.**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
