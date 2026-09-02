# 上繳包 13 — vsm_v42：b1 出貨（Pei「出貨」2026-09-02）

日期：2026-09-02　執行層：Claude Code　授權：**Pei 明示「出貨」**（R-VL25(b) 之末句「交付仍待 Pei『出貨』」）

> 本件無對應之下放包 —— 係 Pei 於上繳 12 覆核後直接下令。上繳取號 13
> （`docs/upstream/` 實測有 00–12）。下放包 13（`13_b2_camera.md`）為**另一事**（b2-2 生成），本包不涉。

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | `delivered/` 建立；交付本落檔（sha256 相等）；`MANIFEST.tsv`；`DELIVERY_NOTE.md`；`feature.yaml` 之 `delivery` 宣告 |
| 核實無誤 | 交付本 ↔ 候選 **sha256 逐字相等**；`lint_paths` 之 delivered sha 對照**本線無違規** |
| 正確地不動 | **TC ID 未改**（R-VL3 為 Pei 裁定）；**`scripts/lint_delivery_spec.py` 未改**（共用檔） |

**總判：已出貨。`lint_delivery_spec` 由 PASS 轉 FAIL —— 出貨動作所致，4 項判紅已補正 3 項，
餘 1 項為 R-VL3 與該 lint 正規式之直接衝突，不自行調和（第 4 節）。**

---

## 1. 出貨動作

| 項 | 值 |
|---|---|
| 目錄 | `features/vsm_v42/delivered/`（**本次建立**） |
| 檔名 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_VehicleSetupManagementR1Low_20260902.xlsx` |
| 依據 | **R-VL3**（`{FeatureName}` ＝ Test Group 去空白，無尾綴） |
| 產出方式 | `shutil.copy2` 自 `sandbox/b1/candidate_vsm42_b1.xlsx` |
| 候選 sha256 | `abc7f8aecd23987fc75a11897c3d5b1132b7c62849f3b64cbd04f6fb6b972aa6` |
| **交付 sha256** | **`abc7f8aecd23987fc75a11897c3d5b1132b7c62849f3b64cbd04f6fb6b972aa6`** |
| **逐位元相等** | **True** |
| 同名檔覆寫 | **未發生** —— 落檔前斷言 `not OUT.exists()`，若存在即停下不覆寫 |

`delivered/MANIFEST.tsv` 落 1 列（格式沿既有 17 個 `delivered/MANIFEST.tsv` 之五欄：
`filename`／`sha256`／`source_path`／`delivered_round`／`note`），
`note` 載交付範圍、lint 淨紅 0 之依據、x14 存活與 members 48、及「母體 128 之其餘 111 leaf 尚未交付」。

---

## 2. `lint_paths` —— 本線無新增違規

```
delivered/ sha 對照：2 筆不符
  紅  features/ics_management/…_ICSManagement_20260830.xlsx：sha256 與對照表不符
  紅  features/sw_update/…_SWUpdate_20260830.xlsx：delivered/ 內而對照表未列
FAIL: 基線外違規 + delivered 不符 = 4
```

**四筆與前七包逐字相同，全屬他線。** 本線之交付本因 `MANIFEST.tsv` 已同步落列且 sha256 相符，
**未觸發任何一筆**（`delivered/ 內而對照表未列` 之型即 sw_update 之情形，本線已避開）。

---

## 3. `lint_delivery_spec` —— **由 PASS 轉 FAIL，肇因為本包之出貨動作**

出貨前該閘為 `PASS: 基線外判紅 0（掃 4 檔）`；出貨後掃 5 檔，本線交付本判紅 **4 項**：

| # | 判紅 | 處置 |
|---|---|---|
| 1 | 二 TC ID 形制：17 列不合 `NR1L-{ABBR}-{nnn}` | **未解，交裁**（第 4 節） |
| 2 | 二 `feature.yaml` 未宣告 `delivery.tc_id_abbr` | **已補** |
| 3 | 六 `delivered/` 無 `DELIVERY_NOTE.md` | **已補** |
| 4 | 六 未結 DR 清單缺 | **已補**（`DELIVERY_NOTE.md` 第二節，含 `DR-` 段） |

補正後：**`FAIL: 基線外判紅 1（掃 5 檔，基線 4 列）`** —— 四項降為一項。

### 補正內容

**(a) `feature.yaml` 之 `delivery` 宣告**（本線檔，非共用）：
```yaml
delivery:
  test_group: "Vehicle Setup Management R1 Low"      # R-VL3
  tc_id_abbr: "VSM42"                                # R-VL3 之 {ABBR}
```
**`leaf_ids` 刻意未宣告**，理由寫入該處註解：其比對式為
「037 有列而簿上無列即**判紅**」，而本交付件只含 b1 之 17 條，
母體 128 之其餘 111 leaf 尚未生成／交付 —— **現在宣告會使該檢查對一件本就部分交付之簿判紅 111 次**。
待全批交付後再宣告，屆時該比對方為有意義之覆蓋檢查。**據實記明。**

**(b) `delivered/DELIVERY_NOTE.md`** —— 六節：交付範圍與**未涵蓋之 111 leaf**／
未結 DR 清單（DR-VL1／VL2／VL4 未送出，DR-VL3 結案）／
**本件之未驗證性質逐項揭露**（PENDING 6 格 3 條、11 個賦值無 `VAL_` label、
`-059` 之 ignition 分支未涵蓋、§K K-1〜K-6）／品質證據／與 lint 判準之衝突／追溯表。

---

## 4. **未解之一項：R-VL3 與 `lint_delivery_spec` 之正規式直接衝突**

```python
TC_ID_RE = re.compile(r"^NR1L-([A-Za-z]+)-(\d{3})$")   # scripts/lint_delivery_spec.py:40
```

**`{ABBR}` 只收字母**；本線之 TC ID 依 **R-VL3**（Pei 2026-09-01 裁定「3 准」）為
`NR1L-**VSM42**-{nnn}`，**含數字 42**。故 17 列全數判「不合形制」。

**本包之處置 —— 兩者皆不改**：

| 可能之改法 | 為何不做 |
|---|---|
| 改 TC ID 為純字母 | R-VL3 為 **Pei 裁定**；且該 ID 已寫入交付簿 F 欄 17 列、`writeback_map_b1.tsv`、`generated/b1_epb/INDEX.md`。改之須新裁決 |
| 改 `TC_ID_RE` 為 `[A-Za-z0-9]+` | `scripts/` 為**共用檔**，改之影響全部 18 條線之交付檢查（FO 第 8.6 節第 4 項之戒） |

**待裁（擇一）**：
- **(a)** 放寬 `TC_ID_RE` 為 `^NR1L-([A-Za-z0-9]+)-(\d{3})$`；
  —— 本線之 `VSM42`、姊妹線之 `VSM43`（若同型）皆屬此類，且 `NR1L-` 前綴與三位序號不變。
- **(b)** 改 R-VL3 之 ABBR 為純字母（如 `VSM`）—— 但兩線同名，會與 `vsm_v43` 撞。

> **(b) 之撞名風險須先查**：若 `vsm_v43` 亦用 `VSM`，兩線之 TC ID 將無法區分。
> **本包未查該線之 TC ID**（他線範圍），僅指出風險。

---

## 5. `gate_all.py` 與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 509
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
**FAIL**  exit 1   lint_delivery_spec FAIL: 基線外判紅 1（掃 5 檔，基線 4 列）
```

**(甲) `lint_delivery_spec`** —— **本包所致**（見第 3／4 節）。
4 項降為 1 項，餘 1 項為條文與判準之衝突，**不自行調和**。
**這是本線首次使該閘轉紅，且原因具名可裁。**

**(乙) `rulings_hash`** —— 依 R-VL13 記「待 Pei 重生」。
承上繳 12 第 7 節甲：`R-VF83`（`vehicle_setting` 線）之 `body_sha8` 變動使
R-VL15(c) 之免責判準不滿足；本包未再重測（無新變數）。

**(丙) `canon_refs` 509** —— 含 `vsm_v42` 者 **3 列**，與上繳 02–12 逐字相同。
**本包新增之 3 檔（交付本／MANIFEST／DELIVERY_NOTE）未新增任何一列。**
509 之增量落於本線之外。

**(丁) `gates_tsv`／(戊) `lint_paths`** —— 與本線無關，先在（第 2 節）。

---

## 6. 獨立判斷

1. **一項本包造成之 gate 轉紅已補正大半**：`lint_delivery_spec` 4 → 1。
   **未補之 1 項不是疏漏，是條文衝突**，兩造皆為不可由執行層擅動之物。
2. **一項刻意不宣告**：`delivery.leaf_ids`（第 3 節 a）。
   若分析層認為部分交付亦應宣告全母體並容忍 111 筆紅，請指示。
3. **一項未查而具名**：`vsm_v43` 之 TC ID 是否亦為 `VSM`＋數字（第 4 節 b 之撞名風險）。
4. **交付件之範圍已於 `DELIVERY_NOTE.md` 第一節明列** ——
   **本件只含 128 之 17**，其餘 111 leaf 未交付；`Park Sense` 18 條已生成未寫回。
   **此揭露為 R-VL4 與 DR-VL1 之交付說明要求所必需。**
5. **一項提醒**：交付本之 sha256 已三處落檔（`MANIFEST.tsv`／`DELIVERY_NOTE.md`／本上繳）。
   日後若 b2 併入同一本重出，**該三處須同步更新**，否則 `lint_paths` 之 delivered sha 對照即紅
   （ics_management 之現況即此型）。

---

## 7. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `features/vsm_v42/delivered/FM-WI-FSM-036-A01 …_VehicleSetupManagementR1Low_20260902.xlsx` | **新建**（`copy2`，sha256 相等） |
| `features/vsm_v42/delivered/MANIFEST.tsv` | **新建**（1 列） |
| `features/vsm_v42/delivered/DELIVERY_NOTE.md` | **新建**（六節） |
| `features/vsm_v42/feature.yaml` | 加 `delivery` 宣告（`test_group`／`tc_id_abbr`；`leaf_ids` 刻意不宣告） |
| `features/vsm_v42/docs/upstream/13_ship_b1.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：**`scripts/`（含 `lint_delivery_spec.py`）**、`generated/b1_epb/`（凍結件）、
`generated/b2_park_sense/`、`sandbox/`（含 `base/`／`b1/`／`wb_trial/`）、
`data/`、`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`、`backend/`、`forms/`、
`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 8. 待 Pei／分析層

1. **TC ID 形制之衝突**（第 4 節）：放寬 `TC_ID_RE` 或改 R-VL3 之 ABBR。
   **在裁定前，`lint_delivery_spec` 對本線之交付本恆為 1 紅。**
2. **`delivery.leaf_ids`** 是否於部分交付時宣告（第 3 節 a）。
3. 承前未結：R-VL15(c) 之但書（`R-VF83`）、`wb_trial/` 六件之去留、
   綠色通道計數、§K K-1〜K-8、DR-VL1／VL2／VL4 之送出、台帳重生。
4. **下放包 13（`13_b2_camera.md`）已落**，為 b2-2（Camera Gridlines 10 leaf）之生成包，本包未執行。
