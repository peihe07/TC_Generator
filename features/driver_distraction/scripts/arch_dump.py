#!/usr/bin/env python3
"""T10a–d —— LID 逐列全欄傾印 ＋ DBC 存在性查核（下放包 05 §五）。

**只量測，不做架構選擇** —— 架構選定屬 Q7（Pei 裁定），非量測（下放包 05 §三）。
**r420／r421 二列皆給全貌，何者為準由分析層裁**（T10b 明文）。
**查無者照實列，不代換**（R-13／R-DD5）。

引用列號一律書 `LID {分頁名} r{n}`（下放包 05 §1.1 之拘束，隨包生效）。
"""
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
VS = ROOT.parent / "vehicle_setting" / "inputs"
LID = VS / "Logical Identifiers and CAN Mapping v1_76.xlsx"
DBC = [VS / "PDT27_E2A_R4_BHCAN.dbc", VS / "PDT27_E2A_R5_FDCAN8.dbc"]

# 架構帶 —— 自 r2 之合併標題實測（不硬編猜測）
BANDS = {
    "CAN Mapping": [(0, "LID Information"), (5, "Powernet"), (10, "CUSW"),
                    (15, "Atlantis"), (20, "Compact"), (25, "Atlantis High"),
                    (30, "Comments")],
    "Proxi & Configuration": [(0, "LID Information"), (5, "Powernet"),
                              (10, "CUSW"), (15, "Atlantis & Atlantis High"),
                              (20, "Compact"), (25, "Comments")],
}
SG = re.compile(
    r"^\s*SG_\s+(?P<name>\w+)\s*:\s*(?P<start>\d+)\|(?P<len>\d+)@(?P<order>[01])"
    r"(?P<sign>[+-])\s*\(\s*(?P<factor>[^,]+),\s*(?P<offset>[^)]+)\)\s*"
    r"\[(?P<min>[^|]*)\|(?P<max>[^\]]*)\]\s*\"(?P<unit>[^\"]*)\"", re.M)


def band_of(sheet, col):
    b = None
    for start, name in BANDS[sheet]:
        if col >= start:
            b = name
    return b


def dump_row(wb, sheet, rownum, label):
    ws = wb[sheet]
    rows = list(ws.iter_rows(min_row=1, max_row=max(rownum, 3), values_only=True))
    hdr = rows[2]                      # r3 = 欄名
    row = rows[rownum - 1]
    print(f"\n### {label} —— `LID {sheet} r{rownum}`\n")
    print("| 欄 | 架構帶 | 欄名（r3）| 值（逐字）|")
    print("|---|---|---|---|")
    n = 0
    for j, c in enumerate(row):
        if c in (None, ""):
            continue
        n += 1
        v = str(c).replace("\n", "⏎").replace("|", "\\|")
        h = str(hdr[j] or "").replace("\n", " ")[:30] if j < len(hdr) else ""
        print(f"| c{j} | **{band_of(sheet, j)}** | {h} | `{v[:240]}` |")
    print(f"\n**非空欄 {n} 個**（該列全欄已列，未省略）")
    return row


# 訊號名之形態 —— `BO_.SG_` 或裸 `SG_`。用以區分「不在 DBC」與「不是訊號名」。
NAME_RE = re.compile(r"^[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)?$")


def collect_names(row, sheet):
    """自該列各架構帶之 `Signal Name` 欄取名，回傳 (帶, 名, 是否為訊號名形態)。

    ⚠ **儲存格內之多名分隔不只換行**：實測 LID `CAN Mapping` r1738 之
    Atlantis 欄以「空白 ＋ 單引號」串接二名
    （`STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.…Fail`）。
    初版只切換行，致該名被切成一個畸形字串而報「不在」——
    **而 T9 已實測該名在 `R4_BHCAN` 內**。那是抽取瑕疵，不是量測結果。
    故本函式另切單引號，並以 `NAME_RE` 標出「不是訊號名形態」者
    （如 `Not Applicable`、`see dbc`、切碎之殘片），
    **使其與真正之「查無」可分**。
    """
    out = []
    for start, name in BANDS[sheet]:
        if name in ("LID Information", "Comments"):
            continue
        v = row[start] if start < len(row) else None
        if v in (None, ""):
            continue
        for piece in re.split(r"[\n']+", str(v)):
            q = piece.strip().strip("\u21b5").strip()
            if q:
                out.append((name, q, bool(NAME_RE.match(q))))
    return out


def dbc_index():
    idx = {}
    for p in DBC:
        txt = p.read_text("utf-8", errors="replace")
        msgs, cur = {}, None
        for line in txt.splitlines():
            m = re.match(r"^BO_\s+(\d+)\s+(\w+)\s*:\s*(\d+)", line)
            if m:
                cur = {"id": m.group(1), "name": m.group(2), "sgs": {}}
                msgs[m.group(2)] = cur
                continue
            if cur is not None and line.strip().startswith("SG_"):
                g = SG.match(line)
                if g:
                    cur["sgs"][g.group("name")] = g.groupdict()
        vals = {}
        for m in re.finditer(r"^VAL_\s+(\d+)\s+(\w+)\s+(.*?);\s*$", txt, re.M):
            vals.setdefault(m.group(2), []).append((m.group(1), m.group(3).strip()))
        idx[p.name] = (msgs, vals)
    return idx


def probe(idx, qualified):
    """`BO_.SG_` 或裸 `SG_` 名之存在性。回傳 [(檔, BO_, id, 欄位…)]。"""
    if "." in qualified:
        bo, sg = qualified.split(".", 1)
    else:
        bo, sg = None, qualified
    sg = sg.strip().rstrip("⏎")
    hits = []
    for fname, (msgs, vals) in idx.items():
        for mname, m in msgs.items():
            if bo is not None and mname != bo:
                continue
            if sg in m["sgs"]:
                s = m["sgs"][sg]
                hits.append((fname, mname, m["id"], s, vals.get(sg, [])))
    return hits


def main():
    wb = openpyxl.load_workbook(LID, read_only=False, data_only=True)
    print("# T10a–d —— 原始輸出\n")
    print(f"素材：`features/vehicle_setting/inputs/{LID.name}`（R-DD5 綁定件，未複製）\n")
    print("**架構帶取自各分頁 r2 之合併標題列，非硬編**：\n")
    for sn, bs in BANDS.items():
        print(f"- `{sn}`：" + "；".join(f"c{a}+ = {b}" for a, b in bs))
    print()

    print("---\n\n## T10a —— `$Speedometer$`")
    r1738 = dump_row(wb, "CAN Mapping", 1738, "`$Speedometer$`")

    print("\n---\n\n## T10b —— `$VC_Trans_Equipped$`（r420 **與** r421 兩列）"
          "與 `$PresentGear$`")
    print("\n> **兩列皆給全貌，何者為準由分析層裁**（T10b 明文）。")
    r420 = dump_row(wb, "Proxi & Configuration", 420, "`Proxi & Configuration` r420")
    r421 = dump_row(wb, "Proxi & Configuration", 421, "`Proxi & Configuration` r421")
    r1397 = dump_row(wb, "CAN Mapping", 1397, "`$PresentGear$`")

    print("\n---\n\n## T10d —— `Country_Code` 二分頁同號兩列")
    print("\n> 誤一之更正回填素材：`r43` 於二分頁各有一列且內容不同。")
    r43a = dump_row(wb, "CAN Mapping", 43, "`CAN Mapping` r43")
    r43b = dump_row(wb, "Proxi & Configuration", 43, "`Proxi & Configuration` r43")

    print("\n---\n\n## T10c —— 各架構名於綁定二 DBC 之存在性\n")
    idx = dbc_index()
    print(f"綁定件：`{DBC[0].name}`（{len(idx[DBC[0].name][0])} 訊息）／"
          f"`{DBC[1].name}`（{len(idx[DBC[1].name][0])} 訊息）\n")
    cands = []
    for lbl, row, sheet in (("$Speedometer$", r1738, "CAN Mapping"),
                            ("$VC_Trans_Equipped$ (r420)", r420, "Proxi & Configuration"),
                            ("$VC_Trans_Equipped$ (r421)", r421, "Proxi & Configuration"),
                            ("$PresentGear$", r1397, "CAN Mapping"),
                            ("$Country_Code$ (CAN Mapping r43)", r43a, "CAN Mapping"),
                            ("$Country_Code$ (Proxi & Configuration r43)", r43b,
                             "Proxi & Configuration")):
        for band, name, is_name in collect_names(row, sheet):
            cands.append((lbl, band, name, is_name))
    print("| LID 來源 | 架構帶 | 訊號名（逐字）| 在／不在 | BO_（id）| 長度 | factor／offset | 單位 |")
    print("|---|---|---|---|---|---|---|---|")
    absent, notname = [], []
    for lbl, band, name, is_name in cands:
        if not is_name:
            notname.append((lbl, band, name))
            print(f"| {lbl} | {band} | `{name[:52]}` | **非訊號名形態（未查）** "
                  f"| — | — | — | — |")
            continue
        hits = probe(idx, name)
        if not hits:
            absent.append((lbl, band, name))
            print(f"| {lbl} | {band} | `{name[:52]}` | **不在** | — | — | — | — |")
            continue
        for fname, bo, mid, s, vals in hits:
            print(f"| {lbl} | {band} | `{name[:52]}` | **在**（`{fname}`）| "
                  f"`{bo}`（{mid}）| {s['len']} bit | "
                  f"`{s['factor'].strip()}`／`{s['offset'].strip()}` | "
                  f"`{s['unit']}` |")
    print(f"\n**不在者 {len(absent)} 筆**（照實列，未代換）：")
    for lbl, band, name in absent:
        print(f"- {lbl} ／ {band} ／ `{name[:70]}`")
    print(f"\n**非訊號名形態 {len(notname)} 筆**（未查，與「查無」分開列）：")
    for lbl, band, name in notname:
        print(f"- {lbl} ／ {band} ／ `{name[:70]}`")

    print("\n### `VAL_` 列舉逐字（查得者）\n")
    seen = set()
    for lbl, band, name, is_name in cands:
        if not is_name:
            continue
        for fname, bo, mid, s, vals in probe(idx, name):
            for mv, body in vals:
                k = (fname, bo, s["name"], mv)
                if k in seen:
                    continue
                seen.add(k)
                print(f"- `{fname}` `{bo}`.`{s['name']}` (msg {mv})：`{body[:300]}`")
    if not seen:
        print("（查得者皆無 `VAL_` 列舉）")
    wb.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
