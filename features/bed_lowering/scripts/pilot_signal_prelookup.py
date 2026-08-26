#!/usr/bin/env python3
"""Pre-look-up the pilot batch's signal vocabulary in the bound DBC/LID.

Handoff 04 §二-3: a hit is recorded as a `$MESSAGE.Signal$` candidate, a miss
is recorded as 查無 (looked up, absent). The distinction this exists to
preserve is 查無 vs 沒查 -- IN §8.7.5 (d)/(g) lets a TC keep the source's own
wording only for the former. An unbound database produces neither; it
produces a guess, which is IN §8.4 fabrication.

Matching is substring-on-normalised-name and is deliberately WIDE: this stage
should over-report candidates for a human to narrow, never under-report and
let a real signal read as absent.
"""
import csv
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
FEAT = Path(__file__).resolve().parents[1]

# 取自 pilot 13 leaf 之 037 原文語彙。每組 = (標籤, 該概念之候選詞)。
# 詞由 037 原文抽出，非自 DBC 反推 —— 反推會使查詢自我實現。
# 首版之詞表取自 037 英文原文（"air suspension"/"fault"/"bed lowering"…），
# 於 DBC 訊號名上幾乎全數落空或命中雜訊（"lwr" 命中 HVAC_Blwr_Perct）。
# 成因：DBC 以模組縮寫命名，空氣懸吊控制模組為 **ASCM**，
# 而 "ASCM" 一詞不出現於 037 任何一列。
# 兩者之橋樑是 LID `CAN Mapping` 的英文描述欄（"Air suspension status" →
# `AirSuspensionStatus` → `ASCM_2.ASCM_Stat`）—— 亦即：
# **LID 不只是第四個庫，它是 037 語彙與 DBC 命名之間唯一的對照表。**
# 詞表因而改為「037 語彙 ∪ 自 LID 描述欄查得之 DBC 識別字」，兩者皆保留：
# 只留後者會使查詢自我實現（拿 DBC 的名去查 DBC）。
VOCAB = [
    ("air suspension",        ["airsusp", "air_susp", "suspension", "susp", "ascm"]),
    ("ride height / level",   ["ridehgt", "ride_height", "fl_lvl", "fr_lvl",
                               "rl_lvl", "rr_lvl"]),
    ("fault / failure",       ["sysfail", "failr", "flt", "fault"]),
    ("bed lowering",          ["bdl_", "bdlenbl", "bdl"]),
    ("service required",      ["ascm_srv", "srvs", "srv"]),
]


def load_dbc(path: Path):
    raw = path.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            text = raw.decode(enc); break
        except UnicodeDecodeError:
            continue
    msg_of = {}
    cur = None
    for line in text.splitlines():
        m = re.match(r"^BO_\s+\d+\s+([A-Za-z0-9_]+)\s*:", line)
        if m:
            cur = m.group(1); continue
        s = re.match(r"^\s*SG_\s+([A-Za-z0-9_]+)\s*(?:[Mm]\d*\s*)?:", line)
        if s and cur:
            msg_of.setdefault(s.group(1), set()).add(cur)
    return msg_of


def load_lid(path: Path):
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb["CAN Mapping"]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    return rows


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def main() -> int:
    cfg = yaml.safe_load((FEAT / "feature.yaml").read_text(encoding="utf-8"))
    ref = cfg["reference"]
    buses = {"dbc_b": load_dbc(ROOT / ref["dbc_b"]["file"]),
             "dbc_fd": load_dbc(ROOT / ref["dbc_fd"]["file"])}
    lid_rows = load_lid(ROOT / ref["lid"]["file"])
    lid_blob = [" ".join(str(c) for c in r if c is not None) for r in lid_rows]

    report = {}
    print(f"{'概念':<26} {'匯流排':<8} {'命中'}")
    print("-" * 78)
    for label, terms in VOCAB:
        entry = {"terms": terms, "dbc": [], "lid_rows": 0}
        for bus, msg_of in buses.items():
            hits = []
            for sig, msgs in msg_of.items():
                n = norm(sig)
                if any(t.replace("_", "") in n for t in terms):
                    for m in sorted(msgs):
                        hits.append(f"${m}.{sig}$")
            hits = sorted(set(hits))
            entry["dbc"].extend(hits)
            print(f"{label:<26} {bus:<8} {len(hits)}")
        lid_hits = sum(1 for b in lid_blob
                       if any(t.replace("_", "") in norm(b) for t in terms))
        entry["lid_rows"] = lid_hits
        print(f"{'':<26} {'lid':<8} {lid_hits} 列")
        report[label] = entry
        print()

    print("=" * 78)
    print("逐概念判定（查有 / 查無）")
    print("=" * 78)
    for label, e in report.items():
        n = len(e["dbc"])
        verdict = "查有" if n else ("查無（DBC）" if not e["lid_rows"] else "DBC 查無 / LID 有列")
        print(f"\n## {label}  -> {verdict}")
        print(f"   詞: {e['terms']}")
        print(f"   DBC 候選 {n} 個；LID `CAN Mapping` 命中 {e['lid_rows']} 列")
        for c in e["dbc"][:12]:
            print(f"     {c}")
        if n > 12:
            print(f"     … 另 {n - 12} 個，全文見 json")

    out = FEAT / "batches" / "pilot"
    out.mkdir(parents=True, exist_ok=True)
    f = out / "signal_prelookup.json"
    f.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n落檔 {f.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
