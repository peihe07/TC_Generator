"""lint036 檢查 A–N 之單元測試（每項一正一反例）。"""

from __future__ import annotations

import sys
from pathlib import Path

import openpyxl
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import lint036  # noqa: E402

FIELD_KEYS = ("test_set", "test_item", "pre", "input", "proc", "er", "spec", "author")


def make_fields(**overrides) -> dict[str, str]:
    """建立一列預設全合規的欄位值，再套用覆寫。"""
    base = {
        "test_set": "General Anatomy",
        "test_item": "The system shall display the Media screen\n(Media screen shown)",
        "pre": "1. The Home screen is displayed",
        "input": "NA",
        "proc": "1. Press \"Media\" on the Main Menu Bar",
        "er": "1. The Media screen is displayed",
        "spec": "Media_HMI_Logic_R1.docx",
        "author": "PeiPYHsu",
    }
    base.update(overrides)
    return base


def run(**overrides) -> list[str]:
    """跑單列檢查，回傳觸發的檢查代號清單。"""
    violations = lint036.check_row(make_fields(**overrides), 10, "TC-001",
                                   lint036.DEFAULT_LENGTH_LIMIT)
    return [v.check for v in violations]


def test_clean_row_has_no_violations():
    """預設列應零違規（作為所有反例之基準）。"""
    assert run() == []


# --- header 定位 -------------------------------------------------------------


def build_sheet(header_row: int):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Test Case Specification 測試用例規範"
    headers = ["No.#\n序號", "Requirement or Design ID\n需求ID", "Test Case ID\n測試用例ID",
               "Test Group\n測試組", "Test Set\n測試集", "Test Item\n測試項目",
               "Pre-Conditions\n先前條件", "Input Test Data\n輸入條件",
               "Test procedure\n測試程序", "Expected Result\n預期結果",
               "Specification Reference \n規格參考", "Test Case Author\n測試案例作者"]
    for col, value in enumerate(headers, start=1):
        ws.cell(row=header_row, column=col, value=value)
    return ws


def test_find_header_row_locates_anchor():
    """header 定位：找到含 Specification Reference 之列。"""
    assert lint036.find_header_row(build_sheet(9)) == 9


def test_find_header_row_raises_when_absent():
    """header 定位：前 15 列無錨點時報錯。"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.cell(row=1, column=1, value="無關內容")
    with pytest.raises(ValueError):
        lint036.find_header_row(ws)


def test_build_column_map_covers_all_field_keys():
    """欄位對照：八個欄位鍵全數命中，且 tc_id/req_id 可定位。"""
    ws = build_sheet(9)
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    columns = lint036.build_column_map(list(rows[8]))
    assert set(lint036.FIELD_HEADERS) <= set(columns)
    assert columns["tc_id"] == 2
    assert columns["req_id"] == 1
    assert columns["test_set"] == 4


# --- A–N 逐項 ----------------------------------------------------------------


def test_a_flags_forbidden_verb():
    assert "A" in run(proc="1. Observe the Media screen.")


def test_a_allows_imperative_step():
    assert "A" not in run(proc="1. Press the Media icon.")


def test_b_flags_modal_in_expected_result():
    assert "B" in run(er="1. The screen shall be displayed.")


def test_b_exempts_modal_inside_quotes():
    assert "B" not in run(er='1. The label "system shall reboot" is displayed.')


def test_c_flags_hedge_word():
    assert "C" in run(test_item="The system displays the screen properly.\n(shown)")


def test_c_allows_specific_wording():
    assert "C" not in run(test_item="The system displays the screen.\n(shown)")


def test_d_flags_powered_on_precondition():
    assert "D" in run(pre="1. The HU is powered on.")


def test_d_flags_action_verb_in_precondition():
    assert "D" in run(pre="1. Insert a USB drive.")


def test_d_allows_state_precondition():
    assert "D" not in run(pre="1. The Home screen is displayed.")


def test_e_flags_step_count_mismatch():
    assert "E" in run(proc="1. Press A.\n2. Press B.", er="1. Screen shown.")


def test_e_allows_matching_step_counts():
    assert "E" not in run(proc="1. Press A.\n2. Press B.",
                          er="1. Screen A shown.\n2. Screen B shown.")


def test_f_flags_bracket_placeholder():
    assert "F" in run(proc="1. Press [Media] on the bar.")


def test_f_allows_quoted_label():
    assert "F" not in run(proc='1. Press "Media" on the bar.')


def test_g_flags_empty_test_set():
    assert "G" in run(test_set="   ")


def test_g_allows_filled_test_set():
    assert "G" not in run(test_set="General Anatomy")


def test_h_flags_vague_expected_result():
    assert "H" in run(er="1. The screen works normally.")


def test_h_allows_concrete_expected_result():
    assert "H" not in run(er="1. The Media screen is displayed.")


def test_i_flags_missing_paren_half():
    assert "I" in run(test_item="The system shall display the Media screen.")


def test_i_allows_paren_line():
    assert "I" not in run(test_item="The system displays it.\n(Media screen shown)")


def test_i_allows_trailing_paren():
    assert "I" not in run(test_item="The system displays it (Media screen shown)")


def test_i_sibling_flags_verbatim_duplicate_paren_lines():
    rows = [
        (10, "TC-001", "REQ-1", "Item A.\n(same paren)"),
        (11, "TC-002", "REQ-1", "Item B.\n(same paren)"),
    ]
    assert len(lint036.check_sibling_parens(rows)) == 2


def test_i_sibling_allows_distinct_paren_lines():
    rows = [
        (10, "TC-001", "REQ-1", "Item A.\n(paren one)"),
        (11, "TC-002", "REQ-1", "Item B.\n(paren two)"),
    ]
    assert lint036.check_sibling_parens(rows) == []


def test_j_flags_lowercase_line_start():
    assert "J" in run(er="1. the Media screen is displayed")


def test_j_exempts_numeric_first_token():
    """00b 修訂 2：行號後第一個 token 為數字者整行豁免，不再往後尋找。"""
    assert "J" not in run(er="4. 5 sources are displayed in the Source Menu")


def test_j_exempts_symbol_first_token():
    """第一個 token 以 $ 開頭者整行豁免。"""
    assert "J" not in run(proc="1. $Telematic_Power$ is read")


def test_j_exempts_whitelisted_token():
    assert "J" not in run(proc="1. adb shell dumpsys media.")


def test_j_exempts_camel_case_token():
    assert "J" not in run(proc="1. mediaPlayer is invoked.")


def test_j_exempts_dotted_call():
    assert "J" not in run(proc="1. media.play() is invoked.")


def test_k_flags_cjk_characters():
    assert "K" in run(er="1. 媒體畫面顯示.")


def test_k_allows_ascii_only():
    assert "K" not in run(er="1. The Media screen is displayed")


def test_k_covers_test_set_column():
    """00b 修訂 3：test_set 屬六欄之一。"""
    assert "K" in run(test_set="一般外觀")


def test_k_excludes_spec_column():
    """00b 修訂 3：spec 不屬六欄。"""
    assert "K" not in run(spec="媒體規格_R1.docx")


def test_k_excludes_author_column():
    """00b 修訂 3：author 不屬六欄。"""
    assert "K" not in run(author="許沛")


def test_l_flags_overlong_upper_half():
    long_item = " ".join(["word"] * 60) + ".\n(paren)"
    assert "L" in run(test_item=long_item)


def test_l_ignores_paren_lines_in_length():
    item = " ".join(["word"] * 40) + ".\n(" + " ".join(["x"] * 40) + ")"
    assert "L" not in run(test_item=item)


def test_m_flags_empty_required_column():
    assert "M" in run(spec="")


def test_m_allows_na_placeholder():
    assert "M" not in run(spec="NA")


def test_m_allows_pending_marker():
    assert "M" not in run(spec="PENDING: awaiting spec id")


def test_n_flags_trailing_period():
    """00b 修訂 1：命中 `[.。]$` 即違規（canon §11 禁尾句號）。"""
    assert "N" in run(er="1. The Media screen is displayed.")


def test_n_flags_trailing_cjk_period():
    assert "N" in run(er="1. The Media screen is displayed。")


def test_n_allows_line_without_period():
    assert "N" not in run(er="1. The Media screen is displayed")


def test_n_allows_na_placeholder():
    """`NA` 不以句號結尾，正確方向下零命中（推翻 00 包所稱 M/N 衝突）。"""
    assert "N" not in run(input="NA")


def test_n_exempts_shell_command_line():
    assert "N" not in run(proc="1. Run the command\n$ adb shell dumpsys media.")


def test_n_exempts_indented_continuation():
    assert "N" not in run(proc="1. Press the icon\n    continued fragment.")


# --- 00c 裁定 1：N 子步驟納入，且不得外溢至 E ---


def test_n_flags_lettered_substep_with_period():
    """a./b./c. 縮排子步驟為實質測試步驟（canon §6.1），尾句號計入 N。"""
    proc = "1. Power cycle the HU\n   a. Hold H/K[POWER] for 2 secs."
    assert "N" in run(proc=proc)


def test_n_flags_lettered_substep_with_paren_marker():
    """`a)` 形式之子步驟同樣納入 N 行定義。"""
    assert "N" in run(proc="1. Power cycle the HU\n   a) Hold POWER for 2 secs.")


def test_n_still_exempts_true_continuation():
    """真續行（無 a./b. 標記）維持豁免。"""
    proc = "1. Press the icon\n   duplicate contact entry is created."
    assert "N" not in run(proc=proc)


def test_e_ignores_lettered_substeps():
    r"""迴歸：E 沿用全域 `^\s*\d+[.)]`，不因 N 行定義擴充而漂移。"""
    proc = ("1. Power cycle the HU\n   a. Hold POWER for 2 secs\n"
            "   b. Press MUTE for 1 sec\n2. Observe nothing")
    er = "1. The HU restarts\n2. The screen is shown"
    violations = lint036.check_row(make_fields(proc=proc, er=er), 10, "TC-001",
                                   lint036.DEFAULT_LENGTH_LIMIT)
    assert "E" not in [v.check for v in violations]


def test_numbered_lines_helper_excludes_lettered_substeps():
    """全域 numbered_lines() 不得納入 a./b. —— N 之擴充限定於 n_exempt()。"""
    text = "1. Step one\n   a. Sub step\n2. Step two"
    assert len(lint036.numbered_lines(text)) == 2
    assert lint036.N_STEP_LINE.match("   a. Sub step")
    assert not lint036.NUMBERED_LINE.match("   a. Sub step")


# --- 03 §三 R-6：P 訊號記法之施用範圍 ---


def test_p_flags_legacy_can_notation_in_procedure():
    """作者生成之四欄仍用兩段記法者為違規（R-1）。"""
    assert "P" in run(proc="1. Send STATUS_LIN.Batt_ST_Crit to the bus")


def test_p_allows_three_part_notation():
    assert "P" not in run(proc="1. Send Batt_ST_Crit in STATUS_LIN on BH-CAN to the bus")


def test_p_ignores_internal_signal_notation():
    """內部訊號 `X.Info`／`X.Req` 之 message 段含小寫，不得誤判為 CAN。"""
    assert "P" not in run(er="1. TLM_Status.Info reads \"Standby\"",
                          pre="1. Phone_Call.Info reads \"Not_Active\"")


def test_p_ignores_proxi_parameter():
    """PROXI 層 `$X$` 無兩段記法，且不得被套三件組（A-PM03）。"""
    assert "P" not in run(proc="1. Read $Radio_Theme$ on the bench")


def test_p_exempts_test_item_verbatim_upper_half():
    """R-6：test_item 上半為需求原句 verbatim，其記法保留來源原文。"""
    item = ("When STATUS_LIN.PN14_LS_Actv is received the TLM shall react\n"
            "(read the volume -> The maximum volume is reduced)")
    assert "P" not in run(test_item=item)


def test_p_flags_legacy_notation_in_test_item_paren():
    """R-6：括號下半屬作者生成內容，仍受 R-1 規制。"""
    item = ("The TLM shall react to the load shed signal\n"
            "(drive STATUS_LIN.PN14_LS_Actv -> The maximum volume is reduced)")
    assert "P" in run(test_item=item)


# --- 計數口徑 ---


def test_row_counts_distinguish_line_and_row_basis():
    """同一列多行違規：行計 > 列計。"""
    result = lint036.SheetResult(sheet="s", header_row=9, data_rows=1)
    result.violations = lint036.check_row(
        make_fields(er="1. the screen is shown\n2. the icon is shown"),
        10, "TC-001", lint036.DEFAULT_LENGTH_LIMIT)
    assert lint036.count_by_check([result])["J"] == 2
    assert lint036.rows_by_check([result])["J"] == 1


def test_every_check_has_status_and_granularity():
    """報告表頭所需之兩張對照表須涵蓋全部檢查。"""
    assert set(lint036.CHECK_STATUS) == set(lint036.CHECK_ORDER)
    assert set(lint036.CHECK_GRANULARITY) == set(lint036.CHECK_ORDER)
    assert set(lint036.CHECK_TITLES) == set(lint036.CHECK_ORDER)


# --- 報告命名 ----------------------------------------------------------------


def test_report_stem_strips_date_and_annotation():
    path = Path("FM-WI-FSM-036-A01 x_SWQT_CFTS012_DealerMode_20260417(done).xlsx")
    assert lint036.report_stem(path) == "CFTS012_DealerMode"
