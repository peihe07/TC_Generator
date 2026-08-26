# ANOMALIES — FW036 Vehicle Category HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-VCnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

| A | 內容 | 狀態 | Tier |
|---|---|---|---|
| A-VC1 | 037 第 10–18 欄全為 `\xa0` | **撤銷（R-VC6）** | — |
| A-VC2 | 037 封面 `Reviewer：` 空、`Date：` 為 2020/09/05 | PENDING | 附於 DR-VC2（包 02 §四）|
| A-VC3 | §16.2 之 `SWE1-HMI-VC-066` 僅涵蓋標題一句 | PENDING | 併入 DR-VC3 |
| A-VC4 | `new_feature.py` 之 abbr 推導得 `VE`，非 R-VC1 之 `VC` | PENDING | 全域排程（包 02 §四）|
| A-VC5 | 下放包 01 §3.3 與 repo 037 複本不一致（A-VC1 之成因）| **RESOLVED（包 02 §一）** | — |
| A-VC6 | `recon.py` 於 `spec_reference_template: null` 崩潰 | **RESOLVED（R-VC8）** | — |
| A-VC7 | 規格 PDF 之位元組數與下放包 01 §3.1 不符 | **RESOLVED（R-VC7）** | — |
| A-VC8 | `recon.py` 缺 `leaf_count` assertion | PENDING | 全域排程（包 03 §五）|
| A-VC9 | 037 Priority 按章節整批賦值 | PENDING | 待 DR-VC7 |
| A-VC10 | 037 Title 之資訊量大於 Description | PENDING | 併 DR-VC7（同批 A）|
| A-VC11 | `recon.py` 之 DECISIONS 顯示層將 null 印為字面 `None` | PENDING | 全域排程（包 05 §一）|
| A-VC12 | §11.9 群與 §12.3 群之行為重疊 | PENDING | 條件性，待 DR-VC3 |
| A-VC13 | 送簽稿含自我描述之狀態元資料 | 本 feature 已處置；通則 PENDING | 全域排程（包 08 §一）|
| A-VC14 | 037 Title 與 Description 之數值矛盾（`VC-033-01`）| PENDING | 待 DR-VC8 |

---

## A-VC1 —— 037 第 10–18 欄之 `\xa0` —— **撤銷（R-VC6，Pei 2026-08-25）**

> **本項已撤銷，不得沿用或引述為判準。**
> 依 R-VC6（下放包 02 §二，`RULINGS.md:157`）：下放包 01 §3.3 所記
> 「第 10–18 欄全 145 列皆為 `\xa0`，無內容」為分析層**未經全表掃描之
> 全稱斷言**，作廢；據其所立之 A-VC1 一併撤銷。
> 九欄之正確定性為**有效上游輸入**，於 117 個 leaf 上皆有實質內容。
> 下列原文與重測記錄保留為軌跡，不再具效力。

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

**裁定（R-VC6，Pei 2026-08-25）—— 提案 (a)(b) 全採，(c) 已解**

(a) 採：A-VC1 撤銷，不得沿用或引述。
(b) 採：R-VC6(d) 逐字保留「strip 含 `\xa0` 之技術手段」，
    作廢的只是「不視為已填」之推論。
(c) 已解：A-VC5 之成因由下放包 02 §一裁明，標為 RESOLVED。

R-VC6 立四項拘束，其 (a)(b)(c) **不屬本異常之處置而屬 Phase 4 之範圍**：
欄 18 `Priority` 之 P0–P3 映射規則另裁，**在該裁定落地前 priority 欄
不得產出**；欄 11/13/15/17 之描述文字須納入 Phase 4 資料建置；
欄 14 `Risk Factor` 與欄 12 `Impact` 為 §10.2 映射之佐證，
不單獨作為 priority 之依據。三者已寫入 `RUNBOOK.md` Phase 4。

---

## A-VC2 —— 037 封面之 Reviewer 空白與日期矛盾（下放包 §七原文）

**內容**：037 封面 `Reviewer：` 為空；`Date：` 為 `2020/09/05`，
與修訂履歷（2025-12-26 ~ 2026-04-27）矛盾。

**提案處置**：判為表單樣板殘留。登記留痕；**不得引用該日期為版本依據**。
是否回報上游由 Pei 定。

**裁定（下放包 02 §四，Pei 2026-08-25）—— 不單獨發 DR**

裁：**不單獨發 DR**。於 DR-VC2 發出時（同為對 037 作者之查詢）
附帶一句提及即可。理由：封面欄位不阻斷任何 Phase，
單獨往返一輪之成本高於其資訊價值。維持 PENDING 至 DR-VC2 回覆。

狀態：PENDING（附於 DR-VC2）。本輪未對封面另作重測（不在 T4 之列舉範圍）。

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

**裁定（下放包 02 §四，Pei 2026-08-25）—— 不排入本 feature 之任何 Phase**

裁：A-VC4 與 A-TM04 **兩者維持 PENDING**。理由：A-VC4 已由 T0b 之事後
字串更正繞開，A-TM04 已由甲案傳參繞開 —— **繞開不是壓制**，二者皆無阻斷。
工具修法之時程屬全域議題，待 Pei 於 FW036 全域排程時一併處理，
本 feature 不代為決定。

**R-VC8 之修法不得順手併入 A-VC4 / A-TM04** —— 三者標的不同
（`recon.py` 之 template 處理 vs `new_feature.py` 之命名推導），
併案會使 R-VC8 之授權範圍失去邊界。已遵守：T13 之修法僅動 R-VC8 所指之處。

狀態：PENDING（全域排程）。T0b 之字串更正已完成，驗證 grep 命中數 0
（見上繳包 01 §1）。

---

## A-VC5 —— 下放包 01 §3.3 之量測對象與 repo 內複本不一致 —— **RESOLVED（包 02 §一）**

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

**裁定（下放包 02 §一，Pei 2026-08-25）—— 二可能皆非，成因為第三種**

本項曾列二種可能：(a) 附件傳遞失值；(b) §3.3 之量測方法判讀有誤。
分析層回報其附件雜湊，037 為
`cb80a77e8d57721ef0851c4ce263c46d3cbf5d028bd1a03c89c9d7debfd877ed`、
SYS1 為 `1fcc87116ac3893602f933ea10b2116895265ea0375ed88d0bf02ebcdeb091d6`
—— 與 repo 內複本**逐字相同**，(a) 由此排除。
分析層重跑量測，結果與本項之重測表**逐格相同**，(b) 亦不成立。

裁定之成因：**分析層之全稱斷言未經全表掃描。**
下放包 01 起草時之量測程式只取索引 `0, 1, 3, 5, 6, 7, 8` 七欄，
索引 `9`–`17`（即第 10–18 欄）**未被讀取過一次**；
§3.3 之「全 145 列皆為 `\xa0`」係自表頭附近之局部觀察推廣為全稱斷言，
再以實測值之形式寫入表格。

**不是量錯，是根本沒量。** 本項原提案 (b)「請分析層對其附件複本重跑並
回報 SHA256」已由分析層執行且已回報，請求結案。

提案 (a)（以 repo 內複本之實測為準）已由 R-VC6 全採；
提案 (c)（裁定前不得建立依賴「這九欄無內容」之判準）已被 R-VC6 反轉為
**正向要求**：該九欄是必須使用的上游輸入，見 R-VC6(a)(b)。

**此事之實質後果（分析層之判讀，逐字記錄）**

037 於 117 個 leaf 上提供完整之 Feasibility / Impact / Risk Factor /
Reusable / Priority 判斷，另有四欄逐條分析文字。下放包 01 不僅漏記，
且據該漏記立 A-VC1 指示「不視為已填」。若未經 T4 攔下，後果為 Phase 6 之
`priority` 欄失去上游依據而僅能本地推導 —— 即 IN §8.4.1 所禁之造值，
且影響全部 117 列。

狀態：**RESOLVED**。**T4 之停點解除** —— 30 項中原判 ≠ 之第 23 項，
其比對基準（下放包 01 §3.3）已作廢，實測值即為正解，無待調和之差異。
T12 已以 R-VC6 之條文為基準重跑，見上繳包 02 §3。

---

## A-VC6 —— `recon.py` 於 `spec_reference_template: null` 崩潰 —— **RESOLVED（R-VC8）**

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

**裁定（R-VC8，Pei 2026-08-25）—— 採提案 (b)，不採 (a)**

採 (b)：`spec_reference_template` 為 null 時，`recon_leaf_to_section.tsv`
之 `spec_reference` 欄改**逐字取 037 `HMI Source ID` 欄之原值**。
不採 (a)：其產出為光禿之章節號，與 R-VC4 所裁之全名不同 ——
「崩潰會停，錯值不會，後者為害更甚」（R-VC8 原文）。

R-VC8 為 Tier 2 修法之授權，另立三項實作拘束（保留 `first` 之原值而
不得以 `stem + "_" + sec` 還原；未宣告該鍵之 feature 行為不變；
修法後須對既有 feature 回歸確認逐字不變）。
修法與回歸證據見上繳包 02 §4（T13）。

狀態：**RESOLVED**。T3 之三件已於 T14 產出。

---

## A-VC7 —— 規格 PDF 之位元組數與下放包 01 §3.1 不符 —— **RESOLVED（R-VC7）**

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

**裁定（R-VC7，Pei 2026-08-25）—— repo 內複本為權威**

分析層回報其附件 PDF 為 3,552,260 B，SHA256
`216cfa84dfb84c0b3c44e24881407521412e16d16728aaa49e90ff3b3275a455`
—— 確為與 repo 內複本**不同之檔**。裁：附件之份為 Project 上傳時
**重新渲染之衍生物**，`repo` 內複本為權威，衍生物不得作為任何判準之來源。

連帶拘束（R-VC7 末段）：下放包 01 §4.2(b) 之 18 節「規格內容摘要」
係讀該衍生 PDF 所寫，其**章節號**已由 T4 驗明相符，
**摘要文字未經權威複本確認**。DR-VC3 發出前須以 repo `inputs/` 之 PDF
逐節重驗（T17）；重驗前該摘要不得引為 DR 之措辭依據，亦不得寫入表 B。

狀態：**RESOLVED**。T17 之逐節重驗結果見上繳包 02 §7。

---

## A-VC8 —— `recon.py` 缺 `leaf_count` assertion（新立，下放包 02 §三）

條文逐字：

```
A-VC8（recon.py 缺 leaf_count assertion）

`scripts/recon.py` 之 `run_assertions()` 僅實作
`functional_requirement_count`（以 Categorization 計，本 feature = 145）、
`distinct_spec_sections`、`spec_reference_stem` 三鍵。
R-VC3 所裁之驗證母體為 leaf 全集 117（子需求 ∪ 無子之父），
該值無對應之 assertion 鍵，於 feature.yaml 宣告亦不生效。

leaf 判準三者並存且分歧：145 / 117 / 79。
display 未暴露此分歧，因其 037 之三值恰皆為 8；
Vehicle Category 為首個使三者分離之 feature。

提案處置：`recon.py` 增設 `leaf_count` assertion，判準取 R-VC3 之定義
（子需求 ∪ 無子之父），與現行 `functional_requirement_count` 併列而非
取代 —— 二者為兩個不同的量，皆應可宣告。
屬 Tier 2 工具修法，**與 R-VC8 之修法非同一件，不得併案順手為之**。
在其落地前，117 之守護僅靠 T4 重測與上繳交叉檢查（R-VC9 之揭露義務）。

狀態：PENDING。
```

**執行層回報**：本項已由 T15 落實其揭露面 —— `feature.yaml` 之
`recon_assertions` 已刪去無實作之二鍵，並補記 leaf 判準三者並存
（145 / 117 / 79）之註解。**工具修法本身未實作**（R-VC9 明文：
不得併入 R-VC8 之授權範圍）。

**裁定（下放包 03 §五第 4 項，Pei 2026-08-25）—— 維持 PENDING，不排入本 feature**

處置同 A-VC4。理由：117 之守護目前由 T4／T12 之**集合相等**判定承擔
（非計數相等 —— 「數目對但成員錯」會被抓到），且每包負 R-VC9 之揭露義務。
此為人工守護，但**不是無守護**；在此前提下，工具修法之急迫性不足以
插隊全域排程。

**授權邊界再申明**：R-VC8 之修法不得順手併入 A-VC4（`new_feature.py`
之 abbr 推導）、A-TM04（slugify）、A-VC8（本項）。四者標的各異，
併案即失去授權邊界。已遵守 —— T13 之修法僅動 R-VC8 所指之二處。

狀態：PENDING（全域排程）。

---

## A-VC9 —— 037 Priority 按章節整批賦值（新立，下放包 03 §三）

條文逐字：

```
A-VC9（037 Priority 按章節整批賦值）

037 `Analysis Report` 欄 18 `Priority` 於 117 個 leaf 之分布，
按規格章節完全分群，每章內部無任何例外：

  章  4  Glove Box – Activation         High    4
  章  5  Glove Box – Activation Error   High    3
  章  6  Glove Box – Deactivation       High    3
  章  7  Glove Box – Deactivation Error High    2
  章 13  Settings Behavior/Ignition     High   16
  章  2  Vehicle Category Notes         Medium 24
  章  3  Controls                       Medium 17
  章 11  Settings Templates / Notes     Medium 20
  章 12  Settings                       Medium 25
  章 14  EPB Service Mode               Medium  2
  章 16  Cabrio Widget                  Low     1

即：Priority 之粒度為「章」，非「leaf」。

佐證其粒度不足之一例：章 14（EPB Service Mode，煞車服務模式，
含車輛在動時之禁入條件）與章 12（Settings，含字型與清單排列）
同為 Medium。二者於 IN §10.2 之 rubric 下語意相距甚遠。

另：欄 18 為 037 九個分析欄中**唯一無對應 Description-Action 欄**者
（欄 10/11、12/13、14/15、16/17 皆成對，欄 18 無配對），
故 037 未載其判準。

處置：不回報為缺陷 —— 按章賦值可能是上游之刻意作法。
以 DR-VC7 查詢其判準；在回覆前，依 R-VC11(b) 僅取其為邊界。

狀態：PENDING（待 DR-VC7）。
```

**執行層獨立重測（2026-08-25）—— 條文所載逐項相符**

量測：以 037 `HMI Source ID` 之章節號分群 117 個 leaf，取欄 18 之值集合。

| 章 | 名稱 | leaf | Priority 分布 | 章內單一值 |
|---|---|---|---|---|
| 2 | Vehicle Category Notes | 24 | `{'Medium': 24}` | 是 |
| 3 | Controls | 17 | `{'Medium': 17}` | 是 |
| 4 | Glove Box – Activation | 4 | `{'High': 4}` | 是 |
| 5 | Glove Box – Activation Error | 3 | `{'High': 3}` | 是 |
| 6 | Glove Box – Deactivation | 3 | `{'High': 3}` | 是 |
| 7 | Glove Box – Deactivation Error | 2 | `{'High': 2}` | 是 |
| 11 | Settings Templates / Notes | 20 | `{'Medium': 20}` | 是 |
| 12 | Settings | 25 | `{'Medium': 25}` | 是 |
| 13 | Settings Behavior and Ignition | 16 | `{'High': 16}` | 是 |
| 14 | EPB Service Mode | 2 | `{'Medium': 2}` | 是 |
| 16 | Cabrio Widget | 1 | `{'Low': 1}` | 是 |

合計 `{'Medium': 88, 'High': 28, 'Low': 1}` —— 與條文逐字相符。
**十一章全部章內單一值，零例外。**

欄位配對亦已實測：037 之 20 欄中，欄 10/11、12/13、14/15、16/17 皆成對，
**欄 18 `Priority` 為唯一無 Description-Action 配對者** —— 條文所載成立。

狀態：PENDING（待 DR-VC7）。依 R-VC11(b)，回覆前僅取其為邊界，
不作映射來源。T24 之草案已依此執行。

---

## A-VC10 —— 037 Requirement Title 之資訊量大於 Requirement Description（新立，下放包 04 §四）

條文逐字：

```
A-VC10（037 Requirement Title 之資訊量大於 Requirement Description）

037 於部分 leaf 上，`Requirement Title` 所載之條件多於
`Requirement Description`。實例：

  SWE1-HMI-VC-035-03
    Title : Selecting 'Cancel' on the restore-defaults prompt returns the
            user to the previous screen **without changing any settings**
    Desc  : Selecting cancel will take the user back to the previous screen.

  SWE1-HMI-VC-036-02
    Title : Selecting 'Cancel' on the clear-personal-data prompt returns the
            user to the previous screen **without clearing any data**
    Desc  : Selecting cancel will take the user back to the previous screen.

二例之 Title 皆含「不變更／不清除」之明文，Description 則僅述
「回上一頁」。該差額正是二筆判定 P0 之依據（R-VC14(a)）。

判讀：Description 疑為規格原文之逐字轉錄，Title 為 037 作者之
需求化改寫，改寫時補入了規格他處或圖中之條件。
**兩欄皆為 037 之正式欄位**，本 feature 之判定以二者之聯集為據，
不以任一單欄為唯一來源。

影響：TC 生成時，`test_item` 上半之 verbatim 取材須同時檢視二欄；
僅取 Description 會遺漏 Title 所載之條件，僅取 Title 則失去規格原句。

處置：不回報為缺陷（Title 補條件可能是上游之刻意作法）。
併入 DR-VC7 之同批查詢（同為 037 欄位語意之說明性問題）。

狀態：PENDING（併 DR-VC7，同批 A）。
```

**執行層獨立重測（2026-08-25）—— 條文所舉二例逐字相符**

| req_id | 欄 | 原值 |
|---|---|---|
| `SWE1-HMI-VC-035-03` | Title | `Selecting 'Cancel' on the restore-defaults prompt returns the user to the previous screen without changing any settings` |
| | Description | `Selecting cancel will take the user back to the previous screen.` |
| `SWE1-HMI-VC-036-02` | Title | `Selecting 'Cancel' on the clear-personal-data prompt returns the user to the previous screen without clearing any data` |
| | Description | `Selecting cancel will take the user back to the previous screen.` |

二例之 Description **逐字相同**（同一句），而 Title 各自載明
「without changing any settings」與「without clearing any data」——
差額成立，且正是該二筆定案 P0 之依據（R-VC14(a)）。

**執行層另行盤點全 117 leaf 之同型情形**，結果見上繳包 04 §6。

狀態：PENDING（併 DR-VC7，同批 A）。

---

## A-VC11 —— `recon.py` 之 DECISIONS 顯示層將 null 印為字面 `None`（新立，下放包 05 §一）

條文逐字：

```
A-VC11（recon.py 之 DECISIONS 顯示層將 null 印為字面 None）

`scripts/recon.py` 產生 `DECISIONS.new.md` 之 §4 Style bindings 時，
以 f-string 直接內插 `cfg.get("spec_reference_template")`，
該鍵之值為 `null` 時印出 Python 之 `None`，成為
`- spec_reference: [PROPOSED: None]`。

`None` 非裁定值 —— 它是「未宣告 template」之內部表示被洩漏到產出檔。
簽署者若照簽，簽到的是字面 `None`。

範圍：非本 feature 獨有。凡宣告 `spec_reference_template: null` 之
feature 皆會複現（`display` 之 feature.yaml 同此宣告）。

處置：本 feature 採**簽署時手動覆蓋**（下放包 05 §一），不修腳本。
根治須改顯示層，屬 Tier 2 工具修法，**與 R-VC8 之資料層修法非同一件，
不得併案**（同 A-VC8 之邊界）。與 A-VC4／A-VC8 併入全域排程。

狀態：PENDING（全域排程）。
```

**執行層回報**

1. **本 feature 之處置已依裁定執行**：採簽署時手動覆蓋，**未修 `recon.py`**。
   覆蓋文字見 `docs/upstream/05_partN.md` §3 之送簽稿 §4。
2. **跨 feature 範圍已獨立查證** —— 見上繳包 05 §5。條文所稱
   「`display` 之 feature.yaml 同此宣告」成立。
3. 根治屬 Tier 2 工具修法，**與 R-VC8 之資料層修法非同一件，不得併案**
   （同 A-VC8 之邊界）。與 A-VC4／A-VC8 併入全域排程。

狀態：PENDING（全域排程）。

---

## A-VC12 —— §11.9 群與 §12.3 群之行為重疊（條件性，新立，下放包 06 §二）

條文逐字：

```
A-VC12（11.9 群與 12.3 群之行為重疊，條件性）

規格 §11.9 群（11.9／11.9.1／11.9.2／11.9.3，「General logic for
setting with options」）與 §12.3 群（12.3／12.3.1，設定列之按壓與
旋鈕操作）於行為上有實質重疊：
  11.9.1「按未選中則移動選取；按已選中不作動」
    ↔ 12.3「按壓清單項以選取；列內調整選項可直接觸碰」
  11.9.3「按 +/- 增減；按 +/- 以外不作動；端值灰化」
    ↔ 12.3.1「旋鈕於 -/+ 列進入下壓態後左右轉 increment/decrement」

現況：11.9 群為 037 零涵蓋（R-VC3 表 B 之 17 節之一），
12.3 群已涵蓋（`VC-046-01`～`-05`、`VC-047-01`～`-04`，共 9 leaf）。
**故本重疊現在不生效** —— 只有 12.3 群會產 TC。

風險：若 DR-VC3 回覆為「應補」而 11.9 群進入範圍，兩群各自產 TC
將產生重複追溯，觸 IN §8.2.1。屆時須裁定其分工
（可能之形態：11.9 群為通則不單獨產 TC，或 12.3 群縮限為旋鈕路徑）。

處置：現在不作結構調整。未定之事不預作。
狀態：PENDING（條件性，待 DR-VC3）。
```

**執行層回報**

1. 條文所稱「12.3 群已涵蓋（`VC-046-01`～`-05`、`VC-047-01`～`-04`，
   共 9 leaf）」已重測 —— 見上繳包 06 §4，**9 leaf 相符**。
   母體標註（R-VC15）：9 為 **leaf 母體**之數。
2. 條文所稱「11.9 群為 037 零涵蓋」已重測 —— 11.9／11.9.1／11.9.2／
   11.9.3 四節皆在未引用之 42 section 內，且在表 B 之 17 節內。
   母體標註：42 與 17 皆為 **section 母體**之數。
3. **現在不作結構調整** —— 依條文，未定之事不預作。

狀態：PENDING（條件性，待 DR-VC3）。

---

## A-VC13 —— 送簽稿含自我描述之狀態元資料（新立，下放包 08 §一）

條文逐字：

```
A-VC13（送簽稿含自我描述之狀態元資料）

`docs/DECISIONS_signoff_draft.md` 之標頭載「送簽稿，尚未簽署，
尚未合併」—— 該句描述**該檔自身**之狀態。下放包 07 之 T41 要求
簽出後與送簽稿逐字一致，二者相衝：逐字複製則自我描述失真，
修正自我描述則逐字驗證失敗。

成因：分析層之指令設計未慮及「送簽稿含自身狀態元資料」之情形。
非執行偏差。

處置：本 feature 依下放包 08 §一(a)(b) 修正標頭與 Sign-off 區塊。

通則（建議納入全域）：**送簽稿不應含描述自身狀態之元資料**。
其狀態應由所在路徑（`docs/*_signoff_draft.md` vs 已簽之
`DECISIONS.md`）與外部記錄（下放包／上繳包）承載，不寫入內容。
若不得不寫，逐字驗證之範圍應明文排除該段。

狀態：本 feature 已處置；通則部分 PENDING（全域排程，
與 A-VC4／A-VC8／A-VC11 同批）。
```

**執行層回報**

本 feature 之處置已依下放包 08 §一(a)(b) 於 T46 完成：
標頭改為簽出說明（含送簽稿 SHA256 與授權出處）、
`Sign-off` 區塊改記「授權／寫入／驗證」三者，
原 `Reviewed by: ____` 空白欄刪除。
修改前後之 SHA256 與 diff 見上繳包 08 §1。

**修後與送簽稿不再逐字一致，此為預期**（下放包 08 §五 T46 明文）——
簽出時之逐字一致是**已發生的事實**，記於上繳包 07 §2.1，
其效力不因事後之事實更正而失效。

**本體（§1–§8）逐字未動** —— 已以 diff 驗證，含 §4 之
`spec_reference` 覆蓋段。本次只動元資料，未動任何裁定內容。

狀態：本 feature 已處置；通則 PENDING（全域排程，與 A-VC4／A-VC8／
A-VC11 同批）。

---

## A-VC14 —— 037 Title 與 Description 之數值矛盾（新立，下放包 09 §三）

條文逐字：

```
A-VC14（037 Title 與 Description 之數值矛盾）

`SWE1-HMI-VC-033-01`（§7.1，Glove Box 停用之錯誤鎖定）：

  Requirement Title       : After three sequential wrong PINs …
                            → 第 3 次觸發
  Requirement Description : more than three times in sequence …
                            → 第 4 次觸發

二欄之數值相差一次，為**可測門檻之分歧**，非措辭差異。

與 A-VC10 之區別：A-VC10 為「Title 多載 Description 未載之條件」，
其處置為取二欄之**聯集**；本案為「二欄之數值相互矛盾」，
聯集無法消解，故另立本條，不併入。

拘束：
(a) TC 作者**不得**自行取 3 或 4，不得以「取較嚴者」、「以 Title 為準」
    或任何一般性規則消解之。來源分歧時之職責為登記與查詢
    （DR-VC8），非選擇。
(b) 缺件期間該 TC 之門檻欄填
    `PENDING: DR-VC8 Glove Box lockout threshold`（IN §8.4.3）。
(c) 本條之範圍限於 `VC-033-01`。**未掃描其餘 116 個 leaf 是否存在
    同型矛盾** —— 本條不得被讀為「全表僅此一例」。
    全表掃描列為 T52。

狀態：PENDING（待 DR-VC8）。
```

**執行層回報 —— (c) 之全表掃描已完成（T52）**

條文 (c) 明文「未掃描其餘 116 個 leaf 是否存在同型矛盾，本條不得被讀為
『全表僅此一例』」。**T52 已掃描全部 117 leaf**，結果：

- 二欄至少一方含數值者 **38 leaf**（117 leaf 母體）
- 同類別而 (值, 比較器) 不一致之候選 **10 筆**
- 逐筆人工判讀後，**真陽性 1 筆 —— 即 `VC-033-01` 本身**；
  其餘 9 筆為假陽性（6 筆為 `VC2.2.4` 等章節標記滲入數字抽取、
  3 筆為同義措辭差異如 `exactly one` vs `only one`）

**故「全表僅此一例」現在可以說了 —— 但僅以 T52 之方法為限**，
其偽陰性見上繳包 10 §3.4。掃描腳本：`scripts/t52_numeric_conflict_scan.py`。

⚠ **掃描器初版漏抓本案自身**（類別切分錯誤，詳見上繳包 10 §3.2）。
修正後始命中。此事記於此，以免日後有人以「掃過了」為由信任該腳本
而不看其判準。

狀態：PENDING（待 DR-VC8）。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-VCnn]`.
