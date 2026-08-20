# 00C 下放包補篇 — `inputs/` 落地查驗（2026-08-20）

分析層寫入，同一往返（NN = 00）。
本篇查 Pei 已放入 `features/vehicle_setting/inputs/` 之 12 檔，
並以**原始二進位**複驗 00A／00B 之結論。

**全部量測跑在 `inputs/` 實體檔經 `copy_file_user_to_claude` 取得之副本上。**
副本之 SHA 見 §1；**權威 SHA 須由執行層於 repo 實體檔上以 `shasum -a 256`
重取並寫入 `inputs/INPUTS.sha256`**（G-L；本篇之 SHA 只證明副本自洽）。

---

## 1. 清單與到位判定

| 檔案 | 大小 | 對應 DR | 狀態 |
|---|---|---|---|
| `R1LR_Atl-H_25PI3.5_…CFTS_044_Vehicle Controls_SR26_20250909-1816.docx` | 252.60 KB | DR-1 | ✅ **真二進位**（`PK\x03\x04`，28 個 zip member）。副本 SHA256 `87fe3177…7060` |
| `SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | 15.92 MB | DR-2 | ✅ 已入（**本篇未複驗內文**，見 §5-1） |
| 四份 037（VentedSeat／HeatedSeat／Heated_Steering_Wheel／Common Features） | 71–83 KB | DR-3 | ✅ 已入 |
| `SYS2  R1LR_Atl-H_25PI1.1_…CFTS_044…20250815-1022_20260324_Version3_Released.xlsx` | 315.75 KB | DR-3 | ✅ 已入 |
| `FM-WI-FSM-036-A01 …SWQT_CFTS044_Vehicle Controls_20260819.xlsx` | 105.69 KB | DR-3 | ✅ 已入 |
| **`PDT27_E2A_R4_BHCAN.dbc`** | 431.84 KB | **新增，未列於任何 DR** | ✅ 883 signals／155 messages |
| **`PDT27_E2A_R5_FDCAN8.dbc`** | 1.12 MB | **新增** | ✅ 1755 signals／323 messages |
| **`PDO Graphics Release - SR24_SR25_Post2A_CR27516_CR27517.pdf`** | 203.93 KB | DR-5b | ⚠️ **不符所需**，見 §3 |
| **`PDO Theme Config V3.4.xlsx`** | 43.42 KB | 新增 | ⚠️ 內容為主題／品牌配色表，非圖示規格，見 §3 |

**仍未到位：`TLM HMI Document`（DR-5，16 leaf）。** 該項依 00B §3 之
判定不是索檔而是 **RD-1 提問**（上游從未具名）。

---

## 2. 以原始二進位複驗 00B —— 兩項結論皆成立

### 2.1 具名檔名：仍然沒有（00B §1 成立）

於**真 docx** 之全部 XML part（含 `header1-3.xml`／`footer1-3.xml`／
`footnotes`／`endnotes`，共 28 member）套同一組正則
`[A-Za-z0-9_\-\.\(\)&, ]{3,90}\.(docx?|xlsx?|xls|pdf|dbc|pptx?)`：

- 命中僅 **1 個**，仍是 `RAR_LTM-R1L_SR21_1A_r8.xlsx`（Revision Notes 內）
- `TLM HMI Document` **24 處**、`PDO graphics` **2 處**、`DBC` **13 處**
  —— 數字與轉檔文字完全一致

**00B §5-1 之最脆弱假設（檔名可能藏在圖說／頁首頁尾／文字方塊）已排除。**

### 2.2 章節號：位置法通過樣式階層之複驗（00B §2 之待驗項）

以 `word/styles.xml` 解出 `styleId 1–7 = heading 1–7`，取 body 之
heading 段落：

| 量 | 值 |
|---|---|
| body heading 段落 | **270** |
| 其中帶章節號者 | **270 / 270** |
| 其中帶 `{7位數}` 者 | **270 / 270** |
| 以 `[Artifact Type` 錨定之需求段落 | **2030** |

leaf 回推結果（樣式階層版）：

| 結果 | leaf |
|---|---|
| 解析到 CFTS044 章節號 | **245** |
| 有 7 位數 ID 但落不進章節 | **25** |
| 無 7 位數 ID | **1** |

**與 00B §2 之位置法（245／25／1）逐項相同。**
代理判準與實質判準在此重合 → **R-VS2(c) 之 PENDING 可解除**，
`specification_reference` 之末段取 CFTS044 章節號。

245 個 leaf 共落在 **20 個相異章節**，最大者
`1.3.3.3.3.1`（23）、`1.3.3.3.5.1`（23）、`1.3.3.3.2.1`（20）、
`1.3.2.1.3.11`（20）、`1.3.3.3.4.1`（20）。

> 註：**270 個 heading 對 254 個相異 `{id}`**（00B §2 之數）——差額 16
> 為同一 id 出現於多個 heading 或 TOC 混入，**未追因**，登記 A-VS06。

---

## 3. 兩份 PDO 檔：**都不是那 1 個 leaf 需要的東西**

### 3.1 `PDO Graphics Release …CR27516_CR27517.pdf`

`pdfinfo`：**1 頁**；`pdfimages -list`：**0 張影像**；
`pdftotext`：**489 字元**，全文為發行封面：

- Release Reference No.：SR24 and SR25 Post 2A HEAD UNIT RELEASE
- CR No.：CR27516 and CR27517
- Vehicles：**KX, KM74, EJ, LB**
- Release Details：為 CR27516／CR27517 修改 **Regen 與 Creep**
- Release Date：2024-07-02

**三重不符**：(a) 沒有圖形，只有封面頁；(b) 主題是 Regen／Creep，
不是方向盤加熱圖示；(c) 車型 KX／KM74／EJ／LB，非 R1LR／Atlantis。

**DR-5b 未關閉。** 需要的是 CFTS044 條文所指之
「Heated Steering Wheel 圖示於左右駕之鏡像置放」之圖形規格。

### 3.2 `PDO Theme Config V3.4.xlsx`

四張表（`Revision Log` / `PDO Themes` / `R1L SR21` / `Splashscreen Type`）。
`PDO Themes` 之欄位為 `Brand` / `HMI theme file` / `PDO Theme File (R1H)` /
`PDO Theme File (R1L)` / `RSE Background Color` / `Vehicle` / `Theme Name`
/ `PDO Release Name`。全簿對 `heated steering` / `heated seat` /
`vented seat` / `mirror` / `Left Side` / `Right Side` **命中 0**。

**性質為品牌主題與配色對照表，與座椅／方向盤加熱圖示無關。**
不關閉任何 DR；建議登記為「已入 `inputs/`、本 feature 不取用」（G-D 留痕）。

---

## 4. 兩份 DBC：**關掉 DR-4b，並提供訊號層之可執行錨點**

`DR-4b`（`$TGW_DISP_STAT$` 之訊號讀取途徑）**已關閉**：

| 訊號 | DBC 內名稱 | message | 值域（節錄） |
|---|---|---|---|
| `$TGW_DISP_STAT$` | `TGW_DISP_STATSts` | `TELEMATIC_DISPLAY2`（BHCAN, id 1500）／`TELEMATIC_FD_4`（FDCAN8, id 1427） | `0 Display_off` / `1 Display_closed` / `2 Normal_mode` / `3 DVD_menu` / `7 Rear_Camera_Display` / `8 On_blanked_screen` … |
| `$HSW_StatFailSts$` | `HSW_StatFailSts`（**逐字相同**） | `STATUS_CSWM`（BHCAN, id 1169） | `0 Fail_Not_Present` / `1 Fail_Present` |
| `FL/FR_HS_STATFailSts` | 逐字相同 | `STATUS_CSWM`（1169）／`BCM_FD_22`（FDCAN8, 602） | `0 Fail_Not_Present` / `1 Fail_Present` |

**這同時獨立佐證 00B §0 之自我更正**：`$HSW_StatFailSts$` 之值域
`Fail_Present` / `Fail_Not_Present` 由 DBC 與 CFTS044 兩個來源一致給出。

### 4.1 30 個 token 對 DBC 之覆蓋（**別誤讀這張表**）

以兩份 DBC 之 signal 名全集（union）比對 037 之 30 個 token：

| 類別 | 數 | token |
|---|---|---|
| DBC 內有（逐字或近似） | **6** | `HSW_Stat`（→`HSW_StatSts`／`Tri_Level_HSW_StatSts`）、`PowerMode`（→`PowerModeSts`）、`ESS_ENG_ST`、`HSW_StatFailSts`、`PrplsnSysAtv`、`TGW_DISP_STAT`（→`TGW_DISP_STATSts`） |
| DBC 內無 | **24** | `VentedSeatFR/FL`、`HeatedSeatFL/FR`、`HSW_Stat_2`、`EngRun_Stat`、`Hybrid_Type`、`DriverSide`、`VC_VEH_LINE`、`Heated_Seats`、`Stop_And_Start_cfg`、`RVC_SK_PRSNT`… |

**「DBC 內無」不等於「未定義」。** 那 24 個多為
**PROXI／車型配置參數與邏輯狀態**（`VC_VEH_LINE`、`Hybrid_Type`、
`Stop_And_Start_cfg`、`Heated_Seats`），或規格另以訊號路徑記法書寫
（`TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm`、`STATUS_CSWM.FL_HS_STATFailSts`）。
其值域已於 00B 確認可自 CFTS044 取得。

**故 DR-4 仍為除名狀態，DR-4b 關閉。** 兩份 DBC 之正確定位是
**訊號層之可執行錨點**（message 名 + CAN id + VAL_ 值表），
供 Procedure／ER 寫出可讀可判之訊號斷言。

> 建議新增條文（**待 Pei 裁**）：TC 引用 CAN 訊號時，以 DBC 之
> **signal 逐字名 + message 名**為準，`$var$` 形態只出現在 test_item
> 上半段之來源逐字內。理由：`$HSW_Stat$` 在 DBC 實為 `HSW_StatSts`，
> 直接把 `$var$` 寫進 Procedure 會寫出一個匯流排上不存在的名字。

---

## 5. 尚未做（**具名留下，不假裝已查**）

1. **SYS3 SYSAD 原始二進位未複驗**：00B §1 對 SYS3 之「參考文檔無具名」
   結論仍跑在轉檔文字上。15.92 MB 之真檔可能含轉檔遺失之表格與圖說 →
   **W-1 之後由執行層重跑同一組正則**
2. **四份 037 與 036 未以 `inputs/` 實體檔重測**：00 包 §5.2 之全部預期值
   仍為沙箱數字，等 W-2／W-3
3. **DBC 之 release 身分未驗**：`PDT27_E2A_R4` 與 `R5` 為兩個 release，
   本 feature 之基線是哪一個未定；且 `HSW_StatFailSts` **只在 R4 BHCAN
   有、R5 FDCAN8 無**——**選錯 DBC 會使 16 個 leaf 的訊號斷言落空**。
   → **A-VS07，須裁定基線 DBC**（同 AMFM 之 CIP_Radio_Tables 形態：
   版本標籤不識別內容）
4. 037 之 `$var$` ↔ DBC signal 之逐條對照表尚未產出（W-8 之延伸）

---

## 6. 對 DR 表之淨變動

| DR | 變動 |
|---|---|
| 1 | **關閉**（真二進位已入） |
| 2 | 已入，**待複驗**（§5-1） |
| 3 | **關閉**（12 檔已入；SHA 待執行層取） |
| 4 | 維持除名 |
| **4b** | **關閉**（DBC 給出 `TGW_DISP_STATSts` 之 message 與值表） |
| **5** | **維持 High** —— `TLM HMI Document` 未到，且無檔名，走 RD-1 提問 |
| **5b** | **維持** —— 已入之 PDO 兩檔皆不符（§3） |
| 6 | 維持（R-VS7 待裁） |

## 7. 本篇新開之 anomaly

| id | 內容 |
|---|---|
| **A-VS06** | CFTS044 body heading 270 個對相異 `{7位數}` 254 個，差額 16 未追因 |
| **A-VS07** | 兩份 DBC 分屬不同 release，`HSW_StatFailSts` 僅存於 `R4_BHCAN`；基線 DBC 未裁定 |
| **A-VS08** | `PDO Graphics Release` PDF 之車型（KX/KM74/EJ/LB）與主題（Regen/Creep）與本 feature 無交集，疑為誤置素材 |
