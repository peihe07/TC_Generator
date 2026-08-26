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

---

# 下放包 10 —— 替換命中數、門檻檢查之落實與 profile 草案

來源包：`docs/handoff/10_profile_draft.md`
（SHA256 `ac4e8e8285a662d0d19231ff80261f21303fc664f0666309f5d73861b18064b8`）§二
抄錄日：2026-08-24

## R-PMH41 —— 就地替換須驗命中數；驗證標的須為所欲狀態非代理量

```
R-PMH41（就地替換須驗命中數）
任何以字串替換方式修改檔案之操作（`str.replace`、`sed`、正規式替換），
須於替換後驗其**實際命中數**，並與預期命中數比對；不符即失敗。

`str.replace()` 無命中時不報錯 —— 未驗命中數之替換，其「成功」不含任何
資訊。多段替換須逐段各驗，不得以總殘留數代替：**先前之替換可能已改掉
後續替換之目標字串**。

驗證標的須為「所欲達成之狀態」，不得為「較易量測之代理量」。
驗佔位符殘留數為 0，不等於節標題已更新。

依據：08a 步驟 8 之第二次替換因第一次已改掉其目標而靜默未命中，
而當時之驗證（佔位符殘留 0）通過（09 包上繳 §6.1）。
```

## R-PMH42 —— R-PMH40 之落實須為可執行檢查，附故意失敗驗證

```
R-PMH42（R-PMH40 之落實須為檢查）
R-PMH40 所定之門檻單一來源，其落實須為**可執行之檢查**：
讀取文件中所記之程式 SHA256，比對程式現值，不符即失敗。

文件中記著一個雜湊而無程式驗它者，仍屬宣告 —— 通則 8：文字修補不構成
RESOLVED；一段未被呼叫之正確程式碼，其效力與文字修補相同。

本條之 RESOLVED 條件：檢查已實作、已接上（可由單一指令執行）、
且已以一次**故意失敗**證明其會攔下（改動程式而不重貼文件 → 檢查須 FAIL）。

依據：09 包上繳 §3 末段之自陳。
```

---

## 抄錄逐條核對表（10 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH41 | 就地替換須驗命中數；驗證標的須為所欲狀態非代理量 | 316 | `6f9b2f3973e6d5c3` | `6f9b2f3973e6d5c3` | ✅ 逐字相符 |
| R-PMH42 | R-PMH40 之落實須為可執行檢查，附故意失敗驗證 | 267 | `0f85f96074977fd6` | `0f85f96074977fd6` | ✅ 逐字相符 |

---

# 下放包 11 —— 已發生變更之舉證、勘誤方式與互斥狀態一致性

來源包：`docs/handoff/11_claim_evidence.md`
（SHA256 `5b9d553545dcb17ea67fc2cd590cf2199c6d4416fe39994c76ba152abab394c4`）§三
抄錄日：2026-08-24

## R-PMH43 —— 已發生變更之陳述須附實測證據；同包舉證標準須一致

```
R-PMH43（已發生變更之舉證）
上繳包中任何對「已發生之變更」所作之陳述（「已改為 X」「已撤除」
「已定版」「已更新」），須附該變更之實測輸出 —— before/after、
`grep -n` 命中、或等效之可重跑證據。**敘述本身不構成證據。**

覆核方（分析層）不得僅憑敘述核可此類陳述；缺證據者退回，
不得因其看來合理而放行。

下放包對同一包內各項變更所要求之舉證標準須一致 —— 對某項要求「須貼出
實測輸出」而對另一項不要求，即為指示缺陷。

依據：08a 上繳 §11.3(a) 逐字稱「狀態由『未定版』改為定版」，
而該變更從未發生（`framework.md:7` 至 10 包回掃時仍為「未定版」）；
分析層於覆核時讀到該句並核可（10 包 §二）。
```

## R-PMH44 —— 已提交之往返包原文不改字，以檔末勘誤節處理

```
R-PMH44（已提交之上繳／下放包之更正方式）
已提交之上繳包或下放包**原文一字不改**。發現其含不實或過時陳述時，
以**勘誤附註**處理：

(a) 於該檔末追加 `## 勘誤` 節，載明：被更正之節號與原句逐字、
    正確之事實、發現該誤之輪次與其證據；
(b) 於 `docs/INDEX.md` 該輪次列標記「含勘誤」；
(c) **不得刪除、不得改寫原句** —— 原句連同勘誤並存，方能看出當時
    相信了什麼、何時發現不是。

追加勘誤節本身是對檔案之修改，須列入該輪之 pathspec 並揭露。

依據：08a 上繳 §11.3(a) 之誤稱（10 包 §4.2）；本 repo 對 `RULINGS.md`
之既有作法（原文不改字、以附註承接，R-P36 形態）擴及往返包。
```

## R-PMH45 —— 同檔內互斥狀態陳述之一致性檢查

```
R-PMH45（同檔內互斥狀態陳述之一致性）
同一檔案內對同一對象所作之**互斥狀態陳述**須一致，並以可執行之檢查驗之。

最低限度之互斥對：`定版`/`未定版`、`PENDING`/`RESOLVED`、
`待裁`/`已裁`/`已結清`、`wired: true`/`wired: false`。

檢查方式：對每一互斥對，掃全檔取其全部出現位置；同時出現兩側者即失敗，
並列出行號與逐字內容。**不得以「總數為 0」代替**（R-PMH41 末段）。

此檢查之價值在於它抓的是**替換未命中之結果**，而非替換之過程 ——
歷史上已無 before 可查之替換，其殘留仍會被它抓到。

依據：`framework.md` 第 7 行「未定版」與第 24 行「定版」跨 08a、09
兩輪並存（10 包 §4.3）。
```

---

## 抄錄逐條核對表（11 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH43 | 已發生變更之陳述須附實測證據；同包舉證標準須一致 | 341 | `bfa28d4131e17cb8` | `bfa28d4131e17cb8` | ✅ 逐字相符 |
| R-PMH44 | 已提交之往返包原文不改字，以檔末勘誤節處理 | 354 | `91b85993581cc00a` | `91b85993581cc00a` | ✅ 逐字相符 |
| R-PMH45 | 同檔內互斥狀態陳述之一致性檢查 | 361 | `eb951180053ad6b6` | `eb951180053ad6b6` | ✅ 逐字相符 |

---

# 下放包 12 —— profile 落檔、A-PMH13 定案與 Phase 4 首批

來源包：`docs/handoff/12_phase4_batch1.md`
（SHA256 `c197c4ffe49038ad5c3707557b8b06f647cc396d82b7b8159f8e61affe931d53`）§三
抄錄日：2026-08-24
Pei 之裁定原文（2026-08-24，逐字）：「上繳了 兩項都核可」

## R-PMH46 —— profile 落檔一次性授權（含明文不授權清單）

```
R-PMH46（profile 落檔授權 —— 一次性）
Pei 於 2026-08-24 核可 10 包 §四之 profile 草案。

授權執行層將該草案寫入
`docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md`，**一次**。

**寫入內容須為 10 包 §四之 markdown 區塊逐字**，另加 R-PMH47 所定之
兩處連帶修改（§0 與 §2 之「48 leaf」加註）。除該兩處外不得增刪改。

**明文不授權**：`docs/runtime/` 下任何其他檔案（含 canon、其他 feature
之 profile、`PROFILE_INTEGRATION.md`）。若 `PROFILE_INTEGRATION.md`
需登錄本 profile，**列為待裁，不逕行修改**。

驗證義務：寫入後以逐字比對證明其與 10 包 §四之區塊（加上兩處連帶）相同，
並附行數與 SHA256。本授權用畢即失效。
```

## R-PMH47 —— A-PMH13 定案 (ii)＋(iii)：out of scope ＋ 揭露列 ＋ DR-PMH1

```
R-PMH47（A-PMH13 定案 —— (ii)＋(iii) 併行）
`SWE1-HMI-PM-028` 之處置如下：

(a) **判為 out of scope**（canon §8.4.2）—— 其內文逐字為
    `OFF2.) Please refer to CFTS009 for complete behavior.`，本身無可驗證
    行為；其行為定義於 CFTS009，屬他規格。**不得為其撰寫驗證 CFTS009
    行為之 TC**。
(b) **該列仍寫入工作簿並揭露**，不靜默丟棄（比照 R-VF12：460/1087
    out of SWE.1 scope 須揭露）。其欄位處置：
      `Test Set` = `Off Road Plus`（維持 R-PMH36 之分組）
      `Test Item` = 037 之 `Requirement Title` 逐字（`CFTS009 Behavior
        Reference`）＋ 括號下半（R-PMH36 之 profile §3.1 硬規則）
      `Test Procedure` / `Expected Result` = `PENDING: DR-PMH1 CFTS009
        所定之 Off Road+ power moding 行為`（§8.4.3 之缺件佔位，
        不得留空、不得填 NA）
      `Remarks` = `[BLOCKED-SPEC] Owner: CFTS009 — behavior defined in an
        external specification; no coverage found in any delivered workbook.`
        （形態沿用 Comfort 之既有慣例，非自創）
(c) **開 `DR-PMH1`** 向上游詢問：該 leaf 之行為應由 CFTS009 之 SWE 需求
    涵蓋，抑或本報告應自行載明其行為。DR 登記於本 feature 之
    `DATA_REQUESTS.md`，每包上繳附未結 DR 清單。

**含 PENDING 之工作簿不得出貨**（§8.4.3）—— 交付前須 DR-PMH1 結案，
或由 Pei 裁定降轉。

**連帶修改（兩處）**：profile §0 與 §2 之「48 leaf」加註
「**其中 1 條（`SWE1-HMI-PM-028`）為揭露列，不含可驗證行為，見 §6**」。
48 之總數不變 —— 該 leaf 仍在 R-PMH1 之範圍內。

依據：跨 feature 擴查零命中（母體 15 個有內容交付件、3,023 資料列、
11 個欄位、166 個相異 Test Set 全數人工核對）—— 兩邊都沒有，
是全案缺口而非分工；其 037 `Requirement Title` 逐字為
`CFTS009 Behavior Reference`，上游自己即命名為「參照」。
```

## R-PMH48 —— 下放包不載 git 提交狀態

```
R-PMH48（下放包不載 git 提交狀態）
下放包不得記載 git 之提交狀態（「尚未提交」「累積未提交」「已授權」）。

理由：提交狀態為撰包時點之外之事實，分析層無從得知其於執行時是否仍成立
—— 已三次過時（08 §5.1、10 §七、11 §五）。

改為：提交狀態一律由執行層於上繳回報（R-G6 之揭露表已涵蓋）；
下放包若需觸及提交，只寫**授權與否**（授權為分析層或 Pei 之行為，
其效力不隨時間變動），不寫**已否提交**。

採納執行層 11 包上繳 §6 第 5 項之建議。
```

## R-PMH49 —— 互斥對擴充至八組 ＋ 按條號切分實作

```
R-PMH49（互斥狀態檢查之兩項擴充）
(a) **互斥對清單擴充**，於 R-PMH45 之四組外增列：
      `已授權`/`未授權`、`已接上`/`wired: false`、`已定案`/`待裁`、
      `FULL`/`BLANK`（workbook_state）
    並於程式中明載「本清單為列舉而非全集」——
    列舉式判準之形態一變即靜默脫落（A-PMH08／A-PMH13 之同族形態）。

(b) **`RULINGS.md`／`ANOMALIES.md` 之按條號切分實作**：
    以 `^#{1,3}\s*(A-PMH\d+|R-PMH\d+|Q\d+)` 切段，段內判互斥。
    切分失敗（某狀態陳述不落在任何段內）者須具名列出，不得靜默歸入前段。

    實作後 11 包 §3.2 之具名排除即解除；若實作證明不可行，
    **維持具名排除並記其嘗試與失敗之處**，不得放寬判準後宣稱通過。

採納執行層 11 包上繳 §6 第 1、2 項之自陳。
```

## R-PMH50 —— 每批 JSON 之 `source_clause` 須取自 PDF

```
R-PMH50（每批產出 JSON 之 source_clause）
Phase 4 之每批產出 JSON，其每一 leaf **必附 `source_clause`** ——
該 leaf 所對應章節之**規格原文子句**。

**取自 PDF**（判讀基準，通則 3），**不得取自 SYS1 匯出**
（追溯用）—— A-PMH03 已實測 SYS1 匯出相對 PDF 有 4 則偏離，
其中 outline 7.1 之偏離正是動畫／splash 之**時序子句重排**。

- 不得節錄至失去語意；過長者以 `...` 標明截斷處並另附全文檔。
- **該 TC 之 `expected_result` 所斷言之每一項行為，其規格依據必須完整
  出現於 `source_clause` 中**（比照 Power R-P109）。
- **機械檢查**：逐 leaf 檢查該欄存在且非空。
  **「是否忠於規格」本身不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
  該檢查只保證覆核所需之材料存在，不保證覆核已做。

依據：Power Management 之 `006` 時序誤讀（A-PW68）歷經兩輪修正與多次
lint 全綠而未被察覺，最後由 `source_clause` 查出（R-P103／R-P104）。
本 feature 之 A-PMH03 為同一形狀且已知落在 7.1。
```

---

## 抄錄逐條核對表（12 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH46 | profile 落檔一次性授權（含明文不授權清單） | 448 | `3c12ee5e7db1e695` | `3c12ee5e7db1e695` | ✅ 逐字相符 |
| R-PMH47 | A-PMH13 定案 (ii)＋(iii)：out of scope ＋ 揭露列 ＋ DR-PMH1 | 1312 | `391b39313a6b3759` | `391b39313a6b3759` | ✅ 逐字相符 |
| R-PMH48 | 下放包不載 git 提交狀態 | 253 | `46273e8cf65f867a` | `46273e8cf65f867a` | ✅ 逐字相符 |
| R-PMH49 | 互斥對擴充至八組 ＋ 按條號切分實作 | 456 | `404337182adbefd7` | `404337182adbefd7` | ✅ 逐字相符 |
| R-PMH50 | 每批 JSON 之 `source_clause` 須取自 PDF | 609 | `879f74215e51fa7e` | `879f74215e51fa7e` | ✅ 逐字相符 |

---

# 下放包 13 —— batch 1 覆核不通過與 A-PMH03 之改判

來源包：`docs/handoff/13_batch1_rework.md`
（SHA256 `73c6b907c0b883477a0518e0c7f18efebfd1a245d67c87420b5a62a736a81aa6`）§五
抄錄日：2026-08-24

## R-PMH51 —— A-PMH03 之 7.1 改判為漏句；規格比對一律雙向

```
R-PMH51（A-PMH03 之改判與雙向比對義務）
A-PMH03 之 outline 7.1 一則，其性質由「重排」改判為「**漏句**」——
PDF 之 SU1.) 含 `after the animation (3 sec) a splash screen is presented
timeout (1.5 each).`，而 SYS1 匯出全 52 則描述中該子句之四組探針
（`after the animation`／`splash screen is presented`／`1.5 each`）
命中皆為 0（分析層 13 包 §二獨立複驗）。

**規格比對一律雙向**：既驗 SYS1→PDF（SYS1 之字是否出現於 PDF），
亦驗 PDF→SYS1（PDF 之字是否出現於 SYS1）。單向比對看不見漏句，
而漏句正是最危險之形態 —— 它不會在任何逐字比對中顯示為「不符」，
只顯示為「沒有這一則」。

A-PMH03 之其餘三則（8、9.1、11.1）之判定依據與 7.1 相同，
**須以雙向法複驗**；未複驗前，其「重排／拼字／條列再流」之標題結論
不得引用。
```

## R-PMH52 —— lint 須具名未涵蓋節號；全綠不構成 TC 可用之證據

```
R-PMH52（lint 之涵蓋範圍須具名，且不得作為 TC 可用之證據）
任何 lint 之輸出須具名其**未涵蓋**之 canon 節號，不得只列已通過項。

現行 `lint_batch.py` 之 20 項全為 profile 欄位層與 id 層，
**零項檢查 canon §4.3.1／§5.1／§5.2／§5.5／§8.5／§10.5／§11** ——
而 batch 1 於該七節共六類違規、涉及全部八條，lint 仍 20/20 全綠。

「lint 全綠」不得作為 TC 可用、可提交人讀覆核或可寫回之證據；
其僅證明所檢查之項通過。

依據：13 包 §四；A-PW68 之同一形狀（Power `006` 歷經多次 lint 全綠
而時序誤讀未被察覺）。
```

## R-PMH53 —— 拆分後之交叉引用連帶更新

```
R-PMH53（拆分後之連帶更新）
一條 TC 拆為多條而使其後之 tc_id 位移時，須重掃該批全部交叉引用
（`test_item` 括號下半、`reasoning`、`distinguishing_axis`、
`split_reason`），並驗其所指之 tc_id 仍為所欲指者。

**機械檢查**：批內任一欄位所引之 `-\d{3}` 形態 tc_id，其被引用者之
`leaf_id` 或 `distinguishing_axis` 須與引用處之語意相容；
無法機械判定者，逐處列出供人讀。

依據：batch 1 因 `001-04` 拆為兩條而使 `-005` 之後全體 +1，
`-005`／`-006` 之四處交叉引用未更新，所指者變為無關之 TC（13 包 §4.7）。
```

---

## 抄錄逐條核對表（13 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH51 | A-PMH03 之 7.1 改判為漏句；規格比對一律雙向 | 500 | `55d75bee47dedba9` | `55d75bee47dedba9` | ✅ 逐字相符 |
| R-PMH52 | lint 須具名未涵蓋節號；全綠不構成 TC 可用之證據 | 339 | `5abf94f6836df206` | `5abf94f6836df206` | ✅ 逐字相符 |
| R-PMH53 | 拆分後之交叉引用連帶更新 | 348 | `8520b02b6d6c5dc4` | `8520b02b6d6c5dc4` | ✅ 逐字相符 |

---

# 下放包 14 —— marker 枚舉法、SU9 缺口之處置與 batch 1 第二輪覆核

來源包：`docs/handoff/14_marker_enumeration.md`
（SHA256 `de8919b23576789dcb5f6b2dc58956e3d5c6f1a4740f302e170c17f9b2a35c1a`）§四
抄錄日：2026-08-24

## R-PMH54 —— 規格覆蓋以 marker 枚舉為權威（無門檻）；句級 diff 降為輔助

```
R-PMH54（規格覆蓋以 marker 枚舉為權威判準）
規格文件與其結構化匯出之覆蓋比對，以**需求 marker 之枚舉**為權威判準：
自 PDF 枚舉全部需求標記（本 feature 為 `SU\d`／`SSND \d`／`PM\d`／
`PITA\d`／`VRLP\d`／`OFF\d`），逐一檢查其是否出現於匯出之描述全文。

此法**無門檻、無取樣、無相似度參數**，其結果為二值（在／不在），
故不受任何可調參數之影響。

句級雙向 diff（13 包）**降為輔助** —— 其用於發現 marker 內部之子句缺漏
（如 7.1 之時序子句），不用於判定需求單位之覆蓋。二者分工：
  marker 枚舉 → 需求單位是否存在
  句級 diff  → 已存在之單位其內容是否完整

實測（分析層 14 包 §3.2）：PDF 30 個 marker，SYS1 缺 2 個
（`SU9.)`、`SU9.1)`），**截斷非系統性，限於章 7 末尾**。
```

## R-PMH55 —— 無 leaf 之規格內容得限縮條件、不得新增涵蓋（三項判準）

```
R-PMH55（以無 leaf 之規格內容限縮既有 TC 之條件）
自規格取得、但於 037 無對應 leaf 之內容，**得用於限縮既有 TC 之條件，
不得用於新增涵蓋**。

判準（三項須同時成立）：
(a) 該內容之作用為**使既有 leaf 之驗證正確**（排除會使該 leaf 之
    預期結果不成立之情境），而非**驗證該內容自身之行為**；
(b) 其於 TC 中僅出現於 `pre_conditions` 或步驟之限定子句，
    **不得出現於 `expected_result`** —— ER 一旦斷言該內容，
    即成為對無 leaf 之行為之驗證（§8.4.2）；
(c) 其來源與缺 leaf 之事實須於 `reasoning` 具名，並開 DR。

現行適用：`-003`／`-004` 之「不按任何硬鍵」限定，源自 PDF `SU9.1`
（按 Power Off／Screen Off 會重設逾時），該 marker 於 SYS1 缺失
（A-PMH14、DR-PMH3）。三項判準皆成立：其作用為排除會使逾時不發生之
操作、只出現於步驟之限定子句、已於 reasoning 具名。

**若 DR-PMH3 回覆為「SU9／SU9.1 應在 037」**，則該二 marker 將成為
新 leaf，本條之適用即告終止，其內容改以獨立 TC 涵蓋。
```

## R-PMH56 —— 未涵蓋清單須由程式自 canon 節號全集產生

```
R-PMH56（未涵蓋清單本身須經完整性檢查）
R-PMH52 所要求之「lint 未涵蓋之 canon 節號」具名清單，**其自身須以
canon 之節號全集為母體逐節核對**，不得以人工回想列舉。

實施：以 canon 之節標題產生節號全集，減去 lint 已涵蓋者，
其差集即為應具名之清單；清單由程式產生，不手寫。

依據：13 包所具名之未涵蓋清單列了九節，**而 §5.2（步驟字數上限）、
§5.3（標準片語）、§5.6（baseline）、§6.1（多階段 ER 版面）、
§10.4（reasoning 2–5 句）、§10.6、§12（design method first-match）
七節既未被檢查、亦未被具名** —— 清單漏列使「已具名」產生虛假之完整感
（14 包 §5.4）。
```

---

## 抄錄逐條核對表（14 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH54 | 規格覆蓋以 marker 枚舉為權威（無門檻）；句級 diff 降為輔助 | 437 | `96653ba4141df0c0` | `96653ba4141df0c0` | ✅ 逐字相符 |
| R-PMH55 | 無 leaf 之規格內容得限縮條件、不得新增涵蓋（三項判準） | 598 | `2ed40ce75a1234a6` | `2ed40ce75a1234a6` | ✅ 逐字相符 |
| R-PMH56 | 未涵蓋清單須由程式自 canon 節號全集產生 | 356 | `68cd3f7735af913e` | `68cd3f7735af913e` | ✅ 逐字相符 |

---

# 15 包 —— marker 前綴之反向驗證、priority 之內部矛盾與 COVERED 自動化

## R-PMH57 —— marker 前綴清單須由反向掃描產生

```
R-PMH57（marker 前綴清單須由反向掃描產生）
marker 枚舉法（R-PMH54）所用之前綴清單，**不得人工列舉**，
須以反向掃描產生：對規格全文掃 `\b([A-Za-z][A-Za-z_ ]{0,8}?)\s?
(\d+(?:\.\d+)?)\s?([.):])`，取其前綴分布，逐一判定為
「需求 marker」或「交叉參照／偽命中」，判定結果逐項具名留檔。

實測（分析層 15 包 §2.1）：人工列舉之六個前綴遺漏 **`DS`**
（`DS4.1)`，PDF 行 306，對應 outline 7.5.1）。
**PDF marker 全集為 31 而非 14 包所報之 30。**
缺漏數不變（`DS4.1)` 於 SYS1 內），**故結論不變而分母錯**。

**此錯為分析層與執行層獨立計算而得之同一值** —— 二者用了同一份人工清單。
**先算後比只能抓「算法不同而結果不同」，抓不到「前提相同而前提本身錯」**；
故前提本身須另有反向驗證，不得倚賴對照。
```

## R-PMH58 —— `COVERED` 須自檢查點自動產生

```
R-PMH58（COVERED 須自檢查點自動產生）
`lint_batch.py` 之 `COVERED`（已涵蓋之 canon 節號集合）**不得手寫**。

實施：每一檢查點於其註冊處附其所檢查之 canon 節號，
`COVERED` 由該等註冊自動彙集；`canon_coverage.py` 匯入之。

依據：14 包 §3.2 —— `COVERED` 先宣告 `5.2` 而該檢查尚未實作，
致未涵蓋清單稱其「已涵蓋」而實際沒有。**宣告與實作分離即會分岔**
（A-PMH12 之同型）。手寫之集合無法防此。
```

## R-PMH59 —— priority 之依據須批內互不矛盾

```
R-PMH59（priority 之依據須批內互不矛盾）
同一批內各 TC 之 `priority` 依據**須互不矛盾**：若某條以「後果 X 嚴重」
判為高級，而另一條以「X 為正常設計且可接受」判為低級，二者不得並存。

檢查方式：批內成對之 TC（同一軸之兩側、變體對、正負對）其級別若不同，
須於 `reasoning` 說明**該差異之來源**，且該說明不得與對側之 reasoning
相衝突。此項不可機械判定，屬人讀覆核之必查項。

依據：batch 1 第三輪之 `-003`（P0，依據為「逾時失效使車輛永遠停在
免責畫面」）與 `-004`（P1，依據為「Maserati 設計上即無逾時，
Accept 路徑仍在」）—— 二者不能同時成立（15 包 §3.1）。
```


## 抄錄逐條核對表（15 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH57 | marker 前綴清單須由反向掃描產生；先算後比抓不到共同前提之錯 | 450 | `24d7227229777e17` | `24d7227229777e17` | ✅ 逐字相符 |
| R-PMH58 | `COVERED` 須自檢查點自動彙集，不得手寫 | 263 | `5ab305927c4b7525` | `5ab305927c4b7525` | ✅ 逐字相符 |
| R-PMH59 | priority 之依據須批內互不矛盾 | 343 | `a95567765836a477` | `a95567765836a477` | ✅ 逐字相符 |

---

# 16 包 —— `-002` 判錯、萃取等同性之判準與 VERDICT 之殘餘盲區

## R-PMH60 —— 兩份萃取之等同性判準

```
R-PMH60（兩份萃取之等同性判準）
同一規格文件之兩份獨立萃取（不同工具、不同正規化策略），其等同性
以 **marker 集合是否逐項相等**驗之，**不以字元數、行數或位元組數**。

理由：R-PMH21 已裁定抽取字元數不得作為完整性、正確性或版本一致性之判準；
「兩份萃取是否為同一份文件」即版本一致性之問題，
故以字元數之差異為據提出或消解該疑慮，皆為判準之誤用。

marker 集合為需求單位之標記，**不受正規化策略影響**；其逐項相等
即證二者為同一份規格之同一版本。

實測（16 包 §四）：分析層之 `pymupdf` 萃取與執行層之 `spec.txt`，
marker 全集皆 31、逐章計數皆同、缺漏皆為 `SU9.)`／`SU9.1)` ——
**等同性成立**，字元數之 584 差額不予採認為疑點。
```

## R-PMH61 —— `VERDICT` 誤判之偵測

```
R-PMH61（VERDICT 誤判之偵測）
marker 前綴之 `VERDICT` 判定（R-PMH57）中，判為 `noise` 或 `xref` 者，
須另行檢查其鄰近文句是否具**需求語氣**（`shall`／`should`／`will`／
祈使句起首），命中者升為「須人讀確認」並於輸出具名。

must-hit（缺之則本條無效）：將一個已知為 `req` 之前綴（如 `SU`）之判定
改為 `noise`（測試替身），其鄰近文句必含需求語氣，
**故須被升為須人讀並攔下**；攔不下者，本檢查對真正之誤判亦無效。

依據：15 包 §10 第 1 項 —— 反向掃描保證「沒有候選被漏看」，
但 must-hit C 只攔「未判定」，不攔「判錯」；
誤判為 `noise` 者，該章一樣靜默消失。
```

## R-PMH62 —— 自訂判準須雙向自套

```
R-PMH62（自訂判準須雙向自套）
提出某一判準以質疑某項結論時，須將同一判準**回頭套用於支持該質疑之
其他項**，並記其結果。

單向套用會產生一種特定形態之錯誤：**被質疑者被修正，而質疑所倚賴之
另一項帶著同型缺陷通過**。

依據：分析層於 15 包 §3.1 以「其失效使開機無法完成」之判準抓出 `-003`
之 P0 依據不成立，卻於同一份文件 §3.3 放行 `-002` ——
而 `-002` 之依據犯的是同一個錯之鏡像（論證 Accept 之重要性時把逾時路徑
當作不存在）。由執行層於 15 包 §4.2 查出（16 包 §二）。

此為 R-PMH51「單向比對看不見漏句」在推理層之同型。
```


## 抄錄逐條核對表（16 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH60 | 兩份萃取之等同性以 marker 集合驗，不以字元數 | 370 | `903b6b94a57e7b4d` | `903b6b94a57e7b4d` | ✅ 逐字相符 |
| R-PMH61 | `VERDICT` 誤判之偵測（需求語氣 ＋ 其 must-hit） | 357 | `6e47d9e94b073bd1` | `6e47d9e94b073bd1` | ✅ 逐字相符 |
| R-PMH62 | 自訂判準須雙向自套 | 310 | `e52b305c6074138b` | `e52b305c6074138b` | ✅ 逐字相符 |

---

# 17 包 —— 「只列不改」之界線、質疑型條文之母體與 A-PMH14 之修正

## R-PMH63 —— 「只列不改」之適用範圍

```
R-PMH63（「只列不改」之適用範圍）
「只列不改」之指示，其適用範圍限於**尚未決定處置之待辦盤點**；
**不適用於檔案中已知不實或自相矛盾之陳述**。

判別：該項若為「一件待決定之事」→ 只列不改，等候裁定；
該項若為「一句現存於檔案而每被讀一次就誤導一次之話」→ **立即更正**，
其更正方式依 R-PMH44（原文保留、附勘誤或結論改寫並保留原句）。

下放包不得以「只列不改」之措詞暫停 R-PMH43（不實陳述須更正）
或 R-PMH45（同檔內互斥狀態須一致）—— 若確有暫停之必要，
須具名該二條並載其理由。

依據：17 包步驟 5 之「只列不改」使 `ANOMALIES.md` 之 A-PMH14 同時寫著
「9.1 條列再流維持」與「9.1 之狀態矩陣全缺」而未被更正；
由執行層於 16 包 §10 第 3 項指出（17 包 §二）。
```

## R-PMH64 —— 質疑型條文之機械判準

```
R-PMH64（質疑型條文之機械判準）
R-PMH62 之回溯自套，其母體以下列判準自 `RULINGS.md` 產生，不得人工挑選：

條文之依據段含下列任一標記者，即列為質疑型之候選 ——
`不成立`／`作廢`／`撤回`／`改判`／`取代`／`推翻`／`未套用`／`誤用`／
`判錯`／`不符`／`矛盾`／`由…查出`／`之錯`／`之缺陷`／`之瑕疵`

該判準會有偽陽（條文僅引他處之錯為例證者），**故其輸出為候選清單，
逐條由人確認**，與 `VERDICT` 之處理相同（R-PMH57／R-PMH61）。

判準與其偽陽率須於每次回溯時一併回報；**候選數為 0 者視為判準失效**，
不得視為「無質疑型條文」。

依據：16 包 §10 第 4 項 —— 執行層自陳其回溯只查了四條而無自動判定之判準，
故所交清單之完整性無法主張。
```

## R-PMH65 —— 下放包只得記載分析層自身之行為

```
R-PMH65（下放包只得記載分析層自身之行為）
下放包對 git 之記載，限於**分析層自身之行為**：
「本包未由分析層授權提交」為可知且永不過時之陳述。

**不得記載 Pei 之授權狀態**（「未授權」「已授權」）——
授權為 Pei 之行為，發生於撰包時點之外，與提交狀態同樣會過時。
Pei 是否已授權，一律由執行層於執行時實地確認並於上繳回報。

本條擴充 R-PMH48：該條只擋了「已否提交」，未擋「已否授權」，
而二者過時之機制完全相同。

依據：16 包 §八／§十記「14／15／16 三包之提交未授權」，
而 14／15 已於同日經 Pei 授權並提交（`99b4269`）——
該陳述形式上合於 R-PMH48 而實質上仍然過時（17 包 §四）。
```


## 抄錄逐條核對表（17 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH63 | 「只列不改」限於待辦盤點，不適用於已知不實之陳述 | 384 | `65ec9bce9abddb63` | `65ec9bce9abddb63` | ✅ 逐字相符 |
| R-PMH64 | 質疑型條文之機械判準（回溯自套之母體） | 374 | `368719384072aec8` | `368719384072aec8` | ✅ 逐字相符 |
| R-PMH65 | 下放包只得記載分析層自身之行為（擴充 R-PMH48） | 338 | `d6dd025abf3c1f50` | `d6dd025abf3c1f50` | ✅ 逐字相符 |

---

# 18 包 —— 切斷循環指涉、判準之偽陰與 doc-sync 之錨

## R-PMH66 —— 判定為二值，門檻只分流殘餘

```
R-PMH66（判定為二值，門檻只分流殘餘）
規格比對之判定以**逐字命中**（二值）為權威。相似度門檻
（6-gram 覆蓋率等）**不得作為判定之依據**，其唯一用途為
**將逐字未命中之殘餘分流供人讀**。

具體拘束三項：
(a) 逐字命中者即定案為「非漏」，不再計算任何相似度；
(b) 逐字未命中者一律進入殘餘；**殘餘不得由門檻自動判為「非漏」** ——
    門檻只決定人讀之優先順序，不決定結論；
(c) 殘餘之每一句，其最終判定須有人讀之具名結論，不得只留門檻之數值。

依據：17 包 §三之章 8 實跑 —— 方向二 8 句**全部逐字命中**，
6-gram 門檻一次都未被用到。判定之權威本即在二值之逐字命中，
門檻只是殘餘之分流器；**此分工一經明載，9.1／11.1 即不必倚賴
未受檢驗之門檻**（16 包 §12 第 2 項所指之循環指涉，自此切斷）。
```

## R-PMH67 —— 列舉式判準須附偽陰之抽樣估計

```
R-PMH67（列舉式判準須附偽陰之抽樣估計）
以標記列舉為基礎之判準（R-PMH57 之前綴、R-PMH64 之質疑型標記、
R-PMH45／R-PMH49 之互斥對），其回報**須含偽陰之抽樣估計**：

自**未命中**之母體中隨機抽 N 條（N >= 10）人讀，逐條判其是否應命中；
命中數即偽陰率之估計，與判準、偽陽數一併回報。

**補標記不構成本條之滿足** —— 補完之後仍無人知道還有多少種措詞未被列舉。
抽樣之作用不在補齊，在於**使「不知道還漏多少」變成一個有數字之陳述**。

已知偽陰（實測，18 包 §3.2）：**R-PMH20 未進 R-PMH64 之候選 23**，
其依據段逐字為「實測全簿為 5 組**而非** 4 組」——
形態與 R-PMH51／R-PMH59 相同，未命中之原因是「而非」不在 15 個標記內。
同型可疑者另有 R-PMH21（「**非**內容差異」）。

標記清單應補 `而非`／`並非`／`過時`／`失效`／`無來源`／`湊得`，
**惟補標記與抽樣估計二者皆須為之，不得以其一代替其二。**
```

## R-PMH68 —— doc-sync 之錨取門檻表，不取整支程式

```
R-PMH68（doc-sync 之錨取門檻表，不取整支程式）
`--check-doc-sync` 之錨為 `--emit-thresholds` **輸出之 SHA256**，
不為實作該門檻之程式檔之 SHA256。

理由：以整支程式為錨者，任何編輯（含純註解、含新增與門檻無關之常數）
皆使文件失效，而門檻一字未動。該誤報會訓練出「重跑 emit 再貼上」之
反射動作，**而該反射正是使本檢查失效之途徑** —— 門檻真變之日，
重貼之動作與誤報之日完全相同，無任何東西提醒其不同（17 包 §12 第 5 項）。

**殘餘盲區須具名寫入 `LIMITS`**：門檻表之雜湊守的是**值**，
不是**產生該值之邏輯** —— 改計算方式而值不變者，本檢查不會察覺。
```


## 抄錄逐條核對表（18 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH66 | 判定為二值（逐字命中），門檻只分流殘餘且殘餘須人讀 | 395 | `a9ed686549088dfc` | `a9ed686549088dfc` | ✅ 逐字相符 |
| R-PMH67 | 列舉式判準須附偽陰之抽樣估計；補標記不構成滿足 | 479 | `8effc16c06b1800f` | `8effc16c06b1800f` | ✅ 逐字相符 |
| R-PMH68 | doc-sync 之錨取門檻表輸出，不取整支程式 | 340 | `88c540f9cba69e2b` | `88c540f9cba69e2b` | ✅ 逐字相符 |

---

# 19 包 —— A-PMH16 之複驗、PDF 原句損壞與 Pei 之四項 DR 裁定

## 19 本文（R-PMH69 ~ R-PMH71）

### R-PMH69

```
R-PMH69（來源本身損壞時之處置）
當規格 PDF 之原句本身損壞（非英文字、兩個主謂結構相連而無連接詞、
同一條件之新舊兩版疊寫等），**不得逕以 PDF 為準**，
R-PMH50「source_clause 取自 PDF」於該處**不適用** ——
該條之依據為「SYS1 相對 PDF 有偏離」，其預設 PDF 為正確者，
而此處該預設不成立。

處置三項：
(a) 該處之欄位以 `PENDING: DR-{n} …` 佔位（§8.4.3），不得留空、不得填 NA；
(b) 開 DR 向上游詢問**何者為權威**，並附兩版之逐字對照；
(c) 其所涉之 leaf 所屬 Test Set **不得開批**，直至該 DR 結案。

現行適用：outline `9.1` 之 PDF 句含 `aofnd`（非英文字）、
`the radio should shut Off the popup should close`（兩主謂相連無連接詞）、
`within 60 seconds the timeout defined in pop-up list`（兩時間條件並列
無連接詞）—— 形態為一次未完成之編輯，舊文字與新文字疊寫。
SYS1 之版本恰好刪去該兩段舊文字並將 `aofnd` 改回 `if`，
**故其可能是編輯之意圖而非漏字**。
→ **`DR-PMH4`**；`Power Transitions` 組（5 leaf，`SWE1-HMI-PM-018-01`～`-05`）
**凍結，不得開批**。
```

### R-PMH70

```
R-PMH70（立條後須處置該條所指認之對象）
新立之條文若其依據指認了某一具體對象（某支程式、某項判準、某份產出）
之缺陷，**該對象須於同一輪或次一輪內被處置**：改造、停用、或具名標註為
「已知不合本條而暫留」三者擇一，**不得只立條而讓該對象照原樣繼續運作**。

處置結果須於上繳具名；未處置者列入下一輪之待辦，不得靜默略過。

本條補 R-PMH62：該條只要求「回頭套用於支持該質疑之其他項」，
**未要求處置該條所指認之對象本身**。

依據：R-PMH66 立於 18 包，其依據即「6-gram 門檻做了本不該由它做的判定」，
而做那件事的 `bidirectional_spec_diff.py` 於同輪未被改造、未被停用、
亦未被標註，仍以門檻自動判定（18 包 §11 第 5 項，執行層自陳）。
```

### R-PMH71

```
R-PMH71（結論與其量測須可由同一支程式重現）
任何寫入 `RESIDUE_VERDICT`、`ANOMALIES.md` 或上繳包之人讀結論，
其**產生該結論之量測**須可由該檢查之預設設定重現。

若結論係以非預設之來源或參數查出（如 block 層萃取而預設為 `-layout`），
二者擇一：
(a) 將該來源／參數改為預設，並依 R-PMH35 補其 must-hit；或
(b) 於該結論處具名「本結論不可由預設設定重現」，並記其實際所用之設定。

**不得只留結論而不留其可重現之量測** —— 此為「宣告與實作分離」
（A-PMH12 形態）在結論層之同型。

依據：A-PMH16 係以 PyMuPDF block 層萃取查出，
而 `chapter_bidirectional.py` 之預設來源為 `pdftotext -layout`；
該程式此刻重跑**查不出 A-PMH16**（18 包 §11 第 1 項，執行層自陳）。
```

## 19a —— Pei 之四項裁定（R-PMH72 ~ R-PMH75）

### R-PMH72

```
R-PMH72（`SWE1-HMI-PM-028` 不寫入工作簿）
Pei 於 2026-08-24 裁定「DR-PMH1 拿掉」。

`SWE1-HMI-PM-028`（outline 12.2，內文為 `OFF2.) Please refer to CFTS009 for
complete behavior.`）**不寫入交付工作簿**，不產出 TC，不以 `PENDING` 佔位。

**R-PMH47 之 (b)(c) 撤回**：
(b) 「該列仍寫入工作簿並揭露（比照 R-VF12）」—— 撤回；
(c) 「開 DR-PMH1」—— 撤回，該 DR 標 `CLOSED-BY-RULING`（未答覆而結案）。
**R-PMH47 之 (a)（判為 out of scope，不得為其撰寫驗證 CFTS009 行為之 TC）
維持有效** —— 本裁定只改其揭露方式，不改其 out of scope 之判定。

**repo 內部之紀錄不受本條影響**：`ANOMALIES.md` 之 A-PMH13、
`DECISIONS.md` 之登記、本條文本身**皆保留** ——
「拿掉」之範圍為**交付件**，非本 feature 之內部台帳（G-D：
「不做」與「沒發現」須在紙上分得開）。

**連帶（須重算，不得沿用）**：
  Layer 2 之 `Off Road Plus` 組由 3 leaf 降為 **2**（`-027`／`-029`）；
  有 TC 之 leaf 總數由 48 降為 **47**；
  granularity 之分母 `n_leaf` 隨之改變，G1–G5 須以 47 重跑。
分析層之對照值：8/47 = 0.170（G1 ✅）、min = 2（G2 ✅）、
max = 9/47 = 0.191（G4 ✅）、全組落 [2, 23]（G5 ✅）。
**先算後比，不得引用本行數字為結果。**
```

### R-PMH73

```
R-PMH73（Power Moding State Matrix 已到，DR-PMH2 結案）
Pei 於 2026-08-24 提供 DR-PMH2 所索取之文件：

  features/power_moding/inputs/Power Moding HMI State Matrix R1 SR24 Post 2A
  DCR21421 (August 3 2022).xlsx

該檔為本 feature 之**第六筆素材**，須依 R-PMH4 補入
`inputs/MANIFEST.sha256`（SHA256 ＋ `shasum -c` 通過方為到齊）。

**其效力**：PDF p10 逐字載 `Power Moding behavior shall not be developed
without following the Power Moding State Matrix` —— 該矩陣自此為
**ch 9（`Power Transitions` 組）之判讀背景，具規範性**，
非參考資料。ch 9 之 TC 撰寫須以其為據。

**A-PMH14 之新漏 2（p9 狀態矩陣於 SYS1 全缺）與新漏 3（p10 之
`POWER MODING STATE MATRIX:` 段於 SYS1 全缺）之補救來源自此確定** ——
二者不再是無解之缺口，而是「內容在另一份素材裡」。
**其 anomaly 不撤銷**（SYS1 匯出確實缺該內容，該事實不變），
狀態改為 `RESOLVED（來源已補）`。

**素材真確性**：該檔之 DCR 編號（`DCR21421`）與日期（`August 3 2022`）
**早於**規格 PDF（`DCR22412`／`January 24 2023`）—— 執行層須於上繳
具名此一事實並回報矩陣內容與 PDF p9／p10 是否一致；
**不一致者不得自行取捨，停並上呈。**
```

### R-PMH74

```
R-PMH74（`SU9.)`／`SU9.1)` 不納入，DR-PMH3 結案）
Pei 於 2026-08-24 裁定「037 沒有納入就不放」。

`SU9.)` 與 `SU9.1)` **不補入本 feature 之 leaf 母體**；
leaf 母體維持 **48**（R-PMH1 不變），`Disclaimer Screen` 維持 **7 leaf**。
`DR-PMH3` 標 `CLOSED-BY-RULING`。

**A-PMH14 之新漏 1 不撤銷** —— 「PDF 有而 SYS1／037 無」之事實不變，
其狀態改為 `ACCEPTED（經裁定不補）`。

**R-PMH55 之適用繼續成立** —— 該條原載「若 DR-PMH3 回覆為
『SU9／SU9.1 應在 037』，則本條之適用即告終止」。
**本裁定為其反面**，故 batch 1 之 `-003`／`-004` 依 PDF `SU9.1` 所加之
「不按任何硬鍵」限定**繼續有效**，其三項判準（作用為使既有 leaf 之驗證
正確、只出現於步驟限定子句、於 reasoning 具名）仍須逐條滿足。

**18 包所預先登記之四項連帶（Layer 2 計數、granularity 分母、
`layer3_sections.tsv`／`outline_map.json`、batch 1 增 2 條）全部不觸發。**
```

### R-PMH75

```
R-PMH75（outline 9.1 以 SYS1 為權威，DR-PMH4 結案）
Pei 於 2026-08-24 裁定「以刪掉之後的為主」。

outline `9.1` 之權威文本為 **SYS1 匯出之版本**（即已刪去 PDF 疊寫舊文字者），
**非 PDF**。

**R-PMH50 於 outline 9.1 反轉**：該條「`source_clause` 取自 PDF，
不取自 SYS1」於 `9.1` 之 5 個 leaf（`SWE1-HMI-PM-018-01`～`-05`）
**不適用**，其 `source_clause` 取自 SYS1；`source_clause_origin`
須逐字記 `sys1_export 9.1`，並註 `R-PMH75`。
**R-PMH50 於其餘 47 leaf 維持不變。**

**A-PMH16 之三處改判**：由「SYS1 漏字」改判為「**編輯後之定稿**」——
  (1) `for 60 seconds` —— 舊文字，已刪，**不驗**；
  (2) `seconds`（`within 60 seconds`）—— 舊文字，已刪，**不驗**；
  (3) `the radio should shut Off the` —— 舊文字，已刪，**不驗**。
A-PMH16 狀態改為 `RESOLVED（PDF 側為未刪淨之舊文字）`，**原文保留**
（R-PMH44）；其原判定「(1)(2) 為時序漏失、(3) 為獨立行為結果」
**逐條標記為已被本條推翻**。

**⚠ 承擔之風險須具名**：依本裁定，`the radio should shut Off`
（逾時後收音機關機）**不會有任何一條 TC 驗到**。
若上游日後主張該行為仍屬需求，本 feature 之 ch 9 覆蓋即有缺口 ——
**該風險由本裁定承擔，已於此具名。**

**`Power Transitions` 組解凍**（R-PMH69 之凍結解除），
惟其開批仍以 R-PMH73 之矩陣一致性查核通過為前提。
```


## 抄錄逐條核對表（19 包步驟 1）

| 條號 | 來源 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH69 | 19 | 來源本身損壞時不得逕以 PDF 為準；開 DR ＋ 凍結該組 | 666 | `acaf24b5400373fc` | `acaf24b5400373fc` | ✅ 逐字相符 |
| R-PMH70 | 19 | 立條後須處置該條所指認之對象（補 R-PMH62） | 361 | `6340568122683bf1` | `6340568122683bf1` | ✅ 逐字相符 |
| R-PMH71 | 19 | 結論與其量測須可由同一支程式之預設重現 | 430 | `19fafeda0d151611` | `19fafeda0d151611` | ✅ 逐字相符 |
| R-PMH72 | 19a | `-028` 不寫入工作簿；R-PMH47(b)(c) 撤回；leaf 47 之連帶 | 823 | `0c4232afd78c4a82` | `0c4232afd78c4a82` | ✅ 逐字相符 |
| R-PMH73 | 19a | State Matrix 已到，為 ch 9 之規範性判讀背景；第六筆素材 | 831 | `20e0ae860856d0bb` | `20e0ae860856d0bb` | ✅ 逐字相符 |
| R-PMH74 | 19a | `SU9.)`／`SU9.1)` 不納入；R-PMH55 適用繼續成立 | 612 | `d7fba3b8cafd1d3c` | `d7fba3b8cafd1d3c` | ✅ 逐字相符 |
| R-PMH75 | 19a | 9.1 以 SYS1 為權威；R-PMH50 於該處反轉；風險具名 | 896 | `0ade6f67a43241e5` | `0ade6f67a43241e5` | ✅ 逐字相符 |

---

# 20 包 —— State Matrix 之定位更正、Off Road+ 之互補分支與兩項停止條件之處置

## R-PMH76

```
R-PMH76（State Matrix 之效力範圍更正）
R-PMH73 所稱「該矩陣自此為 ch 9（`Power Transitions` 組）之判讀背景」
**更正**。

實測（分析層 20 包 §2.1）：該 Excel 為**事件驅動之狀態轉移表**
（列軸為事件、欄軸為情境條件、格為轉移後之結果，分 `Key-on`／`Key-off`／
`Key On, Gear ≠ Reverse` 三區塊）；PDF p9 之矩陣為**靜態能力表**
（列軸為電源狀態、欄軸為受控對象、格為是否可用）。
**二者主題不同、粒度不同，該 Excel 不含 p9 之內容。**

其真正之效力範圍為：
  **ch 12（Off Road+）** —— 列 16 `SRT or Off Road+ Hard Button press.`；
  **ch 10 之一部** —— 列 44–48（`Screen Off Button Pressed`／
  `Mute Button Pressed`／`HVAC Hard Control Adjustment`）；
  另涵蓋 `Incoming Call`／`Projection`／`Door` 等事件之電源轉移。

**p9 之能力矩陣仍無來源** —— A-PMH18 維持 `PENDING`，
其狀態不因該 Excel 到齊而改變。**須另開 DR-PMH5。**

**R-PMH73 之其餘部分維持**：該檔為第六筆素材、須入 `MANIFEST.sha256`、
其為規範性文件（`shall not be developed without following`）。

**本條之成因記明**：R-PMH73 於**未讀該檔內容之前**即寫定其效力範圍，
依據僅為 PDF p10 之一句與檔名。**素材之效力範圍須由其內容決定，
不得由其名稱或引用它的那句話推定。**
```

## R-PMH77

```
R-PMH77（停止條件須寫成可判之形式）
停止條件之文字須與其所欲攔截之事一致。「發現任一 X」與「發現**新的** X」
為不同之條件；前者於已登記之 X 存在時必然觸發，使該條件失去分辨力。

撰寫停止條件時之三項要求：
(a) 若所欲攔截者為**新增**之情形，須寫「新的」「未經登記之」「未經裁定之」，
    不得只寫「任一」；
(b) 條件之判定所需之基準（何謂「已登記」）須於同一條件內指明其出處；
(c) 字面與目的分歧時，**執行層據實兩面回報並繼續**，由分析層裁；
    **不得由執行層自行以目的覆蓋字面**。

依據：19 包停止條件 7 寫「章 7 殘餘發現任一漏字或漏句」，
而其目的為「發現**新的**漏句則 batch 1 重做」；殘餘三句皆為已登記且已裁定者，
致字面觸發而目的不觸發（19 包 §2.1）。
**同一形態於 18 包 §9 已由執行層指出過一次，而分析層未將該指認
回頭套用於其後所寫之停止條件** —— R-PMH62 之同型，第三次。
```

## R-PMH78

```
R-PMH78（R-PMH71 之 must-hit 撤回並改寫）
19 包步驟 4 所指定之 must-hit（「以 `-layout` 跑章 9 → A-PMH16 之三處
查不出」）**撤回** —— 其前提為假：三個探針於 `-layout` 之殘餘中同樣存在
（3/3，19 包 §4）。

**撤回之成因**：分析層指定該 must-hit 之期望結果時**未先驗證該期望成立**，
而 R-PMH35(c) 明訂 must-hit 須「實跑並證明其 FAIL」。
**要求他人實跑而自己以推測寫下期望值，即為該條之單向套用。**

改寫後之 must-hit（驗 R-PMH71 之本文主張，形式為二值，不涉門檻）：

  以該檢查之**預設設定**重跑，其 `RESIDUE_VERDICT` 所引之逐字內容
  須出現於輸出中 —— 此為範圍向。
  must-hit：將預設來源換為一個**確定不含該內容之替身**
  （例如僅取 SYS1 側文字），輸出須**不含**該逐字內容而 FAIL。

`--source-must-hit` 於改寫完成前**維持紅燈**，且其紅燈為正確
（19 包 §14 第 6 項）。**不得為使其轉綠而調整其期望值。**
```


## 抄錄逐條核對表（20 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH76 | State Matrix 之效力範圍更正；素材效力須由內容決定 | 823 | `71bb5693d2b9d86f` | `71bb5693d2b9d86f` | ✅ 逐字相符 |
| R-PMH77 | 停止條件須寫成可判之形式（「新的」vs「任一」） | 448 | `203077bcec41e483` | `203077bcec41e483` | ✅ 逐字相符 |
| R-PMH78 | R-PMH71 之 must-hit 撤回並改寫為二值形式 | 538 | `9c193ffb5c31d6fc` | `9c193ffb5c31d6fc` | ✅ 逐字相符 |

---

# 21 包 —— 牴觸之判準、PITA6 之處置與 DR 之狀態機

## 21 本文（R-PMH79 ~ R-PMH81）

### R-PMH79

```
R-PMH79（牴觸之判準與三種記法）
規格文字與規範性素材（矩陣等）之對照，其結果只得記為下列三者之一：

  **牴觸**   —— 二者就**同一謂詞取相反值**（如 displayed / not displayed）。
             須具名該謂詞，並上呈，不得自行調和。
  **印證**   —— 二者就同一謂詞取相同值，或素材補上文字所缺之同一命題之
             另一半。須具名該謂詞。
  **未對照** —— 二者**無共同謂詞**，或素材中**無對應列**。

**「無對應列」不得記為「無矛盾」；「不同謂詞」不得記為「非牴觸」** ——
二者皆會使讀者以為已比對而通過，而實際上該命題從未被素材檢驗過。

判準之依據：牴觸須有共同謂詞方能成立；無共同謂詞者，素材既未支持
亦未否定該敘述。

依據：20 包 §4 之七項對照中，`10.6` 記為「非牴觸」而其二者為不同謂詞
（畫面 vs 電源）、`10.5`／`10.7` 記為「無矛盾」而實為「無對應列」
（20 包 §12 第 1、2 項，執行層自陳）。
```

### R-PMH80

```
R-PMH80（`10.3` PITA6 之處置）
`10.3`（`PITA6`）與 State Matrix `r48c10` 之字面牴觸，
**不裁定何者為權威**，以下列二項處置：

(a) `10.3` 之 TC 於 Pre-Condition 加「倒車影像未顯示（`Gear != Reverse`）」，
    依 R-PMH55 之形態限縮 —— 其作用為使既有 leaf 之驗證正確，
    只出現於 Pre-Condition，來源（矩陣 `r48c10`）於 `reasoning` 具名；
(b) RVC 情境之行為（`Popup not displayed over RVC`）**只在矩陣有、
    規格未載**，依 R-PMH55(b) 不得為其撰寫 TC，
    **登記為覆蓋缺口並開 `DR-PMH6`**。

**執行層所提之「通則／例外」調和不採**：其依據為 `PITA4` 建立之
「倒車影像優先」原則，而 `PITA4` 之逐字為
`Screen Off and HU Power button **selections** shall be ignored while backup
cam is being shown.` —— **其對象為使用者之按鍵輸入，非 popup 之顯示**。
以規格未載之推論消解真實之字面牴觸，形態同於 A-PMH03 之「拼字錯誤」歸因
（一個未經查證之推論被沿用兩包，19 包 §3.2）。

`Power Off Behavior` 組（8 leaf）**得開批**，其餘 7 leaf 不受影響。
```

### R-PMH81

```
R-PMH81（R-PMH26 之範圍不外推至素材內容）
R-PMH26 之適用範圍為**上游 037 報告之檔名**，
**不外推至規範性素材之格內容**。

素材格內容之明顯損壞（如 State Matrix `r16c12` 之 `rmutes`），其處置為：
(a) 登記於 `ANOMALIES.md`，載其逐字與其對稱位置之值；
(b) **不代為改寫、不代為修正**；
(c) 若該損壞**影響某條 TC 之斷言**，則開 DR；不影響者只登記。

`rmutes` 一例：其對稱位置（`r16c13`）為 `mutes`，二值僅差一字母，
且 `OFF3.)` 之「靜音」與之印證 —— **不影響斷言**，故只登記，不開 DR。

依據：20 包 §12 第 4 項（執行層自陳其將 R-PMH26 之精神外推至素材格內容，
而該外推未經裁定）。
```

## 21a —— Pei 之發出授權（R-PMH82 ~ R-PMH83）

### R-PMH82

```
R-PMH82（DR 之狀態機）
DR 之狀態分四級，`DATA_REQUESTS.md` 之狀態欄只得取其一：

  `DRAFT`      —— 已登記於本 repo，**尚未發出**。
  `SENT`       —— 已發出。**須同時記載：發出日期、發出對象、發出管道**。
                 三者缺一即不得標 `SENT`。
  `ANSWERED`   —— 已獲上游答覆。須記答覆日期與其逐字內容之出處。
  `CLOSED`     —— 已結案。須記其結案依據（`ANSWERED` 之內容，
                 或 Pei 之裁定條號）。

**未記載發出日期與對象者，一律為 `DRAFT`，不得稱「已發」。**

本條之必要性：`DR-PMH1`～`4` 自 2026-08-24 開立起，經執行層於六個往返
連續重申而其狀態欄始終為 `OPEN` —— **該欄無法分辨「登記了」與「發出了」**，
致「尚未發出」這件事沒有任何欄位承載它。

**回溯適用**：`DR-PMH1`～`4` 已由 Pei 之裁定結清，其狀態改為
`CLOSED`（依 R-PMH72／73／74／75），**其歷程中從未 `SENT`，此事實須記明**。
```

### R-PMH83

```
R-PMH83（DR-PMH5／DR-PMH6 之發出授權）
Pei 於 2026-08-25 授權發出 `DR-PMH5` 與 `DR-PMH6`，其內容依 21a §三之全文。

發出後二者之狀態改為 `SENT`，並記其發出日期與對象；
**執行層不得代為發出** —— 對外發文為 Pei 之行為，
執行層只更新狀態欄且須以 Pei 告知之實際日期為準，
**不得以「下放包之日期」充當發出日期**（R-PMH43：已發生變更之陳述須有證據）。

**阻斷不變**：`DR-PMH5` 於 `ANSWERED` 前，ch 9（`Power Transitions` 組，
5 leaf）**維持不得開批**。`DR-PMH6` 不阻斷 —— `Power Off Behavior` 組
已由 R-PMH80 以限縮 ＋ 揭露解除。
```


## 抄錄逐條核對表（21 包步驟 1）

| 條號 | 來源 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH79 | 21 | 牴觸之判準（同一謂詞相反值）與三種記法 | 479 | `2434c2ce08f08f0d` | `2434c2ce08f08f0d` | ✅ 逐字相符 |
| R-PMH80 | 21 | `10.3` 之處置：限縮 ＋ 揭露，不裁權威 | 695 | `f680f9dd1d940a54` | `f680f9dd1d940a54` | ✅ 逐字相符 |
| R-PMH81 | 21 | R-PMH26 之範圍不外推至素材格內容 | 382 | `7c6a15c014300329` | `7c6a15c014300329` | ✅ 逐字相符 |
| R-PMH82 | 21a | DR 之四級狀態機；未記發出日期與對象者不得稱「已發」 | 549 | `8c412360a1a1e9c0` | `8c412360a1a1e9c0` | ✅ 逐字相符 |
| R-PMH83 | 21a | `DR-PMH5`／`DR-PMH6` 之發出授權；執行層不得代為發出 | 370 | `264be045c8906824` | `264be045c8906824` | ✅ 逐字相符 |

---

# 22 包 —— pop-up 組改判為牴觸、`VP` 之未定義與 batch 1 之連帶

## R-PMH84

```
R-PMH84（條件互斥須被證明，不得被假定）
二陳述有共同謂詞而取相反值時，**除非其條件已被證明互斥，否則判為牴觸**。

「素材未提及某條件」**不等於**「素材不涉及該條件」——
前者是素材之沉默，後者是一個關於素材涵蓋範圍之主張，須有依據。

具體：一方為**全稱否定**（`No X will appear until Y`）而另一方為
**無條件肯定**（`Show X`）時，全稱否定之範圍涵蓋所有時刻，
無條件肯定落於其中任一時刻即成牴觸。**判為「未對照」者，
須具名指出使二者條件互斥之依據**；無依據即為牴觸。

R-PMH79 之「未對照」一支自此限縮為：**無共同謂詞**，
或**有共同謂詞而條件已證互斥**。

依據：21 包 §3.3 將 `SU3.)`（`No pop-ups will appear until the disclaimer
screen has been removed`）與矩陣 `r6`／`r15`／`r24`／`r25`／`r48` 之
pop-up 諸格判為「未對照」，其理由為「矩陣之軸不含 disclaimer 狀態」——
而免責畫面出現於開機序列（Key-on），`r6` 之條件為 Key-on × Call Active
（使用者上車前已通話），**二者可同時成立**。
由執行層於 21 包 §13 第 2 項自陳（22 包 §三）。
```

## R-PMH85

```
R-PMH85（素材使用規格未定義之術語）
規範性素材若使用**規格全文 0 命中**之術語，該術語之指涉**不得由分析層或
執行層推定**，縱其用法可推知其功能。

處置三項：
(a) 登記於 `ANOMALIES.md`，載其命中數（素材側／規格側各若干）與其用法之逐字；
(b) **開 DR 詢問其定義**；
(c) 在該 DR `ANSWERED` 前，**凡以該術語為據之對照判定，一律標「待定義」**，
    不得判為「牴觸」或「未對照」——**該判定所需之語意尚未存在。**

現行適用：`VP` —— 規格 PDF 全 11 頁 **0 命中**，Excel State Matrix **30 格**。
其用法為 `VP Stays ON`／`VP Turns OFF`／`VP display pop-up: "…"`，
可知其為「會開關且會顯示 pop-up 之物」，**惟其指涉未定義**。
→ **`DR-PMH7`**。

**與 R-PMH84 之關係**：本條優先。若某對照之判定倚賴 `VP` 之指涉，
則其記法為「待定義」而非 R-PMH84 之「牴觸」；
**惟 §三之 pop-up 組不倚賴 `VP` 之指涉** —— `r48` 之
`Show Pop-Up` 未用 `VP` 一詞，其牴觸獨立成立。
```

## R-PMH86

```
R-PMH86（`matrix_vs_chapter.py` 之結果標未實測）
`matrix_vs_chapter.py` 於補上 must-hit 前，其結果**只得標「未實測」**，
不得標 PASS（R-PMH35(c)）。**採認執行層 21 包 §13 第 6 項之自我更正。**

其 must-hit 之最低要求：
(a) 將一組已知之真牴觸（`10.3` × `r48c10`）餵入，**檢查須報「牴觸」**；
(b) 將一組已知之真印證（`10.1` × `r40`／`r44` 之 `Event ignored`）餵入，
    **檢查須報「印證」**；
(c) 將一組無共同謂詞者餵入，**檢查須報「未對照」**。

三者皆為**正向錨點**（must-hit 於此為「須報出該記法」而非「須 FAIL」）——
本檢查之輸出為三分類而非二值，故其錨點形態隨之。
```


## 抄錄逐條核對表（22 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH84 | 條件互斥須被證明，不得被假定；R-PMH79 之「未對照」一支限縮 | 605 | `3eb154d9a736b93f` | `3eb154d9a736b93f` | ✅ 逐字相符 |
| R-PMH85 | 素材使用規格未定義之術語 → 標「待定義」並開 DR | 574 | `9ec1d35217e49049` | `9ec1d35217e49049` | ✅ 逐字相符 |
| R-PMH86 | `matrix_vs_chapter.py` 標未實測；三分類之正向錨點 | 393 | `9b5b226ebad5f7f5` | `9b5b226ebad5f7f5` | ✅ 逐字相符 |

## 22a —— R-PMH87（`-007` 之限定）

```
R-PMH87（`-007` 之限定）
`-007`（`SU3.)`，outline 7.4）之 procedure 加事件層限定：
**不按 ON/OFF 鍵、不轉 key-off、不開啟車門、不操作 HVAC 硬控**。

依據：State Matrix 之五個 pop-up 列（`r6`／`r15`／`r24`／`r25`／`r48`）
**全數繫於該四個事件**（其列標籤即該事件），且四者皆為測試員可控之操作；
**排除該四事件即排除全部五格**，R-PMH84 所要求之「條件互斥之證明」
由 TC 自身之構造成立，非由對矩陣涵蓋範圍之推定成立。

**不採之三案及其理由須隨本條保留**：
(a) `No phone call is active` —— **不充分**（`r48` 不涉通話）
    **且冗餘**（事件不發生時通話與否皆不產生 pop-up）；
(b) `Gear != Reverse` —— 只擋 `r48` 之一部；
(c) 通話 ＋ 事件並列 —— 違 §8.5 之不必要窄化。

**實施二項**：
1. 限定加上後逾 §5.2 之 18 字上限，**須拆為兩步**，
   **不得為湊字數而刪去四項中之任一項** —— 缺一即漏一格；
2. **不得以 `R1Low` 限定 `r15`** —— `SU3.)` 全稱適用於所有變體，
   以變體限定屬縮減涵蓋而非使驗證正確，違 R-PMH55(a)。

**連帶之覆蓋缺口三項**（`r6`／`r15`／`r48` 於免責畫面期間之 pop-up 行為，
皆無 leaf）依 R-PMH55(b) 登記，併入 `DR-PMH6` 或另開 `DR-PMH8`，
由 Pei 依其是否已發出決定。
```

| 條號 | 來源 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH87 | 22a | `-007` 之事件層限定；不採三案之理由；拆步與變體之二項實施拘束 | 749 | `f660aab26625f0b4` | `f660aab26625f0b4` | ✅ 逐字相符 |

---

# 23 包 —— 條文優先於步驟、規格內部之牴觸與 batch 1 之逐條對照

## R-PMH88

```
R-PMH88（條文優先於步驟）
下放包之**作業步驟**若與**裁決條文**（同包或既有）相衝突，
**以條文為準**；執行層依條文執行，並於上繳具名該衝突與其選擇。

**執行層不因此承擔判斷之責任** —— 條文為已裁定者，步驟為其實施之描述；
描述與被描述者相衝時，錯在描述。

依據：22 包 §2.2 —— 下放包步驟 2 令五格全改「牴觸」，
而 R-PMH85(c) 令「凡以該術語為據之對照判定一律標『待定義』」；
執行層依條文只改 `r48`。**該選擇正確。**
其成因為分析層於 R-PMH85 之但書中**以一列之證據（`r48` 未用 `VP`）
寫了涵蓋五列之結論**，其後之步驟 2 沿用該過寬之結論。
```

## R-PMH89

```
R-PMH89（規格內部之牴觸）
牴觸之兩造若**同屬規格文件本身**（非規格 vs 素材），
其處置與 R-PMH80 相同（限縮 ＋ 揭露，不裁權威），
**惟須另立 anomaly 並於其中明記「不得以『以規格為權威』解之」** ——
兩造皆是規格，該原則在此無分辨力。

現行適用：`SU3.)`（p8，`No pop-ups will appear until the disclaimer screen
has been removed`）與 p9 能力矩陣之
`HVAC Knobs: Fully functional. Pop-ups still shown.`（p9 出現兩次，
`KEY OFF (ACC)` 與 `KEY OFF (No ACC)` 兩列之 `HEADUNIT POWER OFF` 欄）。
共同謂詞為 pop-up 是否顯示；條件互斥未證（免責畫面之相位為開機序列，
p9 之軸為電源狀態，二軸不同而無依據證明不重疊）。

**連帶**：`DR-PMH5` 之問題全文須增列此項 ——
p9 之能力矩陣不只「無來源」，**其自身之內容與 p8 之 `SU3.)` 相衝**。
```

## R-PMH90

```
R-PMH90（斷言類之反向掃描）
凡以「限定排除某類斷言」為據之 TC（如 `-007` 以四項事件限定排除 pop-up），
其限定之充分性**須經規格全文之反向掃描**，不得只掃素材。

方法：以該類斷言之關鍵詞（`pop-up`／`popup`／`pop up` 等，含大小寫變體）
掃規格全文，逐處判其與該 TC 之情境是否可共存，
並將結果分為印證／牴觸／未對照三類（R-PMH79）。

**掃描之結果須寫入該 TC 之 `reasoning`** —— 只寫素材側之依據而未寫
規格側者，其「限定為充分」之主張未經完整檢驗。

依據：22 包 §12 第 4 項（執行層自陳只排除矩陣之 pop-up 而未反向掃規格）；
分析層 23 包 §3.1 之掃描查出 25 處，其中 **2 處為牴觸**（p9 之
`Pop-ups still shown`），其餘 23 處為印證 5／未對照 18。
```


## 抄錄逐條核對表（23 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH88 | 條文優先於步驟；描述與被描述者相衝時錯在描述 | 317 | `1feb1c559eb1374a` | `1feb1c559eb1374a` | ✅ 逐字相符 |
| R-PMH89 | 規格內部之牴觸；不得以「以規格為權威」解之 | 507 | `95189413b2b17a98` | `95189413b2b17a98` | ✅ 逐字相符 |
| R-PMH90 | 斷言類之限定須經規格全文反向掃描 | 406 | `319bfcb85c10532a` | `319bfcb85c10532a` | ✅ 逐字相符 |

---

# 24 包 —— 攔截式列舉改為正向要求、A-PMH21 之欄位未驗與 ER 逐斷言掃描

## R-PMH91

```
R-PMH91（對照結論須以規定記法作結 —— 取代攔截式列舉）
凡「規格 × 素材」「素材 × 素材」「規格 × 規格」之對照結論，
**其結論必須以下列四詞之一作結**：`牴觸`／`印證`／`未對照`／`待定義`
（R-PMH79 之三者 ＋ R-PMH85 之第四者）。

檢查改為**正向**：驗其**是否以四詞之一作結**，
**不再驗其是否含某些禁用詞**。未以四詞之一作結者即 FAIL。

**停止條件 8 之列舉式判準（攔「無矛盾」「非牴觸」二詞）廢止** ——
其形態為攔截式列舉，兩層抽樣之偽陰率為 10% → **20%，未見收斂**，
且其漏網者「**非漏**」正是 `RESIDUE_VERDICT` 20 條中最常用之起首詞
（23 包 §7.2）。

**本條之判準與母體皆非列舉**：四詞由條文定義而非掃描而得；
「未以四詞之一作結」涵蓋所有其他措詞，含尚未被人用過者。
**R-PMH67 之抽樣義務於本檢查不適用** —— 無列舉即無偽陰可估。
```

## R-PMH92

```
R-PMH92（總表之結果欄由 must-hit 之註冊決定）
各檢查於其註冊處須聲明其 **must-hit 之有無**；
上繳包之檢查總表，其結果欄**由程式產生**：

  已註冊 must-hit 且通過        → `PASS`
  已註冊 must-hit 而未通過      → `FAIL`
  **未註冊 must-hit**           → **`未實測`**（不得為 `PASS`）

**手寫之結果欄不予採認。**

依據：「新增程式無 must-hit 而總表標 PASS」於 21、22、23 三包連續出現，
**三次皆由執行層於 §12 自行更正**（R-PMH35(c) 之重複違反）。
**自行更正三次，即應改為不必自行更正。**
```

## R-PMH93

```
R-PMH93（反向掃描須及於 ER 之每一斷言）
R-PMH90 之反向掃描，其單位為**斷言**而非 TC，亦非 ER 之條。
一條 ER 若含多個斷言，**每一斷言各須一次掃描**，其關鍵詞各自取用。

依據：`-007` 之 ER4 含兩個斷言 ——（a）`no pop-up is displayed`、
（b）`The announcement is heard in the background`；
23 包只掃了（a）。（b）之風險非零：矩陣有 `r16`（`Radio Wakes Up and
mutes`）、`r45`（`Mute Button Pressed`），規格有 `OFF3.)`
（`Head unit is muted when launching app from Power Off State`）——
**「靜音」與「聽得到報導」為同一謂詞之相反值**（23 包 §12 第 6 項，執行層自陳）。
```


## 抄錄逐條核對表（24 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH91 | 對照結論須以四詞之一作結；攔截式列舉廢止 | 441 | `cb23dff4c2cb9088` | `cb23dff4c2cb9088` | ✅ 逐字相符 |
| R-PMH92 | 總表結果欄由 must-hit 註冊決定，手寫不採認 | 339 | `3484fcee117abb9c` | `3484fcee117abb9c` | ✅ 逐字相符 |
| R-PMH93 | 反向掃描之單位為斷言，非 TC 亦非 ER 之條 | 421 | `713a8ff045dc8fde` | `713a8ff045dc8fde` | ✅ 逐字相符 |

---

# 25 包 —— A-PMH21 之欄位以字級座標確認、`r45` 之處置與限定之逐斷言導出

## R-PMH94

```
R-PMH94（限定須逐斷言導出，其總集為聯集）
TC 之事件層限定，其導出單位為**斷言**（R-PMH93 之單位），非 TC。

每一斷言各須：
(a) 以其自身之關鍵詞反向掃描規格與素材（R-PMH90／R-PMH93）；
(b) 列出與其取相反值之格／行；
(c) 導出使該等格／行不適用所需之限定。

**TC 之限定為各斷言所需限定之聯集**；
**在其全部斷言皆完成 (a)~(c) 前，不得主張該 TC 之限定為充分。**

依據：R-PMH87 之四項限定係自 pop-up 一個斷言導出，其對該斷言充分，
**而被當成整條 TC 之限定**；24 包對 audio 斷言之掃描查出 `r45` 之牴觸
（`Mute Button Pressed` → `Mute --> Active` × `The announcement is heard
in the background`），**該格不為原四項所排除**。
`-007` 之限定因而由四項增為七項（25 包 §3.4），
**而其 ER1／2／3／5 之斷言仍未掃**（24 包 §10 第 3 項）。
```

## R-PMH95

```
R-PMH95（歧義以涵蓋兩讀之限定處置，不以判讀處置）
素材之記法有歧義而其兩讀導致不同判定時，
**若存在一個涵蓋兩讀之處置，取該處置，不判讀該歧義**。

理由：判讀可能判錯，而涵蓋兩讀之處置不會；
且判讀須寫入依據而該依據無來源（素材未定義其記法），
即為以無來源之推論支撐判定。

現行適用：矩陣 `r46`／`r47` 之 `Else: Mute Active` 可讀為「維持靜音」
或「使之靜音」，執行層以「箭頭之有無」判為前者而自陳矩陣未定義其記法
（24 包 §4.3／§10 第 1 項）。
**其觸發（`Headunit Mode Button Pressed`／`Headunit Mode Change via VR`）
為測試員可控之事件，故納入限定即涵蓋兩讀** —— 不判讀。

**本條不使該歧義消失** —— `Else: Mute Active` 之語意仍未定，
其登記（A-PMH22）保留；本條只使**本 TC 之判定不再倚賴它**。
```

## R-PMH96

```
R-PMH96（互斥之依據優先取規格逐字）
條件互斥之證明（R-PMH84），其依據**優先取規格之逐字**；
無逐字可取時方得取素材之結構；**常識與通念不得作為依據**。

依據：A-PMH21 之互斥證明，執行層原繫於「免責畫面必為 head unit 開機中
所顯示」並自陳「它是常識而非引文」（24 包 §10 第 4 項）。
**引文存在** —— `PITA6.1`（outline 10.4）逐字為
`Upon pressing power button to On state disclaimer screen shall be displayed
(see SU6.) unless certain phone call scenarios have occurred.`
免責畫面之顯示條件即 head unit 轉為 On，
**故其不可能出現於 `HEADUNIT POWER OFF` 欄所述之狀態**（25 包 §2.2）。
```


## 抄錄逐條核對表（25 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH94 | 限定須逐斷言導出，TC 之限定為聯集 | 492 | `d325186a59bd934a` | `d325186a59bd934a` | ✅ 逐字相符 |
| R-PMH95 | 歧義以涵蓋兩讀之限定處置，不以判讀處置 | 438 | `d4a8dad7d4b76f85` | `d4a8dad7d4b76f85` | ✅ 逐字相符 |
| R-PMH96 | 互斥之依據優先取規格逐字；常識不得為依據 | 428 | `292f12b3812d2d8f` | `292f12b3812d2d8f` | ✅ 逐字相符 |

---

# 26 包 —— 斷言之二分、掃描母體改為全枚舉與限定之合併上限

## R-PMH97

```
R-PMH97（斷言之二分：SUT 行為斷言 vs 測試執行斷言）
ER 之斷言分二類：

  **SUT 行為斷言** —— 其標的為受測系統之行為或狀態
                    （`The announcement is heard`／`no pop-up is displayed`）。
                    **須依 R-PMH94 逐斷言反向掃描。**
  **測試執行斷言** —— 其標的為測試過程中測試員之作為或不作為
                    （`No ON/OFF key press occurs`／`No door is opened`）。
                    **不入反向掃描之母體。**

判別法：該斷言之主語是否為 SUT（或其部件）。
主語為測試員之操作者，屬後者。

**不入母體者須逐條具名其歸類與理由**，並寫入該檢查之常數
（非只寫於上繳包）；**未具名而略過者，視為未掃描。**

依據：25 包 §4.1 —— 執行層對 `-007` 之 ER1／ER2 判「不需反向掃描」，
其理由成立（素材不描述測試員做了什麼，故無共同謂詞），
**而 R-PMH94 之 (a)~(c) 未給該出口，執行層自行加之**（25 包 §12 第 2 項自陳）。
本條使該出口成為條文，**加得對與否不影響「自行加例外」之性質** ——
下次若加錯，同樣不會有東西攔它。
```

## R-PMH98

```
R-PMH98（斷言掃描之母體為全枚舉，關鍵詞降為排序輔助）
斷言之反向掃描（R-PMH90／R-PMH93／R-PMH94），其母體為
**規格之全部敘述行**與**素材之全部有值格**，
**不得為關鍵詞命中之子集**。

關鍵詞之角色由「決定何者進入母體」降為「**決定人讀之先後**」。

規模不可行時得以**謂詞層粗篩**分兩層（機器先篩、人讀其入選者），
**惟粗篩之落選者仍須逐格／逐行具名其落選理由** ——
否則只是把關鍵詞換了個名字。

依據：25 包 §5 之 15 個同義表述量測命中 0／0，執行層自陳
**「那只證明『我想到的 15 個都不在』…… 這不是隨機抽樣，是我自己出的題目」**
（25 包 §12 第 4 項）。其形態同於 24 包 §7.2 之「非漏」——
**漏掉的可能正是用最多的那個**，補列舉不解決。

**本 feature 已有正解之實例**：`matrix_vs_chapter.py` 對章 7／8／10／11
各以 30 列**全具名**，不以關鍵詞篩選；
**而 `spec_assertion_scan.py` 仍以關鍵詞篩母體** ——
**兩支同時存在，一支已經解決了另一支還在犯的問題。**
```

## R-PMH99

```
R-PMH99（限定合併之上限與其可驗性）
事件層限定（R-PMH87／R-PMH94）得合併於同一 procedure 步驟，
**惟須同時滿足三項**：

(a) **每步至多兩項**；
(b) **ER 逐項複述** —— 合併之步驟，其 ER 須將各項分列或以連接詞明列，
    使每一項各自可判；
(c) **lint 須驗各限定項之字串於 procedure 中各出現一次**
    （出現 0 次或 2 次以上皆 FAIL）。

**不禁止合併之理由**：canon §5.2 之字數上限使「一項一步」於本例產生
十步且每步字數遠低於上限，形式冗贅。

依據：25 包 §3.3 —— 七項限定壓縮於四步（2/2/2/1），
執行層自評**「若某項因合併而在執行時被忽略，其後果與刪去相同」**
（25 包 §12 第 3 項）。**現行之四步合於本條。**
```


## 抄錄逐條核對表（26 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH97 | 斷言之二分；測試執行斷言不入掃描母體，須具名 | 633 | `831a17ff1f6c624b` | `831a17ff1f6c624b` | ✅ 逐字相符 |
| R-PMH98 | 掃描母體為全枚舉，關鍵詞降為排序輔助 | 530 | `ac0769deb890f727` | `ac0769deb890f727` | ✅ 逐字相符 |
| R-PMH99 | 限定合併之上限 ＋ ER 逐項複述 ＋ lint 字串檢查 | 388 | `9ac724e2d21b886d` | `9ac724e2d21b886d` | ✅ 逐字相符 |

---

# 27 包 —— 落選即判定、斷言切分以謂詞為準與 Pre-Condition 之納入

## R-PMH100

```
R-PMH100（落選即判定 —— 消滅「落選」類別）
斷言掃描（R-PMH98）之粗篩，**其落選項須以四詞記法（R-PMH91）
入判定表**，不得另列於「落選」欄。

落選之常見記法為 `未對照`，其依據即粗篩所憑之理由
（如「該格之謂詞域與本斷言不交」）。

**「落選」這個類別消滅後，關鍵詞即自動降為排序輔助** ——
其不再決定任何格之待遇，只決定人讀之先後。R-PMH98 之要求於此達成。

**本條同時改變偽陰之性質**：
  改造前 —— 某格因其用詞未被想到而**不存在於輸出**，**不可檢查**；
  改造後 —— 某格因其**謂詞域分類錯誤**而得 `未對照`，**可構造 must-hit**
            （一格含該斷言之用詞而被分入他域 → 須 FAIL）。

**R-PMH98 之實質不是消滅列舉，是使列舉之錯誤變成可檢查的。**

依據：26 包 §4 之 `audio` 落選 126 格，其輸出已含具名理由
（「其謂詞域為 `['state']`，與 `audio` 不交」）—— **該理由即一個
`未對照` 之判定**，只是不在 `VERDICT` 表內（26 包 §12 第 1 項自陳）。
```

## R-PMH101

```
R-PMH101（斷言之切分以謂詞為準，非以連接詞）
斷言之單位為**謂詞**：一個可各自為真為假之命題即一個斷言。

切分之作法為兩層：
(a) 機器以連接詞（` and `／` with `／` while `／`;`／`,`）**產生候選切分**；
(b) **人讀複核**其各切片是否各自可獨立為真為假，
    複核結果寫入常數（非只在上繳包）。

**不得以任一連接詞之有無單獨決定切分。**

依據：26 包以 ` and ` 切分得 23 個斷言，而
`-002` ER1 `The disclaimer screen is displayed with the "Accept" button`
含兩個可分之命題（畫面之顯示／按鈕之呈現）而其連接詞為 `with`，
**未被切開**；執行層自陳「**23 這個數字是該規則之產物**」
（26 包 §12 第 3 項）。
```

## R-PMH102

```
R-PMH102（掃描母體及於 Pre-Condition）
斷言掃描之母體及於 `pre_conditions`。

依 R-PMH97 之判別法（主語是否為 SUT）：
  `expected_result` —— 多為 SUT 行為斷言，**入母體**；
  `pre_conditions`  —— **SUT 之狀態斷言**（`The system has reported ready`），
                      **入母體**；
  `test_procedure`  —— 測試員之操作，屬測試執行斷言，**不入母體**。

**Pre-Condition 之牴觸比 ER 之牴觸更早失效**：若素材某格斷言
「在該情境下 SUT 不可能處於該狀態」，則該 TC 之前提無法建立，
**整條 TC 不可執行**，而其 ER 是否牴觸已無意義。

依據：26 包 §12 第 6 項（執行層自陳只掃 `expected_result`）。
```


## 抄錄逐條核對表（27 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH100 | 落選即判定，消滅「落選」類別；偽陰自此可檢查 | 526 | `5ca9d19aee81fa98` | `5ca9d19aee81fa98` | ✅ 逐字相符 |
| R-PMH101 | 斷言之切分以謂詞為準，兩層作法 | 395 | `74ca235020e7ce60` | `74ca235020e7ce60` | ✅ 逐字相符 |
| R-PMH102 | 掃描母體及於 `pre_conditions`；其牴觸較 ER 更早失效 | 437 | `979ad49681c50b00` | `979ad49681c50b00` | ✅ 逐字相符 |

---

# 28 包 —— 覆核線之收束、apparatus 凍結與 batch 2 開批

## R-PMH103

```
R-PMH103（覆核線之收束判準）
一條覆核線（同一批產出之反覆查驗）於**該輪之自評項多數不指向
「產出可能有錯」而指向「檢查可更細」**時結束。

判別：逐項問「若此項不修，是否可能使某條 TC 之內容錯誤？」
  是 → 實質項，須處理；
  否 → 精化項，入 Phase 5 之待辦，**不阻斷開批**。

**精化項不因其未結清而使該批不可用** —— 其登記於 `DECISIONS.md`
之 KNOWN-INCOMPLETE，附其風險陳述。

依據：28 包 §2.3 —— 27 包之六項自評中三項實質、三項精化，
為 Phase 4 開批十六輪以來首次多數不指向產出。
同期產出 8 條 TC（7/48 leaf）而新增 53 條裁決、11 支檢查程式，
**缺口之產生率高於結清率且已維持十六輪**（§2.1）。
```

## R-PMH104

```
R-PMH104（apparatus 凍結）
自本包起，**不再新增檢查程式或檢查項**，除下列二情形：

(a) 某條已產出之 TC 經**實測**有誤（非「可能有誤」），且該誤為現行
    檢查所不能攔者；
(b) Pei 裁定。

現有 32 項 lint、13 支檢查程式、四詞記法、must-hit 註冊機制**全部保留並繼續執行**；
**凍結者為其增長，非其運作。**

**理由**：檢查之邊際產出已隨輪次遞減（§2.2 之發現集中於 13–24 包，
25–27 包所查出者為「檢查可更細」），而其成本為每輪一個完整往返。

**本條可由任一實測之 TC 缺陷解凍** —— 屆時新增之檢查須指名其所攔之
該項缺陷，不得泛化。
```


## 抄錄逐條核對表（28 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH103 | 覆核線之收束判準（實質項 vs 精化項） | 369 | `fb29dcf1d6aac404` | `fb29dcf1d6aac404` | ✅ 逐字相符 |
| R-PMH104 | apparatus 凍結；其解凍條件 | 323 | `7703ef72dbbf2c85` | `7703ef72dbbf2c85` | ✅ 逐字相符 |

## R-PMH105

```
R-PMH105（R-PMH103／R-PMH104 之核可生效）
Pei 於 2026-08-25 核可 R-PMH103（覆核線之收束判準）與
R-PMH104（apparatus 凍結）。二條即刻生效。

**其效力起算之三項**：
(a) batch 1（8 條、7 leaf）之覆核線**結束** ——
    其殘餘為三項精化（切分之連接詞列舉／`SPLIT_REVIEW` 無第二來源／
    規格側全枚舉未做）＋ `-007` 之 `L160` 待確認，
    全數入 `DECISIONS.md` 之 KNOWN-INCOMPLETE，**不阻斷開批**；
(b) **不再新增檢查程式或檢查項** —— 現有 32 項 lint 與 13 支程式
    全數保留並繼續執行；
(c) batch 2（`Startup Sounds`，ch 8，6 leaf）**開批**。

**解凍條件不變**（R-PMH104(a)(b)）：某條已產出之 TC 經**實測**有誤
且為現行檢查所不能攔者，或 Pei 裁定。
```

## R-PMH106

```
R-PMH106（三筆 DR 之發出授權）
Pei 於 2026-08-25 裁定發出 `DR-PMH5`／`DR-PMH6`／`DR-PMH7`，
其內容依 28a §三之最終全文。

**執行層不得代為發出**（R-PMH83）。其職責為：
(a) 將 §三之三份全文寫入 `DATA_REQUESTS.md`（或指向本檔）；
(b) `SENT` 欄**留空**，待 Pei 告知**實際發出日期與對象**後方填
    —— **不得以本包之日期充當**（R-PMH43）；
(c) 三者之狀態於填入日期前維持 `DRAFT`。

**內容之變更須記明**：`DR-PMH5` 自 21a 之初版起經**兩次變更**
（24 包增欄位之問；25 包該問由字級座標自答，性質降為「請確認」），
且 **21a 所載之「p9 矩陣與 p8 之 `SU3.)` 相衝」一項已撤回** ——
A-PMH21 於 24 包改判為 `未對照`（其欄位為 `HEADUNIT POWER OFF`，
而 `PITA6.1` 逐字載免責畫面顯示於 head unit 轉為 On，二者互斥）。
**寄出之版本不得含該已撤回之主張。**
```


## 抄錄逐條核對表（28a 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH105 | R-PMH103／R-PMH104 核可生效；覆核線結束、apparatus 凍結、batch 2 開批 | 470 | `abf53c1beca313fa` | `abf53c1beca313fa` | ✅ 逐字相符 |
| R-PMH106 | 三筆 DR 之發出授權；已撤回之主張不得寄出 | 514 | `11acf30c93066500` | `11acf30c93066500` | ✅ 逐字相符 |

## R-PMH107

```
R-PMH107（apparatus 凍結之範圍界定）
R-PMH104 所凍結者為**檢查邏輯之增長**，非**既有檢查對新資料之適用**。

判別法：該動作是否增加了「**檢查什麼種類的錯誤**」——
  增加種類者（新程式、新 lint 項、新判準）→ **凍結**；
  只是把既有種類套用到新資料者（既有斷言掃描跑一個新斷言、
  既有限定檢查讀該批之限定清單、既有檢查之期望值由寫死改為讀宣告）
  → **不凍結，且為義務**。

**理由**：每一新批次必帶進其自身之新斷言與新限定。
若其適用亦被凍結，則凍結等同「第一批之後不再驗任何東西」——
**非立 R-PMH104 之意**。

現行應為之二項（28 包 §10 第 1、5 項所指者）：
(a) `animation` 斷言之掃描（`-009`／`-010` 之 ER 含之）—— **應做**；
(b) R-PMH99(c) 之限定字串檢查**擴及 batch 2 之十二項** —— **應做**，
    其作法比照 28 §5.2 之一般化（讀該批之限定清單，非寫死 tc_id）。

依據：28a 上繳 §5 第 3 項 —— 執行層指出凍結後該掃描
「已不可能因『謹慎』而被排程，只可能因『已經出錯』而被排程」。
**該後果為分析層立 R-PMH104 時未寫明者。**
```

## R-PMH108

```
R-PMH108（`-013` 與 `-011` 之未定義項開 DR-PMH8）
下列二項為規格未定義而以措詞繞過者，**開 `DR-PMH8`**：

(a) `SSND 2.2)` 之「一日」**未定義其起算點**（午夜／點火週期／其他）——
    `-013` 現以「今日尚未播放過」與 `on the same day` 繞過；
(b) `SSND 2)` 之設定**未給其所在路徑** ——
    `-011` 現以「設定選單可達」繞過。

**DR 不在 R-PMH104 之凍結範圍內** —— 凍結者為檢查裝置，非對外詢問。

**其形態與 A-PMH22（`Else: Mute Active`）相同**：
以措詞繞過而不判讀，**繞過不使該未定義消失**，故仍須詢問。
執行層 28 §10 第 2 項自陳「未開 DR，因判其已由措詞繞過，
**惟該判斷未經裁定**」—— 本條即其裁定：**繞過與詢問並行，不互相取代。**

`DR-PMH8` 不阻斷 batch 2；若上游另有定義，`-013` 之步驟與
`-011` 之 pre-condition 須重寫。
```

## R-PMH109

```
R-PMH109（`-009` 之跨螢幕同步維持併入）
`Sounds will sync amongst all supported vehicle displays.` **維持併入 `-009`
之 ER4，不另立第三條**。

依據二項：
(a) canon §5.7 —— 其為同一觸發（駕駛門關閉引發之啟動音播放）之必然後果，
    **非另一觸發**；
(b) 該句**無其自身之觸發** —— 其主語為 `Sounds`，
    描述已在播放之聲音如何分佈，不描述何時開始播放。

**執行層 28 §10 第 4 項所提之另一讀法（其為獨立能力，則 leaf 012 應拆三條）
不採**，其理由：若視為獨立能力，則該 TC 之觸發仍須借用 `-009` 之門關閉，
**兩條將共用同一觸發而只在 ER 上不同** —— 正是 §5.7 所禁之拆法。

**惟其限度須具名**：本條只涵蓋**啟動音**之跨螢幕同步；
**告別音之跨螢幕同步（`-010`）未被任何 ER 斷言** ——
`-010` 之 ER 只驗其與關機動畫之同步。**登記為覆蓋缺口，不另立 TC**
（其屬同一 `Sounds will sync` 句，若上游確認該句涵蓋二者，
則 `-010` 之 ER 須增一條）。**併入 `DR-PMH8` 詢問。**
```


## 抄錄逐條核對表（29 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH107 | 凍結之範圍：檢查邏輯之增長 vs 既有檢查對新資料之適用 | 581 | `a6b76c2f4a928cfe` | `a6b76c2f4a928cfe` | 1 | ✅ 逐字相符 |
| R-PMH108 | `-013`／`-011` 之未定義項開 `DR-PMH8`；繞過與詢問並行 | 496 | `230743b664d34739` | `230743b664d34739` | 1 | ✅ 逐字相符 |
| R-PMH109 | `-009` 之跨螢幕同步維持併入；告別音之同步登記為覆蓋缺口 | 579 | `6ede4f6c7ae461b2` | `6ede4f6c7ae461b2` | 1 | ✅ 逐字相符 |

## R-PMH110

```
R-PMH110（三筆 DR 之 SENT 落實）
Pei 於 **2026-08-25** 發出 `DR-PMH5`／`DR-PMH6`／`DR-PMH7`，
其內容為 28a §三之全文（`DR-PMH5` 採其 §3.1）。

`DATA_REQUESTS.md` 之處置：
(a) 三者狀態由 `DRAFT` 改 **`SENT`**；
(b) 發出日期填 **2026-08-25**；
(c) 發出對象填規格 p1 所載之 `HMI Lead: Paolo Visconti` 或其現任接手人
    —— **若 Pei 所告之實際對象與此不同，以 Pei 所告者為準**，
    執行層不得自行認定；
(d) 發出管道欄**留空**，待 Pei 告知。

**`DR-PMH8` 不在本條範圍** —— 其於本裁定當下尚未開立（29 包步驟 5 方令），
狀態維持 `DRAFT`，發出另候 Pei。

**`SENT` 不等於 `ANSWERED`**（R-PMH82）——
**`DR-PMH5` 之阻斷於 `ANSWERED` 前不解除**，見 §三之提問。
```


## 抄錄逐條核對表（29a 包）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH110 | 三筆 DR 之 `SENT` 落實；`DR-PMH8` 不在其內；`SENT` ≠ `ANSWERED` | 492 | `68b1a265ba8cbe7e` | `68b1a265ba8cbe7e` | 1 | ✅ 逐字相符 |

## R-PMH111

```
R-PMH111（ch 9 之限縮解凍）
`Power Transitions` 組**解凍，得開批**。A-PMH18（p9 之能力矩陣無來源）
**維持 PENDING**，其阻斷範圍由「整組不得開批」限縮為下列條件式：

**任一 TC 之任一斷言若倚賴 p9 能力矩陣之內容，該條停並登記，不得產出。**

**判別法**（須逐條套用並具名結果）：該斷言之謂詞是否為
「**某受控對象於某電源狀態下是否可用**」——
受控對象指 `ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／`Headunit`，
電源狀態指 `KEY ON ENGINE ON`／`KEY ON ENGINE OFF (ACC or RUN)`／
`KEY OFF (No ACC position)`／`KEY OFF (ACC position available)` ×
`HEADUNIT POWER ON`／`OFF`。

**是 → 該條停**；否 → 得產出。

依據：ch 9 之 5 leaf 所依之 `PM1)` 其主題為 **IGN OFF 時之 popup 群**
（FOTA／Wi-Fi／Charge Now／`stay awake` 之時序），
**不涉及受控對象於各電源狀態下之可用性**（29a §3.2）。
二者主題不同，故 p9 之缺口不必然阻斷該 5 leaf。

**`DR-PMH5` 之(1)(2)兩問仍待答** —— 其答覆若確立 p9 之權威來源，
本組已產出之 TC 須依 R-PMH94 重掃其斷言。
```

## R-PMH112

```
R-PMH112（對上游已作陳述之更正義務）
我方於已發出之文件中對上游所作之作業狀態陳述，若其後因裁定而不再成立，
**須於下一次對外通信之首段更正之**，不得靜默改變作法。

現行適用：2026-08-25 發出之 `DR-PMH5` 逐字載
`Until (1) and (2) are clarified we have suspended test case authoring for
section 9 (Power Moding), which covers 5 requirements
(SWE1-HMI-PM-018-01 through -05).`
—— 該陳述因 R-PMH111 之解凍而不再成立。

**更正之載體為 `DR-PMH8`**（其尚未發出，狀態 `DRAFT`），
於其首段加入更正句；**不另發短箋**，以免對上游造成無謂之往返。
其逐字見 29b §三。

**更正之發出仍屬 Pei**（R-PMH83）—— 執行層只落檔。
```


## 抄錄逐條核對表（29b 包）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH111 | ch 9 限縮解凍；A-PMH18 之阻斷改為條件式判別法 | 690 | `94bdfb0c9888cb88` | `94bdfb0c9888cb88` | 1 | ✅ 逐字相符 |
| R-PMH112 | 對上游已作陳述之更正義務；載體為 `DR-PMH8` 首段 | 439 | `97b33607dd29c166` | `97b33607dd29c166` | 1 | ✅ 逐字相符 |

## R-PMH113

```
R-PMH113（batch 3 之限定授權）
`Power Transitions` 組之各 TC，其斷言涉及 head unit 於 key-off 後是否維持
喚醒者，**加 Pre-Condition**：

    No phone call or projection call is active

**其位置為 Pre-Condition 而非 procedure** —— 「無通話進行中」為一個**狀態**
（canon §4.4 之合法型態），非測試員之動作。
**不得為求與 R-PMH87 之七項一致而寫成 `Do not…` 形態** ——
**限定之位置由其型別決定，非由前例決定。**

其充分性：`r31`（`Call Ended`）與 `r32`（`Projection call ends`）之事件
**皆以「有一通進行中之通話」為前提**；無之則該事件不可能發生，二格不適用。

**連帶之覆蓋缺口**：「IGN OFF 時通話結束且有 popup 待顯示」之行為
只在矩陣有、規格未載，依 R-PMH55(b) 不得為其撰寫 TC，
**登記為覆蓋缺口並併入 `DR-PMH8`**。

**本授權不預判 `Power Accessory Delay` 與 `Radio off Delay` 是否同一**
（A-PMH24）—— 兩讀皆通向「須加限定」，故限定不待其釐清。
```

## R-PMH114

```
R-PMH114（A-PMH24 併入 `DR-PMH8` 為第四問）
A-PMH24（`Power Accessory Delay` 與 `Radio off Delay` 從未同時出現於任一
文件，二者是否指同一設定未知）**併入 `DR-PMH8`**，為其第四問。

**執行層所判「與 `DR-PMH5` 同源」不採** —— 三者對象不同：
`DR-PMH5` 問**文件之缺失**（p9 矩陣之來源）；
`DR-PMH7` 問**記法之未定義**（`VP`／`Else: Mute Active`／`Note:`）；
A-PMH24 問**兩個名詞是否指同一物**。
**其形態屬 `DR-PMH7` 之類，非 `DR-PMH5` 之類。**

`DR-PMH8` 尚未發出，故直接增問，不另發文。
```

## R-PMH115

```
R-PMH115（`PENDING-ON-DR` 登記簿）
凡某項判定之結論**繫於某 DR 之答覆**者，須登記於 `DECISIONS.md` 之
`PENDING-ON-DR` 一節，每筆四欄：

  (1) 該判定之所在（檔案、條目、格號）；
  (2) 其所繫之 DR 與其第幾問；
  (3) **答覆為何值時，該判定改為何** —— 逐值列出，不得只寫「須重看」；
  (4) 登記日期。

**DR 之狀態改為 `ANSWERED` 時，該簿中對應之各筆為必辦事項**，
須於該輪之上繳逐筆回報其處置。

**本簿不是檢查** —— 其不判定任何事、不產生 PASS／FAIL、
不增加「檢查什麼種類的錯誤」，**故不在 R-PMH104 之凍結範圍內**
（R-PMH107 之判別法）。

現行應登記者至少三筆：
  `r15` 之條件式判定（繫於 `DR-PMH5` (1)(2) 與 `DR-PMH7` Q1）；
  `r46`／`r47` 之納入限定（繫於 `DR-PMH7` Q2 —— 若答為「維持靜音」，
  batch 2 之六條限定即為過度限定）；
  `-013` 之「一日」與 `-011` 之設定路徑（繫於 `DR-PMH8` (a)(b)）。

依據：29b 上繳 §5 第 3 項 —— 執行層指出該條件式「寫在依據文字裡，
而依據文字不是機器可判之物，答覆到達時沒有任何東西會提醒我們回來改它」。
```


## 抄錄逐條核對表（30 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH113 | batch 3 之限定授權；限定之位置由型別決定，非由前例決定 | 609 | `b64fcc9f090e5e62` | `b64fcc9f090e5e62` | 1 | ✅ 逐字相符 |
| R-PMH114 | A-PMH24 併入 `DR-PMH8` 第四問；不採「與 `DR-PMH5` 同源」 | 357 | `4c809f779bd6a6bc` | `4c809f779bd6a6bc` | 1 | ✅ 逐字相符 |
| R-PMH115 | `PENDING-ON-DR` 登記簿；其不是檢查，不在凍結範圍 | 623 | `b97321495dec10ba` | `b97321495dec10ba` | 1 | ✅ 逐字相符 |

## R-PMH116

```
R-PMH116（apparatus 首次解凍 —— Final Step 檢查之強化）
依 R-PMH104(a) 解凍，**其範圍嚴格限於 lint 之
「canon §5.2B／§5.5 Final Step 含驗證意圖」一項之強化**，不及其餘。

**解凍之依據（實測，非可能）**：batch 3 之 `-017`／`-018`／`-019`／`-020`／
`-021` 五條，其 Final Step **無任何驗證子句**
（`record when the radio powers off`／`read the display`／
`Read the radio power state`），而該項檢查標 **PASS**。
其為 13 包 §4.3 已判過之同一違規類型，其檢查亦於 13 包加入。

**強化之要求三項**：
(a) 執行層須先查明現行判準為何放行，並具名其病灶；
(b) **must-hit**：本批五條之現行 Final Step 須 **FAIL**；
(c) **範圍向**：batch 1／batch 2 之現行 Final Step 須 **PASS**。

`Compare` 之處置**須具名** —— `-016` 之 `Compare the recorded duration with
the stated maximum` 為 §5.1 之 preferred verb 而未言其判準，
**其屬邊界**；判其通過或不通過皆可，**但須寫出理由並一體適用**。

**本次解凍用畢即恢復凍結。** 新增之檢查不得泛化至其他 canon 節。
```

## R-PMH117

```
R-PMH117（`-002` 之處置 —— 待 Pei 核可）
`SWE1-HMI-PM-002`（outline 7.1.1，`SU1.1)`）**判為 out of scope，
不寫入交付工作簿**，比照 R-PMH72 對 `-028` 之處置。

依據三項（與 `-028` 完全同型）：
(a) 其逐字將行為委於 `based on vehicle architecture. See CFTS009 for
    clarification.` —— 行為定義於**外部規格**（canon §8.4.2）；
(b) 本 feature **不持有 CFTS009**；
(c) 不取得而撰寫，須自行指定「哪一種架構對應哪一種轉換」，
    **即造值**（canon §8.4.1）。

**本條之效力起於 Pei 之核可** —— 其動到範圍（有 TC 之 leaf 由 47 降為 **46**），
而 R-PMH1 為範圍條文。**核可前 `-002` 維持停手、不產出、不寫入。**

**若 Pei 判其應產出**，則須先取得 CFTS009，或由 Pei 裁定一個架構為準；
**二者皆非分析層可代決。**

`Power Transitions` 組因而為 **5 leaf 有 TC**（`-018-01`～`-05`）、
**2 leaf 停手**（`-023` 依 R-PMH111、`-002` 依本條）。
```

## R-PMH118

```
R-PMH118（等價類之數量不決定技術）
`design_method` 之選定依 canon §12 之 first-match，
**其判準為輸入是否被劃分為等價類，非該 TC 之內含幾類**。

一條 TC 只涵蓋一個等價類者，其技術仍為 `等價劃分 (Equivalence Partitioning, EP)`；
**不因其只有一類而改判 `功能測試 (Functional based)`。**

依據：batch 3 之 `-018`（接受 FOTA）標 FUNC，而 `-019`／`-020`
（排程／取消、設定／取消）標 EP —— 三者同軸（使用者於同一 popup 上之選擇），
**其差別只在一條之內含幾個類**。canon §12 之
`Input partitioned valid / invalid → Equivalence Partitioning`
**未要求一條之內須含多類**。
執行層 30 包 §10 第 4 項已自陳其一致性可議。
```


## 抄錄逐條核對表（31 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH116 | apparatus 首次解凍，限 Final Step 檢查之強化；用畢恢復凍結 | 706 | `a1dca5d4759e0e2c` | `a1dca5d4759e0e2c` | 1 | ✅ 逐字相符 |
| R-PMH117 | `-002` 判 out of scope，**待 Pei 核可**（核可前不生效） | 626 | `896dc34b89c5597a` | `896dc34b89c5597a` | 1 | ✅ 逐字相符 |
| R-PMH118 | 等價類之數量不決定技術 | 442 | `782875467a48ebf0` | `782875467a48ebf0` | 1 | ✅ 逐字相符 |

> ~~⚠ **R-PMH117 標「待 Pei 核可」，核可前不生效**（其動到範圍：有 TC 之 leaf 47 → 46，而 R-PMH1 為範圍條文）。**抄錄不等於生效。**~~
>
> **勘誤（2026-08-25，正文未改一字，SHA256 不變）**：Pei 逐字裁定「**核可**」——
> **R-PMH117 已生效**。其連帶已於同日執行：`layer3_sections.tsv` 與 `outline_map.json`
> 之 `-002` 列標 `EXCLUDED-BY-R-PMH117`；`check_granularity.py` 之 `N_LEAF` 47 → **46** 並全項重跑；
> `framework.md` 之 Layer 2 表 `Power Transitions` 7 → **6**、合計 47 → **46**；
> **A6 錨點之組態由 `15×3+1×2` 改為 `14×3+2×2`**（沿用舊式會使 `min=1`，隔離失效）。

## R-PMH119

```
R-PMH119（R-PMH117 之核可生效）
Pei 於 2026-08-25 核可 R-PMH117。`SWE1-HMI-PM-002`（outline 7.1.1，`SU1.1)`）
**判為 out of scope，不寫入交付工作簿**，其效力自即刻起算。

**連帶三項，皆須重算不得沿用**：
(a) 有 TC 之 leaf 由 47 降為 **46**；
(b) `Power Transitions` 組為 **5 leaf 有 TC**（`-018-01`～`-05`）、
    **2 leaf 停手**（`-023` 依 R-PMH111、`-002` 依 R-PMH117）；
(c) `check_granularity.py` 之 `n_leaf` 由 47 改為 **46**，五項判準與六個
    must-hit 錨點之期望值隨分母重算並全項重跑。

**停手之三筆（`-002`／`-023`／`-028`）其內部台帳一律保留**
（`ANOMALIES.md`／`DECISIONS.md`／`layer3_sections.tsv` 之 `EXCLUDED` 註記）——
**「拿掉」之範圍為交付件，非台帳**（R-PMH72 之同一理由）。
```

## R-PMH120

```
R-PMH120（收尾計畫與覆核循環之上限）
本 feature 之 TC 產出以三批完成，各批得含一個以上之 Test Set：

  batch 4 —— `Startup Animation`(9) ＋ `Splash Screen`(3)   = 12 leaf
  batch 5 —— `Power Off Behavior`(8) ＋ `Off Road Plus`(2)   = 10 leaf
  batch 6 —— `Voice Assistant Key`(5)                        = 5 leaf

三批合計 **27 leaf**，加已完成之 18 leaf 為 **45**；
另 `-002`／`-023`／`-028` 三筆停手，合 48。

**每批之覆核循環上限為二輪**（產出一輪 ＋ 重做一輪）。
**第三輪起須上呈 Pei**，並於上呈時具名「為何二輪不足」。

依據：batch 1 費 16 輪、batch 2 與 batch 3 各費 2 輪
（apparatus 凍結後之實測）。**上限之作用不在催促，
在於使「又一輪」成為一個須被說明之事，而非預設。**
```

## R-PMH121

```
R-PMH121（DR 未覆之交付截止規則 —— 待 Pei 核可）
交付日至，而 `DR-PMH5`／`6`／`7`／`8` 有任一未 `ANSWERED` 者：

(a) **以現況交付** —— 46 leaf 之 TC 不因其未覆而延；
(b) `PENDING-ON-DR` 登記簿之各筆**全數轉為交付揭露事項**，
    隨交付附一份「已知未決清單」，逐筆載其判定、所繫之問、
    以及答覆為何值時該判定改為何（即該簿之第 (3) 欄）；
(c) 停手之三筆（`-002`／`-023`／`-028`）於該清單中另列一節，
    載其停手依據與其所需之上游輸入。

**本條之依據**：現行三批**無任何 `PENDING` 欄位**（其以「停手」而非
佔位處理），故 §8.4.3 之「含 PENDING 之工作簿不得出貨」**不觸發** ——
DR 未覆不阻斷該 46 leaf 之交付，其只影響 `PENDING-ON-DR` 之回頭複核。

**本條之效力起於 Pei 之核可**（交付政策屬 Pei）。核可前，交付日之處置未定。
```

> **核可生效（R-PMH132，2026-08-25，正文未改一字）** —— Pei 逐字裁定「裁 出34」。
> 其三項即刻生效；`PENDING-ON-DR` 須補入本輪所生之三筆。


## 抄錄逐條核對表（32 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH119 | R-PMH117 核可生效；三項連帶須重算 | 546 | `91d4d92a801d8bc3` | `91d4d92a801d8bc3` | 1 | ✅ 逐字相符 |
| R-PMH120 | 收尾計畫（三批）＋ 每批覆核循環上限二輪 | 520 | `7e0e469a04b1b50a` | `7e0e469a04b1b50a` | 1 | ✅ 逐字相符 |
| R-PMH121 | DR 未覆之交付截止規則（**待 Pei 核可**） | 481 | `04cdd9167e63da4b` | `04cdd9167e63da4b` | 1 | ✅ 逐字相符 |

> ⚠ **R-PMH121 標「待 Pei 核可」，核可前不生效**（交付政策屬 Pei）。**抄錄不等於生效。**

> **R-PMH119 之連帶已於 2026-08-25 先行執行** —— Pei 於 31 包後逐字裁定「核可」，
> 執行層當輪即落實（`N_LEAF` 47→46、台帳標記、granularity 全項重跑、A6 錨點重造）。
> **本條之抄錄為其追認，非其觸發**；32 包步驟 2 因而為**複驗**而非重做。

## R-PMH122

```
R-PMH122（追溯欄不得記載該條未驗證之句子）
`source_clause` 與 `specification_reference` 所載者，**須為該條實際驗證之句子**。

為使某項檢查通過而補入該條並未驗證之句子，**禁止** ——
其使追溯欄記載一件不實之事，**是把檢查做綠而不是把事做對**。

**檢查若因此不過，錯在檢查之對象指認，不在產出。**

依據：32 包停止條件 7 逐字為「`-001-01`／`-001-02` 之 `source_clause`
未含 `SU1.)` 之漏句子句」，而該子句實由 **`-024`** 承載
——**分析層以 leaf 指稱承載者，而承載者為 TC**；
`-001-01` 之另一條（`-025`）與 `-001-02`（`-026`）各驗別句，
補入即為不實。執行層拒絕補入並兩面並陳，**其處置正確**（32 包 §停止條件 7）。

**連帶**：停止條件之對象若為某一句之承載，**須以 TC 指稱，不得以 leaf 指稱**
—— 一個 leaf 可有多條 TC，各驗其不同之句。
```

## R-PMH123

```
R-PMH123（`A-PMH27` 之狀態詞採 `ACCEPTED`）
`A-PMH27`（`-002` 判 out of scope）之狀態詞為 **`ACCEPTED`**，非 `RESOLVED`。
**採認執行層 32 包之更正，分析層 32 包步驟 2 所令之 `RESOLVED` 撤回。**

其三項理由皆成立：
(a) 該缺口之**事實未消失** —— CFTS009 仍未持有，該行為仍無 TC；
(b) **R-PMH74 對同形態用的即 `ACCEPTED`**（`SU9.)`／`SU9.1)` 經裁定不補）；
(c) **R-PMH121(c) 之「已知未決清單」取 `ACCEPTED` 方成立** ——
    標 `RESOLVED` 者沒有理由出現在一份未決清單上。

**同理適用於 `-023`／`-028` 之狀態詞**，執行層須一併核對其一致。
```

> **撤回一部（R-PMH130，2026-08-25，正文未改一字）**：其末句「**同理適用於 `-023`／`-028`
> 之狀態詞**」中之 **`-023` 部分撤回** —— `-023` **仍在交付範圍內**，與經裁定不寫入之
> `-002`／`-028` 不同類；**標 `ACCEPTED` 會使人以為它已被裁定不寫入，而它沒有**。
> **`-028` 部分維持有效**（其已於 33 包改為 `ACCEPTED`）。

## R-PMH124

```
R-PMH124（一般化須同時及於期望值與母體）
既有檢查之一般化（R-PMH107 所稱「不凍結且為義務」者），
**須同時及於其期望值之來源與其母體之來源**。

只改期望值而母體仍為寫死之列舉者，**新資料永不進入該檢查**，
而該檢查仍會報 PASS —— 其形態為「檢查通過而未檢查」。

實施：一般化後須以**新批之資料**實跑一次，並比對其母體規模之變化；
規模未變者即為未竟。

依據：32 包 §兩件我自己抓到的 第 1 項 —— `--limit-must-hit` 之迴圈寫死
`("batch01","batch02")`，batch 3／4 從未進過該錨點；
**上繳草稿一度寫成 33/33 而實測 19/19**。
執行層之歸因逐字為「**28 §5.2 一般化之未竟處 —— 當時只改了期望值的來源，
沒改母體的來源**」。
```

## R-PMH125

```
R-PMH125（`layer3_sections.tsv` 增 `requirement_title` 欄）
`data/layer3_sections.tsv` 增一欄 `requirement_title`，其值逐字取自 037
`Analysis Report` 之 `Requirement Title` 欄。

**理由**：037 之子項分法（`-006-01`／`-02`／`-03` 等）**記載於該欄**，
而台帳未帶之，致「037 依何而分」在台帳上不可見
（32 包 §10 第 3 項，執行層自陳其三分為「我的讀法」）。

**分析層實測**（037 `Analysis Report`）：
  `-006-01` = `Start-up Animation Duration and Trigger`
  `-006-02` = `Shut-down Animation Duration`
  `-006-03` = `Shut-down Animation Trigger Conditions`
**分法為 037 之分法，非執行層之讀法**（canon §8.2：RD 為需求單位之權威）。

**連帶義務**：增欄後，各批之每一 TC 須驗其射程與其 leaf 之
`requirement_title` 相符，不符者具名。
```

> **撤回一部（R-PMH127，2026-08-25，正文未改一字）**：其「驗其射程與其 leaf 之
> `requirement_title` 相符」**撤回** —— **title 為標籤，DESC 為範圍**；改取 037 之
> `Requirement Description`。**其增欄之要求保留並擴充為兩欄**（`requirement_title` ＋
> `requirement_description`）。
> **實據**：33 包依本條以 title 比對得五處不符，分析層以 DESC 複驗，**其中三處為偽陽**。

## R-PMH126

```
R-PMH126（限定之依據須逐條導出，不得為樣板）
事件層限定之 `reasoning`，**須逐條具名該條之哪一個 ER 斷言與素材取相反值**。

**逐字相同之樣板不構成 R-PMH94 之「逐斷言導出」** ——
其於某些條上必為不成立之陳述（R-PMH43）。

泛稱（「本條之逾時斷言」「本條之音訊斷言」）**不得用於未實際含該斷言之條**；
該條若無與素材取相反值之斷言，**其限定即為 §8.5 之不必要窄化，須移除**。

依據：batch 4 之十四條 `reasoning` 皆含一字不差之
「與**本條之逾時斷言**同謂詞取相反值」，而逐條實查其 ER，
**九條無任何逾時斷言**（`-025`／`-027`／`-030`／`-031`／`-033`／`-034`／
`-035`／`-036`／`-037`）。
其中 `-035` 更因該限定而與其步驟 2 指涉同一顆實體按鍵
（`SU9.)` 之 `"Power Off" hard key` 即電源鍵），
**使測試員讀到「不要按這顆鍵」而後「按這顆鍵」**。
```


## 抄錄逐條核對表（33 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH122 | 追溯欄不得記載該條未驗證之句子；停止條件須以 TC 指稱承載者 | 482 | `55366ba34f74179b` | `55366ba34f74179b` | 1 | ✅ 逐字相符 |
| R-PMH123 | `A-PMH27` 採 `ACCEPTED`；分析層之 `RESOLVED` 撤回 | 395 | `ee77d0a36d1230ed` | `ee77d0a36d1230ed` | 1 | ✅ 逐字相符 |
| R-PMH124 | 一般化須同時及於期望值與母體 | 379 | `880a2d7e17eeae55` | `880a2d7e17eeae55` | 1 | ✅ 逐字相符 |
| R-PMH125 | TSV 增 `requirement_title`；037 為分法之權威 | 582 | `618b40eca70718e6` | `618b40eca70718e6` | 1 | ✅ 逐字相符 |
| R-PMH126 | 限定之依據須逐條導出，不得為樣板 | 473 | `007460230dc2e4eb` | `007460230dc2e4eb` | 1 | ✅ 逐字相符 |

## R-PMH127

```
R-PMH127（射程之比對取 `Requirement Description`）
TC 射程與其 leaf 之比對，**取 037 之 `Requirement Description` 欄**，
**不取 `Requirement Title`** —— title 為標籤，DESC 為範圍。

**R-PMH125 之比對欄更正**：該條「驗其射程與其 leaf 之
`requirement_title` 相符」**撤回**，改為 DESC。
**其增欄之要求保留並擴充**：`layer3_sections.tsv` 增
`requirement_title` **與 `requirement_description` 兩欄**。

依據：33 包依 R-PMH125 以 title 比對得五處不符，
**分析層以 DESC 複驗，其中三處為偽陽**：
  `-025` —— `-001-01` 之 DESC 第二句逐字為
    `If ignition remains OFF after animation, the system turns the screen black.`，
    `-025` 正是其標的；
  `-032` —— `-008-01` 之 DESC **兩個單位皆在**
    （`If the ignition cycle has not changed … only once per CAN BUS wake-up`），
    037 未替任何人選；其 title 與 DESC 之不一致屬上游（R-PMH26，只登記）。

**偽陽之成因為分析層令錯了欄**，非執行層之判讀。
```

## R-PMH128

```
R-PMH128（`-017`／`-018` 之 leaf 更正）
batch 3 之 `-017` 由 `SWE1-HMI-PM-018-01` 改掛 **`-018-02`**；
`-018` 由 `-018-02` 改掛 **`-018-03`**。

依據（037 `Requirement Description`）：
  `-018-02` = `If the user interacts with the FOTA popup, the system shall stay
    awake until the user has not interacted with the popup for 60 seconds.
    The maximum time … is 10 minutes.` —— **與 `-017` 逐項相符**；
  `-018-01` = 2.5 分鐘與 60 秒逾時 —— **為 `-016` 之標的**；
  `-018-03` = `Pop-up Priority 1: FOTA Update Available` —— **為 `-018` 之標的**。

**本更正不計入 batch 3 之輪數上限（R-PMH120）** ——
**更正一個事實錯誤不是重做一批**；其計入者為產出面之覆核循環。

**分析層之覆核責任記明**：batch 3 於 31 包經分析層覆核通過，
**而該次覆核未查 leaf 與 DESC 之對應** —— 其為分析層之遺漏。
`requirement_title`／`requirement_description` 兩欄不存在時該項不可查，
**惟不可查不等於已查**。
```

## R-PMH129

```
R-PMH129（`-024` 撤除；32 包 §4.2(a) 撤回）
batch 4 之 `-024`（`SU1.)` 之「動畫後呈現 splash，1.5 each」）**撤除**，
不寫入交付工作簿。

依據：該子句於 SYS1 匯出 **0 命中**（A-PMH03），037 因而**無對應 outline、
無 leaf**；依 **R-PMH55(b)**，無 leaf 之規格內容**不得為其撰寫 TC**。

**32 包 §4.2(a)（令 `-001-01`／`-001-02` 之 `source_clause` 須含該子句）
撤回** —— **該指示與 R-PMH55(b) 直接相衝，而執行層依指示照做，錯不在它。**
32 包之停止條件 7 一併失效。

**其內容登記為覆蓋缺口**（比照 `-028` 之 R-PMH72、A-PMH03 之既有登記），
**併入 `DR-PMH8`** —— 其問題為：該子句是否應納入 037？
若上游確認應納入，則其成為新 leaf，`Splash Screen` 組由 3 增為 4，
`-024` 屆時重寫。

**`-025`／`-026` 不受影響** —— 二者各有其 leaf（`-001-01` 之 DESC 第二句、
`-001-02`），其 `source_clause` 各取其所驗之句（R-PMH122）。

batch 4 由 14 條減為 **13 條**；`Splash Screen` 組為 **2 leaf 有 TC**
（`-001-01`／`-001-02`）＋ `-011`，合 3 leaf。
```

## R-PMH130

```
R-PMH130（`-023` 之狀態詞維持，不改 `ACCEPTED`）
`-023`（`PITA8`）之 anomaly 狀態詞**維持不改為 `ACCEPTED`**。
**採認執行層 33 包之判斷，分析層 33 包步驟 4 所令之一併改動撤回。**

其理由成立：`-023` **仍在交付範圍內**，其停手繫於 `DR-PMH5` 之答覆
（R-PMH111 之條件式），**與經裁定不寫入之 `-002`／`-028` 不同類**；
**標 `ACCEPTED` 會使人以為它已被裁定不寫入，而它沒有。**
該區別正是 R-PMH119(b) 所分者。

**三筆之狀態詞自此不同而各有其理由**：
  `-002`／`-028` → `ACCEPTED`（經裁定不寫入，其缺口事實不消失）；
  `-023` → 維持其原狀態（**待 DR 答覆，仍在範圍內**）。
```

## R-PMH131

```
R-PMH131（A-PMH28 定案 —— 流程圖之未涵蓋行為）
PDF p3–p7 流程圖文字層所載、而散文（p8–p11）**0 命中**之五類行為，
**不為其撰寫 TC**，登記為覆蓋缺口並併入 `DR-PMH8`。

依據：該五類行為於 037 **無對應 leaf**（其來源為流程圖而非散文，
037 之 `HMI Source ID` 皆指向散文之 outline），
依 **R-PMH55(b)**，無 leaf 之規格內容不得為其撰寫 TC。

**其與 R-PMH129 之 `-024` 同型且同時裁定**：
二者皆為「規格文件中存在、而 037 未納入」之內容；
其別在於 `-024` 之句因 SYS1 匯出漏句而未入 037（A-PMH03），
本五類因其載體為流程圖而未入 037（A-PMH04／A-PMH28）。
**處置相同：不寫 TC、登記缺口、入 DR。**

**其中 `toggle them one after another`（splash 之輪替順序）
直接落在 `-026`／`-033`／`-034` 之標的內** ——
該三條**維持不斷言其輪替順序**（§8.4.1 不造值），
其 `reasoning` 已具名，本條使該具名成為裁定而非暫置。

**流程圖之規範性本身仍未決** —— 本條只裁「不為其撰寫 TC」，
未裁「流程圖是否為規範性來源」。後者繫於 `DR-PMH8` 之答覆，
**須登記於 `PENDING-ON-DR`**：若上游確認流程圖為規範性且該五類應入 037，
則其成為新 leaf，屆時另批撰寫。
```

## R-PMH132

```
R-PMH132（R-PMH121 核可生效）
Pei 於 2026-08-25 核可 R-PMH121。DR 未覆之交付截止規則即刻生效：

(a) 交付日至而 `DR-PMH5`／`6`／`7`／`8` 有任一未 `ANSWERED` 者，
    **以現況交付**，其 TC 不因未覆而延；
(b) `PENDING-ON-DR` 登記簿之各筆**全數轉為交付揭露事項**，
    隨交付附一份「已知未決清單」，逐筆載其判定、所繫之問、
    及答覆為何值時該判定改為何；
(c) 停手之三筆（`-002`／`-023`／`-028`）另列一節，
    載其停手依據與其所需之上游輸入。

**連帶（本條生效後即須辦者）**：
`PENDING-ON-DR` 現有 10 筆，**須補入本輪所生之三筆**：
  `-024` 之撤除（繫於 `DR-PMH8` 之「該句是否應納入 037」）；
  A-PMH28 之五類（繫於 `DR-PMH8` 之流程圖規範性一問）；
  `-023` 之停手（繫於 `DR-PMH5`(1)(2)）—— **其狀態詞依 R-PMH130 維持，
  故其於未決清單中之出現理由為「待答」而非「已接受」**。
```


## 抄錄逐條核對表（34／34a 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH127 | 射程之比對取 `Requirement Description`；R-PMH125 之比對欄撤回 | 722 | `3cf3aa7cc03bd8ed` | `3cf3aa7cc03bd8ed` | 1 | ✅ 逐字相符 |
| R-PMH128 | `-017`／`-018` 之 leaf 更正；更正不計入輪數上限 | 737 | `065bb0558d84ce47` | `065bb0558d84ce47` | 1 | ✅ 逐字相符 |
| R-PMH129 | `-024` 撤除；32 包 §4.2(a) 撤回 | 704 | `07f8217a1426bb68` | `07f8217a1426bb68` | 1 | ✅ 逐字相符 |
| R-PMH130 | `-023` 之狀態詞維持；33 包步驟 4 之一併改動撤回 | 392 | `d13fb40f03759651` | `d13fb40f03759651` | 1 | ✅ 逐字相符 |
| R-PMH131 | A-PMH28 定案：不寫 TC、登記缺口、入 DR | 697 | `eac5e46245f19887` | `eac5e46245f19887` | 1 | ✅ 逐字相符 |
| R-PMH132 | R-PMH121 核可生效；`PENDING-ON-DR` 補三筆 | 530 | `75d2fabf5d246937` | `75d2fabf5d246937` | 1 | ✅ 逐字相符 |

## R-PMH133

```
R-PMH133（DESC 為斷言完整性之權威）
037 之 `Requirement Description` 為**該 leaf 應被驗證之範圍**之權威。

**每一 leaf 之 DESC 所含之每一斷言，須被掛在該 leaf 之 TC 集合完整涵蓋。**
涵蓋之單位為**斷言**（R-PMH101 之切分），非 TC、非 ER 之條。

依據二項：
  canon §6 —— `Final ER covers the **complete** Test Item outcome`
               （partial = incomplete）；
  canon §8.2 —— RD（037）為「什麼構成一個需求單位」之權威。

**分工自此明定**：
  **DESC 決定「要驗什麼」**；
  **PDF／SYS1 決定「其措詞為何」**（`source_clause` 之來源，R-PMH50／R-PMH75）。

**二者衝突時**：DESC 缺而 PDF 有者 → 該內容無 leaf，依 R-PMH55(b) 不寫 TC
（`-024` 之形態）；DESC 有而 PDF 側為破句者 → **以 DESC 為準**
（A-PMH25 之形態，34 包 §3.2）。

**本條之回溯效力**：凡以「素材不足」「無法確定」「破句」為由而未斷言者，
**須逐項對照 DESC 重判** —— 其前提可能只在 SYS1 側成立。
```

## R-PMH134

```
R-PMH134（追溯維度之封閉）
TC 與其 leaf 之對應，其比對維度**封閉為三項**：

  (1) **leaf 指派** —— TC 所掛之 leaf 是否為其 DESC 所述之行為之 leaf；
  (2) **斷言涵蓋** —— 該 leaf 之 DESC 之每一斷言是否被涵蓋（R-PMH133）；
  (3) **單位** —— TC 所用之計次／計時單位是否與 DESC 逐字相同。

**自本包之總結完成後，不再新增第四個維度**，除非：
  (a) 某條已交付或已產出之 TC 經**實測**有誤，且該誤為上開三項所不能攔；或
  (b) Pei 裁定。

**其判別與 R-PMH104 同** —— 增加「檢查什麼種類的對應」者為封閉之標的；
既有三項對新批之適用不是。

**理由**：33、34 兩包各新增一個維度，各回頭作廢一批已通過之產出
（33 之 title 打到 batch 3／4，34 之 DESC 打到 batch 1／3／4，
34 之單位打到 batch 3／4）。**維度一次加一個，則每一批都會被作廢 N 次。**
**一次做完並封閉，其總成本低於逐次加。**
```

## R-PMH135

```
R-PMH135（因新判準而生之修正不計入輪數上限）
R-PMH120 之「每批覆核循環上限二輪」，其所計者為**產出面之覆核循環**
（同一判準下，產出有誤而重做）。

**因新立或新修之判準而回頭所生之修正，不計入該上限**，
其比照 R-PMH128（更正一個事實錯誤不是重做一批）。

**惟其須具名**：該次修正之上繳須載明「本次修正繫於哪一條新判準」，
不得以「重做」之名記之 —— 二者之意義不同：
前者是**判準變了**，後者是**做錯了**。

依據：`-016`／`-026` 之射程不足係 R-PMH133 之產物，
而 batch 3 已覆核通過、batch 4 已用滿二輪（34 包 §12 第 3 項，執行層自陳
「其輪數如何計，未定」）。
```


## 抄錄逐條核對表（35 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH133 | DESC 為斷言完整性之權威；其回溯效力 | 633 | `8b9afef57405b1d3` | `8b9afef57405b1d3` | 1 | ✅ 逐字相符 |
| R-PMH134 | 追溯維度封閉為三項 | 511 | `1a49271c17a82617` | `1a49271c17a82617` | 1 | ✅ 逐字相符 |
| R-PMH135 | 因新判準而生之修正不計入輪數上限 | 335 | `77838e4e34085bff` | `77838e4e34085bff` | 1 | ✅ 逐字相符 |

## R-PMH136

```
R-PMH136（反向涵蓋 —— TC 之斷言須有 DESC 依據）
R-PMH133 之涵蓋為**雙向**：

  正向（35 包已做）—— DESC 之每一斷言須被 TC 涵蓋；
  **反向（未做）—— TC 之每一 ER 斷言須有其 leaf 之 DESC 依據。**

反向之違反即 **§8.4.1 之造值**（斷言了來源所無之內容）
或 **§8.4.2 之範圍捏造**（斷言了他 leaf 所有之內容）。

**本項屬 R-PMH134 已封閉之維度 (2)「斷言涵蓋」之另一向，非第四個維度。**

依據：35 包 §10 第 2 項 —— 執行層指出 037 之 DESC 會**增寫 PDF 所無之語義**
（`-003` 之 `which automatically equals Accept`），
而本 feature **只查了「未斷言」之側，反向之側未查** ——
**有多少 TC 斷言了 DESC 所無之內容，至今無人知道。**
```

## R-PMH137

```
R-PMH137（037 自身重複時之涵蓋認定 —— A-PMH30 定案）
037 於兩個 leaf 之 DESC 重複同一行為時，該行為**由任一 leaf 之 TC 涵蓋
即為已涵蓋**；於另一 leaf 記
`未涵蓋（重複於 {leaf}，由 {tc} 涵蓋）`，**不補 TC**。

理由三項：
(a) 補之即為**重複驗證**，其兩條之 pass/fail 恆同，
    canon §8.2.1 明禁「cramming related behaviors … creates duplicate
    traceability and double-test maintenance burden」；
(b) **不改 leaf 指派** —— 037 為需求單位之權威（canon §8.2）；
(c) **不對 RD 提異議** —— 重複是上游之事實，非其缺陷之主張。

現行二例（A-PMH30）：
  `-001-01` A1（門關閉→3 秒動畫）—— 由 `-028` 涵蓋（掛 `-006-01`）；
  `-003` A2（Maserati 無逾時）—— 由 `-004` 涵蓋（掛 `-001-05`）。

**交付揭露之義務**：二例須列入 R-PMH132(b) 之「已知未決清單」之一節，
載明「其行為已被驗證，其未涵蓋僅為追溯之位置」——
**使讀者不致將 `未涵蓋` 讀成 `未驗證`**。

**若交付方要求「每 leaf 之每一斷言於其本 leaf 上皆有 TC」，本條即不適用**，
屆時須另裁（35 包 §10 第 4 項所指之未定）。
```

## R-PMH138

```
R-PMH138（第二次解凍 —— 斷言涵蓋表之程式化承載）
依 R-PMH104(a) 解凍，**其範圍嚴格限於「DESC 逐斷言涵蓋表」之程式化**，
不及其餘。

**解凍之依據（實測，非可能）**：R-PMH134 所封閉之維度 (2)「斷言涵蓋」
**無任何檢查程式承載** —— 35 包之涵蓋表為一次人讀之產物；
而該次人讀於四批中查出**七處**（`-016` ×3、`-026` ×2、`-008`、`-025`），
**其中一處在 batch 1，經十九輪未被任何判準碰過**。
**batch 5／6 產出時，沒有東西會自動再做一次那張表。**

**其要求四項**：
(a) 自 037 讀 DESC、依 R-PMH101 切分（機器候選 ＋ 人讀複核）；
(b) 對每一 leaf 輸出其斷言 × 其 TC 集合之涵蓋表，
    未涵蓋者標 `未涵蓋`，並依 R-PMH137 區分「重複於他 leaf」者；
(c) **反向亦輸出**（R-PMH136）—— TC 之 ER 斷言無 DESC 依據者標 `無依據`；
(d) **must-hit**：刪去 `-016` 之 ER4 → 正向須報 `未涵蓋`；
    於 `-035` 增一條 DESC 所無之 ER → 反向須報 `無依據`。

**本次解凍用畢即恢復凍結**（R-PMH104）。
```


## 抄錄逐條核對表（36 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH136 | 反向涵蓋（TC 之斷言須有 DESC 依據）；屬維度 (2) 之另一向 | 433 | `0c48178345281323` | `0c48178345281323` | 1 | ✅ 逐字相符 |
| R-PMH137 | 037 自身重複時之涵蓋認定；A-PMH30 定案 | 697 | `32cb7496eddb0e80` | `32cb7496eddb0e80` | 1 | ✅ 逐字相符 |
| R-PMH138 | 第二次解凍 —— 涵蓋表之程式化承載；用畢恢復凍結 | 592 | `bac5e5f237cf40f5` | `bac5e5f237cf40f5` | 1 | ✅ 逐字相符 |

## R-PMH139

```
R-PMH139（例外條款之依據得取其本體 leaf）
某 leaf 之 DESC 以例外標記起首（`Exception:`／`unless`／`except`／
`Exception for`），且其**本體 leaf 可資辨識**者，
其 TC 之 ER 得以**本體 leaf 之 DESC** 為依據，
**不計為 canon §8.4.2 之範圍捏造**（R-PMH136 之反向涵蓋於此不報 `無依據`）。

**其條件二項**：
(a) 該 ER 所斷言者須為**本體 leaf 已載之行為**，非新增之行為；
(b) `reasoning` 須**具名其本體 leaf**，使追溯可循。

現行適用：`-004`（leaf `-001-05`，DESC 為
`**Exception:** For Maserati applications, the system provides no timeout
(per CFTS009); the user must manually press Accept.`）之 ER3
`The disclaimer screen is removed and the last mode screen is displayed`
—— 其依據為本體 leaf `-001-04` 之 `press Accept to go directly to last mode screen`。

**不採（甲）刪去 ER3 之理由**：例外條款不重述其本體之後續行為，
為規格書寫之常態；刪之則該條之 procedure 終於「按下 Accept」而無結果，
**違 canon §5.5**（Final Step 須持有可觀察之驗證標的）。
```

## R-PMH140

```
R-PMH140（許可式之斷言處置）
`source_clause` 以許可式書寫者（`can`／`may`／`is able to`），
其保證該行為之**容許**，不保證其**必然發生**。

其 ER 之寫法：**以「於本條所述之條件下實測其發生」為之**，
**並須於 `reasoning` 具名三事**：
(a) 其來源為許可式；
(b) 本 TC 所驗者為「於該條件下該行為確實可發生」；
(c) **其不發生不必然為缺陷** —— 判 fail 前須先確認該條件確已成立。

**不另開 DR** —— 許可式為規格之常見書寫，非未定義之記法；
其與 A-PMH22（`Else: Mute Active` 之記法未定義）不同類。
**採認執行層 36 包 §10 第 4 項之判斷（「不值再增一問」），本條使其成為裁定。**

現行適用：`-042`（`PITA9: Phone call popups **can** be displayed …`）、
`-045`（`PITA10: SOS and ASSIST **can** turn head unit power back on.`）。
```

## R-PMH141

```
R-PMH141（priority 之依據與級別須於同一條之內相符）
R-PMH59 所規之「priority 依據須批內互不矛盾」，**擴及一條之內**：
該 TC 之 `priority` 欄之值，須與其 `reasoning`／軸註中所載之依據相符。

**檢查方式**：凡 `reasoning` 或軸註中出現 `P0`／`P1`／`P2`／`P3` 之字樣者，
其與 `priority` 欄比對；不符即 FAIL。**此項不可機械涵蓋於現行 lint
（apparatus 凍結，R-PMH104），故列為人讀覆核之必查項。**

依據：`-045` 之 `priority` 欄為 `P1`，而其軸註逐字為
`等價類：緊急呼叫鍵之電源回復（**本批唯一之 P0**）` ——
**同一條之內，依據寫 P0 而級別填 P1**；
且 P0 為正解（canon §10.2 之 P0 明列 `safety`／`eCall`）。
```


## 抄錄逐條核對表（37 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH139 | 例外條款之依據得取其本體 leaf | 746 | `fd15fbb8599d6d1a` | `fd15fbb8599d6d1a` | 1 | ✅ 逐字相符 |
| R-PMH140 | 許可式之斷言處置；不另開 DR | 509 | `cf25538cf5c6196a` | `cf25538cf5c6196a` | 1 | ✅ 逐字相符 |
| R-PMH141 | priority 之依據與級別須於同一條之內相符 | 419 | `b9bbbd71e7cd7248` | `b9bbbd71e7cd7248` | 1 | ✅ 逐字相符 |

## R-PMH142

```
R-PMH142（`-050`～`-053` 之封鎖）
`-050`／`-051`／`-052`／`-053` 四條標 **`BLOCKED-UNTIL-DR`**，
**其狀態為「已產出、不可執行」**，於交付時隨附其封鎖依據。

依據：四條之 `test_procedure` 逐字相同而其 `expected_result` **互斥**
（螢幕開關 × 音訊開關之四個組合）——
**同一組步驟執行一次只會落在一類，四條之中至多一條能通過，
其餘三條必然 fail**，其為 canon §7 之 **false fail**（因設計而失敗，非因缺陷）。

**成因不在撰寫** —— 規格 `VRLP1` 與 037 之 DESC **皆未言如何使互動之結果
落在某一類**；執行層於無條件可寫時未造值（§8.4.1），其處置正確。
**其代價為該四條不可執行，該代價須被記為封鎖，不得被記為通過。**

**`DR-PMH8` 增第九問**：該四種結果各自之適用條件為何。

**解封條件**：`DR-PMH8` Q9 `ANSWERED` 且其答覆載明各類之條件；
屆時四條各加其條件為 Pre-Condition，`BLOCKED` 解除。
**若答覆為「四者皆為可能之結果而無條件之分」**，則四條**併為一條**
（其 ER 為「結果為所列四類之一」），並以 R-PMH137 之形態於其餘三 leaf
記 `未涵蓋-重複`。**二路皆須屆時另裁，本條不預判。**

**入 `PENDING-ON-DR`**（第 15 筆），第 (3) 欄逐值列出上開二路。
```

## R-PMH143

```
R-PMH143（`tc_id` 之單次指派規則）
Phase 5 之 `tc_id` 單次指派，其規則四項：

(a) **連續編號，不留空** —— provisional 期間之空位（`-024` 依 R-PMH129
    撤除所遺者）**不保留**；provisional 本為暫號，其連續性無保存價值；
(b) 編號順序依 **Test Set 之 Layer 2 定版順序**（R-PMH36：`Splash Screen` →
    `Disclaimer Screen` → `Startup Animation` → `Startup Sounds` →
    `Power Transitions` → `Power Off Behavior` → `Voice Assistant Key` →
    `Off Road Plus`），組內依其 leaf 之 037 列序；
(c) 格式為 `NR1L-DisclaimerScreen-{NNN}`（R-PMH16），`NNN` 自 `001` 起；
(d) **須產出 provisional → final 之映射表**並落檔於
    `data/tc_id_map.tsv`，其為 TestRail 對應與日後追溯之依據。

**指派後 `tc_id_status` 由 `provisional` 改 `final`**，
`check_write_back` 之第四項（R-PMH104 時期所加之 provisional 防護）
於其為 `final` 時方放行。
```

## R-PMH144

```
R-PMH144（`and`／`or` 並列之一次性全批掃描）
A-PMH31（`and`／`or` 並列之語意未定）之範圍**擴及全六批**，
以**一次性人讀**為之，**不建檢查程式**（apparatus 凍結，R-PMH104）。

其產出為一份清單：逐項載該 TC、其並列之逐字、其兩讀、
以及本 feature 現行採何讀及其理由。
**採「兩讀皆涵蓋之處置」者（R-PMH95）記明之，不必開 DR；
採其一讀而另一讀未涵蓋者，入 `PENDING-ON-DR`。**

依據：37 包 §10 第 3 項 —— 執行層自陳其只查了 batch 6 之四條，
**其餘五批未查**。
```


## 抄錄逐條核對表（38 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH142 | `-050`～`-053` 封鎖；其解封二路不預判 | 691 | `1299376430c8f112` | `1299376430c8f112` | 1 | ✅ 逐字相符 |
| R-PMH143 | `tc_id` 單次指派四項規則 ＋ 映射表 | 682 | `e4a4a1ceca117d89` | `e4a4a1ceca117d89` | 1 | ✅ 逐字相符 |
| R-PMH144 | `and`／`or` 之一次性全批掃描，不建程式 | 300 | `793d5756a4658f48` | `793d5756a4658f48` | 1 | ✅ 逐字相符 |

## R-PMH145

```
R-PMH145（Q10 定案 —— `Product Document 記錄封面頁` 不填）
`Product Document 記錄封面頁` **整張分頁不填**，維持母本現況（僅標籤、值全空）。

Pei 於 2026-08-25 裁定。

**其語料與 R-PMH27 之不同須記明**：D5 之語料為 9 空／7 非空，
本項為 **4 空／12 填** —— **本裁定明知其為語料之少數側**。
其依據非多數，而為三項成本：
(a) 五個欄位之字串須由我方自擬（`B3` `new R1L`(8) vs `NR1L`(4)、`B4` 文件名、
    `B5` `V1.0`(11) vs `Initial`(1)、`B8` 日期格式、`A13:D13` 修訂列）；
(b) `B4` 取檔名即依賴上游命名，**與 R-PMH26(d) 相衝**；
    其值不得自客戶那份複製，**與 R-PMH23 相衝**；
(c) `B7` 帶 DV 而 `check_write_back` 之三項不涵蓋之。

**其為交付揭露事項** —— 入 R-PMH132(b) 之「已知未決清單」一節，
載明「本欄依裁定留空，與 12/16 之語料多數不同」，
**使交付方一望即知其為選擇而非遺漏**。
```

## R-PMH146

```
R-PMH146（profile §1.2 之落檔 —— 一次性授權）
Pei 於 2026-08-25 授權於
`docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` **增一節 §1.2**，
其內容為 38a §三之全文，**逐字，一次**。

**明文不授權**：該檔之其他任何節、`docs/runtime/` 下之其他任何檔案。
**R-PMH46 之一次性授權已用畢，本條為第二次且獨立**。

**驗證義務**：寫入後以逐字比對證明其與 §三之區塊相同，
並附該檔之前後 SHA256 與行數變化；**§1 原文不得改一字**。

**其必要性**：R-PMH75（9.1 之 `source_clause` 取 SYS1）只記於 `RULINGS.md`，
而 profile §1 仍載「判讀基準為 PDF、SYS1 為追溯用」。
**profile 為給未來讀者與其他 session 之規則書** ——
依其字面「修正」該 8 條之 `source_clause_origin`，
**恰會把 A-PMH16 所查出、SYS1 已刪之舊文字放回**
（`for 60 seconds`／`the radio should shut Off`）。

**本條不改變 R-PMH75 之效力**，只使規則書與實作一致。
```


## 抄錄逐條核對表（38a 包）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH145 | Q10 定案：不填；其為語料少數側之選擇，須揭露 | 555 | `c8e18052baf1d67d` | `c8e18052baf1d67d` | 1 | ✅ 逐字相符 |
| R-PMH146 | profile §1.2 之一次性落檔授權 | 599 | `843bf29c164246d3` | `843bf29c164246d3` | 1 | ✅ 逐字相符 |

## R-PMH147

```
R-PMH147（A-PMH32 之處置 —— 擴而不拆）
`-012`／`-013` 之步驟與 ER **擴及告別音側**，**不拆為四條**。

依據：其軸為 `SSND 2)` 之設定三值（`Always`／`Once a Day`／`Never`），
**其驗證單位為「該設定值對兩種聲音之效果」** ——
`-014` 已於一條之內涵蓋二者，拆 `-012`／`-013` 而不拆 `-014`
將使同軸三條之單位不一（R-PMH59 之精神）。

**與 canon §5.7 之張力具名**：門關閉與關機動畫為兩個觸發，
惟此處之驗證單位由**設定值**定義而非由觸發定義；
且拆分將使 `-014` 亦須拆為兩條幾近同義之負向條，
而 canon §7 只要求「至少一條負向」。

**成因記明**：`SSND 2.1)`／`2.2)` 之句子自身不一致 ——
主語為 `start-up **and** goodbye sounds` 而觸發只寫 `startup animation`；
執行層「取了字面之觸發而未取字面之主語」（38 包自陳）。
**不開 DR** —— 其為規格書寫之不精確，非未定義之記法，
且擴涵蓋後兩讀皆被涵蓋（R-PMH95 之形態）。
```

## R-PMH148

```
R-PMH148（`workbook_state` 維持 `BLANK`，另立 `delivery_state`）
`feature.yaml` 之 `workbook_state` **維持 `BLANK`**，不因寫回而改。

理由：該欄描述**交付基底之初始狀態**，其為歷史事實
（R-PMH8：母本資料區非空儲存格 0），**不因其後之寫入而改變**；
改之則日後無從得知本 feature 起始於空白母本。

**另增 `delivery_state`**，其值為 `WRITTEN`，
並記其工作副本之路徑與 SHA256、寫入列數、寫回日期。

依據：38 包所指之「`workbook_state` 是否要改未裁」。
```

## R-PMH149

```
R-PMH149（停手三筆之工作簿無痕跡 —— 不改工作簿，於交付文件載明）
`-002`／`-023`／`-028` 三筆不寫入工作簿**維持**，
**不比照 comfort 之「未產出 TC 之 leaf 仍佔一列」**。

理由：其不寫入係**依裁定**（R-PMH72／R-PMH117／R-PMH111），
而 R-PMH47(b) 之「該列仍寫入並揭露」已於 19a 經 Pei 裁定
「`DR-PMH1` 拿掉」而撤回。**工作簿看不到它們是裁定之結果，非遺漏。**

**惟其須於交付文件載明** —— `DELIVERY_NOTE.md` 須明載
**48 leaf → 45 leaf 有 TC** 之差，及其三筆各自之依據與所需之上游輸入，
使交付方不必自工作簿反推。

依據：38 包 §10 第 3 項 —— 執行層指出「若交付方只看工作簿，
48 → 45 之差是看不出來的」，**且其未裁**。
```


## 抄錄逐條核對表（39 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH147 | A-PMH32 擴而不拆；與 §5.7 之張力具名 | 543 | `db3754369b99b4f9` | `db3754369b99b4f9` | 1 | ✅ 逐字相符 |
| R-PMH148 | `workbook_state` 維持 `BLANK`，另立 `delivery_state` | 318 | `11d2154f0e1321fa` | `11d2154f0e1321fa` | 1 | ✅ 逐字相符 |
| R-PMH149 | 停手三筆不改工作簿，於 `DELIVERY_NOTE.md` 載明 | 414 | `fc3d0f85e3a59a28` | `fc3d0f85e3a59a28` | 1 | ✅ 逐字相符 |

## R-PMH150

```
R-PMH150（#11／#12 照預設排除 —— DR-PMH8 Q6／Q7 降格為告知性附註）
未決清單第 11 筆（`SU1.)` 之 splash 1.5s 句，A-PMH29／R-PMH129）與
第 12 筆（p3–p7 流程圖五類行為，A-PMH28／R-PMH131）**照既定預設排除**：
範圍以 037 之 leaf 全集為界，037 未載者不納入本輪交付，
**永久登記為覆蓋缺口**（DELIVERY_NOTE §9 第 4、5 項維持，加註「依本條屬裁定排除」）。

**DR-PMH8 之 Q6／Q7 就地降格為〔告知性附註〕**：保留原編號不重編
（Q1–Q9 之交叉引用已遍布未決清單），於題前標註
「本問為通報上游漏項之附註，其答覆不改變本輪交付物；
 若上游日後裁納入，屬新 leaf 之變更申請，於 Revise 批次另案處理」。

效果：未決清單第 11／12 筆**結案**，結案詞 `CLOSED-BY-RULING`。
其(甲)路（成為新 leaf、n_leaf 增）不再是本輪之可能結果。

裁定：Pei，2026-08-26（「#11/#12 照預設排除」）。
```

## R-PMH151

```
R-PMH151（`-002`／`-028` 之停手改判「依裁定結案」—— 不再等 CFTS009）
`SWE1-HMI-PM-002`（7.1.1 SU1.1)）與 `SWE1-HMI-PM-028`（12.2 OFF2)）
二筆維持不寫入工作簿，惟其性質由「停手待上游輸入（CFTS009）」
**改判為「OUT-OF-SCOPE，依裁定結案」**：

- `-002`：行為逐字委於 `based on vehicle architecture. See CFTS009 for
  clarification.`；`-028`：內文逐字為 `Please refer to CFTS009 for complete
  behavior.`。二者之行為定義皆在外部規格 CFTS009，
  依 IN §8.4.2（行為定義於被引用之外部規格者，屬該規格 owner 之
  SWE 需求範圍，不得由本 feature 吸收），**出範圍，記 coverage note 結案**。
- **CFTS009 不再是本 feature 之待取件**；取得與否不改變本輪交付。
  若日後取得且上游要求納入，屬範圍變更，另案。

效果：停手清單 3 → **1**（僅餘 `-023`，其仍繫 DR-PMH5，維持
STOPPED-PENDING-DR）。`DELIVERY_NOTE.md` §2 之「所需之上游輸入」欄，
`-002`／`-028` 二列改為「無 —— 依 R-PMH151 結案」；統計數字不變
（48／45／3 之 3 維持，惟 3 = 1 停手 + 2 依裁定結案，表下註明）。

沿革：本條**取代** R-PMH117／R-PMH72 中「待 CFTS009」之等待語義，
其「不寫入工作簿」之處分維持（R-PMH149 亦不受影響）。

裁定：Pei，2026-08-26（「002（停手）028（停手）」——
經分析層確認其意為結案而非續等，Pei 以「出」核可）。
```

## R-PMH152

```
R-PMH152（#9／#10 之終態為揭露 —— 不開 Q10／Q11）
未決清單第 9 筆（`-017` 之「60 秒無互動」與「總計 10 分鐘」交互作用
不斷言）與第 10 筆（A-PMH25——`-016` 不斷言逾時秒數）**不另開問**：
DR-PMH8 不增列 Q10／Q11，二筆之(丙)路（未開問、風險續存）
**依裁定為終態**，結案詞 `ACCEPTED-RISK`。

其風險承擔須於 DELIVERY_NOTE §9 具名為獨立二項：
- `-016` 之逾時秒數無任何 TC 驗到（與 R-PMH75 之
  `the radio should shut Off` 風險同源而非同項，分列）；
- `-017` 之二上限交互作用無任何 TC 驗到。

日後若上游主動釐清，屬 Revise 批次，屆時依第 9／10 筆原載之
(甲)(乙)路處置，本條不預判。

裁定：Pei，2026-08-26（分析層提議「不另開問、揭露為終態」，Pei 以「出」核可）。
```


## 抄錄逐條核對表（39a 包步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS **讀回** SHA256（前 16） | 命中數 | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH150 | #11／#12 照預設排除；Q6／Q7 降格為告知性附註 | 507 | `d469fac0a1b7c56f` | `d469fac0a1b7c56f` | 1 | ✅ 逐字相符 |
| R-PMH151 | `-002`／`-028` 依裁定結案，不再等 CFTS009 | 853 | `ea6a108b1a712f29` | `ea6a108b1a712f29` | 1 | ✅ 逐字相符 |
| R-PMH152 | #9／#10 之終態為揭露，不開 Q10／Q11 | 445 | `9822c575ce2c9d9a` | `9822c575ce2c9d9a` | 1 | ✅ 逐字相符 |

> **本包只追加，既有條文一 byte 未改**（含 R-PMH72／R-PMH117）——
> **R-PMH151 以沿革語句取代其「待 CFTS009」之等待語義，不回改原文**（R-PMH44）。
