"""產出物落點檢查（R-G64，27 包 §D-5）。

**政策自生效日管新檔** —— 故本檔之重點在基線之兩端：
基線內不紅（既有檔案不搬移），基線外照紅（G-9 範圍向）。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import lint_paths as lp  # noqa: E402


def seed(root: Path, rel: str, content: bytes = b"x") -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


# --- 落點 ---------------------------------------------------------------------

def test_conforming_paths_are_silent(tmp_path) -> None:
    seed(tmp_path, "features/power/generated/batch1.json")
    seed(tmp_path, "features/power/sandbox/b29/pm_29.xlsx")
    seed(tmp_path, "features/power/data/ledger.tsv")
    seed(tmp_path, "features/power/inputs/source.xlsx")
    assert lp.offenders(tmp_path) == []


def test_misplaced_artifact_is_flagged(tmp_path) -> None:
    seed(tmp_path, "features/bed_lowering/batches/b01.json")
    seed(tmp_path, "features/bed_lowering/workbook/bl_01.xlsx")
    found = {r[0] for r in lp.offenders(tmp_path)}
    assert found == {"features/bed_lowering/batches/b01.json",
                     "features/bed_lowering/workbook/bl_01.xlsx"}


def test_exempt_tops_are_not_artifacts(tmp_path) -> None:
    """`docs/`／`scripts/`／`output/` 非產出物目錄，其下不入本檢查。"""
    for rel in ("features/power/docs/notes.json",
                "features/power/scripts/fixture.json",
                "features/power/output/scratch.xlsx"):
        seed(tmp_path, rel)
    assert lp.offenders(tmp_path) == []


def test_baseline_grandfathers_only_what_it_lists(tmp_path) -> None:
    seed(tmp_path, "features/bed_lowering/batches/b01.json")
    baseline = tmp_path / lp.BASELINE_DEFAULT
    baseline.parent.mkdir(parents=True, exist_ok=True)
    baseline.write_text(
        "\t".join(lp.BASELINE_COLUMNS) + "\n"
        "features/bed_lowering/batches/b01.json\t.json\t既有\n", encoding="utf-8")

    listed = lp.load_baseline(baseline)
    assert [r for r in lp.offenders(tmp_path) if r[0] not in listed] == []

    seed(tmp_path, "features/bed_lowering/batches/b02.json")   # 新檔
    fresh = [r[0] for r in lp.offenders(tmp_path) if r[0] not in listed]
    assert fresh == ["features/bed_lowering/batches/b02.json"], "新檔須照紅"


# --- delivered/ 之 sha 對照（R-G64 末句）--------------------------------------

def write_manifest(root: Path, feature: str, rows: list[str]) -> None:
    path = root / "features" / feature / "delivered" / lp.MANIFEST_NAME
    path.parent.mkdir(parents=True, exist_ok=True)
    header = "filename\tsha256\tsource_path\tdelivered_round\tnote"
    path.write_text("\n".join([header, *rows]) + "\n", encoding="utf-8")


def test_delivered_sha_matches(tmp_path) -> None:
    book = seed(tmp_path, "features/power/delivered/pm_29.xlsx", b"payload")
    write_manifest(tmp_path, "power",
                   [f"pm_29.xlsx\t{lp.sha256_of(book)}\tsandbox/b29\t27\t—"])
    assert lp.check_delivered(tmp_path) == []


def test_delivered_sha_mismatch_is_red(tmp_path) -> None:
    seed(tmp_path, "features/power/delivered/pm_29.xlsx", b"payload")
    write_manifest(tmp_path, "power", ["pm_29.xlsx\t" + "0" * 64 + "\tsandbox/b29\t27\t—"])
    assert any("sha256 與對照表不符" in p for p in lp.check_delivered(tmp_path))


def test_unlisted_workbook_in_delivered_is_red(tmp_path) -> None:
    """`delivered/` 為交付定稿唯一位置——未列入對照表者即身分不明。"""
    seed(tmp_path, "features/power/delivered/stray.xlsx", b"payload")
    write_manifest(tmp_path, "power", [])
    assert any("對照表未列" in p for p in lp.check_delivered(tmp_path))


def test_manifest_row_without_file_is_red(tmp_path) -> None:
    write_manifest(tmp_path, "power", ["ghost.xlsx\t" + "0" * 64 + "\tsandbox/b29\t27\t—"])
    assert any("檔不存在" in p for p in lp.check_delivered(tmp_path))
