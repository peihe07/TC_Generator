"""量測產出排除集（R-G16 補充）。

此規則在 GC 系列犯過兩次（`up/20260905_GC-02.md` 9-3、`up/20260905_GC-03.md` 9-4），
兩次都是「腳本把自己剛寫出的表當成母體」。案例以**字面**釘入（G-N）：
下列檔名即當時實際造成錯值者。
"""
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from measure_common import MEASUREMENT_OUTPUT_GLOBS, is_measurement_output


@pytest.mark.parametrize("rel", [
    "docs/reports/rg_refs_20260905.tsv",            # GC-03 9-4：母體膨脹 2620 -> 8574
    "docs/reports/lint_reports_refs_20260905.tsv",  # GC-02 9-3：可移除 81 -> 0
    "docs/reports/source_identity_20260905.tsv",
    "docs/reports/binding_diff_comfort_1.tsv",
    "docs/reports/binding_hits_20260905.tsv",
])
def test_known_measurement_outputs_are_excluded(rel):
    assert is_measurement_output(rel)


@pytest.mark.parametrize("rel", [
    "docs/fw036/RULINGS_LEDGER.md",
    "docs/fw036/RULINGS.sha.tsv",        # 指紋表是治理產物，不是量測產出
    "docs/fw036/DELIVERY_SPEC_BASELINE.tsv",
    "features/vsm_v43/data/signal_chain_v43.tsv",
    "docs/reports/whitespace_matrix.tsv",  # 無日期尾綴，不在排除集內
])
def test_non_measurement_files_are_not_excluded(rel):
    """範圍向（R-G9）：排除集不得過寬，否則會把治理檔一併掃掉。"""
    assert not is_measurement_output(rel)


def test_canon_refs_uses_the_shared_exclusion():
    """使用處：`canon_refs.in_scan_surface` 必須走同一支，不得自帶副本。"""
    spec = importlib.util.spec_from_file_location("tc_cr_x", ROOT / "scripts" / "canon_refs.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["tc_cr_x"] = mod          # dataclass 解析註記時需自 sys.modules 找回本模組
    spec.loader.exec_module(mod)
    assert mod.is_measurement_output is is_measurement_output
    assert not mod.in_scan_surface(Path("docs/reports/rg_refs_20260905.tsv"))


def test_globs_are_anchored_to_docs_reports():
    """排除集只管 `docs/reports/`，不得誤及他處之同名樣式。"""
    assert all(g.startswith("docs/reports/") for g in MEASUREMENT_OUTPUT_GLOBS)
    assert not is_measurement_output("features/f/reports/x_20260905.tsv")
