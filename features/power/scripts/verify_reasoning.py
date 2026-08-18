"""G129 —— 產出 JSON 之 leaf `reasoning` 非空（R-P190）。

§10.4 明訂 `reasoning` 為稽核軌跡，其用途為
「reviewers can align on the AI's interpretation without re-reading the source」。
**批次四、五之 leaf `reasoning` 於 26 包實測前為空**（47 / 54 完全空，
其餘 7 個僅有個案註記而非 §10.4 之四項軌跡）——
而**現行閃點皆無法發現此事**：G19 所量者為 037 之欄位，非產出 JSON 之欄位。

本閘之判準：
  （a）每一 leaf 之 `reasoning` 須**非空**
  （b）長度須不低於 `MIN_CHARS` —— 空字串與一句套語皆不構成稽核軌跡
  （c）**不判內容品質** —— §10.4 四項之充分與否須人讀，
       本閘只攔「根本沒寫」與「寫得不可能涵蓋四項」

門檻之依據：批次一 ~ 三之既有 `reasoning`（其為 §10.4 之合格樣本）
之最短者為量測所得，見 `--calibrate`。**門檻取該最短值向下取整至十位**，
非憑印象設定。

用法：
    python features/power/scripts/verify_reasoning.py
    python features/power/scripts/verify_reasoning.py --calibrate
    python features/power/scripts/verify_reasoning.py --self-test
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"

# 校準（`--calibrate`，實測）—— **依 R-P182 並陳新舊值**：
#
# | 版 | 校準語料 | 最短 | 門檻 |
# | 26 包 | 批次一 ~ 三（重評前）| 26 字（`SWE-PM-022`）| **20** |
# | 27 包 | 批次一 ~ 三（依 R-P203 重評並補寫後）| 201 字（`SWE-PM-060`）| （見下）|
# | 27 包（採用）| **全六批** | **131 字（`SWE-PM-094`）** | **130** |
#
# **未取 200 之理由**：批次一 ~ 三補寫後之最短為 201，惟批次四 ~ 六尚有
# 131 / 169 / 177 / 181 / 184 字者。以 200 為門檻將迫使該等 `reasoning`
# **為過門檻而加字** —— 該形態與 R-P203(c) 所禁之「為使門檻好看而改動」
# 方向相反而性質相同（一個是刪、一個是灌水），皆使長度失去其代理意義。
# 故以**全六批之實測最短**為校準基礎，取 130。
#
# **長度仍為弱代理，據實登記**：其只攔得住「根本沒寫」與「寫得極薄」。
# §10.4 四項之實質涵蓋由 **G137**（`assess_reasoning.py`）判，非本閘。
MIN_CHARS = 130


def check(batch: dict) -> list[dict]:
    out = []
    for leaf in batch.get("leaves", []):
        text = str(leaf.get("reasoning", "")).strip()
        if not text:
            out.append({"leaf": leaf.get("parent", "?"), "len": 0,
                        "reason": "`reasoning` 為空 —— §10.4 之稽核軌跡缺漏"})
        elif len(text) < MIN_CHARS:
            out.append({"leaf": leaf.get("parent", "?"), "len": len(text),
                        "reason": f"`reasoning` 僅 {len(text)} 字，"
                                  f"低於門檻 {MIN_CHARS} —— 不可能涵蓋 §10.4 四項"})
    return out


def batches() -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(GENERATED.glob("*.json"))]


def calibrate() -> int:
    lens = []
    for b in batches():
        # 27 包起以**全六批**為校準語料（見 MIN_CHARS 之並陳表）。
        for leaf in b.get("leaves", []):
            t = str(leaf.get("reasoning", "")).strip()
            if t:
                lens.append((len(t), b["batch"], leaf["parent"]))
    lens.sort()
    print("  全六批之 `reasoning` 長度（校準語料，27 包起）：")
    for n, batch, leaf in lens[:5]:
        print(f"    {n:4d} 字  {leaf}  ({batch})")
    print(f"  最短 {lens[0][0]} 字 → 門檻取向下取整至十位 = {lens[0][0] // 10 * 10}")
    return 0


def self_test() -> int:
    """R-P190(iii)：以**刻意置空**之 fixture 證明本閘確實會 FAIL。"""
    real = batches()[0]
    failures = 0

    def case(label: str, batch: dict, want_fail: bool) -> None:
        nonlocal failures
        got = bool(check(batch))
        ok = got == want_fail
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G129 {label}")
        print(f"          期望 {'FAIL' if want_fail else '通過'}；"
              f"實際 {'FAIL（' + check(batch)[0]['reason'] + '）' if got else '通過'}")

    case("應通過 —— 現況之批次一", real, False)
    blanked = json.loads(json.dumps(real))
    blanked["leaves"][0]["reasoning"] = ""
    case("應 FAIL —— 刻意將第一個 leaf 之 `reasoning` 置空", blanked, True)
    stub = json.loads(json.dumps(real))
    stub["leaves"][0]["reasoning"] = "單一行為，不拆。"
    case("應 FAIL —— 以套語充數（短於門檻）", stub, True)
    dropped = json.loads(json.dumps(real))
    del dropped["leaves"][0]["reasoning"]
    case("應 FAIL —— 整個欄位不存在", dropped, True)
    print(f"\n  G129 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--calibrate" in sys.argv:
        raise SystemExit(calibrate())
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    bad = total = 0
    for b in batches():
        findings = check(b)
        n = len(b.get("leaves", []))
        total += n
        bad += len(findings)
        print(f"  {b.get('batch','?')}: {n - len(findings)} / {n} 合格")
        for f in findings:
            print(f"     **{f['leaf']}**: {f['reason']}")
    print(f"\nG129：{total - bad} / {total} leaf 之 `reasoning` 合格"
          f"（門檻 {MIN_CHARS} 字）")
    raise SystemExit(0 if not bad else 1)


if __name__ == "__main__":
    main()
