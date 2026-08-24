"""VF230 pilot #2（W-VF68 §2.2）—— 10 條，seq 258–267。

取樣依上繳 V26 §3 之表（已核可），記於 `data/_vf230_pilot2_sel.json`。

**書寫形態之依據（W-VF68 §2.1 之查證，先於本檔呈現於上繳）**：
  1 訊號送出型之書寫式：**有先例，不回退**。
    首查只查 `propId`／`setProperty` 字樣（0 行），**其為查錯標的** ——
    真正該查者為「以顧客操作為刺激、斷言 HU 送出訊號」之書寫式。
    複查得 **154 個實例**，其式為**單一步驟**：
      P `… and check that MESSAGE.Signal = <raw> (<Label>) is transmitted`
      E `MESSAGE.Signal = <raw> (<Label>) is sent`
    例：`SWE1-VC-TwoStagesVentedSeatsManagement-045` step 3、
        `SWE1-VC-TwoStagesHeatedSeat-058` step 3。
    Android 屬性層之名詞（propId／setProperty）Part 1 確無，**不寫入 TC**。
  2 訊號上行型（CAN 刺激 ＋ 畫面斷言）：**有先例**（353 行 `Send CAN:`，
    如 `SWE1-VC-Stop-StartSystem-005`）。依先例，不回退。
  3 `displayed and modifiable`：Part 1 內 **0 行 —— 查無**。
    回退為 pilot #1 v4 之正向式，於 remarks 逐條具名。
  4 訊號送出型 318 條之二式比例：`MESSAGE.Signal` 式 189（59%）／兩式皆有 75
    （24%）／皆無 32（10%）／純 `propId` 式 22（7%）。本批 4 條為
    兩式皆有 2 ＋ `MESSAGE.Signal` 式 2 —— **純 propId 式之 22 條未涵蓋**，具名於上繳。
  5 「其他」殘餘 4 條：皆為 `TimeandDateSettings`，用 `<Name>.Info` 第三種訊號
    命名空間（非 `TELEMATIC_*`／`IPC_*`），故未落入訊號送出型。具名於上繳。

priority 不寫死（A-VF17）—— 由 `vf230_wvf45_priority` 之判準推得，
其為本檔之外之物，故驗證之依據不在被驗之物內。
"""
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FEAT / "scripts"))
import vf230_wvf45_priority as PR      # noqa: E402  判準之單一來源
import vf230_wvf61_pilot as P1         # noqa: E402  spec_refs() 之錨鏈

EP = "等價劃分 (Equivalence Partitioning, EP)"
FULLOP = "The HU is in the Full-Operation state"

# 回退之具名（V28 §2.1）——  形態 → 具名文字
FB_PROPID = ("書寫式**有先例，不回退**（W-VF68 §2.1 第 1 項之複查）：Part 1 有 "
             "154 個「顧客操作為刺激、斷言 HU 送出訊號」之實例，其式為單一步驟 "
             "`… and check that MESSAGE.Signal = <raw> (<Label>) is transmitted`／"
             "ER `… is sent`（如 `SWE1-VC-TwoStagesVentedSeatsManagement-045` "
             "step 3）。條文之 Android 屬性層名詞（propId／setProperty）"
             "Part 1 確無先例，**不寫入 TC**。")
BUS = ("FD-CAN8 is connected to the bus simulator with signal tracing enabled")
BUS_NOTE = ("匯流排前置沿用 Part 1 之式（`CAN-B is connected to the bus simulator "
            "with signal tracing enabled` 59 例／`BH-CAN …` 21 例），其命名依 DBC "
            "檔名（`PDT27_E2A_R4_BHCAN.dbc` → `BH-CAN`）。本批之訊號皆在 "
            "`PDT27_E2A_R5_FDCAN8.dbc`，依同一慣例推得 `FD-CAN8` —— "
            "**此為推得而非交付本逐字，具名待覆核**。")
FB_DISPMOD = ("**回退並具名**（W-VF68 §2.1 第 3 項）：`displayed and modifiable` "
              "之書寫形態於 Part 1 查無先例（0 行），"
              "故沿用 pilot #1 v4 之正向式。")

# 逐條之作者內容。priority／priority_class／test_set／spec_ref 不在此表內。
TCS = [
    dict(
        leaf="SWE1-VC-Blind Spot with Trailer Detection-046", seq=258, form="PROXI 型",
        title='Blind Spot with Trailer Detection is displayed and modifiable when '
              'Blindspot_Trailer_Detection is "Present"',
        item='If Blindspot_Trailer_Detection = [Present], the LTM or ETM shall display '
             'the Blind Spot with Trailer Detection customer setting to allow the '
             'customer the ability to modify the setting.',
        pre=[FULLOP,
             'PROXI $Blindspot_Trailer_Detection$ is set to "Present" '
             '(PENDING: DR-34)'],
        proc=['Power cycle the HU',
              'Open the Vehicle Settings menu and wait until it is fully rendered',
              'Read the Vehicle Settings menu and check that the "Blind Spot with '
              'Trailer Detection" customer setting is displayed',
              'Select the "Blind Spot with Trailer Detection" customer setting and '
              'check that its value can be changed'],
        er=['The HU completes start-up',
            'The Vehicle Settings menu is displayed',
            'The "Blind Spot with Trailer Detection" customer setting is displayed',
            'The value of the "Blind Spot with Trailer Detection" customer setting '
            'can be changed'],
        vsrc="0-CLAUSE", dr="DR-34",
        remarks='W1（R-VS47／R-VS71）：`Blindspot_Trailer_Detection` 之值域未見於 '
                'PROXI 表（DR-34 之 11 個參數之一），標 `PENDING: DR-34`。'
                '去 PENDING 後仍餘 4 個可執行步驟（≥2 ✅），且未解者為該參數之'
                '**值域全集**，而被驗之值 `"Present"` 由條文逐字帶出（0-CLAUSE），'
                '**非驗證標的**（✅）。',
        reason='值域來源 **0-CLAUSE**（R-VF13／R-VF60）—— 條文逐字：'
               '「If Blindspot_Trailer_Detection = [Present]」。'),
    dict(
        leaf="SWE1-VC-ParkSense-085", seq=259, form="PROXI 型",
        title='Park Sense is displayed and modifiable when CAN Node 24 is "Present"',
        item='If CAN Node 24 (PAM/CVADAS) = [Present], the LTM or ETM shall display '
             'the Park Sense customer setting to allow the customer the ability to '
             'modify the setting.',
        pre=[FULLOP,
             'PROXI $CAN_Node_24 (PAM/CVADAS)$ is set to "Present"'],
        proc=['Power cycle the HU',
              'Open the Vehicle Settings menu and wait until it is fully rendered',
              'Read the Vehicle Settings menu and check that the "Park Sense" '
              'customer setting is displayed',
              'Select the "Park Sense" customer setting and check that its value '
              'can be changed'],
        er=['The HU completes start-up',
            'The Vehicle Settings menu is displayed',
            'The "Park Sense" customer setting is displayed',
            'The value of the "Park Sense" customer setting can be changed'],
        vsrc="0-CLAUSE", dr="",
        remarks='PROXI 參數名之書寫形態：本條取條文逐字 `CAN Node 24 (PAM/CVADAS)`。'
                '**pilot #1 v4 內同類參數有二式**（seq 238 之 `$CAN_Node_82_PTGM$` '
                '底線式，seq 242 之 `$CAN_Node_27(ASM / ASCM)$` 括號式）—— '
                '已開 A-VF22，待裁示，本批不自行統一。',
        reason='值域來源 **0-CLAUSE** —— 條文逐字：'
               '「If CAN Node 24 (PAM/CVADAS) = [Present]」。'),
    dict(
        leaf="SWE1-VC-PowerLiftgate/TailgateAlert-018", seq=260, form="訊號送出型",
        title='TELEMATIC_VEHICLE_SETUP.PLGAlert_Req is sent as 0 (Off) when Power '
              'Liftgate Alert is disabled',
        item='When the customer chooses to disable the Power Liftgate Alert setting '
             'on the LTM or ETM, the HMI layer shall send the updated customer '
             'preference to the HW. When the HMI receives the value as [Off] via '
             'signal, $TELEMATIC_VEHICLE_SETUP.PLGAlert_Req$, Then the HMI shall '
             'display the Power Liftgate Alert status as Off.',
        pre=[FULLOP, BUS,
             'The "Power Liftgate Alert" customer setting is set to On'],
        proc=['Open the Vehicle Settings menu and wait until it is fully rendered',
              'Set the "Power Liftgate Alert" customer setting to Off and check that '
              'TELEMATIC_VEHICLE_SETUP.PLGAlert_Req = 0 (Off) is transmitted',
              'Read the Vehicle Settings menu and check that the Power Liftgate '
              'Alert status is displayed as Off'],
        er=['The Vehicle Settings menu is displayed',
            'TELEMATIC_VEHICLE_SETUP.PLGAlert_Req = 0 (Off) is sent',
            'The Power Liftgate Alert status is displayed as Off'],
        vsrc="2-DBC", dr="",
        remarks=BUS_NOTE + ' ' + FB_PROPID + ' 本條之條文**二式皆有**（`propId = PLGAlert_Req and '
                'value = [Off]` 與 `$TELEMATIC_VEHICLE_SETUP.PLGAlert_Req$`），'
                '取後者。',
        reason='值域來源 **2-DBC** —— `PDT27_E2A_R5_FDCAN8.dbc` 之 '
               '`VAL_ PLGAlert_Req 0 "Off" 1 "On"`；raw 0 對應條文之 [Off]。'),
    dict(
        leaf="SWE1-VC-IlluminatedApproach-004", seq=261, form="訊號送出型",
        title='TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req is sent as 0 (Zero) '
              'when Illuminated Approach is Disabled',
        item='When the customer chooses to set the Illuminated Approach setting to '
             'Disabled on the LTM or ETM, the HMI layer shall send the updated '
             'customer preference to the HW. When the HMI receives the value as '
             '[Zero] via signal, $TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req$, '
             'Then the HMI shall display the Illuminated Approach status as Disabled.',
        pre=[FULLOP, BUS,
             'The "Illuminated Approach" customer setting is set to Thirty'],
        proc=['Open the Vehicle Settings menu and wait until it is fully rendered',
              'Set the "Illuminated Approach" customer setting to Disabled and check '
              'that TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req = 0 (Zero) is '
              'transmitted',
              'Read the Vehicle Settings menu and check that the Illuminated '
              'Approach status is displayed as Disabled'],
        er=['The Vehicle Settings menu is displayed',
            'TELEMATIC_VEHICLE_SETUP.Illuminated_Approach_Req = 0 (Zero) is sent',
            'The Illuminated Approach status is displayed as Disabled'],
        vsrc="2-DBC", dr="",
        remarks=BUS_NOTE + ' ' + FB_PROPID + ' 本條之條文**二式皆有**，取後者。'
                'DBC 之標籤為 `Zero`，而畫面之措辭為 `Disabled` —— '
                '二者為同一值之訊號側與畫面側名稱，條文逐字如此，不改寫。',
        reason='值域來源 **2-DBC** —— `VAL_ Illuminated_Approach_Req 0 "Zero" '
               '1 "Thirty" 2 "Sixty" 3 "Ninety"`；raw 0 對應條文之 [Zero]。'),
    dict(
        leaf="SWE1-VC-SWITCH1Type-002", seq=262, form="訊號送出型",
        title='TELEMATIC_FD_1.AUX1_TYPE_Req is sent as 0 (Latching) when SWITCH 1 '
              'Type is Latching',
        item='The HMI layer shall capture the customer selection for the SWITCH 1 '
             'Type setting and send the request using the TELEMATIC_FD_1.AUX1_TYPE_Req '
             'signal value as LATCHING. The HMI layer shall maintain/update the '
             'displayed setting according to the requested value.',
        pre=[FULLOP, BUS,
             'The "SWITCH 1 Type" customer setting is set to Momentary'],
        proc=['Open the Vehicle Settings menu and wait until it is fully rendered',
              'Set the "SWITCH 1 Type" customer setting to Latching and check that '
              'TELEMATIC_FD_1.AUX1_TYPE_Req = 0 (Latching) is transmitted',
              'Read the Vehicle Settings menu and check that the SWITCH 1 Type '
              'setting is displayed as Latching'],
        er=['The Vehicle Settings menu is displayed',
            'TELEMATIC_FD_1.AUX1_TYPE_Req = 0 (Latching) is sent',
            'The SWITCH 1 Type setting is displayed as Latching'],
        vsrc="2-DBC", dr="",
        remarks=BUS_NOTE + ' ' + FB_PROPID + ' 本條之條文**僅 `MESSAGE.Signal` 式**。'
                '條文書為 `LATCHING`，DBC `VAL_` 之標籤為 `Latching`（僅大小寫之別）；'
                '依 R-VF13 之值域來源鏈取 DBC 逐字。'
                '條文之「any invalid value shall be considered invalid by HMI」'
                '為無效值形態，不在本條之斷言內（另條涵蓋）。',
        reason='值域來源 **2-DBC** —— `VAL_ AUX1_TYPE_Req 0 "Latching" 1 "Momentary"`。'),
    dict(
        leaf="SWE1-VC-BlindSpotAlert-004", seq=263, form="訊號送出型",
        title='TELEMATIC_VEHICLE_SETUP.BSDEnable_Req is sent as 0 (Not_Enable) when '
              'Blind Spot Alert is disabled',
        item='The HMI layer shall capture the customer selection for the Blind Spot '
             'Alert setting and send the request using the '
             'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req signal value as Not_Enable. '
             'The HMI layer shall maintain/update the displayed setting according to '
             'the requested value.',
        pre=[FULLOP, BUS,
             'The "Blind Spot Alert" customer setting is set to Enable_LED'],
        proc=['Open the Vehicle Settings menu and wait until it is fully rendered',
              'Set the "Blind Spot Alert" customer setting to Not_Enable and check '
              'that TELEMATIC_VEHICLE_SETUP.BSDEnable_Req = 0 (Not_Enable) is '
              'transmitted',
              'Read the Vehicle Settings menu and check that the Blind Spot Alert '
              'setting is displayed as Not_Enable'],
        er=['The Vehicle Settings menu is displayed',
            'TELEMATIC_VEHICLE_SETUP.BSDEnable_Req = 0 (Not_Enable) is sent',
            'The Blind Spot Alert setting is displayed as Not_Enable'],
        vsrc="2-DBC", dr="",
        remarks=BUS_NOTE + ' ' + FB_PROPID + ' 本條之條文**僅 `MESSAGE.Signal` 式**。',
        reason='值域來源 **2-DBC** —— `VAL_ BSDEnable_Req 0 "Not_Enable" '
               '1 "Enable_LED" 2 "Enable_ LED_Chime"`。'),
    dict(
        leaf="SWE1-VC-SuspensionServiceMode-006", seq=264, form="訊號上行型",
        title='Suspension Service Mode status is displayed as On when '
              'Susp_Tire_Jack is 1 (On)',
        item='When the LTM or ETM receives the value via signal '
             '$IPC_VEHICLE_SETUP.Susp_Tire_Jack$, the LTM or ETM shall update the '
             'Suspension Service Mode setting status Information on the display '
             'within the defined system response time.',
        pre=[FULLOP, BUS,
             'The Vehicle Settings menu is open'],
        proc=['Send CAN: IPC_VEHICLE_SETUP.Susp_Tire_Jack = 0 (Off)',
              'Send CAN: IPC_VEHICLE_SETUP.Susp_Tire_Jack = 1 (On)',
              'Read the Vehicle Settings menu and check that the Suspension Service '
              'Mode setting status is displayed as On'],
        er=['IPC_VEHICLE_SETUP.Susp_Tire_Jack = 0 (Off) is sent',
            'IPC_VEHICLE_SETUP.Susp_Tire_Jack = 1 (On) is sent',
            'The Suspension Service Mode setting status is displayed as On'],
        vsrc="2-DBC", dr="",
        remarks=BUS_NOTE + ' 書寫形態**有先例**（W-VF68 §2.1 第 2 項）—— Part 1 之 353 行 '
                '`Send CAN:`，如 `SWE1-VC-Stop-StartSystem-005` 之「Send CAN: … '
                'and check that …」／ER「… is sent」。不回退。'
                '條文之「within the defined system response time」**未定量**，'
                '交付集內無其值 —— 故本條**不斷言時間**，僅斷言顯示之結果；'
                '此為刻意之不涵蓋，具名。',
        reason='值域來源 **2-DBC** —— `VAL_ Susp_Tire_Jack 0 "Off" 1 "On"`；'
               '條文未帶值，取 DBC 之 On 分區。'),
    dict(
        leaf="SWE1-VC-Blind Spot with Trailer Detection-049", seq=265, form="訊號上行型",
        title='Blind Spot with Trailer Detection is displayed as Max when '
              'Trailer_detection_blind_spot is 1 (Max)',
        item='The HMI layer shall evaluate the received '
             'IPC_VEHICLE_SETUP.Trailer_detection_blind_spot signal and '
             'update/display the Blind Spot with Trailer Detection setting '
             'information accordingly within <TDisplay>.',
        pre=[FULLOP, BUS,
             'The Vehicle Settings menu is open'],
        proc=['Send CAN: IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 0 (Auto)',
              'Send CAN: IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 1 (Max)',
              'Read the Vehicle Settings menu and check that the Blind Spot with '
              'Trailer Detection setting information is displayed as Max'],
        er=['IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 0 (Auto) is sent',
            'IPC_VEHICLE_SETUP.Trailer_detection_blind_spot = 1 (Max) is sent',
            'The Blind Spot with Trailer Detection setting information is displayed '
            'as Max'],
        vsrc="2-DBC", dr="",
        remarks=BUS_NOTE + ' 書寫形態有先例，同 seq 264。'
                '條文之 `<TDisplay>` 為**未解之符號**，交付集內無其值 —— '
                '本條**不斷言時間**，僅斷言顯示之結果；此為刻意之不涵蓋，具名。'
                '本訊號之 `VAL_` 為 `Auto`／`Max`（非 On／Off）—— '
                '其為偵測範圍之設定而非開關，故畫面之措辭取 DBC 標籤逐字。',
        reason='值域來源 **2-DBC** —— `VAL_ Trailer_detection_blind_spot 0 "Auto" '
               '1 "Max"`；條文未帶值，取 Max 分區。'),
    dict(
        leaf="SWE1-VC-Language-059", seq=266, form="設定顯示與修改型",
        title='Language customer setting is displayed and modifiable on the LTM '
              'screen',
        item='The HMI layer shall display the Language customer setting and allow the '
             'customer to modify the setting through the LTM or ETM screen. The LTM '
             'or ETM shall display the available language options according to the '
             'configured market/language settings.',
        pre=[FULLOP],
        proc=['Open the Vehicle Settings menu and wait until it is fully rendered',
              'Read the Vehicle Settings menu and check that the "Language" customer '
              'setting is displayed',
              'Select the "Language" customer setting and check that the available '
              'language options are displayed',
              'Select a language option other than the current one and check that '
              'the "Language" customer setting is changed to the selected option'],
        er=['The Vehicle Settings menu is displayed',
            'The "Language" customer setting is displayed',
            'The available language options are displayed',
            'The "Language" customer setting is changed to the selected option'],
        vsrc="", dr="",
        remarks=FB_DISPMOD + ' 條文之「according to the configured market/language '
                'settings」—— 市場配置之選項清單**無來源**（交付集內無市場對映表），'
                '故本條**不斷言選項清單之內容**，僅斷言選項被顯示且可被選取；'
                '此為刻意之不涵蓋，具名。',
        reason='本條無訊號亦無 PROXI，值域來源欄留白（非未查，而是條文本無值）。'),
    dict(
        leaf="SWE1-VC-TimeandDateSettings-002", seq=267, form="設定顯示與修改型",
        title='Time & Date customer setting is displayed and modifiable on the LTM '
              'screen',
        item='The HMI layer shall display the Time & Date customer setting and allow '
             'the customer to modify the settings through the LTM or ETM screen. The '
             'HMI layer shall update and manage the Time & Date settings based on the '
             'customer selection in the display.',
        pre=[FULLOP],
        proc=['Open the Vehicle Settings menu and wait until it is fully rendered',
              'Read the Vehicle Settings menu and check that the "Time & Date" '
              'customer setting is displayed',
              'Select the "Time & Date" customer setting and check that the Time & '
              'Date setting items are displayed',
              'Change one Time & Date setting item and check that the "Time & Date" '
              'customer setting is updated to the changed value'],
        er=['The Vehicle Settings menu is displayed',
            'The "Time & Date" customer setting is displayed',
            'The Time & Date setting items are displayed',
            'The "Time & Date" customer setting is updated to the changed value'],
        vsrc="", dr="",
        remarks=FB_DISPMOD + ' 條文之「shall follow the Radio HMI Look & Feel (L&F) '
                'guidelines」—— 該 guidelines **不在交付集內**，'
                '故本條**不斷言外觀與互動之樣式**，僅斷言顯示與可修改；'
                '此為刻意之不涵蓋，具名。',
        reason='本條無訊號亦無 PROXI，值域來源欄留白（非未查，而是條文本無值）。'),
]


def numbered(xs: list[str]) -> str:
    return "\n".join(f"{i}. {x}" for i, x in enumerate(xs, 1))


def priority_of(title: str, text: str) -> tuple[str, str]:
    """判準取自 `vf230_wvf45_priority`，非本檔之寫死（A-VF17）。"""
    if title in PR.P0A:
        return "P0", "P0(a)"
    if title in PR.P0_SAFETY:
        return "P0", "P0(c)"
    if title in PR.P1_SAFETY_PRESENTATION:
        return "P1", "P1"
    if PR.P2_PAT.search(text):
        return "P2", "P2"
    return "P1", "P1"


def main() -> None:
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    sel = json.loads((FEAT / "data/_vf230_pilot2_sel.json").read_text())["sel"]
    refs = P1.spec_refs()

    assert [s["leaf_id"] for s in sel] == [t["leaf"] for t in TCS], \
        "本檔之 leaf 序與 V26 §3 已核可之取樣表不符"

    out = []
    for t in TCS:
        leaf, lf, w = t["leaf"], lv[t["leaf"]], wr[t["leaf"]]
        title3 = lf["title"].replace("\\n", " ")
        pri, cls = priority_of(title3, re.sub(r"\s+", " ", lf["desc"]))
        ref = refs.get(lf["src_ref"], "")
        assert ref, f"{leaf}：spec_reference 未由 R-VF68 之錨鏈解出"
        out.append({
            "leaf_id": leaf, "seq": t["seq"], "test_set": w["test_set"],
            "layer3": title3, "tc_title": t["title"], "test_item": t["item"],
            "pre_conditions": numbered(t["pre"]), "input_test_data": "NA",
            "test_procedure": numbered(t["proc"]),
            "expected_result": numbered(t["er"]),
            "specification_reference": ref, "priority": pri, "priority_class": cls,
            "design_method": EP, "writable": w["writable"], "dr_dependent": t["dr"],
            "remarks": t["remarks"], "value_source": t["vsrc"],
            "clause_form": t["form"], "reasoning": t["reason"],
        })

    # 檔頭之 priority 分布**由逐條實測算出**，不寫死（A-VF17 之同一教訓）
    from collections import Counter
    dist = Counter(t["priority_class"] for t in out)
    dist_s = "；".join(f"{k} {v}" for k, v in sorted(dist.items()))

    doc = {
        "batch": "vf230_pilot2",
        "line": "VF230", "feature": "vehicle_setting / VF230",
        "test_group": "Vehicle Setting",
        "handoff": "docs/handoff/V28_batch_reform.md（sha256 4b17cc6cc238f18b…，4051 bytes）",
        "work_order": "W-VF68（併 W-VF65／W-VF66／W-VF67）",
        "selection": "V26 §3 之表（已核可），記於 data/_vf230_pilot2_sel.json —— "
                     "四形態分層：PROXI 型 2／訊號送出型 4／訊號上行型 2／"
                     "設定顯示與修改型 2。priority 分布（逐條實測）：" + dist_s + "。",
        "form_precedent": {
            "propId 式": "查無（Part 1 218 條內 0 行）→ 回退 MESSAGE.Signal 式，逐條具名",
            "訊號上行型": "有先例（353 行 Send CAN:）→ 依先例，不回退",
            "displayed and modifiable": "查無（0 行）→ 回退 pilot #1 v4 正向式，逐條具名",
            "訊號送出型二式比例": "MESSAGE.Signal 189 (59%)／兩式皆有 75 (24%)／"
                            "皆無 32 (10%)／純 propId 22 (7%)；"
                            "本批涵蓋前二式，**純 propId 之 22 條未涵蓋**",
        },
        "signal_notation": 'R-1 v2／R-VS52：Send CAN: MESSAGE.Signal = <raw> (<Label>)；'
                           'ER「… is sent」；procedure「… is transmitted」；'
                           'PROXI $Param$ = "值"；Input Test Data 為 NA',
        "spec_reference_source": "R-VF68：037 `Source Requirement ID` → 035 SYSRA "
                                 "`Basic Report` 之「來源需求項目 ID」",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "b_column_start": "R-VF1（VF230 線）：pilot #1 用 238–247；本批 258–267",
        "delegation": "既有委派表 627 全數 `no`（未動）；"
                      "條文委派語路徑另表 docs/reports/vf230_deleg_phrase.tsv（1 條，"
                      "`E-Save-095` → CFTS 088，不在 features/ 之下）",
        "pool": "620（W2(a) 路徑落地後 `E-Save-095` 由 W0 改判 W2，池 621 → 620）",
        "write_back": "**未寫回**（R-VF26）。`seq` 僅記於產出。",
        "tcs": out,
    }
    p = FEAT / "generated/vf230_pilot2.json"
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(out)} 條 → {p.relative_to(FEAT)}")
    for t in out:
        print(f"  {t['seq']} {t['priority']}/{t['priority_class']:5} {t['writable']} "
              f"{t['specification_reference']:24} {t['clause_form']:9} "
              f"{t['leaf_id'][:40]}")


if __name__ == "__main__":
    main()
