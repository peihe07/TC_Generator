# ANOMALIES — FW036 Time Management HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-TMnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

A-TM01…A-TM05 由下放包 `docs/handoff/00_intake_scaffold.md` §5 指定登記。
A-TM06…A-TM08 為執行層於本次 intake 實測時自行登記（Tier 1 之登記權限）。

| # | 標題 | 狀態 | 處置層級 |
|---|---|---|---|
| A-TM01 | `features/vehicle setting`（含空格）孤兒 scaffold | PENDING | Tier 3 |
| A-TM02 | 037 之身分未定 | PENDING | Tier 2 |
| A-TM03 | SYS2 EE Architecture 欄大小寫漂移 | PENDING | Tier 1 判準 |
| A-TM04 | `new_feature.py` 目錄名推導無 slugify | PENDING | Tier 2 |
| A-TM05 | `intake.py --scaffold` 與 `--adopt-existing` 整合缺口 | PENDING | Tier 2 |
| A-TM06 | `a03_report` 路徑含 `&` 字元 | PENDING | Tier 1 判準 |
| A-TM07 | 036 工作簿缺件 → `workbook_state` 無法判定 | PENDING | Tier 3（取件） |
| A-TM08 | SYS2 EE Architecture 表頭宣告詞彙集與實測值集不符 | PENDING | Tier 2 |
| A-TM09 | 037 只覆蓋 SYS2 功能需求之 59.5%，51 筆 FR 無對應 leaf | PENDING | **Tier 2（阻塞覆蓋稽核）** |

---

## A-TM01 — `features/` 下有孤兒 scaffold `vehicle setting`（含空格）

**狀態：PENDING。處置屬不可逆操作，Tier 3，執行層不得動。**

實測（分析層，2026-08-20，對 repo 實際路徑）：`features/vehicle setting/`
與 `features/vehicle_setting/` 並存，兩者皆為完整 feature 目錄結構。
比對 `feature.yaml`：

| | `vehicle setting`（空格） | `vehicle_setting`（底線） |
|---|---|---|
| paths | 全為 `<FW036 xlsx>` 等佔位符 | 真實檔名 |
| spec_mode | `"A"`（模板預設） | `"D"`（00 包 W-12） |
| design_method 欄 | `Q`（模板值） | `R`（實測；Q 為 Estimated Test Time）|
| author 欄 | `Z`（模板值） | `AA`（實測；Z 為 Fastack (376) Atl-Mi）|
| `RECON.md` | 無 | 有 |

判讀：含空格者為未填之 scaffold，實跑者為底線版。成因已由 A-TM04 查明，
非人為手滑而是工具行為。建議 `mv` 入 `archive/`（比照 R-G2 不刪除慣例），
待 Pei 裁。

**執行層複核（2026-08-20）**：本次 intake 已獨立確認兩目錄仍並存，且兩者
皆未進 git（`git status` 顯示為 untracked）。本次作業未觸及任一目錄。

---

## A-TM02 — 037 之身分未定

**狀態：PENDING。Tier 2。**

`SWE1_Secure_Date&Time.xlsx` 之命名與封面欄位與 FW036-037-A03 之既有命名
慣例不符。是否為本 feature 之權威 037 待確認。未確認前，**不得以其 leaf
集合作為覆蓋稽核之分母。** 本件因只有單一 swra_report，`intake.py` 不會
觸發多報告仲裁，故腳本不會自行提出本問題 —— 這是登記本條的理由。

**執行層重測（2026-08-20，對 `inputs/` 原始 binary）**：

- SHA256 `3d692e75b3bf1dc7359443483a551145f4696b3f2c509d3019569ef7139ee279`
- 分頁：`封面` / `ChangeHistory 修訂履歷` / `Product Document 記錄封面頁` /
  `Analysis Report`
- `Analysis Report` 封面塊：`Project Name：` = `New R1L`（列 3）、
  `Date：` = `2020/09/05`（列 4）、**`Reviewer：` 欄空白**（列 4，未填）
- **列 6 為未清除之模板佔位說明列**（`< Mention the ID generated from the
  tool>` 等）。表頭在列 8，資料列為列 9–30。
- 需求列 22 筆，`SWE-RA-TIME&DATE-001` 至 `-022`，**連號無缺號**。
  `intake.py` 報告之 22 rows 與此一致，佔位列未被誤算入分母。

新增之疑點（強化本條，非另立）：**Reviewer 欄空白**與**模板佔位列未清除**
兩者並存，指向本件可能為未經審查之工作稿而非釋出版。對照日期 `2020/09/05`
早於 SYS2 之 SR26 釋出甚多，益發可疑。

**執行層建議（不自行認定）**：向來源索取 FW036-037-A03 之正式釋出件，
比對其 leaf 集合是否亦為 22 筆連號。若正式件不存在，需 Pei 明裁本件可否
充當覆蓋稽核分母。已登記為 DATA_REQUESTS #2。

---

## A-TM03 — SYS2 之 EE Architecture 欄大小寫漂移

**狀態：PENDING。判準之建立屬 Tier 1，但須先對全集驗過。**

分析層對沙箱副本之唯讀探測（2026-08-20）：`Basic Report` 分頁，第 2 列起
共 227 資料列，取第 7 欄 `SYS2 EE Architecture (All,ATL-Hi,ATL-Mi)` 之值，
區分大小寫，精確相等計數。

`ATL-Hi` 與 `Atl-Hi` 為同義不同寫。**任何以字串等值篩 Atlantis High 之
腳本會靜默漏掉 10 列**，且不會報錯 —— canon §5a「詞彙型工具之缺陷不會
報錯，須以已知全集驗證」。凡涉本欄之篩選，判準須先對 227 列全集驗過再立。

**執行層重測（2026-08-20，對 `inputs/` 原始 binary，非沙箱副本）**

量測條件：`SYS2_CFTS_015_Time and Date _SR26_V1_Including_Delta_Released.xlsx`
（SHA256 `ecf665a1…c432dec1`），`Basic Report` 分頁，`openpyxl` read_only +
data_only，表頭為列 1，資料列為列 2 起共 **227** 列，區分大小寫精確相等計數。

第 7 欄 `SYS2 EE Architecture (All,ATL-Hi,ATL-Mi)`：

| 值 | 沙箱副本 | **原始 binary 重測** | 差異 |
|---|---|---|---|
| `ATL-Hi` | 101 | **101** | 無 |
| `All` | 61 | **61** | 無 |
| `ATL-Mid` | 55 | **55** | 無 |
| `Atl-Hi` | 10 | **10** | 無 |
| 合計 | 227 | **227** | 無 |

第 10 欄 `SYS2 分類 Category`：

| 值 | 沙箱副本 | **原始 binary 重測** | 差異 |
|---|---|---|---|
| `Functional Requirement` | 126 | **126** | 無 |
| `Heading` | 70 | **70** | 無 |
| `Information` | 30 | **30** | 無 |
| `Out of Scope` | 1 | **1** | 無 |
| 合計 | 227 | **227** | 無 |

**重測結論：兩組數字與沙箱副本逐項相符，無差異可報。** 本條之事實基礎
成立，以重測值為基線。Atlantis High 之正確全集為 `ATL-Hi` ∪ `Atl-Hi`
= 111 列；任何只取 `ATL-Hi` 之判準漏 10 列（9.0%）。

重測另發現表頭與值集之第二層不符，另立 A-TM08。

---

## A-TM04 — `new_feature.py` 之目錄名推導無 slugify（工具缺陷，A-TM01 之成因）

**狀態：PENDING。根本修法屬 Tier 2，執行層不得逕改。**

`scripts/new_feature.py` `scaffold()`：

```python
feat_dir = root / "features" / feature.lower()
```

`.lower()` 不處理空格。`python scripts/new_feature.py "Vehicle Setting"` 即
產生 `features/vehicle setting/` —— A-TM01 之孿生目錄由此而來，不是手滑。
腳本不報錯、不警告，且該目錄之後續一切操作看起來都正常。

現行迴避方式已寫入 R-TM3(1)（參數帶底線）。提議之處置：加 slugify 並對
既有目錄做一次性對照表，或至少在偵測到空格時 `sys.exit`。連帶副作用須
評估：`abbr = feature[:2].upper()` 亦受參數字面值影響（見 R-TM3(3)）。

**執行層複核（2026-08-20）**：迴避方式有效。本次以 `Time_Management`
呼叫，產出 `features/time_management/`，`ls -d "features/time management"`
無命中。缺陷本身未修，仍對後續 feature 有效。

---

## A-TM05 — `intake.py --scaffold` 與 `new_feature.py --adopt-existing` 之整合缺口

**狀態：PENDING。修法屬 Tier 2，執行層不得逕改。**

`new_feature.py` 之註解明言 `--adopt-existing` 的用途是「the analysis layer
has already delivered docs/handoff/ into an otherwise-empty feature dir」——
正是本包之形態。但 `intake.py` `scaffold()` 為：

```python
feat_dir = root / "features" / feature.lower()
if not feat_dir.exists():
    subprocess.run([... "new_feature.py", feature ...], check=True)
...
text = yaml_path.read_text(encoding="utf-8")     # ← 目錄已存在時，此檔不存在
```

目錄已存在時直接跳過 scaffold，隨即在讀 `feature.yaml` 處
`FileNotFoundError`。亦即：兩支腳本對「分析層先落檔」這件事的假設相反，
一支專門設計了旗標去支援，另一支則會崩。

現行迴避方式已寫入下放包 §3（先手動跑 `--adopt-existing` 再跑 `--scaffold`）。
提議之處置：`intake.py` 改為既存目錄時以 `--adopt-existing` 呼叫
`new_feature.py`，而非跳過。

**執行層複核（2026-08-20）**：迴避序列有效，四步全數成功，`--adopt-existing`
未覆寫 `docs/handoff/00_intake_scaffold.md`。缺陷本身未修。

---

## A-TM06 — `feature.yaml` 之 `a03_report` 路徑含 `&` 字元

**狀態：PENDING。執行層登記。判準之建立屬 Tier 1。**

實測：037 之檔名為 `SWE1_Secure_Date&Time.xlsx`，含 shell 之控制字元 `&`。
`intake.py --scaffold` 已將其原樣寫入 `feature.yaml`：

```yaml
  a03_report: "inputs/SWE1_Secure_Date&Time.xlsx"
```

YAML 層安全（雙引號包覆，`&` 僅在值起首才是 anchor 語法，此處在字串中段）。
**風險在下游**：任何從 `feature.yaml` 讀出此值後未加引號傳入 shell 的腳本，
`&` 會被解為背景執行運算子，指令在 `inputs/SWE1_Secure_Date` 處被切斷 ——
與 A-TM03 同型，**失敗形態為靜默而非報錯**。

附帶：下放包 §2 與 R-TM1 均記本檔為 `SWE1_Secure_DateTime.xlsx`（無 `&`），
與實測不符。屬別名字面差異，不動 R-TM1 之裁定內容，已於 `RULINGS.md`
R-TM1 之執行層回報段註記。

**執行層建議**：涉本路徑之 shell 呼叫一律 `shlex.quote()` 或改用
`subprocess` 之 list 形式；不建議改名檔案（改名會使 SHA256 稽核與來源
可追溯性斷鏈）。

---

## A-TM07 — 036 工作簿缺件，`workbook_state` 無法判定

**狀態：PENDING。取件屬 Tier 3（Pei）。**

本 feature 之 FW036 客戶原件未隨素材投放。`feature.yaml` 之
`paths.workbook` 仍為佔位符 `"inputs/<FW036 xlsx>"`。

下放包 §2 已預先揭露此為已知缺件，§6 並列為升級條件。執行層照序列跑完
scaffold 而未中止，理由：本包明訂止於 scaffold，缺件不阻塞 Phase 0；
但**阻塞 Phase 1 recon 之下列項目**，於此逐項落實：

1. `workbook_state` 判不出來（BLANK / PARTIAL_CLEAN / PARTIAL_INTERLEAVED / FULL）
2. R-TM2 之推翻條件（G 欄非空值）無法判定 → `test_group` 永遠停在 [PROVISIONAL]
3. `workbook.columns` 全欄之 header match 無法驗證，現值皆為模板預設，
   未經實測 —— 對照 A-TM01 之表，`vehicle_setting` 實測後 `design_method`
   由 `Q` 改為 `R`、`author` 由 `Z` 改為 `AA`，**本 feature 極可能同樣需
   位移**，現值不得引為基線
4. done-region 偵測（`author_value: "Arif"`）無從驗證
5. 覆蓋稽核之被除數（已覆蓋 leaf 數）無從取得

`intake.py` 之 SWRA 仲裁本亦依賴 workbook 之 Scope 欄；本 feature 僅一份
swra_report，故 `pick = swras[0]` 不致誤選，但 A-TM02 之身分問題因此
無法由腳本回答，必須人工裁。

已登記為 DATA_REQUESTS #1，Urgency = High。

---

## A-TM08 — SYS2 EE Architecture 欄之表頭宣告詞彙集與實測值集不符

**狀態：PENDING。執行層登記。Tier 2（涉來源資料正確性，非本地判準）。**

A-TM03 之重測附帶發現，為 A-TM03 之外的獨立事實：

第 7 欄之**表頭字面**為 `SYS2 EE Architecture (All,ATL-Hi,ATL-Mi)`，
即表頭自行宣告其值域為 `{All, ATL-Hi, ATL-Mi}`。但 227 列之**實測值集**為
`{All, ATL-Hi, ATL-Mid, Atl-Hi}`。

兩處不符：

| | 表頭宣告 | 實測 | 說明 |
|---|---|---|---|
| Atlantis Mid | `ATL-Mi` | `ATL-Mid`（55 列） | 表頭少一個 `d`；**無任何一列之值為 `ATL-Mi`** |
| Atlantis High | `ATL-Hi` | `ATL-Hi` 101 + `Atl-Hi` 10 | 即 A-TM03 |

意義：**表頭不可作為值域之權威**。任何以表頭括號內容自動推導 enum 或
建 dropdown 驗證之做法，會產生一個沒有任何資料列命中的 `ATL-Mi`，並同時
漏掉真正存在的 `ATL-Mid` 與 `Atl-Hi`。與 A-TM03 同屬 canon §5a 之
「詞彙型工具靜默失效」形態，但成因不同：A-TM03 是資料端大小寫不一致，
本條是**後設資料與資料不一致**。

**執行層建議**：值域一律由資料端全集導出並人工複核，不由表頭導出。
本欄之權威值集以本次重測之四值為準，直到 SYS2 有新版釋出。

---

## A-TM09 — 037 只覆蓋 SYS2 功能需求之 59.5%，51 筆 Functional Requirement 無對應 SWE leaf

**狀態：PENDING。Tier 2。執行層登記。本條阻塞覆蓋稽核之分母認定。**

**本條非下放包指派，為執行層依 §7(6)「該驗而未驗者之獨立判斷」自行盤點時
發現可驗、遂驗之結果。** 下放包全篇未觸及 037 與 SYS2 之交叉比對。

### 量測條件

037 `Analysis Report` 列 9–30 之第 2 欄（`Source System Requirement items`）
取出所引用之 `SYS-RA-TIME&DATE-*` 序號；SYS2 `Basic Report` 列 2–228 之
第 2 欄（`SYS2 Sys-RA-Feature-ID`）取全集，按第 10 欄 `Category` 分類。
序號一律 zero-pad 至三位比對。解析同時處理三種書寫：完整 id、逗號延續之
裸數字（`…-021, 022`）、範圍（`029–033`，含 en-dash 與 hyphen 兩形）。

### 結果

| | 數量 |
|---|---|
| SYS2 `Sys-RA-Feature-ID` 全集 | 227 |
| 037 引用之相異序號 | 75 |
| **037 引用但 SYS2 找不到（懸空引用）** | **0** |
| SYS2 有而 037 未引用 | 152 |

152 筆未引用者按 Category 拆解：

| Category | 未引用數 | 判讀 |
|---|---|---|
| `Heading` | 70 | 標題列，本就不該有 leaf — 非缺口 |
| `Information` | 30 | 資訊列，非可測需求 — 非缺口 |
| `Out of Scope` | 1 | 明示不在範圍 — 非缺口 |
| **`Functional Requirement`** | **51** | **真缺口** |

**037 已引用之 75 筆，Category 全部為 `Functional Requirement`，
無一為 Heading／Information／Out of Scope。** 且 75 + 51 = 126，恰等於
SYS2 之 FR 總數（見 A-TM03 之 Category 重測）。

### 解析可靠性

上述完美分割即為解析正確性之驗證：若裸數字啟發式有誤（把不相干數字誤認
為 id），誤中之序號會隨機落在 Heading／Information 上，不可能 75 筆全數
落在 FR 內，亦不可能與 FR 總數恰好互補。

**方向性**：裸數字啟發式若有偏差，只可能**高估**引用集。故 75 為覆蓋數
之**上界**，51 為缺口之**下界**。真實覆蓋率 ≤ 59.5%。

### 意義

037 對 SYS2 功能需求之覆蓋率為 **75/126 = 59.5%**，51 筆功能需求在 037 中
無對應之 SWE-RA leaf。

此結果與 A-TM02 相互強化：一份 Reviewer 欄空白、模板佔位列未清、日期
`2020/09/05` 早於 SR26、且只覆蓋六成功能需求的檔案，**其為未完成工作稿之
可能性高於其為權威釋出件**。

### 對後續 Phase 之影響

1. **覆蓋稽核之分母不得取 22（037 之 leaf 數）**，那只會得出「已全覆蓋」
   之假象，而真正的問題在 037 自身相對 SYS2 就短少 51 筆。
2. 分母之候選有二，屬 Tier 2 裁決：
   - 取 037 之 22 leaf → 稽核範圍等同接受 59.5% 之上游缺口
   - 取 SYS2 之 126 筆 FR → 51 筆將全數落為 BLOCKED，需上游補件
3. 在 Pei 裁定前，**任何覆蓋率數字都不得寫入交付物**。

### 執行層建議（不自行認定）

連同 A-TM02 一併向來源查詢：037 是否另有涵蓋全部 126 筆 FR 之正式版。
若答覆為「037 即此件、51 筆確實不在 SW 範圍」，則需其書面依據，並應說明
為何該 51 筆在 SYS2 標為 `Functional Requirement` 而非 `Out of Scope`
（SYS2 全表僅 1 筆標 `Out of Scope`，顯示該欄有被實際使用，非虛設）。

已登記為 DATA_REQUESTS #4。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-TMnn]`.
