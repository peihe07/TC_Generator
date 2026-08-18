"""B3 —— 成對／重複錨點之屬性查證（R-P135 / R-P136）。

CFTS 本文之需求錨點標頭載有 `[Artifact Type:…]` / `[State:…]` / `[ECU:…]` /
`[Market:…]` / `[Model Year:…]` / `[Radio:…]` / `[EE Architecture:…]` 等屬性。
本腳本逐錨點抽出該等屬性並成對比對。

R-P135：`SWE-PM-038` 之三組成對錨點（不含／含 `RemStartFail` 處置）——
  屬性相同 → 同一適用範圍下之不同行為，各自成條正確
  屬性相異 → 變體登載，**須停並上繳，由 Pei 裁定是否合併**
R-P136：跨章節逐字相同之錨點（§1.8.1.1.1 vs §1.6.2.1.17）——
  屬性全同 → 重複登載成立
  屬性相異 → **停並上繳**

**不得自行合併或拆分任何 TC**（19 §I）。

用法：
    python features/power/scripts/build_anchor_attributes.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_tcs as L  # noqa: E402

ATTR_RE = re.compile(r"\[([^:\]]+):([^\]]*)\]")

# R-P135 —— `SWE-PM-038` 之三組成對錨點
PAIRS_135 = [("4941727", "4941728"), ("4941729", "4941730"), ("4941735", "4941736")]
# R-P136 —— 跨章節逐字相同者（§1.6.2.1.17 vs §1.8.1.1.1）
PAIRS_136 = [("4941692", "4941814"), ("4941693", "4941815"), ("4941695", "4941817")]


def anchor_attributes() -> dict[str, dict[str, str]]:
    """anchor_id -> {屬性名: 值}。取自該錨點之標頭段落（bold 層，R-P17）。"""
    out: dict[str, dict[str, str]] = {}
    for path in [L.find("CFTS_009_Wake-up"),
                 next(x for x in L.IN.iterdir() if x.suffix == ".doc")]:
        for plain, bold in L.paragraphs(path):
            found = L.REQ_RE.findall(bold)
            if not found:
                continue
            attrs = {k.strip(): " ".join(v.split()) for k, v in ATTR_RE.findall(plain)}
            if attrs:
                out[found[0]] = attrs
    return out


def norm_set(value: str) -> frozenset:
    """`ECU:RRM, ETM, LTM` 與 `ECU:LTM, ETM, RRM` 為同一集合 —— 次序不具語義。"""
    return frozenset(x.strip() for x in value.split(",") if x.strip())


def compare(a: str, b: str, attrs: dict) -> dict:
    ka, kb = attrs.get(a, {}), attrs.get(b, {})
    keys = sorted(set(ka) | set(kb))
    rows, differ = [], []
    for k in keys:
        va, vb = ka.get(k, "（無）"), kb.get(k, "（無）")
        same = norm_set(va) == norm_set(vb)
        rows.append((k, va, vb, same))
        if not same:
            differ.append(k)
    return {"a": a, "b": b, "rows": rows, "differ": differ,
            "identical": not differ}


def main() -> None:
    attrs = anchor_attributes()
    bodies = L.anchor_bodies()
    out = ["# B3 —— 成對／重複錨點之屬性查證（R-P135 / R-P136）\n",
           "\n> 屬性取自 CFTS 本文錨點標頭（R-P17 之文字層，bold 層辨識錨點、plain 層取屬性）。\n",
           "> **集合型屬性之次序不具語義**（`ECU:RRM, ETM, LTM` 與 `ECU:LTM, ETM, RRM` 視為相同）。\n",
           "> **執行層未合併或拆分任何 TC**（19 §I）。\n",
           f"> 已抽出屬性之錨點數：**{len(attrs)}**\n"]

    for title, pairs, rule in [("## 1. R-P135 —— `SWE-PM-038` 之三組成對錨點", PAIRS_135, "R-P135"),
                               ("## 2. R-P136 —— 跨章節逐字相同之三對錨點", PAIRS_136, "R-P136")]:
        out.append(f"\n{title}\n")
        for a, b in pairs:
            r = compare(a, b, attrs)
            same_text = (" ".join("".join(bodies.get(a, [])).split())
                         == " ".join("".join(bodies.get(b, [])).split()))
            out.append(f"\n### `{a}` vs `{b}` —— "
                       f"{'**屬性全同**' if r['identical'] else '**屬性相異：' + '、'.join(r['differ']) + '**'}"
                       f"（內文逐字{'相同' if same_text else '不同'}）\n\n"
                       f"| 屬性 | `{a}` | `{b}` | 相同 |\n|---|---|---|---|\n")
            for k, va, vb, same in r["rows"]:
                out.append(f"| {k} | {va} | {vb} | {'是' if same else '**否**'} |\n")
            verdict = ("(a) 同一適用範圍下之不同行為 —— 各自成條正確"
                       if r["identical"] else
                       f"**(b) 變體登載 —— 依 {rule} 須停並上繳，由 Pei 裁定是否合併**")
            out.append(f"\n判定：{verdict}\n")

    path = DATA / "b3_anchor_attributes.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes\n")
    for label, pairs in [("R-P135", PAIRS_135), ("R-P136", PAIRS_136)]:
        for a, b in pairs:
            r = compare(a, b, attrs)
            print(f"  {label} {a} vs {b}: "
                  f"{'屬性全同' if r['identical'] else '**屬性相異 → ' + '、'.join(r['differ']) + '**'}")


if __name__ == "__main__":
    main()
