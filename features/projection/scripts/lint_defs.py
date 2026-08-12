#!/usr/bin/env python3
"""Single source of truth for every Projection lint comparison (R-P49).

**Batch scripts import from here. They never re-implement a pattern.**

The rule exists because A-PJ48: A-PJ38 fixed L-PJ5's word boundary and added
`re.I`, but the B6/B7/B8 batch scripts re-implemented the same expression and
dropped `re.I`. Banned verbs are capitalised at step start (`Check whether`),
so every one of them fell through — a false negative that no gate could catch,
because the gate itself was the broken part. **A condition that is correct but
implemented in several places is equivalent to not having fixed it.**

Any change to a comparison condition (word boundary, case, scan range) is made
HERE and nowhere else; after changing it, re-run the whole workbook and update
the baseline recorded below.
"""

import re

# ==========================================================================
# 量測條件（R-P65，2026-08-12）
# ==========================================================================
# R-P49 收編了「比較條件」（regex、詞界、大小寫），但量測條件——欄索引、掃描
# 範圍、計數單位、列身分——仍分散在各腳本，每寫一支就重新假設一次。dry-run v2
# 的四項過程缺陷全部源於此，且分別與 A-PJ19／27／30／37／38 同型：**同一類錯誤
# 在收編比較條件後仍持續發生，證明收編範圍不足。**
#
# 批次腳本與驗證腳本一律 import，不得自行假設任何欄索引、範圍或單位。

# --- 欄索引（表頭 row 2 實測，非推測）--------------------------------------
COL = {
    "seq": 2,              # No.#　**內容為公式 `=ROW()-3`，非字面值**（見 ROW_IDENTITY）
    "polarion_id": 3, "req_id": 4, "tc_id": 5,
    "test_group": 6, "test_set": 7, "test_item": 8,
    "pre": 9,              # Pre-Conditions (I)　可編輯
    "input": 10,
    "proc": 11,            # Test procedure (K)　可編輯
    "er": 12,              # Expected Result (L)　凍結，僅 L-PJ4 窄口例外
    "spec_ref": 13, "tc_ref_id": 14, "priority": 15, "est_time": 16,
    "design_method": 17, "functional_safety": 18,
    "author": 26,          # Test Case Author　**c26，dry-run v2 曾誤設為 c35**
    "test_result": 30,     # Test Result　c30–c34 為 5 個 build 結果欄
    "defect_id": 35, "remarks": 36,
}

EDITABLE_COLS = [COL["pre"], COL["proc"]]
FROZEN_COLS = [c for c in range(1, 37) if c not in EDITABLE_COLS]   # 34 欄

DATA_FIRST, DATA_LAST = 4, 561      # r562 為 SWE1-PROJ-227 之追溯列，單獨處理

# --- 掃描範圍（canon §5a 第四條：須言明掃描哪些欄）--------------------------
SCAN_RISK = [8, 9, 10, 11, 12, 36]   # risk-matrix scans: all text columns
SCAN_EDITABLE = [9, 11]              # defect scans: only the editable columns

# --- 每個 gate 的量測規格（單位 + 範圍），與比較式並列為單一事實來源 -------
# unit: "hit" = 逐次計數（同列命中兩次算兩次）；"row" = 逐列計數
MEASURE = {
    "L-PJ5 banned verbs":        {"unit": "hit", "cols": [9, 11]},
    "L-PJ6 vague":               {"unit": "hit", "cols": [9, 11, 12]},
    "L-PJ9 generic tool":        {"unit": "row", "cols": [9, 11],
                                  "note": "PRE 命中泛稱 且 PROC 無具名工具，兩條件同時成立"},
    # L-PJ10 兩類都以「列」計，且**範圍必須含 ER**：參數類 8 列中 r60／r61 之
    # `<Device Name>` 只出現在 Expected Result，只掃可編輯兩欄會得到 6。
    "L-PJ10 defect placeholders":    {"unit": "row", "cols": [9, 11, 12]},
    "L-PJ10 parameter placeholders": {"unit": "row", "cols": [9, 11, 12]},
    "step cross-references":     {"unit": "row", "cols": [11]},
    "step != ER exceptions":     {"unit": "row", "cols": [11, 12]},
    "forward xrefs":             {"unit": "hit", "cols": [11]},
    "L-PJ1 signal refs":         {"unit": "hit", "cols": SCAN_RISK,
                                  "note": "先移除 $...$ token 內容；豁免見 SIGREF_EXEMPT"},
}

# --- 列身分（R-P66 之修正提案，見 DECISIONS）-------------------------------
# R-P66 定 `No.#` 為列身分。**實測推翻其前提**：c2 的內容是公式 `=ROW()-3`，
# 其值恆等於列位置，**任何列移動後 No.# 都會跟著改，永遠偵測不到重排**。
# 558 列 558 個相異值不是唯一性，是位置標籤。
#
# 可用的列身分是**凍結 34 欄之逐列雜湊**：實測 558 列 558 個相異值，且內容
# 導出，移動時雜湊隨列走。D-2 已在算它，D-3 直接沿用即可。
# --- 凍結欄之授權例外（單一清單，新增窄口只改這裡）---------------------------
# 每一項都是「凍結欄上的合法變更」。R-P84：列身分由此**推導**，不得另行列舉。
FROZEN_EXCEPTIONS = {
    COL["er"]:     {"ruling": "R-P12", "rows": 6,  "form": "純刪除",
                    "log": "data/er_narrow_gate.log.json"},
    COL["remarks"]: {"ruling": "R-P75", "rows": 30, "form": "純附加",
                     "log": "data/remarks_scope_gate.log.json"},
    COL["author"]:  {"ruling": "R-P19/R-P54", "rows": 40, "form": "補值",
                     "log": None},
}

ROW_IDENTITY = "frozen_hash_minus_authorised_exception_cols"
# **推導式，非列舉**（R-P84）：
#     IDENTITY_COLS = 凍結欄 − 全部授權例外欄
# 授權變更的欄位天然不可作為身分的一部分 —— 它一變，身分就跟著變，該列會被
# 讀成「被移動了」。
# A-PJ57（ER 窄口 6 列 FAIL）與 A-PJ66（Remarks 窄口 30 列 FAIL）是同一缺陷的
# 兩次發生：**第一次的修正寫成了「排除 ER 這個特例」，所以第二次還會踩。**
# 改為推導後，任何新增的窄口自動排除，不需要記得回來改這一行。
ROW_IDENTITY_COLS = [c for c in FROZEN_COLS if c not in FROZEN_EXCEPTIONS]
IDENTITY_EXCLUDED = set(FROZEN_EXCEPTIONS)      # 回溯相容
ROW_IDENTITY_REJECTED = {
    "seq (c2)": "公式 =ROW()-3，值恆等於列位置，偵測不到重排",
    "polarion_id (c3)": "558 列僅 162 個相異值",
    "req_id (c4)": "558 列僅 163 個相異值",
    "tc_id (c5)": "555 個相異值：2 組重複 + 3 列空白",
}

# --- 值域（以**資料驗證實際指向者**為準，非以分頁名猜測）-------------------
# `Test Case Design Methods` (Q) 的資料驗證指向 `Reference!$C$4:$C$12`，
# **不是** `下拉選單` 分頁。兩份清單在「組合測試」一項拼法不同
# （Reference: `Pair-wise / N-wise`；下拉選單: `Pairwise / t-wise`），
# 且既有 r372／r376 用的是**下拉選單**那個拼法 —— 該二列違反本簿自身的
# 資料驗證。dry-run v2 的 D-6 驗的是沒有被強制的那一份。
VALIDATION_SOURCE = {
    "priority":      {"col": 15, "sqref": "O4:O562",  "values": ["P0", "P1", "P2", "P3"]},
    "design_method": {"col": 17, "sqref": "Q4:Q152 Q167:Q190 Q219:Q562",
                      "source": "Reference!$C$4:$C$12"},
    "test_result":   {"col": 30, "sqref": "AD4:AH562",
                      "values": ["Pass", "Fail", "Block", "NA", "Pending"]},
}

# --- L-PJ5 banned procedure verbs -----------------------------------------
# Word-boundary (A-PJ38: `inspect` matched `Car Inspector`) AND case-insensitive
# (A-PJ48: verbs are capitalised at step start). Both flags are required.
BANNED_VERBS = ["observe", "check whether", "confirm whether", "see if",
                "watch", "monitor", "inspect"]
RE_BANNED = re.compile(
    r"\b(?:" + "|".join(re.escape(v) for v in BANNED_VERBS) + r")\b", re.I)

# --- L-PJ6 vague language --------------------------------------------------
# Word-boundary (A-PJ18: `a while` matched `content area while`).
RE_VAGUE = re.compile(
    r"\b(?:correctly|normally|properly|successfully|as expected|reasonable|a while)\b",
    re.I)

# --- CAN mention -----------------------------------------------------------
# CASE-SENSITIVE on purpose (A-PJ37: `re.I` matches the English modal "can" and
# inflated HMI Display 0→17, Knob 0→20 over the risk scan range).
RE_CAN = re.compile(r"\bCAN\b")

# --- L-PJ1 signal authority (R-P51) ---------------------------------------
# The two PHDCC27 DBCs are NOT the whole CAN authority for this workbook.
# Cluster Navigation cites TELEMATIC_NAV_INFO.* / TELEMATIC_DISPLAY_INFO.*,
# which are defined in the VF176 cluster-navigation spec that shipped in
# inputs/ at Phase 0 (A-PJ49). L-PJ1's authority is DBC ∪ the VF176 register
# held in data/signal_map.json["vf176_signals"].
#
# The register is maintained BY HAND (R-P51: 5 rows do not justify an
# extraction pipeline). A VF176 signal that is not registered still ABORTs —
# the gate is not bypassed, it acknowledges a second authority.
VF176_REGISTER_PATH = "features/projection/data/signal_map.json"
VF176_REGISTER_KEY = "vf176_signals"


def vf176_signals(register: dict) -> dict:
    """Registered VF176 signals, keyed `MESSAGE.Signal` (drops the _meta row)."""
    return {k: v for k, v in register.get(VF176_REGISTER_KEY, {}).items()
            if not k.startswith("_")}


def resolve_signal(msg: str, sig: str, dbc_fd, dbc_bh, vf176: dict, proxi=None):
    """L-PJ1 resolution, PROXI first (R-P57).

    Resolution order matters because a PROXI configuration word written in its
    full formal shape — `Car_Configuration_15.Vehicle_Line_Configuration` —
    is textually indistinguishable from a CAN `MESSAGE.Signal`. B9 wrote that
    formal shape into two Procedures and L-PJ1 tried to resolve it against the
    DBCs, failing. R-P57 rules that the gate adapts, not the wording: writing
    a less precise form to dodge a regex is the wrong direction.

      1. PROXI parameter table (incl. the `Group.Param` full form)
         → PROXI configuration word; L-PJ2 owns it, L-PJ1 stands down
      2. DBC ∪ VF176 register  → CAN / VF176 signal
      3. neither               → ABORT

    Returns (authority, value_table); authority None means ABORT.
    `proxi` is {parameter_name: value_table_text}; pass None to skip step 1.
    """
    if proxi:
        # Both `Group.Param` and the bare `Param` are legal PROXI spellings.
        if sig in proxi or f"{msg}.{sig}" in proxi or msg in proxi:
            return "PROXI", {}
    for label, (msgs, vals) in (("FD", dbc_fd), ("CAN-B", dbc_bh)):
        if msg in msgs and sig in msgs[msg]:
            return label, vals.get(sig, {})
    entry = vf176.get(f"{msg}.{sig}")
    if entry is not None:
        return "VF176", entry.get("enum") or {}
    return None, None


# --- L-PJ9 generic measurement equipment (R-P42, extended by R-P46) --------
# Incrementable list. Every extension is recorded in DECISIONS §0.12's table
# with: new patterns, hit count before/after, newly hit rows.
GENERIC_TOOL_PATTERNS = ["Test equipment for", "test setup for", "analyzer for",
                         "equipment for measuring", "trace tool", "capture tool",
                         "measurement tool", "test tool", "simulator",
                         "A method to"]   # +2026-08-12 (A-PJ50, second extension)
RE_GENERIC_TOOL = re.compile(
    "|".join(re.escape(p) for p in GENERIC_TOOL_PATTERNS), re.I)
# Second condition: a named tool path in the Procedure exempts the row.
RE_NAMED_TOOL = re.compile(
    r"CarPlay Tests App >|Utilities >|\bATS\b|logcat|PCTS|CAN tool|iPerf", re.I)

# --- L-PJ10 placeholders (R-P43) ------------------------------------------
RE_PLACEHOLDER = re.compile(r"<[^>]{2,40}>")
# Parameter placeholders are maintained as an EXPLICIT LIST, never inferred by
# shape — `<Device Name>` and `<TBD>` are shape-identical and only semantics
# separates them (R-P43).
PLACEHOLDER_WHITELIST = {"<Device Name>", "<Apple CarPlay OR Android Auto>"}

# --- step cross-reference (R-P39) -----------------------------------------
# Cross-references are NOT defects. Only a forward reference whose target is a
# verification step is (the D-1 circular pattern). Backward references such as
# `as recorded in step 1` are the backbone of comparison steps — 30 rows carry
# them workbook-wide and none is to be touched.
RE_STEP_XREF = re.compile(r"\bsteps?\s+\d+", re.I)

# --- tokens ---------------------------------------------------------------
RE_TOKEN = re.compile(r"\$[^$\s]+\$")

# --- L-PJ1 訊號指涉之抽取式（R-P49，2026-08-12 收編）----------------------
# 這條先前散落在三支批次／dry-run 腳本，三次寫法不同，結果也不同：要求點號
# 左側全大寫的版本抽不到 `Car_Configuration_15.Vehicle_Line_Configuration`
# （PROXI 之完整正式形式含小寫），使 R-P57 之 PROXI 優先序永遠不被觸發。
# 抽取式與解析式必須同源，否則解析對了也沒用。
RE_SIGREF = re.compile(r"\b([A-Za-z][A-Za-z0-9_]{3,})\.([A-Za-z_][A-Za-z0-9_]*)\b")


# 放寬左側大小寫（為涵蓋 PROXI 之 `Car_Configuration_15.` 形式）後浮出的
# 非訊號字串。**以列舉排除，不以樣式推斷**（比照 PLACEHOLDER_WHITELIST 之
# R-P43 理由：`tone_sin_1KHz.wav` 與 `BCM_FD_27.DAY_LGT_MD_DISP` 形狀同構，
# 只有語意能分開）。新增項須連同來源列號記於 DECISIONS。
SIGREF_EXEMPT = {
    "bthci_cmd.opcode",      # r481，Wireshark 過濾式，非 CAN 訊號
    "tone_sin_1KHz.wav",     # r521，音檔檔名
    "view.The",              # r539/r540，句號後未空格，非指涉
}


def sigrefs(text, skip_tokens=True):
    """`MESSAGE.Signal` 指涉。

    `skip_tokens=True` 時先移除 `$...$` —— token 內的 `HCP_DISP2.Est_Range_BEV`
    是待解析之 token 而非已解析之訊號指涉，交由 L-PJ3 處理（R-P9：不填訊號）。
    """
    t = str(text or "")
    if skip_tokens:
        t = RE_TOKEN.sub(" ", t)
    return {(m, s) for m, s in RE_SIGREF.findall(t)
            if f"{m}.{s}" not in SIGREF_EXEMPT}

# --- frozen rows ----------------------------------------------------------
FROZEN_ROWS = {376, 377, 378, 379}        # feature.yaml done_region.frozen_rows

# --- baselines (whole workbook, rows 4-561; re-measure after any change) ---
BASELINE = {
    "L-PJ5 banned verbs": 5,      # observe 1 (r150), check whether 3 (r89/98/542), inspect 1 (r230)
    "L-PJ6 vague": 10,            # 9 rows, r520 hits in both PROC and ER
    "L-PJ9 generic tool": 17,     # 7 Performance + 3 VR + 5 HMI Display + 2 Day/Night
                                  # (R-P46 ext#2 "A method to"; R-P56: B2's CAN-step
                                  # rewrite removed the literal "CAN tool", unmasking
                                  # r177/r188 — 17 is correct, 15 was masked)
    "L-PJ10 defect placeholders": 5,   # r36, r111, r124, r149, r225
    "L-PJ10 parameter placeholders": 8,  # r60, r61, r317-r322
    "step cross-references": 30,  # all backward; R-P39 leaves them alone
    "step != ER exceptions": 3,   # r184 (5/4), r355 (5/4), r517 (5/9)
}


def steps(text) -> list:
    """Numbered steps in a Procedure or Expected Result cell."""
    return [l for l in str(text or "").split("\n")
            if re.match(r"^\s*\d+[.)]\s*\S", l)]


def norm(v) -> str:
    return re.sub(r"[ \t]+", " ", str(v or "")).strip()


def placeholder_defects(text) -> list:
    """`<...>` occurrences that are NOT whitelisted parameter placeholders."""
    return [m for m in RE_PLACEHOLDER.findall(text)
            if m not in PLACEHOLDER_WHITELIST]


def forward_xrefs(procedure) -> list:
    """(step_no, referenced_step) pairs where a step points at a LATER step.

    Backward references are legal (R-P39). Only forward ones can create the
    circular order D-1 hit.
    """
    out = []
    for line in steps(procedure):
        cur = int(re.match(r"^\s*(\d+)", line).group(1))
        for m in re.finditer(r"\bsteps?\s+(\d+)", line, re.I):
            if int(m.group(1)) > cur:
                out.append((cur, int(m.group(1))))
    return out


# ==========================================================================
# spec_reference 錨點解析（R-P73，2026-08-12）
# ==========================================================================
# D-6 原本只做格式比對，v2 報告的「7/7 通過」僅證明格式正確。R-P73 改為真解析。
#
# **抽取式比解析式更容易錯**（第三次同型：RE_SIGREF、Addendum 版本標記、本條）。
# 兩個實測到的陷阱：
#   1. `..._CarPlay_Addendum_R10` 的 `R10` 會被當成章節號 10
#   2. 同一格的散文註記含大量數字 —— `Table 18-11`、`line 845`、
#      `main display minimum resolution 800 x 480` 全都不是章節錨點
# 故 Addendum 的章節錨點**限定為 `§` 前綴**，其餘一律視為散文，標「未解析」。
SPEC_ANCHOR = {
    "CFTS085": re.compile(r"^CFTS085-(\d{7})$"),
    "SYSAD_NRL": re.compile(r"NRL-(\d+)"),
    "HUIG": re.compile(r"^R\d{2}-\d{3}"),
    "ADDENDUM_SECTION": re.compile(r"§\s*(\d+(?:\.\d+)*)"),
}


def _norm_section(s):
    """`2.0` 與 `2` 是同一節的兩種書寫。"""
    return re.sub(r"(\.0)+$", "", s) or "0"


def resolve_spec_anchor(anchor, sections):
    """回傳 (kind, resolved, detail)。resolved=None 表示無可解析之錨點，僅格式比對。

    `sections` = {"cfts085": {...}, "sysad": {...}, "huig": {...},
                  "addendum_ids": {...}}
    """
    a = str(anchor or "").strip()
    if not a:
        return None
    m = SPEC_ANCHOR["CFTS085"].match(a)
    if m:
        v = sections["cfts085"].get(m.group(1))
        return ("CFTS085", bool(v), f"§{v[0]}" if v else "clause 不存在")
    if "NRL-" in a:
        ids = SPEC_ANCHOR["SYSAD_NRL"].findall(a)
        miss = [i for i in ids if i not in sections["sysad"]]
        return ("SYSAD", not miss, "缺 " + ",".join(miss) if miss else f"{len(ids)} 個全部命中")
    if SPEC_ANCHOR["HUIG"].match(a):
        return ("HUIG", a in sections["huig"], "命中" if a in sections["huig"] else "不存在")
    # **限定 CarPlay Addendum**。只比對 `Addendum` 會把
    # `Apple MFi Accessory Interface Specification §15 Addendum: Location
    # Information` 也吃進來 —— 那是另一份文件（MFi AIS），本 repo 無其 sections
    # 檔，應歸「其他／未解析」而非判 FAIL。
    if "CarPlay_Addendum" in a or "CarPlay Addendum" in a:
        secs = [_norm_section(s) for s in SPEC_ANCHOR["ADDENDUM_SECTION"].findall(a)]
        if not secs:
            return ("CarPlayAddendum", None, "文件層級引用或散文註記，無 § 章節錨點")
        miss = [s for s in secs if s not in sections["addendum_ids"]]
        return ("CarPlayAddendum", not miss,
                "缺 " + ",".join(miss) if miss else f"命中 §{','.join(secs)}")
    return ("其他", None, "無對應 sections 檔")
