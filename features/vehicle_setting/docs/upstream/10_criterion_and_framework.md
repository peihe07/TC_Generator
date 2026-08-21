# 上繳 10 —— 判準之反向驗證、負向掛載、framework Layer 3 草案

執行層寫入。依據：`docs/handoff/28_review_round11.md` §5。
canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 逐字轉錄 R-VS36 | ✅ |
| D-3 | A-VS41 ＋ 登記簿兩數 | ✅ 見 §5.1 |
| **W-39** | in-scope 判準之反向驗證 | ⚠ **升級條件命中** |
| **W-40** | 負向候選掛載 ＋ 階數複核 | (1) ✅ ／ (2) ⚠ **升級條件命中** |
| **W-41** | framework Layer 3 草案 | ✅ `framework.md`，**未鎖定** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-39(1)(3)(4) —— 新舊兩組判準之全量重算

| 判準 | in-scope | 全文未覆蓋 | 21 節內 | 已覆蓋 | 未覆蓋 | 覆蓋率 |
|---|---:|---:|---:|---:|---:|---:|
| **LEGACY**（27 包：AT ＋ EE Arch） | **1,128** | **998** | **169** | **130** | **39** | **76.9%** |
| **NEW**（11 輪：＋ECU ＋Radio） | **294** | **164** | 136 | **130** | **6** | 95.6% |

**LEGACY 六數與 27 包逐項相符**（1,128／998／169／130／39／76.9%）——
`998` 之來源確認為 `1,128 − 130`。區塊總數 **2,030** 相符，落點章節 **21** 相符。

> **NEW 之未覆蓋數 6，恰等於 11 輪 W-37 逐條讀出之 6 筆 (c)。**
> 即新判準把 33 筆 (b) 全數排除、且**只**排除它們 —— 兩條獨立路徑得同一集合。

### 1.2 W-39(2) —— 範圍向（R-G9）

| 檢查 | 結果 |
|---|---|
| NEW 相對 LEGACY，於已覆蓋集上**額外**排除者 | **0**（130 → 130） |
| **251 個已覆蓋 reqid 落在 NEW 之外者** | **121** ⚠ |
| 其中落在 **LEGACY** 之外者 | **同一 121** |

**ECU／Radio 兩條件本身通過範圍向檢查**（額外排除 0）。
**但 121 筆落在兩版判準之外 —— 此為 LEGACY 既有之缺陷，見 §2.1。**

### 1.3 W-40(1) —— 負向候選之掛載（依 R-VS36 三形態）

| token | `$X$` | 裸名 | 描述式 | 聯集 |
|---|---:|---:|---:|---:|
| `$ESS_ENG_ST$` | **5** | **7** | 0 | **7** |
| `$EngRun_Stat$` | 13 | 13 | 0 | 13 |
| `$Heated_Seats_Levels$` | 2 | 2 | 0 | 2 |
| `$Hybrid_Type$` | 14 | 14 | 0 | 14 |
| `$PowerMode$` | 13 | 13 | 0 | 13 |
| `$VC_VEH_LINE$` | 2 | 2 | 0 | 2 |

**17 / 17 列 `mounted`，`no_mount_point` = 0。** Functional leaf 母體 **237** 相符。

> **R-VS36 首次使用即命中**：`$ESS_ENG_ST$` 之 `$X$` 形態得 5，
> 裸名得 7 —— **多出之 2 個 leaf 若只試 `$X$` 便會漏掉**。

### 1.4 W-41 —— framework Layer 3

| 項 | 來源記載 | 實測 | 判定 |
|---|---|---|---|
| Functional leaf | 237（R-VS15） | **237** | 符 |
| delegate yes／no／blocked | 174／46／17（08 包） | **174／46／17** | 符 |
| CFTS044 章節 | 21（27 包） | **21** | 符 |
| Layer 3 token | 未給 | **18** | 新 |

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **升級：in-scope 判準漏 `Atlantis Mid`，121 / 251 已覆蓋條文被排除在母體外**

251 個已覆蓋 reqid 中 **121 筆落在 in-scope 之外**。逐筆查其失敗條件：

| 失敗於 | 筆數 |
|---|---:|
| `EE Architecture` | **121（全部）** |
| `Artifact Type` | 0 |

**121 筆之 `EE Architecture` 值全數為 `Atlantis Mid`**，
`Artifact Type` 全數為 `Subsystem Functional Requirement`。

全 2,030 條之 `EE Architecture` 值域：

| 值 | 筆數 |
|---|---:|
| `Atlantis High` | 825 |
| `PowerNet` | 498 |
| `CUSW` | 388 |
| `All` | 354 |
| **`Atlantis Mid`** | **247** |

27 包之判準取 `{Atlantis High, All}`，**未取 `Atlantis Mid`**。

**這不是推測** —— 那 121 筆是 037 之 237 個 Functional leaf **實際引用**的條文。
**它們被 037 覆蓋，卻不在 in-scope 母體內**：判準與事實直接矛盾。

**28 包 §5 之升級條件逐字為「251 個已覆蓋 reqid 有任一落在新判準之外」——
實測 121 筆落外，命中。判準之修訂屬分析層，執行層不自行擴充。**

**其連鎖後果**（須由分析層重述，非本層自行改）：

| 受影響 | 現況 |
|---|---|
| 27 包之 1,128／998／169／39／76.9% | 皆以漏 `Atlantis Mid` 之判準算得 |
| **11 輪之「(a) = 0，母體 237 完整」** | **不再安全** —— 其只在 169 條上查過 |

**敏感度觀測（未採用，僅供分析層裁定時參考）**：

| 若判準加入 `Atlantis Mid` | in-scope | 全文未覆蓋 | 21 節內 | 已覆蓋 | 未覆蓋 |
|---|---:|---:|---:|---:|---:|
| LEGACY ∪ Mid | 1,314 | 1,063 | 308 | **251** | **57** |
| NEW ∪ Mid | 425 | 174 | 259 | **251** | **8** |

加入後 251 筆全數落入母體。`NEW ∪ Mid` 之未覆蓋為 **8** ——
**較 11 輪已逐條讀過之 6 筆多 2 筆，該 2 筆從未被檢視，其是否為 (a) 未知。**

### 2.2 ⚠ **升級：階數之明示數 5 / 17，與 08 包之 1 / 27 不符**

W-40(2) 依 28 包放寬之判準
`\b(one|two|three|single|multi)[\s-]?(stage|level)s?\b` 複核，得 **5 筆明示階數**：

| Comfort leaf | 命中 | 原文節錄 |
|---|---|---|
| `SWE1-HVAC-054` | `Multi Level` | `For Multi-Level Heated/Vented seats, a press of the heated seat button open…` |
| `SWE1-HVAC-055` | `Multi Level` | `For Multi-Level Heated/Vented seats, a press of the vented seat button open…` |
| `SWE1-HVAC-062` | `Multi Level` | `For Multi-Level Heated steering wheel, a press of the heated steering wheel…` |
| `SWE1-HVAC-063` | `Single Level` | `For Single-Level heated steering wheel, a press of the heated steering wheel…` |
| `SWE1-HVAC-067` | `Multi Level` | `For Multi-Level Heated/Vented seats a press of the heated seat button turns…` |

08 包之判準為 `one／two／three stage(s)` ——
**`Multi-Level` 與 `Single-Level` 兩種寫法皆不在其形態內，故必然得 1。**

> **R-VS34 形態第三次**（`$HSW_StatFailSts$`、`$Cooled_Seats$`，今為階數）。
> **且這次的後果最重**：08 包據「1 / 27」判「**資料本身沒有可收斂之維度**」，
> 而資料其實有 —— **只是寫成 `Multi-Level` 而非 `stage`**。
> W-34(1) 之 `0 / 174` 收斂失敗，其成因診斷**可能整個是錯的**。

**且此維度正是 DR-15 之維度。** DR-15 問「請求訊號為 1 bit 或承載階數」，
而 Comfort 側原來明寫 `Multi-Level` / `Single-Level` 之分 ——
**DR-15 之問法應否據此改寫，屬分析層。**

側別維度同時複核：**2 / 17**，與 08 包之 2 / 27 之**分子相符**。

### 2.3 Comfort 側三處母體數字互不一致

| 出處 | 數 |
|---|---|
| 08 包 §2.2「委派所引之相異 Comfort leaf」 | **27** |
| 08 包 §（另處）「相異 Comfort leaf」 | **22** |
| **本輪自 `delegation_lookup.tsv` 實測**（`delegate = yes` 之 174 列） | **17** |
| 06 輪「Comfort leaf 全母體」 | **498** |
| **本輪自 037 `Analysis Report` 分頁實測之相異 `SWE1-HVAC-` id** | **129** |

**不自行調和。** 分母之差直接影響 §2.2 之比例（5 / 17 vs 1 / 27）,
惟**分子（5 vs 1）之差與分母無關**，§2.2 之結論不因此動搖。

### 2.4 W-40(1) 之 17 / 17 與 11 輪之「7 有／10 無」不衝突

11 輪之 `leaf_ids` 欄問的是「**哪些 leaf 提到該排除值**」（per-value）；
28 包 §4 之掛載規則問的是「**哪些 leaf 引用該 token**」（per-token）。
**兩者是不同的問題**，非同一數字之二測。前者 7／10，後者 17／0，兩者並存。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `negative_test_candidates.tsv` 增 `mount_leaf_ids`／`mount_status` 兩欄，17/17 掛載；`scripts/inscope_w39.py`／`scripts/mount_negative_w40.py` 兩支新腳本；`framework.md` Layer 1–3 草案（四數全符） |
| **核實無誤** | LEGACY 六數與 27 包逐項相符；NEW 之未覆蓋 6 與 11 輪逐條讀出之 6 筆 (c) 為同一集合；ECU／Radio 之範圍向額外排除 0；237／174／46／17／21 全符 |
| **正確地不動** | **未把 `Atlantis Mid` 自行加入判準**（§2.1，屬分析層）；**未據 5 / 17 改寫 DR-15 之問法**（§2.2）；**未調和 27／22／17／498／129 五個數**（§2.3）；**`framework.md` 未鎖定**（Tier 2 屬 Pei） |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| CFTS044 條文區塊 | `inputs/R1LR_Atl-H_25PI3.5_…CFTS_044_Vehicle Controls_SR26_20250909-1816.docx`；`word/document.xml` body 段落；以 `\d{7}\s*:\s*\[Artifact Type` 為界，得 **2,030** |
| 屬性 | `\[([^:\]]+):([^\]]*)\]`，多值以 `,` 展開；**同名屬性取首次命中**（已知界線） |
| 章節歸屬 | `<w:pStyle w:val="1".."7">` 之標題段落；**節號為標題文字之前綴**（非自動編號欄位），以 `^\s*((?:\d+\.)+\d+|\d+)\s+\S` 取得；區塊繼承其上一個標題之節號 |
| LEGACY 判準 | `Artifact Type` 含 `Subsystem Functional Requirement` **且** `EE Architecture` 含 `Atlantis High` 或 `All` |
| NEW 判準 | LEGACY ＋ `ECU` 含 `LTM`／`ETM`／`RRM` 之一 ＋ `Radio` 含 `R1L` 或 `R1L-R`（**`Radio` 欄為空者視為不限**） |
| 已覆蓋 reqid | `data/leaf_to_reqid.tsv` 之 `CFTS044-(\d{7})`，得 **251** |
| W-40(1) token | **R-VS36 三形態**：`$X$`／`\bX\b`／`(?:PROXI parameter\|signal\|LID\|parameter)\s+X`（描述式不分大小寫），取聯集；leaf 全文為 `leaves.tsv` 各欄以空白接合，母體扣除 `non_functional_leaves.tsv` 之 34 列 |
| W-40(2) | Comfort 037 之 `Analysis Report` 分頁，逐列各欄以空白接合，**每個 `SWE1-HVAC-\d+` 取其首次出現之列**；階數 `\b(one\|two\|three\|single\|multi)[\s-]?(stage\|level)s?\b`、側別 `\b(driver\|passenger\|left\|right)\b`，皆不分大小寫 |
| W-41 Layer 3 | `SWE1-VC-(.+)-\d+$` 之中段 token；Layer 2 以 token 含 `HeatedSteeringWheel`／`HeatedSeat`／`VentedSeat` 判，其餘歸 `Common Features` |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS41** | —（28 包 §4 指定登記，不排作業） | 純交叉參照條文無機器判準 |
| **A-VS42** | —（判準，屬分析層） | **in-scope 判準漏 `Atlantis Mid`，121 / 251 已覆蓋條文被排除在母體外**。⚠ 升級 |
| **A-VS43** | **DR-15 之問法受影響** | **階數之掃描形態只試 `stage`，未試 `Level`；實為 5 / 17 而非 1 / 27**。⚠ 升級。R-VS34 形態第三次 |
| **A-VS44** | — | Comfort 側母體數字互不一致（27／22／17；498／129） |

**無新開 DR。** DR-8／DR-12 維持；DR-15 **未送出，且其問法因 A-VS43 須先由分析層複審**。

### 5.1 D-3 —— 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **4**（A-VS41／42／43／44） | **43** |
| `DATA_REQUESTS.md` | **0** | 不變 |

§5 表列 4 筆，登記簿逐筆核對**皆在**，**差額 0**。

> **登記簿之相異編號為 43，而最大號為 A-VS44 —— `A-VS02` 未曾使用（缺號）。**
> 逐號檢視 1–44，缺者僅此一個。**不自行補號、不重編**，於此記明。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **`Atlantis Mid` 之外，`EE Architecture` 尚有 `PowerNet`(498) 與 `CUSW`(388) 未查。**
   本輪只證明 `Atlantis Mid` 必須納入（121 筆實證），
   **未查已覆蓋之 251 筆是否還有落在其他值上者** —— 實測 251 全數僅含
   `Atlantis High`／`All`／`Atlantis Mid` 三值，故**此點已封閉**。
   但**未來若母體擴大，此檢查須重做**。

2. **`NEW ∪ Mid` 之 8 筆未覆蓋中，有 2 筆從未被逐條讀過。**
   11 輪只讀了 6 筆並全判 (c)。**那 2 筆是否為 (a) 未知** ——
   **在其讀完之前，「母體 237 完整」不能算已證。**

3. **W-40(2) 只複核了 `delegate = yes` 所引之 17 個 Comfort leaf。**
   Comfort 全母體（實測 129）中其餘 112 個未掃。
   若 `Multi-Level` 之寫法在未掃部分更普遍，
   **08 包「資料無可收斂維度」之結論會錯得更多。**

4. **`framework.md` 之 Layer 3 以 SWE ID 中段 token 機械切分，未經語意複核。**
   `LeftFrontHeatedSeat`(17) 與 `RightFrontHeatedSeat`(15) 之 leaf 數不等 ——
   **左右理應對稱，差 2 未追因。**
