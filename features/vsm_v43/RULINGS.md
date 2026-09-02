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
