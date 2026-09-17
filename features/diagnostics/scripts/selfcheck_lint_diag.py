#!/usr/bin/env python3
"""CDD-01_A T4 —— Diagnostics profile 五項 lint 之正反例自測。

每項 5 條正例（不得命中）＋ 5 條反例（須命中）。
正例命中 = 假陽性；反例未命中 = 假陰性。二者皆使該項不成立。

用法：python features/diagnostics/scripts/selfcheck_lint_diag.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))

import lint036 as L


def F(**kw) -> dict:
    """四個作者側欄之預設空值。"""
    base = {"test_item": "", "pre": "", "proc": "", "er": ""}
    base.update(kw)
    return base


CASES: dict[str, dict] = {}

# --- P-DIAG：$XXXX 白名單（R-DIAG5(a)）----------------------------------
CASES["P-DIAG"] = dict(
    fn=lambda c: L.check_diag_did(c, 1, "NR1L-DIAG-001"),
    ok=[
        F(test_item="Update the brightness of Rear view Camera via DID $283F"),
        F(pre="The radio is reading DID $2843 (X65 Module Version)"),
        F(proc="2. Send UDS request 22 28 12 via diagnostic tool"),
        F(er="The value of $BCM_Status.Signal$ is 1"),          # 帶尾 $，歸檢查 P
        F(test_item="Routine $0312 and DID $5000 are both exercised"),
    ],
    ng=[
        F(test_item="Report the value of DID $9999"),            # 不在白名單
        F(pre="Precondition references DID $F1F0"),              # CFTS004 有節但 037 未引用
        F(proc="Send UDS request for DID $7000"),                # 同上
        F(er="Expected response for $5007 is returned"),         # Mid-Range，037 未引用
        F(test_item="DID $1803 is read"),                        # Tuner Signal Strength，未引用
    ],
)

# --- U-DIAG：UDS 位元組串（R-DIAG5(b)／R-DIAG5(amend)(d)）----------------
CASES["U-DIAG"] = dict(
    fn=lambda c: L.check_diag_uds(c, 1, "NR1L-DIAG-001"),
    ok=[
        F(proc="2. Send UDS request 22 28 3F via diagnostic tool"),
        F(proc="3. Check that positive response 62 28 3F 05 is received"),
        F(proc="4. Check that negative response 7F 22 31 (requestOutOfRange) is received"),
        F(proc="4. Check that negative response 7F 22 31 (Request Out of Range) is received"),
        F(proc="2. Send UDS request 2F 50 00 03 via diagnostic tool"),
    ],
    ng=[
        F(proc="2. Send UDS request 22 283F via diagnostic tool"),       # 未每 byte 分隔
        F(proc="2. Send UDS request 22 28 3f via diagnostic tool"),      # 小寫
        F(proc="4. Check that negative response 7F 22 31 is received"),  # 缺 (<label>)
        F(proc="4. Check that negative response 7F 22 31 (Out Of Range) is received"),  # label 不在值域
        F(proc="2. Send UDS request 0x22 28 3F via diagnostic tool"),    # 帶 0x
    ],
)

# --- R1-DIAG：Requirement ID 單值（R-DIAG1(a)／R-DIAG2）------------------
CASES["R1-DIAG"] = dict(
    fn=lambda c: L.check_diag_req_id(c, 1, "NR1L-DIAG-001"),
    ok=["SWE1-Diagnostics-001", "SWE1-Diagnostics-340-001",
        "SWE1-Diagnostics-340-002", "SWE1-Diagnostics-057",
        "  SWE1-Diagnostics-388  "],
    ng=["", "SWE1-Diagnostics-001, SWE1-Diagnostics-002",
        "SWE1-Diagnostics-340", "SWE1-Diag-001", "SYS-RA-DIAG-146"],
)
# 註：`SWE1-Diagnostics-340` 無尾綴為反例 —— R-DIAG2 要求重號列一律帶 -001／-002。

# --- RM-DIAG：Remarks 定型句 --------------------------------------------
CASES["RM-DIAG"] = dict(
    fn=lambda c: L.check_diag_remarks(c, 1, "NR1L-DIAG-001"),
    ok=["", "Harman Scope: Need Rework",
        "CFTS004 Category: Out of Scope",
        "NRC per ISO 14229-1 (037 unspecified)",
        "Harman Scope: Accepted; SID per 037 SWE1-Diagnostics-058"],
    ng=["Harman Scope: Rework",                       # status 值域外
        "CFTS004 Category: OutOfScope",               # 空白不符
        "NRC per ISO 14229 (037 unspecified)",        # 缺 -1
        "SID per 037 SYS-RA-DIAG-058",                # 非 SWE1 ID
        "See CFTS004 for details"],                   # 自由散文
)


def vm(values: dict[str, str]) -> list:
    """VM-DIAG（≡ Z）之施檢：以七欄值構造一列 raw。"""
    order = list(L.VEHICLE_MODEL_HEADERS)
    raw = tuple(values[n] for n in order)
    cols = {n: i for i, n in enumerate(order)}
    return L.check_vehicle_model(raw, cols, 1, "NR1L-DIAG-001")


def row(*v: str) -> dict:
    return dict(zip(L.VEHICLE_MODEL_HEADERS, v))


CASES["VM-DIAG (= Z)"] = dict(
    fn=vm,
    ok=[row("1", "1", "1", "0", "0", "1", "1"),   # Region = All
        row("1", "1", "1", "0", "0", "0", "0"),   # Region = NAFTA
        row("1", "0", "0", "0", "0", "0", "0"),
        row("0", "0", "1", "0", "0", "1", "1"),
        row("1", "1", "1", "0", "0", "1", "0")],
    ng=[row("1", "1", "1", "1", "0", "1", "1"),   # 598 = 1（R-G74）
        row("1", "1", "1", "0", "1", "1", "1"),   # 5210 = 1
        row("1", "1", "", "0", "0", "1", "1"),    # 留空
        row("1", "1", "Y", "0", "0", "1", "1"),   # 非 0／1
        row("0", "0", "0", "0", "0", "0", "0")],  # 五有效欄無 1
)


def main() -> int:
    bad = 0
    print(f"{'check':16} {'正例(不得命中)':>16} {'反例(須命中)':>14}  判")
    for name, spec in CASES.items():
        fp = sum(1 for c in spec["ok"] if spec["fn"](c))
        fn_ = sum(1 for c in spec["ng"] if not spec["fn"](c))
        ok = (fp == 0 and fn_ == 0)
        bad += 0 if ok else 1
        print(f"{name:16} {f'5/5 通過' if fp == 0 else f'假陽性 {fp}':>16} "
              f"{f'5/5 命中' if fn_ == 0 else f'假陰性 {fn_}':>14}  {'PASS' if ok else '**FAIL**'}")
        if not ok:
            for c in spec["ok"]:
                for v in spec["fn"](c):
                    print(f"    假陽性: {v.detail} | {v.snippet!r}")
            for c in spec["ng"]:
                if not spec["fn"](c):
                    print(f"    假陰性: {c!r}")
    print("\n" + ("全部 PASS" if bad == 0 else f"**{bad} 項 FAIL**"))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
