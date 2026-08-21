#!/usr/bin/env python3
"""產生 PM 回修之編輯集（M3／M11／M15），輸出 edits.json 供 apply.py 寫回。

順序：M3 先行（四欄），M15 之 token 自 **M3 後**之欄位推導，
以免把舊式 CAN 記法帶進 test_item 括號。
"""

from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint036                                    # noqa: E402
import edits as E                                 # noqa: E402
import excerpt as XC                              # noqa: E402
import sibling_tokens as ST                       # noqa: E402

SANDBOX = ROOT / "features/power/sandbox/b02"
M11_ROWS = (20, 204)                              # 下放包 02 指定


def main() -> None:
    rows = json.loads((SANDBOX / "rows.json").read_text(encoding="utf-8"))
    by_row = {r["row"]: r for r in rows}
    changes: dict[int, dict[str, str]] = collections.defaultdict(dict)

    # ── M3：四欄訊號記法 ──
    for r in rows:
        for field in E.SIGNAL_FIELDS:
            new = E.apply_signal_map(r[field])
            if new != r[field]:
                changes[r["row"]][field] = new
                r[field] = new                     # 供後續 M15 推導使用

    # ── M11：首字大寫 ──
    for row in M11_ROWS:
        r = by_row[row]
        new = E.capitalise_first(r["test_item"])
        if new != r["test_item"]:
            changes[row]["test_item"] = new
            r["test_item"] = new

    # ── M15：sibling 區分 token（自 M3 後欄位推導）──
    groups = collections.defaultdict(list)
    for r in rows:
        paren = "\n".join(lint036.paren_lines(r["test_item"]))
        if r["req_id"].strip() and paren:
            groups[(r["req_id"].strip(), paren)].append(r)

    unresolved, derived = [], []
    for (req, _paren), group in sorted(groups.items(), key=lambda x: x[1][0]["row"]):
        if len(group) < 2:
            continue
        field, tokens = ST.derive(group)
        if field is None:
            unresolved.extend(r["row"] for r in group)
            continue
        for r, token in zip(group, tokens):
            new = E.rewrite_paren(r["test_item"], token)
            changes[r["row"]]["test_item"] = new
            r["test_item"] = new
            derived.append({"row": r["row"], "req": req, "source": field,
                            "token": token})

    # ── M10-PM：test_item 上半摘句（R-3），括號下半不動 ──
    excerpted = []
    for r in rows:
        upper = lint036.upper_half(r["test_item"])
        if XC.n_tokens(upper) <= XC.LIMIT:
            continue
        paren = lint036.paren_lines(r["test_item"])
        new_upper, chosen = XC.excerpt(upper, "\n".join(paren))
        # R-4：自原句中段起抄，句首字母轉大寫（排版正規化）
        new_upper = E.capitalise_first(new_upper)
        new_item = new_upper + "\n\n" + "\n".join(paren)
        changes[r["row"]]["test_item"] = new_item
        r["test_item"] = new_item
        excerpted.append({"row": r["row"], "before": XC.n_tokens(upper),
                          "after": XC.n_tokens(new_upper), "segments": chosen})

    payload = {"changes": {str(k): v for k, v in sorted(changes.items())},
               "m15_derived": derived, "m15_unresolved": unresolved,
               "m10_excerpted": excerpted}
    (SANDBOX / "edits.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    per_field = collections.Counter(f for v in changes.values() for f in v)
    print(f"變動列數 {len(changes)}｜欄位別 {dict(per_field)}")
    print(f"M15 已解 {len(derived)} 列｜未解 {len(unresolved)} 列 {unresolved}")
    print(f"M10 摘句 {len(excerpted)} 列")


if __name__ == "__main__":
    main()
