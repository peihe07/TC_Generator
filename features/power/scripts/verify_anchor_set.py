"""G99 —— 錨點清單完整性（R-P134）。

G94 驗「抄對了」—— `source_clause` 與 `source_anchor` 所指之原文逐字相符。
**它不驗「抄全了該抄的」** ——若某個該被引用之錨點根本未被列進
`source_anchor`，G94 一樣會全綠（18 §七(乙)7 自陳）。

G99：逐 leaf 比對其 `source_anchor` 集合與 `layer3_full.tsv` 所載
該 leaf 之 `item_ids` 集合（同一 leaf 跨多章節者取聯集）。
不相等即 FAIL，並列出兩側之差集。

`item_ids` 即 §C 錨點鏈之產物（`Sys-RA-* → Polarion item id → CFTS 章節`），
其正確性由 03–06 包所驗；本閘只驗「TC 之 `source_anchor` 是否等於它」。

用法：
    python features/power/scripts/verify_anchor_set.py
    python features/power/scripts/verify_anchor_set.py --self-test
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"
LAYER3 = DATA / "layer3_full.tsv"


def layer3_anchors() -> dict[str, set[str]]:
    """leaf -> 其被引用錨點之聯集（跨章節）。"""
    out: dict[str, set[str]] = {}
    rows = LAYER3.read_text(encoding="utf-8").splitlines()
    header = rows[0].split("\t")
    i_leaf, i_ids = header.index("leaf"), header.index("item_ids")
    for row in rows[1:]:
        if not row.strip():
            continue
        cells = row.split("\t")
        ids = {x.strip() for x in cells[i_ids].split(",") if x.strip()}
        out.setdefault(cells[i_leaf], set()).update(ids)
    return out


def parse_anchor(value) -> set[str]:
    if isinstance(value, (list, tuple, set)):
        return {str(x).strip() for x in value if str(x).strip()}
    return {x.strip() for x in str(value).split(",") if x.strip()}


def check_leaf(parent: str, source_anchor, expected: set[str]) -> dict:
    got = parse_anchor(source_anchor)
    return {
        "parent": parent,
        "got": sorted(got), "expected": sorted(expected),
        "missing": sorted(expected - got),      # 該抄而未抄
        "extra": sorted(got - expected),        # 抄了不該抄的（R-P42）
        "ok": got == expected,
    }


def run(batches: list[dict]) -> list[dict]:
    expected = layer3_anchors()
    out = []
    for batch in batches:
        for leaf in batch.get("leaves", []):
            parent = leaf.get("parent", "?")
            out.append(check_leaf(parent, leaf.get("source_anchor", ""),
                                  expected.get(parent, set())))
    return out


def self_test() -> int:
    """R-P134 —— 以刻意刪去一個錨點之 fixture 證明本閘確實會失敗。"""
    failures = 0
    expected = layer3_anchors()["SWE-PM-038"]
    full = ",".join(sorted(expected))

    def case(label: str, anchor, want_ok: bool) -> None:
        nonlocal failures
        r = check_leaf("SWE-PM-038", anchor, expected)
        ok = r["ok"] == want_ok
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G99 {label}")
        print(f"          期望 {'相等' if want_ok else 'FAIL'}；"
              f"實際 {'相等' if r['ok'] else 'FAIL'}"
              f"（缺 {r['missing']}，多 {r['extra']}）")

    case("應相等 —— 完整清單", full, True)
    case("應相等 —— 次序不同", ",".join(sorted(expected, reverse=True)), True)
    dropped = sorted(expected)[:-1]
    case("應 FAIL —— 刻意刪去一個錨點", ",".join(dropped), False)
    case("應 FAIL —— 多列一個未被引用之錨點（R-P42）",
         full + ",4941999", False)
    case("應 FAIL —— 空清單", "", False)
    print(f"\n  G99 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())

    batches = [json.loads(p.read_text(encoding="utf-8"))
               for p in sorted(GENERATED.glob("*.json"))]
    results = run(batches)
    bad = [r for r in results if not r["ok"]]

    lines = ["# G99 —— 錨點清單完整性（R-P134）\n",
             "\n> 比對 `source_anchor` 與 `layer3_full.tsv` 之 `item_ids`（跨章節取聯集）。\n",
             "> G94 驗「抄對了」，G99 驗「抄全了該抄的」——二者缺一，反向涵蓋之地基仍不完整。\n",
             "\n| leaf | `source_anchor` 數 | `item_ids` 數 | 該抄未抄 | 抄了不該抄 | 判定 |\n"
             "|---|---|---|---|---|---|\n"]
    for r in results:
        lines.append(f"| `{r['parent']}` | {len(r['got'])} | {len(r['expected'])} | "
                     f"{'、'.join(r['missing']) or '—'} | {'、'.join(r['extra']) or '—'} | "
                     f"{'**相等**' if r['ok'] else '**FAIL**'} |\n")
    lines.append(f"\n**{len(results) - len(bad)} / {len(results)} 相等。**\n")
    (DATA / "g99_anchor_set.md").write_text("".join(lines), encoding="utf-8")

    for r in results:
        print(f"  {r['parent']:12} got {len(r['got']):2} / expected {len(r['expected']):2}  "
              f"{'相等' if r['ok'] else '**FAIL** 缺=' + str(r['missing']) + ' 多=' + str(r['extra'])}")
    print(f"\nG99：{len(results) - len(bad)} / {len(results)} 相等")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
