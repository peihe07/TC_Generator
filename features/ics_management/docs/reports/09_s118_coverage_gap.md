# 下放包 09 作業 B —— §1.18 獨有行為面之覆蓋缺口清點

> 依據 **R-ICS35(a)**：§1.8 與 §1.18 同時具母條效力，二節獨有之行為面各自為該面之
> **唯一母條** —— 故 §1.18 獨有面之覆蓋缺口現在即可清點，不待 (b) 之生效。
>
> **本作業一條 TC 都不生成**（下放包 09 明令）。本檔只出清單，不作裁決、不代擬條文、
> 不自取 `A-`／`DR-` 編號。任何 TC JSON（含 `specification_reference`）本次**零寫入**。
>
> 實測層由 `features/ics_management/scripts/s118_gap_09.py` 產生；
> 判讀層（§1 之「有無覆蓋」欄）為人工判，判準逐項揭露於 §0，可逐條覆核。

---

## §0 掃描條件與「有無覆蓋」之判準定義

### §0-1 掃描條件

| 項 | 值 |
|---|---|
| 來源規格 | `features/ics_management/inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` |
| 物件抽取／適用性判定 | `features/ics_management/scripts/cfts020_probe.py` 之 `parse()`（**未修改**，以 `importlib` 載入） |
| 適用性判準 | **R-ICS2 v2(b)**：`Radio ∋ {R1L, R1L-R, allSys}` ∧ `EE ∋ {Atlantis High, All}`；`ECU` 軸存在時須含 `{ICS, LTM}`，不存在時不判不適用 |
| 現有 TC 母數 | `features/ics_management/generated/b0{1..6}/b0*_tcs.json`（**唯讀**），實測 **27 條** |
| 現有 TC 之相異錨 | **22 個**（CFTS020 15 + CFTS022 7）；其中指向 §1.18 物件者 **0 個** |
| 訊號綁定佐證 | `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`（`CAN Mapping` 分頁）＋ `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`（唯讀查詢，同 b03 作業 E 之來源） |

### §0-2 母數複驗（不抄上一輪，逐項自測）

| 量 | 本輪實測 | 08 報告所載 | 是否一致 |
|---|---|---|---|
| §1.18 物件總數 | **37** | 37 | ✅ 一致 |
| §1.18 判適用數 | **29** | 29 | ✅ 一致 |
| §1.18 判不適用數 | **8**（`4821682`、`4821692`、`4821711`~`4821716`） | 8（同一組 ID） | ✅ 一致 |
| 現有 TC 數 | **27** | 25（08 報告成文時之數；b06 之 2 條為該包產出） | ⚠️ 差 2，**原因可解釋**，非不符 |
| §1.18 之 Back 面適用物件 | `4821681`、`4821704` | 同 | ✅ 一致 |
| §1.18 之 CLIMATIC_PANEL 點名（**適用者**） | `4821688`、`4821689`、`4821700` | 同 | ✅ 一致 |
| §1.18 之 Logistic 面適用物件 | `4821679` | 同 | ✅ 一致 |

**下放包所列之族成員與實測不符者一處**：下放包 09 §2 將 `4821692` 列入
「CLIMATIC_PANEL 之逐字點名」族，但 `4821692` 依 R-ICS2 v2(b) 判**不適用**
（`Radio=['noSys'] ∩ {R1L,R1L-R,allSys} = ∅`；`EE=['Atlantis Mid'] ∩ {Atlantis High,All} = ∅`
—— **二軸皆實值落空，非軸缺**），故**不在 29 個判適用物件之內**。
08 報告該列之「§1.18（含不適用者）」欄本即已與「§1.18（適用）」欄分列，08 報告無誤；
係下放包引用時將二欄合併。本檔於 §2-2 將 `4821692` 單獨列為「族內但判不適用」，
**不併入缺口計數**，亦不靜默刪除。

### §0-3 「有無覆蓋」之判準（可覆核）

**驗證文字之定義**：一條 TC 之「驗證文字」＝ `test_item` ＋ `test_procedure` ＋ `expected_result`
三欄之串接。**不含** `pre_conditions`、`tc_title`、`reasoning`
—— 理由：前置條件只佈置環境、理由欄只記敘述，二者皆非「實際驗到」；
若納入前置條件，b04-06／b05-01／b05-02 之 `PENDING: DR-ICS6` 佔位文字會使多個物件假性命中。

**第一層（機械層，可原地複現）—— 鑑別 token 比對**

對每一判適用物件之本文，以下列正則抽「鑑別 token」（全為正則，不作語意判讀）：

| 正則 | 抓什麼 |
|---|---|
| `\$[A-Za-z0-9_<>]+\$` | LID／訊號符號（如 `$ICS_KNOB<n>_DIR$`） |
| `\b[A-Z][A-Z0-9_]{4,}\b` | 全大寫訊息／狀態名（如 `CLIMATIC_PANEL`） |
| `"([^"]+)"` | 逐字定值（如 `"Not_Pressed"`） |
| `\bT[A-Za-z][A-Za-z0-9_]{3,}\b` | 時間符號（如 `Tbutton`、`TPeriodToCountKnobDetents`） |

去停用詞（`ICS`／`TLM`／`CFTS`／`HMI`／`SHALL`／`SIGNAL`／`SCREEN`／`CLIMATIC`／`PANEL` 等泛用大寫詞，
全表見腳本 `STOP`）。比對前正規化：去 `$`、去 `<n>` 索引、去非英數字元、轉小寫
—— 使母條之 `$ICS_KNOB<n>_DIR$` 能與 TC 逐字之 `$CLIMATIC_PANEL.Radio_Knob2_DIR$` 對上。

**第一層之已知不足（必須明說）**：token 比對會產生**假性全中**。
最清楚之反例為 `4821700`（「TLM shall acquire CLIMATIC_PANEL message…」）——
其唯一鑑別 token 為 `CLIMATIC_PANEL`，而 27 條中有 22 條之驗證文字含該字串，
機械層判「全 token 同時命中 22 條」，但**無任一條驗到「acquire 並據以啟閉內部功能」此一行為**。
同理 `4821710` 機械層判 b03-01~04 全中，實際上該四條無一驗 `Front_Panel_OnOff.Info`。
故第一層**只作為必要篩選，非充分條件**。

**第二層（判讀層）—— 行為三要件 C1/C2/C3**

一物件判「**有覆蓋**」，須存在至少一條 TC 同時滿足：

- **C1 主體對位**：該 TC 之驗證文字含該物件之全部鑑別 token（第一層命中）。
- **C2 行為對位**：該 TC 之 `test_procedure` 有**一步實際施加該物件所述之觸發條件**，
  且 `expected_result` 有**一項實際判該物件所述之結論**。
  觸發或結論任一僅「順帶提及」而未施加／未判者，不算。
- **C3 無佔位遮蔽**：C2 所依之那一步／那一項，其判斷值**不是** `PENDING: DR-…` 佔位。
  佔位僅出現在同條之「supporting observation」而不承載該判斷者，不算遮蔽。

三值：

- **有覆蓋**：C1∧C2∧C3 成立。
- **部分覆蓋**：C1 成立、C2 只對位一半（觸發施加但結論未判，或母條為複合而只驗其一分支）。
  **本檔將「部分覆蓋」計為仍有殘留缺口**，於 §3 一併列其解鎖條件。
- **無覆蓋**：C2 全不成立。

**另設一類「非行為母條（NB）」**（不列為缺口、不列解鎖條件）：
物件為 `Description` 型、或本文為純指向句（`See …`／`Refer to par. …`）、
或為 LID 清單、或為適用條件宣告 —— **無可驗行為**，其「無 TC」不構成覆蓋缺口。
`4821681` 之歸此類係 **R-ICS35(g) 逐字認定**（「ICS 側 `4821681` 為 LID 清單非行為母條」）。

**再設一類「本作業範圍外（OS）」**：下放包 09 明令
`4821683`~`4821689` 之**泛用母條不在本作業範圍**（A-ICS55 繫於 R-ICS35(b)）。
其與 CLIMATIC_PANEL 族之重疊處置見 §4。

---

## §1 §1.18 之 29 個判適用物件 —— 逐一覆蓋判

（`§` 欄為節號；「行為摘要」為本文之壓縮，非逐字，逐字見規格原文與腳本 `--objects` 輸出。）

| # | ObjectID | § | Artifact Type | 行為摘要 | 有無覆蓋 | 若有／部分則為哪條 TC |
|---|---|---|---|---|---|---|
| 1 | `4821675` | 1.18.1 | Description | 「TLM 之多數指令存在於 ICS 節點」之敘述句 | **NB** 非行為母條（Description 型） | — |
| 2 | `4821676` | 1.18.1 | Subsystem Functional Requirement | 宣告本節需求於 8 種 Ignition Working Conditions 皆有效 | **NB** 非行為母條（適用條件宣告，無獨立可驗行為） | —（附註：27 條之 `pre_conditions` 一律只寫 `exited SLEEP MODE`，無一枚舉 Ignition 狀態） |
| 3 | `4821679` | 1.18.1.1.1 | Subsystem Functional Requirement | ICS 處 logistics mode（依 `{VF601}`）時報 `$PowerModeSts_CStack$ = [Logistic_Mode_ON]`，否則 `[Standard_Power]` | **無覆蓋** | —（機械層：`$PowerModeSts_CStack$`、`VF601` 皆 0 條命中） |
| 4 | `4821681` | 1.18.1.1.2 | Subsystem Functional Requirement | 「見 LID／CAN Mapping 檔」＋列 5 個 LID（`$ICSPowerButton$`／`$Enter_Button$`／`$ICSScreenOffButton$`／`$Back_Button$`／`$ICSMuteButton$`） | **NB** 非行為母條（LID 清單；**R-ICS35(g) 逐字認定**） | —（機械層雖有 4/5 token 命中，係他條 TC 之訊號名巧合，非驗此清單） |
| 5 | `4821683` | 1.18.1.1.2 | Subsystem Functional Requirement | ICS 於 BH-CAN 送機械按鍵狀態予 TLM（泛用引言） | **OS** 本作業範圍外（`4821683`~`4821689` 泛用母條） | — |
| 6 | `4821684` | 1.18.1.1.2 | Subsystem Functional Requirement | `For all buttons`：未按時送 `"Not_Pressed"` | **OS** 範圍外 | —（機械層全中 b01-01/02/03、b02-02） |
| 7 | `4821685` | 1.18.1.1.2 | Subsystem Functional Requirement | 按下時於 `Tbutton` 內送 `"Pressed"` | **OS** 範圍外 | —（機械層全中 b01-01） |
| 8 | `4821686` | 1.18.1.1.2 | Subsystem Functional Requirement | 持續按住時以 `Tbutton` 速率續送至放開 | **OS** 範圍外 | —（機械層全中 b01-01） |
| 9 | `4821687` | 1.18.1.1.2 | Subsystem Functional Requirement | 放開後送 `"Not_Pressed"` | **OS** 範圍外 | —（機械層全中 b01-01/02/03、b02-02） |
| 10 | `4821688` | 1.18.1.1.2 | Subsystem Functional Requirement | **多鍵同時按下**時，ICS 須於 **`CLIMATIC_PANEL`** 訊息中將**全部**相關訊號一併置 `"Pressed"` | **無覆蓋** | —（機械層假性全中 14 條；27 條無一條之 `test_procedure` 同時按下二鍵以上，故 C2 不成立） |
| 11 | `4821689` | 1.18.1.1.2 | Subsystem Functional Requirement | **每一次**按鍵事件變化（按下或放開）須使 ICS 於 `Tbutton` 內送出**更新後之 `CLIMATIC_PANEL` 幀** | **無覆蓋** | —（機械層全中 b01-01，但 b01-01 之 120 s 為 stuck DTC mature time，非 `Tbutton`；無一條量「事件變化→幀更新」之時限） |
| 12 | `4821691` | 1.18.1.1.3 | Subsystem Functional Requirement | 「見 LID／CAN Mapping 檔」＋列 4 個旋鈕 LID | **NB** 非行為母條（LID 清單） | — |
| 13 | `4821693` | 1.18.1.1.3 | Subsystem Functional Requirement | ICS 於 BH-CAN 送旋鈕狀態（泛用引言，涵蓋 KNOB1 與 KNOB2） | **部分覆蓋** | b04-01～b04-05（**僅 KNOB2**）；**KNOB1 之訊號面無 TC**（b01-06 只驗音量級數之可見結果，不讀 `$ICS_KNOB1_*$`） |
| 14 | `4821694` | 1.18.1.1.3 | Subsystem Functional Requirement | 未轉動時 `DIR="Knob_no_change"`、`VAL="0"` | **有覆蓋** | b04-03（靜止 5 s 讀二次 DIR=0）、b04-04（DIR=0 且 VAL=0） |
| 15 | `4821695` | 1.18.1.1.3 | Subsystem Functional Requirement | 轉動中於 `TPeriodToCountKnobDetents` 期內計算 detent 數 | **有覆蓋** | b04-05（一次連續轉三格 → `VAL=3`；計數窗 50 msec 為具體值，非佔位） |
| 16 | `4821696` | 1.18.1.1.3 | Subsystem Functional Requirement | 送 `DIR="Knob_increment"/"Knob_decrement"`、`VAL` 介於 `"1"`~`"63"`，速率為 `TPeriodToCountKnobDetents` | **有覆蓋** | b04-01（increment, VAL=1）、b04-02（decrement, VAL=1）、b04-05（VAL=3） |
| 17 | `4821697` | 1.18.1.1.3 | Subsystem Functional Requirement | 判定無變化時以該速率送 `DIR="Knob-no_change"`、`VAL="0"` | **有覆蓋** | b04-04（DIR=0、VAL=0，並記錄二連續幀之 cycle time） |
| 18 | `4821698` | 1.18.1.1.3 | Subsystem Functional Requirement | 續以排定週期速率送出，直至再次轉動 | **有覆蓋** | b04-04（步驟 3 量 cycle time、步驟 4 再次轉動後 DIR=1） |
| 19 | `4821700` | 1.18.1.2 | Subsystem Functional Requirement | **TLM 須取得 `CLIMATIC_PANEL` 訊息**，並依收到之訊號值啟／閉其內部功能 | **無覆蓋** | —（機械層假性全中 22 條；無一條以「TLM 取得該訊息並據以啟閉內部功能」為 `expected_result`） |
| 20 | `4821701` | 1.18.1.2 | Subsystem Functional Requirement | TLM 依 `$ICS_KNOB1_DIR/VAL$` 調音量，並須將 `Volume_Knob_Val.Info`／`Volume_Knob_Dir.Info` 置同值 | **部分覆蓋** | b01-06（驗音量級數 +3，即「調音量」半）；**`Volume_Knob_*.Info` 之置值面無 TC**（該二訊號於 LID mapping 表與二 DBC 皆查無，見 §3-4） |
| 21 | `4821702` | 1.18.1.2 | Subsystem Functional Requirement | TLM 依當前畫面，據 `$ICS_KNOB2_DIR/VAL$` 管理其畫面與瀏覽清單 | **有覆蓋** | b04-06（browse）、b05-01（scroll）、b05-02（tune）；三條之 `PENDING: DR-ICS6` 僅在 `pre_conditions`，不遮蔽 C2 之判斷（C3 成立） |
| 22 | `4821703` | 1.18.1.2 | Subsystem Functional Requirement | 收到 `DIR="Knob_no_change"` 時，TLM 須忽略 `VAL` | **有覆蓋** | b04-03（DIR=0 期間畫面內容不變，即「不作動」之判） |
| 23 | `4821704` | 1.18.1.2 | Subsystem Functional Requirement | TLM 依當前畫面，據 **`$Enter_Button$` 與 `$Back_Button$`** 管理其畫面／瀏覽清單 | **部分覆蓋** | b04-07（**僅 Enter** 面）；**`$Back_Button$` 面 0 條**（`$Back_Button$` 於 27 條驗證文字中 0 命中） |
| 24 | `4821705` | 1.18.1.2 | Subsystem Functional Requirement | TLM 處 `"Screen Off"` 模式且收 `$ICSScreenOffButton$` 由 `"Not_Pressed"`→`"Pressed"` 時，設 Screen On | **有覆蓋** | b03-08（HU Screen OFF 下按 Screen Off 鍵 → `Radio_btn2=1`，前一畫面回復）；`PENDING: DR-ICS8` 僅在 supporting observation，C3 成立 |
| 25 | `4821706` | 1.18.1.2 | Subsystem Functional Requirement | TLM 處 `"Screen On"` 模式且收同一上升緣時，設 Screen Off | **有覆蓋** | b03-05 ＋ b03-07（按下 → 三秒窗 → 螢幕全暗）；**附註**：§1.18 本條無三秒窗，該窗為 §1.8 獨有，故此覆蓋屬「行為等值」而非逐字對位 |
| 26 | `4821707` | 1.18.1.2 | Subsystem Functional Requirement | 「Screen On／Screen Off 模式之細節見 TLM HMI」 | **NB** 非行為母條（純指向句） | — |
| 27 | `4821708` | 1.18.1.2 | Subsystem Functional Requirement | 「TLM 依 `$ICSPowerButton$` 之行為見 `TLM Operative States management` 節」 | **NB** 非行為母條（純指向句） | —（機械層之 b03-01~04 命中僅來自 `$ICSPowerButton$` 一詞） |
| 28 | `4821709` | 1.18.1.2 | Subsystem Functional Requirement | TLM 依 `$ICSMuteButton$` 調音訊輸出，並須將 `Mute.Req` 置同值 | **部分覆蓋** | b06-01／b06-02（驗靜音／解靜音之可聽狀態）；**`Mute.Req` 之置值面無 TC**（該訊號於 LID mapping 表與二 DBC 皆查無） |
| 29 | `4821710` | 1.18.1.2 | Subsystem Functional Requirement | TLM 須將 `Front_Panel_OnOff.Info` 置為與 `$ICSPowerButton$` 同值 | **無覆蓋** | —（機械層假性全中 b03-01~04；該四條驗 `$TGW_DISP_STAT$`／`$RQ_DISP_INTS$`，無一讀 `Front_Panel_OnOff.Info`） |

### §1-1 計數（實測，含 NB／OS 之分離）

| 類 | 數 | ObjectID |
|---|---|---|
| **有覆蓋** | **9** | `4821694`、`4821695`、`4821696`、`4821697`、`4821698`、`4821702`、`4821703`、`4821705`、`4821706` |
| **部分覆蓋**（仍有殘留缺口） | **4** | `4821693`、`4821701`、`4821704`、`4821709` |
| **無覆蓋** | **5** | `4821679`、`4821688`、`4821689`、`4821700`、`4821710` |
| **NB 非行為母條**（不計缺口） | **6** | `4821675`、`4821676`、`4821681`、`4821691`、`4821707`、`4821708` |
| **OS 本作業範圍外**（泛用母條） | **5** | `4821683`、`4821684`、`4821685`、`4821686`、`4821687` |
| 合計 | **29** | — |

**若以「有／無」二分回答下放包之問**（NB 與 OS 併入「不計」）：
於 **18 個有可判行為且在範圍內**之物件中，**有覆蓋 9 個、非全覆蓋 9 個**
（＝ 部分覆蓋 4 ＋ 無覆蓋 5）。
於 **29 個判適用物件**之總母數上：有覆蓋 9、部分覆蓋 4、無覆蓋 5、NB 6、OS 5。

**另一機械層事實（獨立於上表）**：27 條 TC 之 22 個相異錨中，
**指向任一 §1.18 物件者 0 個** —— 即上表所有「有覆蓋」皆為**行為等值覆蓋**，
無一為錨層之直接覆蓋。此與 R-ICS35(f)「25 條既有錨全部維持有效」相容
（既有錨皆屬 §1.8／CFTS022），**本檔不因此建議任何改錨**。

---

## §2 獨有面三族之缺口（逐族一節）

三族之族籍依 08 報告 §2 之「僅 §1.18 有」列，**ObjectID 已於本輪逐一複驗**。

### §2-1 `Back_Button` 族

| ObjectID | § | 本輪判 | 缺口內容 |
|---|---|---|---|
| `4821681` | 1.18.1.1.2 | **NB**（LID 清單） | **不構成缺口** —— R-ICS35(g) 逐字：「ICS 側 `4821681` 為 LID 清單非行為母條」 |
| `4821704` | 1.18.1.2 | **部分覆蓋** | **缺口 G1**：`$Back_Button$` 之行為面 0 條。母條原文為 `$Enter_Button$` 與 `$Back_Button$` 之並列複合句；b04-07 只驗 Enter 半（`$CLIMATIC_PANEL.Radio_btn1$`），Back 半無任何 TC。`$Back_Button$` 於 27 條驗證文字中命中 **0** 次 |

**族缺口數：1**（G1）。族內物件 2 個，1 個為 NB。

複驗註：08 報告「Back 按鍵行為」列所載 `4821681, 4821704` 與本輪實測**一致**。

### §2-2 `CLIMATIC_PANEL` 之逐字點名族

| ObjectID | § | R-ICS2 v2(b) 判 | 本輪覆蓋判 | 缺口內容 |
|---|---|---|---|---|
| `4821688` | 1.18.1.1.2 | 適用 | **無覆蓋** | **缺口 G2**：多鍵同時按下時，`CLIMATIC_PANEL` 訊息中**全部**相關訊號須一併為 `"Pressed"`。27 條中無一條之 `test_procedure` 施加「同時按下二鍵以上」之觸發 |
| `4821689` | 1.18.1.1.2 | 適用 | **無覆蓋** | **缺口 G3**：每一次按鍵事件變化（press 或 release）須使 ICS 於 `Tbutton` 內送出更新後之 `CLIMATIC_PANEL` **幀**。27 條中無一條量「事件變化 → 幀更新」之時限；b01-01 之 120 s 係 stuck DTC mature time，屬 §1.8 之量，不可挪用（同 R-ICS9(d) 之意旨） |
| `4821692` | 1.18.1.1.3 | **不適用** | — | **不列缺口**。`Radio=['noSys']`、`EE=['Atlantis Mid']` 二軸皆實值落空。本文為 `Volume_Knob_Dir.Req`／`Tune_Scroll_*.Req` 對 `CLIMATIC_PANEL.Radio_Knob*` 之映射表。列於此僅為說明下放包之族成員清單與實測之差（見 §0-2），**不併入計數** |
| `4821700` | 1.18.1.2 | 適用 | **無覆蓋** | **缺口 G4**：TLM 須**取得** `CLIMATIC_PANEL` 訊息並依其值啟／閉內部功能。27 條驗的都是 HU 對單一按鍵／旋鈕之個別回應，無一驗「取得整則訊息並據以啟閉功能」此一母條層行為 |

**族缺口數：3**（G2、G3、G4）。族內判適用物件 3 個，另 1 個（`4821692`）判不適用。

複驗註：08 報告該列之「§1.18（適用）」欄載 `4821688, 4821689, 4821700`，
「含不適用者」欄載 `4821688, 4821689, 4821692, 4821700` —— **與本輪實測一致**，08 報告無誤。

### §2-3 Logistic Mode 狀態回報族

| ObjectID | § | 本輪判 | 缺口內容 |
|---|---|---|---|
| `4821679` | 1.18.1.1.1 | **無覆蓋** | **缺口 G5**：ICS 處 logistics mode（依 `{VF601}`）時須報 `$PowerModeSts_CStack$ = [Logistic_Mode_ON]`，否則 `[Standard_Power]`。27 條中 `$PowerModeSts_CStack$` 與 `VF601` 皆 **0** 命中；亦無任一條之 `pre_conditions` 佈置 logistics mode |

**族缺口數：1**（G5）。

複驗註：08 報告「Logistic／Power Mode 狀態回報」列所載 `4821679` 與本輪實測**一致**。

### §2-4 三族外之缺口（一併列出，不靜默省略）

下放包只點名三族，但 §1 之判讀另得出 **4 個不屬三族之殘留缺口**。
列出以免遺漏，其歸屬由分析層另定：

| 編號 | ObjectID | 缺口內容 |
|---|---|---|
| G6 | `4821710` | `Front_Panel_OnOff.Info` 須與 `$ICSPowerButton$` 同值 —— 無 TC |
| G7 | `4821709`（殘留） | `Mute.Req` 須與 `$ICSMuteButton$` 同值 —— 無 TC（可聽面已由 b06 覆蓋） |
| G8 | `4821701`（殘留） | `Volume_Knob_Val.Info`／`Volume_Knob_Dir.Info` 須與 `$ICS_KNOB1_*$` 同值 —— 無 TC（音量面已由 b01-06 覆蓋） |
| G9 | `4821693`（殘留） | 旋鈕狀態送出之 **KNOB1 訊號面** —— 無 TC（KNOB2 面已由 b04 覆蓋） |

---

## §3 每一缺口之解鎖條件（三分類）

分類定義（依下放包）：
- **[T] 繫於作業 A 之 TLM 指涉量測** —— 該母條主詞為 TLM，可用與否待 R-ICS35(b)。
- **[D] 繫於 DR-ICS6** —— 需 HMI Logic and Flow 之畫面流方可定義觸發／判準。
- **[N] 現在即可生成** —— 母條主詞為 ICS／HU 且無佔位依賴。

| 缺口 | ObjectID | 母條主詞（逐字所據） | 分類 | 判斷理由 |
|---|---|---|---|---|
| **G1** | `4821704` | **TLM**（`TLM shall manage its screens and/or browsing lists according to $Enter_Button$ and $Back_Button$`） | **[T]** | **R-ICS35(g) 逐字**：「行為母條 `4821704` 主詞為 TLM —— 其可用與否正是 (b) 待量之事。**009 於 (b) 定案前不生成**」。**次要依賴亦存在**：該母條末句 `See TLM CFTS and TLM HMI for details`，其畫面流須 DR-ICS6；但 R-ICS35(g) 之逐字令為**主**，故歸 [T] 不歸 [D] |
| **G2** | `4821688` | **ICS**（`ICS shall send all the relative BH-CAN signals in CLIMATIC_PANEL message, set to "Pressed"`） | **[N]** | 主詞 ICS，非 TLM；不涉畫面流故不繫 DR-ICS6；訊號名已由 b03 作業 E 於 `PDT27_E2A_R4_BHCAN.dbc` 實測（`CLIMATIC_PANEL` = `BO_ 1050`、發送節點 ICS、`Radio_btn*` 已具 `VAL_` 列舉）；定值 `"Pressed"` 為逐字常數，非符號。**無佔位依賴** |
| **G3** | `4821689` | **ICS**（`shall cause the ICS to send CLIMATIC_PANEL frame … within the time period of Tbutton`） | **[N]（附帶佔位）** | 主詞 ICS、不涉 TLM、不涉畫面流 —— 三分類中只能落 [N]。**但 `Tbutton` 於 CFTS020 為符號而無定值**（同 `Tstuck_button` 之情形），嚴格言之非「無佔位依賴」。詳見 §3-3 之提請 |
| **G4** | `4821700` | **TLM**（`TLM shall acquire CLIMATIC_PANEL message and activate/deactivate internal functionalities`） | **[T]** | 主詞逐字為 TLM；「TLM 是否即本 DUT」正是作業 A 待量者（A-ICS56）。量測未回前不可判其可用 |
| **G5** | `4821679` | **ICS**（`ICS shall report $PowerModeSts_CStack$`） | **[N]（附帶佔位）** | 主詞 ICS、不涉 TLM、不涉畫面流 —— 落 [N]。**但存在二項實測落空**，見 §3-2 |
| G6 | `4821710` | **TLM**（`TLM has to set signal Front_Panel_OnOff.Info`） | **[T]** | 主詞逐字為 TLM；且 `Front_Panel_OnOff.Info` 於 LID mapping 表與二 DBC 皆查無 |
| G7 | `4821709`（殘留） | **TLM**（`TLM shall set Mute.Req signal`） | **[T]** | 同上；`Mute.Req` 於 LID mapping 表與二 DBC 皆查無 |
| G8 | `4821701`（殘留） | **TLM**（`TLM shall set Volume_Knob_Val.Info and Volume_Knob_Dir.Info`） | **[T]** | 同上；二訊號於 LID mapping 表與二 DBC 皆查無 |
| G9 | `4821693`（殘留） | **ICS**（`The ICS shall send signals on the BH-CAN to communicate the status of the rotary knobs`） | **[N]** | 主詞 ICS；KNOB1 之訊號名已於 b03 作業 E 實測（`CLIMATIC_PANEL.Radio_Knob1_DIR`，`BO_ 1050`、節點 ICS、`VAL_ 0 "Knob_no_change" 1 "Knob_increment" 2 "Knob_decrement" 3 "Knob_enter"`）。無佔位依賴 |

### §3-1 三分類計數

| 分類 | 三族之內 | 三族之外 | 合計 |
|---|---|---|---|
| **[T] 繫於 TLM 指涉量測** | **2**（G1、G4） | 3（G6、G7、G8） | **5** |
| **[D] 繫於 DR-ICS6** | **0** | 0 | **0** |
| **[N] 現在即可生成** | **3**（G2、G3、G5） | 1（G9） | **4** |
| 合計 | **5** | 4 | **9** |

**[D] 為 0 之說明**：三族之缺口無一以「畫面流未知」為其**主要**阻塞。
唯一沾到 DR-ICS6 者為 G1（`4821704` 之 `See TLM CFTS and TLM HMI for details`），
但其主要阻塞由 R-ICS35(g) 逐字定為 TLM 量測，故計入 [T] 而非 [D]，**不重複計數**。
若分析層認為 G1 應雙記，本檔之三族 [T]=2／[D]=0 應改讀為 [T]=2／[D]=1（G1 重複），
惟本檔不自行如此調和 —— **只列不裁**。

### §3-2 G5（`4821679`）之二項實測落空 —— 影響其 [N] 之成色

以 `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`（`CAN Mapping`，Atlantis High 群組欄）
與二綁定 DBC 實測：

| 項 | 實測 |
|---|---|
| LID `PowerModeSts_CStack` 於 mapping 表 | **有** → `STATUS_CENTERSTACK.PowerModeSts_CStack`（CAN-B；`0 = Standard_Power / 1 = Logistic_Mode_ON / 2 = Logistic_Mode_PR / 3 = Not_Used`） |
| `STATUS_CENTERSTACK` 於 `PDT27_E2A_R4_BHCAN.dbc` | **查無** |
| `STATUS_CENTERSTACK` 於 `PDT27_E2A_R5_FDCAN8.dbc` | **查無** |
| `PowerModeSts_CStack` 字串於二 DBC | **皆 0 命中** |
| 旁證（非本 LID）：另一 LID `PowerModeSts` → `BCM_FD_9.PowerModeSts` | 二 DBC 中 `PowerModeSts` 存在於 `BO_ 854 STATUS_BH_BCM1`，**發送節點為 BCM**（非 ICS），`VAL_` 逐字為 `0 "Standard_Power" 1 "Logistic_Mode_ON" 2 "Logistic_Mode_PR" 3 "LogisticModeON_and_EngineON"` |

二點後果，**本檔只陳述不處置**：
1. G5 之**觀察訊號於二綁定 DBC 皆查無** —— 依 b03 作業 E 之升級判準（「二 DBC 皆查無 → E4」），
   此為 **E4 形態**。故 G5 雖主詞為 ICS，**並非「無佔位依賴」**：其 CAN 訊號名須另立 DR
   或以 `PENDING:` 佔位方能落 `test_procedure`。
2. 母條之觸發側 `ICS is in logistics mode (per {VF601})` 之進入程序，
   其定義在 `{VF601}` —— **不在本 feature 之 5 個 inputs 內**（跨 feature 之 vehicle_setting 線）。
   本檔不越界取用，僅記此一依賴。

**需新編號**（不自取）：上開第 1 點（`$PowerModeSts_CStack$` 之 LID 有映射而二 DBC 皆查無）
建請以 **`A-ICS?`** 立案。第 2 點（`{VF601}` 跨 feature 依賴）是否另立，由分析層定。

### §3-3 G3（`4821689`）之 `Tbutton` 佔位 —— 三分類無適格者之提請

G3 主詞為 ICS、不涉 TLM、不涉 HMI 畫面流，故三分類中**只能落 [N]**；
但下放包對 [N] 之定義為「母條主詞為 ICS／HU **且無佔位依賴**」，
而 `Tbutton` 於 CFTS020 §1.18 全節僅以符號出現、**無任何定值**
（同 b02 對 `<Tstuck_button>` 之處置：全數以 `PENDING: DR-ICS10` 佔位，
且**不挪用** CFTS022 之 120 s，R-ICS9(d)）。

故 G3 屬「主詞可用但量值待補」之第四形態，三分類未涵蓋。
本檔**不自行調和**：於 §3-1 仍計入 [N]（因三選一無他適格者），
但於此明白標注其附帶佔位，計數之讀法由分析層定。
`Tbutton` 是否沿用 DR-ICS10 之提問或另立，同樣不自取編號 —— 需要時記為 **`DR-ICS?`**。

### §3-4 [T] 類之共同佐證（供作業 A 參考，非結論）

G4、G6、G7、G8 四者之 TLM 側訊號（`Front_Panel_OnOff.Info`、`Mute.Req`、
`Volume_Knob_Val.Info`、`Volume_Knob_Dir.Info`）於
`Logical Identifiers and CAN Mapping v1_78.xlsx` 之 `CAN Mapping` 全表逐格搜尋
**皆 0 命中**，於二綁定 DBC 亦 **皆 0 命中**。

此為**中性事實**，二向皆可解讀，本檔**不自行推論**：
可讀為「TLM 側訊號不在 ICS 之 LID／DBC 範圍內，支持 TLM 非本 DUT」；
亦可讀為「本 feature 綁定之二 DBC 本就只涵蓋 BH-CAN 之 ICS 側，未涵蓋 TLM 內部匯流排」。
判讀權屬作業 A 與 R-ICS35(b)。

---

## §4 範圍重疊之處理說明（泛用母條 vs CLIMATIC_PANEL 族）

### §4-1 重疊之實況

下放包同時下達二條互相牴觸之範圍令：

- **排除令**：`4821683`~`4821689` 之**泛用母條不在本作業範圍**（A-ICS55 繫於 R-ICS35(b)）。
- **納入令**：`4821688`／`4821689` 因屬「CLIMATIC_PANEL 逐字點名」族而**在範圍內**。

`4821688`、`4821689` 二者同時落在排除令之 ID 區間與納入令之族內，構成重疊。
另 `4821683`~`4821687` 五個只落排除令，無重疊。

### §4-2 本檔之處置（明示，不靜默取捨）

**採納入令優先**，理由三項：

1. **下放包自身已明文指定優先序** —— 「但 `4821688`／`4821689` 因屬『CLIMATIC_PANEL
   逐字點名』族而在範圍內」一語，其句法（「但…」）即為對前一句排除令之例外設定。
   本檔照辦，非自行取捨。
2. **二令之立法目的不同，實際上不牴觸**：
   排除令之根據為 **A-ICS55** —— 其問題是「**泛用母條得否充錯、是否造成重複追溯**」，
   即**錨層**之問題，繫於 R-ICS35(b)。
   本作業之產出為**覆蓋缺口清單**，不改任何 `specification_reference`、不生成任何 TC，
   **不觸及 A-ICS55 所問之錨層問題**。
   納入令之根據為 R-ICS35(a) —— §1.18 獨有面之**唯一母條**地位，屬**覆蓋層**。
   二者分屬不同層，故 `4821688`／`4821689` 可在覆蓋層被清點，而其錨層歸屬仍懸而未決。
3. **`4821688`／`4821689` 之獨有性經本輪實測成立**：二者本文含 `CLIMATIC_PANEL` 逐字，
   而 §1.8 全域（490 物件）該行為之 §1.18-only 判定於 08 報告 §2 已載，
   本輪就該二 ID 之族籍複驗一致。其行為若不在本作業清點，
   將無其他作業會清點（§1.8 側無對應母條），構成真正的遺漏。

### §4-3 處置之界限（本檔明確不做的事）

- **不將 `4821688`／`4821689` 認定為任何 TC 之錨** —— 錨層仍繫 A-ICS55／R-ICS35(b)。
- **不因其在範圍內而生成 TC** —— 下放包明令一條不生成；E6 之處置見 §5。
- **不將 `4821683`~`4821687` 一併納入** —— 該五者無納入令，`Not_Pressed`／`Pressed`／
  `Tbutton` 之泛用行為面留待 A-ICS55 與 R-ICS35(b) 處理。
  惟其機械層命中已列於 §1 之表（標 **OS**），供將來覆核，避免將來重掃。
- **不將 `4821692` 納入族內計數** —— 其判不適用，理由見 §0-2、§2-2。

---

## §5 E6 升級 —— 觸發，且不生成

**E6 觸發**：本輪發現「現在即可生成」之缺口共 **4 個**（三族之內 3 個：G2、G3、G5；
三族之外 1 個：G9）。

依下放包之令 **「列出即可，絕不生成」**，本檔對此四者：

- **未生成任何 TC**（全 feature 本輪 TC JSON 零寫入，`specification_reference` 零變更）。
- **未預先擬定** 任何 `test_item`／`test_procedure`／`expected_result` 之草稿。
- 是否生成、以何 `req_id` 生成、依 R-ICS35(a) 之何款立錨，**由分析層另行下放**。

四者之成色不齊，分析層下放前宜先分辨：

| 缺口 | 主詞 | 訊號綁定實測 | 量值 | 生成之現實可行性 |
|---|---|---|---|---|
| **G2** `4821688` | ICS | ✅ `CLIMATIC_PANEL` = `BO_ 1050`、節點 ICS、`Radio_btn*` 有 `VAL_` | 無需量值（純狀態） | **最乾淨**，無任何佔位 |
| **G9** `4821693`（KNOB1 面） | ICS | ✅ `CLIMATIC_PANEL.Radio_Knob1_DIR/VAL`、節點 ICS、有 `VAL_` | 無需量值 | **乾淨**，無佔位；惟須確認與 SWE-ICS-001／002（音量面）之切分不重複 |
| **G3** `4821689` | ICS | ✅ 同 G2 | ⚠️ `Tbutton` 無定值 | 可生成但須 `PENDING:` 佔位（見 §3-3） |
| **G5** `4821679` | ICS | ❌ `STATUS_CENTERSTACK` 於二 DBC 皆查無（E4 形態） | 值域已知（`VAL_` 在 mapping 表） | 觸發側另依 `{VF601}`（跨 feature）；**兩處佔位**（見 §3-2） |

---

## §6 本檔之寫入範圍（自證未越禁區）

本輪只寫二檔：

- `features/ics_management/docs/reports/09_s118_coverage_gap.md`（本檔，新建）
- `features/ics_management/scripts/s118_gap_09.py`（新建）

**未寫入**：`RULINGS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`framework.md`、
`ANALYSIS_LOCK.md`、`docs/handoff/**`、`feature.yaml`、任何 TC JSON、
repo 根之 `scripts/`／`docs/runtime/`／`docs/fw036/`、
`features/ics_management/scripts/` 下之任何既有檔（`cfts020_probe.py` 以 `importlib` 唯讀載入）。
**未執行任何 git 指令**。**未自取 `A-`／`DR-` 編號**（需要處一律寫 `A-ICS?`／`DR-ICS?`）。

實測層可原地複現：

```
python3 features/ics_management/scripts/s118_gap_09.py            # §0 母數
python3 features/ics_management/scripts/s118_gap_09.py --objects  # §1 機械層逐物件
python3 features/ics_management/scripts/s118_gap_09.py --tcs      # 27 條 TC 與其錨
```
