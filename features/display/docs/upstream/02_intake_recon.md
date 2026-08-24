# 上繳包 02 —— Display 素材來源更正，01 步驟 1–14 全數執行

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/02_source_correction.md`（併同
  執行下放包 01 §四步驟 1–14）
- 結果：**步驟 1–14 全數執行；01 §五之九條停止條件全未觸發**
- 全部 git 操作屬 Pei —— 本輪未執行任何 `git` 指令（§12 只備妥訊息與 pathspec）

---

## 0. 本輪之偏離事項（先講）

1. **步驟 12 與 13 之順序對調。** `recon.py` 讀 `feature.yaml` 之
   `paths.workbook`，而該值在 scaffold 後仍為模板佔位符
   `inputs/<FW036 xlsx>`，腳本以 `input not found` 立即中止。故先做步驟 13
   （依實測填 `feature.yaml`）再回頭跑步驟 12。此為執行順序調整，不改任何
   判準；`feature.yaml` 之值全部來自本輪實測，未取自任何既有 feature。
2. **步驟 12 之 `recon.py` 依 R-DM5(b) 預期失敗，未修腳本**，故
   `RECON.md` / `DECISIONS.md` / `data/recon.json` **本輪未產出**。
   詳見 §A-DM8 與 §11。
3. **canon §Phase 1 之「下拉選單 design-method 詞彙抽取」由本輪手動補測**
   （見 §6.4），因 `recon.py` 未及走到該步。

---

## 1. 素材台帳

四份素材之來源目錄為 R-DM9 所定之
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/`
（唯讀，本輪只讀不寫）。搬入路徑為 `_intake/Display/` → （`intake.py
--scaffold` 搬移）→ `features/display/inputs/`。台帳機器產出於
`features/display/data/materials_ledger.tsv`。

### 037_A03_SWRA

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
- 目的：`features/display/inputs/Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
- size：46993　mtime（搬入前／後）：2026-08-22T16:02:56 ／ 2026-08-22T16:02:56
- SHA256（搬入前）：`ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050`
- SHA256（搬入後）：`ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050`
- `shasum -c`：**OK**
- 他處同名／同內容副本：`/Users/peihe/Work_Projects/R1L_RTM_V3/data/9_ASPICE/04_SWE.1 Software Requirements Analysis/Display Management/Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
  - SHA256 `100f75b7110e3c83330fd6401be00aa0da859af4bcc12fc8665b72fda5f374f0` → **SAME_CONTENT_DIFF_FILE (R-DM10: 0 差異格)**

### CFTS_020_doc

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx`
- 目的：`features/display/inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx`
- size：292827　mtime（搬入前／後）：2026-08-22T16:02:33 ／ 2026-08-22T16:02:33
- SHA256（搬入前）：`8696d1f596e3367754b092ff6d810cccff6258f46d6e90f8c0b30864314a30f3`
- SHA256（搬入後）：`8696d1f596e3367754b092ff6d810cccff6258f46d6e90f8c0b30864314a30f3`
- `shasum -c`：**OK**
- 他處同名／同內容副本：`/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/26PI1.5/SubSystem/Cabin/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx`
  - SHA256 `8696d1f596e3367754b092ff6d810cccff6258f46d6e90f8c0b30864314a30f3` → **SAME**

### SYS2_polarion_export

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx`
- 目的：`features/display/inputs/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx`
- size：193683　mtime（搬入前／後）：2026-08-16T06:30:00 ／ 2026-08-16T06:30:00
- SHA256（搬入前）：`421c8eef3f5cb01a2d4d4768b41d38897009c53cdfdff2ff1b6ab80ba72adb1d`
- SHA256（搬入後）：`421c8eef3f5cb01a2d4d4768b41d38897009c53cdfdff2ff1b6ab80ba72adb1d`
- `shasum -c`：**OK**
- 他處同名／同內容副本：`/Users/peihe/Work/02_Project_R1LR/9_ASPICE/SYS.2 System Requirements Analysis/CFTS_020 ICS and DCSD/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx`
  - SHA256 `421c8eef3f5cb01a2d4d4768b41d38897009c53cdfdff2ff1b6ab80ba72adb1d` → **SAME**

### SYS3_SYSAD_doc

- 來源：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Display/SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx`
- 目的：`features/display/inputs/SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx`
- size：3663612　mtime（搬入前／後）：2026-08-16T06:32:00 ／ 2026-08-16T06:32:00
- SHA256（搬入前）：`be9c97af0211a70357d4484fcfbd19b72d3d439ff28e7d09a11dda3146b3c298`
- SHA256（搬入後）：`be9c97af0211a70357d4484fcfbd19b72d3d439ff28e7d09a11dda3146b3c298`
- `shasum -c`：**OK**
- 他處同名／同內容副本：`/Users/peihe/Work/02_Project_R1LR/9_ASPICE/SYS.3 System Architectural Design/Display/SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx`
  - SHA256 `be9c97af0211a70357d4484fcfbd19b72d3d439ff28e7d09a11dda3146b3c298` → **SAME**
### 036 母本（R-G1，另計）

- 來源：`forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx`
- 目的：`features/display/inputs/`（同名）
- size：200650　mtime：2026-08-17T09:46:09
- SHA256（前／後）：`6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`（相同）
- 全程未以 `openpyxl` 存回（R-G1 之 x14 DV 保護）；本輪對母本之所有操作
  皆為 `load_workbook` + `close`，無 `save()`

### 到齊判定（R-DM6）

`shasum -c` 對四份素材（以來源目錄之雜湊清單為基準，於 `inputs/` 執行）
**4/4 OK**。四份以外未搬入任何檔案；來源目錄之檔案清單與 R-DM9 §三所列
逐字相符（4 檔，無多無少），停止條件 8 未觸發。

---

## 2. R-DM2′ 之 64 碼雜湊逐字比對（下放包 02 §六第 14 項）

| 項 | 值 |
|---|---|
| 條文所載 | `ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050` |
| 實測（來源目錄） | `ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050` |
| 逐字（64/64） | **MATCH** |

比對於複製動作**之前**執行，不符即中止（腳本以 `exit 1` 實作）。

---

## 3. 兩處同名檔比對（下放包 02 §五步驟 1b、§六第 15 項）

| 檔 | 交付夾版 SHA256 | 他處版路徑 | 他處版 SHA256 | 判定 |
|---|---|---|---|---|
| CFTS_020 docx | `8696d1f5…4a30f3` | `1_Customer_Requirement/…/SubSystem/Cabin/` | `8696d1f5…4a30f3` | **SAME** |
| SYS2 xlsx | `421c8eef…2adb1d` | `9_ASPICE/SYS.2 …/CFTS_020 ICS and DCSD/` | `421c8eef…2adb1d` | **SAME** |
| SYS3 docx | `be9c97af…6b3c298` | `9_ASPICE/SYS.3 …/Display/` | `be9c97af…6b3c298` | **SAME** |

三份皆同一，交付夾版與 ASPICE 歸檔版同步，`A-DM{n}` 未開立、未停手。

---

## 4. 裁決條文抄錄核對表（§二八條 + 02 §四五條 = 13 條）

抄錄方式：以 `re` 自兩份下放包之 fenced 區塊機器抽取後原樣寫入
`features/display/RULINGS.md`，**未經人工轉錄**。核對方式：抄錄後自
`RULINGS.md` 反向抽取各區塊，與下放包原檔逐字元 `==` 比對。

| # | 條號 | 來源包 | 字元數 | SHA256（前 12 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 1 | R-DM1 | 01 | 337 | `f8181c4bd16d` | 是 |
| 2 | R-DM2 | 01 | 488 | `231830d8d5cd` | 是 |
| 3 | R-DM3 | 01 | 739 | `dc68c2bbe205` | 是 |
| 4 | R-DM4 | 01 | 367 | `25f632b137ac` | 是 |
| 5 | R-DM5 | 01 | 607 | `19bfd2399bb2` | 是 |
| 6 | R-DM6 | 01 | 216 | `1d8eb69193c7` | 是 |
| 7 | R-DM7 | 01 | 498 | `b967b0965266` | 是 |
| 8 | R-DM8 | 01 | 559 | `e6ff38e7f747` | 是 |
| 9 | R-DM2（廢止） | 02 | 329 | `eecfc177bae7` | 是 |
| 10 | R-DM2′ | 02 | 406 | `c4f685368910` | 是 |
| 11 | R-DM9 | 02 | 397 | `ac0b6373fe6b` | 是 |
| 12 | R-DM10 | 02 | 519 | `4a0756e807a1` | 是 |
| 13 | R-DM11 | 02 | 193 | `381220990cd1` | 是 |

**13/13 逐字元相符。** 下放包 02 §三之來源目錄路徑區塊為路徑而非條文，
未計入。

---

## 5. `intake.py` 之實際分類輸出（全文）

指令：`python3 scripts/intake.py Display`（不加 `--scaffold`，未改腳本）

```
# INTAKE — Display (generated by intake.py)

## Classified files
- `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` -> **spec_xlsx** — sheets: SWE1 Requirements, SYS2 Traceability, Excluded NRLs (HW-only)
- `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` -> **cfts_doc** — CFTS/Word candidate (spec_mode D)
- `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` -> **polarion_export** — SYS2 safety-analysis export (Sys-RA ids)
- `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` -> **cfts_doc** — CFTS/Word candidate (spec_mode D)

## Documents cited by the requirement report (need list)
- **NO requirement report found** — cannot derive the need list; this is the first file to obtain

## Proposed spec_mode: **D** — CFTS/Word is the spec source; spec_reference by lookup

## Action: complete — run `--scaffold` then Phase 1 recon
```

> 上為 2026-08-24 首次執行（`_intake/Display/` 四檔齊備時）之逐字輸出。
> **本節不可由重跑取得**：`--scaffold` 已將四檔搬入 `inputs/`，此後再跑
> `intake.py Display` 面對的是空資料夾，會輸出 `Classified files` 空清單
> 與 `spec_mode E`。撰稿時曾誤植該重跑結果，已更正為首跑輸出。

**R-DM5(a) 之預期偏差如實命中**：037 被分類為 `spec_xlsx`（非
`swra_report`），note 為其三個分頁名。腳本未被預先修改。

need-list 一節之輸出為 `NO requirement report found — cannot derive the
need list`。該句非空清單且有說明，故未達 R-DM5(c) 之登記門檻；惟其理由
（找不到 requirement report）與 R-DM5(c) 所述之理由（`Source Requirement
ID` 欄為 Polarion id 而非文件引用）不同 —— 以 **A-DM9** 登記為理由失真，
並記「need list 是否可推導」一事本輪實質未受檢驗。

`--scaffold` 之追加輸出：

```
scaffolded /Users/peihe/Work_Projects/TC_Generator/features/display; classified files moved to inputs/; feature.yaml paths + spec_mode pre-filled
CONFLICT (A-TM10): spec_pdf: kept `inputs/R1LR_…CFTS_020 ICS and DCSD _20260310-1533.docx`, did NOT overwrite with `inputs/SYS3_…SYSAD_v1.0.docx` (cfts_doc)
```

該 CONFLICT 為腳本既有之保護行為（A-TM10）：兩份 docx 都映射到
`spec_pdf`，先到者不被後到者蓋掉。本輪於 `feature.yaml` 另立
`sys3_sysad:` 鍵承接 SYS3，並註明其為追溯／架構參考而非判讀基準。

### 骨架建立之選擇與覆寫檢查（步驟 3）

選 `intake.py --scaffold`，理由：它是 `intake.py` 自身輸出所指定之下一步，
內部即以 `--adopt-existing` 呼叫 `new_feature.py`，並一次完成 scaffold、
搬入 `inputs/`、`feature.yaml` 路徑預填，較兩步手動搬檔少一次人為誤差。

覆寫檢查（§五第 7 條）：`new_feature.py:184` 對已存在之目標一律 `skip`，
且其寫入清單只含 feature 根層 8 個檔，不含 `docs/` 下任何路徑。實測
`docs/handoff/01_intake_recon.md` 與 `02_source_correction.md` 於 scaffold
前後 mtime 與內容未變。**第 7 條未觸發。**

---

## 6. 獨立重算

### 6.1 量測條件（自行宣告）

| 項 | 037 | SYS2 | 036 母本 |
|---|---|---|---|
| 引擎 | openpyxl, `data_only=True` | openpyxl, `data_only=True` | openpyxl, `data_only=True` |
| 模式 | **非唯讀**全表掃描 | **唯讀** | 非唯讀（只讀不存） |
| 判空 | 該列 A..`max_column` 全格 `str(v).strip()==""` 即為空列 | A 欄（`ID`）非空即資料列，r2 起 | 同 037 |
| 大小寫 | **區分** | **兩種算法皆報**（見 6.3） | 比對欄名時不分（並列原始字串） |
| 空白 | 欄名比對前 `" ".join(str(s).split())` 正規化（見 A-DM5） | 同左（欄名帶雙語括號尾綴） | 同左 |

腳本：`features/display/scripts/recount_037.py`、`recount_sys2.py`、
`probe_036.py`、`coverage_map.py`、`probe_spec_mode.py`、
`probe_missing_values.py`。標的一律為 `features/display/inputs/` 之複本。

### 6.2 037 重算（步驟 6）

```
# 037 recount — measurement conditions
engine=openpyxl data_only=True | mode=NON-read-only full scan
empty-row rule=all cells in A..max_column blank after str().strip()
string compare=case-SENSITIVE
file=Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx

| sheet | read_only max_row | non-read-only max_row | non-empty rows | row indices |
|---|---|---|---|---|
| SWE1 Requirements | 226 | 226 | 14 | 1,2,3,4,6,7,8,9,10,11,12,13,14,15 |
| SYS2 Traceability | 18 | 10 | 9 | 1,2,3,4,5,6,7,8,9 |
| Excluded NRLs (HW-only) | 9 | 9 | 9 | 1,2,3,4,5,6,7,8,9 |

header row (first non-empty) = r7; data rows = r8–r15 (8)
columns (RAW, repr — note irregular whitespace):
   c1: 'SWE-Requirement ID '
   c2: 'Source Requirement ID'
   c3: 'Requirement  Title'
   c4: 'Requirement  Description'
   c5: 'Release Version'
   c6: 'Categorization'
   c7: 'Sub Categorization'
   c8: 'Feasibility'
   c9: ' Description/Action for Feasibility'
   c10: ' Impact'
   c11: 'Description/Action for  Impact'
   c12: 'Risk Factor'
   c13: 'Description/Action for Risk Factor'
   c14: 'Reusable'
   c15: 'Description/Action for Reusable'
   c16: 'Priority'
   c17: 'Verification Criteria'
   c18: 'Verification Method '

SWE-Requirement ID matches ^SWE-DM-\d{3}$ : 8/8
Source Requirement ID matches ^SYS-DISP-\d{3}$ : 8/8
Categorization distinct: ['Functional Requirement'] (Functional Requirement 8/8)
Sub Categorization distinct count: 8

| ID | Sub Categorization | Requirement Title |
|---|---|---|
| SWE-DM-001 | State Management | Display Operative State Management [ON/OFF/Wakeup] - ON/OFF states |
| SWE-DM-002 | Wake-up Management | Display Operative State Management [ON/OFF/Wakeup] - Touch Based WakeUp |
| SWE-DM-003 | Startup & Wake-up Handling | Display Operative State Management [ON/OFF/Wakeup] - Sleep and Splash |
| SWE-DM-004 | Thermal Management | Display Operative State Management & Warning Pop Ups - Hot Algorithm & Warning Expectations |
| SWE-DM-005 | Thermal Protection Management | Display Operative State Management & Warning Pop Ups - Hot Algorithm & Decisions of OFF/ON |
| SWE-DM-006 | HMI Popup Management | Display Operative State Management & Warning Pop Ups - Pop Up handling |
| SWE-DM-007 | RVC Management | Display RVC Handling - Static |
| SWE-DM-008 | Dynamic Display Arbitration | Display RVC Handling - Dynamic |

SYS2 Traceability header r1 (RAW): 'SWE1 ID' / 'Source NRL ID(s)' / 'Sys-RA-Feature-ID(s)' / 'SW/HW/System Classification' / 'SWE1 Requirement Title'
Source NRL ID(s) EMPTY: 8/8
   r2: SWE1-DM-001 | None | SYS-RA-DISP-001 | Software | Display Operative State Management [ON/OFF/Wakeup] - ON/OFF states
   r3: SWE1-DM-002 | None | SYS-RA-DISP-002 | Software | Display Operative State Management [ON/OFF/Wakeup] - Touch Based WakeUp
   r4: SWE1-DM-003 | None | SYS-RA-DISP-003 | Software | Display Operative State Management [ON/OFF/Wakeup] - Sleep and Splash
   r5: SWE1-DM-004 | None | SYS-RA-DISP-004 | Software | Display Operative State Management & Warning Pop Ups - Hot Algorithm & Warning Expectations
   r6: SWE1-DM-005 | None | SYS-RA-DISP-005 | Software | Display Operative State Management & Warning Pop Ups - Hot Algorithm & Decisions of OFF/ON
   r7: SWE1-DM-006 | None | SYS-RA-DISP-006 | Software | Display Operative State Management & Warning Pop Ups - Pop Up handling
   r8: SWE1-DM-007 | None | SYS-RA-DISP-007 | Software | Display RVC Handling - Static
   r9: SWE1-DM-008 | None | SYS-RA-DISP-008 | Software | Display RVC Handling - Dynamic

Excluded NRLs header r1 (RAW): 'NRL ID' / 'Sys-RA-Feature-ID' / 'SW/HW/System' / 'Reason Excluded'
   r2: PSCFTS020-1-45-1 | None | Hardware | Touch coordinate transmission handling over LVDS interface is below HAL scope and managed by HW supplier.
   r3: PSCFTS020-1-45-2 | None | Hardware | LVDS touch communication interface implementation is below HAL scope and managed by HW supplier.
   r4: PSCFTS020-1-45-3 | None | Hardware | LVDS display frame transmission handling is below HAL scope and managed by HW supplier.
   r5: PSCFTS020-1-45-4 | None | Hardware | DCSD backchannel communication handling is below HAL scope and managed by HW supplier.
   r6: PSCFTS020-1-56-9 | None | Hardware | HU and DCSD low-level display synchronization mechanism is below HAL scope and managed by HW supplier.
   r7: PSCFTS020-1-56-10 | None | Hardware | Display state mismatch recovery at interface communication level is below HAL scope and managed by HW supplier.
   r8: PSCFTS020-1-2-7 | None | Hardware | Display variant association and hardware configuration handling is below HAL scope and managed by HW supplier.
   r9: PSCFTS020-1-2-8 | None | Hardware | Hardware variant initialization handling is below HAL scope and managed by HW supplier.
```

**與下放包 01 §3.2 之對照**：三分頁資料列 8/8/8、`SWE-DM-\d{3}` 8/8、
`SYS-DISP-\d{3}` 8/8、`Categorization` 全為 `Functional Requirement`、
Sub Categorization 8 個相異值、`Source NRL ID(s)` 空 8/8、八個 leaf 之
標題與 Sub Categorization 逐列相符 —— **全數相符**。§3.1 所記「唯讀模式
`max_row` 為 226、實際非空列 14」亦相符。

**新增之不符項**：§3.2 所列之欄名為正規化後之寫法，原始字串含尾空格與
雙空格（A-DM5）。

### 6.3 SYS2 重算（步驟 7）

```
# SYS2 recount — measurement conditions
engine=openpyxl data_only=True | mode=READ-ONLY
data row rule=column A non-blank after str().strip(), from r2
file=SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx
sheets: ['Basic Report', 'Polarion', '_polarion']
Basic Report dims: 334 rows x 81 cols
data rows (A non-blank, r2+): 333
Sys-RA-Feature-ID ^SYS-RA-DM-\d+$ : 87
Sys-RA-Feature-ID ^SYS2-RA-\d+$  : 246
other                            : 0
ids containing 'DISP'            : 0
SYS2 Grouping blank              : 333/333

## Category x id-segment — CASE-NORMALISED (lower)
| Category | SYS-RA-DM-* | SYS2-RA-* | other | total |
|---|---|---|---|---|
| functional requirement | 44 | 36 | 0 | 80 |
| heading | 22 | 23 | 0 | 45 |
| information | 14 | 71 | 0 | 85 |
| out of scope | 7 | 116 | 0 | 123 |

## Category x id-segment — VERBATIM (case-sensitive)
| Category | SYS-RA-DM-* | SYS2-RA-* | other | total |
|---|---|---|---|---|
| Functional Requirement | 44 | 35 | 0 | 79 |
| Functional requirement | 0 | 1 | 0 | 1 |
| Heading | 22 | 23 | 0 | 45 |
| Information | 14 | 71 | 0 | 85 |
| Out of Scope | 0 | 116 | 0 | 116 |
| Out of scope | 7 | 0 | 0 | 7 |

## case-variant rows (verbatim Category differs from its lower form)
  'functional requirement': {'Functional Requirement': 79, 'Functional requirement': 1}  -> minority rows: 1
     r314 SYS2-RA-313 'Functional requirement'
  'out of scope': {'Out of scope': 7, 'Out of Scope': 116}  -> minority rows: 7
     r23 SYS-RA-DM-022 'Out of scope'
     r24 SYS-RA-DM-023 'Out of scope'
     r25 SYS-RA-DM-024 'Out of scope'
     r27 SYS-RA-DM-026 'Out of scope'
     r64 SYS-RA-DM-063 'Out of scope'
     r70 SYS-RA-DM-069 'Out of scope'
     r81 SYS-RA-DM-080 'Out of scope'
  total rows a verbatim gate would miscount: 8

## SYS2 SW/HW/System distribution (verbatim)
  'Out of Scope': 116
  'Information': 85
  'System': 47
  'Heading': 45
  'HW': 26
  'SW': 7
  'Out of scope': 7
  SW rows:
     r17 SYS-RA-DM-016 | Functional Requirement | The DCSD supplier and the HU supplier shall work together to develop a [DCSD_and_HU_LVDS_B
     r18 SYS-RA-DM-017 | Functional Requirement | The DCSD supplier and the HU supplier shall work together to develop a [DCSD* and HU CAN a
     r245 SYS2-RA-244 | Functional Requirement | [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year
     r246 SYS2-RA-245 | Functional Requirement | [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year
     r247 SYS2-RA-246 | Functional Requirement | [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year
     r248 SYS2-RA-247 | Functional Requirement | [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year
     r249 SYS2-RA-248 | Functional Requirement | [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year

## SYS2 Melco ID distinct tokens: 99
037 Excluded-NRL values found in Melco ID tokens: 8/8
   PSCFTS020-1-45-1: HIT
   PSCFTS020-1-45-2: HIT
   PSCFTS020-1-45-3: HIT
   PSCFTS020-1-45-4: HIT
   PSCFTS020-1-56-9: HIT
   PSCFTS020-1-56-10: HIT
   PSCFTS020-1-2-7: HIT
   PSCFTS020-1-2-8: HIT
```

**是否正規化大小寫：兩種算法皆已列出。** 正規化後之交叉表
（44/36、22/23、14/71、7/116）與下放包 01 §3.3 逐格相符；未正規化之原始
分布（`Out of Scope` 116、`Information` 85、`Functional Requirement` 79、
`Heading` 45、`Out of scope` 7、`Functional requirement` 1）亦逐項相符，
且變體之 8 個列號（r314 與 r23/r24/r25/r27/r64/r70/r81）與 §3.3 所記之
r314 相符、其餘 7 列為本輪新列出。`SW` = 7 列之列號 r17/r18/r245–r249
亦相符。Melco ID 8/8 命中（R-DM4 複驗成立）。

### 6.4 036 母本欄位對應與詞彙（步驟 9、canon §Phase 1 補測）

```
# 036 master probe — READ-ONLY (never saved: x14 DV, R-G1)
file=FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx
sheets: ['Cover_old', 'ChangeHistory_old', 'Cover 封面', 'ChangeHistory 修訂履歷', 'Product Document 記錄封面頁', 'Test Case Specification 測試用例規範', 'Reference', 'QS Suggestion', '下拉選單']
feature.yaml DECLARES sheet='Test Case Specification 測試用例規範' header_row=9
EFFECTIVE (derived from the master): sheet='Test Case Specification 測試用例規範' header_row=9
derivation: first sheet carrying a row within r1-r30 whose cells include both 'test item' and 'expected result'
dims: max_row=1411 max_col=34

## header row content (raw)
  B: 'No.# 序號'
  C: 'Requirement or Design ID (Polarion) 設計/需求 ID (Polarion)'
  D: 'Requirement or Design ID 需求/設計 ID'
  E: 'Test Case ID (TestRail) 測試用例 ID (TestRail)'
  F: 'Test Case ID 測試用例ID'
  G: 'Test Group 測試組'
  H: 'Test Set 測試集'
  I: 'Test Item 測試項目'
  J: 'Pre-Conditions 先前條件'
  K: 'Input Test Data 輸入條件'
  L: 'Test procedure 測試程序'
  M: 'Expected Result 預期結果'
  N: 'Specification Reference 規格參考'
  O: 'Test Case Reference ID 測項參考ID'
  P: 'Test Case Priority 測試用例優先級別'
  Q: 'Estimated Test Time (mins) 預估測試時間 （分鐘）'
  R: 'Test Case Design Methods 測試用例設計方法'
  S: 'Functional Safety 功能安全'
  T: 'HDCC27 Atl-Hi'
  U: 'DT27 Atl-Hi'
  V: 'VF(ProMaster)637 Atl-Mi'
  W: 'Commander (598) Atl-Mi'
  X: 'Regengade (5210) Atl-Mi'
  Y: 'Toro(2261) Atl-Mi'
  Z: 'Fastack (376) Atl-Mi'
  AA: 'Test Case Author 測試案例作者'
  AB: 'Test Version 測試版號'
  AC: 'Test Vehicle (Bench) 測試車型(Bench)'
  AD: 'Test Period 測試期間'
  AE: 'Tester 測試者'
  AF: 'Test Result 測試結果'
  AG: 'Defect ID 缺陷ID'
  AH: 'Remarks 備註'

## column mapping — declared vs header-derived
| key | declared | header text at declared col | expected label | verdict |
|---|---|---|---|---|
| req_id | D | Requirement or Design ID 需求/設計 ID | requirement or design id | MATCH |
| test_group | G | Test Group 測試組 | test group | MATCH |
| test_set | H | Test Set 測試集 | test set | MATCH |
| test_item | I | Test Item 測試項目 | test item | MATCH |
| pre_conditions | J | Pre-Conditions 先前條件 | pre-condition | MATCH |
| input_test_data | K | Input Test Data 輸入條件 | input | MATCH |
| test_procedure | L | Test procedure 測試程序 | procedure | MATCH |
| expected_result | M | Expected Result 預期結果 | expected result | MATCH |
| spec_reference | N | Specification Reference 規格參考 | spec | MATCH |
| tc_ref_id | O | Test Case Reference ID 測項參考ID | test case reference id | MATCH |
| priority | P | Test Case Priority 測試用例優先級別 | test case priority | MATCH |
| design_method | R | Test Case Design Methods 測試用例設計方法 | design methods | MATCH |
| functional_safety | S | Functional Safety 功能安全 | functional safety | MATCH |
| author | AA | Test Case Author 測試案例作者 | test case author | MATCH |
| remarks | AH | Remarks 備註 | remark | MATCH |

match count: 15/15
matching method: whitespace-normalised, case-insensitive substring of the expected label in the header cell at the declared column

## header-derived column map (candidates per key)
| key | expected label | candidate columns | declared | 生效提案 |
|---|---|---|---|---|
| req_id | requirement or design id | C,D | D | D |
| test_group | test group | G | G | G |
| test_set | test set | H | H | H |
| test_item | test item | I | I | I |
| pre_conditions | pre-condition | J | J | J |
| input_test_data | input | K | K | K |
| test_procedure | procedure | L | L | L |
| expected_result | expected result | M | M | M |
| spec_reference | spec | N | N | N |
| tc_ref_id | test case reference id | O | O | O |
| priority | test case priority | P | P | P |
| design_method | design methods | R | R | R |
| functional_safety | functional safety | S | S | S |
| author | test case author | AA | AA | AA |
| remarks | remark | AH | AH | AH |

## workbook_state — canon §2
data rows scanned: r10–r1411 (1402)
step 1 filled rows (Test Item or TC ID non-empty): 0 -> （無）
step 2 qualifying done rows (author AND >=2 numbered steps): 0 -> （無）
step 3 -> workbook_state = BLANK
note: 'content is non-placeholder' (step 2 third clause) is 未實測 —— with zero qualifying rows there is nothing to inspect; it is not asserted as PASS.
```

**匹配數 12/15。** 比對方法：以工作簿自身表頭列之文字為準
（whitespace 正規化 + 小寫 + 子字串），**未沿用任何既有 feature 之欄位表**。
不符 3 鍵之實測更正已寫入 `feature.yaml`：
`design_method` Q→**R**、`functional_safety` R→**S**、`author` Z→**AA**。
成因為本母本在 Q 欄多一欄 `Estimated Test Time (mins)`，其後右移一格
（A-DM7）。`req_id` 之候選有 C、D 兩欄（C 為 `(Polarion)` 版），沿用宣告
之 D。

下拉選單詞彙（`下拉選單` 分頁，9 個值，exact-string 詞彙表）：

```
功能測試 (Functional based ; no specific technique)
狀態轉換 (State Transition Testing)
決策表 (Decision Table Testing)
等價劃分 (Equivalence Partitioning, EP)
邊界值分析 (Boundary Value Analysis, BVA)
組合測試 (Combinatorial Testing ; Pairwise / t-wise)
情境 / 用例 (Scenario / Use Case Testing)
負向測試 (Negative / Invalid)
基礎故障注入 (Fault Injection Lite)
```

TC 分頁之 legacy DV 三條（openpyxl 可見者）：`P10:Q1411` = `P0,P1,P2,P3`、
`T10:Z1411` = `0,1`、`AF10:AF1411` = `Pass, Fail, Pending,Block,NA`。
R 欄（design_method）之 DV 為 x14 擴充，openpyxl 讀取即丟棄 —— 與 R-G1
所載一致，本輪全程未存回母本。

---

## 7. `workbook_state` 判定之逐列依據（步驟 10）

依 canon §2 三步，標的為 `inputs/` 之 036 母本複本，分頁
`Test Case Specification 測試用例規範`，表頭 r9，掃描 r10–r1411（1402 列）：

| 步 | 判準 | 實測 | 列號集合 |
|---|---|---|---|
| 1 | Test Item（I）或 TC ID（O）非空 → filled | **0** | 空集 |
| 2 | author（AA）非空 **且** Procedure（L）有 ≥2 個編號步驟 → qualifying | **0** | 空集 |
| 3 | filled = 0 → `BLANK` | **`BLANK`** | — |

- 步驟 2 之第三項判準「content 非 placeholder」**未實測** —— qualifying 列
  為 0，無標的可檢；依 01 §四步驟 10 之要求，標「未實測」而非 PASS。
- 判定依實測而非依「預期為 BLANK」：1402 列逐列掃過，兩個集合皆為空集
  已列出。
- 連帶生效之綁定（canon §2.1）：style authority 走 fallback chain、
  write-back 自首個資料列 append、Test Group／Test Set 欄 **FILL**
  （`feature.yaml` 之 `fill_test_group_set` 已由模板之 `false` 改為
  `true`），done invariant n/a。

> 下放包 02 §三所記「交付夾內無 036 工作簿」與本判定方向一致，但本判定
> 未以該節為據，而是以母本之逐列掃描為據。

---

## 8. spec_mode 之實測依據（步驟 11）

```
# spec_mode extraction probe
engine: python-docx (paragraphs + table cells), zipfile for media

## CFTS_020 本文 (candidate spec source, mode D) — R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx
paragraphs: 7372 (non-empty 5170)
tables: 1
non-empty table cells: 21
embedded media files: 1
extracted characters: 908640
paragraphs with a Heading style: 407
  id form melco (PSCFTS020-n-n-n): 全文 0 次 / 0 相異 | 標題(索引) 0 相異
  id form outline heading (n.n / n.n.n): 全文 366 次 / 184 相異 | 標題(索引) 182 相異
     sample: ['1.1', '1.10', '1.10.1', '1.10.1.1', '1.11']

## SYS3 SYSAD (candidate, traceability/architecture) — SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx
paragraphs: 311 (non-empty 151)
tables: 44
non-empty table cells: 1233
embedded media files: 8
extracted characters: 58108
paragraphs with a Heading style: 21
  id form melco (PSCFTS020-n-n-n): 全文 0 次 / 0 相異 | 標題(索引) 0 相異
  id form outline heading (n.n / n.n.n): 全文 29 次 / 18 相異 | 標題(索引) 1 相異
     sample: ['0.1', '0.2', '0.3', '0.5', '0.6']

## SYS2 Polarion export — outline anchor availability
columns present: Document ID=True Source Requirement items=True
  Document ID: 324/333 non-blank, 247 distinct
     'SR26_20250813-1632' x78
     'SR26_20260310-1533' x1
     'SR26_20260310-1534' x1
     'SR26_20260310-1535' x1
     'SR26_20260310-1536' x1
  Source Requirement items: 302/333 non-blank, 302 distinct
     '4819125' x1
     '4819126' x1
     '4819127' x1
     '4819128' x1
     '4819129' x1

## 交叉：SYS2 Melco ID 是否可在 CFTS 本文中定位
  SYS2 Melco tokens: 99; found verbatim in CFTS body: 1
  found verbatim in SYS3 body: 0
```

### 判讀

| 素材 | 抽取能力 | 判定 |
|---|---|---|
| CFTS_020 docx | 5170 非空段、908,640 字元、407 個 Heading 樣式段；outline id **184 相異（全文）／182 相異（標題可達）** | **判讀基準**（mode D） |
| SYS2 xlsx | `Basic Report` 333 列 × 81 欄，欄位結構完整（Category／SW-HW／Melco ID／Document ID 皆可取） | **追溯用**，非判讀基準 |
| SYS3 SYSAD docx | 151 非空段、44 表、1233 表格非空格、8 張圖；Heading 樣式段僅 21，outline id 標題可達 **1** | **架構參考**，不足以作為判讀或 spec_reference 索引 |

- **提案 `D` 成立，且係以實測支持**：CFTS 側有可用之條號索引（184/182），
  而 SYS2 側無指向 CFTS 條號之錨（`Document ID` 為逐列遞增之 Polarion
  文件 id `SR26_20260310-1533…-1778`，非條號；Melco token 99 個在 CFTS
  本文逐字命中者僅 1 個且該 token 為 `NA`）。故 spec_reference 只能
  「查得」而非「構造」，正是 canon §3 對 mode D 之定義。
- 惟自 SWE-DM leaf 走到 CFTS 條號之鏈路每一段都無 id 橋樑（A-DM10）。
  `spec_reference_template` 已設為 `null`。
- SYS3 之 21 個 Heading 中只有 1 個帶 outline 形態編號，且內容集中在表格
  與圖，故不列為判讀基準。

---

## 9. R-DM7 覆蓋對照表（步驟 8）

母體：SYS2 `Category` 正規化為 `functional requirement` 之 **80 列**
（含 r314 之大小寫變體 1 列）。全表（80 列，含每列之依據）機器產出於
`features/display/data/coverage_sys2_vs_swe_dm.tsv`，人可讀版見下。

依據之定義（不是裁定）：

- `id`：該列之 `SYS2 Sys-RA-Feature-ID` 等於 037 `SYS2 Traceability` 之
  `Sys-RA-Feature-ID(s)` 值之一 —— **實測 0 列**
- `Melco`：該列之 Melco ID 出現於 037 `Excluded NRLs (HW-only)` —— 命中即
  表示 037 明列排除，**不構成 leaf 對應**
- `Description 文字`：機械 bag-of-words 重疊（小寫、去停用詞、長度 ≥4），
  門檻 3 個共通 token。**此為搜尋輔助，非對應之認定**
- `無`：以上皆不成立（最佳文字分數一併列出）

| SYS2 列 | Sys-RA-Feature-ID | Melco ID | SW/HW | 對應 SWE-DM | 對應依據 |
|---|---|---|---|---|---|
| r13 | SYS-RA-DM-012 | PSCFTS020-1-116-1 PSCFTS020-1-116-2 PSCFTS020-1-262-1 PSCFTS020-1-262-2 | System | 無 | 無（最佳文字分數 2，SWE-DM-002 ['dcsd', 'received']） |
| r17 | SYS-RA-DM-016 | PSCFTS020-1-45-5 PSCFTS020-1-45-6 | SW | 無 | 無（最佳文字分數 2，SWE-DM-002 ['dcsd', 'touch']） |
| r18 | SYS-RA-DM-017 | PSCFTS020-1-45-5 PSCFTS020-1-45-6 PSCFTS020-1-88-10 PSCFTS020-1-88-11 | SW | 無 | 無（最佳文字分數 1，SWE-DM-001 ['dcsd']） |
| r26 | SYS-RA-DM-025 | PSCFTS020-1-109-7 PSCFTS020-1-109-8 | HW | 無 | 無（最佳文字分數 0） |
| r28 | SYS-RA-DM-027 | PSCFTS020-1-109-11 PSCFTS020-1-109-12 | HW | 無 | 無（最佳文字分數 0） |
| r31 | SYS-RA-DM-030 | NA | System | SWE-DM-001 | Description 文字：共通 token 3 個 ['dcsd', 'send', 'transition'] |
| r32 | SYS-RA-DM-031 | NA | System | SWE-DM-001 | Description 文字：共通 token 3 個 ['dcsd', 'send', 'transition'] |
| r33 | SYS-RA-DM-032 | NA | System | 無 | 無（最佳文字分數 2，SWE-DM-001 ['dcsd', 'send']） |
| r34 | SYS-RA-DM-033 | NA | System | SWE-DM-003 | Description 文字：共通 token 4 個 ['normal', 'resume', 'screen', 'sequence'] |
| r37 | SYS-RA-DM-036 | PSCFTS020-1-48-1 PSCFTS020-1-48-2 | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r39 | SYS-RA-DM-038 | PSCFTS020-1-49-1 PSCFTS020-1-49-2 | System | 無 | 無（最佳文字分數 2，SWE-DM-003 ['normal', 'screen']） |
| r41 | SYS-RA-DM-040 | PSCFTS020-1-50-1 PSCFTS020-1-50-2 | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r42 | SYS-RA-DM-041 | PSCFTS020-1-50-7 PSCFTS020-1-50-8 | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r44 | SYS-RA-DM-043 | PSCFTS020-1-52-1 PSCFTS020-1-52-2 | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r45 | SYS-RA-DM-044 | PSCFTS020-1-38-5 PSCFTS020-1-52-7 PSCFTS020-1-52-8 | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r47 | SYS-RA-DM-046 | PSCFTS020-1-53-5 PSCFTS020-1-53-6 | System | SWE-DM-002 | Description 文字：共通 token 5 個 ['active', 'coordinates', 'dcsd', 'previous', 'touch'] |
| r49 | SYS-RA-DM-048 | PSCFTS020-1-54-1 PSCFTS020-1-54-2 | System | 無 | 無（最佳文字分數 1，SWE-DM-001 ['send']） |
| r52 | SYS-RA-DM-051 | PSCFTS020-1-56-1 PSCFTS020-1-56-2 | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r53 | SYS-RA-DM-052 | PSCFTS020-1-56-7 PSCFTS020-1-56-8 | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r54 | SYS-RA-DM-053 | PSCFTS020-1-56-9 PSCFTS020-1-56-10 | System | 無 | Melco：037 Excluded NRLs (HW-only) 列有此 Melco ID （['PSCFTS020-1-56-10', 'PSCFTS020-1-56-9']）—— 037 明列排除，非 leaf 對應 |
| r56 | SYS-RA-DM-055 | PSCFTS020-1-57-3 PSCFTS020-1-57-4 | System | SWE-DM-002 | Description 文字：共通 token 4 個 ['coordinates', 'dcsd', 'previous', 'touch'] |
| r58 | SYS-RA-DM-057 | — | HW | 無 | 無（最佳文字分數 0） |
| r59 | SYS-RA-DM-058 | — | HW | 無 | 無（最佳文字分數 0） |
| r60 | SYS-RA-DM-059 | — | HW | 無 | 無（最佳文字分數 0） |
| r61 | SYS-RA-DM-060 | — | HW | 無 | 無（最佳文字分數 0） |
| r65 | SYS-RA-DM-064 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-001 ['dcsd']） |
| r66 | SYS-RA-DM-065 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['touch']） |
| r67 | SYS-RA-DM-066 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-001 ['dcsd']） |
| r68 | SYS-RA-DM-067 | — | HW | 無 | 無（最佳文字分數 2，SWE-DM-002 ['dcsd', 'touch']） |
| r69 | SYS-RA-DM-068 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['touch']） |
| r71 | SYS-RA-DM-070 | — | HW | 無 | 無（最佳文字分數 2，SWE-DM-002 ['dcsd', 'touch']） |
| r73 | SYS-RA-DM-072 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-001 ['dcsd']） |
| r74 | SYS-RA-DM-073 | — | HW | SWE-DM-002 | Description 文字：共通 token 3 個 ['dcsd', 'previous', 'touch'] |
| r76 | SYS-RA-DM-075 | — | System | 無 | 無（最佳文字分數 2，SWE-DM-002 ['coordinates', 'touch']） |
| r77 | SYS-RA-DM-076 | — | HW | 無 | 無（最佳文字分數 0） |
| r78 | SYS-RA-DM-077 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['touch']） |
| r79 | SYS-RA-DM-078 | — | System | 無 | 無（最佳文字分數 0） |
| r80 | SYS-RA-DM-079 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['touch']） |
| r82 | SYS-RA-DM-081 | — | HW | SWE-DM-002 | Description 文字：共通 token 5 個 ['coordinates', 'dcsd', 'event', 'touch', 'valid'] |
| r83 | SYS-RA-DM-082 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['touch']） |
| r84 | SYS-RA-DM-083 | — | HW | SWE-DM-002 | Description 文字：共通 token 3 個 ['coordinates', 'dcsd', 'touch'] |
| r86 | SYS-RA-DM-085 | — | HW | 無 | 無（最佳文字分數 2，SWE-DM-002 ['coordinates', 'touch']） |
| r87 | SYS-RA-DM-086 | — | HW | 無 | 無（最佳文字分數 2，SWE-DM-002 ['dcsd', 'touch']） |
| r88 | SYS-RA-DM-087 | — | HW | SWE-DM-002 | Description 文字：共通 token 3 個 ['coordinates', 'dcsd', 'touch'] |
| r182 | SYS2-RA-181 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-005 ['determine']） |
| r183 | SYS2-RA-182 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-003 ['screen']） |
| r184 | SYS2-RA-183 | — | HW | SWE-DM-006 | Description 文字：共通 token 3 個 ['events', 'priority', 'requests'] |
| r185 | SYS2-RA-184 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-005 ['determine']） |
| r188 | SYS2-RA-187 | — | System | 無 | 無（最佳文字分數 2，SWE-DM-003 ['normal', 'screen']） |
| r189 | SYS2-RA-188 | — | System | 無 | 無（最佳文字分數 2，SWE-DM-003 ['normal', 'screen']） |
| r190 | SYS2-RA-189 | — | System | SWE-DM-006 | Description 文字：共通 token 3 個 ['events', 'priority', 'requests'] |
| r192 | SYS2-RA-191 | — | System | 無 | 無（最佳文字分數 2，SWE-DM-002 ['previous', 'touch']） |
| r193 | SYS2-RA-192 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-001 ['send']） |
| r194 | SYS2-RA-193 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-001 ['send']） |
| r195 | SYS2-RA-194 | — | System | 無 | 無（最佳文字分數 2，SWE-DM-003 ['normal', 'screen']） |
| r201 | SYS2-RA-200 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-005 ['determine']） |
| r202 | SYS2-RA-201 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-003 ['screen']） |
| r203 | SYS2-RA-202 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-002 ['received']） |
| r209 | SYS2-RA-208 | — | HW | 無 | 無（最佳文字分數 2，SWE-DM-003 ['normal', 'screen']） |
| r213 | SYS2-RA-212 | — | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r217 | SYS2-RA-216 | — | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r219 | SYS2-RA-218 | — | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r222 | SYS2-RA-221 | — | System | 無 | 無（最佳文字分數 2，SWE-DM-001 ['conditions', 'send']） |
| r226 | SYS2-RA-225 | — | System | SWE-DM-008 | Description 文字：共通 token 4 個 ['camera', 'rear', 'screen', 'view'] |
| r238 | SYS2-RA-237 | — | System | 無 | 無（最佳文字分數 2，SWE-DM-002 ['coordinates', 'touch']） |
| r241 | SYS2-RA-240 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-001 ['send']） |
| r245 | SYS2-RA-244 | — | SW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['event']） |
| r246 | SYS2-RA-245 | — | SW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['touch']） |
| r247 | SYS2-RA-246 | — | SW | 無 | 無（最佳文字分數 2，SWE-DM-002 ['event', 'touch']） |
| r248 | SYS2-RA-247 | — | SW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['event']） |
| r249 | SYS2-RA-248 | — | SW | 無 | 無（最佳文字分數 1，SWE-DM-002 ['touch']） |
| r294 | SYS2-RA-293 | — | System | 無 | 無（最佳文字分數 0） |
| r295 | SYS2-RA-294 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-001 ['manage']） |
| r296 | SYS2-RA-295 | — | System | 無 | 無（最佳文字分數 0） |
| r297 | SYS2-RA-296 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-001 ['manage']） |
| r298 | SYS2-RA-297 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-003 ['screen']） |
| r299 | SYS2-RA-298 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-003 ['screen']） |
| r302 | SYS2-RA-301 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-004 ['logic']） |
| r303 | SYS2-RA-302 | — | HW | 無 | 無（最佳文字分數 1，SWE-DM-007 ['signal']） |
| r314 | SYS2-RA-313 | — | System | 無 | 無（最佳文字分數 1，SWE-DM-005 ['determine']） |

## 依據別統計
  melco: 1
  id: 0
  text: 22
  none: 57

## 無對應之列（列號 + Sys-RA-Feature-ID）
  count = 58
  r13 SYS-RA-DM-012, r17 SYS-RA-DM-016, r18 SYS-RA-DM-017, r26 SYS-RA-DM-025, r28 SYS-RA-DM-027, r33 SYS-RA-DM-032, r39 SYS-RA-DM-038, r49 SYS-RA-DM-048, r54 SYS-RA-DM-053, r58 SYS-RA-DM-057, r59 SYS-RA-DM-058, r60 SYS-RA-DM-059, r61 SYS-RA-DM-060, r65 SYS-RA-DM-064, r66 SYS-RA-DM-065, r67 SYS-RA-DM-066, r68 SYS-RA-DM-067, r69 SYS-RA-DM-068, r71 SYS-RA-DM-070, r73 SYS-RA-DM-072, r76 SYS-RA-DM-075, r77 SYS-RA-DM-076, r78 SYS-RA-DM-077, r79 SYS-RA-DM-078, r80 SYS-RA-DM-079, r83 SYS-RA-DM-082, r86 SYS-RA-DM-085, r87 SYS-RA-DM-086, r182 SYS2-RA-181, r183 SYS2-RA-182, r185 SYS2-RA-184, r188 SYS2-RA-187, r189 SYS2-RA-188, r192 SYS2-RA-191, r193 SYS2-RA-192, r194 SYS2-RA-193, r195 SYS2-RA-194, r201 SYS2-RA-200, r202 SYS2-RA-201, r203 SYS2-RA-202, r209 SYS2-RA-208, r222 SYS2-RA-221, r238 SYS2-RA-237, r241 SYS2-RA-240, r245 SYS2-RA-244, r246 SYS2-RA-245, r247 SYS2-RA-246, r248 SYS2-RA-247, r249 SYS2-RA-248, r294 SYS2-RA-293, r295 SYS2-RA-294, r296 SYS2-RA-295, r297 SYS2-RA-296, r298 SYS2-RA-297, r299 SYS2-RA-298, r302 SYS2-RA-301, r303 SYS2-RA-302, r314 SYS2-RA-313

## 每個 SWE-DM leaf 被指到之列數（僅文字依據，非裁定）
  SWE-DM-001 (State Management): 2
  SWE-DM-002 (Wake-up Management): 6
  SWE-DM-003 (Startup & Wake-up Handling): 1
  SWE-DM-004 (Thermal Management): 0
  SWE-DM-005 (Thermal Protection Management): 0
  SWE-DM-006 (HMI Popup Management): 2
  SWE-DM-007 (RVC Management): 0
  SWE-DM-008 (Dynamic Display Arbitration): 11

wrote /Users/peihe/Work_Projects/TC_Generator/features/display/data/coverage_sys2_vs_swe_dm.tsv

**揭露而非界定**：本表之用途為 R-DM7 所要求之揭露。80 列中 58 列無對應，
且 `SWE-DM-004`／`005`／`007` 之文字依據命中列數為 0。範圍之裁定屬
Tier 2（下放包 01 Q2），執行層不裁定，亦不主張「037 之 8 筆即全集」。

---

## 10. `feature.yaml` 草案全文（步驟 13）

宣告值（scaffold 模板所填）與生效值（本輪實測）分列於 §6.4；下為最終檔：

```yaml
# feature.yaml — pipeline configuration for Display
# All feature-specific constants live HERE; shared scripts read this file
# and contain no per-feature literals. Regenerate nothing by editing code.

feature: "Display"
test_group: "Display"          # framework-internal; workbook write per profile

paths:
  workbook: "inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx"   # R-G1 母本；sha256 6372fb6b…
  a03_report: "inputs/Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx"   # R-DM2′；intake.py sniffer 誤判為 spec_xlsx（R-DM5(a)），故本行為人工填入
  sys1_export: "inputs/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx"        # null if spec_mode has no export
  spec_pdf: "inputs/R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx"   # CFTS 本文；spec_mode D 之判讀基準
  sys3_sysad: "inputs/SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx"   # 追溯/架構參考，非判讀基準（intake.py A-TM10 未填入）
  popup_list: null                       # 交付夾內無 Pop Up List

spec_mode: "D"        # A/B/C/D/E per FO §3
spec_reference_template: null   # mode D：spec_reference 為查得，非構造（canon §3）

workbook:
  sheet: "Test Case Specification 測試用例規範"   # 實測自母本；模板之 rev A/B 名在本母本不存在
  header_row: 9
  # column letters, verified by recon header match — do not guess
  columns:
    req_id: "D"
    test_group: "G"
    test_set: "H"
    test_item: "I"
    pre_conditions: "J"
    input_test_data: "K"
    test_procedure: "L"
    expected_result: "M"
    spec_reference: "N"
    tc_ref_id: "O"
    priority: "P"
    design_method: "R"      # 實測；母本 Q 欄為 Estimated Test Time
    functional_safety: "S"  # 實測
    author: "AA"            # 實測；母本 Z 欄為 Fastack (376) Atl-Mi
    remarks: "AH"      # verify at recon; dropping it drops BLOCKED notes

done_region:
  # detection: "author" (author-cell match) or "rows" (explicit ranges)
  detection: "author"     # workbook_state = BLANK：無 done region，本節不生效
  author_value: null      # BLANK：無既有作者
  # invariant: "content_hash" (interleaved-safe) or "positional"
  invariant: "content_hash"

write_back:
  author_value: "PeiPYHsu"
  tc_ref_id_value: "NEW"
  fill_test_group_set: true      # workbook_state = BLANK -> FILL（canon §2.1）

lint:
  design_method_source: "dropdown_sheet"   # exact-string vocabulary
  popup_ids: []                            # e.g. [PU0091, PU0942] — verbatim check
  extra_rules: []                          # feature-specific lint hooks
```

宣告 vs 生效之差異一覽：

| 鍵 | 宣告（模板／scaffold） | 生效（實測） | 依據 |
|---|---|---|---|
| `workbook.sheet` | `Test Case Specification&Result` | `Test Case Specification 測試用例規範` | 母本無模板之分頁名（A-DM7） |
| `columns.design_method` | `Q` | `R` | 母本 Q 欄為 Estimated Test Time |
| `columns.functional_safety` | `R` | `S` | 表頭比對 |
| `columns.author` | `Z` | `AA` | 母本 Z 欄為 Fastack (376) Atl-Mi |
| `paths.a03_report` | `inputs/<037 xlsx>`（未填） | 037 實際路徑 | sniffer 未認出（R-DM5(a)），人工填入 |
| `paths.popup_list` | `inputs/<Pop Up List xlsx>` | `null` | 交付夾內無此檔 |
| `paths.sys3_sysad` | （模板無此鍵） | SYS3 路徑 | intake.py A-TM10 未填，另立鍵 |
| `spec_reference_template` | `<Spec Filename>_{outline}` | `null` | mode D：查得而非構造（A-DM10） |
| `done_region.author_value` | `Arif` | `null` | `workbook_state = BLANK` |
| `write_back.fill_test_group_set` | `false` | `true` | canon §2.1 之 BLANK 綁定 |

`test_group` 為 `Display`（R-DM1）。037 之模組名 `Display Management`
與 CFTS_020 之 `ICS and DCSD` 未進入任何欄位，僅見於本檔之路徑與註解。

---

## 11. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 8 項。** 逐項列出，不以「已依步驟執行完畢」代替此判斷。

1. **`recon.py` 之全部產物未取得。** `RECON.md`／`DECISIONS.md`／
   `data/recon.json` 本輪不存在（A-DM8）。凡 recon 才會算的項目
   （leaf inventory、coverage-gap counts、done-region req_id sets 等）
   本輪只有我手寫腳本涵蓋到的部分，**未經 repo 既有管線複核**。
2. **need list「不可推導」未受檢驗**（A-DM9）。sniffer 修好前，
   037 之 `Source Requirement ID` 欄語意是否真的不可推導，無人驗過。
3. **覆蓋對照之文字依據是啟發式。** 22 列之「有對應」與 57 列之「無」
   都可能被停用詞表與門檻 3 左右。此數字可用於揭露落差之量級，
   **不可用於任何「涵蓋率」之主張**。
4. **037 之 8 筆需求描述本文未逐條精讀。** 本輪只取了 ID／Title／
   Sub Categorization／Categorization 與描述之 token，`Requirement
   Description` 之語意、`Verification Criteria`／`Verification Method`
   二欄之內容皆未檢視（後者依 R-DM8 末段本輪一律不用）。
5. **SYS2 之 `Polarion` 與 `_polarion` 兩個分頁完全未看。** 只測了
   `Basic Report`。二者是否另有追溯欄位，未知。
6. **R-DM8 之四處缺值只做了 regex 定位。** 004／005 記到章節
   （`1.11.2.2 DCSD Display Hot Behavior {4820281}` 等），但**門檻值本身
   未讀出、未確認其適用架構**（CFTS 有 1.8／1.11／1.15.1／1.15.2／1.15.4
   數套架構分節，何者適用本專案未查）。這是 Phase 2 之事，但須明記本輪
   沒做。
7. **CFTS 之 184 個 outline id 未與 037 之 8 個 leaf 建立任何對應。**
   spec_reference 之實際取得路徑仍是空的（A-DM10）。
8. **036 母本之 x14 DV 完好性只以 SHA256 佐證。** 本輪未對
   `inputs/` 複本做 zip member 層級之檢查（R-G1 所述之 48→47 判準）。
   雜湊與來源相同即可推得未被改動，但「未被改動」與「原本就完好」是
   兩件事，後者未驗。

另記兩項**已驗而下放包未要求**者：037 A/B 逐格比對本輪獨立複算
（4606 格、差異 0，見 §16）；三份素材之交付夾版與歸檔版雜湊比對（§3）。

---

## 12. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(display): open feature — intake, rulings, recon measurements

- materials ledger: 4 sources from ASW-R2/Display, sha256 verified,
  037 matches R-DM2' 64-char hash; 3 archived copies identical
- RULINGS.md: 13 rulings transcribed verbatim (machine-extracted, 13/13)
- independent recount of 037 and SYS2 reproduces every handoff figure,
  both case-normalised and verbatim
- R-DM7 coverage cross-reference: 80 SYS2 FR rows, 58 with no leaf link
- feature.yaml from measurement: sheet name and 3 column letters differ
  from the scaffold template against the R-G1 master
- workbook_state = BLANK (0 filled of 1402 rows)
- A-DM1..A-DM11 registered, DR-DM1..DR-DM3 opened
```

pathspec（**併行 session 會 stage 他檔，務必帶路徑**）：

```
git add features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/DECISIONS.md \
        features/display/RUNBOOK.md \
        features/display/PLAYBOOK.md \
        features/display/feature.yaml \
        features/display/.gitignore \
        features/display/scripts/ \
        features/display/data/materials_ledger.tsv \
        features/display/data/coverage_sys2_vs_swe_dm.tsv \
        features/display/docs/
```

`features/display/inputs/` 由該 feature 之 `.gitignore` 排除（客戶素材
不進 git）；`_intake/Display/` 亦已被根 `.gitignore` 排除。

---

## 13. `docs/INDEX.md` 與 `DECISIONS.md`

已建立 `features/display/docs/INDEX.md`，含 01（步驟 1 停手）與 02
（步驟 1–14 全跑）兩輪次列，並附本輪之相符／不符要點。

`DECISIONS.md` 依慣例應由 `recon.py` 產出，本輪因 A-DM8 未能產出，故由
執行層以本輪之量測值逐項填寫，並於檔頭明記其非 recon 產物、凡未測者
標「未實測」。`[PEI]` 兩項為 `spec_reference format`（A-DM10 使其無法提案）
與 Q2／Q3；`[PROPOSED]` 各項未經 Pei 修改即於簽核時生效。

---

## 14. `A-DM{n}` 異常清單

全文見 `features/display/ANOMALIES.md`。摘要：

| 編號 | 主旨 | 狀態 |
|---|---|---|
| A-DM1 | 037 二分頁 id 兩套寫法（`SWE-DM-nnn` / `SWE1-DM-nnn`） | PENDING |
| A-DM2 | `SYS-RA-DISP-*` 在 SYS2 released 版 0 命中 | PENDING |
| A-DM3 | `Source NRL ID(s)` 8/8 空，Excluded 分頁反有 id | PENDING |
| A-DM4 | SYS2 `Category` 大小寫變體 8 列 | PENDING |
| A-DM5 | 037 表頭含不規則空白，逐字取欄必失敗 | PENDING |
| A-DM6 | Excluded 分頁 `Sys-RA-Feature-ID` 8/8 空 | PENDING |
| A-DM7 | scaffold 模板 vs R-G1 母本：1 分頁名 + 3 欄不符 | PENDING |
| A-DM8 | `recon.py` 於 037 分頁名中止，recon 產物缺 | PENDING |
| A-DM9 | `intake.py` need-list 之理由失真 | PENDING |
| A-DM10 | SYS2 無 CFTS 條號錨，mode D 無 id 橋樑 | PENDING |
| A-DM11 | 覆蓋落差：80 列母體 58 列無對應 | PENDING |

下放包 02 §五指定之首批四項對應為 A-DM1／A-DM2／A-DM3／A-DM4，內容依
指定；A-DM5–A-DM11 為本輪實測新增。A/B 版本歧異依 R-DM10 未列入
（並已於 §16 複算確認）。

## 14b. `DR-DM{n}` 開放清單

全文見 `features/display/DATA_REQUESTS.md`。

| # | 需求 | Leaves | Urgency |
|---|---|---|---|
| DR-DM1 | CFTS_009（條號 `{CFTS009-722}`，定義 Splash/Disclaimer 時段） | SWE-DM-003 | HIGH |
| DR-DM2 | popup 優先序仲裁規則與 timeout 之來源 | SWE-DM-006 | HIGH |
| DR-DM3 | `SYS-RA-DISP-*` ↔ SYS2 對應表，或含 `DISP` id 之 SYS2 版本 | 全 8 leaf | MEDIUM |

R-DM8 之查證義務已履行：004／005 於 CFTS **查得**章節
（`1.11.2.2 DCSD Display Hot Behavior {4820281}`，另 `1.15.1.5 {4820659}`／
`1.15.2.5 {4820937}`／`1.15.4.x`），故不開 DR，僅記位置；003 之時段被 CFTS
轉指外部條號 `{CFTS009-722}`，006 在 CFTS 只有個別「high priority RVC」
語句而無仲裁表與 timeout，二者開 DR。**四處值皆未回填。**

---

## 15. 停止條件逐條回報（01 §五九條）

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | **未觸發**（01 預期會觸發）。`SYS-RA-DISP-*` 0 命中一事，R-DM3 已明定其處置為「登記而非解決」，本輪即以 A-DM2 登記，未作跨命名推定，故不構成未解之查找 |
| 2 | `workbook_state` 分段有歧義 | 未觸發（filled = 0，無分段可歧義） |
| 3 | 寫回不變量違反 | 未觸發（本輪無任何工作簿寫入；母本全程未 `save()`） |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | **未觸發**（01 預期會觸發）。R-DM8 之四處值本輪一處未填：查得者只記章節，查不得者開 DR-DM1／DR-DM2 |
| 6 | done region 與規格矛盾 | 未觸發（無 done region） |
| 7 | scaffold 會覆寫既有檔 | 未觸發（見 §5 末之覆寫檢查） |
| 8 | `_intake/Display/` 清單不符 | 未觸發（依 02 §五改判之條件，與 R-DM9 來源目錄之四份逐字相符） |
| 9 | 需修改 `scripts/` 既有腳本才能繼續 | 未觸發。`recon.py` 失敗後即停止該步並登記，未修腳本亦未繞道；後續步驟 13／14 不依賴其產物 |

---

## 16. A 之 `max_row` 228 vs 226 —— 量測條件確認（下放包 02 §六第 16 項）

下放包 02 §2.2 推測該差異「應為唯讀模式與非唯讀模式之 `max_row` 計算
不同」。**該推測不成立。** 實測：

| 檔 | 分頁 | read_only `max_row` | 非 read_only `max_row` |
|---|---|---|---|
| A | `SWE1 Requirements` | **228** | **226** |
| B | `SWE1 Requirements` | **226** | **226** |
| A / B | `SYS2 Traceability` | 18 | 10 |
| A / B | `Excluded NRLs (HW-only)` | 9 | 9 |

兩種模式之差確實存在（A 之 228 vs 226、兩檔之 Traceability 18 vs 10），
但 **228 這個數字只出現在 A**：B 在唯讀模式下即為 226。故 228 與 226 之
差不是模式差，而是**兩檔所宣告之 sheet dimension 不同**（A 宣告到 228 列，
B 宣告到 226 列）。執行層先前回報之「A max_row = 228」係唯讀模式所得，
數字無誤。

此差異仍屬 §2.2 之結論範疇 —— **格式／中繼資料層，非內容層**。本輪並
獨立複算了逐格比對（`data_only=True`、非唯讀、三分頁取
`max_row × max_column` 之聯集、越界取 `None`）：

```
比對格數 4606；差異 0
```

**與分析層之 0 差異格一致。** R-DM10 之處置維持：A 不搬入、不引用，
僅記於台帳之「同內容他處副本」欄（`materials_ledger.tsv` 已記，
verdict = `SAME_CONTENT_DIFF_FILE (R-DM10: 0 差異格)`）。
