# 上繳包 11 — vsm_v42：b2 生成（Park Sense，18 leaf）

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/11_b2_park_sense.md`

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | 規格節 `1.11.1.1.29` 切出；18 leaf × 1 TC 生成；`generated/b2_park_sense/` 37 檔 |
| 核實無誤 | **E38–E45／E56／E86 全過**（E56 **18／18**）；lint 判準預檢 J／K／Q／V／M 全 0；**C hedge 0**（b1 教訓已入自檢） |
| 正確地不動 | b1 凍結件 34 檔 sha8 複驗**不符 0**；未寫工作簿、未建 `delivered/`；同文兩對各出一條不合併；`-051` 未入（非本 test_set） |

**總判：18／18 覆蓋，自檢全綠。三項與下放包所述不符之事實據實回報（第 5 節），皆不影響產出。**

---

## 1. 母體與素材

| 項 | 實測 |
|---|---|
| `leaves.tsv` 之 `test_set = Park Sense` | **21 列** = leaf **18** ＋ `No TC — Heading` **3** |
| 家族分布（leaf） | `PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2` **5**／`Rear Park Sense Volume/ ParkSense Volume` **6**／`Front Park Sense Volume` **7** |
| 與下放包 §二-1 之 5／6／7 | **逐項相符** |
| `-051`（未分類列） | 屬 `Speed Assist`，**不在本 test_set**，自然未入 |

規格節切出：`1.11.1.1.29`（段 **1202–1243**，非空 **39** 段），逐字落
`features/vsm_v42/data/b2_park_sense_spec.md`（含段號，未改寫未省略），切法同 05 包 W-1。

---

## 2. 訊號解析（全數自 v3 ＋ `val_tables_v42.tsv`）

| 訊號 | v3 結果 | 段 3 證據 | `VAL_` |
|---|---|---|---|
| `TELEMATIC_VEHICLE_SETUP.PamAlertMode_Req` | 解得 | `BO_158` | 3 項：`0 = Off`／`1 = Sound`／`2 = Sound_Display` |
| `IPC_VEHICLE_SETUP.PamAlertMode` | 解得 | `BO_1468` | 3 項（同上） |
| `TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req` | 解得 | `BO_158` | 3 項：`0 = Low`／`1 = Medium`／`2 = High` |
| `IPC_VEHICLE_SETUP.PamChimeVolumeRear` | 解得 | `BO_1468` | 3 項（同上） |
| `TELEMATIC_VEHICLE_SETUP.PamChimeVolumeFront_Req` | 解得 | `BO_158` | 3 項（同上） |
| `IPC_VEHICLE_SETUP.PamChimeVolumeFront` | 解得 | `BO_1468` | 3 項（同上） |
| `TLM_Vehicle_Setup_Menu.Info` | **未解得(止於段1)** | — | `PENDING: DR-VL4`（R-P355(c)） |

> **與 b1 之對比**：本批**六個 CAN 訊號全部具備完整 `VAL_` 表**，
> 故**無 b1 之 §K K-1 情形**（`= <raw>` 無 label）。
> **本批之 lint 檢查 P 預期為 0**（b1 為 23）。

### PROXI

| 參數 | 段 1 命中 | 值域 |
|---|---|---|
| `PAM_Configuration` | `PROXI/Format/r516cF/R1 逐字` | `0 = Rear`／`1 = Front And Rear` |
| `CAN node 24 (PAM )`（規格寫法） | **PROXI Format r30 欄 F 之逐字為 `CAN node 24 (PAM/CVADAS)`** | `0 = Absent`／`1 = Present` |

**`CAN node 24 (PAM)` 之處置**：規格原名與 PROXI 實名**不逐字相同**
（規格 `CAN node 24 (PAM )` vs PROXI `CAN node 24 (PAM/CVADAS)`）。
依 **R-13** 保留規格原名書寫 `PROXI CAN node 24 (PAM) = 1 (Present)`，
**PROXI 錨點（r30 欄 F 之逐字與值域）記入該 6 條之 `remarks`，不以 PROXI 實名代入**。

### 值之拼法（R-6）

規格與 037 寫 **`Med`**，DBC `VAL_` label 為 **`Medium`** ——
步驟採 **DBC 寫法**（`= 1 (Medium)`），`test_item` 上半 **verbatim 保留 `Med`**，
`remarks` 逐條註明。涉 `-010`／`-017` 兩條。

---

## 3. 產出

`features/vsm_v42/generated/b2_park_sense/`：18 × `.json` ＋ 18 × `.md` ＋ `INDEX.md` = **37 檔**。
**req_id 18／TC 總數 18／PENDING 項 6**（`-005`／`-012`／`-019` 各 2，皆為 `TLM_Vehicle_Setup_Menu.Info`）。

檔名之 `/` 以 `_` 取代（`SWE1-VC-RearParkSenseVolume/ParkSenseVolume-008` →
`SWE1-VC-RearParkSenseVolume_ParkSenseVolume-008.json`）；**`req_id` 欄內仍為原名**，
`INDEX.md` 亦列原名。**據實記明**（下放包未述檔名規則；b1 之 req_id 無 `/` 故未遇）。

### spec_reference 二型（R-VL19(b)）

| 家族 | 條數 | 錨 |
|---|---|---|
| `PARK SENSE w/o HC…` | **5** | `Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29` |
| `Rear Park Sense Volume/ ParkSense Volume` | **6** | `Sys-RA-VF665_V42_VSM-796`…`-801` |
| `Front Park Sense Volume` | **7** | `Sys-RA-VF665_V42_VSM-803`…`-809` |

**E86：Volume 13 條之 `specification_reference` 全為 `Sys-RA-VF665_V42_VSM-{nnn}` 實名，
非 Sys-RA 者 0，無臆造章節號。** PARK SENSE 5 條全為章節號。
13 條之 `remarks` 逐條註 R-VL19(b) 與其依據（上繳 04 W-8 實測「含 Volume 之標題 0」）。

### 分布

| 項 | 分布 |
|---|---|
| priority | **P2 ×18**（本家族為設定項之顯示與傳遞，不涉安全／開機／音訊輸出等 P0–P1 範疇） |
| design_method | 等價劃分 8／負向測試 3／狀態轉換 3／決策表 2／功能測試 2 |
| `$…$` 使用 | 6 種訊號、32 處，**全數為 v3「解得」** |

---

## 4. 自檢（E38–E45／E56／E86 ＋ lint 判準預檢）

| # | 項 | 實測 | 判 |
|---|---|---|---|
| **E38** | 覆蓋 | leaf 18／有 TC 18／**落空 0** | **過** |
| **E39** | R-S4 括號下半 | 違規 **0**；**全批 18 個下半互不重複**（跨 req_id 亦查） | **過** |
| **E40** | 尾句號 | **0** | **過** |
| **E41** | `[..]`／`'..'`／`<..>` | **0** | **過** |
| **E42** | `$..$` 皆可回溯 v3 解得 | **0** 違規（6 種訊號皆解得） | **過** |
| **E43** | PENDING 格式 | **0** 違規（6 項全為 `PENDING: DR-VL4 <名>`） | **過** |
| **E44** | reasoning 繁中 2–5 句 | **0** 違規 | **過** |
| **E45** | ER／下半 modal | **0** | **過** |
| **E56** | 逐字全等（037 Description） | **18／18** | **過** |
| **E86** | Volume 13 條 spec_ref 全 Sys-RA | 非 Sys-RA **0** | **過** |

### lint 判準預檢（承上繳 09／10 之差集，本批**生成時即納入自檢**）

| 判準 | 實測 |
|---|---|
| **C hedge**（`properly`／`successfully`／… ） | **0** ← **b1 之 `-057` 教訓，本批新增** |
| J 行首大寫 | 0 |
| K CJK 於入簿欄 | 0 |
| Q 不可見字元・行尾空白 | 0 |
| V 行首空白 | 0 |
| M 空欄三態 | 0 |
| Procedure ↔ ER 1:1／步驟數 ≥ 2／`tc_title` 2–14 words | 全過 |
| bus-error 式限測試員送出步 | **0** 違規 |

> **b1 之兩個缺陷（`-057` hedge、`-059` 句內剪接）在本批之對應檢查皆已前置**，
> 且 **E56 首次於生成當輪即攔下三條** —— 見第 5 節。

---

## 5. 三項與下放包所述不符之事實（**據實回報，不自行調和**）

### (甲) 規格節 `1.11.1.1.29` **內含 Volume 二家族之逐字段落**

下放包 §二-2／§二-3 之理由為「**規格無章節標題**」與「**規格無節**」。

**實測**：
- 「無**章節標題**」**成立** —— outline 之 115 個標題段中含 `Volume` 者 **0**
  （段 1216 `Rear Park Sense Volume/ ParkSense Volume` 與段 1229 `Front Park Sense Volume`
  **非 heading style**，故不入 outline）。
- 但「**規格無節**」**不成立** —— 該二家族之需求文本**確實位於節 `1.11.1.1.29` 之內**：
  Rear 段 **1216–1228**、Front 段 **1229–1241**，且與 037 Description 一一對應
  （如段 1220 `TLM shall set "TELEMATIC_VEHICLE_SETUP.PamChimeVolumeRear_Req" B-CAN signal equal to "Low"`）。

**本包之處置**：**依明文施作** —— Volume 13 條之 `specification_reference` 用 Sys-RA 實名（E86 過），
`test_item` verbatim 取 037 Description。
**但該二家族並非「無規格可錨」**，其內容錨得到 `1.11.1.1.29`。
**待裁**：Volume 13 條之 `spec_reference` 是否應改為（或增列）`…_1.11.1.1.29`。
**這會影響交付本之追溯欄**，且 b2 一旦覆核通過即固化。

### (乙) 兩對 037 Description **逐字相同**

| 對 | 內容 |
|---|---|
| `PARKSENSE…-002` ↔ `PARKSENSE…-006` | **逐字相同**（皆為 `CAN node 24 (PAM )` = Present → 顯示 Park Sense Setting）；規格側亦重複（段 1203–1204 與 1214–1215 同文） |
| `RearParkSenseVolume…-008` ↔ `FrontParkSenseVolume-015` | **逐字相同**（皆述 `CAN node 24 (PAM)` 與 `PAM_Configuration` 之取得與判定） |

**處置**：依 §8.2.2 各出一條**不合併**，括號下半逐條區分（E39 全批不重複已證）：
- `-002` 下半 `first`／`-006` 下半 `second …by a second requirement id`；
- `-008` 之條件為 `PAM_Configuration ∈ {0 (Rear), 1 (Front And Rear)}`（規格段 1217 之 OR），
  `-015` 為 `= 1 (Front And Rear)` 單值（規格段 1230 之 AND）—— **二者之 PROXI 條件實質不同**，
  雖 037 文字相同。此差異取自**規格段**，非臆測。

**待裁**（§K K-7）：`-002`／`-006` 之差異規格未述（規格側亦是重複段），
是否為上游之贅列。**未合併、未臆測其差異。**

### (丙) 檔名之 `/`

三個 `Rear Park Sense Volume/ ParkSense Volume` 家族之 `req_id` 含 `/`，
檔名以 `_` 取代（`req_id` 欄與 `INDEX.md` 仍為原名）。下放包未述此規則。

---

## §K 增補

### K-7 —— 兩對 037 Description 逐字相同（見第 5 節乙）

`-002`／`-006` 與 `-008`／`-015`。前者連規格段亦重複，後者之規格條件實質不同。
**同 b1 之 K-2（Fdbk 4／5 同文）之型**。

### K-8 —— 規格之 PROXI 名與 PROXI 表實名不一致

規格：`" CAN node 24 (PAM ) "`（含前後空白）；PROXI Format r30 欄 F：`CAN node 24 (PAM/CVADAS)`。
依 R-13 保留規格原名，PROXI 錨點記 `remarks`。
**待裁**：是否認定為同一參數（其值域 `0 = Absent`／`1 = Present` 與規格之 Present／Absent 相符，
且 PROXI 表中無其他 `node 24` 條目）。

---

## 6. 獨立判斷

1. **E56 於生成當輪攔下三條**（`-004`／`-017`／`-019`）：
   我把 037 原文之排版噪音正規化掉了 —— `-017` 漏了原文之 stray backtick
   （`…PamChimeVolumeFront_Req\``）、`-019` 漏了 `received \`IPC_VEHICLE…` 之 backtick、
   `-004` 把 `**Sound+Display**` 寫成無星號。
   **修法採「程式自原文取子字串」而非手打**，避免同型再犯；修後 18／18。
   > **這正是 b1 `-059` 之同型缺陷**，差別在：b1 是凍結後才被 E56 抓到（需新裁決），
   > **本批在生成當輪即攔下並自修**。E56 之制度化在此見效。
2. **b1 之 hedge 教訓已入本批自檢**（C 檢查），實測 0。
3. **一項本批未遇而 b1 有之風險**：`VAL_` 缺值 —— 本批六訊號皆有完整 `VAL_`，
   故 lint 檢查 P 預期為 0。**惟本批未跑 lint 實跑**（需寫入工作簿，本包禁區），
   仍以預檢代之；**b1 之 P=23 與 I-cross=17 兩項判準問題若未裁，b2 寫回後同樣會出 I-cross 紅**
   （本批 18 條之 ER 同樣不採觀測窗式書寫）。
4. **一項提醒**：本批為 R-VL25(a) 綠色通道計數之**第一批**。
   若覆核零修訂，計 1／3。**但第 5 節之三項與 §K 兩項若導致修訂，計數應歸零** ——
   其判定屬分析層。
5. **未做且指得出理由**：未對 b2 建試驗簿跑 lint —— 下放包明定「不寫工作簿」。

---

## 7. `gate_all.py` 與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 506
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash`** —— 依 R-VL13 記「待 Pei 重生」。
id 級實測：**新增 42／移除 0／`body_sha8` 亦變 0** ——依 R-VL15(c) 判準滿足。
**`R-VL25` 之 `body_sha8` = `0de42ae8`**（`sha8` = `09052fef`）。

**(乙) `canon_refs`** —— 含 `vsm_v42` 者 **3 列**，與上繳 02–10 逐字相同。
> **一項自修**：本包執行中實測為 **4 列** —— 多出者為**上繳 09 之補記所寫之裸節號**
> （`canon §0 第 3 項`，`09_writeback_method.md:202`）。
> 此為本執行層所造，已改為 `FO 第 0 節第 3 項` 並複驗回到 3 列。
> **b2 之 37 個新檔未新增任何一列。**

**(丙)(丁) `gates_tsv`／`lint_paths` = 4** —— 與本線無關，先在。

**無一支肇因於本包之產出。**

---

## 8. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `features/vsm_v42/data/b2_park_sense_spec.md` | **新建**（規格節 1202–1243 逐字，39 非空段） |
| `features/vsm_v42/generated/b2_park_sense/*.json`（18）／`*.md`（18）／`INDEX.md` | **新建**（37 檔） |
| `features/vsm_v42/docs/upstream/09_writeback_method.md` | 一處字面修正（裸節號 → 具名節，見第 7 節乙） |
| `features/vsm_v42/docs/upstream/11_b2_park_sense.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：**`generated/b1_epb/` 全 35 檔（凍結件，34 檔 sha8 複驗不符 0）**、
`sandbox/`（含 `base/` 與 `wb_trial/`）、`delivered/`（未建）、
`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`、`scripts/`、`backend/`、`forms/`、
`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、
`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md, ANOMALIES.md, DECISIONS.md, feature.yaml,
framework.md, data/ 之其餘}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 9. 待 Pei／分析層

1. **第 5 節甲**：Volume 13 條之 `spec_reference` 是否改／增列 `…_1.11.1.1.29`
   —— 規格節內確有其逐字段落，「無節」之理由不成立。**影響交付追溯欄。**
2. **§K K-7**：兩對 037 同文（`-002`/`-006`、`-008`/`-015`）。
3. **§K K-8**：`CAN node 24 (PAM )` 與 PROXI 實名 `CAN node 24 (PAM/CVADAS)`。
4. **綠色通道計數**：本批是否計為乾淨之第 1／3 批（第 6 節 4）。
5. 承前未結：b1 之 `-057` hedge、D／C 欄牴觸、lint 檢查 P 之豁免、I-cross 適用性、
   §K K-1〜K-6、DR 送出、台帳重生、`wb_trial/` 去留。
