# 上繳包 00 — vsm_v43（Vehicle Setup Management R1L TBM，VF665 V43）：進場與 recon

日期：2026-09-01　執行層　對應下放包：`docs/handoff/00_intake_and_rulings.md`
條號系列：`R-VT`　姊妹線 `vsm_v42` 獨立（本包不涉，未讀寫其任何檔以外之引用）

---

## 〇、一句話結論

**本包停於 W-1。** `_intake/Vehicle_Setup_VF665/` 實測為**空目錄**，
下放包 §三 #1–#3 之原檔**一件未投遞**，W-2～W-5 全部不可執行。
W-1（scaffold ＋ `feature.yaml`）已完成，W-6（anomaly／DR）已登記。
**§六 E1–E9 之九項預期數字本包一項亦無法實測** —— 非「相符」，是「無素材」。

停下依據：下放包本身之 W-1 條件（「#1–#3 原檔未齊者停於 W-1 並回報缺件」）；
併觸 FO §0 停下條款第 1 條（missing file）與下放包 §八升級條件第 3 條
（`recon.py` 需改碼方能跑，見 §三）。

## 一、作業清單完成狀態

| 項 | 內容 | 狀態 |
|---|---|---|
| W-1 | scaffold ＋ `feature.yaml` | **完成** |
| W-2 | sources 落檔／sha／R-G28 | **未執行**（無原檔，A-VT1） |
| W-3 | recon | **未執行**；`recon.py` 不支援無 037 之判定已作成（A-VT3） |
| W-4 | SYSRA 分層預查 `data/sysra_v43_functional.tsv` | **未執行**（無 #2，A-VT1） |
| W-5 | R-VT2 訊號解析預查 `data/signal_chain_v43.tsv` | **未執行**（無 #1，A-VT1） |
| W-6 | anomaly／DR | **完成**（A-VT1–A-VT4 登記；DR-VT1／DR-VT2 沿用，未送出） |

---

## 二、W-1 scaffold 輸出（逐字）

指令：`python3 scripts/new_feature.py vsm_v43 --adopt-existing`

```
scaffolded /Users/peihe/Work_Projects/TC_Generator/features/vsm_v43
  kept existing (not overwritten): DATA_REQUESTS.md, RULINGS.md
next steps:
  1. drop source files into .../features/vsm_v43/inputs
  2. fill .../features/vsm_v43/feature.yaml (spec_mode, paths)
  3. run Phase 1 recon (Claude Code, Tier 1)
  4. review DECISIONS.md [PROPOSED] items and sign (Tier 2)
```

產出（`--adopt-existing` 未覆寫既有兩檔，符合預期）：

```
features/vsm_v43/
  .gitignore  ANOMALIES.md  DECISIONS.md  PLAYBOOK.md  RUNBOOK.md  feature.yaml
  batches/  data/  docs/  generated/  inputs/  scripts/
  （既存未動：RULINGS.md、DATA_REQUESTS.md、docs/handoff/00_intake_and_rulings.md）
```

### 2.1 `feature.yaml` 之落值

| 鍵 | 值 | 依據 |
|---|---|---|
| `feature` | `Vehicle Setup Management R1L TBM` | R-VT3 |
| `test_group` | `Vehicle Setup Management R1L TBM` | R-VT3（Layer 1） |
| `tc_id_prefix` | `NR1L-VSM43-` | 下放包 §五 W-1 原文；**鍵名爭點見 A-VT2** |
| `paths.a03_report` | `null`，就地註 **DR-VT1** | R-VT4；037 = 0 |
| `paths.workbook` | `null` | R-VT1 BLANK 起建，工作簿尚未建（W-2 未執行） |
| `paths.spec_docx` / `sysra_export` / `sysad` | `TBD` | 原檔未投遞（A-VT1）；不猜檔名 |
| `paths.sys1_export` / `spec_pdf` / `popup_list` | `null` | 本 feature 無 |
| `spec_mode` | `D` | 下放包 §三 #1 為 docx；scaffold 原值 `A` 為模板值 |
| `done_region.author_value` | `null` | BLANK 起建無 done region；scaffold 原值 `"Arif"` 為模板值 |
| `write_back.fill_test_group_set` | `true` | BLANK，FO §2 |
| `workbook.columns` | **未改，全為 scaffold 模板值** | 無工作簿可測；已就地標註 power A-PW37 錯位先例，W-2 後須自 r9 表頭複驗 |

`a03_report: null` 之註記全文已寫入 `feature.yaml`，載明：037 不存在、
現有 037 兩份之 Source Requirement ID 152/152 皆為 V42、依 R-VT4 止於 P0–P3、
阻塞型請求為 DR-VT1、**不得以 SYSRA 或規格代 037 建母體或生成 TC**。

YAML 可解析性已驗（`yaml.safe_load` 通過，`paths` 讀回如上）。

---

## 三、缺件回報（下放包 §三 #1–#3）

實測（2026-09-01）：

```
$ ls -la _intake/Vehicle_Setup_VF665/
total 0
drwxr-xr-x   2 peihe  staff   64 Sep  1 16:19 .
drwxr-xr-x  14 peihe  staff  448 Sep  1 16:19 ..
```

| # | doc_id（擬） | 檔名（下放包所載） | 投遞區實測 | 全庫實測 |
|---|---|---|---|---|
| 1 | `vf665_v43_spec_r4` | `Vehicle Setup Management by VP - LTM (R1L) with TBM [VF665_V43_R4].docx` | **無** | 無 |
| 2 | `vf665_v43_sysra` | `FMWIFSM035A02_VF665_V43_STLA_SYSRA…_VF665_V43_Release.xlsx` | **無** | 無 |
| 3 | `vf665_sysad_sys3` | SYSAD SYS3 v1.0 docx | **無** | 無（`vsm_v42` 亦未落檔，`sources/raw/` 無此 doc_id） |

旁證：
- `find . -iname "*V43*"` 命中二筆，皆非素材：`features/vsm_v43/`（本包 scaffold）、
  `features/vehicle_setting/docs/handoff/V43_writeback_unfreeze.md`（他線文件）。
- `sources/raw/` 現有三目錄：`core_hmi_lf_pdf`、`core_hmi_lf_sys1`、`popup_037_v0_2`。無 V43。
- DR-VT1 所述之「現有 037 兩份」（Park Sense And Restore Default Setting／
  Side Distance Warning Audio Repetition）於全庫 `*.xlsx` 亦查無，故 **E7 亦不可實測**。

**故 W-2 之 sources 落檔與 sha：無可落、無可算。R-G28（CFTS 嵌入物件）：無母檔可查，
本項未執行**（非「已查而查無」—— 兩者不可混同）。

### 3.1 `recon.py` 對 `a03_report: null` 之行為（W-3 前置判定）

依 W-3 指示先查腳本，**未改碼**。原始碼判讀（未跑；本線既無工作簿亦無 037，跑不起來）：

- `scripts/recon.py:1150-1156`：`p = resolve_glob(feature_dir, pat) if pat else None`
  → 路徑為 null 時 `paths[key] = None`，**其後無任何 None guard**。
- `scripts/recon.py:1164`：`survey_workbook(cfg, paths["workbook"])`
  → `:430 openpyxl.load_workbook(wb_path)`，`wb_path=None` 即 TypeError。
- `scripts/recon.py:1165`：`survey_a03(paths["a03_report"], …)`
  → `:582 openpyxl.load_workbook(a03_path, read_only=True)`，同上。
- `--help` 之旗標僅 `--feature`／`--root`，無「缺 037」路徑。

**結論：`recon.py` 需改碼方能於 037 = 0 之 feature 上執行** → 登 A-VT3，
併觸下放包 §八升級條件第 3 條。依 W-3「不改腳本」，改人工 `RECON.md`；
**惟人工 `RECON.md` 之三項內容中，素材 sha 與 SYSRA 計數皆依賴 A-VT1 之原檔**，
故本包**亦未產出人工 `RECON.md`**（僅 workbook_state = BLANK 一項可寫，
單此一項不成一份 RECON）。原檔到齊後補。

> §七 之「`RECON.md`（機器或人工，註明何者）」一項：**本包無 RECON.md，
> 機器與人工皆無**，理由如上。

---

## 四、§六 E1–E9 逐項對照（相符者亦列）

**全部九項「未實測」，理由同一：素材 #1／#2 未投遞（A-VT1）。**
下欄「實測」一律不填臆測值，亦不轉錄下放包 §三 之數字充作實測
（下放包 §三 之數字為分析層於 Project 內所測，非本執行層之量測，
兩者不可互冒 —— R-G8 量測條件揭露之要求）。

| # | 項 | 預期 | 掃描條件 | **本包實測** | 判定 |
|---|---|---|---|---|---|
| E1 | `Basic Report` 資料列 | 1280 | 表頭列 1，任一欄非空 | 未實測 | 不可判（無 #2） |
| E2 | Functional | 507 | `SYS2 分類 Category` 全等 | 未實測 | 不可判（無 #2） |
| E3 | `Out of scope` ＋ `Out of Scope` | 55 ＋ 44 | 全等，分開計 | 未實測 | 不可判（無 #2） |
| E4 | DocID `VF665_V43_R3`／`VF655_V43_R3`／空 | 951／247／82 | 全等 | 未實測 | 不可判（無 #2） |
| E5 | Functional 中 DocID `VF655_V43_R3` | 171 | 同列 | 未實測 | 不可判（無 #2） |
| E6 | EE ATL-Mi | 1280 | 全等 | 未實測 | 不可判（無 #2） |
| E7 | 037 兩檔內 `V43` 字串命中 | 0 | 全欄串接 substring | 未實測 | 不可判（**該兩檔全庫查無**，見 §三） |
| E8 | V43↔V42 Functional 描述逐字相同 | 30／398 去重 | `re.sub(r'\s+',' ').strip().lower()` | 未實測 | 不可判（無 #2，且需 V42 側 SYSRA） |
| E9 | `Verification Method` 相異值 | 4（`verified by in-vehicle testing` 47、`internal signal stimulation test…` 28） | 正規化後 | 未實測 | 不可判（無 #2） |

**不符者：0。相符者：0。不可判者：9。** 不調和、不推估。

E2／E4 為下放包 §八之升級條件（不符即停）—— 本包**既未相符亦未不符**，
其升級條件尚未進入可判狀態，待原檔到齊後首測。

---

## 五、W-4／W-5 之產出

| 產出 | 狀態 |
|---|---|
| `data/sysra_v43_functional.tsv` | **未產出**（無 #2）。`data/` 為空目錄 |
| `data/signal_chain_v43.tsv` | **未產出**（無 #1）。`data/` 為空目錄 |

連帶未產出者，逐項列明以免日後誤認為已辦：

- W-4 之 `VF655` 247 列與 DocID 空 82 列之**分別標記**（DR-VT2 所令「不入分母」）—— 未辦。
- W-4 之 `Out of scope`／`Out of Scope` 二拼法正規化計數（合計 99）與其 anomaly —— 未辦。
  （上游拼法不一之 anomaly 待實測後始得登記；**本包不憑下放包轉述先登**。）
- W-5 段 1 之**兩欄組分開計數**（LID `CAN Mapping` 之 `Atlantis High` 欄組
  ／`637MCA Specific Signals` 分頁）—— 未辦，且**不自行選定**（R-P368(a) 段 1；
  R-VT2 註記所載「LID 欄組適用性與 `vsm_v42` 同題，recon 實測後另裁」仍未解）。
- W-5 之 **V42 ↔ V43 訊號名集合差集（新增／刪除）** —— 未辦。無 #1 即無 V43 側集合；
  V42 側亦無素材（`vsm_v42` 之 #1 同樣未投遞）。此差集為 DR-VT1「差異列」請求之依據，
  其缺席直接削弱 DR-VT1 之舉證力，建議 Pei 送 DR-VT1 時一併說明。
- R-P368 三段鏈之 `forms/` 三檔（LID v1_78、`PDT27_E2A_R1_BHCAN2.dbc`、
  `R1_FDCAN8.dbc`）與 PROXI（`PROXI_HDCC27_R3_20250424.xlsx`）**本包未觸**，
  因段 1 之入口（規格原名）尚無來源。段 3 B-1 型衝突（R-P368(e)，下放包 §八第 4 條）
  未進入可判狀態。

---

## 六、anomaly／DR 成對清單

### ANOMALIES（本包新登，`features/vsm_v43/ANOMALIES.md`）

| id | 一句話 | 狀態 | 配對 DR |
|---|---|---|---|
| A-VT1 | 投遞區為空，#1–#3 原檔全未投遞；W-2～W-5 不可執行 | PENDING | — （投遞屬 Pei 動作，非上游資料請求；不另開 DR） |
| A-VT2 | `tc_id_prefix` 鍵名無腳本讀取，repo 慣例為 `tc_id_format` | PENDING | — （內部形制爭點，Tier 2 裁，不送上游） |
| A-VT3 | `recon.py` 不支援 `a03_report: null`（亦不支援 `workbook: null`） | PENDING | — （工具問題，非資料問題） |
| A-VT4 | scaffold 之 ANOMALIES 模板序列標記寫成 `[A-VSnn]` | RESOLVED（執行層改為 `[A-VTnn]`） | — |

> 三條 PENDING 皆無配對 DR，且皆非「向上游索資料」型：A-VT1 之解在 Pei 投遞、
> A-VT2／A-VT3 之解在本專案內部裁決。故本包**不新增 DR**（禁區 §零-6：不自行送 DR；
> 此處連登記都無新增之必要）。

### DATA_REQUESTS（沿用，未動）

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VT1 | VF665 V43 之 037（SWE1 分析報告）缺件 | **yes** | 已登記，建議送出，**未送出** |
| DR-VT2 | SYSRA DocID `VF655_V43_R3` 疑誤植；SYSRA R3 vs 規格 R4 | no | 已登記，**未送出** |

送出權屬 Pei（Tier 3）。本包未送、未改 `DATA_REQUESTS.md`。

---

## 七、R-VT 條文 sha8（R-G13）

`python3 scripts/rulings_hash.py --out <scratchpad>/rulings.sha.tsv`（**未寫入台帳**，理由見 §八）

| 條號 | 一句話 | `sha8`（錨點全體） | `body_sha8`（fenced 本體） | 來源：列 | 本體列數 |
|---|---|---|---|---|---|
| R-VT1 | 獨立 slug；工作簿自 BLANK 起建 | `9d60e34c` | `93666dae` | `features/vsm_v43/RULINGS.md`:12 | 11 |
| R-VT2 | 訊號書寫依 canon §8.7.5 v3 ＋ PM 現行條文；不承襲 R-VS52 | `efec2621` | `a6acf352` | 同上:26 | 23 |
| R-VT3 | Test Group／TC ID／交付檔名 | `f7f9c460` | `d3823bca` | 同上:52 | 9 |
| R-VT4 | 037 = 0：本線止於 P0–P3，TC 生成待 037 | `d50ba0a0` | `9844b823` | 同上:64 | 9 |
| R-VT5 | 素材落點；spec_mode D 需 OOXML 原檔 | `1409b527` | `e8e8724b` | 同上:76 | 7 |

五條 `body_kind` 皆為 `fenced`（合 R-G29）。
**取號無碰撞**（實測）：全庫 `R-VT` 僅命中本檔五條，另一命中為
`features/vsm_v42/RULINGS.md:4` 之交互指涉句（提及，非定義）。
`rulings_hash.py` 之重複 id 報告中無任何 `R-VT`。

---

## 八、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 502
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
```

**四支紅之歸因（逐支查證，非推測）：**

| 閘 | 與 vsm_v43 之關係 | 實測 |
|---|---|---|
| `canon_refs` | **無關（實測）** | `--waiver --gate` 之 unresolved 369 ＋ ambiguous 133 = 502。**移除歸因法實測**：將本上繳檔移出樹外重跑，仍為 502 → 本包產出之貢獻 **0**。輸出中 `vsm_v43`／`R-VT` 命中 0 |
| `rulings_hash` | **相關（唯一一支）** | 重生本與台帳之差為**且僅為** 10 列新增：`R-VL1–5`（`features/vsm_v42/RULINGS.md`）與 `R-VT1–5`（本線）。台帳現有 664 列，重生 674 列，**其餘 664 列逐位元相同** |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`（`I-cross`、`W`）、`driver_distraction`／`ics_management` 之 selfcheck 腳本、`lint_docs036` 之 `body_kind`。無 vsm_v43 之列 |
| `lint_paths` | **無關** | 四筆紅全在 `features/driver_distraction/workbook/*.xlsx`（2）、`features/ics_management/delivered/…`（1）、`features/sw_update/delivered/…`（1） |

**未動台帳之理由（提請裁決）**：`docs/fw036/RULINGS.sha.tsv` 重生可一次轉綠，
指令為 `python3 scripts/rulings_hash.py`，本執行層**已驗證其輸出唯一差異為上述 10 列**。
未逕行寫入，因：
1. 該檔於本包執行時已處 `M`（工作區有他線之未提交修改，355 insert／339 delete），
   覆寫將與該線之作業交疊；
2. 重生必然夾帶 `R-VL1–5`（`vsm_v42` 之條文列）。該檔檔頭雖明載「夾帶之他線列為
   結構性質，非該次提交之瑕疵（下放包 56 §二 #1）」，惟本包禁區 §零-2
   令「不得寫入 `features/vsm_v42/` 之任何檔」，其精神是否延及**代 `vsm_v42` 落其 sha 台帳列**，
   本執行層讀不出唯一解 —— 依 FO §0「AUTO 管的是怎麼做，不是做什麼」，此為 Tier 2。

其餘三支為存量紅，本包不觸（非本線之責，且 `lint_paths` 之四筆分屬三個他 feature）。

**同一輪內之 501 → 502 漂移**：本包首跑 `gate_all.py` 得 501，數分鐘後複跑得 502，
其間本執行層僅新增本上繳檔一件，而移除歸因法已證該檔貢獻為 0。
研判為工作區之他線同時作業所致（`git status` 顯示 `docs/fw036/`、`docs/runtime/`、
`scripts/`、`features/driver_distraction/` 等多處同時處於未提交狀態）。
**本包不追該 1 之來源**，僅記明：`canon_refs` 之計數於本輪不可重現，
其紅與本線無關之結論不受影響（移除歸因法為直接證據，計數漂移不動搖之）。

依 FO §8.2／26 包 §C 裁定 2：**本包附本節之升級說明上繳**。

---

## 九、獨立判斷（執行層）

1. **停在 W-1 是正解，且應停得比字面更早一格。** 下放包 §四假定「#1、#2 原檔放此即可」，
   §三 對 #3 記「與 `vsm_v42` 共引一份（R-VT5）」—— 實測 `vsm_v42` 側**亦未落檔**，
   `sources/raw/` 無此 doc_id。故 #3 不是「已有、共引即可」，是**三件皆缺**。
   若照 §三 字面理解為「#3 已在」，W-2 會在找不到檔時才發現，徒增一輪。建議下放包
   §三 之「共引」欄改記共引**目標路徑**與其現況（已落／未落），而非僅記關係。

2. **下放包 §三 之數字不可充作 recon 實測，本包一項未轉錄。** §三 已載
   「`Basic Report` 資料 1280 列、Functional 507、DocID 951／247／82」等，
   與 §六 E1／E2／E4 之預期值同源。若執行層將其抄入 §四之「實測」欄，
   E1–E9 會**全綠而零證據** —— 預期與實測同源即失去對照之全部作用。
   本包一律填「未實測」。此為 R-G8（量測條件揭露）之直接推論，一併提請確認。

3. **A-VT3 是本線之結構性障礙，不是一次性缺陷。** R-VT4 令本線長期停於 P0–P3，
   即長期處於 `a03_report = null`。每次 P1 都要人工 RECON，成本落在每一輪。
   `recon.py` 加 None guard 約十行（`survey_workbook`／`survey_a03` 兩處早退，
   回傳空 result dict），且**對既有十餘個 feature 零行為改變**（其路徑皆非 null）。
   建議 Pei 核可改碼；本包不改，等裁。

4. **A-VT2 之形制爭點宜在 P3 一次解掉，勿留到 P4。** `tc_id_prefix` 目前無人讀，
   若延到 P4 才發現 lint／write-back 取不到值，會在生成中途才炸。
   建議 P3 profile 落檔時同步定 `write_back.tc_id_format: "NR1L-VSM43-{NNN}"`，
   `tc_id_prefix` 保留為下放包原文之見證（或刪，由 Pei 定）。

5. **`workbook.columns` 之模板值是下一輪最可能的地雷。** power 之 A-PW37 實測：
   同一 scaffold 模板值自 `priority` 起全部錯位，且該 workbook 有**兩個**
   `Estimated Test Time` 欄。本線 BLANK 起建之母本為 R-G1 之 `_ext.xlsx`，
   其欄位須自 r9 表頭實測，**不得沿用本 `feature.yaml` 現值**。已就地註明。

6. **R-VT2 之未決項未因本包而縮小。** 「本線 SYSRA EE Architecture 全為 ATL-Mi
   （1280/1280），R-P368(a) 段 1 之 LID 欄組適用性與 `vsm_v42` 同題」—— 該註記所依之
   1280/1280 本身尚未經本執行層實測（E6 不可判）。另註：R-P368(a) 段 1 之入口
   已由 **R-P375** 擴為 `forms/` 全部參考檔（`features/power/RULINGS.md`:12640），
   R-VT2(b) 引 R-P368 時是否連帶承接 R-P375 之擴張，下放包未言。提請 P3 一併裁。

---

## 十、禁區遵守聲明

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 未跑任何 `git` 寫入指令（僅 `git diff --stat` 唯讀，用於 §八歸因） |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫；`vsm_v42` 僅讀 `RULINGS.md`／`feature.yaml` 作對照 |
| 3. 不寫 `docs/runtime/profiles/` | 未寫 |
| 4. 不改寫 `sources/raw/` 原檔 | 未寫（該目錄本包全程唯讀） |
| 5. 不以 SYSRA 或規格代 037 建 leaf 母體或生成 TC | 未建、未生成；`data/`、`generated/`、`batches/` 皆為空目錄 |
| 6. 不自行送 DR | 未送；`DATA_REQUESTS.md` 本包未動 |

本包寫入之檔，全數在 `features/vsm_v43/` 之下：
`feature.yaml`（改）、`ANOMALIES.md`（改）、`docs/upstream/00_intake_recon.md`（新）；
另 scaffold 產出 `.gitignore`／`DECISIONS.md`／`PLAYBOOK.md`／`RUNBOOK.md`（新，未再編輯）。
`docs/fw036/`、`docs/runtime/`、`scripts/` 之任何檔本包**未寫入**。

---

## 十一、下一步（阻塞順序）

1. **Pei 投遞 #1–#3 原檔**至 `_intake/Vehicle_Setup_VF665/`（解 A-VT1，解開 W-2～W-5）
2. Pei 裁 A-VT3（`recon.py` 改碼 or 一律人工 RECON）
3. Pei 決定 DR-VT1（建議送出）／DR-VT2 之送出
4. 原檔到齊後執行層跑 W-2～W-6，首測 E1–E9，上繳 01
5. Tier 2：`docs/fw036/RULINGS.sha.tsv` 之重生歸屬（§八）與 A-VT2 之鍵名形制
