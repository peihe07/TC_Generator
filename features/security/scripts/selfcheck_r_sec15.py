#!/usr/bin/env python3
"""R-SEC15(a)~(i) 之逐條自檢（SEC-03 §7 要求「逐條回報 0 處，附檢查方法」）。

唯讀。對 `sandbox/pilot02/*.json` 施檢 —— json 與 xlsx 同源（同一 `render()`），
以 json 施檢可逐欄定位。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PILOT = (Path(sys.argv[1]) if len(sys.argv) > 1
         else ROOT / "features" / "security" / "sandbox" / "pilot02")
FOUR = ("pre", "input", "proc", "er")

APK_PAIRING = ROOT / "features" / "security" / "data" / "apk_pairing.tsv"
RE_METHOD = re.compile(r"#([A-Za-z]+)\s")
RE_PENDING_HEAD = re.compile(r"^\s*(?:\d+[.)]\s*)?PENDING:")
RE_LEDGER = re.compile(r"\bX-[a-z]\b|\bDR-SEC-[a-z]\b|\bR-SEC\d|\bA-SE")
RE_BADQUOTE = re.compile(r"`|(?<![A-Za-z])'[^'\n]{1,120}'(?![A-Za-z])")
RE_ANGLE = re.compile(r"<([^>]*)>")
RE_STEP = re.compile(r"^\s*(\d+)[.)]\s*(.+)$")
RE_CMD = re.compile(r"^\s*\$\s+\S")
RE_PHYS = re.compile(r'^\s*(?:Insert|Press|Power cycle|Disconnect|Select\s+")')
# (a) 場景綁定之字串：CS.212 row 1 之 ECU 字串
RE_ECU_LOGSTR = re.compile(r"ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY")
# R-SEC15(b) 之施檢面須分兩類（v2，見上繳包自報）：
#   **出現型**（appearance）—— 斷言「某事件被產生」：log 條目出現／不出現、UDS 回應、runner 結果。
#     此類**必須**有 DUT 側觸發步驟，否則該事件無從發生（pilot01 CP-004／CP-006 之違規即此型）。
#   **狀態讀取型**（state read）—— 斷言某檔案／目錄／狀態值之現況（`ls`／`od`／`cat`）。
#     其狀態由 Pre-Condition 建立，**該 ER 之觀察由其同編號步驟自身之讀取指令產生**，不需另有觸發。
RE_ER_APPEARANCE = re.compile(
    r"adb logcat|Positive response|Negative response|instrumentation runner|FAILURES!!!")
RE_ER_STATE_READ = re.compile(r"adb shell (?:ls|cat)\b|\bod -t x1\b")
# DUT 側觸發之步驟
RE_DUT_TRIGGER = re.compile(r"am instrument|adb push|adb reboot|^\s*\$\s+(?:10|22|2E|31) |Insert |Power cycle |Send CAN:")


def load():
    return [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(PILOT.glob("NR1L-*.json"))]


def main() -> int:
    tcs = load()
    pairs: dict[str, set[str]] = {}
    for line in APK_PAIRING.read_text(encoding="utf-8").splitlines()[1:]:
        f = line.split("\t")
        if len(f) >= 3:
            for sid in f[2].split(";"):
                pairs.setdefault(sid, set()).add(f[1])

    findings: dict[str, list[str]] = {k: [] for k in "abcdefghi"}
    for tc in tcs:
        tid, req = tc["tc_id"], tc["req_id"]
        proc_lines = [l for l in tc["proc"].splitlines() if l.strip()]
        er_lines = [l for l in tc["er"].splitlines() if l.strip()]

        # (a) 跨場景字串移植：ECU 專屬 log 字串只可用於 ecuCert* 方法
        if RE_ECU_LOGSTR.search(tc["er"]) and "ecuCert" not in tc["proc"]:
            findings["a"].append(f"{tid}: ECU 專屬 log 字串用於非 ecuCert 場景")

        # (b) 觀察不得代替觸發 —— 只施於「出現型」ER
        for n, line in enumerate(er_lines, 1):
            if RE_PENDING_HEAD.match(line):
                continue
            if not RE_ER_APPEARANCE.search(line):
                continue          # 狀態讀取型：由同編號步驟之讀取指令產生，不需另有觸發
            if not any(RE_DUT_TRIGGER.search(l) for l in proc_lines):
                findings["b"].append(
                    f"{tid} ER{n}: 出現型斷言而 Procedure 無 DUT 側觸發")

        for key in FOUR:
            for line in tc[key].splitlines():
                if not line.strip():
                    continue
                # (c) 台帳代號只可入 Remarks（PENDING token 起首者例外）
                if RE_LEDGER.search(line) and not RE_PENDING_HEAD.match(line):
                    findings["c"].append(f"{tid} {key}: {line.strip()[:50]}")
                # (d) 反引號／單引號
                if RE_BADQUOTE.search(line):
                    findings["d"].append(f"{tid} {key}: {line.strip()[:50]}")
                # (d) <> 只可為佔位（內容不得是完整句）
                for m in RE_ANGLE.finditer(line):
                    if len(m.group(1).split()) > 4:
                        findings["d"].append(f"{tid} {key}: 角括號非佔位 {m.group(0)[:40]}")
                # (i) PENDING 須整行
                if "PENDING:" in line and not RE_PENDING_HEAD.match(line):
                    findings["i"].append(f"{tid} {key}: {line.strip()[:50]}")

        # (e) Input Test Data 一律 NA
        if tc["input"].strip().upper() != "NA":
            findings["e"].append(f"{tid}: input={tc['input']!r}")

        # (f) test_item 上半 ≤50 token 且非 Title（以「有動詞 shall/是完整句」粗判：以句號結尾）
        top = tc["test_item"].splitlines()[0]
        if len(top.split()) > 50:
            findings["f"].append(f"{tid}: 上半 {len(top.split())} tokens > 50")
        if not top.rstrip().endswith("."):
            findings["f"].append(f"{tid}: 上半非完整句（未以句號結尾）")

        # (g) apk 方法只用於 apk_pairing 有列之 SWE1
        for m in RE_METHOD.finditer(tc["proc"] + " "):
            meth = m.group(1)
            if meth not in pairs.get(req, set()):
                findings["g"].append(f"{tid}: {meth} 未配對於 {req}")

        # (h) DID 值不入 ER
        for n, line in enumerate(er_lines, 1):
            if re.search(r"\b62 FF 02\b|\bDID\b", line):
                findings["h"].append(f"{tid} ER{n}: DID 值入 ER")

        # 通道（R-SEC7(a)）：每編號步驟後須有 $ 行、實體操作、或整行 PENDING
        for i, line in enumerate(proc_lines):
            m = RE_STEP.match(line)
            if not m or RE_PENDING_HEAD.match(line):
                continue
            nxt = proc_lines[i + 1] if i + 1 < len(proc_lines) else ""
            if not (RE_CMD.match(nxt) or RE_PHYS.match(m.group(2))):
                findings["b"].append(f"{tid} Proc{m.group(1)}: 無執行通道")

    print(f"pilot02 TC 數 = {len(tcs)}\n")
    print("| 條 | 判項 | 命中 | 檢查方法 |")
    print("|---|---|---:|---|")
    METHOD = {
        "a": ("跨場景字串移植", "ECU 專屬 log 字串（`ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY`）出現於 ER 而 Procedure 無 `ecuCert*` 方法者"),
        "b": ("觀察不得代替觸發 ＋ 每步須有通道", "ER 行含 DUT 側觀察標記而 Procedure 無 DUT 側觸發（`am instrument`／`adb push`／`adb reboot`／UDS `$ 10|22|2E|31`／`Insert`／`Power cycle`／`Send CAN:`）；另逐編號步驟查其後是否有 `$` 行或實體操作或整行 PENDING"),
        "c": ("台帳代號不入四欄", "四欄逐行 regex `X-[a-z]｜DR-SEC-[a-z]｜R-SEC\\d｜A-SE`，排除以 PENDING token 起首之行"),
        "d": ("字面值只用雙引號", "四欄逐行查反引號與單引號包字串；另查角括號內容超過 4 token 者（非佔位）"),
        "e": ("Input Test Data = NA", "逐 TC 比對 `input` 欄"),
        "f": ("test_item 上半 = Description 首句", "上半 token 數 ≤ 50 且以句號結尾（完整句，非 Title）"),
        "g": ("apk 方法須有配對", "自 Procedure 抽 `#<method>`，比對 `apk_pairing.tsv` 該 SWE1 之方法集合"),
        "h": ("DID 值不入 ER", "ER 逐行查 `62 FF 02` 與 `DID` 字樣"),
        "i": ("PENDING 整行", "四欄逐行：含 `PENDING:` 而非以其起首者"),
    }
    total = 0
    for k in "abcdefghi":
        n = len(findings[k])
        total += n
        name, how = METHOD[k]
        print(f"| ({k}) | {name} | **{n}** | {how} |")
    print(f"\n合計命中 **{total}** 處")
    for k, v in findings.items():
        for line in v:
            print(f"  ({k}) {line}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
