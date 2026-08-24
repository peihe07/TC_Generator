# RULINGS — Power Moding (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Power Moding 之裁決權威；
跨 feature 條文承接時註明來源包。

來源包：`docs/handoff/01_intake.md` §二
（SHA256 `0f11160c8efcac11423a43c2cc86fe387ce99155b4366c6a4600fbfe0b914838`）
抄錄日：2026-08-22

---

## R-PMH1 —— 範圍 = 037 `Functional Requirement` 全集

```
R-PMH1（範圍）
本 feature 之驗證範圍為 037「Analysis Report」分頁中 `Categorization`
欄逐字為 `Functional Requirement` 之列全集，不以 `FROP /
(Feature Rollout Plan)` 欄之值作範圍過濾。

判準為可測：以 `Categorization == "Functional Requirement"` 掃描全表求
其全集，另以「全表列數 − Heading 列數 − 表頭與抬頭列數」求餘數驗證其
為空（R-G10）。分析層 2026-08-22 之實測值為 48（Heading 8），供對照，
不得以該數字代替重算。

交付夾名 `Disclaimer screen` 為 FROP 標籤，不縮減本範圍；FROP 欄之值
於本 feature 之用途僅為 framework Layer 2 之候選輸入（見 R-PMH5），
不作為 in/out of scope 之判準。
```

## R-PMH2 —— feature 身分與 `test_group`，交付夾名不入欄位

```
R-PMH2（feature 身分與 test_group）
`feature` 為 `Power Moding`，slug 為 `power_moding`，`test_group` 為
`Power Moding`（規格標題之模組名）。

交付夾名 `Disclaimer screen` 不進入 `test_group`、不進入任何 TC 欄位，
僅記於 `feature.yaml` 之交付路徑註解。

依據：Comfort R-C6 之同型處置（交付夾 `Climate Control Interface`，
`test_group` 為 `Comfort`）。
```

## R-PMH3 —— 與 `features/power` 之分離（欄位／前綴／glob 三項）

```
R-PMH3（與既有 `power` feature 之分離）
`features/power`（test_group `Power Management`，來源 CFTS009／CFTS010，
需求 id 形態 `SWE-PM-nnn`）與本 feature 為不同需求族、不同交付物、
不同客戶交付夾，**任何產物不得跨用**。

具體拘束三項：
(a) 欄位對應不得沿用 `features/power/feature.yaml` 之 `workbook.columns`，
    須自本工作簿 r9 表頭逐欄實測後書寫；
(b) 本 feature 之裁決前綴為 `R-PMH`、異常前綴為 `A-PMH`、
    資料請求前綴為 `DR-PMH`，不與 `R-P` / `A-PW` / `DR-PW` 共用序號；
(c) 任何以 `features/power*` 形態之 glob 自本日起會同時命中兩個目錄；
    腳本、備份、掃描與 `git add` 之 pathspec 一律寫全名，不用萬用字元。
```

## R-PMH4 —— 素材台帳之到齊定義

```
R-PMH4（素材台帳之到齊定義）
素材之「到齊」定義為：清單每項附其檔案系統絕對路徑與 SHA256，且
`shasum -c` 對得上（G-L）。「檔名相符」「大小相同」皆不構成到齊。

本 feature 之素材來源目錄為
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Disclaimer screen/`
（唯讀，不得寫入）。搬入 `features/power_moding/inputs/` 者為複本，
搬入前後各記 SHA256 並登入台帳（G0）。
```

## R-PMH5 —— 既有 48 列非 done region，視為草稿列

```
R-PMH5（工作簿既有 48 列之處置）
本工作簿之資料列 10–57 共 48 列已填入 B/D/G/H/I/L/M/N 八欄，其內容為
037 對應欄位之機械搬運（D←SWE-Requirement ID、G←FROP、H←Requirement
Title、I←Requirement Description、L←Verification Method、
M←Verification Criteria、N←HMI Source ID）。

該 48 列**不是 done region**，不具 style authority：其 `Test Case Author`
欄（AB）48 列皆空、`Test Case ID`（F）48 列皆空、`Test procedure`（L）
48 列皆無編號步驟，不滿足 canon §2 之「qualifying done row」三項。

處置：視為**待改寫之草稿列**，其現況以 content-hash 立為基線，供改寫前後
比對；style authority 依 canon §3 之 BLANK 回退鏈決定，**不得取自該 48 列**
（§9.1 通則 4：BLANK 之 style authority 不得取本管線自身或未經核可之產出）。
```

## R-PMH6 —— G/H 兩欄之處置延後至 Phase 3

```
R-PMH6（G/H 兩欄現值之處置延後）
現況 G 欄（Test Group）之值為 FROP 標籤、H 欄（Test Set）之值為 037 之
Requirement Title（完整句子，違反 canon §4.2「短名詞片語、非句子」）。

二欄之最終值屬 framework Layer 1／Layer 2 之產物，於 Phase 3 定版；
**Phase 0/1 不得改動該二欄**，僅登記現況。FROP 欄之 13 個相異值得作為
Layer 2 之候選輸入之一，與規格目次取交集後再判granularity（canon §4.1.2）。
```

> **執行層勘誤附註（2026-08-22，A-PMH01）** —— 上列 R-PMH6 條文中之
> 「FROP 欄之 13 個相異值」，執行層實測為 **12**。`13` 係對 037 全 56 資料列
> 取 `set()` 而未排除 8 個 Heading 列之空 `FROP` 欄所致（空值被計為一類）。
> handoff §3.1 自身所列之 FROP 分布明細即為 12 項（合計 48，餘數 0），
> 與執行層實測逐項逐數相符。
> **原條文不改字（R19-2）**；往後引用一律以 12 為準。待 Pei 核可。

---

## 抄錄逐條核對表（步驟 2）

抄錄方式：以 `re.findall` 自 handoff §二之 fenced block 直接取出字串寫入，
未經人工重打，故不存在轉錄漂移之可能；下表之 SHA256 為
**handoff 原文區塊**與 **RULINGS.md 落地區塊**各自獨立再抽取後計算。

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH1 | 範圍 = 037 `Functional Requirement` 全集 | 441 | `468fc43132ac1b9f` | `468fc43132ac1b9f` | ✅ 逐字相符 |
| R-PMH2 | feature 身分與 `test_group`，交付夾名不入欄位 | 287 | `19f57d23b1cf9800` | `19f57d23b1cf9800` | ✅ 逐字相符 |
| R-PMH3 | 與 `features/power` 之分離（欄位／前綴／glob 三項） | 464 | `84acd49a1fc7f6ae` | `84acd49a1fc7f6ae` | ✅ 逐字相符 |
| R-PMH4 | 素材台帳之到齊定義 | 277 | `04d87eb139a11e2b` | `04d87eb139a11e2b` | ✅ 逐字相符 |
| R-PMH5 | 既有 48 列非 done region，視為草稿列 | 555 | `e589281f93426f27` | `e589281f93426f27` | ✅ 逐字相符 |
| R-PMH6 | G/H 兩欄之處置延後至 Phase 3 | 278 | `5bb6ebe395b25187` | `5bb6ebe395b25187` | ✅ 逐字相符 |

---

# 下放包 02 —— 母本改定、workbook_state 改判

來源包：`docs/handoff/02_baseline_switch.md`（SHA256 `a820199d7fefe707a81882d993e375c96a68e06ab372733a6b2142e43580fa65`）§二
抄錄日：2026-08-23

## R-PMH7 —— 交付母本為 forms ext；客戶那份降為來源複本

```
R-PMH7（交付母本）
本 feature 之交付基底為 `forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果
_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`
（SHA256 `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`），
即 R-G1 所定之全域母本，不另行例外。

客戶交付夾之 `…_SWQT_PowerModingHMI_20260819.xlsx`
（SHA256 `2be63febf005dd87ad302b78989ee7800a1a90c60f1f6673f9b455e664625a54`）
自本條起之身分為「需求對應之來源複本」，其用途限於 037→036 之 leaf 對應
查核與其三個附屬分頁之內容取得，**不作交付基底、不作版面依據、
不作 style authority**。

判準：交付副本之 r9 表頭欄數為 34（A–AH），`Estimated Test Time (mins)`
恰出現一次。出現兩次或欄數為 35 者，即非本條所定之母本。
```

## R-PMH8 —— `workbook_state` = `BLANK`；撤回 `PREFILLED_DRAFT`

```
R-PMH8（workbook_state）
`workbook_state` 為 `BLANK`。

Q1 所核可之 `PREFILLED_DRAFT` 提案**撤回**。撤回之依據為 R-PMH7 更換交付
基底，致該狀態所描述之 48 列預填不存在於交付標的，**非原判定有誤** ——
01 包 §4.3 對客戶那份之逐列判定（filled 48 / qualifying-done 0）仍然成立，
且為本條之前提。

丟棄該 48 列之資訊損失為零：01 包 §4.4 已逐格驗證其 336/336 逐字等同 037
之七欄，037 本身為本 feature 之權威輸入且已在 `inputs/` 內。

連帶：`done_region` 不適用（`author_value: null`）；write-back 為自首資料列
（r10）append；done invariant 不適用。
```

## R-PMH9 —— 欄位對應作廢重測，四方交叉佐證

```
R-PMH9（欄位對應重測）
01 包 §4.2 之 `16/16` 欄位對應**作廢** —— 其量測對象為 R-PMH7 所排除之
離群版面（35 欄，priority Q / design_method S / author AB / remarks AI）。

重測須對 R-PMH7 之母本 r9 表頭進行，並與下列三份**已交付件**交叉佐證
（G-H：先查他 feature 之交付件，且須先確認母本同一）：

  User Profiles 20260820、Comfort 20260817、Time Management 20260822

四者（母本 ＋ 三份交付件）之 r9 表頭須逐欄相等；不相等者停並回報，
不得擇一採用。
```

## R-PMH10 —— D3／D4／D5 一律留空

```
R-PMH10（前言欄之留白）
工作簿 `Test Case Specification 測試用例規範` 分頁之
`D3 審查者` / `D4 目的` / `D5 範圍 Scope` 三欄**一律留空**。

依據為實測：已交付件 User Profiles 20260820、Comfort 20260817、
Time Management 20260822、Power Management 20260821 四份之該三欄皆空，
R-PMH7 之母本亦空 —— 語料 5/5 無一填寫。

不得自擬字串填入。若日後客戶要求填寫，其字串由 Pei 給定，本條屆時另立
新條取代，不以「補上」之名逕行填寫。
```

> **已於 2026-08-24 重裁定案，見 R-PMH27（05b 包）。`[PEI-REOPEN]` 標記撤除。**
>
> **本條之結論（D3／D4／D5 一律留空）維持不變；其依據段由 R-PMH27 更換。**
> 原依據句「已交付件四份之該三欄皆空，母本亦空 —— 語料 5/5 無一填寫」
> **作廢**（母體未定義，04 包 §2、05 包 §二）。
>
> 語料之四次演進（供追溯，**原條文不改字**）：
>
> | 母體判準 | 母體 | `D3` 空 | `D4` 空 | **`D5` 空 / 非空** |
> |---|---|---|---|---|
> | 原依據（母體未定義） | 「5」 | 5 | 5 | 5 / **0** |
> | R-PMH19（04 包） | 11 | 11 | 11 | 8 / **3** |
> | R-PMH24（分析層 05 §三） | 16 | 16 | 16 | 9 / **7** |
> | **R-PMH24（執行層實測，上繳 05 §2）** | **17** | **17** | **17** | **9 / 8** |
>
> `D3`／`D4` 於四次量測皆全空。**R-PMH27 明載本裁定「不是多數決」**，
> 故 16 與 17 之差不影響其結論；母體之定案繫於
> `Engineering Mode/App Team Effort/` 之身分，待 Pei 裁（上繳 05 §9 第 2 項）。
>
> **R-PMH10 之末句效力維持**：日後若客戶要求填寫，其字串由 Pei 給定並
> 另立新條取代，**不得以「補上」之名逕行填寫**。

## R-PMH11 —— `MANIFEST.sha256` 入版控

```
R-PMH11（素材雜湊檔之版控）
`features/power_moding/inputs/MANIFEST.sha256` 須入版控。

實施方式：於 `features/power_moding/.gitignore` 之 `inputs/` 排除規則後
增列否定規則 `!inputs/MANIFEST.sha256`，並以 `git check-ignore -v` 對該
路徑實測其不再被忽略（唯讀指令，執行層可執行）。

素材檔本身（四份）維持不入版控。本條解 A-PMH05 所指之 §9.1 通則 9 衝突，
其適用範圍限於本 feature；`scripts/new_feature.py` 之 `GITIGNORE` 樣板
是否同步修改，屬 canon 層，本條不及之。
```

> **執行層附註（2026-08-23，A-PMH06 → RESOLVED）** —— 上列 R-PMH11 所指定之
> 實施方式（`inputs/` ＋ `!inputs/MANIFEST.sha256`）**實測無效**：git 不遞迴
> 進入已排除之目錄，其內之否定規則不被求值。**本條之目的未變**，其寫法由
> **R-PMH15** 取代（`inputs/*` ＋ 否定規則，四項雙向驗證），並經 **R-PMH17**
> 由 Pei 於 2026-08-23 追認。**原條文不改字**（比照 R-PMH6／R-P36）。
>
> ⚠ **canon 層成因未解（PENDING-CANON）** —— `scripts/new_feature.py` 之
> `GITIGNORE` 樣板仍為 `inputs/` 目錄形態，任何新 feature 照樣板產出者，
> 其雜湊檔都會被忽略。Pei 之追認就其字面只及於本 feature 之 `.gitignore`，
> 未及於樣板；執行層不得順手改之（03a §四）。

## R-PMH12 —— 跨表列號以 id 實測，不以位移推算

```
R-PMH12（跨表列號之比對方式）
跨表之列號對應一律以 id 實測比對，不以列號位移推算。

依據：037 之 56 列含 8 個 Heading 列而 036 之 48 列不含之，位移非定值
（01 包 §3.3）。本條適用於本 feature 之全部跨表比對，不限於 037↔036。
```

---

## 抄錄逐條核對表（02 包步驟 1）

抄錄方式同 01 包：以 `re.findall` 自 handoff §二之 fenced block 直接取字串
寫入，未經人工重打；核對時對 handoff 原文與 `RULINGS.md` 落地文**各自獨立
再抽取**後計 SHA256。

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH7 | 交付母本為 forms ext；客戶那份降為來源複本 | 545 | `78b740e423d40164` | `78b740e423d40164` | ✅ 逐字相符 |
| R-PMH8 | `workbook_state` = `BLANK`；撤回 `PREFILLED_DRAFT` | 400 | `533aac08d7e1c3da` | `533aac08d7e1c3da` | ✅ 逐字相符 |
| R-PMH9 | 欄位對應作廢重測，四方交叉佐證 | 325 | `e32121320838363a` | `e32121320838363a` | ✅ 逐字相符 |
| R-PMH10 | D3／D4／D5 一律留空 | 304 | `885070968235b262` | `885070968235b262` | ✅ 逐字相符 |
| R-PMH11 | `MANIFEST.sha256` 入版控 | 347 | `bbba2810887e6e96` | `bbba2810887e6e96` | ✅ 逐字相符 |
| R-PMH12 | 跨表列號以 id 實測，不以位移推算 | 146 | `e56341f8ea5c4b56` | `e56341f8ea5c4b56` | ✅ 逐字相符 |

---

# 下放包 03 —— Test Group 欄值改判、DV 列舉值實測

來源包：`docs/handoff/03_testgroup_and_dv.md`
（SHA256 `22ad9db5775e46518be65e7e3bfbc2c75f40700667065a109bf711dee8d24e59`）§三
抄錄日：2026-08-23

## R-PMH13 —— G 欄填交付夾名；撤回 R-PMH2 後半

```
R-PMH13（workbook Test Group 欄之值）
工作簿 `Test Group`（G）欄一律填交付夾名 `Disclaimer screen`。

依據為四份已交付件之實測：G 欄相異值恰為交付夾名，覆蓋 4/4、
各檔 100% 之資料列（Comfort 466/466 = `Climate Control Interface`、
User Profiles 189/189、Time Management 59/59、
Power Management 283/283）。

R-PMH2 之後半（`test_group` 為 `Power Moding`）**撤回**。
R-PMH2 之前半（`feature` = `Power Moding`、slug = `power_moding`）
**維持有效** —— 其為 repo 內部識別，不進入任何交付欄位，不受本條影響。

`feature.yaml` 之 `test_group` 鍵改為 `Disclaimer screen`，並於註解記明
其為交付夾名而非規格模組名，以免日後被讀成 R-C6 之同型錯誤。

本條之效力起於 Pei 核可；核可前 G 欄不得寫入任何值（R-PMH6 之延後仍在）。
```

## R-PMH14 —— 語料之鑑別力口徑（分母為能分辨者）

```
R-PMH14（語料之鑑別力口徑）
以已交付件語料支持某一判斷時，其分母為「**能分辨候選各案之交付件數**」，
不是「交付件總數」。

不能分辨者（各候選在該件上取值相同）不計入分子亦不計入分母，並須於
引用處具名列出其被排除之理由。

依據：Q7 之語料中，三份交付件之交付夾名與規格模組名恰好相同，
故其 `{abbr}` 無論依何者取值都得同一結果 —— 該三份對本題之鑑別力為零，
「3 / 4 支持某案」為無效之比率（R-G8：缺判準之比率不予採認）。
```

## R-PMH15 —— `.gitignore` 之 `inputs/*` 形態與四項雙向驗證

```
R-PMH15（A-PMH06 之落實方法）
`features/power_moding/.gitignore` 之素材排除改以 `inputs/*` 形態書寫，
其後接否定規則放行 `inputs/MANIFEST.sha256`。

不得使用 `inputs/`（目錄形態）＋ 否定規則之組合 —— git 不遞迴進入已排除
之目錄，該組合實測無效（A-PMH06）。

驗證條件（雙向，缺一不可）：
(a) `git check-ignore -v` 對 `MANIFEST.sha256` 無命中；
(b) 同指令對四份素材各自仍命中；
(c) 他 feature 之忽略行為不變；
(d) `git add --dry-run` 對 `inputs/` 恰輸出一筆。

R-PMH11 之目的未變，本條僅取代其所指定之寫法。
```

---

# 下放包 03a —— Pei 裁定三項（與 03 同一往返）

來源包：`docs/handoff/03a_pei_rulings.md`
（SHA256 `3da4ce9e6aa88f3b8230ae03837998a0a89baa562b3630068ff26b268d88598e`）§二
抄錄日：2026-08-23
Pei 之裁定原文（2026-08-23，逐字）：「R-PMH13 核可、Q7 乙、A-PMH06 追認」

## R-PMH13 之生效 —— 核可生效，G 欄停止條件解除

```
R-PMH13 之生效（加註，原條文不改字）
Pei 於 2026-08-23 核可 R-PMH13。該條末句「本條之效力起於 Pei 核可；
核可前 G 欄不得寫入任何值」之停止條件**解除**。

`feature.yaml` 之 `test_group` 得改為 `Disclaimer screen`。
R-PMH6 對 H 欄（Test Set）之延後**不受本核可影響**，仍待 Phase 3。
```

## R-PMH16 —— `tc_id_format` = `NR1L-DisclaimerScreen-{NNN}`，附已知反例

```
R-PMH16（tc_id 之 {abbr}）
`tc_id_format` 為 `NR1L-DisclaimerScreen-{NNN}`。

判準：`{abbr}` = 交付夾名去除空白後之 PascalCase，即
`Disclaimer screen` → `DisclaimerScreen`。與 R-PMH13 之 G 欄值同源。

Pei 於 2026-08-23 裁定採 03 包 §4.3 之（乙）案，未採分析層所提之（甲）案
（`PowerModingHMI`）。

**已知反例須隨本條保留，不得略去**：Comfort 之 `{abbr}` 為 `ComfortHMI`，
其交付夾名為 `Climate Control Interface` —— 該件不符本條之判準，且它是
03 包 §4.2 依 R-PMH14 篩出之唯一具鑑別力語料。

故本條為**本 feature 之裁定，不主張為全案慣例**；他 feature 引用本條前
須自行查其交付件。
```

## R-PMH17 —— A-PMH06 之追認，RESOLVED

```
R-PMH17（A-PMH06 之追認）
Pei 於 2026-08-23 追認 R-PMH15 所定之 `.gitignore` 寫法
（`inputs/*` ＋ 否定規則放行 `MANIFEST.sha256`，四項雙向驗證）。

A-PMH06 → RESOLVED。R-PMH11 之目的未變，其所指定之無效寫法由 R-PMH15
取代，原文不改字。
```

## R-PMH18 —— 兩個字面常數之大小寫保真

```
R-PMH18（本 feature 兩個字面常數之保真）
下列二字串為逐字常數，大小寫、空白、單複數一律照抄，任何比對與 lint
須為大小寫敏感：

  G 欄（Test Group）之值：`Disclaimer screen`   —— screen 為小寫 s
  tc_id 之 {abbr}：      `DisclaimerScreen`     —— Screen 為大寫 S

二者刻意不同（前者為交付夾名原樣，後者為其去空白之 PascalCase），
**不是筆誤，不得「統一」**。任何將二者正規化為同一形態之處理即為缺陷。
```

---

## 抄錄逐條核對表（03 ＋ 03a）

抄錄方式同 01／02 包：`re.findall` 自 handoff 之 fenced block 直接取字串寫入，
未經人工重打；核對時對 handoff 原文與 `RULINGS.md` 落地文**各自獨立再抽取**
後計 SHA256。

| 來源 | 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|---|
| 03 | R-PMH13 | G 欄填交付夾名；撤回 R-PMH2 後半 | 544 | `6e163ef260ff31e6` | `6e163ef260ff31e6` | ✅ 逐字相符 |
| 03 | R-PMH14 | 語料之鑑別力口徑（分母為能分辨者） | 232 | `6d4b62eca4fb8279` | `6d4b62eca4fb8279` | ✅ 逐字相符 |
| 03 | R-PMH15 | `.gitignore` 之 `inputs/*` 形態與四項雙向驗證 | 368 | `8c7e1e9140c9575f` | `8c7e1e9140c9575f` | ✅ 逐字相符 |
| 03a | R-PMH13 之生效 | 核可生效，G 欄停止條件解除 | 204 | `5c2d8191265d14af` | `5c2d8191265d14af` | ✅ 逐字相符 |
| 03a | R-PMH16 | `tc_id_format` = `NR1L-DisclaimerScreen-{NNN}`，附已知反例 | 441 | `b5c1dca6cebb18b6` | `b5c1dca6cebb18b6` | ✅ 逐字相符 |
| 03a | R-PMH17 | A-PMH06 之追認，RESOLVED | 179 | `8d9e34596fe21d01` | `8d9e34596fe21d01` | ✅ 逐字相符 |
| 03a | R-PMH18 | 兩個字面常數之大小寫保真 | 273 | `8ec7e2b9cf2f794d` | `8ec7e2b9cf2f794d` | ✅ 逐字相符 |

---

# 下放包 04 —— 母體判準與機器檢查補實

來源包：`docs/handoff/04_corpus_and_assertions.md`
（SHA256 `3a8648a0a6973b6286bb47b126e9a780b8b43ea122a831cd3a93b35be2a18eac`）§四
抄錄日：2026-08-23

## R-PMH19 —— 已交付件語料之母體判準（三條排除規則 ＋ 揭露義務）

```
R-PMH19（已交付件語料之母體判準）
以「已交付件」為據之任何陳述，其母體為：`ASW-R2` 樹下符合下列全部條件
之 036 檔案 ——

(a) 位於某一交付夾之根層（不在 `REF/`、`output/`、`validation/`
    或任何子目錄內）；
(b) 檔名不含中間態標記：`(Review)`、`(Revise)`、`(Refine)`、`(done)`、
    `_Rebuilt`、`pre_writeback`；
(c) 同一交付夾內有多份符合 (a)(b) 者，取檔名日期最大之一份，
    其餘列為「同夾舊版」並具名排除。

陳述時須同時載明：母體清單（逐檔全路徑）、依 (a)(b)(c) 各排除幾份、
以及分子之計數方式。未載明者，其比率不予採認（R-G8）。
```

> **執行層附註（2026-08-24，05 包 §二）** —— 上列 R-PMH19 之 **(a)「位於某一
> 交付夾之根層」已由 R-PMH24 取代**。原 (a) 以「深度」表達「用途」，二者無關，
> 致 `Core HMI/HomeHMI/`、`Core HMI/Menu Bar and AppDrawer/`、
> `Core HMI/Notifications HMI/`、`Vehicle Settings/CFTS044/`、
> `Vehicle Settings/VF230_V1_R5/` **五個交付件被誤排除**，母體由 16 縮為 11。
> **(b)(c) 與揭露義務維持有效。** 修正後母體 **16**。
> **原條文不改字**（比照 R-PMH6／R-PMH10／R-PMH11）。

> **執行層附註二（2026-08-24，06 包）** —— R-PMH19 **(b) 之中間態標記清單依
> R-PMH31 收斂**：移除 `_Rebuilt` 與 `(done)` 二項（其字面語意皆為成品，
> 以之為中間態標記等同讓檔名字串去判定交付態）。
> 保留者：`(Review)`／`(Revise)`／`(Refine)`／`pre_writeback`／
> `pre_fullwrite`／`pre_final`。二者所涉之檔案改由 **R-PMH28** 或 **(c)** 排除。
>
> **(a) 已由 R-PMH24 取代、(b) 已由 R-PMH31 收斂、(c) 與揭露義務維持**，
> 惟揭露義務依 **R-PMH30** 增列「母體之量測時點」。
> **原條文不改字。**

> **執行層附註三（2026-08-24，07 包）** —— R-PMH19 **(c) 遇檔名日期相同時
> 依 R-PMH32 處置**：**不得擇一**，亦不得由排序之實作細節決定；改為
> 全部平手候選並列 ＋ R-PMH29 之敏感度陳述。
> **`資料列較多`／`mtime 較晚`／`檔名較規範` 三者明文禁止作為 tie-break**
> —— 該三者皆是在判定他 feature 之交付態，不在本判準之授權範圍內。
>
> 依據：`Engineering Mode` 夾之 `EngeeringMode_20260816`(211 列) 與
> `EngMode_20260816_Rebuilt`(527 列) 檔名日期相同（06 包上繳 §2.4）。
> **原條文不改字。**

## R-PMH20 —— 量詞與量測範圍須一致

```
R-PMH20（量詞與量測範圍須一致）
任何帶全稱量詞之陳述（「全部」「總數」「除此之外無」「N/N」），
其量測範圍必須等同該量詞所涵蓋之範圍。

分頁層之量測不得寫成活頁簿層之結論；單一 feature 之量測不得寫成
全案之結論；樣本之量測不得寫成母體之結論。

若量測範圍小於量詞，二者擇一修正：縮小量詞，或擴大量測。
不得以「實務上不會有別的」為由保留較大之量詞。

依據：A-PMH11（分頁層量測寫成全簿結論，實測全簿為 5 組而非 4 組）；
以及 R-PMH10 之成因（四份樣本寫成「語料 5/5」，實際母體未定義）。
```

## R-PMH21 —— 規格文字量不作完整性判準

```
R-PMH21（規格文字量不作完整性判準）
規格 PDF 之抽取字元數不得作為規格完整性、抽取正確性或版本一致性之判準。

`pymupdf` 得 15,618 chars 而 `pdftotext -layout` 正規化後得 15,167 chars
（差 451，約 3%）—— 二者皆為正常結果，差異來自換行與空白之正規化策略，
非內容差異。

本條不要求追查該 3% 之成因。完整性之判準為
`outline_map.json` 之 29/29 章節命中與 48/48 leaf 全解，該二者已成立。
```

## R-PMH22 —— `write_back` 之機器檢查（含故意失敗之驗證要求）

```
R-PMH22（write_back 之機器檢查）
`write_back` 之 `mode: append` 與 `first_row: 10` 須有機器可執行之檢查，
於每次寫回前自動驗證，失敗即中止寫回。

最低要求三項：
(a) 目標分頁自 `first_row` 起至寫回前之最後一列，`D` 欄全空
    （BLANK 之前提仍成立）；
(b) 寫回之起始列 == `first_row`，不得由任何其他來源推導
    （特別是 `outline_map.json` 之 `row_036_customer`，該欄記的是
    客戶那份之列號）；
(c) 寫回後之列數 == 寫回前之列數 ＋ 本批 TC 數。

`feature.yaml` 之註解與本條文本身**都不構成本條之滿足**（通則 8：
文字修補不構成 RESOLVED）。本條之 RESOLVED 條件為：檢查已實作、
且已以一次**故意失敗**之測試證明其會攔下（檢查項須確認其在該階段
確實可能失敗）。
```

## R-PMH23 —— 客戶那份之封面五頁禁用

```
R-PMH23（客戶那份之可用範圍收緊）
客戶交付夾之 `…_PowerModingHMI_20260819.xlsx`（R-PMH7 所定之「來源複本」）
之下列分頁**一律不得取用**：

  `Cover 封面`、`ChangeHistory 修訂履歷`、`Product Document 記錄封面頁`、
  `Cover_old`、`ChangeHistory_old`

理由：其 `ChangeHistory` ver C 已被他 feature（AMFM）之中繼寫回註記覆寫，
`Cover!D6` 版本標為 `A` 而其 ChangeHistory 有 A/B/C 三列（檔案自相矛盾）。
取用其任一格，等同把他 feature 之修訂履歷帶入本 feature 之交付物。

R-PMH7 所稱之「附屬分頁」自本條起明確限定為三頁：
`Reference`、`QS Suggestion`、`Test Case Framework`。
```

---

## 抄錄逐條核對表（04 包步驟 1）

抄錄方式同前：`re.findall` 自 handoff §四之 fenced block 直接取字串寫入，
未經人工重打；核對時對 handoff 原文與 `RULINGS.md` 落地文**各自獨立再抽取**
後計 SHA256。

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH19 | 已交付件語料之母體判準（三條排除規則 ＋ 揭露義務） | 354 | `cbdeed8b8bc0774b` | `cbdeed8b8bc0774b` | ✅ 逐字相符 |
| R-PMH20 | 量詞與量測範圍須一致 | 269 | `786c9662722e59ac` | `786c9662722e59ac` | ✅ 逐字相符 |
| R-PMH21 | 規格文字量不作完整性判準 | 255 | `7224a21216886aab` | `7224a21216886aab` | ✅ 逐字相符 |
| R-PMH22 | `write_back` 之機器檢查（含故意失敗之驗證要求） | 445 | `c9930caa2cfc8567` | `c9930caa2cfc8567` | ✅ 逐字相符 |
| R-PMH23 | 客戶那份之封面五頁禁用 | 427 | `70982925ea302e53` | `70982925ea302e53` | ✅ 逐字相符 |

---

# 下放包 05 —— 母體判準之修正與 Phase 3 前置

來源包：`docs/handoff/05_corpus_fix_and_framework_prep.md`
（SHA256 `94acbb14b0569d3b393dd5066f38ddadeb8b446fc6a909de53d40ba4a0043648`）§四
抄錄日：2026-08-24

## R-PMH24 —— 母體判準以用途目錄排除，非以深度；新增反向驗證義務

```
R-PMH24（母體判準之修正，取代 R-PMH19 之 (a)）
R-PMH19 之 (a)「位於某一交付夾之根層」**撤回**，改為：

(a′) 排除位於**用途目錄**下之檔案 —— 目錄名為 `REF`、`output`、
     `validation`、`archive`、`backup` 者及其所有子層。
     交付夾之層數不列入判準：`Core HMI/HomeHMI/` 與
     `Vehicle Settings/CFTS044/` 皆為交付夾，其深度不影響其身分。

R-PMH19 之 (b)(c) 與揭露義務**維持不變**。

**新增反向驗證義務**：套用任何母體規則後，須逐項列出被排除之檔案，
並對每一項回答「排除它的理由是否成立」。排除清單只列數量而未逐項
覆核者，該母體不予採認。

依據：原 (a) 以「深度」表達「用途」，二者無關，致 Home、AppDrawer、
Notifications HMI、CFTS044、VF230 五個交付件被誤排除；修正後母體
由 11 增為 16。
```

## R-PMH25 —— `design_method` vocabulary 取自 x14 所指 source，非同名分頁

```
R-PMH25（design_method vocabulary 之權威）
本 feature 之 `design_method` 合法值取自**母本 x14 DV 所指之 source 範圍**
（`下拉選單!$A$1:$A$9`），不取自任何同名分頁之內容。

判準：先讀 `xl/worksheets/*.xml` 之 `<x14:dataValidation>` 之 `<xm:f>`
求得 source 位址，再讀該位址之內容；不得因某分頁名為 `下拉選單`
即認定其為 source。

依據：客戶那份之 x14 指向 `Reference!$C$4:$C$12`，其 `下拉選單` 分頁
存在、內容與母本僅第 6 項不同、且**無任何 DV 指向它**（孤兒分頁）。
以分頁名認 source 會取到未生效之清單。
```

---

## 抄錄逐條核對表（05 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH24 | 母體判準以用途目錄排除，非以深度；新增反向驗證義務 | 472 | `9f02fc8ad0606ad4` | `9f02fc8ad0606ad4` | ✅ 逐字相符 |
| R-PMH25 | `design_method` vocabulary 取自 x14 所指 source，非同名分頁 | 364 | `37324b2cec85648b` | `37324b2cec85648b` | ✅ 逐字相符 |

---

# 下放包 05a —— 上游命名之範圍界定（與 05 同一往返）

來源包：`docs/handoff/05a_upstream_naming_scope.md`
（SHA256 `1b07c8091c00e8bceba756641075d13ef60c310990a601e8507170ea78e599a7`）§二
抄錄日：2026-08-24
Pei 之裁定原文（2026-08-24，逐字）：
「037的報告命名不一致不關我的事 我不能要求他們改」

## R-PMH26 —— 上游 037 命名不在範圍（四項拘束）

```
R-PMH26（上游 037 報告命名之範圍界定）
上游 037 報告之檔名一致性**不在本 feature 之驗證與處理範圍內**。

具體拘束四項：
(a) 不得就 037 檔名之形態差異開立 DR，不得產生要求上游改名之建議或
    回報；
(b) 不得以「上游命名將趨於一致」為前提設計任何欄位、判準或腳本；
(c) 037 檔名之差異不得登記為 anomaly —— 它不是缺陷，是本 feature
    無權處置之外部事實；
(d) 若某判準之正確性取決於上游命名一致，該判準即不成立，須改用不依賴
    命名之判準（例如以檔案 SHA256 或其在 `inputs/` 之台帳編號指稱）。

依據：Pei 於 2026-08-24 之裁定（逐字見 05a §一）。

適用範圍為上游之**命名**。本 feature 自身欄位（如 D5）要不要引用該檔名，
屬 Q3，與本條無涉。
```

---

## 抄錄核對表（05a）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH26 | 上游 037 命名不在範圍（四項拘束） | 401 | `94a9c442a2f7f36e` | `94a9c442a2f7f36e` | ✅ 逐字相符 |

---

# 下放包 05b —— Q3 重裁定案（與 05 同一往返）

來源包：`docs/handoff/05b_q3_final.md`
（SHA256 `65aeeb7f2ae48848a646c0104ae223ceca4520731408e594f8d738533dce9719`）§二
抄錄日：2026-08-24
Pei 之裁定原文（2026-08-24，逐字）：「（甲）」

## R-PMH27 —— Q3 重裁定案：三欄留空，依據更換為母體實測

```
R-PMH27（Q3 重裁定案，取代 R-PMH10 之依據段）
`D3 審查者`／`D4 目的`／`D5 範圍 Scope` 三欄**一律留空**。
結論與 R-PMH10 相同，**其依據更換如下**。

R-PMH10 所載之依據句「已交付件四份之該三欄皆空，母本亦空 ——
語料 5/5 無一填寫」**作廢** —— 其母體未定義（04 包 §2、05 包 §二）。

改以 R-PMH24 修正後之母體 16 檔實測為據：

  D3：16/16 空
  D4：16/16 空
  D5：9/16 空、7/16 非空

**本裁定不是多數決**，須連同下列三項一併記載，不得只留結論：
(a) 七個非空者中有兩者填錯 —— `HomeHMI` 之值逐字等同 `AppDrawer` 之
    037 報告名（他 feature 之報告），`Notifications HMI` 之值為
    `FM-WI-FSM-036-A01`（表單編號本身，非任何規格或報告）；
(b) 案（乙）之代價為版號過期無通知機制（本 feature 之 037 為 `V0.1`，
    而 Popup 已至 `V0.2`，證明版號會動）；
(c) 部分 feature 無「單一份 037」可寫（VF230 對應 11 份、CFTS044 對應
    4 份），案（乙）在全案並非良定義。

R-PMH10 之末句效力**維持**：日後若客戶要求填寫，其字串由 Pei 給定並
另立新條取代，**不得以「補上」之名逕行填寫**。

R-PMH10 之 `[PEI-REOPEN]` 標記**撤除**。
```

> **勘誤附註已撤除（2026-08-24，06 包 §八步驟 1）。**
>
> 該附註原記「執行層實測母體 17，條文所載 16 應為 17」。**06 包 §二以
> R-PMH28 定案：`Engineering Mode/App Team Effort/` 為工作子目錄而非交付夾**，
> 其 036 依 (c) 視為同夾舊版排除。**母體回到 16，R-PMH27 所載之
> `9/16 空、7/16 非空` 與其 (a) 之「兩者填錯」皆成立。**
>
> 差異之歸屬（06 包 §2.1）：分析層之補測清單漏列第 17 個，
> 而 (a′) 之字面把工作子目錄當成了交付夾 —— **後者為 R-PMH24 之缺口，
> 由 R-PMH28 補**，非執行層之誤判。執行層之停止條件 7 為**正確觸發**。

---

## 抄錄核對表（05b）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH27 | Q3 重裁定案 | 701 | `e6e14fc0a96c1ccc` | `e6e14fc0a96c1ccc` | ✅ 逐字相符 |

---

# 下放包 06 —— 停止條件之處置與 Layer 2 提案

來源包：`docs/handoff/06_framework_proposal.md`
（SHA256 `09b5f79ee4118e9383c76ee59ff098f3b90dcfe332d920f9e89f282692b572d7`）§四
抄錄日：2026-08-24

## R-PMH28 —— 多層目錄之交付夾判準（取最上層）

```
R-PMH28（多層目錄之交付夾判準，補 R-PMH24 之缺口）
同一 feature 之交付夾若有下層目錄亦持有 036，取**最上層**持有該 feature
036 之目錄為其交付夾；下層目錄之 036 依 (c) 視為同夾舊版，具名排除。

判準：下層目錄之 036 與上層之現行交付件，其 `Requirement or Design ID`
欄之值域屬同一 feature 者，即為同一交付夾之多層結構。

本條不適用於 (a′) 所列之用途目錄 —— 那些不論層數一律排除。

依據：`Engineering Mode/App Team Effort/` 內四檔為 258→296 之遞進，
其成品以 `20260429`(296 列) 出現於父層，形態為工作子目錄而非交付夾。
R-PMH24 之 (a′) 只處理用途目錄，未處理同 feature 之多層結構。
```

## R-PMH29 —— 不確定性以敏感度處置，量測全部候選

```
R-PMH29（不確定性之處置方式）
當某判準之適用結果不確定，且該不確定性之解決須判定**他 feature 之交付態**
或其他本 feature 無權判定之事項時，不得任選一案，亦不得擱置。

處置為：**量測全部候選**，並就當前結論做敏感度陳述 ——
(a) 各候選皆導致同一結論者，記明「結論對此不確定性不敏感」，該不確定性
    即不必解決，並具名記載其存在；
(b) 不同候選導致不同結論者，停並上呈，附各候選之結論。

量測候選不等於將其併入母體；併入才是。以「測了會有併入之誘惑」為由
不測，會讓一個可關閉之不確定性繼續開著。

依據：`Engineering Mode` 兩候選（211 列 vs 527 列）之 `D3`／`D4`／`D5`
實測皆空，Q3 之計數對該夾之取捨不敏感（分析層 06 包 §3.2）。
```

## R-PMH30 —— 母體揭露須含量測時點

```
R-PMH30（母體揭露須含量測時點）
R-PMH19 之揭露義務增列一項：**母體之量測時點**（日期與時分）。

依據：`ASW-R2` 為活動中之目錄，04 包量得候選 28、05 包量得 32，
兩者皆正確，差別只在時點（新增之 4 檔為併行 session 於 04 包之後產生之
寫回前備份）。未載明時點者，兩份上繳之數字無法對得起來。
```

## R-PMH31 —— (b) 清單移除 `_Rebuilt` 與 `(done)`

```
R-PMH31（R-PMH19 (b) 清單之收斂）
R-PMH19 (b) 之中間態標記清單移除 `_Rebuilt` 與 `(done)` 兩項，
保留者為語意明確表示未完成之標記：
`(Review)`／`(Revise)`／`(Refine)`／`pre_writeback`／`pre_fullwrite`／
`pre_final`。

理由：`_Rebuilt`（已重建）與 `(done)`（完成）之字面語意皆為成品，
以其為中間態標記，等同讓檔名字串去判定交付態 —— 而該判定不在
判準之授權範圍內。二者所涉之檔案改由 R-PMH28 或 (c) 排除。
```

---

## 抄錄逐條核對表（06 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH28 | 多層目錄之交付夾判準（取最上層） | 390 | `42020936a93e1fcd` | `42020936a93e1fcd` | ✅ 逐字相符 |
| R-PMH29 | 不確定性以敏感度處置，量測全部候選 | 370 | `9d97e3adc5136862` | `9d97e3adc5136862` | ✅ 逐字相符 |
| R-PMH30 | 母體揭露須含量測時點 | 174 | `a1af90628c847c78` | `a1af90628c847c78` | ✅ 逐字相符 |
| R-PMH31 | (b) 清單移除 `_Rebuilt` 與 `(done)` | 286 | `3140f6236bf98b33` | `3140f6236bf98b33` | ✅ 逐字相符 |

---

# 下放包 07 —— tie-break、granularity 與跨 feature 缺口擴查

來源包：`docs/handoff/07_gap_widening.md`
（SHA256 `388434d9971cbe592e2ecbe5d7a48d2dcaa35a865a5ce5cbafe4e27e6f14678e`）§四
抄錄日：2026-08-24

## R-PMH32 —— (c) 平手時不擇一，改敏感度處置；三種 tie-break 明文禁止

```
R-PMH32（(c) 平手時不擇一）
R-PMH19 (c)「同一交付夾內取檔名日期最大之一份」遇日期相同而無從分辨時，
**不得擇一**，亦不得由排序之實作細節決定。

處置為：該夾之全部平手候選並列，依 R-PMH29 做敏感度陳述 ——
各候選導致同一結論者，該夾照常計入母體並記明「其代表檔未定，
但結論對此不敏感」；不同候選導致不同結論者，停並上呈。

**不得以「資料列較多」「mtime 較晚」「檔名較規範」為 tie-break** ——
該三者皆是在判定他 feature 之交付態，而該判定不在本判準之授權範圍內
（R-PMH31 之同一理由）。

依據：`Engineering Mode` 夾之 `EngeeringMode_20260816`(211 列) 與
`EngMode_20260816_Rebuilt`(527 列) 檔名日期相同，(c) 無鑑別力
（06 包上繳 §2.4）。
```

## R-PMH33 —— 條文修訂之連帶檢查（移除一項須驗接手者接得住）

```
R-PMH33（條文修訂之連帶檢查）
自任何判準移除一項條件時，須逐一檢查該項原本排除之對象改由何者接手，
並實測其接手後之結果與移除前相同。

僅確認「移除後總數不變」不足 —— 總數相同而代表檔改變者，
其後續量測即不同（R-PMH32 所指之情形）。

依據：R-PMH31 自 (b) 移除 `_Rebuilt` 與 `(done)` 時，分析層只驗了
母體仍為 16，未檢查 `_Rebuilt` 改由 (c) 接手後 (c) 是否接得住 ——
實測 (c) 在該夾為平手。
```

---

## 抄錄逐條核對表（07 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH32 | (c) 平手時不擇一，改敏感度處置；三種 tie-break 明文禁止 | 409 | `3f3db769108e0ead` | `3f3db769108e0ead` | ✅ 逐字相符 |
| R-PMH33 | 條文修訂之連帶檢查（移除一項須驗接手者接得住） | 242 | `3b2fe5dcd67478b1` | `3b2fe5dcd67478b1` | ✅ 逐字相符 |

---

# 下放包 08 —— granularity 判準之補正與分母口徑

來源包：`docs/handoff/08_criterion_repair.md`
（SHA256 `8076bde9f53038f7c704d1be4d9b600210be9d46524d807e2ba6c0ce1773bfc9`）§四
抄錄日：2026-08-24

## R-PMH34 —— 涵蓋率陳述之分母（排除無內容者、平手只計一份、盲區聲明）

```
R-PMH34（涵蓋率類陳述之分母）
以「N 個交付件、M 筆資料零命中」形式所作之涵蓋率陳述，其分母須：

(a) **排除無內容者**，或將其分列並具名 —— 資料列為 0 之工作簿無從命中，
    計入分母會使結論看起來比實際強；
(b) **平手並列之候選只計一份**，並註明所取者與另一候選之列數；
    兩候選同時計入即重複計算（R-PMH32 之並列不等於分母加倍）；
(c) 載明檢索所及之欄位，未及之欄位以盲區聲明列出（R-G11）。

依據：07 包上繳 §3.3 之「16 個交付件、3,234 列」中，
`VF230_V1_R5` 為 0 列之空白工作簿，`Engineering Mode` 之兩候選
（527 + 211）重複計入。
```

## R-PMH35 —— 判準須有可執行門檻 ＋ must-hit 錨點實跑；無鑑別力須明示

```
R-PMH35（判準須含 must-hit 且經實跑）
任何正式判準（gate、granularity、涵蓋、lint 規則）於採用前，須具備：

(a) **可執行之數值或字串門檻** —— 「約等於」「過半」「大致」不構成門檻；
(b) **must-not-hit 錨點**：現行對象應通過者，實跑並記其通過；
(c) **must-hit 錨點**：**刻意構造之反例，實跑並證明其 FAIL**。

缺 (c) 者不得標為 PASS，只得標「未實測」—— 全由 must-not-hit 構成之檢查
無法區分「判準有效」與「判準對所有東西都通過」。

判準若在候選各案上結果相同，須依 R-PMH14 明示其**無鑑別力**，
不得被引為支持任一案之理由。

依據：07 包 §三之 granularity 檢查六列皆為 must-not-hit，且其門檻
（「≈ TC/leaf 數」「過半」）不可執行；經本包補正後試算，
該檢查對 Q11 之三案全部 PASS，即對該題無鑑別力（08 包 §2.3）。
```

---

## 抄錄逐條核對表（08 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH34 | 涵蓋率陳述之分母（排除無內容者、平手只計一份、盲區聲明） | 332 | `3e895648a1294f2c` | `3e895648a1294f2c` | ✅ 逐字相符 |
| R-PMH35 | 判準須有可執行門檻 ＋ must-hit 錨點實跑；無鑑別力須明示 | 458 | `369e0e4c5849ccf2` | `369e0e4c5849ccf2` | ✅ 逐字相符 |

---

# 下放包 08a —— Q11 定案與 git 窄口授權（與 08 同一往返）

來源包：`docs/handoff/08a_q11_and_git.md`
（SHA256 `b63ee6decb4ef06bc70dd74b6fd7136da6386f1597eeae4356955191490d63b1`）§二
抄錄日：2026-08-24
Pei 之裁定原文（2026-08-24，逐字）：「甲 commit 交給claude code」

## R-PMH36 —— Q11 定案 —— Test Set #2 = `Disclaimer Screen`；Layer 2 定版 8 組

```
R-PMH36（Q11 定案 —— Test Set #2 之名）
Layer 2 之第 2 組名為 `Disclaimer Screen`。Layer 2 自此**定版為 8 組**：

  Splash Screen(3)／Disclaimer Screen(7)／Startup Animation(9)／
  Startup Sounds(6)／Power Transitions(7)／Power Off Behavior(8)／
  Voice Assistant Key(5)／Off Road Plus(3)   —— 合計 48，餘數 0

本組名與 Test Group `Disclaimer screen` **字面重複，為 canon §4.2
「不得重複 Test Group 字樣」之明示例外**，其範圍嚴格限定為：
本 feature、本組、此一情形（Test Group 取交付夾標籤而非能力名，
致交付夾名恰等於其中一個能力群之名稱）。**不得外推至他 feature，
亦不得作為 §4.2 之一般性放寬。**

未採之兩案及其理由，須隨本條保留：
(乙) `Acceptance Screen` —— `Acceptance` 非規格用語（規格自 7.1 SU1 至
     10.4 PITA6.1 一律用 `disclaimer`），屬造詞，違 §8.4.1 之精神；
(丙) 併入 `Splash Screen` —— 合 §4.2 字面，但該 10 leaf 混兩個 FROP、
     兩種觸發情境（開機動畫 vs 免責畫面互動），且客戶無法以 H 欄過濾出
     disclaimer 之 7 條。

**granularity 判準對三案全部 PASS，對本題無鑑別力**（08 包 §2.3），
故不得引之為支持本條之理由。本條之依據為上開可過濾性與不造詞二者。
```

## R-PMH37 —— git 一次性窄口授權（八路徑、逐字訊息、明文不授權清單）

```
R-PMH37（git 窄口授權 —— 一次性）
Pei 於 2026-08-24 授權執行層執行**一次** git 提交，範圍嚴格限定如下。

**授權範圍**：06＋07 兩包之工作區異動，八個路徑：
  features/power_moding/ANOMALIES.md
  features/power_moding/RULINGS.md
  features/power_moding/framework.md
  features/power_moding/docs/INDEX.md
  features/power_moding/docs/handoff/06_framework_proposal.md
  features/power_moding/docs/handoff/07_gap_widening.md
  features/power_moding/docs/upstream/06_framework_proposal.md
  features/power_moding/docs/upstream/07_gap_widening.md

**訊息**（逐字）：
  feat(power_moding): packages 06-07 — layer 2 verified, granularity pass, CFTS009 gap widened

**時點**：於 08 包步驟 1 之前執行，使 08 之異動落在乾淨之工作樹上。

**明文不授權**：`push`／`amend`／`rebase`／`tag`／`reset`／`checkout`／
`stash`／分支操作；上列八路徑以外之任何檔案（含他 feature、
`scripts/new_feature.py`、`forms/`）；第二次提交。

**執行後義務**：於上繳包揭露 `git status --short` 與 `git log -1 --stat`
之實際輸出，並確認暫存區於提交後為空。

**失敗處置**：任一指令非零退出、或 `git status` 顯示上列八路徑以外之
檔案被暫存 —— **立即停手，不得補救、不得重試**，於上繳回報。

本授權用畢即失效。08 包及其後各包之提交仍須另行授權（R-G5 未變）。
```

> **執行層附註（R-PMH37 之履行狀態，原條文不改字）** —— 本授權之標的
> **已於本輪之前完成**：Pei 於 08 落檔前另行指示提交，執行層據以提交為
> **`a345ca8`**。經逐項比對，該提交**完全符合 R-PMH37 之規格**：
>
> | 項 | 結果 |
> |---|---|
> | 訊息逐字（大小寫敏感） | **相符** |
> | 八路徑 | **完全相符**（無多、無少，共 8 檔） |
> | 時點「08 步驟 1 之前」 | **符合** —— `a345ca8` 於 08 包開工前落地 |
>
> 故執行層**不執行第二次提交** —— R-PMH37 明文不授權「第二次提交」。
> 本授權視為**已用畢並失效**。08 包之提交仍須另行授權（R-G5 未變）。

---

## 抄錄核對表（08a）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH36 | Q11 定案 —— Test Set #2 = `Disclaimer Screen`；Layer 2 定版 8 組 | 813 | `eacfc3241aa619ae` | `eacfc3241aa619ae` | ✅ 逐字相符 |
| R-PMH37 | git 一次性窄口授權（八路徑、逐字訊息、明文不授權清單） | 980 | `5467892a87269e61` | `5467892a87269e61` | ✅ 逐字相符 |

---

# 下放包 09 —— must-hit 隔離度、G1 門檻之推導與門檻單一來源

來源包：`docs/handoff/09_threshold_derivation.md`
（SHA256 `beb797dcbc8ba1a13da635d1e4f4f402c94e7875865d542daa9cdf7484660913`）§四
抄錄日：2026-08-24

## R-PMH38 —— must-hit 之隔離度三級，結構性連帶須有算式

```
R-PMH38（must-hit 錨點之隔離度）
must-hit 錨點之通過條件為「**其指定判準如期 FAIL**」。
指定以外之判準一併 FAIL **不使該錨點失敗**，但須記其隔離度，
因隔離度決定該錨點之證明力：

  **隔離**      —— 僅指定判準 FAIL。可單獨證明該判準有效。
  **結構性連帶** —— 連帶之 FAIL 可由構造參數以算式推出者。
                  須寫出該算式，不得以文字論述代替。
  **未隔離**    —— 連帶之 FAIL 既非指定、亦無算式可推。
                  該錨點不足以證明任一判準有效，須另構造隔離錨點。

任一判準若無任何「隔離」或「結構性連帶」之錨點，該判準依 R-PMH35(c)
標「未實測」，不得標 PASS。

現行錨點之隔離度：
  A1（29 組）／A2（48 組）—— **結構性連帶**。算式：n 個 leaf 分 k 組，
    每組規模 >= 2 須 n >= 2k；故 k > floor(n/2) 時必有單 leaf 組，
    G2 必然 FAIL。A1: 29 > floor(48/2)=24；A2: 48 > 24。
  A3／A4／A5 —— **隔離**。
```

## R-PMH39 —— G1 門檻改 `1/3` 並附推導；`0.35` 作廢

```
R-PMH39（G1 之門檻與其來源）
granularity 判準 G1 之門檻為 `組數 / leaf 數 <= 1/3`（即平均組規模 >= 3），
**取代 08 包 §2.1 所給之 0.35**。

來源：canon §4.1.3 之決策測試「filter 後須得有意義之簇 —— 不是一條，
也不是整本」。其「不是一條」由 G2（`min >= 2`）承接單組下限；
G1 承接其平均意義 —— 平均每組不足 3 個 leaf 時，過濾結果多為 1–2 列，
索引價值與逐條列舉無異。

`0.35` 之作廢理由：該值係湊得，且現有錨點對 `0.35` 與 `0.5` 無鑑別力
（A1 之 0.604 對兩者皆 FAIL），依 R-PMH14 不足以支持之。

G1 不得省略 —— 存在 G2／G4／G5 全通過而仍過細之組態（48 leaf 分 20 組，
每組 2–3），其過細正是 canon §4.1.3 所指「Test Set 欄淪為 TC ID 欄之副本」。
該組態即 G1 之隔離錨點 A6。
```

## R-PMH40 —— 判準門檻之單一來源

```
R-PMH40（判準門檻之單一來源）
判準之門檻只有一個來源：**實作該判準之程式**。

文件（`framework.md`／`DECISIONS.md`／handoff／upstream）中出現之門檻數值，
須由程式輸出產生，或加一致性檢查驗其與程式相同；
**兩份獨立維護之副本一律視為缺陷** —— 程式改而文件未改（或反之）
不會被任何檢查發現。

實施：`check_granularity.py` 增 `--emit-thresholds` 輸出門檻表，
文件之門檻節由該輸出貼入並附產生時之程式 SHA256；
或增一檢查比對文件中之數值與程式常數。二擇一，於上繳說明所採者。

依據：08 包上繳 §7 第 4 項自陳 `framework.md` 之 granularity 節與
`check_granularity.py` 之門檻為兩份獨立副本（與 A-PMH12 同型：
宣告與實際分離）。
```

---

## 抄錄逐條核對表（09 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH38 | must-hit 之隔離度三級，結構性連帶須有算式 | 556 | `a5fccf32d6dc67d3` | `a5fccf32d6dc67d3` | ✅ 逐字相符 |
| R-PMH39 | G1 門檻改 `1/3` 並附推導；`0.35` 作廢 | 462 | `5d7333930b591c6c` | `5d7333930b591c6c` | ✅ 逐字相符 |
| R-PMH40 | 判準門檻之單一來源 | 408 | `c0a3a3cbfc7c711b` | `c0a3a3cbfc7c711b` | ✅ 逐字相符 |
