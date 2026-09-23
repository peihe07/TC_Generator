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
