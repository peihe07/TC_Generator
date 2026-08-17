"""G28 — `Verification Criteria` / `Verification Method` 可執行性量測（R-P49）。

06 §D 之 G28 判準（分析層自裁）：

  可執行  —— 含至少一個具體可操作之條件或動作
              （具名訊號、具名 UI 元件、具體數值、具名工具指令）
  不可執行 —— 僅含泛稱環境陳述而無任何具體條件
              （例：「Vehicle equiped with CAN」）
  空      —— 不適用（G19 已證零空值）

本閘不設期望值，**首次量測即為基線**。

判定分三層：VC 單欄、VM 單欄、二欄合觀（pair）。
Phase 4 之直接輸入為二欄合觀 —— 一欄泛稱而另一欄具體者仍可執行。

具體性訊號為明列之正則（見 SIGNALS），逐 leaf 記錄命中之訊號名稱與依據字串。
邊界個案以 OVERRIDES 人工覆寫（隨腳本版控，附理由），腳本不自行判斷。

用法：
    python features/power/scripts/build_vcvm.py
"""

from __future__ import annotations

import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
IN = ROOT / "features/power/inputs"
DATA = ROOT / "features/power/data"

# 具體性訊號 —— 明列，可逐條檢驗
SIGNALS: list[tuple[str, re.Pattern]] = [
    ("具名訊號／參數", re.compile(
        r"\$[A-Za-z_]+\$"                     # $Telematic_Power$
        r"|\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+\b"   # SwitchOff_Timeout_Setting
        r"|\b[A-Z][A-Za-z0-9]*\.[A-Za-z][A-Za-z0-9_.]*\b"  # STATUS_BH_BCM1.PowerModeSts
        r"|\b[A-Z]{4,}\b"                     # PROXI / CAN / TLM
    )),
    ("具體數值", re.compile(r"\b\d+\s*(?:min|minutes|sec|seconds|s|ms|V|volts?|%)\b", re.I)),
    ("引號字面值", re.compile(r"[\"“”'][^\"“”']{2,}[\"“”']")),
    ("具名元件／畫面", re.compile(
        r"\b(?:button|screen|menu|display|icon|splash|panel|HMI|HU|TLM|ICS|AMP|FPDM|DCSD)\b", re.I)),
    ("具名狀態", re.compile(
        r"\b(?:Ignition\s+(?:On|Off|Cranking|Pre[_\s-]?Start|Pre\s+Off)"
        r"|Full[-\s]?Operation|Partial\s+Operation|Standby|Sleep|Idle|Timed|Bench"
        r"|Logistic|suspend[-\s]?resume)\b", re.I)),
    ("操作動詞", re.compile(
        r"\b(?:press|change|set|select|switch|send|apply|trigger|navigate|enter|exit|reboot)\b",
        re.I)),
]

# 邊界個案人工覆寫：leaf -> (欄位, 判定, 理由)。欄位為 'vc' / 'vm' / 'pair'。
OVERRIDES: dict[tuple[str, str], tuple[str, str]] = {
    ("SWE-PM-007", "vc"): (
        "不可執行",
        "「Vehicle not equiped with CAN or engineering line is active」—— "
        "`CAN` 雖為全大寫 token 而命中「具名訊號／參數」，但此處僅為總線之泛稱，"
        "非可設定之訊號；「engineering line is active」亦無具名訊號或設定值。"
        "全句無任何可操作之條件，與判準所舉之反例同型。",
    ),
    ("SWE-PM-009", "vm"): (
        "可執行",
        "「Perform voltag spike / drop EMC test as per CS.00244 and observe the behavior」——"
        "`CS.00244` 為具名之外部測試標準（拼字 `voltag` 為原文錯字，不影響可執行性）。"
        "正則未命中係因 `CS.00244` 之點號後為數字，不符「具名訊號」之識別式；為偽陰性。",
    ),
    ("SWE-PM-065", "vm"): (
        "可執行",
        "「Make a phone call / Disconnect phone call before Timeout1 expiration / "
        "Audio source prior to Phone Call shall be restored」——"
        "含操作動作（撥打、掛斷）與具名參數 `Timeout1`。"
        "正則未命中係因 `Timeout1` 無底線且非全大寫；為偽陰性。",
    ),
    ("SWE-PM-071", "vm"): (
        "可執行",
        "「Log timestamp checks / HIL boot test / Visual boot inspection」——"
        "`HIL` 為具名測試環境（Hardware-in-the-Loop）。"
        "正則未命中係因全大寫識別式要求 4 字元以上；為偽陰性。"
        "併觀其 VC（`SplashScreen_Time`、`StandardScreen_Time` 兩個具名參數）更為明確。",
    ),
    ("SWE-PM-072", "vm"): (
        "可執行",
        "「Log analysis / HIL test triggering events during boot / State-machine validation / "
        "Event-queue stress testing」—— `HIL` 同上為具名測試環境。"
        "併觀其 VC（`TLM_Status` 具名訊號）更為明確。",
    ),
    ("SWE-PM-008", "vc"): (
        "不可執行",
        "「Vehicle equiped with CAN」—— **判準所舉之反例本身**。"
        "`CAN` 為總線泛稱，全句無任何可操作條件。",
    ),
}


def find(pattern: str) -> Path:
    return next(f for f in IN.iterdir() if pattern in f.name)


def signals_of(text: str) -> list[tuple[str, str]]:
    """回傳 [(訊號名, 依據字串)]。"""
    hits = []
    for name, rx in SIGNALS:
        m = rx.search(text)
        if m:
            hits.append((name, m.group(0)))
    return hits


def verdict(leaf: str, field: str, text: str) -> tuple[str, list[tuple[str, str]], str]:
    hits = signals_of(text)
    if (leaf, field) in OVERRIDES:
        v, reason = OVERRIDES[(leaf, field)]
        return v, hits, reason
    if not text.strip():
        return "空", [], "（G19 已證零空值，不應出現）"
    if hits:
        return "可執行", hits, ""
    return "不可執行", [], "無任何具體性訊號命中"


def main() -> None:
    wb = openpyxl.load_workbook(find("FSM-037"), data_only=True, read_only=True)
    ws = wb["SWE1 Requirements"]
    rows = [
        (str(r[0]).strip(), str(r[16] or "").strip(), str(r[17] or "").strip())
        for r in ws.iter_rows(min_row=8, max_row=145, values_only=True)
        if r[0] and str(r[0]).strip()
    ]
    wb.close()

    test_set = {}
    for line in (DATA / "leaf_testset.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip():
            leaf, ts, _ = line.split("\t")
            test_set[leaf] = ts

    results = []
    for leaf, vc, vm in rows:
        v_vc, h_vc, r_vc = verdict(leaf, "vc", vc)
        v_vm, h_vm, r_vm = verdict(leaf, "vm", vm)
        pair = "可執行" if "可執行" in (v_vc, v_vm) else "不可執行"
        results.append({
            "leaf": leaf, "vc": vc, "vm": vm,
            "v_vc": v_vc, "v_vm": v_vm, "pair": pair,
            "h_vc": h_vc, "h_vm": h_vm, "r_vc": r_vc, "r_vm": r_vm,
            "ts": test_set.get(leaf, "（未指派）"),
        })

    bad_vc = [r for r in results if r["v_vc"] == "不可執行"]
    bad_vm = [r for r in results if r["v_vm"] == "不可執行"]
    bad_pair = [r for r in results if r["pair"] == "不可執行"]

    out = [
        "# G28 — `Verification Criteria` / `Verification Method` 可執行性（R-P49）\n",
        "\n> 判準見 06 下放包 §D 之 G28。本閘**不設期望值，首次量測即為基線**。\n",
        "> 具體性訊號為明列正則（見 `scripts/build_vcvm.py` 之 `SIGNALS`）；\n",
        "> 邊界個案以 `OVERRIDES` 人工覆寫，隨腳本版控並附理由。\n",
        "> 產生指令：`python features/power/scripts/build_vcvm.py`\n",
        f"\n## 1. 基線\n\n| 判定層 | 可執行 | 不可執行 | 母體 |\n|---|---|---|---|\n",
        f"| `Verification Criteria` 單欄 | {len(rows) - len(bad_vc)} | **{len(bad_vc)}** | {len(rows)} |\n",
        f"| `Verification Method` 單欄 | {len(rows) - len(bad_vm)} | **{len(bad_vm)}** | {len(rows)} |\n",
        f"| **二欄合觀（Phase 4 之實際輸入）** | {len(rows) - len(bad_pair)} | **{len(bad_pair)}** | {len(rows)} |\n",
        "\n二欄合觀之判定規則：任一欄可執行即為可執行 —— "
        "一欄泛稱而另一欄具體者，TC 作者仍有可操作之依據。\n",
    ]

    for label, bad, field in [("Verification Criteria", bad_vc, "vc"),
                              ("Verification Method", bad_vm, "vm")]:
        out.append(f"\n## 2.{'1' if field == 'vc' else '2'} `{label}` 判定為不可執行者"
                   f"（{len(bad)} 個）\n\n")
        if not bad:
            out.append("（無）\n")
            continue
        out.append("| leaf | Test Set | 欄位全文 | 判定依據 |\n|---|---|---|---|\n")
        for r in bad:
            text = (r[field] or "（空）").replace("\n", " ／ ").replace("|", "\\|")
            reason = (r[f"r_{field}"] or "無任何具體性訊號命中").replace("|", "\\|")
            out.append(f"| `{r['leaf']}` | {r['ts']} | {text} | {reason} |\n")

    out.append(f"\n## 3. 二欄合觀為不可執行者（{len(bad_pair)} 個）\n\n")
    if not bad_pair:
        out.append("**（無）** —— 每個 leaf 至少有一欄含具體性訊號。\n")
    else:
        out.append("| leaf | Test Set | VC | VM |\n|---|---|---|---|\n")
        for r in bad_pair:
            out.append(f"| `{r['leaf']}` | {r['ts']} | {r['vc'][:70]} | {r['vm'][:70]} |\n")

    out.append("\n## 4. 逐 leaf 明細（依據字串）\n\n")
    out.append("| leaf | VC 判定 | VC 命中訊號（依據字串） | VM 判定 | VM 命中訊號（依據字串） |\n")
    out.append("|---|---|---|---|---|\n")
    for r in results:
        def fmt(hits):
            return "；".join(f"{n}=`{s[:24]}`" for n, s in hits) or "—"
        out.append(f"| `{r['leaf']}` | {r['v_vc']} | {fmt(r['h_vc'])} | "
                   f"{r['v_vm']} | {fmt(r['h_vm'])} |\n")

    path = DATA / "g28_vcvm_quality.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes")
    print(f"G28 基線：VC 不可執行 {len(bad_vc)} / {len(rows)}；"
          f"VM 不可執行 {len(bad_vm)} / {len(rows)}；"
          f"**二欄合觀不可執行 {len(bad_pair)} / {len(rows)}**")
    for r in bad_vc:
        print(f"  VC 不可執行 {r['leaf']} ({r['ts']}): {r['vc'][:60]!r}")
    for r in bad_vm:
        print(f"  VM 不可執行 {r['leaf']} ({r['ts']}): {r['vm'][:60]!r}")


if __name__ == "__main__":
    main()
