"""臨時 tc_id 之全域重編（R-P113(b)）。

`tc_id` 為批次內臨時號，其權威編號待寫回時由 `assign_final_tc_id.py` 指派。
補測若插入於既有批次之中段，其後全部批次之號段即與之衝突
（27 包：批次三 +4 使其由 `044`–`107` 變為 `044`–`111`，與批次四之 `108` 起衝突）。

本腳本依**批次序 → 各批次之 JSON 陣列序**重新指派 `001` 起之連號，
使 G38（格式、唯一、單調遞增、無跳號）維持綠燈。
**不改動任何 TC 之內容**，僅改 `tc_id`；並回報各批次之新號段，
供產生器之 `START_ID` 同步。

用法：
    python features/power/scripts/renumber_tc_ids.py            # 實際重編
    python features/power/scripts/renumber_tc_ids.py --dry-run  # 只回報
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"
PREFIX = "NR1L-PowerManagement-"


def main() -> None:
    dry = "--dry-run" in sys.argv
    n = 1
    changed = 0
    for path in sorted(GENERATED.glob("*.json")):
        b = json.loads(path.read_text(encoding="utf-8"))
        start = n
        for tc in b.get("tcs", []):
            new = f"{PREFIX}{n:03d}"
            changed += tc.get("tc_id") != new
            tc["tc_id"] = new
            n += 1
        print(f"  {b.get('batch','?')}: {len(b.get('tcs', []))} TC  "
              f"→ {start:03d}–{n - 1:03d}")
        if not dry:
            path.write_text(json.dumps(b, ensure_ascii=False, indent=1) + "\n",
                            encoding="utf-8")
    print(f"\n合計 {n - 1} TC；**變動之 tc_id：{changed}**"
          f"{'（dry-run，未寫入）' if dry else ''}")


if __name__ == "__main__":
    main()
