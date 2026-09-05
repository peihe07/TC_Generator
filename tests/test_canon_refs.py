"""Tests for scripts/canon_refs.py（R-G57 之引用解析器）。

依 G-K，每一判準皆附「對已知案例會轉紅」之實測；依 R-G9，每一判準皆附
範圍向（對不該轉紅之近似案例證明其不轉紅）。案例以**字面**釘入（G-N）：

- `§8.4` —— FO 有「結果三分法」、IN 有「No Fabrication」，**裸引用即歧義**
- `§7.3` —— 兩份 canon 皆無此節（FO:432 之實例），須 unresolved
- `§5a` —— 僅 FO 有，須 resolved
- `§10.4` —— 僅 IN 有，須 resolved
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("tc_canon_refs", ROOT / "scripts" / "canon_refs.py")
assert _spec and _spec.loader
cr = importlib.util.module_from_spec(_spec)
sys.modules["tc_canon_refs"] = cr
_spec.loader.exec_module(cr)

FO_TEXT = """## 5a. 數字紀律

| 條 | 內容 |
|---|---|
| 1 | 列號須標明實體列號 |
| 2 | 計數須標明逐列或逐引用 |

## 8. 下放包與上繳包契約

### 8.4 結果三分法

## 9. 通則

### 9.2 全域條文

| 條 | 一句話 |
|---|---|
| R-G5 | 全部 git 操作屬 Pei |
| R-G51 | git commit 一律帶 pathspec |
"""

IN_TEXT = """## 8. Requirement Alignment

### 8.4 No Fabrication

## 9. Self-Check

1. 第一項
2. 第二項

## 10. Tool-Specific Output Contract

### 10.4 `reasoning` field
"""


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """最小 repo：兩份 canon ＋ 一個 feature 目錄。"""
    fo = tmp_path / "docs/fw036/FEATURE_ONBOARDING.md"
    inn = tmp_path / "docs/runtime/ASPICE_SWE6_AI_Instruction.md"
    for p, text in ((fo, FO_TEXT), (inn, IN_TEXT)):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    monkeypatch.setitem(cr.CANONS, "FO", "docs/fw036/FEATURE_ONBOARDING.md")
    monkeypatch.setitem(cr.CANONS, "IN", "docs/runtime/ASPICE_SWE6_AI_Instruction.md")
    return tmp_path


def cite(repo, line: str) -> list:
    p = repo / "features/f/docs/handoff/01_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(line + "\n", encoding="utf-8")
    _, refs, _ = cr.collect(repo)
    return [r for r in refs if r.source.startswith("features/")]


def one(repo, line: str, kind: str | None = None):
    got = [r for r in cite(repo, line) if kind is None or r.kind == kind]
    assert len(got) == 1, f"預期一筆，實得 {[(r.kind, r.target, r.verdict) for r in got]}"
    return got[0]


# --- 索引建立 -------------------------------------------------------------

def test_index_finds_shared_section_numbers(repo):
    rs = cr.Resolver(repo)
    shared = set(rs.canons["FO"].sections) & set(rs.canons["IN"].sections)
    assert {"8", "8.4", "9"} <= shared
    assert "5a" not in shared and "10.4" not in shared


def test_item_caps_read_from_table_and_ordered_list(repo):
    rs = cr.Resolver(repo)
    assert rs.canons["FO"].items["5a"] == 2      # 表列
    assert rs.canons["IN"].items["9"] == 2       # 編號條列


# --- section 型：三種判定各附反向與範圍向 ---------------------------------

def test_shared_section_is_ambiguous(repo):
    """已知案例：canon §8.4 於 FO 與 IN 皆有 → 須轉紅為 ambiguous（G-K）。"""
    r = one(repo, "依 canon §8.4 三分法處置。", kind="section")
    assert r.verdict == "ambiguous"
    assert set(r.hits) == {"FO§8.4", "IN§8.4"}


@pytest.mark.parametrize("line, target", [
    ("依 canon §5a 之數字紀律。", "§5a"),
    ("依 canon §10.4 之 reasoning 欄。", "§10.4"),
])
def test_unique_section_resolves(repo, line, target):
    """範圍向（R-G9）：只在一份 canon 內之節號不得轉紅。"""
    r = one(repo, line, kind="section")
    assert r.verdict == "resolved" and r.target == target


def test_missing_section_is_unresolved(repo):
    """FO:432 之字面案例：canon §7.3（雙層檢驗）兩份 canon 皆無。"""
    r = one(repo, "雙向查證是雙層檢驗（canon §7.3）在事實陳述上的對應物。", kind="section")
    assert r.verdict == "unresolved" and r.hits == ()


def test_doc_prefix_disambiguates(repo):
    """FO／IN 前綴為消歧手段：同一節號加前綴後須由 ambiguous 轉 resolved。"""
    assert one(repo, "依 canon §8.4 三分法。", kind="section").verdict == "ambiguous"
    assert one(repo, "依 FO §8.4 三分法。", kind="section").verdict == "resolved"
    assert one(repo, "依 IN §8.4 之 No Fabrication。", kind="section").verdict == "resolved"


def test_duplicate_heading_within_one_canon_is_ambiguous(repo, monkeypatch):
    """FO 現有兩個 `## 9.`；同一 canon 內之重複亦須判為 ambiguous。"""
    fo = repo / "docs/fw036/FEATURE_ONBOARDING.md"
    fo.write_text(FO_TEXT + "\n## 9. 全域慣例\n", encoding="utf-8")
    r = one(repo, "見 FO §9。", kind="section")
    assert r.verdict == "ambiguous" and r.hits == ("FO§9×2",)


# --- item 型 --------------------------------------------------------------

def test_item_within_cap_resolves(repo):
    r = one(repo, "依 canon §5a 第 2 條。", kind="item")
    assert r.verdict == "resolved"


def test_item_beyond_cap_is_unresolved(repo):
    """§5a 索引只到第 2 條，引用第 9 條須轉紅。"""
    r = one(repo, "依 canon §5a 第 9 條。", kind="item")
    assert r.verdict == "unresolved" and "上限 2" in r.hits[0]


def test_dash_form_item(repo):
    assert one(repo, "依 canon §5a-1 之列號紀律。", kind="item").verdict == "resolved"
    assert one(repo, "依 canon §5a-9 之列號紀律。", kind="item").verdict == "unresolved"


def test_item_on_ambiguous_section_stays_ambiguous(repo):
    r = one(repo, "依 canon §9 第 1 條。", kind="item")
    assert r.verdict == "ambiguous"


# --- ruling 型 ------------------------------------------------------------

def test_ruling_resolves_without_canon_prefix(repo):
    """R-Gn 為全域命名空間，不需 `canon` 前綴。"""
    r = one(repo, "全部 git 操作屬 Pei（R-G5）。", kind="ruling")
    assert r.verdict == "resolved" and r.hits == ("FO:R-G5",)


def test_unknown_ruling_is_unresolved(repo):
    """R-G52 尚未併入 canon → 須 unresolved。整併後本測試之預期須反轉。"""
    assert one(repo, "依 R-G52 之引用制。", kind="ruling").verdict == "unresolved"


@pytest.mark.parametrize("line", ["R-G4-1 之衍生檔紀律", "R-G7-1 之對照向"])
def test_ruling_with_revision_suffix(repo, line):
    """`R-G4-1` 之尾碼為修訂版次，其基號仍為 4／7。"""
    monkey = one(repo, line + "（見 FO §9.2）", kind="ruling")
    assert monkey.verdict == "unresolved"  # 範例 canon 只載 R-G5／R-G51


def test_ruling_word_boundary_not_matched_inside_longer_token(repo):
    """範圍向：`R-G50`／`XR-G5` 不得被讀成 R-G5。"""
    assert [r.target for r in cite(repo, "見 R-G50 與 XR-G5。") if r.kind == "ruling"] == ["R-G50"]


# --- unqualified 為盲區，不計入 FAIL ---------------------------------------

def test_bare_section_ref_is_unqualified(repo):
    r = one(repo, "見本包 §8.4 之處置。", kind="unqualified")
    assert r.verdict == "resolved"


def test_unqualified_excluded_from_gate(repo):
    """裸 §7.3（feature 自身節號）不得使閘轉紅 —— R-G9 範圍向。"""
    p = repo / "features/f/docs/handoff/02_y.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("見 §7.3 與 §8.4 與 §99.9。\n", encoding="utf-8")
    _, refs, _ = cr.collect(repo)
    assert all(r.kind == "unqualified" for r in refs if r.source.endswith("02_y.md"))


# --- 掃描面 ---------------------------------------------------------------

@pytest.mark.parametrize("rel, included", [
    ("docs/fw036/handoff/23_x.md", True),
    ("scripts/lint036.py", True),
    ("features/f/RULINGS.md", True),
    ("features/f/docs/upstream/01_a.md", True),
    ("features/f/scripts/lint_tcs.py", True),
    ("features/f/data/pending_sibling.tsv", False),
    ("features/f/generated/batch01.json", False),
    ("archive/M1/findings.json", False),
    ("features/f/sandbox/backup/x.md", False),
])
def test_scan_surface(rel, included):
    assert cr.in_scan_surface(Path(rel)) is included


# --- 離開碼 ---------------------------------------------------------------

def run(repo, *args) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "canon_refs.py"), "--root", str(repo), *args],
        capture_output=True, text=True)


def test_gate_green_on_clean_repo(repo):
    """範圍向：全部引用皆可解析時，--gate 不得轉紅。"""
    p = repo / "features/f/docs/handoff/01_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("依 canon §5a 第 1 條與 canon §10.4，並見 R-G51。\n", encoding="utf-8")
    r = run(repo, "--gate")
    assert r.returncode == 0, r.stdout
    assert "PASS" in r.stdout


def test_gate_red_on_ambiguous_ref(repo):
    p = repo / "features/f/docs/handoff/01_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("依 canon §8.4 三分法。\n", encoding="utf-8")
    r = run(repo, "--gate")
    assert r.returncode == 1 and "FAIL" in r.stdout


# --- waiver（R-G57 修訂版，24 包 §C 裁定 2）-------------------------------
#
# 三向皆須實測（G-K ／ R-G9）：
#   waiver 內同一引用不轉紅、waiver 外之**同型**引用仍轉紅、
#   waiver 只減不增（新增一處即紅；清單內而現已消失者記 stale 不紅）。

def hist(repo, text: str) -> Path:
    """歷史檔（`docs/handoff/`）—— waiver 之對象。"""
    p = repo / "features/f/docs/handoff/07_round.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def active(repo, text: str) -> Path:
    """活躍檔 —— 不入 waiver，須改寫加前綴。"""
    p = repo / "features/f/RULINGS.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def test_is_historical_classification():
    assert cr.is_historical("features/f/docs/handoff/07_x.md")
    assert cr.is_historical("docs/fw036/upstream/23a_wp1.md")
    assert not cr.is_historical("features/f/RULINGS.md")
    assert not cr.is_historical("docs/fw036/FEATURE_ONBOARDING.md")


def test_emit_waiver_covers_historical_and_classifies_reason(repo):
    hist(repo, "依 canon §8.4 三分法。\n")
    active(repo, "依 canon §8.4 三分法。\n")
    r = run(repo, "--emit-waiver", "w.tsv")
    assert r.returncode == 0, r.stdout
    rows = (repo / "w.tsv").read_text(encoding="utf-8").strip().splitlines()
    assert rows[0].split("\t") == cr.WAIVER_COLUMNS
    reasons = {ln.split("\t")[0]: ln.split("\t")[5] for ln in rows[1:]}
    assert reasons["features/f/docs/handoff/07_round.md"] == "historical-record"
    assert reasons["features/f/RULINGS.md"] == "active-backlog"


def test_fenced_ruling_text_is_mention_not_waived(repo):
    """條文圍籬內之引用為「提及」，**不入 waiver 亦不計 FAIL**（27 包 §三）。

    27 包前此類以 `verbatim-ruling-text` 之 waiver 列處置；
    mention 判準生效後該特例被吸收 —— **一個不必豁免的東西不該出現在豁免清單裡。**
    """
    fo = repo / "docs/fw036/FEATURE_ONBOARDING.md"
    fo.write_text(FO_TEXT + "\n#### R-G52 — 引用制\n\n```\n"
                  "R-G52：裁決條文集中於各 feature 之 RULINGS.md 與 canon §8.4。\n```\n",
                  encoding="utf-8")
    r = run(repo, "--emit-waiver", "w.tsv")
    rows = (repo / "w.tsv").read_text(encoding="utf-8").strip().splitlines()[1:]
    assert not [ln for ln in rows if ln.startswith("docs/fw036/FEATURE_ONBOARDING")]
    assert run(repo, "--waiver", "w.tsv", "--gate").returncode == 0


def test_waived_ref_does_not_trip_gate(repo):
    """已 waive 之引用不得轉紅。"""
    hist(repo, "依 canon §8.4 三分法。\n")
    assert run(repo, "--gate").returncode == 1, "無 waiver 時須紅"
    run(repo, "--emit-waiver", "w.tsv")
    r = run(repo, "--waiver", "w.tsv", "--gate")
    assert r.returncode == 0, r.stdout
    assert "PASS" in r.stdout


def test_same_shape_ref_outside_waiver_still_trips(repo):
    """範圍向之對面：waiver 外之**同型**引用（同一 target，另一檔）仍須紅。"""
    hist(repo, "依 canon §8.4 三分法。\n")
    run(repo, "--emit-waiver", "w.tsv")
    active(repo, "依 canon §8.4 三分法。\n")          # waiver 產出後才出現
    r = run(repo, "--waiver", "w.tsv", "--gate")
    assert r.returncode == 1, r.stdout
    assert "FAIL" in r.stdout


def test_new_line_in_waived_file_still_trips(repo):
    """waiver 逐檔逐行 —— 同一檔新增一行同型引用仍須紅（只減不增）。"""
    hist(repo, "依 canon §8.4 三分法。\n")
    run(repo, "--emit-waiver", "w.tsv")
    hist(repo, "依 canon §8.4 三分法。\n又依 canon §8.2 之成分。\n")
    assert run(repo, "--waiver", "w.tsv", "--gate").returncode == 1


def test_stale_waiver_row_reported_not_failed(repo):
    """清單內而現已不存在者記 stale，只回報，不 FAIL。"""
    hist(repo, "依 canon §8.4 三分法。\n")
    run(repo, "--emit-waiver", "w.tsv")
    hist(repo, "依 FO §8.4 三分法。\n")               # 已改寫加前綴
    r = run(repo, "--waiver", "w.tsv", "--gate")
    assert r.returncode == 0, r.stdout
    assert "stale 1 列" in r.stdout


def test_missing_waiver_file_is_empty_not_error(repo):
    hist(repo, "依 canon §8.4 三分法。\n")
    r = run(repo, "--waiver", "nope.tsv", "--gate")
    assert r.returncode == 1 and "FAIL" in r.stdout


# --- 使用／提及（27 包 §三）------------------------------------------------
#
# 判準表自 26 上繳 §五-2 所載之**四次誤踩實例**歸納。四例逐一釘入（G-N），
# 並附範圍向：真正的援引不得被誤判為提及（R-G9）。

@pytest.mark.parametrize("line, expect, case", [
    # 例 1：複寫並列字串以說明前綴不及於後續節號（26 §五-0 初稿）
    ('初稿寫「`FO §8.1／§8.2／§8.8`」—— 前綴只涵蓋第一個', "mention", "圍籬（「」＋反引號）"),
    # 例 2：引述一句本身含規範性動詞之原文（V33 §C-2 加註）
    ('本條二款括號內「依 canon §8.7」所指為 FO §8.7', "mention", "圍籬優先於其內之動詞"),
    # 例 3：條文圍籬內（FO §9.2 之 R-G52 條文）—— 見 in_fence 之測試
    ('條文本體提及 canon 之 §9 → 已豁免', "mention", "詞彙標記「提及」"),
    # 例 4：更正文字又引述原句（26 §五-2 之第四次）
    ('上表原以「條文本體提及 canon §9」書之，該句自身遂成為命中', "mention", "圍籬"),
    # 範圍向：真正的援引
    ('依 canon §8.7 其下放包已落檔且入版控', "use", "規範性動詞引導"),
    ('違反 canon §5.1 之禁用動詞', "use", "規範性動詞引導"),
    ('見 canon §5a 之數字紀律', "use", "規範性動詞引導"),
    ('依 canon §8.4.3 填 PENDING: DR-20', "use", "規範性動詞引導"),
])
def test_usage_four_misfires_and_range_vector(line, expect, case):
    assert cr.usage_of(line, line.index("§"), False, False) == expect, case


def test_fence_and_superseded_regions_are_mention():
    line = "R-G52：裁決條文集中於各 feature 之 RULINGS.md 與 canon §9"
    assert cr.usage_of(line, line.index("§"), True, False) == "mention"
    assert cr.usage_of(line, line.index("§"), False, True) == "mention"
    assert cr.usage_of(line, line.index("§"), False, False) == "use"


def test_mention_is_not_counted_in_gate(repo):
    active(repo, '本條所指者為「依 canon §8.4」之三分法。\n')
    r = run(repo, "--gate")
    assert r.returncode == 0, r.stdout
    assert "mention     = 1" in r.stdout


def test_use_is_still_counted_in_gate(repo):
    active(repo, '依 canon §8.4 之三分法處置。\n')
    assert run(repo, "--gate").returncode == 1


# --- waiver 之內容雜湊鍵（27 包 §四）---------------------------------------
#
# 鍵之語意為「**這一行的這個引用**」。故須兩向都驗：
#   行移動  → 不失效（26 上繳 §五-1 之兩次假性新增，即由此消除）
#   內容變動 → 失效（內容改了本來就該重判）

def test_waiver_survives_line_movement(repo):
    """字面案例：於被豁免行之**上方**插入內容，waiver 不得失效。"""
    hist(repo, "依 canon §8.4 三分法。\n")
    run(repo, "--emit-waiver", "w.tsv")
    assert run(repo, "--waiver", "w.tsv", "--gate").returncode == 0
    hist(repo, "新增之前言一行。\n又一行。\n\n依 canon §8.4 三分法。\n")
    r = run(repo, "--waiver", "w.tsv", "--gate")
    assert r.returncode == 0, "行下移不得使 waiver 失效\n" + r.stdout
    assert "stale 0 列" in r.stdout


def test_waiver_fails_when_line_content_changes(repo):
    """反向：同一行之**內容**改動即失效 —— 內容改了本來就該重判。"""
    hist(repo, "依 canon §8.4 三分法。\n")
    run(repo, "--emit-waiver", "w.tsv")
    hist(repo, "依 canon §8.4 三分法，並加一句改變語意之補述。\n")
    assert run(repo, "--waiver", "w.tsv", "--gate").returncode == 1


def test_waiver_columns_carry_hash_and_advisory_line(repo):
    hist(repo, "依 canon §8.4 三分法。\n")
    run(repo, "--emit-waiver", "w.tsv")
    rows = (repo / "w.tsv").read_text(encoding="utf-8").strip().splitlines()
    assert rows[0].split("\t") == cr.WAIVER_COLUMNS
    c = rows[1].split("\t")
    assert len(c[3]) == 8 and all(ch in "0123456789abcdef" for ch in c[3])
    assert c[4].isdigit(), "line 欄保留為輔助欄（顯示用）"


def test_line_sha8_ignores_trailing_whitespace():
    assert cr.line_sha8("依 canon §8.4 三分法。") == cr.line_sha8("依 canon §8.4 三分法。   ")


def test_legacy_waiver_format_still_matches(repo, tmp_path):
    """遷移期相容：舊格式（無 line_sha8）之列仍應命中。"""
    hist(repo, "依 canon §8.4 三分法。\n")
    legacy = repo / "old.tsv"
    legacy.write_text(
        "source\tline\tkind\ttarget\treason\n"
        "features/f/docs/handoff/07_round.md\t1\tsection\t§8.4\thistorical-record\n",
        encoding="utf-8")
    assert run(repo, "--waiver", "old.tsv", "--gate").returncode == 0
