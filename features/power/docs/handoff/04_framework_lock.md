# 04 — Power Management framework 定版

下放包 | 分析層 → 執行層 | 往返 NN = 04

前置：docs/upstream/03_framework_inputs.md 已覆核，判定 ACCEPT。
十一步全完成、十八閘無 MISMATCH，並推翻分析層之 R-P16 與 A-PW05。

分析層已補讀 03 上繳包 §五 / §六 / §七 全文，
並獨立重算 §五之算術閉合（套用兩筆移動於 64/24/16/7/3
得 62/24/16/8/3 ＋ 未歸類 1，逐格相符，兩側總數皆 114）。
03 包所提之 R-P29（分析層未讀即裁准）因此不再需要，未納入本包。

> **註記（R-P36，05 包加註）**：本節稱「03 包所提之 R-P29」有誤。03 上繳包之待裁項為 Q1–Q8，未提出任何編號 R-P29 之條文，亦未提出該議題。該敘述所指者為分析層自身之 04 草稿，該草稿從未落檔。見 04 上繳包 §一之登記。原文保留，依 R-P36 不改。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P24] 一個 leaf 得對應多個 Layer 3 章節。
        Layer 3 記錄該 leaf 觸及之全部相異章節，不擇一。
        Layer 2（Test Set）仍為單值，需擇一。
        理由：Layer 3 為文件內部之導航與涵蓋單位，不入工作簿（§4.1.5），
        無「一列一值」之約束；R-P15 將 Layer 2 之欄位限制
        誤套於 Layer 3，該前提本身未經驗證（03 §九第 1 項）。
        R-P15(b) 之「逐條裁定」範圍因此收窄為僅 Test Set 歸屬，
        Layer 3 之章節集合改為自動記全集。
        裁決者 Pei，逐字依據：「照建議吧」（回應 03 Q5）。
```

```
[R-P25] R-P16 撤回。
        撤回理由並非「§1.8.1 無 leaf」為單純誤測，而是
        **規則已廢止而其結論留存**：
        SWE-PM-057 觸及 §1.8.1.1.1，與 §1.6.2.1.17、§1.6.3.1.1
        三方同票（各 3 次）；「§1.8.1 零落點」僅在 02 包
        「同票取最深」之 tie-break 下成立（深度 5 勝 4），
        而該 tie-break 已由 R-P15 廢止。
        此與 R-P18 所訂正之 G6 錯誤同型：以一個層級或一條已失效之
        規則所得之結果，斷言另一層級之事實。
        §E Layer 3 之 §1.8.1 刪除線移除，改記 §1.8.1.1.1。
        裁決者 Pei，逐字依據：「照建議吧」（回應 03 Q2）。
```

```
[R-P26] 11 條跨章節 leaf 之處置：
        （a）Layer 3 —— 十一條全部依 R-P24 自動記全集，無需裁定。
        （b）Layer 2 Test Set —— 僅 SWE-PM-008 與 SWE-PM-057
             兩條之歸屬會改變分布。分析層已獨立重算確認算術閉合。
             此二條依 R-P15(b) 逐條由 Pei 裁定。
        （c）SWE-PM-057 之裁定素材已於 03 §七備齊，本包不重複產出。
             SWE-PM-008 之素材見 §B1。
        裁決者 Pei，逐字依據：「照建議吧」（回應 03 Q1）。
```

```
[R-P27] A-PW16 之 9 個未覆蓋章節：不併入既有 Test Set、
        不另立 Test Set、不宣告不涵蓋。
        先查清其是否為真實 coverage hole ——
        Stolen Vehicle Mode 與三個 Logistic 狀態為實質功能，
        「它們沒有 TC」比「它們該歸哪個 Test Set」重要。
        判定素材見 §B2。
        裁決者 Pei，逐字依據：「照建議吧」（回應 03 Q4）。
```

```
[R-P28] 量測章節層之反向缺口。
        R-P7 所裁「不追 SYS2 反向缺口」指需求層，
        章節層不在其射程內，且從未量測。
        CFTS009 196 章 + CFTS010 92 章 = 288 章，
        現被觸及者 46 章（16%）。須產出未被觸及之 242 章清單並分類。
        A-PW16 之 9 章為此問題之子集。
        裁決者 Pei，逐字依據：「照建議吧」（回應 03 Q6）。
```

```
[R-P29] A-PW05 訂正（分析層逐字指定）。
        原描述「SYS2 Traceability 用 SWE1-PM-TLM-001..033 / -ANT-」
        之 -ANT- 部分為假：該分頁 33 列中含 ANT 者 0 筆。
        SWE1-PM-ANT-008 僅出現於 SWE1 Requirements 分頁
        SWE-PM-089 之 Source Requirement ID 欄，即 A-PW01 所指者。
        分析層將 A-PW01 之證據誤植於 A-PW05。

        訂正後描述逐字如下：
        「037 內部 id 命名空間不一致：SWE1 Requirements 分頁用
         SWE-PM-001..115（115 筆連續）；SYS2 Traceability 分頁用
         SWE1-PM-TLM-001..033（33 列，前綴分布單一）。
         該分頁 SWE-PM- 出現 0 次，兩套互不對應。
         實測附註：SWE1-PM-ANT- 命名空間不在本分頁，
         其唯一出處為 SWE-PM-089 之 Source Requirement ID 欄（見 A-PW01）。」

        核心主張（兩套命名空間互不對應）維持成立，僅證據出處訂正。
        裁決者 Pei，逐字依據：「好 出」。
```

```
[R-P30] A-PW03 加註（分析層逐字指定）。
        原描述僅指出「涵蓋範圍不足」。實測顯示分類亦不實。
        加註逐字如下：
        「加註（03 §六複驗）：分頁名為 Excluded NRLs (HW-only)，
         但 26 列之 SW/HW/System 欄實測為 HW 18 / Information 4 /
         Out of Scope 2 / Heading 1 / 空白 1。
         故『(HW-only)』在分類上亦不實，不僅是涵蓋範圍不足；
         原描述只指出後者。」
        A-PW04 經逐字複驗成立（NRL-994xx 0 次、Sys-RA-PD 0 次、
        Sys-RA-PM- 76 次），不動。
        裁決者 Pei，逐字依據：「好 出」。
```

```
[R-P31] A-PW06（037 Sub Categorization 詞彙漂移）補驗。
        其宣稱「不可作分批判準」，而分批規劃即將用到（DECISIONS.md §7），
        卻自 01 包以來從未由執行層複驗。
        03 包之 R-P21 僅點名 A-PW03/04/05 三條，為分析層之疏漏。
        裁決者 Pei，逐字依據：「照建議吧」（回應 03 Q7）。
```

```
[R-P32] 04 包安排 SYS3 SYSAD §4.x 與 §E 之交叉比對。
        R-P20 之理由為「§4.x 為目前唯一可能提供獨立分組來源之文件」，
        03 包依 B3 禁區只取素材未做比對，故 R-P20 僅完成一半，
        §E「不是交集、只由單一來源支撐」之弱點原封不動。
        切入點：03 §七實測 SYS3 §4「動態行為 Dynamic Behavior」
        下有七個狀態子節，與 Power State 所轄之 TLM 狀態直接可比。
        本包完成比對後，該弱點方得結論（無論結論為支持或不支持）。
        裁決者 Pei，逐字依據：「照建議吧」（回應 03 Q8）。
```

（以上**九條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。）

## B. 本包須產出之三項素材

### B1. SWE-PM-008 之 Test Set 裁定素材（R-P26(c)）

**僅此一條**。SWE-PM-057 之素材已於 03 §七備齊，不重複產出。

輸出：
  Requirement Title（03 §四實測為空，如實回報）
  Requirement Description 全文，不截斷
  Verification Criteria 與 Verification Method 全文
  Source Requirement ID 完整 token 清單
  每個 token → (CFTS, 章節號, 章節標題)
  六個相異章節各自之標題與內文首段
    （§1.6.2.1、§1.6.2.1.9、§1.6.2.1.10、§1.6.2.1.11、
      §1.6.2.1.14、§1.6.7.1）
  歸屬後果：分別歸 Power State 與 Timeout Settings 時，
    五個 Test Set 之 leaf 分布

輸出至 features/power/data/b1_swepm008.md。
**不得附建議歸屬**（R-P15(b)）。

### B2. A-PW16 之 9 章判定素材（R-P27）

  9 章之章節號、標題、本文全文（不截斷）
  SWE-PM-003 與 SWE-PM-008 之 Requirement Description 全文
  逐章判讀：該章之行為是否已被其所屬 leaf 之 Description 涵蓋
    —— 僅陳述「涵蓋 / 未涵蓋 / 無法判定」與其逐字依據，
       **不建議處置**

輸出至 features/power/data/b2_uncovered_chapters.md。

### B3. SYS3 §4.x 與 §E 之交叉比對（R-P32）

  §4.x 之 36 項元件分解逐項列出（推導章節號 + 標題 + pStyle）
  「動態行為 Dynamic Behavior」之七個狀態子節逐項列出，
    並與 CFTS009 §1.6.2.1.1–.13 之 TLM 狀態逐一對照
    （名稱對得上者、SYS3 有而 CFTS 無者、CFTS 有而 SYS3 無者）
  以 SYS3 元件為獨立分組軸，對 114 leaf 重新聚類
  與 §E 現行五個 Test Set 比對：一致者、分歧者、SYS3 無對應者
  結論：SYS3 是否構成 §4.1.2 所要求之「第二來源」
    —— 若否，說明其失敗形態（粒度不符 / 無 leaf 對應 / 分類軸不同）

輸出至 features/power/data/b3_sys3_crosscheck.md。
**不得據此調整 §E** —— 比對結果為 05 包之裁定素材。

## C. 抽取規格異動

  §C rule 1 / 2 / 3 / 4 正則不變。
  Layer 3 建構依 R-P24 改為記全集。
  「主章節」概念僅保留於 Layer 2 之 Test Set 指派，
  且該指派限 SWE-PM-008 / SWE-PM-057 兩條待裁。

  分析層自裁補充（量測定義，非裁決條文）：
  （i）A-PW15 之 81 個章節錨點 token 於 Phase 4 產生
       specification_reference 時引用格式將不同，本包不處理，
       但須於 ANOMALIES 之 A-PW15 加註此下游影響。
  （ii）037 全 18 欄之空值率須量測（G19）——
       03 §九第 4 項指出 Requirement Title 有 7 條為空，
       而 §E「本分組之已知弱點」所稱之「20+ 種」正依賴該欄。

## D. 閃點

G0 為前置閘，不通過則其後一律不執行、不回報。
G0–G16 沿用 03 包，期望值不變（G8 = 904/196、G6b 列層 = 336/337、
G6a = 337/338、G13 = 11、G14 = 被丟棄 10 / 未覆蓋 9、G16 = 0 等）。
本包新增四項：

| # | 項目 | 期望值 |
|---|---|---|
| G13b | Layer 3 全集化後所記之相異章節總數 | **46** |
| G17 | 章節層反向缺口（R-P28） | 【實測填入】288 章中未被任何 leaf 觸及者之數量與清單，並分類 |
| G18 | A-PW06 複驗（R-P31） | 【實測填入】037 Sub Categorization 之實際值域與計數；與 01 包所稱之 5 值 115 筆比對 |
| G19 | 037 全 18 欄空值率 | 【實測填入】逐欄非空計數；特別回報 Requirement Title 之空值數 |
| G20 | SYS3 交叉比對結論（R-P32） | 【實測填入】SYS3 是否構成第二來源，及其失敗形態（若否） |

G11 已依 R-P14(b) 移除、G6 已依 R-P18 拆分，編號皆不遞補。

## E. framework

**本包仍不定版。** §E 標題維持「待定版」。
依 R-P25 移除 §1.8.1 之刪除線，改記 §1.8.1.1.1。
依 R-P24 於 data/layer3_full.tsv 建立 Layer 3 全集
（結構由執行層自裁，須可重現）。

**leaf 分布數字仍不得重算或改寫。**
待 SWE-PM-008 與 SWE-PM-057 兩條裁定後於 05 包定版。

分析層已算出之三種情形（供 05 包對照，非本包任務）：
  兩條皆歸 Power State           → 64 / 24 / 16 / 7 / 3
  008→Timeout、057→Power State   → 63 / 24 / 16 / 8 / 3
  008→Power State、057→Timeout   → 63 / 24 / 16 / 8 / 3
  兩條皆歸 Timeout Settings      → 62 / 24 / 16 / 9 / 3

## F. Anomaly 異動

  A-PW03 → 依 R-P30 加註
  A-PW04 → 複驗成立，不動
  A-PW05 → 依 R-P29 以指定文字整條替換
  A-PW06 → 依 R-P31 複驗後更新，若原描述有誤即訂正
  A-PW14（R-P16 前提有問題）→ 依 R-P25 標記為已處置
  A-PW15 → 依 §C(i) 加註下游影響
  A-PW16 → 維持 live，待 B2 素材齊備後裁定
  新增 A-PW17：R-P15 建立於「一 leaf 對一章節」之未驗前提上（R-P24）
  新增 A-PW18：分析層將 A-PW01 之證據誤植於 A-PW05（R-P29）

## G. DATA_REQUESTS

  DR-PW1（SWE-PM-089 來源）→ live，High
  DR-PW3（4942087 歸屬）→ live，Medium
  DR-PW2、DR-PW4 → 維持撤回
  無新增

## H. 作業指示

  1. G0 前置閘
  2. 依 R-P24 建 data/layer3_full.tsv，驗 G13b（相異章節 46）
  3. 依 R-P25 訂正 §E 之 §1.8.1 → §1.8.1.1.1
  4. 產出 B1（SWE-PM-008 素材）
  5. 產出 B2（9 章判定素材）
  6. 產出 B3（SYS3 交叉比對），驗 G20
  7. 依 R-P28 量測章節層反向缺口，驗 G17
  8. 依 R-P31 複驗 A-PW06，驗 G18
  9. 依 §C(ii) 量測 037 全欄空值率，驗 G19
 10. 依 R-P29 / R-P30 落實 A-PW05 替換與 A-PW03 加註，
     於上繳包全文引用訂正前後文字
 11. 依 §C(i) 為 A-PW15 加註下游影響
 12. 以 §D 全表自驗
 13. §A 九條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
 14. 上繳 features/power/docs/upstream/04_framework_lock.md，更新 docs/INDEX.md

## I. 禁區

  不得寫回 FW036 workbook
  不得執行任何 git 操作（全數屬 Pei）
  不得以 openpyxl save 寫任何 xlsx（R16 凍結）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得為 SWE-PM-008 之 Test Set 歸屬附建議（R-P15(b)、B1）
  不得為 A-PW16 之 9 章建議處置（R-P27、B2）
  不得據 SYS3 交叉比對結果調整 §E（B3）
  不得重算或改寫 §E 之 leaf 分布數字
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P24 leaf 得對應多個 Layer 3 章節，Layer 3 記全集、Layer 2 擇一
  R-P25 R-P16 撤回 —— 規則已廢止而結論留存
  R-P26 11 條跨章節 leaf：Layer 3 自動、Layer 2 僅兩條待裁
  R-P27 A-PW16 之 9 章不併不立不棄，先查是否為真 coverage hole
  R-P28 量測章節層反向缺口（288 章 vs 46 章）
  R-P29 A-PW05 訂正（逐字指定）
  R-P30 A-PW03 加註（逐字指定）
  R-P31 A-PW06 補驗
  R-P32 04 包安排 SYS3 §4.x 與 §E 交叉比對

  逐條確認：**九條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 9、§J 列數 = 9、§H 步驟 13 寫「九條」，三處一致。
