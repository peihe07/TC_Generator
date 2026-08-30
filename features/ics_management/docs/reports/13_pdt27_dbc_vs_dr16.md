# 13_pdt27_dbc_vs_dr16 — `PDT27_E2A_R1_BHCAN2.dbc` 對 DR-ICS16 之填補程度（唯讀量測）

下放包 13 作業 C。**本報告只量測、不採認、不裁決、不結案。**
未生成任何 TC、未改任何錨或 reasoning、未動分析層五簿、未自取 `A-`／`DR-` 編號。
`forms/PDT27_E2A_R1_BHCAN2.dbc` **只讀不綁定**：`feature.yaml` 與 `FORMS.md` 皆未動。

## §0 量測條件與素材指紋

量測腳本：`features/ics_management/scripts/pdt27_probe_13.py`（本包新建，唯讀）。

讀法（沿 `features/ics_management/scripts/crossref_probe_12.py` 之慣例）：

- `.dbc` 一律以 `latin-1` 開檔。
- **`BO_` 區塊不以空行分隔**：以 `^BO_ ` 行為分段起點自行切段，段內收所有縮排之
  `SG_ ` 行，遇下一 `^BO_ ` 或任何其他頂層關鍵字（`BO_TX_BU_`／`CM_`／`BA_`／
  `VAL_` …）即結束當前段。
- 「發送節點」取 `BO_` 行末之單一節點；「接收節點」取該 `SG_ ` 行末之收方欄；
  `BO_TX_BU_` 另記（DBC 語意為**追加發送方**，非收方）。

| 檔 | 路徑 | sha256 | 行數 | `BO_` 段數 | `BO_TX_BU_` 條數 | `BU_:` 節點表 |
|---|---|---|---|---|---|---|
| A｜R1_BHCAN2（**未綁定**） | `forms/PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60` | 3367 | 63 | 14 | `BU_: ETM FPDM LTM SGW` |
| B｜R4_BHCAN（`reference.dbc_b`） | `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` | `9ef1ec9830fc8018b23d0e36dbd7ca6023b9b0a03124095726eb5583a01930d0` | 8590 | 155 | 0 | `BU_: AMP ANC BCM DALM DCSD DDM DSM ECC ICS PDM PFTM PSM PSSM PTGM SGW SMMD SMMP` |
| C｜R5_FDCAN8（`reference.dbc_fd`） | `features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2` | 20971 | 323 | 28 | `BU_: ETM LTM SGW TBM` |

B、C 二檔之 sha256 與 `features/ics_management/feature.yaml` 之 `reference.dbc_b`／
`reference.dbc_fd` 宣告值逐字相同（本包重算）。

本 DUT：Radio `R1L`／EE `Atlantis High`／ECU `LTM`／變體 `Disassociated`。

---

## §1 二訊號於 PDT27（A 檔）之逐字資料

### §1-0 實際拼法之確認

佔位所書之字面 `TGW_DISP_STAT` 與 `Telematic_Power`，**於三檔皆非實際訊號名**：

- `SG_` 名等於 `TGW_DISP_STAT` 者：A 檔 **0 筆**、B 檔 **0 筆**、C 檔 **0 筆** — **查無**。
- `SG_` 名等於 `Telematic_Power` 者：A 檔 **0 筆**、B 檔 **0 筆**、C 檔 **0 筆** — **查無**。

實際拼法（全文搜尋所得，逐字）：

| 佔位字面 | 實際 `SG_` 名 | 備考 |
|---|---|---|
| `$TGW_DISP_STAT$` | **`TGW_DISP_STATSts`** | 另有近名 `TGW_CAMERA_DISP_STAT`（B、C 檔）與 `TGW_FPDM_DISP_STATSts`（A 檔），**非**同一訊號 |
| `$TGW_DISP_STAT$`（上一輪點名之相關訊號） | **`DCSD_DISP_STAT`** | 承載於 `BO_ 1445 DIS_CENTERSTACK`；為 DCSD 側之螢幕狀態，與 `TGW_DISP_STATSts` 為**二個不同訊號** |
| `$Telematic_Power$` | **`PowerSts_Telematic`** | 承載於 `BO_ 1470 STATUS_TELEMATIC` |

`PowerSts_Telematic` 之 `VAL_` 值名含 `Idle` 與 `Full_Operation`，與 b03 之
`pre_conditions` 所書之 `"Full_Operation" state`／`"Idle" state` **逐字相符**，
故本報告以 `PowerSts_Telematic` 為 `$Telematic_Power$` 之對應候選（**只登記，不採認**）。

### §1-1 `TGW_DISP_STATSts`（A 檔）

承載訊息、發送節點（`BO_` 行逐字，L407）：

```
BO_ 1500 TELEMATIC_DISPLAY2: 8 ETM
```

訊號行與收方（`SG_` 行逐字，L408）：

```
 SG_ TGW_DISP_STATSts : 0|4@0+ (1,0) [0|14] "" SGW
```

- 發送節點：`ETM`
- 接收節點（逐字）：`SGW`　—— **`LTM` 不在收方清單內**
- `BO_TX_BU_`（L457，逐字）：

```
BO_TX_BU_ 1500 : ETM,LTM;
```

　即本檔另列 **`LTM` 為 `BO_ 1500` 之追加發送方**（非收方）。

- 註解（L783，逐字）：`CM_ SG_ 1500 TGW_DISP_STATSts "TGW Display status";`
- 值表（L3353，逐字）：

```
VAL_ 1500 TGW_DISP_STATSts 0 "Display_off" 1 "Display_closed" 2 "Normal_mode" 3 "DVD_menu" 4 "DVD_Setup" 5 "DVD_display" 6 "Mode_select_display" 7 "Rear_Camera_Display" 8 "On_blanked_screen" 9 "Splashscreen_Display" 10 "Rear Entertainment HMI" 11 "Rear Entertainment Full Screen Video " 12 "DTV Program Display" 13 "DTV fullscreen Video Display" 14 "DTV Camera Video Display" 15 "SNA";
```

### §1-2 `DCSD_DISP_STAT`（A 檔）

承載訊息、發送節點（L130，逐字）：

```
BO_ 1445 DIS_CENTERSTACK: 8 SGW
```

訊號行與收方（L133，逐字）：

```
 SG_ DCSD_DISP_STAT : 7|3@0+ (1,0) [0|6] "" ETM,LTM
```

- 發送節點：`SGW`（即**由 SGW 轉發**，與上一輪之發現一致）
- 接收節點（逐字）：`ETM,LTM`　—— **`LTM` 明列為收方**
- `BO_TX_BU_ 1445`：**查無**（本檔 14 條 `BO_TX_BU_` 之 message id 為
  1478／899／2654208036／302／303／1282／1283／1284／1285／1470／1500／156／158／1291，不含 1445）
- 註解（L540，逐字）：`CM_ SG_ 1445 DCSD_DISP_STAT "Remote Display Status";`
- 值表（L3126，逐字）：

```
VAL_ 1445 DCSD_DISP_STAT 0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA";
```

### §1-3 `PowerSts_Telematic`（A 檔）

承載訊息、發送節點（L378，逐字）：

```
BO_ 1470 STATUS_TELEMATIC: 8 ETM
```

訊號行與收方（L384，逐字）：

```
 SG_ PowerSts_Telematic : 12|3@0+ (1,0) [0|7] "-" FPDM,SGW
```

- 發送節點：`ETM`
- 接收節點（逐字）：`FPDM,SGW`　—— **`LTM` 不在收方清單內**
- `BO_TX_BU_`（L456，逐字）：

```
BO_TX_BU_ 1470 : ETM,LTM;
```

　即本檔另列 **`LTM` 為 `BO_ 1470` 之追加發送方**（非收方）。

- 值表（L3333，逐字）：

```
VAL_ 1470 PowerSts_Telematic 0 "Sleep" 1 "Standby" 2 "Timed" 3 "Idle" 4 "Full_Operation" 5 "Logistic_On" 6 "Bench" 7 "Partial_Operation";
```

---

## §2 三 DBC 發收方矩陣

格式：**發**＝該檔中該節點列於 `BO_` 行末（發送方）或 `BO_TX_BU_`（追加發送方）；
**收**＝列於 `SG_ ` 行末之收方欄；**未載**＝該檔查無此 `SG_` 名。
每格附該檔之逐字證據行。

### §2-1 `TGW_DISP_STATSts`

| | A｜R1_BHCAN2 | B｜R4_BHCAN | C｜R5_FDCAN8 |
|---|---|---|---|
| 承載訊息 | `BO_ 1500 TELEMATIC_DISPLAY2: 8 ETM` | `BO_ 1500 TELEMATIC_DISPLAY2: 8 SGW` | `BO_ 1427 TELEMATIC_FD_4: 32 ETM` |
| 發送節點 | **發**＝`ETM`（＋`BO_TX_BU_` 之 `ETM,LTM`） | **發**＝`SGW` | **發**＝`ETM`（＋`BO_TX_BU_` 之 `ETM,LTM`） |
| 接收節點 | **收**＝`SGW` | **收**＝`DCSD` | **收**＝`Vector__XXX`（未指派） |
| `LTM` 之角色 | **發**（僅 `BO_TX_BU_`） | **未載**（本檔 `BU_` 無 `LTM`） | **發**（僅 `BO_TX_BU_`） |
| `ICS` 之角色 | **未載**（本檔 `BU_` 無 `ICS`） | 未列於此訊號 | **未載**（本檔 `BU_` 無 `ICS`） |

逐字證據：

- A：`BO_ 1500 TELEMATIC_DISPLAY2: 8 ETM` ／ ` SG_ TGW_DISP_STATSts : 0|4@0+ (1,0) [0|14] "" SGW` ／ `BO_TX_BU_ 1500 : ETM,LTM;`
- B：`BO_ 1500 TELEMATIC_DISPLAY2: 8 SGW` ／ ` SG_ TGW_DISP_STATSts : 0|4@0+ (1,0) [0|14] "" DCSD`（B 檔 `BO_TX_BU_` 全檔 0 條）
- C：`BO_ 1427 TELEMATIC_FD_4: 32 ETM` ／ ` SG_ TGW_DISP_STATSts : 79|4@0+ (1,0) [0|14] "" Vector__XXX` ／ `BO_TX_BU_ 1427 : ETM,LTM;`

### §2-2 `DCSD_DISP_STAT`

| | A｜R1_BHCAN2 | B｜R4_BHCAN | C｜R5_FDCAN8 |
|---|---|---|---|
| 承載訊息 | `BO_ 1445 DIS_CENTERSTACK: 8 SGW` | `BO_ 1445 DIS_CENTERSTACK: 8 DCSD` | **未載** |
| 發送節點 | **發**＝`SGW` | **發**＝`DCSD` | 未載 |
| 接收節點 | **收**＝`ETM,LTM` | **收**＝`SGW` | 未載 |
| `LTM` 之角色 | **收** | **未載** | **未載** |

逐字證據：

- A：`BO_ 1445 DIS_CENTERSTACK: 8 SGW` ／ ` SG_ DCSD_DISP_STAT : 7|3@0+ (1,0) [0|6] "" ETM,LTM`
- B：`BO_ 1445 DIS_CENTERSTACK: 8 DCSD` ／ ` SG_ DCSD_DISP_STAT : 7|3@0+ (1,0) [0|6] "" SGW`
- C：`SG_` 名等於 `DCSD_DISP_STAT` 者 0 筆 — 查無。

### §2-3 `PowerSts_Telematic`

| | A｜R1_BHCAN2 | B｜R4_BHCAN | C｜R5_FDCAN8 |
|---|---|---|---|
| 承載訊息 | `BO_ 1470 STATUS_TELEMATIC: 8 ETM` | `BO_ 1470 STATUS_TELEMATIC: 8 SGW` | `BO_ 1427 TELEMATIC_FD_4: 32 ETM` |
| 發送節點 | **發**＝`ETM`（＋`BO_TX_BU_` 之 `ETM,LTM`） | **發**＝`SGW` | **發**＝`ETM`（＋`BO_TX_BU_` 之 `ETM,LTM`） |
| 接收節點 | **收**＝`FPDM,SGW` | **收**＝`AMP,ANC,DCSD,ICS` | **收**＝`TBM` |
| `LTM` 之角色 | **發**（僅 `BO_TX_BU_`） | **未載** | **發**（僅 `BO_TX_BU_`） |
| `ICS` 之角色 | **未載** | **收** | **未載** |

逐字證據：

- A：`BO_ 1470 STATUS_TELEMATIC: 8 ETM` ／ ` SG_ PowerSts_Telematic : 12|3@0+ (1,0) [0|7] "-" FPDM,SGW` ／ `BO_TX_BU_ 1470 : ETM,LTM;`
- B：`BO_ 1470 STATUS_TELEMATIC: 8 SGW` ／ ` SG_ PowerSts_Telematic : 12|3@0+ (1,0) [0|7] "-" AMP,ANC,DCSD,ICS`
- C：`BO_ 1427 TELEMATIC_FD_4: 32 ETM` ／ ` SG_ PowerSts_Telematic : 103|3@0+ (1,0) [0|7] "-" TBM` ／ `BO_TX_BU_ 1427 : ETM,LTM;`

### §2-4 E21 判定

**E21 未觸發。**

理由（逐訊號檢定）：

1. `TGW_DISP_STATSts`：A 由 `ETM` 發、B 由 `SGW` 發。二者非矛盾，因 A 檔之
   `BU_` 為 `ETM FPDM LTM SGW`（無 `ICS`／`DCSD`）、B 檔之 `BU_` 為
   `AMP ANC BCM … DCSD … ICS SGW …`（無 `ETM`／`LTM`）—— 二檔為**同一 SGW 兩側之兩個網段**。
   A 側收方為 `SGW`、B 側發方即 `SGW`，方向首尾相接，正是「`SGW` 閘道轉發」之形。
2. `DCSD_DISP_STAT`：B 由 `DCSD` 發、收方 `SGW`；A 由 `SGW` 發、收方 `ETM,LTM`。
   同樣首尾相接（`DCSD` → `SGW` → `ETM,LTM`），為閘道轉發可解釋。
3. `PowerSts_Telematic`：A 由 `ETM` 發、收方含 `SGW`；B 由 `SGW` 發、收方含 `ICS`。
   首尾相接，為閘道轉發可解釋。C 檔由 `ETM` 發，與 A 之發方同，無分歧。
4. 三檔中**無任一訊號出現「A 由 X 發、B 由 Y 發，且 X→Y 或 Y→X 之轉發鏈不成立」之情形**。

故未見須停下之互斥；本節不作採認，只記「未觸發」。

---

## §3 是否足以定台架觀察點

**判定：部分。**（不採認、不裁決；僅為量測結論。）

理由：

1. **下放包之問法之前提於此二訊號不成立。** 下放包問「若本 DUT（`LTM`）於 PDT27 dbc
   **明列為收方**」。實測：`TGW_DISP_STATSts` 之收方逐字為 `SGW`、
   `PowerSts_Telematic` 之收方逐字為 `FPDM,SGW` —— **`LTM` 皆不在收方欄**。
   `LTM` 出現之處為 `BO_TX_BU_ 1500 : ETM,LTM;` 與 `BO_TX_BU_ 1470 : ETM,LTM;`，
   即**追加發送方**。就 DR-ICS16 所問之「於哪一條匯流排觀察」而言，
   發送方之身分同樣可定觀察面（DUT 自己送、以 CAN trace 在該匯流排錄），
   故此點對 DR-ICS16 是**正向**的；但它回答的不是下放包所設之「收方」問法。
2. **`DCSD_DISP_STAT` 一項確以收方明列 `LTM`**（` SG_ DCSD_DISP_STAT : … "" ETM,LTM`），
   但該訊號**不是** `$TGW_DISP_STAT$` 之對應訊號，二者為不同 `SG_`、不同 `BO_`。
   以它去填 `$TGW_DISP_STAT$` 屬替換而非查得。
3. **值名對不上。** b03 之 8 條 `test_item` 所書為 `$TGW_DISP_STAT$ = [DISP_OFF]` 與
   `= [DISP_NORMAL]`；A 檔 `VAL_ 1500` 之值名為 `"Display_off"`（0）與
   `"Normal_mode"`（2），**無 `DISP_OFF`／`DISP_NORMAL` 二字面**。
   對應關係看似顯然，但「顯然」不等於「查得」——此為一次取捨，非本層可作。
   相對地 `PowerSts_Telematic` 之 `"Idle"`／`"Full_Operation"` 與 b03 之
   `pre_conditions` 逐字相符，無此問題。
4. **該檔未綁定本 feature、A-DM14 未裁**（下放包明令列入之限制）：
   `forms/FORMS.md` L465–467 之登錄逐字為
   「**使用中之 feature（R-G15 反向記載）**：`display`（R-DM19 選定為其 B-CAN 資料庫）」，
   `features/ics_management/feature.yaml` 之 `reference` 區塊只綁 `dbc_b`（R4_BHCAN）
   與 `dbc_fd`（R5_FDCAN8），**未綁 A 檔**。R4 與 A 之取捨（A-DM14）未裁前，
   採 A 檔之發收方去覆蓋既綁之 R4 等同以未裁之檔推翻已綁之檔。
   本作業亦被明令不得改 `feature.yaml`／`FORMS.md`，故連綁定路徑都未開。
5. **正向的一面（故非「不足」而是「部分」）：** A 檔是三檔中唯一同時滿足下列三者者
   —— (a) `BU_` 含 `LTM`（本 DUT 之節點名）；(b) 二目標訊號皆載；
   (c) ICS 按鍵刺激面同檔可見：`BO_ 1050 CLIMATIC_PANEL: 8 SGW` 之
   ` SG_ Radio_btn0 : 44|1@0+ (1,0) [0|1] "" LTM`（收方**僅** `LTM`）與
   ` SG_ Radio_btn2 : 42|1@0+ (1,0) [0|1] "" ETM,LTM`。
   亦即在同一條匯流排上，**刺激（按鍵）與回應（顯示狀態）對本 DUT 皆可觀察**。
   這是 B、C 二檔做不到的（B 檔 `BU_` 無 `LTM`；C 檔無 `BO_ 1050`）。

綜上：**證據面已足以指出候選觀察點為 A 檔所描述之 BHCAN2 網段**，
但**授權面（綁定與 A-DM14）與值名對應面各缺一步**，故為「部分」。

---

## §4 潛在回收數（只估）

### §4-1 先實數：b03 之佔位實測分布

以 `features/ics_management/generated/b03/b03_tcs.json` 全樹走訪，
正規式 `\$[A-Za-z_0-9]+\$`，逐路徑計數（數字自列舉長度取得）：

| 佔位 | 全檔出現總數 | `tcs[i].test_item` | `tcs[i].reasoning` | 頂層 `reasoning` | `revision[*]` |
|---|---|---|---|---|---|
| `$TGW_DISP_STAT$` | **24** | **8** | 13 | 1 | 2 |
| `$RQ_DISP_INTS$` | 15 | 8 | 5 | 0 | 2 |
| `$Telematic_Power$` | 5 | 1 | 2 | 0 | 0 |

`$Telematic_Power$` 另有 `tcs[i].pre_conditions` **2** 處（`tcs[1]` 與 `tcs[3]` 各 1），
未列於上表之欄別中。其逐路徑為：`tcs[1].pre_conditions` 1、`tcs[3].pre_conditions` 1、
`tcs[3].test_item` 1、`tcs[1].reasoning` 1、`tcs[3].reasoning` 1，合計 5
—— **交付欄合計 3**（`test_item` 1 ＋ `pre_conditions` 2）。
`$TGW_DISP_STAT$` 與 `$RQ_DISP_INTS$` 於 `pre_conditions` 欄皆 **0** 處。

`$TGW_DISP_STAT$` 之逐 TC：`tcs[0]`～`tcs[7]` **每條 `test_item` 各 1 處，合計 8**；
`expected_result` 欄 **0 處**（b05 已將 ER 主錨改為 HMI 現象）。

**「12 處」不可複現** —— 見 §5-1。本節以下之估算同時給出「以 8 為母體」與
「若上游堅持以 12 為母體」二式。

### §4-2 各處回收所需之資訊

以 `tcs[0].test_item` 為例（逐字）：

```
Then the HU shall immediately send $TGW_DISP_STAT$ = [DISP_OFF], and send $RQ_DISP_INTS$ = [0% Intensity]
```

每一處要改寫成具名訊號，需齊備四項：

| # | 所需資訊 | A 檔是否提供 | 缺口 |
|---|---|---|---|
| i | 承載訊息之 `BO_` 編號與名稱 | **提供**：`BO_ 1500 TELEMATIC_DISPLAY2` | 無 |
| ii | 訊號實際拼法 | **提供**：`TGW_DISP_STATSts` | 無 |
| iii | 匯流排／觀察節點面 | **提供**：BHCAN2；`LTM` 為 `BO_TX_BU_ 1500` 之追加發送方 | 「發送方」非下放包所設之「收方」（§3-1） |
| iv | 值名對應（`[DISP_OFF]`／`[DISP_NORMAL]` → 列舉字面） | **部分**：`VAL_ 1500` 有 `"Display_off"`／`"Normal_mode"` | **字面不一致，需一次取捨；非查得** |

`$Telematic_Power$` 之三處交付欄（`pre_conditions` 2、`test_item` 1）四項全齊：
i `BO_ 1470 STATUS_TELEMATIC`、ii `PowerSts_Telematic`、iii BHCAN2、
iv `"Idle"`／`"Full_Operation"` **與 b03 逐字相符**，無取捨缺口。

### §4-3 估值（**以下為估值，非量測值**）

**`$TGW_DISP_STAT$` 之潛在回收數估：上限 8、下限 0，最可能 8。**

- 上限 8：A 檔若獲採認，8 處 `test_item` 之 i／ii／iii 一次補齊，
  8/8＝**100%** 可具名為 `$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$`（BO_ 1500）。
- 下限 0：iv 之值名字面不一致。既有 R-ICS22(a)（不得自選匯流排／不得自行指定畫面名）
  之精神若延伸到值名，則在另一次裁定之前一處都不能改，回收數為 0。
- 最可能 8：iv 之對應在 `VAL_` 中有唯一合理對象（`Display_off`＝唯一 off 態、
  `Normal_mode`＝唯一 normal 態），且 b04 曾以同一形式回收 `$RQ_DISP_INTS$`
  3 處（`revision.b04_applied` 逐字：`作業 B：$RQ_DISP_INTS$ 佔位 3 處 → 0
  （RADIO_B3.RQ_DISP_INTS，BO_ 1283）`），有先例。

**`$Telematic_Power$` 之潛在回收數估：3（交付欄全部）。** 四項全齊、無取捨缺口。

**若上游堅持母體為 12**：則 12 處中可具名者估 12（同一訊息一次補齊，比例不隨母體變），
即「潛在回收 12 → 0」；但本包無法指出那 12 處落在哪些欄位（§5-1）。

**估算之不確定處（逐項）：**

1. 母體本身不確定（8 vs 12），見 §5-1。
2. iv 之值名取捨是否被視為「查得」還是「自選」，本層無權判，二者導出 8 與 0。
3. `reasoning` 欄之 13＋1 處是否算「回收對象」未定 —— 本報告視其為敘述性、不計入交付欄。
4. 若採認同時要求把觀察位置由 `BO_TX_BU_` 之發送方語意改寫成台架步驟，
   則另需一次對「以 CAN trace 錄 DUT 自送訊框」之書寫裁定（R-ICS22(c) 已定
   「一律書為 CAN trace」，故此項風險低，但非零）。
5. `$RQ_DISP_INTS$` 已於 b04 回收為 `BO_ 1283`；A 檔之
   ` SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" SGW`（`BO_ 1283 RADIO_B3: 8 ETM`）
   與該回收一致，故 A 檔之採認**不會**推翻 b04 之回收 —— 但此為附帶觀察，不在本作業之問。

---

## §5 下放包未預料之事

### §5-1 「12 處 `$TGW_DISP_STAT$` 佔位」不可複現

下放包 13（`docs/handoff/13_freeze.md` L108）與其前之 05／06／07／08／09／10／11
各包、以及 `docs/INDEX.md` L145 皆載「12 處」。本包實測 `b03_tcs.json`：

- 全檔 `$TGW_DISP_STAT$` 出現 **24** 次；
- 落在**交付欄**者只有 `tcs[i].test_item`，**8** 次（8 條 TC 每條 1 次）；
- `tcs[i].reasoning` 13 次、頂層 `reasoning` 1 次、`revision.b04_applied[1]` 1 次、
  `revision.b05_applied[2]` 1 次 —— 此四者為敘述文字，非待填欄位；
- `expected_result` 欄 **0** 次。

**8、13、24 三數皆非 12**，且無任何欄位組合得 12。此數自下放包 05 起被逐包轉抄，
其原始量測條件本包查無。**本包不改任何既有檔，故只登記此不一致，不回改任何文件。**

### §5-2 `LTM` 在 A 檔對二目標訊號是「發送方」而非「收方」

下放包 §3 之問法預設「本 DUT（`LTM`）於 PDT27 dbc 明列為收方」。實測相反：
`TGW_DISP_STATSts` 收方 `SGW`、`PowerSts_Telematic` 收方 `FPDM,SGW`，
`LTM` 只在 `BO_TX_BU_ 1500 : ETM,LTM;` 與 `BO_TX_BU_ 1470 : ETM,LTM;` 出現。

這同時與 `docs/upstream/07_unblock_and_recovery.md` L177 之逐字判斷
（「**若 DUT 節點名為 `LTM`，則二 DBC 中根本沒有 `$TGW_DISP_STAT$` 之 DUT 發送側**」）
形成對照：該判斷在**已綁之二 DBC** 中成立（B 檔 `BU_` 無 `LTM`；
C 檔 `TGW_DISP_STATSts` 之 `BO_TX_BU_ 1427 : ETM,LTM;` —— 此處其實**已有** `LTM` 發送側，
見 §5-3），而 A 檔提供了 B-CAN 側之 `LTM` 發送側。

### §5-3 已綁之 C 檔（R5_FDCAN8）本身即載 `BO_TX_BU_ 1427 : ETM,LTM;`

即：**不必採認 A 檔，已綁之 FDCAN8 就已把 `LTM` 列為 `TELEMATIC_FD_4`（載
`TGW_DISP_STATSts` 與 `PowerSts_Telematic` 二者）之追加發送方。**
若 upstream-07 之 E3 判定（「先決不成立」）是以「B、C 二檔無 `LTM` 發送側」為據，
則該據於 C 檔之 `BO_TX_BU_` 面不成立。本包不對此作結論，只登記。

### §5-4 A 檔之 `BU_` 無 `ICS` 節點，但 `BO_ 1050 CLIMATIC_PANEL` 仍在

逐字：`BO_ 1050 CLIMATIC_PANEL: 8 SGW`、` SG_ Radio_btn0 : 44|1@0+ (1,0) [0|1] "" LTM`。
B 檔同訊息為 `BO_ 1050 CLIMATIC_PANEL: 8 ICS`、` SG_ Radio_btn0 : … "" SGW`。
即 ICS 之按鍵訊框由 `SGW` 轉發至 A 檔之網段，收方**僅** `LTM`。
下放包只令量測二個顯示訊號，未預料刺激面同檔可見 —— 這使「同一條匯流排上
刺激與回應皆可觀察」成為可能，是本作業對 DR-ICS16 最強之一項附帶證據。

### §5-5 B 檔（R4_BHCAN）全檔 `BO_TX_BU_` 為 0 條

A 檔 14 條、C 檔 28 條、B 檔 **0** 條。三檔之表達力不對稱：
在 B 檔中「某節點是否為追加發送方」這個問題**無法被回答**（不是答「否」，是無此宣告面）。
§2 矩陣之「未載」在 B 檔一欄須如此讀，不可解為「該檔否認」。

### §5-6 三檔規模差一個量級，A 檔形似 DUT 視角之抽取檔

`BO_` 段數 A 63／B 155／C 323；`BU_` 節點數 A 4／B 17／C 4。
A 檔之 `BU_: ETM FPDM LTM SGW` 恰為「二個 telematic 變體＋前排乘客顯示＋閘道」，
無任何底盤／車身節點。此形制與 B 檔（車身側全節點）性質不同。
本包不推論其產製意圖，只登記形制差異 —— 它會影響 A-DM14 之取捨面。

---

## §6 已知局限

1. **本報告不採認任何證據。** A 檔未綁定 `features/ics_management/feature.yaml`，
   `FORMS.md` 登錄之使用 feature 為 `display`；A-DM14 未裁。
   §1–§2 之一切逐字資料在採認前只是「A 檔如此寫」，不是「本 feature 之事實」。
2. **`$TGW_DISP_STAT$` 與 `TGW_DISP_STATSts` 之等同關係本包未證。**
   本包只證「三檔皆查無名為 `TGW_DISP_STAT` 之 `SG_`」與「`TGW_DISP_STATSts` 為
   最接近之實名」。等同與否須另裁。同理 `$Telematic_Power$` ↔ `PowerSts_Telematic`。
3. **`DCSD_DISP_STAT` 與 `TGW_DISP_STATSts` 為二個不同訊號**，
   上一輪之發現（「`DCSD_DISP_STAT` 之收方明列 `ETM,LTM`」）不能直接充當
   `$TGW_DISP_STAT$` 之收方證據。本報告已分列，未合併。
4. **`BO_TX_BU_` 之語意採 DBC 標準之「追加發送方」讀法。** 若本專案另有把該欄
   讀為「可見節點」之既定慣例，本包查無該慣例之落檔，故未採。此讀法若被推翻，
   §2 矩陣之「`LTM` 之角色」一列與 §3 之判定皆須重算。
5. **§4 為估值。** 母體本身有 8 與 12 之爭（§5-1），值名取捨未裁（§4-2 iv），
   二者相乘使區間為 0～12。
6. **未量測項**：A 檔之 `BA_ "GenSigTimeoutTime_*"`／`Period [ms]` 等時序屬性、
   `BA_ "Description" BU_` 之節點全名、以及 A 檔與 B／C 檔之訊號位元佈局差異
   （實測 `TGW_DISP_STATSts` 起始位元 A/B 為 `0`、C 為 `79`，長度皆 4）之影響，
   下放包未令量測，本包未展開。
7. **本作業全程未執行任何 `git` 指令**（含唯讀）。未改檔之自證以 `shasum -a 256`
   與 `ls -l` 為之：三支 dbc 之 sha256 見 §0，皆與量測前後一致；
   `feature.yaml`、`FORMS.md`、分析層五簿、`b03_tcs.json` 皆只讀未寫。
8. **本包新建之檔共二**：本報告 `docs/reports/13_pdt27_dbc_vs_dr16.md` 與
   量測腳本 `scripts/pdt27_probe_13.py`。無第三個新建檔，無任何既有檔被修改。
