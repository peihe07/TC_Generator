# 下放包 05 —— 母體判準之修正、Q3 完整語料與 Phase 3 前置

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/05_corpus_fix_and_framework_prep.md`
- 前一包：[04_corpus_and_assertions.md](04_corpus_and_assertions.md)
  （上繳 [../upstream/04_corpus_and_assertions.md](../upstream/04_corpus_and_assertions.md)，已覆核）

---

## 一、04 包之覆核結果

**通過。** 十一節齊備，三項故意失敗全部攔下且範圍向亦通過，
`RULINGS.md` 五條 SHA256 全同，R-PMH10 原文 `885070968235b262` 未變。

三項由分析層獨立複驗，**全部相符**：

1. **`Privacy` 與 `SXM` 之 `D5` 非空**，逐字與上繳所報相同
   （`SWE1_CFTS_022-Privacy_Features`／
   `SWE1_SXM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260406`）。
2. **§5.4 之 A-PMH10 更正成立** —— 以 `zipfile` 直讀客戶那份之
   `xl/worksheets/sheet6.xml`：其 x14 之 `<xm:f>` 逐字為
   `Reference!$C$4:$C$12`，實測該範圍第 6 項為
   `組合測試 (Combinatorial Testing ; Pair-wise / N-wise)`；
   而其 `下拉選單!A1:A9` 之第 6 項為 `Pairwise / t-wise` 且**無任何 DV 指向它**。
   **孤兒分頁之判定屬實。**
3. 母本之全簿 5 組 DV 與客戶那份之四組破碎 sqref，皆與上繳相符。

**§5.4 為本輪最有價值之一項**：它更正的是 03 包一個「兩邊值相同 ⇒ 同一件事」
之推論，而該推論本身是我在覆核 03 時放行的。與 03 §3（priority 假衝突）、
02 §3.3（列號位移）合為同一形狀之第三例 —— **比對前先確認兩邊指的是不是
同一個東西**。此形狀已由 R-PMH12、R-PMH20 兩條分別覆蓋，本包不再立新條。

---

## 二、R-PMH19 之 (a) 寫錯了 —— 分析層之判準缺陷

上繳 §8 第 1 項指出：(a) 之「交付夾根層」規則排除了 **Home、AppDrawer、
Notifications HMI、Vehicle Settings(CFTS044)、VF230** 五個 feature 之交付件 ——
它們並非中間態，只是交付夾多了一層（`Core HMI/HomeHMI/`、
`Vehicle Settings/CFTS044/`）。

**執行層照條文執行、未自行放寬、並將其列為五項中最該優先處理者 —— 處置正確。**

**這是我的判準缺陷，不是執行層之執行缺陷。** 我寫 (a) 時的意圖是排除
`REF/`／`output/`／`validation/` 這類**用途目錄**，卻用「深度」去表達它，
而深度與用途無關。

**這是我在同一件事上連續第二次出錯**：R-PMH10 是**樣本不足**（母體未定義），
R-PMH19 是**規則寫錯**（母體定義了，但定錯）。第一次的修法是「把母體寫下來」，
而那個修法本身又引進了新的錯 —— 故本包之 R-PMH24 不再只是改規則，
而是加上**反向驗證義務**：任何母體規則須列出其排除清單並逐項確認
「排除的理由是否成立」。

---

## 三、補測：修正後之母體 16 檔（分析層實測）

**量測條件**：`ASW-R2` 全樹 `**/*036*.xlsx`（候選 28），依 R-PMH24 之修正
規則重篩得 16；`openpyxl` `data_only=True` 讀 `Test Case Specification*`
分頁之 `D3`／`D4`／`D5` 與 `Cover 封面!D6`。

### 3.1 04 包已測之 11 檔 —— 不重列（見上繳 §2.2）

`D3`／`D4` 全空；`D5` 非空者 3：AMFM、Privacy、SXM。

### 3.2 本次補測之 5 檔

| 交付夾 | 欄數 | `Cover!D6` | 資料列 | D3 | D4 | **D5** |
|---|---|---|---|---|---|---|
| `Core HMI/HomeHMI/` | **33** | `B` | 216 | 空 | 空 | **`FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告`** |
| `Core HMI/Menu Bar and AppDrawer/` | **33** | `B` | 219 | 空 | 空 | **`FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告`** |
| `Core HMI/Notifications HMI/` | **33** | `B` | 82 | 空 | 空 | **`FM-WI-FSM-036-A01`** |
| `Vehicle Settings/CFTS044/` | 34 | `C` | 243 | 空 | 空 | 空 |
| `Vehicle Settings/VF230_V1_R5/` | 34 | `C` | **0** | 空 | 空 | **`FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA`** |

**補測 5 檔中 4 檔之 `D5` 非空。**

### 3.3 修正後之全母體計數（分母 = 16）

| 欄 | 空 | 非空 |
|---|---|---|
| `D3` | **16** | 0 |
| `D4` | **16** | 0 |
| **`D5`** | **9** | **7** |

**由 3/11 變為 7/16。** `D3`／`D4` 之結論不變（全母體皆空）。

### 3.4 七個非空 `D5` 之逐字與指向

| # | 交付夾 | `D5` 逐字 | 指向 |
|---|---|---|---|
| 1 | `AM:FM/` | `SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323` | 自身之 037 報告全名 |
| 2 | `SiriusXM/` | `SWE1_SXM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260406` | 自身之 037 報告全名（同 #1 模板） |
| 3 | `VF230_V1_R5/` | `FM-WI-FSM-037-A03_SWE1_VF230_STLA 報告_SWRA_STLA` | 自身之 037 報告名（不同排列、無日期） |
| 4 | `Menu Bar and AppDrawer/` | `FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告` | 自身之 037 報告名（第三種排列） |
| 5 | **`HomeHMI/`** | **與 #4 逐字相同** | **他 feature（AppDrawer）之報告名 —— 疑為複製未改** |
| 6 | `Privacy Mode/` | `SWE1_CFTS_022-Privacy_Features` | CFTS 規格條目 id，非報告名 |
| 7 | **`Notifications HMI/`** | **`FM-WI-FSM-036-A01`** | **表單編號本身 —— 非任何規格或報告** |

**觀察（描述，非提案）**：

- 七個非空者用了**五種不同格式**；無兩個 feature 用同一模板者超過兩份
  （#1／#2 同模板，#3／#4 各自不同）。
- **兩個是錯的**：#5 指向他 feature 之報告，#7 指向表單編號本身。
- 若只看「填得對」者：4 份，全部指向**自身之 037 報告名**，但排列各異。
- `D5` 非空與 `Cover!D6` 版本、欄數、資料列數皆無相關性
  （33 欄 ver B 三份全非空；34 欄 ver C 十份中三份非空）。

---

## 四、裁決條文（逐條抄入 `RULINGS.md`）

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

## 五、**Q3 重裁 —— 完整語料已備齊，請 Pei 裁定**

`D3`／`D4`：全母體 16/16 皆空，**維持留空無爭議**，本項不需重裁。

`D5`：**9/16 空、7/16 非空**（原據之「5/5 皆空」與修正後之「3/11」皆已作廢）。

| 案 | 內容 | 支持 |
|---|---|---|
| **（甲）維持留空** | `D5` 不填 | 母體最大單一群（9/16）；且非空之七者中有兩者填錯（一者指向他 feature 之報告、一者指向表單編號），顯示該欄無有效管制 |
| **（乙）填自身之 037 報告全名** | 建議字串：`SWE1_PowerModingHMI_FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1 STLA 報告` | 七個非空者中「填得對」之四者全部採此指向；且本 feature 之 037 檔名已知，可逐字取得 |

**分析層不提案。** 理由：兩案之語料強度相當（9 vs 7 之差距不足以稱慣例），
且此欄屬交付形式，其取捨牽涉客戶端閱讀習慣，非分析層可判。

**裁定前 `D3`／`D4`／`D5` 一律不寫入**，行為與現行 R-PMH10 相同，不阻斷任何步驟。

---

## 六、作業步驟

1. **抄錄** —— §四之 R-PMH24／R-PMH25 逐字抄入 `RULINGS.md`，附核對表。
   R-PMH19 條後加「(a) 已由 R-PMH24 取代」之附註（**原文不改字**）。
   R-PMH10 之 `[PEI-REOPEN]` 標記更新其語料為 §三之 16 檔數據。

2. **A-PMH12 之全母體 DV 掃描**（清償 04 §8 第 5 項）—— 對 R-PMH24 修正後
   之 16 檔各自全簿掃 DV（legacy ＋ x14），回報：
   (a) `AF`／`AG` 之 `formula1` 是否皆帶前導空白；
   (b) 各檔之 x14 source 指向何處（`下拉選單` 或 `Reference` 或其他）；
   (c) priority DV 之 sqref 是否跨欄。
   **依 R-PMH20，結論句之量詞須等同實測範圍**（16 檔即說 16 檔，不說「表單」）。

3. **`Product Document!B7:C7` 之影響評估**（清償 04 §8 第 4 項）——
   16 檔中該格有值者幾份、其值為何。**只登記，不提案**。

4. **Phase 3 前置：Layer 3 表之機器產出** —— 產出
   `data/layer3_sections.tsv`：48 leaf ×（`SWE-Requirement ID`、
   `outline_number`、`章`、`FROP`、`PDF 頁次`）。
   **Layer 3 為規格章節分群，取規格自身之 section id，不得自創標籤**
   （canon §4.1.1）。此表為 Layer 2 提案之輸入。
   **不擬 Layer 2 名稱、不定 granularity** —— 該提案由分析層於下一包提出，
   Pei 裁定。

5. **`check_write_back.py` 之接線狀態登記**（清償 04 §8 第 3 項）——
   於 `DECISIONS.md` 明記：三項檢查已實作並經故意失敗驗證，
   但**尚未被任何寫回路徑呼叫**；R-PMH22 所要求之「每次寫回前自動驗證」
   之接線為 **Phase 6 之交付項**。標為**已知未完成**，非疏漏、非 RESOLVED。

6. **母體排除清單之反向覆核**（R-PMH24 新增義務）—— 對 28 個候選中被排除
   之 12 個，逐項列出其路徑與排除理由，並逐項回答「該理由是否成立」。

---

## 七、停止條件

canon §0 六條，另加本包三條：

7. R-PMH24 修正後之母體 ≠ 16（分析層實測值；不符即停並回報差異）
8. 步驟 6 之反向覆核發現任一被排除檔之理由不成立
9. 步驟 4 之 Layer 3 表有任一 leaf 無法對應到規格自身之 section id

**本包零寫回工作簿。** 全部改狀態 git 屬 Pei（R-G5）。
**不得改動 `scripts/new_feature.py`**（禁止項仍在）。

---

## 八、上繳包要求（`docs/upstream/05_corpus_fix_and_framework_prep.md`）

1. §四二條之抄錄核對表 ＋ R-PMH19 附註之落實證明（原文 SHA256 未變）
2. 步驟 2 之 16 檔 DV 掃描表 ＋ 依 R-PMH20 檢查過之結論句
3. 步驟 3 之 `Product Document!B7:C7` 登記
4. `data/layer3_sections.tsv` ＋ 其 48/48 對應之驗證
5. 步驟 5 之 `DECISIONS.md` 登記段落
6. 步驟 6 之 12 項排除清單與逐項覆核結果
7. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
8. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之唯讀／改狀態分列

---

## 九、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §四 |
|---|---|---|
| R-PMH24 | 母體判準以用途目錄排除，非以深度；新增反向驗證義務 | ✅ |
| R-PMH25 | `design_method` vocabulary 取自 x14 所指 source，非同名分頁 | ✅ |

二條各管一事。R-PMH24 為**取代型**，其取代範圍（僅 (a)）與保留範圍
（(b)(c) 與揭露義務）已於條內分別明載。

**待 Pei 者一項**：Q3 之 `D5`（甲留空／乙填自身 037 報告全名），
完整語料見 §三、§五。
