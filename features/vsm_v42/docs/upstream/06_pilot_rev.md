# 上繳包 06 — vsm_v42：pilot b1 修訂輪（R-VL21 REV-1／2／4）

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/06_pilot_rev.md`

## 結果分類（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | REV-1／2（`-046`）＋ REV-4（Fdbk 族 9 條）；INDEX 重產並記族內一致選擇 |
| 核實無誤 | **E46 過**（改 20 檔／不動 15 檔 diff = 0）；**E47 過**（E38–E45 全數）；**E48 過**；**E49 過** |
| 正確地不動 | 七條逐字不動；**`-053` 不改**（E50 之唯一違規落於該條，見第 5 節 —— 改它會破 E46）；不寫工作簿；不寫 `Press "Yes"`（無逐字依據）；退出側請求訊號**不臆造** |

**總判：修訂完成。E50 = 1，肇因為 E46 與 E50 在 `-053` 上直接衝突，不自行調和。**

---

## 1. 第一節之一 —— 分支查證（逐字引段）

**問**：規格節有無「等候 IPC 回應期間 Initializing popup 持續顯示」之逐字依據？

**查證**（掃 `data/pilot_epb_spec.md` 全 58 非空段，關鍵詞
`initializ|remain|still|during|persist|not expired|keep`，不分大小寫）：

| 段 | 逐字原文 |
|---|---|
| 1055 | `activate and display the Popup related to "  initializing "  like described in the "Human Machine Interface logic &  flow" document` |
| 1056 | `Start T_EPB_MM ` |
| 1057 | `T_EPB_MM  is the timeout for the EPB Maintenance Mode setting` |
| 1058 | `IF  T_EPB_MM  is not expired` |
| 1059 | `IF        "IPC_VEHICLE_SETUP2.EPB_MaintenanceMode" B CAN signal  change from "Off"  to "On"` |

**結論：無。** 規格只述「activate and display」（1055）與「Start T_EPB_MM」（1056），
1058 隨即進入分支條件，**全節無任何述及該 popup 於等候期間之持續狀態之句**。
命中 `remain`／`still`／`during`／`persist`／`keep` 者 **0 段**。

→ 依下放包第一節之一之「無」分支：**刪步驟 4 與 ER 4**，
`reasoning` 補「T_EPB_MM 之到期效果由 `-053` 驗（§8.2.1 委任）」。

### 連帶查證 —— Yes 確認 popup（Fdbk 族之 `-050`／`-051`）

下放包令「`-050`/`-051` 若規格載確認 popup 之 Yes，則含 `Press "Yes" in the popup`，**逐字有據才寫**」。

**查證**：全節含 `yes` 之段共 8 段（1061／1066／1071／1076／1081／1086／1099／1113），
**其 `yes` 一律出現在 popup 訊息文之內**（`the user selected yes to entering/exiting service mode …`），
描述使用者**已做過**之動作，**非規格所定之確認對話步驟**。
全節無 `confirm` 命中；`select` 亦僅出現於同一批 popup 文內。

**結論：無逐字依據 → 不寫該步。** 觸下放包第四節升級條件之「發起步需臆造 popup 文字方能寫」之
前半但未觸其後半 —— 本包**未造**，改以規格段 1052–1054 所載之實際發起路徑書寫（見第 3 節）。

---

## 2. REV-1／2 —— `-046` 逐項 diff

| 項 | 修訂前 | 修訂後 |
|---|---|---|
| Procedure 步數 | 4 | **3** |
| P1 | `Select "EPB Maintenance Mode" = "On" to trigger $…Req$ signal transmission` | **不變** |
| P2 | `Read the signal $…Req$ and check that it is 1 (On)` | **`Read the named UI element "EPB Maintenance Mode" setting control and check that it is "On"`** |
| P3 | `Read the named UI element "Initializing" pop-up and check that it is displayed` | **不變**（位次由 3 → 3） |
| P4 | `Hold for 35000 ms` | **刪除**（REV-1） |
| ER1 | `The signal $…Req$ = 1 (On) is registered without a bus error` | **刪除**（REV-2：本條為 DUT 送出，非測試員送出） |
| ER 現 1 | — | `The signal value $…Req$ = 1 (On) is received` |
| ER 現 2 | — | **`The named UI element "EPB Maintenance Mode" setting control is "On"`**（REV-2 新增：涵蓋 test_item 之 status → On） |
| ER 現 3 | `The named UI element "Initializing" pop-up is displayed` | 不變 |
| ER4 | `The T_EPB_MM timer is held for 35000 ms` | **刪除**（REV-1：timer 為內部態，不可觀察，違 §6） |
| remarks | `T_EPB_MM = 35000 ms per the spec constant table…` | **`UI element names are taken from the menu item and popup wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List`** |
| reasoning | 原 4 句 | **重寫 5 句**：含 (i) 三結果、(ii) §5.7／R-VL21(b) 不拆、(iii) **T_EPB_MM 委任 `-053`（§8.2.1）**、(iv) **方向註記**（037 之 `TLM receives` 為應用層視角；依 DBC `BO_162` 之發送方為 TLM、接收節點為 IPC，故本 TC 方向為 TLM 送出，兩者不矛盾） |

**Procedure ↔ ER 3:3，1:1 成立。**

### E48 —— `-046` 之 ER 涵蓋

`test_item` 上半明載三結果，逐一對應：

| test_item 之結果 | 對應 ER |
|---|---|
| `Update the EPB Maintenance Mode setting status to On` | **ER2**（UI 設定控制顯示 `"On"`） |
| `Activate and display the "Initializing" popup` | **ER3** |
| 送出 `$TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$` | **ER1**（`is received` 式） |
| `Start the T_EPB_MM timer` | **不入本條 ER** —— REV-1 之處置，委任 `-053`，`reasoning` 已載 |

**E48 過。**

---

## 3. REV-4 —— Fdbk 族 9 條逐項 diff

### 共同結構（修訂後）

**進入側 `-048`／`-049`／`-050`／`-051`／`-052`**（Fdbk 2／3／4／5／6）：

| | 修訂後 |
|---|---|
| Pre-Condition | `PROXI EPB_Maintenance_Menu = 1 (Present)`／`The EPB Maintenance Mode menu item is displayed`／**`The EPB Maintenance Mode setting is Off`**（原第三項為 `The TLM is in the Vehicle Settings menu`） |
| P1（**新增發起步**） | `Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ signal transmission` |
| E1 | `The signal value $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On) is received` —— **依規格段 1054 逐字有據** |
| P2 | `Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = <raw>`（原 P1） |
| E2 | `… = <raw> is registered without a bus error`（測試員送出，E50 允許） |
| P3 | `Read the named UI element "<popup>" and check that it is displayed`（原 P2） |
| E3 | `The named UI element "<popup>" is displayed` |
| **原 P3／E3 回讀步** | **削去**（R-VL21(f) 末句；全族一致） |

**進入側之 E1 依據（逐字）**：段 1054
`Set "TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req" B-CAN signal equal to " On  " and sends this signal to IPC`。

**退出側 `-054`／`-055`／`-056`／`-057`**（Fdbk 8／9／10／11）：

| | 修訂後 |
|---|---|
| Pre-Condition | `PROXI EPB_Maintenance_Menu = 1 (Present)`／`The EPB Maintenance Mode menu item is displayed`／**`The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On)`**（已在 Service Mode 中） |
| P1（**新增發起步**） | `Select "EPB Maintenance Mode" = "Off" to request the exit from Service Mode` |
| E1 | **`The named UI element "EPB Maintenance Mode" setting control is "Off"`** —— **不寫請求訊號**，理由見下 |
| P2／E2／P3／E3 | 同進入側之結構 |
| 回讀步 | 削去 |

> **退出側 E1 不寫請求訊號之理由（§K K-5）**：規格節**只載進入側之請求訊號**（段 1054 之
> `equal to " On  "`），**全節無任何述及退出時送出 `EPB_MaintenanceMode_Req = Off` 之句**。
> 若比照進入側寫 `The signal value $…Req$ = 0 (Off) is received`，即**臆造規格未述之因果**（§8.4.1）。
> 故退出側之發起步 ER 只斷言**可觀察之 UI 設定狀態**，並於 `remarks` 與 `reasoning` 揭露此不對稱。
> **依下放包第四節「無據則發起步 ER 寫請求訊號 is received 式」之字面，本包未照辦** ——
> 該指示之前提為「有據」，退出側實測無據；照辦即造。**據實回報，交分析層裁。**

### 族內一致選擇（R-VL21(f) 末句，已記入 `INDEX.md`）

**回讀步一律削去**（九條無例外）。理由：該步為測試員自送訊號後之回讀，冗餘而不加值。

### 逐條 remarks 增補

| 側 | remarks 內容 |
|---|---|
| 進入側 5 條 | `<VAL_ 缺值揭露>` ＋ `<UI 元件名來源 R-VL21(a)>` ＋ `The entry request step is based on spec paragraph 1054` |
| 退出側 4 條 | `<VAL_ 缺值揭露>` ＋ `<UI 元件名來源>` ＋ `The exit request path is not stated verbatim in the spec section: paragraph 1054 states the entry request only, so the exit step is asserted through the UI control state and not through a request signal (see section K)` |

**括號下半、priority、design_method 皆未動**（下放包第一節之 4）。

---

## 4. 七條不動

`-044`／`-045`／`-047`／`-053`／`-058`／`-059`／`-060` —— **`.json` 與 `.md` 共 14 檔，
逐位元 diff = 0**（`cmp` 對修訂前備份逐檔比對，全部相同）。

---

## 5. 預期數字 E46–E50

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| **E46** | 修訂檔數 | 10 md ＋ 10 json；其餘 14 檔 diff = 0 | **改 20 檔**（`-046`／`-048`–`-052`／`-054`–`-057` 各 json＋md）；**未變 15 檔**（14 檔 ＋ `INDEX.md`；`INDEX.md` 於本節統計後另行重產） | **過** |
| **E47** | E38–E45 重跑 | 全過 | **E38 17/17／E39 0／E40 0／E41 0／E42 0／E43 0／E44 0／E45 0** | **過** |
| **E48** | `-046` 之 ER 涵蓋 | 三結果全數有對應 ER；timer 依分支處置 | **三結果 → ER2／ER3／ER1；timer 委任 `-053`** | **過** |
| **E49** | Fdbk 九條 | 各含發起步且位於送 Fdbk 之前；ER 1:1 | **違規 0**（九條之 `Select` 步索引皆小於 `Send … Fdbk` 步；全 3:3） | **過** |
| **E50** | `registered without a bus error` 僅限測試員送出步 | DUT 送出步 = 0 | **1** | **不符** |

### E50 之不符 —— **E46 與 E50 在 `-053` 上直接衝突，不自行調和**

唯一違規列：

```
-053 步1  P: Select "EPB Maintenance Mode" = "On" to trigger $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ …
          E: The signal $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On) is registered without a bus error
```

此為 **DUT 送出**之步（HMI 觸發 → TLM 送出），其 ER 用了測試員送出之確認式 ——
與 `-046` 之 ER1 **完全同型**，而 `-046` 之該式已依 REV-2 刪除。

**衝突之所在**：
- **E46** 要求「其餘 14 檔 diff = 0」，且下放包明文「修訂限十條，其餘七條**逐字不動**」，`-053` 在該七條內；
- **E50** 要求「DUT 送出步之 bus-error 式 = 0」。

**本包之處置**：**遵守明文之修訂範圍，`-053` 不動**，E50 記不符並歸因。
理由：修訂範圍為條文（R-VL21 末句）與下放包雙重明載之硬界線，
而 E50 為預期數字；FO 第 8.2 節之「不自行調和」要求回報而非擇一修改。
**若分析層裁定 `-053` 應併修，本包已備妥同型修法**（刪該 ER，改 `is received` 式），
一列即可，不影響其餘。

> **附帶觀察（不改）**：`-046` 之 `design_method` 仍為 `情境 / 用例 (Scenario / Use Case Testing)`。
> 修訂後其 Procedure 由 4 步減為 3 步且限於單一功能，依 IN §12 之 tie-break
> （`Scenario = ≥3 steps crossing features`／`Functional = 1–2 steps single feature`）
> 可能應改為 `功能測試`。下放包未令改 `-046` 之 design_method（第一節之 4 之「不動」係就 Fdbk 族而言，
> 但 `-046` 之四項指示亦未含此項），**本包不自行改**，交分析層裁。

---

## 6. §9 機讀重跑

修訂後 17 條全數重跑，機讀可判之 **14 項全 PASS，未過項 0**（清單同上繳 05 第 5 節，逐項結果不變）。

`scripts/lint036.py` 仍未跑 —— 其 positional argument 為 `.xlsx`，而寫工作簿為本包禁區；
依下放包 05 之同一處置以自檢表代。

### 分布（修訂後）

| 項 | 分布 |
|---|---|
| priority | P1 **4**／P2 **13**（未動） |
| design_method | 等價劃分 9／功能測試 2／狀態轉換 2／負向測試 1／情境用例 1／基礎故障注入 1／邊界值分析 1（未動） |
| PENDING | **6**（未動；`-058`／`-059`／`-060` 各 2） |
| `$…$` 使用 | 4 種訊號，皆為 v3「解得」；出現數 `EPB_MaintenanceMode` ×20、`EPB_Maintenance_Fdbk` ×20、`EPB_MaintenanceMode_Req` ×14（修訂後由 6 增為 14，因九條發起步）、`VehicleSpeedVSOSig` ×6 |

---

## §K 增補（承上繳 05 之 K-1〜K-4）

### K-5（**新**）—— 退出側之請求路徑規格未載

規格節段 1052–1054 只載**進入側**（`user sets "Maintenance_Mode_Enable.Req" … " On"` →
`Set "TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req" … " On  "`）；
**全節無退出側之對應句**。而 Fdbk 9／10／11 之 popup 文義明為 `exiting service mode`，
即退出流程確實存在，只是其請求機制未被規格書寫。

**處置**：退出側四條之發起步 ER 只斷言 UI 設定狀態，**不斷言 `Req = 0 (Off)` 之送出**。
**待裁**：(a) 退出是否確實經 `EPB_MaintenanceMode_Req = 0 (Off)`；
(b) 若是，是否認定為規格漏載並比照進入側書寫。

### K-6（**新**）—— `-054`（Fdbk = 8）之進出側歸屬存疑

下放包將 `-054` 歸入退出側（`-054`〜`-057`），本包照辦。
惟其 popup 文字為 `Brake Service – Park Brake Retracted. To reset, press brake pedal and
activate Park Brake switch.`，**未含 entering／exiting 任一詞**（其餘八條皆含）。
037 描述亦然。**其歸屬無逐字依據。**

**處置**：**依下放包之分組照辦**（歸退出側，Pre-Condition 為已在 Service Mode），
差異記於此，不自行改組。**待裁**：`-054` 應屬進入側、退出側，或兩者皆非（獨立狀態回報）。

---

## 7. 獨立判斷

1. **一項未照下放包字面辦並已回報**：退出側 E1 之寫法（第 3 節末／§K K-5）——
   下放包之 fallback「無據則寫請求訊號 `is received` 式」，其前提為該訊號有據；
   退出側實測無據，照辦即造（§8.4.1）。
2. **一項自修**：修訂初版以「附加句」補 `reasoning`，使 Fdbk 族達 6–7 句而破 §10.4 之 2–5 句
   （E44 一度 9 條違規）。已改為**整段重寫**，現 17 條全數合規。
3. **一項衝突已回報不調和**：E46 ↔ E50 於 `-053`（第 5 節）。
4. **一項附帶觀察不改**：`-046` 之 `design_method`（第 5 節末）。
5. **一項下放包未涵蓋而本包未動**：Fdbk 族之 `distinguishing_axis` 仍為原值
   （`input_data` 系列）。修訂後九條之 Procedure 結構一致而僅 Fdbk 值不同，
   該軸仍正確，故未動。
6. **一項須在寫回前解決**：`INDEX.md` 已記族內一致選擇（回讀步全削），
   但**寫回工作簿之工法尚未定**（R-VL21 第五節：另包，含 x14 DV 保全查證）。
   本包產出仍為文字形，**未寫工作簿、未建 `delivered/`**。

---

## 8. `gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 506
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash`** —— 依 **R-VL13** 記「**待 Pei 重生**」。
id 級實測（樹外 `--out`，未寫入 repo）：**新增 id 23**（`R-VL12`–`R-VL21` 等三線之新條）；
**移除 0**；`sha8` 變動者其 **`body_sha8` 皆未變（0）**。
**依 R-VL15(c) 之判準完全滿足，可上繳。**
`R-VL21` 之 **`body_sha8` = `fde2fc91`**（`sha8` = `3dbf6e23`，觀測值）。

**(乙) `canon_refs` 506** —— 含 `vsm_v42` 者 **3 列**，與上繳 02–05 **逐字相同**
（`ANOMALIES.md` 之 `R-G40`、`RUNBOOK.md` 裸 `§3`、`DECISIONS.md` 裸 `§4`）。
**本包修訂之 20 檔未新增任何一列。**

**(丙)(丁) `gates_tsv`／`lint_paths` = 4** —— 與本線無關，先在，與前五包逐字相同。

**無一支肇因於本包之寫入。**

---

## 9. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `generated/b1_epb/…-046.{json,md}` | REV-1／2 |
| `generated/b1_epb/…-{048,049,050,051,052,054,055,056,057}.{json,md}`（18 檔） | REV-4 |
| `generated/b1_epb/INDEX.md` | 重產（加「修訂」欄、族內一致選擇之記載、自檢重跑） |
| `features/vsm_v42/docs/upstream/06_pilot_rev.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：`generated/b1_epb/` 之其餘 14 檔（逐位元 diff = 0）、
`features/vsm_v42/sandbox/`（未開啟）、`delivered/`（未建）、
`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`、`scripts/`、`forms/`、
`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、
`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md, ANOMALIES.md, DECISIONS.md, feature.yaml,
framework.md, data/}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 10. 待 Pei／分析層之五項

1. **E50 ↔ E46 之衝突**：`-053` 之 DUT 送出步 bus-error 式是否併修（一列即可）。
2. **§K K-5**：退出側請求路徑規格未載 —— 退出是否經 `EPB_MaintenanceMode_Req = 0 (Off)`。
3. **§K K-6**：`-054`（Fdbk = 8）之進出側歸屬無逐字依據。
4. **`-046` 之 `design_method`** 是否由 `情境 / 用例` 改為 `功能測試`（§12 tie-break）。
5. **寫回工法另包**（R-VL21 第五節）＋ 承上繳 05 之 K-1〜K-4 四項未結
   ＋ 台帳重生時機、共用腳本一裁。
