"""Tests for scripts/rulings_hash.py（R-G13 之指紋表）。

依 G-N，缺陷之原文以**字面**釘入，不取當前語料為案例：三個成因各有一組
以真實碰撞之措辭寫成之最小案例，另加一組「修正後不得再命中」之回歸。

首跑抓到之三個成因：
1. `R-VS57 之 (4)` 之子條被截成母條 id → 假性碰撞
2. 「執行層回報」段重用條號當標題 → 假性碰撞
3. `<details>` 內之作廢原文與現行條文同號 → 假性碰撞

第四類（R-VS59～R-VS66 之八組）為**真碰撞**，工具須照報 —— 見最後一組測試。
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("tc_rulings_hash", ROOT / "scripts" / "rulings_hash.py")
assert _spec and _spec.loader
rh = importlib.util.module_from_spec(_spec)
sys.modules["tc_rulings_hash"] = rh
_spec.loader.exec_module(rh)


def write(tmp_path: Path, rel: str, text: str) -> Path:
    p = tmp_path / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def ids(rulings) -> list[str]:
    return [r.ruling_id for r in rulings]


def by_id(rulings) -> dict:
    return {r.ruling_id: r for r in rulings}


# --- 1. 基本抽取 ---------------------------------------------------------

def test_extracts_anchor_id_and_body(tmp_path):
    write(tmp_path, "R.md", "# R\n\n### R-VS7 — 委派界線\n\n條文本體一。\n")
    out = rh.extract(tmp_path / "R.md", tmp_path)
    assert ids(out) == ["R-VS7"]
    assert out[0].kind == "ruling"
    assert out[0].body_lines == 1


def test_heading_text_not_in_hash(tmp_path):
    """標題含輪次與日期，其變動不得改變條文身分。"""
    write(tmp_path, "a.md", "### R-VS7 — 委派界線（61 包 §3）\n\n本體不變。\n")
    write(tmp_path, "b.md", "### R-VS7 — 委派界線（63 包 §1，改寫標題）\n\n本體不變。\n")
    a = rh.extract(tmp_path / "a.md", tmp_path)[0]
    b = rh.extract(tmp_path / "b.md", tmp_path)[0]
    assert a.sha256 == b.sha256


def test_body_change_changes_hash(tmp_path):
    """R-G13 之整個效力靠這一條：本體一改，sha 即不符。"""
    write(tmp_path, "a.md", "### R-VS7 — 委派界線\n\n委派不免除產出 TC 之義務。\n")
    write(tmp_path, "b.md", "### R-VS7 — 委派界線\n\n委派免除產出 TC 之義務。\n")
    a = rh.extract(tmp_path / "a.md", tmp_path)[0]
    b = rh.extract(tmp_path / "b.md", tmp_path)[0]
    assert a.sha256 != b.sha256


def test_trailing_hrule_not_absorbed_into_body(tmp_path):
    """章節分隔線不屬任何條文 —— 其後追加新章節不得改變前一條之 sha。

    W-P3 實測之字面案例：`R-VS82` 於其後追加 `## 主線 —— 26 包` 後 sha 變，
    **而其本體一字未改**。假性不符若累積，R-G13 之比對會被當成噪音忽略。
    """
    body = "### R-X1 —— 甲\n\n條文本體，一字未改。\n"
    write(tmp_path, "a.md", body)
    write(tmp_path, "b.md", body + "\n---\n\n## 新章節\n\n### R-X2 —— 乙\n\n另一條。\n")
    a = rh.extract(tmp_path / "a.md", tmp_path)[0]
    b = by_id(rh.extract(tmp_path / "b.md", tmp_path))["R-X1"]
    assert a.sha256 == b.sha256, "末條之 sha 不得因其後有無章節而改變"


@pytest.mark.parametrize("rule", ["---", "***", "___", "-----"])
def test_all_hrule_forms_are_stripped(tmp_path, rule):
    write(tmp_path, "a.md", "### R-X1 — 甲\n\n本體。\n")
    write(tmp_path, "b.md", f"### R-X1 — 甲\n\n本體。\n\n{rule}\n")
    a = rh.extract(tmp_path / "a.md", tmp_path)[0]
    b = rh.extract(tmp_path / "b.md", tmp_path)[0]
    assert a.sha256 == b.sha256


def test_hrule_inside_body_is_kept(tmp_path):
    """範圍向（R-G9）：只剝**尾端**之分隔線；本體中間者為內容，不得剝。"""
    write(tmp_path, "a.md", "### R-X1 — 甲\n\n前段。\n\n---\n\n後段。\n")
    write(tmp_path, "b.md", "### R-X1 — 甲\n\n前段。\n\n後段。\n")
    a = rh.extract(tmp_path / "a.md", tmp_path)[0]
    b = rh.extract(tmp_path / "b.md", tmp_path)[0]
    assert a.sha256 != b.sha256, "本體中間之分隔線為內容之一部分"


def test_anchor_inside_fence_not_collected(tmp_path):
    write(tmp_path, "R.md", "### R-VS7 — 甲\n\n```\n### R-VS8 — 這在 code fence 內\n```\n")
    assert ids(rh.extract(tmp_path / "R.md", tmp_path)) == ["R-VS7"]


# --- 2. 成因一：子條被截成母條 id ---------------------------------------

@pytest.mark.parametrize("heading, expected", [
    ("### R-VS57 之 (4) —— WARN 須名與值域皆有來源（61 包 §4）", "R-VS57(4)"),
    ("### R-VS7(a)′ —— 委派句指名功能群（33 包 §1.2）", "R-VS7(a)′"),
    ("### R-VS35 之補充 —— 登記類 D 項不隨升級而中止（75 包 §1）", "R-VS35+補充"),
    ("### R-VS79 之修訂 —— L3 由「至少一次抽驗」改為「全量驗」（88 包 §2.1）", "R-VS79+修訂"),
    ("### R-VF42 但書 —— 純裁定落檔包不受 R-VF42 第 4 項拘束（V15 §6）", "R-VF42+但書"),
    ("### R-VS19″ —— 適用性判準之更正（34 包 §1）", "R-VS19″"),
])
def test_sub_clause_id_distinct_from_parent(tmp_path, heading, expected):
    write(tmp_path, "R.md", f"{heading}\n\n本體。\n")
    assert ids(rh.extract(tmp_path / "R.md", tmp_path)) == [expected]


def test_parent_and_sub_clause_do_not_collide(tmp_path):
    write(tmp_path, "features/f/RULINGS.md",
          "## 條文\n\n### R-VS57 —— L-VS2 由二值改為三分\n\n母條本體。\n\n"
          "### R-VS57 之 (4) —— WARN 須名與值域皆有來源\n\n子條本體。\n")
    rulings, dupes = rh.collect(tmp_path, ["features/f/RULINGS.md"])
    assert sorted(ids(rulings)) == ["R-VS57", "R-VS57(4)"]
    assert dupes == []


# --- 3. 成因二：回報段重用條號 -------------------------------------------

def test_report_section_heading_not_counted_as_ruling(tmp_path):
    write(tmp_path, "features/f/RULINGS.md",
          "## R-C1 ~ R-C5 —— 下放包 01 §3（Pei 裁定）\n\n### R-C1 —— 條文\n\n條文本體。\n\n"
          "## 執行層回報（2026-08-14，Phase 0 → Phase 1）\n\n"
          "### R-C1 —— 落實於三處，非僅文件\n\n實測紀錄，非條文。\n")
    rulings, dupes = rh.collect(tmp_path, ["features/f/RULINGS.md"])
    kinds = {(r.ruling_id, r.kind) for r in rulings}
    assert ("R-C1", "ruling") in kinds
    assert ("R-C1", "report") in kinds
    assert dupes == [], "回報標題不得與條文判為碰撞"


# --- 4. 成因三：作廢原文與現行條文同號 -----------------------------------

def test_details_block_marks_superseded(tmp_path):
    write(tmp_path, "features/f/RULINGS.md",
          "## VF230 線 —— V25 包\n\n"
          "### ⚠ 作廢 —— 下列 R-VF70 係自 V25 之舊版本落檔，該版本已被改寫\n\n"
          "<details><summary>已作廢之原文（點開）</summary>\n\n"
          "### R-VF70 —— tc_title 採純句式\n\n舊本體。\n\n</details>\n\n"
          "## VF230 線 —— V25 包（改寫後之版本）\n\n"
          "### R-VF70 —— 判準以允許型別之白名單為之（V25 §4）\n\n新本體。\n")
    rulings, dupes = rh.collect(tmp_path, ["features/f/RULINGS.md"])
    kinds = {(r.ruling_id, r.kind) for r in rulings}
    assert ("R-VF70", "superseded") in kinds
    assert ("R-VF70", "ruling") in kinds
    assert dupes == [], "作廢原文不得與現行條文判為碰撞"


def test_superseded_heading_scope_ends_at_same_level(tmp_path):
    """作廢標記只轄其下級；同級之後續標題須回到 ruling。"""
    write(tmp_path, "R.md",
          "### 作廢 —— 舊段\n\n#### R-VF70 —— 舊\n\n舊本體。\n\n"
          "### 現行\n\n#### R-VF71 —— 新\n\n新本體。\n")
    got = by_id(rh.extract(tmp_path / "R.md", tmp_path))
    assert got["R-VF70"].kind == "superseded"
    assert got["R-VF71"].kind == "ruling"


def test_details_mentioned_in_prose_does_not_open_a_fold(tmp_path):
    """敘述行以反引號談論 `<details>` 標籤時，不得計為開啟摺疊區。

    未剝除行內程式碼者，巢深永不歸零，其後全部條文遭誤判 superseded ——
    W-27 實測：VS RULINGS 之兩行敘述使 R-VF96 以降 46 條全數誤判，
    且 R-VS82／R-VS83／R-VF95 之誤判早已隨舊 tsv 入版控。
    """
    write(tmp_path, "R.md",
          "### R-VS82 —— 現行甲\n\n本體甲。\n\n"
          "### R-VS83 —— 談論摺疊區者\n\n"
          "(b) 已作廢之痕收在 `<details>` 摺疊區內，其保留係依 R-VF18 留痕。\n"
          "其判別依 `<details>` 摺疊區之邊界（L4429-L4557）為之 ——\n\n"
          "### R-VF95 —— 現行乙\n\n本體乙。\n")
    got = by_id(rh.extract(tmp_path / "R.md", tmp_path))
    assert [got[k].kind for k in ("R-VS82", "R-VS83", "R-VF95")] == ["ruling"] * 3


# --- 5. 真碰撞須照報（範圍向之另一端，G-K）-------------------------------

def test_genuine_collision_is_reported(tmp_path):
    """R-VS59 之字面案例：VF230 線與 CFTS044 本線之同號兩條，本體不同。"""
    write(tmp_path, "features/f/RULINGS.md",
          "## VF230（Part 2）進場 —— 61 包 §3\n\n"
          "### R-VS59 —— VF230 之 B 欄序號自 238 起（61 包 §3）\n\n"
          "VF230 之 036 workbook，B 欄自 238 起連續遞增。\n\n"
          "## CFTS044 本線 —— 63 包\n\n"
          "### R-VS59 —— 委派不等於不寫（63 包 §1）\n\n"
          "委派不免除產出 TC 之義務。\n")
    rulings, dupes = rh.collect(tmp_path, ["features/f/RULINGS.md"])
    assert len(dupes) == 1
    assert "R-VS59" in dupes[0] and "本體不同" in dupes[0]


def test_same_body_collision_flagged_but_not_hard(tmp_path):
    """同號同本體（重複轉錄）記為碰撞但非 hard，--gate 不轉紅。"""
    write(tmp_path, "features/f/RULINGS.md",
          "### R-VS59 —— 甲\n\n同一本體。\n\n### R-VS59 —— 乙\n\n同一本體。\n")
    rulings, dupes = rh.collect(tmp_path, ["features/f/RULINGS.md"])
    assert len(dupes) == 1 and "本體相同" in dupes[0]


# --- 6. --check 與 --gate 之離開碼 ---------------------------------------

def run(tmp_path, *args) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "rulings_hash.py"), "--root", str(tmp_path), *args],
        capture_output=True, text=True)


def seed_repo(tmp_path, body: str = "條文本體。") -> None:
    write(tmp_path, "docs/fw036/FEATURE_ONBOARDING.md", "## 9. 通則\n\n### R-G1 — 母本\n\n" + body + "\n")
    write(tmp_path, "features/vehicle_setting/RULINGS.md", "### R-VS7 — 委派界線\n\n另一條文。\n")


def test_check_passes_then_fails_after_edit(tmp_path):
    seed_repo(tmp_path)
    assert run(tmp_path).returncode == 0
    assert run(tmp_path, "--check").returncode == 0
    seed_repo(tmp_path, body="條文本體被改了。")
    r = run(tmp_path, "--check")
    assert r.returncode == 1
    assert "與現行條文不符" in r.stderr


def test_check_fails_when_tsv_absent(tmp_path):
    seed_repo(tmp_path)
    r = run(tmp_path, "--check")
    assert r.returncode == 1 and "不存在" in r.stderr


def test_gate_red_on_hard_collision_green_otherwise(tmp_path):
    seed_repo(tmp_path)
    assert run(tmp_path, "--gate").returncode == 0, "無碰撞之語料不得轉紅（R-G9 範圍向）"
    write(tmp_path, "features/vehicle_setting/RULINGS.md",
          "### R-VS7 — 甲\n\n本體一。\n\n### R-VS7 — 乙\n\n本體二。\n")
    assert run(tmp_path, "--gate").returncode == 1, "本體不同之碰撞須轉紅（G-K）"
