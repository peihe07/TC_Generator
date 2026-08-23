# 60 下放包 — 三項裁定、R-VS58（選池優先序）、37 輪

分析層寫入，2026-08-22。**交付 86 條**（76 ＋ batch13 10）。三項作業全數執行且皆有結果。

---

## 1. `DrvSeatHeating.Req` 之表述 —— **成立，來源自證**

執行層列此為「本輪最大未裁項」，且自陳其依據為同族已交付 TC 而非新推論。

**分析層查其來源條文，該表述由來源自身給出**。`4859508` 逐字：

> when `$DriverSide$` = [Right Drive] and the customer **selects
> DrvSeatHeating.Req** in CFTS044-3023/1787/2585 **or the left heated seat**
> in CFTS044-2585, the HU shall send the on-change `$FL_HS_RQ$` = [Pressed]
> or `TELEMATIC_CLIMATE_SETUP.FL_HS_Cmd_Tlm` = [Pressed] …

**來源以 `or` 並列「selects DrvSeatHeating.Req」與「selects the left heated seat」**
—— 即該請求之觸發即為按壓該座椅加熱項。**此為轉錄，非推論。**

```
分析層裁定 2026-08-22
`DrvSeatHeating.Req` 以「按壓左前座椅加熱圖示」表述**成立**，
其依據為 `4859508` 之 `or` 並列，非同族 TC 之慣例，亦非推論。
batch13 之 6 條式 A **不退回**。
撰寫時 `reasoning` 須記其依據為 `CFTS044-4859508` 之並列表述。

**與 35 輪 `-038` 之別**：後者之 `not selectable` 於來源中無任何對應文字，
係自 tc_title 反推；本項於來源中有逐字並列。**轉錄與推論之界線即在此。**
```

---

## 2. `dr_dependent` 之標記範圍 —— **採寬標（65）**

```
分析層裁定 2026-08-22
`dr_dependent` 依**實測之 WARN 類**標記（5 訊號、65 leaf），
非依 DR 之字面範圍（3 訊號、47 leaf）。

理由：該欄之用途為「覆後回溯清單之完備性」。
漏標之代價為回溯遺漏（不可事後補救），多標之代價為多覆核（可事後剔除）。
**兩者不對稱，取寬。**

執行層之選擇正確。
```

---

## 3. A-VS115 —— DR-25 擴為五訊號（分析層改寫）

```
DR-25′（取代 57 包 §2 之 DR-25；型 A/B 兼具，Urgency Medium）
CFTS044 之 SWE leaf 其行為賦值於下列五個訊號，
而該五者於本專案之基線 CAN 資料庫
（`PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`，
 VersionYear 25／VersionWeek 50）中**皆不存在**（`SG_` 命中各 0）：

    TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm      17 leaf
    TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm      16 leaf
    TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm     14 leaf
    TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm     14 leaf
    HSW_Cmd_Tlm                                 4 leaf
    ——— 相異 leaf 合計 65

基線僅有 `TELEMATIC_VEHICLE_SETUP3`。
而 `Logical Identifiers and CAN Mapping v1.76` 之 `Atlantis` 欄組
確載其值域。該等條文之 `EE Architecture` 皆為 `Atlantis Mid`。

請確認：
(a) 承載該五訊號之 CAN 資料庫為何？（請提供）；或
(b) 該等訊號不適用於 R1LR，其對應之 CFTS044 條文於本專案不需驗證？

我方之暫行處置（Pei 2026-08-22，R-VS57）：**以 spec 與 037 所載為主**，
訊號名取來源逐字撰寫 TC，並標 `dr_dependent = DR-25`。
**該等 TC 在現行 CAN 環境上無法執行**，其依賴已逐條標記。
若答覆為 (b)，該 65 leaf 之 TC 逐條撤回。
```

---

## 4. A-VS116 —— **P0 = 6 反映選池歷史，不是風險分布**

`*_STATFailSts` 於 CFTS044 引用 **83 次**，其值域早由 A-VS102 自 DBC 補收
（`0 = Fail_Not_Present`／`1 = Fail_Present`），**即非不可寫**；
而 86 條 TC 中以 `Fail_Present` 為標的者 **0**。

**R-VS56 之 P0(b) 有一半沒有任何 TC。**

成因為選池一路依「reqid 升冪 ＋ 逐 Layer 2 輪流」，**與風險無關**。

```
R-VS58（選池之優先序，分析層裁定 2026-08-22；本輪唯一新條文）
選 leaf 之優先序於「逐 Layer 2 輪流」之上，**先取 Priority 較高者**：

  第一序  依 R-VS56 判為 **P0** 之 leaf
  第二序  P1
  第三序  P2
  同序內  依既有之逐 Layer 2 輪流 ＋ reqid 升冪

**判定時點**：選池時以其**來源條文**預判 Priority（非待 TC 寫成後），
預判與 TC 定稿後之判定不一致者，於上繳具名。

理由：Priority 判準立於 R-VS56，而選池順序未隨之調整，
致 P0(b)（加熱元件失效狀態）之 83 處引用在 86 條 TC 中命中 0。
**「P0 = 6」因而反映選池歷史，不反映風險分布** ——
交付時若被問「最高風險項是否已覆蓋」，該數字無法作答。
```

---

## 5. pilot #3 —— **提前，以 batch13 為主體**

原定門檻為累計 120 條（53 包）。**提前之理由**：
batch13 之 10 條為本 feature 首批「標的訊號不在基線 DBC」之 TC，
其形態（前提為 `Fail_Not_Present`、標的為 Mid 網段命令訊號、
全數標 `dr_dependent`）與前 76 條皆不同，**pilot #1／#2 之結論不涵蓋它**。

```
pilot #3 之抽樣（分析層裁定）
母體：batch13 之 **10 條全數**（不抽樣 —— 其為新形態，且量小）
另加 **3 條**自 W-101 之 Priority 變動 24 條中取
（P0 之 6 條中取 2、由 P2 升 P1 者取 1），驗 R-VS56 之判定是否可覆核。
**合計 13 條。**

分析層先讀並附建議分類，Pei 覆核分類。
```

---

## 6. 37 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/60_review_round36.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/33_priority_pool.md，六節先留空。
D-2  逐字轉錄 60 包 §4 之 **R-VS58** 入 RULINGS.md。
D-3  `DATA_REQUESTS.md`：**DR-25 改寫為 DR-25′**（60 包 §3 全文，5 訊號／65 leaf），
     原文保留加註。
D-4  ANOMALIES.md：A-VS115 依 DR-25′ 關閉；A-VS113／114／116／117 標處置。
     依 R-VS35 列兩數。D-6 照做。

## 作業（三項，R-VS25）

W-104 **pilot #3 之 review sheet**
      batch13 之 **10 條全數** ＋ W-101 之 Priority 變動中取 3 條
      （P0 6 條中取 2、由 P2 升 P1 者取 1），合計 **13 條**。
      產 `docs/reports/pilot3_sheet.md`，每條含十欄全文 ＋
      `dr_dependent`／`priority` 及其所依類別 ＋ 來源條文逐字節錄。

W-105 **batch14 —— 10 條，依 R-VS58 之優先序**
      (1) 先以來源條文預判全池之 Priority，**列 P0／P1／P2 三數**
      (2) 依 R-VS58 選 leaf：P0 優先，同序內逐 Layer 2 輪流
      (3) **`*_STATFailSts` 之 `Fail_Present` 類須優先納入**（A-VS116）
      (4) 預判與定稿後之判定不一致者具名
      套 profile ＋ R-VS52／R-VS56／R-VS57 ＋ Sibling Rows ＋ 無效值優先序；
      §9 十七項自檢 ＋ DBC／LID 值表核對 ＋ **R-VS54 之錨點**

W-106 **`FR_VS_Cmd_Tlm`／`HSW_Cmd_Tlm` 之 18 leaf 可寫性實測**（§3.3 未驗第四項）
      該二訊號之 WARN 類 leaf 從未取用，其可寫性未實測。
      逐 leaf 判其分級與阻塞因子；**`FR_VS_Cmd_Tlm` 另受 A-VS103／DR-18 牽制**，
      其值域之跨列問題須具名，**不得跨列引入**。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
不得跨列引入 `FR_VS_Cmd_Tlm` 之值域；不得放寬 L-VS2 之 FAIL 支。
**不得為使 P0 數上升而改判 Priority** —— R-VS56 之類別為準。

## 升級條件

W-105(1) 之預判 P0 數為 0（則 R-VS58 無標的，須追因）；
W-105(4) 之不一致 > 3；
W-106 判該 18 leaf 全數不可寫；
§9 之任一錨點未命中。
```

---

## 7. 待 Pei

| 項 | 內容 |
|---|---|
| **pilot #3** | 13 條，分析層於次包出建議分類 |
| **DR-25′**（65 leaf）／DR-26／DR-21／DR-17／DR-24′／DR-18／DR-11／DR-20／DR-23／DR-8′ | 待送（**十份**） |
| DR-15 | 待覆；覆後回溯已交付 **6** 條（A-VS86 3 ＋ A-VS108 2 ＋ A-VS114 1） |

---

## 8. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS58 | 選池優先序依 R-VS56 之 Priority；P0 優先 | 分析層（本輪額度用畢） |
| `DrvSeatHeating.Req` 之裁定 | 成立，來源 `4859508` 之 `or` 並列自證 | 分析層 |
| `dr_dependent` 之範圍 | 採寬標（65），漏標與多標之代價不對稱 | 分析層 |
| DR-25′ | 擴為五訊號／65 leaf | 分析層擬 |
