# RULINGS — Display (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Display 之裁決權威；
跨 feature 條文承接時註明來源包。

抄錄方式：以 `re` 自下放包之 fenced 區塊機器抽取後原樣寫入，未經人工
轉錄。逐條 SHA256 核對表見文末。

---

## 來源：下放包 01

```
R-DM1（feature 身分與 test_group）
`feature` 為 `Display`，slug 為 `display`，`test_group` 為 `Display`。
（Pei 2026-08-24 裁定「就用 Display」。）

037 之模組名 `Display Management` 與 CFTS_020 之文件名
`ICS and DCSD` 皆不進入 `test_group`、不進入任何 TC 欄位；二者僅得
記於 `feature.yaml` 之路徑註解與 `framework.md` 之說明文字。

裁決前綴為 `R-DM`、異常前綴為 `A-DM`、資料請求前綴為 `DR-DM`，
不與任何既有 feature 共用序號。
```

## 來源：下放包 01

```
R-DM2（037 之來源授權）
037 A03 SWRA（`Display_Management_FMWIFSM037A03_STLA_Report_SWRA.xlsx`）
於 2026-08-24 在 Pei 之磁碟上未能定位；分析層已查
`9_ASPICE/`（無 SWE.1 目錄）、`10_Reviewing/00_TestCase/`、
`6_SW_Test/`、`7_Delivery/`、`0_Project_Management/`、
`Work_Projects/` 下各專案，皆無。

Pei 2026-08-24 授權：以 Claude Project 之附件為該檔之唯一來源，
由 Pei 手動置入 `_intake/Display/`。

執行層拘束二項：
(a) 不得自行向上游索取該檔，亦不得以任何其他檔案代替；
(b) 該檔一經置入即記其 SHA256 與 mtime 入素材台帳；台帳建立後，
    後續各輪之引用一律對台帳所記之 repo 內複本實測，不回頭引用
    本包之任何數字（canon §5a：不以自身先前輸出為來源）。
```

## 來源：下放包 01

```
R-DM3（多套 id 命名之處置 —— 登記，不解）
本 feature 之追溯鏈在文件間出現多套互不相同之 id 命名：

  037 `SWE1 Requirements` 分頁   → `SWE-DM-001` … `SWE-DM-008`
  037 `SWE1 Requirements` 分頁   → `SYS-DISP-001` …（Source Requirement ID）
  037 `SYS2 Traceability` 分頁   → `SWE1-DM-001` …（同一物件，另一寫法）
  037 `SYS2 Traceability` 分頁   → `SYS-RA-DISP-001` …（指向 SYS2）
  SYS2 `Basic Report` 分頁       → `SYS-RA-DM-001` … `SYS-RA-DM-087`
                                    及 `SYS2-RA-088` 以後

`SYS-RA-DISP-*` 與 `SYS-DISP-*` 兩種寫法在 SYS2 released 版中之出現次數
為 **0**（量測條件見 §三 3.3）。

本輪之處置為**登記而非解決**：執行層以 `A-DM{n}` 逐項登記，附證據與
提案處置，不得自行推定其對應關係（例如推定
`SYS-RA-DISP-001` ↔ `SYS-RA-DM-001`）。任何跨命名之對應皆屬
canon §0 逸出觸發第 1 條「規格查找未解」，須停並回報。

`feature.yaml` 之 `req_id` 欄最終寫何種形態，屬 Tier 2，於 Phase 2 裁定；
本輪僅記現況。
```

## 來源：下放包 01

```
R-DM4（037 之 Excluded 分頁其 id 語意已查明）
037 `Excluded NRLs (HW-only)` 分頁之 `NRL ID` 欄，其 8 個值
（`PSCFTS020-1-45-1` 等）**不是 SYS2 之 NRL ID**（SYS2 之 NRL ID
形態為 `NRL-52839`），而是 SYS2 `SYS2 Melco ID` 欄之值。

分析層已實測：該 8 值在 SYS2 Melco ID 欄之 99 個 token 中 8/8 命中
（量測條件見 §三 3.3）。

拘束：執行層引用該分頁時一律稱其為 Melco ID，不得以「NRL ID」之欄名
為據去 SYS2 之 NRL 欄查找 —— 那會 8/8 查無，並被誤讀為追溯斷鏈。
本條為已解之項，不再登記為 anomaly。
```

## 來源：下放包 01

```
R-DM5（intake.py 之 sniffer 對本 037 之已知偏差）
`scripts/intake.py` 之 `SHEET_SIGNATURES` 以
`"Analysis Report" in names` 判定 `swra_report`。本 037 之分頁為
`SWE1 Requirements` / `SYS2 Traceability` / `Excluded NRLs (HW-only)`，
無 `Analysis Report`，故必然被分類為 `spec_xlsx`。

執行層拘束三項：
(a) 照跑 `intake.py`，如實回報其實際分類結果，不得預先改腳本使其命中；
(b) 分類偏差之修法（新增分頁簽章、或以 feature.yaml 人工指定
    `a03_report`）屬 Tier 2，本輪只提案不實作 —— 改判準會改結論，
    不屬 AUTO 之技術選擇；
(c) `intake.py` 之 need-list 推導對本檔亦不適用：其
    `Source Requirement ID` 欄之內容為 `SYS-DISP-nnn` 形態之
    Polarion id，非 `name_{section}` 形態之文件引用。腳本應如實
    報告「不可推導」而非產出空清單；若其產出空清單而未說明，
    以 `A-DM{n}` 登記。
```

## 來源：下放包 01

```
R-DM6（素材台帳之到齊定義）
素材之「到齊」定義為：清單每項附其檔案系統絕對路徑與 SHA256，且
`shasum -c` 對得上。「檔名相符」「大小相同」皆不構成到齊。

搬入 `features/display/inputs/` 者為複本，來源目錄一律唯讀，
搬入前後各記 SHA256 與 mtime 並登入台帳。

四份以外之檔案不得搬入；`_intake/Display/` 若另有本包未列之檔，
登記後停手詢問。
```

## 來源：下放包 01

```
R-DM7（覆蓋落差之量測義務 —— 8 vs 80）
037 之 leaf 全集為 8，而 SYS2 released 版之 `Functional Requirement`
列數為 80（`SYS-RA-DM-*` 區段 44 + `SYS2-RA-*` 區段 36；大小寫變體
1 列已計入，見 §三 3.3）。

本落差不得以「037 為權威、故 8 即全集」一句帶過。執行層須於本輪
產出可審之對照：以 SYS2 之 `Functional Requirement` 全集為母體，
逐列標記其是否可對應到 8 個 SWE-DM leaf 之一，對應依據逐列寫明
（Melco ID、Description 文字、或無）。無法對應者列出其列號與
`SYS2 Sys-RA-Feature-ID`。

該對照之用途為**揭露**，不是重新界定範圍。範圍之裁定屬 Tier 2，
於 Phase 2 依此對照為之。此處之判準為 canon §5a：引用任何單一來源
為「權威」前，先確認其涵蓋範圍是否等同其類別 —— 037 只有 8 筆，
不等於 Display 之軟體需求只有 8 筆。
```

## 來源：下放包 01

```
R-DM8（缺值不得自填）
037 之 8 筆需求描述皆為 SWE 層抽象語句，其中至少四處之具體值
在 037 內不存在：

  SWE-DM-003  Splash / sleep 之時長門檻
  SWE-DM-004  thermal warning threshold 之門檻值與單位
  SWE-DM-005  thermal protection 之 critical 判準與回復條件
  SWE-DM-006  popup priority arbitration 之優先序規則與 timeout

上述各項一律先回 CFTS_020 本文與 SYS3 SYSAD 查；查得者記其章節，
查不得者以 `DR-DM{n}` 登記，不得以領域常識、其他 feature 之值、
或 037 之 `Verification Criteria` 欄文字回填（canon §8.4.1）。

`Verification Criteria` / `Verification Method` 二欄之地位為
**參考輸入而非權威**：其為上游之推導產物，以其為據等同以推導物
取代來源。（形態同 Vehicle Setting R-VF13，惟本 feature 尚未取得
該條之五項限制之對應裁定，故本輪一律不用。）
```

## 來源：下放包 02

```
R-DM2（廢止並以 R-DM2′ 取代）
~~037 A03 SWRA 於 2026-08-24 在 Pei 之磁碟上未能定位……以 Claude
Project 之附件為該檔之唯一來源，由 Pei 手動置入 `_intake/Display/`。~~

廢止理由（2026-08-24，下放包 02）：前提「磁碟上未能定位」為誤。
分析層以附件之正規化檔名 `FMWIFSM037A03`（無連字號）為搜尋字串，
而磁碟實際檔名為 `FM-WI-FSM-037-A03`（帶連字號），致搜尋落空；
且查 `10_Reviewing/00_TestCase/` 時僅列至 `ASW-R2` 一層即轉往他處，
未下鑽至 `ASW-R2/Display/`。
```

## 來源：下放包 02

```
R-DM2′（037 之來源）
037 A03 SWRA 之來源為
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/
Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`，
其 SHA256 須為
`ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050`。

該值與 Pei 授權之 Claude Project 附件為位元級同一（分析層 2026-08-24
以 `sha256sum` 對附件複本實測所得）。故本條非「以他檔代替附件」，
而是同一內容之磁碟路徑。

拘束：搬入前以完整 64 碼比對，不符即停並回報，不得以「首尾相符」
或「size 相符」放行。
```

## 來源：下放包 02

```
R-DM9（素材來源目錄）
本 feature 之素材來源目錄為
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/`
（唯讀，不得寫入），四份素材皆取自該目錄。

下放包 01 §3.4 所列之三條路徑（`9_ASPICE/SYS.2 …`、
`9_ASPICE/SYS.3 …`、`1_Customer_Requirement/… 26PI1.5/SubSystem/Cabin/`）
**作廢，不得再作為來源**；該三處之同名檔僅得作為比對對象，
其與交付夾版之 SHA256 比對結果登入台帳。

依據：`power_moding` 之 `ASW-R2/Disclaimer screen/` 為同型前例 ——
FROP 交付夾內含該 feature 之完整素材組，為專案之組織慣例。
```

## 來源：下放包 02

```
R-DM10（A 版本之處置）
`/Users/peihe/Work_Projects/R1L_RTM_V3/data/9_ASPICE/
04_SWE.1 Software Requirements Analysis/Display Management/
Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
（SHA256 `100f75b7…a5f374f0`，44697 bytes）與 R-DM2′ 之標的
**內容同一、檔案相異**。

分析層 2026-08-24 之逐儲存格比對（三分頁、`data_only=True`、
非唯讀模式、取兩者 max_row × max_column 之聯集、越界取 None）
差異格數為 0。

處置：不搬入、不引用、不登記為版本歧異。其存在僅記於台帳之
「同內容他處副本」欄。若日後任一方內容變動致比對不再為 0，
以 `A-DM{n}` 登記並停手。

同目錄之 `SWE1_DISPLAY_MANAGEMENT_INIT_ONLY_OBSELETE.xlsx`
（檔名自書 OBSOLETE）不搬入、不開啟。
```

## 來源：下放包 02

```
R-DM11（檔名正規化之通則）
Claude Project 附件之檔名經上傳正規化（連字號、空格、`&` 等字元
被移除或替換），與磁碟原始檔名不同。分析層引用附件檔名於磁碟搜尋時，
**須先以其去除分隔符後之骨幹字串為鍵**，或改以目錄下鑽窮舉，
不得以附件檔名逐字搜尋後即斷定「磁碟上無此檔」。

本條為 R-DM2 致誤之防再犯條文。適用範圍為全案，非僅本 feature。
```

## 來源：下放包 03

```
R-DM12（啟發式輸出之命名與引用）
凡以文字相似度、token 重疊、模糊比對等啟發式產出之欄位，其欄名
一律冠 `candidate_` 或等義之未定語，不得使用 `對應`、`mapping`、
`match` 等已認定語氣之名稱。

引用該欄時必須同時引用其依據種類欄（`anchor_kind` 或等義欄），
禁止單獨引用結果欄。

理由：正文之免責敘述與欄名分離後，欄名會被單獨引用。本條為
上繳包 02 §9 之「對應 SWE-DM」欄致誤之防再犯條文。
```

## 來源：下放包 03

```
R-DM13（覆蓋對照之錨定方法）
SYS2 ↔ 037 之覆蓋對照一律以結構性錨為據，優先序為：
`$Signal$` token → `[VALUE]` token → SYS2 Heading 從屬 → Melco ID →
無錨。bag-of-words 重疊**不得作為錨**，亦不得作為候選之產生方式。

下放包 01 R-DM7 所列之「Description 文字（機械 bag-of-words 重疊）」
一項**廢止**。廢止理由：該方法對 SYS2 之 hot-behaviour 四列
（r31–r34）同時產生偽陰性與偽陽性，致 `SWE-DM-004`/`005` 被誤報為
命中 0 列（詳見下放包 03 §3.1）。R-DM7 之其餘部分（揭露義務、
不得裁定範圍）不受影響。
```

## 來源：下放包 03

```
R-DM14（訊號值域之來源）
本 feature 之訊號名與值域以 SYS2 `Basic Report` 之 `$Signal$` 與
`[VALUE]` token 為第一來源（實測：80 個 FR 列中 43 列含訊號，
相異訊號名 15、相異值 token 9）。

037 不含訊號層資訊，不得作為值域來源。
CFTS_020 之對應章節為行為敘述，與 SYS2 併讀。

本條僅定來源，不定 TC 之書寫格式；書寫格式依 canon §8.7.5 或本
feature 日後之 profile override，本輪不定。
```

## 來源：下放包 03

```
R-DM15（036 母本 B 欄）
036 母本 `Test Case Specification 測試用例規範` 分頁之 B 欄
（`No.#`）為公式欄，B10–B1411 逐列為
`=IF(ISBLANK($D{row}),"",ROW()-9)`。

寫回一律不得對 B 欄賦值。序號由 D 欄（`req_id`）之填寫自動產生。
```

## 來源：下放包 04

```
R-DM16（`[VALUE]` token 之定義 —— Display）
SYS2 之 `[VALUE]` token 一律以寬式定義擷取：`\[([^\]]+)\]`，
不限大寫。實測相異 13 個。

下放包 03 §3.3 所載之「相異 9 個」係以 `\[([A-Z0-9_]+)\]` 取得，
該定義丟棄了 `[0% Intensity]`（出現 20 次，為 FR 母體中最頻繁之值
token）、`[pressed]`、`[Idle]`、`[DCSD_and_HU_LVDS_Backchannel_Protocol]`。
**「9」之數字撤回**，R-DM14 所引之 9 一併改為 13。

理由：`[0% Intensity]` 是 `$RQ_DISP_INTS$` 之值（LID 1626 →
`RADIO_B3.RQ_DISP_INTS`，8 bit、0.5 %/bit、0–100、255 = SNA），
正是 R-DM14 所定之值域來源。以大小寫為過濾條件會依書寫習慣而非
語意切分資料。
```

## 來源：下放包 04

```
R-DM17（訊號名之解析鏈 —— Display，取代 R-DM14 之單段表述）
SYS2 之 `$Signal$` 為 Logical Identifier，非 CAN 訊號名。解析為三段：

  SYS2 `$Signal$`
    → LID `CAN Mapping` 分頁之 `Logical Identifier` 欄逐字比對
    → 該列 `Atlantis High` 欄組之 `Signal Name`（形如 `MESSAGE.Signal`）
    → DBC 之 `SG_` 定義與 `VAL_` 列舉

架構欄組固定取 **Atlantis High**（沿用 R-VS67）。
LID 一列可載多個 `MESSAGE.Signal`（以換行分隔，對應不同匯流排或
不同硬體變體），**不得任取其一**；須依該列之 `CAN` 欄與本專案之
匯流排配置擇定，擇定依據逐筆記錄。

R-DM14 之「SYS2 為訊號值域之第一來源」不變，但其表述之
「037 → SYS2 → DBC 兩段」修正為本條之三段。
分析層 2026-08-24 誤將 `TGW_DISP_STAT` → `TGW_DISP_STATSts` 之差異
讀為 R-13/(g)「規格名 DBC 查無」，該讀法撤回：LID 為應查之處，
查了就有。
```

## 來源：下放包 05

```
R-DM18（`[VALUE]` token 之擷取 —— 取代 R-DM16）
R-DM16 廢止。其 regex 與其所載之數字不相容（條文指定
`\[([^\]]+)\]` 而記「相異 13 個」），致誤原因為分析層將上繳包 03 以
`\[([A-Za-z0-9_%\s]+)\]` 量得之 13 誤植為寬式之產物。

現行判準：以 `\[([^\]]+)\]` 擷取後，**排除 token 中含 `:` 者**。
冒號為 Polarion 匯出 metadata 之逐字標記（`[Artifact Type:…]`／
`[State:…]`／`[Market:…]`／`[Radio:…]`／`[EE Architecture:…]`），
非規格值。此判準為逐字比對，不涉相似度。

分析層 2026-08-24 實測（母體 80 列 FR，`Description` 欄）：
寬式相異 59、含 `:` 43、不含 `:` **16**、至少含一個不含 `:` token
之 FR 列 **35**。執行層須先調和其 44 與本處之 59 之切分差異，
以調和後之數字為準。

不含 `:` 之 16 個中，`DCSD_and_HU_LVDS_Backchannel_Protocol`、
`DCSD* and HU CAN and LVDS Backchannel Message Sequence Charts`、
`SD.xxxxx DCSD LVDS VIDEO COMMUNICATION INTERFACE` 三者為文件／協定名，
於輸出中另標 `kind=document`，不計入值域。其餘 13 個為值 token。

`[current non-zero value]`（8 次）必須保留：它是 `$RQ_DISP_INTS$` 之值，
且其模糊性為規格自身所有。依 canon §8.4.1，來源模糊即保留模糊；
丟棄它會使 TC 撰寫時被迫填入一個來源未載之具體數值。
```

## 來源：下放包 05

```
R-DM19（B-CAN 資料庫之選定）[PROPOSED]
本 feature 之 B-CAN 資料庫為 `forms/PDT27_E2A_R1_BHCAN2.dbc`
（SHA256 `46cb73f3db62ac9f…`）。依據：Pei 2026-08-24 之指示
「BHCAN 改成 BHCAN2」並親自置檔。

FD-CAN 資料庫為 `forms/PDT27_E2A_R1_FDCAN8.dbc`
（SHA256 `2a86c4bf3e670d71…`）。

承載範圍（本條若有誤，下列全部須重做）：
  - `features/display/data/signal_resolution.tsv` 之 26 列
  - `forms/LOOKUP_MISSES.md` 之 M-1／M-2 兩筆查無
  - 此後所有 Display TC 之訊號名、訊息、raw 值、VAL_ 標籤、
    收發節點

`features/vehicle_setting/inputs/` 之 `PDT27_E2A_R4_BHCAN.dbc` 與
`PDT27_E2A_R5_FDCAN8.dbc` **不因本條而作廢**；vehicle_setting 之
已交付件依既有慣例不回頭改（同 R-G1）。

BHCAN-R4 有 573 個訊號名不在 BHCAN2 中（A-DM14）。其他 feature 若
改用 BHCAN2，須逐一複驗既有訊號 —— 不在本 feature 範圍，登記於
`forms/LOOKUP_MISSES.md` 之備註區。
```

## 來源：下放包 05

```
R-DM20（PROXI 之開工 —— 步驟 11 之觸發放寬）
下放包 04 步驟 11 之停手觸發原為「LID `Proxi & Configuration` 分頁與
本 feature 之**訊號**有關聯」。該條件過窄：PROXI 參數本就不是訊號，
以訊號為觸發等於永不觸發。

放寬為：**與任一 leaf 之前置條件、可用性條件、或配備有無相關者**。
A-DM16 所列之 `DCSD_cfg`（DCSD Present）、`DSP_SK_PRSNT`（Display off
soft key present）、`RVC_SK_PRSNT`（Rear Camera soft key present）
三者已滿足此條件，故 PROXI 解析自本輪起為 in scope。

值域仍依 R-VS49 之既有裁定：PROXI 表本身為該參數值域之權威。
`forms/PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁（1,060 列）
為主表。

**本條只開放解析，不授權將任何 PROXI 參數寫入 TC 之 Pre-Condition。**
何者進入 Pre-Condition 屬 §8.5 之範疇（須為規格明載之觸發條件，
非隱含環境穩定前提），於 Phase 2 逐 leaf 判定。
```

## 來源：下放包 05

```
R-DM21（「解得」須指明止於哪一段）
R-DM17 之解析鏈為三段（SYS2 `$Signal$` → LID → DBC）。任何「解得」
「查得」「resolved」之陳述，一律須指明其止於哪一段，並分別給數。

實例（2026-08-24）：下放包 04 §3.4 記「15 個 `$Signal$` 全數解得」，
該陳述止於 LID 成立（15/15），止於 DBC 不成立（14/15）。
單寫「全數解得」會使讀者以為 TC 可用之 CAN 名已備齊。

本條同理適用於 CFTS 條號之解析（A-DM10b）與任何多段查找。
```

## 來源：下放包 06

```
R-DM22（縮寫錨 —— glossary_phrase）
下放包 03 §七第 10 條之禁令（「不逐字即無錨」）**限縮**：其所禁者為
token 重疊、相似度、模糊比對；**不禁**封閉且逐條有出處之縮寫對照表。

本 feature 建立 `features/display/data/glossary.tsv`，欄位：

  abbrev | expansion | source_file | source_locator | cooccurrence_quote

**每一條目必須引一處「縮寫與其展開在同一句並列」之來源。**
查無此種並列者，不得建立條目 —— 那會是以領域常識填入，觸 canon §8.4.1。

首條（分析層已查得）：

  RVC | Rear View Camera | Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx
      | SWE1 Requirements r14 (SWE-DM-007), 亦見 r15 (SWE-DM-008)
      | "transition display state to Rear View Camera (RVC) mode"

以對照表展開後之比對，其 `anchor_kind` 為 **`glossary_phrase`**，
與 `verbatim`、`signal`、`value`、`heading` 分列，**不得合併計數**。
引用時依 R-DM12 須連同 `anchor_kind` 一併引用。

拘束三項：
(a) 展開後之片語須 **≥ 2 個詞**。單詞展開不得作為錨（鑑別力不足）。
(b) 比對為**逐字子字串包含**，區分大小寫；大小寫折疊須另行裁定。
(c) 展開後仍不逐字相符者，即為不相符，**不得再放寬一層**。
    實例：`RVC` → `Rear View Camera` 後，SYS2 之 heading
    `Rear Camera Events`（少一個 `View`）仍**不**相符。
```

## 來源：下放包 06

```
R-DM23（未追查 ≠ 查無）
`proxi_candidates.tsv` 之 269 列 `anchor_kind = none`，其狀態為
**未追查**，非查無。本輪只追了 A-DM16 指名之三個起點。

凡輸出中以 `none`／`無`／空值表示之列，其欄位或說明須明載該值之語意
屬下列何者：

  (1) 已依 R-G13 三要件查證而確認不存在（= 查無）
  (2) 本輪未追查（= 未知）
  (3) 方法之界線所致（= 接不上，非不存在）

三者不得共用同一個表示。本 feature 現有之三處輸出
（`coverage_sys2_vs_swe_dm.tsv` 之 76 列無候選、
`proxi_candidates.tsv` 之 269 列、`signal_resolution.tsv` 之
`resolved = N`）須逐處補上其語意別。

理由：`LOOKUP_MISSES.md` 記的是 (1)，而 (2) 與 (3) 若混入，
台帳就變成「已查過而沒有」的假象，下一個讀者不會再去查。
```

## 來源：下放包 07

```
R-DM24（Q5 定案：intake 之 kind 覆寫機制）
Pei 2026-08-25 裁定採 B。授權修改 `scripts/intake.py`，範圍**僅限**
新增讀取 `feature.yaml` 之 `intake.kind_overrides` 節之機制。

`SHEET_SIGNATURES` 一字不動。

覆寫之五項拘束：
(a) 鍵為檔名，值須含 `kind`、`reason`、`sha256`
(b) 覆寫僅在實際雜湊與所載相符時生效；不符則不套用並警示，
    不得靜默略過
(c) 無 `kind_overrides` 節時行為與現行完全相同（缺省惰性）
(d) `intake.json` 與 `INTAKE.md` 須記 `kind_source: override|signature`
    及 `reason` 全文
(e) 改動前後對 `_intake/` 下現有全部目錄跑回歸比對，除 Display 之 037
    外任一檔分類結果改變即還原並停手

本授權不及於 `recon.py` 或任何其他共用腳本。
```

## 來源：下放包 07

```
R-DM25（分隔符正規化 —— 宣告式對稱，非放寬）
R-DM22(c)「展開後仍不逐字相符者即為不相符，不得再放寬一層」**維持**。
本條所開放者不是「再放寬一層」，而是**在比對之前、對兩側同時施加之
宣告式字元類正規化**，其性質與大小寫折疊同類。

允許之正規化僅一項：**底線 `_` 與空格之互換**（`[ _]+` → 單一空格，
兩側皆施）。其餘（連字號、點號、駝峰切分）不在本條範圍，
需要時另行裁定。

四項拘束：
(a) 正規化須**兩側同時施加**，不得只正規化一側
(b) 產出須**同時報告嚴格比對與正規化比對之命中數**，兩數並列
(c) 僅在正規化後才成立之候選，其 `anchor_kind` 標
    `glossary_phrase_norm`，與 `glossary_phrase` 分列，不合併計數
(d) 正規化之定義須逐字寫入產出檔之檔頭

理由：底線與空格之互換在識別碼與散文之間是書寫慣例差異，非語意差異，
且該轉換有限、可逆、可逐字稽核。但它確實會使 `A_B` 與 `A B` 相等，
故其產物必須可與嚴格比對之產物分離 —— (b)(c) 即為此。

實例（上繳 06 §4）：LID `Proxi & Configuration` 之
`Rear_View_Camera` 與展開後之 `Rear View Camera`，在本條下相符，
標 `glossary_phrase_norm`。
```

## 來源：下放包 07

```
R-DM26（錨優先序修正 —— heading 降為最低）
覆蓋對照之錨優先序改為：

  signal → value → glossary_phrase → glossary_phrase_norm → melco
         → heading → none

heading 自第三位降至倒數第二。依據（兩輪實測）：
  - SYS2 之 80 列 FR 母體中，有 heading 祖先者 80/80，
    存在性 100%，不構成區別
  - 單一節點 r72（序列器觸控中斷接腳定義）底下掛 48 個 FR，
    佔母體 60%，與顯示行為無關

一個命中率 100% 且最大節點佔六成之錨置於高位，會遮蔽其下所有錨 ——
上繳 06 §3.2 之「`glossary_phrase` 在 `anchor_kind` 中永不出現」
即為此效應。

`candidate_from` 欄依 R-DM12 保留，與 `anchor_kind` 並列輸出，
兩欄不得合併：前者記全部生效之錨，後者記最高優先者。
```

## 來源：下放包 07

```
R-DM27（R-DM8 之缺值範圍由四處改為全稱）
R-DM8 列 `SWE-DM-003`／`004`／`005`／`006` 四處為缺值點。
上繳 06 §8 之全文精讀實測：八條之「數值＋單位」命中 **0/8**、
`$Signal$` token **0/8**、外部文件引用 **0/8**。

**四處為抽樣所得之低估，改為全稱：037 八條皆不含任何具體值。**
例 `SWE-DM-001` 含 `based on system operational requests and timeout
conditions`，而 timeout 之值未載，該條原不在四處之列。

R-DM8 之禁止回填規定不變，適用範圍擴及八條全部。

附帶記明（上繳 06 §8）：八條皆為兩句併寫且句號後缺空格（8/8），
第二句多為回復／還原語意（restore／resume／ensure）。
以句號斷句之實作會把兩句併為一句，使回復語意附著於第一句之條件之下。
撰寫 test_item 上半之 verbatim 摘句時須注意此形態。
```

## 來源：下放包 08

```
R-DM28（`anchor_kind` 與 `candidate_from` 回答不同問題）
覆蓋對照之兩欄不得互相替代，亦不得合併：

  `anchor_kind`     = 這一列帶有哪些種類之證據（其最高優先者）
  `candidate_from`  = 是什麼把這一列連到某個 leaf

實測（上繳 07 §6.1）：16 個產生候選之列全部同時含 `$signal$`，
故 `anchor_kind` 恆為 `signal`，而候選之實際來源為
heading 4 列、glossary 12 列。單看 `anchor_kind` 會得出
「glossary 錨無作用」之相反結論。

**凡引用覆蓋結果者，一律以 `candidate_from` 為準**；`anchor_kind`
僅供說明該列之證據構成。

R-DM26 之錨優先序調整維持有效（heading 之 100% 存在性不宜居高位，
此點獨立成立），但其所宣稱之效果（使 `glossary_phrase` 現身於
`anchor_kind`）**不成立** —— 遮蔽者是 signal，不是 heading。
分析層之診斷有誤，此處更正。
```

## 來源：下放包 08

```
R-DM29（`kind: a03_report` 之惰性已知，不改）
R-DM24 之範例所載之 `kind: a03_report` 為 `feature.yaml` 之 paths 鍵，
非 `intake.py` 之 kind 詞彙（後者為 `swra_report`）。

實測（上繳 07 §5.2）：`a03_report` 覆寫生效、標記正確、不崩潰，
但不驅動 `intake.py` 之下游；`swra_report` 驅動下游並崩潰於
`intake.py:311` 之 `wb["Analysis Report"]`。

**維持 `a03_report`，不改為 `swra_report`。** 理由：本 feature 之
`feature.yaml` paths 已於 02 輪人工填妥，不需 `intake.py` 之下游驅動；
改為 `swra_report` 只是把「不驅動」換成「崩潰」。

A-DM21 維持 PENDING，其處置與 `intake.py:114`／`:311` 之寫死一併
留待，不與選項 D 打包。
```

## 來源：下放包 09

```
R-DM30（`data/` 下之 TSV 不得有註解行）
`features/display/data/` 下之 `.tsv`，**第一行必須是表頭列**，
不得有 `#` 或任何形式之前置行。

出處、量測條件、所依之裁決、廢止註記等移入同 stem 之
`<name>.tsv.meta.json`。產生腳本一律同時寫資料檔與 sidecar，
缺一即為腳本缺陷。

不採「保留註解行並明定慣例」：那需要每個未來讀取者都記得略過 `#`，
而其失敗形態是靜默的空資料（`csv.DictReader` 把註解讀成表頭）。
sidecar 之失敗形態是檔案不存在，會出聲。

本條回溯適用於 Display `data/` 下現有全部 `.tsv`；
其他 feature 之既有檔不回頭修改，新產出者適用。
```

## 來源：下放包 09

```
R-DM31（A-DM21 之更正：5 處出現，性質有別）
A-DM21 記 `"Analysis Report"` 於共用腳本中「寫死 5 處」。
數量無誤，性質須分：

  scripts/intake.py:63   SHEET_SIGNATURES 之判準      — 簽章表，非讀取
  scripts/intake.py:114  _swra_profile()              — 未防護
  scripts/intake.py:311  cited_documents()            — 未防護
  scripts/recon.py:568   survey_a03()                 — 未防護（本輪由選項 D 處理）
  scripts/compare_req_families.py:41  SHEET 常數      — **有 sys.exit guard**

`compare_req_families.py` 另經清查（上繳 08 §6）：無任何腳本或管線
呼叫，為手動 CLI，唯一使用紀錄為 AMFM，Display 用不到
（其用途為比較兩份競爭之需求報告，本 feature 只有一份 037）。
**自 A-DM21 之待處理清單除名。**

`intake.py:114` 在本 feature 從未被觸及（R-DM29 用 `a03_report`），
故對它之描述僅來自讀碼，非實測 —— 此限定須隨其被引用。
```

## 來源：下放包 10

```
R-DM32（`DECISIONS.md` 之權威與 `[PEI]` 之不可降格）
既有之 `features/display/DECISIONS.md` 為**權威**；
`recon.py` 產出之 `DECISIONS.new.md` 為**證據**。
合併為人工逐項，每一處分歧須於合併後之檔中留下處置與理由。

**機器不得將 `[PEI]` 降格為 `[PROPOSED]`。** 兩者之差別不在內容
而在簽核時之行為：`[PROPOSED]` 未經修改即生效（canon §4），
`[PEI]` 必須被回答。把一個無法提案之項標成已提案，
會使它在簽核時無聲通過。

實例（上繳 09 §5.2）：`spec_reference` 一項，`recon.py` 依
`spec_reference_template` 為 null 機械讀出 `[PROPOSED: None]`；
既有 `DECISIONS.md` 標 `[PEI]`，理由為 mode D 要求查得，
而 leaf → CFTS 條號之橋樑不存在（A-DM10b），**故無法提案**。
**維持 `[PEI]`。**

反向亦然：`recon.py` 所提之項若為既有檔所無（本輪之
safety attributes、batch plan、版面 revision），一律以
`[PROPOSED]` 併入，不自動升格為 `[PEI]`。
```

## 來源：下放包 10

```
R-DM33（PROXI 改為需求驅動）
PROXI 之對照**停止由供給側進行**。`proxi_candidates.tsv` 之
446 列保留為索引（其中 177 列之值域已查得），
`related_leaf` 欄停止填寫，全欄語意標 R-DM23 之 (2) 未追查，
並於 sidecar 註明「本欄不再由供給側填寫」。

改為：TC 撰寫時某 leaf 需要一個前置條件，才去 PROXI 查那一個參數。
查得即用（值域依 R-VS49 以 PROXI 表為權威）；查不得則依 R-G13
三要件登記 `LOOKUP_MISSES.md` 並開 DR。

理由：三輪嘗試（keyword 相鄰、heading、`Used by NODE` 含 ETM）
全部失敗。ETM 之實測為群內命中率 8.0%、群外 9.1%、倍率 0.88x ——
**群內低於群外**。三次失敗不是判準不夠好，是供給側沒有指向需求側
之資訊：在不知道需要什麼之前，446 列分不出來。

`docs/proxi_triage_proposal.md` 撤回，依 R-TM13 保留原文並加註。
已查得之線索（`DCSD_cfg`／`RVC_SK_PRSNT`／`Splashscreen_Type`）
保留供 Phase 2 優先查證，但不因此取得 Pre-Condition 之資格 ——
該資格仍受 §8.5 拘束。
```

## 來源：下放包 10

```
R-DM34（`estimated_test_time` 與 `spec_pdf` 之兩項記明）
(a) 036 母本之 Q 欄 `Estimated Test Time (mins)` 為版面 revision 標記，
    非管線欄位（`recon.py` 自身註解已定其性質）。
    **不加入 `feature.yaml` 之 `workbook.columns`，寫回一律不觸碰。**
    其地位與 B 欄（公式欄，R-DM15）同：存在、被辨識、不被寫入。

(b) `feature.yaml` 之 `paths.spec_pdf` 於本 feature 指向一份 `.docx`，
    欄名與內容不符；`survey_spec_text_layer()` 之 docstring 亦以 PDF
    為前提。**不改欄名**（會動到所有 feature），以 A-DM26 登記。
    引用該欄時須知其內容未必為 PDF。
```

## 來源：下放包 11

```
R-DM35（`DECISIONS.new.md` 之地位與失效）
`DECISIONS.new.md` 為 `recon.py` 某一次執行之產出，其地位為
**帶時間戳之證據**，非待處理之草稿。

三項規定：
(a) 合併完成後，檔首須加註「已於 <日期> 併入 `DECISIONS.md`，
    分歧處置見 <上繳包>」；原文依 R-TM13 保留
(b) 下次 `recon.py` 重跑產生新的 `DECISIONS.new.md` 時，
    舊者改名為 `DECISIONS.new.<日期>.md` 保留，不刪除、不覆寫
(c) `DECISIONS.md` 恆為權威（R-DM32）。任何一份 `.new.md` 皆不得
    被當作簽核標的

理由：檔名 `.new` 讀起來像「較新且待採用」，而其實際地位是
「較舊之一次量測」。名稱與地位相反之檔案會被誤用。
```

## 來源：下放包 12

```
R-DM36（已裁常數宣告入 recon_assertions）
本 feature 之已裁常數須宣告入 `feature.yaml` 之 `recon_assertions`，
使其於每次 `recon.py` 執行時被機器比對，而非靠注意力維持。

本輪宣告一項：
  functional_requirement_count: 8
（037 之 leaf 全集，recon 與自寫腳本兩側相符 —— 上繳 09 §4 第 2 項）

不宣告 `distinct_spec_sections` 與 `spec_reference_stem`：本 feature
之 `sections` 為 0、`citation_stems` 為空，宣告必然為 0 之 assertion
只會製造一個不可能失敗之檢查（canon §5a）。

`DECISIONS.md` 之 `ruled-constant assertions` 一項自
`[AUTO] 0 checked` 改為實際值，並記其宣告內容。

**Q2 若裁為選項 B 或 C 而 leaf 母體改變，須改宣告值並記其理由，
不得靜默更新** —— 靜默更新 assertion 等同取消該 assertion。
```

## 來源：下放包 12

```
R-DM37（036 母本納入 reference: 綁定）
`feature.yaml` 之 `reference:` 節現綁 dbc_b／dbc_fd／lid／proxi 四項，
**036 母本不在其中** —— 其 sha256 僅存在於 `paths.workbook` 之註解，
不被 `verify_reference_binding.py` 檢查。

而 036 母本是**寫回之標的**：其欄位配置一旦改變，
`workbook.columns` 之 15 個鍵、B 欄公式（R-DM15）、Q 欄之版面判準
（R-DM34(a)）全部受影響。

處置：於 `reference:` 節增 `workbook_master` 一項，綁其檔名與 sha256，
納入檢查範圍。

一般化：**凡其變動會使既有產出失效之素材，皆應在 `reference:` 節內。**
判準不是「它是不是參考資料庫」，是「它變了以後我們的東西還對不對」。
```

## 來源：下放包 13

```
R-DM38（`inputs/` 之素材納入綁定檢查）
R-DM37 之判準為「凡其變動會使既有產出失效之素材，皆應在
`reference:` 節內」。依該判準，`inputs/` 下之四份素材
（037／SYS2／CFTS_020／SYS3）**符合而尚未納入**：

  037    —— leaf 全集、`recon_assertions` 之 8、八條之缺值判定
  SYS2   —— 80 列母體、15 個訊號、13 個值 token、覆蓋對照全部
  CFTS_020 —— spec_mode D 之判讀基準、glossary 13 條之出處
  SYS3   —— glossary 之 DPU 一條

其 sha256 已記於 `data/materials_ledger.tsv`，**而無腳本比對**
（上繳 12 §8 第 3 項自陳）。此即 R-G23 所指之「宣告不等於保護」。

處置：於 `feature.yaml` 之 `reference:` 節增
`a03_report`／`sys2_export`／`cfts_doc`／`sys3_sysad` 四項，
與既有五項同受 `verify_reference_binding.py` 檢查。

**`reference:` 節與 `paths:` 節之分工自此明確**：
`paths:` 記「檔在哪」，`reference:` 記「檔是哪一份」。
同一個檔出現在兩節不是重複，是兩個不同的問題。
```

## 來源：下放包 13

```
R-DM39（A-DM27 之 10 項須逐項值比對）
A-DM27 所指之 10 項，本輪僅判明其「非 recon 漏測」，
**未比對其值**。判明「有測」與比對「測得相同」是兩件事，
前者不蘊含後者。

10 項為：Missing referenced specs／Header row index／
`feature.yaml` column conflicts／Regen-region segments／
Draft-region disposition／Categorization 欄與分布／
Covered by done region／Parent-child both-leaf duplications／
Priority rubric deviations／Authors present

須自 `recon.json` 與 `RECON.md` 取其值，與 `DECISIONS.md` 及自寫腳本
之對應值逐項比對，結果依上繳 09 §4 之格式列「相符／不符」。

不符者一律停並回報，不得逕以任一方為準（停止條件 20 之延伸）。

理由：上繳 09 §4 之 17 項交叉檢查是本 feature 唯一一次獨立驗證，
而它漏掉了這 10 項 —— 因為它也是以 `.new.md` 為界。
交叉檢查之涵蓋面自身未被檢查過。
```

## 來源：下放包 19（原出處 `14_mapping_audit.md`）

```
R-DM40（`Missing referenced specs` 拆為兩名）
本 feature 之 `DECISIONS.md` 中，`Missing referenced specs` 一名之下
並存兩個不同的量，拆分如下：

(a) **`Cited outline sections absent from the ruled export`**
    —— `recon.py` 之 `outline_misses`。本 feature 之值為 **0**，
    且該 0 為**空的 0**：`citation column: NOT FOUND`、`sections: 0`，
    故此檢查在本 feature 不可能失敗。
    依 canon §5a **標「未實測」，不標 PASS 亦不標 0**。

(b) **`External CFTS documents cited by the body`**
    —— CFTS_020 本文以 `{CFTSnnn-mmm}` 引用之外部文件。
    已評估者二：CFTS_009（`{CFTS009-722}`，→ DR-DM1）、
    CFTS_013（→ DR-DM4）；**另 6 份未評估**（A-DM13）。

兩者皆為有效之量，皆保留。**不得合併、不得擇一** ——
一個是「查不到缺口，因為沒有東西可查」，另一個是
「查到兩份缺件並已開 DR」，合併會使後者被前者的 0 蓋掉。
```

## 來源：下放包 19（原出處 `15_scope_settled.md`）

```
R-DM41（Q2 定案 —— 範圍取 037 之 8 個 leaf）
Pei 2026-08-25 裁定：驗證範圍取 037 之 8 個 leaf
（`SWE-DM-001`…`008`）。**選項 B（以 SYS2 之 80 列 FR 為母體）排除。**

裁定理由（Pei 原話）：「037 也界定要不要測才對啊，因為有可能 SYS2
的範圍已經判給 SYSTEM 測試，而我這裡是 software」。

即：037 為 SWE.1 之交付物，其界定者不只「測什麼」，亦包含
**「要不要測」** —— 一條 SYS 層需求未進入 037，可能正是因為它已
分派給系統測試層級，而 SWE.6 之標的是軟體。

三項隨附拘束：

(a) **SYS2 仍為內容來源**，不因本條而失效。R-DM14（值域來源）、
    R-DM17（三段解析鏈）、R-DM8 再判定（hot 行為之併讀）皆維持有效。
    037 界定「測什麼／要不要測」，SYS2 供給「怎麼測」。

(b) **借用 SYS2 某列之內容，不得使該列之驗證目的進入 TC。**
    TC 之驗證目標一律為其所屬之 SWE-DM leaf；SYS2 列僅供其訊號名、
    值域、狀態轉換之取材（§8.2.1、§8.4.2）。

(c) **揭露義務不因範圍縮小而消失**（R-DM7 之揭露義務未廢止）。
    交付時須附「037 leaf ↔ SYS2 列」之對照表，並載明：
      - 以 id 為據之對應 **0 列**（A-DM2）
      - 候選：004／005 各 4 列、007／008 各 12 列、其餘四 leaf **0 列**
      - **64 列無候選之語意為 R-DM23 之 (3) 方法界線**，
        不等於「不屬於本 feature 範圍」
      - SYS2 之 `SW/HW/System` 欄對 80 列 FR 之分布：
        System 47／HW 26／SW 7；**該欄之語意為「由誰實現」，
        非「由哪個測試層級驗證」**，故不得以其單獨論證範圍
```

## 來源：下放包 19（原出處 `15_scope_settled.md`）

```
R-DM42（Q3 定案 —— req_id 形態）
Pei 2026-08-25 裁定：`req_id` 取 **`SWE1-DM-{nnn}`** 形態
（037 `SYS2 Traceability` 分頁之寫法），填入 036 之 D 欄
`Requirement or Design ID`。

八個值為 `SWE1-DM-001` … `SWE1-DM-008`。

三項隨附：
(a) `SWE-DM-{nnn}`（`SWE1 Requirements` 分頁之寫法）**不入任何交付欄位**；
    其於 `reasoning`、`ANOMALIES.md`、內部資料檔中之引用不受限制，
    但須與 `SWE1-DM-` 明確區分，不得混用。
(b) **A-DM1 不因本裁定結案** —— 該條記的是「037 兩個分頁對同一物件
    使用兩種寫法」，屬上游文件內部不一致，與「我們採哪一個」是兩件事。
    仍須向上游反映。
(c) `recon_assertions` 之 `functional_requirement_count: 8` 不受影響
    （leaf 數未變，僅書寫形態改變）。
```

## 來源：下放包 19（原出處 `15_scope_settled.md`）

```
R-DM43（DR-DM8 定案 —— 以訊號名稱為主）
Pei 2026-08-25 裁定：037 之 `DISPLAY_ON`／`DISPLAY_OFF`
與 SYS2／DBC 之 `DISP_ON`／`DISP_OFF`，**以訊號名稱為主**。

即：TC 之 Procedure 與 Expected Result 一律採 `DISP_ON`／`DISP_OFF`
（DBC `DCSD_DISP_STAT` 之 `VAL_` 標籤側）。

本條與 R-6 之既有規定一致：「訊號名以 DBC 為準；來源文件與 DBC
大小寫不一致時，步驟採 DBC 寫法，verbatim 上半仍保留來源原文」。
**037 原文於 `test_item` 上半之 verbatim 摘句中仍寫 `DISPLAY_ON`**，
不得改寫 —— 本條規制的是步驟與預期結果，不是引文。

DR-DM8 **結案**。A-DM18 之該項隨之結案；A-DM18 之其餘部分
（八條無值、八條併句）不受影響。
```

## 來源：下放包 19（原出處 `15_scope_settled.md`）

```
R-DM44（DR-DM7 結案 —— 需求已由 R-DM33 消滅）
`forms/PROXI_HDCC27_R3_20250424.xlsx` 經實測為**格式／標準文件**
（`Cover`：`27MY HDCC SPECIFIC PROXI TABLE`、`Support Document`；
`Header`：`HDCC27 - Draft`），不含任一具體車輛之已填值，
亦不載本專案之 VF 代碼。

DR-DM7 原求「本專案之 VF 代碼，或已填值之 PROXI 實例檔」，
其目的為**收斂 446 列之供給側母體**（`Used by NODE(VFXXX)` 之篩選）。
**該目的已由 R-DM33 消滅** —— PROXI 改為需求驅動後，
不再需要對 446 列分類，只在某 leaf 需要某參數時查該一個參數。

處置：**DR-DM7 結案**，理由記為「所求之用途已由 R-DM33 取消，
非取得所求之物」。A-DM20 改標 RESOLVED-BY-SCOPE-CHANGE，
不標 RESOLVED。

**重開條件**：若 Phase 2 之逐 leaf 查詢中，某參數之值域在
PROXI 中依 VF 而異，則 VF 代碼重新成為必要，DR-DM7 以新編號重開。
```

## 來源：下放包 19（原出處 `16_sysad_allocation.md`）

```
R-DM45（SYS3 之地位：軟體分派之 id 層級證據）
`SYS3_CFTS_020_display_…SYSAD_v1.0.docx` 表 31（`System Requirement
ID` → `SYSAD-ID` → `% of allocation`）為本 feature 目前**唯一**
id 層級逐字之軟體分派證據。

實測（分析層 2026-08-25，執行層須獨立重算）：
  9 個 SYSAD 元件、31 個相異 `SYS-RA-DM-*` id、分派比例皆 100%
  31/31 落在 SYS2 之 80 列 FR 母體內，0 查無、0 非 FR
  16 個候選列中 12 個在分派表內（未在者 4 個皆為 `SYS2-RA-*` 區段）

用途二項：
(a) 供 R-DM41(c) 之揭露 —— 以「80 列中 31 列明確分派至軟體元件」
    取代（並非廢止）`SW/HW/System` 欄之 System 47／HW 26／SW 7。
    兩個量並列揭露，因其回答的是不同的問題。
(b) 供 Phase 2 判定某 SYS2 列之內容是否可取用於某 leaf 之 TC ——
    **僅為佐證，非授權**。取用之正當性仍依 R-DM41(a)(b)。

三項不得為之：
(1) 不得以 SYSAD 元件名與 037 之 Sub Categorization 語意相近
    建立 leaf ↔ 元件映射（R-DM13／R-G27）
(2) 不得以「未出現於分派表」推論該列不屬軟體範圍 ——
    未出現之 49 列其成因未量測
(3) 不得以本表取代 037 之範圍界定（R-DM41 已定範圍為 8 leaf）
```

## 來源：下放包 19（原出處 `16_sysad_allocation.md`）

```
R-DM46（`Safety attributes` 之依據更正）
`DECISIONS.md` §3 之 `Safety attributes (ASIL/FTTI)` 一項，
其敘述「受裁之來源不帶 ASIL／FTTI 欄」**須更正**。

實測：037 確無該欄；**SYS3 表 6 有 `ASIL Level` 欄，31/31 為 `QM`**，
另有 `SG ID`／`FSR ID` 兩欄，兩欄之非空列數皆為 **0**。

更正後之敘述：
  037（受裁之範圍界定來源）不帶 ASIL／FTTI 欄；
  SYS3 帶 `ASIL Level` 欄，其值於 31 個被分派之需求上皆為 `QM`，
  且 `SG ID`／`FSR ID` 全空 ——
  即安全目標與功能安全需求未掛於這些條上。
  故安全層不進入追溯鏈。

`[PROPOSED]` 之結論不變，**依據由「查不到」改為「查到了，答案是沒有」**。
依 R-G19，理由與數字須分別成立；一個正確的結論配一個錯誤的理由，
會使下一個人依那個理由去推論別的事。
```

## 來源：下放包 20

```
R-DM47（`paths:` 與 `reference:` 之路徑基準不同）
`feature.yaml` 之兩節其路徑基準不同，宣告時不可互抄：

  `paths:`      —— 基準為 **feature 目錄**（`recon.py` 之
                    `resolve_glob()`）。宣告 repo 相對路徑會使
                    `recon.py` 以 `input not found` 中止
  `reference:`  —— 基準為 **repo 根**（`verify_reference_binding.py`）

`forms/` 之共用素材若須同時入兩節，依 `home` 之既有先例：
複本置於 `features/<f>/inputs/`（SHA 須與 `forms/` 之正本逐檔相符），
`paths:` 寫 `inputs/…`，`reference:` 寫 `features/<f>/inputs/…`。
`inputs/` 由 feature 之 `.gitignore` 排除，複本不入 git。

本條補 R-DM38 之未涵蓋處：該條界定兩節之**用途**
（`paths:` 記檔在哪、`reference:` 記檔是哪一份），**未及基準**。

實例（上繳 19 §3.1）：Pop Up List 兩檔首次以 `forms/…` 宣告於
`paths.popup_list`，`recon.py` 當場中止。
```

## 來源：下放包 20

```
R-DM48（值標籤缺 DBC 對應時之寫法）
規格（SYS2／CFTS）所載之值標籤，其**逐字**解得 DBC `VAL_` 列舉者，
依 §8.7.5(a) 寫入 `= <raw> (<label>)`；**解不得者不寫入訊號值**，
ER 改驗規格所載之**可觀察行為**，規格側之值標籤記入 `reasoning`。

**不得以語意相近或前綴規則外推。** `DCSD_DISP_STAT` 之六個值中，
唯 `DISP_HOT`（raw 4）與規格側逐字相符；`[DISP_REAR_CAMERA]` 對
`RR_CMRA`（raw 3）證明不存在單純之 `DISP_` 前綴規則 ——
**規則在六個值裡就不一致，故不可外推**。

本條與 §8.7.5(g)（R-13：規格所載訊號名 DBC 查無時保留原文，
不代以語意相近之他訊號）同一理路：**代入會改變 TC 之驗證對象。**
差別在於 (g) 規制名稱、本條規制值。

適用之前提：該 leaf 之需求標的為可觀察行為。若某需求之標的
**就是**匯流排上的某個值，則其值不可得即為真阻塞，
應 deferred 並開 DR，不得以行為描述頂替。

配套：**DR-DM9** 已開（HIGH）。取得並列出處後依 R-DM22 之三要件
建值標籤 glossary，屆時得於既有 ER 增列訊號值 —— 增列不改變
其行為驗證，故不構成回修。
```

> **補充（下放包 23）**：見本檔末〈來源：下放包 23（R-DM48 之補充）〉節之
> `R-DM48 之補充（跨訊號不可外推）`。**原條文依 R-TM13 不刪不改。**
> 補充置於檔末而非緊接本條之下，理由見上繳 23 §1.1（實測：
> 緊接置放會使 `transcribe_rulings.py` 之順序驗證由「全數相符」轉為
> 「有不符」並 exit 1）。

---

## 來源：下放包 22

```
R-DM49（負向條之 ER：「不發生」得自觸發條件未成立推得）
負向／邊界條之 ER 若為「某事不發生」（無 popup、訊號不為某值、
狀態不轉換），其證據形態與正向條不同：規格通常只寫「條件成立時
做什麼」，不寫「條件不成立時不做什麼」。

**判定：可寫。** 但須滿足三項：
(a) 其所否定之行為，其**正向出處逐字存在**（即「條件成立則發生」
    有明確出處），否定係自「條件未成立」推得；
(b) 該否定**不得引入任何新的值**——只能否定正向所載之值
    （✓ `is not 4 (DISP_HOT)`；✗ `should be 0 (OFF)`，後者需 DR-DM9）；
(c) 於 `reasoning` 或 `split_reason` 記明其證據強度與正向 ER 不同。

理由：若不許此形態，則一切負向條皆不可寫，而 canon §9 第 11 項
與 §7 明文要求 supported 配負向。兩項要求不可兼得時，
**選擇留下並揭露**，不選擇沉默移除。

實例（上繳 21 §八第 3 項，執行層自陳）：#4 之
`No popup is shown on the display`——`{4820289}` 只說越過門檻時
做四件事，未說未越過時不做。執行層判其可寫並記明證據強度差異，
本條將該處置定為規則。
```

---

## 來源：下放包 23（R-DM48 之補充）

```
R-DM48 之補充（跨訊號不可外推）
R-DM48 原載：規格值標籤逐字解得 DBC `VAL_` 者始寫入訊號值，
不得以語意相近或前綴規則外推，理由為「同一訊號之六個值裡規則就不一致」。

**本條補一項更強之理由：同一標籤跨訊號亦不一致。**

實測（上繳 22 §6.2.1，A-DM34）：
  `DCSD_DISP_STAT`       : `4 "DISP_HOT"`
  `FPDM_DISP_STAT`       : `3 "DISP_HOT"`
  `TGW_FPDM_DISP_STATSts`: `3 "DISP_HOT"`

即：即使某標籤在某訊號上已逐字解得，**該對應不得搬至另一訊號**。
值之解析一律以 `MESSAGE.Signal` 兩半皆相等為選定判準
（`signal_resolution.py`，04 輪之修正），不得以訊號名單獨匹配。

本補充不改 R-DM48 之處置規則，只加強其理由與適用範圍。
```

---

## 來源：下放包 24

```
R-DM51（Associated Display 與 DCSD 為不同標的，其值不得互相代入）
CFTS013（`Radio Error Management - Associated Display`）之需求標的為
**Associated Display**（觸控螢幕整合於 HU 模組者）；
CFTS_020 `1.11.2.2` 之需求標的為 **DCSD**
（Disassociated Center Stack Display，外部觸控螢幕模組）。

`{CFTS013-930}` 逐字定義該區分（`_ADspl` vs `_DDspl`）。

三項拘束：
(a) CFTS013 之門檻（50／51–55／56–<60／>=60 degrees C）與
    CFTS_020 之門檻（85 degrees C）**分屬兩個標的**，
    不得互相代入、不得以其一補其二之缺（§8.4.1）。
(b) `{CFTS013-951}` 之亮度規則（每高於 50 一度降 5%）為 Associated
    Display 之規則。**DCSD 側之亮度降低數值仍屬未給**
    （上繳 22 之 B4 對 DCSD 仍成立）。
(c) 引用 CFTS013 之任一值時，須於 `reasoning` 逐字記其標的為
    Associated Display，並記其與本 TC 標的之關係。

本條為本 feature 第四個命名近似陷阱（前三：037 檔名連字號 R-DM11、
CFTS043 為 HVAC A-DM31、SYS3 無 `SYS-RA-DISP`）。
**其形態最隱蔽** —— 檔名、章節名、門檻語彙、popup id 全部相似，
差別只在 `Associated` 與 `Dis`associated 一字。
```

```
R-DM52（本檔為 CFTS013 之部分分析，不得視為全文）
`SYS2_CFTS013_…xlsx` 之 `Document ID` 為 32 個值，
**不含 DR-DM4 所求之 `629`／`633`／`952`** ——
三者僅出現於 `r8`（`CFTS013-752`，Category = Information）之
修訂履歷自由文字內，非 `Document ID` 欄之值。

即：**「該 id 之字串出現於檔內」不等於「該需求存在於檔內」。**
凡查證某條號是否到手，須查 `Document ID` 欄，
不得以全檔子字串命中為據（R-G27 之逐字原則於本處之應用）。

DR-DM4 **維持 OPEN**，其標的不變（CFTS013 之 `629`／`633`／`952`）。
```

---

## 來源：下放包 25

```
R-DM53（`deferred` 項改為物件，明載其英文 token）
`batch_context.md` 與 `generated/*.json` 之 `deferred` 陣列，
其每一項改為物件，必含四鍵：

  leaf_id      該 deferred 項所屬之 leaf
  token        R-G33(c) 檢查所用之英文 token，**逐字**
  reason       其被 deferred 之理由（中文可）
  blocking_dr  阻斷之 DR 編號；無則 null

`token` 為**寫 deferred 項時**決定之值，由寫的人負責，
並於上繳包中可見。R-G33(c) 之檢查改為「括號下半是否含該項之 `token`
逐字」—— 檢查成為純字串比對，**無判斷成分**。

理由（上繳 23 之 B11）：原陣列為自由文句，檢查者須自中文標的
對譯英文 token 方能比對。本批三項標的具體（popup／shutdown／
multi-stage）故對譯無爭議，**而「對譯無爭議」本身是檢查者之判斷，
無第二來源核對**。措辭較抽象時，該對譯即成判斷而非量測。

本條與 B9（停止條件 58 之自訂詞表）同類：
**一個看起來是機器判準之檢查，其詞表是人給的。**
差別在本條可結構性解決 —— 把詞從檢查端移到宣告端。

現行三項之 `token` 依上繳 23 §2.1 之對譯落定，
**不重新決定**（其已通過複驗且三條之揭露句已依其補寫）。
```
---

## 來源：下放包 27

```
R-DM54（deferred 之解除以標記為之，不以刪除為之 —— STALE 修法乙案）
`deferred` 陣列（R-DM53 之四鍵物件）自本條起**只增不減**。
項之解除不刪除該物件，改增三鍵：

  lifted      true
  lifted_at   解除日期（YYYY-MM-DD）
  lifted_by   解除依據（DR 答覆／裁定之編號，逐字）

`check_disclosure.py` 之兩向據此重定義：
  MISSING —— 未解除項（無 `lifted` 或 `lifted: false`）之 token
             不見於其 leaf 各 TC 之括號下半
  STALE   —— **已解除項**之 token 仍見於其 leaf 任一 TC 之括號下半
  跨 leaf 誤置之檢查維持既有行為

理由（上繳 26 §5.2 之確診）：原實作之 STALE 候選集自當前陣列建，
被整個移出陣列之 token 從此無人檢查 ——
**它抓得到的，正好不是 R-G33(d) 要防的那一種**（deferred 解除之
實際形態即是移出）。乙案把「解除」變成一次**寫入**：token 永遠
在候選集內，且解除之時點與依據成為可查之紀錄 —— 與本案每一條
機器保證（sidecar、綁定、核對表、順序驗證）同一理路：
**留下可比對之痕跡；刪除本質上不留痕跡。**

規模之界：本 feature 8 leaf，deferred 項之堆積以每 leaf 三面向計
不逾二十餘項，不構成代價。他 feature 沿用本條時若逾百項，
屆時再議歸檔機制，**不得預先為此複雜化**。

配套：本條生效後，R-G25 之誘發測試須以「標 lifted」之形態重跑
一次並 PASS（上輪以「移除」形態測試 FAIL，即本條之立條原因）。
```

---

## 抄錄核對表

| # | 條號 | 來源包 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 1 | R-DM1 | 01 | 337 | `f8181c4bd16d0ca9` | 是 |
| 2 | R-DM2 | 01 | 488 | `231830d8d5cda432` | 是 |
| 3 | R-DM3 | 01 | 739 | `dc68c2bbe20556b5` | 是 |
| 4 | R-DM4 | 01 | 367 | `25f632b137ac858d` | 是 |
| 5 | R-DM5 | 01 | 607 | `19bfd2399bb2aad2` | 是 |
| 6 | R-DM6 | 01 | 216 | `1d8eb69193c73a8b` | 是 |
| 7 | R-DM7 | 01 | 498 | `b967b09652669c91` | 是 |
| 8 | R-DM8 | 01 | 559 | `e6ff38e7f7472ac1` | 是 |
| 9 | R-DM2 | 02 | 329 | `eecfc177bae79ee9` | 是 |
| 10 | R-DM2′ | 02 | 406 | `c4f6853689107fd1` | 是 |
| 11 | R-DM9 | 02 | 397 | `ac0b6373fe6b919d` | 是 |
| 12 | R-DM10 | 02 | 519 | `4a0756e807a1d6ef` | 是 |
| 13 | R-DM11 | 02 | 193 | `381220990cd1e12e` | 是 |
| 14 | R-DM12 | 03 | 235 | `78599eabe092774d` | 是 |
| 15 | R-DM13 | 03 | 355 | `2b5a77ed7b7ab774` | 是 |
| 16 | R-DM14 | 03 | 269 | `ea998f51f74c258f` | 是 |
| 17 | R-DM15 | 03 | 171 | `135cf28886d145e2` | 是 |
| 18 | R-DM16 | 04 | 462 | `4ab4b941b20a6769` | 是 |
| 19 | R-DM17 | 04 | 579 | `c575758943f0fe02` | 是 |
| 20 | R-DM18 | 05 | 855 | `8db2178577564199` | 是 |
| 21 | R-DM19 | 05 | 681 | `0939e0a7878c49b8` | 是 |
| 22 | R-DM20 | 05 | 576 | `6caf121fb4def656` | 是 |
| 23 | R-DM21 | 05 | 270 | `d384fa5b99e3888a` | 是 |
| 24 | R-DM22 | 06 | 909 | `cdb1b47b562e1a61` | 是 |
| 25 | R-DM23 | 06 | 466 | `96a2c13ba436a16d` | 是 |
| 26 | R-DM24 | 07 | 486 | `5ee430b93d0ece9f` | 是 |
| 27 | R-DM25 | 07 | 628 | `6ef20babc361b7da` | 是 |
| 28 | R-DM26 | 07 | 468 | `dfc9bead9640f247` | 是 |
| 29 | R-DM27 | 07 | 472 | `3d2e2e87dfa640ec` | 是 |
| 30 | R-DM28 | 08 | 518 | `71aca3f7ad551b37` | 是 |
| 31 | R-DM29 | 08 | 482 | `387d90ad885f0c9e` | 是 |

核對方法：抄錄後自 `RULINGS.md` 反向抽取各 fenced 區塊，與下放包原檔
之對應區塊逐字元 `==` 比對並比對 SHA256；**50 條全數相符**（01 包 8、02 包 5、03 包 4、04 包 2、05 包 4、
06 包 2、07 包 4、08 包 2、09 包 2、10 包 3、11 包 1、12 包 2、13 包 2、
19 包 7、**20 包 2**）。

> 19 包為合併包：14–18 五包之編號作廢，其條文由 19 包之執行序抄錄，
> 各條之「原出處」逐條註明於其標題行。

> 自下放包 09 起，核對表由 `scripts/transcribe_rulings.py` 直接產出
> markdown 貼入上繳包（R-G20：報告中之摘要數字須為機器輸出）。

> 下放包 07 之 `R-G17` 為全域條文，抄入 `docs/fw036/RULINGS_LEDGER.md`。
>
> 核對式之注意事項（累計兩則）：
> (1) `R-DM\d+（` 匹配不到 `R-DM2′`（編號後接 `′`）；
> (2) 下放包 07 起出現 ` ```yaml ` 之帶資訊字串圍籬，
>     `^```\n` 之式子會錯配區塊界線，須改用 `^```(\w*)\n`。

> 下放包 06 之 `R-G16` 與 `R-G13 補充` 為全域條文，抄入
> `docs/fw036/RULINGS_LEDGER.md`，不重複於本檔。
>
> 核對式之注意事項：`R-DM\d+（` 匹配不到 `R-DM2′`（編號後接 `′`），
> 反向驗證須以各包原本之抽取方式為之（上繳 05 §1 之教訓）。

> 下放包 05 之 `R-G15` 為全域條文，依該包 §四之指定抄入
> `docs/fw036/RULINGS_LEDGER.md`，不重複於本檔。

### 廢止與取代之對照（原文一律依 R-TM13 保留於上方，不刪除、不改寫）

| 被廢止／修正者 | 取代者 | 出處 |
|---|---|---|
| R-DM7 之「Description 文字（bag-of-words）」一項 | R-DM13 | 下放包 03 |
| R-DM14 之「兩段表述」與其所引之「相異值 token 9」 | R-DM17（三段鏈）、R-DM16→R-DM18 | 下放包 04、05 |
| **R-DM16（全條廢止）** —— 其 regex `\[([^\]]+)\]` 與所載之「13」不相容 | **R-DM18**（寬式扣除含 `:` 者） | 下放包 05 §2.1 |
| R-DM7 之揭露義務、「不得裁定範圍」 | **未廢止，仍有效** | — |
| R-DM8 之缺值範圍「四處」（003/004/005/006） | **R-DM27**（八條全稱；禁止回填之規定不變） | 下放包 07 |
| R-DM22(c) 之「不得再放寬一層」 | **未廢止，仍有效**；R-DM25 所開放者為比對前對兩側同施之宣告式正規化，非放寬 | 下放包 07 §1.2 |
| 錨優先序中 heading 之第三位 | **R-DM26**（降為倒數第二） | 下放包 07 |
| R-DM26 所宣稱之效果（使 `glossary_phrase` 現身於 `anchor_kind`） | **R-DM28 更正**：遮蔽者是 signal 非 heading；R-DM26 之調整本身仍有效 | 下放包 08 §1.3 |
| R-DM48 之理由「同一訊號之六個值裡規則就不一致」 | **R-DM48 之補充（下放包 23）**：跨訊號亦不一致；處置規則不變，理由與適用範圍加強。原條文不刪不改 | 下放包 23 §三 |
| PROXI 之供給側對照（keyword／heading／ETM 三種嘗試） | **R-DM33**：改為需求驅動；`docs/proxi_triage_proposal.md` 撤回（原文保留） | 下放包 10 §三 |
| 分析層於 02 輪自填之 `Test Set table`／`profile [OVERRIDE]` 兩項 `[PROPOSED]` | **R-G24**：marker 衝突取較嚴者 → 改為 `[PEI]`；**機器是對的** | 下放包 12 §二 |

> 下放包 04 之 `R-G12`／`R-G13`／`R-G14` 為全域條文，依該包 §四之指定
> 抄入 `docs/fw036/RULINGS_LEDGER.md`，不重複於本檔。
> R-DM16 撤回「相異值 token 9」改為 13；R-DM17 修正 R-DM14 之兩段表述
> 為三段解析鏈。二者所修正之原條文依 R-TM13 原文保留於上方。

> R-DM13 廢止 R-DM7 之「Description 文字（機械 bag-of-words 重疊）」一項。
> R-DM7 本身仍為有效條文（其揭露義務與「不得裁定範圍」不受影響），
> 依 R-TM13 原文保留於上方，不刪除、不改寫。
