"""Excel writer for generated TC results (RULES.md §10.3)."""
import os
import re
from copy import copy

from openpyxl import load_workbook
from openpyxl.styles import Alignment

TC_SHEET_NAME = "Test Case Specification&Result"
FRAMEWORK_SHEET_NAME = "Test Case Framework"

# Column mapping: field name -> 1-based column index
WRITE_COLUMNS = {
    "tc_id": 6,           # F
    "test_group": 7,      # G
    "test_set": 8,        # H
    "pre_conditions": 10, # J
    "input_test_data": 11,# K
    "test_procedure": 12, # L
    "expected_result": 13,# M
    "spec_reference": 14, # N
    "priority": 16,       # P
    "design_method": 17,  # Q
}

WRAP_TEXT_ALIGNMENT = Alignment(wrap_text=True, vertical="top")
CLEARABLE_FIELDS = {"test_set", "spec_reference"}


def _merge_test_item_text(existing_text: str | None, rewrite: str) -> str:
    """Preserve the original test item text while replacing any older rewrite."""
    original = existing_text or ""
    if "\n\n" in original:
        original = original.split("\n\n", 1)[0]
    return f"{original}\n\n{rewrite}"


# Suffixes that OS file managers append when duplicating a file. We strip
# these before tagging "_generated.xlsx" so the output filename stays clean
# and the `..._SWQT_{TestGroup}_{date}` pattern survives for re-import.
# Order matters: more specific patterns first so e.g. "bar - Copy" strips
# the whole " - Copy" (not just " Copy" leaving a dangling hyphen).
_DUPLICATE_SUFFIX_PATTERNS = [
    re.compile(r"\s*-\s*copy(?:\s*\(\d+\))?$", re.I),  # Windows: "foo - Copy" / "foo - Copy (2)"
    re.compile(r"\s*拷貝(?:\s*\d+)?$"),                 # macOS 繁中: "foo 拷貝" / "foo 拷貝 2"
    re.compile(r"\s*的副本(?:\s*\d+)?$"),                # macOS 簡中: "foo 的副本"
    re.compile(r"\s*copy(?:\s*\d+)?$", re.I),           # macOS 英文: "foo copy" / "foo copy 2"
    re.compile(r"\s*\(\d+\)$"),                         # 通用: "foo (2)"
]


def _clean_basename(basename: str) -> str:
    """Strip common OS "duplicate file" suffixes (拷貝 / copy / (2)) off the tail."""
    cleaned = basename
    while True:
        before = cleaned
        for pattern in _DUPLICATE_SUFFIX_PATTERNS:
            cleaned = pattern.sub("", cleaned)
        cleaned = cleaned.rstrip()
        if cleaned == before:
            return cleaned


def build_output_path(input_path: str, output_dir: str | None = None) -> str:
    """Build output file path: {input_filename}_generated.xlsx"""
    dirname = output_dir or os.path.dirname(input_path)
    basename = os.path.splitext(os.path.basename(input_path))[0]
    basename = _clean_basename(basename)
    return os.path.join(dirname, f"{basename}_generated.xlsx")


_TEMPLATE_CARRY_COLUMNS = (3, 4, 9)  # C: Polarion ID, D: Req ID, I: Test Item


def _has_value(cell) -> bool:
    v = cell.value
    return v is not None and str(v).strip() != ""


def _copy_style(src, dst) -> None:
    """從 src cell 複製字體/填色/對齊/邊框到 dst cell（樣式物件需 copy 避免共享）。"""
    if src.has_style:
        dst.font = copy(src.font)
        dst.fill = copy(src.fill)
        dst.border = copy(src.border)
        dst.alignment = copy(src.alignment)
        dst.number_format = src.number_format
        dst.protection = copy(src.protection)


def _write_tc_row(
    ws,
    row_num: int,
    row_data: dict,
    selected_fields: set[str] | None,
    append_rewrite: bool,
    rewritten_req_ids: set[str] | None = None,
) -> None:
    """把單一 TC 的資料寫到指定的 Excel 列。

    `rewritten_req_ids` 是「本次 write session 已經在哪些 req_id 上 append 過 rewrite」
    的集合；傳入後同一個 req_id 只會 append 一次（跨列 dedup）。
    """
    for field, col_idx in WRITE_COLUMNS.items():
        if selected_fields is not None and field not in selected_fields:
            continue
        if field not in row_data:
            continue

        value = row_data.get(field)
        cell = ws.cell(row=row_num, column=col_idx)
        has_value = value is not None and str(value).strip() != ""

        if has_value:
            cell.value = value
            cell.alignment = WRAP_TEXT_ALIGNMENT
        elif field in CLEARABLE_FIELDS:
            cell.value = None
            cell.alignment = WRAP_TEXT_ALIGNMENT
        # else: 空值且非 clearable 欄 → 保留 template 既有內容，不覆蓋。

    if append_rewrite:
        rewrite = row_data.get("test_item_rewrite")
        req_id = (row_data.get("req_id") or "").strip()
        already_done = rewritten_req_ids is not None and req_id in rewritten_req_ids
        if (
            rewrite
            and (selected_fields is None or "test_item_rewrite" in selected_fields)
            and not already_done
        ):
            cell_i = ws.cell(row=row_num, column=9)
            cell_i.value = _merge_test_item_text(cell_i.value, rewrite)
            cell_i.alignment = WRAP_TEXT_ALIGNMENT
            if rewritten_req_ids is not None and req_id:
                rewritten_req_ids.add(req_id)


def write_generated_results(
    input_path: str,
    generated_rows: list[dict],
    output_path: str,
    selected_fields: set[str] | None = None,
) -> None:
    """
    Write generated TC results back to xlsx.

    Preserves all original formatting. Only writes to specified columns.
    Col I (Test Item) gets rewrite appended, not overwritten.

    若多筆 generated_rows 指向同一個 row_num（AI 把一個 requirement 拆成 N 筆 TC），
    會在原列下方 `insert_rows` 補 N-1 列、複製 C/D/I 等欄位，再把每筆 TC 各自寫入。
    """
    wb = load_workbook(input_path)
    ws = wb[TC_SHEET_NAME]

    # 依 row_num 分組，保留原本傳入順序；row_num 為 None 的項目丟到尾端維持相容。
    groups: dict[int, list[dict]] = {}
    order: list[int] = []
    orphans: list[dict] = []
    for row_data in generated_rows:
        rn = row_data.get("row_num")
        if not rn:
            orphans.append(row_data)
            continue
        if rn not in groups:
            groups[rn] = []
            order.append(rn)
        groups[rn].append(row_data)

    rewritten_req_ids: set[str] = set()

    # 由上而下處理 row_num 以保留原始順序（尤其影響 rewrite dedup 的先後）。
    # 插列會讓後續列位移，所以維護一個累積 offset 套用到後面的 target row。
    cumulative_offset = 0
    for row_num in sorted(order):
        items = groups[row_num]
        extras = len(items) - 1
        base_row = row_num + cumulative_offset

        if extras > 0:
            # 在原列下方插入 N-1 列，並把 template 的 C/D/I 欄位複製過去，
            # 這樣每筆 split 出來的 TC 都能對應正確的 req_id / test_item 文字。
            ws.insert_rows(base_row + 1, amount=extras)
            for offset in range(1, extras + 1):
                for col in _TEMPLATE_CARRY_COLUMNS:
                    src = ws.cell(row=base_row, column=col)
                    dst = ws.cell(row=base_row + offset, column=col)
                    dst.value = src.value
                    _copy_style(src, dst)

        for idx, row_data in enumerate(items):
            _write_tc_row(
                ws,
                row_num=base_row + idx,
                row_data=row_data,
                selected_fields=selected_fields,
                append_rewrite=True,
                rewritten_req_ids=rewritten_req_ids,
            )

        cumulative_offset += extras

    # row_num 不明的退回舊行為：直接寫末尾，不插列。
    if orphans:
        append_start = ws.max_row + 1
        for i, row_data in enumerate(orphans):
            _write_tc_row(
                ws,
                row_num=append_start + i,
                row_data=row_data,
                selected_fields=selected_fields,
                append_rewrite=True,
                rewritten_req_ids=rewritten_req_ids,
            )

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    wb.save(output_path)
    wb.close()


def write_framework_sheet(
    input_path: str,
    framework_data: list[dict],
    output_path: str,
) -> None:
    """
    Populate the Test Case Framework sheet.

    Columns: A=Test Group, B=Test Set, C=TC Count, D=Req Count.

    TC Count = 匯出到該 test set 的 TC 筆數（一個 req 被拆多筆時每筆各算 1）。
    Req Count = 原始 requirement 數（同一 req 的多筆拆分只算一次）。
    為了向後相容，若 entry 只帶 `req_count` 會當作同時是 TC 與 Req 數。
    """
    wb = load_workbook(input_path)

    if FRAMEWORK_SHEET_NAME not in wb.sheetnames:
        wb.create_sheet(FRAMEWORK_SHEET_NAME)
    ws = wb[FRAMEWORK_SHEET_NAME]

    # Write header
    ws.cell(row=1, column=1, value="Test Group")
    ws.cell(row=1, column=2, value="Test Set")
    ws.cell(row=1, column=3, value="TC Count")
    ws.cell(row=1, column=4, value="Req Count")

    # Write data
    for i, entry in enumerate(framework_data):
        row = i + 2
        ws.cell(row=row, column=1, value=entry["test_group"])
        ws.cell(row=row, column=2, value=entry["test_set"])
        tc_count = entry.get("tc_count", entry.get("req_count", 0))
        req_count = entry.get("req_count", tc_count)
        ws.cell(row=row, column=3, value=tc_count)
        ws.cell(row=row, column=4, value=req_count)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    wb.save(output_path)
    wb.close()
