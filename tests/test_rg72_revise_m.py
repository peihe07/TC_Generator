"""`scripts/rg72_revise_m.py` 之替換語意（GC-13 審閱 二：加同格重複 edit 測試）。

首版之 bug：同一格內同一 `(old, new)` 被 dry-run 表列多次時，逐列套用 ——
第一次已把該格全部出現處換掉，第二次遂找不到而誤判 miss，整批中止。
現行語意為**每格去重後以「出現次數」為單位替換**。
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

_spec = importlib.util.spec_from_file_location(
    "rg72_revise_m", ROOT / "scripts" / "rg72_revise_m.py")
rg72 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rg72)


def write_plan(tmp_path: Path, rows: list[dict]) -> Path:
    import csv
    p = tmp_path / "plan.tsv"
    cols = ["sheet", "row", "col", "tc_id", "rule", "old_text", "new_text", "mechanical"]
    with p.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    return p


def test_duplicate_edit_in_one_cell_is_deduped(tmp_path: Path) -> None:
    """同一 (old, new) 列兩次 → 計畫只收一份，不因第二次找不到而中止。"""
    plan = write_plan(tmp_path, [
        dict(sheet="S", row="10", col="12", tc_id="T-1", rule="r",
             old_text="A", new_text="B", mechanical="Y"),
        dict(sheet="S", row="10", col="12", tc_id="T-1", rule="r",
             old_text="A", new_text="B", mechanical="Y"),
    ])
    loaded = rg72.load_plan(plan)
    edits = loaded[("S", 10, 12)]
    assert len(edits) == 2, "load_plan 保留原始列（去重在 apply 時做）"
    assert len({(o, n) for o, n, _, _ in edits}) == 1


def test_non_mechanical_rows_are_not_in_the_plan(tmp_path: Path) -> None:
    """`mechanical=N`（X-nav／bare-$）不入 Revise-M（R-G72(g)）。"""
    plan = write_plan(tmp_path, [
        dict(sheet="S", row="10", col="12", tc_id="T-1", rule="x-nav",
             old_text="A", new_text="", mechanical="N"),
    ])
    assert rg72.load_plan(plan) == {}


def test_result_columns_are_the_protected_range() -> None:
    """結果欄 Y–AH ＝ 1-based 25–34；回修不得觸及（R-G72(c)）。"""
    assert list(rg72.RESULT_COLS) == list(range(25, 35))
