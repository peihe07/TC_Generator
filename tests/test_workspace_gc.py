"""清理候選（R-G65，27 包 §D-6）。**本工具不刪檔** —— 測其列與判，不測刪。"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import workspace_gc as gc  # noqa: E402


def seed(root: Path, rel: str, text: str = "x") -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


# --- 候選之列舉 ---------------------------------------------------------------

def test_lower_versions_of_a_family_are_candidates(tmp_path) -> None:
    for n in (1, 2, 3):
        seed(tmp_path, f"features/power/generated/batch_v{n}.json")
    found = {p.name: r for p, r in gc.candidates_of(tmp_path, "power")}
    assert set(found) == {"batch_v1.json", "batch_v2.json"}, "最高版須留"
    assert "batch_v3.json" in found["batch_v1.json"]


def test_single_version_is_not_a_candidate(tmp_path) -> None:
    """`_v1` 沒有 `_v2` 就不是「被新版取代」—— 版本記法本身不是作廢證據。"""
    seed(tmp_path, "features/power/generated/batch_v1.json")
    assert gc.candidates_of(tmp_path, "power") == []


def test_dead_marker_in_name_is_a_candidate(tmp_path) -> None:
    seed(tmp_path, "features/power/data/SUPERSEDED_47_maps.md")
    assert [p.name for p, _ in gc.candidates_of(tmp_path, "power")] \
        == ["SUPERSEDED_47_maps.md"]


def test_output_dir_is_out_of_scope(tmp_path) -> None:
    """`output/` 不入版控 —— 移除無歸檔，故不由本條授權（FO R-G26 註）。"""
    seed(tmp_path, "features/power/output/SUPERSEDED_old.json")
    assert gc.candidates_of(tmp_path, "power") == []


# --- 引用懸空檢查 -------------------------------------------------------------

def test_referenced_candidate_is_kept(tmp_path) -> None:
    seed(tmp_path, "features/power/data/SUPERSEDED_47_maps.md")
    seed(tmp_path, "features/power/RULINGS.md",
         "見 `features/power/data/SUPERSEDED_47_maps.md` 之對照。\n")
    assert "SUPERSEDED_47_maps.md" in gc.index_references(tmp_path)


def test_unreferenced_candidate_is_removable(tmp_path) -> None:
    seed(tmp_path, "features/power/data/SUPERSEDED_47_maps.md")
    seed(tmp_path, "features/power/RULINGS.md", "本條不指名任何檔。\n")
    assert gc.index_references(tmp_path) == {}


def test_dangling_reference_is_named(tmp_path) -> None:
    seed(tmp_path, "features/power/ANOMALIES.md", "素材 `SYS2_VF230.xlsx` 未到。\n")
    assert [n for n, _ in gc.dangling(tmp_path, gc.index_references(tmp_path))] \
        == ["SYS2_VF230.xlsx"]


def test_file_under_output_is_not_reported_dangling(tmp_path) -> None:
    """`output/` 不入版控，但檔在盤上 —— 其引用非懸空。"""
    seed(tmp_path, "features/privacy/output/x2.xlsx")
    seed(tmp_path, "features/privacy/RULINGS.md",
         "對 `features/privacy/output/x2.xlsx` 之處置。\n")
    assert gc.dangling(tmp_path, gc.index_references(tmp_path)) == []


def test_slash_shorthand_fragment_is_not_a_filename(tmp_path) -> None:
    """`gen_batch04/05/06.py` 為簡寫，其 `06.py` 不是一個檔名。"""
    seed(tmp_path, "features/power/ANOMALIES.md",
         "僅見於 `gen_batch04/05/06.py` 三個產生器。\n")
    assert gc.dangling(tmp_path, gc.index_references(tmp_path)) == []
