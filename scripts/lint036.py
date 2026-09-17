#!/usr/bin/env python3
"""FM-WI-FSM-036 工作簿靜態檢查（報告模式）。

檢查 A–N 之定義見 docs/fw036/handoff/00_lint_spec.md。
本工具唯讀開啟 xlsx，絕不寫回任何 xlsx。

`--profile <feature>` （21 包）：指定時 P 改採 **R-1 v3** 判準
（`$MESSAGE.Signal$` ＋ DBC `VAL_` 標籤），並另跑
Q（不可見字元，R-10(a)）／R（Pre-Condition 版面，R-9(a)）／
T（PENDING 說明語言，R-14）。**未指定時行為與 21 包之前完全一致** ——
既有八本之報告基線因而不動（迴歸基準見上繳 22）。

gate 政策（S3）：`--gate` 旗標保留但**尚不啟用**。啟用時機為尾批
（全數回修完成後）；現階段啟用將使所有既有交付本 exit 1，阻斷正常
作業。裁決條文見 docs/fw036/RULINGS_LEDGER.md。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field as dc_field
from datetime import date
from pathlib import Path

import openpyxl

# --- 欄位鍵與標頭關鍵字（startswith 匹配） ---------------------------------

FIELD_HEADERS: dict[str, str] = {
    "test_set": "Test Set",
    "test_item": "Test Item",
    "pre": "Pre-Conditions",
    "input": "Input Test Data",
    "proc": "Test procedure",
    "er": "Expected Result",
    "spec": "Specification Reference",
    "author": "Test Case Author",
}

# 輔助欄（非檢查對象，供報告定位與 I-sibling 分組用）
REQ_ID_HEADER = "Requirement or Design ID"
TC_ID_FIRSTLINE = "Test Case ID"

# `Vehicle Model 車型` 七子欄（母本第 9 列 T–Z 實測，R-G48）。
# 比對取標頭之**首行**去空白後之字串 —— 母本各欄為 `HDCC27\nAtl-Hi\n` 之形，
# 第二行之 EE（Atl-Hi／Atl-Mi）不入比對鍵，避免 ext 變體換行位置不同即失配。
VEHICLE_MODEL_HEADERS: tuple[str, ...] = (
    "HDCC27", "DT27", "VF(ProMaster)637", "Commander (598)",
    "Regengade (5210)", "Toro(2261)", "Fastack (376)",
)
# R-CAM2(b)：兩車型已不支援，Camera 兩本一律 `0`。
# **R-G74（Pei 2026-09-17）由 Camera 升為全域**：FW036 全 feature 之此二欄一律 `0`。
VEHICLE_MODEL_ZERO: frozenset[str] = frozenset(
    {"Commander (598)", "Regengade (5210)"})
VEHICLE_MODEL_ALLOWED: frozenset[str] = frozenset({"0", "1"})

# --- Diagnostics profile 專屬常數（R-DIAG5(amend)／R-DIAG1(a)／R-DIAG3(amend)／R-DIAG6）---
# 白名單之**定義**為 `features/diagnostics/data/layer3_assign.tsv` 之 DID 集合
# （下放包 CDD-01_A T4 括號內書「27 種」，該數為 CDD-01 3-5 之 037 token 種數，非本集合；
#  依定義實測為 36 種 —— 見上繳包 §4）。白名單外之 `$`+4hex 即非本 feature 之 DID。
DIAG_DID_WHITELIST: frozenset[str] = frozenset({
    "$0307", "$0309", "$030A", "$0312", "$031B", "$1801", "$180C", "$1820",
    "$1821", "$280C", "$2812", "$283F", "$2840", "$2841", "$2842", "$2843",
    "$2844", "$2845", "$2846", "$2847", "$2848", "$2870", "$5000", "$5001",
    "$5002", "$5003", "$5004", "$5005", "$5006", "$5008", "$5009", "$500A",
    "$500B", "$500C", "$500D", "$5100",
})
# `$`+4hex，且**不以 `$` 結尾** —— `$MESSAGE.Signal$` 式維持檢查 P 原判（R-DIAG5(a)）
RE_DIAG_DID = re.compile(r"\$[0-9A-Fa-f]{4}(?!\$)(?![0-9A-Za-z_.])")
# R-DIAG5(amend)(d) 五碼之 ISO 名稱；U-DIAG 之 label 值域 = 本集合 ∪ CFTS004 原字
DIAG_NRC_LABELS: frozenset[str] = frozenset({
    "serviceNotSupported", "subFunctionNotSupported",
    "incorrectMessageLengthOrInvalidFormat", "conditionsNotCorrect",
    "requestOutOfRange",
    # CFTS004 原字（up CDD-01 §7-1：帶值之 5 列所用者）
    "Conditions Not Correct", "Request Out of Range",
    # 037 定型句原字（R-DIAG5(amend)(d) 之觸發語，ER 引 037 逐字時用）
    "Service Not Supported",
})
# UDS 位元組串之起點：`Send UDS request`／`positive response`／`negative response`。
# **不在正則內貪婪吃完整串** —— 起點之後逐 token 走，遇第一個「非位元組候選」即止，
# 否則 `… 22 28 3F via diagnostic tool` 之 `via`／`diag` 會被當成壞 byte 報出
# （T4 自測實測之假陽性 3 例）。
RE_UDS_START = re.compile(
    r"(?:Send\s+UDS\s+request|positive\s+response|negative\s+response)\s+", re.I)
# 位元組候選：純 hex 1–4 位，或帶 `0x` 前綴者（後者本身即違規，須被收進來才報得出）
RE_UDS_CAND = re.compile(r"^(?:0[xX])?[0-9A-Fa-f]{1,4}$")
RE_UDS_BYTE_OK = re.compile(r"^[0-9A-F]{2}$")
# `7F <SID> <NRC> (<label>)`
RE_DIAG_7F = re.compile(r"\b7F\s+(?P<sid>\S+)\s+(?P<nrc>\S+)(?P<tail>\s*\([^)]*\))?")
# R-DIAG1(a)＋R-DIAG2：Requirement ID 欄單值
RE_DIAG_REQ_ID = re.compile(r"^SWE1-Diagnostics-\d{3}(?:-00[12])?$")
# R-DIAG2：037 之重號 ID。此二號**必帶** `-001`／`-002` 尾綴，裸號即違規
# （T4 自測實測之假陰性 1 例：`(?:-00[12])?` 之 `?` 使裸號也通過）。
DIAG_DUP_REQ_IDS: frozenset[str] = frozenset({"SWE1-Diagnostics-340"})
# R-DIAG7(a)／R-DIAG3(amend)／R-DIAG6／R-DIAG5(amend)(d)(e) 之 Remarks 定型句
# 比對自串首起，不錨定串尾 —— 多句以 `; ` 接合時逐句消耗（見 check_diag_remarks）。
# `037 VM blank; …` 一式自身含 `; `，故其必須排在其他式之前，先長後短。
RE_DIAG_REMARKS_OK = (
    re.compile(r"^037 VM blank; procedure derived from Description \+ CFTS004"),
    re.compile(r"^Harman Scope: (?:Need Rework|Need Clarification|Accepted)"),
    re.compile(r"^CFTS004 Category: Out of Scope"),
    re.compile(r"^NRC per ISO 14229-1 \(037 unspecified\)"),
    re.compile(r"^SID per 037 SWE1-Diagnostics-\d{3}(?:-00[12])?"),
)
DIAG_AUTHOR_FIELDS = ("test_item", "pre", "proc", "er")
# R-DIAG18（IN §4.4 之本 feature 實作）：Pre-Condition 只述狀態。
# 需 do／check／record 者不是 Pre-Condition —— `*_initial` 只得於 Procedure 宣告並於 ER 使用。
# R-DIAG18 所列之動作詞取**詞幹**比對 —— 條文書 `press`，而實文為 `is pressed`；
# 僅以 `\bpress\b` 比對會漏（自測之假陰性 1 例）。
RE_DIAG_PC_ACTION = re.compile(
    r"\b(?:record(?:ed|s)?|read|measure(?:d|s)?|send|sent|press(?:ed|es)?)\b"
    r"|by a diagnostic command|has been sent|was sent", re.I)


# 否定式之靜止態不是動作 —— `No push button … is pressed` 描述初始狀態，
# 無須 do／check／record 即成立（R-DIAG18 之立意為「需執行才成立者不是 Pre-Condition」）。
# 詞幹比對若不設此例外，會攔下合法前提（CDD-06 自測之假陽性 2 例）。
RE_DIAG_PC_NEGATED = re.compile(r"\bno\b[^.]*\b(?:pressed|sent|recorded|read)\b", re.I)


def check_diag_pc(fields: dict, row_no: int, tc_id: str) -> list[Violation]:
    """PC-DIAG —— Pre-Condition 之機械守門（R-DIAG18）。"""
    out: list[Violation] = []
    for line in fields.get("pre", "").split("\n"):
        if RE_DIAG_PC_NEGATED.search(line):
            continue
        m = RE_DIAG_PC_ACTION.search(line)
        if m:
            out.append(Violation(
                "PC-DIAG", row_no, tc_id, "pre",
                "R-DIAG18：Pre-Condition 只述狀態，不得含動作詞；"
                "`*_initial` 只得於 Procedure 宣告", m.group(0)))
    return out

# --- R-DIAG13／R-DIAG14 之母體（CDD-04 追補 A §一：**依母節反查，不依位元組串**）-------
# 依位元組串會漏 —— pilot `-006` 之觸發步驟曾整行為 `PENDING`，無 `2F` 串而仍屬 0x2F 之 TC。
# 兩表自 `features/diagnostics/data/layer3_assign.tsv` 導出，以號段書寫（逐一列出 114 個號無益於閱讀）。
def _diag_ids(ranges: tuple) -> frozenset[str]:
    out = set()
    for lo, hi in ranges:
        for n in range(lo, hi + 1):
            out.add(f"SWE1-Diagnostics-{n:03d}")
    return frozenset(out)


# 母節 = I/O Control DIDs 之 037 列（114 列）
DIAG_IO_ROWS = _diag_ids(((7, 12), (31, 43), (58, 147), (336, 340)))
# `$1820`／`$1821` 之 037 列（7 列）
DIAG_KEY_ROWS = _diag_ids(((54, 55), (344, 345), (386, 388)))
# R-DIAG2 之三段式號：`-340-001` 屬 I/O（`$500D`）、`-340-002` 屬 R/W（`$280C`）
DIAG_IO_SUFFIXED = frozenset({"SWE1-Diagnostics-340-001"})
# R-DIAG13(amend)（Pei 2026-09-17）：unsupported 型送的是**不支援之 SID**，不發 0x2F，
# 不在 SEC-DIAG 母體。33 個 I/O ∩ unsupported 之 037 列（號段不連續，逐一列出）。
DIAG_IO_UNSUPPORTED: frozenset[str] = frozenset({
    "SWE1-Diagnostics-009", "SWE1-Diagnostics-033", "SWE1-Diagnostics-037", "SWE1-Diagnostics-040", "SWE1-Diagnostics-043", "SWE1-Diagnostics-060", "SWE1-Diagnostics-063", "SWE1-Diagnostics-072", "SWE1-Diagnostics-075", "SWE1-Diagnostics-078", "SWE1-Diagnostics-081", "SWE1-Diagnostics-084", "SWE1-Diagnostics-087", "SWE1-Diagnostics-090", "SWE1-Diagnostics-093", "SWE1-Diagnostics-096", "SWE1-Diagnostics-099", "SWE1-Diagnostics-102", "SWE1-Diagnostics-105", "SWE1-Diagnostics-108", "SWE1-Diagnostics-111", "SWE1-Diagnostics-114", "SWE1-Diagnostics-117", "SWE1-Diagnostics-120", "SWE1-Diagnostics-123", "SWE1-Diagnostics-126", "SWE1-Diagnostics-129", "SWE1-Diagnostics-132", "SWE1-Diagnostics-135", "SWE1-Diagnostics-138", "SWE1-Diagnostics-141", "SWE1-Diagnostics-144", "SWE1-Diagnostics-147",
})
DIAG_SEC_PC = "Security access 0x27 has been granted"
RE_DIAG_FORBIDDEN_KEY = re.compile(r'"(Power|Dark)"')


def check_diag_security(req_id: str, fields: dict, row_no: int, tc_id: str) -> list[Violation]:
    """SEC-DIAG —— I/O Control（0x2F）之 TC 須含 security Pre-Condition（R-DIAG13）。"""
    rid = req_id.replace("\xa0", " ").strip()
    if rid not in DIAG_IO_ROWS and rid not in DIAG_IO_SUFFIXED:
        return []
    if rid in DIAG_IO_UNSUPPORTED:       # R-DIAG13(amend)
        return []
    if DIAG_SEC_PC in fields.get("pre", ""):
        return []
    return [Violation(
        "SEC-DIAG", row_no, tc_id, "pre",
        f"R-DIAG13：SID 0x2F 之 TC 須含 Pre-Condition `{DIAG_SEC_PC}`", rid)]


def check_diag_key(req_id: str, fields: dict, row_no: int, tc_id: str) -> list[Violation]:
    """KEY-DIAG —— 按鍵狀態 DID 之觸發鍵不得為 Power／Dark（R-DIAG14）。"""
    rid = req_id.replace("\xa0", " ").strip()
    if rid not in DIAG_KEY_ROWS:
        return []
    out: list[Violation] = []
    for key in ("proc", "er"):
        for m in RE_DIAG_FORBIDDEN_KEY.finditer(fields.get(key, "")):
            out.append(Violation(
                "KEY-DIAG", row_no, tc_id, key,
                "R-DIAG14：觸發鍵不得選會改變 HU 電源或畫面狀態之鍵；優先選 Up／Down／Select",
                m.group(0)))
    return out



HEADER_ANCHOR = "Specification Reference"
HEADER_SCAN_ROWS = 15
TC_SHEET_PREFIX = "Test Case Specification"

# --- 各檢查所涵蓋之欄位 ------------------------------------------------------

# K「六欄」（00b 修訂 3 明確化）：不含 spec、author、remarks
K_FIELDS = ("test_item", "test_set", "pre", "input", "proc", "er")
M_FIELDS = ("pre", "proc", "er", "spec")
N_FIELDS = ("pre", "input", "proc", "er")
# P（R-1／R-6）：僅施於作者生成之內容 —— 四欄 ＋ test_item 之括號下半。
# test_item 上半為需求原句 verbatim，其訊號記法保留來源原文，不套 R-1。
P_FIELDS = ("pre", "input", "proc", "er")
J_NUMBERED_FIELDS = ("pre", "proc", "er")
# Q（R-10(a)）：不可見字元不構成內容，全欄位適用（含 verbatim 上半與 spec）
Q_FIELDS = ("test_item", "test_set", "pre", "input", "proc", "er", "spec")
# T（R-14）：`PENDING:` 佔位之說明須為英文
T_FIELDS = ("pre", "input", "proc", "er")

# --- 正則 --------------------------------------------------------------------

NUMBERED_LINE = re.compile(r"^\s*\d+[.)]")          # 全域編號行定義（E 等沿用，勿動）
NUMBER_PREFIX = re.compile(r"^\s*\d+[.)]\s*")
# N 檢查自身之行定義：另納 a./b./c. 縮排子步驟（canon §6.1 子層為實質測試步驟）
# 限定僅供 n_exempt() 使用，不得外溢至 NUMBERED_LINE 之使用點
N_STEP_LINE = re.compile(r"^\s*(\d+|[a-z])[.)]")

RE_A = re.compile(
    r"(^\s*\d+[.)]\s*(Observe|Verify|See if|Watch|Monitor|Inspect)\b)"
    r"|\b(observe whether|check whether|confirm whether|see if)\b",
    re.I | re.M,
)
RE_B = re.compile(r"\b(shall|should|will)\b")
RE_C = re.compile(r"\b(properly|successfully|within reasonable time)\b", re.I)
RE_D_POWERED = re.compile(r"\b(HU|system|unit) is powered on\b", re.I)
RE_D_VERB = re.compile(
    r"^(Insert|Connect|Press|Open|Enable|Disable|Launch|Select|Tap|Trigger|Perform|Set)\b",
    re.I,
)
RE_F = re.compile(r"\[[A-Za-z][^\]]{0,30}\]")
# `--profile` 專屬例外（下放包 43 §二 #1）：緊接於 `$<name>$ =` 之後之方括號
# **不是未填佔位，是車輛屬性之值**（037 逐字之訊號記法 `$FOTA_Status$ = [值]`）。
# 未指定 `--profile` 時本例外不生效 —— 既有八本之基線因而完全不動。
RE_F_SIGNAL_VALUE = re.compile(r"\$[A-Za-z][A-Za-z0-9_.]*\$\s*=\s*(\[[^\]]{0,60}\])")
RE_H = re.compile(r"\b(as expected|works? normally|normal(ly)? operation)\b", re.I)
# `--profile` 專屬（下放包 47 §二 #6）：**關係模糊詞** ——
# 其與上式之**程度／狀態模糊詞**不同族，現行詞表**整族未收**。
# 程度模糊詞（`properly`）一望即知其模糊；**關係模糊詞看起來很具體** ——
# 它指名了二個被比較的量，只是沒說「相符」到什麼程度算相符。
RE_H_RELATION = re.compile(
    r"\b(corresponds? to|matches?|is consistent with|in line with|aligns? with)\b", re.I)
RE_PAREN_LINE = re.compile(r"^\(.+\)$")
RE_PAREN_TAIL = re.compile(r"\([^)]{3,}\)\s*$")
RE_CJK = re.compile(r"[一-鿿]")
RE_TOKEN = re.compile(r"[A-Za-z0-9$_.'\"-]+")
RE_TRAILING_PERIOD = re.compile(r"[.。]$")
# CAN 訊號 token `MESSAGE.Signal`（message 段全大寫）。
# 內部訊號 `TLM_Status.Info`／`Phone_Call.Info` 之 message 段含小寫，不命中。
RE_CAN_TOKEN = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\b")
# R-1 v1 之三件組，已撤銷；殘留即違規。
RE_P_TRIPLET = re.compile(
    r"\b[A-Za-z0-9_]+\s+in\s+[A-Z][A-Z0-9_]{2,}\s+on\s+[A-Za-z0-9-]+\b")
# 賦值之偵測：CAN token 後接 `=`／`from`／`to`（不論是否合式）。
RE_P_ASSIGNMENT = re.compile(
    r"\b[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\s*(?:=|from\b|to\b)")
# R-1 v2(a)(b) 共通之賦值形：`<MSG>.<Sig> = <raw> (<label>)`。
# 括號標籤即 R-7 之 DBC `VAL_` 語意標籤。收尾語不設限（見 check_signal_line）。
RE_P_VALUE_FORM = re.compile(
    r"[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\s*=\s*[^\s(]+\s*\([^)]+\)")
# R-G70(h)（GC-12 審閱 §一）：v3 記法殘留 —— `$<MSG>.<Sig>$` 之 `$` 包覆式，
# **不論其後有無 `= raw (label)`**，一律 FAIL。
# 其必須獨立於 `RE_P_ASSIGNMENT`：後者要求訊號名與 `=` 相鄰，而 `$` 隔在中間，
# 故 v3 殘留行在 v3 分支移除後**不被任何式命中**，`check_signal_line` 於
# `if not assignments: return out` 提早返回，P 恆 0（GC-12 上繳 1 節之正控）。
RE_P_V3_DOLLAR = re.compile(
    r"\$[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\$")
# PROXI 行（R-G70 v4.1，Pei 裁定 2026-09-05：**SWC 式為標準**）
# 標準：`PROXI <Param> = <值>`（不加 `$`）。舊式：`PROXI $<Param>$ is set to "<值>"`（VF230）。
# 舊式**不 FAIL**，記於 Y（WARN 只報不改）；兩式皆不中之 PROXI 行記 P。
# `(?!=)`：`==` 非標準式 —— 原式會把 `PROXI Foo == "x"` 之首個 `=` 讀成賦值
# 而判為合規（GC-14 實測；GC-13 審閱所指定之正控樣本正踩此鬆脫）。
RE_P_PROXI = re.compile(r"\bPROXI\s+([A-Za-z][A-Za-z0-9_]*)\s*=(?!=)")
RE_P_PROXI_LEGACY = re.compile(r"\bPROXI\s+\$[^$]+\$\s+is\s+set\s+to\b")
RE_P_PROXI_ANY = re.compile(r"\bPROXI\b")
# R-G70(i)（GC-13 審閱 一 之 1）：fallback 只在該行為**賦值形態**時報。
# 純散文提及（`Hold for the PROXI Switch_Off_Time value`／
# `The Rear_View_Camera PROXI parameter reads "Present"`）不是 PROXI 行，
# 對其報 P（FAIL 類）會擋出貨閘 —— pm_73 之 19 處誤報即此（GC-13 上繳 3 節）。
#
# ⚠ 判準為「**緊接 `PROXI` 之參數後**有 `=`／`==`／`is set to`」，
# **不是「同行有」** —— 審閱原文之「同行」過寬：
# `STATUS_TELEMATIC.PowerSts_Telematic = 1 (Standby) is sent after the PROXI
#  Switch_Off_Time value has elapsed` 之 `=` 屬 CAN 斷言而非 PROXI，
# 以「同行」為準會留下 5 處誤報（GC-14 實測；見上繳 1-3 節）。
RE_P_PROXI_ASSIGN_SHAPE = re.compile(
    r"\bPROXI\s+\$?[A-Za-z][A-Za-z0-9_]*\$?\s*(?:==|=|is\s+set\s+to\b)")
# --- profile 專屬（未指定 --profile 時全部不啟用）-----------------------------
# R-1 v3 之判準（`RE_P3_DOLLAR_ASSIGN`／`RE_P3_BARE_ASSIGN`／`RE_P3_SEND_CAN`／
# `RE_P3_PROXI_DOLLAR`）**已隨 v3 撤銷而移除**（R-G70，GC-08）。
# 以下二式**不屬 v3 記法**，故不隨之移除 —— 見其自身之註解。
# 下放包 43 §二 #1：無點之車輛屬性記法 `$<Name>$ = [值]`（037 逐字）。
# **P 之各式皆要求訊號名含一個點，故本形態原本不被任何式命中** ——
# `P=0` 是沉默不是核可（上繳包 37 §2.2）。本式使其**被檢查**：
# `$` 包覆之名、`=`、方括號包覆之值，三者齊備即通過；缺一即報。
RE_P3_PROP_OK = re.compile(r"\$[A-Za-z][A-Za-z0-9_]*\$\s*=\s*\[[^\]]{1,60}\]")
# 候選：`$` 包覆之無點名後接 `=`，其值形態不拘 —— 用以偵測「有名有等號而值不合式」
RE_P3_PROP_ANY = re.compile(r"\$([A-Za-z][A-Za-z0-9_]*)\$\s*=\s*(?P<val>\S+)")
# Q（R-10(a)）
RE_Q_TRAILING_WS = re.compile(r"[ \t]+$")
# V 行首空白（IN §11）。**行尾空白不在本檢查**——其已由 Q 覆蓋，
# 兩處同時計數會使量化矩陣之命中數雙倍膨脹（G-D：數字須可解釋）。
RE_V_LEADING_WS = re.compile(r"^[ \t]+")
RE_V_BLANK_WS = re.compile(r"^\s+$")
# IN §11 之唯二例外：§6.1 子層記法（`a./b./c.` 縮排 3 格、`-` 子彈 6 格）
# 與 §5.4 之 `$` 命令行（縮排 3 格）。
RE_V_EXEMPT = re.compile(r"^(?: {3}(?:[a-z]\.\s|\$ )| {6}- )")
# R（R-9(a)）：多條件並列之謂詞計數
RE_R_PREDICATE = re.compile(r"\b(is|are|was|were|reads?|holds?|has|have)\b")
R_TOOL_PHRASE = "tool is available on HU"
# T（R-14）
RE_T_PENDING = re.compile(r"PENDING:\s*(?P<dr>[A-Za-z0-9-]+)?(?P<desc>.*)$")

RE_CAMEL = re.compile(r"^[a-z][a-zA-Z0-9_]*[A-Z]")
RE_DOTCALL = re.compile(r"^[a-z][a-z0-9_]*\.[a-zA-Z(]")

J_WHITELIST = {
    "adb", "tmpfs", "iPod", "iOS", "iPhone", "dd", "cat", "mount",
    "btsnoop", "hciconfig", "hcitool", "logcat", "sdptool",
}

DEFAULT_LENGTH_LIMIT = 50

CHECK_TITLES = {
    "A": "禁用動詞 (proc)",
    "B": "ER 情態詞 (er)",
    "C": "hedge (test_item 括號下半)",
    "D": "PC 違規 (pre)",
    "E": "proc/er 編號行數不對齊",
    "F": "方括號佔位 (proc)",
    "G": "Test Set 空值",
    "H": "ER 模糊語 (er)",
    "I": "test_item 括號下半缺失",
    "I-sibling": "同 Requirement ID 括號行逐字重複",
    "J": "行首大寫",
    "K": "CJK 字元",
    "L": f"test_item 上半過長 (>{DEFAULT_LENGTH_LIMIT} tokens)",
    "M": "空欄三態",
    "N": "行尾多餘句號",
    "P": "訊號寫法不合 R-1 v2",
    "Q": "不可見字元（NBSP／全形空格／行尾空白）",
    "R": "Pre-Condition 版面（未編號行／多條件並列）",
    "T": "PENDING 說明非英文",
    "U": "PENDING 佔位（四欄全掃，含 ER 側）",
    "V": "行首空白（IN §11）",
    "I-cross": "跨 req_id：觀測窗相同且違例類有交集（R-SU34 v3）",
    "W": "ER 含比較關係而 test_item 上半無數值（下放包 47 §二 #6）",
    "X": "導航路徑無固定入口（§5.8／R-G71）",
    "Y": "PROXI 舊式（R-G70 v4.1：`$Param$ is set to` 為 VF230 同義舊式）",
    "Z": "Vehicle Model 七欄 1／0（R-CAM2，Camera profile 專屬）",
    "SC": "步驟無執行通道／ER 無觀察手段（R-SEC7，Security profile 專屬）",
    "P-DIAG": "`$XXXX` 非本 feature 之 DID 白名單（R-DIAG5(a)，Diagnostics profile 專屬）",
    "U-DIAG": "UDS 位元組串格式／`7F` 後缺 `(<label>)`（R-DIAG5(b)，Diagnostics profile 專屬）",
    "R1-DIAG": "Requirement ID 欄非單一 SWE1 ID（R-DIAG1(a)，Diagnostics profile 專屬）",
    "RM-DIAG": "Remarks 非 R-DIAG 所定之五種定型句（Diagnostics profile 專屬）",
    "SEC-DIAG": "I/O Control（0x2F）之 TC 缺 security Pre-Condition（R-DIAG13，Diagnostics profile 專屬）",
    "KEY-DIAG": "按鍵狀態 DID 之觸發鍵為 Power／Dark（R-DIAG14，Diagnostics profile 專屬）",
    "PC-DIAG": "Pre-Condition 含動作詞（R-DIAG18，Diagnostics profile 專屬）",
    "SS": "Remarks 無 `source:` 標記／資產佔位之 `X-` 代號未載於 Remarks"
          "（R-SEC4(a)／R-SEC21(e)，Security profile 專屬）",
}
# `--profile` 啟用時 P 改以 R-1 v3 判準，標題隨之替換
# R-G70：P 於 profile 與非 profile 下判準相同，故無標題覆寫。
CHECK_TITLE_PROFILE: dict[str, str] = {}

# 校準狀態（00c 最終版）：M、J 經全語料分佈補校，改標已校準
CHECK_STATUS = {
    "A": "已校準", "B": "已校準", "C": "已校準（R-6b 範圍：Media 錨值 1→0）",
    "D": "已校準",
    "E": "已校準", "F": "已校準", "G": "已校準（詞彙表外值待接入）",
    "H": "已校準", "I": "已校準", "I-sibling": "未校準（M15）",
    "J": "已校準（行計口徑）", "K": "已校準（分級待 R-5）",
    "L": "已校準（閾值待 R-3）", "M": "已校準", "N": "已校準",
    "P": "已校準（SWC 0708：195 —— proc 11／er 184，見上繳 09）",
    "Q": "未校準（R-10(a)，21 包新增）",
    "R": "未校準（R-9(a)，21 包新增）",
    "T": "未校準（R-14，21 包新增）",
    "U": "計數用（A-PM16：ER 側原不受任何檢查覆蓋）",
    "V": "未校準（IN §11，27 包新增）",
    "I-cross": "警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL",
    "W": "**待人裁非 FAIL** —— 輸出分二段（下放包 48 §二）：(a) 已裁段只報列數、(b) 新命中段逐列陳述",
    "X": "未校準（§5.8／R-G71，GC-07 新增）—— **WARN 只報不改**",
    "Y": "未校準（R-G70 v4.1，GC-10 新增）—— **WARN 只報不改**；既有交付本不回修（R-TM13），回修依 R-G72",
    "Z": "未校準（R-CAM2，CAM-02 新增）—— **feature 專屬**，僅 `--profile camera` 啟用；"
         "既有八本無此七欄，未啟用即不檢查（`Z=0` 在未啟用時是沉默，不是核可）",
    "P-DIAG": "未校準（R-DIAG5(a)，CDD-01_A 新增）—— **feature 專屬**，僅 `--profile diagnostics` 啟用。",
    "U-DIAG": "未校準（R-DIAG5(b)，CDD-01_A 新增）—— **feature 專屬**。",
    "R1-DIAG": "未校準（R-DIAG1(a)，CDD-01_A 新增）—— **feature 專屬**。",
    "RM-DIAG": "未校準（R-DIAG3(amend)／R-DIAG6／R-DIAG7(a)，CDD-01_A 新增）—— **feature 專屬**。",
    "SEC-DIAG": "未校準（R-DIAG13，CDD-04 新增；R-DIAG13(amend) 排除 unsupported 型）—— **feature 專屬**；母體依母節反查（追補 A §一）。",
    "KEY-DIAG": "未校準（R-DIAG14，CDD-04 新增）—— **feature 專屬**。",
    "PC-DIAG": "未校準（R-DIAG18，CDD-06 新增）—— **feature 專屬**；IN §4.4 之機械守門。",
    "SC": "未校準（R-SEC7，SEC-02 新增）—— **feature 專屬**，僅 `--profile security` 啟用。"
          "對既有語料之假陽性率 Procedure 98.4%／ER 74.9%（九本 1,700 列實測，SEC-01 上繳包 8-2），"
          "**故絕不可入 PROFILE_CHECKS**；對 Security 自身之假陽性率待 Pilot",
    "SS": "未校準（R-SEC4(a)，SEC-02 新增；R-SEC21(e) 判項 SEC-08 增列）—— **feature 專屬**。"
          "判準面之偏差：R-SEC4(a) 原文為「於 reasoning 註明來源」，而 reasoning 在生成側 JSON、不在工作簿；"
          "本檢查改以 **Remarks 欄**之 `source:` 標記為判準，待 Pei 覆核（SEC-02 上繳包自報）。"
          "R-SEC14(c)：`<…>` 佔位不報",
}
CHECK_STATUS_PROFILE: dict[str, str] = {}
CHECK_ORDER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "I-sibling",
               "J", "K", "L", "M", "N", "P"]
# profile 專屬檢查：僅於 `--profile <feature>` 指定時啟用。
# 未指定時 CHECK_ORDER 不變 —— 既有八本之報告基線因而完全不動。
PROFILE_CHECKS = ["Q", "R", "T", "U", "V", "I-cross", "W", "X", "Y"]
# **feature 專屬**檢查：只在指名之 profile 下啟用，不隨任意 `--profile` 值生效。
# 立此結構之由（CAM-02 §2 任務 3）：`Z` 檢查之七欄為 Camera 兩本所獨有，
# 既有八本之工作簿無此七欄；若併入 PROFILE_CHECKS，任何 feature 之 profile 執行
# 都會整本 FAIL。判準與粒度照 R-CAM2，啟用面縮到 feature。
# R-SEC13(a)：`SC`／`SS` 只入 `FEATURE_CHECKS["security"]`，不入 `PROFILE_CHECKS`。
# R-SEC13(b)：單字母 `C` 已為既有檢查（hedge）所佔，故取多字元代號 `SC`／`SS`
# （多字元代號有既有先例 `I-cross`／`I-sibling`）。
# CDD-01_A T4：Diagnostics 之五項。下放包書 `VM-DIAG`，其判準逐字即 R-CAM2(a)(b)(c)，
# 與既有 `Z` 完全相同（R-G74 且已將 598／5210 升為全域），故**沿用 `Z` 不另立代號**——
# 另立即為同一判準之第二份實作。`VM-DIAG` ≡ `Z`，記於 profile §4 與上繳包 §4。
FEATURE_CHECKS: dict[str, list[str]] = {
    "camera": ["Z"], "security": ["SC", "SS"],
    "diagnostics": ["P-DIAG", "U-DIAG", "R1-DIAG", "Z", "RM-DIAG", "SEC-DIAG", "KEY-DIAG",
                    "PC-DIAG"],
}
# **feature 專屬之豁免**：某 profile 下不適用之 `PROFILE_CHECKS` 項。
# R-SEC15(j)：Security 之 ER 為指令輸出斷言，無 R-SU33/34 之「觀測窗」概念，
# `I-cross` 對其 10 列全報「窗未完整宣告」而非跨列衝突，故豁免。
FEATURE_EXEMPT: dict[str, list[str]] = {"security": ["I-cross"],
                                        # R-DIAG12：比照 R-SEC15(j) —— Diagnostics 之 ER 為
                                        # UDS 請求／回應斷言，無 R-SU33/34 之觀測窗，
                                        # pilot01 實測 14/14 全報「窗未完整宣告」。
                                        # R-DIAG17：本 feature 不寫導航 hop，`X` 之命中皆為
                                        # DID 名／CFTS004 用詞之字面（batch 3 實測 12 行，真違規 0）。
                                        "diagnostics": ["I-cross", "X"]}
# R-SEC20(amend)(c)（SEC-10）：**部分**豁免 —— 只吞「命中位置落於 `"…"` 內」者。
# `FEATURE_EXEMPT` 之語意為整項移出 `check_order()`，無從表達位置條件
# （整項豁免會連引號外之命中一起吞，違 SEC-10 §5 第二條），故另立本表。
# 出處：R-SEC20(c) 要求 ER 引 037 逐字要件，037 CP-006 VC 之
# `logs must align with Logdog requirements (Error-level only for defects)` 自帶關係模糊語，
# 改寫即造值 —— 故豁免限於引文內。
# 施檢面之判定沿用檢查 B 之同一機制（`quoted_spans()` ＋ `inside_spans()`）。
FEATURE_EXEMPT_QUOTED: dict[str, list[str]] = {"security": ["H"]}


# **列級**豁免（R-DIAG11，Pei 2026-09-17）：與 FEATURE_EXEMPT（整項移出 check_order）不同 ——
# 本表所列之項只對**符合條件之列**不施檢，其餘列照檢。
# 立此結構之由（CDD-02 pilot01 實測）：R-DIAG3(amend) 之 Out of Scope 佔列不產 TC，
# 其 test_item 無括號下半、四欄空白、Pre-Condition 無編號行、Vehicle Model 無從填，
# `I`／`M`／`R`／`Z` 恆紅 12 行計，且**無論如何填寫皆不可能同時滿足**
# （`Z` 之 R-CAM2(a) 要求填 0／1，而 (c) 要求五有效欄至少一個 `1`；該列 Region 為空，
#  填 `1` 即斷言其適用於該車型，為 §8.4.1 之造值）。
# `R1-DIAG`／`RM-DIAG` **不在豁免內** —— Requirement ID 仍須單值，
# Remarks 仍須含 `CFTS004 Category: Out of Scope`。
ROW_EXEMPT_OOS: dict[str, list[str]] = {"diagnostics": ["I", "M", "R", "Z"]}
# 判別條件：`Test Result 測試結果` 欄之值（去空白後）
ROW_EXEMPT_OOS_VALUE = "Out of Scope"
TEST_RESULT_HEADER = "Test Result"


def test_result_idx(header_values: list) -> int | None:
    """`Test Result 測試結果` 欄之 0-based 索引。

    R-G48 母本第 9 列為 `AF`。以 startswith 比對英文段，與 FIELD_HEADERS 同機制。
    母本另有 r7 之區塊標題 `Test Result 測試結果`（合併儲存格），但其不在第 9 列，不受影響。
    """
    for idx, value in enumerate(header_values):
        if value is not None and str(value).strip().startswith(TEST_RESULT_HEADER):
            return idx
    return None


def row_exempt(profile: str | None, test_result: str) -> set[str]:
    """本列所豁免之檢查代號（R-DIAG11）。"""
    if not profile:
        return set()
    if test_result.replace("\xa0", " ").strip() != ROW_EXEMPT_OOS_VALUE:
        return set()
    return set(ROW_EXEMPT_OOS.get(profile, []))


def check_order(profile: str | None) -> list[str]:
    """本次執行所啟用之檢查序列。"""
    if not profile:
        return list(CHECK_ORDER)
    exempt = set(FEATURE_EXEMPT.get(profile, []))
    return ([k for k in CHECK_ORDER + PROFILE_CHECKS if k not in exempt]
            + FEATURE_CHECKS.get(profile, []))


def check_title(key: str, profile: str | None) -> str:
    if profile and key in CHECK_TITLE_PROFILE:
        return CHECK_TITLE_PROFILE[key]
    return CHECK_TITLES[key]


def check_status(key: str, profile: str | None) -> str:
    if profile and key in CHECK_STATUS_PROFILE:
        return CHECK_STATUS_PROFILE[key]
    return CHECK_STATUS[key]

# 各檢查之記錄粒度（報告表頭「行計」欄之語意）
CHECK_GRANULARITY = {
    "A": "每次命中", "B": "每次命中", "C": "每次命中",
    "D": "每次命中／每編號行", "E": "每列", "F": "每次命中",
    "G": "每列", "H": "每次命中", "I": "每列", "I-sibling": "每列",
    "J": "每行", "K": "每列每欄", "L": "每列", "M": "每列每欄", "N": "每行",
    "P": "每次命中",
    "SC": "每編號步驟／每 ER 行", "SS": "每列",
    "P-DIAG": "每列每欄每 token", "U-DIAG": "每列每位元組串",
    "R1-DIAG": "每列", "RM-DIAG": "每列每段",
    "SEC-DIAG": "每列", "KEY-DIAG": "每列每次命中", "PC-DIAG": "每列每行",
    "Q": "每行每欄", "R": "每行", "T": "每次命中", "U": "每次命中",
    "V": "每行每欄",
    "I-cross": "每列每配對（一組命中記二列）",
    "W": "每次命中",
    "X": "每行",
    "Y": "每行",
    "Z": "每列每欄；七欄全缺時每 sheet 記一筆",
}


# --- 資料結構 ----------------------------------------------------------------


@dataclass
class Violation:
    """單筆違規記錄。"""

    check: str
    row: int
    tc_id: str
    field: str
    detail: str
    snippet: str = ""

    def as_dict(self) -> dict:
        return {
            "check": self.check,
            "row": self.row,
            "tc_id": self.tc_id,
            "field": self.field,
            "detail": self.detail,
            "snippet": self.snippet,
        }


@dataclass
class SheetResult:
    """單一 TC sheet 的檢查結果。"""

    sheet: str
    header_row: int
    data_rows: int
    violations: list[Violation] = dc_field(default_factory=list)
    # I-cross 之原料（`--merge` 用）：(列, TC id, req id, Test Set, proc, er)
    cross_rows: list[tuple] = dc_field(default_factory=list)


# --- 工具函式 ----------------------------------------------------------------


def cell_text(value) -> str:
    """儲存格轉純文字；None 視為空字串。"""
    if value is None:
        return ""
    return str(value)


def split_lines(text: str) -> list[str]:
    """欄內以 \\n 切分為行。"""
    return text.split("\n")


def numbered_lines(text: str) -> list[str]:
    """取出編號行。"""
    return [ln for ln in split_lines(text) if NUMBERED_LINE.match(ln)]


def find_header_row(ws) -> int:
    """掃前 15 列，找含 Specification Reference 之列作為 header。"""
    for idx, row in enumerate(ws.iter_rows(min_row=1, max_row=HEADER_SCAN_ROWS,
                                           values_only=True), start=1):
        for value in row:
            if value is not None and HEADER_ANCHOR in str(value):
                return idx
    raise ValueError(f"sheet {ws.title!r} 前 {HEADER_SCAN_ROWS} 列找不到 "
                     f"{HEADER_ANCHOR!r} 標頭")


def build_column_map(header_values: list) -> dict[str, int]:
    """依 startswith 建立 欄位鍵 -> 0-based 欄索引 對照。"""
    columns: dict[str, int] = {}
    for idx, value in enumerate(header_values):
        if value is None:
            continue
        text = str(value).strip()
        first_line = text.split("\n", 1)[0].strip()
        for key, keyword in FIELD_HEADERS.items():
            if key not in columns and text.startswith(keyword):
                columns[key] = idx
        if "req_id" not in columns and text.startswith(REQ_ID_HEADER):
            columns["req_id"] = idx
        if "tc_id" not in columns and first_line == TC_ID_FIRSTLINE:
            columns["tc_id"] = idx
    return columns


def build_vehicle_model_columns(header_values: list) -> dict[str, int]:
    """`Vehicle Model 車型` 七子欄 -> 0-based 欄索引。

    比對取標頭之首行去空白；母本為 `HDCC27\nAtl-Hi\n` 之形，第二行之 EE 不入鍵。
    找不到者不入 dict —— 呼叫端以「缺幾欄」判別工作簿是否具備此七欄。
    """
    columns: dict[str, int] = {}
    for idx, value in enumerate(header_values):
        if value is None:
            continue
        first_line = str(value).split("\n", 1)[0].strip()
        for name in VEHICLE_MODEL_HEADERS:
            if name not in columns and first_line == name:
                columns[name] = idx
    return columns


def check_vehicle_model(raw: tuple, vm_columns: dict[str, int],
                        row_no: int, tc_id: str) -> list[Violation]:
    """Z —— Vehicle Model 七欄之 1／0 檢查（R-CAM2）。

    (a) 七欄每欄須為 `1` 或 `0`，不留空、不用其他符號。
    (b) `Commander (598)`／`Regengade (5210)` 恆為 `0`。
    (c) 其餘五欄至少一個 `1`。
    """
    out: list[Violation] = []
    values: dict[str, str] = {}
    for name in VEHICLE_MODEL_HEADERS:
        idx = vm_columns[name]
        text = cell_text(raw[idx]) if idx < len(raw) else ""
        values[name] = text.replace("\xa0", " ").strip()

    for name in VEHICLE_MODEL_HEADERS:
        value = values[name]
        if value not in VEHICLE_MODEL_ALLOWED:
            out.append(Violation(
                "Z", row_no, tc_id, f"vehicle_model[{name}]",
                "R-CAM2(a)：七欄每列須填 `1` 或 `0`，不留空、不用其他符號",
                "(空)" if not value else value[:40]))
        elif name in VEHICLE_MODEL_ZERO and value != "0":
            out.append(Violation(
                "Z", row_no, tc_id, f"vehicle_model[{name}]",
                f"R-CAM2(b)／R-G74：`{name}` 已不支援，一律 `0`", value))

    active = [n for n in VEHICLE_MODEL_HEADERS
              if n not in VEHICLE_MODEL_ZERO]
    if all(values[n] in VEHICLE_MODEL_ALLOWED for n in active) \
            and not any(values[n] == "1" for n in active):
        out.append(Violation(
            "Z", row_no, tc_id, "vehicle_model",
            "R-CAM2(c)：五個有效車型欄每列至少一個 `1`",
            "／".join(f"{n}={values[n]}" for n in active)))
    return out


def quoted_spans(text: str) -> list[tuple[int, int]]:
    """回傳成對引號（" " 與 “ ”）涵蓋之區間，供 B 豁免用。"""
    spans: list[tuple[int, int]] = []
    positions = [i for i, ch in enumerate(text) if ch == '"']
    for i in range(0, len(positions) - 1, 2):
        spans.append((positions[i], positions[i + 1]))
    start = None
    for i, ch in enumerate(text):
        if ch == "“":
            start = i
        elif ch == "”" and start is not None:
            spans.append((start, i))
            start = None
    return spans


def inside_spans(span: tuple[int, int], spans: list[tuple[int, int]]) -> bool:
    """判斷 match 區間是否完整落於任一引號區間內。"""
    return any(lo < span[0] and span[1] <= hi for lo, hi in spans)


def snippet_of(text: str, start: int = 0, width: int = 80) -> str:
    """取違規上下文片段，換行改為 ⏎ 以利單行呈現。"""
    lo = max(0, start - 20)
    return text[lo:lo + width].replace("\n", " ⏎ ").strip()


def upper_half(test_item: str) -> str:
    """test_item 上半：去除整行為 (…) 之括號行。"""
    kept = [ln for ln in split_lines(test_item)
            if not RE_PAREN_LINE.match(ln.strip())]
    return "\n".join(kept)


def paren_lines(test_item: str) -> list[str]:
    """test_item 中整行為 (…) 之括號行。"""
    return [ln.strip() for ln in split_lines(test_item)
            if RE_PAREN_LINE.match(ln.strip())]


def first_token(text: str) -> str | None:
    """取第一個 token（00b 修訂 2：不再跳過非字母 token）。"""
    tokens = text.split()
    return tokens[0] if tokens else None


def j_violating_token(line_body: str) -> str | None:
    """J 判定：回傳違規 token，合規或豁免則回傳 None。

    第一個 token 若非以字母開頭（數字、$、引號、符號），該行豁免。
    """
    token = first_token(line_body)
    if token is None:
        return None
    if not token[0].isalpha():
        return None
    if not token[0].islower():
        return None
    if j_exempt(token):
        return None
    return token


def j_exempt(token: str) -> bool:
    """J 檢查之豁免判斷。"""
    bare = token.strip(".,;:)!?")
    if token in J_WHITELIST or bare in J_WHITELIST:
        return True
    if RE_CAMEL.match(token) or RE_CAMEL.match(bare):
        return True
    if RE_DOTCALL.match(token) or RE_DOTCALL.match(bare):
        return True
    if token[:1] in ('$', '"', "'", "“"):
        return True
    return False


def n_exempt(line: str) -> bool:
    """N 檢查之豁免：空行、$ 指令行、縮排續行。"""
    if not line.strip():
        return True
    if line.strip().startswith("$"):
        return True
    if line[:1] in (" ", "\t") and not N_STEP_LINE.match(line):
        return True
    return False


# --- 逐列檢查 ----------------------------------------------------------------


def check_row(fields: dict[str, str], row_no: int, tc_id: str,
              length_limit: int, profile: str | None = None) -> list[Violation]:
    """對單列跑 A–N（除 I-sibling 外）之檢查。

    `profile` 為 None 時行為與 21 包之前完全一致；指定時另跑 Q／R／T／U／V／W／X
    與車輛屬性方括號式。**P 之判準兩者相同**（R-G70：v4 為全域預設）。
    """
    out: list[Violation] = []
    proc = fields["proc"]
    er = fields["er"]
    pre = fields["pre"]
    item = fields["test_item"]

    def add(check: str, field_key: str, detail: str, snippet: str = "") -> None:
        out.append(Violation(check, row_no, tc_id, field_key, detail, snippet))

    # A 禁用動詞
    for m in RE_A.finditer(proc):
        add("A", "proc", f"禁用動詞 {m.group(0).strip()!r}",
            snippet_of(proc, m.start()))

    # B ER 情態詞（引號內豁免）
    spans = quoted_spans(er)
    for m in RE_B.finditer(er):
        if inside_spans((m.start(), m.end()), spans):
            continue
        add("B", "er", f"情態詞 {m.group(0)!r}", snippet_of(er, m.start()))

    # C hedge（範圍依 R-6b：僅括號下半。上半為需求原句 verbatim，
    # 其用語屬來源文件而非作者所擇，不受「作者用語品質」類檢查規制）
    for line in paren_lines(item):
        for m in RE_C.finditer(line):
            add("C", "test_item(括號下半)", f"hedge {m.group(0)!r}", line[:80])

    # D PC 違規
    for m in RE_D_POWERED.finditer(pre):
        add("D", "pre", f"通電前提 {m.group(0)!r}", snippet_of(pre, m.start()))
    for line in split_lines(pre):
        if not NUMBERED_LINE.match(line):
            continue
        body = NUMBER_PREFIX.sub("", line)
        m = RE_D_VERB.match(body)
        if m:
            add("D", "pre", f"編號行行首動詞 {m.group(0)!r}", line.strip()[:80])

    # E 對齊
    n_proc, n_er = len(numbered_lines(proc)), len(numbered_lines(er))
    if n_proc > 0 and n_er > 0 and n_proc != n_er:
        add("E", "proc/er", f"proc {n_proc} 步 vs er {n_er} 步", "")

    # W：ER 有比較而上半無數值（profile 專屬）
    if profile:
        _up = split_lines(fields["test_item"])
        if _up and not RE_W_NUMERAL.search(_up[0]):
            for m in RE_W_COMPARE.finditer(er):
                add("W", "er", f"比較關係 {m.group(0)!r}，而 test_item 上半無數值",
                    snippet_of(er, m.start()))

    # F 方括號 —— profile 啟用時，`$<name>$ = [值]` 之值不判（下放包 43 §二 #1）
    exempt = {m.span(1) for m in RE_F_SIGNAL_VALUE.finditer(proc)} if profile else set()
    for m in RE_F.finditer(proc):
        if m.span() in exempt:
            continue
        add("F", "proc", f"方括號佔位 {m.group(0)!r}", snippet_of(proc, m.start()))

    # G Test Set 空值
    if not fields["test_set"].strip():
        add("G", "test_set", "Test Set 為空", "")

    # H ER 模糊（R-SEC20(amend)(c)：引文內之命中依 `FEATURE_EXEMPT_QUOTED` 豁免）
    h_quoted = profile is not None and "H" in FEATURE_EXEMPT_QUOTED.get(profile, [])
    for m in RE_H.finditer(er):
        if h_quoted and inside_spans((m.start(), m.end()), spans):
            continue
        add("H", "er", f"模糊語 {m.group(0)!r}", snippet_of(er, m.start()))
    if profile:
        for m in RE_H_RELATION.finditer(er):
            if h_quoted and inside_spans((m.start(), m.end()), spans):
                continue
            add("H", "er", f"關係模糊語 {m.group(0)!r}", snippet_of(er, m.start()))

    # I 括號下半（缺括號）
    if item.strip():
        has_paren_line = bool(paren_lines(item))
        has_paren_tail = bool(RE_PAREN_TAIL.search(item.strip()))
        if not has_paren_line and not has_paren_tail:
            add("I", "test_item", "缺括號下半", snippet_of(item))

    # J 行首大寫
    first_line = split_lines(item)[0] if item else ""
    token = j_violating_token(NUMBER_PREFIX.sub("", first_line))
    if token:
        add("J", "test_item", f"首字小寫 {token!r}", first_line.strip()[:80])
    for key in J_NUMBERED_FIELDS:
        for line in split_lines(fields[key]):
            if not NUMBERED_LINE.match(line):
                continue
            token = j_violating_token(NUMBER_PREFIX.sub("", line))
            if token:
                add("J", key, f"首字小寫 {token!r}", line.strip()[:80])

    # K CJK
    for key in K_FIELDS:
        m = RE_CJK.search(fields[key])
        if m:
            add("K", key, "含 CJK 字元", snippet_of(fields[key], m.start()))

    # L 長度
    head = upper_half(item)
    n_tokens = len(RE_TOKEN.findall(head))
    if n_tokens > length_limit:
        add("L", "test_item", f"上半 {n_tokens} tokens > {length_limit}",
            snippet_of(head))

    # M 空欄三態
    for key in M_FIELDS:
        value = fields[key].strip()
        if value:
            continue
        add("M", key, "空欄（非 NA、非 PENDING:）", "")

    # N 尾句號：命中 [.。]$ 即違規（canon §11 禁尾句號；00b 修訂 1 反轉）
    for key in N_FIELDS:
        for line in split_lines(fields[key]):
            if n_exempt(line):
                continue
            if RE_TRAILING_PERIOD.search(line.rstrip()):
                add("N", key, "行尾多餘句號", line.strip()[:80])

    # P 訊號寫法（範圍依 R-6：作者生成內容，不含 test_item 上半）
    # R-G70（v4）：判準即 `Send CAN:` 式，**全域預設**；v3 分支已移除。
    signal_check = check_signal_line
    for key in P_FIELDS:
        for line in split_lines(fields[key]):
            out.extend(signal_check(line, key, row_no, tc_id))
    for line in paren_lines(item):                    # test_item 括號下半
        out.extend(signal_check(line, "test_item(括號下半)", row_no, tc_id))

    if not profile:
        return out

    # --- 以下僅於 --profile 指定時啟用 --------------------------------------

    # Q 不可見字元（R-10(a)，全欄位含 verbatim 上半）
    for key in Q_FIELDS:
        for line in fields.get(key, "").split("\n"):
            hits = []
            if "\xa0" in line:
                hits.append("NBSP")
            if "\u3000" in line:
                hits.append("全形空格")
            if RE_Q_TRAILING_WS.search(line):
                hits.append("行尾空白")
            if hits:
                add("Q", key, "／".join(hits), line.strip()[:80])

    # V 行首空白（IN §11，27 包 §D-4）
    for key in Q_FIELDS:
        for line in fields.get(key, "").split("\n"):
            if RE_V_BLANK_WS.match(line):
                add("V", key, "整行僅空白", "")
            elif RE_V_LEADING_WS.match(line) and not RE_V_EXEMPT.match(line):
                add("V", key, "行首空白", line[:80])

    # R Pre-Condition 版面（R-9(a)）
    for line in split_lines(pre):
        if not NUMBERED_LINE.match(line):
            add("R", "pre", "未編號行", line.strip()[:80])
            continue
        body = NUMBER_PREFIX.sub("", line).replace(R_TOOL_PHRASE, "")
        if (" and " in body or ", " in body) and \
                len(RE_R_PREDICATE.findall(body)) >= 2:
            add("R", "pre", "多條件並列於同一行", line.strip()[:80])

    # T PENDING 說明之語言（R-14）
    for key in T_FIELDS:
        for line in split_lines(fields[key]):
            m = RE_T_PENDING.search(line)
            if not m:
                continue
            desc = m.group("desc") or ""
            bad = [c for c in desc if ord(c) > 127]
            if bad:
                add("T", key, f"PENDING 說明含非 ASCII 字元 {bad[:3]!r}",
                    line.strip()[:80])
            # U 佔位之可見性（A-PM16）：ER 側原不受任何檢查覆蓋，
            # 致 `PENDING` 行「未被覆蓋」與「通過」無從分辨。逐一列出。
            add("U", key, f"PENDING 佔位（{m.group('dr') or '未標 DR'}）",
                line.strip()[:80])

    # 車輛屬性方括號式（下放包 43 §二 #1）—— 原實作於 v3 分支內，
    # v3 撤銷後獨立保留（R-G70 未廢此裁定）。
    for key in P_FIELDS:
        for line in split_lines(fields[key]):
            out.extend(check_vehicle_property_line(line, key, row_no, tc_id))

    # PROXI 形態（R-G70 v4.1）—— 標準 SWC 式合規、VF230 舊式記 Y（WARN）、其餘記 P。
    for key in P_FIELDS:
        for line in split_lines(fields[key]):
            out.extend(check_proxi_line(line, key, row_no, tc_id))

    # X 導航路徑之固定入口（§5.8／R-G71）—— WARN 只報不改。
    # 入口以**整列** proc＋pre 為範圍（§5.8(a) 之「同 TC 內」）：入口常寫在
    # Pre-Condition 或前一步驟，逐行判會把正確的多步路徑全報成違規。
    nav_scope = pre + "\n" + proc
    if not RE_X_ENTRY.search(nav_scope):
        for line in split_lines(proc):
            if RE_X_PENDING.search(line):
                continue
            m = RE_X_TARGET.search(line)
            if m:
                add("X", "proc", f"導航標的 {m.group(0)!r} 而同 TC 無固定入口",
                    line.strip()[:80])

    return out


def check_signal_line(line: str, field: str, row_no: int, tc_id: str
                      ) -> list[Violation]:
    """R-1 v2 之單行判定（逐賦值出現，非逐行）。

    四項：(1) 撤銷之三件組殘留（v1）；(2) **v3 記法殘留**（`$<MSG>.<Sig>$`
    包覆式，R-G70(h)）；(3) CAN 賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`；
    (4) Procedure 之賦值行缺 `Send CAN:` 前綴。

    逐「出現」而非逐「行」判定，是因 SWC 語料一行可載多個賦值
    （`… = 1 (Pressed) and BCM_FD_14.Command_09Sts = 0 (Not_Pressed)`），
    且 ER 之收尾語不固定（`is sent`／`is set`／`during …`／`then …`），
    對收尾語設限即與基準本相牴觸。
    """
    out: list[Violation] = []

    def add(detail: str) -> None:
        out.append(Violation("P", row_no, tc_id, field, detail, line.strip()[:80]))

    for m in RE_P_TRIPLET.finditer(line):
        add(f"三件組已撤銷（R-1 v1）{m.group(0)!r}")

    # R-G70(h)：v3 記法殘留 —— 須在下方之提早返回**之前**判，
    # 否則 `$` 包覆式因不含相鄰之 `=` 而永不被計（GC-12 正控之成因）。
    for m in RE_P_V3_DOLLAR.finditer(line):
        add(f"v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）{m.group(0)!r}")

    assignments = list(RE_P_ASSIGNMENT.finditer(line))
    if not assignments:
        return out

    for m in assignments:
        if not RE_P_VALUE_FORM.match(line, m.start()):
            add(f"賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：{m.group(0)!r}")

    if field == "proc" and "Send CAN:" not in line:
        add("Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)）")
    return out


def check_proxi_line(line: str, field: str, row_no: int, tc_id: str
                     ) -> list[Violation]:
    """PROXI 行之形態（R-G70 v4.1，Pei 裁定 2026-09-05）。

    標準式 `PROXI <Param> = <值>`（SWC）→ 無違規。
    舊式 `PROXI $<Param>$ is set to "<值>"`（VF230 152 列）→ 記 **Y（WARN，不 FAIL）**。
    兩式皆不中而含 `PROXI` **且該行為賦值形態**者 → 記 **P**（形態不明，須人看）。
    **純散文提及不報**（R-G70(i)，GC-13 審閱）—— 賦值形態之判準為同行有
    `=` 或 `is set to`。

    v4.0 之方向相反（VF230 為標準），已由 Pei 裁定更正；成因見
    `up/20260905_GC-09_notice.md` 與台帳 R-G70 之 v4.1 註。
    """
    out: list[Violation] = []
    if not RE_P_PROXI_ANY.search(line):
        return out
    if RE_P_PROXI.search(line):
        return out
    if RE_P_PROXI_LEGACY.search(line):
        out.append(Violation(
            "Y", row_no, tc_id, field,
            "PROXI 舊式 `$Param$ is set to`（R-G70 v4.1：新產出採 `PROXI <Param> = <值>`）",
            line.strip()[:80]))
        return out
    # R-G70(i)：非賦值形態者為散文提及，不報。
    if not RE_P_PROXI_ASSIGN_SHAPE.search(line):
        return out
    out.append(Violation(
        "P", row_no, tc_id, field,
        "PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式",
        line.strip()[:80]))
    return out


def check_vehicle_property_line(line: str, field: str, row_no: int, tc_id: str
                                ) -> list[Violation]:
    """無點之車輛屬性 `$<Name>$ = [值]`（下放包 43 §二 #1，037 逐字記法）。

    **本檢查不屬 R-1 v3**，故 v3 撤銷（R-G70）時不隨之移除 —— 它原本只是
    實作在 `check_signal_line_v3` 之內。P 之各式皆要求訊號名含一個點，
    本形態因而不被任何式命中，`P=0` 是沉默不是核可（上繳包 37 §2.2）。

    profile 專屬（與其原本之啟用條件相同），違規記於 P。
    """
    out: list[Violation] = []
    ok = {m.start() for m in RE_P3_PROP_OK.finditer(line)}
    for m in RE_P3_PROP_ANY.finditer(line):
        if "." in m.group(1):          # 含點者為訊號名，由 check_signal_line 管
            continue
        if m.start() in ok:
            continue
        if m.group("val").startswith("PENDING"):   # R-14 佔位，另由 T 檢查
            continue
        out.append(Violation(
            "P", row_no, tc_id, field,
            f"車輛屬性之值須以 `[…]` 包覆（037 逐字記法）：{m.group(0).strip()!r}",
            line.strip()[:80]))
    return out


def check_sibling_parens(rows: list[tuple[int, str, str, str]]) -> list[Violation]:
    """I-sibling：同 Requirement ID 下多列括號行內容逐字相同。"""
    out: list[Violation] = []
    groups: dict[tuple[str, str], list[tuple[int, str]]] = {}
    for row_no, tc_id, req_id, item in rows:
        content = "\n".join(paren_lines(item))
        if not req_id.strip() or not content:
            continue
        groups.setdefault((req_id.strip(), content), []).append((row_no, tc_id))
    for (req_id, content), members in groups.items():
        if len(members) < 2:
            continue
        for row_no, tc_id in members:
            out.append(Violation(
                "I-sibling", row_no, tc_id, "test_item",
                f"與 {req_id} 下另 {len(members) - 1} 列括號行逐字相同",
                content.replace("\n", " ⏎ ")[:80],
            ))
    return out


# --- W：ER 含比較關係而 `test_item` 上半無數值（下放包 47 §二 #6）------------
#
# 其形態為「指名二個被比較的量，而規格未給任何數值」—— **精度遂由讀者決定**。
# **待人裁非 FAIL**：有些列之精度由畫面粒度給出（`041` 改寫後即是），合法。
RE_W_COMPARE = re.compile(
    r"\b(corresponds? to|equals?|differs? from|matches?|greater than|less than|"
    r"same as|identical to)\b", re.I)
RE_W_NUMERAL = re.compile(r"\d")

# --- X 導航路徑（§5.8／R-G71）------------------------------------------------
# 觸發詞：步驟指向某個畫面／層級而未必寫出入口。
RE_X_TARGET = re.compile(r"\b(menu|page|screen|settings|tab)\b", re.I)
# 固定入口之閉合清單（§5.8(a)）。`H/K "<button>"` 之標籤自由，故只認前綴。
RE_X_ENTRY = re.compile(
    r'Menu Bar|App Drawer|Home Screen|Status Bar|H/K\s*"|Dealer Mode|Eng Mode')
# 已依 §5.8(d) 登記者不重複報 —— PENDING 行本身由 U 承擔。
RE_X_PENDING = re.compile(r"PENDING:\s*DR-")


# --- I-cross（R-SU34 v3）------------------------------------------------------
#
# `I-sibling` 之分組鍵含 `req_id`，故跨 `Requirement ID` 之偽通過**結構上永不觸發**。
# 本檢查補該缺口，其指標為 **觀測窗 × 違例類**（非行文相似度 —— v1 之比率指標
# 經回測與欲測性質負相關而作廢，見 `features/sw_update/scripts/i_cross.py`）。
#
# ⚠ **本檢查有一處前提被寫死在檢查裡**（R-SU34 v3(b) 之明令、PLAYBOOK (33)）：
#   `IX_NORMALISE` 把「未指定之起點」正規化為可用性查詢、
#   把 `until the update finishes` 正規化為版本號改變。
#   **其來源為下放包 30 §2.1 之裁定，不是 TC 之文字。**
#   **若該裁定改動，本表須同步改** —— 否則本檢查會沉默地沿用一個已失效之前提。

IX_START = [(r"from the availability check", "availability-check"),
            (r"from the start of the session", "session-start")]

# ── 訖點之抽取（下放包 43 §二 #4：改語形抽取，不寫死片語）────────────────
#
# **首版為一張寫死之片語表**（`until the software version changes`／
# `until the update finishes`），二者皆出自 `Silent Update` 那一批。
# `ROV Installation` 之 `until the installation ends` 二者皆不匹配，
# 遂被靜默算成半窗（上繳包 37 §2.3）。**每進一個新 Test Set 該表即落後一次。**
#
# **正規化規則（須隨結果揭露）**：
#   1. 取 `until` 之後至行尾／逗號／分號為止之整段子句；
#   2. 去冠詞（`the`／`a`／`an`）、轉小寫、空白收斂為單一連字號；
#   3. 查 `IX_END_ALIAS` —— **其只收「由裁定導出之等價」**，不收語形近似。
RE_IX_UNTIL = re.compile(r"\buntil\s+([^,;]+?)(?=[,;]|$)", re.M)
IX_END_ALIAS = {
    # 下放包 30 §2.1 之裁定：更新完成之唯一外部表徵為版本號改變，
    # 故「更新結束」與「版本改變」為同一訖點。**此為裁定，非語形。**
    "update-finishes": "software-version-changes",
    "update-finish": "software-version-changes",
}


def _ix_end_label(txt: str) -> str | None:
    m = RE_IX_UNTIL.search(txt)
    if not m:
        return None
    s = re.sub(r"\b(the|a|an)\b", " ", m.group(1).lower())
    lab = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return IX_END_ALIAS.get(lab, lab) or None
# ⚠ **正規化之射程限於「起點」**（下放包 30 §2.1 所裁者為起點）。
# **首版誤把同一規則同時套在訖點上**，致無 `until …` 片語之 TC 之窗
# 退化為 `availability-check → availability-check` —— **它長得像一個窗，
# 故沒有任何檢查會攔它**（下放包 34 §1.2）。訖點缺失時**不正規化**。
IX_NORMALISE_START = {None: "availability-check"}      # 未指定之起點 → 唯一可觀測者
# 訖點之等價由 `IX_END_ALIAS` 承擔（見上），此處不再另設對照
# 取最細之類；交集以上下位關係判（R-SU34 v3(b)）
IX_VIOLATION = [
    (r"download confirmation screen", "confirmation-screen/download"),
    (r"deployment confirmation screen", "confirmation-screen/deployment"),
    (r"\bconfirmation screen", "confirmation-screen"),
    (r"SW Update prompt", "prompt"),
    (r"progress notification", "progress-notification"),
    (r"opt-out control", "opt-out"),
    (r"defer control", "defer"),
]
IX_NEG = re.compile(r"contains no |no SW Update prompt|no progress notification"
                    r"|no download confirmation|no deployment confirmation"
                    r"|no confirmation screen|no opt-out|no defer")


def _ix_window(proc: str, er: str) -> tuple[str | None, str | None]:
    """回傳 (起, 訖)。訖點無片語可抽時為 `None` —— **半窗，不參與比對**。"""
    txt = proc + " " + er
    s = next((v for p, v in IX_START if re.search(p, txt)), None)
    e = _ix_end_label(txt)
    return IX_NORMALISE_START.get(s, s), e


def _ix_violations(er: str) -> set[str]:
    """僅取**否定式**之 ER 行；同行命中概括式與子類時只留子類。"""
    out: set[str] = set()
    for ln in er.split("\n"):
        if not IX_NEG.search(ln):
            continue
        hit = {v for p, v in IX_VIOLATION if re.search(p, ln)}
        out |= {v for v in hit
                if not any(o != v and o.startswith(v + "/") for o in hit)}
    return out


def _ix_subsumes(a: str, b: str) -> bool:
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def check_cross(rows: list[tuple[int, str, str, str, str, str]]) -> list[Violation]:
    """I-cross：**同一 Test Set 內**，觀測窗相同且違例類有交集之跨 req_id 配對。

    **警示器非判準**（R-SU34 v3(c)）—— 窗同而違例類不同者合法。
    人裁所問為「本 TC 是否有屬於其需求單元之驗證點」，
    **不是**「其驗證點是否被他 TC 涵蓋」——**覆蓋是允許的**（R-SU34 v3(e)）。
    """
    out: list[Violation] = []
    info: list = []
    half: list = []          # 窗未完整宣告者（待補），不參與比對
    for row_no, tc_id, req_id, test_set, proc, er in rows:
        w = _ix_window(proc, er)
        if w[0] is None or w[1] is None:
            # **半窗**：R-SU36(b)／R-SU33 v1(b) 令 ER 須明載窗之起訖，
            # 抽不出訖點者其窗未完整宣告 —— **不參與比對，列為待補**。
            half.append((row_no, tc_id, w))
            continue
        info.append((row_no, tc_id, req_id, test_set, w, _ix_violations(er)))
    for i, (ra, ta, qa, sa, wa, va) in enumerate(info):
        for rb, tb, qb, sb, wb, vb in info[i + 1:]:
            if qa.strip() == qb.strip() or sa.strip() != sb.strip():
                continue          # 同 req_id 由 I-sibling 管；跨 Test Set 不比
            if wa != wb:
                continue
            inter = {min(x, y, key=len) for x in va for y in vb
                     if _ix_subsumes(x, y)}
            if not inter:
                continue
            for rn, tid, other in ((ra, ta, tb), (rb, tb, ta)):
                out.append(Violation(
                    "I-cross", rn, tid, "expected_result",
                    f"與 {other} 之觀測窗相同（{wa[0]} → {wa[1]}）且違例類有交集",
                    "／".join(sorted(inter))[:80],
                ))
    for rn, tid, w in half:
        out.append(Violation(
            "I-cross", rn, tid, "expected_result",
            "**窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對"
            "（R-SU33(b)：ER 須明載窗之起訖）",
            f"起 {w[0] or '—'} → 訖 **未載**",
        ))
    return out


# --- 工作簿層 ----------------------------------------------------------------


def lint_workbook(path: Path, length_limit: int = DEFAULT_LENGTH_LIMIT,
                  profile: str | None = None) -> list[SheetResult]:
    """唯讀開啟工作簿，對每個 TC sheet 跑檢查。"""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        results: list[SheetResult] = []
        for sheet_name in wb.sheetnames:
            if not sheet_name.startswith(TC_SHEET_PREFIX):
                continue
            results.append(lint_sheet(wb[sheet_name], length_limit, profile))
        if not results:
            raise ValueError(f"{path.name}：找不到以 {TC_SHEET_PREFIX!r} 開頭之 sheet")
        return results
    finally:
        wb.close()


def lint_sheet(ws, length_limit: int, profile: str | None = None) -> SheetResult:
    """單一 sheet 的檢查流程。"""
    header_row = find_header_row(ws)
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    columns = build_column_map(list(rows[header_row - 1]))
    missing = [k for k in FIELD_HEADERS if k not in columns]
    if missing:
        raise ValueError(f"sheet {ws.title!r} 缺欄位：{missing}")

    result = SheetResult(sheet=ws.title, header_row=header_row, data_rows=0)
    sibling_input: list[tuple[int, str, str, str]] = []
    cross_input: list[tuple[int, str, str, str, str, str]] = []

    # Z 為 feature 專屬（FEATURE_CHECKS）。七欄不齊時整 sheet 記一筆，
    # 不逐列複述 —— 缺欄是工作簿之事實，不是每一列各自的違規。
    enabled = check_order(profile)
    remarks_idx = (security_remarks_idx(list(rows[header_row - 1]))
                   if ("SS" in enabled or "RM-DIAG" in enabled) else None)
    # R-DIAG11 列級豁免所需之 `Test Result` 欄
    tr_idx = (test_result_idx(list(rows[header_row - 1]))
              if ROW_EXEMPT_OOS.get(profile or "") else None)
    vm_columns: dict[str, int] = {}
    if "Z" in enabled:
        vm_columns = build_vehicle_model_columns(list(rows[header_row - 1]))
        if len(vm_columns) != len(VEHICLE_MODEL_HEADERS):
            missing_vm = [n for n in VEHICLE_MODEL_HEADERS
                          if n not in vm_columns]
            result.violations.append(Violation(
                "Z", header_row, "", "vehicle_model",
                "R-CAM2：本 sheet 無完整之 `Vehicle Model 車型` 七子欄，Z 無法施檢",
                "缺 " + "／".join(missing_vm)))
            vm_columns = {}

    for offset, raw in enumerate(rows[header_row:], start=header_row + 1):
        fields = {key: cell_text(raw[idx]) if idx < len(raw) else ""
                  for key, idx in columns.items() if key in FIELD_HEADERS}
        if not any(fields[k].strip() for k in ("test_item", "proc", "er")):
            continue
        tc_id = cell_text(raw[columns["tc_id"]]) if "tc_id" in columns else ""
        req_id = cell_text(raw[columns["req_id"]]) if "req_id" in columns else ""
        result.data_rows += 1
        # R-DIAG11：本列之豁免集（Out of Scope 佔列）。`I`／`M`／`R` 由 check_row 產出，
        # 於此濾除；`Z` 於下方分支跳過。整項豁免請用 FEATURE_EXEMPT，不要走這裡。
        exempt_row = row_exempt(
            profile,
            cell_text(raw[tr_idx]) if tr_idx is not None and tr_idx < len(raw) else "")
        # `check_row()` 內部不知道 FEATURE_EXEMPT —— 其產出之 `X` 等項於豁免後
        # 仍會回傳，而該代號已不在 `enabled`，排序時 `enabled.index()` 會 ValueError
        # （R-DIAG17 落地後於 290 列之合併本實測 crash）。故於此一併依 `enabled` 過濾：
        # 列級豁免（exempt_row）與整項豁免（FEATURE_EXEMPT）在此收斂為同一道。
        enabled_set = set(enabled)
        result.violations.extend(
            v for v in check_row(fields, offset, tc_id, length_limit, profile)
            if v.check not in exempt_row and v.check in enabled_set)
        if vm_columns and "Z" not in exempt_row:
            result.violations.extend(
                check_vehicle_model(raw, vm_columns, offset, tc_id))
        # P-DIAG／U-DIAG／R1-DIAG／RM-DIAG 為 feature 專屬（FEATURE_CHECKS["diagnostics"]）；
        # 同組之 VM-DIAG 沿用 `Z`，於上方 vm_columns 分支施檢。
        if "P-DIAG" in enabled:
            result.violations.extend(check_diag_did(fields, offset, tc_id))
        if "U-DIAG" in enabled:
            result.violations.extend(check_diag_uds(fields, offset, tc_id))
        if "R1-DIAG" in enabled:
            result.violations.extend(check_diag_req_id(req_id, offset, tc_id))
        if "SEC-DIAG" in enabled:
            result.violations.extend(check_diag_security(req_id, fields, offset, tc_id))
        if "KEY-DIAG" in enabled:
            result.violations.extend(check_diag_key(req_id, fields, offset, tc_id))
        if "PC-DIAG" in enabled:
            result.violations.extend(check_diag_pc(fields, offset, tc_id))
        if "RM-DIAG" in enabled:
            diag_remarks = (cell_text(raw[remarks_idx])
                            if remarks_idx is not None and remarks_idx < len(raw) else "")
            result.violations.extend(
                check_diag_remarks(diag_remarks, offset, tc_id))
        # SC／SS 為 feature 專屬（FEATURE_CHECKS["security"]）
        if "SC" in enabled:
            result.violations.extend(
                check_security_channel(fields, offset, tc_id))
        if "SS" in enabled:
            remarks_text = (cell_text(raw[remarks_idx])
                            if remarks_idx is not None and remarks_idx < len(raw) else "")
            result.violations.extend(
                check_security_source(fields, remarks_text, offset, tc_id))
        sibling_input.append((offset, tc_id, req_id, fields["test_item"]))
        test_set = (cell_text(raw[columns["test_set"]])
                    if "test_set" in columns else "")
        cross_input.append((offset, tc_id, req_id, test_set,
                            fields["proc"], fields["er"]))

    result.violations.extend(check_sibling_parens(sibling_input))
    result.cross_rows = cross_input
    if "I-cross" in enabled:          # I-cross 為 profile 專屬（PROFILE_CHECKS），可被 FEATURE_EXEMPT 豁免
        result.violations.extend(check_cross(cross_input))
    result.violations.sort(key=lambda v: (enabled.index(v.check), v.row))
    return result


# ---------------------------------------------------------------- Security
# R-SEC7（下放包 SEC-01_E §1）之 `SC`，與 R-SEC4(a) 之 `SS`。
# 兩者只在 `--profile security` 下啟用（FEATURE_CHECKS），不隨任意 profile 生效。

# (a) 執行通道：編號步驟其後須有 `$` 指令行，或步驟句以實體操作動詞起首。
# R-SEC7(a) 之 CAN 類其指令行為 `Send CAN: …`（IN §8.7.5(c)），非 `$` 起首。
SEC_CMD_LINE = re.compile(r"^\s*(?:\$\s+\S|Send CAN:\s*\S)")
SEC_PHYS_STEP = re.compile(r'^\s*(?:Insert|Press|Power cycle|Disconnect|Select\s+")')
SEC_STEP_NO = re.compile(r"^\s*(\d+)[.)]\s*(.+)$")
# (c) ER 觀察手段之七類標記（LOG／FILE／UDS／RC／HOST／CAN／UI）
SEC_OBSERVE = re.compile(
    r"adb logcat\b"                                   # LOG
    r"|\bod -t x1\b|adb shell (?:cat|ls)\b"           # FILE
    # SEC-04 執行層延伸（待 Pei 確認）：R-SEC7(c) 之 FILE 類只列 od／cat／ls，
    # 而 037 KI-013／CP-010 之 verbatim 取樣指令為 `procrank`／`df`，SAM-0002 為 `ps -A`。
    # 其輸出同為 shell stdout，歸 FILE 類。
    r"|adb shell (?:procrank|df|ps)\b"
    # SEC-04 §2 明訂之兩個 ER 措辭（審閱指定）：`adb pull` 之傳輸回報與 log buffer 清空。
    # 二者不在 R-SEC7(c) 之七類字面內，惟其為分析層指定之修法，故收入。
    r"|adb pull\b|The log buffer is cleared"
    # R-SEC7(c) amend（SEC-05）增列：037 SWE1-LOGENC-006 之 verbatim 工具 ——
    # `adb shell getsslog`（觸發取樣）與 `logdecrypt_Ver2.sh`（解密驗證），出處為該列 VC。
    r"|adb shell getsslog\b|logdecrypt_Ver2\.sh"
    r"|Positive response is received|Negative response is received"   # UDS
    r"|OK \(\d+ tests?\)|FAILURES!!!"                 # RC
    r"|\bopenssl\b|: OK\b|error \d+ at \d+ depth"    # HOST
    r"|is sent\b"                                     # CAN
    r"|screen is displayed\b"                         # UI
    # R-SEC20（SEC-08）：X-i 裁降為文件審查後，其 ER 之觀察面為「審查」本身。
    # 出處：037 CP-006／CP-008 VC 之 `Inspect the build files`／`Inspect the source code`、
    # KI-012 之 Verification Method `Document Review / Static Analysis / Log Observation`。
    r"|(?:is|are) available for review\b"
    r"|\b(?:satisfies|satisfy|contains|contain|declares|declare) \u0022")   # DOC
# R-SEC4(a)：最終驗證步驟之觸發詞
SEC_VERIFY_VERB = re.compile(r"\b(?:Verify|Check|Confirm)\b")
SEC_SOURCE_MARK = re.compile(r"\bsource:", re.I)
# `remarks` 不在 `FIELD_HEADERS` 內（其為 A~N 主欄之對照表），故 `SS` 自行解析其欄位，
# 不動 `FIELD_HEADERS` —— 動之會改變所有既有檢查之 `fields` 內容。
SEC_REMARKS_HEADER = "Remarks"
# SEC-03 §4：`SC` 之四個補強判項。
# (1) 反引號／單引號包字串（R-SEC15(d)：字面值一律 `"…"`）
SEC_BAD_QUOTE = re.compile(r"`[^`\n]{1,120}`|(?<![A-Za-z])'[^'\n]{1,120}'(?![A-Za-z])")
# (2) 內部台帳代號（R-SEC15(c)）
SEC_LEDGER_ID = re.compile(r"\bX-[a-z]\b|\bDR-SEC-[a-z]\b|\bR-SEC\d|\bA-SE")
# (3) PENDING 須整行起首（R-SEC15(i)）
SEC_PENDING = re.compile(r"PENDING:")
SEC_PENDING_HEAD = re.compile(r"^\s*(?:\d+[.)]\s*)?PENDING:")
# R-SEC21(a)（SEC-08）：PENDING 之描述性佔位 —— `<性質 provided by <供給方> (X-<n>)>`。
# 該式為 R-SEC15(c)「內部代號只入 Remarks」之例外擴充（R-SEC21(a) 明文），
# 故 (2) 判項於比對前先剝除佔位片段；ER 之整行佔位比同整行 PENDING 免觀察手段。
# R-SEC20(b)（SEC-08）：文件審查之兩式步驟 —— 取得步驟整步為佔位、審查步驟為 `Review … against "…"`。
# 037 未載其檢查指令、執行層不得自擬（R-SEC20(b)），故此二式為 R-SEC7(a) 執行通道之例外（DOC 面）。
SEC_DOC_STEP = re.compile(
    r'^\s*(?:\d+[.)]\s*)?(?:<obtain [^<>]+ per RD>|Review .+ against ")')
SEC_PLACEHOLDER = re.compile(r"<[^<>]*\bprovided by\b[^<>]*\((X-[a-z0-9-]+)\)>")
SEC_PLACEHOLDER_LINE = re.compile(
    r"^\s*(?:\d+[.)]\s*)?<[^<>]*\bprovided by\b[^<>]*\(X-[a-z0-9-]+\)>"
    r"(?:\s+is\s+(?:executed|available|observed))?\s*$")
# (4) ER 行所引之指令須出現於同編號之 Procedure 步驟。
# SEC-04 §3：原式只認 `$ …` 形，抓不到散文形（`The adb shell ls -l … output`）。
# 改為自 ER 抽「指令片語」：動詞 token ＋ 其後之參數，止於第一個散文停用詞。
SEC_CMD_VERB = re.compile(
    r"\b(adb(?:\s+(?:shell\s+(?:ls|cat|od|am)|pull|push|logcat|reboot|root))?"
    r"|openssl|od|pytest)\b")
# 散文停用詞：其後之 token 不屬指令片語
SEC_PROSE_STOP = {"command", "output", "transfer", "result", "results", "stdout",
                  "run", "returns", "reports", "prints", "shows", "lists",
                  "contains", "is", "and", "on", "the", "for", "with"}
SEC_CMD_TOKEN = re.compile(r"[-A-Za-z0-9_./#@{}<>*]+")
SEC_LINE_NO = re.compile(r"^\s*(\d+)[.)]")
SEC_FOUR_FIELDS = ("pre", "input", "proc", "er")


def security_remarks_idx(header_values: list) -> int | None:
    for idx, value in enumerate(header_values):
        if value is not None and str(value).strip().startswith(SEC_REMARKS_HEADER):
            return idx
    return None



def sec_command_phrases(line: str) -> list[str]:
    """自 ER 行抽出「指令片語」（SEC-04 §3）。

    片語 = 指令動詞 token ＋ 其後之參數，止於第一個散文停用詞或引號。
    例：`The adb logcat -s logdog output is empty` → `adb logcat -s logdog`；
        `The openssl command prints "…"` → `openssl`（次 token 為停用詞）。
    """
    out: list[str] = []
    for m in SEC_CMD_VERB.finditer(line):
        verb = " ".join(m.group(0).split())
        rest = line[m.end():]
        parts = [verb]
        for tok in SEC_CMD_TOKEN.findall(rest):
            if tok.lower() in SEC_PROSE_STOP or tok.startswith('"'):
                break
            parts.append(tok)
        out.append(" ".join(parts))
    return out


def check_security_channel(fields: dict[str, str], row_no: int,
                           tc_id: str) -> list[Violation]:
    """SC —— R-SEC7(a)(c)：每步須有執行通道，每 ER 行須有觀察手段。"""
    out: list[Violation] = []
    proc_lines = [ln for ln in fields.get("proc", "").splitlines() if ln.strip()]
    for i, line in enumerate(proc_lines):
        m = SEC_STEP_NO.match(line)
        if not m:
            continue
        nxt = proc_lines[i + 1] if i + 1 < len(proc_lines) else ""
        # R-SEC15(b)：無可用觸發手段者，該步驟整行寫 PENDING token —— 免通道。
        if SEC_PENDING_HEAD.match(line):
            continue
        if SEC_CMD_LINE.match(nxt) or SEC_PHYS_STEP.match(m.group(2)):
            continue
        if SEC_DOC_STEP.match(line):      # R-SEC20(b)：文件審查步驟免執行通道
            continue
        out.append(Violation(
            "SC", row_no, tc_id, "proc",
            "R-SEC7(a)：編號步驟其後須有 `$` 指令行，或步驟句須為 "
            "`Insert`／`Press`／`Power cycle`／`Disconnect`／`Select \u0022…\u0022` 之實體操作",
            line.strip()[:60]))
    er_lines = [ln for ln in fields.get("er", "").splitlines() if ln.strip()]
    for line in er_lines:
        if SEC_PENDING_HEAD.match(line):     # R-SEC15(i)：整行 PENDING 免觀察手段
            continue
        if SEC_PLACEHOLDER_LINE.match(line):  # R-SEC21(b)：整行佔位同免（值尚未到手）
            continue
        if SEC_OBSERVE.search(line):
            continue
        out.append(Violation(
            "SC", row_no, tc_id, "er",
            "R-SEC7(c)：ER 每行須含七類觀察手段之一（LOG／FILE／UDS／RC／HOST／CAN／UI）",
            line.strip()[:60]))

    # --- SEC-03 §4 之四個補強判項 ---
    for key in SEC_FOUR_FIELDS:
        text = fields.get(key, "")
        for line in (ln for ln in text.splitlines() if ln.strip()):
            m = SEC_BAD_QUOTE.search(line)
            if m:                                                        # (1)
                out.append(Violation(
                    "SC", row_no, tc_id, key,
                    "R-SEC15(d)：字面值一律 \u0022…\u0022，反引號／單引號禁用",
                    m.group(0)[:60]))
            probe = SEC_PLACEHOLDER.sub("", line)     # R-SEC21(a)：佔位內之 X- 為例外
            m = SEC_LEDGER_ID.search(probe)
            if m and not SEC_PENDING_HEAD.match(line):                   # (2)
                out.append(Violation(
                    "SC", row_no, tc_id, key,
                    "R-SEC15(c)：內部台帳代號只可入 Remarks；PENDING token 起首者例外",
                    line.strip()[:60]))
            if key == "er" and SEC_PENDING.search(line) \
                    and not SEC_PENDING_HEAD.match(line):                # (3)
                out.append(Violation(
                    "SC", row_no, tc_id, "er",
                    "R-SEC15(i)：PENDING 為整行 token，不與散文混寫",
                    line.strip()[:60]))

    # (4) ER 某行引用之指令須出現於同編號之 Procedure 步驟
    proc_by_no: dict[str, str] = {}
    cur = ""
    for line in proc_lines:
        m = SEC_LINE_NO.match(line)
        if m:
            cur = m.group(1)
            proc_by_no[cur] = proc_by_no.get(cur, "") + line
        elif cur:
            proc_by_no[cur] += "\n" + line
    for line in er_lines:
        m = SEC_LINE_NO.match(line)
        if not m:
            continue
        step = " ".join(proc_by_no.get(m.group(1), "").split())
        for phrase in sec_command_phrases(line):
            if phrase not in step:
                out.append(Violation(
                    "SC", row_no, tc_id, "er",
                    "SEC-04 §3：ER 所引之指令未出現於同編號之 Procedure 步驟",
                    phrase[:60]))
    return out


def check_diag_did(fields: dict[str, str], row_no: int, tc_id: str) -> list[Violation]:
    """P-DIAG —— `$XXXX` 白名單（R-DIAG5(a)）。

    作者側四欄出現白名單外之 `$`+4hex 即 FAIL。`$MESSAGE.Signal$` 式帶尾 `$`，
    由 `RE_DIAG_DID` 之 negative lookahead 排除，維持檢查 P 原判。
    """
    out: list[Violation] = []
    for key in DIAG_AUTHOR_FIELDS:
        text = fields.get(key, "")
        for m in RE_DIAG_DID.finditer(text):
            token = m.group(0)
            if token.upper() not in {d.upper() for d in DIAG_DID_WHITELIST}:
                out.append(Violation(
                    "P-DIAG", row_no, tc_id, key,
                    "R-DIAG5(a)：`$XXXX` 須為本 feature 之 DID"
                    "（`layer3_assign.tsv` 之 36 種）", token))
    return out


def check_diag_uds(fields: dict[str, str], row_no: int, tc_id: str) -> list[Violation]:
    """U-DIAG —— UDS 位元組串格式（R-DIAG5(b)）。

    (1) 每 byte 兩位大寫 hex、單空格分隔。
    (2) `7F` 後兩 byte 必接 ` (<label>)`，label ∈ ISO 五名 ∪ CFTS004 原字。
    """
    out: list[Violation] = []
    proc = fields.get("proc", "")
    for m in RE_UDS_START.finditer(proc):
        for tok in proc[m.end():].split():
            if not RE_UDS_CAND.match(tok):
                break            # 串已結束（`via`／`is`／`received` 等散文）
            if not RE_UDS_BYTE_OK.match(tok):
                out.append(Violation(
                    "U-DIAG", row_no, tc_id, "proc",
                    "R-DIAG5(b)：UDS 位元組須為兩位大寫 hex、單空格分隔", tok))
    for m in RE_DIAG_7F.finditer(proc):
        tail = m.group("tail")
        if not tail:
            out.append(Violation(
                "U-DIAG", row_no, tc_id, "proc",
                "R-DIAG5(b)：`7F <SID> <NRC>` 後須接 `(<label>)`",
                m.group(0)[:60]))
            continue
        label = tail.strip()[1:-1].strip()
        if label not in DIAG_NRC_LABELS:
            out.append(Violation(
                "U-DIAG", row_no, tc_id, "proc",
                "R-DIAG5(amend)(d)：`(<label>)` 須為 ISO 14229-1 五名之一"
                "或 CFTS004 原字", label[:40]))
    return out


def check_diag_req_id(req_id: str, row_no: int, tc_id: str) -> list[Violation]:
    """R1-DIAG —— Requirement ID 欄單值（R-DIAG1(a)、R-DIAG2）。"""
    value = req_id.replace("\xa0", " ").strip()
    if not value:
        return [Violation("R1-DIAG", row_no, tc_id, "req_id",
                          "R-DIAG1(a)：Requirement ID 欄不得為空", "(空)")]
    if not RE_DIAG_REQ_ID.match(value):
        return [Violation(
            "R1-DIAG", row_no, tc_id, "req_id",
            "R-DIAG1(a)：只得一個 SWE1 ID，形式 `SWE1-Diagnostics-nnn`"
            "（重號者 `-001`／`-002`，R-DIAG2）", value[:60])]
    if value in DIAG_DUP_REQ_IDS:
        return [Violation(
            "R1-DIAG", row_no, tc_id, "req_id",
            f"R-DIAG2：`{value}` 為 037 之重號，須帶 `-001`／`-002` 尾綴區分",
            value)]
    return []


def check_diag_remarks(remarks: str, row_no: int, tc_id: str) -> list[Violation]:
    """RM-DIAG —— Remarks 定型句（R-DIAG3(amend)／R-DIAG6／R-DIAG7(a)／R-DIAG5(amend)）。

    Remarks 得為空（多數列無註）。非空者逐段（以 `;` 或換行分隔）須全數命中五式之一。
    """
    text = remarks.replace("\xa0", " ").strip()
    if not text:
        return []
    out: list[Violation] = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        # 定型句之一（R-DIAG6）**自身含 `; `**，故不得先以 `;` 切段再逐段比對 ——
        # 那會把該句切成兩半，使其永遠不可能通過自己所規定之檢查
        # （CDD-02 pilot 實測之假陽性 2 例）。改為自串首貪婪比對，以 `; ` 為接合符。
        rest = line
        while rest:
            for rx in RE_DIAG_REMARKS_OK:
                m = rx.match(rest)
                if m:
                    rest = rest[m.end():].lstrip()
                    if rest.startswith(";"):
                        rest = rest[1:].lstrip()
                    break
            else:
                out.append(Violation(
                    "RM-DIAG", row_no, tc_id, "remarks",
                    "R-DIAG：Remarks 須為所定五種定型句之一（多句以 `; ` 接合）",
                    rest[:60]))
                break
    return out


def check_security_source(fields: dict[str, str], remarks: str, row_no: int,
                          tc_id: str) -> list[Violation]:
    """SS —— R-SEC4(a)：最終驗證步驟須有 `source:` 標記。

    判準面之偏差（SEC-02 上繳包自報）：R-SEC4(a) 原文為「於 reasoning 註明來源」，
    reasoning 在生成側 JSON、不在工作簿；本檢查改以 **Remarks 欄**為判準面。
    """
    out: list[Violation] = []
    # R-SEC21(e)（SEC-08）：交付欄含 `<… provided by … (X-…)>` 者，
    # Remarks 須含同一 `X-` 代號（`asset: X-<n> — …`），否則追溯斷裂。
    for key in SEC_FOUR_FIELDS:
        for token in dict.fromkeys(SEC_PLACEHOLDER.findall(fields.get(key, ""))):
            if re.search(rf"{re.escape(token)}(?![0-9a-z-])", remarks):
                continue
            out.append(Violation(
                "SS", row_no, tc_id, key,
                "R-SEC21(e)：交付欄之資產佔位，Remarks 須含同一 `X-` 代號",
                token))
    proc_lines = [ln for ln in fields.get("proc", "").splitlines() if ln.strip()]
    numbered = [ln for ln in proc_lines if SEC_STEP_NO.match(ln)]
    if not numbered or not SEC_VERIFY_VERB.search(numbered[-1]):
        return out
    if SEC_SOURCE_MARK.search(remarks):
        return out
    return out + [Violation(
        "SS", row_no, tc_id, "remarks",
        "R-SEC4(a)：最終步驟含 `Verify`／`Check`／`Confirm`，"
        "Remarks 須有 `source:` 標記其落地來源",
        numbered[-1].strip()[:60])]


def count_by_check(results: list[SheetResult],
                   profile: str | None = None) -> dict[str, int]:
    """彙總各檢查之行計（違規記錄數）。"""
    counts = {key: 0 for key in check_order(profile)}
    for result in results:
        for violation in result.violations:
            counts[violation.check] += 1
    return counts


def rows_by_check(results: list[SheetResult],
                  profile: str | None = None) -> dict[str, int]:
    """彙總各檢查之列計（涉及之相異資料列數）。"""
    seen: dict[str, set[tuple[str, int]]] = {key: set()
                                             for key in check_order(profile)}
    for result in results:
        for violation in result.violations:
            seen[violation.check].add((result.sheet, violation.row))
    return {key: len(value) for key, value in seen.items()}


# --- 報告輸出 ----------------------------------------------------------------


def render_report(path: Path, results: list[SheetResult], length_limit: int,
                  profile: str | None = None) -> str:
    """產生 markdown 報告。"""
    order = check_order(profile)
    counts = count_by_check(results, profile)
    row_counts = rows_by_check(results, profile)
    total_rows = sum(r.data_rows for r in results)
    lines = [
        f"# lint036 報告：{path.name}",
        "",
        f"- 來源：`{path}`（唯讀）",
        f"- 資料列數：{total_rows}",
        f"- sheet：" + ", ".join(f"`{r.sheet}`（header 第 {r.header_row} 列）"
                                for r in results),
        f"- L 閾值：{length_limit} tokens",
        "",
        "## 違規統計",
        "",
        "計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），"
        "**附列計**（涉及之相異資料列數）。兩者不可互相加總。",
        "",
        "| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]
    for key in order:
        lines.append(
            f"| {key} | {check_title(key, profile)} | {counts[key]} "
            f"| {row_counts[key]} "
            f"| {CHECK_GRANULARITY[key]} | {check_status(key, profile)} |"
        )
    if profile:
        lines.insert(6, f"- profile：`{profile}`（P 採 R-1 v3；另跑 Q／R／T）")
    lines += ["",
              f"**總計：行計 {sum(counts.values())}**"
              f"（列計不加總——同一列可觸發多項檢查）",
              "", "## 明細", ""]

    for key in order:
        items = [v for r in results for v in r.violations if v.check == key]
        if not items:
            continue
        affected = len({(v.row) for v in items})
        lines += [f"### {key} — {check_title(key, profile)}"
                  f"（行計 {len(items)}／列計 {affected}）", "",
                  "| 列 | TC ID | 欄位 | 說明 | 片段 |",
                  "| ---: | --- | --- | --- | --- |"]
        for v in items:
            detail = v.detail.replace("|", "\\|")
            snippet = v.snippet.replace("|", "\\|")
            lines.append(f"| {v.row} | {v.tc_id} | {v.field} | {detail} | {snippet} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def source_sha8(path: Path) -> str:
    """來源工作簿之 sha256 前 8 碼（26 包 §C 裁定 3）。

    報告檔名自本裁定後之新產報告起採 `{tag}_{來源檔sha8}_{YYYYMMDD}`。
    **`tag` 本身不足以識別報告**：同一 feature 之兩個來源日期於同一天被
    lint，其 `{tag}_{今日}` 相同，後者靜默覆寫前者（25 上繳 §九-2 實測
    18 組）。sha8 帶回來源之身分，且它比檔名可靠 —— **檔名可以改，
    位元組不會**。

    讀不到者回 `nosha`，**不回退為空字串** —— 空字串會使檔名退回舊式而
    看起來正常，`nosha` 則在檔名上自陳其缺。
    """
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    except OSError:
        return "nosha"


def report_stem(path: Path) -> str:
    """由檔名推出報告 tag（取 SWQT_ 之後、日期之前的段）。

    **日期起首之 tag 併入 feature 名**（25 包 §D-6）：036 母本之副本檔名為
    `…_SWQT_20260817_ext.xlsx`，`SWQT_` 之後直接是日期，去日期後 tag 為
    `20260817_ext` —— **不帶任何 workbook 身分**，故 `user_profiles`／
    `time_management`／`power_moding` 三份之報告互相覆寫。
    此形態下以 `features/<name>/` 之 name 前置，使 tag 帶回身分。

    **非此形態者 tag 一律不變** —— `AMFM`／`Home`／`CFTS012_DealerMode`
    等既有八本之報告檔名須維持（G-N 之回歸向）。
    """
    stem = path.stem
    m = re.search(r"SWQT_(.+)$", stem)
    tag = m.group(1) if m else stem
    tag = re.sub(r"_\d{8}.*$", "", tag)          # 去除尾端日期與 (done)/(Refine) 註記
    tag = re.sub(r"[^\w.-]+", "_", tag).strip("_")
    if re.match(r"^\d{8}(?:[_.-]|$)", tag):
        tag = f"{_identity_dir(path)}_{tag}"
    return tag


# 通用容器目錄 —— 其名不帶 workbook 身分，取身分時跳過
_GENERIC_DIRS = {"inputs", "SWE6", "docs", "test", "data", "generated", "output", "_intake"}


def _identity_dir(path: Path) -> str:
    """日期起首之 tag 取身分用之目錄名。

    `features/<name>/…` 取 `<name>`；否則取**最近之非通用容器**祖先目錄
    （`docs/test/Dealer Mode/SWE6/x.xlsx` → `Dealer_Mode`）。
    皆無者取 `unknown` —— 不回退為空字串，否則又得到一個不帶身分之 tag。
    """
    parts = path.resolve().parts
    if "features" in parts:
        i = parts.index("features")
        if i + 1 < len(parts):
            return parts[i + 1]
    for name in reversed(parts[:-1]):
        if name not in _GENERIC_DIRS and not name.startswith("."):
            return re.sub(r"[^\w.-]+", "_", name).strip("_") or "unknown"
    return "unknown"


# --- CLI ---------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lint036.py",
        description="FM-WI-FSM-036 工作簿靜態檢查（報告模式，唯讀）",
    )
    parser.add_argument("files", metavar="FILES", nargs="+",
                        help="一個或多個 .xlsx 路徑")
    parser.add_argument("--report-dir", default="docs/fw036/lint_reports",
                        help="報告輸出目錄（預設 docs/fw036/lint_reports/）")
    parser.add_argument("--gate", action="store_true",
                        help="任一違規 exit 1（本包不啟用）")
    parser.add_argument("--json", action="store_true",
                        help="另輸出機讀 json")
    parser.add_argument("--length-limit", type=int, default=DEFAULT_LENGTH_LIMIT,
                        help=f"L 檢查 token 閾值（預設 {DEFAULT_LENGTH_LIMIT}）")
    parser.add_argument("--merge", action="store_true",
                        help="把所有 FILES 之列視為同一本簿再跑一次 I-cross —— "
                             "使比對範圍等同**交付簿**。開發期之 sandbox 分簿"
                             "會使跨簿配對逐簿比不到（PLAYBOOK (36)）。"
                             "逐簿之報告不受影響。")
    parser.add_argument("--profile", default=None, metavar="FEATURE",
                        help="feature 專屬判準：P 改採 R-1 v3，另跑 Q／R／T。"
                             "未指定時行為與既有八本之報告基線完全一致")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    report_dir = Path(args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)

    total_violations = 0
    for raw_path in args.files:
        path = Path(raw_path)
        if not path.is_file():
            print(f"錯誤：找不到檔案 {path}", file=sys.stderr)
            return 2
        results = lint_workbook(path, args.length_limit, args.profile)
        counts = count_by_check(results, args.profile)
        total_violations += sum(counts.values())

        tag = report_stem(path)
        if args.profile:
            tag = f"{tag}__{args.profile}"
        report_path = report_dir / f"{tag}_{source_sha8(path)}_{date.today():%Y%m%d}.md"
        report_path.write_text(
            render_report(path, results, args.length_limit, args.profile),
            encoding="utf-8")
        print(f"{path.name}\n  -> {report_path}")
        print("  行計 " + "  ".join(f"{k}={counts[k]}"
                                   for k in check_order(args.profile)))

        if args.json:
            json_path = report_path.with_suffix(".json")
            payload = {
                "source": str(path),
                "profile": args.profile,
                "counts": counts,
                "row_counts": rows_by_check(results, args.profile),
                "granularity": CHECK_GRANULARITY,
                "status": {k: check_status(k, args.profile)
                           for k in check_order(args.profile)},
                "sheets": [
                    {
                        "sheet": r.sheet,
                        "header_row": r.header_row,
                        "data_rows": r.data_rows,
                        "violations": [v.as_dict() for v in r.violations],
                    }
                    for r in results
                ],
            }
            json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                                 encoding="utf-8")
            print(f"  -> {json_path}")

    # --- `--merge`：跨簿之 I-cross（R-SU34 v1(d)／PLAYBOOK (36)）-------------
    if args.merge:
        if not args.profile:
            print("錯誤：--merge 須與 --profile 併用（I-cross 為 profile 專屬）",
                  file=sys.stderr)
            return 2
        pooled: list[tuple] = []
        for raw_path in args.files:
            for r in lint_workbook(Path(raw_path), args.length_limit, args.profile):
                pooled.extend(r.cross_rows)
        merged_v = check_cross(pooled)
        pairs = sorted({tuple(sorted((v.tc_id, v.detail.split("與 ")[1].split(" 之")[0])))
                        for v in merged_v if v.detail.startswith("與 ")})
        half = sorted({v.tc_id for v in merged_v if "窗未完整宣告" in v.detail})
        print(f"\n=== --merge：{len(args.files)} 簿併為一，共 {len(pooled)} 列 ===")
        print(f"  I-cross(merged) = {len(merged_v)}"
              f"（配對 {len(pairs)} 組；窗未完整宣告 {len(half)} 列）")
        for a, b in pairs:
            print(f"    · {a} ↔ {b}")
        if half:
            print("    窗未完整宣告（不參與比對，待補）：" + "、".join(half))

    if args.gate and total_violations:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
