# 下放包 14 — Bed Lowering Mode：交付準備（DELIVERY_NOTE 起草 + 定稿義務）

日期：2026-08-27
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–13，取 14
對象：執行層（Tier 1）
依據：R-BLM2、R-BLM5、R-BLM14、R-BLM16、A-BLM11。
**生成階段已結束**（176 leaf 全數處置，上繳 13）。本包為交付準備，
**不含新 TC 生成**。

---

## 〇、前置狀態（本包不重驗，僅引用）

| 項 | 值 | 來源 |
|---|---|---|
| 工作簿 | `workbook/bed_lowering_10.xlsx` sha `8adbbe86…1728e` | 上繳 13 |
| 已寫回 | 151 列（列 10–160）| 上繳 13 |
| 生成總數 | 163（151 寫回 + 12 PENDING 未寫回）| 上繳 13 §二 |
| coverage gap | 13 | `COVERAGE_GAPS.md` |
| 覆蓋台帳 | 163 + 13 = 176／176，未歸屬 0、重複 0 | 上繳 13 §二 |
| 未結 DR | 4（DR-1 ~ DR-4）| `DATA_REQUESTS.md` |

**Pei 之 R-G14 抽樣覆核尚未完成**，本包產出於其完成前**不得視為可交付**
（見 §四停點）。

---

## 一、`DELIVERY_NOTE.md` 起草（本包主要產出）

落 `features/bed_lowering/DELIVERY_NOTE.md`。**七節，缺一不可**：

### 1. 交付範圍與計數
- 母體 218 列 = 42 Heading + 176 leaf（R-BLM2）
- 42 Heading 標 `No TC — Heading; refer to child IDs`，不生成
- 176 leaf → 163 生成（151 寫回 + 12 PENDING 未寫回）+ 13 coverage gap
- 所有計數標分母（R-G8）

### 2. 追溯粒度之揭露（R-BLM5，**必揭**）
`specification_reference`（N 欄）全簿 151 列同值，為單行常數
`SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)`，
**不帶章節號**。成因：上游 037 `HMI Source ID` 218/218 列相異值數為 1，
無章節錨（A-BLM4 實測）；錨定原則禁止分析層自行推定。
**後果**：審查者無法自 N 欄定位規格章節，定位須經
`Requirement or Design ID` → 037 → `Requirement Description`。
此為已知代價，非缺陷。

### 3. 上游重複之揭露（A-BLM11，**必揭**）
037 之 006（`request`）與 020（`enable request`）兩群條件逐條對應，
致 006-03/020-03、006-05/020-05 兩對之 Procedure 與 Final 逐字相同。
**保留未合併**（§8.2.1 尊重上游分解），**未製造差異**（造假區分比重複更糟）。
四條各帶鏡映註。

### 4. 非匯流排可判之統計（**必揭**，量級問題）
38 條（B3 LED×4、B4 chime×2、B5 20、B7 12），佔已寫回 151 列之 **25.2%**。
判定方式為目視／可聽，非訊號擷取。
**逐條清單附表**（TC ID + 判定方式：目視／可聽）——
台架若僅具訊號注入與擷取能力，此部分須由人工測試流程承接。
**本節之處置待 Pei 裁**，起草時據實陳述現況，不預設結論。

### 5. PENDING 12 條（未寫回）
逐條列 TC 內容位置（batch json 路徑）、所屬 DR、代入後之補寫回動作。
按 DR 歸屬：DR-1×7、DR-3×1、DR-4×4。

### 6. coverage gap 13 條
引 `COVERAGE_GAPS.md`（不重抄全表），**但必須轉載其「判準與其模稜之處」一節**
—— 該節之兩點分界為執行層判斷、非 037 明載，交付對象有權知道。

### 7. 操作化判斷清單（**必揭**）
散在各批自陳、交付時集中一處。至少含：
- 002-04/05 姿態判準（「後角落低於記錄值」「後低於前」代替 037 之定性描述）
- 041-01/02 以「highest／lowest reported value」代替 `Off-Road 2`／`Easy Entry Mode`（DR-2）
- B7 日／夜環境光無 lux 門檻
- 015-02／016-02 字級判準（「不小於周邊本文」）
- B6 039 群之選單改動途徑未載，以泛稱書寫
- 各批 `provisional_inputs` 之暫定車速值（待 DR-1 複驗）
- 003-04／009-02／033-03／034-03 之「他處不顯示」為有限窮舉

## 二、附表產出

1. `data/nonbus_verdict.tsv` —— 38 條清單（TC ID／req_id／判定方式／所屬批）
2. `data/pending_ledger.tsv` —— 12 條清單（TC ID 佔位／req_id／DR／batch json 路徑）
3. 兩表之計數與 §一各節逐項對帳，不符即停

## 三、TestRail 舊→新 ID 對映

**本 feature 為 BLANK 起建、無既有 TestRail 案例**，故對映表為新建清單而非
新舊對照：`data/testrail_new.tsv`（TC ID／test_set／priority／寫回列號）。
若 Pei 指出實有既有案例需對映，停下回報，不自行推定對映關係。

## 四、停點

`DELIVERY_NOTE.md` + 三份附表產出後停，上繳包 14。

**交付授權為 Pei 之 Tier 3，且以下三項未完成前不得請求授權**：
1. Pei 之 R-G14 抽樣覆核（建議 B7 全查 + 其餘批各抽 1 parent）
2. §一-4 之非匯流排量級問題處置
3. 四筆 DR 之送出決定

**含 PENDING 之工作簿不得出貨（IN §8.4.3）** —— 12 條 PENDING 未寫回，
故現行 151 列工作簿本身不含 PENDING，可出貨性不受阻；但 12 條之
未涵蓋須於 DELIVERY_NOTE §5 明列，不得默記。

## 五、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；7 條 PENDING |
| DR-2 | Off-Road 2／Easy Entry ride-height 對映 | 草案已登記，送否 Pei 決 |
| DR-3 | Bed Lowering cluster graphics definition（PDO）| 草擬完成，送出待 Pei；1 條 PENDING ＋ 2 條連動 |
| DR-4 | 三份 HMI_BP 指引（W-01／X-01／L-34）| 執行層登記；**草擬待分析層**，4 條 PENDING |
