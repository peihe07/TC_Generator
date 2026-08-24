# 下放包 04 —— 參考素材庫建置（`forms/` 內），上繳 03 覆核

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：**全域**（`forms/`、`.gitignore`、全案條文）＋ Display feature
- 對應上繳：`features/display/docs/upstream/04_reference_store.md`
- 前一包：`03_coverage_redo.md`（上繳已覆核，見 §一）

---

## 一、上繳包 03 之覆核

**核可，無退回項。** 品質較 02 提升一級，三處具名：

1. **自行檢出分析層之定義缺陷。** 下放包 03 §3.3 記「`[VALUE]` 相異 9 個」，
   執行層以寬式 regex 得 13 個，並指出差異中之 `[0% Intensity]` 出現
   **20 次**，多於 `[DISP_OFF]` 之 15 次，且為 `$RQ_DISP_INTS$` 之值 ——
   屬 R-DM14 之值域來源，卻被「僅大寫」之定義整個丟棄。兩種定義之數字
   皆列出，未擇一。**處置正確。** 裁定見 §四 R-DM16。
2. **拒絕把方法界線報成發現。** `SWE-DM-007`／`008` 候選 0 之原因為
   `RVC` → `Rear View Camera` 之展開非逐字，非「SYS2 無 RVC 需求」。
   §4.4 明寫「兩者若混同，就是把上一輪的錯誤換個方向再犯一次」。
3. **自陳現行方法對 60% 母體無效。** heading 錨在 r72 底下掛 48 個 FR，
   而該 heading 講的是序列器觸控中斷接腳定義。並據此主張 Q2 不得提交
   裁定 —— **此判斷採認**，Q2 維持暫緩。

`A-DM12` 之 B10 快取陳舊值（D10 為空而快取仍存 `1`）為下放包未要求而
自行發現者，且指出「以 `data_only=True` 讀 B 欄判該列是否已填之實作會
誤判 r10」。記明。

`DR-DM4`（CFTS_013）、`A-DM13`（CFTS_020 外指 8 份外部 CFTS，
`CFTS019-723` 被引 12 次而完全未查）採認。

---

## 二、素材已就位 —— Pei 2026-08-24 置於 `forms/`

分析層實測 `forms/` 現況：

| 檔 | 角色 |
|---|---|
| `FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx` | 036 母本（R-G1，既有） |
| `FORMS.md` | manifest（既有） |
| **`PDT27_E2A_R1_BHCAN2.dbc`** | 新置 |
| **`PDT27_E2A_R1_FDCAN8.dbc`** | 新置 |
| **`PROXI_HDCC27_R3_20250424.xlsx`** | 新置 |
| **`Logical Identifiers and CAN Mapping v1_78.xlsx`** | 新置 |

Pei 之指示為「放 `forms/` 裡面」，故**不另立 `reference/`**（下放包 03
之後的口頭提案作廢）。`forms/*` 已被 `.gitignore` 排除、`FORMS.md` 已
tracked，形狀正確，**不需改 `.gitignore`**。

「BHCAN 改成 BHCAN2」之意義已實測釐清，見 §三。

---

## 三、分析層實測（對照向，執行層須獨立重算）

量測條件：DBC 以 `grep`／`awk` 對純文字逐行比對（`^ SG_` 判訊號定義列、
`^BO_ ` 判訊息列）；LID 以 `openpyxl`、`read_only=True`、`data_only=True`；
標的為 `forms/` 之複本經 `copy_file_user_to_claude` 取得者，**無雜湊保證**，
執行層之重算為取代而非複驗。

### 3.1 BHCAN2 不是 BHCAN 之新版 —— 是不同的資料庫

| 檔 | 訊號定義列 | 訊息 | bytes |
|---|---|---|---|
| `PDT27_E2A_R1_BHCAN2.dbc` | **344** | 63 | 167,226 |
| `PDT27_E2A_R1_FDCAN8.dbc` | 1,916 | 318 | 1,106,532 |
| `PDT27_E2A_R4_BHCAN.dbc`（vehicle_setting） | 914 | 155 | 442,200 |
| `PDT27_E2A_R5_FDCAN8.dbc`（vehicle_setting） | 2,037 | 323 | 1,177,931 |

BHCAN2-R1 與 BHCAN-R4 之訊號名集合比對（相異名，逐字）：

| | 數 |
|---|---|
| 兩者皆有 | **310** |
| 僅 BHCAN-R4 有 | **573** |
| 僅 BHCAN2-R1 有 | **32** |

**故「BHCAN2 取代 BHCAN」不是換版次，是換資料庫。** 573 個只在舊檔中
存在之訊號名，其在新架構下之地位（移除／改名／移至他匯流排）本包
不推定。

僅 BHCAN2 有者含四個與本 feature 直接相關之訊號：

```
FPDM_DISP_STAT          BO_ 1513 FPDM1      VAL_ 0 OFF 1 ON 2 BLANK 3 DISP_HOT 7 SNA
TGW_FPDM_DISP_STATSts   BO_ 1282 RADIO_B2   VAL_ 0 OFF 1 ON 2 BLANK 3 DISP_HOT 7 SNA
FPDM_RQ_DISP_INTS       BO_ 1282 RADIO_B2   8 bit, 0.5 %/bit, 0–100, 255 SNA
CameraDisplaySts        BO_ 1283 RADIO_B3   VAL_ 0 Default 1 View_1 … 7 View_7
```

`FPDM_*` 為 `DCSD_*` 之平行族（同樣的 OFF/ON/BLANK/DISP_HOT 值域）。
**037 與 SYS2 皆未提及 FPDM。** 這是新素材帶進來的問題，不是既有缺漏。

### 3.2 三個顯示訊號在兩本 BHCAN 中定義相同，但**發送節點不同**

| 訊號 | 訊息 | BHCAN2-R1 發送節點 | BHCAN-R4 發送節點 |
|---|---|---|---|
| `DCSD_DISP_STAT` | `BO_ 1445 DIS_CENTERSTACK` | **SGW** | **DCSD** |
| `RQ_DISP_INTS` | `BO_ 1283 RADIO_B3` | **ETM** | **SGW** |
| `TGW_DISP_STATSts` | `BO_ 1500 TELEMATIC_DISPLAY2` | **ETM** | **SGW** |

VAL_ 列與位元定義兩本逐字相同（`DCSD_DISP_STAT`：
`0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA"`；
`RQ_DISP_INTS`：`55|8@0+ (0.5,0) [0|100] "%"`）。

**發送節點決定 TC 該寫「送出」還是「觀察」**，故此差異非中繼資料。

### 3.3 `CM_TCH_STAT` 在 BHCAN2 中不存在 —— 但不是缺漏

`CM_TCH_STAT` 於 BHCAN-R4、FDCAN8-R1、FDCAN8-R5 皆有，BHCAN2-R1 為 0。
LID 表載其為 `TELEMATIC_FD_5.CM_TCH_STAT`，`CAN` 欄為 `FD` ——
**它本來就在 FD-CAN 上，不在 B-CAN 上。** BHCAN2 查無屬正常，
不得登記為缺漏。

### 3.4 LID v1.78 是缺失的那座橋 —— A-DM10 之訊號側已關閉

`Logical Identifiers and CAN Mapping v1_78.xlsx`，分頁 `CAN Mapping`，
r2 為架構分組列、r3 為欄名列、資料自 r4 起共 **2,624** 列。
架構欄組七個：`LID Information`(1)／`Powernet`(6)／`CUSW`(11)／
`Atlantis`(16)／`Compact`(21)/**`Atlantis High`(26)**／`Comments`(31)。

依 R-VS67 之既有裁定（訊號名取 LID 之 Atlantis High 欄組），實測
SYS2 之 15 個 `$Signal$` **全數解得**：

| SYS2 `$Signal$` | LID 列 | Atlantis High `MESSAGE.Signal` | CAN |
|---|---|---|---|
| `TGW_DISP_STAT` | 2084 | `TELEMATIC_DISPLAY2.TGW_DISP_STATSts`／`TELEMATIC_FD_4.TGW_DISP_STATSts` | CAN-B／CAN-FD |
| `DCSD_DISP_STAT` | 420 | `DIS_CENTERSTACK.DCSD_DISP_STAT` | B-CAN |
| `RQ_DISP_INTS` | **1626** | `RADIO_B3.RQ_DISP_INTS` | B-CAN |
| `CCDMF_RQ_DISP_INTS` | 255 | `RADIO_B4.CCDMF_RQ_DISP_INTS` | CAN-B |
| `CM_TCH_STAT` | 368 | `TELEMATIC_FD_5.CM_TCH_STAT` | FD |
| `ICSPowerButton` | 1039 | `CLIMATIC_PANEL.Radio_btn0`／`DIS_CENTERSTACK.DCSD_Power` | CAN-B |
| `ICSMuteButton` | 1038 | `CLIMATIC_PANEL.Radio_btn4`／`GW_B_5.Mute_Button`／`DIS_CENTERSTACK.DCSD_Mute` | CAN-B |
| `ICSScreenOffButton` | 1044 | `CLIMATIC_PANEL.Radio_btn2`／`DIS_CENTERSTACK.DCSD_Screen_Off` | CAN-B |
| `ICS_KNOB1_DIR` | 1024 | `CLIMATIC_PANEL.Radio_Knob1_DIR`／`DIS_CENTERSTACK.DCSD_VOLKNOB_DIR` | CAN-B |
| `ICS_KNOB1_VAL` | 1025 | `CLIMATIC_PANEL.Radio_Knob1_VAL`／`DIS_CENTERSTACK.DCSD_VOLKNOB_VAL` | CAN-B |
| `ICS_KNOB2_DIR`／`ICS_KNOB2_VAL` | 1026／1027 | （同族，須逐列讀出） | CAN-B |
| `Enter_Button` | 666 | `CLIMATIC_PANEL.Radio_btn1`／`DIS_CENTERSTACK.DCSD_Enter` | CAN-B |
| `Back_Button` | 131 | `CLIMATIC_PANEL.Radio_btn3` | CAN-B |
| `Telematic_Power` | 2069 | `TELEMATIC_FD_4.PowerSts_Telematic`／`STATUS_TELEMATIC.PowerSts_Telematic` | CAN_FD／CAN-BH |

**三項後果，逐項改寫既有結論：**

1. **`TGW_DISP_STAT` → `TGW_DISP_STATSts` 之 `Sts` 尾綴不是規格錯誤。**
   LID 之左欄是 Logical Identifier，右欄才是 CAN 訊號名，兩者本就不同名。
   分析層前一輪把它讀成 R-13/(g)「規格訊號名 DBC 查無」之情形，**該讀法
   撤回**。R-13 之適用前提是「查遍應查之處仍無對應」，而 LID 就是應查
   之處。
2. **`ICS*` 系列在兩本 DBC 皆 0 命中，亦非缺漏。** 其 CAN 訊號名為
   `Radio_btn0`／`DCSD_Power` 等，以 LID 名去 DBC 查必然 0。
   **這正是「查無是查了哪幾個檔的屬性」之延伸：也是「用什麼名字查」
   的屬性。**
3. **A-DM10 須拆為兩半。** 訊號側之 id 橋樑已由 LID 建立，**關閉**；
   章節側（SWE-DM leaf → CFTS 條號）之橋樑仍不存在，**維持 PENDING**。

### 3.5 LID 版本：v1.78 vs v1.76

`features/vehicle_setting/inputs/` 之 LID 為 **v1_76**，`forms/` 新置者為
**v1_78**。兩者差異本包未測。vehicle_setting 之已交付件依既有慣例不因
新版而改（同 R-G1 之「新版不回頭修已交出去的檔」）。

---

## 四、裁決條文（抄入 `docs/fw036/RULINGS_LEDGER.md` 之全域段；
`R-DM16` 另抄入 `features/display/RULINGS.md`）

```
R-G12（參考素材庫之位置與 manifest —— 全域）
DBC、PROXI 表、LID 對照表一律置於 `forms/`，與 036 母本同目錄。
不另立 `reference/` 目錄（Pei 2026-08-24 裁定）。

`forms/*` 已由根 `.gitignore` 排除、`FORMS.md` 已 tracked，
形狀無須變更：檔案不入 git，manifest 入 git。

`FORMS.md` 新增一節 `## 參考資料庫（DBC / PROXI / LID）`，每檔一條目，
必填欄位六項：

  (a) 檔名、SHA256、bytes、mtime
  (b) **涵蓋範圍** —— DBC 記其匯流排與訊號定義列數、訊息數；
      LID 記其分頁、資料列數、架構欄組清單；PROXI 記其分頁與參數列數
  (c) 版次與其來源（檔名所載，非推定）
  (d) 已知不涵蓋者（如 BHCAN2 不含 FD-CAN 上之訊號）
  (e) 取代關係（本檔取代誰、被誰取代、或並存）
  (f) 首個採用之 feature 與日期

(b) 為必填之理由見 R-G13：無涵蓋範圍之登錄，「查無」不構成發現。
```

```
R-G13（查無之成立要件 —— 全域）
「某訊號／參數查無」之陳述，僅在同時載明下列三項時成立：

  (1) 查了哪些檔（檔名 + SHA256）
  (2) 用什麼名字查（LID 名？CAN 訊號名？規格原文名？）
  (3) 該檔之涵蓋範圍是否本應包含之（匯流排、架構、版次）

三項缺一，該陳述一律記為「未查得」而非「查無」，且不得據以開 DR。

實例（2026-08-24，Display）：分析層先以 `PDT27_E2A_R5_FDCAN8.dbc` 查
`DCSD_DISP_STAT` 得 0，若逕報查無即為誤 —— 該訊號在 B-CAN 上，
FD-CAN 之 DBC 本就不含之。同日又以 LID 名 `ICSPowerButton` 查 DBC 得 0，
亦為誤 —— 其 CAN 訊號名為 `Radio_btn0`／`DCSD_Power`。
```

```
R-G14（查無台帳 —— 全域）
`forms/LOOKUP_MISSES.md`（tracked）為全案唯一之查無台帳。
凡經 R-G13 三要件仍查無者，登記一列，欄位：

  query | 查詢用之名稱種類 | 查了哪些檔(含SHA256前16碼) | 涵蓋範圍是否應含
  | 結果 | 發現之feature | DR編號 | 狀態

目的為避免同一個 miss 被各 feature 重複發現、重複向上游提問。
新 feature 開案時須先讀本檔。

登記之同時，仍須於該 feature 之 `ANOMALIES.md` 登 anomaly、
`DATA_REQUESTS.md` 開 DR —— 三處各有其職，不互相取代：
台帳防重複發現，anomaly 綁該 feature 之批次，DR 綁上游提問。
```

```
R-DM16（`[VALUE]` token 之定義 —— Display）
SYS2 之 `[VALUE]` token 一律以寬式定義擷取：`\[([^\]]+)\]`，
不限大寫。實測相異 13 個。

下放包 03 §3.3 所載之「相異 9 個」係以 `\[([A-Z0-9_]+)\]` 取得，
該定義丟棄了 `[0% Intensity]`（出現 20 次，為 FR 母體中最頻繁之值
token）、`[pressed]`、`[Idle]`、`[DCSD_and_HU_LVDS_Backchannel_Protocol]`。
**「9」之數字撤回**，R-DM14 所引之 9 一併改為 13。

理由：`[0% Intensity]` 是 `$RQ_DISP_INTS$` 之值（LID 1626 →
`RADIO_B3.RQ_DISP_INTS`，8 bit、0.5 %/bit、0–100、255 = SNA），
正是 R-DM14 所定之值域來源。以大小寫為過濾條件會依書寫習慣而非
語意切分資料。
```

```
R-DM17（訊號名之解析鏈 —— Display，取代 R-DM14 之單段表述）
SYS2 之 `$Signal$` 為 Logical Identifier，非 CAN 訊號名。解析為三段：

  SYS2 `$Signal$`
    → LID `CAN Mapping` 分頁之 `Logical Identifier` 欄逐字比對
    → 該列 `Atlantis High` 欄組之 `Signal Name`（形如 `MESSAGE.Signal`）
    → DBC 之 `SG_` 定義與 `VAL_` 列舉

架構欄組固定取 **Atlantis High**（沿用 R-VS67）。
LID 一列可載多個 `MESSAGE.Signal`（以換行分隔，對應不同匯流排或
不同硬體變體），**不得任取其一**；須依該列之 `CAN` 欄與本專案之
匯流排配置擇定，擇定依據逐筆記錄。

R-DM14 之「SYS2 為訊號值域之第一來源」不變，但其表述之
「037 → SYS2 → DBC 兩段」修正為本條之三段。
分析層 2026-08-24 誤將 `TGW_DISP_STAT` → `TGW_DISP_STATSts` 之差異
讀為 R-13/(g)「規格名 DBC 查無」，該讀法撤回：LID 為應查之處，
查了就有。
```

---

## 五、作業步驟

1. 抄錄 §四五條入指定檔，附逐條核對表。
   `R-G12`／`R-G13`／`R-G14` 入 `docs/fw036/RULINGS_LEDGER.md`；
   `R-DM16`／`R-DM17` 入 `features/display/RULINGS.md`。
2. **`forms/` 四個新檔之台帳**：逐檔 SHA256、bytes、mtime，
   依 R-G12 六項必填欄位寫入 `FORMS.md` 之新節。
   涵蓋範圍(b) 須自行實測，不得抄本包 §3.1 之數字。
3. **建 `forms/LOOKUP_MISSES.md`**，依 R-G14 之欄位建表頭。
   本輪之首批登記見步驟 6。
4. **獨立重算 §3.1／§3.2**：四本 DBC 之訊號定義列數與訊息數；
   BHCAN2 vs BHCAN-R4 之訊號名集合三分（皆有／僅舊／僅新）；
   三個顯示訊號之訊息 id、位元定義、VAL_ 列、**發送節點**。
   量測條件自行宣告（如何判 `SG_` 定義列、是否含 `\r`）。
5. **獨立重算 §3.4**：以 LID `CAN Mapping` 之 `Atlantis High` 欄組解析
   SYS2 之 15 個 `$Signal$`，輸出
   `features/display/data/signal_resolution.tsv`，欄位：
   `sys2_signal | lid_row | atl_high_signal_name | can | format | sna |
   dbc_file | dbc_msg_id | dbc_val_labels | resolved(Y/N) | note`
   多值列（一 LID 對多 `MESSAGE.Signal`）**逐值一列**，不合併、不擇一；
   擇定留待 Phase 2。
6. **首批 `LOOKUP_MISSES.md` 登記**：步驟 5 中 `resolved = N` 者，
   逐筆依 R-G13 三要件登記。若全數 resolved，登記「本輪無 miss」一列
   並註明查詢範圍，**不留空表**。
7. **`A-DM10` 拆條**：訊號側依 §3.4 標 RESOLVED 並記其依據；
   章節側（leaf → CFTS 條號）維持 PENDING，另編 `A-DM10b` 或於原條
   分段記載，擇一並說明。**原文依 R-TM13 保留，不刪除。**
8. **`A-DM14` 新增**：BHCAN2 與 BHCAN-R4 為不同資料庫（573 個訊號名
   僅存於舊檔），且三個顯示訊號之發送節點不同。附證據，**不裁定**
   何者適用於本專案。
9. **`A-DM15` 新增**：BHCAN2 含 `FPDM_DISP_STAT`／`TGW_FPDM_DISP_STATSts`／
   `FPDM_RQ_DISP_INTS`／`CameraDisplaySts` 四個顯示相關訊號，
   而 037 與 SYS2 皆未提及 FPDM。附證據，**不推定其是否在範圍內**。
10. 依 R-DM16 以寬式 regex 重出 `[VALUE]` token 清單，更新
    `coverage_sys2_vs_swe_dm.tsv` 之 `values` 欄與其統計；
    `ANOMALIES.md` A-DM11 之「相異值 token」數字一併更正。
11. **PROXI 表本輪只登台帳，不解析。** 其與本 feature 之關聯尚未確立
    （037 與 SYS2 皆未提及 PROXI 參數），逕行解析屬無據之工。
    若步驟 5 之過程中發現 LID `Proxi & Configuration` 分頁與本 feature
    之訊號有關聯，登記後停手詢問。
12. 更新 `docs/INDEX.md`。

---

## 六、停止條件

沿用下放包 01 §五九條 ＋ 03 §七第 10 條，另加：

11. 任一「查無」之陳述無法同時滿足 R-G13 三要件 → 不得寫入任何產出，
    停並回報。
12. 步驟 5 需要以相似度、模糊比對或人為推定才能把某個 `$Signal$` 接到
    LID 之某列 → 該筆標 `resolved = N`，**不得猜**；連續 3 筆以上如此
    則停並回報。
13. 需要修改 `forms/` 內任何檔案之內容 → 停。台帳只讀不寫，
    `FORMS.md` 與 `LOOKUP_MISSES.md` 除外。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/04_reference_store.md`）

1. §四五條之抄錄核對表
2. `FORMS.md` 新節全文（四檔 × 六項必填欄位）
3. `LOOKUP_MISSES.md` 全文
4. 步驟 4 之獨立重算，含量測條件自行宣告
5. `signal_resolution.tsv` 全文與其 resolved 比率
6. `A-DM10` 拆條後全文、`A-DM14`／`A-DM15` 新增全文
7. A-DM11 之 `[VALUE]` 數字更正
8. **「本包是否仍有該驗而未驗者」之獨立判斷**
9. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-G12 | 參考素材庫置於 `forms/`；manifest 六項必填欄位 | 全域 | 是 |
| R-G13 | 查無之成立三要件 | 全域 | 是 |
| R-G14 | `forms/LOOKUP_MISSES.md` 查無台帳 | 全域 | 是 |
| R-DM16 | `[VALUE]` 寬式定義；「9」撤回改 13 | Display | 是 |
| R-DM17 | 訊號名三段解析鏈；R-13/(g) 誤讀撤回 | Display | 是 |

五條皆為獨立單一事項。
