# ANOMALIES — FW036 Time Management HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-TMnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

A-TM01…A-TM05 由下放包 `docs/handoff/00_intake_scaffold.md` §5 指定登記。
A-TM06…A-TM08 為執行層於本次 intake 實測時自行登記（Tier 1 之登記權限）。

| # | 標題 | 狀態 | 處置層級 |
|---|---|---|---|
| A-TM01 | `features/vehicle setting`（含空格）孤兒 scaffold | **MOOT**（目標已滅失）| Tier 3 |
| A-TM02a | 037 之版本身分未定（原 A-TM02，經 R-TM6 分拆）—— **阻塞 D5 交付欄位** | PENDING | Tier 3（隨 RD-1 上問）|
| A-TM03 | SYS2 EE Architecture 欄大小寫漂移 | PENDING | Tier 1 判準 |
| A-TM04 | `new_feature.py` 目錄名推導無 slugify | PENDING | Tier 2 |
| A-TM05 | `intake.py --scaffold` 與 `--adopt-existing` 整合缺口 | PENDING | Tier 2 |
| A-TM06 | `a03_report` 路徑含 `&` 字元 | PENDING | Tier 1 判準 |
| A-TM07 | 036 工作簿缺件 → `workbook_state` 無法判定 | **RESOLVED**（R-TM5） | — |
| A-TM08 | SYS2 EE Architecture 表頭宣告詞彙集與實測值集不符 | PENDING | Tier 2 |
| A-TM09 | 037 只覆蓋 SYS2 功能需求之 61.9%，48 筆 FR 無對應 leaf | PENDING | **Tier 2（阻塞覆蓋稽核）** |
| A-TM10 | `spec_pdf` 仍為佔位符，CFTS docx 未回填 feature.yaml | PENDING | Tier 1 補填／Tier 2 修法 |
| A-TM11 | 母本 Scope 欄（`D5`）為空 | PENDING | **Tier 2（填值）** |
| A-TM12 | `recon.py` 無 spec_mode D 之 outline map 路徑 | PENDING | **Tier 2（阻塞 Phase 4）** |
| A-TM13 | 2 筆被引用需求之來源物件不在 CFTS 基線內 | PENDING | **Tier 2（RD-1 候選）** |
| A-TM14 | FORMS.md 引用之 Home v2 交付件不在磁碟上 | PENDING | **Tier 2** |
| A-TM15 | `recon.py` 整份重寫 `DECISIONS.md`，沖掉手工裁決引用段 | PENDING | Tier 2（修法）／Tier 1（重建） |
| A-TM16 | Home A-H26 之既有定性可能低估 | PENDING | Tier 2（屬 Home）|
| A-TM17 | repo 內有身分不明之併行寫入者（含 `vehicle setting` 滅失、git race）| **RESOLVED**（Pei 確認）| Tier 3 |
| A-TM18 | Comfort 之 framework 僅存本地、未併入全域檔 | PENDING | Tier 2（屬 Comfort）|
| A-TM19 | intake.py 之 A-TM10 衝突訊息未進 INTAKE.md | PENDING | Tier 2（併 A-TM12）|
| A-TM20 | 併行者寫入本 feature，兩支腳本被覆蓋且內容失落 | **RESOLVED**（R-TM44）| Tier 3 |
| A-TM21 | 現存 write_back.py / lint_tcs.py 六項實質缺陷 | PENDING | Tier 2（凍結中不修）|
| A-TM22 | verify_structure 三層全為反向驗證，member 層對映錯誤不可偵測 | PENDING | **Tier 2（B1 前必決）**|
| A-TM23 | CFTS015 兩套物件編號並存，工作簿採 7 位家族而文件無此寫法先例 | **AWAITING_UPSTREAM**（R-TM43）| Tier 2 |

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

**處置（2026-08-20）—— MOOT，非依 R-TM18 完成**

R-TM18 指派將 `features/vehicle setting/` mv 至 `archive/`。執行時實測：
原路徑不存在、`archive/` 內無、全 repo `os.walk` 零命中、
`git log --all` 從未追蹤過 → 形態為 **rm 而非 mv，不可復原**。
分析層與執行層皆未執行任何刪除。

R-TM18 之「archive 內容須逐檔可讀」無法滿足，故**不標 RESOLVED** ——
標了等於以處置條文記載一件與該條文不符之事實（R-TM13 所防之情形）。

狀態改 **MOOT — 目標已滅失**。刪除事件本身另立 A-TM17。

---

## A-TM02a — 037 之版本身分未定

**狀態：PENDING。Tier 3（隨 RD-1 上問）。**
**經 R-TM6(2) 由原 A-TM02 分拆而來：本條僅存版本身分問題；內容缺口
（48 筆 FR 無 leaf）已獨立為 A-TM09，兩條各自處置。R-TM6 明訂：縱使本條
裁定手上這件即權威 037，A-TM09 之缺口依然存在。**

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

**性質升級（2026-08-20，依 `docs/handoff/01Z-A3_review.md` §3.1(c)）**

本條由「上游版本問題」升為 **阻塞交付欄位**。

036 工作簿之 `D5`（範圍 Scope）欄，其語意為「本工作簿所依據之 037 報告
之文件識別」，值即該 037 檔名去副檔名（R-TM9-A2）。交付路徑實測：

| 目錄 | 037 檔名 |
|---|---|
| `Core HMI/HomeHMI/` | `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx` |
| `Core HMI/Menu Bar and AppDrawer/` | `FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx` |
| `User Profiles/` | `FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx` |
| `Time Management/` | **無任何符合該形態之檔案** |

本 feature 手上之 037 名為 `SWE1_Secure_Date&Time.xlsx`，不符該形態。
故 D5 在本條裁定前**無值可填**（非「暫緩填」）。

RD-1 應問：`Time Management` 是否另有正式 037，或
`SWE1_Secure_Date&Time.xlsx` 即是而命名未依慣例。

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

**狀態：RESOLVED（2026-08-20）。處置條文 R-TM5，逐字如下：**

```
R-TM5（Pei, 2026-08-20）—— 036 工作簿以母本為之

本 feature 不索取客戶預填之 036 工作簿。036 以 R-G1 之全域母本
forms/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx 為之。

直接後果：workbook_state = BLANK。
A-TM07（036 缺件 → workbook_state 無法判定）由本條解消，轉 RESOLVED。
```

**解消方式為「改以母本為之」，非「取得客戶件」。** 本條所列之五項阻塞
因而全部解除，但解除方式各異，逐項交代於本條末節。

以下為本條 PENDING 期間之原始登記內容，保留為軌跡：

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

### 解除後之逐項交代（2026-08-20）

| 原阻塞項 | 解除方式 |
|---|---|
| 1. `workbook_state` 判不出 | R-TM5 直接定為 **BLANK**（母本資料區非空格 0，FORMS.md 實測） |
| 2. R-TM2 推翻條件無法判定 | 母本 G 欄資料區為空 → 推翻條件**不成立**，`test_group` 維持 `"Time Management"`；[PROVISIONAL] 標記可於本包後移除，但屬 R-TM2 之判定範圍，本包不逕改，於上繳提請 |
| 3. `workbook.columns` 未經實測 | 已依 FORMS.md 之 rev C 實測值更正五處，並由 recon 之表頭文字比對複驗 |
| 4. done-region 偵測無從驗證 | BLANK 下**無 done region**，`detection` 改 `"none"`（§2.1） |
| 5. 覆蓋稽核被除數無從取得 | 與本條無關 —— 分母已由 R-TM6 定為 SYS2 FR 126，不取 workbook |

**DATA_REQUESTS #1 隨本條轉為 CLOSED。**

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

## A-TM09 — 037 只覆蓋 SYS2 功能需求之 61.9%，48 筆 Functional Requirement 無對應 SWE leaf

**狀態：PENDING。Tier 2。執行層登記，分析層 00R §2 更正數字。**
**本條阻塞覆蓋稽核之分母認定。**

本條非下放包指派，為執行層依 §7(6) 自行盤點時發現可驗、遂驗之結果。
**首版數字（75 / 51 / 59.5%）有誤，已由 00R 更正為 78 / 48 / 61.9%；
更正經過完整保留於本條 §D，不得抹除 —— 更正軌跡本身是稽核證據。**

### A. 量測條件（更正後，為現行基線）

037：`Analysis Report` 第 9 列起、第 1 欄非空者共 22 列，取第 2 欄字串。
展開程序：先將 U+2013 / U+2014 正規化為 `-`，以 `(\d{3})\s*-\s*(\d{3})`
抓範圍展開為**閉區間**，將範圍字串自原字串抽除後，再抓剩餘之 `\d{3}`，
聯集去重。

SYS2：`Basic Report` 第 2 列起 227 列，第 2 欄尾碼三位數 → 第 10 欄
`Category`。227 筆 id 全數解析成功、無重號。

### B. 結果（現行基線）

| | 數量 |
|---|---|
| 037 引用之相異 SYS-RA id | **78** |
| 其中 Category = `Functional Requirement` | **78**（Heading / Information 命中 0） |
| 懸空引用（SYS2 無此 id） | **0** |
| SYS2 FR 總數 | **126** |
| **FR 未被任何 SWE leaf 引用** | **48** |
| **覆蓋率** | **78/126 = 61.9%** |

逐列計數（22 列全列舉，與 00R §2 之人工點數逐項相符）：

```
001:4  002:6  003:3  004:4  005:2  006:3  007:4  008:7  009:9
010:2  011:3  012:2  013:1  014:3  015:6  016:2  017:4  018:3
019:3  020:4  021:1  022:2          合計 78，列間無重號
```

**78 筆之完整 id 清單**：

```
010 011 017 018 021 022 023 024 025 026 027 028 029 030 031 032 033
037 039 042 044 045 046 047 048 049 050 053 054 055 058 059 060 063
068 069 071 075 076 077 079 080 081 082 083 084 085 090 094 096 097
106 109 112 116 118 119 121 125 126 127 136 137 138 139 140 141 142
145 146 147 148 153 154 155 158 221 224
```

**48 筆缺口之完整 id 清單**（皆為 `Functional Requirement`）：

```
009 012 016 036 038 040 041 064 065 066 086 087 088 089 091 092 093
099 108 110 111 113 115 117 122 123 124 128 129 130 131 134 135 144
149 151 152 157 170 172 217 220 222 225 226 227 228 229
```

### C. 意義與對後續 Phase 之影響

037 對 SYS2 功能需求之覆蓋率為 **61.9%**，48 筆功能需求在 037 中無對應
之 SWE-RA leaf。缺口之性質與量級不因 3 筆之差而改變。

與 A-TM02 相互強化：Reviewer 欄空白 + 模板佔位列未清 + 日期 `2020/09/05`
早於 SR26 + 只覆蓋六成 FR，四項合觀，本件為未完成工作稿之可能性高於
其為權威釋出件。

1. **覆蓋稽核之分母不得取 22**（037 之 leaf 數）—— 取 22 只會得出「已全
   覆蓋」之假象，真正的缺口在 037 自身相對 SYS2 就短少 48 筆。
2. 分母之候選有二，屬 Tier 2，與 A-TM02 一併裁：
   - 取 037 之 22 leaf → 等同接受 61.9% 之上游缺口
   - 取 SYS2 之 126 筆 FR → 48 筆全數落為 BLOCKED，需上游補件
3. **A-TM02 與 A-TM09 未裁前，任何覆蓋率數字不得寫入交付物。**

### D. 更正經過（稽核軌跡，不得抹除）

**首版（執行層，2026-08-20）**：75 / 51 / 59.5%。
**更正版（00R §2 提出，執行層獨立復現確認，同日）**：78 / 48 / 61.9%。

**差額 3 筆為 `030` `031` `032`，全部漏在 `SWE-RA-TIME&DATE-009` 一列。**
執行層以 00R 之方法重跑並對差，確認：新有舊無 3 筆，**舊有新無 0 筆**
（即首版無誤抓，純為漏抓）。三筆經查皆為 `Functional Requirement`，
故缺口由 51 降為 48。

**根因**（執行層自查）：該列原始字串為

```
SYS-RA-TIME&DATE-029–033, 046, 047, 080, 081
```

首版之範圍 regex 為 `(?<![\w-])(\d{2,3})\s*[–-]\s*(\d{2,3})`。負向後查
`(?<![\w-])` 之本意是防止把 id 尾碼誤認為範圍起點，**但範圍起點 `029`
前面正是 id 之連字號，故該防護把唯一一個真範圍擋掉，範圍展開完全未觸發**。
其後 `029` 由完整 id regex 撿回、`033` 由裸數字 regex 撿回（其前為 U+2013，
不在字元類 `[\w&-]` 內），中間 `030`–`032` 遂無任何規則命中而蒸發。
全表僅此一列使用範圍寫法搭配 en-dash，故只錯一列。

**首版之兩項推論不成立，登記於此因該形態會重演**（00R §2.1）：

- **(a) 方向性搞反。** 首版稱「75 筆全部命中 FR，故啟發式只會高估，
  59.5% 為上界」。「全部命中 FR」證明的是**零偽陽性**，而零偽陽性與**低估**
  完全相容 —— 本例即是低估。零偽陽性只能支持「引用集 ⊆ 真集」，推出的是
  **下界**。真值 61.9% > 59.5%，「上界」之主張被其自身證據推翻。
- **(b) 恆等式充作檢查。** 首版稱「75 + 51 = 126 恰等於 FR 總數，此完美
  互補即解析正確性之驗證」。但未覆蓋數既定義為 `126 − 命中數`，兩者相加
  必為 126，與引用集對錯無關；`78 + 48 = 126` 同樣成立。**該式之鑑別力
  為零。**

兩者同屬 canon §5a「代理判準（自資料推導之統計範圍）不得凌駕實質判準」
之失誤。實質判準是**逐筆對照**（本條 §B 之逐列點數與 id 清單），非計數
之自洽性。往後凡以解析結果立論者，須公布展開後之完整 id 清單供反驗，
不得只給計數。

---

## A-TM10 — `spec_pdf` 仍為佔位符，CFTS docx 未回填 `feature.yaml`

**狀態：PENDING。補填屬 Tier 1（已執行）；腳本修法屬 Tier 2（未動）。**
由分析層覆核包 `00R` §3 指派登記。

### 成因（執行層已獨立複驗）

`scripts/intake.py:420` 之 `KIND_TO_YAML` 無 `cfts_doc` 鍵：

```python
KIND_TO_YAML = {
    "workbook": "workbook", "swra_report": "a03_report",
    "polarion_export": "sys1_export", "spec_pdf": "spec_pdf",
    "popup_list": "popup_list",
}
```

`scaffold()` 內為 `key = KIND_TO_YAML.get(f["kind"])`，隨後 `if key:` 才回填。
`cfts_doc` 取不到鍵得 `None`，該檔案**被移入 `inputs/` 但不回填任何 yaml
路徑，且不報錯**。

後果：`spec_mode = D` 正是以這份 docx 為 spec 來源，Phase 4 會在
`spec_pdf` 處找不到 spec。與 A-TM03 / A-TM06 / A-TM08 同屬**靜默失效**
形態 —— 本 feature 迄今第四例。

### 處置（已執行）

比照既有先例機械套用。`features/vehicle_setting/feature.yaml` 之
`spec_pdf` 亦指向一份 `.docx`（`R1LR_..._CFTS_044_Vehicle Controls_...docx`），
該值為手填、非腳本產出 —— 執行層已複驗確認。

改前：

```yaml
  spec_pdf: "inputs/<spec pdf>"            # null if spec_mode E
```

改後：

```yaml
  spec_pdf: "inputs/R1LR_Atl-H_25PI3.5_Cabin_CFTS _015 Time and Date _SR26_20250909-1851.docx"  # cfts_doc；手填，見 A-TM10
```

腳本本身之修法（`KIND_TO_YAML` 加 `cfts_doc`）跨 feature 影響，Tier 2，
**未改**。留予 Pei 與 A-TM04 / A-TM05 之腳本修法一併裁。

### 執行層之自我檢討（00R §3 末段所指）

本條屬首版 §7(6) 應盤到而未盤到者。首版之未驗項清單列了 036 缺件導致
之 4 項與範圍外 2 項，但 `spec_pdf` 是**已在 `inputs/`、可立即驗、且在
本包範圍內**之欄位。

失誤在盤點所用之全集：首版是以「本包產出之數字與路徑值」為全集逐一回溯
依據，該全集不含「已存在但未被回填」之欄位 —— 亦即**只盤了寫進去的東西，
沒盤該寫而空著的東西**。正確全集應為 `feature.yaml` 之**全部 path 鍵**，
逐鍵確認其值是否仍為佔位符。

依該正確全集重盤，現況為：

| path 鍵 | 值 | 判定 |
|---|---|---|
| `workbook` | `"inputs/<FW036 xlsx>"` | 佔位符 — 缺件，A-TM07 |
| `a03_report` | 真實檔名 | 已填 |
| `sys1_export` | 真實檔名 | 已填 |
| `spec_pdf` | 真實檔名 | **本條補填後已填** |
| `popup_list` | `"inputs/<Pop Up List xlsx>"` | 佔位符 — 未命中，DATA_REQUESTS #3，非缺陷 |

五鍵全數有交代，無第二個漏網者。

---

## A-TM11 — 母本之 Scope 欄（`D5`）為空

**狀態：PENDING。登記並提案，填值屬 Tier 2，執行層不得自填。**
由下放包 `01_recon.md` §4 指派登記。

### 實測

`forms/FORMS.md` 記載（2026-08-17 唯讀實測）：母本 `C5` 標籤為
`範圍 Scope：`，**值格 `D5` 為空**。執行層已對 `inputs/` 之複本複驗，
與母本一致（複本 SHA256 與母本相同，見上繳包 01 §3）。

### 形態比較

| feature | Scope 值 | 狀態 |
|---|---|---|
| Home | 手工維護 | **錯**（A-H26） |
| AMFM | 手工維護 | **錯**（RULINGS C1） |
| **Time Management** | **空** | 起點較佳 —— 空而非錯，但仍須填 |

兩個既有實例皆為手工維護且皆錯，顯示本欄之填寫缺乏機械保障。本 feature
因採母本，起點是空白 —— 不會繼承錯值，但也不會自動正確。

### ~~提案（Tier 2，執行層不自填）~~ —— **已作廢（R-TM9-A2）**

> **本段之整個框架錯誤，保留為軌跡。** 其前提為「D5 是 feature 標籤欄，
> 可由 feature 名或 spec 標題組成」，經 01Z-A3 §3 實測證否：D5 之語意為
> **037 報告之文件識別**。故下列兩個候選值皆為「指向不存在文件之字串」，
> **任何一個都不得填入**。

~~填值屬交付件內容之範圍界定，執行層登記並提案，等裁。~~

~~格式參照：Home v2 之正確值形態為 `…Home-HMI-V0.1`。依該形態，本 feature
之候選值為 `Time-Management-HMI-V0.1` 或以 spec 文件標題為本之
`Time-and-Date-HMI-V0.1`。~~

~~二者之取捨非執行層可決，因其牽動 R-TM1 之別名體系，與 R-TM2 之
`test_group` 取值屬同一組命名決定，宜一併裁。~~

**解除條件（2026-08-20 依 R-TM9-A2(4) 改寫）**：

原條件（Home v2 之 D5 前綴段切分）**作廢** —— D5 非 feature 標籤欄，
不可由前綴段組成（R-TM9-A2）。

新條件（兩項均須）：
1. A-TM02a（037 身分）經 Pei 裁定
2. 該 037 之檔名逐字實測，去副檔名後即為 D5 之值

在此之前 D5 維持空白，A-TM11 維持 PENDING。

---

## A-TM12 — `recon.py` 無 spec_mode D 之 outline map 建立路徑

**狀態：PENDING。Tier 2（跨 feature，執行層不得逕改）。**
**不阻塞 recon；阻塞 Phase 4 之 `spec_reference` 生成。** 執行層登記。

### 實測

`recon.py` 之 `build_outline_map(sys1_path)` **只接受 `sys1_export`**
（`scripts/recon.py:143`），其 docstring 自陳用途為 spec_mode **A**：

> This is the lookup every spec_reference is linted against under spec_mode A

本 feature 為 **spec_mode D**，01 包 §5(6) 明訂 outline map 應「以
`spec_pdf` 所指之 CFTS docx 為之」。但該函式不讀 `spec_pdf`，逕以
`sys1_export`（SYS2 export）為來源，而該檔**無 `Outline Number` 欄**，
故回傳空 map 與理由字串：

```
SYS2_CFTS_015_...xlsx: no 'Outline Number' column —
this export does not carry a document outline
```

recon 輸出佐證：`sections: {}`、`distinct_sections: []`、
`data/recon_leaf_to_section.tsv` 僅存表頭列、無資料列。

### 為何 recon 未因此中止

037 **無 citation 欄**（`citation column: NOT FOUND`），故
`distinct sections cited by the leaves = 0`。`build_outline_map` 之
docstring 已預期此情形：

> a feature that never cites document sections must not be blocked by a
> lookup it does not use

零引用 → 空 map 無對象可比對 → 不構成 miss（`outline_misses: []`）。
**故本條不觸發 01 包 §6 之「spec_id → outline 有無法解析之項」** ——
無「項」可解析，非「項」解析失敗。二者須分辨，登記於此以免日後誤讀。

### 何以仍須登記 —— Phase 4 之實質阻塞

`feature.yaml` 之 `spec_reference_template` 為：

```yaml
spec_reference_template: "<Spec Filename>_{outline}"
```

Phase 4 生成 `spec_reference` 欄時需要 `{outline}` 之值。其來源本應是
outline map，而該 map 為空且**現行工具無任何路徑可為 spec_mode D 建立它**。
亦即：recon 全綠，但 Phase 4 一定撞牆。

此為典型之**延遲失效**：缺陷在 Phase 1 完全不顯現，要到 Phase 4 才爆，
且屆時已投入生成成本。與本 feature 既有之靜默失效系列同屬 canon §5a
射程，但時間差更長。

### 處置 —— 執行層首版兩案**皆非正解**，經 01R §3 更正

**首版提案（保留為軌跡）**：(a) `recon.py` 增 spec_mode D 路徑自 CFTS docx
解析章節；(b) 改 `spec_reference_template`。

**01R §3 之更正，執行層複驗後接受**：

- **(a) 不可行，且理由比「工具缺路徑」更根本。** `survey_a03()` 之 citation
  欄尋找為 `find("hmi source")` → `find("source", forbid=("description",
  "requirement id"))`。本件 037 之來源欄表頭為 `Source System Requirement ID`，
  含 `requirement id` 故被 forbid 排除。**即 `citation column: NOT FOUND`
  不是解析失敗，是本 037 根本不含文件章節引用** —— 它引用的是 SYS-RA
  需求 id，不是 spec 章節。縱使把 CFTS docx 解析成完整章節索引，**仍無任何
  欄位能把 leaf 接到章節上**。首版建的是索引的一端，缺的是連結本身。
- **(b) 為時過早** —— 在確認 `{outline}` 真接不上之前就改 template，
  等於放棄可追溯性。

**首版失誤之定性**：兩案都只看「map 是空的」這個表象，未回頭問「即使 map
不空，leaf 憑什麼接得上」。與 A-TM09 首版同型 —— **未追問連結是否存在，
逕自處理連結的一端。**

### 正解 —— 第三案：經 SYS2 之 Source Requirement items 欄建錨鏈

```
SWE-RA-TIME&DATE-nnn → SYS-RA-TIME&DATE-nnn → CFTS 物件 id → CFTS 章節號
   （037 第 2 欄）        （SYS2 第 2 欄）      （SYS2 第 5 欄）  （docx 標題 {id}）
```

**執行層已對 `inputs/` 之原始 docx 與 xlsx 實測**（非沙箱轉換副本），
六項數字與 01R §3.1 逐項相符，詳見上繳包 `01R_corrections.md` §2。
可達 21 節，71 筆直接可達 + 5 筆多物件（切分後全數可達）+ 2 筆真缺口
（A-TM13）。

**處置意見（待 Pei）**：`spec_reference_template` 暫不改；`recon.py` 之
修法應為「增一條 leaf→章節之間接解析路徑（經 SYS2 來源物件 id）」，
非「增 docx 章節解析」。本 feature 可先以獨立腳本產出
`data/leaf_to_section.tsv`，不動 `recon.py` —— 該路線不需 Tier 2，
Phase 4 亦不必等腳本修法。

---

**降為非阻塞（2026-08-21，依 R-TM40）**

spec_reference 之取值改為 `CFTS015-{Source Requirement item id}`，
止於物件 id，不再需要「物件 id → 章節號」之 docx 解析。
故本條由「B1 之欄位內容阻塞」降為**非阻塞**，其 recon.py 修法
（R-TM19 階段三）不再是 B1 之前置。

錨鏈工作不作廢：`data/leaf_to_section_probe.txt` 仍為 framework
Layer 3 主軸章節表之依據，亦為 R-TM23 兩條界線之 spec 依據。
改變者為其角色 —— 由交付欄位之來源，改為 framework 導航之依據。

## A-TM13 — 2 筆被引用之需求，其來源物件不在 CFTS 基線內

**狀態：PENDING。Tier 2，RD-1 候選。** 由 01R §4 指派登記。

### 實測（執行層對 `inputs/` 原始檔複驗，與 01R 相符）

| SYS-RA id | SYS2 第 5 欄之來源物件 id | 於 CFTS docx 之出現次數 |
|---|---|---|
| `SYS-RA-TIME&DATE-221` | `6151328` | **0** |
| `SYS-RA-TIME&DATE-224` | `6151331` | **0** |

全檔搜尋 `615\d{4}` 形態：**零命中**（執行層獨立複驗，相符）。

被引用之路徑：221 ← `SWE-RA-TIME&DATE-005`（Internal Clock Accuracy）；
224 ← `SWE-RA-TIME&DATE-002`（GPS Sync Enable/Disable Logic）。

SYS2 描述節錄：221 為 `$GPS_Presence$ = [Absent]` 時之內部時鐘精度；
224 為 `$GPS_Presence$ = [Present]` 時之個人化設定。

### 性質

**非解析缺陷，是基線缺口** —— SYS2 引用了現行 CFTS 版本
（SR26 `20250909-1851`）所不含之物件。可能為 SYS2 較新、CFTS 較舊，
或物件遷自他份 CFTS。與 A-TM02a（037 版本身分）同屬「上游版本對齊」
一族，宜併入 RD-1 一次問。

### 對 TC 之立即影響

`SWE-RA-TIME&DATE-005` 與 `-002` 兩個 leaf 之 `specification_reference`
在該兩筆上**無章節可寫**。

**不得以鄰近章節填充** —— §8.4.1 禁止捏造來源未述之值。兩 leaf 之其餘
引用仍有章節可寫，故非整條 leaf 阻塞；缺的是該兩筆之對應。

### 執行層補充實測（01R 未提，不推翻其結論）

01R §4 稱「CFTS015 全篇之物件 id 皆為 `481xxxx` 區段」。執行層全檔實測
相異 7 位數 id 之前綴分佈為：

| 前綴 | 相異 id 數 | 性質 |
|---|---|---|
| `481` | **358** | 需求物件（標題 88 + 物件行 270） |
| `456` | **3** | **`WrapperResource`（內嵌 RTF 資源）**，非需求物件 |

三筆為 `4561062` / `4561063` / `4561064`，行文形態為
`4561062- CFTSMV015_CIP_R1_O833_116_inline.rtf WrapperResource`。

**此不推翻 A-TM13**：`456xxxx` 非需求物件，`615xxxx` 仍為零命中，
結論不變。登記之理由是**判準精確性** —— 若日後有人以「全檔 7 位數 id
集合」作為物件全集（361），會比真實物件數（358）多 3，且該誤差不會報錯。
物件全集之正確取法為「標題 `{id}` ∪ 物件行 `^\d{7}:`」，非「全檔 id 掃描」。

**下游影響（2026-08-20，執行層 02 上繳 §4.3 之發現）**

本條之影響不限於 `spec_reference` 欄無章節可寫，亦使受影響 leaf 之
**章節證據殘缺**，連帶降低 framework 檢驗之效力：

| leaf | `#SYS-RA` | 可解析出之章節數 | 缺口來源 |
|---|---|---|---|
| `SWE-RA-TIME&DATE-005` | 2 | 1 | `SYS-RA-221` → 物件 `6151328` 不在 CFTS 基線 |
| `SWE-RA-TIME&DATE-002` | 6 | 4 | `SYS-RA-224` → 物件 `6151331` 不在 CFTS 基線 |

即 005 之章節證據僅一半可用。framework 檢驗時若據其判定歸組，
係據殘缺樣本而為 —— 02R §2.1 之定案改以 leaf 描述之語意軸為據，
不依賴該殘缺章節證據。

---

## A-TM14 — FORMS.md 引用之 Home v2 交付件不在磁碟上

**狀態：PENDING。Tier 2。** 由 `01Z-A1_amendment.md` §4 指派登記。

```
A-TM14（PENDING，Tier 2）—— FORMS.md 引用之 Home v2 交付件不在磁碟上

FORMS.md 之 instance register 與 provenance warning 均以
features/home/output/…_Home_20260720.xlsx（SHA cfc007f3…、
tag fw036-home-regen-v2）為 Home 之權威交付件，並以之為判定
archive 內 Home 複本受污染之比對基準。

實測（2026-08-20）：features/home/output/ 目錄不存在。

後果有二，須分開處置：
1. 對本 feature —— R-TM10 之樣式參照無來源可用（見 R-TM10-A1）
2. 對 repo —— FORMS.md 之 provenance warning 其比對基準已不可覆驗。
   該 warning 所述之四項差異目前無法被任何人重新驗證，
   只能作為歷史記載引用，不得作為現行判準。
   此與 A-UP03／A-UP05 同形態，為第二例。

不建議之處置：以 archive 內之 Home 複本替代基準 —— 那正是被判定為
受污染的那一份，以受測物充當基準即失去比對意義。

建議之處置（待 Pei 裁）：確認該交付件是否仍存於他處
（交付路徑 /Users/peihe/Work/02_Project_R1LR/10_Reviewing/…）；
若確已不存，則 FORMS.md 相關段落須標註其基準不可覆驗，
比照 A-UP05 之處理方式。
```

### 執行層舉證（T2，2026-08-20）—— 「確已不存」成立

分析層之建議處置指定要查交付路徑。**已查，逐項如下。**

**(1) 目錄層級**

```
ls -d features/home/output   →  ABSENT
```

`features/home/` 內容：`.gitignore` / `ANOMALIES.md` / `DECISIONS.md` /
`PLAYBOOK.md` / `RECON.md` / `RUNBOOK.md` / `data` / `docs` /
`feature.yaml` / `generated` / `scripts` —— **無 `output/`，亦無 `inputs/`**。
與分析層實測相符。

**(2) 檔名搜尋 —— 三個獨立方法，全部 0 命中**

| 方法 | 結果 |
|---|---|
| `command find`（繞過 shell function） | 0 |
| Python `os.walk` 獨立實作 | 0 |
| **陰性對照**：同一掃描找「含 `Home` 之 xlsx」 | **35 筆** |

第三列為**必要之陰性對照**：證明掃描確實有效、非空掃。
本 shell 之 `find` 為 Claude Code 包裝之 `bfs` function（非系統 `find`），
故不以其單一結果為據 —— 此為 R-TM7 精神之延伸（不假設工具行為）。

**(3) SHA256 全域比對 —— 檔名可能已變，故不依賴檔名**

掃描 `/Users/peihe/Work` 與 `/Users/peihe/Work_Projects` 下**全部**檔名含
`036` 或 `SWQT` 之 xlsx，共 **150 筆**，逐一計算 SHA256 並比對
FORMS.md 所載之 `cfc007f3…`：

```
SHA256 前綴 cfc007f3 命中：0 筆 / 150
```

**此為決定性證據**：縱使該檔被改名，其內容亦不存在於上述兩個根目錄下。

**結論：A-TM14 之「確已不存」成立。** 依分析層之建議，FORMS.md 相關段落
應標註其基準不可覆驗，比照 A-UP05。**該標註屬 `forms/` 之修改，跨 feature，
執行層未動。**

### 執行層額外發現（T2 附帶，分析層未知）

**交付路徑存在一份 Home 工作簿，與 archive 那份同名但內容不同。**

| | 交付路徑 | archive |
|---|---|---|
| 路徑 | `…/10_Reviewing/00_TestCase/ASW-R2/Core HMI/HomeHMI/` | `archive/forms_superseded/` |
| 檔名 | `…_SWQT_Home_20260809.xlsx` | `…_SWQT_Home_20260809.xlsx`（**同名**） |
| SHA256 | `469b2f6d346d0b1ddd8c86b597760c60a643b3a6beab2036a358b1e288f6c3df` | `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72` |
| bytes | 120,639 | 119,885 |
| mtime | 2026-08-19 12:01 | 2026-08-09 22:22 |
| `cmp` | **differ: char 2534, line 3** | |

**兩份同名、不同內容、相差 754 bytes、mtime 差 10 天。**

意義有三，均**登記不裁**：

1. **FORMS.md 之 provenance warning 其受測物身分本身即有歧義** ——
   該 warning 描述「archive 內之 Home 複本」有四項污染，但磁碟上有兩份
   同名檔案。warning 所測者為何份，現無從得知。此使 A-TM14 之問題
   **比分析層所述更深**：不只基準（v2）不可覆驗，**受測物亦不唯一**。
2. **交付路徑之該份為 R-TM10-A1 解除條件 (b) 之潛在候選** —— 但
   R-TM10-A1 明文禁止者為 `archive/` 之那份，交付路徑此份**未被提及**
   （分析層不知其存在）。**執行層不自行認定其可用**：它既非 v2
   （SHA 不符 `cfc007f3…`），亦不能因「不是被禁的那一份」就推定乾淨。
   **解除須 Pei 裁。**
3. 同一目錄另有 `FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx`
   —— 其**檔名**即 R-TM9 所稱之正確形態 `…Home-HMI-V0.1`，構成前綴段
   之獨立第二樣本。詳見上繳 §3.2。

**本節全部為登記，執行層未複製任何檔案進 `inputs/`，未援引任何樣式，
未組 D5 值。**

**補充（2026-08-20，01Z 上繳 §2.2）—— 受測物身分亦不可判定**

除基準（Home v2）不存在外，磁碟上另有**兩份同名之 Home 036 複本**：

| | 交付路徑 | `archive/forms_superseded/` |
|---|---|---|
| 檔名 | `…_SWQT_Home_20260809.xlsx` | `…_SWQT_Home_20260809.xlsx`（同名）|
| SHA256 | `469b2f6d346d0b1ddd8c86b597760c60a643b3a6beab2036a358b1e288f6c3df` | `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72` |
| bytes | 120,639 | 119,885 |
| mtime | 2026-08-19 12:01 | 2026-08-09 22:22 |

`cmp` 報 differ: char 2534, line 3。

故 FORMS.md provenance warning 所述之四項污染，**其受測物為哪一份現已
無從得知**。損害範圍因此擴大：不只基準不可覆驗，被判定受污染者是哪一份
亦不確定。

不得以任一份充當基準 —— 以受測物充當基準即失去比對意義。

---

## A-TM15 — `recon.py` 整份重寫 `DECISIONS.md`，沖掉執行層之裁決引用段

**狀態：PENDING。重建屬 Tier 1（已執行）；修法屬 Tier 2（未動）。**
執行層登記。**本條同時記錄執行層自身於 01 包之一項未察覺失誤。**

### 成因

`recon.py:294` 之註解自陳：

> recon.py rewrites DECISIONS.md whole. That is fine for an unsigned sheet

實測確認：本檔僅在**已簽核**時才受保護（改寫入 `DECISIONS.new.md`，
`recon.py:302-304`）。未簽核者整份重寫，無備份、無警告、無提示。

### 與流程要求直接衝突

三個下放包均要求執行層於 `DECISIONS.md` 建裁決引用條目：

| 包 | 要求 |
|---|---|
| `00_intake_scaffold.md` §4(1) | 「於 `DECISIONS.md` 以 `[PEI]` 條目引用」 |
| `01_recon.md` §1 | 「執行層須…於 `DECISIONS.md` 建 `[PEI]` 條目引用」 |
| `01Z-A2_command_set.md` T5(4) | 「`DECISIONS.md` 建對應條目」 |

**但 `01_recon.md` §5 又要求跑 `recon.py`** —— 該步驟必然沖掉前一步寫入
之引用條目。**兩項要求在同一個下放包內互相抵銷**，且失敗形態為靜默：
recon 只印 `DECISIONS.md written.`，不提示其覆寫了什麼。

### 執行層之失誤（如實記錄）

執行層於 01 包**先寫 §0 裁決引用與 §1 Intake 詳細內容，後跑 recon**，
未於 recon 後複查該檔，故未察覺內容已被沖掉。

01 包上繳 §5 所稱「`DECISIONS.md` §2 / §3 已由 recon 結果填實」字面無誤
（recon 確實填了），但**遺漏了「先前寫入之 §0 與 §1 詳細內容已消失」
這件事** —— 該陳述因而在整體上造成誤導。

**失誤性質**：寫入後未複查。與 A-TM09 首版（未驗證解析正確性）、
A-TM12 首版（未驗證連結存在性）同族 —— **完成一個動作後，未確認該動作
之結果仍然成立**。前兩例是未驗證前提，本例是未驗證後果。

**發現時機**：本包 T5(4) 欲更新 `DECISIONS.md` 時，`str.replace` 之目標
字串不存在，替換靜默失敗（`grep` 無輸出）而暴露。**若非本包恰好要改同
一處，此事不會被發現。**

### 處置

**已執行（Tier 1）**：於 `DECISIONS.md` 重建 §0 裁決引用段，並在該節
開頭以區塊引言標示本條之警告與「每次重跑 recon 後必須手動補回」。
同時於該節列出 recon 之 `[AUTO]` 預填值與既有裁決之**四項覆寫關係**
（`test_group` / 覆蓋分母 / exemplar source / spec_reference），
使兩者並存時不致誤讀。

**未動（Tier 2）**：`recon.py` 之修法。可能方向：

1. 保留手工節區 —— 以標記（如 `<!-- MANUAL -->`）圈出不重寫之區段
2. 覆寫前備份為 `DECISIONS.prev.md`，並於輸出提示
3. 至少在輸出訊息中列出被覆寫之節名，使其非靜默

**權威來源之提醒**：條文全文之權威在 `RULINGS.md`，該檔**不受 recon
影響**，故本次無條文遺失。`DECISIONS.md` 之 §0 僅為引用索引。
此為損害有限之唯一理由 —— 非因流程健全。

---

## A-TM16 — Home A-H26 之既有定性可能低估

**狀態：PENDING。Tier 2。屬 Home，非本 feature —— 僅登記供 Home owner 覆核。**

Home 之 A-H26 於既有文件中記為「Scope 欄未修正」。依 `docs/handoff/
01Z-A3_review.md` §3 之實測，該欄之語意為 037 文件識別，而 Home 工作簿
之 D5 值為：

    FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告

該值指向 AppDrawer-Projection 之 037，即**另一個 feature 的追溯來源**；
且其 `SWE1HMI` 形態不對應交付路徑上任何實存檔名（三個實例一致為 `HMI`）。

若此讀法成立，A-H26 不是標籤筆誤而是追溯來源指錯文件，其嚴重性與既有
記載不同。

證據：交付路徑三個 feature 之 037 檔名形態一致
（`Home-HMI-V0.1` / `AppDrawer-HMI-V0.1` / `PersonalAccount-HMI-V0.1`）。

執行層 01Z 上繳 §3.1 所取得之 D5 `repr()` 原樣，保留為本條之證據，
不因 T3 切分作業作廢而刪除。

### 執行層取得之 `repr()` 原樣（歸屬由 01Z §3.1 移入本條）

```python
row5 col3: '範圍 Scope：'
row5 col4: 'FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告'
row5 col9: '日期 Date：2026'
row5 col33: 'FM-WI-FSM-036-A01'
```

來源：`archive/forms_superseded/…_SWQT_Home_20260809.xlsx`
（SHA `1895fb2a…`），分頁 `Test Case Specification&Result`（rev A/B 版面）。
無前後空白、無換行。

**注意該值取自 archive 之複本，而 A-TM14 已載明磁碟上有兩份同名檔案、
內容相異。** 故本條之證據僅能證明「archive 那一份的 D5 是這個值」，
不能證明 FORMS.md provenance warning 所述者即此份。此限制須與本條並讀。

**（2026-08-20）執行層以純目錄列舉獨立複驗三個 037 檔名，與分析層實測相符。
本條之檔名形態論證自此為雙方確認，非單方實測。**

本 feature 之處置已由 R-TM9-A2 涵蓋，本條不影響本 feature 之任何動作。

---

## A-TM17 — repo 內有身分不明之併行寫入者

**狀態：PENDING。Tier 3 —— 呈報 Pei。** 由 `03R_review.md` §3 指派登記。

```
A-TM17（PENDING，Tier 3 —— 呈報 Pei）—— repo 內有身分不明之併行寫入者

三個獨立事實，時序相連：

1. （01Z-A3 §6 已報，Pei 未回覆）features/vehicle_setting/ 於 session
   開始時整個 untracked，其後除 docs/handoff/02_coverage_baseline_
   correction.md 外似被 add 過。本 session 未動 git。
2. features/vehicle_setting/ANOMALIES.md mtime 16:51:28、data/ 16:49，
   落在本 session 期間；本 session 未寫入該目錄任何檔案。
3. features/vehicle setting/（含空格）於 R-TM18 指派前已從磁碟消失，
   非 mv 至 archive，全 repo 零命中，git 從未追蹤故不可復原。

三者可能同源。分析層與執行層皆未執行任何刪除或 git 操作。

在併行者身分與作業範圍釐清前：
- 不對任何跨 feature 共用檔（scripts/、docs/fw036/、docs/runtime/、
  forms/）執行寫入以外之破壞性操作
- 不對 features/vehicle_setting/ 執行任何寫入或腳本實跑
- 腳本修法 HOLD（見 R-TM22）

呈報 Pei 之具體請求：確認另一 session 之身分與作業範圍；確認
features/vehicle setting/ 之刪除是否為其所為（若是，事件關閉為已知；
若否，則 repo 有未受控之刪除行為，須先查明再繼續）。
```

### 執行層補充：第 4 項事實（git race，本 session 實測）

本 session 執行 `git add features/time_management/` 後、`git commit` 前，
他方執行了 commit。結果：

| | |
|---|---|
| commit | `554079e`，標題 `feat(vehicle_setting): rounds 02-03 …` |
| 內含 | **25 個 `time_management` 檔 + 12 個 `vehicle_setting` 檔** = 37 檔 |
| 本執行層之 commit message | **未進入 git**（`git commit` 回報 `nothing added to commit`）|
| 內容完整性 | 已驗：R-TM 16 條、A-TM 16 條、`test_group` 正確、上繳 333 行皆在該 commit 內 |
| push 狀態 | 未 push（`ahead 7`），歷史理論上可重寫 |

**執行層未自行修復**：修復須重寫歷史，而併行者狀態未明時重寫會破壞其
工作；且該 commit 不屬本 feature。已呈報 Pei，未獲指示，維持現狀。

**與上列第 1–3 項之關係**：本項為第 1 項之後續實例，同一形態
（他方之 git 操作與本 session 交錯），可作為釐清併行者身分之時間錨點
（`554079e` 之 commit 時間即其活動時點之一）。

### 歸屬結案（2026-08-21，R-TM44）

```
R-TM44（Pei, 2026-08-21）—— features/time_management/ 由本 session 續持
```

Pei 裁定 `features/time_management/` 由本 session 續持，**本條轉 RESOLVED**。

直接後果四項（R-TM44 逐字，見 `RULINGS.md`）：`scripts/` 解凍；
現存三支腳本為工作基底且**不因來源而降低其地位**（依 G-TM2 逐項修正，
非整檔重寫）；快照保留不刪；併行寫入風險由 Pei 於另一端停止作業消除。

**本條之事實記載不因結案而變**（R-TM13）：09:13–09:14 之覆蓋確曾發生，
執行層原產出之兩份確已失落無備份。結案的是歸屬，不是事件。

### 結案（2026-08-20）

```
A-TM17 —— RESOLVED（Pei, 2026-08-20「A-TM17是」）

Pei 確認：併行寫入者為 Pei 自己開啟之另一 session；
features/vehicle setting/ 之刪除為其所為。三項登記事實均已解釋，
repo 無未受控之刪除行為。

保留之限制（理由改變，限制不變）：features/vehicle_setting/ 仍不列為
回歸受測物，且不對其寫入或實跑腳本 —— 理由不再是身分不明，而是
併行編輯使量測失去鑑別力（受測目錄同時被他方寫入時，diff 有輸出
無法區分成因，R-TM21 同一判準）。屬技術限制。
```

**A-TM01 之 MOOT 不因本條改變** —— 標的確已滅失、R-TM18 確實未能執行，
事實記載不隨成因解釋而變（R-TM13）。

**第 4 項事實（git race）之殘留**：`554079e` 內 25 個 `time_management`
檔仍掛於標題為 `feat(vehicle_setting)` 之 commit 下，本執行層之 commit
message 未進入 git。內容完整、未 push、歷史仍可重寫。**該項屬 git 歷史
之整理，非本 feature 之技術債，執行層未自行處置，待 Pei 決定。**

---

## A-TM18 — Comfort 之 framework 僅存本地、未併入全域檔

**狀態：PENDING。Tier 2。屬 Comfort，非本 feature —— 僅登記供 Comfort owner 覆核。**
由 `03Z_closure.md` §1.2 指派登記。

```
A-TM18（PENDING，Tier 2 —— 屬 Comfort，非本 feature）

features/comfort/framework.md 存在，而 docs/fw036/framework.md
無 Comfort Part。故 Comfort 之 framework 僅存於本地，與其餘六個 feature
之作法不一致。

兩種可能，本包不判定：
(a) Comfort 仍在進行中，尚未併入全域檔 —— 則屬正常中間狀態
(b) Comfort 採本地檔為最終形態 —— 則全域檔非唯一位置，R-TM16 之
    依據 3（Part I 跨領域裁決之拘束）在 Comfort 亦未生效

本條僅登記，不裁 Comfort 之事。供 Comfort owner 覆核。
本 feature 之處置不受影響：Part VII 已併入，位置正確。
```

### 緣起

本條源於執行層於 `03R` 上繳 §5.6 之提請：R-TM16 依據 2 為全稱斷言
（「一例也沒有」），而全稱斷言被單一反例推翻，驗證成本卻只有一道指令 ——
成本與風險不對稱。分析層即刻補驗，反例確實存在。

R-TM16 之依據訂正見 `RULINGS.md` 該條末節；**其結論（本 feature 併入
全域檔）不變**，因依據 1 與依據 3 未受影響。

---

## A-TM19 — `intake.py` 之 A-TM10 衝突訊息未進 `INTAKE.md`

**狀態：PENDING。Tier 2 —— 併 A-TM12 之腳本批次修，不單獨開包。**
由 `04_scripts.md` §7 指派登記。

```
A-TM19（PENDING，Tier 2 —— 併 A-TM12 批次修）

intake.py 之 A-TM10 衝突訊息只印 stdout（`CONFLICT (A-TM10): ...`），
未進 INTAKE.md。成因為結構性：INTAKE.md 由 report() 產出，而衝突發生於
scaffold()，兩者無共用資料結構。

執行層之偏離處置正確（不硬塞）。但 stdout 訊息在自動化流程中會遺失，
而 INTAKE.md 是該資訊之正確歸屬地。

建議修法（隨 A-TM12 之腳本批次一併做，不單獨開包）：scaffold() 將
conflicts 寫入 intake.json，report() 讀取後渲染入 INTAKE.md。
```

### 緣起

本條源於執行層於 `03Z-A1` 上繳 §4.3 之主動提請：A-TM10 之修法要求
「於 `INTAKE.md` 註明衝突」，但 `report()` 與 `scaffold()` 無共用資料
結構，硬塞會製造第二個問題。執行層改印 stdout 並提請 —— 分析層確認
該處置正確，另立本條記錄殘留缺口。

**待修者為「歸屬地」而非「功能」**：衝突偵測本身已運作（守衛已就位，
不覆寫真實路徑），缺的是其記錄落在正確的檔案裡。

---

## A-TM20 — 併行者寫入本 feature，兩支腳本被覆蓋且內容失落

**狀態：PENDING。Tier 3 —— 呈 Pei，分析層明言不裁。**
由 `04R_review.md` §5 指派登記。

```
A-TM20（PENDING，Tier 3 —— 呈 Pei，本包不推進）

A-TM17 已 RESOLVED（Pei 確認併行者為其自己開啟之另一 session），
但當時三項登記事實之作業範圍皆在 features/vehicle_setting/。

本次為首次觀察到併行者寫入 features/time_management/：

| 腳本 | 執行層所寫 | 現存 | 特徵字串 `Structure ported from` |
|---|---|---|---|
| write_back.py | 351 行，英文 | 214 行，中文 | 0（非執行層）|
| lint_tcs.py | 312 行，英文 | 301 行，中文 | 0（非執行層）|
| build_batch_context.py | 222 行，英文 | 222 行，英文 | 1（執行層）|

覆蓋發生於 09:13–09:14。執行層之兩份內容已不存於磁碟，無備份。

推定（未證實，須 Pei 確認）：Pei 於另一 session 對同一 feature 指派了
相同或相近之工作。

本條不由分析層裁定 —— 「哪一個 session 擁有 features/time_management/」
是資源分配問題，非技術判斷，只有 Pei 能答。

在 Pei 裁定前之保全措施（分析層逕行，逆轉成本為零）：
  - features/time_management/scripts/ 凍結：不寫入、不覆蓋、不修改任一行
  - 對該目錄之作業一律唯讀
  - 分析層不再下放任何寫入 scripts/ 之指令
```

### 執行層回報（2026-08-21）

**凍結已遵守**：本包對 `scripts/` 之全部動作為唯讀（`cat` / `grep` /
`wc`），未寫入、未覆蓋、未修改任一行，未執行任一支。
`git status --short features/time_management/scripts/` 之輸出見上繳 §5。

**分析層 §5 對第 3 點之補強，執行層接受**：不能預設我方版本較好。
Pei 之偏好明載程式碼註解用繁體中文，現存中文版在該點上更貼近；
四項缺口是客觀可查之缺漏，但那不等於整份較差。

**執行層補一項本條未載之事實**：`build_batch_context.py` 為執行層所寫
且**未被覆蓋**，其內已含 `SPEC_GAP` 與 `BOUNDARIES` 兩表。即三支腳本
現為**混合來源**，非單一 session 之產出。日後若採整檔取代，須注意該支
之歸屬與另二支不同。

---

## A-TM21 — 現存 `write_back.py` / `lint_tcs.py` 六項實質缺陷

**狀態：PENDING。Tier 2 —— 凍結中不修，登記待歸屬裁定（A-TM20）。**
由 `04Z_closure.md` §2 指派登記。發現者為執行層 `04R` T4 之唯讀全文評估。

```
A-TM21（PENDING，Tier 2 —— 凍結中不修，登記待歸屬裁定）

features/time_management/scripts/ 現存之 write_back.py（214 行）與
lint_tcs.py（301 行）經唯讀全文評估，六項實質缺陷：

(a) resolve_columns() docstring 承諾表頭複驗與不符即 raise，
    實作只讀 feature.yaml 之字母，ws / header_row 兩參數未使用。
    —— docstring 承諾而實作沒有，靜默失效第六例
(b) check_other_sheets() docstring 稱「逐位元相同」，實作只比對 zip
    member 名稱集合，內容被改寫而名稱不變則全綠。
    —— 同上，第七例
(c) TC_ID_FORMAT 為模組常數（None）且不讀 feature.yaml。R-TM32 已裁定
    且值已入 feature.yaml:49，write-back 仍會被 unresolved 檢查攔死
(d) write_rows() 不寫 tc_id；feature.yaml 之 columns 亦無 tc_id 鍵。
    合 (c) 即「Test Case ID 欄永遠不會被寫入」
(e) CONST_FUNCTIONAL_SAFETY 為死碼 —— 僅出現於定義與 unresolved 檢查，
    write_rows() 內未使用，填值亦不會進工作簿
(f) lint_required_fields() 只檢查鍵存在不檢查是否為空；base_tc() 為
    全空字串，故一條所有欄位皆空之 TC 會全綠通過

另一項強度差異（非缺陷，§3.6）：read_design_methods() 遍歷整個
`下拉選單` 分頁收詞彙，僅檢查非空。FORMS.md 實測 DV 來源為 $A$1:$A$9
恰九條；現實作讀到 8 條或 10 條皆不報錯。

(a)(b)(f) 為讀碼推得，凍結期間未實跑證實（04R §4.3 項 2）。
```

### 分析層之補充判讀（`04Z` §2，執行層照錄）

> (a) 與 (b) 是同一形態，且是最嚴重的兩項……**讀 docstring 的人會以為
> 保護存在。這比「沒有保護」更危險 —— 沒有保護時，下一個人會去加；
> 假裝有保護時，沒有人會去加。**

> (c)+(d) 合起來是一個完整的斷鏈：三處各自看都像小問題，合起來是
> 「Test Case ID 欄永遠不會被寫入」。

### 處置

**凍結中不修**（A-TM20）。必修項與不得回退項見 **G-TM2**（十二項）。
`feature.yaml` 之 `tc_id` 欄位對映已由 R-TM34 補入（不在凍結範圍），
為 (d) 之其中一環，但實際寫入仍待 (c)(d) 修畢。

**現存版之三項優點須保留**，見 G-TM2 項 6–8 —— 其中
`lint_spec_reference` 之物件 id 存在性閘門為**被覆蓋之執行層版本所無**，
不得因整檔取代而回退。

### (b) 降級（2026-08-21，依 `04Z` 上繳 §5 之 verify_structure 評估）

```
**(b) 降級（2026-08-21，依 04Z 上繳 §5 之 verify_structure 評估）**

check_other_sheets() 所指之保護**實際存在**，由
backend/xlsx_surgical.py:268-275 之 verify_structure 第三層提供，
且較 docstring 所承諾者更嚴格（逐 member 位元組比對 `a.read(m) !=
b.read(m)`，且限定僅 patched 之 member 得有差異）。

故 (b) 由「保護缺失」降為「docstring 與實作不符」。
處置隨之由「補實作」改為「移除該函式」（G-TM2 項 2 訂正）。

**(a) 不隨之降級** —— resolve_columns() 之欄位對映無任何其他機制涵蓋：
verify_structure 保護檔案結構，不驗欄位對映是否取對。寫入落在錯欄時，
錯欄仍在目標分頁內屬 patched，結構檢查全綠。
```

### (d) 嚴重性提高（2026-08-21，依 `04Z-A2` 上繳 §1）

```
**(d) 嚴重性提高（2026-08-21，依 04Z-A2 上繳 §1）**

原記為「F 欄不會被寫入」。經 canon §10.3 末句
（`the generator handles assignment, the LLM does not emit tc_id`，
ASPICE_SWE6_AI_Instruction.md:521-525）確認，本項尚多一層：
修法若照最直覺路徑做（讓 TC JSON 攜帶 tc_id 並由 tc.get(key) 取），
會引入一個**違反 canon 的新缺陷**。處置見 G-TM2 項 3 訂正。
```

---

## A-TM22 — `verify_structure` 三層全為反向驗證，member 層對映錯誤不可偵測

**狀態：PENDING。Tier 2 —— B1 生成前必決。**
由 `04Z-A3_positive_verification.md` §3 指派登記。
發現者為執行層 `04Z-A2` 上繳 §5.3 項 1。

```
A-TM22（PENDING，Tier 2 —— B1 生成前必決）

backend/xlsx_surgical.py 之 verify_structure 三層全為反向驗證
（不該變的沒變）：
  第一層 zip member 名稱集合未增減
  第二層 DV 計數（classic / x14）未變
  第三層 逐 member 位元組比對，僅 patched 者得異

**無一層驗證正向**（該變的變對了地方）。若 sheet_members() 之
sheet 名 → zip member 對映錯誤，寫入會落在另一分頁之 member，
而該 member 恰在 patched 之列，三層全綠。

與 A-TM21(a) 同構（欄位對映錯 → 結構檢查全綠），發生層級不同：
前者 column 層，本條 member 層。

sheet_members() 與 diff_cells() 尚未讀（04Z-A3 T3 指派）。
本條之嚴重性須待該二函式讀畢方能定級 —— 若 sheet_members() 之對映
有自身之正確性保證，本條降為理論風險；若無，則為實質盲區。
```

### 兩層盲區之並置（`04Z-A3` §3，執行層照錄）

| 層 | 對映 | 錯了會怎樣 | 現有檢查 |
|---|---|---|---|
| column | `feature.yaml` 字母 → 實際欄 | 寫進錯欄，仍在目標分頁內 | 全綠（A-TM21(a)）|
| member | `sheet_members()` sheet 名 → zip member | 寫進錯分頁，該 member 在 patched 內 | 全綠（A-TM22）|

**兩者皆非「保護失效」，而是「該方向根本沒有檢查」。**

### 定級（執行層，依 `04Z-A3` T3 讀畢後判定）

見上繳 `04Z-A3_corrections.md` §3.3。

### 處置

**G-TM3**（寫回後須有正向驗證）為本條之對策，與 G-TM1 / G-TM2 並列為
B1 前閘門。凍結中不實作。

---

## A-TM23 — CFTS015 兩套物件編號並存，工作簿採 7 位家族而文件無此寫法先例

**狀態：PENDING。Tier 2 —— 交付件可讀性。**
由 `04Z-A5_numbering_correction.md` §4.1 指派登記。
**緣起為 Pei 於聊天層之質疑**（「CFTS015 編號不都是 7 位數字嗎？」），
分析層實測後發現其 R-TM40 之依據取錯類別。

```
A-TM23（PENDING，Tier 2 —— 交付件可讀性）

CFTS015 內存在兩套並存且可互相對應之物件編號：

  短號家族：CFTS015-732 … CFTS015-1639（26 個相異值，僅見於修訂註記）
  7 位家族：4813898 … 4814253（270 個相異值，全篇正文與章節標題）

對應實例：物件 4814185 之內文含 `CFTSMV015_CIP_R1_O922_118_inline.rtf`，
其次一物件 4814186 稱 `CFTS015-922` —— 短號 922 即 7 位 4814185。

R-TM40 採 7 位家族（SYS2 `Source Requirement items` 欄之值）。
`CFTS015-<7 位>` 之寫法於 CFTS015 全文出現 **0 次**，
故為本專案新定之形式，非沿用文件既有慣例。

風險：審閱者若見工作簿之 `CFTS015-4814185` 而在文件中搜尋
`CFTS015-4814185`，將零命中；須改搜 `4814185`。反之若見文件之
`CFTS015-922` 而在工作簿中搜尋，亦零命中。**兩套編號在字面上不互通。**

處置提請（Tier 2，待 Pei）：
(a) 維持現狀，並於工作簿 Remarks 或交付說明註明編號家族；或
(b) 改用短號家族 —— **不可行**，SYS2 不提供短號，且短號僅 26 個
    相異值涵蓋不到全部 270 個物件；或
(c) 於 RD-1 併問上游該參照體系之期望寫法

分析層建議 (a) + (c)：先照 R-TM40 執行不阻塞 B1，同時於 RD-1 併問。
```

### 執行層補充：本條與 A-TM13 之交會

A-TM13 之兩個 BLOCKED 物件（`6151328` / `6151331`）為 **`615xxxx` 區段**，
既不屬短號家族亦不屬本檔之 `481xxxx` 7 位家族。即 SYS2 引用了**第三個
區段**之物件 id。

此使 A-TM23 之「兩套編號」描述在嚴格意義上不完整 —— 就本 feature 之
資料而言，**SYS2 側可見三個區段**：`481xxxx`（CFTS015 本文，270 個）、
`456xxxx`（WrapperResource，3 個，見 A-TM13 末節）、
`615xxxx`（不在 CFTS015 內，2 個）。

**不影響 A-TM23 之結論與處置**（其論述對象為「工作簿寫法 vs 文件寫法」
之不互通），但 RD-1 若依 (c) 併問，**宜一併問及 `615xxxx` 區段之歸屬**
—— 那與 Q-TM2 是同一個問題的兩面。

### 處置已定（2026-08-21，R-TM43）—— 轉 AWAITING_UPSTREAM

Pei 採 **(a) + (c)**：維持 7 位家族不阻塞 B1，並於交付說明註明兩套編號
不互通；同時於 RD-1 併問（**Q-TM4 已增列**，狀態 DRAFT）。
(b) 改用短號家族確定不採。

**本條由 PENDING 轉 AWAITING_UPSTREAM** —— 處置已定，答案待 RD-1 回覆。

**執行層提請**：(a) 之「交付說明」落點未指定（候選：工作簿 Remarks 欄 /
`docs/fw036/` 交付文件 / Part VII）。影響 B1 之 Remarks 設計，見
`RULINGS.md` R-TM43 之回報段。

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-TMnn]`.
