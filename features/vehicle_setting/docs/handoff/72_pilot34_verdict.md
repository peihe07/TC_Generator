# 72 下放包 — pilot #3＋#4 之建議分類、PDT24 入庫、46 輪

分析層寫入，2026-08-23。**pilot #4 之 15 條已逐條讀畢並分類。**

---

## 1. 最重要之一項：**畫面層並非全然不可驗**

七條之 procedure 步驟 3 為

```
3. Read the … icon … and check that it changes from the state shown before the failure
```

而其 ER 3 為 `PENDING: DR-5-B`。

**「圖示改變」本身可驗 —— 需要 DR-5-B 的是「改成什麼」，不是「有沒有變」。**
現行寫法把一個**已可斷言之事實**丟進 PENDING。

```
分析層裁定 2026-08-23（R-VS59(4) 之細化）
畫面層待補時，**先寫可觀察之最弱斷言**，其具體內容以 Remarks 承載：

  ER   `The … icon changes from the state recorded in step 1`
  AH   `BLOCKED: DR-5-B —— 變更後之圖示樣式待 TLM HMI Document`

**僅在連「是否改變」都無從斷言時**（如整個彈窗之存在與否依賴未知規格），
方寫 `PENDING: DR-{n}`。

理由：`PENDING` 之 TC 於執行時無通過條件，等同不驗；
而「改變」為來源逐字所載（`shall change`），其可觀察性不依賴 TLM HMI Document。
**此舉使 21 條 `screen_pending` 中之圖示變更類由「不可驗」升為「部分可驗」。**
```

**適用**：pilot #4 之 #1／#2／#5／#6／#7／#8／#11（七條）
＋ 全母體同型者（`shall change according to TLM HMI Document`）。

**不適用**：#3／#4（`shall show an informative popup`）——
其彈窗之存在與否即依賴 TLM HMI Document，維持 `PENDING`。
**惟其 procedure 步驟 3 已寫「check that an informative popup … is shown」，
與 ER 之 `PENDING` 不一致**（§6 之 1:1）→ 見 §2 之 D-3。

---

## 2. pilot #4 之逐條分類

| # | leaf | 內容正確性 | Priority | 畫面層 |
|---:|---|---|---|---|
| 1 | `OneStageHeatedSeat-051` | **defect D-1, D-4** | pass | **defect D-2** |
| 2 | `OneStageHeatedSeat-052` | **defect D-1, D-4, D-5** | pass | **defect D-2** |
| 3 | `TwoStagesHeatedSeat-064` | **defect D-1, D-3** | pass | pass（維持 PENDING） |
| 4 | `TwoStagesHeatedSeat-065` | **defect D-1, D-3** | pass | pass |
| 5 | `TwoStagesHeatedSeat-074` | **defect D-1, D-4, D-5** | pass | **defect D-2** |
| 6 | `ThreeStagesHeatedSeat-098` | **defect D-1, D-4** | pass | **defect D-2** |
| 7 | `ThreeStagesHeatedSeat-099` | **defect D-1, D-4** | pass | **defect D-2** |
| 8 | `ThreeStagesVentedSeats-080` | **defect D-1, D-4** ＋ note | pass | **defect D-2** |
| 9 | `TwoStagesHeatedSeat-061` | **defect D-1, D-6** | pass | n/a |
| 10 | `TwoStagesHeatedSeat-070` | **defect D-1, D-6** | pass | n/a |
| 11 | `TwoStagesHeatedSeat-073` | **defect D-1, D-4** | pass | **defect D-2** |
| 12 | `OneStageHeatedSeat-047` | **defect D-1, D-7** | pass | **defect D-2** |
| 13 | `TwoStagesHeatedSeat-071` | **defect D-1, D-6** | pass | n/a |
| 14 | `TwoStagesHeatedSeat-072` | **defect D-1, D-6** | pass | n/a |
| 15 | `ThreeStagesHeatedSeat-084` | **defect D-1, D-6** | pass | n/a |

**Priority 判定 15/15 pass** —— R-VS56 之類別逐條可覆核，P0(b)／P1 之分界一致。

### D-1（**系統性，15/15**）—— `pre_conditions` 之架構條目

全 15 條之 `pre_conditions` 第 4 項皆為：

```
4. The vehicle architecture is Atlantis Mid
```

**本專案之架構為 Atlantis High。** R-VS19″ 已定架構標籤為**來源沿革**，
非適用性；R-VS67 更定取值一律取 `Atlantis High` 欄組。

**把沿革標籤寫成前置條件，等於要求測試員把車設成 Atlantis Mid** ——
其一不可布置，其二與本專案矛盾，其三與 §4.4（Pre-Condition 為狀態／環境）不合。

**修法**：**刪除該條**。架構沿革記於 `reasoning`，不入工作簿。

### D-2（**7 條**）—— 畫面層之最弱斷言未寫（§1）

### D-3（**2 條**：#3／#4）—— procedure 與 ER 不一致

procedure 步驟 3 寫 `check that an informative popup … is shown`，
而 ER 3 為 `PENDING` —— **§6 要求 ER 與步驟 1:1 且可判定**。

**修法**：procedure 之 check target 改為
`check whether an informative popup is shown`（不預設其存在），
ER 維持 `PENDING: DR-5-B`；或依 §1 寫最弱斷言
`An informative popup is shown`（其存在與否即為斷言），
內容待補於 AH。**二擇一由執行層依來源逐字定，並具名其選擇。**

### D-4（**7 條**）—— `test_item` 上半段吞入下一節標題

#2 之 `test_item` 上半段：

```
Regardless of the value of $HeatedSeatFR$, … according to TLM HMI Document.
1.3.3.3.2 Two Stages Heated Seats Management {4859374}
1.3.3.3.2.1 TLM Algorithm requirements {4859375}
```

**後兩行為下一節之標題，非本需求之文字。**
其成因為 34 輪 §2.1(a) 已具名之區塊切割缺陷（節標題落在前一區塊之尾），
**當時判為「W-107 之正規化式」問題，未察其已落入交付物**。

**違 R-VS6**（上半段須為 037 Requirement Description **逐字**）。

**修法**：`test_item` 上半段以節標題樣式（`\d+(\.\d+)+ .* \{\d{7}\}$`）
逐行剝除。**須以錨點驗**：剝除後 #2 之上半段須僅餘一行。

### D-5（**2 條**：#2／#5）—— HTML 實體未還原

#12 之 `test_item` 含 `&lt;Tdisplay&gt;`，應為 `<Tdisplay>`。
**抽取缺陷落入交付物。** 全母體須掃 `&lt;`／`&gt;`／`&amp;`。

### D-6（**5 條**）—— 訊號名待 R-VS67 之改寫

#9／#10／#13／#14／#15 用 `TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm`，
依 R-VS67 應為 `TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm`（1 bit）。
**已排入 W-128，此處僅記其於 pilot 樣本中之比例（5/15）。**

**惟須注意**：改為 1 bit 後，`= 3 (Heated_seat_high)` 之斷言**無法成立**
（該訊號只有 `0/1`）—— **此即 DR-15′ 之標的**。
**該 5 條改寫後須標 `dr15_exposed = yes`**（R-VS67(d)）。

### D-7（**1 條**：#12）—— 時限之處置

其來源含 `within a time period of <Tdisplay>`，而 TC 之 ER 未提時限
亦未標 BLOCKED。**依 42 包之 D-4 處置**（`-014`／`-031` 之先例）：
ER 寫可觀察終態，**時限以 AH 標 `BLOCKED: DR-24′`**。

### note（#8）—— 兩個 reqid 之條文逐字相同

`4859486`／`4859487` 逐字完全相同。`test_item` 只取其一，**處置正確**；
惟 `specification_reference` 列兩者亦正確（R-VS14）。
**其為 A-VS119 型冗餘之新實例**，登記即可。

---

## 3. pilot #3 之 13 條 —— **不重讀，依同型套用**

其 10 條為 `batch13_v2` 之 `TwoStages*`（與 pilot #4 之 #9／#10／#13～#15 同型），
3 條為 W-101 之 Priority 變動。

```
分析層裁定
pilot #3 之 13 條**依 pilot #4 之同型分類套用**：
  D-1（架構前置條件）／D-4（節標題）／D-5（HTML 實體）／D-6（訊號名）
  四項之掃描**施於全母體 143 條**，不限樣本。
  其逐條結果即 pilot #3 之分類。
**不另出 13 條之逐條表** —— 四項皆為機械可檢，逐條表無增益。
`ThirdRowHeadrestDump-025`／`-030`／`TwoStagesHeatedSeat-057` 三條
之 Priority 判定，依 pilot #4 之 15/15 pass 一併通過。
```

---

## 4. pilot #3＋#4 之總結論

```
pilot #3＋#4（分析層建議，待 Pei 覆核）

**不通過。** 七項 defect，其中 D-1（架構前置條件）為 **15/15 系統性**，
其餘六項各涉 1–7 條。**Priority 判定 15/15 pass。**

七項 defect 之修正**全數為機械可檢**（D-3 需一次擇一之判斷）：
  D-1 刪除 pre_conditions 之架構條目          全母體
  D-2 畫面層改寫最弱斷言 ＋ AH 承載具體內容    圖示變更類
  D-3 procedure／ER 之 1:1                    彈窗類 2 條
  D-4 test_item 剝除節標題                    全母體
  D-5 HTML 實體還原                           全母體
  D-6 訊號名依 R-VS67                         全母體（W-128）
  D-7 時限以 AH 標 BLOCKED                    含 <T…> 者

**修正後方得貼回。** 其與 W-128 合併為一次全母體改寫。
```

---

## 5. PDT24 兩份入庫

```
R-VS68（Pei 2026-08-23）
`PDT24_E2A_R3.3_BHCAN2_melco.dbc`（VersionYear 22／Week 23）與
`20240703_PDT24_E2A_R8.5_FDCAN8_Hand_modified_melmb.dbc`（Week 42）
入 `features/vehicle_setting/inputs/`，標 **`evidence-only`**。

**其不得作為訊號名、值域、或 message 歸屬之來源** ——
基線仍為 `PDT27_E2A_R4_BHCAN`／`R5_FDCAN8`（R-VS8）。
其用途限於**跨版本一致性之佐證**（如 DR-15′ 之補充證據段）。

`INPUTS.sha256` 補入該二檔（**18 檔**），並於 profile 之 `[ADD]` 段
記其 `evidence-only` 之限制。
```

---

## 6. 46 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/71_lid_primary.md    ← 45 輪（未執行）
  features/vehicle_setting/docs/handoff/72_pilot34_verdict.md ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/39_pilot_fix.md，六節先留空。
D-2  逐字轉錄 71 包 §1 之 R-VS67、§2 之 R-VS66、69 包 §1 之 R-VS65、
     72 包 §5 之 **R-VS68** 入 RULINGS.md；R-VS51(2) 標「經 R-VS67 推翻」。
D-3  `INPUTS.sha256` 補入 PDT24 兩檔（**18 檔**）並跑 `shasum -c`；
     profile 之 `[ADD]` 段記其 `evidence-only` 限制。
D-4  `AA` 欄之作者姓名定為 **`PeiPYHsu`**（Pei 2026-08-23），
     寫入 `writeback_036.py` 之常數並更新 dry-run。
D-5  ANOMALIES.md：新開 A-VS146（節標題落入 test_item，34 輪已具名而未察其入交付物）、
     A-VS147（HTML 實體未還原）。依 R-VS35 分線列兩數。D-6 照做。

## 作業（三項，R-VS25）

W-130  **pilot 七項 defect 之全母體修正**（72 包 §2）
       D-1 刪 pre_conditions 之架構條目／D-4 剝除 test_item 之節標題／
       D-5 還原 HTML 實體／D-7 時限改 AH 標 BLOCKED。
       **錨點（R-VS54，須可失敗）**：
         D-1 —— 修正前之版本須報出 143 條含該條目
         D-4 —— `OneStageHeatedSeat-052` 之 test_item 上半段修正後須僅餘一行
         D-5 —— 修正前須報出含 `&lt;`／`&gt;` 者
       各批產 `_v{n+1}`，原版保留。**必列**：各項之修正條數。

W-131  **R-VS67 之全量重跑 ＋ 訊號名改寫**（71 包 §5 之 W-127＋W-128）
       (1) 取值來源改 LID `Atlantis High` 欄組；錨點同 71 包 §5
       (2) 已交付 143 條之訊號名逐條改寫，列「原名 → 新名」
       (3) **改寫後 `= 3 (Heated_seat_high)` 之類斷言無法成立者**
           （1 bit 訊號），逐條列出並標 `dr15_exposed = yes`
       (4) 全量重跑分級，列 W0／W1／W2 與 **138/2/97** 之對照

W-132  **D-2／D-3 之畫面層改寫**（72 包 §1）
       圖示變更類：ER 改 `The … icon changes from the state recorded in step 1`，
       AH 記 `BLOCKED: DR-5-B —— 變更後之圖示樣式待 TLM HMI Document`
       彈窗類（2 條）：依 72 包 §2 之 D-3 二擇一，**具名其選擇**
       **必列**：由 `PENDING` 升為可驗者之條數，與 `screen_pending` 之新數

## 禁區

git 不執行。**不實寫 036 母本**。不執行備份（屬 Pei）。
不補素材、不代擬條文、不自行調和數字。各版保留不刪。
**PDT24 兩檔不得作為取值來源**（R-VS68）。

## 升級條件

W-130 之任一錨點未報出違規；
W-131(3) 之無法成立斷言 > 30（則 DR-15′ 之回溯範圍過半）；
W-132 之升為可驗者 < 10。
```

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS68 | PDT24 兩檔入庫，`evidence-only`，不得作為取值來源 | **Pei** |
| R-VS59(4) 之細化 | 畫面層待補時先寫最弱斷言，具體內容以 AH 承載 | 分析層 |
| pilot #3＋#4 之建議分類 | **不通過**；七項 defect，Priority 15/15 pass | 分析層 → **待 Pei 覆核** |
