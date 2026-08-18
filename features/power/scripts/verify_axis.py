"""G168 —— `distinguishing_axis` 之契約檢查（R-P247）。

34 §6.5 第 3 項：`distinguishing_axis` **僅出現於 `gen_batch04/05/06.py`
三個產生器，不見於任何閘門或驗證腳本** —— 該欄所聲稱之差異軸從未被驗證。
本檔為其補閘。

**⚠ 契約原文之缺口（35 包實測）**：R-P247 稱「§4.6 已定其契約
（`axis` ∈ 列舉值；`axis="none"` ⇔ `duplicate_of` 已設）」，
惟 `§4.6` 之原文於本庫查無（`RULINGS.md` / `PLAYBOOK.md` / `DECISIONS.md` /
`RUNBOOK.md` / `docs/INDEX.md` 皆無），且 **`duplicate_of` 欄不存在於任何 TC**。
故**列舉值之清單無從取得**，執行層**不自行擬定**（比照 34 包對 G167 之處置）。

本閘就**可查證之結構**檢：

  C1 鍵組合恰為 `{axis, delta}`
  C2 `axis` 非空且為字串
  C3 `delta` 非空且為字串
  C4 `axis == "none"` 者須有 `duplicate_of` —— **列為條件式檢查**；
     語料中 `axis="none"` 現為 0，故本項現不觸發（據實標明，非「已驗通過」）
  C5 **同一 leaf 內二條之 `delta` 逐字相同** → 觸發（疑未真正互斥）

C5 為 R-P247 明令之偵測。**觸發不等於違規** —— 逐條之判定屬人工。

用法：
    python features/power/scripts/verify_axis.py
    python features/power/scripts/verify_axis.py --self-test
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

BASE_RE = re.compile(r"(SWE-PM-\d+)")


def check_one(tc: dict, n_siblings: int = 2) -> list[str]:
    """回傳該 TC 之結構違規清單（空 = 通過）。

    `n_siblings` = 該 TC 所屬 leaf 之 TC 數，供 C2 / C8 判斷。
    """
    bad = []
    d = tc.get("distinguishing_axis")
    # **C2 訂正（R-P265(b)，39 包）**：由「`axis` 須存在且非空」
    # 改為「**若該欄存在則須非空且為六值之一**」——
    # §10.1 明訂 `distinguishing_axis` 為 **optional**，
    # §4.6 明訂其輸出時機為 **`## Sibling Rows` injection** 時；
    # leaf 僅產出 1 條 TC 者無 sibling 可注入，該欄之輸出條件本即不成立。
    if d is None:
        # **C8（R-P265(c)）**：leaf 產出 ≥ 2 條 TC 者，該欄**必須存在** ——
        # 以免省略被誤用於有 sibling 之情形。
        if n_siblings >= 2:
            return [f"C8 該 leaf 產出 {n_siblings} 條 TC 而 `distinguishing_axis` 缺漏"]
        return []
    if not isinstance(d, dict):
        return [f"C1 `distinguishing_axis` 非物件（{type(d).__name__}）"]
    if set(d) != {"axis", "delta"}:
        bad.append(f"C1 鍵組合為 {sorted(d)}，應為 ['axis', 'delta']")
    axis = d.get("axis")
    if not isinstance(axis, str) or not axis.strip():
        bad.append("C2 `axis` 存在而為空或非字串")
    elif axis not in AXIS_ENUM:
        bad.append(f"C6 `axis=\"{axis}\"` 不在 §4.6 之六值列舉內")
    if not isinstance(d.get("delta"), str) or not d.get("delta", "").strip():
        bad.append("C3 `delta` 空或非字串")
    dup = str(tc.get("duplicate_of", "")).strip()
    if axis == "none" and not dup:
        bad.append("C4 `axis=\"none\"` 而 `duplicate_of` 未設")
    if dup and axis != "none":
        bad.append(f"C7 `duplicate_of` 已設而 `axis=\"{axis}\"`，應為 \"none\"")
    return bad


def run(tcs: list[dict]) -> dict:
    by_leaf: dict[str, list[dict]] = {}
    for t in tcs:
        by_leaf.setdefault(BASE_RE.match(t["req_id"]).group(1), []).append(t)
    viol = [(t["tc_id"], b) for t in tcs
            if (b := check_one(t, len(by_leaf[BASE_RE.match(t["req_id"]).group(1)])))]

    dup = []
    for leaf, group in by_leaf.items():
        seen: dict[str, list[str]] = collections.defaultdict(list)
        for t in group:
            d = t.get("distinguishing_axis") or {}
            if isinstance(d, dict) and isinstance(d.get("delta"), str):
                seen[d["delta"]].append(t["tc_id"])
        for delta, ids in seen.items():
            if len(ids) >= 2:
                dup.append((leaf, ids, delta))
    axes = collections.Counter((t.get("distinguishing_axis") or {}).get("axis")
                               for t in tcs)
    return {"viol": viol, "dup": dup, "axes": axes,
            "n_none": axes.get("none", 0)}


def self_test() -> int:
    """R-P247：以 fixture 證明本閘會 FAIL。fixture 全部自撰，不取自本語料。"""
    failures = 0

    def case(label: str, tcs: list[dict], want_viol: int, want_dup: int) -> None:
        nonlocal failures
        r = run(tcs)
        ok = len(r["viol"]) == want_viol and len(r["dup"]) == want_dup
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G168 {label}")
        print(f"          期望 違規 {want_viol} / 重複 {want_dup}；"
              f"實測 違規 {len(r['viol'])} / 重複 {len(r['dup'])}")

    def t(tid: str, req: str, axis, delta, **kw) -> dict:
        d = {"tc_id": tid, "req_id": req, **kw}
        d["distinguishing_axis"] = ({"axis": axis, "delta": delta}
                                    if axis is not None else None)
        return d

    # ⚠ 二個「應 PASS」案原用 `axis="behaviour"`，於 C6（六值列舉，R-P248）
    # 生效後即為非法 —— 36 包改用合法值 `trigger_state`。
    # **此為 fixture 隨契約更新，非放寬判準**：C6 之新增使舊 fixture 失效，
    # 該失效正是 C6 生效之證據（36 包實測：二案由 PASS 轉 FAIL）。
    case("應 PASS —— 二條 axis 相同而 delta 相異",
         [t("X-001", "SWE-PM-900", "trigger_state", "驗正向分支"),
          t("X-002", "SWE-PM-900", "trigger_state", "驗抑制分支")], 0, 0)
    case("應觸發 C5 —— 同 leaf 內 delta 逐字相同",
         [t("X-001", "SWE-PM-900", "trigger_state", "同一句話"),
          t("X-002", "SWE-PM-900", "trigger_state", "同一句話")], 0, 1)
    case("應 FAIL C3 —— `delta` 為空",
         [t("X-001", "SWE-PM-900", "trigger_state", "")], 1, 0)
    # **C2 訂正後（R-P265(b)）**：單條 leaf 缺該欄**不再違規** ——
    # §10.1 明訂其為 optional，§4.6 明訂其輸出時機為 sibling 注入時。
    case("應 PASS —— 單條 leaf 省略該欄（C2 訂正之效果）",
         [t("X-001", "SWE-PM-900", None, None)], 0, 0)
    # **C8（R-P265(c)）**：≥ 2 條之 leaf 缺該欄則違規 —— 防止省略被誤用
    case("應 FAIL C8 —— leaf 有 2 條 TC 而缺該欄",
         [t("X-001", "SWE-PM-900", None, None),
          t("X-002", "SWE-PM-900", "trigger_state", "另一分支")], 1, 0)
    case("應 FAIL C1 —— 欄位存在而非物件",
         [t("X-001", "SWE-PM-900", None, None),
          t("X-002", "SWE-PM-900", "trigger_state", "另一分支")], 1, 0)
    case("應 FAIL C4 —— `axis=\"none\"` 而無 `duplicate_of`",
         [t("X-001", "SWE-PM-900", "none", "與他條重複")], 1, 0)
    case("應 PASS C4 —— `axis=\"none\"` 且 `duplicate_of` 已設",
         [t("X-001", "SWE-PM-900", "none", "與他條重複",
            duplicate_of="X-000")], 0, 0)
    # ── C6 / C7（R-P248(a)(c)），36 包新增 ──
    case("應 FAIL C6 —— `axis` 不在六值列舉內（`behaviour`）",
         [t("X-001", "SWE-PM-900", "behaviour", "語料現行之值")], 1, 0)
    case("應 FAIL C6 —— `trigger` 近於 `trigger_state` 而不相等",
         [t("X-001", "SWE-PM-900", "trigger", "近似值亦非法")], 1, 0)
    case("應 FAIL C7 —— `duplicate_of` 已設而 `axis` 非 `none`（**反向**）",
         [t("X-001", "SWE-PM-900", "trigger_state", "有重複標記卻非 none",
            duplicate_of="X-000")], 1, 0)
    case("應 PASS —— 六值皆合法",
         [t(f"X-{i:03d}", f"SWE-PM-9{i:02d}", a, f"軸 {a}")
          for i, a in enumerate(("trigger_state", "input_data", "timing",
                                 "boundary", "mode"), 1)], 0, 0)
    print(f"\n  G168 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())

    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]
    r = run(tcs)

    out = ["# G168 —— `distinguishing_axis` 契約檢查（R-P247）\n",
           "\n> **⚠ §4.6 之契約原文於本庫查無**，`duplicate_of` 欄亦不存在於任何 TC；\n",
           "> 故 `axis` 之**列舉值清單無從取得，執行層不自行擬定**。\n",
           "> 本閘只檢可查證之結構（C1–C5）。\n",
           f"\n## 一、結構違規（C1–C4）—— **{len(r['viol'])}** 條\n\n"]
    if r["viol"]:
        out.append("| tc | 違規 |\n|---|---|\n")
        for tid, b in r["viol"]:
            out.append(f"| `{tid}` | {'；'.join(b)} |\n")
    else:
        out.append("**無。**\n")
    out.append(f"\n**C4 之現況**：`axis=\"none\"` 者 **{r['n_none']}** 條 ——"
               f"該項現**不觸發**，故其正確性**未經本批語料檢驗**"
               f"（fixture 已另行證明其會 FAIL）。\n")
    out.append(f"\n## 二、`axis` 之值分布\n\n| axis | 條數 |\n|---|---|\n")
    for k, v in r["axes"].most_common():
        out.append(f"| `{k}` | {v} |\n")
    out.append(f"\n## 三、C5 同 leaf 內 `delta` 逐字相同 —— **{len(r['dup'])}** 組\n\n"
               "> **觸發不等於違規** —— 逐組之判定屬人工。\n\n"
               "| leaf | TC | `delta` |\n|---|---|---|\n")
    for leaf, ids, delta in sorted(r["dup"]):
        out.append(f"| `{leaf}` | {'、'.join('`…-' + i[-3:] + '`' for i in ids)} | "
                   f"{delta[:88]} |\n")

    p = DATA / "g168_axis_contract.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"G168：結構違規 {len(r['viol'])}；C5 觸發 {len(r['dup'])} 組；"
          f"axis=none {r['n_none']} 條")
    for leaf, ids, delta in sorted(r["dup"]):
        print(f"   {leaf}  {[i[-3:] for i in ids]}  {delta[:70]}")
    raise SystemExit(1 if r["viol"] else 0)


# §4.6 之列舉值 —— **R-P248 逐字**（分析層於 36 包提供原文）。
# 09 包以降執行層無該原文可查，故 35 包之 G168 未設本項；
# **當時之「結構違規 0」為對照表缺漏，非判定錯誤**（A-PW197 依 R-P248 結案）。
AXIS_ENUM = ("trigger_state", "input_data", "timing", "boundary", "mode", "none")


if __name__ == "__main__":
    main()
