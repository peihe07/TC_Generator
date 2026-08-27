"""lint_docs036（docs_structure）之單元測試 —— 每項一正一反例。

檢查對象為治理文件而非工作簿；其存在理由是 A-PM17：
落檔位置表以「同上」串接指涉時，插入列會靜默改變其後各列之指涉對象，
而該類缺陷於工作簿層無從察覺。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import lint_docs036 as ld  # noqa: E402

LEDGER_OK = """# 裁決台帳

| 編號 | 日期 | 標題 | 狀態 | 出處 | 範圍 |
|---|---|---|---|---|---|
| R-1 | 2026-08-21 | 甲條 | ACTIVE | 01 | 全案 |
| R-2 | 2026-08-21 | 乙條 | SUPERSEDED | 02 | 全案 |

## 條文落檔位置

| 編號 | 條文全文所在 |
|---|---|
| R-1 | `docs/a.md` §1 |
| R-2 | `docs/b.md` §2 |
"""


def write(tmp_path: Path, ledger: str = LEDGER_OK, dr: str = "", anom: str = "") -> Path:
    (tmp_path / "docs/fw036").mkdir(parents=True, exist_ok=True)
    (tmp_path / "features/power").mkdir(parents=True, exist_ok=True)
    (tmp_path / ld.LEDGER).write_text(ledger, encoding="utf-8")
    (tmp_path / "features/power/DATA_REQUESTS.md").write_text(dr, encoding="utf-8")
    (tmp_path / "features/power/ANOMALIES.md").write_text(anom, encoding="utf-8")
    return tmp_path


def checks(findings) -> list[str]:
    return [f.check for f in findings]


# --- 台帳 --------------------------------------------------------------------


def test_clean_ledger_passes(tmp_path: Path) -> None:
    assert ld.check_ledger(write(tmp_path)) == []


def test_illegal_status_value(tmp_path: Path) -> None:
    bad = LEDGER_OK.replace("| ACTIVE | 01 |", "| 生效中 | 01 |")
    assert "ledger_status" in checks(ld.check_ledger(write(tmp_path, bad)))


def test_empty_ruling_text(tmp_path: Path) -> None:
    bad = LEDGER_OK.replace("| 甲條 |", "|  |")
    assert "ledger_text" in checks(ld.check_ledger(write(tmp_path, bad)))


def test_series_gap_is_reported(tmp_path: Path) -> None:
    """撤回列不刪、不重編號（R-TM13）—— 跳號即代表有條文遺失登載。"""
    bad = LEDGER_OK.replace("| R-2 | 2026-08-21 | 乙條 | SUPERSEDED | 02 | 全案 |",
                            "| R-3 | 2026-08-21 | 丙條 | ACTIVE | 03 | 全案 |\n"
                            "| R-2 | 2026-08-21 | 乙條 | SUPERSEDED | 02 | 全案 |")
    bad = bad.replace("| R-2 | `docs/b.md` §2 |",
                      "| R-2 | `docs/b.md` §2 |\n| R-3 | `docs/c.md` §3 |")
    assert ld.check_ledger(write(tmp_path, bad)) == []
    gapped = bad.replace("| R-2 | 2026-08-21 | 乙條 | SUPERSEDED | 02 | 全案 |\n", "")
    gapped = gapped.replace("| R-2 | `docs/b.md` §2 |\n", "")
    assert "ledger_series" in checks(ld.check_ledger(write(tmp_path, gapped)))


def test_ruling_missing_from_location_table(tmp_path: Path) -> None:
    bad = LEDGER_OK.replace("| R-2 | `docs/b.md` §2 |\n", "")
    assert "ledger_location" in checks(ld.check_ledger(write(tmp_path, bad)))


def test_tongshang_chain_is_rejected(tmp_path: Path) -> None:
    """A-PM17 —— 「同上」串接於插入列時靜默改指。"""
    bad = LEDGER_OK.replace("| R-2 | `docs/b.md` §2 |", "| R-2 | 同上 §2 |")
    assert "ledger_location" in checks(ld.check_ledger(write(tmp_path, bad)))


def test_strikethrough_id_still_parsed(tmp_path: Path) -> None:
    """撤銷列以刪除線保留，其編號仍須參與連續性判定。"""
    struck = LEDGER_OK.replace("| R-2 | 2026-08-21 | 乙條 |",
                               "| ~~R-2~~ | 2026-08-21 | ~~乙條~~ |")
    struck = struck.replace("| R-2 | `docs/b.md` §2 |", "| ~~R-2~~ | 已撤銷 |")
    assert ld.check_ledger(write(tmp_path, struck)) == []


def test_r6b_suffix_form_is_legal(tmp_path: Path) -> None:
    ok = LEDGER_OK.replace("| R-2 | 2026-08-21 | 乙條 | SUPERSEDED | 02 | 全案 |",
                           "| R-2 | 2026-08-21 | 乙條 | SUPERSEDED | 02 | 全案 |\n"
                           "| R-6b | 2026-08-21 | 丙條 | ACTIVE | 06 | 全案 |")
    ok = ok.replace("| R-2 | `docs/b.md` §2 |",
                    "| R-2 | `docs/b.md` §2 |\n| R-6b | `docs/c.md` §6 |")
    assert "ledger_id" not in checks(ld.check_ledger(write(tmp_path, ok)))


# --- DR／ANOMALIES 之序列 ----------------------------------------------------


DR_OK = """| DR | 內容 |
|---|---|
| DR-PW1 | 甲 |
| DR-PW2 | 乙 |

| DR-PW3 | 丙 |
"""


def test_series_scan_does_not_skip_first_row_of_each_table(tmp_path: Path) -> None:
    """長條目常被空行切成獨立表格；跳過表首即會誤報跳號。"""
    root = write(tmp_path, dr=DR_OK)
    assert ld.check_series(root, "features/power/DATA_REQUESTS.md", "DR-PW") == []


def test_series_gap_in_dr(tmp_path: Path) -> None:
    root = write(tmp_path, dr=DR_OK.replace("| DR-PW2 | 乙 |\n", ""))
    assert "DR-PW_series" in checks(
        ld.check_series(root, "features/power/DATA_REQUESTS.md", "DR-PW"))


# --- 表格列格式 --------------------------------------------------------------


def test_row_missing_trailing_pipe(tmp_path: Path) -> None:
    root = write(tmp_path, dr="| DR-PW1 | 甲 | 尾管遺漏\n")
    assert "table_row" in checks(
        ld.check_malformed_rows(root, "features/power/DATA_REQUESTS.md"))


def test_well_formed_row_passes(tmp_path: Path) -> None:
    root = write(tmp_path, dr=DR_OK)
    assert ld.check_malformed_rows(root, "features/power/DATA_REQUESTS.md") == []


# --- R-POP10：前綴自動抽取（A-POP4 之處置）------------------------------------
#
# G-N —— 缺陷原文以字面釘入，不以當前語料為案例：下列 fixture 逐字寫死
# `A-POP` 與 `DR-POP` 兩個前綴。硬寫時代之清單為
# `("DR-PW", "A-PW", "A-PM")`，兩者皆不在其中，故本組 fixture 即
# A-POP4 之缺陷原文 —— 整輪 gate 全綠而該兩系列一次未受檢。
# repo 內 popup 之台帳日後如何改寫，都不影響本組測試之證明力。

ANOM_POP_GAP = """# ANOMALIES

| A | 內容 | 狀態 |
|---|---|---|
| A-POP1 | 甲 | RESOLVED |
| A-POP2 | 乙 | PENDING |
| A-POP9 | 丙 | PENDING |
"""

ANOM_POP_OK = ANOM_POP_GAP.replace("A-POP9", "A-POP3")

DR_POP_OK = """# DATA REQUESTS

| DR | 項目 |
|---|---|
| DR-POP1 | 甲 |
| DR-POP2 | 乙 |
"""


def test_未列於硬寫清單之前綴一樣受跳號檢查(tmp_path: Path) -> None:
    """A-POP4 之缺陷本體：`A-POP` 不在硬寫清單內，整輪不受檢而 gate 全綠。"""
    root = write(tmp_path, anom=ANOM_POP_GAP)
    found = ld.check_series(root, "features/power/ANOMALIES.md")
    assert "A-POP_series" in checks(found)
    # 回報之編號須是語料裡真的寫得出來的字串 —— `A-POP-3` grep 不到東西
    assert {f.where for f in found} == {"A-POP3", "A-POP4", "A-POP5",
                                        "A-POP6", "A-POP7", "A-POP8"}


def test_修正後不得再命中(tmp_path: Path) -> None:
    """G-N 之回歸向：同一 fixture 補齊連號後，同一支檢查須沉默。"""
    root = write(tmp_path, anom=ANOM_POP_OK, dr=DR_POP_OK)
    assert ld.check_series(root, "features/power/ANOMALIES.md") == []
    assert ld.check_series(root, "features/power/DATA_REQUESTS.md") == []


def test_硬寫時代之前綴不因改為自動抽取而漏檢(tmp_path: Path) -> None:
    """對照向：舊清單涵蓋得到的案例，新機制須同樣抓得到。"""
    root = write(tmp_path, dr=DR_OK.replace("| DR-PW2 | 乙 |\n", ""))
    assert "DR-PW_series" in checks(
        ld.check_series(root, "features/power/DATA_REQUESTS.md"))


def test_G_B_差集列出硬寫清單外之新受檢前綴(tmp_path: Path) -> None:
    root = write(tmp_path, anom=ANOM_POP_OK, dr=DR_POP_OK)
    seen, newly, skipped = ld.prefix_reconciliation(
        root, ["features/power/DATA_REQUESTS.md", "features/power/ANOMALIES.md"])
    assert seen == ["A-POP", "DR-POP"]
    assert newly == ["A-POP", "DR-POP"]
    # G-D —— 被略過之首格須報數；表頭 `A`／`DR` 兩格即為此處之被抑制條數
    assert skipped == 2


def test_前綴抽取不吞掉單字母系列(tmp_path: Path) -> None:
    """`R-27` 與 `A-POP4` 之分界：交替須讓單字母分支先試而後回溯。"""
    assert ld.RE_SERIES.match("R-27").group("prefix") == "R"
    assert ld.RE_SERIES.match("R-POP5").group("prefix") == "R-POP"
    assert ld.RE_SERIES.match("A-POP4").group("prefix") == "A-POP"
    assert ld.RE_SERIES.match("DR-PW3").group("prefix") == "DR-PW"
    assert ld.RE_SERIES.match("S3").group("prefix") == "S"
