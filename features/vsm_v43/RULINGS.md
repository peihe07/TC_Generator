# RULINGS — Vehicle Setup Management R1L TBM（VF665 V43）

Feature slug：`vsm_v43`。條號系列 **`R-VT`**（本線單一來源，R-G23 live 取號）。
姊妹線 `vsm_v42`（`R-VL` 系列）為獨立 feature；兩線互不引用對方條號作為依據，
共用者一律引 canon（IN／FO／`RULINGS_LEDGER.md`）或 PM 之 `R-P` 條文。

裁決者標示：**Pei** = Tier 3 裁定；**分析層** = Tier 2 於 Pei 授權範圍內之裁定。
歷史條文不刪，修訂加註（R-TM13）。

---

### R-VT1 —— 獨立 slug；工作簿自 BLANK 起建

```
R-VT1（Pei 裁定 2026-09-01，00 包待裁題 1：「1 准」）
VF665 V43（Vehicle Setup Management by VP - LTM (R1L) with TBM）立為獨立 feature，
slug = vsm_v43，自有 RULINGS／ANOMALIES／DATA_REQUESTS／feature.yaml／
framework.md／docs/{handoff,upstream}/。
不併入 features/vehicle_setting/，不與 vsm_v42 共用任何工具、資料檔或條號。
工作簿自 BLANK ＋ R-G1 模板起建，不沿用任何既有 036 本。
```

依據：R-BLM1／R-VC1 先例；`vehicle_setting/CROSSLINE.md`（A-VF8／A-VF9／A-VF30）所載
兩線共目錄之代價。V43 ↔ V42 之 Functional 描述逐字重疊實測僅 30／398（V43 側）。

### R-VT2 —— 訊號書寫依 canon §8.7.5 v3 ＋ PM 現行條文；不承襲 R-VS52

```
R-VT2（Pei 裁定 2026-09-01，00 包待裁題 2：「2 准」）
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
      R-P355  內部訊號不得直接 Set；尚無 DBC 對照者 `PENDING: DR-{n} <訊號名>`
      R-P368  訊號實名依 forms/ 三段鏈（LID v1_78 → MESSAGE.Signal →
              forms/PDT27_E2A_R1_BHCAN2.dbc／R1_FDCAN8.dbc）；R4／R5 DBC 降旁證
(c) lint 檢查 P 對本線以 `--profile vsm_v43` 走 v3 判準。
(d) input_test_data 一律 NA，資料內聯至 pre_conditions／test_procedure（IN §4.5）。
```

依據：Pei 原話「訊號寫法要遵照 power management 最新的部分」；分析層之讀法即 (a)(b)，
已於 00 包報 Pei，未點名出入即為採認。
**待 recon 查證**：本線 SYSRA EE Architecture 全為 ATL-Mi（1280/1280），R-P368(a) 段 1 之
LID 欄組適用性與 `vsm_v42` 同題，recon 實測後另裁。

> **註記（R-TM13，2026-09-01，R-VT6）**：(b) 所引 R-P368 連帶承接 **R-P375**，欄組二擇一問題消滅，
> 處置見 R-VT6。分析層引用未讀至 R-P375，記 A-VT5。

### R-VT3 —— Test Group／TC ID／交付檔名

```
R-VT3（Pei 裁定 2026-09-01，00 包待裁題 3：「3 准」）
Test Group（Layer 1）= `Vehicle Setup Management R1L TBM`
TC ID = `NR1L-VSM43-{nnn}`（R-G42 二之 Pei 裁一次；037 token `VC` 已為 vehicle_category 所佔）
交付檔名 = `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
           Specification & Result_SWQT_VehicleSetupManagementR1LTBM_{YYYYMMDD}.xlsx`
```

依據同 `vsm_v42` R-VL3 之理由（兩線同名則 `delivered/` 撞名，R-G42 五禁尾綴）。

### R-VT4 —— 037 = 0：本線止於 P0–P3，TC 生成待 037

```
R-VT4（Pei 確認 2026-09-01，00 包待裁題 4：「4 無其他」）
現有 037 兩份之 Source Requirement ID 全為 V42（152/152），本線 037 = 0；
Pei 確認無其他 037 檔。
依 IN §8.2（037 為需求單位之權威）與 R-VS15／R-BLM2 先例（母體自 037 取），
本線無母體，TC 生成不得以 SYSRA 或規格直接代之。
本線之作業止於 P0 intake／P1 recon／P2 DECISIONS／P3 framework 與 profile，
P4 以後待 037 到齊。DR-VT1 登記並建議送出（阻塞型）。
```

### R-VT5 —— 素材落點；spec_mode D 需 OOXML 原檔

```
R-VT5（Pei 裁定 2026-09-01，00 包待裁題 5：「5 准」）
投遞區 _intake/Vehicle_Setup_VF665/（與 vsm_v42 共用投遞區，落點分開；R-G24 已建妥實測）。
原檔落點 sources/raw/<doc_id>/，feature.yaml 以 doc_id 引用（R-G27）。
SYSAD 一份兩線共引；LID／DBC／PROXI 取 forms/。
Project 內 docx 為文字抽取本；spec_mode D 之抽取須自原檔，Pei 須投遞原始 .docx。
```

### R-VT6 —— R-VT2(b) 加註：段 1 入口依 R-P375 擴為 forms/ 全部參考檔；多命中之處置

```
R-VT6（分析層裁定 2026-09-01，上繳 00 §九-6；訂正分析層對 Pei「PM 最新」之窄讀）
(a) R-VT2(b) 所引 R-P368 連帶承接 R-P375(a)–(e)：段 1 入口為 forms/ 全部參考檔
    （LID 全分頁含 `637MCA Specific Signals`、HMI Settings List R1 SR25、PROXI_HDCC27_R3 `Format`、
    SR26 Default Settings、SR24 Market Configuration Table），每檔以 forms/FORMS.md 之 SHA 入台帳。
(b) `X.Req` 類設定值依 R-P375(b)走 UI／PROXI 路徑；`X.Info` 類致能狀態依 R-P375(c)。
(c) 同一規格原名多處命中而解至同一標的者為同物，附表記全部命中處；解至不同標的者記 B-1 型衝突
    交 Pei（R-P369(b) 型）。命中即候選非認定（R-P375(d)）。
(d) R-VT2 原文不改，加註指向本條。
```

### R-VT7 —— TC ID 鍵名採全庫慣例 `write_back.tc_id_format`

```
R-VT7（分析層裁定 2026-09-01，A-VT2）
feature.yaml 落 `write_back.tc_id_format: "NR1L-VSM43-{n:03d}"`；`tc_id_prefix` 鍵刪除，不保留（R-VC9）。
R-VT3 之值不變。A-VT2 依本條 RESOLVED，其根因為分析層之誤（A-VT5）。
```

### R-VT8 —— `docs/fw036/RULINGS.sha.tsv` 本線不重生；sandbox 與欄位從 R-VL8 同法

```
R-VT8（分析層裁定 2026-09-01，上繳 00 §八／§九-5）
(a) 台帳重生由 vsm_v42 之 01 包執行一次（其 R-VL9），本線包不重生；本線 sha8 自重生後之台帳讀取回報。
(b) 工作簿：W-2 起始建 `features/vsm_v43/sandbox/base/`，自 forms/ R-G1 母本（sha256 6372fb6b…825b2）
    檔案複製，不經 openpyxl 存回；`workbook.*` 自副本 r9 實測回填，模板值不得沿用。
    先驗（同 sha 母本實測）：priority P、estimated_test_time Q、design_method R、functional_safety S、
    author AA、test_version AB。
(c) `spec_reference_template` 落 null，待 P3 裁（VF 類母件之 IN §10.7 型態未定）。
```

### R-VT9 —— B-1 之定義收斂；訊息名不符者依 R-13 保留規格原名；兩本 DBC 各解一處者先查 LID 匯流排

```
R-VT9（分析層裁定 2026-09-01，上繳 01 §七 7.4 §K 29 列、A-VT12）
(a) B-1 型衝突僅限 R-VT6(c) 字面：同一規格原名多處命中而解至不同 MESSAGE.Signal。
    「段 3 之 SG_ 所屬 BO_ 與規格訊息名不符」（上繳 01 型態一 22 列、型態二 6 列）**非 B-1**，
    屬 IN §8.7.5(g)（R-13）之「規格訊號名與 DBC 不符」：結果欄記「訊息名不符(R-13)」，
    保留規格原名（不得代以 DBC 之他訊息名），段 3 命中處記為旁證，候選非認定（R-P375(d)），
    向上游查 DBC 版次與規格版次之對應（DR-VT3）。本線尚無 TC，不生 PENDING 佔位。
(b) 型態三（兩本 DBC 各解一處，如 BRAKE1.VehicleSpeedVSOSig → BHCAN2:STATUS_CCAN3 ＋ FDCAN8:BRAKE_FD_2）：
    先查 LID 段 1 命中列之 `CAN` 欄（匯流排）；LID 載明者取該匯流排之 DBC，另一本記旁證；
    LID 未載或規格原名未入 LID 者才列 §K 交 Pei。可以查表解者不升級。
(c) E15 依此重判：B-1 預期 0；「訊息名不符(R-13)」列數為觀測值。上繳 01 之停 2 依本條解除。
```

### R-VT10 —— 條文身分比 body_sha8；E2／E9 判準修正；W-5 之標籤與重做條件

```
R-VT10（分析層裁定 2026-09-01，上繳 01 §五 5.2、A-VT10／A-VT11／A-VT13、§十-1／-2）
(a) 預期數字之「條文逐字相同」一律比 body_sha8；sha8 為觀測值（同 vsm_v42 R-VL10(a)）。
    R-VT2 sha8 `671c5b72` 為 R-VT6(d) 加註後之現值，非漂移；停 1 解除。
    台帳無 R-VT 列前，樹外 `--out` 量測為合法替代來源（A-VT13 裁可）。
(b) E2：「Functional」指 `Functional Requirement` 逐字全等；計數 507 相符，A-VT10 RESOLVED。
    E9：原預期「4」為分析層 `most_common(4)` 之誤讀（A-VT14）；以上繳 01 之實測為基線：
    Functional 507 列內正規化後非空相異值 56（`verified by in-vehicle testing` 47）。A-VT11 RESOLVED。
(c) `signal_chain_v43.tsv` 之「查無(R-G13)」102 列標籤改「未解得(止於段1)」；
    「查無(R-G13)」僅於三要件皆滿足且已登 forms/LOOKUP_MISSES.md 時用。
(d) W-5 重做條件（02 包 W-5′）：① PROXI 與 .Req 另自 docx 表格結構（<w:tbl>）抽；
    ② 段 1 施作 R-P368(b) 擴充比對（LID Logical Identifier／Description 欄，容許前後綴／底線差異），
      每一擴充命中另欄記比對依據；③ 重算結果分布，181 名視為下界。
(e) #1 docx 之 `word/media/image1.wmf`：列 P3 待辦，於 framework 鎖定前轉圖一看；不施作 R-G28 二欄表。
```

### R-VT11 —— 段 1 擴充比對之對象欄與對象檔；OOXML 抽取自驗

```
R-VT11（分析層裁定 2026-09-01，上繳 02 §二-2 回報、§八-2、A-VT15）
(a) LID v1_78 無 `Description` 欄（實測表頭：Logical Identifier | Function | Object Text | Arch Basis | …）。
    R-P368(b) 所稱「Description 欄」於本線讀作 `Function` 與 `Object Text` 二欄；擴充比對對象為
    `Logical Identifier`／`Function`／`Object Text` 三欄，每一命中記欄名。
    此為跨線觀察：R-P368(b) 之字面與 LID 實檔不符，PM 線之核對由 PM 線自為，本線不動其檔。
(b) 擴充比對之對象檔自 LID 擴及 `HMI Settings List R1 SR25`（設定項名欄）與 `PROXI_HDCC27_R3` `Format`
    （參數名欄）；四規則不變，另加第五條：去 `_Menu`／`_Setting` 後綴（僅對 HMI Settings List 與 PROXI）。
    理由：上繳 02 PROXI 49 名含多個明顯 HMI 設定項而 HMI Settings List 命中 0，係比對未施於該檔所致。
(c) `.` 分隔符變體不採（實測僅 +1）；內部訊號之解析不走正規化放寬，走 R-P375(b)(c) 與 DR-VT4。
(d) 凡以正則讀 OOXML 者，抽完即斷言輸出不含 `</?w:`（A-VT15 之防再犯）。
```

### R-VT12 —— R-VT9(b) 但書：規格自載之兩條弧線不得合併；HU 所在匯流排依 SYSAD；母體可變之指標採同母體差

```
R-VT12（分析層裁定 2026-09-01，A-VT16／A-VT17）
(a) 規格同時載有 `BRAKE1.VehicleSpeedVSOSig`（VF408→BCM）與 `STATUS_CCAN3.VehicleSpeedVSOSig`（BCM→LTM）
    二名者，為兩個規格原名、兩條弧線，各自解析，不得以一方為他方旁證。R-VT9(b) 之「另一本記旁證」
    僅適用於規格只載一名而兩本 DBC 各解一處之情形。
(b) TC 之刺激／觀察目標取 HU（LTM）所在匯流排之那一弧；LTM 於 ATL-Mi 之網路位置自 SYSAD（SYS3）之
    網路拓撲節實測後定，未定前兩弧皆記「解得」不標主旁。此為 LID `Atlantis High` 欄組適用性一題之重現，
    解法在 SYSAD 而非 LID。
(c) 母體會變之指標（如 E16）一律以同母體差或比率表述，不沿用絕對閾值；E16 依同母體 97 < 102 判相符，
    全母體 113 為觀測值。A-VT17 RESOLVED。分析層同包並命「擴充母體」與「< 102」之誤記 A-VT18。
```

> **作廢部分（R-TM13，2026-09-01，R-VT13(c)）**：(b)「依 SYSAD」作廢 —— SYSAD 為 AOSP 軟體架構文件（A-VT19）；
> HU 匯流排依 LID `Atlantis` 欄組之 `CAN` 值。「解法在 SYSAD 而非 LID」一句為分析層誤判（A-VT22）。

### R-VT13 —— ATL-Mi 線之訊號解析綁定：段 1 取 LID `Atlantis` 欄組；段 3 待 ATL-Mi DBC；K-1／A-VT16／DR-VT3 依此重判

```
R-VT13（分析層裁定 2026-09-01，上繳 03 §K K-1、A-VT16、A-VT12／DR-VT3；訂正 R-VT2(b) 之分析層誤，A-VT22）
(a) 同 vsm_v42 R-VL12(a)：LID v1_78 `CAN Mapping` 有獨立欄組 `Atlantis`（P–T）與 `Atlantis High`（Z–AD），
    本線 EE = ATL-Mi（1280/1280），段 1 一律取 `Atlantis` 欄組，`Atlantis High` 只作旁證。
    實測（分析層，v3 TSV × LID）：CAN 形 93 名 Atlantis 欄逐字命中 21、Atlantis High 10（10 ⊂ 21）；
    R-13 28 列 Atlantis 命中 6、Atlantis High 0；段 2 待解 13 列 Atlantis 命中 7。
(b) 段 3：forms/ R1 DBC 為 Atlantis High 之件，本線需 ATL-Mi CAN-B／CAN-C DBC → DR-VT5（與 vsm_v42 DR-VL3 同件）。
    到件前 CAN 訊號一律「段3待ATL-Mi DBC」，不得記「解得」、不得寫 `$…$`；v3 之「解得 41」重判。
(c) K-1 結案：LID Atlantis 欄 `Speedometer` 列為 `STATUS_CCAN3.VehicleSpeedVSOSig`（無 `BRAKE_FD_2`），
    即 ATL-Mi 之 LTM 觀察面為 `STATUS_CCAN3.*`（BCM→LTM 弧），`BRAKE1.*` 為上游弧。A-VT16 RESOLVED；R-VT12(b) 之「依 SYSAD」作廢，
    HU 匯流排依 LID Atlantis 欄之 `CAN` 值（A-VT19 結案：SYSAD 非拓撲文件，不再等）。
(d) DR-VT3 重寫：原問「DBC 版次對應」為誤問；28 列之「不符」是拿 Atlantis High 之 DBC 解 ATL-Mi 之規格，
    `TELEMATIC_VEHICLE_SETUP2`／`TELEMATIC_SERVICE_SETUP`／`SERVICE_SETUP` 皆見於 LID Atlantis 欄。
    DR-VT3 改為「待 ATL-Mi DBC 後重驗；若仍不符再問」，送出前不得以原文送。
(e) A-VT20 之第六規則（Unicode 去重音）：準，但命中者備註必記「重音正規化」並列 DR-VT2 佐證；不推廣為其他字符。
```

### R-VT14 —— 值域增「UI+PROXI 雙路徑」；HMI Settings List `Technical Reference` 欄先篩；台帳重生同 R-VL13

```
R-VT14（分析層裁定 2026-09-01，上繳 03 §二-2、§九-3、§九-5(a)）
(a) 結果值域增 `UI+PROXI 雙路徑`（R-P375(b)：Procedure 用 UI、Pre-Condition 用 PROXI，備註各引其列）；
    另增 `段3待ATL-Mi DBC`（R-VT13(b)）。
(b) HMI Settings List `Settings` 分頁 F 欄 `Technical Reference (CFTS/VF)` 含 `VF665` 者先篩出為本線候選集，對該集先比；
    未命中者再對全表。命中列之 F 欄值為 UI 元件之來源錨點（R-P353 (ii)），入備註。`Brand-Specific Names` 分頁於 P4 取 UI 實名時用，P3 不動。
(c) 台帳重生同 vsm_v42 R-VL13(a)（Pei 提交前一次）；R-VT8(a) 之「由 vsm_v42 重生」作廢（加註）。
(d) DR-VT4 升為與 DR-VT1 同級（三次擴充內部訊號 83→83，已證非比對問題）。
```

### R-VT15 —— 段 3 DBC 綁定：`P363_BH-CAN [07338]_3A_R2.dbc`；DR-VT5 結案

```
R-VT15（分析層裁定 2026-09-02，Pei「1 放了」；分析層驗收後綁定）
(a) 本線段 3 之 DBC = `forms/P363_BH-CAN [07338]_3A_R2.dbc`
    （實測：BO_ 99／SG_ 4576／VAL_ 503；ISO-8859、CRLF —— 以 latin-1 讀）。
    Atlantis High 之 R1 DBC 對本線降旁證；R-VT13(b) 之「待件」結案。
(b) 驗收（分析層實測）：原 R-13 28 名對本 DBC **逐字命中 26／28**；v3「解得 41」之 CAN 名命中 31／41。
    未命中之 2 名：`SERVICE_SETUP.TelematicSetupACK`、`TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock` ——
    W-5‴ 實測後若仍未解，入重寫後之 DR-VT3（暫持，不送）。
(c) CAN-C 未到件之處置同 vsm_v42 R-VL14(c)。
(d) 「解得」自此合法，`<label>` 逐字取本 DBC VAL_。DR-VT5 結案（到件）。
```

> **更正（R-TM13，2026-09-02，A-VT28）**：(a) 之 `SG_ 4576` 為含 `BA_` 屬性行之計數，
> **訊號定義行實為 688（相異 655）** —— 分析層自誤，同 vsm_v42 A-VL11。索引行首錨定，
> BO_ 99／VAL_ 503 相符，件之真偽不受影響。

### R-VT16 —— W-5 判準收尾：優先序與多值切分；E29 寬讀；排除清單；拼字疑誤值域；A-VT26 五列退回

```
R-VT16（分析層裁定 2026-09-02，上繳 04 A-VT24／E29／A-VT23／§八-3／A-VT26）
(a) 段 1 命中規則優先序與儲存格多值切分同 vsm_v42 R-VL15(a)(b)：E25 採 21（多值切分＋逐字，禁子串）。
(b) E29 採寬讀：`Technical Reference` 含 `665` 即入候選集（`VF230/665` 為 VF230 與 VF665 共用標記，247 列）；
    字面 `VF665` 3 列為其子集。錨點引用時備註保留原字。
(c) A-VT23 四名（`LTM`／`TBM`／`Unit`／`Resolution`）准入排除清單（偽陽性，標記不刪）；
    PROXI 母體以 39 為報表基準。
(d) 值域增 `未解得（規格拼字疑誤）`（同 R-VL16(a)）：`SERVICE_SETUP.RestoreDefaulSetting`／
    `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq` 自「CAN-C 未到件」改記此值；
    CAN-C 真缺口收斂為 6 列（含 `PROXI.First` 待審其是否抽名偽陽性，下包審）。
(e) A-VT26 五列（內部形僅段 3 同名）退回「未解得(止於段1)」（同 R-VL16(b)）；
    本線「解得」基線 = **81**（全數 CAN 形、全數有 VAL_）。A-VT26 RESOLVED。
```

### R-VT17 —— P3 收案；DECISIONS 簽核代記；本線掛起

```
R-VT17（Pei 裁定 2026-09-02：「皆授權」；收案內容分析層記）
(a) DECISIONS 四欄簽核，分析層代記「Pei 授權 2026-09-02」。P0–P3 收案。
(b) 本線掛起：下一個事件為 037 到件（DR-VT1，Pei 裁先不送）→ Layer 2 聚合 → P4。
    掛起期間無例行包；事實表定版 v5（解得 81／VAL_ 277 值）、profile、framework Layer 1 皆就緒。
(c) 上繳 05 §九-5(b)「FORMS.md 仍未登錄 P363 DBC」為沿抄前包之未測斷言（實已登錄，
    2026-09-02 分析層 ATL-Mi DBC 專節）；執行層小誤記此，不另立 A 號。
(d) GenSigSendType 列舉未查得前不得臆用（同 vsm_v42 R-VL18(c)）；037 到件後之首包併查。
```

### R-VT18 ——「送＋三」並行：SYSRA 暫代母體（295 列）；重錨條款；掛起解除

```
R-VT18（Pei 裁定 2026-09-02：「送＋三」；條文內容分析層記）
(a) DR-VT1 狀態改「Pei 裁定送出」（發送動作屬 Pei）；同時本線不等回覆，以 SYSRA 暫代母體進 P4。
    R-VT4 之「止於 P0–P3」自此解除；R-VT17(b) 掛起解除（兩條不刪，加註）。
(b) 暫代母體 = V43 SYSRA `Basic Report` Functional 507 列扣除 DocID `VF655_V43_R3` 171 列與
    DocID 空 41 列，得 **295 列**（上繳 01 W-4 之乾淨分母；被扣兩批隔離待 DR-VT2 澄清，
    確認誤植者屆時以增補批併入，不回溯改已生成之 TC）。
(c) 重錨條款：暫代期間所有 TC 之 D 欄（Requirement or Design ID）用 `Sys-RA-VF665_V43_VSM-…` 實名，
    Remarks 逐列註 `Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1)`。
    037 到件後逐 TC 對映 037 需求單位：對得上者換錨（舊→新 ID 對映表隨包），對不上者作廢或重寫；
    重錨完成前**不得交付**，除非 Pei 另裁。返工風險為 Pei 知情採認之代價。
(d) TC 切分權威暫代期間為 SYSRA 列（IN §8.2 之「上游分解」代位）：不得再分解、不得合併 SYSRA 列；
    驗證單位仍依 §8.2.2（一列得多 TC）。交付說明須揭露暫代構型（與全案他 feature 不同構）。
(e) Layer 2 暫代：自 295 列之 `chapter_for_vf` 完整值與標題聚合，執行層出材料（06 包）、
    分析層出草案、Pei 裁後鎖；framework Layer 2 節之「留白為裁決結果」加註 R-VT18 改走暫代線。
```

### R-VT19 —— Layer 2 暫代鎖定（16 組，Pei「准」）；暫代期 spec_reference 型態

```
R-VT19（Pei 裁定 2026-09-02：「准」；草案分析層，材料上繳 06）
(a) Layer 2 暫代鎖定 16 組，合計 295（全表見 framework.md）：
Exterior Lighting 32／Lane Departure Warning 18／Forward Collision Warning 15／
Side and Blind Spot Warnings 16／Park Sense 15／Units 26／Clock and Time 24／Language 4／
Door Lock and Access 30／Interior Ambient Lighting 10／Wiper and Sensor 5／
Phone and Navigation Repetition 4／Privacy and Service Data Reset 14／
Setup Acknowledge and Recovery 13／Menu Access and Persistence 2（真離群，IN §4.2）／
PROXI Configuration 67（含 01.14.01 表 38＋01.14.02.01.* 用途 29，不拆）。
Layer 3 = chapter_for_vf 完整值（不入工作簿）。037 到件重錨時 Layer 2 重議，本鎖定不預先拘束正式版。
(b) 暫代期 spec_reference：主錨 `Sys-RA-VF665_V43_VSM-{nnn}`（一 ID 一行，同 R-VL19(b) 型）。
    chapter_for_vf 與 V43 R4 規格章節號之對應（如 01.11.01.01.06 ↔ 1.11.1.1.6）為假說，
    須逐章實測規格標題後方得加列 spec 錨（P4 包 W 項）；未驗證前只寫 Sys-RA 錨，不臆配。
(c) P4 pilot 提案：Interior Ambient Lighting（10 leaf，單一 chapter，含解得 80%）；開跑前 Pei 可改指。
```

### R-VT20 —— pilot b1_ambient 覆核：K-1 驗證法定為 token 共現；K-2〜K-4 裁；制度化二條

```
R-VT20（分析層裁定 2026-09-02，上繳 07；實檔抽驗 -659／-661 逐字）
(a) K-1：+1 偏移之確立改用**字面判準**，非語意 —— 訊號名／PROXI 參數名為逐字 token，
    同時出現於 SYSRA Description 與規格節內文即為證：建 42 節全表（推算章節號、標題逐字、
    節內 token 集 ∩ 各 chapter 組 token 集之命中數）。判準：偏移全表一致且 token 支持 ≥ 40／42 節
    → 鎖雙錨（spec 錨 `…_VF665_V43_R4_{推算章節號}` 加列在前，Sys-RA 錨保留在後）；
    未達 → 暫代期全案只 Sys-RA 錨。一次驗完再鎖，不逐包零星判（執行層 §九-1 建議採）。
    ELSE 對應範圍（para 1028↔1046 型）於同表併驗。
(b) K-2：-661 兩條准（合取式之兩否定支各自獨立，§8.2.2／§8.3；德摩根讀出非增範圍）。
(c) K-3 入 DR-VT2 佐證；K-4：以規格 7 級為準（§8.4.2 範圍），VAL_ 16 級之差入 DR-VT3 佐證，
    不擴生成不上問。
(d) 追認：-659 注入值選擇為測試設計自由度（須與起始值相異、取 VAL_ 實值、reasoning 記選擇理由）；
    本批 0 PENDING 之理由成立且附防推廣警語，其餘 15 組逐組實測不得沿用。
(e) 制度化（跨線，vsm_v42 同適用）：test_item 逐字全等斷言入每一生成包固定自檢；
    訊號名比對預設詞界式（子串式僅限明令）。
(f) b1_ambient 11 條覆核通過；待 (a) 驗後補 spec 錨即凍結，併入寫回批。
```

### R-VT21 —— 42 節表判定採認；K-5 掛起待 K-6；K-7／K-8 處置；下一量測

```
R-VT21（分析層裁定 2026-09-02，上繳 08）
(a) 判定「不成立」採認；b1_ambient 以 Sys-RA 錨凍結（INDEX 記「b1 FROZEN (R-VT21)」，
    此後變更須新裁決；重錨條款 R-VT18(c) 不受影響）。
(b) K-5（常數偏移→保序對齊之改判準）**掛起，待 K-6 量測定案後併裁** ——
    若母體組成重議，對錯了的批鎖逐節對應即白工。
(c) K-6 為母體級問題，先量後裁：令 171 × 295 逐列文本比對（下放包 09）；
    量測前不動 R-VT18(b) 暫代母體、R-VT19 十六組、已凍之 b1。DR-VT2 加 K-6 重量級佐證（定性待量測）。
(d) K-7：ELSE 轄域「不可判」採認；SYSRA -660 列位置與逐字否定對偶兩旁證已足支持 R-VT20(b) 之兩條，
    轄域之進一步判定非 b1 所需，掛起。
(e) K-8：`1.11.1.1.35` 無詞可證 —— 於 09 包以 `01.13.*` 章節組之 token 集補測一次（仍字面法）；不硬配。
```

### R-VT22 —— K-6／K-9 裁：甲案——暫代母體 v2 合成；K-5 定案；K-10 回掃令

```
R-VT22（Pei 裁定 2026-09-02：「甲」；合成規則分析層記）
(a) 暫代母體 v2 合成規則：
    (i) 128 逐字重複對取 295 批列（已凍 b1 之錨不動）；
    (ii) VF655 實質獨有列全數納入（含無對應 38 列與近似對中屬不同功能之 5 列）；
    (iii) 同功能新舊對（對 1／4／5）取 VF655 新寫法列、廢 295 舊列（superseded 清單留檔，R-TM13 不刪只標）；
    (iv) 41 批獨有 1 列納入。確實列數由執行層實測回報（預期約 336–339，不預斷）。
    v2 逐列帶 batch_source（295／VF655／nodocid）與 chapter（原值）。
(b) Layer 2 v2：新增 EPB Maintenance Mode／Auto Park Brake／Rearview Camera 三組；
    RainSensor 2 列入 Wiper and Sensor、AHB 2 列入 Exterior Lighting、FuelCons 1 列入 Units、
    01.08.03 1 列入 Clock and Time、組態表列（含 -1278）入 PROXI Configuration。
    執行層實測各組列數後分析層定表、Pei 准後鎖（取代 R-VT19(a)，不刪只標）。
(c) K-5 定案：保序對齊成立（雙鏈互證：section_map 37 強節＋09 包 Δ 同構）。spec_section 推導：
    VF655 批列之 chapter 即規格節號（偏移 0 實證）；295 批列依 section_map 之分段偏移換算；
    換算來源逐列標註。未來批生成時雙錨（spec 前、Sys-RA 後）；已凍 b1 不解凍，其 spec 錨隨 037 重錨補。
(d) K-10 回掃令：R4 修訂說明逐項逐字取出，回掃 v2 全批（含 295 批存留列）之舊寫法命中；
    命中列只報不自修，逐項待裁。
(e) DR-VT2 定性更新：非單純 DocID 誤植 —— 係較新版次之部分重匯（75% 重複）且含舊批所無之四節；
    VF655／R3 標籤與內容較新之矛盾上問。重錨條款 R-VT18(c) 不變。
```

---

## 取號紀錄

| 條號 | 落檔日 | 取號依據 |
|---|---|---|
| R-VT1–R-VT5 | 2026-09-01 | 本檔新建，全庫 `R-VT` 系列實測未佔 |
| R-VT6–R-VT8 | 2026-09-01 | 落檔當下讀本檔實測至 R-VT5；上繳 00 §七 sha 表亦止於 R-VT5 |
| R-VT9–R-VT10 | 2026-09-01 | 上繳 01 §五 5.3 sha 表止於 R-VT8；本檔錨點實測 8 |
| R-VT11–R-VT12 | 2026-09-01 | 上繳 02 §三 sha 表止於 R-VT10；本檔錨點實測 10 |
| R-VT13–R-VT14 | 2026-09-01 | 上繳 03 §五 sha 表止於 R-VT12；本檔錨點實測 12 |
| R-VT15 | 2026-09-02 | 本檔錨點實測 14 |
| R-VT16 | 2026-09-02 | 上繳 04 §三 sha 表止於 R-VT15；本檔錨點實測 15 |
| R-VT17 | 2026-09-02 | 上繳 05 §六 sha 表止於 R-VT16；本檔錨點實測 16 |
| R-VT18 | 2026-09-02 | 本檔錨點實測 17 |
| R-VT19 | 2026-09-02 | 上繳 06 §五 sha 表止於 R-VT18；本檔錨點實測 18 |
| R-VT20 | 2026-09-02 | 上繳 07 §八 sha 止於 R-VT19；本檔錨點實測 19 |
| R-VT21 | 2026-09-02 | 上繳 08 §八 sha 止於 R-VT20；本檔錨點實測 20 |
| R-VT22 | 2026-09-02 | 上繳 09 §九 sha 止於 R-VT21；本檔錨點實測 21 |
