# 下放包 08 —— Q5-B 之誤診歸屬、選項 D 之提交、正規化回施

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display ＋ 全域一條
- 對應上繳：`features/display/docs/upstream/08_recon_and_norm.md`
- 前一包：`07_pipeline_and_anchors.md`（上繳已覆核，見 §一）

---

## 一、上繳包 07 之覆核

**核可，無退回項。** §0 之判斷正確且重要，見 §二。

### 1.1 回歸語料之重建 —— 這是本輪最該記下來的一步

執行層依 §2.2 對六個 `_intake/` 目錄跑回歸時發現：**四個目錄是空的**
（AMFM／Comfort／Privacy／Time_Management 各 0 個可分類檔），
歷次 `--scaffold` 已把素材 `shutil.move` 進各 feature 之 `inputs/`。

它沒有照跑然後報「六個目錄全部無變化」—— 那會是一句真話配一個假結論。
它改為還原 Display 素材、另建 8 個 `_regr_*` hard-link 語料，把回歸母體
擴到 **14 個目錄、82 個檔、7 種 kind**，才得出 14/14 逐字相同。

**若照原樣跑，「無變化」證明不了任何事。** 這是「空集合上的檢查一律
PASS」之實例，與 canon §5a「不可能失敗之檢查項標未實測而非 PASS」同型。

`_intake/` 四個目錄為空另有後果，已升為全域條文（§四 R-G18）。

### 1.2 §5.2 之處置正確

R-DM24 之範例寫 `kind: a03_report`，而 `intake.py` 之 kind 詞彙是
`swra_report`（`KIND_TO_YAML` 將後者映至前者）。執行層實測兩種設定：
條文所載者不驅動下游、詞彙正確者當場崩潰於 `intake.py:311`。

**保留條文所載之值、不自行改寫、以 A-DM21 登記** —— 正確。
改了也只是把「不驅動」換成「崩潰」，而條文之字面不由執行層修改。

### 1.3 §6.1 推翻了我的診斷

R-DM26 之依據是「heading 100% 命中會遮蔽其下所有錨」。調整後
`anchor_kind` 分布**一字未變**（`signal 43 / heading 37`）——
因為 16 個產生候選之列**全部同時含 `$signal$`**，而 signal 在新舊序中
皆居首。遮蔽者是 signal，不是 heading。

**我的診斷錯了。** R-DM26 仍應保留（heading 之 100% 存在性確實不宜居
高位，這一點獨立成立），但它解決不了執行層原本提出的問題。

執行層之結論採認並升為條文（§四 R-DM28）：

> 兩欄回答的是不同的問題：`anchor_kind` 答「這列帶有哪些證據」，
> `candidate_from` 答「是什麼把它連到 leaf」。

### 1.4 首個 leaf ↔ PROXI 連結

`RVC_SK_PRSNT` → PROXI `Format` r401／r494，值域
`0 = Absent 1 = Present`，`anchor_kind = glossary_phrase_norm`。
停止條件 19 之三組母體（1,052／429／2,548 個相異名）碰撞檢查皆 0。

`glossary_phrase` 嚴格 0 / 正規化後 1 之並列報告符合 R-DM25(b)。

---

## 二、Q5-B 是誤診，誤診歸屬於我

執行層 §0 之陳述成立：**Q5-B 沒有達到它宣稱的目的，且機制本身完好。**

### 2.1 誤診之鏈條

我在下放包 01 立 R-DM5 時，把「`intake.py` 之 sniffer 認不出這份 037」
判為 `recon.py` 跑不動之原因。此後五輪都掛在這個前提上，直到 Q5 提交
裁定時，我給 Pei 的三個選項（A／B／C）**全部建立在該前提上**。

實測（執行層 §5.1，分析層已讀 `scripts/recon.py` 全文複驗）：

```
recon.py:main()
  → paths[key] = resolve_glob(feature_dir, cfg["paths"][key])
  → a03res = survey_a03(paths["a03_report"])
  → survey_a03(): ws = wb["Analysis Report"]      ← 崩在這裡
```

`recon.py` 讀的是 `feature.yaml` 之 `paths.a03_report`
（本 feature 於 02 輪即已人工填妥），**它從來就不經過 `intake.py` 之
分類結果**。`intake.py` 之 kind 只在 `--scaffold` 預填 `feature.yaml`
之 paths 時起作用，而那一步早已由人工完成。

**故 Q5-B 對 `recon.py` 是純裝飾。** A、B、C 三個選項沒有一個會讓
`recon.py` 跑起來 —— 我出的是一份三選一皆錯的選單。

### 2.2 Q5-B 之機制仍應保留

雖不解本問題，`kind_overrides` 本身是可用之機制：五項拘束落實完整、
`SHEET_SIGNATURES` 逐字未動、82 個檔之回歸逐字相同。
**保留，不撤回。** 其正確用途是使 `INTAKE.md` 之分類結果誠實
（037 標 `a03_report` 而非 `spec_xlsx`），這本身有價值，只是與
`recon.py` 無關。

### 2.3 真正的阻塞點與選項 D

分析層讀畢 `scripts/recon.py` 全文（1,100+ 行），逐項檢 Display 之
037 會不會通過 `survey_a03()` 之其餘部分：

| `survey_a03()` 之步驟 | Display 之 037 | 判定 |
|---|---|---|
| `wb["Analysis Report"]` | 分頁名為 `SWE1 Requirements` | **崩潰** |
| 表頭列 = 含 `requirement description` 之列 | r7 有 `Requirement Description` | 通過 |
| `find("categorization", forbid=("sub",))` | 有 `Categorization` 與 `Sub Categorization`，唯一命中 | 通過 |
| `is_leaf = cat.lower().startswith("functional")` | 8/8 為 `Functional Requirement` | 通過，得 8 leaves |
| `src_i = find("hmi source")` → `find("source", forbid=("description","requirement id"))` | `Source Requirement ID` 含 `requirement id` → 被排除 → `src_i = None` | 通過（sections 為空，不崩） |
| `build_outline_map(paths.sys1_export)` | Display 無 `sys1_export` → 回 `({}, reason)` | 通過 |
| `run_assertions` | `recon_assertions` 未宣告 → 空清單 | 通過 |

**除分頁名一處外，其餘全部通過。** 即：**一處參數化即可跑通。**

**選項 D**（提交 Pei，見 §三）：於 `feature.yaml` 增
`paths_meta.a03_sheet`，`survey_a03()` 由

```python
ws = wb["Analysis Report"]
```

改為

```python
ws = wb[sheet_name]        # sheet_name 預設 "Analysis Report"
```

**預設值不變，未宣告者行為完全相同。** 形態與 Q5-B 之覆寫同型，
且這一次確實落在阻塞點上。

`intake.py:114`／`:311` 與 `compare_req_families.py:41` 之三處寫死
**本輪不動** —— 前二者只在 kind 為 `swra_report` 時觸及（本 feature 用
`a03_report`，不觸及），後者之呼叫者未查（上繳 07 §11 第 4 項）。
**分開處理，不打包。**

---

## 三、提交 Pei —— 選項 D

| | 內容 |
|---|---|
| **改動** | `scripts/recon.py` 之 `survey_a03()` 一處：分頁名由字面改為參數，預設 `"Analysis Report"` |
| **設定** | `feature.yaml` 增 `paths_meta.a03_sheet: "SWE1 Requirements"`（僅 Display 宣告） |
| **不動** | `intake.py` 之三處、`compare_req_families.py` 之一處、`SHEET_SIGNATURES`、`recon.py` 之其他任何部分 |
| **回歸** | 對現有全部 feature 跑 `recon.py`，逐 feature 比對 `RECON.md`／`recon.json`。任一 feature 之輸出改變即還原並停手 |
| **取得** | 本 feature 五輪來第一次獨立管線交叉檢查：`recon.py` 之 leaf 數／`workbook_state`／欄位解析，對照十四支自寫腳本之結論 |
| **代價** | 又一次修改共用腳本。惟改動面小於 Q5-B（Q5-B 加了兩個函式與一段分支；本項為一個參數） |

**若 Pei 不授權**，本 feature 之替代路徑為：接受無獨立管線交叉檢查，
於 `DECISIONS.md` 明記此事並將其列為交付時之已知限制。
分析層不建議此路徑 —— 六輪來四次同型自我更正，全靠事後自查。

---

## 四、裁決條文

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

```
R-G18（`--scaffold` 之搬移使 intake 不可重現 —— 全域）
`intake.py --scaffold` 以 `shutil.move` 將素材自 `_intake/<Feature>/`
搬入 `features/<f>/inputs/`。搬移後該 `_intake/` 目錄為空，
**該 feature 之 intake 分類結果不再可重現**。

實測（上繳 07 §3.1）：`_intake/` 六個目錄中四個
（AMFM／Comfort／Privacy／Time_Management）之可分類檔為 **0**。

三項拘束：
(a) 凡於空目錄上執行之檢查，其 PASS 一律不成立，須標「未實測」
    （canon §5a：不可能失敗之檢查項不標 PASS）
(b) 需要回歸驗證分類器時，須先自各 feature 之 `inputs/` 重建語料
    （hard link 即可，不複製位元），並於報告中載明語料為重建者
(c) 重建之臨時目錄用後刪除；`_intake/` 全域被 `.gitignore` 排除，
    不入 git

本條不要求改變 `--scaffold` 之行為 —— 搬移而非複製有其理由
（避免兩份來源）。本條要求的是**知道它的後果**。
```

---

## 五、作業步驟

> 步驟 1–2 不待 Pei 裁示即可執行；步驟 3 待裁。

1. 抄錄 §四三條入指定檔（`R-G18` 入 `docs/fw036/RULINGS_LEDGER.md`；
   `R-DM28`／`R-DM29` 入 `features/display/RULINGS.md`），附核對表。

2. **R-DM24(b) 之警示分支測試**（上繳 07 §11 第 3 項自陳未測）：
   以一份雜湊蓄意不符之暫時副本觸發該分支，證明
   (i) 警示訊息印出、(ii) signature 結果保留、(iii) 不崩潰。
   測試用檔用後刪除，測試輸出附於上繳包。
   **未經執行驗證之錯誤路徑等同未實作。**

3. **選項 D**（待 Pei 裁示；裁示為「授權」時才做）：
   依 §三之四項欄位實作、宣告、回歸、對照。
   回歸須涵蓋現有全部 feature，逐 feature 比對 `RECON.md` 與
   `recon.json`；任一 feature 輸出改變即還原並停手。
   跑通後之**對照表為本步驟之主要產物**：`recon.py` 所報之
   leaf 數／`workbook_state`／欄位解析／design-method 詞彙，
   對照十四支自寫腳本之既有結論，逐項列「相符／不符」。
   **不符者一律停並回報，不得逕以任一方為準**（停止條件 20）。

4. **R-DM25 之正規化回施於 SYS2 側**（上繳 07 §11 第 6 項自陳未測）：
   對覆蓋對照施用 `[ _]+ → " "`，嚴格與正規化兩數並列。
   執行層之推測「SYS2 之 `Description` 是散文，底線少見」須以實測
   取代，不得以推測結案。

5. **PROXI 之 269 列排程**（連續三輪未排）：
   本輪不追查其內容，但須**產出一份排程判準之提案** ——
   以何種順序、以何為停止點、DR-DM7 到齊與否如何改變作法。
   提案不裁定，供 Phase 2 選用。

6. **`compare_req_families.py` 之呼叫者清查**（上繳 07 §11 第 4 項）：
   查誰呼叫它、本 feature 是否會用到。**只查不改。**

7. 更新 `docs/INDEX.md`。

---

## 六、停止條件

沿用既有各條（1–20），另加：

21. 步驟 3 之回歸中，任一既有 feature 之 `RECON.md` 或 `recon.json`
    改變 → 還原 `recon.py` 之改動，停並回報。
22. 步驟 2 之警示分支若**未如預期印出警示**，或崩潰，或靜默套用覆寫
    → 停並回報。R-DM24(b) 之落實即為不成立。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/08_recon_and_norm.md`）

1. §四三條之抄錄核對表
2. R-DM24(b) 警示分支之測試輸出（三項各自之證據）
3. 選項 D 之實作 diff、回歸逐 feature 對照、**與自寫腳本之逐項對照表**
   （或「未獲授權，未執行」之聲明）
4. SYS2 側正規化之嚴格／正規化兩數並列
5. PROXI 269 列之排程判準提案
6. `compare_req_families.py` 之呼叫者清查結果
7. **「本包是否仍有該驗而未驗者」之獨立判斷**
8. 建議之 commit 訊息與 pathspec（不執行）

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-DM28 | `anchor_kind` 與 `candidate_from` 不可互替；引用以後者為準 | Display | 是 |
| R-DM29 | `kind: a03_report` 之惰性已知，維持不改 | Display | 是 |
| R-G18 | `--scaffold` 搬移使 intake 不可重現；空目錄上之 PASS 不成立 | 全域 | 是 |

三條皆為獨立單一事項。
