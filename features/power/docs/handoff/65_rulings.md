# 65 — 六名人讀裁決；代理量表退回；`$PowerMode$` 與 `OperationalModeSts` 分立

下放包 | 分析層 → 執行層 | 往返 NN = 65

前置：`data/64_report.md` 已覆核，判定 **ACCEPT**。G255 5/5；
`pending_recount_64.tsv` 補甲列正確；供料頁完整；A-PW364 為重要附帶發現；
「機器只到候選，擇一仍須人判」之自陳正確。寫回移至 66 包，續受 S6 阻斷。

## 0. 分析層人讀（R-P381(b)）—— 六名七條

**六名皆非「查無」，全屬 TC 措辭問題**：觀察目標是 TC 作者自造之複合名詞，
規格段落本身有可觀察面。逐條裁決如下（步驟措辭由執行層依 R-1 v3 / IN §11 定稿，
本節給觀察量與結構，不給逐字）。

| tc_id | 原 `<X>` | 裁決 | 觀察量（白名單類）| 備註 |
|---|---|---|---|---|
| `-027` | `call audio routing and the TLM state` | 措辭 | 去話：手機端顯示通話已接通＋HU 揚聲器有通話音訊 (iii)；來話：HU 顯示來電 pop-up (ii)；TLM 態：`$STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed)` (i) | 錨點 `4941715` 為導言句（「according to following logics」），實質規則在 `4941716`+ 各 Case；本條與 `SWE-PM-064/065` 之 Case TC 有 §8.2.1 重疊之虞，**記入 reasoning，不刪**（RD 單位屬上游）|
| `-031` | 同上 | 措辭 | 第二通來話接聽後 HU 揚聲器有通話音訊 (iii)；`PowerSts_Telematic = 2 (Timed)` (i) | `Timeout1 still running` 由 `ENTER_TIMED` ＋ `$BCM_FD_27.Comfort_Enable_Time$` 值建立（R-P371）|
| `-117` | `remote start outcome flag and the TLM state` | 措辭＋C3 | TLM 態：`PowerSts_Telematic = 1 (Standby)` (i)；`RemStartFail` 讀值：**維持 `PENDING: DR-PW23 RemStartFail`** | 步 1「Send the value listed in ITD」為家族 K，依 R-P366 內聯；因（`PhoneCall.Info` 轉 Not_Active）為內部變數，**不符 R-P376(a)(ii)，不適用丁案** |
| `-172` | `HU behavior and the stored logs` | 措辭＋§8.2.1 | 主 CPU 重置：HU 畫面熄滅後重新顯示啟動畫面 (ii)；CAN micro 重置：bus trace 上 `STATUS_TELEMATIC` 訊息中斷後恢復發送 (iv)。觸發：`Press and hold H/K "Power" button for 10 seconds`（`$ICSPowerButton$ = [Pressed]` 10 s，`4941858`）| **ER 2「collects and saves logs」屬 `4941860`，非本條 `test_item`（`4941861`），依 §8.2.1 移除**，reasoning 註明由該錨點之 TC 承擔；「HU performs a radio reset」為 `4941858`，同理僅作 setup ER |
| `-224` | `shown wording` | 措辭＋缺件 | 觀察面：`"Disclaimer"` 畫面／geolocation pop-up 之文字內容 (ii)；具體文字：規格寫「See HMI」，HMI 文件不在 G0 台帳 | **開 DR**（未尋獲文件型，同 DR-PW16–18）：Disclaimer／geolocation pop-up 之 ADAS＋SOS 文字定義與「pop-up or disclaimer」之分流條件；ER 該項 `PENDING: DR-PW{n} HMI disclaimer wording`。Pre-Condition 補 `PROXI VC_VEH_BRAND`、`PROXI TBM_Present`、`PROXI Country_Code` 三值（PROXI `Format` 有列者引列） |
| `-262` | `TLM_Status.Info after each one` | 措辭 | 每一點火條件後 `PowerSts_Telematic = 4 (Full_Operation)` (i)；「功能可用」代理量：當前音源持續播放 (iii)（`4941453` 表 Full-Operation 列「TLM plays the audio active source」）| 家族 K (c) 類，五值逐一，ER 逐值對齊 |
| `-271` | `TLM state again after Timeout1 has elapsed` | 措辭 | 進入時 `PowerSts_Telematic = 2 (Timed)`；`Hold for <Comfort_Enable_Time 值> ms`（R-1 v3 (e)）；之後 `= 1 (Standby)` (i)。步 1「TLM power indication and AMP/ICS/DTV states」改為訊號＋音源播放 (iii) | 與 Timeout1 到期轉態之 TC（`SWE-PM-0xx`）重疊之虞，記 reasoning |

**查無：0。開 DR：1（`-224`）。M-n：不登。**

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P383] 六名之處置依 65 包 §0 表；G252 之六名結案。
         六名皆為 TC 措辭問題，無查無。執行層依 §0 表改寫七條，
         每一觀察量引其錨點 ObjectID；`-172` 依 §8.2.1 移除 `4941860` 之 ER；
         `-224` 開 DR（未尋獲文件型）並登 DATA_REQUESTS；`-117` 之 `RemStartFail` 維持 PENDING。
         G252 期望值：「有錨者入代理量表；六名依 R-P383 結案」。
         裁決者：分析層（Tier 2，R-P381(b) 之人讀）。
```

```
[R-P384] `observable_proxy_64.md` 退回；(ii) 之「具名」不以引號為要件；39 名改人讀。
         （a）機器候選不採：其 (i) 類多為段落中之**觸發**訊號而非**觀察**量
              （如 `disclaimer wording` → `CmdIgnSts`、`displayed font` → `Radio_Theme`），
              以觸發代觀察即 R-13 所禁之對象替換
         （b）R-P353(ii) 之「具名 UI 元件」指規格段落**指名**之元件（logo、icon、gauge、
              seat graphic、App icon、theme、font、pop-up、screen），不以規格原文帶引號為要件；
              引號是 TC 書寫規則（IN §11），非抽取判準。64 包 22 個「填不出」多屬此類
         （c）39 名全數改由分析層人讀：執行層依 R-P381(a) 之格式供料
              `data/g252_thirtynine_65.md`（每名：所屬 tc_id、`test_item` 上半 verbatim、
              各錨點段落全文、現行 Procedure／ER），**不判定**；分析層於 66 包逐名裁
         （d）複合觀察目標（`A and B`、`X against Y`）於供料頁保留原形，
              拆分與否由分析層裁，執行層不預拆
         R-P382 依 R-P36 原文不改，加註。
         裁決者：分析層（Tier 2）。
```

```
[R-P385] `$PowerMode$` 與 `OperationalModeSts` 為規格中二個不同變數，分立處理。
         （a）`ENTER_<STATE>` 之點火序列維持 `$STATUS_BH_BCM1.OperationalModeSts$`：
              CFTS009-4941357 之 token（`Ignition On, Ignition Pre_Start, Ignition Start,
              Ignition Cranking, Ignition On Engine On`）與 `VAL_ 854` 標籤
              （`Ignition_On`、`Ignition_Pre_Start`…）逐字對應，為 R-P371 型證據
         （b）`$PowerMode$`（值域 `IGN_ACC` / `IGN_RUN` / `IGN_LK` / `SNA`…）為另一變數，
              LID 逐字命中 `PowerMode` → `STATUS_BH_BCM2.CmdIgnSts`，`VAL_ 1132` 之
              `IGN_LK` / `SNA` 逐字、餘為 `IGN_` 前綴差，記為**強候選**；
              凡 TC 引 `$PowerMode$` 之步驟改以 `$STATUS_BH_BCM2.CmdIgnSts$` 候選寫，
              Remarks 標待上游確認，**不改 (a) 之片段**
         （c）DR-PW26 第 (1) 問改為二問：`LTM_OperationalModeSts.Info` ≟ `OperationalModeSts`；
              `$PowerMode$` ≟ `CmdIgnSts`。A-PW364 之「方向相反」訂正為「二者非同一變數」
         裁決者：分析層（Tier 2，二項皆機讀逐字證據，上游確認前為候選）。
```

## H. 作業指示

1. 抄 R-P383–R-P385（R-P379：7 條／1 DR／39 名／0 查無 之來源見 §0）；R-P382 加註；DR-PW26 改寫
2. 七條改寫（R-P383），`-224` 開 DR（先查現行最大號）
3. `g252_thirtynine_65.md` 供料 → **停**
4. `$PowerMode$` 引用列改候選（R-P385(b)），列數回報
5. 上繳 `features/power/docs/upstream/65_rulings.md`，附 G255 表

## I. 禁區

沿用 64 包 §I，另增列：不得以觸發訊號充代理量（R-P384(a)）；不得改 `ENTER_<STATE>` 之點火訊號（R-P385(a)）；供料不得預拆複合名（R-P384(d)）。

## J. 自檢

三條。C(3,2)：R-P384×R-P385 — `$PowerMode$` 列可能同在 39 名供料中，供料保留原形、候選由 R-P385 定，一致；餘無交集。
對既有 canon（引用＋觸及）：R-P383 對 §8.2.1 — `-172` 落實；對 R-P376(a) — `-117` 排除，合；對 S6 — PENDING 維持，合；對 R-G13 — 無查無故不觸。R-P384 對 R-P353(ii) — 解釋其「具名」，非改；對 IN §11 — 區分書寫與抽取，合；對 R-13 — (a) 合；對 R-P382 — 退回其產出，加註。R-P385 對 R-P354(a) — 維持；對 R-P368(b) — (b) 逐字證據，合；對 §8.4.1 — 候選不認定，合。無違反。

本包數字（R-P379(a)）：六名七條（`g252_six_63.md` 標題計）；39（`proxy_reachability_63.md` 有錨列）；22／17（`observable_proxy_64.md` 總計列）。

## K. 待 Pei

無阻斷項。B5 續凍。66 包為分析層人讀 39 名，量大，預告。
