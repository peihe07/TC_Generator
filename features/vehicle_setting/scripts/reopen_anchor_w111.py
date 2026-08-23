"""W-111 之錨點（R-VS54，63 包 §7）。

  必命中   —— 16 個 `Fail_Present` leaf 須由 `generatable = no` 轉 `yes`
  必不命中 —— `M182` 相關 leaf 須維持未解

二錨點同批執行並列回報。**錨點無標的者，依 R-VS54 不得讀為通過。**
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402
from writability_driver import run       # noqa: E402

FEAT = Path(__file__).resolve().parents[1]


def leaf_text(l2r: dict, blocks: dict, leaf: str) -> str:
    qs = re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or ""))
    return " ".join("\n".join(blocks[q]["text"].split("\n")[1:]) for q in qs if q in blocks)


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    now = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    pre = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable_pre_w111.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    _, detail = run()

    fp = [l for l in l2r if "Fail_Present" in leaf_text(l2r, blocks, l)]
    turned = [l for l in fp if pre.get(l, {}).get("generatable") == "no"
              and now.get(l, {}).get("generatable") == "yes"]
    stuck = [l for l in fp if l not in turned]
    ok1 = len(turned) == len(fp)
    print(f"錨點 1（必命中）  `Fail_Present` leaf {len(fp)} —— 轉 yes {len(turned)}   "
          f"{'PASS' if ok1 else '⚠ 部分未轉，逐筆列出'}")
    for l in stuck:
        print(f"    {l}  {pre.get(l, {}).get('generatable')} → "
              f"{now.get(l, {}).get('generatable')}  ({detail.get(l, {}).get('理由')})")

    m = [l for l in l2r if re.search(r"M182|M189|M240", leaf_text(l2r, blocks, l))]
    print(f"錨點 2（必不命中）`M182`／`M189`／`M240` 相關 leaf **{len(m)}**   "
          f"{'⚠ 錨點無標的 —— 依 R-VS54 不得讀為通過' if not m else 'PASS'}")
    for l in m:
        print(f"    {l}  W={now.get(l, {}).get('writable')}  "
              f"gen={now.get(l, {}).get('generatable')}")


if __name__ == "__main__":
    main()
