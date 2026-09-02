# 上繳包 12 — vsm_v43：b2-1 生成　Forward Collision Warning（15 leaf）

日期：2026-09-02　執行層　對應下放包：`docs/handoff/12_b2_fcw.md`
產出止於 `generated/`；**未寫工作簿、未寫 `delivered/`、未動 `sandbox/base/`、已凍 b1 一位元未動**。
台帳不重生；DR 不代發。**綠色通道計數第一批。**

---

## 〇、一句話結論

**15 leaf → 15 TC，E 全項通過；K-14 新法順做成功，21/29 組唯一命中、回填 22 列，`none` 99 → 77。**

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E38 | 覆蓋 | 15 leaf 各 ≥1 TC | **15/15** | ✅ |
| E39 | R-S4 括號下半 | 每 TC 有；同 req_id 內不逐字相同 | **15/15；重複 0** | ✅ |
| E40 | 尾句號違規 | 0 | **0** | ✅ |
| E41 | `[...]`／`'...'`／`<...>` | 0 | **0** | ✅ |
| E42 | `$…$` 可回溯 v5 解得 | 全數 | **4 名，皆解得** | ✅ |
| E43 | PENDING 格式 | 全為 `PENDING: DR-VT4 <名>` | **本批 0**（理由逐一實測，見 §四） | ✅ |
| E44 | reasoning | 繁中 2–5 句、含切分依據 | **15 則，各 4 句** | ✅ |
| E45 | modal 於 ER／test_item 下半 | 0 | **0** | ✅ |
| E51 | Remarks provisional | 15/15 | **15/15** | ✅ |
| **E56** | test_item 上半逐字全等 | 對 `leaves_interim_v2` | **15/15** | ✅ |
| **E87** | K-14 補列數／仍 none | 觀測 | **補 22 列**；`none` **99 → 77** | ✅ |

## 〇′、首項（R-VT25(a)）

`framework.md` 之 Layer 2 v2 表標籤已由「**待 Pei 准後鎖**」改為「**鎖定 (R-VT24)**」。

## 一、契約落實與雙錨前綴（首列回報供覆核）

| 項 | 本批落實 |
|---|---|
| D 欄（`req_id`） | `Sys-RA-VF665_V43_VSM-{nnn}` 實名，**15/15** |
| Remarks | 逐列以 `Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1)` 起首，**15/15** |
| **spec_reference 雙錨** | **spec 錨在前、Sys-RA 錨在後，15/15**；本批 `spec_section` 全為 `1.11.1.1.6`（`segment_map`，Δ0 區） |
| **所用前綴（逐字）** | `Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4` |
| 首列樣本 | `Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6` ⏎ `Sys-RA-VF665_V43_VSM-453` |

> **⚠ 前綴與實際檔名不逐字相同，請覆核（§六 K-16）**：
> 實際檔名 stem 為 `Vehicle_Setup_Management_by_VP_-_LTM_(R1L)_with_TBM_VF665_V43_R4`。
> 12 包 §一給定之字串為 `Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4`
> （`VP_-_LTM` → `VP-LTM`、去括號、`with_TBM` → `TBM`）。
> **本包依下放包所給之字串逐字使用**（IN §10.7(b) 禁同檔名拼寫變體，全案須一致，
> 故不由執行層自行改寫）；若應改以實際檔名 token 化，請一次裁定，本批 15 列一併改。

## 二、本批母體與規格節

母體：v2 之 `test_set = Forward Collision Warning` 且 `status = active`，**15 列**
（`chapter_for_vf = 01.11.01.01.06`，`spec_section = 1.11.1.1.6`，含解得 12）。
規格節 `1.11.1.1.6`（para 578–629）已切出為行為佐證；**test_item 上半仍取 SYSRA `Description` 逐字**（E56 15/15）。

規格節之結構（供覆核切分依據）：

| 規格段 | 內容 | 對應 leaf |
|---|---|---|
| 579–580 | `Forward_Collision_Mitigation` PROXI → 顯示兩個選單項 | `-453` |
| 583–586 | `Country_Code` ∈ NAFTA/LATAM → Setting1，選項 `Off, Audio, Audio_Brake` | `-455` |
| 588–595 | 三個選項之送出 | `-456`／`-457`／`-458` |
| 597–598 | 收訊 → 顯示更新 | `-459` |
| 600–603 | `Country_Code` ∉ NAFTA/LATAM → Setting2，選項 `Off, Brake, Audio_Brake` | `-460` |
| 605–612 | 三個選項之送出 | `-461`／`-462`／`-463` |
| 614–615 | 收訊 → 顯示更新 | `-464` |
| 617–625 | Sensitivity `Near`／`Med`／`Far` 之送出 | `-466`／`-467`／`-468` |
| 627–628 | 收訊 → 顯示更新 | `-469` |

**15 leaf 一對一對映，無未對映者。**

## 三、產出（`generated/b2_fcw/`）

15 × `.json` ＋ 15 × `.md` ＋ `INDEX.md`（共 **31** 檔）。**一 leaf 一 TC，TC 總數 15。**

| req_id | tc_title | design_method |
|---|---|---|
| `-453` | FCW setting and sensitivity menus shown when mitigation configured | 決策表 |
| `-455` | FCW Setting1 offers three options in NAFTA and LATAM markets | 決策表 |
| `-456`／`-457`／`-458` | FCW Setting1 request sent for off／audio／audio brake selection | 等價劃分 |
| `-459` | FCW Setting1 display updated on reception of setting message | 功能測試 |
| `-460` | FCW Setting2 offers three options outside NAFTA and LATAM markets | 決策表 |
| `-461`／`-462`／`-463` | FCW Setting2 request sent for off／brake／audio brake selection | 等價劃分 |
| `-464` | FCW Setting2 display updated on reception of setting message | 功能測試 |
| `-466`／`-468` | FCW sensitivity request sent for near／far selection | **邊界值分析**（值域兩端） |
| `-467` | FCW sensitivity request sent for med selection | 等價劃分 |
| `-469` | FCW sensitivity display updated on reception of activation mode message | 功能測試 |

**Priority 全批 `P1`**（高於 b1 之 `P2`）：本組設定直接組態一個 ADAS 安全功能之告警／制動行為
（IN §10.2「Major user-facing functionality or key operational logic flow」）；
未用 `P0` —— 本批驗的是 HMI 設定與其 CAN 請求訊號，非制動控制本身。

**訊號寫法**：`$TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req$`／`$…FSFCWPlusActivationMode_Req$`／
`$IPC_VEHICLE_SETUP2.FSFCWPlusSetting$`／`$…FSFCWPlusActivationMode$` 四名皆 v5「解得」；
`<label>` 逐字取 `val_tables_v43.tsv`（`0=Off｜1=Audio｜2=Brake｜3=Audio_Brake｜4=Not_Request`；
`0=Near｜1=Med｜2=Far`）。**無 VAL_ 缺值。**

## 四、PENDING —— 本批 **0**，但**逐一實測**（不沿用 b1 結論，R-VT20(d)）

| 內部訊號 | v5 | **本批實測之 UI 面** | 判 |
|---|---|---|---|
| `FSCWPlus_Setting.Req` | 未解得(止於段1) | 規格 **para 584／601** 逐字具名 `" Forward Collision Warning Setting1"`／`" … Setting2"` 選單項，且 para 586／603 逐字載其選項集合 | **可走 UI 路徑**（R-P375(b)／R-VL21(a)） |
| `FSCWPlus_Activation_Mode_Setting.Req` | 未解得(止於段1) | 規格 **para 580／617** 具名 `"Forward Collision Warning Sensitivity"`；**另有 HMI Settings List `Settings` r9／r255 `"Forward Collision Sensitivity*"`，Technical Reference `VF230/665`，選項 `Near , Med, Far` 與規格逐字相符** | **可走 UI 路徑，且有 HMI 錨** |
| `TLM_Vehicle_Setup_Menu.Info` | 未解得(止於段1) | 規格 **para 598／615／628** 同句載「updates the … information **on its display**」，效果面即具名選單項 | **ER 觀察具名選單項**（R-P353 白名單 (ii)） |

> **三者各自查證，未引用 b1 之任何結論。** 本批同樣得 0 PENDING，
> 但那是本組恰好三個內部訊號都有規格具名面之結果 —— **仍不得推廣至其餘 15 組**。

## 五、K-14 新法順做（E87，R-VT25(c)）

### 方法（純字面）

1. 自 `1.14.1`（Configuration Parameters Table，para 1289–1775）解析 **ID ↔ 參數名**：
   該表在 docx 中**逐格一段**，每列 **11 格**（`ID｜Parameter Name｜First Trial Value｜Range Value｜
   Resolution｜Unit｜Component｜Implementation｜XCP Availability｜Impact｜Parameter Description`），
   以 11 為步長解析 → **38 對**。
2. 每個 SYSRA 組 `01.14.02.01.NN` 之 `Description` 以**詞界逐字**比對，取出其參數名。
3. 對每個 `1.14.2.1.M`（標題 `ID n Description`）節，以 `id2name[n]` 之參數名**逐字**查該節內文；
   命中且唯一者即對應。

### 結果

| 判 | 組數 | 列數 |
|---|---|---|
| **唯一命中** | **21** | **22** |
| 無命中 | 8 | 8 |
| 多重命中 | 0 | 0 |

**回填 `spec_section` 22 列**，`spec_section_source = k14_param_match`。
v2 之來源分布：`segment_map` **195**／`direct` **42**／**`k14_param_match` 22**／`none` **77**（原 99）。

> **對映非序位** —— 例如 `01.14.02.01.14` → `1.14.2.1.12`、`.20` → `.18`、`.29` → `.27`。
> **這確證 11 包判「序位假說不成立」是對的**，而參數名逐字比對才是可判之法。

### 8 組無命中之逐組歸因（全部可解釋，非方法失效）

| chapter | SYSRA 之參數寫法 | 表內之寫法 | 成因 |
|---|---|---|---|
| `.02` | `Odo_Units Change` | `Odo_Units_Change` | **空格 vs 底線** |
| `.10` | `DRL_Menù_Enable` | `DRL_Menu_Enable` | **重音 `ù`** |
| `.11` | `Greeting_Lights_Menù` | `Greeting_Lights_Menu` | **重音 `ù`** |
| `.15` | `Remote_Door_Unlock _Menu` | `Remote_Door_Unlock_Menu` | **多一空格** |
| `.16` | `Sound_Horn_Remote_Start _Menu` | `Sound_Horn_Remote_Start_Menu` | **多一空格** |
| `.17` | `Horn_Chirp_Menù` ＋ `Model_Year` | `Horn_Chirp_Menu` | 重音 ＋ **`Model_Year` 已由 R4 刪除**，規格無其 ID Description 節 |
| `.12` | `CAN node 51 (LBSS)` | — | **R4 已刪 ID14**（K-13，該列狀態 `stale_ref_r4`），規格無對應節 |
| `.13` | `CAN node 52 (RBSS)` | — | **R4 已刪 ID15**（同上） |

> **`.12`／`.13`／`.17` 之無命中與 K-10／K-13 之刪除清單完全一致 —— 兩項獨立量測互證。**
> **`.02`／`.10`／`.11`／`.15`／`.16` 五組為上游拼法變體**（重音／空格），
> 即 DR-VT2 已載之同一問題，**新增 5 筆逐字佐證**。
> **本包維持逐字比對，未套用 R-VT13(e) 之第六規則（去重音）** ——
> 該規則係為「段 1 擴充比對」而裁，而 R-VT25(c) 令 K-14 新法為「逐字」；
> 跨情境套用屬擴張，列 §六 K-17 交裁（若准，`.10`／`.11`／`.17` 三組可再補）。

## 六、§K

| # | 項 | 待裁 |
|---|---|---|
| **K-16**（新） | **spec 錨前綴與實際檔名不逐字相同**（見 §一）。本批 15 列已依下放包所給字串寫入 | 確認前綴；若改以實際檔名 token 化，本批 15 列一併改（全案一致性，IN §10.7(b)） |
| **K-17**（新） | K-14 之 5 組因**拼法變體**（重音 ×3／空格 ×2）無命中 | 是否准第六規則（去重音）與新增「空白正規化」規則用於 K-14 比對？現行為逐字，未套用 |
| K-15 | 占比兩數並列已入 R-VT25(b) | 已裁，交付說明時採用 |

## 七、anomaly／DR

**本包無新登 anomaly。**

| DR | 狀態 | 本包新增佐證 |
|---|---|---|
| DR-VT1 | 裁送出，待發 | — |
| DR-VT2 | 建議併送 | **規格拼字 `Forward Collision Warinig`**（para 580，b1 之 test_item 逐字保留）；**K-14 之 5 組拼法變體**（`Odo_Units Change`／`DRL_Menù_Enable`／`Greeting_Lights_Menù`／`Remote_Door_Unlock _Menu`／`Sound_Horn_Remote_Start _Menu`） |
| DR-VT3／DR-VT4 | 暫持／先不送 | 本批 0 PENDING，DR-VT4 之缺口不變 |

---

## 八、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 510
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **510**（與上繳 11 同）。將 `framework.md` 還原至 `HEAD`、`generated/b2_fcw/` 31 檔與本檔移出樹外後重跑**仍為 510** |
| `rulings_hash` | **相關，為預期狀態** | R-VT11–R-VT25 十五條未入台帳；重生歸 Pei 提交前一次 |
| `gates_tsv`／`lint_paths` | **無關** | 紅列全屬他 feature |

---

## 九、獨立判斷

1. **K-16 應該在 b2-2 開跑前裁掉，因為它是全案一致性問題。**
   前綴一旦分歧，往後每一批都會帶著同一個字串，改起來是全批重寫。
   本批 15 列改起來便宜，300 列就不便宜了。

2. **K-14 的 21/29 是好結果，但真正有價值的是那 8 個無命中。**
   其中 3 個（`.12`／`.13`／`.17`）與 K-10／K-13 的刪除清單完全對上 ——
   **兩個獨立方法在同一批列上互證**，這比命中率本身更能說明資料狀態。
   另 5 個是拼法變體，又替 DR-VT2 補了 5 筆逐字佐證。

3. **本批 0 PENDING 是第二次，我還是要說一次「不能推廣」。**
   FCW 的三個內部訊號都有規格具名面，是這一節寫得詳細（連選項集合都逐字列出）。
   Clock and Time（16% 解得）那種組不會這麼幸運。**每組仍須逐一實測。**

4. **`-456`／`-461` 與 `-459`／`-464` 兩對之 `Description` 逐字相同，但不是重複。**
   前者在 Setting1（NAFTA/LATAM）脈絡、後者在 Setting2 脈絡，Pre-Condition 之 `Country_Code` 分支不同，
   故未用 `duplicate_of`（IN §10.6 要求 trigger／outcome／input／verification target 四者全同）。
   **`distinguishing_axis` 逐條標明市場分支**，覆核時請一併確認此判斷。

5. **本包未驗而下放包亦未要求者**：
   (a) HMI Settings List 之 `Forward Collision Warning*` 列（r251）選項為
       `Off/ Only Active Braking/Warn+Active Braking`，**與規格之 `Off, Audio, Audio_Brake` 不逐字相符** ——
       本批 UI 名取規格（IN §8.6 source spec wins），未採 HMI 清單之選項；該差異未上問；
   (b) `Not_Request`（VAL_ 之 raw 4）於規格未出現，本批未生成其 TC（§8.4.2 不擴範圍）；
   (c) 規格 para 581「Forward Collision Warning Setting」為一個無編號之小標，
       其與 `1.11.1.1.6` 之階層關係未查（非標題樣式），本批未據以切分。

---

## 十、禁區遵守聲明

| 禁區 | 遵守 |
|---|---|
| 00 包 §零 1／2／3／4／6 | git 未動；未寫 `vehicle_setting`／`vsm_v42`；未寫 profiles；`sources/raw/` 唯讀；未代發 DR |
| 12 包 對象限制 | **未寫工作簿**；**已凍 b1 一位元未動**；未寫 `delivered/`；未開 `sandbox/base/` |
| V42 05 包 §零 | 未生成本批以外之 TC；工作簿欄位全 English、`reasoning` 繁中；語意不明處未補洞（列 §六） |

本包寫入之檔：
`generated/b2_fcw/`（31 檔，新）、`data/leaves_interim_v2.tsv`（回填 22 列之 `spec_section`）、
`data/section_map_114_v43.tsv`（改為 K-14 新法之結果）、`framework.md`（標籤一行）、
`docs/upstream/12_b2_fcw.md`（新）。
`generated/b1_ambient/`、`RULINGS.md`、`DATA_REQUESTS.md`、`ANOMALIES.md`、`DECISIONS.md` **未動**。

---

## 十一、下一步

1. **Pei／分析層裁 K-16（前綴）** —— 建議在 b2-2 開跑前，避免全案分歧
2. K-17（K-14 是否放寬至去重音／空白正規化）
3. **b2-2 = Side Distance Warning 10 leaf**（R-VT25(d) 批次序第二）
4. 綠色通道：本批為第一批；三批零修訂後啟用（R-VT25(d)）
5. Pei：發送 DR-VT1（併 DR-VT2，本包新增 6 筆拼字佐證）；台帳重生（R-VT11–R-VT25 十五條）
