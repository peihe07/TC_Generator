# 上繳包 05 — vsm_v42：P4/P5 pilot（EPB Maintenance Mode，17 leaf）

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/05_pilot_epb.md`

## 結果分類（FO 之第 8.4 節）

| 分類 | categories |
|---|---|
| 改對了 | W-0 列舉查得；W-1 規格節切出＋17／17 對映；W-2 生成 17 TC；W-3 自檢；W-4 sibling 軸 |
| 核實無誤 | **E38–E45 全數過**；§9 機讀可判之 14 項全 PASS |
| 正確地不動 | **未寫工作簿、未寫 `delivered/`、未開啟 `sandbox/base/` 為 read-write**（R-VL20／本包禁區 1）；Fdbk 2–11 之 label **不造**；ignition 分支**不臆造訊號名**；`profiles/` 只讀 |

**總判：pilot 17 leaf 全數產出，無升級條件觸發。§K 四項待裁。**

---

## 1. W-0 `GenSigSendType` 列舉（R-VL18(c)）

**查得**，兩本 ATL-Mi DBC **逐字一致**：

```
BA_DEF_ SG_ "GenSigSendType" ENUM "NotUsed","OnWrite","OnWriteWithRepetition",
  "OnChange","OnChangeWithRepetition","IfActive","IfActiveWithRepetition","NoSigSendType";
BA_DEF_DEF_ "GenSigSendType" "NoSigSendType";
```

| 值 | 列舉字 | 本線 `ba_sendtype_v42.tsv` 之列數 |
|---|---|---|
| 0 | `NotUsed` | 0 |
| **1** | **`OnWrite`** | **38** |
| 2 | `OnWriteWithRepetition` | 0 |
| **3** | **`OnChange`** | **57** |
| 4 | `OnChangeWithRepetition` | 0 |
| 5 | `IfActive` | 0 |
| 6 | `IfActiveWithRepetition` | 0 |
| **7** | **`NoSigSendType`**（＝ `BA_DEF_DEF_` 之預設） | **4** |

上繳 04 第 8 節第 5 項所留之「不得憑數值猜測」自此解除。
**惟本包之 Procedure 仍只依規格行為書寫**，未依 SendType 改寫任何步驟
——`ba_sendtype_v42.tsv` 維持參考地位（R-VL18(c) 之「表僅參考」）。

---

## 2. W-1 規格節切出與對映

**切法**：起＝標題段 **1047**（`1.11.1.1.19 EPB Maintenance Mode`）；
迄＝下一同級標題段 **1118**（`1.11.1.1.20 Auto Park Brake`）之前一段。
節內段落 1047–1117，**非空 58 段**，逐字落 `data/pilot_epb_spec.md`（含段號，未改寫未省略）。

### 17 leaf → 段號（**17／17 全對映，未對映 0**）

| req_id | 段號 | 段落起句（節錄） |
|---|---|---|
| `…-044` | **1048** | `IF"EPB_Maintenance_Menu" PROXI parameter is equal to "Absent"` |
| `…-045` | **1050** | `IF" EPB_Maintenance_Menu " PROXI parameter is equal to "Present"` |
| `…-046` | **1052** | `IFthe user sets "Maintenance_Mode_Enable.Req" internal signals equal to " On"` |
| `…-047` | **1059** | `IF "IPC_VEHICLE_SETUP2.EPB_MaintenanceMode" B CAN signal change from "Off" to "On"` |
| `…-048` | **1064** | `IF TLM receives "…EPB_Maintenance_Fdbk" set to " 2 "` |
| `…-049` | **1069** | 同上，`" 3 "` |
| `…-050` | **1074** | 同上，`" 4 "` |
| `…-051` | **1079** | 同上，`" 5 "` |
| `…-052` | **1084** | 同上，`" 6 "` |
| `…-053` | **1091** | `activate and display the Popup related to " no response from EPB module "` |
| `…-054` | **1093** | `…Fdbk" set to " 8 "` |
| `…-055` | **1097** | 同上，`" 9 "` |
| `…-056` | **1101** | 同上，`" 10  "` |
| `…-057` | **1105** | 同上，`" 11  "` |
| `…-058` | **1109** | `IF "IPC_VEHICLE_SETUP2.EPB_MaintenanceMode" B CAN signal is equal to "On"` |
| `…-059` | **1111** | `IF "STATUS_CCAN3.VehicleSpeedVSOSig" B CAN signal changes from a value ≤ "V_Car_Moving"…` |
| `…-060` | **1116** | `THEN TLM shall update the EPB Maintenance Mode information on its display through "TLM_Vehicle_Setup_Menu.Info"` |

**升級條件「對映不上之 leaf > 3」未觸發（實測 0）。**

### 規格常數（自規格常數表逐字取，**不臆造**）

| 常數 | 值 | 範圍 | 容差 | 單位 | 來源 |
|---|---|---|---|---|---|
| `T_EPB_MM` | **35000** | [0;50000] | 200 | ms | `document_tables.tsv` 表 4 列 2 |
| `V_Car_Moving` | **4** | [0;7] | 0,5 | km/h | 同表 列 3 |

---

## 3. W-2 產出

`features/vsm_v42/generated/b1_epb/`：17 × `.json` ＋ 17 × `.md` ＋ `INDEX.md` = **35 檔**。
**req_id 17／TC 總數 17／PENDING 項 6。**

### 訊號書寫之實據（逐一可回溯 v3）

| 訊號 | v3 結果 | 段 3 證據 | 本包寫法 |
|---|---|---|---|
| `TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req` | 解得 | `BO_162`／`SG_`／`VAL_` 2 項 | `$…$ = 1 (On)`，label 逐字取 VAL_ |
| `IPC_VEHICLE_SETUP2.EPB_MaintenanceMode` | 解得 | `BO_1486`／`VAL_` 0=Off、1=On | `$…$ = 0 (Off)` / `= 1 (On)` |
| `IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk` | 解得 | `BO_1486`／**`VAL_` 只有 0=Initialization、31=SNA** | `$…$ = <raw>`，**無 label**（見 §K K-1） |
| `STATUS_CCAN3.VehicleSpeedVSOSig` | 解得 | `BO_994`／`VAL_` 只有 8191=SNA；`SG_` 13 bit、factor 0.0625、`Km/h` | `$…$ = 64` / `= 65`（raw，物理量非列舉） |
| `EPB_Maintenance_Menu` | PROXI路徑 | 段 1 `PROXI/Format/r585cF/R1 逐字`；`0 = Absent / 1 = Present` | `PROXI EPB_Maintenance_Menu = 0 (Absent)`，**不加 `$`**（IN §8.7.5(c)） |
| `EPB_MaintenanceMode_Active.Info` | 未解得(止於段1) | — | `PENDING: DR-VL4 <名>`（R-P355(c)） |
| `ServiceMode_Popup_Trigger.Info` | 未解得(止於段1) | — | 同上 |
| `TLM_Vehicle_Setup_Menu.Info` | 未解得(止於段1) | — | 同上 |
| `Maintenance_Mode_Enable.Req` | 未解得(止於段1) | — | **未用**：`-046` 之可觀察觸發改採 UI（`Select "EPB Maintenance Mode" = "On"`）＋ 其下游 CAN `$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$`（R-P355 不得直接 Set 內部訊號） |

---

## 4. E38–E45 逐項對照

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| **E38** | 覆蓋 | 17／17 leaf 各 ≥1 TC，無落空 | **17 leaf／17 req_id 有 TC；落空 0；0 TC 者 0** | **過** |
| **E39** | R-S4 括號下半 | 每 TC 有；同 req_id 內不逐字相同 | **違規 0**（缺括號 0／下半含中文 0／同 req_id 重複 0；上半 >50 token 者 0） | **過** |
| **E40** | 尾句號違規 | 0（四欄逐 item 掃） | **0** | **過** |
| **E41** | `[...]`／`'...'`／`<...>` | 0 | **0** | **過** |
| **E42** | `$…$` 之列全數可回溯 v3「解得」 | 非解得列出現 `$` = 0 | **0** —— 使用之訊號 4 種（Fdbk ×38、MaintenanceMode ×16、Req ×6、VehicleSpeedVSOSig ×6），**四者於 v3 皆為「解得」** | **過** |
| **E43** | PENDING 格式 | 全為 `PENDING: DR-VL4 <名>`，無裸空欄 | **違規 0**（6 項全合格式） | **過** |
| **E44** | reasoning | 每 req_id 一則、繁中 2–5 句、含切分依據 | **違規 0**（17／17） | **過** |
| **E45** | modal 於 ER／test_item 下半 | 0 | **0** | **過** |

> **E45 曾為 1，本包自修**：`-056` 之 popup 原以規格全句
> `"Brake Service – To exit Service Mode, vehicle must not be in motion."` 作具名 UI 元件，
> 其內含 `must`，觸 IN §6 之 ER 無 modal；`-054` 之同型全句則使 `tc_title` 達 21 words（超 §4.3 之 14）。
> **處置**：具名 UI 元件改取該 popup 之可識別前段
> （`"Brake Service - Park Brake Retracted"`／`"Brake Service - To exit Service Mode"`），
> **規格全句保留於 `test_item` 上半 verbatim**，追溯性不損；`tc_title` 改為場景標籤（§4.3(c)）。
> **未刪改規格文字，只改「以哪一段作為具名元件」。**

---

## 5. W-3 §9 自檢彙總

17 leaf × 1 TC = **17 條全數**逐條過檢。機讀可判之 **14 項全 PASS**，**未過項 0**：

| 項 | 結果 |
|---|---|
| 1 Test Set 名詞片語、與 `framework.md` 一致 | PASS |
| 2 tc_title 2–14 words、無 modal | PASS |
| 3 Pre-Condition 只收狀態（§4.4） | PASS |
| 4 `input_test_data` = `NA`（§4.5／profile 6） | PASS |
| 5 步驟可執行、無禁用動詞（§5.1） | PASS |
| 6 步驟數 ≥ 2（§10.5） | PASS |
| 10 Procedure ↔ ER 1:1（§6） | PASS |
| 12 traces to Req（§8.1） | PASS |
| 13 design_method 為下拉詞彙逐字（§12） | PASS |
| 14 四欄無尾句號（§11） | PASS |
| 15 UI 標籤用 `"..."`（§11） | PASS |
| 16 `specification_reference` 列出所驗章節（§10.7） | PASS |
| §10.2 priority ∈ P0–P3 | PASS |
| §10.1 十鍵齊全 | PASS |

**人判項未列之理由（誠實揭露）**：§9 之 7（標準片段複用）、8（CLI 格式）、9（baseline）、
11（FP/FF）本批**無適用對象** —— 無 CLI 步驟、無 before/after 比較需求；
標準片段（如 `ENTER_<STATE>` 型）本線尚未建立，P5 覆核後再議。

### lint036 之施作結果

`scripts/lint036.py` 之 positional argument 為 **`.xlsx` 路徑**（`usage: lint036.py … FILES`，
`FILES: 一個或多個 .xlsx 路徑`），**不支援 `generated/` 之文字形**。
本包**未跑**該工具 —— 跑它需先寫工作簿，而寫工作簿為本包禁區（R-VL20）。
依下放包「不支援則記明並以自檢表代」，以上表代之。

### 分布

| 項 | 分布 |
|---|---|
| priority | P1 **4**／P2 **13**（無 P0：本家族不涉安全／開機／音訊輸出等 P0 範疇；P1 為進出 Service Mode 之主流程與逾時） |
| design_method | 等價劃分 9／功能測試 2／狀態轉換 2／負向測試 1／情境用例 1／基礎故障注入 1／邊界值分析 1 |

---

## 6. W-4 sibling／duplicate

17 leaf 同屬 `EPB Maintenance Mode`，互為 sibling 候選（§4.1.4-2）。
**`duplicate_of` 全部未設**（無兩條之 trigger＋outcome＋input＋驗證對象全同）；
`distinguishing_axis` 逐 TC 出，軸分布：

| 軸 | 條數 | 例 |
|---|---|---|
| `input_data` | 11 | Fdbk 值 2／3／4／5／6／8／9／10／11 之等價分割；PROXI Absent／Present 對偶 |
| `trigger_state` | 3 | `-046` HMI 送出 vs `-047` IPC 變遷 vs `-058` 持續 On |
| `timing` | 1 | `-053` T_EPB_MM 逾時且無回應 |
| `boundary` | 1 | `-059` 車速跨 `V_Car_Moving` |
| `mode` | 1 | `-060` 下游對象為選單畫面（vs `-058` 之顯示控制器） |

---

## 7. PENDING 清單（**6 項，3 個內部訊號**）

| req_id | 欄 | 內容 | 錨 |
|---|---|---|---|
| `…-058` | test_procedure／expected_result | `PENDING: DR-VL4 EPB_MaintenanceMode_Active.Info` | DR-VL4 |
| `…-059` | test_procedure／expected_result | `PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info` | DR-VL4 |
| `…-060` | test_procedure／expected_result | `PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info` | DR-VL4 |

三者於 `signal_chain_v42_v3.tsv` 皆為 **未解得(止於段1)**（LID／HMI Settings／PROXI 三處
段 1 皆無依據），依 **R-P355(c)** 不得以 `Set X.Info` 假裝可執行。
**三條 TC 非全 PENDING** —— 其上游 CAN 訊號與具名 UI 元件仍逐步可驗，
故各 TC 仍有實質可執行之步驟與 ER。

---

## §K —— 規格語意不明處（四項，不補洞）

### K-1 `EPB_Maintenance_Fdbk` 之 2–11 於 DBC **無 `VAL_` label**（影響 9 條 TC）

DBC 實測 `VAL_ 1486 EPB_Maintenance_Fdbk: 0 "Initialization" 31 "SNA"`；
`SG_` 定義為 `21|5@0+ (1,0) [0|31] "-"`（5 bit，範圍 0–31）。
規格與 037 所用之 **2／3／4／5／6／8／9／10／11 九個值全數無 label**。

**處置**：依 IN §8.7.5(a)（label 逐字取 DBC `VAL_`）與 §8.4.1（不造值），
九條 TC 寫 `$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = <raw>`，**不附 `(<label>)`**，
並於每條 `remarks` 揭露原因。**未自造 label**（如把「vehicle speed not 0」寫成列舉字）。
**待裁**：是否向上游索該訊號之完整 `VAL_`（DR 依 Pei 裁先不送）。

### K-2 Fdbk **4 與 5 之規格文字逐字相同**

段 1076 與 1081 之 popup 描述皆為
`the user selected yes to entering service mode but the EPB switch is currently engaged`
（037 之 `-050`／`-051` 描述亦逐字相同）。
兩個不同回饋碼對應**同一句**使用者訊息，規格未述其差異。

**處置**：依 §8.2.2（RD 分解紀律：一 Req 一條，不合併）各出一條，
`-051` 之括號下半明記 `second refusal code carrying the same EPB switch text as Fdbk = 4`，
`distinguishing_axis` 記其為等價類之不同分割。**未合併、未臆測其差異。**
**待裁**：兩碼之語意差異（可能為 switch engaged vs released，或不同偵測來源）。

### K-3 `-059` 之 ignition 分支**無訊號名可用**

規格段 1111 之或分支寫 `in case of transition from "Ignition Off" to "Inigtion On"`
（原文含拼字 `Inigtion`）；037 描述寫 `(Ignition_{S}tatus)` —— **`{S}` 為佔位符殘留**，
非合法訊號名，且該名於 `signal_chain_v42_v3.tsv` 與主 DBC 皆查無。

**處置**：`-059` 只覆蓋**車速跨門檻**分支，ignition 分支**未涵蓋**，
於該 TC 之 `remarks` 與 `reasoning` 明白揭露（IN §10.4 之「未涵蓋」）。
**未臆造 ignition 訊號名、未以他訊號代入**（R-13／§8.4.1）。
**待裁**：ignition status 之實名（可能為 `STATUS_*` 家族之某訊號）。

### K-4 規格節內之拼字與排版瑕疵（**已記，不改**）

| 段 | 原文 | 疑 |
|---|---|---|
| 1049／1051 | `EPB Maintance Mode` | 少 `en`（應為 `Maintenance`） |
| 1065／1070／1075／1080／1085／1094／1098／1102／1106 | `THEN TLM sall:` | `sall` 應為 `shall` |
| 1111 | `Inigtion On` | 應為 `Ignition` |
| 1054／1059 等 | 值以 `" On  "`／`" 2 "` 前後帶空白 | 引號內空白，比對時須 strip |

**處置**：`test_item` 上半之 verbatim **取 037 之 `Requirement Description`**
（其為 SWE1 已整理之版本，拼字正確且為 RD 分解之權威單位，IN §8.2），
非取規格段之原始瑕疵句；規格段以 `specification_reference` 指回。
**規格原文未改，瑕疵據實記於此。**

---

## 8. 獨立判斷

1. **一項本包自修並已揭露**：E45／`tc_title` 長度之衝突（第 4 節末），
   起因於把 popup 全句當具名 UI 元件。已改為取可識別前段，規格全句保留於 verbatim 上半。
2. **一項未做且指得出理由**：`lint036.py` 未跑（只吃 `.xlsx`，而寫工作簿為禁區），
   以自檢表代（第 5 節）。
3. **一項刻意窄做**：`-046` 之規格觸發為內部訊號 `Maintenance_Mode_Enable.Req`（段 1052），
   本包**未以 `Set …Req` 書寫**（R-P355 明禁），改以 UI 選擇觸發並驗其下游 CAN 訊號。
   此為 R-P375(b) 之 UI 路徑精神，但 `Maintenance_Mode_Enable.Req` 於段 1 **未命中 HMI Settings**，
   故該 UI 元件名 `"EPB Maintenance Mode"` 取自**規格與 037 之選單項名**，非 HMI Settings 錨點。
   **據實記明，交分析層判是否須改為 PENDING。**
4. **一項未涵蓋而具名**：`-059` 之 ignition 分支（§K K-3）。
5. **一項提醒 P5 覆核**：本批 17 條**全為 1 TC／1 leaf**，無一條拆分（`split_flag` 全 `False`）。
   其正當性逐條寫入 `reasoning`（§10.4 第 3 點），但**若覆核者認為 `-046`
   之三個同時效果（送訊號／popup／起計時）應拆為三條**，則須重做該條 ——
   本包依 §8.2.2「不得再分解、不得合併」採一條，以多階段 ER 表達。

---

## 9. A／DR 狀態

**本包未新開 anomaly。** §K 四項為規格語意問題，依下放包令列 §K 而非 A 號；
若分析層認為 K-1／K-3 須立 A 號，請指示。

| DR | 狀態 |
|---|---|
| DR-VL1／DR-VL2 | 已登記，未送出 |
| **DR-VL4** | 本包 6 個 PENDING 之錨；**未送出**（Pei 裁先不送） |
| DR-VL3 | 結案 |

**本包未送出任何 DR。**

---

## 10. `gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 505
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash`** —— 依 **R-VL13** 記「**待 Pei 重生**」。
id 級實測（樹外 `--out`，未寫入 repo）：新增 id 為 `R-VL12`–`R-VL20`（本線）
＋ `R-VT*`（vsm_v43）＋ `R-VS84`–`R-VS88`（vehicle_setting）；**移除 0**；
`sha8` 變動者其 **`body_sha8` 皆未變**。
**依 R-VL15(c) 修訂後之判準（無刪除列、既有列 `body_sha8` 無變動）完全滿足，可上繳。**

**(乙) `canon_refs` 505** —— 含 `vsm_v42` 者 **3 列**，與上繳 02／03／04 **逐字相同**
（`ANOMALIES.md` 之 `R-G40`、`RUNBOOK.md` 裸 `§3`、`DECISIONS.md` 裸 `§4`，
後二者為共用腳本模板）。**本包新增之 35 個 `generated/` 檔未新增任何一列。**

**(丙)(丁) `gates_tsv`／`lint_paths` = 4** —— 與本線無關，先在，與前四包逐字相同。
本包產出皆為 `.json`／`.md`，落 `generated/`，未觸 `lint_paths` 之 xlsx 落點規則。

**無一支肇因於本包之寫入。**

---

## 11. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `features/vsm_v42/data/pilot_epb_spec.md` | **新建** —— 規格節 1047–1117 逐字（58 非空段） |
| `features/vsm_v42/generated/b1_epb/*.json`（17） | **新建** —— IN §10.1 十鍵＋`reasoning`＋`distinguishing_axis`＋`remarks` |
| `features/vsm_v42/generated/b1_epb/*.md`（17） | **新建** —— 人讀形 |
| `features/vsm_v42/generated/b1_epb/INDEX.md` | **新建** —— 索引＋自檢表＋PENDING 清單 |
| `features/vsm_v42/docs/upstream/05_pilot_epb.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動（逐項聲明）**：
**`features/vsm_v42/sandbox/`（連 read-write 開啟都未為之；本包對母本副本只做 `read_only=True` 之讀取，
用於取下拉選單詞彙）**、`features/vsm_v42/delivered/`（不存在，未建）、
`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`（**只讀**）、`scripts/`、
`forms/`（DBC／PROXI 只讀）、`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、
`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md, ANOMALIES.md, DECISIONS.md, feature.yaml,
framework.md, data/*.tsv（除新建之 pilot_epb_spec.md）}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 12. 待 Pei／分析層之五項

1. **§K K-1**：`EPB_Maintenance_Fdbk` 之 2–11 無 `VAL_` label —— 9 條 TC 之值無列舉字。
   是否向上游索完整 `VAL_`。
2. **§K K-2**：Fdbk **4 與 5 規格文字逐字相同**，兩碼語意差異未明。
3. **§K K-3**：`-059` 之 ignition 分支無合法訊號名（037 寫 `(Ignition_{S}tatus)`），
   該分支**未涵蓋**。
4. **第 8 節第 3 項**：`-046` 之 UI 元件名取自規格選單項名而非 HMI Settings 錨點，
   是否須改為 PENDING。
5. **第 8 節第 5 項**：`-046` 是否應拆為三條（送訊號／popup／起計時）。
   ＋ P5 覆核後之寫回授權（R-VL20：待分析層覆核與 Pei 再授權）。
