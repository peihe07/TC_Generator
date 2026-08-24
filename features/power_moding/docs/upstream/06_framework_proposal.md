# 上繳包 06 —— 兩項停止條件之處置、Layer 2 複算與跨規格缺口

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/06_framework_proposal.md`
- 前一包：[upstream/05_corpus_fix_and_framework_prep.md](05_corpus_fix_and_framework_prep.md)
- 執行狀態：**步驟 1–5 全部執行完畢。九條停止條件全未觸發。**
  **零寫回工作簿**；git 指令零次；**未修改 `features/power` 之任何檔案**。

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH28 | 多層目錄之交付夾判準（取最上層） | 390 | `42020936a93e1fcd` | `42020936a93e1fcd` | 逐字相符 |
| R-PMH29 | 不確定性以敏感度處置，量測全部候選 | 370 | `9d97e3adc5136862` | `9d97e3adc5136862` | 逐字相符 |
| R-PMH30 | 母體揭露須含量測時點 | 174 | `a1af90628c847c78` | `a1af90628c847c78` | 逐字相符 |
| R-PMH31 | (b) 清單移除 `_Rebuilt` 與 `(done)` | 286 | `3140f6236bf98b33` | `3140f6236bf98b33` | 逐字相符 |

### 1.1 R-PMH27 勘誤附註之撤除證明（原文 SHA256 未變）

| 條號 | SHA256（前 16） | 與前包所記 |
|---|---|---|
| **R-PMH27** | **`e6e14fc0a96c1ccc`** | 相同（05b 包） |
| R-PMH19 | `cbdeed8b8bc0774b` | 相同（04 包） |
| R-PMH10 | `885070968235b262` | 相同（02 包） |

R-PMH27 條後之勘誤附註（「母體應為 17」）**已撤除**，改記
「經 R-PMH28 定案，母體 16，原載數字成立」，並載明差異之歸屬
（分析層之列舉遺漏 ＋ R-PMH24 (a′) 之缺口）與
「執行層之停止條件 7 為**正確觸發**」。

R-PMH19 條後另加**附註二**：(b) 依 R-PMH31 收斂、揭露義務依 R-PMH30
增列量測時點；(a) 已由 R-PMH24 取代。**四處附註皆置於 fenced block 之外。**

---

## 2. 步驟 2 —— 母體重算：**16**（停止條件 7 未觸發）

### 2.1 量測時點（R-PMH30）

**`2026-08-24T10:35:05+0800`**

（05 包之量測時點為 `2026-08-24` 稍早；04 包為 `2026-08-23`。
候選數 28 → 32 之變動即發生於 04 與 05 之間，成因見 05 包 §2.1。）

### 2.2 篩選（R-PMH24 ＋ R-PMH28 ＋ R-PMH31）

| 階段 | 檔數 |
|---|---|
| 候選全集 | 32 |
| (a′) 位於用途目錄下 | 7 |
| (b) 中間態標記（**R-PMH31 收斂後之六項**） | **3** |
| **R-PMH28 下層目錄** | **2** |
| (c) 同夾舊版 | 4 |
| **母體** | **16** ✅ |

**交付夾 16 個**：`AM:FM`／`Audio Management `／`Climate Control Interface`／
`Connection Manager`／`Core HMI/HomeHMI`／`Core HMI/Menu Bar and AppDrawer`／
`Core HMI/Notifications HMI`／`Disclaimer screen`／`Engineering Mode`／
`Power Management`／`Privacy Mode`／`SiriusXM`／`Time Management`／
`User Profiles`／`Vehicle Settings/CFTS044`／`Vehicle Settings/VF230_V1_R5`

**`Engineering Mode/App Team Effort` 已不再是獨立交付夾**（R-PMH28）。

### 2.3 排除清單逐項反向覆核（16 項，R-PMH24 之義務）

| # | 檔（相對 `ASW-R2/`） | 排除理由 | 理由是否成立 |
|---:|---|---|---|
| 1 | `Core HMI/Notifications HMI/…_20260303.xlsx` | (c) 同夾舊版 | **成立** |
| 2 | `Core HMI/Notifications HMI/…_20260309(Review).xlsx` | (b) `(Review)` | **成立** |
| 3 | `Engineering Mode/App Team Effort/…_CFTS011_EngMode.xlsx` | **R-PMH28 下層目錄** | **成立** —— 新理由，取代 05 包之「(a) 深度」 |
| 4 | `…/App Team Effort/…_20251222(Refine).xlsx` | (b) `(Refine)` | **成立** |
| 5 | `…/App Team Effort/…_20260129(Revise).xlsx` | (b) `(Revise)` | **成立** |
| 6 | `…/App Team Effort/…_20260416(done).xlsx` | **R-PMH28 下層目錄** | **成立** —— 05 包所指之「(b) 措辭與事實相反」已由 R-PMH31 移除該項，改由本條排除 |
| 7 | `Engineering Mode/…_EngMode_20260429.xlsx` | (c) 同夾舊版 | **成立** |
| 8 | `Engineering Mode/…_EngMode_20260816_Rebuilt.xlsx` | **(c) 同夾舊版** | **成立，惟其 tie-break 未定 —— 見 §2.4** |
| 9 | `Power Management/…_20260820.xlsx` | (c) 同夾舊版 | **成立** |
| 10–14 | `Vehicle Settings/CFTS044/REF/` 之 5 檔 | (a′) `REF` | **成立** |
| 15 | `Vehicle Settings/VF230_V1_R5/output/…` | (a′) `output` | **成立** |
| 16 | `…/output/validation/…` | (a′) `output/validation` | **成立** |

**16 項之理由全部成立。停止條件 8 未觸發。**

### 2.4 ⚠ 新發現：(c) 在 `Engineering Mode` 遇到**平手**，而條文未定 tie-break

R-PMH31 把 `_Rebuilt` 自 (b) 移除後，該檔改由 **(c) 同夾舊版**排除。
但 (c) 之判準逐字為「取**檔名日期最大**之一份」，而該夾兩檔：

| 檔 | 檔名日期 | 資料列 |
|---|---|---:|
| `…_EngeeringMode_20260816.xlsx` | **20260816** | 211 |
| `…_EngMode_20260816_Rebuilt.xlsx` | **20260816** | 527 |

**日期相同 —— (c) 無鑑別力。** 本輪實際入母體者為
`EngeeringMode_20260816`，**其取捨由排序之實作細節決定，非由條文決定**。

**依 R-PMH29 之敏感度處置**（量測全部候選，本輪獨立複驗）：

| 候選 | 分頁 | 欄數 | `Cover!D6` | 資料列 | `D3` | `D4` | `D5` |
|---|---|---:|---|---:|---|---|---|
| `EngeeringMode_20260816` | `…&Result` | 35 | `A` | 211 | 空 | 空 | **空** |
| `_Rebuilt_20260816` | `…&Result` | 35 | `A` | 527 | 空 | 空 | **空** |

兩候選之 `(D3, D4, D5)` **相異組合數 = 1**（皆 `(None, None, None)`）。

> **敏感度陳述（R-PMH29(a)）**：**Q3 之結論對 (c) 之 tie-break 不敏感** ——
> 該夾恆計為「`D5` 空」一份。**該不確定性不必解決，但其存在已具名記載。**

**惟須指出**：R-PMH29 保證的是「**本次結論**不敏感」，不是「(c) 有 tie-break」。
**日後若有其他判準落在該夾，(c) 仍會給不出答案。** 建議 (c) 補一句
tie-break（例如「日期相同者取資料列較多之一份」或「取 mtime 較晚者」）——
**本包不自行補，列為待裁。**

---

## 3. 步驟 3 —— Layer 2 之機器複算（停止條件 8 未觸發）

以 `data/layer3_sections.tsv` 重算 06 §5.2 之逐 leaf 分配：

| 項 | 結果 |
|---|---|
| TSV leaf 數 | **48** |
| 提案分配總數 | **48** |
| 提案內重複 | **0** |
| 提案有而 TSV 無 | **無** |
| TSV 有而提案無 | **無** |
| **R-G10 餘數** | **48 − 48 = 0** |

| Test Set | §5.1 | 實算 | 相符 | Layer 3（由 TSV 反推） |
|---|---:|---:|:--:|---|
| Splash Screen | 3 | 3 | ✅ | 7.1, 7.9 |
| **#2（待命名）** | 7 | 7 | ✅ | 7.1, 7.2, 7.3, 7.4, 10.4 |
| Startup Animation | 9 | 9 | ✅ | 7.5, 7.5.1, 7.6, 7.7, 7.8 |
| Startup Sounds | 6 | 6 | ✅ | 8.1, 8.2, 8.2.1, 8.2.2, 8.2.3, 8.3 |
| Power Transitions | 7 | 7 | ✅ | 7.1.1, 9.1, 10.5 |
| Power Off Behavior | 8 | 8 | ✅ | 10.1, 10.2, 10.3, 10.4, 10.6, 10.7 |
| Voice Assistant Key | 5 | 5 | ✅ | 11.1 |
| Off Road Plus | 3 | 3 | ✅ | 12.1, 12.2, 12.3 |

**八組全部相符，無須以 TSV 覆蓋提案。**

### 3.1 §5.3 三處切法之 TSV 複驗

| # | 提案之依據 | TSV 實測 |
|---|---|---|
| 1 | 7.1 依 FROP 拆兩組 | `001-01`／`001-02` 之 FROP = `Customizable Splash Screen / Animations`；`001-03`／`-04`／`-05` = `Disclaimer screen` **✅** |
| 2 | 10.4 依 FROP 拆兩組 | `022-01` = `Climate Control`；`022-02` = `Disclaimer screen` **✅** |
| 3 | 章 9 五 leaf 同歸一組 | 五者皆 outline `9.1`、`pdf_page` 皆 **p9**；FROP 四值（Power Management／FOTA Via Wi-fi ×2／WiFi／EV/PHEV Pages）**✅** |

前二者為**上游 RD 之切法**（037 `FROP` 欄），非 TC 作者重新分解（canon §8.2）。

### 3.2 `framework.md` 已產出

含 Layer 1（`Disclaimer screen`，附 R-PMH18 之大小寫警語）、
Layer 2（8 組，**#2 記 `<PENDING Q11>`，未預填**）、
Layer 3（章層對照表 ＋ 指向 `data/layer3_sections.tsv`）、
三處切法之依據與其 TSV 複驗、未決項表。

**狀態標為「未定版」** —— Q11 未裁前不得視為定版。

---

## 4. 步驟 4 —— A-PMH13：`features/power` 之涵蓋查證 → **零命中**

**量測對象**：`ASW-R2/Power Management/…_PowerManagement_20260821.xlsx`
（R-PMH24 母體之該夾交付件），分頁 `Test Case Specification&Result`。
**唯讀開啟；未修改 `features/power` 之任何檔案。**

**實測 284 條**（非 06 §六所稱之 283 —— 口徑差異見下）。

| 標的 | 檢索式 | 命中 |
|---|---|---:|
| 12.2（`-028`）本身 | `OFF2` | **0** |
| 12.1：Off Road state 下按 Off Road+ 不喚醒 | `off[\s\-_]*road` | **0** |
| 同上 | `hard control` | **0** |
| 同上 | `Power Button On` | **0** |
| 同上 | `wake\s*up` | 1 → **人工複核不相關** |
| 12.3：Power Off State 啟動 app 時靜音 | `Power Off State` | **0** |
| 同上 | `launch.*app` | **0** |
| 同上 | `\bmute` | 9 → **皆非本標的** |

唯一之 `wake up` 命中為 `NR1L-PowerManagement-233`，其 Test Item 逐字為
「The HU shall skip start-up animation … until the next CAN wakeup cycle …」，
Test Set 為 `Startup Display`，`spec_reference` 為
`CFTS009-4941301`／`CFTS009-4941941` —— **與 Off Road+ 無關**。

**佐證**：該 284 條之 `specification_reference` 相異前綴僅
**`CFTS009`／`CFTS010`**；Test Set 為 `Power State`(148)／
`Startup Display`(59)／`Branding and Theme`(34)／`Timeout Settings`(26)／
`Power Down`(16)／(空)(1) —— **無任何 Off Road 相關之 Test Set**。

### 4.1 **06 §六之前提不成立**

§六逐字：「**若已涵蓋，(ii) 成立且無缺口；若未涵蓋，則為真缺口。**」

**實測為未涵蓋 → 這是一個真缺口。** 且 (ii) 之形態因而改變：
原設想為「已被他 feature 涵蓋，故本 feature 不重複」，
實測為「**兩邊都沒有**」。若仍採 (ii)，其記載須為
「out of scope 且 `features/power` 亦未涵蓋 → 全案缺口」，
而非「已由他 feature 涵蓋」。**執行層不裁定 (i)/(ii)/(iii)。**

### 4.2 口徑差異：283 vs 284（R-G8）

06 §六稱「已交付 283 條」，本包實測 **284**（分母：`D` 欄非空之資料列）。
差 1 之成因未追。**本 feature 不改他 feature 之數字，僅具名其差異。**

### 4.3 範圍限定 —— 本則只涉一個 leaf

`-027`（12.1「不喚醒」）與 `-029`（12.3「靜音」）**本身含可驗證行為**，
不受影響，仍在 Test Set `Off Road Plus` 內正常生成。
**A-PMH13 只涉 `-028`。**

已登記於 `ANOMALIES.md`（A-PMH13，PENDING），含查證表、口徑註、
三種處置之並列與 §4.1 之形態更正。

---

## 5. 步驟 5 —— Q10 之影響評估（只列不改）

### 5.1 母本之 `Product Document 記錄封面頁` 結構

| 項 | 值 |
|---|---|
| `dims` | `A1:H16` |
| 合併 | `A1:D1`／`E1:H1`／`B3:D3`／`B4:D4`／`B5:D5`／`B6:D6`／**`B7:D7`**／`B8:D8`／`A11:D11` |
| DV | **`B7:C7`**，`type=list`，`allowBlank=1`，`formula1=`**`"Confidential, Top Secret"`** |
| 母本之值 | **標籤列（A3–A8、A12–D12）有值，B 欄之值全空** |

⚠ **DV 之 sqref 為 `B7:C7`，而合併範圍為 `B7:D7`** ——
DV 不覆蓋 `D7`。此為表單層之不一致（與 A-PMH12 同型：sqref 與實際欄範圍不符）。
**只登記，本包不處置。**

### 5.2 母體 16 檔之填寫實況 —— **不只 `B7`，是整張分頁**

| 交付夾 | B3 專案 | B4 文件名 | B5 版本 | B6 部門 | **B7 分類** | B8 日期 | 修訂列 |
|---|---|---|---|---|---|---|---:|
| `AM:FM` | `NR1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 有 | 1 |
| `Audio Management ` | `NR1L` | 空 | `V1.0` | `SW Testing` | **`Confidential`** | 空 | 1 |
| `Climate Control Interface` | 空 | 空 | 空 | 空 | **空** | 空 | 0 |
| `Connection Manager` | `new R1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 有 | 1 |
| `Core HMI/HomeHMI` | `new R1L` | 空 | `V1.0` | `SW Testing` | **`Confidential`** | 空 | 1 |
| `Core HMI/Menu Bar and AppDrawer` | `new R1L` | 空 | `V1.0` | `SW Testing` | **`Confidential`** | 空 | 1 |
| `Core HMI/Notifications HMI` | `new R1L` | 有 | `Initial` | `SW Testing` | **`Confidential`** | 有 | 1 |
| **`Disclaimer screen`（客戶那份）** | `new R1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 有 | 1 |
| `Engineering Mode` | `new R1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 有 | 1 |
| `Power Management` | `new R1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 有 | 1 |
| `Privacy Mode` | 空 | 空 | 空 | 空 | **空** | 空 | 0 |
| `SiriusXM` | `NR1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 有 | 1 |
| `Time Management` | 空 | 空 | 空 | 空 | **空** | 空 | 0 |
| `User Profiles` | 空 | 空 | 空 | 空 | **空** | 空 | 0 |
| `Vehicle Settings/CFTS044` | `new R1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 空 | 1 |
| `Vehicle Settings/VF230_V1_R5` | `NR1L` | 有 | `V1.0` | `SW Testing` | **`Confidential`** | 空 | 1 |

**`B7` 非空 12/16**，與 05 包所報相符。

**兩項本包新見**：

1. **這是全有全無**：12 個填的，其 B3／B5／B6／B7 與修訂列**都有值**；
   4 個空的，**整張分頁一格未填**。**故 Q10 之範圍不是「一格」，
   是「一張分頁」** —— 06 §七所述之「`B7`」低估了範圍。
2. **未填之 4 個為 `Climate Control Interface`／`Privacy Mode`／
   `Time Management`／`User Profiles`** —— 恰為 05 包 §6 所測 `B7` 為空者，
   兩次量測一致。**`Power Management` 有填**，故並非「本 repo 產出者皆未填」。

### 5.3 若 Q10 裁為「須填」，`feature.yaml` 之 `write_back` 需增補之項目

**只列不改。** 現行 `write_back` 只描述 `Test Case Specification 測試用例規範`
一個分頁，其 `first_row: 10`／`mode: append` 皆為資料列語意，**不適用於封面頁**。

| # | 需增補之項目 | 內容 | 備註 |
|---|---|---|---|
| 1 | 目標分頁 | `Product Document 記錄封面頁` | 現行 `workbook.sheet` 為單值，須改為可容多分頁 |
| 2 | 寫入模式 | **具名儲存格**（非 append） | 與現行 `mode: append` 為不同語意，須另立鍵 |
| 3 | `B3` 專案代號 | 語料 12 者用 `new R1L`(8)／`NR1L`(4) | **兩種寫法並存，須 Pei 指定** |
| 4 | `B4` 文件名稱 | 語料 12 者中 8 者有值（本 036 之檔名） | 依 **R-PMH26(d)**，若取檔名即依賴上游命名 —— **須改以其他方式指稱或由 Pei 給定** |
| 5 | `B5` 版本 | `V1.0`(11)／`Initial`(1) | 須 Pei 指定 |
| 6 | `B6` 部門 | `SW Testing`（12/12 一致） | **唯一無歧義者** |
| 7 | `B7` 分類 | `Confidential`（12/12 一致） | **受 DV 約束**（`"Confidential, Top Secret"`）；**注意 DV sqref 為 `B7:C7` 而合併為 `B7:D7`** |
| 8 | `B8` 日期 | 格式不一（`2026.8.10`／`2026.02.`／`2026`／空） | 須 Pei 指定格式 |
| 9 | `A13:D13` 修訂列 | 版本／修訂內容／作者／日期 | **與 `Cover 封面`／`ChangeHistory` 之關係未查** |
| 10 | **DV 約束之檢查** | `B7` 之寫入須驗其在 `"Confidential, Top Secret"` 內 | 現行 `check_write_back.py` 三項**皆不涵蓋封面頁** |
| 11 | **R-PMH23 之交互** | 客戶那份之封面三頁**禁用** | 故值不得自客戶那份複製，須另有來源 |

**執行層之判斷（不裁定）**：11 項中有 **5 項須 Pei 給定字串**（#3/#4/#5/#8 與 #9），
**1 項與 R-PMH26(d) 相衝**（#4 取檔名即依賴上游命名），
**1 項需擴充現行機器檢查**（#10）。**Q10 之成本高於「填一格」。**

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **(c) 之 tie-break 未定，本包未補**（§2.4）。R-PMH29 保證的是本次結論
   不敏感，**不是 (c) 有 tie-break**。日後若有其他判準落在
   `Engineering Mode` 夾，(c) 仍給不出答案。**建議補一句，本包不自行補。**

2. **`framework.md` 之 Layer 2 未經 canon §4.1.3 之過細／過粗檢查。**
   R-VF44 之前例（他 feature）逐項驗了「過細否（set 數／平均／最小）
   ／過粗否（無收容簇）」。**本包只驗了計數與餘數，未驗 granularity** ——
   因 06 §5 明令「不定 granularity」屬分析層。惟**定版前該檢查須有人做**。
   本 feature 之數字供對照：8 set／平均 6.0／最小 3／最大 9。

3. **A-PMH13 之查證只做了 `features/power`。** CFTS009 之行為是否落在
   **其他** feature（例如 `Core HMI`、`Notifications`）之交付件內，**未查**。
   零命中之結論**僅限於 `features/power` 之 284 條**（R-PMH20 之量詞限制）。

4. **Q10 §5.3 之第 9 項未查** —— `Product Document` 之修訂列與
   `Cover 封面`／`ChangeHistory 修訂履歷` 之關係。三者皆有「版本」與
   「修訂」語意，**是否須一致、由誰主導，未查**。若 Q10 裁為須填，
   這是下一個會冒出來的問題。

5. **母本之 `Cover 封面` 於本輪未複驗。** 04 包 §8.1 測過（`D6=C`、
   核准者／審查者有值、作者欄空），**本輪未重測** —— 依通則 5，
   §5.3 之 #9 所涉之「三者關係」中，`Cover` 那一面是**被取代而非被複驗**。

---

## 7. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發（§2.4 之 tie-break 缺口已具名，不阻斷本輪） |
| 5 | 造值壓力 | 未觸發 —— `framework.md` 之 Test Set #2 記 `<PENDING Q11>`，未預填 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | 步驟 2 之母體 ≠ 16 | **未觸發** —— **16** |
| 8 | Layer 2 複算與 §5.2 不符 | **未觸發** —— 48/48、八組全符、餘數 0 |
| 9 | `features/power` 之涵蓋狀態無法判定 | **未觸發** —— 判定為**零命中**（既非「無法判定」） |

---

## 8. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 06 — corpus 16 confirmed, layer 2 verified, CFTS009 gap found
```

```
git add -- features/power_moding/ANOMALIES.md \
           features/power_moding/RULINGS.md \
           features/power_moding/framework.md \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/06_framework_proposal.md \
           features/power_moding/docs/upstream/06_framework_proposal.md

git commit -- features/power_moding/ANOMALIES.md \
              features/power_moding/RULINGS.md \
              features/power_moding/framework.md \
              features/power_moding/docs/INDEX.md \
              features/power_moding/docs/handoff/06_framework_proposal.md \
              features/power_moding/docs/upstream/06_framework_proposal.md
```

- **未觸及 `features/power` 之任何檔案**（禁止項），亦未觸及本 feature 目錄以外者。
- `feature.yaml`／`DECISIONS.md`／`PLAYBOOK.md` **本輪未改** ——
  Layer 2 未定版（Q11），不宜先落 `test_set` 相關之值。
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
| **Q11** | Test Set #2 之命名（甲 `Disclaimer Screen`／乙 `Acceptance Screen`／丙 併入 Splash Screen） | **是** —— Layer 2 定版 |
| **A-PMH13** | `-028` 之處置 (i)/(ii)/(iii) —— **查證後為真缺口，(ii) 之形態已變**（§4.1） | 否，Phase 4 前 |
| **Q10** | `Product Document 記錄封面頁` —— **範圍是一張分頁而非一格**，11 項增補中 5 項須 Pei 給定字串、1 項與 R-PMH26(d) 相衝 | 否，Phase 7 前 |
| — | (c) 之 tie-break 是否補（§2.4、§6 第 1 項） | 否 |
| — | A-PMH06 canon 層（`new_feature.py` 樣板） | 否，PENDING-CANON |
