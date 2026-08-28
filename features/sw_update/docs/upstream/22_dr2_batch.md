# 上繳包 22 —— DR-SU2 開立、欄 14 材料重列、pilot v3 欄集補齊

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/23_dr2_batch.md`
  （SHA256 `31c7efaee6d4ee773e8ff9a39440be61d4fd85e8d5d69a24410ba4ad3c9a7100`，181 行）
- **未結 DR：2 筆（DR-SU1、DR-SU2）** —— 由 1 筆增為 2 筆
- 新腳本：無｜`scripts/gen_pilot.py` 改 v3

## 本輪三個主結果

1. **pilot v3 之 lint 與 v2 逐項相同**：**K=0／T=0／U=3**，20/21 全 0。
   欄集補齊（`S`=`NA`、`T`–`Z` 留空）**未觸發任何新違規** —— 與預期相符。
2. **DR-SU2 開立**，初始清單 5 列（`363`–`367`）。
   其立論已由「我方找不到通道」改為**上游文件之內在不一致**。
3. **`SOURCE_COLUMNS.md` 更新後：037 之未定由 4 → 1**（僅欄 14，延展一輪）；
   全案未定由 24 → **21 欄**。併出 21 欄之來源分佈與可逕裁者之指認。

---

## 1. T36e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU28 v2 | 914 | **OK** | `d7514de983d7` |
| R-SU29 | 859 | **OK** | `52eead3217fa` |

二條逐字 append，**既有 43 個條文區塊未受影響** ✅（現 45 塊）。
索引表現行 **29 條**（R-SU28→**v2**、新增 R-SU29）；
留存 **16 條**（新增 `R-SU28`(v1)）。與下放包 23 §五 T36e 所定之數一致。

`PLAYBOOK.md` §7 追加 **(23)**「否證之方向本身是資訊」，
判準為**「這個否證，讓我知道了什麼新的東西，還是只讓我不知道原本以為知道的東西？」**

---

## 2. T36a —— 欄 14 之裁定材料（重列，R-SU28 v2 之延展）

### 欄 14 — `Description/Action for Reusable`

- 非空 **311／311**｜unique **115**

**unique 值前 5 名**：

| 次數 | 值（前 90 字元） |
|---:|---|
| 191 | The requirement can reuse above 50% of previous requirement, but not fully reuseable. |
| 2 | Existing version handling and Arbiter decision logic can be reused with additional compari |
| 2 | Existing update availability handling and Arbiter-based priority control can be reused wit |
| 2 | Existing status handling and pop-up framework can be reused. |
| 2 | Existing HMI callback handling and signal transmission logic can be reused. |

**抽樣 8 列之全文**：

- `SWE1-FOTA-352` — Software Inventory Request Handling
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-228` — Use FOTA_Status from SGW as Master HMI Trigg
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-099` — Handle “Update Now” Selection for ROV Forced
  > Reuses HMI interaction and signal write mechanisms.

- `SWE1-FOTA-231` — Display What’s New Popup on User Selection
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-111` — Enable TBM Update Functions Only When TBM Is
  > Same logic reused across all TBM FOTA flows.

- `SWE1-FOTA-199` — Transmit Tester Present During External ECU 
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-286` — OTA Flow Status Reporting
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.

- `SWE1-FOTA-173` — Integrate with Signature Verification Module
  > The requirement can reuse above 50% of previous requirement, but not fully reuseable.


> **執行層不裁。** 下一輪必裁（R-SU28 v2：延展為一次性，不得累積）。

---

## 3. T36b —— DR-SU2 開立

`DATA_REQUESTS.md` 新增 **DR-SU2**，狀態 `OPEN`、Urgency `High`，初始清單 5 列。

| 欄 | 值 |
|---|---|
| 事項 | 105 列（內部服務主體且 VC 亦無外部面者）於**系統測層級**之觀測手段 |
| pattern | log tag 清單／診斷 DID 表／服務介面定義／HMI 間接後果之對照 |
| Leaves served | 初始 5 列（`363`–`367`，`Telematics Client`）；**滾動清單** |
| Batch impact | 全部 21 個 Test Set 之撰寫（`Telematics Client` **5/5 全落此類**） |
| Urgency | **High** |

### 3.1 其立論之改變（本輪之關鍵）

檔內載明：

> 037 自身將該 105 列之 **85% 標為含 `System Test`**，
> 而其 `Verification Criteria` **未指出任何外部可觀測面**。
> **文件說要做系統測，卻沒說系統測時要看哪裡。**

先前之立論為「我們找不到通道」——**對上游而言那是我方之困難，非其文件之缺陷**。
上繳包 21 §T35a 之實測（15% vs 35%）把它變成了**文件內在之不一致**。

### 3.2 未結 DR 清單（2 筆）

| # | 事項 | 狀態 | Urgency | 阻斷 |
|---|---|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | **OPEN** | High | `newR1L-SU-003` 三欄 PENDING（lint U=3） |
| **DR-SU2** | 105 列於系統測層級之觀測手段 | **OPEN** | High | 初始 5 列；隨批次滾動增列 |

**與下放包 23 §六.3 之預期（2 筆）相符。**

---

## 4. T36c —— `SOURCE_COLUMNS.md` 更新

| 素材 | 欄數 | 已用 | 不用 | 未定 |
|---|---:|---:|---:|---:|
| 037 `AnalysisReport_FULL` | 18 | 8 | **9**（+3） | **1**（−3） |
| SYS1 `Basic Report` | 7 | 2 | 0 | 5 |
| 036 母本 TC 分頁 | 33 | 17 | 1 | 15 |
| **合計** | **58** | **27** | **10** | **21** |

欄 8／10／12 之「不用」理由**逐欄抄 R-SU28 v2 之原文**；
欄 14 標 `未定（延展一輪，下輪必裁）`，並載明
「**一次性延展，理由為分析層之閱讀順序，非默許跨輪；延展須逐次記明，不得累積**」。

### 4.1 未定 21 欄之來源分佈（T36c 所令）

| 來源 | 未定欄數 | 欄 | 可逕裁者之指認 |
|---|---:|---|---|
| **037** | **1** | 14 | 材料已備，下輪必裁 |
| **SYS1** | **5** | 0 `ID`、1 `Space / Document`、4 `SYSRE_HMI_Source ID`、5 `Type`、6 `_polarion` | **1 與 5 為常數欄**（全 `Requirements / SYS`／全 `SYSRE_HMI`），依 **R-SU28 v1(a) 之判準可逕裁「不用」，不需讀其內容**；0／4／6 為 unique=120 之識別碼 |
| **036** | **15** | `C`、`E`、`T`–`Z`(7)、`AB`–`AG`(6) | `T`–`Z` 本輪已裁**留空**（§5），其「用途」標記待同步；`AB`–`AG` 為**測試結果面**之欄（Test Version／Test Vehicle／Test Period／Tester／Test Result／Defect ID），**其填寫者為測試執行端而非產出端** |
| **合計** | **21** | | |

**排序之建議（陳報，不裁）**：SYS1 之 1／5 與 036 之 `AB`–`AG` 共 **8 欄**
可依值型態或欄位語意逕裁；037 之欄 14 材料已備（共 9 欄可於下輪清掉）。
餘 `C`／`E`（Polarion／TestRail 之 id）與 SYS1 之三個識別碼欄，
須先確認其在交付流程中之角色。

---

## 5. T36d —— pilot v3 之欄集補齊與 lint

產出：`sandbox/pilot03/…_ext.xlsx`。**TC 內容逐字沿 v2 不動**，僅補欄集：

| 欄 | v2 | **v3** | 依據 |
|---|---|---|---|
| `S`（Functional Safety） | 未寫 | **`NA`** | 下放包 23 §四：他 feature 5/6 之實務 |
| `T`–`Z`（車型適用旗標） | 未寫 | **留空**（明示不寫） | 下放包 23 §四：他 feature 6/6 之實務 |

實測（`openpyxl` 覆核 pilot03 之第 10–14 列）：
`S` 五列皆 `'NA'`；`T`–`Z` 五列皆 `None`。✅

```
python3 scripts/lint036.py <pilot03 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=3  V=0        exit 0
```

| 項 | v2 | v3 | 下放包 23 §五 T36d 之預期 | |
|---|---|---|---|:--:|
| K／T／U | 0／0／3 | **0／0／3** | 與 v2 同 | ✅ |
| 全 0 之項數 | 20/21 | **20/21** | 與 v2 同 | ✅ |

**欄集補齊未觸發任何新違規。** 特別是 `M`（空欄三態）仍為 0 ——
即 lint 對 `T`–`Z` 之留空**不視為空欄違規**（該檢查之範圍為
`FIELD_HEADERS` 之八欄，不含車型欄）。

> ⚠ **此一「未觸發」之正確讀法**：lint **沒有覆蓋** `S` 與 `T`–`Z`，
> 故其全綠**不構成對本輪欄集裁定之驗證**。
> 二者之正確性只有他 feature 之實務可佐（5/6、6/6），
> 而**「六本皆未填」不蘊含「應留空」**（上繳包 21 §4.1 已記）。

---

## 6. 未結 DR 清單

見 §3.2 —— **2 筆（DR-SU1、DR-SU2）**。

### 待分析層確認之事項（非 DR）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **欄 14 之裁定**（延展一輪，下輪必裁） | §2 |
| 2 | **SYS1 欄 1／5 為常數欄，可逕裁不用**；036 `AB`–`AG` 六欄屬測試執行端 | §4.1 |
| 3 | **`T`–`Z` 之「用途」標記**：本輪裁「留空」是**填法**之裁定，其在 `SOURCE_COLUMNS.md` 之 `已用/不用/未定` 標記尚未同步 | §4.1 |
| 4 | **v3 之欄集裁定未被任何機械檢查覆蓋** —— lint 不查 `S`／`T`–`Z` | §5 |

---

## 7. 獨立自評

### 7.1 §六.6 所問：滾動清單會不會使「已在清單上」被誤讀為「已確認無解」

**會，而且是反過來的那一半更危險。**

**(甲) 「已在清單上」之語意 —— 這一半我可以定義清楚。**

依 R-SU29(b)(c)，入清單之條件為
**「撰寫該列 TC 時，依 R-SU25(c) 求其外部可觀測後果而取不到」**。
即入清單者**已逐列試過**。我已將此逐字寫入 `DATA_REQUESTS.md` 之 DR-SU2 節。

**(乙) 「不在清單上」之語意 —— 這一半才是真正的風險，且它不對稱。**

DR-SU2 現有 5 列，而 105 列中之**其餘 100 列尚未逐列試過**。
於是清單上有一個**沉默的多數**：

| 讀者可能之推論 | 是否成立 |
|---|:--:|
| 清單上之 5 列 = 已試過且取不到 | ✅ |
| 不在清單上之 100 列 = 已試過且取得到 | ❌ **完全不成立** |
| DR-SU2 之規模 = 5 列 | ❌ **其潛在規模為 105 列** |

**最危險之處在於進度感**：滾動清單會隨批次成長，
而**成長本身看起來像「新發現的問題」，其實是「原本就在那裡、現在才輪到它」**。
若不明說潛在上界，讀者會把「DR-SU2 現有 5 列」讀成一個小問題，
而它可能是 105 列 —— **佔母體 34%**。

**(丙) 我做了什麼**：於 `DATA_REQUESTS.md` 之 DR-SU2 節逐字載明 ——

> **「已在清單上」= 已逐列試過且取不到**；
> **「不在清單上」≠ 已確認有解** —— 105 列中之其餘 100 列**尚未逐列試過**。
> 二者不可互推。

**(丁) 我做不到什麼**：**這句話擋不住進度感之誤讀。**
一段警語與一個會成長的數字並排時，**數字比較大聲**。

**唯一真正的解法是把上界也放進清單之標題**，例如
「DR-SU2：5 / **上界 105** 列」—— 使規模一眼可見，而非藏在註解裡。
**執行層不自行改 DR 之表頭格式**（其為台帳體例），
**建議之，列為待確認。**

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §5 之「欄集補齊未觸發任何新違規」。**

那句話讀起來像是「`S`=`NA` 與 `T`–`Z` 留空之裁定已被驗證」。
**實際上 lint 根本不查那八欄** —— 其 `M`（空欄三態）之範圍為
`FIELD_HEADERS` 之八個 TC 內容欄，不含 `S` 與 `T`–`Z`。

**故 v3 之 20/21 與 v2 完全相同，是必然的** ——
我改的是 lint 看不見的地方。**「未觸發新違規」在此不是證據，是同義反覆。**

**與 §7(16)（空測通過與實測通過是兩件事）同族**：
上次是「驗收路徑沒呼叫到被驗的程式碼」，
這次是「**檢查工具沒覆蓋到被改的欄**」。
二者之外觀都是一張全綠的表。

我已在 §5 之後加了該限度之說明。**能誠實說的是**：
v3 之欄集裁定，其依據**只有他 feature 之實務**（5/6、6/6），
而那不是驗證，是**從眾**；且「六本皆未填」不蘊含「應留空」。

### 7.3 一項我做了而下放包未要求的事

**§4.1 —— 列 24 欄之來源分佈時，順手指認了其中 8 欄「可逕裁」。**

T36c 只令「列出其餘 24 個未定欄之來源分佈，供分析層排下輪之裁定順序」。
照做就是一張三列的表（037／SYS1／036 各幾欄）。

我另做的是**對每一組套一次 R-SU28 v1(a) 之判準** ——
於是看見 **SYS1 之欄 1（全 `Requirements / SYS`）與欄 5（全 `SYSRE_HMI`）
是常數欄**，依該判準**可逕裁「不用」且不需讀其內容**；
而 036 之 `AB`–`AG` 六欄（Test Version／Test Vehicle／Test Period／
Tester／Test Result／Defect ID）之**填寫者為測試執行端，非產出端**，
其歸屬亦不需讀內容即可判。

**記明此事之理由**：R-SU28 v1(a) 之判準是**可重複套用**的 ——
它一旦成立，就不只適用於當初裁定它的那 9 欄。
**把一條判準寫進條文之後，下一步是掃一遍還有誰符合它**，
否則同一個判準每次都要重新被發現一次。

**其限度**：我只做了**指認**，未裁 —— 因為 R-SU26(b) 之裁定權在分析層，
且「常數欄可逕裁」在 SYS1 上是否同樣成立，**取決於 SYS1 在本 feature 之角色**
（R-SU11 已裁其接點為 HMI 87 列），而那不是我能判的。
