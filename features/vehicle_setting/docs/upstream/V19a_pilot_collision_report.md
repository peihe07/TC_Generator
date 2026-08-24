# 上繳 V19a —— **事故報告：W-VF53 重做與覆寫**（不是一份工單完成報告）

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/V19_pilot_start.md`（W-VF53）
- **本檔不取代 `docs/upstream/V19_pilot_start.md`** —— 該檔為併行 session 於
  commit `6e0f0a0` 所交，仍為 W-VF53 之正式上繳。
- **狀態：停手。** 未提交任何 git、未寫回工作簿。

---

## 0. 一句話

**W-VF53 已於今日 09:12–09:14 由併行 session 完成並提交（`6e0f0a0`），
我在不知情下重做了一次**，過程中**覆寫了三個已提交之產物**（工作區，
未提交），並且在重做時發現**已交付之 pilot 批有一項實質缺陷**。

依 R-G5「遇覆寫事故：兩版並存、上報、停手，不自行還原」，
**兩版已並存於磁碟，本層停手，請 Pei 裁定取捨。**

---

## 1. 事故經過（時序）

| 時刻 | 事件 |
|---|---|
| 09:05 | `docs/handoff/V19_pilot_start.md` 落檔 |
| 09:12 | 併行 session 產出 `generated/vf230_pilot1.json`（10 TC） |
| 09:14 | 併行 session 產出 `docs/upstream/V19_pilot_start.md` |
| （之後） | commit **`6e0f0a0`** —— `feat(vehicle_setting): package V19 — VF230 pilot batch, 10 TCs, seq 238-247` |
| 09:1x | **本 session 受交辦「pilot 批開跑」**，未察上列已完成 |
| 09:2x | 本 session 改 `vf230_wvf45_priority.py`、重跑、產出 `generated/vf230_batch01.json` |
| 09:22 | 察覺 `docs/upstream/V19_pilot_start.md` 與 `generated/vf230_pilot1.json` 已存在且已入版控 → **停手** |

### 1.1 根因 —— **A-VF9 之第三次發生，這次方向相反**

A-VF9 逐字：「**併行線不知本線裁定之存在**」。本次為其鏡像 ——
**本 session 不知併行線已完成本線之工單**。

`CROSSLINE.md`（R-VF38 之產物）所載為「條文之跨線保護」，
**不載「工單之完成狀態」**。故一個已完成之工單，對另一 session 而言
與未完成無法區分 —— **`docs/handoff/` 內有下放包、`docs/upstream/` 內有
上繳包，二者之並存即為「已完成」之唯一訊號，而該訊號無人被要求去看。**

**本層之疏失具名**：接下工單時**未先查 `docs/upstream/` 是否已有對應包**。
這是一個零成本之檢查（`ls docs/upstream/ | grep V19`），本層沒做。

---

## 2. 覆寫事故 —— 三個已提交檔案被工作區覆寫（未提交）

| 檔 | 狀態 | HEAD 版之保全 |
|---|---|---|
| `scripts/vf230_wvf45_priority.py` | ` M` 已修改 | `scripts/vf230_wvf45_priority.py.HEAD_V19` |
| `data/_vf230_priority.json` | ` M` 已修改 | `data/_vf230_priority.json.HEAD_V19` |
| `docs/reports/vf230_priority_batches.md` | ` M` 已修改 | `docs/reports/vf230_priority_batches.md.HEAD_V19` |

**HEAD 版以 `git show`（唯讀）取出並落為 `.HEAD_V19` 旁檔，兩版並存。**
**本層未執行 `git checkout`／`restore`／`stash`／`clean`**（R-G5 明列屬 Pei）。

⚠ **現存風險**：工作區之三檔為本層之版本。**若併行 session 執行
`git add -A` 或不帶 pathspec 之 commit，會把本層之修改一併提交** ——
此即 R-G12 所防之形態，而這次的加害者是本 session。**請儘速處置。**

---

## 3. 本層所改之內容為何 —— 一項真缺陷，但**修法可能不是這個**

### 3.1 缺陷：選池序與 R-VS58 逐字不符

`vf230_wvf45_priority.py` 原實作將 Priority 併入 round-robin 之鍵：

```python
buckets[(order[x["priority"]], x["test_set"])].append(x)
...
while any(buckets.values()):
    for key in sorted(buckets):        # ← 涵蓋 P0、P1、P2 之全部組合
        if buckets[key]: pool.append(buckets[key].pop(0))
```

`sorted(buckets)` 一輪走遍 (P0, TS)…(P1, TS)…(P2, TS) **全部 19 個 bucket**，
故每輪同時取 P0、P1、P2 各若干 —— **Priority 成為同層之排序鍵，
而非外層之分割**。

**R-VS58 逐字**：「第一序 依 R-VS56 判為 **P0** 之 leaf／第二序 P1／
第三序 P2／**同序內** 依既有之逐 Layer 2 輪流 ＋ reqid 升冪」。
**V19 §5.1 亦逐字重述**：「依 R-VS58 之選池序（**P0→P1→P2**；
同序內逐 Test Set 輪流 ＋ reqid 升冪），自池首取 10 條」。

**實測後果**：舊池首 10 條為 **6 個 P0 ＋ 4 個 P1**；88 個 P0 中有 82 個
散落於其後。**該腳本自身之註解亦寫「P0→P1→P2」，與其實作不符。**

### 3.2 兩版池首之差異（僅第 7–10 條）

| # | HEAD 版（已交付所據） | 本層修正版 |
|---:|---|---|
| 1–6 | （相同）PowerLiftgate-016／BlindSpotAlert-002／LaneSenseWarning-014／SuspensionServiceMode-002／BlindSpotTrailer-045／ParkSense-084 | 同左 |
| 7 | `IlluminatedApproach-002`（**P1**） | `PowerLiftgate/TailgateAlert-017`（P0） |
| 8 | `4AUXSwitches-027`（**P1**） | `BlindSpotAlert-003`（P0） |
| 9 | `DaytimeRunningLights-002`（**P1**） | `LaneSenseWarning-015`（P0） |
| 10 | `PassiveEntry-009`（**P1**） | `SuspensionServiceMode-003`（P0） |

分布（P0 88／P1 267／P2 272）與池長（621）**兩版相同**，
池之**集合亦相同**，**僅順序不同**。

---

## 4. **已交付之 pilot 批之實質缺陷 —— 本報告最重要之一節**

已提交之 `generated/vf230_pilot1.json` 第 7–10 條，其 `priority` 欄標 **`P0`**，
`reasoning` 逐字為：

> 「**P0(c) safety (R-VF57)**：{X} 之設定項決定試驗者能否開關**該警示**；
> 其不顯示即駕駛無從調整。」

**而該四簇不在 R-VF57 所確認之 P0(c) 七簇內。** R-VF57 逐字列舉之七簇為：

```
Forward Collision Warning ／ Pedestrian Emergency Braking or Warning &
Active Braking ／ Blind Spot Alert ／ Blind Spot with Trailer Detection ／
Lane Sense Warning ／ Park Sense ／ Traffic Sign Warning
```

`Illuminated Approach`／`4 AUX Switches`／`Daytime Running Lights`／
`Passive Entry` —— **四者皆不在其中**，且 priority 產物（兩版皆同）
將此四者判為 **P1**。

### 4.1 更值得記者：該 `reasoning` 為套版

四條之 reasoning 僅置換簇名，其餘逐字相同，皆稱
「決定試驗者能否開關**該警示**」。而：

- **`4 AUX Switches`** 為輔助開關之型別組態，**不是警示**；
- **`Passive Entry`** 為免鑰進入，**不是警示**；
- **`Illuminated Approach`** 為迎賓照明，**不是警示**；
- **`Daytime Running Lights`** 為日行燈，**不是警示**。

**一個套版之理由被套到四個不同性質之功能上，其中沒有一個是警示。**

### 4.2 本層之研判（不裁定）

兩版之池首前 6 條相同且皆為 P0。**已交付版之第 7–10 條為 P1，
而 V19 §1 逐字要求「pilot 批取 P0」** —— 二者衝突。
該衝突有兩種解法：

| 解法 | 動作 | 是否符合條文 |
|---|---|---|
| （甲）**修選池序** | 令 P0 為外層分割，池首 10 條自然全為 P0 | **符合** R-VS58 逐字與 V19 §5.1 |
| （乙）**改 priority 標記** | 把落入池首之 4 個 P1 標成 P0 | **違反** R-VF57 之七簇列舉與其「界線自此為判準（非建議）」 |

**已交付版採（乙）**。本層採（甲）。

**本層不主張自己對** —— 若分析層之本意是（乙）（即池首之內容優先於
Priority 標記之正確性），則本層之修正應撤回。**但（乙）之代價須明說**：
R-VF57 逐字稱該界線「**自此為判準（非建議）**」，且其鑑別對
（`Forward Collision Warning` P0 vs `…Sensitivity` P1）正是為了防止
「以名為鍵之規則判同級」。**把四個非警示功能標為 P0(c) safety，
即是該鑑別對所欲防之錯誤之放大版。**

---

## 5. 本層之產出（**不主張採用，供比對**）

| 檔 | 內容 |
|---|---|
| `generated/vf230_batch01.json` | 10 TC，**全為 P0**，依修正後之池首 |
| `scripts/vf230_wvf53_pilot.py` | 其生成腳本，含 V19 §5.3 六項升級條件之機器自檢 |

**此非 V19 §5.4 所禁之「第 2 批」** —— 其為同一批（pilot）之**替代版本**，
非續批。本層未生成任何續批。

### 5.1 六項升級條件之自檢結果

```
=== V19 §5.3 六項升級條件之自檢 ===
  全部通過 ✅
```

逐項為機器檢查：test_item 括號下半／Input Test Data 為 `NA`／
無 `PENDING: DR-{n}` 以外之空欄或以 `NA` 充當未知／spec_ref 格式
（`VF230_V1_(PHDCC27|PDT27)_VF_\d+`）／Test Set 在已鎖 9 名內／
畫面層敘述可指素材來源。另檢 procedure 與 ER 步數一致。

### 5.2 `specification_reference` 之取值路徑（與已交付版比對之需）

R-VS33′ 之錨鏈末端本應取 SYS2 `Basic Report` 之
`SYS2 來源需求項目ID`，**而 VF230 之 SYS2 缺件（DR-28）**。
本層改取 `inputs/FM-WI-FSM-035-A02_…_SYSRA_VF230_V4_Released.xlsx`
之 `Basic Report`（A-VS134 已認可其為同型且涵蓋 037 全部 745 列）。
**10/10 全解**，形態為 `VF230_V1_{PHDCC27|PDT27}_VF_{n}`。

**此代用未經明文裁定** —— 若已交付版採別的路徑，二者須調和。
列為待裁項。

---

## 6. 新登記之異常（**未寫入 `ANOMALIES.md`** —— 停手，待裁後再落）

| 擬編 | 主旨 |
|---|---|
| **A-VF17** | `vf230_wvf45_priority.py` 之選池序與 R-VS58 逐字不符（Priority 為同層排序鍵而非外層分割）；**其自身註解亦與實作不符** |
| **A-VF18** | `SWE1-VC-LaneSenseWarning-014` 條文內部不一致：第 4 句稱評估 Lane_Assist 以決定 **`Cornering Lights`** feature availability，結論句處置之對象為 **`Lane Sense Warning`** customer setting |
| **A-VF19** | 已交付 pilot 批第 7–10 條標 `P0(c) safety (R-VF57)`，而該四簇不在 R-VF57 之七簇內；其 reasoning 為套版且四者皆非警示（§4） |
| **A-VF20** | **工單完成狀態無跨 session 訊號** —— A-VF9 之鏡像。`CROSSLINE.md` 載條文保護，不載工單狀態 |

**四則皆未寫入登記簿**：本輪為事故報告，寫入前須先定「哪一版為準」，
否則登記簿會記到一個可能被撤回之版本。

---

## 7. 待 Pei 裁定（四項，**本層停手不動**）

1. **池首取捨** —— 甲（修選池序，池首全 P0）或乙（維持已交付版）？
   此決定 pilot 批之 10 條為何，且決定 §2 之三個工作區檔案是保留或撤回。
2. **§4 之 P0 標記** —— 已交付版之 4 條 `P0(c) safety` 標記是否更正為 P1？
   若更正，該 4 條 TC 之 `priority` 欄與 `reasoning` 須重寫。
3. **§2 之覆寫處置** —— 三個 ` M` 檔案：採本層版、還原 HEAD 版、或人工併版？
   **全部 git 動作屬 Pei（R-G5），本層不執行。**
4. **§5.2 之 `specification_reference` 代用路徑**是否認可（DR-28 缺件下
   以 SYSRA 之 `Basic Report` 代 SYS2）。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **未比對兩版 TC 之內容差異。** 本報告只比對了「哪 10 條」，
   **未逐欄比對已交付版與本層版在前 6 條（相同 leaf）上之書寫差異** ——
   二者可能在 test_item、procedure、spec_ref 上寫法不同。若裁定採已交付版，
   本層版可整份丟棄；若採本層版，該比對就必要。**未做，因為裁定未下。**

2. **A-VF13 之涵蓋範圍未重估。** `ANOMALIES.md` 之 A-VF13 記
   「pilot 批 10 條中 9 條之值域來源被誤記為『無』」，其所舉變體
   （`[ DRL_Menu_Enable ]`、`AUX_Switch_Types`）屬**舊池首**之第 9、8 條。
   若池首改為本層版，**A-VF13 之舉例將不在 pilot 批內**，
   該則之「pilot 批」一語須改指。本層未改（不動他人已落之登記）。

3. **82 個 P0 之位置未查。** 舊選池序下，88 個 P0 中有 82 個散落於
   621 條之後段。**其散落到多後面，本層未量** ——
   若裁定採乙案，這 82 個 P0 何時才會被生成，是一個該答而未答之問題
   （R-VS58 之立法目的即為「最高風險項是否已覆蓋」可作答）。

4. **本層對併行 session 之影響未評估。** §2 之三個 ` M` 檔案自 09:2x 起
   即在工作區。**若併行 session 在此期間讀取過 `_vf230_priority.json`
   或 `vf230_priority_batches.md`，其讀到的是本層之版本** ——
   本層無法得知其是否讀過，亦無法得知其後續產出是否已受影響。
   **這是本次事故中唯一無法由本層自行界定範圍者。**

---

## 9. git 揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | `git status --short` | 3 |
| **唯讀 git** | `git log --oneline -3 -- <path>` | 2 |
| **唯讀 git** | `git show HEAD:<path>`（保全 HEAD 版） | 4 |
| **改狀態 git** | **無** | **0** |

**未執行 `git add`／`commit`／`checkout`／`restore`／`stash`／`clean`。**

## 10. 工作區動作全列

| # | 動作 | 對象 | 可逆性 |
|---|---|---|---|
| 1 | Python 就地改寫 | `scripts/vf230_wvf45_priority.py`（選池序） | HEAD 版已保全為 `.HEAD_V19` |
| 2 | 執行該腳本 | 覆寫 `data/_vf230_priority.json`、`docs/reports/vf230_priority_batches.md` | 同上 |
| 3 | heredoc 新建 | `scripts/vf230_wvf53_pilot.py` | 新檔，刪之即可 |
| 4 | 執行該腳本 | 新建 `generated/vf230_batch01.json` | 新檔，刪之即可 |
| 5 | `git show`（唯讀）→ 落檔 | 三個 `.HEAD_V19` 旁檔 | 新檔，刪之即可 |
| 6 | heredoc 寫檔 | `docs/upstream/V19a_pilot_collision_report.md`（本檔） | 新檔 |

**對工作簿之寫入：無**（R-VF26 寫回凍結，本層亦未觸及）。
**對 Part 1（CFTS044）線之任何檔案：未觸及。**
