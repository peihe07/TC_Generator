# 上繳包 12 — vsm_v42：修訂落地 → b1 寫回 → 交付候選

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/12_write_b1.md`

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | `-057` 解凍修一列並重新凍結；b2 Volume 13 條雙錨＋`-006` remarks；`writeback_map_b1.tsv` 對調；`lint_p_waivers_b1.tsv` 新建；**b1 寫回 `sandbox/b1/`**；交付候選 |
| 核實無誤 | **E90／E91／E92／E93 全過**；**lint 淨紅 0**（C=0、P 對銷 23／23、I-cross 全屬基線型）；`sandbox/base` sha 不變 |
| 正確地不動 | b1 其餘 16 條、b2 其餘 4 條一位元未動；`delivered/` **未建**；C／Q／T–Z／AB 欄留空 |

**總判：E89–E93 全過，b1 已寫回且 lint 淨紅 0 → 待 Pei「出貨」。
一項 `rulings_hash` 之新情形須回報（第 7 節甲）。**

---

## 1. 修訂落地（§一，順序執行）

### 1.1 `-057` 解凍修一列（R-VL26(a)）

| | 內容 |
|---|---|
| 舊括號下半 | `(Fdbk = 11: exit completed successfully)` ← hedge `successfully`（IN §4.3 禁用） |
| **新** | **`(Fdbk = 11: exit process reported as complete)`** |
| 其餘欄位 | `test_item` 上半／Procedure／ER／`remarks`／`priority`／`design_method`／`distinguishing_axis` **一字未動** |
| 新 sha8 | **`72c5b02a`**（`.json`） |

**重跑**：E39 違規 **0**（全批括號下半互不重複）；E56 **17／17**；**hedge 掃描 0**。
`INDEX.md` 已記 **`-057 amended per R-VL26(a); refrozen`**。

### 1.2 b2 錨層修訂（R-VL26(b)）

Volume **13 條**之 `specification_reference` 改**雙錨**：

```
["Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29",
 "Sys-RA-VF665_V42_VSM-{nnn}"]
```

章節號一行在前、原 Sys-RA 行保留在後。PARK SENSE 家族 **5 條**維持單錨章節號。
**異常 0**（逐條機讀驗：Volume 13 條皆為 2 元素且首為章節號、次符 `Sys-RA-VF665_V42_VSM-\d+`）。

`-006` 之 `remarks` 追加：
`; upstream duplicate suspected (verbatim same as -002 and spec paras 1203-1204 / 1214-1215) — DR-VL2 evidence`

### 1.3 `writeback_map_b1.tsv` 對調（R-VL26 依交付慣例）

| 欄 | 舊 | 新 |
|---|---|---|
| D | `req_id_D` = `Sys-RA-VF665_V42_VSM-{nnn}` | **`swe_id_D` = `SWE1-VC-EPBMaintenanceMode-{nnn}`** |
| C | `polarion_C` = SWE-Requirement ID | **`empty_C` = 留空** |
| S | （無） | **`functional_safety_S` = `NA`**（新增欄，依上繳 10 第 1 節之交付慣例實測 713／745 列為 `NA`） |

現行欄序：`row`／`tc_id`／`swe_id_D`／`empty_C`／`functional_safety_S`／`test_group_G`／
`test_set_H`／`src_json`／`src_sha8`。

> 上繳 10 第 5 節所報之「D／C 與四本交付慣例相牴觸」自此**依慣例定案**，
> 本包之寫回即以新映射為之。

### 1.4 `data/lint_p_waivers_b1.tsv` 新建

**11 個賦值**，欄 `assignment`／`signal`／`raw`／`basis`：

| 訊號 | raw |
|---|---|
| `IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk` | 2／3／4／5／6／8／9／10／11（**9 項**） |
| `STATUS_CCAN3.VehicleSpeedVSOSig` | 64／65（**2 項**） |

`basis` 逐列為 `R-VL21(c)/R-VL26(c): DBC has no VAL_ entry for this raw value; disclosed in remarks`。

---

## 2. E89 修訂範圍

| 批 | 下放包所述 | 實測 | 說明 |
|---|---|---|---|
| b1 | `-057` **2 檔** | **2 檔**（`.json` ＋ `.md`） | 相符 |
| b2 | **14 檔** | **28 檔**（**14 個 req_id** × `.json`＋`.md`） | **計數口徑不同** —— 修訂之 req_id 為 14（Volume 13 ＋ `-006`），每 req_id 兩檔。**據實並列，不自行調和。** |
| `writeback_map_b1.tsv` | 1 | 1 | 相符 |
| `lint_p_waivers_b1.tsv` | 1（新建） | 1 | 相符 |
| **其餘 diff = 0** | — | b1 其餘 **16 條 32 檔**、b2 其餘 **4 條 8 檔** 逐位元相同 | **過** |

（`INDEX.md` 兩批另行重產，不計入上表。）

---

## 3. E90 b2 重跑（綠色通道 1／3 要件）

| # | 實測 |
|---|---|
| E38 覆蓋 | 18／18，落空 0 |
| E39 R-S4 | 違規 **0**；全批括號下半互不重複 |
| E40 尾句號 | **0** |
| E41 `[..]`／`'..'`／`<..>` | **0** |
| E42 `$..$` 皆可回溯解得 | **0** |
| E43 PENDING 格式 | **0** |
| E44 reasoning | **0** |
| E45 modal | **0** |
| **E56 逐字全等** | **18／18** |
| C hedge | **0** |
| **E86′（R-VL26(b) 雙錨）** | PARK SENSE 5 條單錨章節號／Volume 13 條雙錨，**異常 0** |

> **E86 之原判準（「全為 Sys-RA 實名」）已由 R-VL26(b) 之雙錨取代**，
> 以原判準跑會判 13 條「非 Sys-RA」—— 那是**判準過時**，非產出缺陷。
> 本包以 **E86′**（雙錨結構）重述並實測，據實記明。

**E90 全過。** 綠色通道 1／3 之要件（零它項）就本包所測**成立**；
其計數之認定屬分析層。

---

## 4. E91 寫回複驗

工法：`sandbox/base/` → `copy2` → `sandbox/b1/vsm42_b1_src.xlsx` →
openpyxl 計算層填 17 列（列 10–26）→ **`surgical_save`** → `sandbox/b1/vsm42_b1.xlsx`。
**單次 117.5 秒**（與 09／10 包之 119.4／117.4 秒同量級）。

`surgical_save` 回報：
`{'sheets_patched': {'Test Case Specification 測試用例規範': 269}, 'members_patched': ['xl/worksheets/sheet6.xml'], 'members': 48, 'differing': ['xl/worksheets/sheet6.xml'], 'dv_counts': {'xl/worksheets/sheet5.xml': (1, 0), 'xl/worksheets/sheet6.xml': (3, 1)}}`

### 強制複驗三斷言

| # | 斷言 | 實測 |
|---|---|---|
| 1 | x14 逐字存活 | **True**（`xl/worksheets/sheet6.xml`，節點位元相同） |
| 2 | member 集合相同 | **True（48）** |
| 3 | differing 僅目標分頁 | **`['xl/worksheets/sheet6.xml']`** |

### 回讀 17 列逐欄比對修訂後 JSON

| 項 | 實測 |
|---|---|
| 比對格數 | **269** |
| **不符** | **0** |
| B 欄公式（r10／r26） | `=IF(ISBLANK($D10),"",ROW()-9)`／`=IF(ISBLANK($D26),"",ROW()-9)` —— **未被值取代** |
| 留空欄抽驗（r10） | `C` = `None`／`Q` = `None`／`V` = `None`／`AB` = `None` —— **依交付慣例留空** |

**E91 全過。**（格數 269 < 上繳 10 之 286，差在 C 欄由「寫 SWE id」改為「留空」17 格。）

---

## 5. E92 lint 實跑與 P 對銷

```
$ python3 scripts/lint036.py "features/vsm_v42/sandbox/b1/vsm42_b1.xlsx" --profile vsm_v42
vsm42_b1.xlsx
  行計 A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 J=0 K=0 L=0 M=0
       N=0 P=23 Q=0 R=0 T=0 U=6 V=0 I-cross=17 W=0
```

| 檢查 | 行計 | 判 |
|---|---|---|
| **C hedge** | **0** | **過** ← `-057` 修訂之效 |
| **P** | 23 | **對銷後淨紅 0** |
| **U** PENDING 佔位 | 6 | 計數用，非 FAIL（與已報之 6 項 PENDING 逐項相符） |
| **I-cross** | 17 | **全 17 列皆為「窗未完整宣告」型**（R-VL26(d) 之基線） |
| 其餘 20 項 | **全 0** | **過** |

### P 之對銷表（23 紅 ↔ 11 waiver）

| waiver 之 assignment | 對銷次數 |
|---|---|
| `$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 2` | 2 |
| 同 `= 3` | 2 |
| 同 `= 4` | 2 |
| 同 `= 5` | 2 |
| 同 `= 6` | 2 |
| 同 `= 8` | 2 |
| 同 `= 9` | 2 |
| 同 `= 10` | 2 |
| 同 `= 11` | 2 |
| `$STATUS_CCAN3.VehicleSpeedVSOSig$ = 64` | **3** |
| `$STATUS_CCAN3.VehicleSpeedVSOSig$ = 65` | 2 |
| **合計** | **23** |

**對銷成功 23／23；涉及 waiver 條目 11／11（無未用之 waiver）；未對銷（淨紅）0。**

（`= 64` 為 3 次係因 `-059` 之 ER 中該值出現於「registered without a bus error」與
「is received」兩式，加 Procedure 一次。）

### I-cross 之型態

17 列**全數**為
`**窗未完整宣告** —— 訖點無片語可抽，本列不參與 I-cross 比對（R-SU33(b)：ER 須明載窗之起訖）`，
即**非 17 組跨列衝突**，而是 17 列各自不參與比對。**全屬 R-VL26(d) 所定之基線型。**

**E92 全過（淨紅 0）。**

---

## 6. E93 交付候選

`sandbox/b1/candidate_vsm42_b1.xlsx` 以 **`shutil.copy2`** 自出件產生（popup `gen_delivery.py` 之作法）。

| 檔 | sha256 |
|---|---|
| `sandbox/b1/vsm42_b1.xlsx` | `abc7f8aecd23987fc75a11897c3d5b1132b7c62849f3b64cbd04f6fb6b972aa6` |
| `sandbox/b1/candidate_vsm42_b1.xlsx` | `abc7f8aecd23987fc75a11897c3d5b1132b7c62849f3b64cbd04f6fb6b972aa6` |
| **相等** | **True** |

**E93 過。`delivered/` 未建**（待 Pei「出貨」）。

### 凍結表更新

`generated/b1_epb/INDEX.md` 已更新：
標頭加 **`-057 amended per R-VL26(a); refrozen`**；凍結檔表之 `-057` 兩檔為修訂後之新 sha8
（`.json` = `72c5b02a`）；新增「寫回產物」節（兩檔 sha256）；
主表加「工作簿列」與「TC ID」「D 欄」三欄，與 `writeback_map_b1.tsv` 對應。

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

### (甲) `rulings_hash` —— **本包實測出現 R-VL15(c) 判準之首次不滿足，且不在本線**

id 級實測（樹外 `--out`）：**新增 43／移除 0／`body_sha8` 亦變 **1**。

R-VL15(c) 之可上繳判準為「**無刪除列，且既有列之 `body_sha8` 無變動**」——
**`body_sha8` 變動 1 項使該判準不滿足**。逐項追出：

| 條號 | 台帳（`HEAD` 版） | 現行 | 所在檔 |
|---|---|---|---|
| **`R-VF83`** | `sha8 beba78c6`／`body_sha8 ebfa087c` | `sha8 895339a6`／`body_sha8 55c067b6` | **`features/vehicle_setting/RULINGS.md`** |

**歸屬**：`R-VF83` 屬 **`vehicle_setting`** 線；該檔**不在本包之修改範圍**
（本包之 `git status` 實測其為乾淨），其本體變動來自該線自身之 commit（最近為 `9f1aed0`）。

**本包之處置**：**不自行調和、不重生台帳**（R-VL13）。
據實回報：**`rulings_hash` 之紅自本包起不再滿足 R-VL15(c) 之免責判準**，
其成因為他線之條文本體修訂。**待裁**：(a) 認列為他線之合法修訂而放行；
或 (b) R-VL15(c) 補「`body_sha8` 變動屬他線者不計」之但書。

### (乙) `canon_refs` 506 —— 含 `vsm_v42` 者 **3 列**，與上繳 02–11 逐字相同。本包新增之檔未增任何一列。

### (丙) `gates_tsv` —— 與本線無關，先在。

### (丁) `lint_paths` = 4 —— **與本線無關，且本包新增之 `sandbox/b1/` 三本 xlsx 未增違規**
（`sandbox` 為合法落點）。四筆與前六包逐字相同：driver_distraction 兩本工作簿落點、
ics_management 與 sw_update 之 `delivered/` sha。

---

## 8. 獨立判斷

1. **一項判準過時已具名**：E86 之原判準與 R-VL26(b) 相反（第 3 節），
   以 **E86′** 重述並實測，**未以舊判準判紅**。
2. **一項計數口徑不同已並列**：E89 之「b2 14 檔」實為 14 req_id × 2 = 28 檔（第 2 節）。
3. **一項 gate 判準首次失效，且不在本線**：`R-VF83` 之 `body_sha8` 變動（第 7 節甲）。
   **這是 R-VL15(c) 立條以來第一次不滿足**，其成因為他線 —— 若不加但書，
   往後兩線並行時每逢他線改條文，本線之上繳都要附此說明。
4. **一項本包未做且指得出理由**：`delivered/` 未建 —— 下放包明定待 Pei「出貨」。
5. **一項提醒**：b1 已寫回 `sandbox/b1/`，其內容對應 `generated/b1_epb/` 之**現行**（含 `-057` 修訂）。
   若日後 `generated/` 再改，**`sandbox/b1/` 之簿與 `INDEX.md` 之凍結表須同步重出** ——
   本包之凍結表已記兩者之 sha，可據以偵測。
6. **一項承前未結**：`wb_trial/` 六件依 R-VL24(d) 仍保留至寫回執行包結案；
   **本包即為該包**，故其去留請於本次覆核一併裁。

---

## 9. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `generated/b1_epb/…-057.{json,md}` | R-VL26(a) 一列 |
| `generated/b1_epb/INDEX.md` | 凍結表更新（`-057` 新 sha8、寫回產物、列對應） |
| `generated/b2_park_sense/`（14 req_id × 2 = 28 檔） | R-VL26(b) 雙錨 ＋ `-006` remarks |
| `data/writeback_map_b1.tsv` | D／C 對調 ＋ S 欄 |
| `data/lint_p_waivers_b1.tsv` | **新建**（11 賦值） |
| `sandbox/b1/vsm42_b1_src.xlsx` | 自 `base` `copy2` |
| **`sandbox/b1/vsm42_b1.xlsx`** | **b1 寫回出件**（17 列、269 格、surgical） |
| **`sandbox/b1/candidate_vsm42_b1.xlsx`** | **交付候選**（`copy2`，sha256 相等） |
| `docs/upstream/12_write_b1.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：**`sandbox/base/`（sha256 不變）**、`generated/b1_epb/` 其餘 16 條 32 檔、
`generated/b2_park_sense/` 其餘 4 條 8 檔、**`delivered/`（未建）**、
`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`、`scripts/`、`backend/`、`forms/`、
`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 10. 待 Pei／分析層

1. **「出貨」授權** —— `delivered/` 之建立與交付本落檔（候選已備妥，sha256 已列）。
2. **R-VL15(c) 之但書**（第 7 節甲）：他線之 `body_sha8` 變動是否不計。
3. **`wb_trial/` 六件之去留**（R-VL24(d) 所定之結案時點即本包）。
4. **綠色通道計數**：本包之 b2 重跑零它項，是否計 1／3。
5. 承前未結：§K K-1〜K-8、DR-VL1／VL2／VL4 之送出、台帳重生、
   b2-2（Camera Gridlines 10 leaf）之生成包。
