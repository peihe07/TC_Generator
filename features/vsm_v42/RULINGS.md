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
R-VL13（分析層裁定 2026-09-01，待 Pei 追認；上繳 02 第 9 節乙、第 11 節 3／4）
(a) 兩線並行時任一包之 W-0 必被對方後續落檔追平（實測兩次：14→21、21→23）。
    改：執行層不重生 `docs/fw036/RULINGS.sha.tsv`；Pei 於每次 commit 前跑一次 `python3 scripts/rulings_hash.py` 併入庫。
    執行層 `gate_all` 之 rulings_hash 紅，若 diff 全為 R-VL*／R-VT* 新增列，於升級說明記「依 R-VL13 待 Pei 重生」即可上繳。
    R-VL9 作廢（不刪，加註）。
(b) 投遞區：實然為 `features/<slug>/inputs/`（gitignored），W-2 以 R-VL11(a) mv 至 `sources/raw/`。
    `_intake/Vehicle_Setup_VF665/` 廢止，由 Pei 刪除空目錄；R-VL5 作廢該句（加註）。
```

---

## 取號紀錄

| 條號 | 落檔日 | 取號依據 |
|---|---|---|
| R-VL1–R-VL5 | 2026-09-01 | 本檔新建，全庫 `R-VL` 系列實測未佔（`RULINGS_LEDGER.md`／FO 內 grep 命中 0） |
| R-VL6–R-VL9 | 2026-09-01 | 落檔當下讀本檔實測至 R-VL5；上繳 00 §9 之 sha 表亦止於 R-VL5 |
| R-VL10–R-VL11 | 2026-09-01 | 上繳 01 第 9 節 sha 表止於 R-VL9；本檔錨點實測 9 |
| R-VL12–R-VL13 | 2026-09-01 | 上繳 02 第 0 節 sha 表止於 R-VL11；本檔錨點實測 11 |
