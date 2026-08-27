"""行首空白量化矩陣（27 包 §D-4）。

判準本體之測試在 `test_lint036.py` 之 V 段；本檔測**取樣面** ——
掃錯地方掃出來的 0，與掃過且乾淨之 0 不可分辨（G-D）。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import whitespace_matrix as wm  # noqa: E402


# --- 判準：字面案例 -----------------------------------------------------------

# `SWE1-HMI-PROF-111-china.json` 之 expected_result 實料（27 包 §D-4 唯一命中）
REAL_HIT = (
    "1. The Local vs Connected Profile screen is displayed\n"
    "2. The row list shows only:\n"
    "   a. Personalization (Presets, Menu Bar Order, App Drawer Favorites, and more)\n"
    "   b. App Store Download\n"
    "   c. Marketplace (Access to Marketplace)\n"
    "   and no Connected Navigation row is present"
)


def test_real_corpus_hit_is_caught() -> None:
    """續行之 3 格縮排非 §6.1 子層記法，照紅 —— 其 a./b./c. 三行則否。"""
    assert wm.scan_text(REAL_HIT) == "leading"


def test_clean_cell_passes() -> None:
    assert wm.scan_text(
        "1. The screen is displayed\n2. The row list shows only two rows") is None


def test_in_11_exemptions_pass() -> None:
    assert wm.scan_text("1. Press the button\n   a. Hold for 3 s") is None
    assert wm.scan_text("1. Press the button\n      - the LED turns on") is None
    assert wm.scan_text("1. Run the tool\n   $ adb shell dumpsys") is None


def test_whitespace_only_line_is_caught() -> None:
    assert wm.scan_text("1. Idle state\n   \n2. Ignition On") == "blank"


# --- 取樣面：TC 列之定位 ------------------------------------------------------

def test_records_are_found_behind_an_earlier_list_of_dicts(tmp_path) -> None:
    """`outline` 在 `tcs` 之前且同為 dict 之 list —— 取首者會掃錯地方。

    此即 `SWE1-HMI-PROF-111-china.json` 之實際結構；修前該檔回報 0 命中。
    """
    payload = {
        "outline": [{"node": "A", "label": "Local vs Connected"}],
        "tcs": [{"tc_id": "T-1", "expected_result": REAL_HIT}],
    }
    path = tmp_path / "leaf.json"
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    status, rows, hits, note = wm.scan_json(path)
    assert (status, rows, note) == ("已掃", 1, "")
    assert hits["er"] == 1


def test_top_level_list_payload_is_found(tmp_path) -> None:
    path = tmp_path / "batch.json"
    path.write_text(json.dumps([{"test_procedure": "1. Press\n  2. Release"}]),
                    encoding="utf-8")
    status, rows, hits, _ = wm.scan_json(path)
    assert (status, rows, hits["proc"]) == ("已掃", 1, 1)


def test_non_corpus_file_is_marked_unscanned_not_zero(tmp_path) -> None:
    """G-D：無 TC 列者標 `未掃`，不得以 0 命中呈現。"""
    path = tmp_path / "meta.json"
    path.write_text(json.dumps({"batch": 12, "note": "配置檔"}), encoding="utf-8")
    status, rows, hits, note = wm.scan_json(path)
    assert status == "未掃" and rows == 0 and not hits and note


def test_unscanned_row_reports_未掃_in_every_field_column() -> None:
    from collections import Counter
    row = wm.row_of("json", "x.json", "未掃", 0, Counter(), "無 TC 列")
    cells = row.split("\t")
    assert cells[4:4 + len(wm.FIELDS)] == ["未掃"] * len(wm.FIELDS)
    assert cells[4 + len(wm.FIELDS)] == "未掃", "合計欄同樣不得以 0 代"
