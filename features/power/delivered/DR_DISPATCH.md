# DR_DISPATCH —— 七張 DR 發送包（74 包 / R-P399(b)②）

> 供 Pei 直接發送（R-P399：DR 由 Pei 親送）。
> 每張附**級別／問題／不阻斷之現行處置／影響**；問題全文逐字取自 `features/power/DATA_REQUESTS.md`，**未改寫**。
> 影響條數取自 `delivered/PENDING_LIST.md`。

| DR | 級別 | 影響 TC 數 |
|---|---|---|
| **DR-PW23** | **Medium（live）** | 92 |
| **DR-PW25** | **Low（live）** | 9 |
| **DR-PW26** | **High（live）** | 3 |
| **DR-PW27** | **Medium（live，未尋獲文件型）** | 54 |
| **DR-PW28** | **High（live，未查得型）** | 0 |
| **DR-PW29** | **Low（live）** | 1 |
| **DR-PW30** | **Medium（live）** | 6 |

## DR-PW23　（**Medium（live）**）

**影響 TC：92 條**（逐條見 `PENDING_LIST.md`）

### 問題（逐字取自 `DATA_REQUESTS.md`）

**`RemStartFail` 之觀察途徑未載。** SYSAD v1.1.0 載其為 `The internal variable to manage the success or failure of remote start`，無對應 HMI 畫面、無 DBC 訊號、無診斷指令記載。行為化不可行（29 包 §二-6）。請上游提供讀取方式（診斷指令？工程模式？）。 | **不阻斷撰寫** —— 現以 `PENDING: DR-PW23 observation method for RemStartFail` 佔位於 11 步 ×（proc＋er）＝ **22 格**（rows 65／93／94／101／120／157／158／159／163／165／168），其餘各步完整

---

## DR-PW25　（**Low（live）**）

**影響 TC：9 條**（逐條見 `PENDING_LIST.md`）

### 問題（逐字取自 `DATA_REQUESTS.md`）

**HMI 設定條目之實際名稱未查證。** 29 包 B1 以 `timeout setting`（本文件 16 列前例）與 `auto switch-on setting`（無前例，SYSAD 意譯）為條目名；`Timeout1` 與 `SwitchOff_Timeout_Setting.Req` 是否同一條目亦僅為 SYSAD 控制關係之推論。請上游提供畫面實際條目名。 | **不阻斷撰寫** —— 30 步 B1 改寫暫用現名，答覆後全域替換一次即可

---

## DR-PW26　（**High（live）**）

**影響 TC：3 條**（逐條見 `PENDING_LIST.md`）

### 問題（逐字取自 `DATA_REQUESTS.md`）

**`ENTER_<STATE>` 片段表所需之四項未載（55 包 B2 / R-P354）。** (1) **`$PowerMode$` 之 DBC 歸屬**：CFTS009 §1.3.1.1 之 Body ON（`4941027`：`[IGN_ACC]`／`[IGN_OFF_ACC]`／`[IGN_RUN]`）與 Body OFF（`4941028`：`[IGN_LK]`／`[IGN_OFF]`／`[IGN_START]`／`[undefined]`／`[SNA]`）皆以 `$PowerMode$` 定義，該名於 BH-CAN（sha256 `9ef1ec98…`）與 FD-CAN8（`51c8fd60…`）**查無**；相近者為 `STATUS_BH_BCM1.OperationalModeSts`（`VAL_ 854` 含 `Ignition_Acc`／`Ignition_On`／`Ignition_Off`／`SNA`，**語義相符而拼法不同**）。27 包（pm_29）已逕以後者表 Body ON/OFF 而未登 DR —— 與 DR-PW21 同一形態，認定屬上游職權（§8.4.1）。請確認二者是否同一訊號，並逐一對應其值。 (2) **`Sleep` 態之觀察方法**：`4941032` 之進入條件為「CAN 無匯流排活動」，`4941035` 僅載 HU 送出 sleep indication flag —— **CAN 睡眠後無法再以 CAN 讀 `PowerSts_Telematic`，確認步不可執行**。請指定 Sleep 態之觀察途徑（診斷指令／log／電流量測皆可）。 (3) **`INIT` 態**：`VAL_ 1470 PowerSts_Telematic` **無 INIT 值**（八值為 Sleep／Standby／Timed／Idle／Full_Operation／Logistic_On／Bench／Partial_Operation）；`4941439`／`4941447`／`4941448` 之電壓門檻與進出時序全數外指 **SIS**，SIS 不在 G0 台帳之九份素材內。請提供 SIS 相關章節，或指定 INIT 態之觀察量。 (4) **`$PwrAccDelayAct$`**：`4941055` 以其換算 `Timeout1`（X = 十進位值 × 15 秒），該名於兩份 DBC 查無。請確認其歸屬。 | **阻斷 G246** —— 八個片段中 `ENTER_SLEEP` 與 `ENTER_INIT` 之確認步不可執行，G246「100%」在本 DR 未結前不可能達成（見 A-PW351）。其餘六片段**不阻斷**，Body ON/OFF 驅動步依 R-13 沿用 `$STATUS_BH_BCM1.OperationalModeSts$` 並標 `(DR-PW26)`

---

## DR-PW27　（**Medium（live，未尋獲文件型）**）

**影響 TC：54 條**（逐條見 `PENDING_LIST.md`）

### 問題（逐字取自 `DATA_REQUESTS.md`）

**Disclaimer／geolocation pop-up 之文字定義與分流條件未載於 G0 台帳。** `NR1L-PowerManagement-224`（`SWE-PM-113`）之 ER 須驗「顯示之文字」，而規格於該處寫「See HMI」，**HMI 文件不在本 feature 之 G0 台帳（素材 9 ＋ 參考庫 7）內**。請上游提供：(1) Disclaimer 畫面與 geolocation pop-up 之**ADAS ＋ SOS 文字定義**（逐字）；(2) 「pop-up or disclaimer」二擇一之**分流條件**（即 DR-PW22 所問者之同一情境）。 | **不阻斷撰寫** —— `-224` 之該項 ER 標 `PENDING: DR-PW27 HMI disclaimer wording`；其 Pre-Condition 依 65 包 §0 補 `PROXI VC_VEH_BRAND`／`PROXI TBM_Present`／`PROXI Country_Code` 三值（PROXI `Format` 有列者引列）

---

## DR-PW28　（**High（live，未查得型）**）

**影響 TC：0 條**（逐條見 `PENDING_LIST.md`）

### 問題（逐字取自 `DATA_REQUESTS.md`）

**`VC_*` 命名空間之實體載體與值域未載於任一參考檔。** CFTS009 以 `$VC_*$`（訊號記法）書寫 **9 個相異名**：`$VC_VEH_BRAND$`（**277 次**）、`$VC_VEH_LINE$`（41）、`$VC_SpecialPKG$`（12）、`$VC_BODY_STYLE$`（10）、`$VC_SRT_PRSNT$`（6）、`$VC_MODEL_YEAR$`（6）、`$VC_SpecialPKG_IC$`（1）、及大小寫變體 `$VC_Veh_Brand$`（2）、`$VC_SpecialPkg_IC$`（1）。逐字查 G0 參考庫七檔：BHCAN2 `SG_` **0**、FDCAN8 `SG_` **0**、PROXI `Format` **0**、LID `Logical Identifier` **0**、SR26 全 3 分頁 **0**、SR24 全 8 分頁 **0**；**`VC_` 前綴之名一個都沒有**。另 `$TBM_Present$` 同樣六處 0 命中。**請上游提供**：(1) 該命名空間之實體載體（CAN 訊號／PROXI 參數／DID／其他）；(2) 各名之值域（`$VC_VEH_BRAND$` 之品牌列舉尤其）；(3) 大小寫變體是否同一物（R-7 之單一拼法在此無所適從）。 | **不阻斷撰寫** —— 依 **R-P389(c)** 以 R-13 保留規格原名，**不加 `$`、不加 `PROXI`**，TC 寫 `Set VC_VEH_BRAND = <值> (DR-PW28)`；原名與值皆規格明載，缺的是載體而非資料，**依 R-P389(c) 不算 PENDING**（⚠ 該解釋為分析層對 S6 適用範圍之解釋，67 包 §K 已交 Pei 得否決）。⚠ **近似名不採**（R-P389(d)）：`Brand_Configuration_2`(PROXI r566)、`Special_Brand_Configuration`(r472)、`Vehicle_Line_Configuration`(r466) 為語意跳接，列此供上游對照，執行層未採。

---

## DR-PW29　（**Low（live）**）

**影響 TC：1 條**（逐條見 `PENDING_LIST.md`）

### 問題（逐字取自 `DATA_REQUESTS.md`）

**`CFTS009-4941453` 之 `Full-Operation` 與 `Timed` 各有二列，`Source` 欄不同。** 二列之其餘八欄（AMP／Display／BoosterOUT／Antenna×2／MCU×2）逐字相同，僅 `Source` 欄一列為 `TLM plays the audio active source (Tuner, USB, AUX_IN, etc)`，另一列多 `SDCARD, BT Music streaming or Phone Call`。**請確認二列是否對應不同 HU 變體**（若是，請指出其區辨條件；若否，請指出何者為準）。 | **不阻斷撰寫** —— 依 **R-P391(c)** `FUNC_STATE_<STATE>` 取二列之**聯集**，TC 之 Source 子項寫 `TLM plays the audio active source`，**不列舉音源**。

---

## DR-PW30　（**Medium（live）**）

**影響 TC：6 條**（逐條見 `PENDING_LIST.md`）

### 問題（逐字取自 `DATA_REQUESTS.md`）

**`SplashScreen_Time` 與 `StandardScreen_Time` 之值未載於任一素材。** 二者僅出現於 `CFTS010-4942337` 一處（`After SplashScreen_Time the splash screen is loaded…`／`After StandardScreen_Time the standard screen is visualized…`），**全案無數值定義**（CFTS009／CFTS010／SYS3 文字層逐字掃描，各僅該一次出現且無值）。`-004`（`SWE-PM-071`）之 ER 須驗「`StandardScreen_Time` 之前不顯示、之後顯示」，無值則無法判。**請上游提供二參數之值**（或其所在之參數表）。 | **不阻斷撰寫** —— `-004` 之時間點以 `PENDING: DR-PW30 <參數名> 之值` 佔位，觀察量（`"Splash Screen"`／標準畫面之有無，(ii)）本身已定

---
