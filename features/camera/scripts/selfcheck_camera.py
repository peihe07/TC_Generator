#!/usr/bin/env python3
"""Camera feature 自檢（四項）—— 不入 lint 序列，落檔前自跑。

CAM-05 審閱 §三-3（Pei 2026-09-23）令 `selfcheck_r_cam10.py` 更名本檔並擴為四項：

1. **R-CAM10 錨反查** —— `specification_reference` 之錨反查回 SYS-RA 來源，
   該來源之承接列須為本 TC 之 `req_id`（承接列 ＝ 引用該來源之最小 SWE ID）。
   **例外（CAM-07 §2，R-CAM14(b) 所迫）**：反查所得之列其 `Category` 為 `Information`
   **且**於 `layer3_a_vf_chapters.tsv` 零命中者，為**標定常數錨**（VF 常數表之值列，
   037 從未引用）。R-CAM10 之規範對象為「037 兩列以上共引同一來源」，
   未被 037 引用之列不可能被共引，故不在其射程 —— 另計一類「常數錨」，不判違反。
   其餘無法反查者仍為 `反查失敗`。
   **多錨之例外（R-CAM10(b)，CAM-06 審閱 §二-4）**：同一行為之 IF 來源與 THEN 來源
   分屬兩承接列時合為一個 TC，其 `specification_reference` 有兩個（以上）非常數錨。
   該情形之判準改為「`req_id` ＝ 諸錨承接列之**最小者**」，逐錨相等之要求不適用；
   另計一類「合一錨」。單錨 TC 仍逐錨相等。
   **共引之例外（R-CAM19(b)，CAM-26）**：R-CAM10 之「較大 SWE ID 不得再以共引來源作錨」撤銷 ——
   單錨 TC 之 `req_id` 不等於承接列、但**為 037 引用該來源之列之一**者，另計一類「共引錨」，不判違反；
   `req_id` 根本不引用該來源者仍為違反。
   **缺件佔位（R-CAM19(d)，CAM-26）**：`specification_reference` 之每一行皆以 `PENDING: DR-` 起首者
   （來源文件未到，無錨可寫），不入第 1 項之反查、第 4 項之子序列與第 8b 項，另計一類「缺件佔位」；
   其 Procedure 仍須 ≥ 2 步（第 2 項）且 `PENDING:` 仍須落於行首（第 8a 項）。
2. **proc ≥ 2 步** —— §10.5；lint 之 `E` 只判 proc/er 對齊，不判步數
   （CAM-05 §5-2 之 `NR1L-RVC-027` 初稿即 1 步而未被 lint 攔下）。
3. **電源態 ↔ 點火步之一致性（雙向）**（CAM-08 審閱 §二-2）——
   `3a 重複`：Pre-Condition 首行為 `Full-Operation`（其定義已含 IGN RUN）而步 1 又送
   `CmdIgnSts = ... (RUN)`（CAM-05 審閱 §二-1）。二者擇一處置：**非開機類**刪步 1；
   **開機類**（該 TC 之驗證目標即開機序列）首行改 `Standby`（profile §4）。
   `3b 矛盾`：Pre-Condition 首行為 `Standby`（HU 已斷電）而 Procedure **無**任何點火步 ——
   該態下不送點火則 HU 不會起來，其後各步皆不可執行。
4. **verbatim 保序子序列** —— `test_item_verbatim` 之 token 須為
   `source_object_id` 所指來源 `Description` 之**保序子序列**（摘句之機器判準，
   CAM-05 審閱 §一-4）；全句者自然成立，摘句者據此驗字元級忠實度。
5. **CAN source 行之適用條件**（**R-CAM3(f)**，CAM-07 審閱 §二-1）—— Pre-Condition 之
   `CAN source:` 行只為「TC **同時**勾 Atl-Hi（`HDCC27`／`DT27`）與 Atl-Mi
   （`VF(ProMaster)637`／`Toro(2261)`／`Fastack (376)`）車型，**且** Procedure 含
   `Send CAN` 步」而設。單一 EE 之列直接以該平台訊息名寫，不加該行；
   無 `Send CAN` 步者該行無代換對象。二條件任一不成立而仍有該行者命中。
6. **設定操作句式**（canon §5.8(e)，CAM-07 審閱 §二-2）—— Procedure 不得寫
   `Select "<label>" and set it to <value>`；一律 `Set "<label>" = "<Option>"`，
   `<Option>` 逐字取 HMI Settings List 該列之選項 label。命中即違規。
7. **點火動作須為 CAN 式**（CAM-08 審閱 §二-1）—— Procedure 不得以散文寫點火
   （`Cycle the ignition`／`Turn the ignition`／`Power on the HU`／`Power cycle`）；
   一律 `Send CAN: <MSG>.CmdIgnSts = <raw> (<label>)`（單 EE 直寫，跨 EE 依 R-CAM3(e)／(f)）。
   其目的子句（`… so that the HU reads the PROXI configuration`）移入 ER。
9. **不可注入之訊號**（profile §7.6，CAM-13 審閱 §一-3）——
   Procedure 之 `Send CAN: <MSG>.<Sig>` 其訊號於 `CameraEventHal status.xlsx` 為
   `Supported by Harman = N` **且** `MD fake CEH status = Not yet`（A-CA16 之「兩者皆是」），
   **並且** `ANOMALIES.md` 有同時提及該訊號與「不可注入／不走 CAN」之列者 → 命中。
   兩個條件皆須成立 —— 只有 `N` 而 CEH 註 `could emulate` 者可注入，不命中。
   該類訊號不可注入，TC 須改以其等價之可判態表達（A-CA16／A-CA17 之處置）。

8. **`PENDING:` 之落點**（§8.4.3，CAM-10 審閱 §二-1）——
   `8a`：`PENDING:` 只得出現於**編號項或子項之行首**（`1. PENDING: …`／`a. PENDING: …`），
   不得嵌入句中 —— 嵌入者其缺值之範圍不可辨。
   `8b`：同一 `DR-CAM-x` 之 `PENDING` 同時出現於 `pre_conditions` 與 `expected_result` 者，
   多為缺值只在 ER 而 Pre-Condition 重複宣告；**佔位只落於缺值之欄**（§8.4.3）。
   本項為**提示**（兩欄確各有缺值時為誤報），命中須逐列覆核。

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
# 第 5 項：Pre-Condition 之 CAN source 行；第 6 項：canon §5.8(e) 之反例句式
RE_CANSRC = re.compile(r"^\s*\d+\.\s*CAN source:", re.I)
RE_SENDCAN = re.compile(r"Send CAN:", re.I)
RE_SETSTYLE = re.compile(r'Select\s+".+?"\s+and\s+set\s+it\s+to', re.I)
# 第 7 項：散文式點火動作；第 3b 項：Standby 首行卻無點火步
RE_IGNPROSE = re.compile(r"\b(Cycle the ignition|Turn the ignition|Power on the HU|Power cycle)", re.I)
RE_STANDBY = re.compile(r"^\s*1\.\s*The HU is in Standby state", re.I)
RE_FULLOP1 = re.compile(r"^\s*1\.\s*The HU is in the Full-Operation state", re.I)
VM_HI = ("HDCC27", "DT27")
VM_MI = ("VF(ProMaster)637", "Toro(2261)", "Fastack (376)")
# 第 8 項：PENDING 之落點
RE_PEND_OK = re.compile(r"^\s*(?:\d+\.|[a-z]\.)\s*PENDING:")
RE_PEND_ANY = re.compile(r"PENDING:")
RE_DRID = re.compile(r"DR-CAM-[a-z]")
# 第 9 項：不可注入之訊號（CEH 表 ＋ ANOMALIES）
CEH = ROOT / "sources/raw/camera_event_hal_status"
ANOM = ROOT / "features/camera/ANOMALIES.md"
RE_SENDSIG = re.compile(r"Send CAN:\s*([A-Za-z0-9_]+\.[A-Za-z0-9_]+)")
# B 本（SYS1）之錨母體：`spec-index/cache/` 兩本（R-CAM6 裁 cache 本為追溯母體）
SYS1_CACHE = ROOT / "spec-index/cache"
SYS1_BOOKS = ["SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_"
              "(February_10th, 2023).xlsx",
              "SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021).xlsx"]
RE_B_REQ = re.compile(r"^SWE1-RVC-")
# ── 第 10 項（**WARN 級**，DECISIONS 6-76）：拆解充分性之候選
# 母體為來源 `Description` 全文（profile §7.7），先剝除影像 token
# （其 URL 編碼 `%E5%9C%96%E7%89%87_…` 會被數值偵測器讀成 `96 %`，CAM-22 §7-1）。
RE_IMG = re.compile(r"\(image:[^)]*\)|\b[\w%.]+\.(?:png|jpg|jpeg|gif)\b", re.I)
RE_A10_NUM = re.compile(r"\b(\d+(?:[.,]\d+)?)\s*(seconds?|sec|mph|km/h|%|characters?|lines?)", re.I)
RE_A10_NEG = re.compile(r"\b(cannot|greyed out|grey out|lock(?:ed)? out|unavailable|"
                        r"does not|will not|shall not)\b", re.I)
RE_A10_BULLET = re.compile(r"[\u25cf\u25cb\u25a0]\s*([A-Z][^\u25cf\u25cb\u25a0]{4,80})")
RE_A10_SERIES = re.compile(r"((?:[A-Z][\w/ +]{2,30}, ){2,}(?:and |or )?[A-Z][\w/ +]{2,30})")
# 導航 hop 之首詞（profile §5.3 之常數），第 10 項之多觸發偵測須排除（GCB-11 同因）
NAV_HOP = re.compile(r'^\s*\d+\.\s*(Press "Apps"|Select "Settings"|Select "Camera"|'
                     r'Select "Aux Cameras"|Select the Camera app)')


def _txt(v) -> str:
    return "" if v is None else re.sub(r"\s+", " ", str(v).replace("\xa0", " ")).strip()


RE_PEND_ANCHOR = re.compile(r"^\s*PENDING:\s*DR-")


def citers() -> dict[str, set[str]]:
    """SYS-RA id -> 037 中引用該來源之全部 SWE ID（R-CAM19(b) 之共引母體）。"""
    out: dict[str, set[str]] = {}
    with XREF.open(encoding="utf-8") as fh:
        for row in list(csv.reader(fh, delimiter="\t"))[1:]:
            out.setdefault(row[1], set()).add(row[0])
    return out


def owners() -> dict[str, str]:
    """SYS-RA id -> 承接之 SWE ID（最小者）。"""
    out: dict[str, str] = {}
    with XREF.open(encoding="utf-8") as fh:
        for row in list(csv.reader(fh, delimiter="\t"))[1:]:
            swe, sid = row[0], row[1]
            if sid not in out or swe < out[sid]:
                out[sid] = swe
    return out


def sys2_index() -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """回傳（錨 -> SYS-RA id、SYS-RA id -> Description 逐字、SYS-RA id -> Category）。

    R-CAM11 之後 `specification_reference` 寫 SYS2 `F` 欄之值，故錨須反查。
    """
    a2s: dict[str, str] = {}
    desc: dict[str, str] = {}
    cat: dict[str, str] = {}
    for label, doc in SYS2.items():
        path = glob.glob(str(ROOT / f"sources/raw/{doc}/*.xlsx"))[0]
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for r in wb["Basic Report"].iter_rows(values_only=True):
            sid, anchor = _txt(r[1]), _txt(r[5])
            if not sid or sid == "SYS2 Sys-RA-Feature-ID":
                continue
            desc[sid] = _txt(str(r[3]).replace("_x000D_", " ") if r[3] is not None else "")
            cat[sid] = _txt(r[10])
            if anchor:
                key = f"CFTS092-{anchor}" if label == "CFTS092" else anchor
                a2s.setdefault(key, sid)
        wb.close()
    return a2s, desc, cat


def sys1_index() -> tuple[dict[str, str], dict[str, str]]:
    """回傳（`{檔名}_{章節號}` 錨 -> Polarion ID、Polarion ID -> Description 逐字）。

    檔名之 token 化依 canon §10.7(b)：**只換空白**，其餘字元逐字（DECISIONS 6-48）。
    """
    a2p: dict[str, str] = {}
    desc: dict[str, str] = {}
    for book in SYS1_BOOKS:
        path = SYS1_CACHE / book
        if not path.exists():
            continue
        stem = path.stem.replace(" ", "_")
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        for r in wb["Basic Report"].iter_rows(min_row=2, values_only=True):
            pid, outline = _txt(r[0]), _txt(r[2])
            if not pid or not outline:
                continue
            a2p.setdefault(f"{stem}_{outline}", pid)
            desc.setdefault(pid, _txt(str(r[3]).replace("_x000D_", " ")
                                      if r[3] is not None else ""))
        wb.close()
    return a2p, desc


def ceh_blocked() -> dict[str, str]:
    """CameraEventHal 表中 `N`／`Not yet` 之訊號 -> 其理由欄。"""
    out: dict[str, str] = {}
    paths = glob.glob(str(CEH / "*.xlsx"))
    if not paths:
        return out
    wb = openpyxl.load_workbook(paths[0], read_only=True, data_only=True)
    for r in wb.worksheets[0].iter_rows(values_only=True):
        sig = _txt(r[0])
        if not sig or sig.lower().startswith("source signal"):
            continue
        sup, fake = _txt(r[3]).upper(), _txt(r[5]).lower()
        if sup == "N" and "not yet" in fake:      # A-CA16 之「兩者皆是」
            out[sig] = _txt(r[7]) or f"Harman={sup or '-'} / CEH={fake or '-'}"
    wb.close()
    return out


def strip_img(t: str) -> str:
    return re.sub(r"\s+", " ", RE_IMG.sub(" ", t)).strip()


def check10(desc: str, tc: dict, sibs: int) -> list[str]:
    """第 10 項（WARN）：拆解充分性之候選軸。回傳命中之軸名。"""
    axes: list[str] = []
    blob = "\n".join(tc[k] for k in ("pre_conditions", "test_procedure", "expected_result"))
    if desc:
        items = [m.group(1).strip() for m in RE_A10_BULLET.finditer(desc)]
        if not items:
            m = RE_A10_SERIES.search(desc)
            if m:
                items = [x.strip() for x in re.split(r",\s*(?:and |or )?", m.group(1)) if x.strip()]
        if len(items) > sibs:
            axes.append(f"列舉({len(items)}>{sibs})")
        nums = {n for n, _ in RE_A10_NUM.findall(desc) if n.isdigit()}
        if nums:
            innum = set(re.findall(r"\b(\d+)\b", blob))
            # 6-76(a)：limit 與 limit±1 **任一**出現即通過（A-CA30 之故）
            ok = {v for v in nums
                  if v in innum or str(int(v) - 1) in innum or str(int(v) + 1) in innum}
            if ok != nums:
                axes.append("boundary(" + "／".join(sorted(nums - ok)) + ")")
        if RE_A10_NEG.search(desc) and not RE_A10_NEG.search(tc["expected_result"]) and sibs < 2:
            axes.append("negative")
    # 6-76(b)：多觸發併列 —— 排除 §5.3 之導航 hop
    trig = [ln for ln in tc["test_procedure"].split("\n")
            if re.match(r"^\s*\d+\.\s*(Send CAN|Press|Select|Set |Type|Tap|Drag|Pinch|Plug)", ln)
            and not NAV_HOP.match(ln)]
    kinds = {re.match(r"^\s*\d+\.\s*(\w+)", t).group(1) for t in trig}
    if len(trig) >= 3 and len(kinds) >= 3:
        axes.append(f"多觸發({len(trig)}步/{len(kinds)}種)")
    return axes


def is_subsequence(short: list[str], full: list[str]) -> bool:
    """short 之 token 是否為 full 之保序子序列。"""
    it = iter(full)
    return all(tok in it for tok in short)


def main() -> None:
    dirs = [Path(a) for a in sys.argv[1:]] or [ROOT / "features/camera/generated/pilot02"]
    own = owners()
    cite = citers()
    a2s, desc, cat = sys2_index()
    a2p, desc1 = sys1_index()
    hit1: list[tuple] = []      # R-CAM10
    hit2: list[tuple] = []      # proc < 2
    hit3: list[tuple] = []      # RUN 重複
    hit4: list[tuple] = []      # 非保序子序列
    unresolved: list[tuple] = []
    constant: list[tuple] = []   # 標定常數錨（Information 且 037 未引）
    merged: list[tuple] = []     # R-CAM10(b) 合一錨
    cocited: list[tuple] = []    # R-CAM19(b) 共引錨
    placeholder: list[str] = []  # R-CAM19(d) 缺件佔位
    hit5: list[tuple] = []       # CAN source 行之適用條件（R-CAM3(f)）
    hit6: list[tuple] = []       # 設定操作句式（canon §5.8(e)）
    hit3b: list[tuple] = []      # Standby 首行卻無點火步
    hit7: list[tuple] = []       # 散文式點火動作
    hit8a: list[tuple] = []      # PENDING 嵌入句中
    hit8b: list[tuple] = []      # 同一 DR 之 PENDING 跨 pre 與 er
    hit9: list[tuple] = []       # 不可注入之訊號
    warn10: list[tuple] = []     # 第 10 項（WARN）：拆解充分性候選
    blocked = ceh_blocked()
    anom = ANOM.read_text(encoding="utf-8") if ANOM.exists() else ""
    no_source: list[tuple] = []
    checked = tcs = 0

    # 先掃一遍以取 sibling 數（同一 source_object_id 之 TC 數）
    sib_n: dict[str, int] = {}
    for d in dirs:
        for p in sorted(d.glob("NR1L-*.json")):
            sid0 = json.loads(p.read_text(encoding="utf-8")).get("source_object_id")
            sib_n[sid0] = sib_n.get(sid0, 0) + 1
    for d in dirs:
        for p in sorted(d.glob("NR1L-*.json")):
            doc = json.loads(p.read_text(encoding="utf-8"))
            req, tc_id = doc["req_id"], doc["tc_id"]
            for tc in doc["tcs"]:
                tcs += 1
                # ── 1 ── R-CAM10 錨反查（含 (b) 之多錨合一）
                is_b = bool(RE_B_REQ.match(req))
                spec_lines = [a for a in tc["specification_reference"].split("\n") if a.strip()]
                is_ph = bool(spec_lines) and all(RE_PEND_ANCHOR.match(a) for a in spec_lines)
                if is_ph:
                    placeholder.append(tc_id)
                owned: list[tuple[str, str, str]] = []   # (anchor, sid, holder)
                for anchor in tc["specification_reference"].split("\n"):
                    anchor = anchor.strip()
                    if not anchor or is_ph:
                        continue
                    checked += 1
                    if is_b:
                        # B 本：錨為 `{SYS1 檔名}_{章節號}`，只驗可反查 ——
                        # R-CAM10 之委派制以 037 A 本之 SYS-RA 對照為母體，不及於 B 本
                        if anchor not in a2p:
                            unresolved.append((tc_id, anchor))
                        continue
                    sid = a2s.get(anchor)
                    if sid is None:
                        unresolved.append((tc_id, anchor))
                        continue
                    holder = own.get(sid)
                    if holder is None and cat.get(sid, "").lower() == "information":
                        constant.append((tc_id, anchor, sid))   # 標定常數錨，不在 R-CAM10 射程
                    else:
                        owned.append((anchor, sid, holder))
                if len(owned) >= 2:
                    # R-CAM10(b)：req_id 須為諸錨承接列之最小者
                    holders = [h for _, _, h in owned]
                    if None in holders or req != min(holders):
                        hit1.append((tc_id, req, "＋".join(a for a, _, _ in owned),
                                     "＋".join(sid for _, sid, _ in owned),
                                     f"min={None if None in holders else min(holders)}"))
                    else:
                        merged.append((tc_id, req, [(a, sid, h) for a, sid, h in owned]))
                else:
                    for anchor, sid, holder in owned:
                        if holder == req:
                            continue
                        if req in cite.get(sid, set()):
                            cocited.append((tc_id, req, anchor, sid, holder))   # R-CAM19(b)
                        else:
                            hit1.append((tc_id, req, anchor, sid, holder))
                # ── 2 ── proc ≥ 2 步
                steps = [ln for ln in tc["test_procedure"].split("\n") if RE_STEP.match(ln)]
                if len(steps) < 2:
                    hit2.append((tc_id, len(steps)))
                # ── 3a ── Full-Operation 首行 ＋ 步 1 送 RUN（重複）
                pre_first = tc["pre_conditions"].split("\n")[0]
                if RE_FULLOP1.match(pre_first) and steps and RE_RUN_STEP1.search(steps[0]):
                    hit3.append((tc_id, steps[0].strip()))
                # ── 3b ── Standby 首行卻無點火步（矛盾）
                if RE_STANDBY.match(pre_first) and not RE_RUN_STEP1.search(tc["test_procedure"]):
                    hit3b.append((tc_id, pre_first.strip()))
                # ── 7 ── 散文式點火動作
                for ln in tc["test_procedure"].split("\n"):
                    m7 = RE_IGNPROSE.search(ln)
                    if m7:
                        hit7.append((tc_id, m7.group(0), ln.strip()[:80]))
                # ── 5 ── CAN source 行之適用條件（R-CAM3(f)）
                src_lines = [ln for ln in tc["pre_conditions"].split("\n") if RE_CANSRC.match(ln)]
                if src_lines:
                    vmv = doc["vehicle_model"]
                    two_ee = (any(vmv.get(k) == "1" for k in VM_HI)
                              and any(vmv.get(k) == "1" for k in VM_MI))
                    has_send = bool(RE_SENDCAN.search(tc["test_procedure"]))
                    if not (two_ee and has_send):
                        why = []
                        if not two_ee:
                            why.append("未同時勾兩 EE")
                        if not has_send:
                            why.append("無 Send CAN 步")
                        hit5.append((tc_id, "／".join(why), src_lines[0].strip()[:70]))
                # ── 6 ── 設定操作句式（canon §5.8(e)）
                for ln in tc["test_procedure"].split("\n"):
                    if RE_SETSTYLE.search(ln):
                        hit6.append((tc_id, ln.strip()[:80]))
                # ── 9 ── 不可注入之訊號（CEH ＋ ANOMALIES）
                for m9 in RE_SENDSIG.finditer(tc["test_procedure"]):
                    sig = m9.group(1)
                    why = blocked.get(sig)
                    if why is None:
                        # CEH 之訊號名可能被截斷（欄寬），以前綴比對補之
                        why = next((v for k, v in blocked.items()
                                    if sig.startswith(k) or k.startswith(sig)), None)
                    if why is None:
                        continue
                    stem = sig.split(".")[-1][:18]
                    blocked_line = any(stem in ln and ("不可注入" in ln or "不走 CAN" in ln)
                                       for ln in anom.split("\n"))
                    if blocked_line:
                        hit9.append((tc_id, sig, why[:60]))
                # ── 8 ── PENDING 之落點（§8.4.3）
                for fld in ("pre_conditions", "test_procedure", "expected_result"):
                    for ln in tc[fld].split("\n"):
                        if RE_PEND_ANY.search(ln) and not RE_PEND_OK.match(ln):
                            hit8a.append((tc_id, fld, ln.strip()[:80]))
                pre_dr = {m for ln in tc["pre_conditions"].split("\n") if "PENDING:" in ln
                          for m in RE_DRID.findall(ln)}
                er_dr = {m for ln in tc["expected_result"].split("\n") if "PENDING:" in ln
                         for m in RE_DRID.findall(ln)}
                for dr in sorted(pre_dr & er_dr):
                    if not is_ph:
                        hit8b.append((tc_id, dr))
                # ── 10 ── 拆解充分性（WARN，DECISIONS 6-76）
                sid10 = doc.get("source_object_id")
                dmap10 = desc1 if is_b else desc
                ax10 = check10(strip_img(dmap10.get(sid10, "")), tc, sib_n.get(sid10, 1))
                if ax10:
                    warn10.append((tc_id, "／".join(ax10)))
                # ── 4 ── verbatim 保序子序列
                sid = doc.get("source_object_id")
                verb = doc.get("test_item_verbatim", "")
                desc_map = desc1 if is_b else desc
                if is_ph:
                    pass                                   # R-CAM19(d)：來源文件未到
                elif not sid or not verb:
                    no_source.append((tc_id, sid))
                elif sid not in desc_map:
                    no_source.append((tc_id, sid))
                elif not is_subsequence(_txt(verb).split(), desc_map[sid].split()):
                    hit4.append((tc_id, sid, len(_txt(verb).split()),
                                 len(desc_map[sid].split())))

    print(f"Camera 自檢：批次 {[str(d) for d in dirs]}（TC {tcs} 筆）")
    print(f"  1 R-CAM10 錨反查：檢查錨 {checked} 個；無法反查 {len(unresolved)}；常數錨 {len(constant)}；"
          f"共引錨 {len(cocited)}；缺件佔位 {len(placeholder)}；**命中 {len(hit1)}**")
    print(f"  2 proc ≥ 2 步　　：**命中 {len(hit2)}**")
    print(f"  3a 電源態 ↔ 點火：**命中 {len(hit3)}**（Full-Operation 首行 ＋ 步 1 送 RUN）")
    print(f"  3b 電源態 ↔ 點火：**命中 {len(hit3b)}**（Standby 首行 ＋ 無點火步）")
    print(f"  4 verbatim 子序列：無來源可比 {len(no_source)}；**命中 {len(hit4)}**")
    print(f"  5 CAN source 行　：**命中 {len(hit5)}**")
    print(f"  6 設定操作句式　 ：**命中 {len(hit6)}**")
    print(f"  7 點火動作 CAN 式：**命中 {len(hit7)}**")
    print(f"  8a PENDING 落點　：**命中 {len(hit8a)}**（嵌入句中）")
    print(f"  8b PENDING 跨兩欄：**命中 {len(hit8b)}**（提示，須逐列覆核）")
    print(f"  9 不可注入之訊號：**命中 {len(hit9)}**")
    print(f" 10 拆解充分性　　 ：**候選 {len(warn10)}**（**WARN**，不阻上繳；DECISIONS 6-76）")
    for tc_id, anchor in unresolved:
        print(f"  [1 反查失敗] {tc_id}  {anchor}")
    for tc_id, anchor, sid in constant:
        print(f"  [1 常數錨] {tc_id}  {anchor} = {sid}（Category=Information，037 未引）")
    for tc_id, req, items in merged:
        detail = "；".join(f"{sid}→{h}" for _, sid, h in items)
        print(f"  [1 合一錨] {tc_id}（{req}）R-CAM10(b)：{detail}")
    for tc_id, req, anchor, sid, holder in cocited:
        print(f"  [1 共引錨] {tc_id}（{req}）錨 {anchor} = {sid}，承接列 {holder}；R-CAM19(b) 同源")
    for tc_id in placeholder:
        print(f"  [1 缺件佔位] {tc_id}  specification_reference 全為 PENDING: DR-（R-CAM19(d)）")
    for tc_id, req, anchor, sid, holder in hit1:
        print(f"  [1 違反] {tc_id}（{req}）錨 {anchor} = {sid}，承接列為 {holder}")
    for tc_id, n in hit2:
        print(f"  [2 違反] {tc_id}  procedure 只有 {n} 步")
    for tc_id, step in hit3:
        print(f"  [3a 違反] {tc_id}  Full-Operation 首行而步 1 又送 RUN：{step}")
    for tc_id, line in hit3b:
        print(f"  [3b 違反] {tc_id}  Standby 首行而 Procedure 無點火步：{line}")
    for tc_id, sid in no_source:
        print(f"  [4 無來源] {tc_id}  source_object_id={sid}")
    for tc_id, sid, n_v, n_s in hit4:
        print(f"  [4 違反] {tc_id}  verbatim（{n_v} token）非 {sid}（{n_s} token）之保序子序列")
    for tc_id, why, snip in hit5:
        print(f"  [5 違反] {tc_id}  {why}：{snip}")
    for tc_id, snip in hit6:
        print(f"  [6 違反] {tc_id}  {snip}")
    for tc_id, kw, snip in hit7:
        print(f"  [7 違反] {tc_id}  {kw!r}：{snip}")
    for tc_id, fld, snip in hit8a:
        print(f"  [8a 違反] {tc_id}  {fld}：{snip}")
    for tc_id, dr in hit8b:
        print(f"  [8b 提示] {tc_id}  {dr} 同時見於 pre 與 er")
    for tc_id, sig, why in hit9:
        print(f"  [9 違反] {tc_id}  {sig} 不可注入（CEH：{why}）")
    for tc_id, ax in warn10:
        print(f"  [10 WARN] {tc_id}  {ax}")
    sys.exit(1 if (hit1 or unresolved or hit2 or hit3 or hit3b or hit4
                   or no_source or hit5 or hit6 or hit7 or hit8a or hit8b
                   or hit9) else 0)


if __name__ == "__main__":
    main()
