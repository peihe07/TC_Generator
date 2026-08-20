"""G237 / G238 —— `test_item` 之形式（R-P342 / R-P336）。

## G237 三項判準（R-P342 撤回長度上限後）

  (a) `test_item` 含**恰一個空行**
  (b) 首段為 `source_clause` 之**連續**子字串（空白正規化後）
  (c) 後段以 `(` 起 `)` 止且含 ` -> `

**無長度判準** —— R-P338(b) 之 P95 上限已由 R-P342 撤回：
Comfort 465 列中 23 列超過 282 字元，以之為 FAIL 門檻即宣告
客戶已交付且 Pei 明示為所要者不合格。

## G238 —— 首段無自加前綴（R-P336）

Comfort 之前綴（`R1C1.)` `HVACSB6.)` 等）係其規格原句自帶；
Power 之 CFTS 本文無此類標籤，故首段不得帶 `<section>)` 形態之前綴。
本閘查首段是否以「數字與點之串 ＋ `)`」起始 —— 該形態只可能是自加的。

## 正規化（比照 R-P125(a)，不得擴大）

僅 NBSP／thin space → 空格、連續空白摺疊為一。
**不做大小寫、標點、引號之正規化** —— 那些差異是真差異。

用法：
    python features/power/scripts/verify_test_item_53.py
    python features/power/scripts/verify_test_item_53.py --self-test
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"

SELF_PREFIX = re.compile(r"^\s*\d+(?:\.\d+)*\)")     # G238：自加之 `1.6.2.1.6)` 形態


def normalize(text: str) -> str:
    return " ".join(text.replace("\xa0", " ").replace(" ", " ").split())


def check(tc: dict, source_clause: str) -> list[str]:
    tid = tc.get("tc_id", "?")
    item = str(tc.get("test_item", ""))
    out = []

    # (a) 恰一個空行
    blanks = len(re.findall(r"\n[ \t]*\n", item))
    if blanks != 1:
        out.append(f"G237(a) {tid}: 空行 {blanks} 個，須恰 1")
        return out                       # 分不出兩段，後續判準無從施行

    first, second = re.split(r"\n[ \t]*\n", item, maxsplit=1)

    # (b) 首段為 source_clause 之連續子字串
    if normalize(first) not in normalize(source_clause):
        out.append(f"G237(b) {tid}: 首段非 source_clause 之連續子字串")

    # (c) 後段形態
    s = second.strip()
    if not (s.startswith("(") and s.endswith(")")):
        out.append(f"G237(c) {tid}: 後段未以 `(` 起 `)` 止")
    if " -> " not in s:
        out.append(f"G237(c) {tid}: 後段不含 ` -> `")

    # G238 —— 首段無自加前綴
    if SELF_PREFIX.match(first):
        out.append(f"G238 {tid}: 首段帶自加前綴 → {first[:30]}")
    return out


def load():
    rows = []
    for f in sorted(GENERATED.glob("batch_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        bp = {l["parent"]: l for l in d["leaves"]}
        for tc in d["tcs"]:
            rows.append((tc, bp[tc["req_id"]]["source_clause"]))
    return rows


# R-P338 之遺制：**以刻意違反之 fixture 證明其會 FAIL**（R-P334 原令，仍適用）
FIXTURES = [
    ("G237(a) 二個空行", {"tc_id": "FX-A", "test_item": "abc\n\n(do -> got)\n\nextra"}, "abc"),
    ("G237(a) 無空行", {"tc_id": "FX-A2", "test_item": "abc (do -> got)"}, "abc"),
    ("G237(b) 首段不在 clause 內", {"tc_id": "FX-B", "test_item": "zzz\n\n(do -> got)"}, "abc"),
    ("G237(c) 無括號", {"tc_id": "FX-C", "test_item": "abc\n\ndo -> got"}, "abc"),
    ("G237(c) 無 ` -> `", {"tc_id": "FX-C2", "test_item": "abc\n\n(do got)"}, "abc"),
    ("G238 自加前綴", {"tc_id": "FX-D", "test_item": "1.6.2.1.6) abc\n\n(do -> got)"},
     "1.6.2.1.6) abc"),
]
GREEN = ("合規者不得轉紅", {"tc_id": "FX-OK", "test_item": "abc def\n\n(do it -> it is done)"},
         "xx abc def yy")


def self_test() -> int:
    bad = 0
    for name, tc, clause in FIXTURES:
        v = check(tc, clause)
        ok = bool(v)
        bad += not ok
        print(f"{'PASS' if ok else '**FAIL**'} 紅向 {name}: {v if v else '未叫 —— 閘失效'}")
    v = check(GREEN[1], GREEN[2])
    ok = not v
    bad += not ok
    print(f"{'PASS' if ok else '**FAIL**'} 綠向 {GREEN[0]}: {v if v else '無違規'}")
    print(f"\n自驗：{len(FIXTURES) + 1 - bad} / {len(FIXTURES) + 1}")
    return 1 if bad else 0


def main() -> int:
    rows = load()
    viol = [v for tc, sc in rows for v in check(tc, sc)]
    print(f"母體 {len(rows)} 條")
    for v in viol[:40]:
        print("  ", v)
    if len(viol) > 40:
        print(f"   …另 {len(viol) - 40} 項")
    print(f"\nG237 / G238：{len(rows) - len({v.split()[1] for v in viol})} / {len(rows)} 通過"
          f"（違規 {len(viol)} 項）")
    return 1 if viol else 0


if __name__ == "__main__":
    raise SystemExit(self_test() if "--self-test" in sys.argv else main())
