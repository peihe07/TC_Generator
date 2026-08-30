# 66 — 39 名人讀裁決

下放包 | 分析層 → 執行層 | 往返 NN = 66

前置：`data/65_report.md` 已覆核，判定 **ACCEPT**。G255 4/4；七條改寫落實；
R-P385(b) 實際 1 列之落差**不須訂正條文**（條文寫「凡引 `$PowerMode$` 之步驟」，
`test_item` 上半非步驟，條文本身無誤，執行層讀法正確）；`-179` 殘留歸 B5 確認。
寫回移至 67 包，續受 S6 阻斷。

## 0. 人讀方法與總結

供料頁 39 名／67 條，分析層以錨點去重後逐名讀（digest 由 `g252_thirtynine_65.md` 機械抽取，
每名之 TC 與錨點全文皆讀，未抽樣）。

| 結果 | 名數 |
|---|---|
| 有觀察量，措辭改寫即可 | 26 |
| 有觀察量，但期望值繫於台帳外文件（PDO／HMI 資產或指派）→ DR-PW27 擴大 | 8 |
| 觀察量為內部變數，維持／新增 PENDING（DR-PW23／25／26）| 3 |
| 供料 0 TC（名稱截斷／已於 R-P383 處理）| 2 |
| **查無（R-G13）** | **0** |

**橫向發現三項**：
1. 品牌視覺類（logo／font／App icon／theme／recirc／gauge／seat graphic）之觀察量全為 (ii)，
   規格皆指名元件；**執行層 64 包填不出的原因是規格未加引號**，R-P384(b) 之判斷成立。
2. `4941453` 狀態表為 A1 家族（`functionality available`）之**規格自帶代理量表**：
   每一態逐欄給 Source／AMP／Display／BoosterOUT／Antenna／MCU 之 ON/OFF。
   代理量不必另造，直接取該表該態之列。
3. BoosterOUT／天線供電為**電氣輸出**，白名單四類無此類，須增 (v)。

## 1. 逐名裁決表

欄位：觀察量（類別）／觸發與前置之改法／PENDING 或 DR／備註。
「ITD 內聯」= 依 R-P366(a)；「PROXI」= `PROXI <Param> = <值>`（R-1 v3 (c)），參數名須在 PROXI `Format` 查得列號。

### 品牌視覺類（(ii)，共 12 名）

| 名 | TC | 觀察量 | 觸發／前置 | PENDING／DR | 備註 |
|---|---|---|---|---|---|
| `shown logos` | 149–152、192–195 | `"<vehicle brand> logo"`、`"Beats Brand White logo"`、`"Sirius logo"` 於 brand logo screen 之有無 | 前置 `PROXI Brand_Configuration_2 = <值>`、`PROXI SDARS_Presence`、`PROXI Audio_Brand`（三名皆須查 PROXI `Format`；查無者 R-P368(d) 記未解得）；ITD 內聯 | 無 | 四條件組合各一 TC 已正確；`SWE-PM-054` 與 `-101` 同錨點雙掛，R-P357(b) 保留 |
| `shown logo against the configured brand` | 155、185 | `"Fiat Latam Logo"` 取代 vehicle brand logo | 前置 `DID "Startup Animation Selection" = Fiat Latam`（DID 為診斷寫入，保留來源名不加 `$`，R-1 v3 (d)）；`PROXI VC_VEH_BRAND` 任一非 Fiat 值以證「regardless」 | 無 | |
| `shown logo against the configured parameter` | 148 | 同 `shown logos` 之 vehicle brand logo | `PROXI Brand_Configuration_2` 取二值各一輪，logo 隨值改變（baseline (f)）| 無 | 單值無法證「依參數」，須二值 |
| `displayed font` | 233–235 | 畫面字型 = `"<Brand> font"` | `PROXI VC_VEH_BRAND = <值>`；ITD 內聯 | 字型辨識參照 = PDO graphics → **DR-PW27 擴大**，ER 不 PENDING（元件已指名，參照為測試設備）| |
| `displayed App icon` | 236–238 | `"<Brand> App icon"` 於 App Drawer | 同上 | 同上 | |
| `applied theme against the brand signal` | 228、229 | 畫面 theme = `$VC_VEH_BRAND$` 對應之預設 theme | `PROXI VC_SpecialPKG = none`／不支援值；`PROXI VC_VEH_BRAND` | 預設 theme 定義 = [PDO Theme Configuration] → **DR-PW27 擴大**，ER 該值 `PENDING: DR-PW27` | 指派規則在台帳外，與 font 不同（font 元件已指名） |
| `shown element` | 230 | 各 PDO branded element 之預設值 | 不支援之 CAN 值 | 同上 `PENDING: DR-PW27` | 「listed」之元件清單亦在該文件 |
| `shown recirc icon` | 242、243 | recirc icon（(ii)）| `PROXI VC_VEH_LINE`、`Car_Shape_Configuration`、`Number_of_Doors`／PNET 走 `$VC_BODY_STYLE$` | 指派 = HMI release／PDO graphics → `PENDING: DR-PW27` | |
| `shown gauges` | 250 | performance gauges | `PROXI VC_VEH_LINE` | 同上 `PENDING: DR-PW27` | |
| `shown seat graphic against the brand signal` | 249 | settings seat graphic | `$VC_VEH_LINE$ <> M240` ＋ `PROXI VC_VEH_BRAND` 二值各一輪 | M240 分支為另一 TC（§8.3）；非 M240 之指派 → `PENDING: DR-PW27` | 現行只測非 M240 一支，補 M240 支 |
| `$Radio_Theme$ against the applied theme` | 231、246 | `$RADIO_B4.Radio_Theme$` (i)（64 包機器候選**此處正確**）| 改 theme 觸發（`VC_SpecialPKG`）| 應送值 = [PDO Theme Configuration] → `PENDING: DR-PW27`；`<Tsend>` 無值 → 同 DR | |
| `season the HU determines` | 255–258 | 播放之啟動動畫 = new season animation／normal brand animation (ii)（`4942092/93`）| HU 日期設為邊界前一日 → Ignition On → normal；設為邊界日 → Ignition On → season（BVA，各季一對）| 動畫辨識參照 → **DR-PW27 擴大**，ER 不 PENDING | 「season the HU determines」本身不可觀察，動畫是規格給的可觀察面 |

### 電源狀態類（(i) 為主，共 11 名）

| 名 | TC | 觀察量 | 觸發／前置 | PENDING／DR | 備註 |
|---|---|---|---|---|---|
| `Timeout1 and then trigger an Ignition On event` | 100、101、103、104 | `PowerSts_Telematic = 2 (Timed)` 持續 `Switch_Off_Time` 後 `= 1 (Standby)`；再 Ignition On → Ignition Off 後**立即** `= 1`（00 min 已恢復）| `PROXI Switch_Off_Time = 20`；`-104` 改 `$BCM_FD_27.Comfort_Enable_Time$`（R-P371）；`Hold for <值> ms` | 前置 `SwitchOff_Timeout_Setting.Req = 00 min`：UI 設定名未查得 → 維持 `PENDING: DR-PW23`；100/101 之 antitheft 成功 → `PENDING: DR-PW23 Antitheft_Result.Info` | Timeout1 本身內部，以狀態持續時間為代理 |
| `Timeout1 against the configured parameter` | 119、120 | 同上（持續時間 = `Switch_Off_Time`）| 自 Full_Operation 送 Ignition_Off | 同上前置 PENDING | |
| `TLM state against the operative state management rules` | 118 | `OperationalModeSts = <SNA raw>` 後之 `PowerSts_Telematic` = 送 `Ignition_Off` 時之值 | baseline (f)：先送 Ignition_Off 記 `State_ignoff`，復位，再送 SNA，`Check that State_sna = State_ignoff` | 無 | 「behaves as」以基線比較落實 |
| `FPDM, AMP, ICS and DTV functions` | 123、125 | 取 `4941453` Standby／Sleep 列：Display OFF (ii)、無音訊輸出 (iii)、`PowerSts_Telematic = 1／0`；觸控畫面無反應 (ii) | `ENTER_STANDBY`／`ENTER_SLEEP`（後者 PENDING DR-PW26）| `-125` 繫 ENTER_SLEEP | **A1 標準代理**，見 R-P387(b) |
| `ICS functions and the DTV` | 202 | Idle 列：Display 僅 `"Splash Screen"` (ii)、Source OFF → 無音訊 (iii)；ICS 可用：ICS 面板操作有回應（DCSD 觸控座標 `DIS_CENTERSTACK.*` 上線 (i)，執行層 R-P368 查 SG_）| `ENTER_IDLE` | 無 | DTV OFF 以「畫面僅 Splash」涵蓋 |
| `AMP, ICS and DTV power states and the audio paths` | 055 | Partial_Operation 列：無娛樂音訊 (iii)、Display OFF (ii)；ANC/ACN/chime 可用：觸發一次 chime 有聲 (iii) | `ENTER_PARTIAL_OPERATION`；chime 觸發訊號由執行層 R-P368 查（查無 → DR）| 視查詢結果 | |
| `TLM_Status.Info and the screen content` | 081 | 畫面僅 rear view camera video (ii)、`PowerSts_Telematic = 3 (Idle)` 不變 | `PROXI Rear_View_Camera = Present`（R-P377 中候選）| `Rear_Camera_Enable.Info` False→True 為運行時 → `PENDING: DR-PW23`（R-P380）| |
| `remote start outcome flags and the TLM state` | 116 | `PowerSts_Telematic = 7 (Partial_Operation)` (i) | `$STATUS_BH_BCM2.RemStActvSts$` Not Active → Active | **適用丁案**（R-P376(a) 三要件全備：同段落 `4941654`、因為 CAN、果為白名單）；`RemStartFail`／`VPLastStatus` 自 Procedure/ER 移除，代價入 reasoning | 丁案第三條 |
| `HU mode after the idle period` | 169 | `"FOTA update available"` pop-up 停留 (ii)；`Hold for 60000 ms`；`PowerSts_Telematic = 1 (Standby)` | 前置：FOTA 可用（R-P354(f) 抽象動詞之外，`-290` 系列同題）| FOTA 可用之建立方法：規格指 CFTS057 → 台帳外 → 記 DR-PW27 擴大（文件型）| 三個離開條件各一 TC（§8.3），現行只測 1 分鐘 |
| `screen across the cycles` | 218 | `"Disclaimer"` 畫面於連續 31 個點火循環中出現次數 = 2（第 1、第 31）(ii) | `OperationalModeSts` Off→On 循環 ×31，每循環讀畫面 | 無 | 家族 K (c) 類寫法：`Repeat … 31 times`，ER 逐輪對齊以計數表 |
| `screen against the elapsed time` | 182 | 同一喚醒週期內第二次關門**不**播放動畫 (ii)；`Hold for 1800000 ms` 後或下一喚醒週期播放 | `$Door_Ajar_Status$` → R-P368 解；喚醒週期需 `ENTER_SLEEP` | 繫 ENTER_SLEEP → PENDING DR-PW26 | 拆二 TC：30 分鐘支／下一週期支 |

### 開機與復位類（共 4 名）

| 名 | TC | 觀察量 | 觸發／前置 | PENDING／DR | 備註 |
|---|---|---|---|---|---|
| `TLM screen content before and after StandardScreen_Time` | 004 | `"Splash Screen"` 於 `SplashScreen_Time` 後、標準畫面（Home）於 `StandardScreen_Time` 後 (ii)，以錄影時間戳判 | 冷啟動（`ENTER_INIT` PENDING）或 suspend-resume（現行）| 二時間值：執行層查 CFTS010 參數表；查無 → DR | |
| `TLM_Status transitions during the remainder of the boot` | 005 | 開機完成後 `PowerSts_Telematic` = 開機中所注入之最後一個 `OperationalModeSts` 對應態 (i) | 開機中連送 2–3 個 `OperationalModeSts` 值 | 無 | 「event log」規格無 → 刪；「buffered count」不可觀察 → 刪；只剩最終態 |
| `three stored variables` | 049 | 三變數皆內部：VPLastStatus 以 Ignition On 後之態為代理 (i)（Recall_Last 邏輯屬 `4941610`，§8.2.1 不擴）；二個 `.Req` 設定值以 UI 讀 | 電池斷接 | 二 `.Req` 之 UI 名 → `PENDING: DR-PW23／25`；VPLastStatus 代理僅「態與斷電前相同」（baseline (f)）| |
| `TLM_Status.Info and the state machine` | 050 | 電池重接後 bus 上 `STATUS_TELEMATIC` **第一幀** `PowerSts_Telematic = 0 (Sleep)` (iv/i) | 電池斷接 | 無 | INIT 之退出以第一幀落實，不需 ENTER_INIT |

### 設定與選單類（共 5 名）

| 名 | TC | 觀察量 | 觸發／前置 | PENDING／DR | 備註 |
|---|---|---|---|---|---|
| `parameters offered for user selection` | 020、021 | Timeout 設定頁所列設定項之數與名 (ii) | 進入 Settings 之該頁 | 設定項名 = DR-PW25 未決 → `PENDING: DR-PW25` | 依 R-P377(b) 弱候選不入 |
| `offered items against the TLM HMI documents` | 121 | Timed 態 Settings 中 vehicle setup 類項目不可用（灰化／不存在）(ii) | `ENTER_TIMED` 經此二條件 | 項目清單 = TLM HMI documents → `PENDING: DR-PW27` | |
| `user selectable parameter on an ex-factory unit` | 143 | 出廠值：設定頁顯示值 (ii) | 出廠重置（方法：執行層查 CFTS／PROXI；查無 → DR）| `PENDING: DR-PW25`（名）；VPLastStatus 不可觀察，僅留 `.Req` 一項 | |
| `user selectable timeout parameter on an ex-factory unit` | 156 | 同上 | 同上 | 同上 | Timeout1 = 00 min 以「Ignition Off 後立即 Standby」為代理 |
| `disclaimer wording` | 216、217、222、223 | 216/217：disclaimer 文字含 `"SOS"`／含 `"Help"` 且不含 `"SOS"` (ii)，**規格自給 token，ER 不 PENDING**；222/223：ADAS 文字 → `PENDING: DR-PW27` | `PROXI Ecall_Button_Variant`、`VC_VEH_BRAND`、`TBM_Present`、`Country_Code` | 222/223 同錨點雙列，`Country_Code` 分支各一（§8.3）| |

### 音訊類（共 2 名）

| 名 | TC | 觀察量 | 觸發／前置 | PENDING／DR | 備註 |
|---|---|---|---|---|---|
| `audio output against the animation start` | 186、187、191 | 啟動音：錄音／錄影同步，聲音起點與動畫第一幀同時 (iii)；191 為無聲 | `$Themed_Sound$` → R-P368 解（PROXI？）；`"Welcome Onboard Sound"` 設定：規格自帶引號，HMI Settings List 查列 | 視查詢 | |
| `call audio routing` | 011、012 | 通話音訊自 HU 揚聲器消失、手機端通話持續且音訊在手機 (iii) | LIN Load Shed 訊號（`STATUS_LIN.*` 依 R-P373(d) 內聯）| 無 | |

### Bench 態（3 名，同一 TC）

| 名 | TC | 觀察量 | 備註 |
|---|---|---|---|
| `audio power amplifier and the BoosterOUT states` | 281 | AMP：音源播放有聲 (iii)；BoosterOUT：輸出腳位電壓 = ON 位準 **(v)** | 見 R-P387(a) |
| `analog and digital antenna supplies` | 281 | 天線相位供電腳位電壓 = ON 位準 **(v)** | 位準值：CFTS024／VF654 → 台帳外 → DR-PW27 擴大（文件型）|
| `USB and AUX MCU states` | 281 | USB：插入 USB 裝置後被列舉／可播放 (iii)；AUX：AUX 輸入播放有聲 (iii) | |

### 供料 0 TC（2 名）

| 名 | 處置 |
|---|---|
| `selectable values offered for SwitchOff_Timeout_Se` | 名稱於 `proxy_reachability_55.md` 產生時被截斷至 50 字元，供料以截斷名比對故 0 TC。執行層以原名重取，其 TC 併入「設定與選單類」依 `parameters offered` 同法處理；截斷登 A-PW |
| `both processors` | `-172`，R-P383 已處理，結案 |

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P386] 39 名依 66 包 §1 表處置；查無 0；G252 結案。
         執行層依 §1 表改寫 67 條；每一觀察量引其錨點；表中「執行層查」項
         走 R-P368 三段鏈或 PROXI `Format`，查無者記未解得／開 DR；
         「拆」項依 §8.3 增列 TC，tc_id 續號。`-116` 適用丁案（R-P376(a) 三要件於
         `4941654` 全備），為第三條。G252 期望值改「39 名依 R-P386 結案」。
         裁決者：分析層（Tier 2，R-P384(c) 之人讀）。
```

```
[R-P387] 白名單增 (v) 電氣量測；A1 家族以 `4941453` 狀態表為標準代理。
         （a）R-P353 白名單增第 (v) 類：規格定義為 ON/OFF 之供電輸出
              （BoosterOUT、天線相位供電）以腳位電壓／電流量測為觀察量，
              步驟寫 `Measure the voltage at <output> and check that it is <ON 位準>`；
              位準值須規格載明，查無者 PENDING
         （b）`<X> functionality is (not) available` 型（A1）之代理量 = `4941453`
              該態之列：Source（音訊有無 (iii)）、Audio Power amplifier（同）、
              Display（畫面有無／內容 (ii)）、BoosterOUT／Antenna（(v)）、MCU（USB 列舉／AUX 播放 (iii)）；
              另加 `PowerSts_Telematic` 該態值 (i) 與觸控無反應（OFF 態）(ii)。
              執行層建 `FUNC_STATE_<STATE>` 標準片段（IN §5.3），每態一組 ER 子項
         裁決者：分析層（Tier 2；(a) 為白名單擴張，Pei 得否決）。
```

```
[R-P388] DR-PW27 擴大為「HMI／PDO 參考文件未尋獲」總表；丁案第三條。
         DR-PW27 自 disclaimer wording 擴為：HMI release、PDO graphics files、
         [PDO Theme Configuration]、TLM HMI documents（Timed 選單項）、CFTS057（FOTA）、
         CFTS024／VF654（天線供電位準）；每項記所影響之 tc_id。
         規格已指名之元件（`"<Brand> font"`、`"<Brand> App icon"`、season animation）
         **ER 不 PENDING**，僅 Remarks 註「辨識參照見 DR-PW27」；
         指派規則本身在該文件者（theme 預設、recirc、gauge、seat graphic 非 M240、
         `$Radio_Theme$` 應送值）ER 該項 `PENDING: DR-PW27`。
         裁決者：分析層（Tier 2）。
```

## H. 作業指示

1. 抄 R-P386–R-P388（R-P379：39／67／26／8／3／2／0 之來源 = 本包 §0 表，執行層以 §1 表重數）
2. 截斷名重取（§1 末表），登 A-PW
3. 依 §1 表改寫 67 條 ＋ 拆分增列；`-116` 丁案；`FUNC_STATE_<STATE>` 片段；DR-PW27 擴大
4. 「執行層查」項逐一回報結果（查得列號／未解得／DR）
5. PENDING 重算 → `pending_recount_66.tsv`
6. 上繳 `features/power/docs/upstream/66_thirtynine.md`，附 G255 表

## I. 禁區

沿用 65 包 §I，另增列：規格已指名元件之 ER 不得寫 PENDING（R-P388）；指派在台帳外者不得自定指派（§8.4.1）；(v) 類位準值不得自造（R-P387(a)）。

## J. 自檢

三條。C(3,2)：R-P386×R-P387 — §1 表之 A1／Bench 列即引 R-P387，一致；R-P386×R-P388 — §1 表之 DR-PW27 項即 R-P388 所列，一致；R-P387×R-P388 — 天線位準值同時為 (v) 與 DR-PW27，一致。
對既有 canon：R-P386 對 R-P376(a) — `-116` 三要件逐項核；對 §8.2.1 — `-049` 不擴入 `4941610`；對 §8.3 — 拆分列明；對 R-P380 — `-081` 運行時維持 PENDING，合。R-P387 對 R-P353 — 擴張，加註；對 §8.4.1 — 位準不造，合。R-P388 對 S6 — PENDING 維持不出貨，合；對 R-P383 — DR-PW27 之擴大不改其原項，合。無違反。

## K. 待 Pei

無阻斷項。R-P387(a) 白名單擴 (v) 為分析層自裁，你若不認可電氣量測入 TC，一句話撤。
