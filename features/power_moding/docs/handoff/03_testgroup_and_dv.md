# 下放包 03 —— Test Group 欄值改判、DV 列舉值實測與 Phase 1 啟動

- 日期：2026-08-23
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/03_testgroup_and_dv.md`
- 前一包：[02_baseline_switch.md](02_baseline_switch.md)（上繳
  [../upstream/02_baseline_switch.md](../upstream/02_baseline_switch.md)，已覆核）

---

## 一、02 包之覆核結果

**通過。** 十三節齊備，九條停止條件之逐條檢查具實據。三項特別記明：

1. **R-PMH7 之判準經反向證明具鑑別力** —— 同一判準對母本判通過、對客戶那份
   判離群（35 欄、`Estimated Test Time` 兩次）。這是 R-G7-1 所要求之對照向，
   且非事後補做。
2. **`outline_map.json` 之兩種先驗定位法皆被 fail-loud 攔下** ——
   尤以子字串包含法之「全解但有錯」（ch7 Startup→p3 實為 p8）最為關鍵：
   **assert 過了而資料是錯的**，正是 G103 之形狀。執行層自行識出此形狀並改法，
   記為本輪最有價值之一項。定案法（首 N 字唯一命中，N 由 80 遞減至 40，
   命中 >1 頁即判未解）之盲區為「未解」而非「錯解」，失效方向正確。
3. **`Test Case Framework` 分頁實測為 0 非空儲存格 → Q8 得解**，
   R-PMH6 之輸入維持兩項（FROP 12 值、規格目次）。
   **01 包自評為「風險最高」者結果為陰性，此事本身要記**：
   自評之價值在於它被驗了，不在於它命中 —— 與 Power Management 之 A-PW56
   （「`Test Case Framework` 為 Power 獨有」之誤判）恰為對照。

### 1.1 A-PMH06 —— 核可等效改寫（分析層追認，另上呈 canon 層）

R-PMH11 所指定之 `inputs/` ＋ `!inputs/MANIFEST.sha256` **實測無效** ——
git 不遞迴進入已排除之目錄，否定規則不生效。執行層改以 `inputs/*` ＋
否定規則並雙向驗證（MANIFEST 解除、四份素材仍排除、他 feature 不受影響、
`add --dry-run` 只出一筆）。

**核可為等效改寫**：R-PMH11 之**目的**（雜湊檔入版控、素材本身不入）未變，
變的是達成方法，且新方法經雙向實測。條文不改字，以附註承接（比照 R-P36）。
A-PMH06 → **RESOLVED**。

> ⚠ **本項須上呈 Pei —— 兩點超出分析層**：
> （一）`.gitignore` 屬版控政策（Operating Charter 明列須 Pei 裁定），
> 本次為「已裁事項之落實方法修正」，故分析層先行核可，**請 Pei 追認或撤銷**；
> （二）**此為 scaffold 給每個 feature 之同一份常數，任何 feature 照 R-PMH11
> 之字面做都會踩到**。`scripts/new_feature.py` 之 `GITIGNORE` 樣板是否同步修改，
> 屬 canon 層，**本包不改、不代裁**。

---

## 二、A-PMH07 —— 成立，且經分析層獨立複驗

執行層指出 R-PMH2 所引之 Comfort R-C6 前例**在交付件上沒有實現**。
分析層**未採信其結論即改判**，另行獨立量測。

**量測條件**：對四份客戶目錄之已交付 xlsx（唯讀複本），`openpyxl`
`read_only=True, data_only=True`，取 `Test Case Specification` 分頁
r10 起 `D` 欄非空之列，統計 `G` 欄之相異值與其列數。

| 交付件 | 交付夾名 | **G 欄實測** | 覆蓋 |
|---|---|---|---|
| Comfort 20260817 | `Climate Control Interface` | **`Climate Control Interface`** | **466 / 466** |
| User Profiles 20260820 | `User Profiles` | `User Profiles` | 189 / 189 |
| Time Management 20260822 | `Time Management` | `Time Management` | 59 / 59 |
| Power Management 20260821 | `Power Management` | `Power Management` | 283 / 283（另 1 列為 `SWE-PM-089` 留白列） |

**4 / 4 皆為交付夾名，無一例外。** 執行層之指認成立。

**R-C6 之條文與其自身交付件相衝突**：R-C6 逐字為
「`test_group: "Comfort"` — spec 標題模組名，非交付夾之 `Climate Control Interface`」，
而該 feature 實際交付之 466 列 G 欄全填 `Climate Control Interface`。
**R-PMH2 建立於一條未被其自身交付件實現之條文之上。**

> 此即「格式權威是既有已交付件，不是條文或分析層設計之理想」之直接實例。
> 我在 01 包引 R-C6 時**只讀了條文與 `feature.yaml` 註解，未查其交付件** ——
> 而 G-H 早已寫明「遇無先例之判斷，先查他 feature 之**交付件**（不是其 yaml）」。
> 記為分析層之作業瑕疵，不歸執行層。

### 2.1 連帶處置

**須回報 comfort feature**（比照 A-PW51 → `features/comfort/ANOMALIES.md`
A-CF-EXT-01 之前例）：R-C6 之條文與其交付件不一致，其 466 列究竟是
（a）條文被違反、（b）條文後被實務推翻而未修訂、或（c）該欄由他人填寫，
**本 feature 無從判定，只登記事實**。

---

## 三、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH13（workbook Test Group 欄之值）
工作簿 `Test Group`（G）欄一律填交付夾名 `Disclaimer screen`。

依據為四份已交付件之實測：G 欄相異值恰為交付夾名，覆蓋 4/4、
各檔 100% 之資料列（Comfort 466/466 = `Climate Control Interface`、
User Profiles 189/189、Time Management 59/59、
Power Management 283/283）。

R-PMH2 之後半（`test_group` 為 `Power Moding`）**撤回**。
R-PMH2 之前半（`feature` = `Power Moding`、slug = `power_moding`）
**維持有效** —— 其為 repo 內部識別，不進入任何交付欄位，不受本條影響。

`feature.yaml` 之 `test_group` 鍵改為 `Disclaimer screen`，並於註解記明
其為交付夾名而非規格模組名，以免日後被讀成 R-C6 之同型錯誤。

本條之效力起於 Pei 核可；核可前 G 欄不得寫入任何值（R-PMH6 之延後仍在）。
```

```
R-PMH14（語料之鑑別力口徑）
以已交付件語料支持某一判斷時，其分母為「**能分辨候選各案之交付件數**」，
不是「交付件總數」。

不能分辨者（各候選在該件上取值相同）不計入分子亦不計入分母，並須於
引用處具名列出其被排除之理由。

依據：Q7 之語料中，三份交付件之交付夾名與規格模組名恰好相同，
故其 `{abbr}` 無論依何者取值都得同一結果 —— 該三份對本題之鑑別力為零，
「3 / 4 支持某案」為無效之比率（R-G8：缺判準之比率不予採認）。
```

```
R-PMH15（A-PMH06 之落實方法）
`features/power_moding/.gitignore` 之素材排除改以 `inputs/*` 形態書寫，
其後接否定規則放行 `inputs/MANIFEST.sha256`。

不得使用 `inputs/`（目錄形態）＋ 否定規則之組合 —— git 不遞迴進入已排除
之目錄，該組合實測無效（A-PMH06）。

驗證條件（雙向，缺一不可）：
(a) `git check-ignore -v` 對 `MANIFEST.sha256` 無命中；
(b) 同指令對四份素材各自仍命中；
(c) 他 feature 之忽略行為不變；
(d) `git add --dry-run` 對 `inputs/` 恰輸出一筆。

R-PMH11 之目的未變，本條僅取代其所指定之寫法。
```

---

## 四、Q7（`tc_id` 之 `{abbr}`）—— 提案與其語料，待 Pei 裁

### 4.1 語料（執行層實測，分析層複驗相符）

| 交付件 | `{abbr}` | G 欄／交付夾名 | 規格模組名 | 三者關係 |
|---|---|---|---|---|
| User Profiles | `UserProfiles` | `User Profiles` | User Profiles | **三者同**（去空白） |
| Time Management | `TimeManagement` | `Time Management` | Time Management | **三者同**（去空白） |
| Power Management | `PowerManagement` | `Power Management` | Power Management | **三者同**（去空白） |
| **Comfort** | **`ComfortHMI`** | `Climate Control Interface` | Comfort | **三者互異** |

### 4.2 依 R-PMH14 之鑑別力篩選

前三份之交付夾名與規格模組名相同，**無論 `{abbr}` 取哪一個來源都得同一字串**
—— 對本題**鑑別力為零**，依 R-PMH14 排除。

**有鑑別力之語料只有 Comfort 一份，且其形態與本 feature 相同**
（交付夾名為與規格模組無關之三字詞組；本 feature 之 `Disclaimer screen` 亦然）。
Comfort 之取法為 **規格模組名 ＋ `HMI`**。

### 4.3 兩案

| 案 | 值 | 支持 |
|---|---|---|
| **（甲）** | `NR1L-PowerModingHMI-{NNN}` | 唯一有鑑別力之語料（Comfort）之取法；且與本 feature 檔名 tag `PowerModingHMI` 逐字相同（自我佐證） |
| （乙） | `NR1L-DisclaimerScreen-{NNN}` | 與 R-PMH13 之 G 欄值一致（去空白）；惟支持它的三份語料依 R-PMH14 為無效比率 |

**分析層提案（甲）**，惟 n = 1，**不宣稱其為「慣例」** —— 一個實例只證明
「曾經這樣做過」，不證明「一律這樣做」。**請 Pei 裁定。**
裁定前 `tc_id_pattern` 維持 `TBD`，不得產生任何 `tc_id`。

---

## 五、作業步驟

1. **抄錄** —— §三之 R-PMH13 / R-PMH14 / R-PMH15 逐字抄入 `RULINGS.md`，
   附核對表。R-PMH11 條後加 A-PMH06 之附註（**原文不改字**，比照 R-PMH6 之
   處理），A-PMH06 標 RESOLVED。
   **R-PMH13 標「待 Pei 核可」，未核可前不得寫入 `feature.yaml` 之 `test_group`。**

2. **DV 列舉值全量實測（本包首要）** —— 對 R-PMH7 母本之
   `Test Case Specification 測試用例規範` 分頁，列出**全部** DV
   （legacy 與 x14 各自分列）：其 `sqref` 範圍、型別、`formula1` 之原文、
   以及若指向他分頁則其目標範圍之逐項值。
   **不得以 `openpyxl` 存回**（x14 一存即毀，R-G1 註／R-G3）；
   建議以 `zipfile` 直讀 `xl/worksheets/*.xml` 之 `<dataValidation>` 與
   `<x14:dataValidation>`，並以 `openpyxl` 之讀取結果互為對照（二證同值方採）。

3. **`priority` 欄之三方衝突判定** —— 下列三個來源互不一致，**本包只查明母本
   現況，不裁定**：
   - `QS Suggestion!B5` 建議「高 High／中 Medium／低 Low／不適用 NA」
   - `user_profiles` 前例記 `[P0, P1, P2, P3]`
   - 037 之 `Priority` 欄實測值為 High／Medium／Low 形態

   須回報：(a) 母本 `P10:P1411` 之 DV 究竟列舉何值（若無 DV 亦須明言）；
   (b) 四份已交付件之 `P` 欄實際值分布（各檔之相異值與計數）；
   (c) 三方之交集與差集。
   **canon §10.2 明訂 `P0/P1/P2/P3`，而已交付件之實測若與之相異，
   即為條文與交付件之衝突（與 A-PMH07 同型），停並上繳，不自行取捨。**

4. **其餘欄位之 DV 對照** —— `design_method`（R 欄，已知 9 項全集）、
   `functional_safety`（S）、車型欄（T–Z）、`Test Result`（AF）等，
   凡母本帶 DV 者，其列舉值與四份已交付件之實際值比對，
   回報「有 DV 而交付件逸出其列舉」之欄位（若有）。

5. **A-PMH07 之連帶回報** —— 於
   `features/comfort/ANOMALIES.md` 新增一則外部回報（編號依該 feature 現行序，
   比照 A-CF-EXT-01 之形態），內容為：R-C6 條文與其交付件 466/466 之不一致，
   **只記事實與證據，不判定成因、不提案修改該 feature 之條文**。
   本 feature 側於 `ANOMALIES.md` 之 A-PMH07 加交叉指引。

6. **Phase 1 recon 啟動** —— 以 `scripts/recon.py`（或依 `feature.yaml` 適配）
   產出 `RECON.md` 與預填之 `DECISIONS.md`。
   `workbook_state` 依 R-PMH8 為 `BLANK`，不再重判。
   leaf 全集依 R-PMH1 之判準重算（不沿用 01 包之 48，須先算後比）。

7. **framework Layer 2 之候選輸入備料** —— 依 R-PMH6，輸入為兩項：
   (a) 037 `FROP` 之 12 個相異值及其 leaf 分布；
   (b) SYS1 匯出之 `Outline Number` 章節結構（52 項）。
   **只備料、只列交集與分歧，不擬 Test Set 名、不定 granularity**
   —— 該二者為 Phase 3 之 Tier 2 事項。

8. **02 包 §11 所列之五項該驗而未驗者** —— 逐項處置或明載其延後理由，
   不得靜默略過。

---

## 六、停止條件

canon §0 六條，另加本包三條：

7. 母本之 `priority` DV 與 canon §10.2 之 `P0/P1/P2/P3` 不一致（步驟 3）
8. 任一欄之已交付件實際值逸出母本 DV 之列舉（步驟 4）
9. leaf 全集重算結果不等於 48（步驟 6）

**本包零寫回工作簿。** 全部改狀態 git 屬 Pei（R-G5）。

---

## 七、上繳包要求（`docs/upstream/03_testgroup_and_dv.md`）

1. §三三條之抄錄核對表 ＋ R-PMH11 附註之落實證明（原文 SHA256 未變）
2. 步驟 2 之 DV 全量清單（legacy／x14 分列，二證同值之對照）
3. 步驟 3 之三方衝突判定表（(a)(b)(c) 三項齊備）
4. 步驟 4 之逸出欄位清單（無則明言「零」，不得省略本節）
5. 步驟 5 之 comfort 側回報全文 ＋ 本側交叉指引
6. `RECON.md` ＋ 預填之 `DECISIONS.md`
7. 步驟 7 之兩項備料與其交集／分歧表
8. 步驟 8 之五項逐項處置
9. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
10. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之 git 唯讀／改狀態分列
11. `docs/INDEX.md` 補本輪次列

---

## 八、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §三 |
|---|---|---|
| R-PMH13 | G 欄填交付夾名；撤回 R-PMH2 後半 | ✅ |
| R-PMH14 | 語料之鑑別力口徑（分母為能分辨者） | ✅ |
| R-PMH15 | `.gitignore` 之 `inputs/*` 形態與四項雙向驗證 | ✅ |

三條各管一事（§9.1 通則 11）。R-PMH13 為**部分撤回型**，
其撤回範圍與保留範圍已於條內分別明載（§9.3 之教訓）。

**待 Pei 者二項**：R-PMH13 之核可、Q7 之 `{abbr}` 裁定。
**上呈 Pei 者一項**：A-PMH06 之追認，及 `new_feature.py` 樣板是否同步修改。
