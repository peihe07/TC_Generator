"""R-C50(amend) 之 `test-item-upper-verbatim` —— 首字母正規化之正／負向測試。

CMF-03 §2 要求「gate 改動須附一個負向測試（首字母以外之差異仍 FAIL）」。
放寬一道 gate 時，證明它還擋得住什麼，和證明它放過了什麼一樣重要 ——
只有正向測試的放寬，與把該 gate 刪掉在證據上等價。
"""
import importlib.util
import sys
from pathlib import Path

import pytest

COMFORT = Path(__file__).resolve().parent.parent / "features" / "comfort"

# features/media、features/home 之 scripts 下各有一支 `lint_tcs.py`。以裸名匯入
# 會使**最先載入者**佔住 `sys.modules["lint_tcs"]` 並被交給另一個 feature 之測試
# （`tests/test_home_lint_tcs.py` 之註解已記此陷阱）。故以唯一名載入。
sys.path.append(str(COMFORT / "scripts"))
_spec = importlib.util.spec_from_file_location(
    "comfort_lint_tcs", COMFORT / "scripts" / "lint_tcs.py")
if _spec is None or _spec.loader is None:
    pytest.skip("features/comfort linter not present", allow_module_level=True)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["comfort_lint_tcs"] = _mod
_spec.loader.exec_module(_mod)
upper_matches = _mod.upper_matches

BODY = ("C2.) AUTO has on/ off state. A pop-up will be shown coming down from "
        "that temperature in the status bar to indicate it is being changed.")


def test_exact_substring_passes():
    assert upper_matches("AUTO has on/ off state.", BODY)


def test_lowercase_first_letter_is_normalised():
    """摘句自句中段起抄，首字母被排版正規化為大寫 —— R-4，須通過。"""
    excerpt = ("A pop-up will be shown coming down from that temperature in "
               "the status bar")
    assert excerpt in BODY                     # 原文即大寫起首
    assert upper_matches(excerpt.replace("A pop-up", "a pop-up", 1), BODY)


def test_uppercase_first_letter_of_a_mid_sentence_excerpt_is_normalised():
    """反向：原文小寫起首而摘句寫成大寫者亦通過（正規化是雙向的）。"""
    body = "the system will show a pop-up when the temperature changes"
    assert upper_matches("The system will show a pop-up", body)


# --------------------------------------------------------------- 負向
def test_difference_beyond_the_first_letter_still_fails():
    """首字母以外之大小寫差異仍 FAIL —— 這是放寬之界線。"""
    assert not upper_matches("A POP-UP will be shown coming down", BODY)
    assert not upper_matches("A pop-Up will be shown coming down", BODY)


def test_word_level_difference_still_fails():
    assert not upper_matches("A popup will be shown coming down", BODY)


def test_non_contiguous_excerpt_still_fails():
    assert not upper_matches("AUTO has on/ off state. A pop-up will be shown "
                             "in the status bar", BODY)


def test_empty_excerpt_fails():
    assert not upper_matches("", BODY)
    assert not upper_matches("   ", BODY)
