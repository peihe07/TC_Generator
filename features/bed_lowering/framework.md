# framework.md — Bed Lowering Mode

狀態：**LOCKED**（Pei 裁定 2026-08-26），Part III 已經 R-G10 餘數驗證
（176/176 leaf、42/42 Heading，餘數與溢出皆空）。阻斷項已清空。
Feature slug：`bed_lowering`
規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、FO §0（Tier 2：framework Test Set derivation 屬 Pei 簽核）

---

## Part I — Layer 1（Test Group）

```
Bed Lowering Mode
```

依 IN §4.1.1：Layer 1 = HMI 模組／feature 名，取規格文件標題
`Bed Lowering Mode HMI Logic and Flow R1 SR24 1A (June 21 2021)` 之特徵名部分。
寫入工作簿 Test Group 欄，全簿逐字一致。

---

## Part II — Layer 2（Test Set，寫入工作簿）

九組。依 IN §4.2：英文名詞片語、1–3 字、不重複 Test Group 前綴、
不得為動作標籤或句子、無 `Misc`／`Unclassified`。

| # | Test Set | 能力叢集 |
|---|---|---|
| 1 | `Feature Entry` | HMI 入口之存在與放置：app drawer、Controls tab、Apps menu、Home Screen 捷徑、圖示 |
| 2 | `Activation Gating` | 啟用前之車輛狀態閘：ignition／engine ON、靜止、0 MPH、gear 不限、ignition OFF 不可用 |
| 3 | `Lowering Operation` | 懸吊動作本體：DT 前升後降、DJ/D2 僅後降、協同動作、目標角度達成、既有氣壓懸吊路徑 |
| 4 | `HU Feedback` | 主機端視覺回饋：圖示 selected 態、highlight、status bar truck-lowering 圖示 |
| 5 | `Cluster Feedback` | 儀表與 EVIC 回饋：in-progress／lowered 訊息、cluster 畫面、完成提示音 |
| 6 | `Fault Handling` | 失敗路徑：fault 偵測、角度未達、highlight 撤除、EVIC unsuccessful 訊息 |
| 7 | `Restore And Exit` | 退出與復位：二次按壓復位、超速退出、回復請求當時之 ride height |
| 8 | `Display Legibility` | 日夜可視性、字體 legibility、標籤指引遵循 |
| 9 | `Access Ergonomics` | 手指觸及淨空、5th 女性至 95th 男性含手套、人因指引遵循、soft button 指引 |

### Layer 2 命名之兩點說明

- **`Cluster Feedback`**：草案原名 `Cluster & EVIC Feedback`。`&` 於 Test Set
  值中不宜（IN §4.2 禁 bracket tag／符號串接之精神），且 EVIC 為 cluster 之
  顯示通道而非並列實體，故收斂為 `Cluster Feedback`；EVIC 訊息 TC 歸此組。
- **`Ergonomics & Legibility` 拆為兩組**（`Display Legibility` + `Access Ergonomics`）：
  草案將視覺可讀性與手部觸及併為一組，二者之 setup pattern 與 UI entry path
  不同（前者不需觸控，後者需實車包裝量測），違反 IN §4.2「同一 Test Set 應
  蘊含共用 setup pattern 與 UI entry path」。拆後兩組各自內聚。

> 上述兩點為**草案之機械化收斂**（IN §4.2 既有判準之套用，FO §0 Tier 0
> 「既有條文之機械套用」），非新增判斷。**若 Pei 要求回復草案原名，逕改，
> 本檔重出。**

### 反模式自查（IN §4.1.3）

- 過細：9 組對 176 leaf，平均 19.6 leaf/組，最小組（`Access Ergonomics`，
  BLM-017 + BLM-023，7 leaf）仍為多 TC 叢集，非 TC ID 之複本 ✓
- 過粗：無 `Misc`／`General`／`Unclassified` ✓
- 決策測試：以任一 Test Set 過濾工作簿，得到相關 TC 之有意義叢集 ✓

---

## Part III — Layer 3（規格章節分組，**不寫入工作簿**）

依 IN §4.1.5：Layer 3 僅存本檔。用途見 IN §4.1.4（TC 排序、sibling 識別、
覆蓋分析單位、scope drift 防制）。

| Layer 2 | 037 Heading（母號） | Heading 數 | leaf 數 | HMI/Service |
|---|---|---|---|---|
| Feature Entry | 004, 018, 019, 025, 028, 029, 030, **039** | 8 | 31 | 31/0 |
| Activation Gating | 005, 006, 007, 020, 024, 042 | 6 | 28 | 7/21 |
| Lowering Operation | 001, 002, 003, 021, 035, **040**, 041 | 7 | 33 | 18/15 |
| HU Feedback | 008, 026, 031, 032, 036 | 5 | 20 | 20/0 |
| Cluster Feedback | 009, 010, 012, 033, 034 | 5 | 13 | 11/2 |
| Fault Handling | 011, 037, 038 | 3 | 13 | 13/0 |
| Restore And Exit | 022, 027 | 2 | 9 | 5/4 |
| Display Legibility | 013, 014, 015, 016 | 4 | 22 | 22/0 |
| Access Ergonomics | 017, 023 | 2 | 7 | 7/0 |
| **合計** | | **42** | **176** | **134/42** |

粗體之 039／040 為 Pei 2026-08-26 裁定之後併項（見下段）。

### 餘數驗證（R-G10）—— 全綠

實測於 2026-08-26，以 `openpyxl`（`read_only=True, data_only=True`）讀
037 `Analysis Report` 分頁，逐列依 `SWE1-HMI-BLM-(\d{3})` 取母號計數：

| 判準 | 結果 |
|---|---|
| 合計 leaf = 母體 176 | **PASS** |
| Heading 已分類 = 42/42 | **PASS** |
| 餘數（全集 − 已分類）= 空 | **PASS** |
| 溢出（已分類 − 全集）= 空 | **PASS** |
| 無 Heading 被重複指派 | **PASS**（以 assert 驗）|

> **前版之「leaf 數合計 186」作廢。** 那是逐 Heading 目測子項數推的，
> 不是數出來的。實測為 176，與母體相符。

> **餘數驗證驗不到的事（G-N 之形態，實例入檔）**：
> 本表首次驗算時，分析層用的是**當下重寫之分組**
> （`003 → Feature Entry`、`024 → Feature Entry`），該版**亦為 176/176 全綠**，
> 但與本檔已鎖定之分組不符（鎖定版：`003 → Lowering Operation`、
> `024 → Activation Gating`）。兩版之 `Feature Entry` 分別為 42 leaf 與 31 leaf。
> **兩版皆通過餘數驗證，因為餘數驗證管的是「有沒有漏、有沒有重」，
> 不管「歸得對不對」。** 本表之數字為鎖定版之實測結果；
> 日後重跑驗算須以本檔之分組為準，不得現場重擬。

### SYS1 Outline 欄之移除

前版本表含一欄「Layer 3（SYS1 Outline）」，**已移除**。
理由：該欄之章節號為分析層依需求文字推定，非上游正式欄之輸出
（A-BLM4）；而依 **R-BLM5**（採乙案）交付欄不帶章節號，
該欄既不入工作簿、亦無上游來源，留著只會被誤讀為已驗之對映。

Layer 3 之分組單位因而改以 **037 Heading 母號**承載（上表第二欄）
—— 該欄為上游正式欄之逐字值，可驗。IN §4.1.4 之四項用途
（TC 排序、sibling 識別、覆蓋分析單位、scope drift 防制）
皆以母號為座標，不受影響。

### 已決一項（Pei 裁定 2026-08-26，採乙）

`System Constraints` **不立獨立組**：

- **BLM-039**（head unit menus modifiable）→ `Feature Entry`
- **BLM-040**（air suspension LED 全滅）→ `Lowering Operation`

理由：039 講選單可修改性（入口放置之前提），040 講懸吊 LED 於 BLM 期間之
狀態（降床動作之伴隨行為）—— 二者能力歸屬不同，併為一組即為過粗形態。
Layer 2 定案為 **9 組**（Part II 不變）。

---

## Part IV — TC ID 與追溯欄

- TC ID：`{project}-BLM-{NNN}`（IN §10.3），project 前綴依 feature.yaml 定義
- `Requirement or Design ID`：填 leaf 之 `SWE1-HMI-BLM-{nnn}-{mm}`，逐字沿用上游
- `specification_reference`（**R-BLM5**，[OVERRIDE IN §10.7(b)]）：逐字取 037
  `HMI Source ID` 欄原值，**單行常數、不帶章節號**：
  `SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)`
  全簿 176 列同值。本 feature 無 CFTS 家族。override 之啟動見
  `docs/runtime/profiles/FW036_R1L_BedLowering_Profile.md` §1
- 42 個 Heading 列（BLM-001 ~ 042 母號）入覆蓋台帳並標
  `No TC — Heading; refer to child IDs`，不生成 TC（R-BLM2）

---

## Part V — 變更紀錄

| 日期 | 變更 | 依據 |
|---|---|---|
| 2026-08-26 | 初版鎖定，Layer 1／2 定案，Layer 3 為草案待 recon 驗證 | Pei 裁定；下放包 01 §五 |
| 2026-08-26 | `System Constraints` 採乙案拆併；發現 A-BLM4（章節錨缺失），Part VI 立 | Pei 裁定；實測 |
| 2026-08-26 | A-BLM4 裁定採乙（R-BLM5）；Part IV spec_reference 改寫、Part VI 由「阻斷」轉「已裁」 | Pei 裁定「乙」 |
| 2026-08-26 | Part III 換上實測表（176/176、42/42 餘數全綠）；SYS1 Outline 欄移除；186 估算作廢 | R-G10 驗算 |

---

## Part VI — spec_reference 無章節錨（A-BLM4，**已裁**）

**裁定：Pei 2026-08-26 採乙案（R-BLM5）。阻斷解除，Phase 4 可開工。**

### 實測事實（2026-08-26，全表掃描）

| 項 | 實測值 |
|---|---|
| 037 `HMI Source ID` 相異值數 | **1**（218/218 列皆為 `SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)`，**無章節號後綴**）|
| 037 `Source Requirement ID` 相異值數 | 42（`SYS-HMI-RA-BLM-001` ~ `-066`，每 Heading 一個，同母號之 leaf 共用）|
| SYS1 `SYSRE_HMI_Source ID` 格式 | `{檔名}_{章節號}`，70 列各異（即 IN §10.7(b) 所要之形式）|
| 兩者之相交 | **無**。`SYS-HMI-RA-BLM-nnn` 不出現於 SYS1 任一欄；SYS1 之 `NRL-nnnnnn` 與章節號不出現於 037 任一欄 |

### 影響

IN §10.7(b) 要求 `specification_reference` = `{檔名}_{章節號}`。
**上游正式欄只給得出檔名，給不出章節號。** 而錨定原則（上游交付物之
正式欄為第一來源，非本地演算輸出）禁止分析層自行推定章節號。

**176 條 leaf 全數受影響。**

### 三個選項之裁定（Pei 2026-08-26：**乙**）

- （甲）登 DR-2 向上游索取對照表。**未採** —— 會阻斷生成至回覆。
- **（乙）`specification_reference` 逐字沿用 037 之 `HMI Source ID`（僅檔名，
  無章節號）。◀ 採此案。** 合於錨定原則；代價為全簿 176 列該欄同值，
  追溯粒度降至文件級，已立 `[OVERRIDE IN §10.7(b)]` 於 profile §1。
- （丙）逐條標 [DERIVED] 交 Pei 追認。**未採** —— 需 override 錨定原則，
  且 176 條逐條追認成本高。

**交付面代價須於交付說明揭露**：審查者無法自 N 欄定位到規格章節；
定位須經 `Requirement or Design ID` → 037 → `Requirement Description` 之路徑。

### 附：24 個 SYS 缺號（**已裁**）

`SYS-HMI-RA-BLM` 之 001~066 中，037 僅引用 42 個；缺號為：
3, 5, 6, 8, 12, 18, 19, 21, 23, 26, 28, 30, 32, 33, 35, 38, 39, 41, 42, 47,
53, 56, 61, 62（共 24）。

**Pei 2026-08-26 裁定（R-BLM6）**：該 24 號為 SYS 側非 HMI 項（底盤、電氣），
未列於 037 即不寫。不生成 TC、不列 coverage gap、不登 DR。

**該裁定之依據為 Pei 之領域判斷，非自手邊文件驗得。**
分析層先前之實測結論為「二者（SYS 側非 HMI 項／037 未分解之項）
在手邊文件上區別不出來」，該結論不因本裁定而改變 ——
改變的是**由誰承擔該判斷**。
