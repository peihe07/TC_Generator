"""Tests for scripts/selfcheck_map.py（R-G21 之自查表機檢對映）。

R-G21 之目的是**使「機器保證」與「人力承擔」在紙上分得開**（G-D、G-E）。
故本檔之測試不只驗「17 項都有分類」，更驗**分類不得虛報**：

- `partial` 必須寫出殘餘人力為何 —— 只標 partial 而不說殘餘是什麼，
  人讀時不知道自己要看什麼
- `full` 之項須真的由其閘承擔 —— 以 A-H10 之引號規則實測該閘轉紅（G-K），
  並附「正當寫法不轉紅」之範圍向（R-G9）
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


sm = _load("tc_selfcheck_map", "scripts/selfcheck_map.py")
lint036 = _load("tc_lint036_sc", "scripts/lint036.py")


# --- 解析 IN §9 -----------------------------------------------------------

def test_parses_seventeen_items():
    items = sm.parse_items(ROOT)
    assert sorted(items) == list(range(1, 18)), "IN §9 自查表為 17 項"


def test_every_item_is_classified():
    """R-G21：17 項全數分類，0 項懸置。"""
    rows = sm.rows(ROOT)
    assert len(rows) == 17
    assert all(r["coverage"] in {"full", "partial", "manual"} for r in rows)
    assert all(r["gate_ids"] for r in rows), "gate_ids 不得為空字串"


def test_coverage_is_three_state_not_two():
    """`partial` 必須存在 —— 二態分類會把「閘只覆蓋一半」記成「已保證」。"""
    cov = {r["coverage"] for r in sm.rows(ROOT)}
    assert cov == {"full", "partial", "manual"}


def test_partial_items_name_their_residual():
    for r in sm.rows(ROOT):
        if r["coverage"] == "partial":
            assert r["residual_manual"].strip(), f"第 {r['item']} 項 partial 而未寫殘餘"


def test_manual_items_are_marked_as_such():
    for r in sm.rows(ROOT):
        if r["coverage"] == "manual":
            assert r["gate_ids"] == "人工項"


def test_full_items_carry_no_residual():
    for r in sm.rows(ROOT):
        if r["coverage"] == "full":
            assert r["residual_manual"] == ""


def test_partial_without_residual_is_rejected(monkeypatch):
    """判準之可失效性：把一項 partial 之殘餘清空，產出須失敗而非靜默通過。"""
    broken = dict(sm.MAPPING)
    broken[1] = ("partial", ["G"], "")
    monkeypatch.setattr(sm, "MAPPING", broken)
    with pytest.raises(SystemExit):
        sm.rows(ROOT)


def test_item_count_mismatch_is_rejected(monkeypatch):
    broken = {k: v for k, v in sm.MAPPING.items() if k != 17}
    monkeypatch.setattr(sm, "MAPPING", broken)
    with pytest.raises(SystemExit):
        sm.rows(ROOT)


# --- A-H10 之已知案例（§D-6 所令之 G-K）-----------------------------------

def _fire(proc: str) -> list[str]:
    fields = {
        "test_set": "General Anatomy",
        "test_item": "The system shall display the Media screen\n(Media screen shown)",
        "pre": "1. The Home screen is displayed", "input": "NA", "proc": proc,
        "er": "1. The Media screen is displayed", "spec": "X_1.1", "author": "PeiPYHsu",
    }
    return sorted({v.check for v in lint036.check_row(
        fields, 10, "TC-001", lint036.DEFAULT_LENGTH_LIMIT, None)})


def test_item_15_maps_to_a_gate_that_actually_fires():
    """Home A-H10 之引號規則：自查第 15 項對映之閘須對方括號標籤轉紅。"""
    coverage, gates, _ = sm.MAPPING[15]
    assert coverage == "full" and gates == ["F"]
    assert "F" in _fire('1. Press [Media] on the Main Menu Bar'), \
        "第 15 項所對映之閘對已知缺陷不轉紅 → 對映失真（26 包 §F-2）"


def test_item_15_gate_does_not_fire_on_correct_notation():
    """範圍向（R-G9）：雙引號為正當寫法，不得轉紅。"""
    assert "F" not in _fire('1. Press "Media" on the Main Menu Bar')


def test_item_14_maps_to_a_gate_that_actually_fires():
    """第 14 項（行尾多餘句號）之對映閘 N 亦須可失效。"""
    coverage, gates, _ = sm.MAPPING[14]
    assert coverage == "full" and gates == ["N"]
    assert "N" in _fire('1. Press "Media" on the Main Menu Bar.')
    assert "N" not in _fire('1. Press "Media" on the Main Menu Bar')


# --- 反向索引 -------------------------------------------------------------

def test_reverse_index_is_consistent_with_mapping():
    idx = sm.reverse_index(ROOT)
    for item, (_, gates, _) in sm.MAPPING.items():
        for g in gates:
            assert str(item) in idx[g]
    flat = {(g, i) for g, items in idx.items() for i in items}
    expect = {(g, str(n)) for n, (_, gs, _) in sm.MAPPING.items() for g in gs}
    assert flat == expect


def test_gates_without_a_selfcheck_item_are_visible():
    """反向：有閘而自查表未問到者須看得見（其為自查表之缺口，非閘之缺陷）。"""
    idx = sm.reverse_index(ROOT)
    unmapped = [g for g in lint036.CHECK_ORDER + lint036.PROFILE_CHECKS if g not in idx]
    assert unmapped, "若全數對映則本測試須改寫 —— 現況為 9 支未對映"
    assert "C" in unmapped and "K" in unmapped


# --- --check --------------------------------------------------------------

def test_check_passes_against_repo_copy():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "selfcheck_map.py"),
                        "--root", str(ROOT), "--check"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_check_fails_when_file_absent():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "selfcheck_map.py"),
                        "--root", str(ROOT), "--out", "nope/SELFCHECK_MAP.tsv", "--check"],
                       capture_output=True, text=True)
    assert r.returncode == 1 and "不符" in r.stderr
