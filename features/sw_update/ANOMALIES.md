# ANOMALIES — FW036 SW Update HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-SUnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

| A | 內容 | 狀態 | Tier |
|---|---|---|---|
| A-SU1 | 下放包 01 §三 3.1 之素材身分判定與 repo 側原件不符（PDF 有完整文字層；三份 docx 皆真 OOXML）—— 使 R-SU6 全條與 R-SU4(a) 之揭露段前提失效 | **PENDING —— T1 起全部暫停待重裁**（Pei 2026-08-27 裁示） | Tier 2（重裁 R-SU6／R-SU4(a)） |

---

## A-SU1 —— 素材身分判定與 repo 側原件不符 —— PENDING

**登記時點**：下放包 01 執行中，T0／T0b 完畢、T1 起跑前。
**觸發**：FO §0 逸出條款 —— 裁決所據之事實在執行層重測後不成立。
**處置（Pei 2026-08-27 裁示）**：登記本項，**T1 起全部任務暫停**，
待 R-SU6／R-SU4(a) 重裁後再續。素材搬入 `inputs/` 改由 Pei 執行，
執行層只做 SHA256 台帳與驗證。

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

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-SUnn]`.
