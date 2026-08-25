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
之對應區塊逐字元 `==` 比對並比對 SHA256；**31 條全數相符**（01 包 8 條、
02 包 5 條、03 包 4 條、04 包 2 條、05 包 4 條、06 包 2 條、07 包 4 條、
08 包 2 條）。

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

> 下放包 04 之 `R-G12`／`R-G13`／`R-G14` 為全域條文，依該包 §四之指定
> 抄入 `docs/fw036/RULINGS_LEDGER.md`，不重複於本檔。
> R-DM16 撤回「相異值 token 9」改為 13；R-DM17 修正 R-DM14 之兩段表述
> 為三段解析鏈。二者所修正之原條文依 R-TM13 原文保留於上方。

> R-DM13 廢止 R-DM7 之「Description 文字（機械 bag-of-words 重疊）」一項。
> R-DM7 本身仍為有效條文（其揭露義務與「不得裁定範圍」不受影響），
> 依 R-TM13 原文保留於上方，不刪除、不改寫。
