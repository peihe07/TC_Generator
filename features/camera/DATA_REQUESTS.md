# DATA REQUESTS — Camera (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`_intake/Camera/`；落點為 `sources/raw/<doc_id>/`（R-G66）。
each landing closes or advances the linked anomaly. Ordered by when a batch
actually needs it. Names are verbatim from the citing source where the source
gives one; otherwise the expected naming pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| DR-CAM-a | `SYS2_VF551_V5_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA …_SYSRA_VF617_V5_V01.xlsx`（pattern，比照 V2/V3/V33/V4/V42 之命名）**＋** `…_VF617_V5_Rn.docx`（pattern，比照 `Video_Parking_Assistance_…_VF551_Vn_Rn.docx`）| MISSING | A 本 `SWE-CAM-024` 全條（12/12 來源）；`-003`／`-015`／`-018` 之部分來源。合計 **119 個來源引用** | `AUX Camera` Test Set（單列）整組 BLOCKED；`State Handling`／`Display Arbitration` 追溯不完整 | A-CA01、A-CA05 | **高** —— A 本先寫，此件不到則 A 本無法收尾 |
| ~~DR-CAM-b~~ | `SYS2_VF551_V4 …_V01.xlsx` 之 `VF章節`(I) 欄補齊版 | **CLOSED**（2026-09-16）| — | — | A-CA02 | — —— **R-CAM7** 裁定改以 `D` 欄前導號向下繼承（321/321、60 章），不需補件 |
| ~~DR-CAM-c~~ | `SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)` 之版本確認 | **CLOSED**（2026-09-16）| — | — | A-CA14 | — —— **R-CAM6** 裁定以 `spec-index/cache/` 本為追溯母體，不需補件 |
| ~~DR-CAM-d~~ | Camera Settings 之導航 hop label 出處 | **CLOSED**（2026-09-16）| — | — | DECISIONS §6-7 | — —— **R-CAM8** 裁定 HMI Settings List `Settings` row 464 為足夠權威（canon §5.8(c)），不需補件 |
| ~~DR-CAM-e~~ | 車型 ↔ 品牌之權威對照表 | **CLOSED**（2026-09-16，確認型）| — | — | A-CA19 | — —— **R-CAM5(c)′** 以 PROXI `Brand_Configuration_2` 之實測值為據，不需補件 |
| DR-CAM-f | **缺件之 DBC 三類**（CAM-13 §1 擴）：(1) ~~Atl-Mi 之 `TRANSM2` DBC~~ —— **CAM-12 已以訊號名重掃解消**（`ShiftLeverPosition` 於 637MCA 之 `BO_ 998 STATUS_CCAN5`）；(2) **`BED_EXTENDER` message**（四本皆無）；(3) **HDCC27 之 FD-CAN8 DBC 全本** —— `forms/` 只有四本 DBC，其中唯一之 FD-CAN8 為 `PDT27_E2A_R1_FDCAN8.dbc`（DT27 側）；`STEERING1.LwsAngle_SCCM`（`-152`／`-153`）很可能只是落在該缺本 | MISSING | A 本 `-015`／`-018` 之 Atl-Mi 分支（pilot `NR1L-RVC-004`）；全量後凡引 `SYS-RA-VF551_V42-302` 者 | Atl-Mi 之 gear 訊號 raw 值與 label 須標 `PENDING`；候選替代為 `STATUS_CCAN5.ShiftLeverPosition`（`BO_ 998`，`2 "R"`，P363／637MCA 皆有）待上游確認是否同一訊號 | A-CA23 | **高** —— 車型軸之 Atl-Mi 半邊全受影響 |
| DR-CAM-g | **HMI 入口路徑之逐字來源**（CAM-15 §3 擴範圍；原題「「Controls page」之 HMI entry path」） —— SYS1 匯出中給出進入下列畫面之逐字 hop label 者：(1) **Controls page**；(2) **Status bar Shortcut menu**（`spec-index/cache/` 之 Status Bar 本 99 列與 Core HMI 本 169 列，掃描字串 `shortcut` 於前者 0 命中、後者 1 命中而為 Home Screen 之拖曳重排，皆非開啟動作） | MISSING | A 本 `-016`（手動入口之 controls page 分支）；B 本 `Activation and Exit` 中凡走 controls page 者 | pilot `NR1L-RVC-005`／`-006` 改走 App Drawer 路徑而不受阻；controls page 分支之 TC 須待此件 | A-CA24 | **中** |
| DR-CAM-i | **`LTM_OperationalModeSts` ↔ `CmdIgnSts` 之值對應表**（V33／V42 之 I/O 表或 LID 對應文件）| MISSING | A 本 `-001` 之關機側（pilot `NR1L-RVC-002`）；全量後凡以 `LTM_OperationalModeSts.Info` 為條件之 V33／V42 列 | 關機序列之 CAN 觸發值無來源，TC 以 `PENDING: DR-CAM-i` 標記 | A-CA25 | **中** |
| DR-CAM-h | **Pop Up List 之 camera 相關缺件**（CAM-17 §1-2 擴範圍；原題「Pop Up List 之 camera out-of-position 條目」）—— `forms/Pop Up List HMI R1 (26PI).xlsx` 查無下列兩類之逐字文字：**(1) out-of-position**：`Camera Not in position`／`Camera Out of Position` 兩串全欄掃描皆 **0 命中**；**(2) `connecting` 狀態訊息**（SYS1 §27.5.1／§27.6.2 之 `a message will show letting the customer know the camera is “connecting”`）：`Main` 分頁中 module 為 `Camera`／`Aux Camera` 之列，其訊息欄含 `connect` 者 **15 筆**，逐筆核皆為 Add／Authenticating／Connection Complete／Connection ERROR／Delete 等流程畫面，**無一為 `connecting` 狀態訊息** | MISSING | A 本 `-025`、B 本 `SWE1-RVC-039`（`Warning Banners`）、`SWE1-RVC-080`（`NR1L-RVCHMI-070`，`AUX Camera Access`）| 最終畫面文字無權威；A-CA20 無法依 DECISIONS 6-9 之裁定結案。相關列之 ER 標 `PENDING: DR-CAM-h`，其餘步驟仍可判，不整列 BLOCKED | A-CA20 | **中** —— `Warning Banners` 與 `AUX Camera Access` 兩組交付前須結 |
| DR-CAM-j | **Additional Cameras 之訊號定義**：(1) `SVC_SoftBtn_Rq`、(2) `SVC_DisplaySts` 之承載 message 與 `VAL_`（`forms/` 四本 DBC 字面掃描皆零命中）；(3) `$TGW_DISP_STAT$` 之 **Surround View 值**（`TELEMATIC_DISPLAY2.TGW_DISP_STATSts` 之 `VAL_` 十六項無此項；CFTS020 `R1LR_Atl-H_25PI3.5_Cabin_CFTS_020 ICS and DCSD_20250910_1124.reqifz` 全文之值域亦無，`SVC` 零命中）；(4) `<Tsend>`／`<Tdisplay>` 之時限值 | MISSING | A 本 `-016` 之 Cargo/CHMSL／SVC／FFC 節（`batch01b` 之 `NR1L-RVC-038`／`-040`／`-043`／`-045`）| 四列之訊號側 ER 標 `PENDING: DR-CAM-j`；影像側與按鍵側仍可判，不整列 BLOCKED | A-CA32、RDF-01 | **中** —— `Additional Cameras` 組交付前須結 |
| DR-CAM-k | **VF664 全文件**（`soft key button controls` 之定義）—— `SYS-RA-VF551_V2-535` 逐字：`The Head Unit shall implement the soft key button controls for RVC activation, refer to VF664 and HMI logic and flow.`；`sources/` 與 `forms/` 皆查無 VF664 | MISSING | A 本 `SWE-CAM-003`（batch02c）| 該列依 R-CAM13(b) 須生成（037 有引，不受 §8.4.2 所擋），軟鍵之具體行為與 hop 標 `PENDING: DR-CAM-k` | —— | **中** |
| DR-CAM-l | **Toro (2261) 之現行 PROXI 表** —— 現有 `forms/proxi/Toro_ATL_MI/FCA_PROXI_BIN_EN_CRC16_Toro_20191112.XLSM`（2019 本）之 `PROXI Write` 分頁止於 byte 172，缺 byte 177（`Surround_View_Camera`／`Forward_Facing_Camera`）與 byte 222（`Digital_CHMSL_Camera_Prsnt`）| MISSING | `batch01b` 12 列之 `Toro(2261)` 欄 | 12 列一律勾 0；補件後若 2261 確有該三參數，須回頭補勾並重跑 `Z` | A-CA31 之鄰項 | **中** |
| DR-CAM-m | **EVS HAL 支援之影像格式** —— `SWE-CAM-005` 題為 `Hardware Image Format Support`，惟其兩個來源中 `SYS-RA-VF551_V3-254` **只載解析度**（`1280 x 800 pixels`）與轉指 HMI／PDO 之 aspect ratio，另一來源 `SYS-RA-VF617_V5-183` 屬 DR-CAM-a 缺件；SYS2 全本查無格式（`format`）之列舉 | MISSING | A 本 `SWE-CAM-005`（`batch02b` 之 `NR1L-RVC-092`）| 解析度面可判並已生成；**格式面**標 `PENDING: DR-CAM-m`，037 之 `physical image format` 不作 literal 來源（RDF-04 同理）| —— | **中** |
| DR-CAM-n | **Atl-Hi PROXI `Body_Types` 之列舉**（byte 231 bit 0–2）—— `forms/proxi/HDCC28_ATL_HI`／`DT28_ATL_HI`／`HDCC27_initial` 三本之 row 1018 **只載現值**（`7 = Type 7`），`I` 欄無 `0 = …`／`1 = …` 之列舉；`SYS-RA-VF551_V2-446`／`-447` 所引之 `Type 4 - DJ`／`Type 1 - D2` 因而無 raw 可實測 | MISSING | A 本 `SWE-CAM-002`（`batch02b` 之 `NR1L-RVC-073`／`-074`）| 兩列之 Pre-Condition 以 label 式書寫（`PROXI Body_Types = Type 4 - DJ`，§8.7.5(e)），補件後可改為 `<raw> (<label>)` | DECISIONS 6-24 | **中** |
| DR-CAM-o | **HU 所支援之語言清單與各語言之警示文字譯文** —— `HMI Settings List` `Settings` 分頁 row 147 只載佔位式之 `List items: 1) Language 1, 2) Language 2, 3) Language 3, …`，無實際語言名；各語言之警示文字譯文亦無來源。（**CAN 側之 raw 對照已不需要** —— 依 A-CA17 該訊號不可注入，觸發改走 HMI 語言設定，CAM-13 §1 縮範圍）| MISSING | A 本 `SWE-CAM-003`（`-113`）與 `SWE-CAM-023`（`batch04` 二列）| procedure 只寫「選一個與現用不同之語言」，ER 只驗「與所選語言一致」不比對字串 | A-CA17 | **低** —— 不阻塞生成 |
| DR-CAM-p | **LVDS 訊息之傳送週期** —— `SYS-RA-VF551_V2-479`／`-480` 要求 `gridZoomRequest.DynamicGridRQSts` 先送 `[OFF]`／`[ON]` **two LVDS message cycles** 後再送穩態值；「一個 LVDS message cycle」之時間值於 SYS2 全本與 `forms/` 皆查無 | MISSING | A 本 `SWE-CAM-008`（`batch03a` 之兩列）| 值切換之**結果**照寫；**時序面**（兩週期之長度）標 `PENDING: DR-CAM-p` | CAM-09 上繳 §4-3 難點 A | **中** |
| DR-CAM-q | **DTC 之識別碼** —— `DTC Criteria Matrix`（V2 所引）與 `"TLM Diagnostic Requirement" document`（V42 所引）兩份文件不在本 feature 之素材；`SWE-CAM-004`／`-006` 之條文只寫「set the DTC as defined in …」而未載碼值 | MISSING | A 本 `SWE-CAM-004`（`batch03c` 之 11 列）與 `SWE-CAM-006`（3 列）| ER 只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`；DTC 之讀取本身以散文書寫（profile §7.3）| —— | **高** —— `Diagnostics` 組交付前必結 |
| DR-CAM-r | **`Camera App` 與 `Enhanced Camera App` 之配備旗標來源** —— 兩者為 SYS1 HeadUnitCameraSystems 本之主要配備分支（§6.1.5／§6.5.1／§6.5.3／§6.7.1 等），惟 `forms/proxi/` **六本零命中**（掃描字串 `Camera_App`、`Enhanced_Camera`，命令 `proxi_have.py`，六本各 0）；`Rear_View_Camera_Soft_Button`（byte 112 bit 3）與 `APPS_Presence`（byte 139 bit 7）皆非該旗標 | MISSING | B 本 `SWE1-RVC-043`／`-048-03`／`-050`／`-051-01`～`-04`（B01a 之 `NR1L-RVCHMI-003`／`-007`／`-009`／`-010`～`-013`，7 列）| B01a 七列之配備前提標 `PENDING: DR-CAM-r`，其餘步驟仍可判，不整列 BLOCKED | — | **中** —— `Activation and Exit` 組交付前須結 |
| DR-CAM-s | **熱保護關顯示狀態之進入法** —— SYS1 RVC+PAM §7.1 要求「顯示因熱保護策略關閉時 HU 須喚醒以顯示相機影像」，惟該狀態之進入手段無來源：`forms/` 四本 DBC 掃描字串 `therm` **零命中**（命令 `grep -ic therm`，四本各 0），CameraEventHal 表亦無對應訊號 | MISSING | B 本 `SWE1-RVC-007-02`（B01a 之 `NR1L-RVCHMI-016`，1 列）| 該列之前置標 `PENDING: DR-CAM-s` 並入 `bench_verify.md`；喚醒後之 ER 仍可判 | — | 中 |
| DR-CAM-t | **LVDS `diagnosticRequest`／`diagnosticResponse` 之訊息定義**（訊息之欄位、值與收發方向）—— 037 A 本 `SWE-CAM-013` 之題名逐字 `Message: diagnosticRequest / Response`、Description 逐字 `NCD HAL shall process Message: diagnosticRequest / Response via LVDS.`，惟其三個來源（`SYS-RA-VF551_V42-592`／`-593`／`-595`）皆不載該訊息；掃描字串 `diagnosticRe`（不分大小寫）於 `sources/raw/sys2_vf551_v42_sysra_v01` 一本 **0 命中**（六本 VF551／CFTS092 SYS2 各 0，命令 openpyxl 全格 regex）| MISSING | A 本 `SWE-CAM-013`（`batch06` 之 `NR1L-RVC-247`，1 列）| 該列 ER 之兩個 LVDS 觀察項標 `PENDING: DR-CAM-t`；DTC 側（`V42-593`）照寫 | A-CA38 | 中 |

## §5.3 常數之 PENDING 承接（R-G71）

R-G71 明文：`§5.3` 三常數之 `PENDING` 二條**不得直接複製到新 feature 而不登 DR**。
本 feature 之承接狀態：

| 常數 | 本 feature 是否使用 | `status:` |
|---|---|---|
| `ENTER_SETTINGS_APP`（2 hops，已鎖定，非 PENDING）| **是** —— 為 `ENTER_CAMERA_SETTINGS` 之第 1–2 hop | `status: RESOLVED（沿用既有鎖定值，不複製 PENDING）` |
| `ENTER_VEHICLE_SETTINGS`（first hop PENDING）| 否 —— Camera 之設定位於 Settings App 之 `13. Camera` 類別，非 Vehicle Settings | `status: NOT_APPLICABLE` |
| `ENTER_HOME_SCREEN`（PENDING）| 否 —— 本 feature 現無需自 Home Screen 起步之 procedure | `status: NOT_APPLICABLE` |
| `ENTER_CAMERA_SETTINGS`（本 feature 新增，**R-CAM8 已鎖定**）| 是 | `status: RESOLVED`（2026-09-16）—— 3 hops：`Press "Apps" on Menu Bar to open App Drawer` → `Select "Settings" in the App Drawer` → `Select "Camera"`；ER `The "Camera" settings screen is displayed`。第 3 hop 來源 `HMI Settings List` 分頁 `Settings` row 464 `13. Camera`（序號非 label），canon §5.8(c) |

**FO §4 [ADD] 之 §5.3 承接：完成**（R-G71）—— 四項全部有 `status:`，無 PENDING 複製。
