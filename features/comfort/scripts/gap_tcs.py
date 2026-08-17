#!/usr/bin/env python3
"""下放包 97／98 之補產 —— 20 個 leaf、31 條 TC。

97 §1 訂正了分析層歷來所用之判準：

    條文說了什麼，就驗什麼。
    沒說的那部分，由測試員面對實車時解決。

據此，`WITHHELD` 中以「不知道哪一種車適用」為由停下之 leaf 全數解封 ——
**「不知道誰適用」與「不知道有哪些」是兩件事**（97 §1.1），而條文把「有哪些」
逐字列出者，其列舉本即 §8.3 之 sibling axes 所要求之拆分維度。

98 之六問裁定（A～F）決定了確切條數：

    A/B  2.1 之 037 與條文有落差（3 tabs／無 Massage）→ **依 R-C33**：
         單位歸 037、內容歸 spec。落差為 RD-1 既有記載 A-CF21，不另立新項
    C    2.12 之「四模式清單與順序」**在 037 無 leaf** → 不借掛 `016-01`，
         登為 R-C16 覆蓋缺口（profile §5.4 第六成員），總 6 條
    D    `018-04` 拆 3，其組成依 §5.7 校正：彈窗出現與不跳轉為**同一觸發之
         兩個後果**，併為一條；閒置 3 秒與按下他鍵為**兩個觸發**，各一條
    E    `018-01` 之 Defrost 排除**另立一條**（§7 之 `ALWAYS` 正面命中），
         018 總數 12
    F    `016-02` 不依四模式展開（§10.6 之近重複），1 條

`019-03`（on/off logic 全部委派 VF HVAC document）**維持不產**，其列為留空列；
`072`（12.6）維持 `[BLOCKED-SPEC]`。兩者皆不在本檔內。

**tc_id 明寫而非自範圍導出**（R-C43，同 `external_docs.py`）：435–465，
依 req_id 遞增指派，故既有 434 列一列都不重編（65 §1）。

Pei 2026-08-17 另裁：**Maserati (Seat & Wheel) 不在 R1LR ATL-H 交付範圍** ——
`2.1` 維持 4 條、不增變體標籤 TC（§8.7.3 不適用），tab 名稱一律寫 `Seats`。
`test_item` 上半為條文原文逐字（95 §1），故 `Seats (WS or R1 Low) or Seat &
Wheel (Maserati)` 仍出現於該欄上半 —— 98 §2 已裁此非規則衝突而是兩欄各司其職。

用法（於 owner generator 內，寫檔前）：
    from gap_tcs import append_gap
    tcs = append_gap(tcs, parent)
"""

TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")

DM_F = "功能測試 (Functional based ; no specific technique)"
DM_S = "狀態轉換 (State Transition Testing)"
DM_B = "邊界值分析 (Boundary Value Analysis, BVA)"
DM_E = "等價劃分 (Equivalence Partitioning, EP)"

EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")

# --- 各節之首行 pre_condition ---------------------------------------------
# 97 §1 之判準所解封者正是這些行：條文列出了有哪些，而未說哪一種車有 ——
# 後者是測試員面對實車時看得見的事。
PC_TABS_4 = ("1. [spec-derived] The vehicle is configured with all four of "
             "the comfort areas the clause lists — Front, Seats, Massage and "
             "Rear (2.1)")
PC_TABS_3 = ("1. [spec-derived] The vehicle is configured with three of the "
             "four comfort areas the clause lists — Front, Seats, Massage and "
             "Rear (2.1)")
PC_TABS_2 = ("1. [spec-derived] The vehicle is configured with two of the "
             "four comfort areas the clause lists — Front, Seats, Massage and "
             "Rear (2.1)")
PC_RECIRC = "1. [test-setup] The climate screen is open and the climate system is on"
# 第三軸之值一。DR #31 記其**適用條件**無正面條文（profile §3.2 附註），
# 而 97 §1 裁定那不是不寫的理由：條文逐字列出了這四個模式是哪四個。
PC_4MODE = ("1. [spec-derived] The vehicle is configured with the four "
            "airflow modes the clause lists — Face, Face plus Feet, Feet and "
            "Feet plus Windshield (2.12)")
# R-C31 —— 條文自身之執行前提（它把 Mode 硬鍵指為被操作之物）。
PC_MODE_HC = "2. [spec-derived] The vehicle has a Mode hard control (2.12.2)"
PC_REAR_SCREEN = "3. [spec-derived] The vehicle has a Rear Climate screen (2.12.2)"
PC_MAXAC = ("1. [spec-derived] The vehicle has MAX A/C functionality, whose "
            "presence the CCM relays (2.13)")
# 與已寫之七條（9.2／9.3／9.4／9.4.1）所用者為同一句 —— 97 §2.5 指出之
# 不一致即在此：七條以該句為 PC，而該句自身之 leaf（`039`）此前無列。
PC_CH9 = ("1. [spec-verbatim] On some vehicles (See CFTS043 for details), "
          "there are additional Rear Climate controls and shortcuts (9.1)")
# 軸一之**正向**值。「(AUTO is not shown in MTC configurations)」為 2.3／16.3
# 之逐字括號，其為本條之**驗證目標**而非前提，故落 ER 而不落 PC ——
# 寫成否定式 PC 會使它同時是前提與結論，且該否定不對應任何軸值（43 §4）。
PC_ECO_MTC = "1. [spec-derived] The climate system is MTC (2.3)"
PC_ECO_EV = ("2. [spec-derived] The vehicle is an EV vehicle, on which ECO "
             "HVAC is used (10.1)")
PC_ICS = ("1. [spec-derived] The vehicle is an EMEA ICS vehicle, whose "
          "climate interface is specified in chapter 16 (16.2)")
PC_COMFORT_CTRL = ("1. [spec-derived] The vehicle is equipped with Comfort "
                   "features, whose available comfort controls depend on "
                   "vehicle configuration (14.15)")
PC_WIDGET = "1. [test-setup] The Comfort widget is shown on the home screen"
# 18.1 與 17.1 之條文逐字相同，唯一區辨者為章標題「10.25" Home screen」。
# 批次 8 曾以「章標題不是條文」為由停下三個 leaf；97 §2.7／98 §1 裁定生成，
# 其 PC 之出處即該章之標題 —— **此為全語料唯一一處 PC 之出處為章標題而非
# 條文句子者**，故逐字記於此並於 reasoning 具名，不使它日後被讀成一般用法。
PC_1025 = ("2. [spec-derived] The vehicle has the 10.25\" head unit screen, "
           "the screen whose Comfort widget chapter 18 states (18.1)")
PC_COMFORT_FEATURES = ("[spec-derived] The vehicle is equipped with Comfort "
                       "features, such as heated/vented seats and a heated "
                       "steering wheel (17.3)")

# --- 拆分理由（split_reason 進工作簿，故其文字須自足）----------------------
_SPLIT = ("§8.2.2 之拆分，依 75 §1 之判準（**條文列舉之項即拆分之維度**）："
          "本節之條文逐字列舉其項 —— 「{quote}」—— 故一項一條。{why} "
          "（**判準之反面**：條文以泛稱表述而由作者挑樣者不拆，其樣本為 "
          "interaction data，§4.5。）")

SPLIT_016_01 = _SPLIT.format(
    quote="There are 4 Airflow Mode displayed in this order (1) Face, "
          "(2) Face plus Feet, (3) Feet, (4) Feet plus Windshield",
    why="四個模式各自可失效：Face 之高亮與放大正確而 Feet plus Windshield "
        "之不正確，是一種失效；反之亦然。")
SPLIT_018_01 = _SPLIT.format(
    quote="Face > Face/Feet > Feet > Feet plus Windshield > then repeat loop. "
          "Defrost will not be included in the loop",
    why="四段轉換各自可失效（前三段正確而繞回起點失敗，是一種失效），"
        "而「Defrost 不在迴圈內」為該列舉之未支援側 —— §7 明文要求列舉之"
        "支援項**一律**配至少一條未支援之負向條，故另立一條走完整個迴圈"
        "並驗 Defrost 自始至終不出現。")
SPLIT_018_04 = (
    "§8.2.2 之拆分，判準為 §5.7（**觸發為驗證之單位**）：本 leaf 含三個觸發。"
    "按 Mode 硬鍵所生之兩個後果（彈窗出現於主類別控制上方、使用者不被移至 "
    "climate main）**同出一個觸發，依 §5.7 併為一條**，以兩行 ER 承載；"
    "而條文另逐字列舉兩個消失條件 —— 「timeout after 3 seconds of inactivity "
    "or as soon as another button except Mode HC is pressed」—— 兩者為不同之"
    "觸發，故各一條。三者可獨立失效：彈窗出現而逾時不消失，是一種失效。")

# `10.4` 之兩條同溯 `047`，故兩列皆須宣告拆分（§8.2.2：一個拆分要在它產出的
# 每一列上都看得見）。既有之 `NR1L-ComfortHMI-070` 於 gen_batch5.py 內引用本串。
SPLIT_047 = (
  "§8.3 之軸拆分：`10.4`（EH4）之「When the AUTO function is off **and "
  "available**」以可用性為其前提，而 profile §3.2 第一軸（ATC／MTC）之 MTC "
  "值使該前提不成立 —— 「(AUTO is not shown in MTC configurations)」為 "
  "`2.3`／`16.3` 之逐字括號（跨節取據 R-C29）。兩個軸值之預期結果相反且"
  "各自可失效：ATC 車上首按進入 AUTO ECO 而 MTC 車上不進入，"
  "任一側錯皆不使另一側錯。**「not shown 是否等於 not available」屬測試員於"
  "實車上之觀察，不屬條文之缺口**（97 §2.6，RD-1 第 7 問據此移除）。")

# --- 2.12／2.12.2 之逐條 EMEA 判定（R-C36-1）------------------------------
# 鏡射表：`16.12 ↔ 2.12` 為 **partial**（其分界欄逐字寫明涵蓋側與未涵蓋側），
# `16.12.1 ↔ 2.12.2` 為 **mirrored**。逐條之答依該分界，不以節級一詞代之。
_E212_COVER = dict(
  ch16_outline="16.12", verdict="yes",
  ch16_sentence="鏡射表 `16.12 ↔ 2.12`（partial）之**涵蓋側**逐字列出本條所驗"
                "之行為（ON state 之高亮與放大、main category control 之顯示、"
                "一次只能選一個）—— EMEA ICS 車輛由 ICE11 自行規範，排除成立；"
                "**惟 ICE11 為五狀態**，故本條所取之四模式集合於 ICS 側不成立")
_E212_ORDER = dict(
  ch16_outline="16.12", verdict="no",
  ch16_sentence="鏡射表 `16.12 ↔ 2.12` 之**未涵蓋側**即「C13 之四模式清單與其"
                "順序（ICE11 為五狀態）」—— 本條逐一選取該四者之一，"
                "其模式身分正落在未涵蓋側，故排除為過嚴側"
                "（R-C36-1，removal 待裁）")
_E2122 = dict(
  ch16_outline="16.12.1", verdict="yes",
  ch16_sentence="鏡射表 `16.12.1 ↔ 2.12.2` 為 **mirrored**：ICE11.1 與 C13.1 "
                "皆述 Mode 硬鍵之循環與 Climate main 內外之呈現 —— "
                "EMEA ICS 車輛由 ICE11.1 自行規範，排除成立"
                "（**其迴圈為五狀態，本節為四**，故兩側之列不得互相移植）")

# ---------------------------------------------------------------------------
# 31 列。鍵為 tc_id 之數字，值為該列之內容；`parent` 決定它掛在哪一個檔。
# 順序即 req_id 之遞增順序（96 §1 之列序規則），tc_id 隨之遞增。
# ---------------------------------------------------------------------------
GAP = [
 # ------------------------------------------------- 2.1  Front Climate Anatomy
 dict(n=435, req="SWE1-HVAC-001-01", parent="SWE1-HVAC-001", outline="2.1",
      test_set="Front Climate Anatomy",
      title="Four tabs are displayed when the vehicle has all four comfort areas",
      item="The comfort category shall have up to 4 tabs depending on vehicle configuration",
      pc=PC_TABS_4, ex=(EX_ICS, EX_LOWER), refs=("2.1", "2.14", "6.3"),
      proc=["1. Open the comfort category",
            "2. Count the tabs displayed"],
      er=["1. The comfort category is displayed",
          "2. Four tabs are displayed and no further tab is displayed"],
      prio="P1", dm=DM_B,
      split_reason="§8.3 之邊界軸（=limit）：條文之上界為 4 個 tab，"
                   "本條取該上界，同 leaf 之另二條分取 limit−1 與其"
                   "內部值，而 =0 之邊界已由 `001-03` 承載。"),
 dict(n=436, req="SWE1-HVAC-001-01", parent="SWE1-HVAC-001", outline="2.1",
      test_set="Front Climate Anatomy",
      title="Three tabs are displayed when the vehicle has three comfort areas",
      item="The comfort category shall have up to 4 tabs depending on vehicle configuration",
      pc=PC_TABS_3, ex=(EX_ICS, EX_LOWER), refs=("2.1", "2.14", "6.3"),
      proc=["1. Open the comfort category",
            "2. Count and read the tabs displayed"],
      er=["1. The comfort category is displayed",
          "2. Three tabs are displayed and each of them is one of Front, "
          "Seats, Massage and Rear"],
      prio="P1", dm=DM_B,
      split_reason="§8.3 之邊界軸（limit−1）：上界為 4，本條取其下一值。"),
 dict(n=437, req="SWE1-HVAC-001-01", parent="SWE1-HVAC-001", outline="2.1",
      test_set="Front Climate Anatomy",
      title="Two tabs are displayed when the vehicle has two comfort areas",
      item="The comfort category shall have up to 4 tabs depending on vehicle configuration",
      pc=PC_TABS_2, ex=(EX_ICS, EX_LOWER), refs=("2.1", "2.14", "6.3"),
      proc=["1. Open the comfort category",
            "2. Count and read the tabs displayed"],
      er=["1. The comfort category is displayed",
          "2. Two tabs are displayed and each of them is one of Front, "
          "Seats, Massage and Rear"],
      prio="P2", dm=DM_E,
      split_reason="§8.3 之邊界軸之內部值：4（上界）與 0（`001-03`）之間，"
                   "本條取一個中間分割，驗 tab 數隨配置而變且其成員恆在"
                   "條文所列之四者內。"),
 dict(n=438, req="SWE1-HVAC-001-02", parent="SWE1-HVAC-001", outline="2.1",
      test_set="Front Climate Anatomy",
      title="Comfort tabs are displayed in the order the clause gives",
      item="The tabs shall be displayed in the order Front, Seats, Massage, Rear",
      pc=PC_TABS_4, ex=(EX_ICS, EX_LOWER), refs=("2.1", "2.14", "6.3"),
      proc=["1. Open the comfort category",
            "2. Read the tabs from left to right"],
      er=["1. The comfort category is displayed",
          "2. The tabs read Front, Seats, Massage and Rear in that order"],
      prio="P1", dm=DM_F),

 # --------------------------------------------------------- 2.5  Climate Modes
 dict(n=439, req="SWE1-HVAC-006-04", parent="SWE1-HVAC-006", outline="2.5",
      test_set="Climate Modes",
      title="The RECIRC icon matches the vehicle configuration",
      item="The recirc icon shall display the vehicle model specific icon as displayed in the table",
      pc=PC_RECIRC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.5", "2.14", "16.2", "6.3"),
      proc=["1. Open the climate screen",
            "2. Read the RECIRC icon"],
      er=["1. The climate screen is displayed",
          "2. A RECIRC icon is displayed and it matches the vehicle's "
          "configuration — the model specific icon, or the generic recirc "
          "symbol where the vehicle model cannot be detected"],
      prio="P2", dm=DM_F,
      emea=dict(ch16_outline="16.5", verdict="yes",
                ch16_sentence="ICE4「The recirc icon will display the vehicle "
                              "model specific icon」與 C4 之同一句逐字相同"
                              "（其表寫作 `Climate Main page table`）—— "
                              "EMEA ICS 車輛由 16.5 自行規範，排除成立")),

 # ------------------------------------------------ 2.12  Airflow and Defrost
 dict(n=440, req="SWE1-HVAC-016-01", parent="SWE1-HVAC-016", outline="2.12",
      test_set="Airflow and Defrost",
      title="Selecting Face highlights and enlarges its button",
      item="The ON state for the four airflow modes shall be shown by highlighting the button and increasing button size",
      pc=PC_4MODE, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open the climate screen",
            "2. Select the \"Face\" airflow mode"],
      er=["1. The climate screen is displayed",
          "2. The \"Face\" button is highlighted and its size is increased"],
      prio="P1", dm=DM_F, split_reason=SPLIT_016_01,
      emea=_E212_ORDER),
 dict(n=441, req="SWE1-HVAC-016-01", parent="SWE1-HVAC-016", outline="2.12",
      test_set="Airflow and Defrost",
      title="Selecting Face plus Feet highlights and enlarges its button",
      item="The ON state for the four airflow modes shall be shown by highlighting the button and increasing button size",
      pc=PC_4MODE, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open the climate screen",
            "2. Select the \"Face plus Feet\" airflow mode"],
      er=["1. The climate screen is displayed",
          "2. The \"Face plus Feet\" button is highlighted and its size is "
          "increased"],
      prio="P1", dm=DM_F, split_reason=SPLIT_016_01,
      emea=_E212_ORDER),
 dict(n=442, req="SWE1-HVAC-016-01", parent="SWE1-HVAC-016", outline="2.12",
      test_set="Airflow and Defrost",
      title="Selecting Feet highlights and enlarges its button",
      item="The ON state for the four airflow modes shall be shown by highlighting the button and increasing button size",
      pc=PC_4MODE, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open the climate screen",
            "2. Select the \"Feet\" airflow mode"],
      er=["1. The climate screen is displayed",
          "2. The \"Feet\" button is highlighted and its size is increased"],
      prio="P1", dm=DM_F, split_reason=SPLIT_016_01,
      emea=_E212_ORDER),
 dict(n=443, req="SWE1-HVAC-016-01", parent="SWE1-HVAC-016", outline="2.12",
      test_set="Airflow and Defrost",
      title="Selecting Feet plus Windshield highlights and enlarges its button",
      item="The ON state for the four airflow modes shall be shown by highlighting the button and increasing button size",
      pc=PC_4MODE, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open the climate screen",
            "2. Select the \"Feet plus Windshield\" airflow mode"],
      er=["1. The climate screen is displayed",
          "2. The \"Feet plus Windshield\" button is highlighted and its size "
          "is increased"],
      prio="P1", dm=DM_F, split_reason=SPLIT_016_01,
      emea=_E212_ORDER),
 dict(n=444, req="SWE1-HVAC-016-02", parent="SWE1-HVAC-016", outline="2.12",
      test_set="Airflow and Defrost",
      title="The main category control shows the newly selected airflow mode",
      item="The main category control shall display the newly selected airflow mode inside the fan space",
      pc=PC_4MODE, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12", "2.14", "16.2", "6.3"),
      proc=["1. Select an airflow mode on the climate screen",
            "2. Read the fan space of the main category control"],
      er=["1. The airflow mode selected is active",
          "2. The fan space of the main category control shows the airflow "
          "mode selected in step 1"],
      prio="P1", dm=DM_F,
      emea=_E212_COVER),
 dict(n=445, req="SWE1-HVAC-016-03", parent="SWE1-HVAC-016", outline="2.12",
      test_set="Airflow and Defrost",
      title="Only one airflow mode is selected at a time",
      item="Only one airflow mode shall be selected at a time",
      pc=PC_4MODE, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12", "2.14", "16.2", "6.3"),
      proc=["1. Select the \"Face\" airflow mode",
            "2. Select the \"Feet\" airflow mode"],
      er=["1. The \"Face\" button is highlighted",
          "2. The \"Feet\" button is highlighted and the \"Face\" button is "
          "no longer highlighted"],
      prio="P1", dm=DM_S,
      emea=_E212_COVER),

 # ---------------------------------------------- 2.12.2  Airflow and Defrost
 dict(n=446, req="SWE1-HVAC-018-01", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="Pressing Mode moves from Face to Face/Feet",
      item="A press of the Mode hard control shall move the user to the next mode available in the loop Face > Face/Feet > Feet > Feet plus Windshield > then repeat loop",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Set the airflow mode to Face",
            "2. Press the Mode hard control once"],
      er=["1. The Face airflow mode is active",
          "2. The Face/Feet airflow mode is active"],
      prio="P1", dm=DM_S, split_reason=SPLIT_018_01,
      emea=_E2122),
 dict(n=447, req="SWE1-HVAC-018-01", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="Pressing Mode moves from Face/Feet to Feet",
      item="A press of the Mode hard control shall move the user to the next mode available in the loop Face > Face/Feet > Feet > Feet plus Windshield > then repeat loop",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Set the airflow mode to Face/Feet",
            "2. Press the Mode hard control once"],
      er=["1. The Face/Feet airflow mode is active",
          "2. The Feet airflow mode is active"],
      prio="P1", dm=DM_S, split_reason=SPLIT_018_01,
      emea=_E2122),
 dict(n=448, req="SWE1-HVAC-018-01", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="Pressing Mode moves from Feet to Feet plus Windshield",
      item="A press of the Mode hard control shall move the user to the next mode available in the loop Face > Face/Feet > Feet > Feet plus Windshield > then repeat loop",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Set the airflow mode to Feet",
            "2. Press the Mode hard control once"],
      er=["1. The Feet airflow mode is active",
          "2. The Feet plus Windshield airflow mode is active"],
      prio="P1", dm=DM_S, split_reason=SPLIT_018_01,
      emea=_E2122),
 dict(n=449, req="SWE1-HVAC-018-01", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="Pressing Mode from Feet plus Windshield repeats the loop at Face",
      item="A press of the Mode hard control shall move the user to the next mode available in the loop Face > Face/Feet > Feet > Feet plus Windshield > then repeat loop",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Set the airflow mode to Feet plus Windshield",
            "2. Press the Mode hard control once"],
      er=["1. The Feet plus Windshield airflow mode is active",
          "2. The Face airflow mode is active"],
      prio="P1", dm=DM_S, split_reason=SPLIT_018_01,
      emea=_E2122),
 dict(n=450, req="SWE1-HVAC-018-01", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="Defrost is never reached through the Mode hard control loop",
      item="Defrost shall not be included in the Mode hard control loop",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Set the airflow mode to Face",
            "2. Press the Mode hard control four times, reading the airflow "
            "mode after each press"],
      er=["1. The Face airflow mode is active",
          "2. The airflow mode read after the four presses is Face/Feet, then "
          "Feet, then Feet plus Windshield, then Face again, and Defrost is "
          "not among them"],
      prio="P1", dm=DM_S, split_reason=SPLIT_018_01,
      emea=_E2122),
 dict(n=451, req="SWE1-HVAC-018-02", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="Press and hold of the Mode control moves only one mode",
      item="Press and hold of the Mode hard control shall only move one mode over and shall not continue to move through modes",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Set the airflow mode to Face",
            "2. Press and hold the Mode hard control"],
      er=["1. The Face airflow mode is active",
          "2. The Face/Feet airflow mode is active and the airflow mode does "
          "not continue to move while the control is held"],
      prio="P1", dm=DM_S,
      emea=_E2122),
 dict(n=452, req="SWE1-HVAC-018-03", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="The new mode button is highlighted on Climate main",
      item="When the Mode hard control is pressed and the user is on Climate main, the new mode button shall be shown highlighted",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open the Climate main screen",
            "2. Press the Mode hard control once"],
      er=["1. The Climate main screen is displayed",
          "2. The button of the new airflow mode is shown highlighted"],
      prio="P1", dm=DM_F,
      emea=_E2122),
 dict(n=453, req="SWE1-HVAC-018-04", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="Pressing Mode off Climate main shows a pop-up without switching screens",
      item="If the user is not on Climate main when pressing the Mode hard control, a small pop-up shall appear above the Climate main category control and the user shall not be shifted to climate main",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open a screen other than Climate main",
            "2. Press the Mode hard control once"],
      er=["1. The Climate main screen is not displayed",
          "2. A small pop-up appears above the Climate main category control "
          "and the Climate main screen is still not displayed"],
      prio="P1", dm=DM_F, split_reason=SPLIT_018_04,
      emea=_E2122),
 dict(n=454, req="SWE1-HVAC-018-04", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="The Mode pop-up times out after 3 seconds of inactivity",
      item="The pop-up shall time out after 3 seconds of inactivity",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open a screen other than Climate main and press the Mode hard "
            "control once",
            "2. Do not interact with the head unit for 3 seconds"],
      er=["1. A small pop-up appears above the Climate main category control",
          "2. The pop-up is no longer shown"],
      prio="P1", dm=DM_S, split_reason=SPLIT_018_04,
      emea=_E2122),
 dict(n=455, req="SWE1-HVAC-018-04", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="The Mode pop-up closes as soon as another button is pressed",
      item="The pop-up shall time out as soon as another button except the Mode hard control is pressed",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open a screen other than Climate main and press the Mode hard "
            "control once",
            "2. Press a button other than the Mode hard control"],
      er=["1. A small pop-up appears above the Climate main category control",
          "2. The pop-up is no longer shown"],
      prio="P2", dm=DM_S, split_reason=SPLIT_018_04,
      emea=_E2122),
 dict(n=456, req="SWE1-HVAC-018-05", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="The main category label is updated on and off Climate main",
      item="In both cases the main category label shall be updated",
      pc=PC_4MODE, pc2=PC_MODE_HC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Press the Mode hard control while on the Climate main screen "
            "and read the main category label",
            "2. Press the Mode hard control from a screen other than Climate "
            "main and read the main category label"],
      er=["1. The main category label shows the new airflow mode",
          "2. The main category label shows the new airflow mode"],
      prio="P2", dm=DM_F,
      emea=_E2122),
 dict(n=457, req="SWE1-HVAC-018-06", parent="SWE1-HVAC-018", outline="2.12.2",
      test_set="Airflow and Defrost",
      title="The Mode hard control alters the front Mode from the Rear Climate screen",
      item="While in the Rear Climate screen the Mode Hard Control button shall alter the front Mode",
      pc=PC_4MODE, pc2=PC_MODE_HC, pc3=PC_REAR_SCREEN,
      ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.12.2", "2.12", "2.14", "16.2", "6.3"),
      proc=["1. Open the Rear Climate screen",
            "2. Press the Mode hard control once"],
      er=["1. The Rear Climate screen is displayed",
          "2. The front airflow mode moves to the next mode in the loop"],
      prio="P1", dm=DM_F,
      emea=_E2122),

 # -------------------------------------------------------- 2.13  Climate Modes
 dict(n=458, req="SWE1-HVAC-019-02", parent="SWE1-HVAC-019", outline="2.13",
      test_set="Climate Modes",
      title="MAX A/C changes more than one climate parameter",
      item="MAX A/C shall modify multiple climate parameters",
      pc=PC_MAXAC, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("2.13", "2.14", "16.2", "6.3"),
      proc=["1. Read the climate parameters shown on the climate screen",
            "2. Turn MAX A/C on and read the climate parameters again"],
      er=["1. The climate screen shows the current climate parameters",
          "2. More than one of the climate parameters read in step 1 has "
          "changed"],
      prio="P1", dm=DM_F,
      emea=dict(ch16_outline="16.13", verdict="no",
                ch16_sentence="ICE12 之 MAX A/C 於 ch16 側**逐項列出**其所改"
                              "之參數，C14 則只說「multiple climate "
                              "parameters」—— 兩側之涵蓋範圍不同，"
                              "故本條之排除為過嚴側（R-C36-1，removal 待裁）；"
                              "**ER 不得引 16.13 之逐項清單**（§8.2.1 禁跨章"
                              "移植），只驗「有改變」")),

 # ------------------------------------------------------------ 9.1  Rear Climate
 dict(n=459, req="SWE1-HVAC-039", parent="SWE1-HVAC-039", outline="9.1",
      test_set="Rear Climate",
      title="The additional Rear Climate controls and shortcuts are present",
      item="On some vehicles there shall be additional Rear Climate controls and shortcuts",
      pc=PC_CH9, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("9.1", "2.14", "16.2", "6.3"),
      proc=["1. Open the Rear Climate tab",
            "2. Open the driver side climate dropdown menu in the status bar"],
      er=["1. The Rear Climate tab shows the additional Rear Climate controls "
          "this vehicle is configured with",
          "2. The dropdown menu shows the additional Rear Climate shortcut "
          "this vehicle is configured with"],
      prio="P1", dm=DM_F,
      emea=dict(ch16_outline="no-counterpart", verdict="no",
                ch16_sentence="ch16 十八節**無後排氣候之節**（DR #41 之實測），"
                              "亦無 status bar dropdown 之後排捷徑，"
                              "故本條之 EMEA 排除無 ch16 對造句可依")),

 # --------------------------------------------------------------- 10.4  ECO HVAC
 dict(n=460, req="SWE1-HVAC-047", parent="SWE1-HVAC-047", outline="10.4",
      test_set="ECO HVAC",
      title="Pressing AUTO does not activate AUTO ECO in an MTC configuration",
      item="AUTO is not shown in MTC configurations, so the first press of the AUTO button shall not activate the AUTO ECO functionality",
      pc=PC_ECO_MTC, pc2=PC_ECO_EV, ex=(EX_ICS,),
      refs=("10.4", "2.3", "10.1", "2.14"),
      proc=["1. Open the climate screen",
            "2. Press the position at which the AUTO button is shown in an "
            "ATC configuration"],
      er=["1. The climate screen is displayed and no AUTO button is shown",
          "2. The AUTO ECO functionality is not activated"],
      prio="P2", dm=DM_F, split_reason=SPLIT_047),

 # ---------------------------------------------------------- 14.15  Climate Popups
 dict(n=461, req="SWE1-HVAC-099", parent="SWE1-HVAC-099", outline="14.15",
      test_set="Climate Popups",
      title="The comfort controls offered match the vehicle configuration",
      item="The available comfort controls (driver/passenger heated/vented seats, seat zones and heated wheel) shall depend on vehicle configuration",
      pc=PC_COMFORT_CTRL, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("14.15", "2.14", "16.2", "6.3"),
      proc=["1. Open the comfort controls from the status bar",
            "2. Read the comfort controls offered"],
      er=["1. The comfort controls are displayed",
          "2. The comfort controls offered match the comfort features this "
          "vehicle is configured with, and no control is offered for a "
          "feature the vehicle does not have"],
      prio="P1", dm=DM_F,
      emea=dict(ch16_outline="no-counterpart", verdict="yes",
                ch16_sentence="ch16 十八節無任何 HVAC popup 之專章"
                              "（`ch16_mirror_map.tsv` 之 ch14 側全無列）—— "
                              "逐條之答為「ch16 無對應句」，故 EMEA ICS "
                              "車輛上本條無對象，排除成立")),

 # ------------------------------------------------------------ 16.16  ICS Anatomy
 dict(n=462, req="SWE1-HVAC-122-02", parent="SWE1-HVAC-122", outline="16.16",
      test_set="ICS Anatomy",
      title="The seat off icon matches the system configuration",
      item="The off icon of seats shall depend on system configuration",
      pc=PC_ICS, ex=(EX_LOWER,), refs=("16.16", "16.2", "6.3"),
      proc=["1. Open the controls screen",
            "2. Read the off icon of the seat controls"],
      er=["1. The controls screen is displayed",
          "2. An off icon is shown for the seat controls and it matches this "
          "vehicle's system configuration"],
      prio="P2", dm=DM_F),

 # ------------------------------------------------------- 18.1  Home Screen Widget
 dict(n=463, req="SWE1-HVAC-129-01", parent="SWE1-HVAC-129", outline="18.1",
      test_set="Home Screen Widget",
      title="Comfort widget has two screens on the 10.25\" screen",
      item="The Comfort widget shall have two screens",
      pc=PC_WIDGET, pc2=PC_1025, pc3="3. " + PC_COMFORT_FEATURES,
      ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("18.1", "17.3", "2.14", "16.2", "6.3"),
      proc=["1. Open the home screen",
            "2. Move through the Comfort widget screens until the first "
            "screen is shown again"],
      er=["1. The Comfort widget is displayed",
          "2. Two widget screens were shown"],
      prio="P1", dm=DM_F,
      emea=dict(ch16_outline="no-counterpart", verdict="yes",
                ch16_sentence="ch16 十八節無任何 widget 條文"
                              "（`ch16_mirror_map.tsv` 之 ch18 側全無列）—— "
                              "逐條之答為「ch16 無對應句」，故 EMEA ICS "
                              "車輛上本條無對象，排除成立")),
 dict(n=464, req="SWE1-HVAC-129-02", parent="SWE1-HVAC-129", outline="18.1",
      test_set="Home Screen Widget",
      title="First Comfort widget screen is Comfort on the 10.25\" screen",
      item="The first of the two Comfort widget screens shall be Comfort",
      pc=PC_WIDGET, pc2=PC_1025, ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("18.1", "2.14", "16.2", "6.3"),
      proc=["1. Open the home screen",
            "2. Read the first Comfort widget screen"],
      er=["1. The Comfort widget is displayed",
          "2. The first widget screen is the Comfort screen"],
      prio="P1", dm=DM_F,
      emea=dict(ch16_outline="no-counterpart", verdict="yes",
                ch16_sentence="ch16 十八節無任何 widget 條文"
                              "（`ch16_mirror_map.tsv` 之 ch18 側全無列）—— "
                              "逐條之答為「ch16 無對應句」，故 EMEA ICS "
                              "車輛上本條無對象，排除成立")),
 dict(n=465, req="SWE1-HVAC-129-03", parent="SWE1-HVAC-129", outline="18.1",
      test_set="Home Screen Widget",
      title="Second Comfort widget screen is Seats on the 10.25\" screen",
      item="The second of the two Comfort widget screens shall be Seats",
      pc=PC_WIDGET, pc2=PC_1025, pc3="3. " + PC_COMFORT_FEATURES,
      ex=(EX_ICS, EX_EMEA, EX_LOWER),
      refs=("18.1", "17.3", "2.14", "16.2", "6.3"),
      proc=["1. Open the home screen",
            "2. Move to the second Comfort widget screen"],
      er=["1. The Comfort widget is displayed",
          "2. The second widget screen is the Seats screen"],
      prio="P1", dm=DM_F,
      emea=dict(ch16_outline="no-counterpart", verdict="yes",
                ch16_sentence="ch16 十八節無任何 widget 條文"
                              "（`ch16_mirror_map.tsv` 之 ch18 側全無列）—— "
                              "逐條之答為「ch16 無對應句」，故 EMEA ICS "
                              "車輛上本條無對象，排除成立")),
]


def _pc(spec: dict) -> str:
    lines = [spec["pc"]]
    for k in ("pc2", "pc3"):
        if spec.get(k):
            lines.append(spec[k])
    n = len(lines)
    for line in spec.get("ex", ()):
        n += 1
        lines.append(f"{n}. {line}")
    return "\n".join(lines)


def row(spec: dict) -> dict:
    """spec → 一列完整之 TC。"""
    out = {
        "req_id": spec["req"],
        "tc_id": TC_ID_FMT.format(n=spec["n"]),
        "tc_title": spec["title"],
        "test_group": "Comfort",
        "test_set": spec["test_set"],
        "test_item": spec["item"],
        "pre_conditions": _pc(spec),
        "input_test_data": "NA",
        "test_procedure": "\n".join(spec["proc"]),
        "expected_result": "\n".join(spec["er"]),
        "specification_reference": "; ".join(
            f"{STEM}_{o}" for o in dict.fromkeys(spec["refs"])),
        "priority": spec["prio"],
        "design_method": spec["dm"],
        "split_flag": bool(spec.get("split_reason")),
        "split_reason": spec.get("split_reason", "") or "",
        "functional_safety": "NA",
        "estimated_test_time": "",
        "remarks": "",
    }
    if spec.get("emea"):
        out["emea_ics_review"] = spec["emea"]
    return out


def append_gap(tcs: list, parent: str) -> list:
    """把本補產包中屬於 `parent` 之列接在既有列之後（tc_id 明寫，不重編）。"""
    return list(tcs) + [row(s) for s in GAP if s["parent"] == parent]


def gap_for(parent: str) -> list:
    return [row(s) for s in GAP if s["parent"] == parent]


PARENTS = list(dict.fromkeys(s["parent"] for s in GAP))
