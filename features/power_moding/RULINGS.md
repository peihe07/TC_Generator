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
