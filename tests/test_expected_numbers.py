"""Tests for scripts/expected_numbers.py（R-G16 之預期數字推導）。

本工具存在之理由是**第二層檢驗**（FO §8.3）：閘全綠而數字不對時攔下它。
故其自身之測試須證明它會在已知缺陷上轉紅（G-K），且不在正常語料上
轉紅（R-G9 範圍向）。

字面釘入之案例（G-N）：`vf230` 之 seq 空洞 248–257 ——
pilot1 佔 238–247、pilot2 佔 258–267，**中間十個序號無任何產出佔用**，
而各批自身連續，故任何逐批之檢查皆全綠。
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("tc_expnum", ROOT / "scripts" / "expected_numbers.py")
assert _spec and _spec.loader
en = importlib.util.module_from_spec(_spec)
sys.modules["tc_expnum"] = en
_spec.loader.exec_module(en)

SELECTION = ("R-VS58 選池序，量產母體 574（620 − pilot 20 − 隔離 26，R-VF77 二）。"
             "事實抽不出者跳過並具名。")


def make_repo(tmp_path: Path, artifacts: dict, *, seq_start: int = 238,
              leaves: int = 10, disagree: int = 0, isolated: int = 3) -> Path:
    """最小 feature：feature.yaml ＋ leaves/isolated tsv ＋ generated/*.json。"""
    fdir = tmp_path / "features" / "f"
    (fdir / "data").mkdir(parents=True, exist_ok=True)
    (fdir / "generated").mkdir(parents=True, exist_ok=True)
    (fdir / "feature.yaml").write_text(
        "feature: F\nprofiles:\n  p:\n    leaves: \"data/p_leaves.tsv\"\n"
        f"    seq_start: {seq_start}\n", encoding="utf-8")
    rows = ["swe_id\tdisagree"] + [
        f"L{i}\t{1 if i < disagree else 0}" for i in range(leaves)]
    (fdir / "data" / "p_leaves.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (fdir / "data" / "p_isolated.tsv").write_text(
        "\n".join(["leaf_id\tclass"] + [f"L{i}\tx" for i in range(isolated)]) + "\n",
        encoding="utf-8")
    for name, seqs in artifacts.items():
        payload = {"batch": name, "selection": SELECTION,
                   "tcs": [{"leaf_id": f"L{s}", "seq": s} for s in seqs]}
        (fdir / "generated" / f"{name}.json").write_text(
            json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    return tmp_path


def metrics(tmp_path: Path) -> dict:
    c = en.Corpus(tmp_path.resolve(), "f", "p")
    c.load()
    ms, extra = en.build(c)
    return {m.key: m for m in ms}, extra


# --- 手算值之抽取 ---------------------------------------------------------

def test_hand_values_parsed_from_selection_field():
    got, src = en.hand_values([("b.json", {"selection": SELECTION})])
    assert got == {"pool_net": 574, "pool": 620, "pilot": 20, "iso": 26}
    assert src == "b.json"


def test_no_selection_yields_no_hand_values():
    got, src = en.hand_values([("b.json", {"selection": "無算式"})])
    assert got == {} and src == ""


# --- seq 空洞：G-K（會轉紅）------------------------------------------------

def test_seq_hole_between_batches_is_caught(tmp_path):
    """字面案例：238–247 ／ 258–267 ——「各批自身連續」而聯集有 10 個洞。"""
    repo = make_repo(tmp_path, {
        "p_pilot1": list(range(238, 248)),
        "p_pilot2": list(range(258, 268)),
    })
    ms, extra = metrics(repo)
    assert ms["seq_holes"].derived == 10
    assert ms["seq_holes"].verdict == "**不符**"
    assert extra["seq"]["holes"] == list(range(248, 258))


def test_each_artifact_alone_is_continuous(tmp_path):
    """反證空洞之隱蔽性：逐檔看皆無斷點，故逐批之檢查必然全綠。"""
    repo = make_repo(tmp_path, {
        "p_pilot1": list(range(238, 248)),
        "p_pilot2": list(range(258, 268)),
    })
    _, extra = metrics(repo)
    for _, _, seqs in extra["seq"]["per"]:
        assert seqs == list(range(seqs[0], seqs[-1] + 1)), "單檔內不得有斷點"


def test_lead_gap_before_seq_start_is_caught(tmp_path):
    """seq_start 之後、實測最小之前的未佔用序號亦須攔下。"""
    repo = make_repo(tmp_path, {"p_batch01": list(range(245, 255))}, seq_start=238)
    ms, _ = metrics(repo)
    assert ms["seq_lead_gap"].derived == 7
    assert ms["seq_lead_gap"].verdict == "**不符**"


def test_duplicate_seq_across_artifacts_is_counted(tmp_path):
    repo = make_repo(tmp_path, {
        "p_batch01": list(range(238, 243)),
        "p_batch02": list(range(242, 247)),      # 242 重複
    })
    ms, _ = metrics(repo)
    assert ms["seq_dupes"].derived == 1


# --- 範圍向（R-G9）：正常語料不得轉紅 -------------------------------------

def test_contiguous_corpus_has_no_seq_findings(tmp_path):
    repo = make_repo(tmp_path, {
        "p_pilot1": list(range(238, 248)),
        "p_batch01": list(range(248, 258)),
        "p_batch02": list(range(258, 268)),
    })
    ms, _ = metrics(repo)
    assert ms["seq_holes"].derived == 0
    assert ms["seq_lead_gap"].derived == 0
    assert ms["seq_dupes"].derived == 0
    assert ms["seq_holes"].verdict == "符"


def test_pilot_and_batch_are_counted_separately(tmp_path):
    repo = make_repo(tmp_path, {
        "p_pilot1": list(range(238, 248)),
        "p_batch01": list(range(248, 258)),
        "p_batch02": list(range(258, 268)),
    })
    ms, _ = metrics(repo)
    assert ms["pilot_files"].derived == 1 and ms["pilot_tcs"].derived == 10
    assert ms["batch_files"].derived == 2 and ms["batch_tcs"].derived == 20
    assert ms["pilot_tcs"].verdict == "**不符**", "手算 pilot 為 20，本例為 10"


def test_leaves_net_subtracts_disagree(tmp_path):
    repo = make_repo(tmp_path, {"p_batch01": [238]}, leaves=30, disagree=4)
    ms, _ = metrics(repo)
    assert ms["leaves_rows"].derived == 30
    assert ms["leaves_disagree"].derived == 4
    assert ms["leaves_net"].derived == 26


def test_no_hand_value_is_not_a_mismatch(tmp_path):
    """手算包未載之項記「無手算值」，**不得記為符**（G-D：未量與量得為 0 不同）。"""
    repo = make_repo(tmp_path, {"p_batch01": [238]})
    ms, _ = metrics(repo)
    assert ms["batch_files"].verdict == "無手算值"
    assert ms["leaves_rows"].verdict == "無手算值"


# --- CLI ------------------------------------------------------------------

def run(repo: Path, *args) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "expected_numbers.py"),
         "--root", str(repo), "--feature", "f", "--profile", "p", *args],
        capture_output=True, text=True)


def test_gate_red_on_hole_green_on_contiguous(tmp_path):
    holed = make_repo(tmp_path / "a", {
        "p_pilot1": list(range(238, 248)), "p_pilot2": list(range(258, 268))})
    r = run(holed, "--gate")
    assert r.returncode == 1 and "seq_holes" in r.stderr

    clean = make_repo(tmp_path / "b", {
        "p_pilot1": list(range(238, 248)), "p_pilot2": list(range(248, 258))},
        isolated=26)
    # pilot 條數 20 且隔離 26 皆與手算相符；leaves_net 亦對齊
    clean_repo = make_repo(tmp_path / "b", {
        "p_pilot1": list(range(238, 248)), "p_pilot2": list(range(248, 258))},
        leaves=620, disagree=0, isolated=26)
    r2 = run(clean_repo, "--gate")
    assert r2.returncode == 0, r2.stderr


def test_report_lists_holes_verbatim(tmp_path):
    repo = make_repo(tmp_path, {
        "p_pilot1": list(range(238, 248)), "p_pilot2": list(range(258, 268))})
    r = run(repo)
    assert "248, 249, 250, 251, 252, 253, 254, 255, 256, 257" in r.stdout
    assert "空洞不使任何 lint 轉紅" in r.stdout
