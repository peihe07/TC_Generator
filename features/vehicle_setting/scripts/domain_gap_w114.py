"""W-114（64 包 §5）—— A-VS137 之補收 ＋ 同型遺漏之全量量測。

(1) `HSW_StatFailSts` 之值域自基線 DBC `VAL_` 補收
(2) **同時檢查同型遺漏**：以 DBC 全部 `VAL_` 為已知全集，逐一比對
    `spec_variables.tsv`（`bus_domain()`）與 LID 兩欄組，
    **列出「DBC 有而我方兩處皆空」之全部 token**

量測範圍與 A-VS102 一致：**237 leaf 之來源條文所引之 token**
（非整個 DBC —— 全庫另有數千個訊號，其多數屬他 feature，
 A-VS102 已於 32 輪以「屬他 feature 條文」排除 38 個同型 token）。
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec                       # noqa: E402
from selfcheck_w53 import DBC_VALS                            # noqa: E402
from writability_driver import SIG_REF, clause_pairs, lid_column_domain  # noqa: E402
from writability_w58 import bus_domain                        # noqa: E402

FEAT = Path(__file__).resolve().parents[1]


def inscope_tokens() -> dict[str, set[str]]:
    """237 leaf 之來源條文所引之 token → 其所屬 leaf 集合。

    兩種來源並收：`clause_pairs()` 之 (token, 值) 形態，
    與 `SIG_REF` 之 `MSG.Signal` 引用形態。
    """
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"] for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    out: dict[str, set[str]] = {}
    for leaf in gen:
        for q in re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or "")):
            blk = blocks.get(q)
            if not blk:
                continue
            toks = set(clause_pairs(blk["text"])) | {m.group(2) for m in
                                                     SIG_REF.finditer(blk["text"])}
            for t in toks:
                out.setdefault(t, set()).add(leaf)
    return out


def main() -> None:
    high, mid = bus_domain(), lid_column_domain()
    toks = inscope_tokens()
    gap = {t: ls for t, ls in toks.items()
           if t in DBC_VALS and not high.get(t) and not mid.get(t)}

    print(f"237 leaf 之條文所引 token：**{len(toks)}**")
    print(f"其中 DBC `VAL_` 有其值域者：**{sum(1 for t in toks if t in DBC_VALS)}**")
    print(f"**「DBC 有而 `spec_variables` 與 LID 兩欄組皆空」者：{len(gap)}**\n")
    print("| token | DBC `VAL_` | 涉及 leaf | 其中未交付 |")
    print("|---|---|---:|---:|")
    import json
    groups = {}
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups.setdefault(m.group(1), []).append((int(m.group(2) or 1), f))
    done = set()
    for v in groups.values():
        done |= {tc["leaf_id"] for tc in
                 json.loads(max(v)[1].read_text(encoding="utf-8"))["tcs"]}
    for t, ls in sorted(gap.items(), key=lambda x: -len(x[1])):
        vals = "／".join(f"{k}={v}" for k, v in sorted(DBC_VALS[t].items())[:4])
        print(f"| `{t}` | {vals} | {len(ls)} | {len(ls - done)} |")
    print()
    for t, ls in sorted(gap.items()):
        print(f"  {t}: {sorted(ls)[:6]}{' …' if len(ls) > 6 else ''}")


if __name__ == "__main__":
    main()
