# 下放包 05 —— `[VALUE]` 定義裁定、PROXI 開工、DBC 適用性

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display ＋ 全域一條
- 對應上繳：`features/display/docs/upstream/05_proxi_and_values.md`
- 前一包：`04_reference_store.md`（上繳已覆核，見 §一）

---

## 一、上繳包 04 之覆核

**核可，無退回項。** 四項具名：

### 1.1 `.gitignore` 之更動 —— 追認，且我的原判為誤

下放包 04 §2 寫「不需改 `.gitignore`」。**該句錯了。** 我同一份包裡以
R-G14 規定 `forms/LOOKUP_MISSES.md` 須 tracked，而 `forms/*` 會排除它 ——
兩者不相容，我沒察覺。執行層加否定行並逐檔複驗（台帳不再被忽略、
三份資料檔仍被忽略），處置正確。

### 1.2 §5.3 之自我更正 —— 這是本輪最重要的一筆

首版腳本以字典序取「首個含該訊號名之 DBC」，把
`TELEMATIC_FD_4.TGW_DISP_STATSts` 接到 BHCAN2 之 `TELEMATIC_DISPLAY2`
（訊號名對、訊息名不對），`Telematic_Power` 同樣。改為「兩半皆相等優先」
後修正。

執行層之評語逐字採認並升為通則（見 §四 R-G15 之理由段）：

> 這個缺陷若沒抓到，輸出仍會是 `resolved = Y` 且看起來合理 —— 錯的是
> 匯流排，而匯流排決定 TC 在哪裡量。**看起來成功的輸出最需要對照其定義。**

### 1.3 「全數解得」之限定 —— 我的陳述須加註，採認其更正

下放包 04 §3.4 記「15 個 `$Signal$` 全數解得」。執行層指出該陳述止於
LID 階段成立（15/15），止於 DBC 階段為 14/15 ——
`CCDMF_RQ_DISP_INTS` → `RADIO_B4.CCDMF_RQ_DISP_INTS` 在兩本 DBC 皆無，
而訊息 `RADIO_B4` 本身存在於 BHCAN2-R1，故為 R-G13 三要件齊備之真查無。

**R-DM17 之三段鏈，「解得」一詞此後一律須指明止於哪一段。** 見 §四 R-DM21。

`LOOKUP_MISSES.md` 之 M-1／M-2 兩筆登記，三要件逐項齊備，
特別是第 (3) 項以「訊息本身存在於該 DBC」為據 —— 這正是 R-G13 要的東西。

### 1.4 rx 節點之補測

下放包 §3.2 只列 tx。執行層補測 rx 並發現其隨 tx 一致地對調
（`DCSD_DISP_STAT` BHCAN2 tx=SGW/rx=ETM,LTM；BHCAN-R4 tx=DCSD/rx=SGW）。
**rx 決定在哪個節點觀察**，與 tx 同等重要。本輪之下放包未要求而自行補測，
記明。

`A-DM10` 採「原條分段記載」之拆法及其理由（a 與 b 之證據互相引用）成立。

---

## 二、`[VALUE]` 定義之裁定 —— R-DM16 撤回改寫

### 2.1 執行層指出之矛盾成立

R-DM16 指定 `\[([^\]]+)\]` 卻記「13 個」，兩者不相容。**這是我的錯**：
我把上繳 03 所量之 13（`[A-Za-z0-9_%\s]+` 之產物）當成寬式之產物寫進條文。
執行層依條文之 regex 產出 44 並保留 13 於 `values_narrow`，未擅自擇一 ——
**處置正確**，這是「不以自己的量測覆蓋條文字面」之正確示範。

### 2.2 兩個定義都不對，真正的判準是冒號

分析層實測（`openpyxl`、`data_only=True`、唯讀；母體為 SYS2 `Basic
Report` 之 `Category` 正規化 = `functional requirement` 之 80 列；
regex `\[([^\]]+)\]` 對 `Description` 欄）：

| 項 | 值 |
|---|---|
| 寬式相異 token | **59** |
| 其中含 `:` 者 | **43** |
| 不含 `:` 者 | **16** |
| 至少含一個「不含 `:`」token 之 FR 列 | **35** |

**含 `:` 者全部是 Polarion 匯出之 metadata**：`[Artifact Type:…]`、
`[State:Approved]`、`[Market:All]`、`[Radio:R1H]`、
`[EE Architecture:Atlantis High, PowerNet]` 等。**不含 `:` 者全部是
規格自身之值 token 或文件名。** 冒號是逐字可測之判準，不是相似度。

不含 `:` 之 16 個，逐字全列（含次數）：

```
  20  0% Intensity
  15  DISP_OFF
  12  DISP_NORMAL
   8  current non-zero value
   5  DISP_REAR_CAMERA
   4  DISP_HOT
   4  pressed
   1  DISP_ON
   1  Idle
   1  OFF
   1  ON_BLANK
   1  RR_CMRA
   1  SNA
   1  DCSD_and_HU_LVDS_Backchannel_Protocol
   1  DCSD* and HU CAN and LVDS Backchannel Message Sequence Charts
   1  SD.xxxxx DCSD LVDS VIDEO COMMUNICATION INTERFACE
```

末三者為文件／協定名而非值，須另標；其餘 13 個為值 token。

**`[current non-zero value]` 出現 8 次，三種舊定義全部丟棄。**
它是 `$RQ_DISP_INTS$` 之值，且其本身就是規格保留之模糊寫法 ——
canon §8.4.1 之「來源模糊即保留模糊」正是指這種東西。丟掉它，
TC 寫到該處時就會有人去填一個具體數字。

### 2.3 一處待調和：59 vs 44

分析層量得寬式相異 59，執行層量得 44。**兩者必有一方之切分條件不同**
（推測與換行、`_x000D_`、或跨儲存格合併有關，但這是推測，不是結論）。
執行層須於下一輪調和此差，並以調和後之數字為準。

---

## 三、BHCAN2 之適用性 —— 已有 Pei 之指示，但須明記其承載

執行層 §8 第 2 項之陳述必須被正視：

> 在這件事定案前，`signal_resolution.tsv` 的每一列都掛在 BHCAN2-R1
> 這個未經確認的前提上。

Pei 2026-08-24 之指示為「BHCAN 改成 BHCAN2」，並親自將
`PDT27_E2A_R1_BHCAN2.dbc` 置入 `forms/`。**該指示即為選定**，
不是待決事項。惟其承載範圍須寫明，故立 R-DM19（[PROPOSED]，見 §四）。

**同時記明其代價**：BHCAN-R4 有 573 個訊號名不在 BHCAN2 中。
本 feature 之 15 個 `$Signal$` 未受影響（24/26 解得），但
**其他 feature（vehicle_setting、power、power_moding）若改用 BHCAN2，
須逐一複驗其既有訊號** —— 這不在本 feature 之範圍，僅登記於全域台帳。

---

## 四、裁決條文

```
R-DM18（`[VALUE]` token 之擷取 —— 取代 R-DM16）
R-DM16 廢止。其 regex 與其所載之數字不相容（條文指定
`\[([^\]]+)\]` 而記「相異 13 個」），致誤原因為分析層將上繳包 03 以
`\[([A-Za-z0-9_%\s]+)\]` 量得之 13 誤植為寬式之產物。

現行判準：以 `\[([^\]]+)\]` 擷取後，**排除 token 中含 `:` 者**。
冒號為 Polarion 匯出 metadata 之逐字標記（`[Artifact Type:…]`／
`[State:…]`／`[Market:…]`／`[Radio:…]`／`[EE Architecture:…]`），
非規格值。此判準為逐字比對，不涉相似度。

分析層 2026-08-24 實測（母體 80 列 FR，`Description` 欄）：
寬式相異 59、含 `:` 43、不含 `:` **16**、至少含一個不含 `:` token
之 FR 列 **35**。執行層須先調和其 44 與本處之 59 之切分差異，
以調和後之數字為準。

不含 `:` 之 16 個中，`DCSD_and_HU_LVDS_Backchannel_Protocol`、
`DCSD* and HU CAN and LVDS Backchannel Message Sequence Charts`、
`SD.xxxxx DCSD LVDS VIDEO COMMUNICATION INTERFACE` 三者為文件／協定名，
於輸出中另標 `kind=document`，不計入值域。其餘 13 個為值 token。

`[current non-zero value]`（8 次）必須保留：它是 `$RQ_DISP_INTS$` 之值，
且其模糊性為規格自身所有。依 canon §8.4.1，來源模糊即保留模糊；
丟棄它會使 TC 撰寫時被迫填入一個來源未載之具體數值。
```

```
R-DM19（B-CAN 資料庫之選定）[PROPOSED]
本 feature 之 B-CAN 資料庫為 `forms/PDT27_E2A_R1_BHCAN2.dbc`
（SHA256 `46cb73f3db62ac9f…`）。依據：Pei 2026-08-24 之指示
「BHCAN 改成 BHCAN2」並親自置檔。

FD-CAN 資料庫為 `forms/PDT27_E2A_R1_FDCAN8.dbc`
（SHA256 `2a86c4bf3e670d71…`）。

承載範圍（本條若有誤，下列全部須重做）：
  - `features/display/data/signal_resolution.tsv` 之 26 列
  - `forms/LOOKUP_MISSES.md` 之 M-1／M-2 兩筆查無
  - 此後所有 Display TC 之訊號名、訊息、raw 值、VAL_ 標籤、
    收發節點

`features/vehicle_setting/inputs/` 之 `PDT27_E2A_R4_BHCAN.dbc` 與
`PDT27_E2A_R5_FDCAN8.dbc` **不因本條而作廢**；vehicle_setting 之
已交付件依既有慣例不回頭改（同 R-G1）。

BHCAN-R4 有 573 個訊號名不在 BHCAN2 中（A-DM14）。其他 feature 若
改用 BHCAN2，須逐一複驗既有訊號 —— 不在本 feature 範圍，登記於
`forms/LOOKUP_MISSES.md` 之備註區。
```

```
R-DM20（PROXI 之開工 —— 步驟 11 之觸發放寬）
下放包 04 步驟 11 之停手觸發原為「LID `Proxi & Configuration` 分頁與
本 feature 之**訊號**有關聯」。該條件過窄：PROXI 參數本就不是訊號，
以訊號為觸發等於永不觸發。

放寬為：**與任一 leaf 之前置條件、可用性條件、或配備有無相關者**。
A-DM16 所列之 `DCSD_cfg`（DCSD Present）、`DSP_SK_PRSNT`（Display off
soft key present）、`RVC_SK_PRSNT`（Rear Camera soft key present）
三者已滿足此條件，故 PROXI 解析自本輪起為 in scope。

值域仍依 R-VS49 之既有裁定：PROXI 表本身為該參數值域之權威。
`forms/PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁（1,060 列）
為主表。

**本條只開放解析，不授權將任何 PROXI 參數寫入 TC 之 Pre-Condition。**
何者進入 Pre-Condition 屬 §8.5 之範疇（須為規格明載之觸發條件，
非隱含環境穩定前提），於 Phase 2 逐 leaf 判定。
```

```
R-DM21（「解得」須指明止於哪一段）
R-DM17 之解析鏈為三段（SYS2 `$Signal$` → LID → DBC）。任何「解得」
「查得」「resolved」之陳述，一律須指明其止於哪一段，並分別給數。

實例（2026-08-24）：下放包 04 §3.4 記「15 個 `$Signal$` 全數解得」，
該陳述止於 LID 成立（15/15），止於 DBC 不成立（14/15）。
單寫「全數解得」會使讀者以為 TC 可用之 CAN 名已備齊。

本條同理適用於 CFTS 條號之解析（A-DM10b）與任何多段查找。
```

```
R-G15（參考資料庫之版本綁定 —— 全域）
每個 feature 之 `feature.yaml` 須新增 `reference:` 節，逐項記載其
所用之參考資料庫檔名與 SHA256：

  reference:
    dbc_b:   { file: ..., sha256: ... }
    dbc_fd:  { file: ..., sha256: ... }
    lid:     { file: ..., sha256: ... }
    proxi:   { file: ..., sha256: ... }

理由：`features/vehicle_setting/` 使用 LID v1_76，`features/display/`
使用 v1_78，而**沒有任何條文在追這件事**（執行層上繳 04 §8 第 4 項
指出）。兩版若對同一 Logical Identifier 給出不同之 CAN 訊號名，
跨 feature 之一致性即斷裂，且斷得無聲無息 ——
「看起來成功的輸出最需要對照其定義」（上繳 04 §5.3）。

`forms/FORMS.md` 之各條目須反向記載「哪些 feature 使用本檔」。
版本差異之實測不在本條範圍；本條只要求**綁定可見**。
```

---

## 五、作業步驟

1. 抄錄 §四五條入指定檔（`R-G15` 入
   `docs/fw036/RULINGS_LEDGER.md`；其餘四條入
   `features/display/RULINGS.md`），附逐條核對表。
   R-DM16 依 R-TM13 原文保留、加註廢止。
2. **調和 59 vs 44**（R-DM18 末段）：說明兩次量測之切分條件差異何在
   （換行、`_x000D_`、儲存格合併、或其他），給出調和後之數字。
3. 依 R-DM18 重出 `[VALUE]` 擷取：`values` 欄改為「寬式扣除含 `:` 者」，
   文件／協定名三者標 `kind=document`。`values_narrow` 欄**保留**
   （R-TM13），並於欄名旁註其定義已廢止。更新 A-DM11 之數字。
4. 依 R-DM19 於 `feature.yaml` 新增 `reference:` 節（R-G15），
   四項逐項填 SHA256。`FORMS.md` 各條目反向記載使用者為 `display`。
5. **PROXI 解析（R-DM20）** —— 本輪之主要工作：
   - `forms/PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁（1,060 列）
     結構實測：表頭列、欄名、參數列數、值域欄之形態
   - 以 A-DM16 之三個參數（`DCSD_cfg`／`DSP_SK_PRSNT`／`RVC_SK_PRSNT`）
     為起點，逐字查其在 PROXI `Format` 分頁之列與值域
   - 另以 LID `Proxi & Configuration` 分頁之 449 列為母體，逐列判其是否
     與 8 個 leaf 之前置條件／可用性／配備有無相關；判準逐列寫明，
     **無錨者標無錨**（R-DM13 之精神：不得以文字相似度判定）
   - 輸出 `features/display/data/proxi_candidates.tsv`，欄位：
     `lid_row | logical_identifier | function | proxi_row | proxi_values |
     related_leaf | anchor_kind | note`
   - **不得將任何值寫入 TC 欄位**（R-DM20 末段）
6. 依 R-DM21 複查本 feature 既有產出中所有「解得／查得／resolved」之
   陳述，逐處補上其所止之段。至少須查：`signal_resolution.tsv` 之
   統計節、`LOOKUP_MISSES.md` 之查詢範圍聲明、A-DM10a。
7. **LID v1.78 vs v1.76 之差異實測**（上繳 04 §8 第 4 項）：
   以兩檔之 `CAN Mapping` 分頁、`Atlantis High` 欄組為比對面，
   逐 Logical Identifier 比對其 `Signal Name`。輸出三分
   （皆有且同／皆有但不同／單側有）。
   **`Signal Name` 相異者為重點** —— 逐筆列出。
   v1_76 位於 `features/vehicle_setting/inputs/`，**唯讀，不得搬動**。
8. 依 R-DM19 於 `LOOKUP_MISSES.md` 之備註區記載 573 訊號差異對其他
   feature 之潛在影響（登記，不評估）。
9. 更新 `docs/INDEX.md`。

---

## 六、停止條件

沿用 01 §五九條 ＋ 03 §七第 10 條 ＋ 04 §六第 11–13 條，另加：

14. 步驟 5 之 PROXI 解析若需要以相似度、語意近似或人為推定才能把某個
    PROXI 參數接到某個 leaf → 該筆標無錨，**不得猜**。
15. 步驟 7 發現 v1.78 與 v1.76 對同一 Logical Identifier 給出**不同**之
    `Atlantis High` `Signal Name`，且該 LID 出現於任何既有 feature 之
    已交付 TC 中 → **停並回報**。這會是跨 feature 之交付件矛盾，
    非本 feature 可處置。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/05_proxi_and_values.md`）

1. §四五條之抄錄核對表
2. 59 vs 44 之調和說明與調和後之數字
3. `[VALUE]` 重出後之清單與 A-DM11 數字更正
4. `feature.yaml` 之 `reference:` 節全文
5. PROXI `Format` 分頁之結構實測
6. `proxi_candidates.tsv` 全文與其錨種類分布
7. LID v1.78 vs v1.76 之三分結果，`Signal Name` 相異者逐筆
8. R-DM21 之複查結果（逐處補註之清單）
9. **「本包是否仍有該驗而未驗者」之獨立判斷**
10. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-DM18 | `[VALUE]` 擷取＝寬式扣除含 `:` 者；R-DM16 廢止 | Display | 是 |
| R-DM19 | B-CAN 資料庫選定 BHCAN2-R1，附承載範圍 | Display | 是 |
| R-DM20 | PROXI 開工；步驟 11 觸發放寬至前置條件 | Display | 是 |
| R-DM21 | 「解得」須指明止於哪一段 | Display | 是 |
| R-G15 | `feature.yaml` 之 `reference:` 版本綁定 | 全域 | 是 |

五條皆為獨立單一事項。
