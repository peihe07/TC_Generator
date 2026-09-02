# 上繳包 08 — vsm_v42：`-059` 一列（R-VL23 A 路）→ **b1 FROZEN**

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/08_freeze.md`

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | `-059` 之 `test_item` 上半改完整原句 verbatim；`INDEX.md` 落凍結表 |
| 核實無誤 | **E62／E63／E64 全過**；E63 = **17／17** |
| 正確地不動 | 其餘 33 檔 diff = 0；`-059` 之括號下半／Procedure／ER／PENDING／remarks **一字未動**；不寫工作簿、不建 `delivered/` |

**總判：三 E 全過 → `b1 FROZEN (R-VL23)` 已落 `INDEX.md`。**

---

## 1. 逐列 diff（`-059`，唯一修訂）

### `test_item` 上半

| | 內容 |
|---|---|
| **舊**（句內剪接，違 R-4／R-6） | `When the TLM receives a value changing from <= [V_Car_Moving] to > [V_Car_Moving] via signals (STATUS_CCAN3.VehicleSpeedVSOSig), Then TLM shall send a layout request to the display manager through internal signal (ServiceMode_Popup_Trigger.Info)` |
| **新**（037 Requirement Description 完整原句 verbatim） | `When the TLM receives a value changing from <= [V_Car_Moving] to > [V_Car_Moving], **or a transition from [Ignition Off] to [Ignition On]** via signals (STATUS_CCAN3.VehicleSpeedVSOSig) **\| (Ignition_{S}tatus)**, Then TLM shall send a layout request to the display manager through internal signal (ServiceMode_Popup_Trigger.Info)` |

**復原之內容**：句中之 ignition 或分支子句與 `| (Ignition_{S}tatus)` 訊號欄。
**機讀驗證**：**42 token**（R-3 上限 50，過）；為 037 Description 之**逐字子字串**（`in` 判 `True`）。

### 未動之欄位（逐項確認）

| 欄 | 狀態 |
|---|---|
| 括號下半 | `(Boundary crossing of V_Car_Moving raises the brake-pedal popup)` —— **一字未動** |
| `test_procedure` | **5 步未動** |
| `expected_result` | **5 ER 未動**（1:1 維持） |
| PENDING | **2 項未動**（`PENDING: DR-VL4 ServiceMode_Popup_Trigger.Info`） |
| `remarks` | **未動** —— ignition 分支未涵蓋之揭露原本即在其中 |
| `tc_title`／`priority`／`design_method`／`distinguishing_axis`／`specification_reference` | 未動 |

### `reasoning` —— **未照下放包字面之「補一句」，改為併入既有句**

下放包第一節允許「僅允許補一句『上半為完整原句，ignition 分支未涵蓋見 remarks』」。
**照辦會使句數由 5 增為 6，破 IN §10.4 之 2–5 句**，而 E64 要求 E38–E45 全過（含 E44）。

**實測**：附加後 `-059` 之 reasoning 句數 = **6**，E44 判違規 1。
**處置**：改為**重寫該段為 4 句**，其中第三句**併入**下放包所要之揭露內容
（上半為完整原句 verbatim（R-VL23(a)）；ignition 分支未涵蓋，037 之 `(Ignition_{S}tatus)`
為佔位符殘留、規格段 1111 拼作 `Inigtion`，皆非合法訊號名，依 §8.4.1 不臆造，
揭露見 remarks 與 §K K-3）。

**要求之實質（揭露）全數保留，只是不另起第 6 句。** 據實回報。

---

## 2. 預期數字

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| **E62** | 修訂檔數 | 2（`-059` json＋md）；其餘 32 檔 diff = 0 | **改 2 檔**；其餘 **33 檔**逐位元 diff = 0（含 `INDEX.md`，其於本節統計後另行重產） | **過** |
| **E63** | E56 重跑 | 17／17（機讀子字串斷言 True） | **17／17，True** | **過** |
| **E64** | E38–E45／E53–E55 重跑 | 全過 | **E38 17/17／E39 0／E40 0／E41 0／E42 0／E43 0／E44 0／E45 0；E54 = 0；Procedure↔ER 非 1:1 = 0** | **過** |

> **E64 曾為不過**：`reasoning` 附加句使 E44 = 1（見第 1 節末），已改為併句，現 0。

---

## 3. 凍結

**`b1 FROZEN (R-VL23)`** 已落 `generated/b1_epb/INDEX.md` 首節。此後任何變更**須新裁決**（R-VL23(d)）。

### 凍結時之狀態

| 項 | 值 |
|---|---|
| req_id（＝leaf） | **17** |
| TC 總數 | **17** |
| 檔數 | **35**（17 json ＋ 17 md ＋ INDEX.md） |
| PENDING 項 | **6**（3 個內部訊號 × 2 欄；錨 DR-VL4） |
| priority | P1 4／P2 13 |
| design_method | 等價劃分 9／功能測試 3／狀態轉換 2／負向測試 1／基礎故障注入 1／邊界值分析 1 |
| `$…$` 訊號 | 4 種，皆 v3「解得」 |
| `registered without a bus error` | 15 處，**全為測試員送出步** |
| 工作簿／`delivered/` | **未寫／未建** |

**逐檔 sha256 前 8 碼表**（34 檔，`INDEX.md` 自指故不入表）已落 `INDEX.md` 之
「凍結檔表」節，供寫回工法包比對。

### 凍結時之未結（皆已具名，不阻塞凍結）

§K **K-1**（Fdbk 2–11 無 `VAL_` label，影響 9 條）／**K-2**（Fdbk 4 與 5 規格同文）／
**K-3**（`-059` ignition 分支無合法訊號名）／**K-4**（規格拼字瑕疵）／
**K-5**（退出側請求路徑規格未載）／**K-6**（`-054` 歸屬 —— 已由 R-VL22(c) 量測定案）。
DR-VL1／DR-VL2／DR-VL4 皆已登記未送出（Pei 裁先不送）。

---

## 4. `gate_all.py` 與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 506
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash`** —— 依 **R-VL13** 記「待 Pei 重生」。
id 級實測（樹外 `--out`）：**新增 33／移除 0／`body_sha8` 亦變 0** ——
依 R-VL15(c) 之判準滿足，可上繳。
**`R-VL23` 之 `body_sha8` = `a9b6218d`**（`sha8` = `32ca3b71`，觀測值）。

**(乙) `canon_refs` 506** —— 含 `vsm_v42` 者 **3 列**，與上繳 02–07 逐字相同
（`ANOMALIES.md` 之 `R-G40`、`RUNBOOK.md` 裸 `§3`、`DECISIONS.md` 裸 `§4`，後二者為共用腳本模板）。
本包修訂之 3 檔未新增任何一列。

**(丙)(丁) `gates_tsv`／`lint_paths` = 4** —— 與本線無關，先在，與前六包逐字相同。

**無一支肇因於本包之寫入。**

---

## 5. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `generated/b1_epb/…-059.{json,md}` | `test_item` 上半改完整原句 verbatim ＋ reasoning 併句（R-VL23(a)） |
| `generated/b1_epb/INDEX.md` | 落 **`b1 FROZEN (R-VL23)`** ＋ 凍結檔表（34 列 sha8）＋ 未結清單 |
| `features/vsm_v42/docs/upstream/08_freeze.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：`generated/b1_epb/` 其餘 32 檔（逐位元 diff = 0）、`sandbox/`（未開啟）、
`delivered/`（未建）、`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`、`scripts/`、
`forms/`、`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、
`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md, ANOMALIES.md, DECISIONS.md, feature.yaml,
framework.md, data/}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 6. 獨立判斷

1. **一項未照下放包字面並已回報**：`reasoning` 之「補一句」與 §10.4 之 2–5 句上限衝突，
   改為併入既有句（第 1 節末）。揭露之實質全保留。
2. **凍結之效力已生**：此後 `generated/b1_epb/` 之任何變更須新裁決。
   本上繳所列之 §K 六項與三個 PENDING **不因凍結而消滅**，其解決須經新裁決回頭改 b1。
3. **一項提醒寫回工法包**：凍結檔表之 sha8 為**文字形**之指紋。
   寫回工作簿後，工作簿列與該表之對應須另建（本包未做，亦不在範圍）。
4. **一項承上**：`lint036.py` 自 05 起未跑（只吃 `.xlsx`）；
   **寫回工法包之後方能首次對本線實跑 lint**，屆時可能揭出文字形自檢未涵蓋之項。

---

## 7. 待 Pei／分析層

1. **寫回工法包**（R-VL22(e)）：含 x14 DV 保全查證、工作簿列 ↔ 凍結檔表之對應建立。
2. **b2 批次序**（R-VL17 十組之其餘九組，128 − 17 = 111 leaf）。
3. **§K K-1〜K-6** 與 DR-VL1／DR-VL2／DR-VL4 之送出與否。
4. **台帳重生**（現落後 33 個新 id，三線；無刪除、`body_sha8` 無變動）。
