"""B5 第一批 —— 依既定配方之機器改寫（69 包 §H 第 3 步 / R-P394(b)(c)）。

**不得引入新判準**（R-P394(b) / §I）。本腳本只施行既已裁定之規則：

  R1  Pre-Condition 之電源狀態 → `Apply ENTER_<STATE>`（R-P354(f) / R-P363）
  R2  `Read the HU mode/state …` → `$STATUS_TELEMATIC.PowerSts_Telematic$`（R-P353(i)）
  R3  家族 K (a) 類：ITD 內聯至回指步，ITD 改 `NA`；多行而每行一訊號一賦值者
      依 R-P373(b) 同以 (a) 內聯（真第 3 類資料集不動）
  R4  `Set <X>.Info/.Req to <v>` → `PENDING: DR-PW23 <X>`（R-P355(c)）
  R5  內部訊號作前置且為運行時 → `PENDING: DR-PW23 <X>`（R-P380(a)）
  R6  未查得之規格 `$X$`（`VC_*` / `Themed_Sound` / `VC_BODY_STYLE` / `TBM_Present`
      / `Door_Ajar_Status`）→ 去 `$`，附 `(DR-PW28)`（R-P389(c) / R-P393(a)）
  R7  `proper` / `as defined` / `normal` → 依 R-P353 末段標 `PENDING: DR-PW27`
  R8  `[1h]` 型方括號值 → `= 1 (<VAL_ 標籤>)`；`VAL_` 查無標籤者寫 `= 1`（R-P373(d)）

**A 家族（G245）之代理量不在本腳本範圍** —— R-P353 令「由執行層為每一功能指定
一個代理量並引錨點」，而該指定於 39 名上已證實**須人讀**（R-P381 / R-P384）。
機器只做上列八條規則，A 家族殘留數據實回報（R-P394(c)：不歸零即停）。

用法：
    python features/power/scripts/b5_batch1_69.py [--dry-run] [--limit N]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"
PS = "$STATUS_TELEMATIC.PowerSts_Telematic$"
MARKS = ("R-P386 第一批", "R-P386 第二批", "R-P376 丁案", "R-P383", "R-P393(c)",
         "R-P394 B5")

STATE_RAW = {"full-operation": (4, "Full_Operation"), "full_operation": (4, "Full_Operation"),
             "full operation": (4, "Full_Operation"), "idle": (3, "Idle"),
             "timed": (2, "Timed"), "standby": (1, "Standby"), "sleep": (0, "Sleep"),
             "bench": (6, "Bench"), "partial operation": (7, "Partial_Operation"),
             "partial-operation": (7, "Partial_Operation"),
             "partial_operation": (7, "Partial_Operation")}
ENTER = {v[1]: "ENTER_" + v[1].upper() for v in STATE_RAW.values()}

# R6：67/68 包實測未查得之規格名
UNRESOLVED = ("VC_VEH_BRAND", "VC_VEH_LINE", "VC_SpecialPKG", "VC_BODY_STYLE",
              "VC_SRT_PRSNT", "VC_MODEL_YEAR", "VC_Veh_Brand", "VC_SpecialPkg_IC",
              "TBM_Present", "Themed_Sound", "Door_Ajar_Status")
# R8：10a §A6 之 `VAL_`（signals.py）
VAL8 = {"PN14_LS_Actv": {0: "Not_Active", 1: "Active"},
        "PN14_LS_Lvl7": {0: "Not_Active", 1: "Active"},
        "Batt_ST_Crit": {0: "False", 1: "True"},
        "RemStActvSts": {0: "Remote Start Not Active", 1: "Remote Start Active"},
        "DriverDoorSts": {0: "Closed", 1: "Open"},
        "PsngrDoorSts": {0: "Closed", 1: "Open"},
        "Radio_btn0": {0: "Not_Pressed", 1: "Pressed"}}

RE_STATE_PRE = re.compile(
    r"^\s*(?:\d+\.\s*)?(?:The (?:HU|TLM) is in ([A-Za-z_\- ]+?)(?: (?:state|status|mode))?"
    r"|TLM_Status\.Info and \$Telematic_Power\$ read \"([A-Za-z_\- ]+)\")\s*$", re.I)
RE_HU_MODE = re.compile(
    r"Read the (?:HU|TLM) (?:mode|state)\s+and check that it is\s+([A-Za-z_\- ]+)", re.I)
RE_SET_INT = re.compile(r"Set\s+([A-Za-z0-9_]+\.(?:Info|Req))\s+to\s+\S+")
RE_BACKREF = re.compile(r"\blisted in Input Test Data\b", re.I)
RE_HEX = re.compile(r"\$?([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)\$?\s*=\s*\[(\d+)h\]")
RE_LEAK = re.compile(r"\b(proper|as defined(?: per HMI)?|normal\w*)\b", re.I)
# R2b：`Read the HU mode to check the transition to <State>` 型（無 `and check that it is`）
RE_HU_MODE2 = re.compile(
    r"Read the (?:HU|TLM) (?:mode|state)((?:,[^\n]*?)?)\s+to check[^\n]*?"
    r"\b(Full-Operation|Full_Operation|FULL OPERATION|IDLE|Idle|Timed|Standby|Sleep|Bench|"
    r"Partial[ _-]Operation)\b", re.I)
# R4b：步驟以內部訊號為讀取／設定標的者（R-P355(c)）
RE_INT_ANY = re.compile(r"\b([A-Za-z0-9_]+\.(?:Info|Req))\b|\b(RemStartFail)\b")
KEEP_INT = {"TLM_Status.Info", "LTM_OperationalModeSts.Info"}


def state_of(txt: str):
    k = txt.strip().lower().rstrip(".")
    return STATE_RAW.get(k)


def r1_r5_pre(pre: str, log: list) -> str:
    out = []
    for line in (pre or "").splitlines():
        body = re.sub(r"^\s*\d+\.\s*", "", line).strip()
        m = RE_STATE_PRE.match(line)
        if m:
            st = state_of(m.group(1) or m.group(2) or "")
            if st:
                out.append(f"Apply {ENTER[st[1]]}")
                log.append("R1")
                continue
        mi = re.search(r"\b([A-Za-z0-9_]+\.(?:Info|Req))\b|\b(RemStartFail)\b", body)
        if mi and "Apply " not in body:
            name = mi.group(1) or mi.group(2)
            if name not in ("TLM_Status.Info", "LTM_OperationalModeSts.Info"):
                out.append(f"PENDING: DR-PW23 {name}")
                log.append("R5")
                continue
        out.append(body)
    return "\n".join(f"{i}. {l}" for i, l in enumerate(out, 1))


def r6(txt: str, log: list) -> str:
    for nm in UNRESOLVED:
        if f"${nm}$" in txt:
            txt = txt.replace(f"${nm}$", nm)
            if "(DR-PW28)" not in txt:
                log.append("R6")
    return txt


def r8(txt: str, log: list) -> str:
    def rep(m):
        msg, sig, raw = m.group(1), m.group(2), int(m.group(3))
        lbl = VAL8.get(sig, {}).get(raw)
        log.append("R8")
        return (f"${msg}.{sig}$ = {raw} ({lbl})" if lbl else f"${msg}.{sig}$ = {raw}")
    return RE_HEX.sub(rep, txt)


def r2_r4_r7(txt: str, log: list) -> str:
    out = []
    for line in (txt or "").splitlines():
        body = re.sub(r"^\s*\d+\.\s*", "", line).strip()
        m2 = RE_HU_MODE2.search(body)
        if m2 and not RE_HU_MODE.search(body):
            st = state_of(m2.group(2))
            if st:
                rest = m2.group(1).strip().lstrip(",").strip()
                repl = f"Read the signal {PS} and check that it is {st[0]} ({st[1]})"
                if rest:
                    repl += f", and read {rest}"
                body = RE_HU_MODE2.sub(repl, body)
                log.append("R2")
        m = RE_HU_MODE.search(body)
        if m:
            st = state_of(m.group(1))
            if st:
                body = RE_HU_MODE.sub(
                    f"Read the signal {PS} and check that it is {st[0]} ({st[1]})", body)
                log.append("R2")
        m = RE_SET_INT.search(body)
        if m:
            body = f"PENDING: DR-PW23 {m.group(1)}"
            log.append("R4")
        else:
            mi = RE_INT_ANY.search(body)
            name = (mi.group(1) or mi.group(2)) if mi else None
            if name and name not in KEEP_INT and "PENDING" not in body:
                # R-P355(c)：該步以內部訊號為標的者，Procedure／ER 改 PENDING 佔位
                body = f"PENDING: DR-PW23 {name}"
                log.append("R4")
            elif RE_LEAK.search(body) and "PENDING" not in body:
                # R-P353 末段：`proper` / `as defined` / `normal` **不得出現**於 PROC/ER，
                # 查無定義者以 PENDING 取代該句（非附註）
                leak = RE_LEAK.search(body).group(1)
                body = f"PENDING: DR-PW27 `{leak}` 之逐字定義（原句：{body[:70]}）"
                log.append("R7")
        out.append(body)
    return "\n".join(f"{i}. {l}" for i, l in enumerate(out, 1))


def r3(tc: dict, log: list) -> None:
    itd = (tc.get("input_test_data") or "").strip()
    if not itd or itd == "NA":
        return
    if not any(RE_BACKREF.search(tc.get(f) or "")
               for f in ("test_procedure", "expected_result", "pre_conditions")):
        return
    lines = [l.strip() for l in itd.splitlines() if l.strip()]
    if len(lines) > 1:
        # R-P373(b)：多行而每行一訊號一賦值者非資料集，依 (a) 內聯 —— 每一賦值一步
        if not all(re.match(r"^[^=:]+[=:]\s*\S", l) for l in lines):
            return                       # 真第 3 類資料集，不動
        inline = "; ".join(lines)
    else:
        inline = itd
    for f in ("test_procedure", "expected_result", "pre_conditions"):
        if tc.get(f):
            tc[f] = RE_BACKREF.sub(inline, tc[f])
    tc["input_test_data"] = "NA"
    log.append("R3")


def main() -> None:
    dry = "--dry-run" in sys.argv
    limit = 70
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
    tcs = [tc for d in files.values() for tc in d["tcs"]]
    if "--redo" in sys.argv:
        # 規則擴充後，對**已標 B5** 之條重跑（規則對已改寫文本為冪等：
        # 已成 `PENDING:` 之句不再觸發）
        und = sorted((t for t in tcs if "R-P394 B5" in (t.get("remarks") or "")),
                     key=lambda t: t["tc_id"])
    else:
        und = sorted((t for t in tcs
                      if not any(x in (t.get("remarks") or "") for x in MARKS)),
                     key=lambda t: t["tc_id"])[:limit]
    print(f"未改寫 {len([t for t in tcs if not any(x in (t.get('remarks') or '') for x in MARKS)])}"
          f"；本批 {len(und)}")

    tally: dict[str, int] = {}
    for tc in und:
        log: list[str] = []
        r3(tc, log)
        tc["pre_conditions"] = r6(r8(r1_r5_pre(tc.get("pre_conditions") or "", log), log), log)
        for f in ("test_procedure", "expected_result"):
            tc[f] = r6(r8(r2_r4_r7(tc.get(f) or "", log), log), log)
        tc["input_test_data"] = r6(r8(tc.get("input_test_data") or "NA", log), log)
        if "(DR-PW28)" not in (tc.get("pre_conditions") or "") and "R6" in log:
            tc["pre_conditions"] += "\n(DR-PW28)"
        applied = sorted(set(log))
        for r in applied:
            tally[r] = tally.get(r, 0) + 1
        base = re.sub(r"\s*\(R-P394 B5[^)]*\)", "", tc.get("remarks") or "").strip()
        tc["remarks"] = (base + (" " if base else "")
                         + f"(R-P394 B5；規則 {'/'.join(applied) or '無'})")
        tc["reasoning_note"] = (tc.get("reasoning_note") or "") + (
            "\n\n**B5 第一批機器改寫（69 包 / R-P394(b)）**：施行既定配方之規則 "
            f"{'、'.join(applied) or '（無可施行之規則）'}。**未引入新判準**。"
            "A 家族（G245）之代理量須人讀指定（R-P381 / R-P384），不在機器範圍。")

    print("規則施行條數：", {k: tally[k] for k in sorted(tally)})
    if not dry:
        for p, d in files.items():
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        print("已寫回")
    else:
        print("（dry-run）")


if __name__ == "__main__":
    main()
