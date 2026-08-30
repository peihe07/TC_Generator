# 60 / 61 / 62 包 —— 執行層回報

三包合併回報。60 包 §H 第 1–3 步、61 包全步、62 包全步完成；
**60 包 §H 第 4 步（R-P372 人讀複查）未做**，理由見 §6。

## 1. 抄錄與登記

- `RULINGS.md`：**R-P371–R-P373**（60 包）、**R-P374**（61 包）、**R-P375**（62 包）逐字抄入。
  抄前重驗 §J：3/3/三條、1/1/一條、1/1/一條，皆一致。
- R-P36 加註二處：**R-P366(c)**（判準由「多行」改「性質」→ R-P373）、
  **R-P368(a)**（段 1 入口擴為 forms/ 全部參考檔 → R-P375(a)）。
- `ANOMALIES.md`：**A-PW360**（60 包 §0）、**A-PW361**（62 包 §0）、
  **A-PW362**（執行層實測，見 §5）。
- `DATA_REQUESTS.md`：DR-PW26 第 (4) 問改「確認」並附 R-P371 之三項證據；
  DR-PW23 更新為 62 版附表。

## 2. G0 台帳（62 包 §H 第 2 步）

參考資料庫段自 3 檔擴為 **7 檔**。三檔原不在 `forms/FORMS.md`，
本包依 §H 第 2 步**補登其六項欄位**（(a)–(f)，涵蓋範圍為執行層實測）：

| 檔 | SHA256 | 補登 |
|---|---|---|
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | `41daac00…` | ✓ |
| `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` | `8f3ae50e…` | ✓ |
| `SR24 R1 Market Configuration Table v1.6.xlsx` | `7e865d55…` | ✓ |
| `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f…` | FORMS.md 已載（與 M-3 一致）|

各檔之 (d)「已知不涵蓋」皆據實填寫，其中 SR24 本輪 **0 命中**，
依 R-G13 登記為**已查之檔**而非缺漏。

**G0 重跑：素材 9 / 9 ＋ 參考庫 7 / 7，PASS。**

## 3. R-P371 —— K-1 裁乙已落實

`data/enter_state_55.md` 二處更新：

- `ENTER_STANDBY` 第 2 步改
  `Wait until $BCM_FD_27.Comfort_Enable_Time$ (Timeout1) has elapsed with no phone call active`
- `ENTER_TIMED` 之離開條件註記改引 `$BCM_FD_27.Comfort_Enable_Act$`
- §4 總表中 `ENTER_STANDBY` 由「可用（附條件）」改為 **「可用」**
- §5：常數表**無未定項，可寫**（隨 B5 落地）

## 4. R-P373 —— 家族 K 依性質重分類

`data/family_k_disposition_55.tsv` 更新（產生指令：`python features/power/scripts/family_k_59.py`）。
偵測器改以 R-P373(a) 之語言標記判定第 3 類（`one at a time` / `in turn` /
`each of` / `boundary values` 等「一步多值」之標記），**不再以行數判**。

| 類 | 59 包 | **60 包重分類** |
|---|---|---|
| (a) 內聯 | 135 | **142** |
| (b) 單行 > 60 字元，逐條檢 | 15 | **14** |
| (c) IN §4.5 第 3 類獨立資料集 | 8 | **2** |

### ⚠ R-P373(c) 預期 (c) = 0，實測為 2

改判準後**雙向移動**，非單向清零：

- 舊 (c) 之八條（`-006`/`-008`/`-009`/`-010`/`-011`/`-013`/`-015`/`-016`）
  **全部改判為 (a) 內聯** —— 與 R-P373(c) 一致。
- **另有二條由 (a)/(b) 改判為 (c)**，其為真正之第 3 類：
  - `-107`：ITD `Rear_Camera_Enable.Info: "False" then "True"`，
    Procedure `Send the two values listed in Input Test Data **in turn**`
  - `-262`：ITD 為五個點火狀態之列舉，
    Procedure `Apply **each** ignition working condition … **in turn**`

二者皆為「一步多值、值間並列」，**正是 R-P373(a) 所定義之第 3 類**。
舊判準（多行）看不到它們，因其 ITD 為單行。

**故 (c) 之正確值為 2 而非 0**，G251 之「ITD 非 `NA` 者」期望值
應為 **16**（= (b) 14 ＋ (c) 2），而非 R-P373(c) 所寫之 15。請訂正。

### R-P366(b) 之拆步條款仍無觸發

重分類後複驗：**回指步從來不是末步（0 / 163）**，
(a) 類內聯後末步逾 18 字者 **0 條**。結論與 59 包同。

## 5. ⚠ A-PW362 —— R-P372(b) 之「antitheft 系列 11 名」實測為 6 名

`data/proxy_reachability_55.md` 之 51 個無錨名中，含 `antitheft` 者**逐字計為 6**：

`antitheft request and the TLM state`、`antitheft request and the screen`、
`antitheft request, the TLM state and the screen`、`antitheft request`、
`antitheft request, the screen and the TLM state`、
`antitheft request, the stored last status and the TLM state`

R-P372(b) 據「11 名」宣告「複查工作量由 51 降至 40」，**實為 51 − 6 = 45**。

**本族第三次**：A-PW358（執行層寫錯數）、A-PW360（分析層覆核未重數）、
本條（分析層自行寫數未重數）。三次皆為**條文所引之數字與其附表不符**，
而 R-P348 / R-P364 之相容性檢查只查條文之間 ——
**無任何一道閘在查條文所引之數字是否與附表一致**。A-PW360 已指出該缺口，本條為其復發。

## 6. 60 包 §H 第 4 步（R-P372 人讀複查）未做

45 名（非 40）之逐名人讀複查未施作。原因：62 包於本輪中段落檔，
其 §H 六步為更新之指示且與 R-P372 無依賴，本層先完成 62 包全步與 61 包試作。

**R-P372 之複查仍為待辦**，工作量依 §5 訂正為 **45 名**。
其產出 `data/proxy_reachability_60.md` 與 G252 之驗證均未進行。

## 7. R-P375 —— forms/ 全檔段 1 重查（62 包 §H 第 3–4 步）

附表 `data/dr_pw23_internal_signals_62.md`；58 版已加標「未解得 11 名之數不得引用」。

**分析層 §0 所列之五筆命中，本層逐格複核，全部屬實**（`openpyxl` 直取該格，非重搜）。

### 結果：解得 2、候選 4、PENDING 7

本層於附表增列**強度**欄（R-P368(b) 之「比對依據」），因 R-P375(e) 令
「語意跳接仍不許」而 R-P375(b) 又以 `Auto_SwitchOn_Setting.Req` 為示例，二者有張力：

| 候選 | 來源 | 差異之性質 | 強度 |
|---|---|---|---|
| `SwitchOff_Timeout_Setting.Req` / `SwitchOffSetting.Req` → `Switch_Off_Time` | PROXI `Format` r510 c6 | 純底線／後綴差異 | **強** |
| `Rear_Camera_Enable.Info` → `Rear Camera Present` / `Rear_View_Camera` | SR26 r14–15 c12、PROXI r401/r494 c6 | 主體逐字同、屬性詞不同 | **中** |
| `Auto_SwitchOn_Setting.Req` → `Auto-On Comfort` / `Auto_On_Comfort_Enable` | HMI r96–97 c2/c4、PROXI r354/r639 c6 | **`Comfort` 為規格原名所無之語意成分** | **弱** |

⚠ **「弱」者須特別提請覆核**：`Comfort` 之新增語意成分正是 R-P368(b) 所禁之形態，
且該識別**即 DR-PW25 之既有未決問題**（29 包 B1 以 `auto switch-on setting` 為條目名，
**無前例、SYSAD 意譯**）。本層照 R-P375(d) 記為候選，
**但不認為其強度足以撤除 PENDING**，請裁。

`RemStartFail` → `Remote_start`（存在性參數）依 R-P375(e) **非候選**，維持 PENDING。

### 本層獨立重查與分析層互補

本層以**全詞素同格**判準獨立重查五檔（共 50,148 個非空字串格）：
十一名中僅 `Phone_Call.Info`（4）與 `PhoneCall.Info`（2）有命中，
**經逐筆檢視全非候選** —— LID r210 為 `Callnum`
（`Func` = `The number which user selects on the assist app.`，AH = `GLOB_TLM.Call_Number`），
**電話號碼選擇而非通話狀態**；HMI r600/612 為音訊類別清單。
**與分析層 §0「無可用命中」之判斷一致。**

二判準之差即「強度」：**命中愈靠部分詞素，強度愈弱。**

### PENDING 重算（`data/pending_recount_62.tsv`）

| 情形 | 條數 | 佔 283 |
|---|---|---|
| 58 包（僅解得 2 名扣除）| 102 | 36.0% |
| **僅強候選撤** | **98** | 34.6% |
| **四候選全撤** | **79** | 27.9% |

與 58 包之 −3 相比**實益顯著**（最寬情形 −23），
惟差額全部落在強度「弱」與「中」之二名，**故實益之大小取決於覆核如何裁強度**。

⚠ **即使四候選全撤，79 條（27.9%）仍帶 PENDING** ——
**forms/ 全檔重查未能解消 S6 衝突**，R-P374(a) 之甲案續為預設。

## 8. 丁案試作（61 包 R-P374(c)）

落檔 `data/pattern_d_trial_61.md`。**不入 corpus、不計 G 閘。**

選 **`NR1L-PowerManagement-057`**（`SWE-PM-014`）—— 其錨點 `CFTS009-4941504`
（1,354 字元）**單一段落內同時載有因與果**，符合 R-P374(c) 之「皆有明文」。
14 條含 `RemStartFail` 之 TC 中**僅本條與 `-065` 具此性質**（同錨點）。

### 自陳三項（R-P374(e)）

| 項 | 答 |
|---|---|
| (i) 上游事件是否 CFTS 逐字 | **是**。一處非逐字為 `LTM_OperationalModeSts.Info` → `$STATUS_BH_BCM1.OperationalModeSts$`，係 R-P368 段 2 產物，非本試作新造，已標 `(DR-PW26)` |
| (ii) 下游效果是否白名單 | **是**。`$STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby)`，落 (i) 類 |
| (iii) 驗證對象是否改變 | **是，改變了** |

**(iii) 之細節不淡化**：原版驗的是 `RemStartFail` **這個內部變數本身**被設為 `True`；
丁版驗的是 **TLM 是否轉入 Standby**。二者是同一因果鏈上相鄰的兩個環節，
**不是同一個斷言**：

- HU 若未設 `RemStartFail = "True"` 卻因他路徑仍轉入 Standby →
  **丁版通過、原版失敗**（丁版較鬆）
- `RemStartFail` 若正確設值而 Standby 轉移因他故失敗 →
  **原版通過、丁版失敗**（丁版較嚴）
- `test_item` 括號下半即驗證標的之宣告，其改寫**等於改宣告**

**R-13 之慮成立**：丁案不是把同一個驗證改寫得可執行，
而是**換一個可執行的驗證去代替不可執行的那個**。
代價為失去對內部狀態機中間值之覆蓋；收益為該條由不可出貨變為可出貨。

### 本層觀察

丁案在**本條**上可行且證據完備，但 14 條中僅 2 條具備「因果同段落」。
**其餘 12 條若推廣，須跨段落拼接因果，而跨段落拼接即 R-P368(b) 所禁之語意跳接之同型風險。**

故：**丁案不是一個可全推的機制，是一個逐條可用的例外。**

## 9. 待裁

1. **丁案是否推廣**（61 包 §K）—— 本層之觀察見 §8，不建議全推。
2. **四候選之強度**（§7）—— 「弱」之 `Auto_SwitchOn_Setting.Req` 是否足以撤 PENDING；
   PENDING 隨之為 79 或 98。
3. **G251 之 ITD 非 `NA` 期望值**（§4）—— R-P373(c) 寫 15，實測應為 **16**。
4. **R-P372 複查之工作量**（§5）—— 訂正為 45 名；是否照做。

**B5 依 R-P374(a) 續凍（K-2 甲）。**
