#!/usr/bin/env python3
"""Camera feature 自檢（四項）—— 不入 lint 序列，落檔前自跑。

CAM-05 審閱 §三-3（Pei 2026-09-23）令 `selfcheck_r_cam10.py` 更名本檔並擴為四項：

1. **R-CAM10 錨反查** —— `specification_reference` 之錨反查回 SYS-RA 來源，
   該來源之承接列須為本 TC 之 `req_id`（承接列 ＝ 引用該來源之最小 SWE ID）。
2. **proc ≥ 2 步** —— §10.5；lint 之 `E` 只判 proc/er 對齊，不判步數
   （CAM-05 §5-2 之 `NR1L-RVC-027` 初稿即 1 步而未被 lint 攔下）。
3. **RUN 重複** —— Pre-Condition 已含 `Full-Operation`（其定義已含 IGN RUN）
   而步 1 又送 `CmdIgnSts = ... (RUN)`（CAM-05 審閱 §二-1，同型第二次出現）。
4. **verbatim 保序子序列** —— `test_item_verbatim` 之 token 須為
   `source_object_id` 所指來源 `Description` 之**保序子序列**（摘句之機器判準，
   CAM-05 審閱 §一-4）；全句者自然成立，摘句者據此驗字元級忠實度。

資料：`features/camera/data/layer3_a_vf_chapters.tsv`（A 本 541 個來源引用之全量展開）
＋ 六本 SYS2 之 `Basic Report` 分頁（`F` 欄錨、`D` 欄 Description）。

    python features/camera/scripts/selfcheck_camera.py [批次目錄 …]

批次目錄預設 `features/camera/generated/pilot02`。任一項命中即 exit 1。
"""
from __future__ import annotations

import csv
import glob
import json
import re
import sys
import warnings
from pathlib import Path

import openpyxl

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[3]
XREF = ROOT / "features/camera/data/layer3_a_vf_chapters.tsv"
SYS2 = {"CFTS092": "sys2_cfts092_sysra_v01", "VF551_V2": "sys2_vf551_v2_sysra_v01",
        "VF551_V3": "sys2_vf551_v3_sysra_v01", "VF551_V33": "sys2_vf551_v33_sysra_v01",
        "VF551_V4": "sys2_vf551_v4_sysra_v01", "VF551_V42": "sys2_vf551_v42_sysra_v01"}
# 步 1 之點火送值：`Send CAN: <msg>.CmdIgnSts = 4 (RUN)`，訊息名依 EE 而異（R-CAM3(e)）
RE_RUN_STEP1 = re.compile(r"CmdIgnSts\s*=\s*(4\s*\(RUN\)|\[?RUN\]?)", re.I)
RE_STEP = re.compile(r"^\s*\d+\.\s")


def _txt(v) -> str:
    return "" if v is None else re.sub(r"\s+", " ", str(v).replace("\xa0", " ")).strip()


def owners() -> dict[str, str]:
    """SYS-RA id -> 承接之 SWE ID（最小者）。"""
    out: dict[str, str] = {}
    with XREF.open(encoding="utf-8") as fh:
        for row in list(csv.reader(fh, delimiter="\t"))[1:]:
            swe, sid = row[0], row[1]
            if sid not in out or swe < out[sid]:
                out[sid] = swe
    return out


def sys2_index() -> tuple[dict[str, str], dict[str, str]]:
    """回傳（錨 -> SYS-RA id、SYS-RA id -> Description 逐字）。

    R-CAM11 之後 `specification_reference` 寫 SYS2 `F` 欄之值，故錨須反查。
    """
    a2s: dict[str, str] = {}
    desc: dict[str, str] = {}
    for label, doc in SYS2.items():
        path = glob.glob(str(ROOT / f"sources/raw/{doc}/*.xlsx"))[0]
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for r in wb["Basic Report"].iter_rows(values_only=True):
            sid, anchor = _txt(r[1]), _txt(r[5])
            if not sid or sid == "SYS2 Sys-RA-Feature-ID":
                continue
            desc[sid] = _txt(str(r[3]).replace("_x000D_", " ") if r[3] is not None else "")
            if anchor:
                key = f"CFTS092-{anchor}" if label == "CFTS092" else anchor
                a2s.setdefault(key, sid)
        wb.close()
    return a2s, desc


def is_subsequence(short: list[str], full: list[str]) -> bool:
    """short 之 token 是否為 full 之保序子序列。"""
    it = iter(full)
    return all(tok in it for tok in short)


def main() -> None:
    dirs = [Path(a) for a in sys.argv[1:]] or [ROOT / "features/camera/generated/pilot02"]
    own = owners()
    a2s, desc = sys2_index()
    hit1: list[tuple] = []      # R-CAM10
    hit2: list[tuple] = []      # proc < 2
    hit3: list[tuple] = []      # RUN 重複
    hit4: list[tuple] = []      # 非保序子序列
    unresolved: list[tuple] = []
    no_source: list[tuple] = []
    checked = tcs = 0

    for d in dirs:
        for p in sorted(d.glob("NR1L-*.json")):
            doc = json.loads(p.read_text(encoding="utf-8"))
            req, tc_id = doc["req_id"], doc["tc_id"]
            for tc in doc["tcs"]:
                tcs += 1
                # ── 1 ── R-CAM10 錨反查
                for anchor in tc["specification_reference"].split("\n"):
                    anchor = anchor.strip()
                    if not anchor:
                        continue
                    checked += 1
                    sid = a2s.get(anchor)
                    if sid is None:
                        unresolved.append((tc_id, anchor))
                        continue
                    if own.get(sid) != req:
                        hit1.append((tc_id, req, anchor, sid, own.get(sid)))
                # ── 2 ── proc ≥ 2 步
                steps = [ln for ln in tc["test_procedure"].split("\n") if RE_STEP.match(ln)]
                if len(steps) < 2:
                    hit2.append((tc_id, len(steps)))
                # ── 3 ── Full-Operation 前提 ＋ 步 1 送 RUN
                if "Full-Operation" in tc["pre_conditions"] and steps and RE_RUN_STEP1.search(steps[0]):
                    hit3.append((tc_id, steps[0].strip()))
                # ── 4 ── verbatim 保序子序列
                sid = doc.get("source_object_id")
                verb = doc.get("test_item_verbatim", "")
                if not sid or not verb:
                    no_source.append((tc_id, sid))
                elif sid not in desc:
                    no_source.append((tc_id, sid))
                elif not is_subsequence(_txt(verb).split(), desc[sid].split()):
                    hit4.append((tc_id, sid, len(_txt(verb).split()), len(desc[sid].split())))

    print(f"Camera 自檢：批次 {[str(d) for d in dirs]}（TC {tcs} 筆）")
    print(f"  1 R-CAM10 錨反查：檢查錨 {checked} 個；無法反查 {len(unresolved)}；**命中 {len(hit1)}**")
    print(f"  2 proc ≥ 2 步　　：**命中 {len(hit2)}**")
    print(f"  3 RUN 重複　　　 ：**命中 {len(hit3)}**")
    print(f"  4 verbatim 子序列：無來源可比 {len(no_source)}；**命中 {len(hit4)}**")
    for tc_id, anchor in unresolved:
        print(f"  [1 反查失敗] {tc_id}  {anchor}")
    for tc_id, req, anchor, sid, holder in hit1:
        print(f"  [1 違反] {tc_id}（{req}）錨 {anchor} = {sid}，承接列為 {holder}")
    for tc_id, n in hit2:
        print(f"  [2 違反] {tc_id}  procedure 只有 {n} 步")
    for tc_id, step in hit3:
        print(f"  [3 違反] {tc_id}  Full-Operation 前提下步 1 又送 RUN：{step}")
    for tc_id, sid in no_source:
        print(f"  [4 無來源] {tc_id}  source_object_id={sid}")
    for tc_id, sid, n_v, n_s in hit4:
        print(f"  [4 違反] {tc_id}  verbatim（{n_v} token）非 {sid}（{n_s} token）之保序子序列")
    sys.exit(1 if (hit1 or unresolved or hit2 or hit3 or hit4 or no_source) else 0)


if __name__ == "__main__":
    main()
