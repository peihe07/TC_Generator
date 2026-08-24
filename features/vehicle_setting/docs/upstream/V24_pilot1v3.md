# 上繳 V24 —— pilot #1 v3（五項字串修正 ＋ 自檢依 R-VF69 改寫）

執行層寫入。依據：`docs/handoff/V24_pilot1v2_review.md` §7（W-VF62）。canon §8.2 六節。
**不重跑選池、不改 leaf 集合、不改 `specification_reference`、不改 `reasoning` 之 Priority 段。**

產物：`generated/vf230_pilot1_v3.json`（10 條，`supersedes: vf230_pilot1.json`）

| 項 | 內容 | 狀態 |
|---|---|---|
| D | 逐字轉錄 **R-VF69** 入 RULINGS.md | ✅ |
| **W-VF62(1)** | 刪 `pre_conditions` 第 1 項（Defect A） | ✅ 10/10 |
| **W-VF62(2)** | `check whether` → `check that`（Defect B） | ✅ 10/10 |
| **W-VF62(3)** | 縮短逾 14 字之 `tc_title`（Defect C） | ✅ **4 條**，見 §2.1 |
| **W-VF62(4)** | 查 Part 1 之 UI 標籤引號慣例並依之 | ✅ 見 §1a |
| **W-VF62(5)** | 檔頭 `selection` 計數改 4／6 | ✅ |
| 自檢 | 依 R-VF69 改逐字 pattern ＋ 可失敗性實測 | ✅ 見 §1b |

**接工單前之查核（V19a 之教訓）**：本層於動手前先查 `docs/upstream/` ——
**無 `V24_*.md`**，且 `generated/vf230_pilot1.json` 停在 V23 之 commit `840796a`
未被改動，工作區亦無其 `M`。**確認 W-VF62 尚未有人動，方接手。**

---

## 1. 預期 vs 實測（相符者亦列出）

| # | 項 | 實測 | 判 |
|---|---|---|---|
| 1 | Defect A 之範圍 | `pre_conditions` 第 1 項 `The vehicle is powered and the HU has completed start-up` —— **10/10 皆有**，已刪；餘 PROXI 設定一項，重編為第 1 | 相符 |
| 2 | Defect B 之範圍 | procedure 步驟 3 之 `check whether` —— **10/10**，已改 `check that` | 相符 |
| 3 | **正向／負向之實測**（V24 §7(2) 令以實測為準） | **負向 6**（seq 238–243，`is not displayed`）／**正向 4**（seq 244–247）。V24 §3 修法段所寫之「負向四條／正向三條」與實測不符，**其 §7 按語已預告此點** | 相符（依實測） |
| 4 | **Defect C 之範圍** | **4 條逾 14 字**（241／244／246／247），**非 V24 §4 表所列之 3 條** | **不符，見 §2.1** |
| 5 | 逾字之實測值 | 241 **15**／244 **16**／246 **15**／247 **18** | 247 與 V24 所載之 17 差 1，見 §2.1 |
| 6 | Note 1 檔頭計數 | 原 `P0(a) 3 ／ P0(c) 7`；逐條實測 **P0(a) 4 ／ P0(c) 6**（238／241／244／247 為 P0(a)），已改 | 相符 |
| 7 | 自檢對 v3 | **違規 0** | PASS |
| 8 | 自檢對 v2（錨點） | **違規 36** | ✅ 可失敗 |
| 9 | 人為插入之可失敗實測 | `The HU is powered on` → rc=1 命中 `\bpowered\b`／`\bpower(?:ed)? on\b`；`check whether` → rc=1 命中 `\bcheck whether\b` | ✅ 兩項皆攔 |

### §1a W-VF62(4) —— Part 1 之 UI 標籤引號慣例（實測，逐字回報）

Part 1 已交付 225 條中，procedure／ER 出現雙引號者 **24 條**，其標籤 7 個：

| 標籤 | **其來源條文是否亦加引號** | 實例（逐字） |
|---|---|---|
| `"Driver"` | **是** | `1. Read the labels of the heated and vented seat buttons and record the button carrying "Driver"` |
| `"Passenger"` | **是** | 同上條之對稱列 |
| `"Headrest Dump"` | **否** | `2. Press the "Headrest Dump" softkey button and check that both the left and the right third row …` |
| `"Rear View Camera"` | **否** | `SWE1-VC-ThirdRowHeadrestDump-037` |
| `"Screen Off"` | **否** | `SWE1-VC-ScreenOFF-047` |
| `"Third Row Headrest Dump"` | **否** | `SWE1-VC-ThirdRowHeadrestDump-028` |
| `"Rear Camera"` | **否** | `SWE1-VC-ThirdRowHeadrestDump-041` |

**慣例判定**：**7 個中 5 個之來源條文並未加引號，而 Part 1 仍加** ——
故其慣例為「**逐字螢幕標籤一律加雙引號，不論來源是否加**」。
**非「隨來源」**。

對照：描述性控制元件名**不加**（`the left front heated seat icon` 17×、
`the heated steering wheel icon` 10× 等），其為 Part 1 之另一類。

**本批之十個標籤皆為逐字螢幕標籤**（`Power Tailgate Alert` 等，
其於條文中為 `the X customer setting` 之 X），**故加引號**。
**依 Part 1 慣例，非自創。**

**附記**：本批十條之來源條文中，**僅 seq 247 之條文自身加引號**
（`the "Suspension Service Mode" customer setting`），其餘 9 條未加 ——
**若採「隨來源」之讀法，同一標籤在 241 與 247 會不一致**。
Part 1 之慣例正好避開此問題。

### §1b 自檢依 R-VF69 之改寫（`scripts/vf230_selfcheck_wvf62.py`）

| 舊（概念型） | 新（逐字 pattern） |
|---|---|
| 「Pre-Condition 無系統預設」 | `PRE_FORBIDDEN = [\bpowered\b, \bpower(?:ed)? on\b, \bstart-?up\b, \bbooted\b, \bignition on\b, \bpower cycle\b]` |
| 「procedure 無禁用動詞」 | `VERB_FORBIDDEN = [\bobserve whether\b, \bobserve\b, \bsee if\b, \bcheck whether\b, \bconfirm whether\b, \bverify\b, \bwatch\b, \bmonitor\b, \binspect\b]` |
| 「tc_title 合規」 | `2 <= len(title.split()) <= 14` |
| 「procedure 與 ER 1:1」 | 步數相等 |
| 「檔頭計數正確」 | `f"{cls} {n}" in selection`，其 `n` 自逐條 `priority_class` 重算（canon §5a） |

---

## 2. 不符項目（不自行調和）

### 2.1 **Defect C 之範圍為 4 條，非 V24 §4 所列之 3 條 —— `seq 241` 漏列**

V24 §4 之表列 244（16）／246（15）／247（17），並稱
「**其餘 7 條為 13–14 字，合規**」。

**本層以同一判準實測（空白切分，括號與引號內之詞計入）**：

| seq | V24 所載 | **本層實測** | tc_title |
|---:|---:|---:|---|
| 241 | *（未列，歸入「合規 7 條」）* | **15** | `Suspension Service Mode is not displayed when CAN node 27 (ASM / ASCM) is "Absent"` |
| 244 | 16 | **16** | ✔ 相符 |
| 246 | 15 | **15** | ✔ 相符 |
| 247 | **17** | **18** | 差 1 |

`seq 241` 之切分：`Suspension`／`Service`／`Mode`／`is`／`not`／`displayed`／`when`／
`CAN`／`node`／`27`／`(ASM`／`/`／`ASCM)`／`is`／`"Absent"` = **15**。

**本層之處置：一併縮短 241。** 其與 247 為同一 leaf 之 Absent／Present 對，
**只縮 247 而留 241 為 15 字，該對之標題形式會不一致**。

**不自行調和 V24 之數** —— 上表兩數並列，其判準是否與本層同（例如
`(ASM` 與 `/` 與 `ASCM)` 是否計為三詞），**待分析層確認**。

### 2.2 procedure 之 `listed` 與 ER 之 `displayed` 用詞不一致

修正後：

```
proc 3. Read the Vehicle Settings menu and check that the "X" customer setting is not listed
ER   3. The "X" customer setting is not displayed
```

**V24 §3 只令改 procedure，未令改 ER**，本層照辦而未動 ER。
**惟 §6 之 1:1 於用詞層面因此不齊** —— `listed` 與 `displayed`
於選單語境是否為同一可觀察，本層判其為是（故未改），**但其為本層之判斷**。

**若分析層認為須齊**，其修法為 ER 改 `is not listed`（或 procedure 改
`is not displayed`），**十條皆然，仍屬字串取代**。

### 2.3 縮短後之 `tc_title` 採情境標籤式 —— **Part 1 無此式**

V24 §4 建議「正向三條改用 §4.3(c) 之情境標籤式…**惟須與已交付之 Part 1 慣例一致，
若 Part 1 無此式，改以縮短句式為之**」。

**實測 Part 1 之 225 條 `tc_title`：無一採 `X: Y = "Z"` 之情境標籤式**，
其全為句式（`Heated steering wheel press sends the request signal` 等）。

**故本層未採情境標籤式，改以縮短句式**：

| seq | 修正後 | 字 |
|---:|---|---:|
| 241 | `Suspension Service Mode not displayed: CAN node 27 "Absent"` | 9 |
| 244 | `Power Tailgate Alert displayed and modifiable: CAN node 82 "Present"` | 10 |
| 246 | `Lane Sense Warning displayed and modifiable: Lane_Assist "Active Lane Management"` | 10 |
| 247 | `Suspension Service Mode displayed and modifiable: CAN node 27 "Present"` | 9 |

**其仍含冒號** —— 嚴格說介於句式與標籤式之間。
**具名供裁**：若須全為純句式（無冒號），其修法為
`Suspension Service Mode is not displayed for CAN node 27 Absent`（10 字）之類，
**仍屬字串取代**。

**手足區辨 token 保留**：分割值本身（`"Absent"`／`"Present"`／
`"Active Lane Management"`）與節點號（27／82）皆在標題內。

---

## 3. 結果三分法（canon §8.4）

**已驗相符**

- 五項修正 **10/10** 落實，逐條差異行已列（見本包所附之對照）
- 自檢依 R-VF69 改為逐字 pattern，**對 v3 得 0、對 v2 得 36**，
  且人為插入 `The HU is powered on` 與 `check whether` **各自被攔**（rc=1）
- W-VF62(4) 之慣例判定**以 Part 1 之 7 個標籤實測為據**，
  其中 5 個「來源未加而 Part 1 加」即其判定之關鍵證據
- 選池、leaf 集合、`specification_reference`、`reasoning` 之 Priority 段
  **一字未動**（`supersedes` 記其前版）

**已驗不符**

- §2.1 Defect C 實為 4 條（241 漏列）、247 之字數差 1
- §2.2 `listed` vs `displayed` 之用詞不齊（未改 ER，具名）
- §2.3 縮短式仍含冒號，Part 1 無情境標籤式之先例

**未驗**

- **v3 之十條無一經人讀** —— 本輪之驗證全為機械 pattern
- **`Power cycle the HU` 現只在 procedure 步驟 1** ——
  刪 pre_condition 後，其前置狀態（HU 之初始電源狀態）**不再有任何記載**。
  測試者自何種狀態開始執行步驟 1，**條文與 TC 皆未定**
- **`PRE_FORBIDDEN` 之 pattern 集是否窮盡**，未驗 ——
  R-VF69 給了六個例（`powered`／`power on`／`start-up`／`booted`／
  `ignition on`），本層加 `power cycle` 為第六。
  **其為「已知之禁止串」而非「全部之系統預設表述」**
- 池 621 中其餘 611 條未生成（本輪不生成第 2 批，依 V24 §7）

---

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| # | 條件 | 值 |
|---|---|---|
| 1 | 接工單前之查核 | `ls docs/upstream/V24_*.md`（無）＋ `git log -1 -- generated/vf230_pilot1.json`（`840796a`，V23）＋ `git status`（無 `M`） |
| 2 | 正負向之判定 | `"is not displayed" in tc_title` |
| 3 | tc_title 字數 | `len(title.split())`，括號與引號內之詞計入（V24 §4 之判準） |
| 4 | UI 標籤之取得 | procedure 之 `the ([A-Z][\w /]*?) customer setting` |
| 5 | 加引號之範圍 | `(?<!")<label>(?!") customer setting` —— **只加於 `customer setting` 之前置標籤**，不動 `test_item`（其為條文逐字，R-VS6） |
| 6 | Part 1 之慣例 | 其 225 條之 procedure／ER 掃 `"([A-Z][\w /]+)"`，逐標籤回查其來源條文（`clause_of`）是否亦加引號 |
| 7 | 檔頭計數 | 自逐條 `priority_class` 以 `collections.Counter` 重算（canon §5a：跨處之同一量須自同一來源重算） |
| 8 | 自檢之可失敗實測 | 深複製 v3 → 插入違規 → 寫暫存檔 → `subprocess` 執行自檢，驗 `returncode == 1` |

---

## 5. 本輪新開之 anomaly 與 DR（成對）

**本輪未新開 anomaly，亦未新開 DR。**

§2.1–§2.3 之三項皆為**本包與 V24 之量測／形式落差**，
其標的為 V24 本身之表列與建議，**非產物之缺陷**，故不開號。

**待 Pei 者仍為一項**（V24 §8）：DR-35（A-VF18，`LaneSenseWarning-014`
條文自相矛盾）之送出，與 DR-34 併同處理（R-VF27）。

### R-VS75 之回流（本輪與 Pei 之直接往返）

**本輪無選項式徵詢，亦無新的 Pei 裁定。**
V24 §1 之 verdict（不通過）為 Pei 所裁，**其已循下放包流通**，不屬直接往返。

---

## 6. 獨立判斷（canon §8.2 §6）

**V24 §9 令附「本包是否仍有該驗而未驗者」之獨立判斷。以下即之。**

1. **有，而且就在 R-VF69 自己身上。**
   R-VF69 說「概念型自檢項之通過，只證明實作者之解讀與其自身一致」。
   **而它給的解法是一組 pattern 清單** —— 那份清單本身是概念（「系統預設」）
   的一次**列舉**，**其是否窮盡沒有任何檢查在管**。
   我加了 `power cycle` 作第六個，是因為我看到了；
   **下一個沒被想到的表述（`the ignition is in RUN`、`after a cold boot`）
   會靜默通過。**
   **pattern 化把「解讀之不可檢驗」換成「列舉之不完整」——
   它是嚴格的改善，但不是消除。**

2. **§2.1 那條 `seq 241` 說明了 V24 §2 那段話的力道。**
   V24 §2 說 V23 的自檢第 7 項「執行層據以自檢、回報通過，而系統預設原封未動」。
   **這一輪換成分析層的表列漏了一條** —— 244／246／247 被逐條數過，
   241 被歸進「其餘 7 條合規」而沒數。
   **兩次是同一件事：一個沒有被機械執行的量測，其結果不可靠。**
   241 與 247 是同一 leaf 的 Absent／Present 對，**只縮 247 會讓那對不一致**。

3. **§3 未驗的第二項，我認為是本批最實質的殘留風險。**
   刪掉 `The vehicle is powered and the HU has completed start-up` 是對的
   （canon §4.4 逐字禁之），**但刪完之後，這十條的起始狀態沒有任何記載**。
   步驟 1 是 `Power cycle the HU` —— 從什麼狀態 power cycle？
   canon 禁的是把系統預設**寫進 Pre-Condition**，
   **不是禁止該狀態存在**。若 Part 1 有處理此形態的既有做法，應照之；
   **若沒有，這是一個 canon 與可執行性之間的縫，值得分析層看一眼。**

4. **W-VF62(4) 的答案我有把握，理由是那 5 個「來源未加而 Part 1 加」。**
   如果 Part 1 是「隨來源」，那 5 個就不會加引號。
   **它們加了，所以慣例是「逐字螢幕標籤一律加」。**
   這個判定是可證偽的 —— 分析層若不同意，只要指出那 5 個之中有任何一個
   其來源其實有引號而我測錯了，結論就翻。**測法已列於 §4 條 6。**

5. **本輪沒有動選池、沒有動 leaf、沒有動 reasoning —— 這是對的，但也意味著
   v1→v2 那一輪的實質判斷至今只被覆核過一次。**
   V24 §1 說改善確實發生（成對進入、reasoning 九句各異、
   `specification_reference` 10/10 全解）。
   **那些是 v2 的成果，v3 完全沒碰它們** ——
   所以 v3 通過與否，**不構成對 v2 那些判斷的第二次確認。**
