# 66 包 —— 執行層回報

**§H 第 1、2、4、5 步完成；第 3 步僅完成其中三項，主體（67 條改寫）未做** —— 理由見 §6。

## 1. G255 —— 本包數字與重算（R-P379(c)）

| 條文所引 | 機讀來源 | 重算 |
|---|---|---|
| 39 名 | `g252_thirtynine_65.md` 之 `## ` 標題 | **39** ✓ |
| 67 條 | 同檔之 `### ` 條目 | **67 條目**；⚠ **相異 `tc_id` 為 65**（二條各掛二名）|
| 26 / 8 / 3 / 2 | §0 表 | 合計 **39**，與 §1 表逐節（12+11+4+5+2+3+2）**一致** ✓ |
| 0 查無 | §0 表 | **0** ✓ |
| DR-PW27 影響列 | §1 表提及 `DR-PW27` 之列 | **12** |

**§H 第 3 步之「改寫 67 條」宜讀為「67 條目 / 65 條相異 TC」。**

## 2. 抄錄與登記

- `RULINGS.md`：**R-P386–R-P388** 逐字抄入（3 / 3）。§J 重驗 3/3/三條，一致。
- R-P36 加註：**R-P353**（白名單增 (v)；A1 家族改取 `4941453` 狀態表）。
- `ANOMALIES.md`：**A-PW366**（見 §3）。
- `DATA_REQUESTS.md`：**DR-PW27 擴大為七項總表**（R-P388），逐項記所影響之 tc_id。

## 3. §H 第 2 步 —— 截斷名重取（A-PW366）

`proxy_reachability_59.py` 之輸出模板為 `` | `{x[:50]}` | ``；
`selectable values offered for SwitchOff_Timeout_Setting.Req` 長 **59 字元**，
截斷後下游以截斷名回查得 0 TC。**以原名重取為 3 條：`-017` / `-018` / `-019`。**

⚠ **截斷發生在報表格式，卻改變了下游之母體** —— 供料頁、代理量表、人讀清單三處皆以該欄為鍵。
**顯示用之截斷不得同時作為資料鍵。** 三個腳本之 `{x[:n]}` 已全部去截斷。

**本次未影響 PENDING 計數**（該三條正是 R-P380(a) 判為運行時而維持 PENDING 者，99 不變）——
**僥倖，同 A-PW356 之形態**。

## 4. §H 第 4 步 —— 「執行層查」逐項結果（`data/lookups_66.md`）

### 解得

| 規格名 | 段 1 | 段 2 / 3 |
|---|---|---|
| `$Radio_Theme$` | LID r1531 | `RADIO_B4.Radio_Theme` ✓ |
| `$ICSPowerButton$` | LID r1039 | `CLIMATIC_PANEL.Radio_btn0` / `DIS_CENTERSTACK.DCSD_Power` ✓ |
| `$Telematic_Power$` | LID r2069 | `STATUS_TELEMATIC.PowerSts_Telematic` ✓ |
| `$PowerMode$` | LID r1375 | `STATUS_BH_BCM2.CmdIgnSts` ✓ |

PROXI `Format` 查得 **9 / 13**：`Brand_Configuration_2`(r566)、`SDARS_Presence`(r542)、
`Audio_Brand`(r597)、`Car_Shape_Configuration`(r305)、`Number_of_Doors`(r309)、
`Rear_View_Camera`(r401)、`Switch_Off_Time`(r510)、`Ecall_Button_Variant`(r871)、`Country_Code`(r468)。
HMI `Settings` 查得 `Welcome Onboard Sound`（r41 / r172）。

### ⚠ §1 表所寫之四個 `PROXI <Param>` 在 PROXI `Format` **不存在**

| §1 表所寫 | PROXI `Format` | LID | 近似名（**不採**）|
|---|---|---|---|
| `VC_VEH_BRAND` | **無** | **無** | `Brand_Configuration_2`(r566)、`Special_Brand_Configuration`(r472) |
| `VC_VEH_LINE` | **無** | **無** | `Vehicle_Line_Configuration`(r466) |
| `VC_SpecialPKG` | **無** | **無** | 無 |
| `TBM_Present` | **無** | **無** | 無 |

`VC_*` 為**規格側之 `$SIGNAL$` 名**（CFTS009 原文即寫 `$VC_VEH_BRAND$`），非 PROXI 參數名。
近似名為**語意跳接**（除 `Brand` 一詞外無共同詞素），屬 R-P368(b) 所禁，**本層不採**。

**影響**：品牌視覺類 12 名中六名（`displayed font`、`displayed App icon`、
`applied theme…`、`shown recirc icon`、`shown gauges`、`shown seat graphic…`）
之**前置條件寫法未定**。三個處置請裁：

- **甲**：依 **R-13** 保留規格原名不加 `$`（`VC_VEH_BRAND = <值>`），PROC 寫出應設定之值
- **乙**：開 DR 請上游確認四對等同性
- **丙**：查 `SR26 Default Settings` / `SR24 Market Config` 之其他分頁（本輪未查）

### 其餘未解得

`$Themed_Sound$`（段 1 無）、`$VC_BODY_STYLE$`（段 1 無）、
`$Door_Ajar_Status$`（**LID r474 有列而 `Atlantis High` 欄空 → 止於段 2**，
與 M-1 / M-2 同型，惟未達 R-G13，**不登 M-n**）、
`Startup Animation Selection`（HMI `Settings` 無 —— 與 §1 表一致，該項為 DID 診斷寫入）。

chime 觸發與 ICS 觸控座標**有候選但無同名**（`GW_B_5.Chime_Priority` 等 /
`DIS_CENTERSTACK.DCSD_DISP_STAT`），**須分析層指定或開 DR**，本層不擇。

## 5. §H 第 3 步 —— 已完成之三項

### 5.1 `FUNC_STATE_<STATE>` 標準片段（R-P387(b)）

落檔 `data/func_state_66.md`，**11 個片段**，自 `CFTS009-4941453` 逐字解析（13 列 × 9 欄）。

⚠ **一項規格結構須記**：星號註腳之定義**不在 `4941453` 段內**，而在相鄰之獨立錨點
（`4941454` / `4941455` = `(*)`；`4941457` = `(**)`；`4941459` = `(***)`）。
**註腳改變 ER** —— 例如 `Idle` 之 Display 欄為 `OFF (*)`，而 `(*)` 明載
「Front_Panel_OnOff.Req icon、**Splash Screen visualization**、HMI Antitheft Screens」為例外，
故**不得寫成「畫面全暗」**。已逐格併入，並與 §1 表 `-202` 之
「Display 僅 `"Splash Screen"`」一致。

⚠ **BoosterOUT／天線二欄之 ON/OFF 位準值規格未載**（逐字為 `ON Refer to {CFTS024}…`），
故 **11 個片段之該三個 (v) 類子項一律 `PENDING: DR-PW27`**，不自造（R-P387(a) / §I）。

⚠ `4941453` 有**二列 `Full-Operation` 與二列 `Timed`**（`Source` 欄之音源清單不同，
後者多 `SDCARD, BT Music streaming or Phone Call`），其餘八欄逐字相同。
本表取**聯集**，差異記明**不擇一**（§8.4.1）。

### 5.2 丁案第三條 `-116`（R-P386 / R-P376(a)）

三要件逐項核：(i) 因（`RemStActvSts` Not Active→Active）與果（轉 `Partial-Operation`）
**同載於 `CFTS009-4941654` 之同一段落**；(ii) 上游為 DBC 訊號；
(iii) 下游為 `$STATUS_TELEMATIC.PowerSts_Telematic$ = 7 (Partial_Operation)`，白名單 (i)。**全備。**

`RemStartFail` 與 `VPLastStatus` 自 Procedure / ER 移除，`test_item` 上半 verbatim 未改，
ITD 內聯改 `NA`。**R-P376(d) 代價**：本條不覆蓋該二內部值本身，已入 `reasoning_note`。

### 5.3 DR-PW27 擴大（R-P388）

七項總表已落，逐項記所影響之 tc_id。**第 (6) 項（CFTS024 / VF654 之位準值）影響最廣** ——
除 `-281` 外，全部 11 個 `FUNC_STATE_<STATE>` 片段之三個 (v) 類子項皆繫於此。

## 6. §H 第 3 步之主體（65 條相異 TC 改寫 ＋ §8.3 拆分）**未做**

據實回報，不粉飾。二個理由：

1. **規模**：§1 表為 39 名 × 逐名之觀察量／觸發／前置／PENDING 四欄指示，
   涉 65 條相異 TC 之全欄重寫，另加 §8.3 拆分增列（`-249` 補 M240 支、
   `-169` 三個離開條件各一、`-182` 拆二、`-222`/`-223` 各一分支）。
   其規模與 B5 相當，而 B5 依 R-P374(a) 續凍。
2. **前置未定**：§4 所報之四個 `PROXI <Param>` 不存在，直接卡住品牌視覺類 12 名中之 6 名；
   chime 與 ICS 觸控之訊號須分析層指定；`$Themed_Sound$` / `$VC_BODY_STYLE$` 未解得。
   在這些未定前改寫，等於以未定判準動 65 條 —— 與 55 包 B5 停手同一理由。

**已可施作而未做者**：電源狀態類 11 名中不依賴上述未定項者、開機與復位類 4 名、
音訊類之 `call audio routing`（`-011` / `-012`）。若分析層裁「先做可做者」，本層可續。

## 7. 現況

| 項 | 值 |
|---|---|
| corpus | 283 條 |
| corpus 內 `PENDING` 文字 | **2**（`-117`、`-224`）|
| 內部訊號 PENDING（R-P380 甲）| 99（未變）|
| 丁案已改寫 | **3**（`-057` / `-065` / `-116`）|
| 家族 K 殘留 | **152**（65 包 154 → 本包 `-116` 內聯 ＋ 1）|
| 五欄逐字相同對 | 11 |
| `FUNC_STATE_<STATE>` 片段 | 11 |
| G0 | 素材 9/9 ＋ 參考庫 7/7 |

## 8. 待裁

1. **四個 `PROXI <Param>` 不存在**（§4）：甲 R-13 保留原名／乙 開 DR／丙 續查其他分頁。
2. **chime 觸發與 ICS 觸控座標之指定**（§4）：候選已列，本層不擇。
3. **§H 第 3 步主體是否分批**（§6）：可先做不依賴未定項者。
4. **`4941453` 之二列 `Full-Operation` / `Timed`**（§5.1）：本層取聯集未擇一，請確認。

**B5 依 R-P374(a) 續凍。**
