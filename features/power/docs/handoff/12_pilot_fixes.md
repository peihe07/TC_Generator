# 12 — pilot 修正與 Test Case Framework 判讀

下放包 | 分析層 → 執行層 | 往返 NN = 12

前置：docs/upstream/11_template_verify.md 已覆核，判定 **ACCEPT**。
R-P79 已取得結論，Power 之 DV 座標正確。

分析層讀畢 `001` / `002` 全文（10 條中 2 條，MCP 限制），
提出四項 pilot 發現，其中二項為系統性。
**寫回仍不開放**，阻斷條件改為 R-P92（`Test Case Framework` 分頁未判讀）。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P86] **`req_id` 不得加後綴，違反 §8.2.2。**
        首批十條之 `req_id` 寫為 `SWE-PM-071-01` / `-02` 等。
        §8.2.2 明文：「when one RD sub-id yields multiple TCs,
        both TCs list the **same** `Requirement or Design ID`」。
        `-01` / `-02` 後綴**發明了 037 中不存在之 ID**，
        寫入工作簿 Requirement 欄即為斷裂之追溯 ——
        客戶以 037 比對將無法對應。
        十條之 `req_id` 一律改為 `SWE-PM-071` / `SWE-PM-072` / `SWE-PM-073`；
        區分由 `tc_id` 承擔，不由 `req_id` 承擔。
        裁決者 Pei，逐字依據：「是」（回應 11 Q8 之 F4）。
```

```
[R-P87] **Procedure ↔ ER 須 1:1（G63）。**
        `001` 之 procedure 為 3 步而 ER 為 2 行；`002` 同。
        §6 要求「1:1 aligned with steps」，§9 第 10 項列為自查項。
        十條全數檢查並修正。
        補設閘門 G63：`test_procedure` 之編號步驟數
        須等於 `expected_result` 之編號行數。
        裁決者 Pei，逐字依據：「是」（回應 11 Q8 之 F5）。
```

```
[R-P88] **`pre_conditions` 不得含系統預設與環境穩定性前提（G64）。**
        `001` / `002` 之第 1 項「The TLM is powered from a stable supply」
        違反 §4.4（禁 system defaults，其範例逐字為 `HU is powered on.`）
        與 §8.5（禁環境穩定性前提，「testers naturally ensure
        the environment is stable」）。
        第 2 項「A suspend-resume boot sequence is available on the bench」
        屬 hardware / peripheral，**合格，不得一併刪除**。
        十條全數檢查；補設閘門 G64 —— 以判準偵測
        「供電／電源／連線穩定」類之泛稱環境陳述。
        判準之詞彙來源須有經驗基礎（比照 R-P83 之作法），
        不得由執行層憑印象列舉。
        裁決者 Pei，逐字依據：「是」（回應 11 Q8 之 F6）。
```

```
[R-P89] **`input_test_data` 之欄位歸屬須符 §4.5（G65）。**
        `002` 之 `input_test_data` 為 `Boot target status: Standby`，
        而其 procedure 第 1 步為「Set the boot target status to Standby」——
        同一值跨欄重複，§4.5 明文禁止。
        此為 interaction data，歸 Procedure；
        `input_test_data` 應為 `NA`（§4.5 明訂 `NA` 為合法且不違自查）。
        十條全數檢查；補設閘門 G65 —— `input_test_data` 之內容
        若逐字或近似出現於 `test_procedure` 或 `pre_conditions`，FAIL。
        裁決者 Pei，逐字依據：「是」（回應 11 Q8 之 F7）。
```

```
[R-P90] **B 欄明寫序號，並自 `NEVER_WRITE` 移除。**
        Comfort / Privacy 將 B 列入禁寫係因**其範本帶自動編號公式**
        （`IF(ISBLANK($D10),"",ROW()-9)`）；
        Power 之 B10 起實測為純空儲存格，無公式無值。
        照抄 Comfort 之設定將交出序號全空之檔 ——
        此與 A-PW40 同型：照抄他人設定即出錯，
        差別在於這次錯的是**行為**而非座標。
        寫回時 B 欄明寫連續序號（自 1 起）。
        補設閘門 G66：寫回後 B 欄非空列數須等於 TC 列數。
        裁決者 Pei，逐字依據：「是」（回應 11 Q1）。
```

```
[R-P91] **profile 條款須有閘門對應（G67）。**
        11 §9.2 第 5 項自陳：profile 之 §2 Test Set 清單、
        §3.3 status 清單、§3.4 檔名、§3.5 priority、
        §3.6–3.8 欄位留白皆無閘門，現為「寫下來的紀律」。
        該形態於本管線已反覆失敗（08 包批評、10 包補二閘、
        11 包再現）。
        可機械檢查者一律補閘，且**優先於第二批之產出**。
        裁決者 Pei，逐字依據：「是」（回應 11 Q6）。
```

```
[R-P92] **`Test Case Framework` 分頁須判讀，為寫回之新阻斷條件。**
        該分頁為 Power 獨有（Comfort / Privacy 皆無），
        其名稱直指 Test Group / Test Set。
        若其載有期望值而與 §E 定版（63/24/16/8/3）不符，
        則該分頁為**藏於交付標的自身內之權威來源**，
        其位階高於任何外部佐證 —— 它就在客戶要收的那份檔案裡。
        11 包僅比對分頁**清單**，未讀其內容。
        判讀範圍見 §B1。
        裁決者 Pei，逐字依據：「是」（回應 11 Q2）。
```

```
[R-P93] **§11 之「no HTML / Markdown tables」補入 G50；
        「blank line between fields」不補。**
        採納執行層 11 §9.1 之判斷逐字：
        前者為純字串規則且 `|` 分隔之表格會直接破壞工作簿儲存格內容；
        後者描述之為**工作簿呈現**，而本管線之 TC 以 JSON 獨立鍵儲存，
        欄位間不存在「空行」之概念，於 JSON 層強制等同發明
        規格未要求之約束。
        裁決者 Pei，逐字依據：「是」（回應 11 Q5）。
```

```
[R-P94] **A-PW51 回報 Comfort，範圍限定。**
        Comfort 已交付件之 466 個車型欄 `1` 非由其管線產生
        （其 profile、`write_back.py` 之 `NEVER_WRITE`、
        baseline 工作簿三者一致指向留白）。
        （a）於 `features/comfort/ANOMALIES.md` 登記此事
        （b）**範圍限定**：僅查 Comfort `write_back.py` 之
             `NEVER_WRITE` 所列各欄於已交付件中是否有值 ——
             此為最小且最直接之判準
        （c）**不得擴大為全欄位稽核**，不得修改 Comfort 之任何交付物
        裁決者 Pei，逐字依據：「是」（回應 11 Q4）。
```

```
[R-P95] A-PW52（Power 範本 DV 覆蓋不齊，三欄僅涵蓋 2–4 列）
        **登記不阻斷**。涉及之 estimated_time 與 Test Result 三欄
        依 profile §3.6 / §0.2 皆留空。
        條件式格式 `H10:H145` colorScale 之語義查明
        （含列上界 145 與 037 資料列末 r145 之關係）
        **可與寫回並行**，非阻斷 —— colorScale 為顯示層，
        最壞情形為著色不當，非資料錯誤。
        裁決者 Pei，逐字依據：「是」（回應 11 Q3、Q7）。
```

（以上**十條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。）

## B. 本包須產出

### B1. `Test Case Framework` 分頁判讀（R-P92）—— **最優先**

以 `zipfile` 直讀，不經 openpyxl 寫入路徑：

  全分頁之逐格內容（非空儲存格之座標與值）
  是否載有 Test Group / Test Set 之清單或期望值
  若有：逐項與 §E 定版（Power State 63 / Startup Display 24 /
    Branding and Theme 16 / Timeout Settings 8 / Power Down 3）比對
  是否載有其他約束（欄位說明、填寫規則、版本資訊）
  該分頁是否為隱藏分頁
  Comfort / Privacy 是否真無同名分頁（複驗）

輸出至 `features/power/data/b1_tc_framework_sheet.md`。

**結論須明確回答：該分頁是否構成與 §E 衝突之權威來源。**
**若衝突，停止並上繳，不得自行調整 §E（R-P35 已定版）。**

### B2. 十條 TC 之四項修正（R-P86–R-P89）

逐條檢查並修正：
  `req_id` 去後綴（R-P86）
  Procedure ↔ ER 1:1（R-P87）
  `pre_conditions` 去系統預設／環境穩定性前提（R-P88）
  `input_test_data` 欄位歸屬（R-P89）

**修正須逐條列出「修正前 / 修正後」**，不得只給修正後版本。
修正後重跑完整 lint。

### B3. 四道新閘（R-P87–R-P90）

  G63 —— Procedure 步數 = ER 行數
  G64 —— `pre_conditions` 之環境穩定性前提偵測
          （詞彙來源須有經驗基礎，比照 R-P83）
  G65 —— `input_test_data` 與 procedure / pre_conditions 之重複偵測
  G66 —— 寫回後 B 欄非空列數 = TC 列數（本包僅實作，寫回時生效）

四閘皆須合成 fixture，違規案例須**實際觸發**。

### B4. profile 條款補閘（R-P91 / G67）

  逐條盤點 profile 之可機械檢查條款，列出清單
  實作其閘門；不可機械檢查者明列並說明理由
  回報覆蓋率（可機械檢查條款中已有閘門者之比例）

### B5. §11 表格檢查補入 G50（R-P93）

  偵測 TC 四個長欄位中之 Markdown / HTML 表格
  fixture 須含 `|` 分隔表格一例

### B6. A-PW51 回報（R-P94）

  於 `features/comfort/ANOMALIES.md` 登記
  查 Comfort `write_back.py` 之 `NEVER_WRITE` 所列各欄
    於已交付件中之非空列數，逐欄回報
  **不得擴大範圍、不得修改 Comfort 之任何交付物**

### B7. 十條 TC 全文（修正後）—— **上繳包必附**

十三欄 × 10 條，逐條含 `reasoning`。
**不得節錄、不得省略換行、不得以摘要代替。**
分析層 11 包僅讀 2 條，本包須完成 10 條之覆核。

## C. 抽取規格

  §C rule 1 / 2 / 3 / 4 正則不變。
  R-P17 文字層定義不變。
  `MIN_FINGERPRINT = 40` 不變（R-P62）。

## D. 閃點

G0 為前置閘。G0–G16、G13b、G18–G62 沿用（G17 已移除），期望值不變。

| # | 項目 | 期望值 |
|---|---|---|
| **G68** | `Test Case Framework` 分頁判讀（R-P92） | 【實測填入】是否載有 Test Group / Test Set 期望值；是否與 §E 衝突 |
| **G63** | Procedure ↔ ER 1:1（R-P87） | fixture 正常 PASS、違規實際 FAIL；十條修正後全 PASS |
| **G64** | `pre_conditions` 環境穩定性偵測（R-P88） | fixture 正常 PASS、違規實際 FAIL；【實測填入】詞彙之經驗基礎與偽陽性數 |
| **G65** | `input_test_data` 重複偵測（R-P89） | fixture 正常 PASS、違規實際 FAIL |
| **G66** | B 欄非空列數 = TC 列數（R-P90） | 本包僅驗閘門邏輯（合成），寫回時方能實測 |
| **G67** | profile 條款閘門覆蓋率（R-P91） | 【實測填入】可機械檢查條款數／已有閘門者／覆蓋率 |
| **G69** | 十條 `req_id` 去後綴（R-P86） | 10 / 10 為 `SWE-PM-071` / `072` / `073` 之一，無後綴 |
| **G70** | 修正後 lint 全閘 | 全 PASS；leaf 涵蓋仍為 3；TC 數不變（修正非拆分） |

G63–G66 之驗證條件同 G33：**須確認其在該階段確實可能失敗**。

## E. framework

§E 已定版（R-P35），本包不動。
**若 B1 查出 `Test Case Framework` 分頁與 §E 衝突，停止並上繳，不得自行調整。**

## F. Anomaly 異動

  A-PW51 → 依 R-P94 回報 Comfort 並登記
  A-PW52 → 依 R-P95 登記不阻斷
  新增 A-PW53：首批十條之 `req_id` 加後綴，發明 037 中不存在之 ID，
               斷裂追溯（R-P86）
  新增 A-PW54：§6 之 Procedure↔ER 1:1、§4.5 之欄位歸屬、
               §8.2.2 之 req_id 一致性 —— 三者皆可機械檢查
               且皆於首批違反而**無任何閘門攔下**（R-P87 / R-P89 / R-P86）
  新增 A-PW55：分析層 11 包之 pilot review 僅讀 10 條中之 2 條，
               覆核不完整；四項發現若如推測為系統性，2 條足以定性，
               但第 3–10 條未讀不等於無問題
  新增 A-PW56：`Test Case Framework` 分頁自 01 包起即存在於交付標的內，
               十一包以來從未被讀取（R-P92）

## G. DATA_REQUESTS

  DR-PW1 → live，High
  DR-PW3 → live，Medium
  DR-PW5 → live，High
  DR-PW6 → live，Medium
  DR-PW7 → live，Low
  DR-PW2、DR-PW4 → 維持撤回
  無新增

## H. 作業指示

  1. G0 前置閘
  2. 產出 B1 `Test Case Framework` 判讀，驗 G68 —— **最優先；衝突即停**
  3. 依 R-P86–R-P89 修正十條（B2），逐條列前後對照
  4. 實作 B3 四閘，fixture 驗證 G63–G66
  5. 依 R-P91 補 profile 條款閘門（B4），驗 G67
  6. 依 R-P93 補 §11 表格檢查入 G50（B5）
  7. 依 R-P94 回報 A-PW51（B6）
  8. 修正後重跑完整 lint，驗 G69 / G70
  9. 輸出 B7 十條全文
 10. 以 §D 全表自驗
 11. §A 十條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
 12. 上繳 features/power/docs/upstream/12_pilot_fixes.md，更新 docs/INDEX.md

## I. 禁區

  **不得寫回 FW036 workbook（R-P92 未取得結論前一律不開放）**
  **不得對任何 workbook 呼叫 `save()`**（R-G3）
  不得執行任何 git 操作（全數屬 Pei）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得修改任何已落檔裁決條文之內文（R-P36）
  不得測試未被引用之錨點（R-P42）
  不得解析任何 RTF 或 OLE stream 之內容（R-P39、R-P48）
  不得續行章節層反向缺口調查（R-P37）
  **不得因 `Test Case Framework` 分頁之內容自行調整 §E（R-P35、R-P92）**
  不得因 A-PW46 / A-PW51 改變 Power 車型欄之留白處置（R-P54、R-P81）
  **不得修改 Comfort 之任何交付物；A-PW51 之查核範圍限 `NEVER_WRITE` 各欄（R-P94）**
  不得調整 `MIN_FINGERPRINT`（R-P62）
  不得擴大批次範圍超出 `Power Down` 3 leaf —— 第二批於 13 包另議
  **G64 之詞彙不得憑印象列舉，須有經驗基礎（R-P88）**
  不得以 repo 現況作為任何 fixture 之測試對照
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P86 `req_id` 不得加後綴（§8.2.2）
  R-P87 Procedure ↔ ER 須 1:1（G63）
  R-P88 `pre_conditions` 不得含系統預設與環境穩定性前提（G64）
  R-P89 `input_test_data` 欄位歸屬須符 §4.5（G65）
  R-P90 B 欄明寫序號並自 `NEVER_WRITE` 移除（G66）
  R-P91 profile 條款須有閘門對應（G67）
  R-P92 `Test Case Framework` 分頁須判讀，為寫回之新阻斷條件
  R-P93 §11 表格檢查補入 G50；blank line 不補
  R-P94 A-PW51 回報 Comfort，範圍限定
  R-P95 A-PW52 與 colorScale 語義查明，登記不阻斷

  逐條確認：**十條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 10、§J 列數 = 10、§H 步驟 11 寫「十條」，三處一致。
