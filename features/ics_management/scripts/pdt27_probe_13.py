#!/usr/bin/env python3
"""下放包 13 作業 C 之量測腳本（唯讀；不改任何既有檔）。

量測 `forms/PDT27_E2A_R1_BHCAN2.dbc`（未綁定，只讀）對 DR-ICS16 之填補程度，
與本 feature 已綁定之二支 DBC（R4_BHCAN／R5_FDCAN8）作發收方對照。

讀法（沿 features/ics_management/scripts/crossref_probe_12.py 之慣例）：
  - `.dbc` 一律 `latin-1` 開檔
  - `BO_` 區塊**不以空行分隔**：以 `^BO_ ` 行為分段起點自行切段，
    段內取所有以空白起首之 `SG_ ` 行；遇下一 `^BO_ ` 或任何非 `SG_` 之
    頂層關鍵字（`BO_TX_BU_`／`CM_`／`BA_`／`VAL_`／`BU_`／`BA_DEF_` …）即結束。

用法：
  python3 features/ics_management/scripts/pdt27_probe_13.py
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]

DBCS = {
    "PDT27_R1_BHCAN2 (未綁)": REPO / "forms/PDT27_E2A_R1_BHCAN2.dbc",
    "PDT27_R4_BHCAN (dbc_b)": REPO / "features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc",
    "PDT27_R5_FDCAN8 (dbc_fd)": REPO / "features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc",
}

# §1 之候選拼法：先全文搜尋確認實際拼法，不預設
NAME_PROBES = [
    "TGW_DISP_STAT",      # 佔位字面
    "TGW_DISP_STATSts",
    "DCSD_DISP_STAT",
    "Telematic_Power",    # 佔位字面
    "PowerSts_Telematic",
]

BO_RE = re.compile(r"^BO_ (\d+) (\S+?)\s*:\s*(\d+)\s+(\S+)\s*$")
SG_RE = re.compile(r"^\s+SG_ (\S+) .*?\s(\S+)\s*$")
TOPLEVEL_RE = re.compile(r"^[A-Z_]+[_ ]")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_lines(path: Path) -> list[str]:
    """latin-1 逐行讀；保留原行（去尾端換行）供逐字引用。"""
    return path.read_text(encoding="latin-1").splitlines()


def parse_bo_blocks(lines: list[str]) -> list[dict]:
    """以 `^BO_ ` 為分段起點切段，不以空行切段。"""
    blocks: list[dict] = []
    cur: dict | None = None
    for idx, raw in enumerate(lines, start=1):
        m = BO_RE.match(raw)
        if m:
            cur = {
                "lineno": idx,
                "raw": raw,
                "id": int(m.group(1)),
                "name": m.group(2),
                "dlc": int(m.group(3)),
                "sender": m.group(4),
                "sgs": [],
            }
            blocks.append(cur)
            continue
        if cur is None:
            continue
        if raw.startswith(" SG_ ") or raw.startswith("\tSG_ ") or raw.lstrip().startswith("SG_ "):
            sm = SG_RE.match(raw)
            if sm:
                cur["sgs"].append({
                    "lineno": idx,
                    "raw": raw,
                    "name": sm.group(1),
                    "receivers": sm.group(2),
                })
            continue
        if raw.strip() == "":
            continue
        # 任何其他頂層關鍵字即結束當前段
        if TOPLEVEL_RE.match(raw):
            cur = None
    return blocks


def tx_bu(lines: list[str]) -> dict[int, str]:
    out: dict[int, str] = {}
    for raw in lines:
        if raw.startswith("BO_TX_BU_ "):
            m = re.match(r"^BO_TX_BU_ (\d+)\s*:\s*(.*?);\s*$", raw)
            if m:
                out[int(m.group(1))] = raw
    return out


def main() -> None:
    for label, path in DBCS.items():
        lines = read_lines(path)
        blocks = parse_bo_blocks(lines)
        txbu = tx_bu(lines)
        print("=" * 78)
        print(f"# {label}")
        print(f"  path   : {path.relative_to(REPO)}")
        print(f"  sha256 : {sha256(path)}")
        print(f"  lines  : {len(lines)}   BO_ blocks: {len(blocks)}   BO_TX_BU_: {len(txbu)}")
        bu = [l for l in lines if l.startswith("BU_:")]
        print(f"  BU_    : {bu[0] if bu else '查無'}")
        for probe in NAME_PROBES:
            # 精確名（SG_ 名等於 probe）與含 probe 之其他名分列
            exact = [(b, s) for b in blocks for s in b["sgs"] if s["name"] == probe]
            print(f"\n  -- SG_ 名 == {probe} : {len(exact)} 筆")
            for b, s in exact:
                print(f"     BO_  L{b['lineno']}: {b['raw']}")
                print(f"     SG_  L{s['lineno']}: {s['raw']}")
                print(f"     sender={b['sender']}  receivers={s['receivers']}")
                t = txbu.get(b["id"])
                print(f"     BO_TX_BU_: {t if t else '查無'}")
        print()


if __name__ == "__main__":
    main()
