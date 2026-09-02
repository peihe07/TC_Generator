# 上繳包 14 — vsm_v42：b2 寫回（累積簿 b1＋b2，**未出貨**）

日期：2026-09-02　執行層：Claude Code　授權：Pei「先 b2」
（R-VL25(b) 之寫回預授權涵蓋寫至 `sandbox/`；交付仍待「出貨」）

> 本件無對應之下放包。上繳取號 14（`docs/upstream/` 實測有 00–13）。
> 下放包 13（`13_b2_camera.md`，Camera Gridlines 10 leaf）**未執行**。

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | 累積簿 `sandbox/b2/vsm42_b1b2.xlsx`（35 列）；`writeback_map_b1b2.tsv`；b2 之 J／R 兩缺陷修訂 |
| 核實無誤 | 三斷言全中；回讀 **557 格不符 0**；**列序四道全過**；lint **淨紅 0**；`sandbox/base` sha 不變 |
| 正確地不動 | **未出貨**（`delivered/` 之現件未動、sha 未變）；b1 之 17 條產物一位元未動；`scripts/` 未改 |

**總判：b2 已寫入累積簿且 lint 淨紅 0。惟出貨須先裁一項 —— 依 037 leaf 序排列使已交付之 17 條 TC ID 全數位移（第 2 節）。**

---

## 1. 一項先於寫回之發現：**b2 不能 append**

交付簿之列序判準（`scripts/verify_row_order_74.py`，取自 comfort §6 三道 ＋ ICS 第四道，
源 Pei「Requirement or Design ID 要照順序排」）：

> `row-order-by-reqid`　D 欄自上而下須為 **037 之 leaf 序**（`<` 為違規）

**實測 `leaves.tsv`（＝037 逐列序）之位置**：

| test_set | 037 leaf 序 | 037 來源檔 |
|---|---|---|
| **Park Sense**（b2，18 條） | **#1 – #18** | `parksense` |
| **EPB Maintenance Mode**（b1，17 條） | **#105 – #121** | `sdw` |

即 **b2 在 037 序中排在 b1 之前**。若將 b2 append 至列 27–44，
D 欄會自 `…EPBMaintenanceMode-060` 掉回 `…PARKSENSE…-002` —— **直接違反第一道**。

**故本包依 037 leaf 序排整本**：Park Sense 列 **10–27**、EPB 列 **28–44**。

---

## 2. **出貨前必須先裁：已交付之 17 條 TC ID 全數位移**

`data/writeback_map_b1b2.tsv`（**35 列**）之 TC ID 依列位重編 `001`–`035`（ICS `R-ICS58` 先例）。
其後果：

| 項 | 舊（已交付） | 新（累積簿） |
|---|---|---|
| `…EPBMaintenanceMode-044` | `NR1L-VSM42-001` | **`NR1L-VSM42-019`** |
| `…-045` | `NR1L-VSM42-002` | **`NR1L-VSM42-020`** |
| …（17 條全數） | `001`–`017` | **`019`–`035`** |
| **變動條數** | — | **17／17** |

**已交付件**（`delivered/…_20260902.xlsx`，sha256 `abc7f8ae…`）**仍為舊編號**，本包**未動**。

### 三案並陳（**執行層不擇一**）

| 案 | 作法 | 代價 |
|---|---|---|
| **A** | 出貨累積簿，**取代**同名交付件（ICS 之先例：「取代同名之誤交付件」） | 已交付之 17 條 TC ID 全變；若上游已引用舊 ID，需一併通知 |
| **B** | 維持 b1 之交付件，b2 另出一本 | **R-VL3 檔名無尾綴**，兩本同名撞檔；且各自之列序仍須合判準 |
| **C** | 暫不出貨，待母體 128 全數生成後一次出 | 交付延後；但 TC ID 只重編一次 |

**本包已備妥 A 案之產物**（`sandbox/b2/vsm42_b1b2.xlsx`），B／C 不需額外產物。

---

## 3. 寫回複驗

`sandbox/base/` → `copy2` → `sandbox/b2/vsm42_b1b2_src.xlsx` → openpyxl 計算層填 **35 列**
（列 10–44）→ `surgical_save` → `sandbox/b2/vsm42_b1b2.xlsx`。**115.8 秒**（與前三次同量級）。

`surgical_save` 回報：`sheets_patched 557`／`members_patched ['xl/worksheets/sheet6.xml']`／
`members 48`／`differing ['xl/worksheets/sheet6.xml']`。

| 斷言 | 實測 |
|---|---|
| x14 逐字存活 | **True**（`sheet6.xml`） |
| member 集合相同 | **True（48）** |
| differing 僅目標分頁 | **`['xl/worksheets/sheet6.xml']`** |
| **回讀 557 格** | **不符 0** |
| B 欄公式（r10／r44） | 皆 `=IF(ISBLANK($D{r}),"",ROW()-9)`，**未被值取代** |
| `sandbox/base` sha256 | **不變** |
| 出件 sha256 | `7086a5f9778123bd33a7e81ba4eb2f9b7b53da15fac9142b5a7680a15db66214` |

### 列序四道（本線首次實跑）

| 道 | 判準 | 實測 |
|---|---|---|
| 1 `row-order-by-reqid` | D 欄自上而下不得遞減（037 leaf 序） | **PASS** |
| 2 `tc-id-sequence` | 同 leaf 內 tc_id 遞增 | **PASS**（`001`–`035` 連續） |
| 3 `all-leaves-present` | 已生成之二 test_set 每一 leaf 皆現 | **PASS（35／35）** |
| 4 `blank-row-shape` | 留空列除 B／D 外皆空 | **PASS**（留空列 0） |

首列 D = `SWE1-VC-PARKSENSEw/oHC.1and…-002`；末列 D = `SWE1-VC-EPBMaintenanceMode-060`。

---

## 4. lint 實跑：**兩個 b2 缺陷被抓出並修正**

### 4.1 第一次實跑（修正前）

```
行計 A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 J=2 K=0 L=0 M=0
     N=0 P=23 Q=0 R=1 T=0 U=12 V=0 I-cross=35 W=0
```

**`J=2` 與 `R=1` 為 b2 之新紅，而上繳 11 之文字形預檢報 0** —— 成因具名：

| 檢查 | 缺陷 | 我的預檢為何漏掉 |
|---|---|---|
| **J 行首大寫** | `-020`／`-021` 之 `test_item` **上半**首字為小寫 `if`（自 037 句中起抄） | **我的預檢只掃 `pre`／`itd`／`proc`／`er` 四欄，未掃 `test_item`**；lint 之 J 涵蓋 `test_item` |
| **R Pre-Condition 版面** | `-013` 之 PC 第 2 項 `PROXI PAM_Configuration = 1 (Front And Rear) is not set and the rear configuration is absent` —— 多條件並列於同一行 | 我的預檢只查 `;` 與雙 `and`，該句為 `A is not set and B is absent` 之單 `and`，未命中 |

### 4.2 修正

| req_id | 舊 | 新 | 依據 |
|---|---|---|---|
| `-020`／`-021` | `if the …` | **`If the …`** | **R-4**：「verbatim 自原句中段起抄時，句首字母轉大寫屬排版正規化，允許」。**E56 仍 18／18**（判準本即含小寫變體） |
| `-013` PC | 上述並列句 | **`The Rear Park Sense Volume feature is not supported by the vehicle configuration`** | 037 只述 `based on the corresponding vehicle configuration or feature availability`，**未指名 PROXI 值** |

### 4.3 第二次實跑（修正後）

```
行計 A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 J=0 K=0 L=0 M=0
     N=0 P=23 Q=0 R=0 T=0 U=12 V=0 I-cross=35 W=0
```

| 項 | 結果 |
|---|---|
| **J／R** | **0／0** —— 已消 |
| **P** | 23 列，**對銷 23／23，未對銷 0**（`lint_p_waivers_b1.tsv` 之 11 賦值；b2 之六訊號皆有完整 `VAL_`，未新增任何 P 紅） |
| **U** | 12 = b1 之 6 ＋ b2 之 6（PENDING 計數，非 FAIL） |
| **I-cross** | 35 列，**全屬「窗未完整宣告」型**（R-VL26(d) 基線） |
| 其餘 19 項 | **全 0** |

**lint 淨紅 0。**

### 4.4 預檢已補強（本輪起）

`J` 之掃描範圍加入 `test_item` **上下兩半**；`R` 之判式加入 `A … and B …` 型。
全批（b1 35 檔 ＋ b2 37 檔）重跑：**0**。

---

## 5. §K 增補

### K-9 —— 規格段 1217 之 AND 條件無法僅由 `PAM_Configuration` 否定

規格段 1217：`"CAN node 24 (PAM)" PROXI = "Present" AND ("PAM_Configuration" = "Rear" OR "Front And Rear")`。
**`PAM_Configuration` 之值域恰為該二值**（PROXI Format r516：`0 = Rear`／`1 = Front And Rear`），
故第二個合取項**恆真** —— 其 ELSE 分支（段 1227–1228，Rear 不顯示）
**只能經 `node 24 ≠ Present` 到達**，而那與 `-021` 之總 ELSE（段 1242–1243）重疊。

**處置**：`-013` 之 Pre-Condition 改以**功能可用性狀態**表達（037 之措詞），
**不臆測 PROXI 組合**；缺口記於該條 `remarks` 與此。
**待裁**：`-013` 與 `-021` 是否實為同一條件之兩種表述（若是，屬上游之贅列，同 K-7 之型）。

---

## 6. 一項外部變更使前議自解

上繳 13 第 4 節所報之衝突（R-VL3 之 `VSM42` vs `lint_delivery_spec` 之
`TC_ID_RE = ^NR1L-([A-Za-z]+)-(\d{3})$`）——
**已由他人放寬**：commit **`c5f471b`**「fix(lint): allow digits in the delivery-spec TC ID abbreviation」，
現行為 `^NR1L-([A-Za-z][A-Za-z0-9]*)-(\d{3})$`。

**實測**：`lint_delivery_spec` 對本線交付本**已無判紅**，該閘回到
`PASS: 基線外判紅 0（掃 5 檔，基線 4 列）`。
`DELIVERY_SPEC_BASELINE.tsv` **未被加入本線之列**（仍 4 列，皆他線）——
**即該紅是被修掉，不是被豁免**。

**`delivered/DELIVERY_NOTE.md` 第五節（記該衝突為「未解，交裁」）已過時**，
**本包未改該檔** —— 其為已出貨件之附隨文件，改之等同動交付內容。**待裁是否更新。**

---

## 7. `gate_all.py` 與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 509
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   **lint_delivery_spec**  PASS: 基線外判紅 0（掃 5 檔，基線 4 列）
```

**`lint_delivery_spec` 已由上繳 13 之 FAIL 回到 PASS**（第 6 節）。
餘四支：`rulings_hash` 依 R-VL13 待 Pei 重生（承上繳 12 之 `R-VF83` 情形）；
`canon_refs` 含 `vsm_v42` 者 3 列，與上繳 02–13 逐字相同，本包新增之檔未增任何一列；
`gates_tsv`／`lint_paths` 與本線無關，先在。**無一支肇因於本包。**

---

## 8. 獨立判斷

1. **一項在寫回前被列序判準攔下**：b2 不能 append（第 1 節）。
   **若未查該判準而直接 append，會產出一本列序違規的簿** —— 且 lint036 不查列序，
   要到 `verify_row_order_74.py` 型之檢查才會現形。
2. **兩項 b2 缺陷由 lint 實跑抓出，我的預檢漏掉**（第 4.1 節）。
   **這是「文字形預檢不足」第三次被證實**（前二次：b1 之 hedge、b1 之句內剪接）。
   預檢範圍已補強（第 4.4 節），但**根本問題是我的自檢是手寫的、lint 是既有的** ——
   建議：生成端改為直接呼叫 `lint036` 之判準模組，而非各批重寫預檢。**此需分析層裁**（動共用碼）。
3. **一項未做且指得出理由**：未出貨 —— TC ID 位移須先裁（第 2 節）。
4. **一項過時文件未改**：`DELIVERY_NOTE.md` 第五節（第 6 節）。
5. **未執行下放包 13**（Camera Gridlines）—— Pei 指示「先 b2」。

---

## 9. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `data/writeback_map_b1b2.tsv` | **新建**（35 列，037 leaf 序，TC ID 001–035） |
| `sandbox/b2/vsm42_b1b2_src.xlsx` | 自 `base` `copy2` |
| **`sandbox/b2/vsm42_b1b2.xlsx`** | **累積簿出件**（35 列、557 格、surgical；sha256 `7086a5f9…`） |
| `generated/b2_park_sense/`（`-013`／`-020`／`-021` 各 json＋md，6 檔） | J／R 兩缺陷修訂 |
| `generated/b2_park_sense/INDEX.md` | 重產（列對應、TC ID、本輪修訂表、K-9） |
| `docs/upstream/14_write_b2.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：**`delivered/` 全部三檔（已交付件，sha 未變）**、
`generated/b1_epb/` 全 35 檔（凍結件）、`data/writeback_map_b1.tsv`（b1 之舊映射，保留供追溯）、
`sandbox/base/`（sha 不變）、`sandbox/b1/`、`sandbox/wb_trial/`、
`docs/fw036/`（含 `RULINGS.sha.tsv`、`DELIVERY_SPEC_BASELINE.tsv`）、`scripts/`、`backend/`、
`docs/runtime/`、`forms/`、`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`。
**git**：本包未執行任何 git 寫入指令。

---

## 10. 待 Pei／分析層

1. **出貨與否，及 A／B／C 三案之擇一**（第 2 節）——
   **A 案會使已交付之 17 條 TC ID 全變**。
2. **§K K-9**：`-013` 與 `-021` 是否為同一條件之兩種表述（第 5 節）。
3. **`DELIVERY_NOTE.md` 第五節之過時段落**是否更新（第 6 節）。
4. **生成端自檢改呼叫 `lint036` 判準模組**之提議（第 8 節 2）。
5. 承前未結：R-VL15(c) 之但書（`R-VF83`）、`wb_trial/` 六件去留、綠色通道計數、
   §K K-1〜K-8、DR-VL1／VL2／VL4 之送出、台帳重生、下放包 13（Camera Gridlines）。
