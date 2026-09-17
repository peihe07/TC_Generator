"""lint036 檢查 H 之引文豁免（R-SEC20(amend)(c)，Security profile 專屬）。

R-SEC20(c) 令 ER 引 037 逐字要件；037 CP-006 之 VC 自帶關係模糊語
（`logs must align with Logdog requirements (Error-level only for defects)`），
改寫即造值，故 `"…"` 內之命中豁免。豁免須為**位置條件**：
引號外之同一模糊語必須仍報（SEC-10 §5 第二條之反例）。
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import lint036  # noqa: E402

QUOTED = ('2. The Cert Provider source code and logs satisfy "logs must align with '
          'Logdog requirements (Error-level only for defects)"')
BARE = "2. The Cert Provider logs align with the Logdog policy"


def fields(er: str) -> dict[str, str]:
    """僅 H 所需之最小列；其餘欄給合規值以免夾帶他項違規。"""
    return {
        "test_set": "Service Robustness",
        "test_item": "The Cert Provider feature shall adhere to the guidelines.\n(logging policy)",
        "pre": "1. Access to the RD build environment for Cert Provider is granted",
        "input": "NA",
        "proc": "1. <obtain the Cert Provider source code and logs per RD>",
        "er": er,
        "spec": "SWE1_CERTPROVIDER_FM-WI-FSM-037-A03_SWE1-CertProvider-006",
        "author": "PeiPYHsu",
    }


def h_hits(er: str, profile: str | None) -> list[lint036.Violation]:
    return [v for v in lint036.check_row(fields(er), 10, "NR1L-CP-012", 50, profile)
            if v.check == "H"]


def test_quoted_relation_word_is_exempt_under_security():
    assert h_hits(QUOTED, "security") == []


def test_bare_relation_word_still_flagged_under_security():
    """§5 反例：引號外之 `align with` 不得被吞。"""
    hits = h_hits(BARE, "security")
    assert len(hits) == 1
    assert "align with" in hits[0].detail


def test_mixed_line_reports_only_the_bare_hit():
    hits = h_hits(f"{QUOTED}\n{BARE}", "security")
    assert len(hits) == 1
    assert "align with the Logdog policy" in hits[0].snippet


@pytest.mark.parametrize("profile", [None, "camera", "power"])
def test_exemption_is_security_only(profile):
    """非 security（含無 profile）之行為不變 —— 引文內仍報。

    無 profile 時 H 只跑 `RE_H`（`as expected` 等），關係模糊語不在其內，
    故以 `works normally` 作該路徑之探針。
    """
    probe = '2. The service satisfies "the module works normally after reset"'
    assert len(h_hits(probe, profile)) == 1
    assert h_hits(probe, "security") == []


def test_reuses_check_b_quote_mechanism():
    """引號範圍沿用檢查 B 之 `quoted_spans()`／`inside_spans()`，不另立一套。"""
    text = 'a "b c" d'
    spans = lint036.quoted_spans(text)
    assert lint036.inside_spans((3, 6), spans)
    assert not lint036.inside_spans((8, 9), spans)


def test_h_is_not_wholly_exempt():
    """`H` 不得進 `FEATURE_EXEMPT` —— 整項豁免會連引號外之命中一起吞。"""
    assert "H" not in lint036.FEATURE_EXEMPT.get("security", [])
    assert "H" in lint036.check_order("security")
