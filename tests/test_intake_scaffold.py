"""Tests for scripts/intake.py scaffold — which requirement report wins.

The defect these pin: scaffold() wrote `a03_report` once per swra_report, so
with two present the last one in sorted order won. That is a coin flip, and
it is free to disagree with the Scope arbitration the INTAKE report just
printed. AM/FM has exactly that shape (SWRA-A02 vs the SWE1 037-A03), and it
landed on the right file only because "S" sorts after "F".
"""
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location(
    "tc_intake", ROOT / "scripts" / "intake.py")
if _spec is None or _spec.loader is None:
    pytest.skip("scripts/intake.py not present", allow_module_level=True)
intake = importlib.util.module_from_spec(_spec)
sys.modules["tc_intake"] = intake
_spec.loader.exec_module(intake)


FEATURE_YAML = '''feature: "AMFM"

paths:
  workbook: "inputs/<workbook xlsx>"
  a03_report: "inputs/<037 A03 xlsx>"
  sys1_export: "inputs/<export xlsx>"
  spec_pdf: "inputs/<spec pdf>"
  popup_list: "inputs/<Pop Up List xlsx>"

spec_mode: "A"
'''


def make_drop(tmp_path, names_and_kinds):
    """Build a _intake/<F>/ drop folder plus a scaffolded feature dir."""
    folder = tmp_path / "_intake" / "AMFM"
    folder.mkdir(parents=True)
    files = []
    for name, kind in names_and_kinds:
        (folder / name).write_text("x", encoding="utf-8")
        files.append({"file": name, "kind": kind, "note": ""})
    feat = tmp_path / "features" / "amfm"
    (feat / "inputs").mkdir(parents=True)
    (feat / "feature.yaml").write_text(FEATURE_YAML, encoding="utf-8")
    return folder, files, feat


def a03_line(feat):
    text = (feat / "feature.yaml").read_text(encoding="utf-8")
    return next(l for l in text.splitlines() if l.strip().startswith("a03_report:"))


def test_the_scope_designated_report_wins_over_sort_order(tmp_path):
    """The pick must win even when it sorts FIRST — the old code would have
    let the later file overwrite it."""
    folder, files, feat = make_drop(tmp_path, [
        ("AAA-SWRA-A02.xlsx", "swra_report"),
        ("ZZZ-037-A03.xlsx", "swra_report"),
    ])
    intake.scaffold("AMFM", folder, files, "D", tmp_path,
                    a03_pick=files[0])
    assert "AAA-SWRA-A02.xlsx" in a03_line(feat)


def test_the_scope_designated_report_wins_when_it_sorts_last(tmp_path):
    folder, files, feat = make_drop(tmp_path, [
        ("AAA-SWRA-A02.xlsx", "swra_report"),
        ("ZZZ-037-A03.xlsx", "swra_report"),
    ])
    intake.scaffold("AMFM", folder, files, "D", tmp_path,
                    a03_pick=files[1])
    assert "ZZZ-037-A03.xlsx" in a03_line(feat)


def test_a_contested_choice_is_annotated_for_tier_2(tmp_path):
    folder, files, feat = make_drop(tmp_path, [
        ("AAA-SWRA-A02.xlsx", "swra_report"),
        ("ZZZ-037-A03.xlsx", "swra_report"),
    ])
    intake.scaffold("AMFM", folder, files, "D", tmp_path, a03_pick=files[1])
    text = (feat / "feature.yaml").read_text(encoding="utf-8")
    assert "CONFIRM (Tier 2): 2 requirement reports" in text
    assert "#   inputs/AAA-SWRA-A02.xlsx" in text, "the loser must be named"


def test_a_single_report_is_written_without_an_annotation(tmp_path):
    folder, files, feat = make_drop(tmp_path, [
        ("only-037.xlsx", "swra_report"),
    ])
    intake.scaffold("AMFM", folder, files, "D", tmp_path, a03_pick=files[0])
    text = (feat / "feature.yaml").read_text(encoding="utf-8")
    assert "only-037.xlsx" in a03_line(feat)
    assert "CONFIRM" not in text


def test_other_path_keys_still_fill(tmp_path):
    folder, files, feat = make_drop(tmp_path, [
        ("wb.xlsx", "workbook"),
        ("only-037.xlsx", "swra_report"),
        ("export.xlsx", "polarion_export"),
    ])
    intake.scaffold("AMFM", folder, files, "D", tmp_path, a03_pick=files[1])
    text = (feat / "feature.yaml").read_text(encoding="utf-8")
    assert 'workbook: "inputs/wb.xlsx"' in text
    assert 'sys1_export: "inputs/export.xlsx"' in text
    assert 'spec_mode: "D"' in text


def test_unclassified_files_are_left_in_the_drop_folder(tmp_path):
    """RULINGS.md is human-authored and must not be swept into inputs/."""
    folder, files, feat = make_drop(tmp_path, [
        ("only-037.xlsx", "swra_report"),
        ("RULINGS.md", "unclassified"),
    ])
    intake.scaffold("AMFM", folder, files, "D", tmp_path, a03_pick=files[0])
    assert (folder / "RULINGS.md").exists()
    assert not (feat / "inputs" / "RULINGS.md").exists()


# --- sources/ 讀取路徑（R-G66，27 包 §D-7）-----------------------------------

def _sources_root(tmp_path, doc_id: str, name: str, payload: bytes):
    import hashlib
    raw = tmp_path / "sources" / "raw" / doc_id
    raw.mkdir(parents=True)
    (raw / name).write_bytes(payload)
    sha = hashlib.sha256(payload).hexdigest()
    (tmp_path / "sources" / "MANIFEST.tsv").write_text(
        "doc_id\tfilename\tsha256\tversion\tfeatures\tnote\n"
        f"{doc_id}\t{name}\t{sha}\t—\t—\t—\n", encoding="utf-8")
    return sha


def test_sources_ref_hits_on_matching_sha(tmp_path):
    _sources_root(tmp_path, "DD_2026", "dd.xlsx", b"payload")
    assert intake.sources_ref(tmp_path, "dd.xlsx") == "sources/raw/DD_2026/dd.xlsx"


def test_sources_ref_misses_when_content_differs(tmp_path):
    """同名而內容不同者不算命中 —— 否則會把 feature 指向另一份文件。"""
    _sources_root(tmp_path, "DD_2026", "dd.xlsx", b"payload")
    (tmp_path / "sources" / "raw" / "DD_2026" / "dd.xlsx").write_bytes(b"changed")
    assert intake.sources_ref(tmp_path, "dd.xlsx") is None


def test_sources_ref_returns_none_without_manifest(tmp_path):
    """既有 feature 之舊路徑 fallback —— 無 manifest 時行為與本輪之前相同。"""
    assert intake.sources_ref(tmp_path, "dd.xlsx") is None
