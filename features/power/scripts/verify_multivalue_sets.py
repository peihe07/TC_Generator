"""G117 —— 多值欄之集合正規化比對（R-P173）。

23 §八第 3 項：`SWE-PM-025` 三對「僅 ECU 相異」，執行層自陳無能力判斷
該差異是否重要。R-P173 查出 20 §二之 R-P135 屬性表其 ECU 值為
`LTM, ETM, RRM` 對 `RRM, LTM, ETM` —— **同一集合之不同排列**，非真差異；
分析層當時採信「相異」而未正規化即比對。

R-P173(a)：`ECU` / `EE Architecture` / `Radio` / `Market` 等**多值欄**
一律以**集合**比對（去空白、統一大小寫、排序後比較），不以字串比對。

本腳本對**六對**執行之：`SWE-PM-025` 三對（R-P167）＋ R-P135 三對，
回報正規化後之相同／相異；相異者附**集合差集**（R-P173(d)）。

屬性自原始檔重抽，**不採信任何既有表格之抄錄值**（R-P64）。

用法：
    python features/power/scripts/verify_multivalue_sets.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_anchor_attributes import PAIRS_135, anchor_attributes  # noqa: E402

# R-P173(a) 所列之多值欄。
MULTIVALUE = ["ECU", "EE Architecture", "Radio", "Market"]

# `SWE-PM-025` 之三對（23 §四所列，錨點編號自原始檔查得）
PAIRS_025 = [("4941569", "4941572"), ("4941570", "4941573"), ("4941571", "4941574")]

# R-P188（26 包）：`SWE-PM-093` 之二錨點內文逐字相同而屬性相異（A-PW138）。
# 上繳其**全部屬性逐欄原值**與集合正規化後之差集；**不合併亦不拆分**。
PAIRS_093 = [("4941301", "4941941")]


def as_set(value: str) -> frozenset[str]:
    """去空白、統一大小寫、以逗號切分 —— 次序不具語義（R-P173(a)）。"""
    return frozenset(x.strip().casefold() for x in value.split(",") if x.strip())


def compare_pair(a: str, b: str, attrs: dict) -> dict:
    ka, kb = attrs.get(a, {}), attrs.get(b, {})
    rows = []
    for key in sorted(set(ka) | set(kb)):
        va, vb = ka.get(key, "（無）"), kb.get(key, "（無）")
        multi = key in MULTIVALUE
        sa, sb = as_set(va), as_set(vb)
        same = (sa == sb) if multi else (" ".join(va.split()) == " ".join(vb.split()))
        rows.append({"key": key, "va": va, "vb": vb, "multi": multi, "same": same,
                     "only_a": sorted(sa - sb), "only_b": sorted(sb - sa)})
    return {"a": a, "b": b, "rows": rows,
            "differ": [r["key"] for r in rows if not r["same"]]}


def render(groups: list[tuple[str, list[tuple[str, str]]]], attrs: dict) -> str:
    out = ["# G117 —— 多值欄之集合正規化比對（R-P173）\n",
           "\n> 多值欄（`ECU` / `EE Architecture` / `Radio` / `Market`）"
           "以**集合**比對：去空白、統一大小寫、次序不計。\n",
           "> 其餘欄位仍以字串比對（僅正規化連續空白）。\n",
           "> 屬性自原始 CFTS 文字層重抽，未採信既有表格之抄錄值。\n"]
    summary = []
    for title, pairs in groups:
        out.append(f"\n## {title}\n")
        for a, b in pairs:
            r = compare_pair(a, b, attrs)
            verdict = "**正規化後相同**" if not r["differ"] else \
                      "**正規化後仍相異：" + "、".join(r["differ"]) + "**"
            summary.append((a, b, r["differ"]))
            out.append(f"\n### `{a}` vs `{b}` —— {verdict}\n\n"
                       "| 屬性 | 多值 | `%s` | `%s` | 集合相同 | 差集 |\n"
                       "|---|---|---|---|---|---|\n" % (a, b))
            for row in r["rows"]:
                diff = "—"
                if not row["same"]:
                    parts = []
                    if row["only_a"]:
                        parts.append(f"`{a}` 獨有 {{{', '.join(row['only_a'])}}}")
                    if row["only_b"]:
                        parts.append(f"`{b}` 獨有 {{{', '.join(row['only_b'])}}}")
                    diff = "；".join(parts) or "（字串相異）"
                out.append(f"| {row['key']} | {'是' if row['multi'] else '否'} | "
                           f"{row['va']} | {row['vb']} | "
                           f"{'是' if row['same'] else '**否**'} | {diff} |\n")
    out.append("\n## 彙總\n\n| 對 | 正規化後 | 相異欄 |\n|---|---|---|\n")
    for a, b, differ in summary:
        out.append(f"| `{a}` vs `{b}` | "
                   f"{'**相同**' if not differ else '**相異**'} | "
                   f"{'、'.join(differ) or '—'} |\n")
    return "".join(out)


def main() -> None:
    attrs = anchor_attributes()
    groups = [("`SWE-PM-025` 三對（R-P167 / 23 §四）", PAIRS_025),
              ("R-P135 三對（`SWE-PM-038`）", PAIRS_135),
              ("`SWE-PM-093` 之二錨點（R-P188 / A-PW138）", PAIRS_093)]
    (DATA / "g117_multivalue_sets.md").write_text(render(groups, attrs),
                                                  encoding="utf-8")
    print(f"wrote {(DATA / 'g117_multivalue_sets.md').relative_to(ROOT)}")
    for title, pairs in groups:
        print(f"  {title}")
        for a, b in pairs:
            r = compare_pair(a, b, attrs)
            if r["differ"]:
                det = []
                for row in r["rows"]:
                    if not row["same"]:
                        det.append(f"{row['key']}: -{row['only_a']} +{row['only_b']}")
                print(f"    {a} vs {b}: **相異** —— {'; '.join(det)}")
            else:
                print(f"    {a} vs {b}: 正規化後**相同**")


if __name__ == "__main__":
    main()
