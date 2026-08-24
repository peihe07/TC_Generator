# 上繳包 07 —— tie-break、granularity 檢查與跨 feature 缺口擴查

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/07_gap_widening.md`
- 前一包：[upstream/06_framework_proposal.md](06_framework_proposal.md)
- 執行狀態：**步驟 1–5 全部執行完畢。九條停止條件全未觸發。**
  **零寫回工作簿**；git 指令零次；**未修改任何他 feature 之檔案**。

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH32 | (c) 平手時不擇一，改敏感度處置；三種 tie-break 明文禁止 | 409 | `3f3db769108e0ead` | `3f3db769108e0ead` | 逐字相符 |
| R-PMH33 | 條文修訂之連帶檢查 | 242 | `3b2fe5dcd67478b1` | `3b2fe5dcd67478b1` | 逐字相符 |

### 1.1 R-PMH19 附註三之落實證明（原文 SHA256 未變）

| 條號 | SHA256（前 16） | 與前包所記 |
|---|---|---|
| **R-PMH19** | **`cbdeed8b8bc0774b`** | 相同（04／05／06 包） |

R-PMH19 條後現有**三則附註**，皆置於其 fenced block 之外：
附註一（(a) 由 R-PMH24 取代）、附註二（(b) 由 R-PMH31 收斂、揭露義務依
R-PMH30 增列量測時點）、**附註三（(c) 遇平手依 R-PMH32 處置，
並照錄三種明文禁止之 tie-break）**。

---

## 2. 步驟 5 —— 母體複驗（R-PMH32 之平手處置）

### 2.1 量測時點（R-PMH30）

**`2026-08-24T11:06:22+0800`**

### 2.2 母體 **16**（停止條件 7 未觸發）

| 交付夾 | 檔名日期 | 平手候選數 |
|---|---|---:|
| `AM:FM` | 20260810 | 1 |
| `Audio Management ` | 20260624 | 1 |
| `Climate Control Interface` | 20260817 | 1 |
| `Connection Manager` | 20260819 | 1 |
| `Core HMI/HomeHMI` | 20260809 | 1 |
| `Core HMI/Menu Bar and AppDrawer` | 20260729 | 1 |
| `Core HMI/Notifications HMI` | 20260817 | 1 |
| `Disclaimer screen` | 20260819 | 1 |
| **`Engineering Mode`** | **20260816** | **2 ⚠ 平手，代表檔未定** |
| `Power Management` | 20260821 | 1 |
| `Privacy Mode` | 20260813 | 1 |
| `SiriusXM` | 20260813 | 1 |
| `Time Management` | 20260822 | 1 |
| `User Profiles` | 20260820 | 1 |
| `Vehicle Settings/CFTS044` | 20260819 | 1 |
| `Vehicle Settings/VF230_V1_R5` | 20260819 | 1 |

**`Engineering Mode` 之兩候選並列，未擇一**（R-PMH32）：
`…_EngMode_20260816_Rebuilt.xlsx`(527 列) 與
`…_EngeeringMode_20260816.xlsx`(211 列)。

**代表檔於輸出中標為「未定」**；依 R-PMH29(a) 之敏感度陳述
（06 包 §2.4 實測，本輪未變）：兩候選之 `(D3, D4, D5)` 皆為
`(空, 空, 空)`，**Q3 之結論對此不敏感**。

**與 06 包之差異**：06 包之實作以排序決定了代表檔（實際取到
`EngeeringMode`）；**本輪依 R-PMH32 改為不擇一**，該夾之代表檔在
資料結構中為一個二元素清單而非單值。**母體計數不變（16）。**

---

## 3. 步驟 2 —— A-PMH13 之跨 feature 擴查

**量測範圍**：R-PMH24 母體之 16 個交付夾，含 `Engineering Mode` 之
**兩個平手候選**（故實際開啟 17 個檔），**合計 3,234 資料列**。
**唯讀開啟；未修改任何他 feature 之檔案。**

檢索欄位：`Test Case ID`／`Test Group`／`Test Item`／`Pre-Conditions`／
`Test procedure`／`Expected Result`／`Specification Reference` 七欄之合併文字，
大小寫不敏感正規式。

### 3.1 逐檔命中表

| 交付夾 | 資料列 | `OFF2` | `off road` | `Off Road+` | `Power Off State` | `launch` | `hard control` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `AM:FM` | 298 | 0 | 0 | 0 | 0 | 0 | 4 |
| `Audio Management ` | 43 | 0 | 0 | 0 | 0 | 0 | 0 |
| `Climate Control Interface` | 466 | 0 | 0 | 0 | 0 | 0 | 119 |
| `Connection Manager` | 123 | 0 | 0 | 0 | 0 | 3 | 0 |
| `Core HMI/HomeHMI` | 216 | 0 | **1** | 0 | 0 | 2 | 0 |
| `Core HMI/Menu Bar and AppDrawer` | 219 | 0 | **1** | 0 | 0 | 25 | 2 |
| `Core HMI/Notifications HMI` | 82 | 0 | 0 | 0 | 0 | 0 | 0 |
| **`Disclaimer screen`（本 feature）** | 48 | **1** | **1** | **1** | **7** | 2 | 2 |
| `Engineering Mode` [Rebuilt] | 527 | 0 | 0 | 0 | 0 | 172 | 0 |
| `Engineering Mode` [Engeering] | 211 | 0 | 0 | 0 | 0 | 0 | 0 |
| `Power Management` | 284 | 0 | 0 | 0 | 0 | 0 | 0 |
| `Privacy Mode` | 11 | 0 | 0 | 0 | 0 | 0 | 0 |
| `SiriusXM` | 215 | 0 | 0 | 0 | 0 | 0 | 2 |
| `Time Management` | 59 | 0 | 0 | 0 | 0 | 0 | 0 |
| `User Profiles` | 189 | 0 | 0 | 0 | 0 | 2 | 0 |
| `Vehicle Settings/CFTS044` | 243 | 0 | 0 | 0 | 0 | 0 | 0 |
| `Vehicle Settings/VF230_V1_R5` | **0** | 0 | 0 | 0 | 0 | 0 | 0 |
| **合計** | **3,234** | **1** | **3** | **1** | **7** | **206** | **129** |

### 3.2 全部命中之人工複核 —— **真命中 0**

| 標的 | 命中 | 複核結果 |
|---|---:|---|
| `OFF2` | 1 | **本 feature 自身**（`Disclaimer screen`）之草稿列 —— R-PMH5 所證之 037 機械搬運（`I` 欄為 `Requirement Description`）。**是來源自身，不是覆蓋。** |
| `off road` | 3 | 1 同上；另 **2 為 `Off Road Pages`** —— Home 之 `NR1L-CoreHMI-Home-126`（Available Widgets List，逐字「`Suspension * | Off Road Pages HMI | High and Low`」）與 MBAD 之 `NR1L-CoreHMI-MBAD-151`（Favorites 預設清單，逐字「`specialty features such as Off Road Pages, Performance Pages…`」）。**是 app／widget 名稱，非 power moding 行為。** |
| `Off Road+` | 1 | 同上，本 feature 自身之草稿列（`OFF1.)` 之敘述） |
| `Power Off State` | 7 | **全部在本 feature 自身之草稿列**（`PITA5`／`PITA6` 等） |
| `launch` | 206 | 無一與「自 Power Off State 啟動 app」相關（Engineering Mode 佔 172，為其自身之啟動流程） |
| `hard control` | 129 | **全部為 ICS hardcontrols 之調台／空調操作**（AMFM／SXM 之 tune、Comfort 之 fan/temperature、MBAD 之 climate popup） |

### 3.3 結論句（依 R-PMH20 限定量詞）

> **本次量測之 16 個交付件（3,234 資料列，量測時點
> `2026-08-24T11:06:22+0800`）中，`SWE1-HMI-PM-028` 所指之
> Off Road+ power moding 行為零命中。**

**停止條件 8 未觸發**（無任一他 feature 已涵蓋）。

A-PMH13 之量詞由「`features/power` 之 284 列」**擴為
「母體 16 個交付件之 3,234 列」**，已更新於 `ANOMALIES.md`。

### 3.4 §二之 283/284 口徑註 —— **已結案**

分析層以 03 包 §2 之既有量測解明：

| 口徑 | 值 |
|---|---|
| `D` 欄非空之**資料列數** | **284** |
| 其中具 `Test Group` 之列（＝ **TC 數**） | **283** |
| 留白列（`SWE-PM-089`，有 req id 無 TC） | **1** |

**兩個數字都對，量的是不同東西。** 本則之查證以資料列為分母（284），
其結論不受影響 —— 留白列不含任何 TC 文字。
`ANOMALIES.md` 之口徑註已由「未追」改為**已結案**；
A-PMH13 之 PENDING 狀態自此**僅繫於 `-028` 之處置**。

**未改動 `features/power` 之任何檔案。**

---

## 4. 步驟 3 —— 母本 `Cover 封面` 之複驗（通則 5）

**量測對象**：`forms/…_20260817_ext.xlsx`（SHA256 `6372fb6b…6fb825b2`），
分頁 `Cover 封面`（`dims=A1:H30`，非空 11 格）。

| 04 包 §8.1 所記 | 本輪實測 | 結果 |
|---|---|---|
| `D6` 版本 = `C` | `'C'` | **✅ 相符** |
| `D7` 核准者 = `劉安哲 AllenACLiu` | `'劉安哲 AllenACLiu'` | **✅ 相符** |
| `D8` 審查者 = `張愷霏 ErinKFChang` | `'張愷霏 ErinKFChang'` | **✅ 相符** |
| `C9` 作者**標籤**存在而 `D9` 值為空 | `D9 = None` | **✅ 相符** |

**四項全部相符。停止條件 9 未觸發。**

04 包 §8.1 之記載自此為**被複驗**（非被取代），通則 5 之要求滿足。

**附帶**：`H30 = 'FM-WI-FSM-036-A01'`、`C4`／`C12` 為文件名 ——
此三格 04 包已記，本輪一併複驗相符。

---

## 5. 步驟 4 —— `framework.md` 之 granularity 節

已寫入六項判準、錨點、**分析層實測與執行層複算並列**、逐組共用情境、
以及其限制。

**執行層複算與分析層 07 §三之對照**：

| 項 | 分析層 | 執行層複算 | 一致 |
|---|---|---|---|
| 組數／48 | 8，0.17 | 8，**0.1667** | ✅ |
| 最小組 | 3 | **3** | ✅ |
| 最大組 | 9，— | **9，0.1875** | ✅ |
| 收容簇 | 零命中 | **零命中** | ✅ |
| 全落區間 | [3, 9] | **[3, 9]** | ✅ |
| 平均 | 6.0 | **6.0** | ✅ |
| **標準差** | **2.2** | **母體 2.06／樣本 2.20** | **口徑差異，見下** |

**唯一之數值差異為標準差**：分析層之 2.2 為**樣本標準差**（`stdev`），
執行層另算**母體標準差**（`pstdev` = 2.06）。**兩者皆對，量的是不同東西**
—— 此 8 組為全集而非樣本，故 `pstdev` 較切題。
**不影響任何判準之通過與否**（標準差非任一錨點之判準）。
二值已於 `framework.md` 並列記明。

**限制已照錄**：本檢查驗的是 **leaf 分布**，不是 TC 分布；
TC 生成後某組暴增則須重驗。**已列入 `framework.md` 之未決表為
「granularity 之重驗 —— Phase 4」。**

**Test Set #2 仍記 `<PENDING Q11>`，未預填**（`framework.md` 內出現 3 處）。

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **`Vehicle Settings/VF230_V1_R5` 之資料列為 0，其「零命中」是空洞的。**
   §3.1 表中該檔 3,234 之貢獻為 **0 列** —— 它是一份空白工作簿。
   **把它計入「16 個交付件」之分母，會讓結論看起來比實際強。**
   誠實之陳述應為：**15 個有內容之交付件（3,234 列）零命中，
   另 1 個為空白工作簿無從命中。** §3.3 之結論句未作此區分，
   **此為本包之口徑瑕疵，具名於此。**

2. **`Engineering Mode` 之兩候選被同時計入 3,234 列。** 二者為同一交付夾
   之兩個版本（527 + 211 = 738 列），**其內容大量重疊**，
   計入分母會重複計算。若只取一份，分母應為 2,707 或 3,023。
   **零命中之結論不受影響**（兩份皆 0），但**分母之數字被灌水**。

3. **檢索僅及於七個欄位之文字。** 未檢索 `Remarks`(AI)／`Design Method`／
   車型欄等。若某 feature 把「此項由 CFTS009 涵蓋」寫在 `Remarks`，
   本次檢索**看不到**。**盲區已聲明（R-G11），未處置。**

4. **`framework.md` 之 granularity 檢查未含 must-hit 錨點。**
   07 §三與本輪複算皆只有 **must-not-hit**（過細／過粗之反例）。
   **一個全部由 must-not-hit 構成之檢查，無法區分「判準有效」與
   「判準對所有東西都通過」**（R-G9 之同一形狀，方向相反）。
   建議補一個 must-hit：例如「若把 8 組併為 1 組，過粗判準須 FAIL」。
   **本包未補**（granularity 屬分析層）。

---

## 7. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— Test Set #2 未預填 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | 步驟 5 之母體 ≠ 16 | **未觸發** —— **16**，平手夾 1 個並列未擇一 |
| 8 | 擴查發現任一他 feature 已涵蓋 `-028` | **未觸發** —— 全部命中經人工複核，**真命中 0** |
| 9 | 步驟 3 之複驗與 04 包 §8.1 不符 | **未觸發** —— 四項全符 |

---

## 8. 建議之 commit 訊息與 pathspec（**未執行**）

> ⚠ **06 包尚未提交** —— 其異動仍在工作區。下列 pathspec **含 06 與 07 兩包**
> 之檔案；若欲分兩次提交，06 之清單見上繳 06 §8。

```
feat(power_moding): packages 06-07 — layer 2 verified, granularity pass, CFTS009 gap widened
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/RULINGS.md \
           features/power_moding/framework.md \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/06_framework_proposal.md \
           features/power_moding/docs/handoff/07_gap_widening.md \
           features/power_moding/docs/upstream/06_framework_proposal.md \
           features/power_moding/docs/upstream/07_gap_widening.md

git commit -- （同上清單）
```

- **未觸及任何他 feature 之檔案**（禁止項）—— `features/power`、
  `features/comfort` 等本輪異動皆為 **0**。
- `feature.yaml`／`DECISIONS.md`／`PLAYBOOK.md` **本輪未改**（Layer 2 未定版）。
- `scripts/new_feature.py` 未改（禁止項仍在）。
- pathspec 逐項寫全名（R-PMH3(c)）。
- **執行層未執行任何改狀態之 git 指令**（R-G5）。

### 8.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | **無** | **0** |
| **改狀態 git** | **無** | **0** |

---

## 9. 待 Pei 裁定

| # | 事項 | 阻斷 |
|---|---|---|
| **Q11** | Test Set #2 之命名（甲／乙／丙） | **是** —— Layer 2 定版 |
| **A-PMH13** | `-028` 之處置 —— 分析層提案 **(ii)＋(iii) 併行且該列仍寫入工作簿並揭露**（比照 R-VF12）。**擴查後其「全案缺口」之判定已由 16 個交付件佐證** | 否，Phase 4 前 |
| **Q10** | `Product Document 記錄封面頁` —— 分析層提案**不填**；語料 12/16 有填 | 否，Phase 7 前 |
| — | §6 第 4 項：granularity 檢查是否補 must-hit 錨點 | 否 |
| — | A-PMH06 canon 層（`new_feature.py` 樣板） | 否，PENDING-CANON |
