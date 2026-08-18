# 上繳 39（**含 38 輪**）— R-U57 入庫、Z-1 與 R-U56 全批自檢、第五批取樣

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`39_rd_disposition.md`（**有裁決條文：R-U57**）＋ `38_batch05_sample.md`
- **合併上繳** —— 39 包明文允許「可與 38 輪之上繳合併，具名所擇」；
  **所擇：合併**。理由：38 之 Z-1 自檢與 39 之作業 2 掃的是同一批餘 leaf，
  分兩檔會使同一次掃描之結果散在兩處。
- **本輪未執行任何 git**；**未寫回工作簿**；**RD v2 未寄出**（Tier 3，屬 Pei）；
  **第五批未生成**
- 語料：**134 條**（修改 2 條：`TC-110` 之內容、`TC-082` 之記載）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 134 條，**違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 134 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | 十一項掃描（見 §6）；**Z-1 0 處** |
| `audit_consistency.py --self-test` | **46 / 46**（＋3：Z-1）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | 紅 0 ／ 黃 15 ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |
| `audit_assignment.py` ／ `--self-test` | 違規 0 ／ 6 / 6 |

---

# A. 38 包

## 1. Z-1 —— `TC-110` **採 (a)**

### 1.1 判定成立，且其論證即為改法

`per Profile` **就寫在 `SWE1-HMI-PROF-018-02` 自己的 037 description 內**：

> `The system will latch on whichever tab was last used within and over key
> cycles, **per Profile**, when entered through pushing the Profile button.`

**R-U56 之適用範圍是「spec 有內容而 037 未產出 leaf」** ——
此處 037 產出了 leaf，該行為就在其描述內。**那不是範圍外，
是該 leaf 之斷言沒有被驗完**（§6）。

其 §8.3 壓力測試為否：**一個把分頁存成全域（非逐 profile）之實作，
A 存 Edit Profile、key cycle 後回來仍是 Edit Profile，與原 ER 完全相符** ——
照樣通過。

### 1.2 修正（採 (a)）

| 欄 | 變更 |
|---|---|
| pre 2（新增）| `The last used tab of Driver Profile B is the “All Profiles” tab` |
| 步驟 3 | `… and check that …` → `… and read which tab is shown` |
| 步驟 4（新增）| `Activate Driver Profile B and check that the “All Profiles” tab is shown` |
| ER4（新增）| `Driver Profile B is active and its “All Profiles” tab is shown, **unchanged by the operations on Driver Profile A**` |

**採 (a) 之理由**：條文之 `within and over key cycles` 與 `per Profile`
**是同一句之兩個修飾** —— 併驗不失焦（§5.7）。
(b) 另立一條則其 procedure 之前三步會與本條逐字相同，
**只有第四步不同** —— 那是把同一次操作寫成兩條。

## 2. R-U56 判定之全批自檢 —— **命中 4 處，誤用 3 處**

38 包之自陳照收：「R-U56 是我裁的。**它若被用成『這句話我不驗』的通行證，
那是我立條時沒有把適用範圍寫得夠窄之代價**。」

**判準**：該行為之關鍵詞是否出現於**任一 leaf** 之 037 `description`／`VC`。

| # | 出處 | 標的 | 關鍵詞是否落在某 leaf 之 description | 判 |
|---|---|---|---|---|
| 1 | `TC-110`（5.1）| 逐 profile 之隔離 | **是** —— `SWE1-HMI-PROF-018-02`（**本 leaf 自己**）| **誤用 → 已改（§1）** |
| 2 | `TC-082`（4.1.1）| 「HU／TBM 未確認時亦顯示 PU1088」| **是** —— `SWE1-HMI-PROF-002-03` | **誤用 → 改為委派（§2.1）** |
| 3 | **37 輪上繳 §3.3**（5.3.1）| `(if turned on for that Profile)` 之關閉側 | **是** —— `SWE1-HMI-PROF-023`（**本 leaf 自己**）| **誤用 → 改判（§2.2）** |
| 4 | `TC-012`（9.8）| PU0609 句 | **否** —— 180 leaf 之 description／VC 皆無 | **判定成立，維持** |

### 2.1 第 2 處：`TC-082` —— **不是範圍外，是已經有人驗了**

`SWE1-HMI-PROF-002-03` 之 description 逐字為
`PU1088 is displayed if HU or TBM do not confirm complete default restoring`
—— **037 確實為其切了 leaf，且該 leaf 已生成**（`NR1L-UserProfiles-002`）。

故 `TC-082` 之記載改為**委派**：

> **該句由 `SWE1-HMI-PROF-002-03`（`NR1L-UserProfiles-002`）承擔** ——
> 037 **確實為其切了 leaf**，且已生成。

**原記載不只分類錯，它還把一個「已被覆蓋」寫成了「不必覆蓋」。**

### 2.2 第 3 處：**我 37 輪自己的判定** —— 一併具名

37 輪上繳 §3.3 我寫：

> 查 037 之 180 leaf 母體：`5.3.1` 只有一個 leaf（`SWE1-HMI-PROF-023`），
> 其 description 為 PRACC9.1 之**整句**（含該括號）。
> 「關閉時不顯示」之分支無對應 leaf —— 依 R-U56 判為 OUT-OF-SCOPE。

**該判定與 `TC-110` 是同一個錯**：我自己寫了「description 為整句（含該括號）」，
**卻仍判它範圍外** —— 括號就在那個 leaf 的描述裡。

**改判**：`(if turned on for that Profile)` 之關閉側**屬 `SWE1-HMI-PROF-023`
自己之斷言，非範圍外**；現行之 `TC-118` 只驗開啟側，
**故為我方之覆蓋不足**（同 A-UP13 之形態）。

**本輪未補該 TC** —— 其為**另一個配置情境**（popup 關閉之 profile），
非同一觸發，依 §5.7 不得併入 `TC-118`；而 38／39 包皆未授權生成。
**具名待排**：建議隨第五批或另立補洞條處理。

### 2.3 掃描落地（`audit_consistency` 之 **Z-1**）

判準即 §2 之關鍵詞比對；**排除自陳「不適用／係誤用／原記」之句**
（那是更正而非宣稱）。現行語料 **0 處**（三處已改、一處判定成立）。

方向性 ＋3（**46 / 46**），含兩條護欄：
「該句自陳 R-U56 不適用 → 不得列入」與「無 R-U56 之 remarks → 不得列入」。

**這是 screen，不是判決**：關鍵詞出現不代表該**行為**被斷言 ——
例如 RD #7（9.1.1 之另一側）之 `username and avatar` 出現在五個 leaf，
但那些 leaf 講的是別的事，**「大螢幕於清單左側顯示」未被任何 leaf 斷言**，
其 R-U56 判定仍成立。**故列待判由人判，不判紅。**

### 2.4 文件級之 R-U56 判定亦查（26 輪之 DR #3／#7、A-UP02）

| 標的 | 是否有 leaf | 判 |
|---|---|---|
| DR #3 之 `3.1`–`3.5`／`10.1`／`11.1`／`11.2` | **八節皆無 leaf** | **判定成立** |
| RD #7（9.1.1 之另一側）| `9.1.1` 僅 `086` 一個 leaf，其描述只述 8.4 吋側 | **判定成立**（見 §2.3 之說明）|

---

## 3. 第五批取樣清單（**先回報，不生成**）

### 3.1 範圍與條數

| 項 | 值 |
|---|---|
| 範圍 | **5.12 – 5.16（`ALLPR1` – `ALLPR6`）** |
| leaf | **13**（實測，與下放包相符）|
| 估條數 | **13**（一葉一 TC；**額外造者 0**，理由見 §3.3）|
| `tc_id` | `135` – `147` |
| 批後 leaf 覆蓋 | 125 → **138 / 180** |

**條數之說明（與下放包之「估 ≈ 14 條」差 1，具名）**：
`041-04`（5.13.2）**本身就是一個 leaf**，其 TC 即「一葉一 TC」——
34 輪已更正「它不是額外造者」之誤，故**不另加條**。
而 §3.3 之 §7 配對經判定**應併於 `042` 之 ER 而非另造**（同 Z-1 之 (a)）。
**故額外造者為 0，13 leaf ＝ 13 條。**

### 3.2 逐 leaf

| 節 | leaf | 037 先驗 | 主題 |
|---|---|---|---|
| 5.12 | `036` | Medium | 依建立順序排列（新的加在右）|
| 5.12.1 | `037` | Medium | 預設 profile 依記憶座椅連結排序 |
| 5.12.2 | `038` | Low | 編輯座椅連結**不**改變順序 |
| 5.13 | `039` | Low | 回復預設（未清除全部）時加到右邊 |
| 5.13.1 | `040` | Low | 清除全部後回復 → 回到預設順序 |
| 5.13.2 | `041-01` | High | Clear Personal Data → 新現用者連現座椅 |
| 5.13.2 | `041-02` | High | 無記憶座椅時 → 預設為 Driver 1 |
| 5.13.2 | `041-03` | Medium | 進度與完成之 popup（PU1089／PU1090）|
| 5.13.2 | `041-04` | Medium | **失敗路徑**（PU1091）—— 須故障注入 |
| 5.14 | `042` | Low | 長按 avatar 拖曳排序（**且不啟用該 profile**）|
| 5.15 | `043` | Low | username 置中且不重疊 |
| 5.15.1 | `044` | Low | 過長時之截斷（**依 Core HMI 文件**）|
| 5.16 | `045` | Medium | 連網帳號之雲朵圖示 |

### 3.3 三項必含

#### (1) 待兌現之 (b) 類委派 —— 本批 **0 處**

ch5 之 `ALLPR` 群內無任何既有委派之被指名者。

#### (2) §7 列舉配對 —— 須額外造者 **1 條**

**`042`（5.14）之括號句**：`Pressing and holding the Avatar … will allow for
dragging and reordering the Profiles **(and will not result in that Profile
being activated)**`。

**「不會啟用」是一個獨立之必然結果，且其為缺席斷言** ——
只驗「拖得動」，一個**拖曳同時也啟用了該 profile** 之實作會通過。
惟其與拖曳**同一觸發**（長按 avatar），依 §5.7 **併於同一條之 ER 即可**，
**不另造 TC**。

故本批之**額外造者為 0**；`042` 以**兩條 ER** 承載其兩個結果。

**與下放包之「估 ≈ 14 條」差 1** —— 差在此處：下放包預留了一條配對，
而本層判定其應**併入**而非另造（同 38 包 Z-1 採 (a) 之理由：同一觸發、同句修飾）。
**若分析層認為該括號句應另立負向 TC，本清單加回一條即可（14 條，`135`–`148`）。**

#### (3) 變體對造之新 axis —— **0，且這是查過的**

V-1 之 6 個 axis 落在 6.1／8.1／9.1／10.3.1／11.4，**ch5 一個都沒有**
（`data/override_notes_m3.tsv` 逐條複驗，同 25／29 輪）。

### 3.4 `pending` 兩 axis —— **再次具名其預定兌現批次**

| axis | leaf | 節 | **預定兌現** |
|---|---|---|---|
| `r1h-cpa-6.1` | `SWE1-HMI-PROF-046` | 6.1 | **第六批**（ch6 ＋ ch7，19 leaf）|
| `r1h-cpa-8.1` | `SWE1-HMI-PROF-065` | 8.1 | **第七批**（ch8，23 leaf）|

**兩者仍不在本批**（本批為 ch5 之 `ALLPR` 群）。
`audit_variant_pairs` 之絆線仍在：**該 leaf 一旦生成 TC 而未配對造即轉紅**。

**剩餘批次規劃（55 leaf 全數落位）**：第五批 13 ＋ 第六批 19（ch6 9 ＋ ch7 10）
＋ 第七批 23（ch8）＝ **55** ✓

### 3.5 本批之已知寫作限制（**先具名**）

| leaf | 限制 |
|---|---|
| **`044`（5.15.1）** | 其截斷規則在 **Core HMI Logic and Flow**，**不在本 feature 之 spec 基線內**。可驗「過長時發生截斷」，**不可寫截斷之具體規則**（§8.4.1）。形態同 `002-02` 之 R-U27 —— **本批唯一同型者**（29 輪已具名）|
| `041-03`／`041-04` | `PU1089`／`PU1090`／`PU1091` 之**內文**未載於 spec；比照 R-U27，ER 只驗其**顯示與時序**，不寫其文字 |
| `041-04` | 須注入「HU 或 TBM 未確認完成」之情境 → `design_method` 為**基礎故障注入**（§12）|
| **`045`（5.16）** | 見 §B.2 —— 其 `Connected account` 落在 RD #5 之掃描命中內 |
| `037` | 其 `(Ex: mem seat 1 + Driver 1 …)` 為條文之**例示**，數字取自條文非自擬 |
| `042` | 拖曳為**手勢操作**；其可執行性依賴實機，pre-condition 須具名至少三個 profile 方能觀察順序改變 |

---

# B. 39 包

## 1. R-U57 入庫

- **逐字**追加於 `RULINGS.md`「第三十九輪條文」（R19-2：原文貼入）。
- `docs/runtime/profiles/…UserProfiles_Profile.md` **§0 範圍段**加註指向本條，
  並複述其界線：**所免除者為字面形式之返工，不含判定翻轉**。
- `DATA_REQUESTS.md` 之 **RD #5／RD #6 兩節**各加註本條與
  **Urgency：高 → 低**，並照錄分析層之自陳
  （「返工面積隨時間變大」之催促理由自本裁定起失效）。
- RD #6 另加一句：其答覆決定 `TC-077` 之 remarks 是否須記為
  **「不可佈署之條文條件」**，**該記載屬交付內容之一部分**，
  故其 Urgency 雖低，答覆仍會改變一份交付欄位。

## 2. 作業 2 —— 餘 55 leaf 之 label 曝險掃描

掃 `5.12`–`5.16`、ch6、ch7、ch8 之 `pdf_text` 與 037 description，
字樣：`Stellantis Account`／`Stellantis Connected Account`／`Connected Account`。

### 2.1 **命中 2 節 / 2 leaf**

| 節 | leaf | 命中字樣 | 上下文 |
|---|---|---|---|
| **5.16** | `SWE1-HMI-PROF-045`（**第五批**）| `Connected account` | `… if the profile is connected with an **Connected account** (See Connected Personal Account HMI)` |
| **8.2** | `SWE1-HMI-PROF-066`（**第七批**）| `Connected account` | `Connecting an account or downloading an existing **Connected account** are not pictured here` |

### 2.2 判定：**RD #5 之兩種讀法都不及於這兩處**

理由二者，皆可查證：

1. **兩處皆非按鈕 label** —— 其 `Connected account`（小寫 a）是**帳號之名詞**
   （「與某個 Connected account 連結」），不是 Table EDPR1 那個**選項列之 label**。
   而 RD #5 所問之覆寫為 `"Stellantis Account"` → `"Connected Account"`，
   **其標的是 label**。
2. **兩處皆不在 ch9** —— RD #5 之兩種讀法（列級／及於 **ch9** 全章）
   **都以 ch9 為上界**。5.16 與 8.2 在其外。

**兩處皆不含 `Stellantis Account`** —— 即那個會被覆寫的字串本身，
在餘 55 leaf 之節文中**一次都沒出現**。

### 2.3 **處置：仍依 39 包加註，但同時記其判定**

39 包云「有命中 → 其撰寫暫依現行（各節逐字），並於該 TC 之 remarks 具名
『本條之 label 依 RD #5 之答覆可能調整』」。

**照辦**：`045`（第五批）與 `066`（第七批）生成時，其 remarks 併記兩句 ——
該提示句，**以及 §2.2 之判定**（兩處皆非 label、皆不在 ch9，
故 RD #5 之答覆**很可能不改變它們**）。

**只寫提示句而不寫判定，會讓讀者以為那兩條懸著。**

### 2.4 **一項界線之聲明（39 包明令）**

39 包禁止「依 R-U57 自行認定某項為**形式差異**」。

**§2.2 之判定不是形式差異之認定** —— 它是**範圍認定**
（那兩處是否落在 RD #5 之標的內），與「答覆到了之後某項改不改」無關。
**本輪未對任何項作形式差異之認定**：RD 尚未寄出，無答覆可套用。

---

## 4. 獨立判斷 —— 本包是否仍有該驗而未驗者

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **5.3.1 之「popup 關閉側」未補** | **本輪改判所生，待排** | §A.2.2 —— 由 OUT-OF-SCOPE 改判為**我方覆蓋不足**；為另一配置情境，不得併入 `TC-118` |
| 2 | **Z-1 掃描為關鍵詞 screen** | 判準界線 | §A.2.3 —— 關鍵詞出現不等於該行為被斷言；**列待判不判紅** |
| 3 | **第五批取樣清單未經覆核** | **分析層待辦** | 生成待其覆核 |
| 4 | **`044` 之基線外文件依賴** | 承 29 輪 | 本批唯一同型；是否轉 DR 屬分析層 |
| 5 | **`042` 之拖曳手勢依賴實機** | note | 其可執行性非文件可決 |
| 6 | Y-1 1／X-1 6／W-1 4／V-1 15／U-1 7／Q-1 11／D-3 15 黃 | 承前 | 本輪新增之黃為 `TC-110` 改述後之句 |
| 7 | **RD v2 未寄出** | **待 Pei（Tier 3）** | R-U57 已降其 Urgency 為低，**但仍應寄** |
| 8 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

---

## 5. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | **檔案追加** | `RULINGS.md`（**R-U57 逐字** ＋ 執行層回報）| 否 |
| 2 | 檔案編輯 | `DATA_REQUESTS.md`（RD #5／#6 之 R-U57 加註與 Urgency 調整）| 否 |
| 3 | 檔案編輯 | `docs/runtime/profiles/…UserProfiles_Profile.md`（R-U56 之窄化、R-U57 之加註）| 否 |
| 4 | 檔案編輯 | `scripts/gen_batch04.py`（`TC-110` 之 pre／proc／ER／remarks／reasoning）、`gen_batch03.py`（`TC-082` 之改判）| 否 |
| 5 | 檔案編輯 | `scripts/audit_consistency.py`（**Z-1 掃描** ＋3 方向性案例）| 否 |
| 6 | 檔案重生成 ×56 | `generated/`（batch03／04；**內容變動者 2 條**：`110`／`082`，其中**測試內容變動者僅 `110`**）| 否 |
| 7 | **檔案新建** | `docs/upstream/39_rd_disposition.md`（本檔，**含 38 輪**）| 否 |
| 8 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 9 | 程式執行 | R-U56 全批自檢（含文件級三項）、label 曝險掃描、餘 leaf 查詢、生成 ×2、全部閘、十一支 audit／lint 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**未依 R-U57 自行認定任何項為「形式差異」**。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第五批未生成** —— 待取樣清單覆核。

**未動**：工作簿、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`DECISIONS.md`、`ANOMALIES.md`、`data/`、`docs/handoff/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_pairs.py`、
`lint_tcs.py`、`lint_variant_labels.py`、`render_spec_region.py`、
`build_batch_context.py`、`audit_variant_pairs.py`、`audit_delegation.py`、
`audit_assignment.py`、`scan_override_notes.py`、`lint_outbound_doc.py`、
**他 feature 之任何檔**、`docs/fw036/`。
