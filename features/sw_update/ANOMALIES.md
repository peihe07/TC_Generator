# ANOMALIES — FW036 SW Update HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-SUnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

| A | 內容 | 狀態 | Tier |
|---|---|---|---|
| A-SU1 | 下放包 01 §三 3.1 之素材身分判定與 repo 側原件不符（PDF 有完整文字層；三份 docx 皆真 OOXML）—— 使 R-SU6 全條與 R-SU4(a) 之揭露段前提失效 | **RESOLVED（下放包 02 §一；R-SU6 v2／R-SU4 v2）** | — |
| A-SU2 | 037 `Source Requirement ID` 欄非單一形態：3 格以 `/` 併記兩個 id、10 格為 `SYS-RA-VF747_V2/V6-{n}` 族 | **RESOLVED（形態面 R-SU5 v2；家族面 下放包 04 §1.1）** | — |
| A-SU3 | 規格 PDF p.46 之 `PU971`（3 位）於 `forms/Pop Up List HMI R1 (26PI).xlsx` 查無 | **RESOLVED（下放包 03 §2.3：原文筆誤，作 `PU0971`）** | — |
| A-SU4 | T20a 之需求物件全文抽取未以 Description 宣告為停界：14/487 物件吞併 43 個 Description，佔需求物件文字之 19.5% | PENDING | Tier 2（停界是否應含 Description；影響 T20b 之語料） |

---

## A-SU1 —— 素材身分判定與 repo 側原件不符 —— **RESOLVED**

**登記時點**：下放包 01 執行中，T0／T0b 完畢、T1 起跑前。
**觸發**：FO §0 逸出條款 —— 裁決所據之事實在執行層重測後不成立。
**處分（下放包 02 §一，2026-08-27）**：A-SU1 成立，成因採認。四項處分
（R-SU6 全條撤銷改 v2；R-SU4(a) 揭露段更正並增 (a2)；下放包 01 §三 3.1
之「已裁認事實」標記撤回；不發 DR）之全文見
`docs/handoff/02_asu1_rulings.md` §一 —— 依 R-G13 citation-by-reference，
不重抄。v2 條文已逐字入 `RULINGS.md`。

**執行層回報（量測條件差異，R-G8）**：本項 §一 所記「83,286 字元」為
逐頁 `get_text().strip()` 之字元和；`recon.py` 與 `intake.py` 以未 strip
之 `len(get_text())` 計得 **83,356**，差 70 字元為頁尾空白。另 intake.py
之文字層判準為「單頁 >100 字元」，故報 **63/68 頁**；本項所記 68/68
之判準為「單頁 >0 字元」。二者皆正確，差異純為門檻不同 ——
5 頁落在 1–100 區間（p.23=73、p.42=74、p.50=74、p.51=87、p.66=84）。
R-SU6 v2 引用之 83,286 不因此失效，惟後續一律引用台帳所記之實測值。

### 一、事實

六份素材皆在本機同一資料夾：
`~/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/SW Update via USB/`

素材身分已用 037／SYS1 之結構量交叉確認為下放包 §三 所述之同一批
（037：資料列 383、`Functional Requirement` 307、`Heading` 45、
`Information` 25、`Non Functional Requirement` 4、`Categorization` 空白 1、
`Out of scope` 1；SYS1 `Basic Report` 資料列 120 —— 與 §三 3.3、3.6 全數相符）。

**但格式判定相反**：

| # | 素材 | 下放包 §三 3.1 判定 | repo 側原件實測 | 大小 |
|---|---|---|---|---|
| 3 | CFTS_57 Reflash | UTF-8 純文字衍生本（非 OOXML） | **真 OOXML docx** | 133,530 B |
| 4 | SYSAD V03 | UTF-8 純文字衍生本 | **真 OOXML docx** | 3,764,644 B |
| 5 | VF747 | UTF-8 純文字衍生本 | **真 OOXML docx** | 865,472 B |
| 6 | HMI 規格「pdf」 | zip 容器，137 張 JPEG，**無文字層** | **真 PDF 1.6，68 頁，68/68 頁皆有文字層，共 83,286 字元** | 4,955,682 B |

成因：衍生本／圖檔身分為 **Claude Project 附件傳遞所致**，非素材本身之性質。
與 A-VC7（規格 PDF 位元組數與下放包 §3.1 不符）同源同型。

### 二、量測條件揭露（R-G8）

- `file -b`＋檔頭 magic（PDF 檔頭實見 `%PDF-1.6`）
- docx：`zipfile` 開 `word/document.xml`，正則去標籤取純文字
- PDF：PyMuPDF `page.get_text()`，逐頁計非空字元數（68/68 頁非空）
- 037／SYS1：openpyxl `read_only=True, data_only=True`，`AnalysisReport_FULL`
  列 8 起／`Basic Report` 列 2 起，col1 非空者計入
- 偽陽性風險：`file` 之判型依 magic，不排除容器正確而內容毀損；
  已用實際解出之正文長度覆核，風險低

### 三、受影響之裁決

**(a) R-SU6（HMI Logic and Flow 規格本文之可及性）—— 全條前提失效**

「非 PDF、實為 zip 容器、137 張 JPEG、無文字層、不可檢索」在 repo 原件上
全部不成立。連帶：
- (b)「須逐頁目視頁圖取得、每次取用記頁碼」失去必要性
- (c)「不因此違 R-G36」之免責前提消失 —— 本件**有**文字層可抽，
  R-G36（機器抽取優先）反而適用
- (a) SYS1 export 作參考索引、(d) 判讀不確定時保留模糊，兩項不受影響

附帶事實：文字層第 10 頁已見 `POP UP REQUIREMENTS` 表與 `PU0152`，
T5 之 `PU\d+` 掃描可直接在文字層執行。

**(b) R-SU4(a)（CFTS 家族錨點）—— 揭露段前提失效，結論不受動搖**

「repo 所存為 UTF-8 純文字衍生本，非權威二進位原件」不成立 ——
repo 側為真 OOXML。Q3 之裁定（ObjectID 可用作錨、不另發 DR）在原件上
只會更成立，但揭露文字須更正。

另一項須併同考量：CFTS_57 原件正文之 ObjectID 有兩種形態 ——
brace 形 `{7位}` 出現 **174 次／unique 87**（與 §三 3.5 完全相符，皆位於 TOC），
裸 7 位數則 **649 次／unique 633**。錨點池是否僅限 TOC 之 87 個，
關係到 Phase 2/3 錨定協定之範圍，一併待裁。

### 四、提案處置（Tier 1 提案，非裁定）

1. 重裁 R-SU6：改為「規格本文為真 PDF，有完整文字層，依 R-G36 一律機器抽取；
   頁碼記錄 `p.{n}` 是否保留為覆核義務，由 Pei 定」
2. 更正 R-SU4(a) 之素材身分揭露段；ObjectID 錨點池之範圍（87 vs 633）另裁
3. §三 3.1 之「已裁認事實」標記撤回，改以 T1 台帳之實測值為準
4. 本項不發 DR —— 素材已在本機，無外部索取需求（T7 之 0 筆不變）

---

---

## A-SU2 —— 037 `Source Requirement ID` 欄之三形態 —— **RESOLVED**

> **形態面結案（下放包 03 §2.1）**：以 **R-SU5 v2** 更正形態陳述，三形態逐項入條文。
> **家族面結案（下放包 04 §1.1，Pei 准）**：VF747 不立為第三錨點家族。
> 處分文見本節末。

**登記時點**：T4' 重測，下放包 01 §三 3.4 之 `373 / 364 / 9-dup` 三數字比對。

### 一、事實

該欄 383 列**全部非空**。以 `re.fullmatch(r"SYS-RA-FOTA-\d+")` 判形，
合形態 370 格、不合形態 **13 格**，分兩類：

| 類 | 格數 | 樣態 | 列 |
|---|---:|---|---|
| 一格兩 id（`/` 併記） | 3 | `SYS-RA-FOTA-336/SYS-RA-FOTA-334` | SWE1-FOTA-171、175、216 |
| VF747 族（**非 FOTA 族**） | 10 | `SYS-RA-VF747_V2-1348`、`SYS-RA-VF747_V6-175` | SWE1-FOTA-225～228、230、239～243 |

下放包 01 §三 3.4 之 `非空 373 / unique 364` **可完整重現** ——
其法為每格 `re.search` 取首個 `SYS-RA-FOTA-\d+`：370 + 3 = 373，
unique 361 + {336, 360, 506} = 364。9 個重複引用之名單亦完全相符。
即：數字本身無誤，但該量測法**靜默丟棄**了 `/` 併記格之第二個 id
（334、361、507）並**靜默排除**了 10 個 VF747 格。

### 二、受影響之裁決

R-SU5 首段稱「037 之 `Source Requirement ID` 欄形態為 `SYS-RA-FOTA-{n}`」
—— 對 13 格不成立。

更實質者為 R-SU5(a) 之理由：「本欄指向之 SYS-RA 母體**無對應規格檔可查**」。
該理由對 10 個 VF747 列**不成立** ——
`inputs/Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx` 即在場且可查，
且已列於 `feature.yaml` 之 `reference.vf747`。R-SU5(b)（本欄不進入任何
TC 欄位）之結論是否隨之調整，非執行層可定。

### 三、量測條件揭露（R-G8）

openpyxl `read_only=True, data_only=True`，`AnalysisReport_FULL` 列 8 起，
col1 非空者計入（383 列）；形態判定用 `re.fullmatch`（非 `re.search`），
差異即本項之成因。偽陽性風險：`/` 之外的其他分隔符未掃 ——
已用「383 − 370 − 10 = 3」閉合，無殘餘。

### 四、提案處置（Tier 1 提案，非裁定）

1. R-SU5 首段之形態陳述改為三形態並記其格數
2. R-SU5(a) 之理由對 VF747 族 10 列另裁：仍不取為 spec_reference，
   或改認 VF747 為第三錨點家族
3. 併記格之第二 id（334、361、507）是否入 037 內部追溯，一併裁

### 五、處分（下放包 04 §1.1，逐字）

```
A-SU2 處分（2026-08-27，Pei 准）：

形態面：R-SU5 v2 已結（上繳包 02 §二核對 OK）。

家族面：**VF747 不立為第三錨點家族**，R-SU5 v2 (a) 對 (iii) 之
「暫行維持」轉**確定維持**。依據：T11 三項獨立事實同向 ——
(a) 在手 VF747_V1_R3 無 Polarion 物件宣告、(b) 無任何 7 位
ObjectID、(c) 037 引用 V2／V6 與在手 V1_R3 為不同大版，
10/10 目標 id 於全文 0 命中（上繳包 02 §一 T11、§三）。

該 10 列（SWE1-FOTA-225, 226, 227, 228, 230, 239, 240, 241, 242,
243）之 spec_reference 於 Phase 2/3 錨定時走既有兩家族
（R-SU4 v2 (a)(b)）；屆時仍無錨可落者，個案依 IN §8.4.3 掛
PENDING 並發 DR。

休眠線索（記錄即止，不納素材、不開檔、不發 DR）：
`~/Work/02_Project_R1LR/9_ASPICE/SYS.1 Requirement Elicitation/
SYS1_VF_with source ID/HDCC27/VF747_V1_R3_PHDCC27.xlsx` 及
`SYS1_DT27_VF_Diff_HDCC27/VF747_V1_R3_PDT27_DiffHDCC27.xlsx`。
若上述個案 DR 發生，優先向此線索取 V2／V6 對應之 export，
屆時為新素材、新登記。
```

**處分之 1、2 已結**（R-SU5 v2 + 本處分）。**提案 3（併記格之第二 id
334／361／507 是否入 037 內部追溯）未見於處分文** —— 依 R-SU5 v2 (b)
「本欄僅作 037 內部追溯保留，不進入任何 TC 欄位」，該三 id 之歸屬
不影響任何 TC 產出；執行層以台帳所記之全集數（unique 366，含該三 id）
為準，不另請裁。若分析層另有意見，下輪逕令。

---

## A-SU3 —— 規格 PDF 之 `PU971` 於 Pop Up List 查無 —— **RESOLVED**

**登記時點**：T5' 兩源掃描。

**事實**：規格 PDF 文字層 unique PU 共 **52**，其中 51 個於
`forms/Pop Up List HMI R1 (26PI).xlsx`（三分頁，unique PU 1,341）**全部查得**；
`PU971` 為 3 位數形態（其餘皆 4 位），僅見於 **p.46**，查無。
同文件另有 `PU0971`（p.43、46、49），於清單內查得。

**處置**：依下放包 01 T5「查無不得代以語意相近者」，本項**不代以 `PU0971`**。
`feature.yaml` 之 `lint.popup_ids` 收 51 個已查得者，`PU971` 排除在外。

**量測條件揭露（R-G8）**：正則 `PU\d+` 逐頁掃 PyMuPDF `page.get_text()`；
清單側掃三分頁全儲存格。偽陽性風險：`PU971` 若為 PDF 文字層之抽取瑕疵
（漏字元），則實體不存在 —— 但 p.46 同頁另有正確之 `PU0971`，
兩者並存使「單純漏字」與「筆誤」不可由抽取結果本身區辨，故列 PENDING。

**提案處置**：目視 p.46 頁圖確認原文字面（R-SU6 v2(c)），再裁其為
`PU0971` 之筆誤或獨立 id。

### 處分（下放包 03 §2.3，逐字）

```
A-SU3 處分（2026-08-27，分析層裁）：`PU971`（p.46，全文件僅 1 見，
FOTAFU4 段）認定為 `PU0971` 之**原文筆誤**，非文字層抽取漏字。

證據：
(i)  分析層目視 p.46 頁面 render：原文自身印作 `PU971` ——
     同頁同段落三處（頁題「Forced Update Available 2 (PU0971)
     for EMEA」、FOTAFU4、FOTAFU4.1）以 `PU0971` 指同一彈窗
     「ROV Forced Update Available 2」，`PU971` 所指亦為同名彈窗
(ii) `PU971` 不在 Pop Up List 之 1,341 個 unique PU 內；
     3 位數形態逸出全清單之編號型態
(iii) 量測出處：附件頁圖 46.jpeg（分析層）；repo 側複證交 T14

處置：
- `lint.popup_ids` 維持 51（`PU0971` 已在內），不新增 id
- 任何 TC 欄位引用該彈窗一律作 `PU0971`
- 例外：test_item 上半之 verbatim 摘句若含該句，逐字保留 `PU971`
  （R-4 之 verbatim 紀律；IN §11 例外同型 —— lint 對引文段之
  保留 token 對來源驗證，不作 ban）
- 不改規格、不發 DR —— 觀察記錄即止
```

### 執行層複證（T14，2026-08-27）—— 證據鏈閉合

對 `inputs/` 之 PDF 原件（sha256 `faa58c3131df…`）第 46 頁：

- 文字層抽取（PyMuPDF `page.get_text()`）：該頁 PU 命中
  `PU0298`、`PU0410`、`PU0411`、`PU0971`、`PU971`
- `PU971` 僅 1 見，原句逐字：
  > `Available 2” (PU971) and “Scheduler” popup (PU0411), only`
  （上句為 `…‘Set Time’ button (PU0411). The same anti-theft behavior will
  apply for the “ROV Forced` —— 即所指為「ROV Forced Update Available 2」）
- 同頁 `PU0971` 3 見（L17、L27、L44），皆指同一彈窗，
  L44 為頁題 `Forced Update Available 2 (PU0971) for EMEA`
- **render 目視複證**：以 `page.get_pixmap(dpi=400)` 裁切該 token 所在矩形
  （`Rect(482.54, 188.93, 518.77, 199.97)`）放大檢視，
  版面上原字面確為 `(PU971)` 三位數 —— 同一裁切區內之
  `(PU0410)` 顯為四位數，二者字距一致。**排除文字層抽取漏字**。

處分之 (i)(ii) 於 repo 側完全複現，(iii) 之 repo 側複證即本節。

---

---

## A-SU4 —— 需求物件全文之抽取停界吞併 Description —— PENDING

**登記時點**：T21d 抽驗（下放包 08）。**由長度極值察覺，非由閉合檢查** ——
T20a 之 `487 = 487` 閉合的是 **id**，不是文字邊界（上繳包 06 §3.1 同型教訓）。

### 一、事實

`scripts/anchor_table.py` 之 `cfts_objects()` 取全文之停界為
「下一個**需求物件宣告段**或**標題段**」，**未含 Description 宣告段**。
故凡需求物件之後、下一需求物件之前存在 Description 物件者，
該 Description 之全文被併入需求物件之文字。

| 量 | 值 |
|---|---:|
| 受影響之需求物件 | **14 / 487（2.9%）** |
| 被吞併之 Description 物件 | **43** |
| 需求物件文字總量 | 103,743 字元 |
| 自首個內嵌宣告起之尾段 | **20,259 字元（19.5%）** |

前 5 例：

| ObjectID | 章 | 全長 | 吞併數 |
|---|---|---:|---:|
| `4907744` | 4.13.4.1 | **7,233** | **19** |
| `4907769` | 4.13.4.3 | 3,444 | 2 |
| `4907444` | 4.7.2 | 1,935 | 2 |
| `4907673` | 4.12 | 1,658 | 2 |
| `4907539` | 4.9.1 | 1,580 | 2 |

若改以「任一 `[Artifact Type:…]` 宣告」為停界：長度中位數 139（現 140）、
**最長由 7,233 降為 1,846**、空字元者 0。

### 二、為何這不是可逕改之 bug

**併入 Description 未必是錯的。** R-SU7 v2 定 Description 不入池，
但其內容被取用時**錨落所屬需求物件** —— 就文字比對之目的而言，
把從屬說明併入宿主需求之語料是可辯護的，甚至可能較佳。

**真正的缺陷是它不一致且未經宣告**：
- T12 實測 Description 歸需求者 **45** 個、歸章節者 92 個
- 現行抽取只吞併到 **43** 個（差 2，為邊界案例）
- 另 92 個歸章節之 Description 完全未進入任何需求物件之語料

即：**同一類內容，有的併有的不併，取決於它恰好排在哪裡**。

### 三、連帶影響（已產出物之污染範圍）

| 產出 | 是否受影響 |
|---|---|
| T20a 之 487 全文 | **是** —— 14 個物件之文字含非其自身之內容 |
| T20e 自我檢定之分數 | **是** —— (i)(ii)(iii) 各例之 TF-IDF 分數皆以此語料算出 |
| T21b 之前 5 候選 | **是** —— 已於材料中逐候選標記 |
| T21c 之首選與序位統計 | **是** |
| `ANCHOR_POOL.md` 之分類與計數 | **否** —— 該檔只用 id 與宣告，不用全文 |
| R-SU7 v2 之 574／487／137 | **否** —— 同上 |

### 四、提案處置（Tier 1 提案，非裁定）

1. 停界改以「任一 `[Artifact Type:…]` 宣告或標題段」為之，
   使需求物件之文字**只含其自身**；
2. 若裁定 Description 應併入宿主之語料，則須**一致地**併 ——
   依 `ANCHOR_POOL.md` §六 之對照表，將歸需求者（45）併入其宿主、
   歸章節者（92）另立章級語料，而非依排版順序決定；
3. 二者擇一定案後，T20e 自我檢定**須整套重跑**（語料變動即檢定失效）。

**執行層未逕改** —— T20b 明令「參數與演算法一次選定後不得中途更動」，
語料為演算法之輸入，中途換語料與換參數同性質。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-SUnn]`.
