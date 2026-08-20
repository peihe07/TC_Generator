"""G237 / G238 —— `test_item` 之形式（R-P342 / R-P336）。

## G237 三項判準（54 包 R-P347 訂正版）

  (a) **末段**為 `(` 起 `)` 止且含 ` -> ` 之區塊，且其**前恰有一個空行**
  (b) **首段為該空行之前的全部文字**，**其內部得含空行**
  (c) 首段為 `source_clause` 之**連續**子字串（空白正規化後）

**無長度判準** —— R-P338(b) 之 P95 上限已由 R-P342 撤回：
Comfort 465 列中 23 列超過 282 字元，以之為 FAIL 門檻即宣告
客戶已交付且 Pei 明示為所要者不合格。

### 判準改過一次（R-P347）

v1 之 (a) 為「`test_item` 含**恰一個空行**」，以**全文之空行總數**為判準 ——
53 包全批 FAIL 11 項，**全部源於同一錨點 `4942354`（`SWE-PM-073`），
其單一段落內含一個空行**。R-P343(a)「逐字」與該判準無同時成立之解。

**問題不在二者互斥，在分隔符之定義選錯** ——
「恰一個空行」之真正用途為**分隔首段與末段**，
當首段自身含空行時該定義即失效。
v2 改以**最後一個空行**為分隔符，首段內部之空行不計。

**不放寬攔截力**：末段之格式要件未變、首段之連續子字串要件未變；
所變者僅分隔符之認定方式。

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

    # R-P347：以**最後一個空行**為分隔符 —— 首段內部之空行不計。
    seps = list(re.finditer(r"\n[ \t]*\n", item))
    if not seps:
        out.append(f"G237(a) {tid}: 無空行，無法分出末段")
        return out
    sep = seps[-1]
    first, second = item[:sep.start()], item[sep.end():]

    # (a) 末段之形態
    s = second.strip()
    if not (s.startswith("(") and s.endswith(")")):
        out.append(f"G237(a) {tid}: 末段未以 `(` 起 `)` 止 → {s[:40]}")
    if " -> " not in s:
        out.append(f"G237(a) {tid}: 末段不含 ` -> `")
    # 「其前**恰有一個**空行」—— 首段尾若仍掛著換行，即分隔處有二個以上空行
    if first.endswith(("\n", "\r")) or second.startswith(("\n", "\r")):
        out.append(f"G237(a) {tid}: 末段前非恰一個空行")

    # (c) 首段為 source_clause 之連續子字串（**首段內部之空行不影響本項**）
    if normalize(first) not in normalize(source_clause):
        out.append(f"G237(c) {tid}: 首段非 source_clause 之連續子字串")

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
    ("G237(a) 無空行", {"tc_id": "FX-A", "test_item": "abc (do -> got)"}, "abc"),
    ("G237(a) 末段前二個空行", {"tc_id": "FX-A2", "test_item": "abc\n\n\n(do -> got)"}, "abc"),
    ("G237(a) 末段無括號", {"tc_id": "FX-C", "test_item": "abc\n\ndo -> got"}, "abc"),
    ("G237(a) 末段無 ` -> `", {"tc_id": "FX-C2", "test_item": "abc\n\n(do got)"}, "abc"),
    ("G237(c) 首段不在 clause 內", {"tc_id": "FX-B", "test_item": "zzz\n\n(do -> got)"}, "abc"),
    ("G238 自加前綴", {"tc_id": "FX-D", "test_item": "1.6.2.1.6) abc\n\n(do -> got)"},
     "1.6.2.1.6) abc"),
]
# R-P347 之正例：**首段內含空行者不得轉紅** —— 即 53 包 `4942354` 之形狀。
# v1 對此判 FAIL 11 項；v2 須綠。
GREEN_BLANK = ("首段內含空行不得轉紅（R-P347 之訂正標的）",
               {"tc_id": "FX-OK2", "test_item": "para one\n\npara two\n\n(do it -> it is done)"},
               "xx para one\n\npara two yy")

GREEN = ("合規者不得轉紅", {"tc_id": "FX-OK", "test_item": "abc def\n\n(do it -> it is done)"},
         "xx abc def yy")


def self_test() -> int:
    bad = 0
    for name, tc, clause in FIXTURES:
        v = check(tc, clause)
        ok = bool(v)
        bad += not ok
        print(f"{'PASS' if ok else '**FAIL**'} 紅向 {name}: {v if v else '未叫 —— 閘失效'}")
    for name, tc, clause in (GREEN, GREEN_BLANK):
        v = check(tc, clause)
        ok = not v
        bad += not ok
        print(f"{'PASS' if ok else '**FAIL**'} 綠向 {name}: {v if v else '無違規'}")
    print(f"\n自驗：{len(FIXTURES) + 2 - bad} / {len(FIXTURES) + 2}")
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
