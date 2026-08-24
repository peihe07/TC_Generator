#!/usr/bin/env python3
"""DBC independent recount (handoff 04 step 4).

Measurement conditions, declared rather than assumed:
  - encoding: the files are NOT valid UTF-8; decoded as cp1252
  - line endings: CRLF, with a handful of bare LFs in each file. Lines are
    split with str.splitlines(), which treats both as breaks — the bare-LF
    count is reported so the reader can see the files are not uniform
  - a signal DEFINITION line is a line whose lstrip() starts with 'SG_ '
    (DBC indents them under their BO_). Counted as LINES, not distinct
    names: one name can be defined in several messages
  - a message line starts with 'BO_ ' at column 0
  - the transmitting node is the LAST whitespace-separated field of the
    BO_ line
Nothing here is compared by similarity.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FILES = {
    "BHCAN2-R1": ROOT / "forms" / "PDT27_E2A_R1_BHCAN2.dbc",
    "FDCAN8-R1": ROOT / "forms" / "PDT27_E2A_R1_FDCAN8.dbc",
    "BHCAN-R4": ROOT / "features" / "vehicle_setting" / "inputs"
                / "PDT27_E2A_R4_BHCAN.dbc",
    "FDCAN8-R5": ROOT / "features" / "vehicle_setting" / "inputs"
                 / "PDT27_E2A_R5_FDCAN8.dbc",
}
DISPLAY_SIGNALS = ["DCSD_DISP_STAT", "RQ_DISP_INTS", "TGW_DISP_STATSts",
                   "CM_TCH_STAT"]

BO = re.compile(r"^BO_\s+(\d+)\s+(\S+?)\s*:\s*(\d+)\s+(\S+)\s*$")
SG = re.compile(r"^SG_\s+(\S+)\s*:\s*(.*)$")


def load(path):
    raw = path.read_bytes()
    txt = raw.decode("cp1252")
    return raw, txt.splitlines()


def parse(path):
    raw, lines = load(path)
    msgs, sig_lines, cur = {}, [], None
    for ln in lines:
        s = ln.strip()
        m = BO.match(s)
        if m:
            cur = {"id": int(m.group(1)), "name": m.group(2),
                   "dlc": int(m.group(3)), "tx": m.group(4), "signals": []}
            msgs[cur["id"]] = cur
            continue
        if s.startswith("SG_ "):
            g = SG.match(s)
            name = g.group(1)
            sig_lines.append((name, cur["id"] if cur else None,
                              cur["name"] if cur else None, g.group(2)))
            if cur:
                cur["signals"].append(name)
    vals = {}
    for ln in lines:
        s = ln.strip()
        if s.startswith("VAL_ "):
            parts = s.split(None, 3)
            if len(parts) >= 4:
                vals.setdefault((int(parts[1]), parts[2]), parts[3])
    return raw, lines, msgs, sig_lines, vals


def main():
    print("# DBC recount — measurement conditions")
    print("encoding=cp1252 (files are not valid UTF-8) | split=str.splitlines()")
    print("signal def line = lstrip() startswith 'SG_ ' (counted as LINES)")
    print("message line = 'BO_ ' at col 0 | tx node = last field of BO_ line")
    print()
    data = {}
    print("| 檔 | bytes | CRLF | bare LF | 訊號定義列 | 相異訊號名 | 訊息 |")
    print("|---|---|---|---|---|---|---|")
    for k, p in FILES.items():
        raw, lines, msgs, sig_lines, vals = parse(p)
        data[k] = (raw, msgs, sig_lines, vals)
        crlf = raw.count(b"\r\n")
        print(f"| {k} | {len(raw)} | {crlf} | {raw.count(chr(10).encode()) - crlf} "
              f"| {len(sig_lines)} | {len({s[0] for s in sig_lines})} "
              f"| {len(msgs)} |")

    a = {s[0] for s in data["BHCAN2-R1"][2]}
    b = {s[0] for s in data["BHCAN-R4"][2]}
    print()
    print("## BHCAN2-R1 vs BHCAN-R4 —— 訊號名集合三分（相異名，逐字）")
    print(f"  兩者皆有      : {len(a & b)}")
    print(f"  僅 BHCAN-R4 有: {len(b - a)}")
    print(f"  僅 BHCAN2-R1 有: {len(a - b)}")
    print(f"  僅 BHCAN2 有者全列（{len(a - b)}）: {sorted(a - b)}")

    print()
    print("## 顯示相關訊號之逐檔定位（訊息 id／發送節點／位元定義／VAL_）")
    for sig in DISPLAY_SIGNALS:
        print(f"\n### {sig}")
        found_any = False
        for k in FILES:
            raw, msgs, sig_lines, vals = data[k]
            hits = [s for s in sig_lines if s[0] == sig]
            if not hits:
                print(f"  {k}: 0 命中")
                continue
            found_any = True
            for name, mid, mname, body in hits:
                tx = msgs[mid]["tx"] if mid in msgs else "?"
                v = vals.get((mid, sig), "（無 VAL_）")
                print(f"  {k}: BO_ {mid} {mname} | tx={tx}")
                print(f"      SG_ {name} : {body}")
                print(f"      VAL_ {v}")
        if not found_any:
            print("  四檔皆 0 命中")

    print()
    print("## §3.1 所列之四個「僅 BHCAN2 有」顯示訊號 —— 逐一複驗")
    for sig in ["FPDM_DISP_STAT", "TGW_FPDM_DISP_STATSts", "FPDM_RQ_DISP_INTS",
                "CameraDisplaySts"]:
        raw, msgs, sig_lines, vals = data["BHCAN2-R1"]
        hits = [s for s in sig_lines if s[0] == sig]
        inr4 = sig in b
        print(f"\n### {sig}  (在 BHCAN-R4: {'有' if inr4 else '無'})")
        for name, mid, mname, body in hits:
            print(f"  BO_ {mid} {mname} | tx={msgs[mid]['tx']}")
            print(f"  SG_ {name} : {body}")
            print(f"  VAL_ {vals.get((mid, sig), '（無 VAL_）')}")


if __name__ == "__main__":
    main()
