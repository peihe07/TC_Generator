# 00D 下放包補篇 — `TLM HMI Document` 之身分查驗（26PI2.5/HMI 目錄）

分析層寫入，2026-08-20，同一往返（NN = 00）。
Pei 指路徑：
`/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/HMI`

---

## 1. 結論先講

該目錄 **112 個檔案中沒有任何一個名為 `TLM HMI Document`**，
**也沒有任何檔名含 `TLM`**。

但目錄內有涵蓋本 feature 畫面行為之 deck。逐份實測後：

| 候選 | 是否承載 CFTS044 所指之內容 |
|---|---|
| `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf` | **部分是** —— 按鍵行為與 LED／highlight 狀態齊全，**但失效彈窗與左右駕鏡像兩項皆無** |
| `Hard Controls HMI Logic and Flow R1L-R (February 12 2026).pdf` | **否** —— 全文僅 7,818 字元，對 `Heated Steering`／`Vented`／`Heated Seat`／`Fail` 命中 **全為 0** |
| `Pop Up List HMI R1 (26PI).xlsx` | **否**（就失效彈窗而言）—— 見 §3 |
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | **旁證** —— `Settings` 表命中 heated seat 4／vented seat 5／heated steering 3／screen off 2 |
| `PDO Theme Config V3.4.xlsx`（已在 `inputs/`） | 否（00C §3.2） |

**故 DR-5 之處置改為：以 Comfort HMI L&F 覆蓋可覆蓋之部分，
其未覆蓋之兩項（失效彈窗、左右駕鏡像）仍為缺口，RD-1 提問。**

---

## 2. Comfort HMI L&F 之實測

檔案：`Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf`
（Visio 2019 產出，PDF 文字層可讀，`pdftotext` 得 **64,978 字元**）

掃描條件：`pdftotext` 全文、字面比對、區分大小寫者另標。

| 關鍵詞 | 命中 |
|---|---|
| `heated steering`（小寫） | 4 |
| `Heated Seat` | 5 |
| `Vented` | 27 |
| `popup` | 54 |
| **`Fail`** | **0** |
| **`Left Side` / `Right Side`** | **0 / 0** |
| **`DriverSide`** | **0** |
| **`TLM`** | **0** |
| `mirror` | 1（**指 HVAC 旋鈕之 UP/DOWN 彈窗方向，與圖示鏡像無關**）|

其內容形態（節錄之條款標籤）：`HVS1.`、`R1HVS1.`、`R1HVS1.2.`、
`R1HVS2.`、`R1HVS3.`、`W1HVS2.`、`HVACP13.`、`CW1.`、`W0.`
—— 與 Home 之 `HVS6.` 同一標籤體系。

**覆蓋到的**：多段式／單段式加熱方向盤之按鍵循環（HI→MED→LO→OFF）、
LED 與箭頭數、soft button 紅色 highlight、seat zone 彈窗預設、
7 吋只有 On/Off 之差異、Front Comfort 與 Status Bar 之控制列。

**未覆蓋**（CFTS044 那 16 個 leaf 真正需要的）：

1. **失效狀態之彈窗**。CFTS044 條文為
   `IF (STATUS_CSWM.FL_HS_STATFailSts == "Fail_Present") THEN TLM has to
   show an informative popup relative to the failure. Refer to TLM HMI
   Document.` —— Comfort deck 對 `Fail` 命中 **0**
2. **圖示之左右駕鏡像**。CFTS044 條文為
   `When $DriverSide$ = [Left Side], the HU shall show the Heated Steering
   Wheel Icon in the left side of the Heated / Vented Seats screen.
   Refer to PDO graphics.` —— Comfort deck 對 `Left Side`／`Right Side`
   命中 **0 / 0**

---

## 3. Pop Up List（26PI）之實測 —— 失效彈窗不在裡面

檔案：`Pop Up List HMI R1 (26PI).xlsx`，`Main` 表 1,344 列 × 17 欄。

與座椅／方向盤加熱相關者 **6 列**（逐列列出，供執行層引用）：

| 列 | PU id | 分類 | 內容摘要 |
|---|---|---|---|
| 229 | `PU0226` | Controls | 進 controls 畫面調整車輛功能 |
| 300 | `PU0297` | Comfort | 按下加熱／通風座椅 soft control 時顯示；standard level 顯示 `HI`／`LO` |
| 367 | `PU0364` | Climate Comfort | 於 App Drawer 調整加熱／通風時顯示 |
| 576 | `PU0573` | Status Bar | 於狀態列操作 comfort 控制時顯示；**其備註寫 `refer to PDO…`** |
| 577 | `PU0574` | Front Comfort | Front Comfort 內操作；顯示 `HI, MED, LO` 或 `HI, LO` |
| 1323 | `PU1557` | Race Options | BEV Race Prep 啟動時，空調／加熱通風座椅／加熱方向盤停用之通知 |

**以「座椅或方向盤」∩「fail／malfunction／service」交集掃全表，
命中 7 列，逐列檢視後全部與本 feature 無關**（SDARS 訂閱、Alexa VR 等，
命中原因為 `steering wheel VR button` 之字面）。

→ **本 feature 之失效彈窗在 Pop Up List 中不存在。**
這與 §2 之發現互相印證：CFTS044 指向的那份文件，**兩處都沒有。**

---

## 4. 對 DR 表之淨變動

| DR | 變動 |
|---|---|
| **5** | **降為 Medium，並拆為兩半**：<br>**5-A（已解）** 按鍵行為與狀態顯示 → `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf`，**請 Pei 授權自 26PI2.5/HMI 複製入 `inputs/`**（素材補入屬 Tier 3）<br>**5-B（未解，RD-1）** 失效彈窗內容 + 圖示左右駕鏡像 → 上游從未具名，兩份候選皆無 |
| **5b** | **併入 5-B** —— `PDO graphics` 與 `Refer to PDO graphics` 指的是同一件事（圖示置放），而 `inputs/` 之 PDO 兩檔皆不符（00C §3） |
| 新增 | `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` 列為**旁證素材**（Settings 表命中 heated seat 4／vented seat 5／heated steering 3／screen off 2），非阻塞 |

### 4.1 修訂後之 RD-1 提問（取代 00B §3 之版本）

> CFTS044 於 24 處引用 `TLM HMI Document`、2 處引用 `PDO graphics`。
> 我方已比對 26PI2.5/HMI 目錄之全部 deck：
> `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025)`
> 覆蓋按鍵循環與狀態顯示，但**不含失效狀態彈窗**（全文 `Fail` 命中 0）
> 亦**不含圖示之左右駕鏡像**（`Left Side`／`Right Side` 命中 0）；
> `Pop Up List HMI R1 (26PI)` 之 1,344 列中無座椅／方向盤加熱之失效彈窗。
> 請確認：(1) `TLM HMI Document` 是否即 Comfort HMI L&F？若是，
> 失效彈窗定義在哪一版？(2) `PDO graphics` 之確切文件（檔名＋版本＋日期）？
> 影響：16 個 SWE leaf 之失效彈窗斷言、1 個 leaf 之圖示位置斷言。
> 若無答覆，該部分 ER 只寫到訊號層（`STATUS_CSWM.*_STATFailSts ==
> "Fail_Present"`，值域由 `PDT27_E2A_R4_BHCAN.dbc` 給出），畫面層標 BLOCKED。

**注意此提問之可回答性已提高**：不再是「這是哪一份」，
而是「我們找到最接近的一份，它缺這兩塊，請補」。

---

## 5. 順帶查得 —— 與其他 feature 之素材關係

`26PI2.5/HMI` 內另有兩份與已交付 feature 同名而**版本較新**者：

- `Pop Up List HMI R1 (26PI).xlsx` + `Pop Up List HMI R1 Change Log(26PI).xlsx`
  —— 而 `features/comfort/inputs/` 內為
  `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`（舊版）
- `Personal Account HMI Logic and Flow R1L-R (February 10 2026).pdf`
  + Change Log —— User Profiles 之來源

**本包不處理**（不越權補件、不改他 feature 之基線），僅登記
**A-VS09**：本 feature 若採 26PI 版 Pop Up List，將與 Comfort／User
Profiles 之交付基線不同版；跨 feature 之 popup 文字一致性須有裁定。

---

## 6. 本篇之盲區（R-G11）

1. **只逐份實測了 4 個候選**（Comfort L&F／Hard Controls／Pop Up List 26PI／
   HMI Settings List），目錄內另有 108 檔未開。判定依據為檔名語意，
   **未以全文檢索窮舉** —— 若失效彈窗寫在
   `Status Bar HMI Logic&Flow(26PI).pdf`、`Massage Seats HMI L&F`、
   `Core HMI Logic and Flow` 或 `Notifications HMI Logic and Flow` 之中，
   本篇會報「沒有」。**建議 W-13：對該目錄全部 PDF／XLSX 跑一次
   `Fail_Present`／`STATFailSts`／`Heated Steering Wheel Icon` 之全文掃描**
   （執行層可跑，成本低，且是 R-G10 之餘數驗證形態）
2. Comfort deck 之 `pdftotext` 只取得文字層；**Visio 匯出之圖形內文字
   若為向量描邊則抽不到**（canon §9.1 第 6 項：判「不可讀」前須跨素材
   形式試過）。應另以頁面點陣化目視抽樣覆核，至少覆核含
   `Heated / Vented Seats screen` 之頁
3. 檔案清單為 `list_directory` 之結果，**未取 SHA**；
   若採用其中任一份，須先入 `inputs/` 並取雜湊（G-L）

---

## 7. 本篇新開之 anomaly

| id | 內容 |
|---|---|
| **A-VS09** | `26PI2.5/HMI` 之 `Pop Up List HMI R1 (26PI).xlsx` 較 `features/comfort/inputs/` 之 SR24 Post 2A (Dec 15, 2023) 版新；跨 feature popup 基線版本不一致，須裁定 |
| **A-VS10** | CFTS044 指名之 `TLM HMI Document` 於客戶 HMI 目錄無同名檔；最接近之 Comfort HMI L&F 缺失效彈窗與左右駕鏡像兩塊 —— **上游引用指向一個我方無法識別之文件** |
