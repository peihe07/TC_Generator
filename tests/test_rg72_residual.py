"""`scripts/rg72_residual.py` 之分類語意（GC-14 審閱 二：未知 detail → unclassified）。

分類表為**白名單式**：只認已知之 lint detail，其餘一律 `unclassified`。
`unclassified` 出現即擋出貨（R-G72(h)）—— 其價值在於
**新增之 lint 檢查不會被靜默歸入「其餘」而通過出貨條件**。

GC-14 上繳 7-2 之自報：三本實測 `unclassified` 為 0，
但該 0 是「目前四類已涵蓋」而非「不可能有第五類」。本檔即釘住該語意。
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

_spec = importlib.util.spec_from_file_location(
    "rg72_residual", ROOT / "scripts" / "rg72_residual.py")
res = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(res)


KNOWN = [
    ("bare-$",  "v3 記法殘留（R-G70(h)：`$` 包覆式已撤銷）'$MSG.Sig$'"),
    ("ReviseC", "Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴（R-1 v2(a)）"),
    ("ReviseC", "賦值未寫成 `<MSG>.<Sig> = <raw> (<label>)`：'X.Y = 1'"),
    ("ReviseC", "PROXI 行形態不合 R-G70 v4.1 之標準式亦非既知舊式"),
]


@pytest.mark.parametrize("expected,detail", KNOWN,
                         ids=[d[:24] for _, d in KNOWN])
def test_known_details_are_classified(expected, detail) -> None:
    klass, dest = res.classify(detail)
    assert klass == expected
    assert dest and "不得出貨" not in dest


UNKNOWN = [
    "某個尚未存在之檢查所產生之訊息",
    "",
    "三件組已撤銷（R-1 v1）'Radio_btn0 in CLIMATIC_PANEL on BH-CAN'",
    "車輛屬性之值須以 `[…]` 包覆（037 逐字記法）：'$Vehicle_Line$ = DT'",
]


@pytest.mark.parametrize("detail", UNKNOWN, ids=["future", "empty", "v1", "bracket"])
def test_unknown_detail_falls_to_unclassified(detail) -> None:
    """**不得歸入「其餘」** —— 未知一律 unclassified，且其去向明說擋出貨。"""
    klass, dest = res.classify(detail)
    assert klass == "unclassified"
    assert "不得出貨" in dest


def test_unclassified_is_not_reachable_by_a_known_class() -> None:
    """反向：四個已知類皆不得回傳 unclassified（否則白名單形同虛設）。"""
    assert {res.classify(d)[0] for _, d in KNOWN} == {"bare-$", "ReviseC"}
