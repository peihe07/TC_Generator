# 上繳包 02 — vsm_v43：W-5′ 訊號解析重做、§K 收斂、P3 前置

日期：2026-09-01　執行層　對應下放包：`docs/handoff/02_signal_redo.md`
本包 sha8 一律報 **`body_sha8`**（R-VT10(a)）；`sha8` 併列為觀測值。
sha 來源：`rulings_hash.py --out <scratchpad 樹外>`（台帳仍無 R-VT 列，R-VT10(a) 裁可）。

---

## 〇、一句話結論

**W-5′ 六項全數執行，兩處停下條款皆解除，§K 空。**
**新登兩項執行層自誤（A-VT15 抽取正則、A-VT17 母體基準），一項觀測（A-VT16）。**

| 前包之停 | 本包 |
|---|---|
| 停 1（E10 R-VT2 `sha8` 異） | **解除** —— E10′ 改比 `body_sha8`，R-VT1–R-VT8 **8/8 相同** |
| 停 2（E15 B-1 = 29） | **解除** —— 依 R-VT9 重分類後 **B-1 = 0**，§K 空 |

**本包新觸之升級條件：無。** E16 於兩種基準下一符一不符，已並列不調和（A-VT17）。

## 一、結果三分法（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | W-5′ 六項；`RECON.md` §7 全面更新；A-VT10／A-VT11／A-VT12 轉 RESOLVED；**上繳 01 之 docx 抽取正則缺陷（A-VT15）** |
| 核實無誤 | E10′ 8/8、E15′ 0、E17 解得、E18 49、E9′ 56；型態一之 22 列與型態二之 6 列合計 **28**，與上繳 01 之 28 逐列相同 |
| 正確地不動 | 舊 `signal_chain_v43.tsv` **不覆寫**（02 包明令，另存 v2）；`查無(R-G13)` 標籤**全面撤除**而非改判（R-VT10(c)）；擴充比對**只實作 02 包所列四規則**，`.` 分隔之變體只量測不採用（02 包 §七）；V42 側**只讀** `signal_chain_v42.tsv`，不存在即記「待 vsm_v42」；A-VT16 依 R-VT9(b) 照辦不自行改判 |

---

## 二、W-5′ 逐項

### 1. 抽名（三式 ＋ `<w:tbl>` 表格結構）

| 階段 | 相異名數 |
|---|---|
| 三式（上繳 01 之抽取式） | 181 |
| **三式（修正抽取正則後）** | **179**（－2，見 A-VT15） |
| ＋ 引號式 PROXI | 219（＋40） |
| ＋ `<w:tbl>` 表格結構 | **230**（＋11） |

類別：**CAN 93／內部 88／PROXI 49**（上繳 01 為 92／87／2）。

**引號式 PROXI 之必要性（揭露）**：規格之 PROXI 參數幾乎一律寫作
`"Cornering_Lights" PROXI parameter is equal to "present"` —— **帶引號**。
上繳 01 之式 `([A-Za-z][A-Za-z0-9_]*)\s+PROXI parameter` 要求引號前為裸識別字，故只得 2 名。
本包加入 `["“”]([^"“”]{2,60})["“”]\s*(?:PROXI|proxi)\s+parameters?` 一式。
**這不是新的比對規則**（02 包 §七所限者為**段 1 擴充比對規則**），
而是修補上繳 01 §十-2 自報之抽名缺陷；仍據實揭露。

**表格結構（02 包 W-5′ 第 1 項所令）之實際貢獻**：`<w:tbl>` 共 557 個儲存格，
新增 **11** 名。本規格之參數主要不在表格而在條件句中，故表格路徑貢獻有限 ——
**照令實作並如實回報其效益**，不因效益低而略過。

**上游拼法不一（實測，供 R-P369(b) 型處置）**：
`Cornering_Light`／`Cornering_Lights`、`Horn_Chirp_Menu`／`Horn_Chirp_Menù`、
`Odo_Units Change`／`Odo_Units_Change`、`Remote_Door_Unlock _Menu`（多一空格）／`Remote_Door_Unlock_Menu`、
`Sound_Horn_Remote_Start _Menu`（多一空格）。**二拼法皆入段 1 查**（R-P369(b)），皆未解得。
另 `CAN Node 35 (TBM)`／`CAN node 24 (PAM)` 二名為句式偽陽性，留於 TSV 並於此標明。

### 2. 段 1 —— 逐字 ＋ R-P368(b) 擴充比對

**擴充比對規則（02 包 §三第 2 項所列四條，逐條實作，未增未減）：**

| 規則 | 實作 |
|---|---|
| 去 `MESSAGE.` 前綴 | 若含 `.` 且點前段全等 `^[A-Z][A-Z0-9_]*$`（全大寫／數字／底線）則取點後段 |
| 去 `_Req`／`_Sts`／`_Info` 後綴 | 不分大小寫，反覆去除至無 |
| 底線 ↔ 空白 | `[_\s]+` → 單一空白 |
| 大小寫不敏感 | 全轉小寫 |

比對對象：**LID 全分頁之 `Logical Identifier` 欄**（14 分頁，逐分頁定位表頭列與該欄，
共 **3382** 結構化列 → 3043 個相異正規化鍵）。
每一擴充命中另欄 `段1擴充命中(前3)` 記 `LID/{分頁}/r{列}c{欄}(擴充鍵:{鍵})`（R-P368(b)）。

> **⚠ 規則所指之 `Description` 欄在 LID 中不存在（回報，未自創替代）**
> 02 包第 2 項與 R-P368(b) 皆令比對 LID 之 `Logical Identifier`／**`Description`** 兩欄。
> 實測 LID 之三類分頁表頭為
> `Logical Identifier | Function | Object Text | Arch Basis | Transfer Function | Signal Name | CAN | Format | SNA | VFs`
> （`Specific Signals` 類為 `Function | Logical Identifier | Object Text | Signal Name | CAN | …`），
> **無任何名為 `Description` 之欄**（`Description` 只出現在 `Rev History` 分頁之版本說明）。
> 語意最近者為 `Function` 與 `Object Text`。
> 依 02 包 §七「新規則不得自創，回報」，**本包只比對 `Logical Identifier` 欄**，
> 未擅自代入 `Function`／`Object Text`。**提請裁決**：是否將該二欄納入擴充比對之對象。

**七檔各命中數（重報）**

| # | 檔（`forms/`） | 段別 | 上繳 01 | **本包** |
|---|---|---|---|---|
| 1 | `Logical Identifiers and CAN Mapping v1_78.xlsx`（逐字，全分頁） | 段 1 | 23 | **31** |
| 1′ | 同上（**R-P368(b) 擴充**，`Logical Identifier` 欄） | 段 1 | — | **24** |
| 2 | `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | 段 1 | 0 | **0** |
| 3 | `PROXI_HDCC27_R3_20250424.xlsx` | 段 1 | 2 | **35** |
| 4 | `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` | 段 1 | 0 | **1** |
| 5 | `SR24 R1 Market Configuration Table v1.6.xlsx` | 段 1 | 0 | **0** |
| 6 | `PDT27_E2A_R1_BHCAN2.dbc`（`SG_` 相異 342） | 段 3 | 4 | **4** |
| 7 | `PDT27_E2A_R1_FDCAN8.dbc`（`SG_` 相異 1634） | 段 3 | 69 | **69** |

**擴充比對之實效與其界線（重要）**：24 個擴充命中中，**內部訊號（`.Req`／`.Info`／`.GUI`）佔 0 個**。
原因是 LID 之 `Logical Identifier` 欄收的是 `ConsumptionUnit` 一類的裸識別字，
而規格之內部訊號寫作 `Consumption_Unit_Setting.Req`；四條規則中**沒有一條處理 `.` 分隔符**，
故 `X.Req` 之 `.Req` 無法被「去 `_Req` 後綴」一條吃掉。
**量測（不採用，僅回報）**：另以「`.` 亦視為分隔符」之變體重跑，
**僅多命中 1 名**（`PrivacyMode.Info` → 解得）。
即：即使放寬該點，內部訊號之解析率也不會顯著改善 ——
**瓶頸不在正規化規則，在 LID 本身不收內部訊號名**。
故 §四之建議不是「放寬規則」，是「內部訊號改走 R-P375(b)(c) 之 UI／PROXI 路徑或另索對照表」。

### 3. 結果值域與分布（新值域取代 01 包）

| 結果 | 本包（母體 230） | 上繳 01（母體 181） |
|---|---|---|
| 解得 | **41** | 40 |
| 訊息名不符(R-13) | **28** | —（原記 B-1 衝突 29 之 28 列） |
| **B-1 衝突** | **0** | 29 |
| 未解得(止於段2) | **13** | 8 |
| 未解得(止於段1) | **113** | —（原記 `查無(R-G13)` 102） |
| UI路徑(R-P375b) | **0** | — |
| PROXI路徑(R-P375b/c) | **35** | 2 |
| 查無(R-G13) | **0** | 102 |
| 合計 | **230** | 181 |

**`查無(R-G13)` 歸零之理由**：R-VT10(c) —— 三要件（段 1 擴充比對已做、段 3 實查、
已登 `forms/LOOKUP_MISSES.md`）須全滿足方得用。本包**未登** `LOOKUP_MISSES.md`
（該檔為全域共用件，且尚有 §四之未竟項），故一律記「未解得(止於段1)」。
**`forms/LOOKUP_MISSES.md` 本包未寫入。**

**同母體對照（181 名 ∩ 本包）**

| 結果 | v1 | v2 |
|---|---|---|
| 解得 | 40 | **41** |
| 訊息名不符(R-13) | —（B-1 29 之 28） | **28** |
| B-1 衝突 | 29 | **0** |
| 未解得(止於段2) | 8 | **13** |
| 未解得(止於段1)／查無 | 102 | **97** |
| PROXI路徑 | 2 | **2** |

`未解得(止於段1)` 113 之類別拆解：**內部 83／CAN 16／PROXI 14**。

### 4. 型態三 `BRAKE1.VehicleSpeedVSOSig`（R-VT9(b)）

實測 LID `CAN Mapping` **r2321**：`Logical Identifier` = `VehicleSpeedVSOSig`、
`Arch Basis` = `Atl High`、`Atlantis High` 欄組之 `Signal Name` = `BRAKE_FD_2.VehicleSpeedVSOSig`、
**`CAN` 欄 = `FD`**。
依 R-VT9(b)：LID 載明匯流排 → 取 **FDCAN8**（`BRAKE_FD_2.VehicleSpeedVSOSig`），
`BHCAN2:STATUS_CCAN3` 記**旁證**，結果 **「解得」**。**§K 空，不升級。**
規格訊息名 `BRAKE1` 與段 3 之 `BRAKE_FD_2` 不同，`test_item` 上半依 R-13／R-6 保留原文。

> **觀測（A-VT16，不改判）**：`STATUS_CCAN3.VehicleSpeedVSOSig` **本身亦為本規格之另一個
> 規格原名**（文字層第 339 行；功能圖中 VF408→BCM 標 `BRAKE1.*`、BCM→LTM 標 `STATUS_CCAN3.*`），
> 且其自身亦判為「解得」。把 `BHCAN2:STATUS_CCAN3` 記為 `BRAKE1.*` 之旁證，
> 可能把兩條獨立弧線併為一物。**本包依 R-VT9(b) 照辦**，僅登記觀測並提請加但書。

### 5. 兩版並存

`data/signal_chain_v43.tsv`（v1，181 列）**未覆寫**；
`data/signal_chain_v43_v2.tsv`（v2，230 列）新增。
v2 欄位：`規格原名 | 類別 | 抽名來源 | 段1命中檔 | 段1逐字命中(前3) | 段1擴充命中(前3) |
段2 | 段3 | 結果 | 備註 | variantB才命中`。
兩版差集：v1 ⊂ v2（**僅 v1 者 0 名**，v2 多 49 名）。

### 6. V42 ↔ V43 訊號名差集

**「待 vsm_v42 W-5」。** 實測 `features/vsm_v42/data/` 仍為**空目錄**，
`signal_chain_v42.tsv` 不存在。依 02 包明令**只讀該檔**，本包不產出差集，
**未讀 V42 之規格 docx**（該檔實體確在 `features/vsm_v42/inputs/`）。

---

## 三、E 對照（相符者亦列，不符不調和）

| # | 項 | 判準／預期 | 實測 | 判 |
|---|---|---|---|---|
| E10′ | R-VT1–R-VT8 `body_sha8` 與前包逐字相同 | 全同 | R-VT1 `93666dae`／VT2 `a6acf352`／VT3 `d3823bca`／VT4 `9844b823`／VT5 `e8e8724b`／VT6 `8db4c81b`／VT7 `9b4427c5`／VT8 `2b3fcbe6` —— **8/8 相同** | ✅ 相符 |
| E15′ | B-1 衝突列 = 0 | 0 | **0** | ✅ 相符 |
| — | 「訊息名不符(R-13)」（觀測值，01 對應 28） | 觀測 | **28**（逐列與上繳 01 之型態一 22 ＋型態二 6 相同） | ✅ 一致 |
| E16 | 擴充比對後「未解得(止於段1)」< 102 | < 102 | **同母體 97**／**全母體 113** | ⚠ **一符一不符**（A-VT17） |
| E17 | 型態三處置 | LID `CAN` 有載 → 解得 | LID r2321 `CAN` = `FD` → **解得**，§K 空 | ✅ 相符 |
| E18 | 表格抽取後 PROXI 名 > 2 | > 2 | **49** | ✅ 相符 |
| E9′ | Verification Method 非空相異值（Functional 507，正規化） | 56 | **56**（`verified by in-vehicle testing` 47） | ✅ 相符 |

**E16 之兩基準（並列，不擇一）**：102 係自上繳 01 之 **181 名**母體算出；
本包依 R-VT10(d) 擴充抽名至 **230**，母體已變。
- 同母體（181 名 ∩ 本包）：**97 < 102 → 相符**，即擴充比對確有實效（－5）
- 全母體（230 名）：**113 ≥ 102 → 不符**；差額 16 列**全部**來自新抽得之 49 名
比率式：97/181 = 53.6% → 113/230 = 49.1%。**不調和，交裁**（A-VT17）。

### R-VT9／R-VT10 之 `body_sha8`

| 條號 | 一句話 | `body_sha8` | `sha8`（觀測） | 來源：列 | 本體列數 |
|---|---|---|---|---|---|
| R-VT9 | B-1 定義收斂；訊息名不符依 R-13；兩本各解一處者先查 LID 匯流排 | **`0f1a1f3f`** | `69c1af47` | `features/vsm_v43/RULINGS.md`:122 | 12 |
| R-VT10 | 條文身分比 body_sha8；E2／E9 判準修正；W-5 標籤與重做條件 | **`fa2558ff`** | `c692ea33` | 同上:137 | 15 |

---

## 四、§K —— B-1 衝突表

**空。** 依 R-VT9 重判後 B-1 = 0：
- 型態一 22 列 ＋ 型態二 6 列 = **28 列** → 「訊息名不符(R-13)」，保留規格原名，段 3 記旁證，上游查詢由 **DR-VT3** 承載
- 型態三 1 列 → LID `CAN Mapping` r2321 載 `FD` → 解得（見 §二-4）

**本表空非因未查**：29 列逐列走過 R-VT9(a)(b) 之判準，分類依據逐列記於
`data/signal_chain_v43_v2.tsv` 之「結果」與「備註」兩欄。

---

## 五、P3 前置（三項，不鎖、不寫 profile）

### 1. `RECON.md` §7 未決表已更新

B-1 依 R-VT9 重分類（0）、E9 基線 56、`查無(R-G13)` 標籤撤除、
訊號母體 181 → 230、LID 欄組適用性一題因 R-VT6(a) 而消滅、WMF 已轉圖。

### 2. 分母 295 列之 `chapter_for_vf` 前二階分布（供 Layer 2 對照，**非依據**）

| 前二階 | 列數 |
|---|---|
| `01.11` | **223** |
| `01.14` | **67** |
| `01.13` | **5** |
| 合計 | **295** |

第一階恆為 `01`（295/295），無鑑別力。
**此分布僅供對照，不得作為 Layer 2 之依據**（R-VT4：Layer 2 待 037 家族聚合）。

### 3. `word/media/image1.wmf` → `data/spec_r4_image1.png`

轉檔以 `soffice --headless --convert-to png`（`sips` 與 `magick` 對 WMF 皆失敗，
後者之 delegate 亦指向 libreoffice）。輸出 794×1123 px，143 KB。

**一句話內容**：R4 之**功能圖** —— 以 `LTM` 為中心節點，左側列 `IPC_VEHICLE_SETUP*`／
`BRAKE1.*` 之入向 CAN 訊號與 `TLM_Display.GUI`、上方列 `*.Req` 內部訊號、
右側列 `TELEMATIC_VEHICLE_SETUP*` 之出向訊號與各 VF 節點（VF747／VF800／VF456／VF230／
VF176／VF155／VF608／VF408），下方為 `BCM` 與 `TBM` 兩節點及 `SERVICE_SETUP.*`／
`TELEMATIC_SERVICE_SETUP.*` 之往返弧線。

**抽樣核對（圖 ↔ 文字層）**：圖中之 `STATUS_CCAN3.VehicleSpeedVSOSig`、`BRAKE1.VehicleSpeedVSOSig`、
`IPC_VEHICLE_SETUP2`、`TLM_Display.GUI` 於文字層命中數分別為 3／2／43／2 ——
**本圖之訊號名未見有僅存在於圖中者**（與 sw_update 之 CFTS 嵌入圖不同）。
依 R-VT10(e)，**不施作 R-G28 二欄表**。

---

## 六、anomaly／DR 清單

### 狀態變更（本包）

| id | 變更 | 依據 |
|---|---|---|
| A-VT10 | PENDING → **RESOLVED** | R-VT10(b)：「Functional」＝ `Functional Requirement`，計數 507 相符 |
| A-VT11 | PENDING → **RESOLVED** | R-VT10(b)：基線 56；E9′ 複測 56 |
| A-VT12 | PENDING → **RESOLVED** | R-VT9：28 列轉 R-13（DR-VT3）、1 列經 LID 解得，B-1 = 0 |
| A-VT13 | **維持 PENDING** | 台帳仍無 R-VT／R-VL 列；vsm_v42 之 W-0 未完成 |

### 本包新登

| id | 一句話 | 狀態 | 配對 DR |
|---|---|---|---|
| A-VT15 | **執行層之誤**：`<w:t[^>]*>` 誤配 `<w:tc>`／`<w:tcPr>`／`<w:tbl>`，上繳 01 之抽取文字含 451 處字面 XML，致 2 個假名 | RESOLVED（已修正） | — |
| A-VT16 | `VehicleSpeedVSOSig` 之兩條規格弧線疑被 R-VT9(b) 合併為一 | PENDING | — （條文但書之爭點，非上游） |
| A-VT17 | E16 之母體於 W-5′ 後由 181 變 230，兩基準一符一不符 | PENDING | — （判準基準，非上游） |

**A-VT15 之自評**：這是本執行層的錯，且**在上繳 01 全程未被任何 gate 攔下** ——
抽取端無自驗，而 gate 不看抽取品質。是 02 包重跑時肉眼看見字面標記才發現。
建議凡以正則讀 OOXML 者，抽完即斷言「輸出不含 `</?w:`」，一行即可（FO 之第 8.3 節第二層之同型防護）。

### 未結 DR（本包未動 `DATA_REQUESTS.md`，未送）

| DR | 項目 | 阻塞 | 狀態 | 本包新增之佐證 |
|---|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 建議送出 | 差集仍待 vsm_v42 |
| DR-VT2 | SYSRA DocID `VF655`／R3 vs R4／Melco ID 全空／二拼法 | no | 未送出 | PROXI 參數名亦見五組拼法不一（§二-1） |
| DR-VT3 | 規格訊息名與 forms/ DBC 不符 28 列 | no | 建議送出 | 28 列逐列依據見 v2 TSV「備註」欄；A-VT16 之但書問題宜併問 |

---

## 七、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 502
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 將本包新增之 `docs/upstream/02_signal_redo.md` 移出樹外重跑，計數不變 |
| `rulings_hash` | **相關** | 台帳缺 `R-VL1–5` ＋ `R-VT1–10` 共 **15** 列（前包 13，本包 R-VT9／R-VT10 再 +2）。**本線不重生**（R-VT8(a)），待 vsm_v42 之 W-0（A-VT13） |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`／`driver_distraction`／`ics_management`／`lint_docs036`，無 vsm_v43 之列 |
| `lint_paths` | **無關** | 四筆紅全在 `driver_distraction/workbook/`（2）、`ics_management/delivered/`（1）、`sw_update/delivered/`（1）。**本包新增之 `data/spec_r4_image1.png` 未判紅** |

依 FO 之第 8.2 節／26 包 §C 裁定 2：**本包附本節之升級說明上繳**。

---

## 八、獨立判斷（「本包是否仍有該驗而未驗者」）

1. **有：內部訊號 88 名之解析仍幾近全滅（83 止於段 1），而本包已證明放寬正規化規則救不了它。**
   擴充比對 24 個命中中內部訊號 **0** 個；`.` 分隔變體只多 1 名。
   根因是 **LID `Logical Identifier` 欄不收 `X.Req` 形之內部訊號名**，
   段 1 之七檔裡也沒有任何一本是「內部訊號 ↔ 可觀察面」的對照表。
   PM 線是靠 **DR-PW23 之內部訊號對照總表**（R-P355(a)）解決同一問題的。
   **本線缺一份等價物** —— 建議 P3 前開 `DR-VT4`（V43 內部訊號之驅動與觀察方法），
   形制照 DR-PW23。本包**未開**（禁區 §零-6，且開 DR 屬分析層草擬）。

2. **`HMI Settings List` 命中 0，是本包最可疑的一個數字。**
   R-P375(b) 之 UI 路徑整條沒有被行使過（`UI路徑(R-P375b)` = 0 列）。
   PM 線上 `.Req` 類設定值大量命中該檔。本線 49 個 PROXI 名裡有
   `Auto_Close_Menu`、`Passive_Entry_Menu`、`Tyre_Pressure_Unit_Menu` 等**明顯是 HMI 設定項**者，
   卻一個都沒在 HMI Settings List 命中。二解：(a) 該檔之命名體系與本 VF 不同；
   (b) 我的比對只做逐字＋LID 擴充，**未對 HMI Settings List 做任何擴充比對**
   （02 包第 2 項只令對 LID 做）。**後者更可能，且是我照令的結果。**
   建議下包令：擴充比對之對象自 LID 擴及 HMI Settings List 與 PROXI `Format`。

3. **`Description` 欄不存在一事，可能同時影響 PM 線。**
   R-P368(b) 明文寫「LID 之 `Logical Identifier` 欄與 `Description` 欄」，
   而 LID v1_78 之三類分頁都沒有 `Description` 欄（最近者為 `Function`／`Object Text`）。
   若 PM 線曾依該條做過擴充比對，其「已比對 Description 欄」之記載值得回頭核對。
   **本包只回報，不去動 PM 線之任何檔。**

4. **E16 這類「跨包沿用絕對閾值」的預期數字，在母體會變的項目上不穩。**
   02 包同時令「擴充抽名（181 為下界）」與「< 102」，二者互相衝突。
   建議此類指標一律以**同母體差**或**比率**表述（FO 之第 8.6 節第 3 條
   「不沿用前輪數字，累計量每輪自總量重算」之同一精神）。

5. **本包未驗而下放包亦未要求者**：
   (a) `Object Text` 欄之比對（見 §二-2 之回報）；
   (b) SYSAD 仍**完全未讀**（連續三包如此）；
   (c) SYSRA 之 `Polarion`／`_polarion` 兩分頁仍未計數；
   (d) `forms/LOOKUP_MISSES.md` 未寫入（R-VT10(c) 之三要件未滿足，故本應不寫 —— 記明以免誤為漏做）。

---

## 九、禁區遵守聲明（00 包 §零）

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 本包未跑任何 `git` 寫入指令 |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫。`vsm_v42` 僅 `ls data/`（實測空）。**未讀其規格 docx** |
| 3. 不寫 `docs/runtime/profiles/` | 未寫 |
| 4. 不改寫 `sources/raw/` 原檔 | 未寫；本包對 `sources/` 全程唯讀 |
| 5. 不以 SYSRA 或規格代 037 建母體或生成 TC | 未建、未生成。`generated/`／`batches/` 仍空；v2 TSV 為訊號預查，非 leaf 母體 |
| 6. 不自行送 DR | 未送、未改 `DATA_REQUESTS.md`。§八-1 之 `DR-VT4` 僅為建議，未登記 |

本包寫入之檔（全在 `features/vsm_v43/` 之下）：
`ANOMALIES.md`（改）、`RECON.md`（改 §7）、`data/signal_chain_v43_v2.tsv`（新）、
`data/spec_r4_image1.png`（新）、`docs/upstream/02_signal_redo.md`（新）。
`feature.yaml`、`data/signal_chain_v43.tsv`、`data/sysra_v43_functional.tsv`、
`sources/`、`forms/`、`docs/fw036/`、`docs/runtime/`、`scripts/` **未寫入**。

---

## 十、下一步

1. Pei：**共用腳本一裁**（五項，02 包 §四-1）—— 已連續三包待裁
2. Pei：**DR-VT1／VT2／VT3 併送**；並考慮 §八-1 之 `DR-VT4`（內部訊號對照總表）
3. 分析層：A-VT16（R-VT9(b) 但書）、A-VT17（E16 基準）、`Description` 欄不存在（§二-2）三題
4. 下包：擴充比對之對象是否擴及 HMI Settings List 與 PROXI `Format`（§八-2）
5. vsm_v42 之 W-0 → 台帳重生（A-VT13）→ 本線 sha8 改自台帳讀；並使 `signal_chain_v42.tsv` 產出 → 補差集
6. P3：framework Layer 1 鎖定、profile、`spec_reference_template` 定案
7. 037 到齊 → 母體建檔 → Layer 2 → P4
