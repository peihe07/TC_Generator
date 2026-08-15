# 上繳包 09 — Part N 修正案 ＋ profile 簽署 ＋ G-1 ＋ A-CF07 備妥

執行層 → 分析層。2026-08-15。回應下放包 `14_partN_amendment.md` §5、
`15_profile_draft.md`、`16_profile_signed.md` §3（三包共用一次往返）。

**結論：五項作業全部完成。G-1 PASS（附 provenance 但書）。
A-CF07 備妥並停下，等 Pei 於 Excel 確認四項。Phase 4 未開始。**

> **與 `09_partN_amendment.md` 之關係**：14 §5 六項於 16 落檔前已執行完畢，
> 當時之上繳包為 `09_partN_amendment.md`。16 §3.3 指定本輪合併上繳為
> `09_partN_amendment_and_profile.md`，故本檔為該次往返之完整上繳；
> 前者保留為當時之紀錄（未刪 —— 它是準確的），其內容由本檔 §1 索引。
> 兩檔同以 `09_` 起首，若分析層認為應合併為一，回報即整併。

---

## 0. 置頂：三件需要分析層知悉的事

| # | 事項 |
|---|---|
| **甲** | **G-1 之量測對象不是 home 之原檔**。home RECON 所測檔（`0e72b1ec…`）與 Home v2（`cfc007f3…`）**皆不在 repo**；唯一帶 144 列 done region 者為 `forms/…_Home_20260809.xlsx`（`1895fb2a…`）。FORMS.md 記其四道編修為 D5／F／G／K／Z —— **I 欄不在其中**，此為「Test Item 未受影響」之論據，但該論據來自 FORMS.md 自身之 diff，無 Home v2 可交叉驗證。**G-1 之 PASS provisional on 此替代** |
| **乙** | **BASELINE 之涵蓋範圍我擴大了**，非依裁決：R-C11 把 spec 移出 `inputs/` 留在 `spec-index/`，而 `.gitignore:58` 使該處同樣不入版控。若 BASELINE 只涵蓋 `inputs/`，R-C11 之副作用即為「Comfort 唯一 spec 來源脫離雜湊保護」。故列入 SR24 三件，共 8 檔。**此為執行層判斷，可駁回** |
| **丙** | **A-CF07 尚未結案**。prepared workbook 已產且結構驗證通過，但 profile §0.1 保留四項 Excel 確認予 Pei（16 §1 裁定 3）。**Phase 4 三個起跑條件中，此為唯一未達成者** |

---

## 1. 下放包 14 §5 六項 —— 已於前一輪完成，本輪逐項複驗

16 §3.1 第 1 項要求執行 14 §5。該六項於 16 落檔前已執行，本輪**複驗現況**
而非重做：

| # | 項目 | 複驗 |
|---|---|---|
| 1 | R-C19 貼入 `RULINGS.md` | ✅ 條文區塊存在 |
| 2 | 四節改置（`test_set_map.tsv`） | ✅ 四節皆為新歸屬 |
| 3 | `verify_partn.py` 七項 | ✅ **7 PASS** |
| 4 | `framework.md` §3.5／§3.6 | ✅ 兩節存在 |
| 5 | `DECISIONS.md` §6 修正案 ＋ Sign-off 未重簽 | ✅ |
| 6 | `RUNBOOK.md` SYNC 註記 | ✅ |

明細見 `09_partN_amendment.md`（該包 §2–§6）。本檔不重複。

## 2. profile 已寫（16 §3.1 第 2 項）

`docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`。

- 下放包 **15** 之全部條款逐條落地（§0 ~ §8）。
- **16 §1 三項裁定皆已寫入**：§3.1 繼承（附 G-1）、§3.4 source token 照錄
  （含 `12.1` 之 `LEDs (.`）、§0.1 Excel 確認由 Pei 執行。
- §2 另加 Part N 兩次修正案之生效註記（#15 更名、四節改置），
  使 profile 與 `framework.md` 現況一致。
- §3.1 依 16 §2 原標 `pending G-1`；G-1 執行後改為
  **`G-1 PASS 2026-08-15（附 provenance 但書）`** —— 未逕行移除標註，
  因為但書本身必須留在 profile 裡（見 §3.3）。

## 3. G-1 執行（16 §3.1 第 3 項）

`features/comfort/scripts/gate_g1_test_item.py`，可重跑。

### 3.1 量測條件（16 §2 要求明載）

| 項 | 值 |
|---|---|
| 檔案 | `forms/FM-WI-FSM-036-A01 …_SWQT_Home_20260809.xlsx` |
| SHA256 | `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72` |
| 工作表 | `Test Case Specification&Result` |
| header 列 | 9 |
| 量測欄 | **I（Test Item）** |
| 母體選取 | **Z 欄 == `ArifChen`** |
| 母體列數 | **144**（assertion PASS） |
| modal 判準 | `\b(shall\|will\|should\|would)\b`，case-insensitive、詞界比對 |
| 抽樣 | 10 列，**seed=20260815**（固定，可重現） |

**母體選擇器為何是 `ArifChen` 而非 `Arif`**：FORMS.md 記該 copy 之 done
region author 為 `ArifChen`，而 `features/home/feature.yaml` 設
`done_region.author_value: Arif`。以 `Arif` 選取會**匹配 0 列**，
而 0 列之量測會「全數不含 modal」—— 那是一個看起來像結論的空集合。
母體列數 assertion（== 144）即為擋此而設。

### 3.2 實測結果

| 項 | 值 |
|---|---|
| 含 modal | **143 / 144（99.3%）** |
| 不含 modal | **1** |
| 空白 | 0 |
| modal 詞頻 | `shall` ×176、`would` ×1 |
| Test Item 長度 | min 83、**中位 273**、max 2657 |

**唯一不含 modal 之列（row 135）**：其內容為 `Available Widgets List and
3rd Party Widget Naming Convention` 之整張 widget 對照表（41 列 `HS9.x |
名稱 | Reference Document | 機型`），非行為陳述。**不構成形態反例。**

**形態**（隨機 10 列全文已列於腳本輸出，此處摘三例）：

> `The system shall implement Display Page Management Options: Shows the
> options to manage pages including "Add Page", "Delete Pages", and "Reorder
> Pages" options.\n\n(Screens with Horizontal menu bar; "Edit Pages" button
> pressed → Add Page, Delete Current Page, Reorder Pages options are
> displayed)`

> `Pressing the full screen icon and widget text title (if available) on a
> widget shall transition the screen to the full page app for that widget
> category.\n\n(Full screen icon pressed on the Media widget → full page
> Media app is displayed)`

> `When button is selected while vehicle is in motion a pop-up shall appear
> stating "Feature not available while vehicle is in motion." [OK, X] shall
> close pop-up.\n\n(…)`

形態為 **需求陳述 ＋ 情境括號**，長度中位 273 字 —— **明確不是 tc_title
型短語**。與 profile §3.1「以 spec 語言濃縮之需求陳述，modal 僅此欄允許」
一致。

### 3.3 判定：**PASS**，但 provisional

依 G-1 之判定規則「若 done region 之形態與 profile §3.1 一致 → §3.1 生效」
—— **形態一致，§3.1 生效**。

**但書（甲）**：量測對象非 home RECON 所測之檔。三份候選之狀態：

| 檔 | SHA256 | 在 repo？ |
|---|---|---|
| home RECON 所測（`…_Home_20260720.xlsx`） | `0e72b1ec…` | ❌ |
| Home v2（`fw036-home-regen-v2`） | `cfc007f3…` | ❌ |
| **本次量測**（`forms/…_Home_20260809.xlsx`） | `1895fb2a…` | ✅ |

FORMS.md 記第三份為 **pre-A-H26 build 加四道編修：`D5` / `F` / `G` / `K` /
`Z`**。**`I` 欄不在其中** —— 此即「Test Item 內容未受影響」之論據。
但該論據來自 FORMS.md 自身之 cell-by-cell diff，**在 Home v2 缺席下無法
交叉驗證**。

**我未自行調整 §3.1 以遷就實測**（16 §2 明文禁止），亦未把但書藏起來 ——
它寫在 profile §3.1 段內，不只在本上繳包裡。若分析層認為該替代不可接受，
§3.1 回到 pending 並重裁。

## 4. `DECISIONS.md`（16 §3.1 第 4 項）

- §6 profile `[OVERRIDE]`：`[PEI — 維持未定]` → **`[SIGNED 2026-08-15]`**，
  記 15 ＋ 16 §1 為依據，並註明 A-CF07 之寫回處置已於 profile §0.1 明文
  （03 §5 之要求自此滿足）。
- **新增 `## Sign-off 2 —— profile [OVERRIDE]`**，Reviewed by `PeiPYHsu`、
  Date `2026-08-15`。**首筆 Sign-off（Part N，2026-08-14）逐字未動。**
- 第二筆明載其**涵蓋範圍**：僅 §6 之 profile 一項；不涵蓋 Part N、
  不涵蓋任何 `[PROPOSED]`。無此界定，日後讀者無從分辨兩筆各簽了什麼。
- Ruling notes 記 G-1 之 PASS 與其但書、A-CF07 之備妥與未結案、
  以及 Phase 4 三個起跑條件之現況。

## 5. A-CF07 備妥（16 §3.1 第 5 項）—— 已停下等候

### 5.1 範本清列

`features/comfort/scripts/prepare_workbook.py`（dry-run 先跑，再 `--write`）。

**取用前之 hash gate**（R-C14）：來源 SHA256 須等於裁定之空白範本
`cd876c202c71e74b…`，不符即 ABORT —— 不同範本會使下列每個儲存格引用都是猜測。
實測 PASS。

清空之五格與其原值：

| 格 | 原值 |
|---|---|
| `D10` | `xxx` |
| `F10` | `NR1L-AntiTheft-001` |
| `G10` | `AntiTheft` |
| `S10` | `NA` |
| `D11` | `xxx` |

**刻意不動**：`B10` / `B11` = `=IF(ISBLANK($D10),"",ROW()-9)` —— 範本自身之
編號機制。**未刪任何列** —— 刪列會位移 DV 之 `sqref` 與 R10 之 x14 下拉。

**寫入路徑**：`backend/xlsx_surgical.py`（profile §6 / R18-3 之唯一路徑）。
結構驗證：**48 zip members，僅 `xl/worksheets/sheet6.xml` 差異**；
DV counts `sheet5 (1,0)` / `sheet6 (3,2)` 與來源相同。

**寫回後自檔案讀回之 assertion**：

```
- PASS — five cells cleared: expected ['D10','F10','G10','S10','D11'],
                             measured ['D10','F10','G10','S10','D11']
- PASS — column B formulas intact: expected ['B10','B11'],
                                   measured ['B10','B11']
```

產出：`output/…_SWQT_Comfort_20260815_prepared.xlsx`，
SHA256 `b68117a211b08009…`。

### 5.2 台帳

**`BASELINE.sha256`（8 檔，全數 `shasum -c` OK）**：

- `inputs/` 5 檔：036 空白範本、037、CFTS043 `.doc`、CFTS043 tree view、
  Market Configuration Table
- **`spec-index/` 3 檔**：SR24 export `.xlsx`、同名 `.json`、SR24 PDF

**乙 —— 涵蓋 `spec-index/` 是我的判斷，不是裁決。** 理由已寫在該檔註解裡：
R-C11 把 spec 移出 `inputs/` 以確保單一來源，但 `.gitignore:58` 之
`spec-index/cache/*` 使該處同樣不入版控。若 BASELINE 只涵蓋 `inputs/`，
**R-C11 之副作用就是「Comfort 唯一之 spec 來源脫離雜湊保護」** —— 而那不是
任何人的本意。這正是本檔註解所述 home/amfm 素材消失事件的同一形態。
若分析層認為不應如此，回報即改。

**`DELIVERY.sha256`（append-only，ENTRY 001）**：記操作、路徑、清列內容、
結構數字，以及**狀態：未經 Excel 確認**。`shasum -c --ignore-missing` 驗過。

### 5.3 已停下

**四項 Excel 確認保留予 Pei**（profile §0.1 / 16 §1 裁定 3）：

1. 無修復提示
2. R 欄下拉可用且為九項
3. D5 Scope 正確
4. 第 10–11 列已清且無殘留列號

**執行層備妥檔案後停下等候**（16 §3.1 第 5 項明文）。
**程式層檢查不能代替 Excel 自身之檔案完整性判定。**

## 6. Phase 4 未開始（16 §3.2）

三個起跑條件：

| 條件 | 狀態 |
|---|---|
| G-1 PASS | ✅（附但書） |
| profile 落檔 | ✅ |
| **A-CF07 清列經 Pei 於 Excel 確認** | **⏳ 未達成** |

未產 TC、未指派 tc_id、未做 sibling 判定。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 7.1 已驗

1. 14 §5 六項之現況逐項複驗（含 `verify_partn.py` 7 PASS）。
2. G-1 之母體列數 assertion（144）與九類統計。
3. G-1 量測對象之 SHA256，及其與另兩份 home 檔之差異。
4. 範本清列之來源 hash gate、五格原值、寫回後讀回之兩項 assertion、
   結構驗證（members／DV counts）。
5. `BASELINE.sha256` 8 檔全數 OK；`DELIVERY.sha256` 2 筆 OK。
6. `DECISIONS.md` 兩筆 Sign-off 並存，首筆逐字未動。

### 7.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **prepared workbook 於 Excel 之實際開啟** | profile §0.1 保留予 Pei（裁定 3） | **設計如此** —— 這不是缺口，是分工。但它是 Phase 4 之唯一未達成條件 |
| 2 | **G-1 之替代是否可接受** | 需 Home v2 交叉驗證，該檔不在 repo | **中** —— §3.3 之但書；若不可接受，§3.1 回 pending |
| 3 | **profile §3.2 之配置軸是否窮盡** | 我照 15 §3.2 逐字落地，未自行對 129 節全文複核其列舉是否完整 | **中** —— 若有未列之配置軸，Phase 4 會在寫 TC 時遇到無 source class 可標之前置條件。全文已在 `section_fulltext.tsv`，可複核，本包未做因未指示 |
| 4 | **profile §3.4 之 token 清單是否窮盡** | 同上 —— 15 §3.4 列四類，我未全文掃描是否另有原文標記 | 中 —— 可機械掃描（如 `«»`、`°`、`h` 結尾數字），本包未做 |
| 5 | DR #6（7" 螢幕配置）、DR #11（HMI Pop Up List） | 待 Pei 指認／補入 | 低 |

**第 3、4 項是同一形態**：profile 之內容條款由分析層依證據導出，我逐字落地
而未複核其**窮盡性**。15 §3.2 說「逐節出現」、§3.4 列出四類 token —— 兩者
都是全稱陳述，而全稱陳述可以機械複核。若分析層希望我做，兩項各一輪掃描
即可；若認為那屬 Tier 2（判斷「這算不算一個配置軸」），請明示。

### 7.3 未做、亦未偷做者

- **未於 Excel 開啟 prepared workbook**，未代 Pei 作四項確認。
- **未自行調整 profile §3.1 以遷就 G-1 實測**（16 §2 明文禁止）。
- 未把 G-1 之 provenance 但書略去 —— 它寫在 profile §3.1 內，非只在本包。
- 未覆寫首筆 Sign-off；第二筆明載涵蓋範圍。
- 未刪 `09_partN_amendment.md`。
- 未產 TC、未指派 tc_id；Phase 4 未開始。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未執行任何 git 操作。

### 7.4 執行層對「本包可否結案」之判斷

**可結案。** profile 已落檔並涵蓋 16 §1 三項裁定；G-1 已執行且判定與但書
俱在；A-CF07 已備妥並依裁定停下；台帳已建並驗過。

**下一步只等一件事**：Pei 於 Excel 開啟
`features/comfort/output/…_Comfort_20260815_prepared.xlsx` 確認四項。
該確認一到，Phase 4 三條件齊備，pilot（`Seat Control Tab`，14 leaves，
首筆落 row 10）即可起跑。

**兩項請分析層裁示**：§0 之乙（BASELINE 涵蓋 `spec-index/`，我的判斷）
與 §7.2 第 3、4 項（profile 內容條款之窮盡性複核，歸屬未明）。
