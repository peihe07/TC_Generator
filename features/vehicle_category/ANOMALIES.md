# ANOMALIES — FW036 Vehicle Category HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-VCnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

| A | 內容 | 狀態 | Tier |
|---|---|---|---|
| A-VC1 | 037 第 10–18 欄全為 `\xa0` —— **本輪重測未重現** | **NOT REPRODUCED** | Tier 2（條文須重裁）|
| A-VC2 | 037 封面 `Reviewer：` 空、`Date：` 為 2020/09/05 | PENDING | Tier 2（是否回報上游）|
| A-VC3 | §16.2 之 `SWE1-HMI-VC-066` 僅涵蓋標題一句 | PENDING | 併入 DR-VC3 |
| A-VC4 | `new_feature.py` 之 abbr 推導得 `VE`，非 R-VC1 之 `VC` | PENDING | Tier 2（工具修法）|
| A-VC5 | 下放包 §3.3 與 repo 037 複本不一致（A-VC1 之成因）| PENDING | **Tier 2（阻斷 T4 收斂）** |
| A-VC6 | `recon.py` 於 `spec_reference_template: null` 崩潰 | PENDING | **Tier 2（阻斷 T3 產出）** |
| A-VC7 | 規格 PDF 之位元組數與下放包 §3.1 不符 | PENDING | Tier 2 |

---

## A-VC1 —— 037 第 10–18 欄之 `\xa0`（下放包 §七原文；**本輪重測未重現**）

**下放包原登記內容**：037 `Analysis Report` 第 10–18 欄（`Feasibility` …
`Priority`）全 145 列皆為 `\xa0`（U+00A0），非空字串。

**下放包提案處置**：執行層讀取時一律 strip 含 `\xa0`；不視為已填。
**不回報上游**（表單樣板行為，非本案缺陷）。

**本輪重測（2026-08-25，repo 內複本）—— 未重現**

量測對象：`features/vehicle_category/inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx`
（SHA256 `cb80a77e8d57721ef0851c4ce263c46d3cbf5d028bd1a03c89c9d7debfd877ed`，100,475 B）
方法：`openpyxl read_only=True, data_only=True`；逐欄取 145 個資料列之原始值集合。

| 欄 | 表頭 | `\xa0` 列數 | 有內容列數 | 有內容列 == 117 leaf ? |
|---|---|---|---|---|
| 10 | Feasibility | 28 | 117 | 是 |
| 11 | Description/Action for Feasibility | 28 | 117 | 是 |
| 12 | Impact | 28 | 117 | 是 |
| 13 | Description/Action for Impact | 28 | 117 | 是 |
| 14 | Risk Factor | 28 | 117 | 是 |
| 15 | Description/Action for Risk Factor | 28 | 117 | 是 |
| 16 | Reusable | 25 | 117 | 是 |
| 17 | Description/Action for Reusable | 25 | 117 | 是 |
| 18 | Priority | 28 | 117 | 是 |

九欄**皆非**「全 145 列為 `\xa0`」。其實際形態為：
**28 個「有子之父」為 `\xa0`，117 個 leaf 皆有實質內容**。
（例：欄 10 `Feasibility` 之分布為 `{'\xa0': 28, 'Yes': 117}`。）

欄 16／17 之 `\xa0` 為 25 而非 28 —— 差額 3 列
（列 70 `SWE1-HMI-VC-034`、列 118 `SWE1-HMI-VC-052`、列 142 `SWE1-HMI-VC-063`）
之值為 `None`（真空儲存格），既非 `\xa0` 亦非內容。

**提案處置（Tier 2，不自行處置）**

(a) A-VC1 之條文以其前提為據（「無內容」），該前提在 repo 複本上不成立，
    故條文**須重裁**，不得沿用。
(b) 「讀取時 strip 含 `\xa0`」之技術手段仍然正確且應保留 ——
    錯的是「不視為已填」之推論：這九欄在 117 個 leaf 上**是已填的**。
(c) 成因見 A-VC5。在 A-VC5 裁定前，本項不得標為 RESOLVED。

---

## A-VC2 —— 037 封面之 Reviewer 空白與日期矛盾（下放包 §七原文）

**內容**：037 封面 `Reviewer：` 為空；`Date：` 為 `2020/09/05`，
與修訂履歷（2025-12-26 ~ 2026-04-27）矛盾。

**提案處置**：判為表單樣板殘留。登記留痕；**不得引用該日期為版本依據**。
是否回報上游由 Pei 定。

狀態：PENDING。本輪未對封面另作重測（不在 T4 之列舉範圍）。

---

## A-VC3 —— §16.2 之需求涵蓋不足（下放包 §七原文）

**內容**：規格 §16.2 之對應需求 `SWE1-HMI-VC-066` 僅涵蓋「widget 標題為
Cabrio」一句，其下之 16.2.1 / 16.2.2（實際操作行為）無對應需求。

**提案處置**：併入 DR-VC3 一併查詢，**不單獨發 DR**。

狀態：PENDING。本輪 T4 已確認 16.1 / 16.2.1 / 16.2.2 確在未引用之 42 節內。

---

## A-VC4 —— `new_feature.py` 之 abbr 推導無法產生規定之前綴

（下放包落檔後由 Pei 於 T0c 指示登記，條文逐字如下。）

```
A-VC4（new_feature.py 之 abbr 推導無法產生規定之前綴）

`scripts/new_feature.py` 以 `abbr = feature[:2].upper()` 推導標記前綴，
對 `Vehicle_Category` 產出 `VE`，而 R-VC1 規定之前綴為 `VC`。
骨架所生之 `RUNBOOK.md` / `DECISIONS.md` / `PLAYBOOK.md` / `ANOMALIES.md`
因此帶錯誤前綴，須以 T0b 之事後字串更正處理。

提案處置：與 A-TM04（`new_feature.py` 拒絕空格而非 slugify，狀態
PENDING / Tier 2）同批處理 —— 兩者同源，皆為 `new_feature.py` 之
命名推導不足。

**本輪不實作、不併案，僅登記。** 腳本之修改屬 Tier 2，
且本包 §五明文「不得預先改腳本」。
```

狀態：PENDING。T0b 之字串更正已完成，驗證 grep 命中數 0（見上繳包 §1）。

---

## A-VC5 —— 下放包 §3.3 之量測對象與 repo 內複本不一致

**證據**

1. 檔案大小一致：下放包 §3.1 記 037 為 100,475 B；repo 內複本亦為 100,475 B。
2. 內容不一致：§3.3 記第 10–18 欄「全 145 列皆為 `\xa0`，無內容」；
   repo 內複本之同九欄於 117 個 leaf 皆有實質內容（見 A-VC1 之重測表）。
3. 其餘 §三／§四 之 29 項數字**全部相符**（見上繳包 §3 之比對表）——
   145 / 66 / 79 / 28 / 38 / 117 / 形態外 0 / 四個欄位分布 / 61 / 66 /
   Verification Method 117 / 108 / 66-命中 / `SYS-HMI-RA` 0 / 未引用 42 及其清單。

即：兩份檔在**結構與需求母體上完全一致**，只在這九個分析欄上不一致。

**判讀（僅陳述，不裁）**

大小相同而內容不同，排除「不同 revision 之檔」之單純解釋
（不同 revision 幾乎不可能位元組數恰好相同）。二種可能：
(a) 下放包之量測對象為附件傳遞後之複本，其九欄於傳遞中失去值；
(b) §3.3 之量測方法在該九欄上判讀有誤（例如以 `data_only=False`
    讀到公式字串、或量測母體取錯列範圍）。
本輪無法從 repo 內分辨二者 —— 分析層之複本不在執行層可及範圍。

**提案處置（Tier 2）**

(a) 依全域拘束 3，**不以下放包之數字覆蓋實測值**：以 repo 內複本之
    實測結果為準，A-VC1 條文重裁（見該項 (a)）。
(b) 請分析層對其附件複本重跑同一量測並回報 SHA256，以分辨 (a)／(b)。
(c) 在裁定前，任何依賴「這九欄無內容」之判準（例如把 `Priority` 欄
    視為未填而改由本地推導）一律不得建立。

狀態：PENDING —— **阻斷 T4 之收斂**。本輪依「任一 ≠ 即停」停於此。

---

## A-VC6 —— `recon.py` 於 `spec_reference_template: null` 崩潰

**證據**

```
$ python scripts/recon.py --feature features/vehicle_category --root .
Traceback (most recent call last):
  File ".../scripts/recon.py", line 1183, in <module>
    main()
  File ".../scripts/recon.py", line 1131, in main
    outcome = emit(feature_dir, cfg, wbres, a03res, textlayer, hashes, asserts,
  File ".../scripts/recon.py", line 900, in emit
    tpl.replace("{outline}", sec), hit.get("title", "")]))
AttributeError: 'NoneType' object has no attribute 'replace'
```

`scripts/recon.py:894` 為 `tpl = cfg.get("spec_reference_template", "{outline}")`。
`dict.get` 之預設值僅在**鍵不存在**時生效；R-VC4 明文要求該鍵為
`null`（模式為查得，非構造），鍵存在而值為 `None`，故落入 `None.replace`。

**影響**：`RECON.md` 已完整寫出（`emit` 於 `recon.py:890` 崩潰前完成該檔），
但 `data/recon_leaf_to_section.tsv`（`:920`）、`data/recon.json`（`:923`）與
`write_decisions()`（`:1079`）**皆在崩潰點之後**，全部未執行。
故 T3 之三項交付件僅得其一，`DECISIONS.md` 仍為 scaffold 樣板。
（另註：即使不崩潰，`DECISIONS.md` 因 scaffold 已建檔，依 A-TM15 之守則
也會被改寫到 `DECISIONS.new.md` 而非原檔 —— 此為既有設計，非缺陷。）

**提案處置（Tier 2 —— 腳本修改，本輪不實作）**

(a) 最小修法：`cfg.get("spec_reference_template") or "{outline}"`。
    但這只是不崩潰 —— 其產出之 `spec_reference` 欄會是**光禿的章節號**，
    與 R-VC4 所裁之「逐字抄 037 `HMI Source ID` 欄原值」不同，
    等於在資料件中埋一個與裁決相左的值。**不建議單獨採用。**
(b) 建議修法：`spec_reference_template` 為 null 時，該欄改**逐字取
    037 `HMI Source ID` 欄之原值**（本 feature 之 66 個相異值已於 T4
    驗明對 SYS1 命中 66/66），使資料件與 R-VC4 一致。
(c) 於 (a)(b) 裁定前，**不得**為了讓 `recon.py` 跑完而把
    `spec_reference_template` 填成任何字串 —— 那會違反 R-VC4。

狀態：PENDING —— **阻斷 T3 之 `recon.json` 與 `recon_leaf_to_section.tsv`**。

---

## A-VC7 —— 規格 PDF 之位元組數與下放包 §3.1 不符

**證據**

下放包 §3.1 記規格 PDF 為 **3,552,260 B**。
全機掃描 `Vehicle Category HMI Logic and Flow R1 SR24 Post 2A
(December 27 2023).pdf` 之全部複本（7 份，含 `spec-index/sources/`、
`1_Customer_Requirement/` 之三個 PI 夾、`10_Reviewing/` 交付夾、
`01_Project_R1L/Spec/` 之兩處）：**全部為 2,828,253 B，SHA256 一律為
`3a6752c83bed1582485ad5e1aa7052ae63e6f0bb94304839beaf0e0b12776a76`**。
無任何一份為 3,552,260 B。

同批比對之另二份素材**大小完全相符**（037 = 100,475 B、
SYS1 = 47,458 B），故「附件傳遞會改變位元組數」不足以解釋本項 ——
若傳遞會改變大小，xlsx 亦應改變。

**提案處置（Tier 2）**

(a) 請分析層回報其附件 PDF 之 SHA256。若與上列不同，則 §四之章節內容
    判讀（尤其 §4.2(b) 之 18 節摘要、§4.4 之題材判讀）之來源即非本 PDF，
    須重新確認。
(b) 在此之前，**§4.2(b) 之 18 節「規格內容摘要」不得引為事實**；
    其章節號本身已由 T4 自 SYS1 outline 獨立驗明（42 節清單逐項相符），
    受影響的只有「該節寫了什麼」這一層。
(c) 本輪不更換 PDF —— 磁碟上不存在其他候選。

狀態：PENDING。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-VCnn]`.
