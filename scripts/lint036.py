#!/usr/bin/env python3
"""FM-WI-FSM-036 工作簿靜態檢查（報告模式）。

檢查 A–N 之定義見 docs/fw036/handoff/00_lint_spec.md。
本工具唯讀開啟 xlsx，絕不寫回任何 xlsx。

gate 政策（S3）：`--gate` 旗標保留但**尚不啟用**。啟用時機為尾批
（全數回修完成後）；現階段啟用將使所有既有交付本 exit 1，阻斷正常
作業。裁決條文見 docs/fw036/RULINGS_LEDGER.md。
"""

from __future__ import annotations

import argparse
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
RE_H = re.compile(r"\b(as expected|works? normally|normal(ly)? operation)\b", re.I)
RE_PAREN_LINE = re.compile(r"^\(.+\)$")
RE_PAREN_TAIL = re.compile(r"\([^)]{3,}\)\s*$")
RE_CJK = re.compile(r"[一-鿿]")
RE_TOKEN = re.compile(r"[A-Za-z0-9$_.'\"-]+")
RE_TRAILING_PERIOD = re.compile(r"[.。]$")
# 舊式 CAN 兩段記法 `MESSAGE.Signal`（message 段全大寫）。
# 內部訊號 `TLM_Status.Info`／`Phone_Call.Info` 之 message 段含小寫，不命中。
RE_P_LEGACY_CAN = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\b")
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
    "C": "hedge (test_item)",
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
    "P": "訊號記法未用三件組",
}

# 校準狀態（00c 最終版）：M、J 經全語料分佈補校，改標已校準
CHECK_STATUS = {
    "A": "已校準", "B": "已校準", "C": "已校準", "D": "已校準",
    "E": "已校準", "F": "已校準", "G": "已校準（詞彙表外值待接入）",
    "H": "已校準", "I": "已校準", "I-sibling": "未校準（M15）",
    "J": "已校準（行計口徑）", "K": "已校準（分級待 R-5）",
    "L": "已校準（閾值待 R-3）", "M": "已校準", "N": "已校準",
    "P": "已校準（PM 批 1：41→0）",
}
CHECK_ORDER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "I-sibling",
               "J", "K", "L", "M", "N", "P"]

# 各檢查之記錄粒度（報告表頭「行計」欄之語意）
CHECK_GRANULARITY = {
    "A": "每次命中", "B": "每次命中", "C": "每次命中",
    "D": "每次命中／每編號行", "E": "每列", "F": "每次命中",
    "G": "每列", "H": "每次命中", "I": "每列", "I-sibling": "每列",
    "J": "每行", "K": "每列每欄", "L": "每列", "M": "每列每欄", "N": "每行",
    "P": "每次命中",
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
              length_limit: int) -> list[Violation]:
    """對單列跑 A–N（除 I-sibling 外）之檢查。"""
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

    # C hedge
    for m in RE_C.finditer(item):
        add("C", "test_item", f"hedge {m.group(0)!r}", snippet_of(item, m.start()))

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

    # F 方括號
    for m in RE_F.finditer(proc):
        add("F", "proc", f"方括號佔位 {m.group(0)!r}", snippet_of(proc, m.start()))

    # G Test Set 空值
    if not fields["test_set"].strip():
        add("G", "test_set", "Test Set 為空", "")

    # H ER 模糊
    for m in RE_H.finditer(er):
        add("H", "er", f"模糊語 {m.group(0)!r}", snippet_of(er, m.start()))

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

    # P 訊號記法（R-1；範圍依 R-6）
    for key in P_FIELDS:
        for m in RE_P_LEGACY_CAN.finditer(fields[key]):
            add("P", key, f"舊式兩段記法 {m.group(0)!r}",
                snippet_of(fields[key], m.start()))
    for line in paren_lines(item):                    # test_item 括號下半
        for m in RE_P_LEGACY_CAN.finditer(line):
            add("P", "test_item(括號下半)",
                f"舊式兩段記法 {m.group(0)!r}", line[:80])

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


# --- 工作簿層 ----------------------------------------------------------------


def lint_workbook(path: Path, length_limit: int = DEFAULT_LENGTH_LIMIT
                  ) -> list[SheetResult]:
    """唯讀開啟工作簿，對每個 TC sheet 跑檢查。"""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        results: list[SheetResult] = []
        for sheet_name in wb.sheetnames:
            if not sheet_name.startswith(TC_SHEET_PREFIX):
                continue
            results.append(lint_sheet(wb[sheet_name], length_limit))
        if not results:
            raise ValueError(f"{path.name}：找不到以 {TC_SHEET_PREFIX!r} 開頭之 sheet")
        return results
    finally:
        wb.close()


def lint_sheet(ws, length_limit: int) -> SheetResult:
    """單一 sheet 的檢查流程。"""
    header_row = find_header_row(ws)
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    columns = build_column_map(list(rows[header_row - 1]))
    missing = [k for k in FIELD_HEADERS if k not in columns]
    if missing:
        raise ValueError(f"sheet {ws.title!r} 缺欄位：{missing}")

    result = SheetResult(sheet=ws.title, header_row=header_row, data_rows=0)
    sibling_input: list[tuple[int, str, str, str]] = []

    for offset, raw in enumerate(rows[header_row:], start=header_row + 1):
        fields = {key: cell_text(raw[idx]) if idx < len(raw) else ""
                  for key, idx in columns.items() if key in FIELD_HEADERS}
        if not any(fields[k].strip() for k in ("test_item", "proc", "er")):
            continue
        tc_id = cell_text(raw[columns["tc_id"]]) if "tc_id" in columns else ""
        req_id = cell_text(raw[columns["req_id"]]) if "req_id" in columns else ""
        result.data_rows += 1
        result.violations.extend(check_row(fields, offset, tc_id, length_limit))
        sibling_input.append((offset, tc_id, req_id, fields["test_item"]))

    result.violations.extend(check_sibling_parens(sibling_input))
    result.violations.sort(key=lambda v: (CHECK_ORDER.index(v.check), v.row))
    return result


def count_by_check(results: list[SheetResult]) -> dict[str, int]:
    """彙總各檢查之行計（違規記錄數）。"""
    counts = {key: 0 for key in CHECK_ORDER}
    for result in results:
        for violation in result.violations:
            counts[violation.check] += 1
    return counts


def rows_by_check(results: list[SheetResult]) -> dict[str, int]:
    """彙總各檢查之列計（涉及之相異資料列數）。"""
    seen: dict[str, set[tuple[str, int]]] = {key: set() for key in CHECK_ORDER}
    for result in results:
        for violation in result.violations:
            seen[violation.check].add((result.sheet, violation.row))
    return {key: len(value) for key, value in seen.items()}


# --- 報告輸出 ----------------------------------------------------------------


def render_report(path: Path, results: list[SheetResult], length_limit: int) -> str:
    """產生 markdown 報告。"""
    counts = count_by_check(results)
    row_counts = rows_by_check(results)
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
    for key in CHECK_ORDER:
        lines.append(
            f"| {key} | {CHECK_TITLES[key]} | {counts[key]} | {row_counts[key]} "
            f"| {CHECK_GRANULARITY[key]} | {CHECK_STATUS[key]} |"
        )
    lines += ["",
              f"**總計：行計 {sum(counts.values())}**"
              f"（列計不加總——同一列可觸發多項檢查）",
              "", "## 明細", ""]

    for key in CHECK_ORDER:
        items = [v for r in results for v in r.violations if v.check == key]
        if not items:
            continue
        affected = len({(v.row) for v in items})
        lines += [f"### {key} — {CHECK_TITLES[key]}"
                  f"（行計 {len(items)}／列計 {affected}）", "",
                  "| 列 | TC ID | 欄位 | 說明 | 片段 |",
                  "| ---: | --- | --- | --- | --- |"]
        for v in items:
            detail = v.detail.replace("|", "\\|")
            snippet = v.snippet.replace("|", "\\|")
            lines.append(f"| {v.row} | {v.tc_id} | {v.field} | {detail} | {snippet} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def report_stem(path: Path) -> str:
    """由檔名推出報告 tag（取 SWQT_ 之後、日期之前的段）。"""
    stem = path.stem
    m = re.search(r"SWQT_(.+)$", stem)
    tag = m.group(1) if m else stem
    tag = re.sub(r"_\d{8}.*$", "", tag)          # 去除尾端日期與 (done)/(Refine) 註記
    tag = re.sub(r"[^\w.-]+", "_", tag).strip("_")
    return tag


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
        results = lint_workbook(path, args.length_limit)
        counts = count_by_check(results)
        total_violations += sum(counts.values())

        tag = report_stem(path)
        report_path = report_dir / f"{tag}_{date.today():%Y%m%d}.md"
        report_path.write_text(render_report(path, results, args.length_limit),
                               encoding="utf-8")
        print(f"{path.name}\n  -> {report_path}")
        print("  行計 " + "  ".join(f"{k}={counts[k]}" for k in CHECK_ORDER))

        if args.json:
            json_path = report_path.with_suffix(".json")
            payload = {
                "source": str(path),
                "counts": counts,
                "row_counts": rows_by_check(results),
                "granularity": CHECK_GRANULARITY,
                "status": CHECK_STATUS,
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

    if args.gate and total_violations:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
