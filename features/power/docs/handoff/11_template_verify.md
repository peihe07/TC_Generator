# 11 — 範本全屬性比對與首批全文覆核

下放包 | 分析層 → 執行層 | 往返 NN = 11

前置：docs/upstream/10_column_verify.md 已覆核，判定 **ACCEPT**。
R-P73 已取得結論，A-PW40 成立，欄位對應確認正確。

**寫回仍不開放。** 阻斷條件改為 R-P79（範本全屬性未比對）。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P79] **範本之 r9 以外屬性須比對，且為寫回之新阻斷條件。**
        R-P73 之結論僅及於「r9 標頭」一個屬性。
        Power 與 Comfort / Privacy 為不同範本版本（A-PW47：
        分頁名不同、35 欄 vs 34 欄）。
        資料驗證範圍、公式、其他分頁、儲存格格式皆**未比對**。
        Comfort 之 `DELIVERY.sha256` 載其 DV 範圍為
        `P10:Q601` / `T10:Z601` / `AF10:AF601` —— 該等欄字母
        係 Comfort 之座標，Power 整體右移一格；
        若 Power 之 DV 以 Comfort 座標設定，寫回將落於錯誤欄位。
        另：既有 **R-G3** 已記載 openpyxl + `wb.save()`
        會破壞 rev C 工作簿之 R 欄 x14 dataValidation ——
        DV 為本管線已知會出事之處。
        比對範圍見 §B1。
        裁決者 Pei，逐字依據：「好」（回應 10 Q2、Q8）。
```

```
[R-P80] **「已交付」作為權威之限度**（跨 feature 通則，canon 候選）。
        已交付件僅於「該 feature 曾明文裁決之屬性」上具權威。
        未經裁決之屬性上：二份已交付件一致僅為巧合，
        不一致則證明其根本不構成權威來源。
        依據：A-PW46 —— Comfort 七個車型欄逐列填 `1`（466/466）、
        Privacy 全數留空（0/11），二份「已知 good」做法相反。
        R-P73 之交叉方法即建立於「已交付＝已知 good」之整體假設上，
        該假設在 r9 標頭成立（二者一致）、在資料內容不成立。
        故 R-P73 之結論**不得外推至標頭以外之任何屬性**。
        裁決者 Pei，逐字依據：「好」（回應 10 Q3）。
```

```
[R-P81] **A-PW46 之處置：先查證，不投票。**
        查 Comfort 之 `RULINGS.md` 有無「車型欄填 `1`」之明文裁決。
        （a）**有** → 屬 feature-scoped override，
             R30-3 / R30-4 仍為預設，Power 依 R-P54 維持留白
        （b）**無** → Comfort 為未登記之偏離且已交付，
             登為跨 feature anomaly，Power 仍依 R-P54 維持留白
        二種情形下 Power 之處置皆為留白 —— 故本條**不阻斷寫回**。
        **不得以「兩個樣本中一個這樣做」為由改變 Power 之處置** ——
        該即 R-P80 所禁之「已交付即權威」之錯用。
        裁決者 Pei，逐字依據：「好」（回應 10 Q1）。
```

```
[R-P82] **建立 Power 之 runtime profile。**
        `docs/runtime/profiles/` 現有七個 feature 之 profile，
        獨缺 Power。§11 之 profile-scoped 例外因此懸空 ——
        首批 TC 中之 `[1h]` / `[0h]` 訊號值方括號現靠 G50 之
        硬編碼豁免，非靠 profile 條款。
        profile 須至少載明：
          §11 之逐字引用 token 例外（訊號值方括號）
          §3.2 之 source-class 標記慣例（`[spec-derived]` 等）
          spec_mode = D 及其讀取方式（R-P3′）
          Test Set 定版清單與分布（R-P35）
        檔名比照既有慣例 `FW036_R1L_Power_Profile.md`。
        裁決者 Pei，逐字依據：「好」（回應 10 Q4）。
```

```
[R-P83] **G51 之動詞判準改以經驗基礎導出。**
        現行 20 個動詞為執行層自行列舉，無來源佐證：
        漏列者不被攔下、誤列者誤殺，二者皆未量測。
        改為：自**已交付 TC 之 `test_procedure` 欄**取動詞聯集
        （該欄內容依定義即為動作），作為動作動詞之經驗基礎；
        再以**已交付之 `pre_conditions` 欄**量測偽陽性率。
        來源為 Comfort 與 Privacy 之已交付件；
        依 R-P80，此處僅用其「procedure 欄含動作、
        pre_conditions 欄不含動作」之結構性事實，
        不引用其任何內容裁決。
        裁決者 Pei，逐字依據：「好」（回應 10 Q5）。
```

```
[R-P84] **F3 之走查須於 CFTS010 全文確認 Load Shed 是否被命名為 status。**
        現行走查所據之 TLM status 清單係自 CFTS009 §1.6.2.1.1–.13 讀出；
        若 CFTS010 另有定義 Load Shed 為一個 status，該論證即不成立，
        `006` / `008` 之 design_method 須重判。
        執行層已於 10 §7.2 第 5 項自行指出此缺口。
        裁決者 Pei，逐字依據：「好」（回應 10 Q6）。
```

```
[R-P85] **pilot review 須以 TC 全文為之，摘要表不足。**
        分析層前次之 F1 / F2 / F3 三項發現**全部僅基於
        `tc_title` / `priority` / `design_method` 之摘要表**；
        `pre_conditions` / `test_procedure` / `expected_result`
        三個主要欄位一字未讀。
        依 canon §1.2，該不構成 pilot review。
        往後任何批次之 pilot review，上繳包須附該批 TC 之**全文**
        （十條以內全附；逾十條依 canon §1.2 分層取樣並註明取樣法）。
        裁決者 Pei，逐字依據：「好」（回應 10 Q7）。
```

（以上**七條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。）

## B. 本包須產出

### B1. 範本全屬性比對（R-P79）—— **本包最重要之產出**

三份工作簿皆 `read_only=False` 開啟但**絕不呼叫 `save()`**；
若需完整讀取 DV 則以 `zipfile` 直讀 XML，不經 openpyxl 寫入路徑。

逐項比對 Power / Comfort / Privacy：

  （a）**資料驗證（DV）** —— 每個 DV 之 `sqref` 範圍、type、formula1
       特別注意 x14 擴充命名空間之 DV（R-G3 所指者）
       以 `zipfile` 讀 `xl/worksheets/sheet*.xml` 與其
       `<extLst>` / `x14:dataValidations` 區段
  （b）**分頁清單** —— 名稱、順序、是否隱藏
  （c）**合併儲存格** —— r1–r9 之 merge 範圍
  （d）**條件式格式** —— 範圍與規則
  （e）**欄寬與凍結窗格**
  （f）**公式** —— 任何含 `=` 之儲存格及其位置

輸出至 `features/power/data/b1_template_diff.md`，逐項標明：
  三者一致 / Power 獨有 / Comfort≠Privacy（依 R-P80 此情形不得取多數）

**結論須明確回答：Power 之 DV 範圍是否與其自身欄位對應相符，
或是否沿用了 Comfort 座標而落在錯誤欄位。**

### B2. A-PW46 之查證（R-P81）

  搜尋 `features/comfort/RULINGS.md` 有無車型欄填 `1` 之裁決
  搜尋 `features/comfort/ANOMALIES.md` 與 `DECISIONS.md` 同
  回報 (a) 或 (b)，附逐字引用或明確之「查無」聲明
  **Power 之處置一律維持留白，不因查證結果改變**

### B3. Power profile 建立（R-P82）

  `docs/runtime/profiles/FW036_R1L_Power_Profile.md`
  內容依 R-P82 所列四項，並比照既有七個 profile 之結構
  建立後，G50 之 `[spec-derived]` 與訊號值方括號豁免
    改為**引用 profile 條款**，不再硬編碼

### B4. G51 動詞判準重導（R-P83）

  自已交付 TC 之 `test_procedure` 取動詞聯集，回報清單與筆數
  以已交付之 `pre_conditions` 量偽陽性，回報誤觸發數與逐條明細
  與現行 20 個動詞對照：漏列者、誤列者各若干
  更新 G51 並重跑 fixture

### B5. F3 之補查（R-P84）

  於 CFTS010 全文（依 R-P3′ 自原始檔抽出之文字層）搜尋
    `Load Shed` 是否被命名為一個 status
  搜尋條件須載明（大小寫、詞界、所掃章節範圍）
  若成立 → `006` / `008` 之 design_method 重判並重跑 lint
  若不成立 → F3 之走查確認成立，逐字回報依據

### B6. 首批 10 條 TC 全文（R-P85）—— **上繳包必附**

十條全部，逐條附：
  `tc_id` / `req_id` / `tc_title` / `test_set`
  `pre_conditions` / `input_test_data` / `test_procedure` /
  `expected_result` / `specification_reference` /
  `design_method` / `priority` / `split_flag` / `split_reason`
  該條之 `reasoning`

**不得節錄、不得省略換行、不得以摘要代替。**

## C. 抽取規格

  §C rule 1 / 2 / 3 / 4 正則不變。
  R-P17 文字層定義不變。
  `MIN_FINGERPRINT = 40` 不變（R-P62）。

## D. 閃點

G0 為前置閘。G0–G16、G13b、G18–G55 沿用（G17 已移除），期望值不變。

| # | 項目 | 期望值 |
|---|---|---|
| **G56** | 範本 DV 比對（R-P79） | 【實測填入】Power 之 DV 範圍清單；與自身欄位對應是否相符 |
| **G57** | 範本其餘屬性比對（R-P79(b)–(f)） | 【實測填入】逐項一致 / Power 獨有 / Comfort≠Privacy |
| **G58** | A-PW46 查證（R-P81） | 【實測填入】(a) 或 (b)，附逐字引用或「查無」聲明 |
| **G59** | Power profile 存在且 G50 引用之（R-P82） | profile 檔存在；G50 之豁免改為引用 profile 條款 |
| **G60** | G51 動詞判準（R-P83） | 【實測填入】經驗動詞清單筆數；對已交付 `pre_conditions` 之偽陽性數 |
| **G61** | F3 補查（R-P84） | 【實測填入】CFTS010 中 Load Shed 是否為 status |
| **G62** | 首批 TC 全文完整性（R-P85） | 十三個欄位 × 10 條皆有內容（`NA` 亦計為有內容） |

G59 之驗證條件：須確認 G50 在移除硬編碼後**仍能正確豁免**
且**仍能攔下不當方括號** —— 二者皆須 fixture 實測。

## E. framework

§E 已定版（R-P35），本包不動。

## F. Anomaly 異動

  A-PW40 → 依 R-P73 之結論標記為**成立且已驗證**（第二來源：Comfort + Privacy r9）
  A-PW46 → 依 R-P81 之查證結果更新為 (a) 或 (b)
  A-PW47 → 依 R-P79 之比對結果擴充；現階段標記為「僅 r9 已比對」
  新增 A-PW48：分析層之 F1 / F2 / F3 三項 pilot 發現僅基於摘要表，
               未讀三個主要欄位；不構成 canon §1.2 之 pilot review（R-P85）
  新增 A-PW49：Power 為八個 feature 中唯一無 runtime profile 者（R-P82）
  新增 A-PW50：G50 第三次「合成 fixture 未涵蓋真實慣例」
               （`[spec-derived]` 判為違規，而 Comfort 已交付件即如此書寫）；
               連同 07 包 `\b` bug、09 包檔名空格，三次同型

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
  2. 產出 B1 範本全屬性比對，驗 G56 / G57 —— **最優先**
  3. 產出 B2 A-PW46 查證，驗 G58
  4. 依 R-P82 建 Power profile，改 G50 為引用條款，驗 G59
  5. 依 R-P83 重導 G51 動詞判準，驗 G60
  6. 依 R-P84 補查 F3，驗 G61；若成立則重判並重跑 lint
  7. 依 R-P85 輸出首批 10 條 TC 全文，驗 G62
  8. 以 §D 全表自驗
  9. §A 七條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
 10. 上繳 features/power/docs/upstream/11_template_verify.md，更新 docs/INDEX.md

## I. 禁區

  **不得寫回 FW036 workbook（R-P79 未取得結論前一律不開放）**
  **不得對任何 workbook 呼叫 `save()`** —— 含 Comfort / Privacy（R-G3）
  不得執行任何 git 操作（全數屬 Pei）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得修改任何已落檔裁決條文之內文（R-P36）
  不得測試未被引用之錨點（R-P42）
  不得解析任何 RTF 或 OLE stream 之內容（R-P39、R-P48）
  不得續行章節層反向缺口調查（R-P37）
  不得變更 §E 之分布數字（R-P35）
  **不得因 A-PW46 之查證結果改變 Power 車型欄之留白處置（R-P81、R-P54）**
  **不得以「兩份已交付件中一份如此」為由推導任何裁決（R-P80）**
  不得調整 `MIN_FINGERPRINT`（R-P62）
  不得擴大批次範圍超出 `Power Down` 3 leaf —— 第二批於 12 包另議
  不得以 repo 現況作為任何 fixture 之測試對照
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P79 範本 r9 以外屬性須比對，為寫回之新阻斷條件
  R-P80 「已交付」之權威限於該 feature 曾明文裁決之屬性（canon 候選）
  R-P81 A-PW46 先查證不投票；Power 一律維持留白
  R-P82 建立 Power runtime profile
  R-P83 G51 動詞判準改以經驗基礎導出
  R-P84 F3 須於 CFTS010 全文確認 Load Shed 是否為 status
  R-P85 pilot review 須以 TC 全文為之，摘要表不足

  逐條確認：**七條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 7、§J 列數 = 7、§H 步驟 9 寫「七條」，三處一致。
