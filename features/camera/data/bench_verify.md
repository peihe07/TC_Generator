# 交付前實機驗證清單 — Camera A 本（DECISIONS 6-33）

本檔列出**其可判性依賴實機輸出**、須由 Pei 於交付前實機驗一次之 TC。
非缺陷清單 —— 各列之 lint 與 selfcheck 皆已全綠；此處記的是「紙面可判、實機待證」者。

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVC-058` | `$ adb shell dumpsys media.camera` | 該命令之輸出是否足以判「`Rear_Camera` data path is open」 | CAM-07 審閱 §四-2 |
| `NR1L-RVC-092` | `$ adb shell dumpsys media.camera` | 該命令之輸出是否載有串流解析度（ER 判 `1280 x 800 pixels`）| CAM-08 §5-5 自報 |
| `NR1L-RVC-131`／`-132`／`-133` | **LVDS 模擬器** | 是否具備**注入** RVCM → HU 方向之 LVDS 訊號（`systemStatus.ZoomViewRes`）之能力；若無，三列於工作簿 `Remarks` 註「需 LVDS 模擬器」而**非刪** | CAM-10 審閱 §一-5／DECISIONS 6-38 |
| `NR1L-RVC-108` | bus analyzer 時戳 | `TIME_W_RVC2` ＝ **50 ms** 之觀察窗於人工不可達；須以匯流排錄製之時戳判該窗內之狀態 | CAM-09 審閱 §二 |

| `NR1L-RVC-214` | **亮度治具** | `V33-234` 之「亮度超過 50 %」須以亮度計量測；量測手段來源未載，不造工具 | CAM-12 §3 |
| `NR1L-RVC-196`／`-197`／`-199`／`-211`／`-212` | **LVDS 影像鏈路之插拔** | 「斷開／接回 RVCM ↔ HU 之 LVDS 影像鏈路」是否為 bench 可執行之動作（或須以模擬器代之）| CAM-12 §3 |

## B 本 —— B01a（CAM-14 §3）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-001` | **後照相機無法顯示 X 之車輛配置** | 前提 3「rear view camera cannot display the \"X\" exit button while in DRIVE」為車輛配置事實，非可注入之訊號；須確認治具側可佈此配置，否則該列改標 PENDING 並開 DR | CAM-14 §3 |
| `NR1L-RVCHMI-016` | **熱保護關顯示之進入法** | 四本 DBC `therm` 零命中（**DR-CAM-s**）；須確認 bench 可使 HU 顯示因熱保護關閉 | CAM-14 §3 |
| `NR1L-RVCHMI-020` | bus analyzer 時戳 | `IMMEDIATELY` 無數值，ER 以 `Reverse_Deb` = 750 ms 為觀察窗上界；該窗於人工不可達，須以匯流排錄製之時戳判（同 `NR1L-RVC-108` 之前例）| CAM-14 §3 |

## B 本 —— B01b（CAM-15 §4）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-033`／`-034`／`-035` | **10 秒計時之人工觀察窗** | 三列皆以 `±1 秒`（`-035` 取 9／11 秒兩點）為觀察窗；須確認人工計時之誤差足以判該窗，否則改以 bus analyzer 時戳（同 `NR1L-RVC-108`／`NR1L-RVCHMI-020` 之前例）| CAM-15 §4 |
| `NR1L-RVCHMI-024`／`-032`／`-040` | **30 秒之「不退出」觀察** | 三列以 30 秒（10 秒計時之三倍）驗其不退出；須確認該長度足以排除更長之未載計時器 | CAM-15 §4 |
| `NR1L-RVCHMI-026`／`-027` | **PROXI `Radio_Display_Type` 可改** | 兩列於 Procedure 內改 PROXI 尺寸值（`1`／`2`／`4`）；須確認治具可於不重開機之情況下套用，否則拆為多列 | CAM-15 §4 |


## B 本 —— B02a（CAM-16 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-048` | **四台無線 MOPAR 相機** | §27.1.5 之上限 `four (4)`；須佈四台已連線之無線相機才驗得「第五台不可加入」| CAM-16 §2 |
| `NR1L-RVCHMI-049`／`-062` | **可掃 QR code 之無線相機** | 認證流程須相機端掃 HU 顯示之 QR code；須確認治具具備該能力 | CAM-16 §2 |
| `NR1L-RVCHMI-055` | **push button 之按住／放開可分辨** | §27.2.5.1 以「按住不觸發、放開才觸發」判 push button 型；須確認觸控治具可分離按下與放開 | CAM-16 §2 |
| `NR1L-RVCHMI-064`／`-065`／`-066`／`-069`／`-072`／`-073` | **CarPlay／Android Auto 投影工作階段** | 六列皆以無線／有線投影工作階段為前提；須確認治具可建立與中斷該階段 | CAM-16 §2 |
| `NR1L-RVCHMI-070` | **可休眠之無線相機** | §27.5.1 之 `camera may be asleep`；須確認治具可使相機進入休眠再被喚醒 | CAM-16 §2 |


## B 本 —— B02b（CAM-17 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-077`／`-078`／`-079`／`-080`／`-088` | **兩台 AUX 相機** | 五列之 `all available`／`each`／`always` 須以兩台以上方驗得；須確認治具可同時接兩台 | CAM-17 §2 |
| `NR1L-RVCHMI-087` | **RVC Absent ＋ CHMSL Present 之 PROXI 組合** | §34.4.1 之「該配置不存在」以佈成該配置後無相機入口驗之；須確認治具可寫入該組合 | CAM-17 §2 |
| `NR1L-RVCHMI-096`／`-097`／`-098` | **AUX 未連線／部分連線之狀態** | 三列須佈「全未連線」與「只有 AUX 2 連線」兩種狀態 | CAM-17 §2 |
| `NR1L-RVCHMI-081`～`-098` 之 R1 Low 前提 | **R1 Low 機型** | HU 等級無 PROXI 編碼（六串六本各 0），前提為散文；須確認治具側如何佈 R1 Low | CAM-17 §2 |


## B 本 —— B03（CAM-18 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-100`／`-101`／`-102` | **5 秒訊息之人工觀察窗** | 三列以 ±1 秒（4／6 秒兩點）驗 `Check Entire Surroundings` 之 5 秒時限；須確認人工計時誤差足以判該窗，否則改 bus analyzer 時戳 | CAM-18 §2 |
| `NR1L-RVCHMI-117`／`-118` | **10 秒延長窗 ＋ 逾速度門檻** | 兩列須同時佈「速度逾 8 mph」與「按鍵後 10 秒」之量測 | CAM-18 §2 |
| `NR1L-RVCHMI-110`／`-111`／`-113`／`-114`／`-115` | **觸控手勢治具** | drag／swipe／pinch／rotate／mirror 五種手勢須以觸控治具施加；須確認治具可分辨單指拖曳與雙指縮放 | CAM-18 §2 |
| `NR1L-RVCHMI-120`／`-121`／`-122` | **12 吋直式面板** | 三列前提為 `Radio_Display_Type = 7 (12" 1200x1920)`；須確認治具具備該面板或可改該 PROXI 值 | CAM-18 §2 |
| `NR1L-RVCHMI-119`／`-102` | **兩台無線相機** | `views`（複數）／`for each` 須兩台方驗得 | CAM-18 §2 |
| `NR1L-RVCHMI-123`～`-127` | **QR code 配對流程 ＋ 投影工作階段** | 五列須佈無線相機配對流程與 CarPlay／Android Auto 投影階段 | CAM-18 §2 |


## B 本 —— B04a（CAM-19 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-142` | **5 秒自動關閉之觀察窗** | §30.1.3 之三條清除路徑中「5 秒自動」一支以 6 秒觀察；須確認人工計時誤差足以判該窗 | CAM-19 §2 |
| `NR1L-RVCHMI-144`／`-147`／`-153` | **兩至三台 AUX 相機** | `-144`／`-153` 需兩台（對照非最愛／未改名者），`-147` 需三台（驗 `2,3,4…` 之序）| CAM-19 §2 |
| `NR1L-RVCHMI-150`／`-155`／`-156`／`-157` | **QWERTY 鍵盤輸入與字數邊界** | 四列須逐字輸入至第 7／8／14／15 字並讀取欄位；須確認治具可精確輸入與讀回 | CAM-19 §2 |
| `NR1L-RVCHMI-137` | **可刪除之無線相機** | §29.2.2 之 Delete 須佈一台可刪之無線相機（有線不可刪，§34.9.3）| CAM-19 §2 |


## B 本 —— B05（尾批，CAM-20 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-173`／`-181` | **5 秒橫幅之觀察窗** | 兩列以 4／6 秒兩點驗 `Check Entire Surroundings` 之 5 秒；SYS1 與 `PU0362` 之時限相左（**RDF-16**），實機所見為裁決依據 | CAM-20 §2 |
| `NR1L-RVCHMI-175`／`-182`／`-183`／`-184` | **相機故障注入** | 四列須分別佈：一般錯誤訊息、LVDS 影像鏈路中斷、藍畫面狀態、相機偏離正常位置 | CAM-20 §2 |
| `NR1L-RVCHMI-177` | **後照相機無法顯示 X 之車輛配置** | 同 `NR1L-RVCHMI-001`（B01a）之前提，為車輛配置事實 | CAM-20 §2 |
| `NR1L-RVCHMI-179` | **透明度量測治具** | `60% ±5%` 之判準須以影像分析量測疊層元素之透明度 | CAM-20 §2 |
| `NR1L-RVCHMI-180` | **12 吋直式面板之版面判斷** | §8.4.1 之「無其他選項才疊層」為條件式判準；若該機型仍疊層，**回報而非判 FAIL** | CAM-20 §2 |
| `NR1L-RVCHMI-189`／`-190` | **同時觀察 HU 與儀表** | 兩列須同時錄 HU 與 cluster 之 PAM 指示（閃爍頻率、告警階）；另須可佈障礙物於遠／近兩距 | CAM-20 §2 |
| `NR1L-RVCHMI-191` | **可聽之 PAM 提示音** | 須確認治具可錄 HU 喇叭輸出以判提示音之有無 | CAM-20 §2 |
| `NR1L-RVCHMI-185`／`-187`／`-193` | **PROXI 可於執行中改值** | 三列於 Procedure 內改 `PAM_Configuration`／`CVPAM_Presence`；須確認治具可不重開機套用 | CAM-20 §2 |
| `NR1L-RVCHMI-194`／`-195`／`-196` | **回復出廠預設** | 三列以 `Factory Default` 為驗證點，須確認治具可將 HU 回復出廠值 | CAM-20 §2 |


## B 本 —— B06（拆解審計補生成，CAM-23 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVCHMI-198`／`-199`／`-200`／`-201` | **四款相機配備之 PROXI 組合** | 四列各佈一款（CHMSL/Cargo、TRG、FFCTL、SVC）之 Present；須確認治具可逐款切換 | CAM-23 §2 |
| `NR1L-RVCHMI-202` | **無線 AUX 相機 ＋ 檔位往返** | 驗無線側之 latching／non-persistent；同 `-044` 之有線側形制 | CAM-23 §2 |
| `NR1L-RVCHMI-203` | **9 秒觀察窗** | 與 `-033`（11 秒）成一對夾 10 秒窗；人工計時誤差須足以判 | CAM-23 §2 |


## A 本 —— batch05（拆解審計補生成，CAM-24 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVC-243` | `$ adb shell dumpsys media.camera` | 該命令之輸出是否足以判「`ADAS_LVDS_RRCamera_Cable` 之輸出已複製入 `Rear_Camera_Repetition.Data`」（同 `-058`／`-092` 之前例）| CAM-24 §2 |
| `NR1L-RVC-244`／`-245` | **亮度計 ＋ 可設定之顯示亮度** | 兩列須把 HU 顯示亮度分別設為 51 %／49 % 並以亮度計量測；母列 `-214` 本即列於本檔（CAM-12 §3）| CAM-24 §2 |
| `NR1L-RVC-242` | **`RVC Image` soft button 之可觸及** | `RVC_ImageDefeat.Req` 為內部訊號（四本 DBC 皆無），觸發取其 HMI 面之 `RVC Image` soft button（`SYS-RA-VF551_V2-549` 逐字）；須確認該鍵於實機之位置與可按性 | CAM-24 §2 |


## A 本 batch06 ／ B 本 b08 —— R-CAM19 追溯補齊（CAM-26 §2）

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVC-246` | **bus analyzer 於 LVDS 影像鏈路** | 該分析儀能否觀察 RVCM → HU 之**影像**（非僅控制訊息）確經 LVDS 送達；`-209` 之前例只觀察控制訊息 | CAM-26 §2 |
| `NR1L-RVC-247` | **bus analyzer ＋ 診斷儀** | 以診斷儀讀 DTC 時 LVDS 上是否確有 `diagnosticRequest`／`diagnosticResponse` 可錄；訊息內容待 **DR-CAM-t** | CAM-26 §2 |
| `NR1L-RVCHMI-214` | **可休眠之無線相機 ＋ R 檔** | 同 `-070` 之休眠治具，另須於 R 檔以 `More Cams` 選取無線相機 | CAM-26 §2 |
| `NR1L-RVCHMI-216` | **RVC Absent ＋ CHMSL Present 之 PROXI 組合** | 同 `-087`；兩列皆只勾 HDCC27／DT27（`-087` 於 CAM-27 §2 補正，A-CA39）| CAM-26 §2 |

## RD 建議手段（CAM-29 §3-2，DECISIONS 6-91）

RD 驗證方法欄所要求、而本 feature 之 TC 未採之手段（CAM-28 對帳之 RD-ONLY 11 列）。**不補列**（手段超出來源所定之驗證點）；
列此供實機階段參考 —— 如治具許可，可於實機驗證時一併採用，其結果不改 TC 之判準。逐字摘自 RD `Verification Method`。

| TC | 來源 | RD 建議手段（逐字摘）|
|---|---|---|
| `NR1L-RVC-136` | `VF551_V2-443` | Nominal Cases: Transmit PROXI Dual_Rear_Wheels_Present for all valid states (e.g., "Present", "Not Present"). Timing Tests ... Fault Injection (Missing) ... Fault Injection (Invalid) |
| `NR1L-RVC-137` | `VF551_V2-444` | Nominal Cases: Transmit PROXI Wheelbase values across its entire valid range, including minimum, maximum, nominal, and boundary values. Timing Tests ... Fault Injection (Missing) ... Fault Injection (Invalid) |
| `NR1L-RVC-073` | `VF551_V2-446` | Negative Test Cases: Program various other valid combinations (e.g., HDCC with different Body_Types, different Vehicle_Line_Configuration with Type 4 - DJ ...) ／／ Fault Injection (Missing) ... Fault Injection (Invalid) |
| `NR1L-RVC-074` | `VF551_V2-447` | Negative Test Cases: Program various other valid combinations (e.g., HDCC with different Body_Types, different Vehicle_Line_Configuration with Type 1 - D2 ...) ／／ Fault Injection (Missing) ... Fault Injection (Invalid) |
| `NR1L-RVC-118` | `VF551_V2-451` | Vary the DynamicGrid values to cover all defined states (e.g., Enabled, Disabled). Vary the transmission rate ... Simulate missing DynamicGrid messages ... Simulate invalid DynamicGrid values |
| `NR1L-RVC-160` | `VF551_V2-453` | Vary the ASCM_Stat values to cover all defined states (e.g., active, passive, fault, unavailable). Vary the transmission rate |
| `NR1L-RVC-153` | `VF551_V2-458` | Vary the duration of the "missing" period and the characteristics of the "missing" event (e.g., intermittent loss, complete loss) |
| `NR1L-RVC-122` | `VF551_V2-479` | simulate a customer selecting the "Disable Dynamic Gridlines" option on the Head Unit's HMI |
| `NR1L-RVC-123` | `VF551_V2-480` | simulate a customer selecting the "Enable Dynamic Gridlines" option on the Head Unit's HMI |
| `NR1L-RVC-223` | `VF551_V2-529` | At various precise time points before 5 seconds (e.g., 1 second, 3 seconds, 4.9 seconds), simulate a transition to a non-camera display |
| `NR1L-RVC-071` | `VF551_V3-205` | Use a multi-channel oscilloscope to probe the CAN bus (High/Low) and the RVCM physical power line. Measure the time delta between the CAN trigger and the voltage rise. |

## 驗證方式

1. 於實機執行該列之 Procedure 至該步。
2. 記錄實際輸出（命令之 stdout ／ bus analyzer 之錄製片段）。
3. 若輸出不足以判 ER：回報，該列之 ER 改寫或標 PENDING 並開 DR。

## 沿革

- 2026-09-23 建檔（CAM-10 §1-6），初始三列。
- 2026-09-23 加 `-131`～`-133` 之 LVDS 注入能力（CAM-11 §1-4）。
- 2026-09-23 加 `-214` 之亮度治具與 `-196` 等五列之 LVDS 影像鏈路插拔（CAM-12 §3）。
- 2026-09-23 加 B 本 B01a 三列（CAM-14 §3）。
- 2026-09-23 加 B 本 B01b 三組共 8 列（CAM-15 §4）。
- 2026-09-23 加 B 本 B02a 五組共 11 列（CAM-16 §2）。
- 2026-09-23 加 B 本 B02b 四組共 12 列（CAM-17 §2）。
- 2026-09-23 加 B 本 B03 六組共 16 列（CAM-18 §2）。
- 2026-09-23 加 B 本 B04a 四組共 10 列（CAM-19 §2）。
- 2026-09-23 加 B 本 B05 九組共 20 列（CAM-20 §2）。B 本至此 230/230 完結。
- 2026-09-23 加 B 本 B06 三組共 6 列（CAM-23 §2）。
- 2026-09-23 加 A 本 batch05 三組共 4 列（CAM-24 §2）。全案累計 101 列。
- 2026-09-24 加 A 本 batch06 兩列、B 本 b08 兩列，共 4 列（CAM-26 §2）。全案累計 105 列。
- 2026-09-24 加「RD 建議手段」一節（RD-ONLY 11 列，CAM-29 §3-2）；**非待證列，不入 105 之計**。
