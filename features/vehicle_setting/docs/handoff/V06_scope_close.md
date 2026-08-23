# V06 — 不回溯已交付、`not clear` 之處置、leaf 母體定為 627

下放包 **V06**。對應上繳：`docs/upstream/V06_*.md`。
本包新增 **R-VF14／R-VF15／R-VF16**（3 條）、**W-VF16／W-VF17**（2 項工單）、
**DR-30**（1 件草稿）。並修訂 **W-VF14** 之範圍（§5.1）。

裁定依據：Pei 於 2026-08-23 之逐字答覆 ——
**「我不影響已經交付的啊 在這裡的分析就歸屬於現在這份」**（對 V05 §4.2）／
**「not clear就寫not clear」**（對 V05 §4.3）／
**「那就627」**（對 V05 §4.1）。

---

## 2. R-VF14 —— 不回溯已交付；本線之分析歸屬於本份交付

```
R-VF14（回溯之界，Pei 裁定 2026-08-23）

逐字：「我不影響已經交付的啊 在這裡的分析就歸屬於現在這份」。

R-VF13（VC/VM 得作值域來源）**不回溯變更已交付之內容**。
本線（VF230）所生之分析結果**歸屬於本份交付**，不倒灌回既有交付物。

**適用**：
1. 已交付之 TC、已鎖之分級、已送出之 RD-1 項次 —— **一律不因 R-VF13 而變更**。
2. R-VF13 之來源開放，適用於**尚未交付**之 leaf 與其後續產出。
3. A-VS118 之 4 leaf（Part 1，`HSW_Cmd_Tlm`）之 W2→W0 轉換，
   **以其是否已交付為斷**（見 §4.1 之定義問題）。
4. 既有以「值域無來源」判 W1／W2 之 leaf，**不作全面回溯重跑**；
   W-VF14 之掃描降為**存查性**，不觸發任何變更。

**理由（記錄 Pei 之取向）**：交付物之穩定優先於分級之最適。
一條後出之來源規則不應使已定案之交付重新打開。
```

---

## 3. R-VF15 —— 上游自述 `not clear` 者逐字轉錄

```
R-VF15（`not clear` 之處置，Pei 裁定 2026-08-23）

逐字：「not clear就寫not clear」。

037 之 `Verification Criteria`／`Verification Method` 自述 `not clear` 者
（VF230 90 ＋ CFTS044 14 = 104 leaf），其處置為 **逐字轉錄**：

- 於該 TC 之 **Remarks（AH 欄）** 逐字記
  `Upstream Verification Criteria: not clear`（或該欄之實際逐字內容）。
- **不新增 blocker 類別。**
- **不因此開 DR**（本條明示不開；DR-30 另有其事，見 §5.3）。
- **不寫入 `expected_result`／`pre_conditions`／`test_procedure`** ——
  `not clear` 非可觀察之結果，寫入 ER 違反 §6。

**限縮 —— 本條不改變該 leaf 之 writability 路徑**：
該欄為 `not clear` 者，其值域仍依既有路徑（LID／DBC／spec）判定。
若既有路徑亦無值域，仍依既有規則標 `PENDING: DR-{n}` 或判 W2 ——
**`not clear` 本身不是一個新的處置類別，只是一項須被誠實記下的事實。**

R-VF13 第 4 項（`not clear` 之列不得作為值域來源）不變。
```

---

## 4. R-VF16 —— VF230 之 leaf 母體定為 627

```
R-VF16（VF230 之 leaf 母體，Pei 裁定 2026-08-23）

逐字：「那就627」。

VF230 之可測 leaf 母體 = **627**。

A-VS132 之 8 列（037 判 `Heading`、035 判 `Functional Requirement`）
**計入可測 leaf**。其 037 條文逐字為需求形態
（`The HMI layer shall capture the customer selection for …` 5 列／
`HW supplier shall notify the IPC_VEHICLE_SETUP2.* signal via VHAL
interface …` 3 列），八者集中於 SWITCH 族。

627 = 619（037 判 Functional）＋ 8（A-VS132）。

**須具名之後果**：本裁定使本層之 Categorization **與 037 於該 8 列相左**。
037 為權威來源（R1 裁定），故此為**刻意之偏離，非錯配之修正**：
- `data/vf230_leaves.tsv` 之該 8 列須標欄位註記（如 `source_disagreement=1`），
  **不得靜默併入**，以免後續無從分辨哪 8 列非 037 所判。
- 交付時須揭露該偏離（併入 R-VF12 §2 所令之揭露段落）。
- 已開 **DR-30** 向上游確認（確認型，不阻塞；**Pei 之裁定不待其覆文**）。

**R-VF12 之交付範圍不因此改變** —— 該 8 列本即在 037 之 745 列內。
```

---

## 5. 工單與 DR

### 5.1 W-VF14 之修訂（依 R-VF14 降為存查性）

V05 §5 之 W-VF14 原為「回溯掃描，供 Pei 決定是否重跑」。
**依 R-VF14，其目的改變**：

- 仍執行掃描（兩 feature 分報），**但不產出「應轉之新分級」之建議**。
- 產出改為**存查表**：哪些 leaf 之值域在 VC/VM 欄有解、其現行分級為何、
  **是否已交付**。
- **不觸發任何變更、不改分級、不改 TC。**
- 其價值在於：日後若上游質疑某 leaf 之分級，可證本層知其存在且依 R-VF14 未改。

### 5.2 W-VF16 — 「已交付」之判準（**先於 W-VF14 執行**）

R-VF14 以「已交付」為界，而該詞於本 feature **尚無操作型定義**。

**實測（分析層，2026-08-23）**：CFTS044 之交付路徑 036
（`.../Vehicle Settings/CFTS044/...20260819.xlsx`，分頁
`Test Case Specification 測試用例規範`，列 10–246）：

```
F 測試用例ID 0 ／ G Test Group 0 ／ J 先前條件 0 ／ K 輸入條件 0
O TC Ref ID 0 ／ P Priority 0 ／ R Design Method 0 ／ AA 作者 0 ／ AH 備註 0
（L 191 ／ M 191 為進場時即有之上游文字，非本 pipeline 產出）
```

→ **交付路徑之工作簿目前不含任何本 pipeline 產出之 TC。**

**故「已交付」須裁定其指下列何者**（W-VF16 只列證據，不決）：

  (a) 已寫回交付路徑並 tag 者 —— 依上列實測，Part 1 現為 **0 條**，
      R-VF14 對 Part 1 現階段**無排除效力**
  (b) 已生成並通過 pilot／lint 之批次（batch01–16）—— 排除範圍最大
  (c) 已於 RD-1 送出之項次（第 1–5 項）—— 介於二者之間

**回報**：三種判準各自涵蓋之 leaf 數與 batch 範圍，附實測。
**不自行選定。** 此為交付形式之界定，屬 Pei。

### 5.3 W-VF17 — 627 之落實

1. 重跑 leaf 母體，`data/vf230_leaves.tsv` 619 → **627**，
   該 8 列加註記欄（R-VF16）。
2. **重算 Layer 2 候選之簇數與 leaf 分布**（8 列集中於 SWITCH 族，
   非隨機散布，簇分布必變）。回報與 619 版之逐簇差異。
3. 全庫掃描以 **619** 為母體之既有陳述，逐處列出（**不改**）——
   含 `docs/reports/`、`upstream/V01`、`V02`、`RULINGS.md` 之執行層註。
4. 依 R-VF11，重跑前先對錨點實測：該 8 列之 `swe_id` 為必命中錨點；
   037 判 Heading 且 035 亦判 Heading 之 118 列為必不命中錨點。

### 5.4 DR-30 草稿（確認型，不阻塞，未送出）

```
DR-30（新，Urgency Low —— 037 與 035 於 8 列之 Categorization 相左；
V06 §4 開立）

型別（R-VS45）：型 A —— 規格／分析文件間之不一致。

成對之 anomaly：A-VS132。

VF230 之 037 分報告判為 `Heading` 而 035（SYSRA）判為
`Functional Requirement` 者 8 列，集中於 SWITCH 族
（Power Mode／Type／Hold Last State）。其 037 條文逐字為需求形態：

  The HMI layer shall capture the customer selection for …          （5 列）
  HW supplier shall notify the IPC_VEHICLE_SETUP2.* signal
  via VHAL interface …                                              （3 列）

**請確認**：該 8 列之正確 Categorization 為 `Functional Requirement`
或 `Heading`？

**本層之處置（已定，不待覆文）**：依 Pei 裁定（R-VF16）計入可測 leaf，
母體為 627。該 8 列於 `leaves.tsv` 已加註記，以資分辨。
若上游覆為 `Heading`，本層將於當時另裁是否回退。

**狀態：未送出。**
```

---

## 6. 仍待 Pei 裁定

| 項 | 內容 |
|---|---|
| **「已交付」之判準** | (a) 已寫回並 tag／(b) 已過 pilot 之批次／(c) 已於 RD-1 送出 —— 待 W-VF16 之實測後裁 |
| **Layer 2 起點與時點** | **A-VS132 已由 R-VF16 解除阻塞**。執行層建議以 037 之 11 份分報告族群為起點；惟簇數須依 627 重算（W-VF17(2)）後方有實數可據 |
| **DR-28／DR-29／DR-30** | 三件皆未送出 |

---

## 7. 本包產生之新條文清單（自檢）

| 編號 | 型別 | 是否以可貼入區塊出現 |
|---|---|---|
| R-VF14（不回溯已交付；本線分析歸屬本份交付） | Pei 裁定 | ✅ §2 |
| R-VF15（`not clear` 逐字轉錄至 Remarks；不新增 blocker 類；不開 DR） | Pei 裁定 | ✅ §3 |
| R-VF16（leaf 母體 627；8 列為刻意偏離，須註記並揭露） | Pei 裁定 | ✅ §4 |
| DR-30（037 vs 035 之 8 列 Categorization） | DR 草稿 | ✅ §5.4 |

**工單**：W-VF14（修訂為存查性）／W-VF16（「已交付」判準之證據，**先行**）／
W-VF17（627 落實＋Layer 2 簇數重算＋619 陳述清單，含錨點前置）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
