# 上繳包 00 — Vehicle Setup Management R1 Low（VF665 V42）：W-1 執行與缺件停下

日期：2026-09-01　執行層：Claude Code　對應下放包：`docs/handoff/00_intake_and_rulings.md`

## 結果分類（FO §8.4）

| 分類 | 內容 |
|---|---|
| 改對了 | W-1 全部：`new_feature.py --adopt-existing` 執行、`feature.yaml` 依 R-VL3／R-G27 填寫 |
| 核實無誤 | R-VL1–R-VL5 五條 sha8 自 repo 原文實算；E14／E15 實測相符（來源為 `forms/`，不受缺件影響） |
| 正確地不動 | W-2～W-6 全數未執行 —— 依下放包 00 §八末條與 FO §0 trigger 1，缺件即停，**不得以抽取本代原檔**；`sources/raw/` 未建、`docs/fw036/RULINGS.sha.tsv` 未重生（理由見 §11） |

**總判：停於 W-1，缺件五件（A-VL1）。**

---

## 1. W-1 之 scaffold 輸出全文

```
$ python3 scripts/new_feature.py vsm_v42 --adopt-existing
scaffolded /Users/peihe/Work_Projects/TC_Generator/features/vsm_v42
  kept existing (not overwritten): DATA_REQUESTS.md, RULINGS.md
next steps:
  1. drop source files into /Users/peihe/Work_Projects/TC_Generator/features/vsm_v42/inputs
  2. fill /Users/peihe/Work_Projects/TC_Generator/features/vsm_v42/feature.yaml (spec_mode, paths)
  3. run Phase 1 recon (Claude Code, Tier 1)
  4. review DECISIONS.md [PROPOSED] items and sign (Tier 2)
exit 0
```

`kept existing` 含 `RULINGS.md`、`DATA_REQUESTS.md` 二者，**與下放包 §五 W-1 之要求相符**。
未出現 whitespace／既存衝突之拒絕（§八第 5 條未觸發）。

落檔後之目錄實測（`find features/vsm_v42`）：

```
features/vsm_v42/.gitignore          新建（scaffold）
features/vsm_v42/ANOMALIES.md        新建（scaffold）→ 本包改寫，見 §8
features/vsm_v42/DATA_REQUESTS.md    kept existing
features/vsm_v42/DECISIONS.md        新建（scaffold 模板，未簽、未預填）
features/vsm_v42/PLAYBOOK.md         新建（scaffold）
features/vsm_v42/RULINGS.md          kept existing
features/vsm_v42/RUNBOOK.md          新建（scaffold）
features/vsm_v42/feature.yaml        新建（scaffold 模板）→ 本包改寫
features/vsm_v42/{inputs,data,batches,generated,scripts,docs}/   目錄，皆空
features/vsm_v42/docs/{handoff,upstream}/
```

### `feature.yaml` 之填寫（W-1 之第二段）

| 鍵 | 值 | 依據 |
|---|---|---|
| `feature` | `Vehicle Setup Management R1 Low` | R-VL3 |
| `test_group` | `Vehicle Setup Management R1 Low`（同值） | R-VL3 |
| `tc_id_prefix` | `NR1L-VSM42-` | R-VL3；**模板無此鍵，依下放包 W-1 之授權新增** |
| `spec_mode` | `D` | R-VL5 |
| `sources.*` | 五個 doc_id | R-G27 |
| `paths.*` | `../../sources/raw/<doc_id>/…` 相對 glob | R-G27（feature 端不存原檔副本） |
| `paths.a03_report` | 指 `vf665_037_parksense`（recon 代表檔） | 下放包 W-3 |
| `paths.a03_report_parksense` / `_sdw` | 兩份 037 各掛一檔 | 下放包 W-3（`resolve_path` 之 glob 恰 1 檔限制） |
| `write_back.fill_test_group_set` | `true` | R-VL1 BLANK 起建 ＋ FO §2 |
| `lint.profile` | `vsm_v42` | R-VL2(c) |

**未實測之宣告（據實揭露）**：`paths.*` 之五個 `sources/raw/` glob **於落檔當下不解析為任何檔**
（該目錄尚未建立，因原檔未投遞）。此為 W-2 之工作，非本包可為。
`paths.lid` / `paths.dbc_*` / `paths.proxi` 四鍵指 `forms/`，**已實測存在**。

**未預期之發現（1）—— `tc_id_prefix` 鍵名與全庫慣例不一致**
掃描條件：`grep -rn "tc_id_prefix\|tc_id_format" scripts/ features/*/feature.yaml docs/fw036/templates/`。
實測：`tc_id_prefix` 全庫命中 **0**；`tc_id_format` 命中 **17 個 feature.yaml**
（popup／power／sxm／ics_management／bed_lowering／… 等）。且
`scripts/recon.py:1103–1104` 讀的是 `cfg["write_back"]["tc_id_format"]`，
**不讀 `tc_id_prefix`** —— W-3 之 recon 將不會印出 tc_id scheme 一行。
本包依下放包指示只落 `tc_id_prefix`，**不自行增設 `tc_id_format`**（FO §8.5 之一：不代擬條文）。
請分析層裁：(a) 維持 `tc_id_prefix` 並改 `recon.py`；或 (b) 併落
`write_back.tc_id_format: "NR1L-VSM42-{n:03d}"`。

---

## 2. sources/ 三處落檔清單 ＋ 原檔 sha256

**未執行（W-2 阻塞）。** `sources/raw/` 下未建立 `vf665_*` 任一目錄，
`sources/extracted/` 未產任何抽取形，`sources/MANIFEST.tsv` **未加任何列**（維持原狀）。

原因：`_intake/Vehicle_Setup_VF665/` 實測 0 files（見 §8 A-VL1）。
原檔 sha256 五筆**皆無法提出** —— 下放包 §三所載之 sha 為 Claude Project 附件抽取本之 sha，
依 R-VL5 與 G-L 不得充作原檔 sha。

### #5 SYSAD 與 `vehicle_setting/inputs/` 同名檔之 sha 比對

| 項 | 值 |
|---|---|
| 對照方（既有檔） | `features/vehicle_setting/inputs/SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` |
| 其 sha256（本包實算，`shasum -a 256`） | `469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200` |
| 大小 / mtime | 16,694,938 bytes / 2026-08-16 06:32 |
| 被比對方（#5 原檔） | **未投遞** |
| **比對結果** | **無法比對** —— 只有一方在場 |

該檔**未被取用為本線之代品**（R-G27：新 feature 一律走 `sources/`）。
`MANIFEST.tsv` 之 `features` 欄應記 `vsm_v42,vsm_v43` 與否，待兩檔 sha 實比後定。

---

## 3. R-G28 嵌入物件檢查結果

**未執行（阻塞）。** 檢查對象依下放包 §二為 VF665 V42 之 docx（#1）之
`word/embeddings/`、`word/media/`；該 docx 未投遞，zipfile 無可開之對象。

**未以他物代查之聲明**：未以 Claude Project 之文字抽取本代之（抽取本無 zip 容器，
其 `word/media/` 本不存在，查了亦為假陰）。R-G28 之「查無亦須記明」須以原檔為之，
本包**不記「已查、無」**，記為**未查（缺件）**。

---

## 4. `RECON.md` ＋ 預填 `DECISIONS.md`（未簽）

| 產出 | 狀態 |
|---|---|
| `RECON.md` | **未產出** —— `scripts/recon.py` 依 `feature.yaml` 解析 `paths.workbook`／`paths.a03_report`／`paths.spec_pdf`，四鍵之目標檔皆不存在，執行必於 `resolve_path` 失敗。**未嘗試以部分素材強跑**。 |
| `DECISIONS.md` | 存在，但為 `new_feature.py` 之**空白模板**（`[AUTO]`／`[PROPOSED]` 佔位未填），**非 recon 預填本**。未簽。**本包未手填任何 `[AUTO]` 欄** —— `[AUTO]` 之定義為機器判定（FO §0 Tier 0），手填即偽造。 |

---

## 5. §六 E1–E16 逐項對照（相符者亦列；不符不調和）

| # | 項 | 預期 | 實測 | 判 | 掃描條件（本包實際所用） |
|---|---|---|---|---|---|
| E1 | #3 有 SWE id 列數 | 82 | **未能實測** | 缺件 | 需 #3 原檔 |
| E2 | #4 有 SWE id 列數 | 70 | **未能實測** | 缺件 | 需 #4 原檔 |
| E3 | Functional leaf 合計 | 128 | **未能實測** | 缺件 | 需 #3＋#4 |
| E4 | Heading 合計 | 23 | **未能實測** | 缺件 | 需 #3＋#4 |
| E5 | `Categorization` 空列 | 1 | **未能實測** | 缺件 | 需 #3＋#4 |
| E6 | Functional Source ID 去重 | 128 | **未能實測** | 缺件 | 需 #3＋#4 |
| E7 | SYSRA `Analysis Report` 資料列 | 1040 | **未能實測** | 缺件 | 需 #2 |
| E8 | SYSRA Functional | 318 | **未能實測** | 缺件 | 需 #2 |
| E9 | SYSRA Functional 之 EE 空 | 112 | **未能實測** | 缺件 | 需 #2 |
| E10 | SYSRA DocID `VF665_V42_P637MCA` | 791 | **未能實測** | 缺件 | 需 #2 |
| E11 | 037 描述內 CAN 訊號名 | 71 ＋ 70 | **未能實測** | 缺件 | 需 #3＋#4 |
| E12 | 037 描述內 `PROXI` | 48 ＋ 23 | **未能實測** | 缺件 | 需 #3＋#4 |
| E13 | 037 描述內 `$token$` | 14 ＋ 16 | **未能實測** | 缺件 | 需 #3＋#4 |
| **E14** | LID v1_78 `CAN Mapping` 含 `IPC_VEHICLE_SETUP`／`TELEMATIC_VEHICLE_SETUP`／`RainSensor` 之列 | **65** | **65** | **相符** | `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`，分頁 `CAN Mapping`，openpyxl `read_only=True, data_only=True`，**逐列取全部儲存格**、None 濾除、以空白接為單一字串後 `in` 判 substring；**區分大小寫**、**不設詞界**、**不去重**；掃描列數 2,627（含表頭與空列） |
| **E15** | LID `637MCA Specific Signals` 非空列 | **22** | **22** | **相符** | 同檔，分頁 `637MCA Specific Signals`；「非空」＝該列至少一格 `is not None` 且 `str(c).strip() != ""` |
| E16 | 037 之 E3 ↔ E8 命中 | 128 | **未能實測** | 缺件 | 需 #2＋#3＋#4 |

**E14／E15 得以實測之理由**：二者之來源為 `forms/Logical Identifiers and CAN Mapping v1_78.xlsx`，
屬 `forms/` 共用參考檔，**不在 §三 之五件缺件內**，故其量測不構成「以他物代原檔」。
十四項未能實測者**不以任何近似來源估算、不自行調和**（FO §8.2）。

實測所用之分頁全集（LID v1_78，14 分頁，供分析層裁 W-5 段 1 欄組時參考）：
`Rev History`／`Notes`／`CAN Mapping`／`Proxi & Configuration`／`Atlantis Low Specific Signals`／
`M240 Specific Signals`／`BSEGMENT Specific Signals`／`332BEV Specific Signals`／
`M182BEV Specific Signals`／`250MCA Specific Signals`／`965 Specific Signals`／
`ALFAMCA Specific Signals`／**`637MCA Specific Signals`**／`356MCA Specific Signals`。

> **未預期之發現（2）**：該檔**無名為 `Atlantis High` 之分頁** ——
> R-P368(a) 段 1 所稱之 `Atlantis High` 係 `CAN Mapping` 分頁內之**欄組**，
> 而 `637MCA Specific Signals` 係**獨立分頁**。二者不同構
> （欄組 vs 分頁），下放包 §五 W-5 之「兩者命中分開計數」因此為
> 跨結構之計數。本包**不自選、不合併**，據實記於此交分析層（R-VL2 末段待查項）。
> 另有 `Atlantis Low Specific Signals` 分頁，與 `Atlantis High` 欄組非同一物，一併記明。

---

## 6. `data/leaves.tsv` 與跨源對帳

**未執行（W-4 阻塞）。** `features/vsm_v42/data/` 實測為空目錄。
列數、分類計數、`Source Requirement ID` ↔ SYSRA `Sys-RA-Feature-ID` 之命中／未命中**皆無數**。
`DATA_REQUESTS.md` 之 DR-VL1「190 列」**未回填**，維持原文之「約 190」。

---

## 7. `data/signal_chain_v42.tsv` 之結果分布

**未執行（W-5 阻塞）。** 該檔未產生。五類（解得／未解得(止於段1)／未解得(止於段2)／查無／B-1 衝突）
各為 **無數**，**兩欄組亦無分開之計數**。

段 1 之來源（LID v1_78）雖在場，但段 1 之**輸入**——#1 docx 之
Functional Diagram／External Interfaces 節所載之訊號原名——不在場，
故三段鏈無起點。**未以 037 描述欄之訊號名代替 docx 之訊號名**（E11 之對象亦缺件）。

`forms/LOOKUP_MISSES.md` **未新增任何列**（R-G14 之登錄前提為段 3 實查，本包未查）。

---

## 8. 新開 anomaly 與 DR 成對清單；未結 DR

### 新開 anomaly

| 編號 | 標題 | 阻塞 | 成對 DR |
|---|---|---|---|
| **A-VL1** | `_intake/Vehicle_Setup_VF665/` 為空，五件原檔全缺 | **是** | **無（理由如下）** |

全文落於 `features/vsm_v42/ANOMALIES.md`（本包新建其內容；scaffold 之空殼被改寫）。

**A-VL1 未成對開 DR 之理由**（FO §8.2「新開 anomaly 與 DR 成對，缺一不可」之例外聲明）：
本項非上游資料疑義，而係下放包 00 §四所載之 **Pei 投遞動作尚未發生**，
屬本專案內部流程步驟，無可向上游詢問之項；且 DR 送出權屬 Pei（禁區第 6 條），
執行層代擬 DR 亦違 FO §8.5 之一。故只登 anomaly。**此為刻意之不成對，非漏做**，
請分析層於覆核時裁可或改令補 DR。

W-6 所列之三項候選 anomaly（037 `Categorization` 空 1 列；SYSRA Functional 之 EE 空 112 列；
SYSRA DocID 空 249 列）**未登記** —— 其登記以實測為前提（E5／E9／E10 皆未能實測），
先登後測即為造值（IN §8.4.1）。A-VL2 起之號**保留給該三項**。

### 未結 DR 清單（IN §8.4.3）

| DR | 項目 | 阻塞 | 狀態 | 送出日 |
|---|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中約 190 列無 037 覆蓋（覆蓋揭露） | no | 已登記，未送出；**本包未回填實數**（W-4 阻塞） | — |

本包**未送出任何 DR**（禁區第 6 條）。

---

## 9. 五條 R-VL 之 sha8

工具：`python3 scripts/rulings_hash.py --target features/vsm_v42/RULINGS.md --out <scratchpad>/vsm_v42.sha.tsv`
（**未寫入 `docs/fw036/RULINGS.sha.tsv`**，理由見 §11）。
量測條件依該工具 docstring：自錨點標題之次行起至下一同級／更高級標題之前一行止，
首尾空行去除、行尾空白去除、`\n` 接合、UTF-8、sha256；標題文字不入雜湊。
來源檔 `features/vsm_v42/RULINGS.md` 全檔 sha256 前 16 碼 `21c04924ac59baf2`。

| 條號 | 一句話 | **sha8** | body_sha8 | body_kind | 行 | 本體行數 |
|---|---|---|---|---|---|---|
| R-VL1 | 獨立 slug `vsm_v42`；BLANK 起建 | **`2a3dd0b6`** | `5897969a` | fenced | 12 | 16 |
| R-VL2 | 訊號依 IN §8.7.5 v3 ＋ R-P353／R-P355／R-P368；不承襲 R-VS52 | **`d6a189ed`** | `01c67a04` | fenced | 31 | 32 |
| R-VL3 | Test Group／TC ID／交付檔名 | **`ec287e40`** | `e306aa75` | fenced | 66 | 14 |
| R-VL4 | 母體 = 037 Functional leaf（128）；SYSRA 其餘不入範圍 | **`49be4fb8`** | `08cea35e` | fenced | 83 | 10 |
| R-VL5 | 素材落點；spec_mode D 需 OOXML 原檔 | **`482a6990`** | `1de01344`  | fenced | 96 | 8 |

五條**皆為 `fenced` 本體**（R-G29 body_kind 閘之要求），無 `section` 型。

### 本包所讀之引用條文（自 repo 原文，非憑記憶）

| 條號 | 來源檔:行 | 所讀要點 |
|---|---|---|
| IN §8.7.5 v3 (a)–(g) | `docs/runtime/ASPICE_SWE6_AI_Instruction.md:517–575` | `$MESSAGE.Signal$ = <raw> (<label>)`；PROXI 不加 `$`；(d) 內部訊號查無者保留原名；(g) R-13 保留規格原名 |
| R-P353 | `features/power/RULINGS.md:12143–12166` | 可觀察目標白名單四類；抽象名詞不得作 `<X>` |
| R-P355 | `features/power/RULINGS.md:12198–12215` | 內部訊號不得直接 Set；(b) 有 DBC 對照者改 `$MESSAGE.Signal$`；(c) 否則 `PENDING: DR-{n}` |
| R-P368 | `features/power/RULINGS.md:12443–12469` | 三段鏈；(b) 不得語意跳接、須載明欄／列；(e) R4 BHCAN 降旁證，衝突記 B-1 |
| R-P375（R-P368 之 62 包加註） | `features/power/RULINGS.md:12640–12672` | **段 1 入口自 LID `CAN Mapping` 擴為 `forms/` 全部參考檔**（LID 全分頁、HMI Settings List R1 SR25、PROXI `Format`、SR26 Default Settings、SR24 Market Configuration Table） |
| R-G27／R-G28 | `docs/fw036/FEATURE_ONBOARDING.md` §9.2 | `sources/` 集中制；嵌入物件逐 feature 檢查 |

> **未預期之發現（3）—— R-VL2(b) 之引用可能已窄**：R-VL2(b) 逐字引 R-P368 之
> 「段 1 → LID `CAN Mapping` `Atlantis High` 欄組」，而 PM 側已於 **R-P375(a)**
> 將段 1 入口擴為 `forms/` 全部參考檔（LID 全分頁 ＋ 另四檔），R-P368 依 R-P36
> 原文不改僅加註。Pei 原話為「訊號寫法要遵照 power management **最新的部分**」。
> 若「最新」含 R-P375，則 W-5 之段 1 應查七檔而非一分頁一欄組。
> 本包**不自行擴大範圍**（FO §8.5 之三：不越權補件），據實回報，交分析層裁
> 是否於 R-VL2 加註引入 R-P375。此亦影響 §5 之未預期發現（2）之欄組取捨。

---

## 10. 獨立判斷：本包是否仍有該驗而未驗者

1. **無**（在缺件前提下）。W-2～W-6 之每一項皆以 §三 五件原檔為輸入，
   缺件即無可驗；E14／E15 為僅有之兩項不依賴缺件者，已驗且相符。
2. **明確未做而應記者三項**：
   - `docs/INDEX.md` 依 FO §8.7 於每次上繳更新 —— 本包**已建**（見 §12）。
   - `docs/fw036/RULINGS.sha.tsv` 未回填 R-VL 五列 —— 刻意，見 §11。
   - `RULINGS.md` 本文之「sha8：待回報」欄未回填 —— 該表在**下放包**
     （`docs/handoff/00_intake_and_rulings.md`）內，屬分析層之檔；
     執行層改寫下放包即竄改上游輸入，故不改，sha8 以本上繳包 §9 為交付面。
3. **一項疑慮，非本包可決**：`feature.yaml` 之 `paths.workbook` 指
   `sandbox/base/…_ext.xlsx`，而 `features/vsm_v42/sandbox/` **尚未建立**
   （`new_feature.py` 之 `DIRS` 不含 `sandbox`，實測 `DIRS = ["inputs", "data",
   "batches", "generated", "scripts", "docs"]`）。R-G25 要求 xlsx 只准在 sandbox 改。
   本包**未建 sandbox/、未複製母本** —— 建簿屬 W-2 之後，且 R-G1 母本之複製
   未在下放包 W-1 之點名範圍內。請分析層於下一包明示其時點。

---

## 11. `python3 scripts/gate_all.py` 輸出

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 501
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
```

### 升級說明（FO §8.2／26 包 §C 裁定 2 —— exit 非 0 須附）

逐支歸因。**四支之中，三支與本線無關，一支與本線有關但刻意不修。**

**(甲) `canon_refs` FAIL = 501 —— 與 vsm_v42 無關，先在。**
掃描條件：`python3 scripts/canon_refs.py --waiver --report --top 400`，
於逐筆輸出中 `grep -ci "vsm_v42\|vsm_v43"` 命中 **0**。
違規之 feature 分布（逐筆輸出中 `features/<x>/` 之出現次數）：
display 25、vehicle_category 13、power_moding 9、audio_mgmt 7、ics_management 3、
driver_distraction 2、vehicle_setting 1、sw_update 1、power 1、popup 1。
本線未新增任何 unresolved／ambiguous 引用。

**(乙) `gates_tsv` FAIL —— 與 vsm_v42 無關，先在。**
掃描條件：`gates_tsv.py --out <scratchpad>/gates_now.tsv` 後與 `docs/runtime/GATES.tsv` 逐行 diff。
差異 6 列，全為他線：新增 `I-cross`（R-SU34 v3，sw_update）、`W`（下放包 47）、
`features/driver_distraction/scripts/selfcheck_pilot_group3.py`、
`…/selfcheck_tcs.py`、`features/ics_management/scripts/selfcheck_b01.py`；
移除 `body_kind`（R-G29）。**無一列涉 vsm_v42。**
另註：`scripts/gates_tsv.py`（+23/-1）與 `scripts/gate_all.py`（+2）於本包開始前
即為 working tree 已改動狀態（`git diff --stat` 實測），本包未動之。

**(丙) `lint_paths` FAIL = 4 —— 與 vsm_v42 無關，先在。** 四筆逐筆：
- 紅 `features/driver_distraction/workbook/driver_distraction_00.xlsx`（落點非 delivered/inputs/sandbox）
- 紅 `features/driver_distraction/workbook/driver_distraction_00_bak.xlsx`（同上）
- 紅 `features/ics_management/delivered/…_SWQT_ICSManagement_20260830.xlsx`（sha 與對照表不符）
- 紅 `features/sw_update/delivered/…_SWQT_SWUpdate_20260830.xlsx`（delivered/ 內而對照表未列）
`features/vsm_v42/` 下**無任何 xlsx**，不可能為其來源。

**(丁) `rulings_hash` FAIL —— 與本線有關，刻意不修。**
掃描條件：`rulings_hash.py --out <scratchpad>/full_now.sha.tsv` 後與
`docs/fw036/RULINGS.sha.tsv` 逐行 diff。差異**恰 10 列，全為新增，無修改、無刪除**：

| 新增列 | 來源 |
|---|---|
| R-VL1–R-VL5 | `features/vsm_v42/RULINGS.md`（本線；分析層先落，非本包所寫） |
| R-VT1–R-VT5 | `features/vsm_v43/RULINGS.md`（**姊妹線**） |

**不重生該 tsv 之理由**：`rulings_hash.py` 為全庫單一輸出檔，重生必同時寫入
R-VT 五列 —— 即以本線之作業，替**姊妹線** `vsm_v43` 完成其條文入台帳。
下放包 §零禁區第 2 條為「不得寫入 `features/vsm_v43/` 之任何檔」；
本動作雖未寫入該目錄，其效果為代該線登錄，屬禁區之精神範圍，
且該 tsv 為共用檔（其標頭自載「其 commit 不可能只含單一變更之列」）。
**本包選擇回報而不調和**（FO §8.2）。R-VL 五條之 sha8 已於 §9 全數提出，
引用制（R-G13）之驗證面不因未回填而缺。
請 Pei／分析層裁：由誰、於哪一包重生 `docs/fw036/RULINGS.sha.tsv`。
（另註：該檔於本包開始前即為 working tree 已改動狀態。）

**結論**：本包之 gate 非 0 全數可歸因，其中三支先在於本線之外，
一支為兩條新線同時落檔所致之台帳待更新。**無一支肇因於本包之寫入。**

---

## 12. 本包之寫入清單（逐檔）

| 檔 | 動作 | 授權 |
|---|---|---|
| `features/vsm_v42/{.gitignore,ANOMALIES.md,DECISIONS.md,PLAYBOOK.md,RUNBOOK.md,feature.yaml}` ＋ 六目錄 | 新建 | W-1 `new_feature.py --adopt-existing` |
| `features/vsm_v42/feature.yaml` | 改寫（模板 → 本線值） | W-1 第二段 |
| `features/vsm_v42/ANOMALIES.md` | 改寫（空殼 → A-VL1） | FO §0 trigger 1「登記並停」 |
| `features/vsm_v42/docs/upstream/00_intake_recon.md` | 新建（本檔） | §七 |
| `features/vsm_v42/docs/INDEX.md` | 新建 | FO §8.7 |

**未動**：git（任何指令）、`features/vehicle_setting/`、`features/vsm_v43/`、
`docs/runtime/profiles/`、`sources/`、`_intake/`、`forms/`、
`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/GATES.tsv`、
`features/vsm_v42/docs/handoff/00_intake_and_rulings.md`（分析層之檔）、
`features/vsm_v42/{RULINGS.md,DATA_REQUESTS.md}`（`kept existing`）。

---

## 13. 待 Pei／分析層之四項

1. **投遞 §三 #1–#5 原檔**至 `_intake/Vehicle_Setup_VF665/`（A-VL1 之解除條件，阻塞 W-2～W-6）
2. `tc_id_prefix` vs `tc_id_format` 之鍵名裁定（§1 未預期發現 1）
3. R-VL2(b) 是否納入 **R-P375**（段 1 入口擴為 forms 七檔）（§9 未預期發現 3），
   併同 W-5 段 1 之「`Atlantis High` 欄組 vs `637MCA Specific Signals` 分頁」欄組取捨（§5 未預期發現 2）
4. `docs/fw036/RULINGS.sha.tsv` 之重生歸屬（§11 丁）；`sandbox/` 建立與 R-G1 母本複製之時點（§10-3）
