#!/usr/bin/env python3
"""Phase 4 batch 1 —— Test Set `Disclaimer Screen`（7 leaf）之 TC 生成。

依 12 包步驟 5 ＋ `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md`。

**R-PMH50**：每 leaf 必附 `source_clause`，**取自 PDF**（判讀基準，通則 3），
不取自 SYS1 匯出 —— 本輪之逐句對照證實 SYS1 之 7.1 **漏一子句**。

輸出：generated/batch01.json（**不寫回工作簿**）。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"

# --- PDF 原文子句（p8 SU1.)–SU3.)、p10 PITA6.1）------------------------------
# 逐字取自 `pdftotext -layout` 之 sandbox/spec.txt，空白正規化，未改字。
PDF = {
 "SU1_full": ("SU1.) When the vehicle’s driver door is closed a startup animation will be "
   "presented (3 sec), after the animation (3 sec) a splash screen is presented timeout "
   "(1.5 each). If ignition remains off after animation, screen is black. If ignition is "
   "turned on during animation, splash screen(s) are presented (1.5 sec timeout each). "
   "The disclaimer screen will be displayed as defined by legal/CFTS009. If the system is "
   "still loading, ‘loading…’ will be displayed. Once the system is ready ‘Loading…’ will "
   "be removed and display an Accept Button. The user is able to either press the Accept "
   "to go directly to their last mode screen or wait for the screen to timeout. No timeout "
   "is provided for Maserati applications, see CFTS009. Please see the official graphics "
   "release for the verbiage, which is defined by legal, to be displayed within the "
   "disclaimer screen."),
 "SU2": ("SU2.) For Maserati vehicles, while on the disclaimer screen the user will have "
   "access to their comfort controls. No timeout is provided for Maserati applications, "
   "see CFTS009."),
 "SU2_1": ("SU2.1) Do not display comfort controls on Maserati disclaimer screen when "
   "vehicle is equipped with lower comfort screen."),
 "SU3": ("SU3.) No pop-ups will appear until the disclaimer screen has been removed. If an "
   "item like a traffic announcement is received like on this screen the user will begin "
   "hearing the announcement in the background but will not see the pop-up until the "
   "disclaimer screen is removed."),
 "PITA6_1": ("PITA6.1: If radio is in Power Button Off state upon going from ignition in OFF "
   "position to ignition in ACC or RUN, HVAC popups shall display on the screen. Upon "
   "pressing power button to On state disclaimer screen shall be displayed (see SU6.) "
   "unless certain phone call scenarios have occurred."),
}

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
NEG = "負向測試 (Negative / Invalid)"

TCS = [
 # §4.3.1 —— `test_item` 上半一律為 **source_clause 之逐字子句**（13 包 §4.4）。
 # §11 —— UI 標籤用直雙引號；交付欄位無 markdown 標記（13 包 §4.5／§4.6）。
 # §5.1 —— procedure 用 `Check that`／`Read`／`Record`，不用 `observe`（§4.2）。
 # §5.2B/§5.5 —— Final Step 含驗證意圖；§10.5 —— 每條 >= 2 步（§4.1／§4.3）。
 dict(leaf="SWE1-HMI-PM-001-03", outline="7.1", src="SU1_full", dm=STATE, pri="P0",
   title="Loading indicator replaced by Accept button when the system becomes ready",
   item=("If the system is still loading, 'loading...' will be displayed. Once the system "
     "is ready 'Loading...' will be removed and display an Accept Button.\n\n"
     "(System-readiness transition on the disclaimer screen — distinguishes the "
     "not-ready state from the ready state)"),
   pre=["1. The disclaimer screen is displayed",
        "2. The system has not yet reported ready"],
   proc=["1. Read the disclaimer screen and record the loading indicator state",
         "2. Wait until the system reports ready",
         "3. Read the disclaimer screen and check that the \"Accept\" button is shown"],
   er=["1. \"loading...\" is displayed and no \"Accept\" button is shown",
       "2. The system reports ready",
       "3. \"Loading...\" is removed and the \"Accept\" button is shown"],
   reason=("**P0 —— §10.2 之 boot/recovery**：本條驗開機序列中免責畫面自載入態"
     "轉為就緒態並出現 Accept；其失效使開機停在載入畫面而無從進入 last mode，"
     "即 recovery 路徑中斷。**非 P1** —— 其標的不是某一使用者功能，是開機本身。"
     "設計方法 STATE —— 標的為 not-ready → ready 之狀態轉換及其顯示差異。"
     "§4.3.1：test_item 上半為 source_clause 之逐字子句。"
     "§8.5：pre-condition 不含 Maserati 與否（本行為與變體無關，13 包 §4.8）。"
     "source_clause 取自 PDF p8 之 SU1.)（R-PMH50）。"),
   axis="就緒狀態：not ready vs ready"),

 dict(leaf="SWE1-HMI-PM-001-04", outline="7.1", src="SU1_full", dm=FUNC, pri="P0",
   title="Accept press goes directly to the last mode screen",
   item=("The user is able to either press the Accept to go directly to their last mode "
     "screen or wait for the screen to timeout.\n\n"
     "(Accept 按壓路徑 —— 與 -003 之逾時路徑成對)"),
   pre=["1. The disclaimer screen is displayed with the \"Accept\" button shown",
        "2. The system has reported ready"],
   proc=["1. Read the disclaimer screen and record which screen is displayed",
         "2. Press the \"Accept\" button and check that the last mode screen is displayed"],
   er=["1. The disclaimer screen is displayed with the \"Accept\" button",
       "2. The disclaimer screen is removed and the last mode screen is displayed"],
   reason=("**P0 —— boot/recovery**：Accept 為離開免責畫面之主動路徑，"
     "且**於 Maserati 為唯一路徑** —— -004 已載明 Maserati 不提供逾時，"
     "故 Accept 失效使 Maserati 車輛之開機序列無法完成。"
     "⚠ R-PMH59：本條與 -003（逾時路徑，P1）之級差**來源在此** —— "
     "Accept 之失效有無替代路徑**視變體而定**（Maserati 無），"
     "逾時之失效則恆有 Accept 可替。"
     "前一輪之依據「唯一主動路徑，其失效即無法進入 last mode screen」"
     "**於非 Maserati 不成立**（逾時仍在），已改寫（15 包 §3.1）。"
     "依 profile §4「不同觸發即拆分」自 leaf 001-04 拆出 —— "
     "「按 Accept」與「等待逾時」為兩個觸發（見 -003）。"
     "§4.3.1：test_item 上半為 source_clause 之逐字整句。"
     "§8.5：不設 Maserati 條件 —— Accept 按壓於 Maserati 亦成立（13 包 §4.8）。"
     "source_clause 取自 PDF p8 之 SU1.)（R-PMH50）。"),
   axis="觸發路徑：按壓 Accept（對 -003 之逾時路徑）"),

 dict(leaf="SWE1-HMI-PM-001-04", outline="7.1", src="SU1_full", dm=STATE, pri="P1",
   title="Disclaimer screen times out without user input on a non-Maserati application",
   item=("The user is able to either press the Accept to go directly to their last mode "
     "screen or wait for the screen to timeout.\n\n"
     "(逾時路徑 —— 與 -002 之 Accept 按壓路徑成對)"),
   pre=["1. The vehicle is a non-Maserati application",
        "2. The disclaimer screen is displayed with the \"Accept\" button shown",
        "3. The system has reported ready"],
   proc=["1. Read the screen and record that the disclaimer screen is displayed",
         "2. Press no hard key and no \"Accept\" button until the screen changes",
         "3. Read the screen and check that the last mode screen is displayed"],
   er=["1. The disclaimer screen is displayed with the \"Accept\" button",
       "2. No user input is given while the disclaimer screen times out",
       "3. The last mode screen is displayed"],
   reason=("**P1 —— 主要功能邏輯**（非 P0）：逾時為離開免責畫面之被動路徑；"
     "其失效使自動離開路徑失效，**惟 Accept 路徑仍在**（-002 已驗），"
     "**開機仍可完成**，故不落 boot/recovery 之射程。"
     "⚠ R-PMH59 —— 前一輪判 P0，其依據為「無人操作之車輛永遠停在免責畫面」，"
     "**該依據與 -004 相矛盾**：-004 已載明 Maserati 之正常設計即為無逾時、"
     "須按 Accept，且判該情形為可接受（P1）；則逾時失效之結果**恰等同 "
     "Maserati 之正常運作**，「永遠停住」不成立。採 15 包 §3.2 之案（甲）降 P1。"
     "同 leaf 之第二條（profile §4 之不同觸發，見 -002）。"
     "設計方法 STATE —— 標的為逾時所引發之狀態離開。"
     "⚠ §8.4.1 不造值：**規格未載逾時之秒數**，亦**未言逾時等同 Accept** —— "
     "本條只斷言「畫面移除並顯示 last mode screen」，"
     "**不斷言其等同 Accept**（13 包 §4.4 之更正）。"
     "⚠ §8.5：pre-condition 之 non-Maserati **是必要的** —— 逾時本身即 Maserati "
     "之差異點。步驟 2 之「不按任何硬鍵」係因 PDF SU9.1 載按 Power Off／Screen Off "
     "會重設逾時，而該子句於 SYS1 缺失（A-PMH14），故自 PDF 取之。"
     "source_clause 取自 PDF p8 之 SU1.)（R-PMH50）。"),
   axis="觸發路徑：等待逾時（對 -002 之 Accept 按壓路徑）"),

 dict(leaf="SWE1-HMI-PM-001-05", outline="7.1", src="SU1_full", dm=NEG, pri="P1",
   title="Maserati disclaimer screen provides no timeout",
   item=("No timeout is provided for Maserati applications, see CFTS009.\n\n"
     "(Maserati 變體之負向側 —— 逾時不得發生，與 -003 之非 Maserati 逾時路徑相對)"),
   pre=["1. The vehicle is a Maserati application",
        "2. The disclaimer screen is displayed with the \"Accept\" button shown",
        "3. The system has reported ready"],
   proc=["1. Press no hard key and no \"Accept\" button",
         "2. Wait longer than the non-Maserati timeout, then read the screen",
         "3. Press the \"Accept\" button and check that the last mode screen is displayed"],
   er=["1. No user input is given",
       "2. The disclaimer screen is still displayed and has not timed out",
       "3. The disclaimer screen is removed and the last mode screen is displayed"],
   reason=("**P1 —— 主要功能邏輯**（非 P0）：本條驗 Maserati 之逾時**不**發生。"
     "其失效之後果為畫面提前消失，而 Accept 路徑仍在（-002 已驗），"
     "**開機仍可完成**，故不落 boot/recovery 之射程。"
     "設計方法 NEG —— 標的為「逾時**不**發生」。"
     "變體詞 Maserati 逐字取自規格（profile §3.2）。"
     "⚠ §8.4.1 不造值：規格未給任一秒數，故步驟 1 以「長於非 Maserati 之逾時」表述。"
     "source_clause 取自 PDF p8 之 SU1.)（R-PMH50）。"),
   axis="變體：Maserati（無逾時），對 -003 之非 Maserati 逾時"),

 dict(leaf="SWE1-HMI-PM-003", outline="7.2", src="SU2", dm=FUNC, pri="P1",
   title="Maserati disclaimer screen exposes the comfort controls",
   item=("SU2.) For Maserati vehicles, while on the disclaimer screen the user will have "
     "access to their comfort controls.\n\n"
     "(Maserati 且未配備 lower comfort screen —— 與 -006 之已配備情形成對)"),
   pre=["1. The vehicle is a Maserati application",
        "2. The vehicle is not equipped with the lower comfort screen",
        "3. The disclaimer screen is displayed"],
   proc=["1. Read the disclaimer screen and check that the comfort controls are displayed",
         "2. Operate one of the comfort controls and check that it responds to the input"],
   er=["1. The comfort controls are displayed on the disclaimer screen",
       "2. The operated comfort control responds to the input"],
   reason=("**P1 —— 主要功能邏輯**（非 P0）：comfort controls 於免責畫面之可及性"
     "為便利性功能，其失效不阻斷開機亦無安全後果。"
     "依 profile §4「變體即拆分」與 -006 成對 —— "
     "本條為未配備 lower comfort screen 之情形。"
     "§4.3.1：test_item 上半為 source_clause 之逐字整句。"
     "source_clause 取自 PDF p8 之 SU2.)（R-PMH50）。"),
   axis="配備：未配備 lower comfort screen，對 -006 之已配備"),

 dict(leaf="SWE1-HMI-PM-004", outline="7.3", src="SU2_1", dm=NEG, pri="P2",
   title="Comfort controls suppressed on Maserati disclaimer when the lower comfort screen is fitted",
   item=("SU2.1) Do not display comfort controls on Maserati disclaimer screen when "
     "vehicle is equipped with lower comfort screen.\n\n"
     "(Maserati 且已配備 lower comfort screen —— 與 -005 之未配備情形成對)"),
   pre=["1. The vehicle is a Maserati application",
        "2. The vehicle is equipped with the lower comfort screen",
        "3. The disclaimer screen is displayed"],
   proc=["1. Read the disclaimer screen and record which controls are displayed on it",
         "2. Check that the comfort controls are not among the controls recorded in step 1"],
   er=["1. The controls displayed on the disclaimer screen are recorded",
       "2. The comfort controls are not displayed on the disclaimer screen"],
   reason=("**P2 —— 次要／支援功能**：本條驗配備 lower comfort screen 時 comfort "
     "controls **不**顯示；其失效為多顯示一組重複控制，**對主要功能之影響有限**"
     "（§10.2 之 P2 定義）。**與 -005 不同級** —— 該條驗功能之存在，本條驗其抑制。"
     "設計方法 NEG —— 標的為「不顯示」。"
     "與 -005 為 profile §4 之變體對（配備 vs 未配備 lower comfort screen）。"
     "§10.5：拆為 record 與 check 兩步，不以單步交付。"
     "source_clause 取自 PDF p8 之 SU2.1)（R-PMH50）。"),
   axis="配備：已配備 lower comfort screen，對 -005 之未配備"),

 dict(leaf="SWE1-HMI-PM-005", outline="7.4", src="SU3", dm=FUNC, pri="P1",
   title="Pop-ups withheld until the disclaimer screen is removed while its audio still plays",
   item=("SU3.) No pop-ups will appear until the disclaimer screen has been removed. If an "
     "item like a traffic announcement is received like on this screen the user will "
     "begin hearing the announcement in the background but will not see the pop-up until "
     "the disclaimer screen is removed.\n\n"
     "(同一觸發之兩個必然後果 —— 視覺抑制與音訊照常，依 §5.7 不拆)"),
   pre=["1. The disclaimer screen is displayed",
        "2. A traffic announcement is available to be received"],
   proc=["1. Deliver a traffic announcement while the disclaimer screen is displayed",
         "2. Read the screen and the audio output and record both",
         "3. Remove the disclaimer screen and check that the pop-up is displayed"],
   er=["1. The traffic announcement is delivered",
       "2. The announcement is heard in the background and no pop-up is displayed",
       "3. The traffic announcement pop-up is displayed"],
   reason=("**P1 —— 主要功能邏輯**（非 P0）：pop-up 抑制影響免責畫面之可讀性，"
     "而免責畫面為 legal 要求（`as defined by legal/CFTS009`）——"
     "**惟其失效不阻斷開機**，故不落 boot/recovery。"
     "依 profile §4／canon §5.7「同一觸發之多個必然後果不拆」 —— "
     "「不顯示 pop-up」與「音訊照常播放」為同一觸發之兩個必然後果，寫為同條之多行 ER。"
     "⚠ R-PMH59 —— 本條與 -008（P0）之**級差來源**：**遮蔽 ≠ 未顯示**。"
     "-008 之失效使免責畫面**根本未出現**，系統以**未取得使用者確認**之狀態"
     "進入 last mode；本條之失效使 pop-up **疊在**免責畫面上，"
     "**畫面仍在、Accept 仍可按、確認仍可取得**。"
     "對 -001（P0）亦然：-001 之失效使 Accept 按鈕**永不出現**，主動路徑消失；"
     "本條之失效不影響任一離開路徑（16 包 §三）。"
     "§4.3.1：test_item 上半為 source_clause 之逐字整段。"
     "source_clause 取自 PDF p8 之 SU3.)（R-PMH50）。"),
   axis="同一觸發之兩後果：視覺抑制 ＋ 音訊照常"),

 dict(leaf="SWE1-HMI-PM-022-02", outline="10.4", src="PITA6_1", dm=STATE, pri="P0",
   title="Power button to On displays the disclaimer screen",
   item=("Upon pressing power button to On state disclaimer screen shall be displayed "
     "(see SU6.) unless certain phone call scenarios have occurred.\n\n"
     "(自 Power Button Off 轉 On 之進入路徑 —— 與 7.1 之開機序列進入路徑區辨)"),
   pre=["1. The radio is in Power Button Off state",
        "2. The ignition has gone from the OFF position to ACC or RUN",
        "3. No phone call scenario is in progress"],
   proc=["1. Read the screen and record the radio power state",
         "2. Press the power button to change the radio to On state",
         "3. Read the screen and check that the disclaimer screen is displayed"],
   er=["1. The radio is recorded as being in Power Button Off state",
       "2. The radio changes to On state",
       "3. The disclaimer screen is displayed"],
   reason=("**P0 —— boot/recovery**：本條驗自 Power Button Off 轉 On 時免責畫面"
     "之顯示；免責畫面為 legal 要求（`as defined by legal/CFTS009`），"
     "其未顯示即以未取得使用者確認之狀態進入 last mode。"
     "設計方法 STATE —— 標的為 Power Button Off → On 之狀態轉換"
     "及其畫面。⚠ §8.4.1 不造值：規格之 unless certain phone call scenarios have "
     "occurred **未列舉該等情境**，故 pre-condition 只寫「無通話情境進行中」，"
     "**不斷言其例外之內容**；該例外之列舉屬 10.6（Power Off Behavior 組），不在本批。"
     "§4.3.1：test_item 上半為 source_clause 之逐字整句。"
     "source_clause 取自 PDF p10 之 PITA6.1（R-PMH50）。"),
   axis="進入路徑：Power Button Off → On"),
]


LEVEL = re.compile(r"^\*\*(P[0-3])\b")


def self_check() -> list[str]:
    """`pri` 欄與 `reason` 首句所稱之級別須一致。

    14 包曾改 `-008` 之 reasoning 而未改其 `pri` 欄 —— 該錯由本檢查抓到
    （R-PMH41：驗證標的須為所欲狀態，非其代理）。本輪將其落為固定步驟。
    """
    bad = []
    for n, t in enumerate(TCS, 1):
        m = LEVEL.match(t["reason"])
        if not m:
            bad.append(f"-{n:03d} reasoning 首句未以 **P?** 起首")
        elif m.group(1) != t["pri"]:
            bad.append(f"-{n:03d} pri={t['pri']} 而 reasoning 稱 {m.group(1)}")
    return bad


def main() -> None:
    bad = self_check()
    if bad:
        raise SystemExit("priority／reasoning 不一致：\n  " + "\n  ".join(bad))
    out = []
    for n, t in enumerate(TCS, 1):
        out.append({
            "tc_id": f"NR1L-DisclaimerScreen-{n:03d}",
            "leaf_id": t["leaf"],
            "test_group": "Disclaimer screen",          # R-PMH13，小寫 s
            "test_set": "Disclaimer Screen",            # R-PMH36，大寫 S
            "tc_title": t["title"],
            "test_item": t["item"],
            "pre_conditions": "\n".join(t["pre"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join(t["proc"]),
            "expected_result": "\n".join(t["er"]),
            "specification_reference": f"{SPEC}_{t['outline']}",
            "design_method": t["dm"],
            "priority": t["pri"],
            "functional_safety": "NA",
            "estimated_test_time": "",                  # profile §3.6 留白
            "vehicle_models": "",                       # profile §3.8 留白
            "remarks": "",
            "reasoning": t["reason"],
            "distinguishing_axis": t["axis"],
            "source_clause": PDF[t["src"]],             # R-PMH50 —— 取自 PDF
            "source_clause_origin": ("spec_pdf p8" if t["src"] != "PITA6_1"
                                     else "spec_pdf p10"),
        })
    doc = {
        "batch": "batch01",
        "feature": "power_moding",
        "test_group": "Disclaimer screen",
        "test_set": "Disclaimer Screen",
        "handoff": "docs/handoff/12_phase4_batch1.md",
        "profile": "docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md",
        "selection": ("Test Set `Disclaimer Screen` 之 7 leaf（R-PMH36 之 Layer 2 定版）。"
                      "**8 條 TC** —— `SWE1-HMI-PM-001-04` 依 profile §4「不同觸發即拆分」"
                      "拆為 2 條（按 Accept／等待逾時）。"),
        "tc_id_status": "provisional",
        "source_clause_basis": ("R-PMH50 —— 取自 spec_pdf（判讀基準，通則 3）。"
                                "**不取自 SYS1 匯出** —— 本輪逐句對照證實其 7.1 漏一子句。"),
        "write_back": "凍結 —— 本批只產出 JSON，不寫回工作簿",
        "tcs": out,
    }
    p = ROOT / "generated" / "batch01.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {p} — {len(out)} TC（自 7 leaf）")


if __name__ == "__main__":
    main()
