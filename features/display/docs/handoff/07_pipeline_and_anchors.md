# 下放包 07 —— Q5 定案（B）、錨優先序修正、分隔符正規化裁定

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display ＋ 全域一條 ＋ **首次授權修改 `scripts/intake.py`**
- 對應上繳：`features/display/docs/upstream/07_pipeline_and_anchors.md`
- 前一包：`06_glossary_anchor.md`（上繳已覆核，見 §一）

---

## 一、上繳包 06 之覆核

**核可，無退回項。** 惟 §10 第 4 項之一個數字須更正，見 §1.3。

### 1.1 §2.1 之首字母判準 —— 這是本輪最好的一步

首版以「括號前最多 6 個詞」為展開，得 25 個縮寫且觸發六組假衝突
（`RVC` 同時得到 `Rear View Camera`、`there is no high priority screen`、
`Upon dismissing high priority screen`）。執行層察覺那是自己的貪婪匹配，
改以**候選詞之首字母須逐一拼出該縮寫**為判準 —— 這是對來源字元本身之
檢驗，不是相似度分數。修正後 13 個縮寫、85 處、全部 strict、零衝突。

`initials_rule` 欄逐條記 strict／filler-skipped，使讓步可稽核。**採認。**

執行層之自評採認：若照報，會以「六組衝突」觸發停止條件 16，
**把一個本不存在的問題送回分析層**。

### 1.2 §4 之拒絕 —— 正確，且我要為它補一條

`Rear View Camera`（空格）在 LID `Proxi & Configuration` 中 0 命中，
`Rear_View_Camera`（底線）2 命中。執行層援 R-DM22(c) 未自行加底線↔空格
正規化，開 A-DM19 回報。

**這正是 R-DM22(c) 要的效果。** 裁定見 §四 R-DM25 —— 開放，但以
「宣告式對稱正規化」之形式開放，不是把 (c) 廢掉。

### 1.3 §10 第 4 項之數字須更正：不是 340 個欄位字典

執行層記「`_polarion` 之其餘 340 個欄位字典完全未用」。
分析層實測（同檔、`read_only=True`、`data_only=True`）：

`_polarion` 之第一欄，**含 `:` 者才是欄位列舉字典**，其餘為工作項連結列
（`NR1L/NRL-52839` 等）：

| 類別 | 數 |
|---|---|
| 欄位列舉字典（鍵含 `:`） | **2** |
| 工作項連結列（鍵無 `:`） | 340 |

兩個字典為：

```
SYS2 分類 Category → 5 值
  Heading / Information / Functional Requirement /
  Non Functional Requirement / Out of scope
Type → 22 值（含一列分隔線 '-----'）
```

且 `Basic Report` 之 81 個欄名中，**能與字典鍵對上者只有 2 個**
（`SYS2 分類 Category`、`Type`）。逐項校驗結果：

| 欄 | 字典值數 | 實際用值數 | 違規列數 |
|---|---|---|---|
| `SYS2 分類 Category` | 5 | 6 | **117** |
| `Type` | 22 | 1 | 0 |

**故「其餘 340 個欄位字典未用」之待辦不存在** —— 可校驗之欄只有兩個，
兩個都已校驗完畢。上繳 06 §10 第 4 項應結案而非留待。

> 此更正不減損 §9 之價值。`Category` 之 117/333 違規、
> `Non Functional Requirement` 合法但 0 列（確認 R-DM7 母體未遺漏 NFR）
> 兩項發現皆成立且經分析層複驗。**只是它的涵蓋面比執行層以為的小，
> 而這對執行層有利** —— 少一個做不完的待辦。

### 1.4 §9 之措辭建議採認

向上游反映改為「值未依 `_polarion` 字典校驗」而非「大小寫不一致」。
後者聽起來像格式瑕疵，前者是資料校驗缺口。**採認**，A-DM4 依此改寫。

### 1.5 §6.1 之自註採認

> 逗號串接在本輪之六份中恰好都不會出錯……改掉不是因為它壞了，
> 是因為 R-G16(a) 要求分隔符不得為資料中可能出現之字元 ——
> **上一次它壞掉時，也是「恰好不會出錯」直到不是。**

---

## 二、Q5 定案 —— Pei 裁定 B

Pei 2026-08-25 裁定：**採 B**（不改 `SHEET_SIGNATURES`，改於
`feature.yaml` 允許人工指定 kind，由 `intake.py` 讀取覆寫）。

**這是本 feature 首次授權修改 `features/display/` 以外之程式碼**，
故拘束寫得比平常細。

### 2.1 覆寫機制之設計拘束

(a) **`SHEET_SIGNATURES` 一字不動。** 分頁簽章表不得增刪改。
(b) 覆寫為**逐檔指定**，形態如：

```yaml
intake:
  kind_overrides:
    "Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx":
      kind: a03_report
      reason: "R-DM5: no 'Analysis Report' sheet; sheets are SWE1 Requirements / SYS2 Traceability / Excluded NRLs (HW-only)"
      sha256: "…"
```

(c) **鍵為檔名，值須含 `sha256`**。覆寫僅在該檔之實際雜湊與所載相符時
    生效；不符則**不套用覆寫並警示**，不得靜默略過。
    理由：覆寫是繞過分類器，繞過的對象必須釘死在特定位元上。
(d) **無 `kind_overrides` 節時，行為與現行完全相同。** 缺省即惰性。
(e) 覆寫生效時，`intake.json` 與 `INTAKE.md` 須記其為 `kind_source:
    override`（相對於 `signature`），並帶 `reason` 全文。
    **分類結果之來源必須看得見。**

### 2.2 回歸驗證 —— 本項為授權之條件

改動前後，對 `_intake/` 下**現有全部目錄**
（`AMFM`／`Comfort`／`Display`／`Privacy`／`SXM`／`Time_Management`）
各跑一次 `intake.py`，逐檔比對其 `kind` 與 `note`。

**除 Display 之 037 一檔外，任一檔之分類結果改變即為失敗**：
還原改動，停並回報。

比對須為機器輸出之逐檔對照表，不得只報「無變化」。

### 2.3 `recon.py` 之處置

覆寫生效後重跑 `recon.py --feature features/display`。
**若仍失敗，回報其失敗訊息與失敗點，不修 `recon.py`** ——
本次授權僅及於 `intake.py` 之覆寫讀取，不及於其他共用腳本。

---

## 三、錨優先序 —— heading 應為最低，非第二

執行層 §3.2 報：`glossary_phrase` 在 `anchor_kind` 中永不出現，因為
80/80 列皆有 heading 祖先。並問優先序是否要改。

**要改，而且改的方向比「把 glossary 提前」更根本。**

heading 錨之鑑別力已由兩輪實測否定：

- 80/80 列皆有 heading 祖先 → 存在性為 100%，不構成區別
- r72 一個節點底下掛 48 個 FR（母體之 60%），而該 heading 講的是
  序列器觸控中斷接腳定義（上繳 03 §4.4）

一個 100% 命中且最大節點佔母體 60% 的錨，放在優先序第二位會遮蔽
其下所有錨。**heading 移至最低（`melco` 之後、`none` 之前）。**

新優先序：

```
signal → value → glossary_phrase → melco → heading → none
```

`candidate_from` 欄依 R-DM12 保留並繼續與 `anchor_kind` 並列輸出 ——
即使優先序修正後 `glossary_phrase` 會現身，**兩欄仍不得合併**：
`anchor_kind` 記最高優先者，`candidate_from` 記全部生效者。

---

## 四、裁決條文

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

```
R-G17（匯出檔之自帶字典須逐欄校驗 —— 全域）
Polarion 匯出之工作簿常帶一個列舉值字典分頁（本案為 `_polarion`）。
凡有此分頁者，須於 Phase 1 逐欄校驗主表之實際用值是否在字典內，
並將違規列數與違規值逐項登記。

校驗前須先分辨字典列與非字典列：本案 `_polarion` 之第一欄
**含 `:` 者才是欄位列舉字典**（2 個），其餘 340 列為工作項連結，
不是欄位字典。誤把後者計入會產生一個做不完的待辦。

向上游反映之措辭為「值未依匯出檔自帶之字典校驗」，
不得寫成「大小寫不一致」—— 後者聽起來像格式瑕疵，前者是資料
校驗缺口，二者之嚴重性與處置對象不同。

實例（本案）：`SYS2 分類 Category` 字典 5 值，主表用 6 值，
違規 117/333（35%），且違規之拼法（`Out of Scope`）是多數。
```

---

## 五、作業步驟

1. 抄錄 §四五條入指定檔（`R-G17` 入 `docs/fw036/RULINGS_LEDGER.md`；
   `R-DM24`–`R-DM27` 入 `features/display/RULINGS.md`），附核對表。
2. **依 R-DM24 實作 `intake.py` 之覆寫機制**，並完成 §2.2 之回歸比對。
   回歸比對之逐檔對照表為上繳必附。
3. `feature.yaml` 增 `intake.kind_overrides` 節（037 一檔）。
4. 重跑 `intake.py Display`，確認 037 之 `kind_source: override`。
5. 重跑 `recon.py --feature features/display`。
   **仍失敗則回報失敗點，不修 `recon.py`**（R-DM24 末段）。
   若跑通，其產出（RECON.md／DECISIONS.md／recon.json）與本 feature
   十四支自寫腳本之既有結論**逐項對照**，不符者逐項列出 ——
   **這是本 feature 首次獲得獨立管線之交叉檢查，對照表比跑通本身重要。**
6. 依 R-DM26 調整錨優先序，重出 `coverage_sys2_vs_swe_dm.tsv`。
   舊檔依 R-TM13 保留（加 `.PRE_PRIORITY` 後綴）。
   `anchor_kind` 與 `candidate_from` 兩欄並列。
7. 依 R-DM25 對 PROXI 側加底線↔空格正規化，重出
   `proxi_candidates.tsv` 之 `related_leaf`。
   嚴格與正規化兩種命中數並列，檔頭載明正規化定義。
8. 依 R-DM27 更新 `RULINGS.md` 之 R-DM8 註記與 `DATA_REQUESTS.md`
   之缺值範圍；八條逐條之缺值點列表入 `data/`。
9. 依 R-G17 與 §1.3 結清 `_polarion` 之校驗：**兩個字典皆已校驗完畢**，
   於 `ANOMALIES.md` 記明可校驗欄只有 2 個、340 列為工作項連結非字典，
   並將上繳 06 §10 第 4 項標為**已結案**。
10. `DISPLAY_ON` ↔ `DISP_ON` 之落差（上繳 06 §8 末段）開 `DR-DM8`：
    037 之 `DISPLAY_ON`／`DISPLAY_OFF` 與 SYS2／DBC 之 `DISP_ON`／
    `DISP_OFF` 是否為同一狀態。**不得自行認定**（無 `(...)` 並列，
    R-DM22 建不了條目；非分隔符差異，R-DM25 亦不適用）。
11. 更新 `docs/INDEX.md`。

---

## 六、停止條件

沿用既有各條，另加：

18. §2.2 之回歸比對中，Display 之 037 以外任一檔之 `kind` 或 `note`
    改變 → **還原 `intake.py` 之改動**，停並回報。
19. R-DM25 之正規化若使任一組原本不同之識別碼變為相等，而該兩者在
    來源中明顯為不同物 → 停並回報，不得逕行採用。
20. 步驟 5 之對照若發現 `recon.py` 之結論與自寫腳本**在任一項上不符**
    → 停並回報，**不得逕以任一方為準** —— 那正是這次交叉檢查的目的。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/07_pipeline_and_anchors.md`）

1. §四五條之抄錄核對表
2. `intake.py` 之改動 diff 全文
3. **§2.2 之回歸比對逐檔對照表**（六個 `_intake/` 目錄）
4. `feature.yaml` 之 `intake.kind_overrides` 節全文
5. `recon.py` 之執行結果；跑通者附**與自寫腳本之逐項對照表**，
   失敗者附失敗點
6. R-DM26 後之錨分布（`anchor_kind` 與 `candidate_from` 並列）
7. R-DM25 後之 PROXI `related_leaf`，嚴格與正規化兩數並列
8. 037 八條之缺值點逐條列表
9. `_polarion` 校驗之結清說明
10. `DR-DM8` 全文
11. **「本包是否仍有該驗而未驗者」之獨立判斷**
12. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-DM24 | Q5 定案 B；`intake.py` 覆寫機制之五項拘束 | Display＋腳本 | 是 |
| R-DM25 | 底線↔空格之宣告式對稱正規化；`glossary_phrase_norm` | Display | 是 |
| R-DM26 | 錨優先序修正，heading 降為倒數第二 | Display | 是 |
| R-DM27 | R-DM8 缺值範圍由四處改為八條全稱 | Display | 是 |
| R-G17 | 匯出檔自帶字典須逐欄校驗；先分辨字典列與工作項列 | 全域 | 是 |

五條皆為獨立單一事項。
