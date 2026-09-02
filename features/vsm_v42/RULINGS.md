# RULINGS — Vehicle Setup Management R1 Low（VF665 V42）

Feature slug：`vsm_v42`。條號系列 **`R-VL`**（本線單一來源，R-G23 live 取號）。
姊妹線 `vsm_v43`（`R-VT` 系列）為獨立 feature；兩線互不引用對方條號作為依據，
共用者一律引 canon（IN／FO／`RULINGS_LEDGER.md`）或 PM 之 `R-P` 條文。

裁決者標示：**Pei** = Tier 3 裁定；**分析層** = Tier 2 於 Pei 授權範圍內之裁定。
歷史條文不刪，修訂加註（R-TM13）。

---

### R-VL1 —— 獨立 slug；工作簿自 BLANK 起建

```
R-VL1（Pei 裁定 2026-09-01，00 包待裁題 1：「1 准」）
VF665 V42（Vehicle Setup Management by VP - LTM (R1 Low)）立為獨立 feature，
slug = vsm_v42，自有 RULINGS／ANOMALIES／DATA_REQUESTS／feature.yaml／
framework.md／docs/{handoff,upstream}/。
不併入 features/vehicle_setting/（CFTS044 主線與 VF230 Part 2 所在），
不與 vsm_v43 共用任何工具、資料檔或條號。
工作簿自 BLANK ＋ R-G1 模板起建，不沿用任何既有 036 本。
```

依據：R-BLM1／R-VC1 先例（Vehicle Settings 區之子功能一律獨立 slug）；
VF230 以 Part 2 併入 `vehicle_setting` 之代價已載該 feature `CROSSLINE.md`
（A-VF8／A-VF9：一線之裁定從無機制送達另一線，R-VF17 被例行 driver 重跑抹除；
A-VF30：`writeback_036.py` 寫死路徑指向另一線之工作簿）。
V42 ↔ V43 之 Functional 描述逐字重疊實測僅 30／398（V43 側）、30／308（V42 側），
兩線實質為兩份文件，共用無利可圖。

### R-VL2 —— 訊號書寫依 canon §8.7.5 v3 ＋ PM 現行條文；不承襲 R-VS52

```
R-VL2（Pei 裁定 2026-09-01，00 包待裁題 2：「2 准」）
(a) 本線 profile 不承襲 FW036_R1L_VehicleSetting_Profile.md 之
    [OVERRIDE §8.7.5]（R-VS52，SWC 0708 交付本式 `Send CAN:` 前綴）。
    訊號書寫依 canon IN §8.7.5 v3 (a)–(g)：
      `$<MESSAGE>.<Signal>$ = <raw> (<label>)`，<label> 逐字取 DBC VAL_；
      PROXI 參數 `PROXI <Param> = <值>`，不加 `$`；
      內部訊號（X.Req／X.Info／X.GUI）優先依對照表轉為可觀察 CAN 訊號，
      DBC 查無者保留來源名不加 `$`（(d)），規格訊號名與 DBC 不符者保留原文（(g)，R-13）；
      Hold 獨立成步（(e)）；baseline 採 <Name>_initial／<Name>_after（(f)）。
(b) 併採 PM 之三條（引用制 R-G13，執行層自 features/power/RULINGS.md 讀原文）：
      R-P353  Procedure／ER 之觀察對象限四類白名單
              （$MESSAGE.Signal$／具名 UI 元件 "..."／可量測音訊／log 具名行）；
              functionality／behavior／state 等抽象名詞不得作 <X>
      R-P355  內部訊號不得直接 Set；已有 DBC 對照者改 $MESSAGE.Signal$，
              尚無者 `PENDING: DR-{n} <訊號名>`，不得假裝可執行
      R-P368  訊號實名依 forms/ 三段鏈解析：
              段 1 規格原名 → forms/Logical Identifiers and CAN Mapping v1_78.xlsx
              段 2 → MESSAGE.Signal
              段 3 → forms/PDT27_E2A_R1_BHCAN2.dbc／forms/PDT27_E2A_R1_FDCAN8.dbc 之 SG_ 逐字
              三段皆過者寫 $MESSAGE.Signal$（DBC 實名含大小寫）；止於段 n 者記「未解得（止於段 n）」；
              段 3 查無者始得記「查無」並登 forms/LOOKUP_MISSES.md（R-G14）＋ ANOMALIES ＋ DR。
              features/vehicle_setting/inputs/ 之 R4 BHCAN／R5 FDCAN8 降為旁證，不得逕用其名。
(c) lint 檢查 P 對本線以 `--profile vsm_v42` 走 v3 判準（IN §8.7.5 沿革末段之註）。
(d) input_test_data 一律 NA，資料內聯至 pre_conditions／test_procedure（IN §4.5 SWC 基準）。
```

依據：Pei 原話「訊號寫法要遵照 power management 最新的部分」；分析層對「最新」之讀法
即 (a)(b) 四條，已於 00 包報 Pei，Pei 未點名出入即為採認。
**待 recon 查證（不改本條）**：R-P368(a) 段 1 取 LID `Atlantis High` 欄組，而本線
SYSRA 之 EE Architecture 全為 ATL-Mi；LID v1_78 另有 `637MCA Specific Signals` 分頁
（22 列）與本線 DocID `VF665_V42_P637MCA` 對應。段 1 應取何欄組，recon 實測後另裁。

> **註記（R-TM13，2026-09-01，R-VL6）**：(b) 所引 R-P368 連帶承接 **R-P375**
> （段 1 入口擴為 forms/ 全部參考檔；`.Req` 設定值走 UI／PROXI 路徑）。
> 上段「待查」之欄組二擇一問題因之消滅，處置見 R-VL6(c)。
> 分析層於落 R-VL2 時未讀至 R-P375 即引 R-P368，記 A-VL2。

> **註記（R-TM13，2026-09-01，R-VL12）**：(b) 所承 R-P368 之段 1 `Atlantis High` 欄組與段 3 R1 DBC 為 **Atlantis High 之綁定**；
> 本線為 ATL-Mi，段 1 改取 `Atlantis` 欄組（P–T）、段 3 待 ATL-Mi DBC（R-VL12(a)(b)）。書寫格式 (a) 與 R-P353／R-P355／R-P375 不變。
> 上段「待 recon 查證」自此結案；分析層於落條時已識別 ATL-Mi 而未實測即承接 PM 綁定，記 A-VL10。

### R-VL3 —— Test Group／TC ID／交付檔名

```
R-VL3（Pei 裁定 2026-09-01，00 包待裁題 3：「3 准」）
Test Group（Layer 1）= `Vehicle Setup Management R1 Low`
TC ID = `NR1L-VSM42-{nnn}`（R-G42 二之 Pei 裁一次：037 req_id token `VC`
       已為 vehicle_category 所佔，有歧義）
交付檔名 = `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
           Specification & Result_SWQT_VehicleSetupManagementR1Low_{YYYYMMDD}.xlsx`
           （R-G42 五：{FeatureName} = Test Group 去空白，無其他尾綴）
```

依據：R-G42 三之「037 feature 全名」於本案不可直取 —— 037 檔名為散落子功能名
（Park Sense And Restore Default Setting／Side Distance Warning Audio Repetition），
故取規格題名；兩線同名則 `delivered/` 檔名撞名而 R-G42 五禁尾綴，
變體名入 Test Group 為唯一不開例外之解。

### R-VL4 —— 母體 = 037 Functional leaf；SYSRA 其餘 Functional 不入範圍

```
R-VL4（Pei 確認 2026-09-01，00 包待裁題 4：「4 無其他」）
本線 037 僅兩份（Park Sense And Restore Default Setting／Side Distance Warning
Audio Repetition），Pei 確認無其他 037 檔。
TC 生成母體 = 該兩份 037 之 Functional Requirement leaf，intake 實測 128
（68 ＋ 60）；Heading 列（13 ＋ 10）入覆蓋台帳標 No TC（R-BLM2 型）。
V42 SYSRA 之 Functional 318 列中未被 037 覆蓋之 190 列**不入本線範圍**，
不得以 SYSRA 直接生成 TC（RD 分解紀律 IN §8.2：037 為需求單位之權威）。
該 190 列以 DR-VL1 登記為覆蓋揭露，Pei 決定是否向上游查詢。
```

### R-VL5 —— 素材落點；spec_mode D 需 OOXML 原檔

```
R-VL5（Pei 裁定 2026-09-01，00 包待裁題 5：「5 准」）
投遞區 _intake/Vehicle_Setup_VF665/（TitleCase；R-G24，已建妥並 list_directory 實測）。
原檔落點 sources/raw/<doc_id>/，feature.yaml 以 doc_id 引用（R-G27；新 feature 不存
inputs/ 副本）。兩線共用之 SYSAD 一份、LID／DBC／PROXI 取 forms/，不重複存。
Claude Project 內之三份 docx 為文字抽取本，非 OOXML；spec_mode D 之抽取須自原檔
（R-P3′ magic bytes 判讀），故 Pei 須投遞原始 .docx。
```

> **作廢部分（R-TM13，2026-09-01，R-VL13(b)）**：`_intake/Vehicle_Setup_VF665/` 投遞區廢止，實然為 `features/<slug>/inputs/`。

### R-VL6 —— R-VL2(b) 加註：段 1 入口依 R-P375 擴為 forms/ 全部參考檔；多命中之處置

```
R-VL6（分析層裁定 2026-09-01，上繳 00 §9 未預期發現 (3)／§5 未預期發現 (2)；
      訂正分析層對 Pei「PM 最新」指示之窄讀，同 R-P375 之自訂正型）
(a) R-VL2(b) 所引 R-P368 連帶承接 R-P375(a)–(e)：三段鏈之段 1 入口為 forms/ 全部
    參考檔（LID 全分頁含 `637MCA Specific Signals`、HMI Settings List R1 SR25、
    PROXI_HDCC27_R3 `Format`、SR26 Default Settings、SR24 Market Configuration Table），
    每檔以 forms/FORMS.md 之 SHA 入台帳。
(b) R-P375(b)(c) 對本線尤要：`X.Req` 類設定值段 1 命中 HMI Settings List 者以 UI 元件寫
    （`Select "<設定名>" = "<值>"`），命中 PROXI `Format` 者寫 `PROXI <Param> = <值>`，
    二者皆命中時 Procedure 用 UI、Pre-Condition 用 PROXI；`X.Info` 類致能狀態依 (c)。
(c) 上繳 00 §5 之「`Atlantis High` 欄組 vs `637MCA Specific Signals` 分頁」不再是二擇一：
    二者皆為段 1 入口。同一規格原名於多處命中而解至同一 MESSAGE.Signal 者為同物，
    附表記全部命中處；解至不同 MESSAGE.Signal 者記 B-1 型衝突，列 §K 交 Pei（R-P369(b) 型）。
    命中即「候選」非認定（R-P375(d)），Remarks 標 `(DR-VL{n} 候選，待上游確認)`。
(d) R-VL2 原文不改，加註指向本條（R-TM13）。
```

### R-VL7 —— TC ID 鍵名採全庫慣例 `write_back.tc_id_format`

```
R-VL7（分析層裁定 2026-09-01，上繳 00 §1 未預期發現 (1)）
feature.yaml 落 `write_back.tc_id_format: "NR1L-VSM42-{n:03d}"`（沿 bed_lowering／amfm
之形制，`scripts/recon.py:1103` 所讀之鍵）。`tc_id_prefix` 鍵刪除，不保留 ——
一個無人讀之鍵即一個永不失敗之檢查（R-VC9）。R-VL3 之值不變。
```

### R-VL8 —— sandbox/ 與 R-G1 母本之時點；欄位自母本 r9 實測

```
R-VL8（分析層裁定 2026-09-01，上繳 00 §10-3）
(a) W-2 起始即建 `features/vsm_v42/sandbox/base/`，自 forms/ 之 R-G1 母本
    （`…_SWQT_20260817_ext.xlsx`，sha256 6372fb6b…825b2）以檔案複製（cmp 全等）
    落為工作副本；自始不得經 openpyxl 存回（R-G1 註／A-UP09：R 欄 x14 下拉會被摧毀）。
(b) `workbook.sheet`／`header_row`／`columns` 一律自該副本第 9 列表頭實測後回填；
    scaffold 模板值（`Test Case Specification&Result`、design_method Q、author Z）
    不得沿用。先驗（bed_lowering 自同 sha 母本實測）：sheet
    `Test Case Specification 測試用例規範`、priority P、estimated_test_time Q、
    design_method R、functional_safety S、author AA、test_version AB —— 為先驗，非免測。
(c) `done_region.author_value` 改 null（BLANK 無 done region，沿 R-BLM3 型）。
```

### R-VL9 —— `docs/fw036/RULINGS.sha.tsv` 之重生歸屬

```
R-VL9（分析層裁定 2026-09-01，上繳 00 §11 丁）
該台帳為全庫單一輸出檔，其夾帶他線之新增列屬結構性（檔頭自載）。
由 vsm_v42 之下一包（01）執行層跑一次 `python3 scripts/rulings_hash.py`，
夾帶 R-VT 五列不視為越禁區；vsm_v43 之包不再重生。
前提：Pei 先將現行 working tree（該檔已處 M）入庫，避免與他線交疊。
```

> **作廢（R-TM13，2026-09-01，R-VL13(a)）**：兩線並行時本條之 W-0 必被追平，重生改歸 Pei 提交前。

### R-VL10 —— 條文身分比 `body_sha8`；跨線計數改性質判準

```
R-VL10（分析層裁定 2026-09-01，上繳 01 第 0 節停下 2／3，第 13 節 2／3）
(a) 預期數字之「條文逐字相同」一律比 `rulings_hash.py` 之 `body_sha8`（fenced 本體）；
    `sha8`（錨點全區段）只作區段完整性觀測值，不作門檻。
    理由：R-TM13 加註屬常規動作，必動 `sha8` 不動 `body_sha8`；E18 比 `sha8` 則每次合法加註誤停一次。
    R-VL2 之 `sha8 = 582d0c6d` 為加註後之現值，非漂移。
(b) 凡預期數字之被數對象含他線產物（如台帳重生之新增列），改性質判準：
    「新增列之 ruling_id 全數 ∈ {R-VL*, R-VT*}，修改 0、刪除 0」，條數列為觀測值。
    E17 依此改寫。
```

### R-VL11 —— W-2 之 inputs/ 清空次序；欄位鍵全集；spec_reference_template 待 P3

```
R-VL11（分析層裁定 2026-09-01，上繳 01 第 10 節 4、第 7 節末註）
(a) inputs/ 之清空須在：落 `sources/raw/` ＋ 逐檔 sha256 前後全等 ＋ MANIFEST 落列 三者皆過之後；
    採 `mv` 而非 cp+rm，以免中途失敗時兩處皆無。
(b) `workbook.columns` 自副本 r9 實測回填時納 `tc_id`（F）與 `estimated_test_time`（Q）；
    上繳 01 第 7 節對 forms/ 母本之逐欄實測得採為先驗，副本仍須重測。
(c) `spec_reference_template` 落 null，待 P3 裁（VF 類母件之 IN §10.7 型態未定）；執行層自填之構造式不得進 recon。
```

### R-VL12 —— ATL-Mi 線之訊號解析綁定：段 1 取 LID `Atlantis` 欄組；段 3 待 ATL-Mi DBC；段 1 不適用之情形；抽名範圍

```
R-VL12（分析層裁定 2026-09-01，上繳 02 第 5.3 節／A-VL8，vsm_v43 上繳 03 §K K-1；訂正 R-VL2(b) 之分析層誤，A-VL10）
(a) 實測（LID v1_78 `CAN Mapping` r2 欄組表頭）：Powernet F–J／CUSW K–O／**Atlantis P–T**／Compact U–Y／
    **Atlantis High Z–AD**，為五個彼此獨立之欄組；兩欄組同列皆有值者 913，其中 589 列值不同。
    本線 EE Architecture = ATL-Mi（SYSRA 實測；V42 206 列、V43 1280/1280），交付本車型欄 V = `VF(ProMaster)637 Atl-Mi`。
    段 1 之 LID 欄組對本線一律取 **`Atlantis`（P–T）**；`Atlantis High`（Z–AD）只作旁證併記。
    佐證（vsm_v43 v3 實測）：CAN 形 93 名中 Atlantis 欄逐字命中 21、Atlantis High 10（且 10 ⊂ 21）；
    「訊息名不符(R-13)」28 列中 Atlantis 欄命中 6、Atlantis High 0（如 `TELEMATIC_SERVICE_SETUP.ClearPersonalDataReq`）；
    `TELEMATIC_VEHICLE_SETUP2.*`／`IPC_VEHICLE_SETUP3.*` 只見於 Atlantis 欄。
(b) 段 3：forms/ 之 `PDT27_E2A_R1_BHCAN2.dbc`／`R1_FDCAN8.dbc` 為 Atlantis High 之 DBC（PM 線之 R-P368 綁定），
    Atlantis 欄之 `CAN` 值為 CAN-B／CAN-C，非 FD／BH-CAN。本線段 3 須以 ATL-Mi 之 DBC（CAN-B／CAN-C）為之；
    forms/ 現無此件 → DR-VL3。到件前，任何 CAN 訊號不得記「解得」、不得寫 `$…$`；結果記「段3待ATL-Mi DBC」，
    並併記對 Atlantis High DBC 之實查結果為旁證。上繳 02 之「解得 35」與「訊息名不符 27」全數重判。
(c) 規格原名已為 `MESSAGE.Signal` 形者，段 1 之目的（邏輯名→實名）已達，記「段 1 不適用」；
    正確架構之 DBC 逐字查得（MESSAGE 與 Signal 皆合）即「解得」，得寫 `$…$`。此為對 R-P368(a)「三段皆過」之意旨讀法，
    跨線觀察記 PM。
(d) 抽名：CAN 形一律用通式 `[A-Z][A-Z0-9_]{3,}\.[A-Za-z]\w*`，不限 `_VEHICLE_SETUP` 家族（`STATUS_*`／`TBM_*`／`GLOB_LTM.*` 皆入）；
    同時報抽名偽陽性率。
(e) Functional Diagram 之流向不於 P3 文字化；P4 逐 TC 需驗因果方向時依圖判，圖為來源（R-G28 型），不臆測。
```

### R-VL13 —— 台帳重生歸 Pei 提交前一次；R-VL9 作廢；投遞區以 inputs/ 為實然

```
R-VL13（分析層裁定 2026-09-01，**Pei 追認 2026-09-02（「2 追認」）**；上繳 02 第 9 節乙、第 11 節 3／4）
(a) 兩線並行時任一包之 W-0 必被對方後續落檔追平（實測兩次：14→21、21→23）。
    改：執行層不重生 `docs/fw036/RULINGS.sha.tsv`；Pei 於每次 commit 前跑一次 `python3 scripts/rulings_hash.py` 併入庫。
    執行層 `gate_all` 之 rulings_hash 紅，若 diff 全為 R-VL*／R-VT* 新增列，於升級說明記「依 R-VL13 待 Pei 重生」即可上繳。
    R-VL9 作廢（不刪，加註）。
(b) 投遞區：實然為 `features/<slug>/inputs/`（gitignored），W-2 以 R-VL11(a) mv 至 `sources/raw/`。
    `_intake/Vehicle_Setup_VF665/` 廢止，由 Pei 刪除空目錄；R-VL5 作廢該句（加註）。
```

### R-VL14 —— 段 3 DBC 綁定：`Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`；DR-VL3 結案

```
R-VL14（分析層裁定 2026-09-02，Pei「1 放了」；分析層驗收後綁定）
(a) 本線段 3 之 DBC = `forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`
    （實測：BO_ 139／SG_ 5568／VAL_ 619；ISO-8859 編碼、CRLF —— 解析以 latin-1 讀）。
    Atlantis High 之 R1 BHCAN2／FDCAN8 對本線降旁證（R-VL12(b) 之「待件」自此結案）。
(b) 驗收（分析層實測）：爭議訊息全數在內 —— `TELEMATIC_VEHICLE_SETUP2`／`IPC_VEHICLE_SETUP2`／
    `IPC_VEHICLE_SETUP3`／`SERVICE_SETUP`／`TELEMATIC_SERVICE_SETUP`／`STATUS_CCAN3`（含 VehicleSpeedVSOSig）。
(c) 本件為 BH-CAN；LID Atlantis 欄 `CAN` 值為 CAN-C 者若段 3 查無，記「未解得（CAN-C DBC 未到件）」，
    實測後再議，不預開 DR（Pei 裁：先不送）。
(d) 「解得」自此合法：段 1 Atlantis 欄（或 R-VL12(c) 段 1 不適用）＋本 DBC 逐字 → 得寫 `$…$`，
    `<label>` 逐字取本 DBC 之 VAL_。DR-VL3 結案（到件，非送出）。
```

> **更正（R-TM13，2026-09-02，A-VL11）**：(a) 之 `SG_ 5568` 為字串出現數（含 `BA_` 屬性行），
> **訊號定義行實為 844（相異 794）** —— 分析層量測條件未揭露即入條文，與 A-VL4 同族（自誤）。
> 索引以行首錨定，BO_／VAL_ 兩數相符，件之真偽不受影響。A-VL11 RESOLVED。
> 另揭露：R-VL13 本體首行於 2026-09-02 由「待 Pei 追認」改「Pei 追認」（body_sha8 `6d382ff3`→`782082cf`），
> 為裁決者欄之狀態更新非條文語義變更，上繳 03 第 1 節所指即此。

### R-VL15 —— W-5 判準收尾：命中規則優先序；儲存格多值切分；R-VL13(a) 但書修訂；v3 為現行

```
R-VL15（分析層裁定 2026-09-02，上繳 03 §K、第 8 節甲、第 7 節 5；vsm_v43 上繳 04 A-VT24）
(a) 段 1 命中規則優先序：目標欄（Atlantis `Signal Name`／Specific Signals `Signal Name`／
    PROXI `Parameter Name`／HMI 設定名欄）之 R1 逐字命中，勝過名稱欄（LID A／B／C）之 R2–R6 命中；
    同強度方為 B-1。依此 K-1 解為 `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req`（目標欄逐字），
    `IPC_VEHICLE_SETUP.LanguageSelection` 為其 Sts 孪生對偶記備註；B-1 歸零。
(b) LID 儲存格內多值（換行、空白＋單引號）一律切分後逐字比，禁子串包含（vsm_v43 A-VT24 同裁，採 21）。
(c) R-VL13(a) 但書修訂：rulings_hash 紅之可上繳判準改「無刪除列，且既有列之 body_sha8 無變動」；
    新增列不限系列（他線合法落條如 R-VS* 亦屬之），sha8-only 變動（R-TM13 加註）亦屬合法。
(d) `signal_chain_v42_v3.tsv` 為現行版；v1／v2 留檔不合併不刪。
```

### R-VL16 —— 值域增「規格拼字疑誤」；非 CAN 形之「解得」須有段 1 依據；PassiveEntry 處置

```
R-VL16（分析層裁定 2026-09-02，上繳 03 第 7 節 3／4；vsm_v43 上繳 04 §八-2／-3、A-VT26）
(a) 結果值域增 `未解得（規格拼字疑誤）`：規格原名於正確拼法下於主 DBC 存在而原拼法查無者屬之。
    規格原名不改（R-13／R-6），備註記正確拼法與佐證位置，佐證掛 DR-VT2（不送，留檔）；
    P4 遭遇時該列寫保留原名不加 `$`。A-VL12 兩名改記此值，A-VL12 RESOLVED。
(b) 內部形（X.Req／X.Info／X.GUI）之「解得」須有段 1 依據（LID／HMI／PROXI 對照命中）；
    僅段 3 同名不算（R-P368 三段鏈之本旨：防同名跳接）。本線「解得 98」中非 CAN 形 3 列逐列審，
    無段 1 依據者退回「未解得(止於段1)」；vsm_v43 之 A-VT26 五列同裁（彼線 R-VT16(e)）。
(c) `IPC_VEHICLE_SETUP.PassiveEntry`／`TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req`：維持
    「未解得(止於段3)」，備註 LID 對映指向 `RFHUB3.RFReq`（他 ECU，本 DBC 查無）；不臆測、
    不代入；P4 遭遇時 PENDING（DR 不送，依 Pei 裁）。
```

### R-VL17 —— Layer 2 鎖定（十組，Pei「准」）

```
R-VL17（Pei 裁定 2026-09-02：「准」）
Layer 2 依 00 包 §九十組草案鎖定，leaf 實測對測相符（data/p3_families_v42.md，24 家族合計 128）：
Park Sense (18)／Camera Gridlines (10)／Lighting (11)／Speed Assist (21)／Driver Warning (13)／
Wiper and Sensor (5)／Units (15)／EPB Maintenance Mode (17)／Personal Data and Defaults (14)／
Time and Navigation (4)。全表見 framework.md（本包同時落檔）。
偏小組（#6、#10）照案保留。Layer 3 之規格章節號由執行層實測回填，回填不解鎖 Layer 2。
Pilot 提案 EPB Maintenance Mode（分析層，開跑前 Pei 可改指）。
```

### R-VL18 —— P3 收尾四裁：Distance 對映；拼字第三例方向；GenSigSendType 不得臆用；DECISIONS profile 欄歸分析層

```
R-VL18（分析層裁定 2026-09-02，上繳 04 第 11 節 1／2／4／5）
(a) `Distance` ↔ 規格 `1.11.1.1.10.5.1 Distances` 認定對映：單複數形態差＋結構證據
    （同層兄弟 10.5.2 Fuel Consumption 已逐字對映，父節 10 Units 與 Test Set 7 組成吻合）。
    E35 → 22／24；framework 回填由分析層為之。本裁限此一對，不立去複數通則。
(b) R-VL16(a) 第三例（`SVC_Gridlines_Req` vs DBC `SVC_Guidelines_Req`）：維持「規格拼字疑誤」值域，
    備註加註「疑 DBC 側誤（Gridlines 為攝影機領域正確用語）」；不分立值域。P4 同保留原名不加 `$`。
(c) `GenSigSendType`（1／3／7）列舉定義未查得前，不得據以決定 Procedure 之 Send／Hold 寫法；
    P5 包 W 項令查兩本 ATL-Mi DBC 之 `BA_DEF_` 列舉，查無則 Procedure 只依規格行為書寫，表僅參考。
(d) DECISIONS 之 `profile [OVERRIDE] clauses` 欄由分析層填（profiles/ 屬分析層）：本線無 OVERRIDE，
    [ADD §8.7.5] 八項見 FW036_R1L_VSM_V42_Profile.md。
```

### R-VL19 —— spec_reference 型態（VF 類母件）；無章節家族之錨

```
R-VL19（分析層裁定 2026-09-02，依 Pei「皆授權」進 P4 之前置；pilot 覆核時 Pei 併驗）
(a) 主錨依 IN §10.7(b) 型：`Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_{章節號}`
    （檔名底線 token 化，括號去除；全案逐字一致），一章節號一行，前綴逐行重述，升冪。
(b) 無規格章節可錨之家族（Rear／Front Park Sense Volume，13 leaf）以上游實名錨：
    `Sys-RA-VF665_V42_VSM-{nnn}`（該 leaf 之 Source Requirement ID，逐列實取），一 ID 一行；
    Remarks 註「規格無章節標題（上繳 04 W-8 實測）」。`-063`（Source 為 Heading）同法並註 DR-VL2(c)。
    ~~前提「無節可錨」~~ **加註（R-VL26(g)，2026-09-02）**：上繳 11 實測該二家族逐字段落
    實在節 1.11.1.1.29 內（段 1216–1241，非 heading 樣式故不入 outline）——「無標題」成立、
    「無節」不成立（分析層之誤，A-VL15(2)）。改雙錨：`…_1.11.1.1.29` 加列在前、
    Sys-RA 實名保留在後（三家族共節，Sys-RA 保逐需求追溯）。
(c) 同具兩型錨者 spec 錨在前、Sys-RA 錨在後（家族排序比照 IN §10.7 SWC 基準之精神）。
Test Set 9 之雙章節家族（1.11.1.*＋1.11.2.*）兩章節皆列，各一行。
```

### R-VL20 —— DECISIONS 簽核代記；P4 開跑（pilot = EPB Maintenance Mode）

```
R-VL20（Pei 裁定 2026-09-02：「皆授權」）
DECISIONS 四欄簽核，分析層代記「Pei 授權 2026-09-02」。P3 完成，進 P4。
pilot = EPB Maintenance Mode（17 leaf，R-VL17 提案未改指即用）；
pilot 產出先落 generated/（文字形，IN §10 十鍵），寫回工作簿待分析層覆核與 Pei 再授權（PM 站式）。
```

### R-VL21 —— pilot 覆核裁定：二裁題皆准；四項處置追認；兩類修訂（REV-1〜4）

```
R-VL21（分析層裁定 2026-09-02，pilot b1 逐 TC 覆核；實檔抽驗 -046／-048／-051 逐字）
(a) 【裁題 1，准】UI 元件名得取自規格／037 具名之選單項／popup 文字（來源入 remarks）；
    HMI Settings List 錨點優先，無錨不降 PENDING —— 規格具名即非臆造（§8.4.1）、可執行即非 PENDING（R-P355(c) 本旨）。
(b) 【裁題 2，准】-046 一條不拆：IN §5.7 字面「一觸發多同時結果屬同一 TC」，多階段 ER 正確；不重做。
(c) 追認：VAL_ 缺值寫 `= <raw>` 不附 label＋remarks 揭露（§8.4.1）；同文兩碼各一條＋括號區分（§8.2.2／R-S4）；
    -059 ignition 分支揭露未涵蓋不臆造（037 佔位符 `{S}` 殘留入 DR-VL2 佐證，不送）；
    test_item 上半得取 037 Requirement Description 為 verbatim 來源（RD 權威單位；規格拼字瑕疵時尤然），spec_reference 指回規格段。
    GenSigSendType 列舉查得（OnWrite=1／OnChange=3／NoSigSendType=7），R-VL18(c) 臆用禁令解除，Procedure 仍只依規格行為。
(d) 【REV-1，-046】步驟 4 `Hold for 35000 ms` 之 ER「The T_EPB_MM timer is held」不可觀察（timer 為內部態，違 §6）：
    刪該步，reasoning 註「T_EPB_MM 之到期效果由 -053 驗（§8.2.1 委任）」；若規格明載等候期間 popup 持續，
    得以「Initializing popup remains displayed」代之（逐字有據才寫）。
(e) 【REV-2，-046】ER 未涵蓋 test_item 明載之「setting status → On」（§6 完整性）：補一 ER（UI 設定狀態顯示 On）；
    ER1「registered without a bus error」為測試員送出之確認式，本條為 DUT 送出，刪 ER1 留「is received」式。
    另 test_item 上半「TLM receives」與 TC 方向（TLM 送出）之表面矛盾，reasoning 補一句方向註記（依 DBC）。
(f) 【REV-4，系統性，Fdbk 族 9 條】缺「已發起進入／退出請求」之 setup：popup 文義為「user selected Yes … but …」，
    直接送 Fdbk 而未建立請求態屬 FF 風險（§7）；該態為步驟控制態不得入 Pre-Condition（§4.4）。
    修：Procedure 前置發起步（Select "EPB Maintenance Mode" = "On"／退出側同理）再送 Fdbk；ER 1:1 同步。
    另：測試員自送訊號後之「Read … check it is <raw>」回讀步削去（冗餘，非錯但不加值），保留者不判錯。
修訂範圍：-046 一條（d／e）＋Fdbk 族 -048〜-052、-054〜-057 九條（f）；其餘七條不動。
```

### R-VL22 —— 修訂輪覆核：-053 併修；K-5／K-6 處置；-046 design_method

```
R-VL22（分析層裁定 2026-09-02，上繳 06）
(a) E50↔E46 之衝突：**-053 併修**（一列，照 REV-2 同型：DUT 送出步之 bus-error 式改 is received 式）。
    衝突肇因在分析層：R-VL21 修訂範圍以條列而非以缺陷型掃全批（同型缺陷應 grep 全 17 條再劃範圍），
    記分析層之誤；執行層守明文不自調和正確。往後修訂包之範圍一律附同型全批掃描式。
(b) K-5 追認：退出側發起步 ER 只斷言 UI 設定狀態，不斷言 `Req = 0 (Off)` 送出（規格未載，寫即造，§8.4.1）；
    執行層拒照 fallback 字面辦正確（其前提「有據」不成立）。退出請求機制未載屬規格缺口，
    入 DR-VL2 佐證（加註，不送），交付說明揭露。
(c) K-6：-054（Fdbk = 8）歸屬依規格段逐字三分類 —— 該段及其鄰句含 entering／exiting／request 詞則依詞歸側；
    皆無則判 **in-mode 狀態回報型**：刪發起步，Pre-Condition 維持「已在 Service Mode（$IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ = 1 (On)）」，
    直接注入 Fdbk = 8。量測後定，不猜。
(d) -046 之 design_method 改「功能測試」（§12 tie-break：3 步單一功能）。
(e) 本輪後 b1 凍結；寫回工法包次之（含 x14 DV 保全查證），b2 批次序待 Pei。
```

### R-VL23 —— E56 之 -059 走 A 路；首跑檢查但書；-054 前置合規；凍結定義

```
R-VL23（分析層裁定 2026-09-02，上繳 07）
(a) -059 走 **A 路**：授權外加修一列 —— test_item 上半改完整原句 verbatim（含 ignition 子句，42 token 過 R-3），
    ignition 分支未涵蓋之揭露維持於 reasoning／remarks（§8.2.1 委任式）。句內剪接違逐字紀律，
    帶違規凍結之成本高於現修；執行層不進凍結而交裁，正確。
(b) 範圍但書採：**首跑之新檢查所揭缺陷自動入同包修訂範圍**，要件為同型全批掃描式＋逐列 diff 上繳；
    非首跑檢查仍守明列範圍（R-VL22(a)）。
(c) -054 之 Pre-Condition 訊號值前置合 §4.4（feature initial state 得以訊號值表達；非步驟控制態 ——
    進入 Service Mode 非本 TC 所驗之因果）；不改。
(d) 凍結定義：E56 = 17／17 後執行層於 INDEX 記「b1 FROZEN (R-VL23)」；此後任何變更須新裁決。
```

### R-VL24 —— 寫回工法定案；三欄依交付本實測；b1 內容 dry-run 准

```
R-VL24（分析層裁定 2026-09-02，上繳 09）
(a) 工法定案：openpyxl 計算層＋`backend.xlsx_surgical.surgical_save` 出件（試驗 C 實證；
    試驗 A 證 openpyxl 連不改值存檔都掉 x14，禁用）。出件後強制 zipfile 直讀複驗（x14 逐字、
    member 集合、differing 僅目標分頁）＋回讀驗證；交付候選以 copy2＋sha256 相等產出（popup 式）。
    單次約 120 秒記入工程預期，不入迴圈。
(b) Q／V（車型欄）／AB 三未裁欄：依格式權威硬規則 —— 先實測 Pei 既交付工作簿（至少
    vehicle_setting／popup／power 三本 delivered）之該三欄實際值分布，照慣例填；
    無一致慣例則留空並報。不憑空設計。
(c) b1 實內容 dry-run 准（執行層 §7-4 建議採）：建 `wb_trial/trial_D_b1.xlsx`（b1 實內容、
    surgical 出件）並 lint 實跑 —— P／I-cross／W 現形，紅項逐項歸因交裁；此為寫回前提。
(d) wb_trial 試驗檔保留至寫回執行包結案。
(e) 正式寫回（sandbox/b1/）與交付候選：待 dry-run 全綠（或紅項裁畢）後由 Pei 再授權（R-VL20）。
```

### R-VL25 —— b2 批次序准；寫回預授權（條件式）

```
R-VL25（Pei 裁定 2026-09-02：「准 准 寫」之後二字；條文分析層記）
(a) b2 批次序准：依 framework 表順 —— Park Sense 18 → Camera Gridlines 10 → Lighting 11 →
    Speed Assist 21 → Driver Warning 13 → Wiper and Sensor 5 → Units 15 →（EPB 已完）→
    Personal Data and Defaults 14 → Time and Navigation 4。三批乾淨（覆核零修訂）後綠色通道：
    後續批自動連跑、上繳彙報式覆核。
(b) 寫回預授權（「寫」）：dry-run E80 = 0 則寫回執行包直接開跑（寫至 sandbox/b1/＋lint 實跑
    全綠＋交付候選 copy2＋sha256 產出），不再往返；E80 > 0 則紅項回分析層裁畢方寫。
    交付（delivered/）仍待 Pei「出貨」。
```

### R-VL26 —— dry-run 與 b2 合裁：-057 解凍一列；D／C 欄依交付慣例對調；lint P 豁免／I-cross 基線；Volume 雙錨；K-7／K-8

```
R-VL26（分析層裁定 2026-09-02，上繳 10＋11）
(a) -057 hedge `successfully`：解凍修一列（括號下半改 `(Fdbk = 11: exit process reported as
    complete)`）後重凍；hedge（C 型）掃描入兩線固定自檢（b2 已納，實測 0）。
(b) D／C 欄依交付慣例對調：**D = SWE-Requirement ID（`SWE1-VC-…-{nnn}`），C 空**（四本交付簿
    1,033 列實測一致）。下放包 05 之反向指令為分析層未先實測交付本即定映射之誤（A-VL15(1)，
    違 R-1 格式權威硬規則）。writeback_map_b1.tsv 對調；Sys-RA 實名不入 D，其出現處為
    spec_reference（R-VL19(b) 雙錨）與 leaves.tsv。vsm_v43 不受影響（無 037，Sys-RA 即需求 ID；
    037 到件重錨時自然轉 SWE ID 合慣例）。
(c) lint 檢查 P 豁免：DBC 無該值 VAL_ 者認列已裁例外（R-VL21(c)，以 remarks 揭露為要件）；
    豁免清單落 `data/lint_p_waivers_b1.tsv`（11 賦值＋依據），寫回後 lint 之 P 紅以清單對銷；
    lint P 判準補丁（「DBC 無 VAL_ 者免附」）入共用腳本一裁清單（Pei）。
(d) I-cross：本線 ER 為即時觀察式不採觀測窗書寫，「窗未宣告」×N 視為預期基線非紅
    （該檢查自載警示器非判準）；入 profile [ADD]（分析層後補）。
(e) Q／AB／車型七欄留空、S = NA、E 留空採認（1,033 列實測）；樣本代換採認。
(f) dry-run 工法全數採認（E79 四斷言＋286 格回讀 0 不符；成本與改動格數無關得證）。
(g) b2 Park Sense 覆核：Volume 13 條 spec_reference 改雙錨（R-VL19(b) 加註，A-VL15(2)）；
    K-7：-002／-006 維持兩條（§8.2.2 逆向禁止），-006 remarks 註疑上游贅列入 DR-VL2 佐證；
    -008／-015 之規格條件實質不同採認；K-8：認定 `CAN node 24 (PAM )` 與 PROXI
    `CAN node 24 (PAM/CVADAS)` 為同一參數（值域相符＋表內唯一 node 24），R-13 保留規格原名、
    實名於 remarks 採認；檔名 `/`→`_`、Med／Medium 處置（步驟 DBC、上半 verbatim）採認。
    本批修訂僅錨層（13 條 spec_ref＋-006 remarks）且肇因分析層，**仍計綠色通道 1／3**，
    惟修訂輪須零它項。
(h) 寫回執行：(a)(b)(c) 落地後 b1 依 Pei「寫」預授權（R-VL25(b)）直接寫至 sandbox/b1/＋
    lint 實跑（預期 C=0、P 對銷後 0、U=6 計數、I-cross 基線）＋交付候選 copy2＋sha256 產出，
    停於待「出貨」。b2 寫回待其修訂輪完成後併批。
```

### R-VL27 —— 寫回包採認；E86′ 取代；R-VL15(c) 他線但書；wb_trial 保留；綠色通道 1／3 確認

```
R-VL27（分析層裁定 2026-09-02，上繳 12）
(a) E89–E93 採認；b1 寫回成立（三斷言＋269 格回讀 0 不符＋lint 淨紅 0），交付候選
    `sandbox/b1/candidate_vsm42_b1.xlsx`（sha256 abc7f8ae…）待 Pei「出貨」。
(b) E86 原判準由 **E86′**（雙錨結構：Volume 13 條 2 元素、首章節號次 Sys-RA）取代；
    修訂計數口徑定為 req_id 計（檔數並列）。
(c) R-VL15(c) 加但書（加註不刪）：既有列 body_sha8 變動**屬他線條文者不計**（歸因只及本線之列）；
    R-VF83 為 vehicle_setting 合法修訂，放行。
(d) wb_trial 六件結案裁保留（dry-run 證據鏈，sandbox 合法落點；交付後隨 tag 存查，不刪）。
(e) 綠色通道 1／3 確認（b2 重跑零它項，E90 全過）。b2 寫回待後續批累積併批。
(f) b2-2 = Camera Gridlines 10 leaf 開跑。
```

---

## 取號紀錄

| 條號 | 落檔日 | 取號依據 |
|---|---|---|
| R-VL1–R-VL5 | 2026-09-01 | 本檔新建，全庫 `R-VL` 系列實測未佔（`RULINGS_LEDGER.md`／FO 內 grep 命中 0） |
| R-VL6–R-VL9 | 2026-09-01 | 落檔當下讀本檔實測至 R-VL5；上繳 00 §9 之 sha 表亦止於 R-VL5 |
| R-VL10–R-VL11 | 2026-09-01 | 上繳 01 第 9 節 sha 表止於 R-VL9；本檔錨點實測 9 |
| R-VL12–R-VL13 | 2026-09-01 | 上繳 02 第 0 節 sha 表止於 R-VL11；本檔錨點實測 11 |
| R-VL14 | 2026-09-02 | 本檔錨點實測 13 |
| R-VL15–R-VL16 | 2026-09-02 | 上繳 03 第 1 節 sha 表止於 R-VL14；本檔錨點實測 14 |
| R-VL17 | 2026-09-02 | 本檔錨點實測 16 |
| R-VL18–R-VL20 | 2026-09-02 | 上繳 04 第 6 節 sha 表止於 R-VL17；本檔錨點實測 17 |
| R-VL21 | 2026-09-02 | 本檔錨點實測 20 |
| R-VL22 | 2026-09-02 | 上繳 06 第 8 節 sha 止於 R-VL21；本檔錨點實測 21 |
| R-VL23 | 2026-09-02 | 上繳 07 第 8 節 sha 止於 R-VL22；本檔錨點實測 22 |
| R-VL24 | 2026-09-02 | 上繳 09 第 8 節 sha 止於 R-VL23；本檔錨點實測 23 |
| R-VL25 | 2026-09-02 | 本檔錨點實測 24 |
| R-VL26 | 2026-09-02 | 上繳 11 第 7 節 sha 止於 R-VL25；本檔錨點實測 25 |
| R-VL27 | 2026-09-02 | 上繳 12 第 7 節 sha 止於 R-VL26；本檔錨點實測 26 |
