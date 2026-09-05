"""Tests for scripts/gates_tsv.py（R-G56 之閘登錄簿）。

R-G56 之除役判準為「連續 10 輪命中 0」。其唯一真正的風險是
**把「未量過」當成「命中 0」** —— 那會使一支從未被跑過的閘被除役，
而除役之理由（沒抓到東西）恰好由「沒跑」偽造。G-D 之字面形態：
**一個永遠空的清單與一個壞掉的清單，輸出相同。**

故本檔之測試集中於三件事：
1. 未涵蓋之閘記 `未知`，**不得記 0**
2. `hit_rounds` 只計實際涵蓋之輪次 —— 未知輪次不得充當「命中 0」
3. 除役候選須「量過 10 輪且全 0」，缺一不可（G-K ／ R-G9 兩向）
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("tc_gates", ROOT / "scripts" / "gates_tsv.py")
assert _spec and _spec.loader
gt = importlib.util.module_from_spec(_spec)
sys.modules["tc_gates"] = gt
_spec.loader.exec_module(gt)


class FakeLint:
    """最小閘登錄：A／B 常跑，Z 為 profile 專屬。"""
    CHECK_TITLES = {"A": "禁用動詞 (proc)", "B": "ER 情態詞 (er)", "Z": "profile 專屬"}
    CHECK_STATUS = {"A": "已校準", "B": "已校準（R-6b 範圍：Media 錨值 1→0）",
                    "Z": "未校準（R-10(a)，21 包新增）"}
    CHECK_GRANULARITY = {"A": "每次命中", "B": "每次命中", "Z": "每行每欄"}
    CHECK_ORDER = ["A", "B"]
    PROFILE_CHECKS = ["Z"]


def reports(tmp_path: Path, series: list[dict]) -> list[Path]:
    d = tmp_path / "docs" / "fw036" / "lint_reports"
    d.mkdir(parents=True, exist_ok=True)
    out = []
    for i, counts in enumerate(series):
        p = d / f"r{i:02d}.json"
        p.write_text(json.dumps({"counts": counts}), encoding="utf-8")
        out.append(p)
    return out


def by_id(rows: list[dict]) -> dict:
    return {r["gate_id"]: r for r in rows}


# --- 來源裁決之抽取 -------------------------------------------------------

def test_source_ruling_keeps_sub_clause():
    """`R-10(a)` 之子條標記不得被吃掉 —— 尾端須用負向前瞻而非 `\\b`。"""
    assert gt.RE_RULING.findall("未校準（R-10(a)，21 包新增）") == ["R-10(a)"]
    assert gt.RE_RULING.findall("已校準（R-6b 範圍：Media 錨值 1→0）") == ["R-6b"]
    assert gt.RE_RULING.findall("計數用（A-PM16：ER 側原不受任何檢查覆蓋）") == ["A-PM16"]


def test_no_ruling_is_marked_unstated_not_blank(tmp_path):
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, [{"A": 1, "B": 0}])))
    assert rows["A"]["source_ruling"] == "未載明"
    assert rows["B"]["source_ruling"] == "R-6b"
    assert rows["Z"]["source_ruling"] == "R-10(a)"


# --- 未知不得以 0 代替（G-D）----------------------------------------------

def test_uncovered_gate_is_unknown_not_zero(tmp_path):
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, [{"A": 0, "B": 0}] * 12)))
    assert rows["Z"]["hits_total"] == "未知"
    assert rows["Z"]["hits_recent"] == "未知，自本輪起算"
    assert rows["Z"]["hit_rounds"] == "0"
    assert rows["Z"]["retire_candidate"] == "N", "從未量過之閘不得成為除役候選"


def test_partially_covered_gate_counts_only_measured_rounds(tmp_path):
    """Z 只在最後兩輪被涵蓋 → hit_rounds = 2，未知輪次不充當命中 0。"""
    series = [{"A": 1}] * 10 + [{"A": 1, "Z": 0}, {"A": 1, "Z": 3}]
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, series)))
    assert rows["Z"]["hit_rounds"] == "2"
    assert rows["Z"]["hits_total"] == "3"
    assert rows["Z"]["hits_recent"].split(",").count("未知") == 8, "取近 10 輪"


def test_measured_zero_is_zero_not_unknown(tmp_path):
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, [{"A": 5, "B": 0}] * 3)))
    assert rows["B"]["hits_total"] == "0"
    assert rows["B"]["hits_recent"] == "0,0,0"


# --- 除役候選之兩向（G-K ／ R-G9）-----------------------------------------

def test_retire_candidate_needs_ten_measured_zero_rounds(tmp_path):
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, [{"A": 1, "B": 0}] * 10)))
    assert rows["B"]["retire_candidate"] == "Y", "量過 10 輪且全 0 → 候選"
    assert rows["A"]["retire_candidate"] == "N", "有命中者不得為候選"


def test_nine_zero_rounds_is_not_yet_a_candidate(tmp_path):
    """範圍向：差一輪即不得列入 —— 判準之邊界須實測，不憑閱讀。"""
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, [{"A": 1, "B": 0}] * 9)))
    assert rows["B"]["retire_candidate"] == "N"


def test_one_late_hit_clears_the_candidacy(tmp_path):
    series = [{"A": 1, "B": 0}] * 9 + [{"A": 1, "B": 1}]
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, series)))
    assert rows["B"]["retire_candidate"] == "N"


def test_recent_window_is_capped_at_ten(tmp_path):
    rows = by_id(gt.rows(FakeLint, reports(tmp_path, [{"A": 1, "B": 0}] * 25)[-gt.RECENT_N:]))
    assert len(rows["B"]["hits_recent"].split(",")) == gt.RECENT_N


# --- 欄與 scope -----------------------------------------------------------

def test_columns_and_scope(tmp_path):
    rows = gt.rows(FakeLint, reports(tmp_path, [{"A": 1}]))
    assert set(rows[0]) == set(gt.COLUMNS)
    d = by_id(rows)
    assert d["A"]["scope"] == "always" and d["Z"]["scope"] == "profile-only"
    assert all(r["retired"] == "N" for r in rows)


# --- CLI 與 --check -------------------------------------------------------

def test_check_detects_drift(tmp_path):
    """`--check` 為閘：登錄簿與現行閘不符即 exit 1。"""
    real = ROOT
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "gates_tsv.py"),
                        "--root", str(real), "--check"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr        # repo 內之 GATES.tsv 應為最新

    r2 = subprocess.run([sys.executable, str(ROOT / "scripts" / "gates_tsv.py"),
                         "--root", str(real), "--out", "nonexistent/GATES.tsv", "--check"],
                        capture_output=True, text=True)
    assert r2.returncode == 1 and "不符" in r2.stderr
