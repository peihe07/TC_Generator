# 10 — 欄位對應交叉驗證與首批 pilot 回覆

下放包 | 分析層 → 執行層 | 往返 NN = 10

前置：docs/upstream/09_phase4_batch1.md 已覆核，判定 **ACCEPT**，
惟 pilot review 有三項發現（F1 / F2 / F3），見 §B4。

**寫回仍不開放。** 開放條件為 R-P73 之交叉驗證取得第二來源佐證。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P73] **`workbook.columns` 之欄位對應須有第二來源佐證，
        且為寫回之阻斷條件。**
        A-PW40 係執行層依 FW036 r9 自行推導，
        分析層**無法獨立實測**（沙箱之 Project 附件已更換，
        Power 之 FW036 不在其中），故現況為單一來源。
        追認一個未經第二來源佐證之欄位對應，與 R-P62
        「論證前提不成立」為同型錯誤。
        交叉方法：取 **Comfort 與 Privacy 之已交付工作簿**
        （已交付、已驗收，屬已知 good）之 r9 逐欄比對。
        （a）若三者 r9 一致 → 錯位者為 scaffold，A-PW40 成立
        （b）若 Power 之 r9 與二者有異 → 差異本身即為證據，
             須逐欄列出並重新判定何者為權威
        寫回於本條取得結論前**一律不開放**。
        裁決者 Pei，逐字依據：「出」（回應 09 Q1、Q5）。
```

```
[R-P74] **兩個逐字相同之 `Estimated Test Time` 欄（P 與 R）
        之權威判定，併入 R-P73 一併查明。**
        判準：已交付之 Comfort / Privacy 工作簿實際填寫哪一欄。
        另一欄之處置（留空或同值）依實測結果裁定。
        裁決者 Pei，逐字依據：「出」（回應 09 Q6）。
```

```
[R-P75] **§11 與 §4.4 入 lint（G50 / G51）。**
        二者皆為零判斷成分之字串規則，靠人工自查即靠紀律。
        G50（§11）：四個長欄位無 trailing period；
          UI 標籤用雙引號不用方括號、單引號、角括號；
          方括號僅得用於逐字引自來源之訊號值，須於 `reasoning` 說明
        G51（§4.4）：`pre_conditions` 不得含動作
          （以動詞偵測；`insert` / `press` / `connect` / `check` /
           `confirm` / `verify` / `open` / `select` 等為主要動詞即 FAIL）
        二閘皆須合成 fixture，違規案例須**實際觸發**。
        裁決者 Pei，逐字依據：「出」（回應 09 Q2）。
```

```
[R-P76] **lint 之 findings 分流為兩類。**
        （a）**阻斷類** —— 所有閘門，使 exit=1
        （b）**待人工裁決類** —— 僅 R-P42(b) 之觸發，
             **不使 exit=1**，另列一節輸出，須逐條人工裁決
             （判為「真違規」或「偽陽性」及其依據）並登記
        R-P67 明令 R-P42(b) 之觸發不得自動判 FAIL；
        現行實作使其與其他閘門混在同一份 findings 且同樣 exit=1，
        該條文因此僅存於紙上。
        裁決者 Pei，逐字依據：「出」（回應 09 Q3）。
```

```
[R-P77] **`feature.yaml` 兩項可疑值訂正。**
        （a）`done_region.author_value: "Arif"` → **改為空值**。
             Comfort 於同為 BLANK 之情形已踩過此坑並留下結論：
             填佔位作者值會**靜默匹配零列，使空的 invariant
             看起來像已滿足**。此為既有政策，依 §5a 第 17 條優先。
        （b）`write_back.fill_test_group_set: false` → **改為 `true`**。
             其自身註解為「true only under BLANK」，
             而本 workbook 實測即為 BLANK（G10）。
        二項皆須納入 G46 之一致性檢查。
        裁決者 Pei，逐字依據：「出」（回應 09 Q7）。
```

```
[R-P78] anomaly 編號重整**追認**。
        執行層將其原有三條改編為 A-PW40/41/42，
        09 §F 指定之兩條取用 A-PW37/38，G45 bug 取 A-PW39；
        現 A-PW01–A-PW42 連續無缺。
        處理方式符「撤回列不刪、不重編號」之精神。
        裁決者 Pei，逐字依據：「出」（回應 09 Q8）。
```

（以上**六條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。）

## B. 本包須產出

### B1. 欄位對應交叉驗證（R-P73 / R-P74）

  取 Comfort 與 Privacy 之**已交付**工作簿
    （路徑見各 feature 之 `DELIVERY.sha256` 最末 `type: delivered` 筆）
  以 `read_only=True` 讀其 r9，逐欄輸出 `(欄字母, 標頭逐字)`
  與 Power 之 FW036 r9 三方對照，逐欄列出
  標明：三者一致之欄、Power 獨有之差異、Comfort/Privacy 間之差異
  **兩個 `Estimated Test Time` 欄**：檢視 Comfort / Privacy 之
    已交付資料列，實際填寫者為 P 或 R，逐列舉證
  結論：A-PW40 成立與否；若成立，錯位者為 scaffold；
    若不成立，重新判定正確對應

輸出至 `features/power/data/b1_column_crosscheck.md`。

**此為本包最重要之產出。寫回之開放與否繫於此。**

### B2. 兩閘與分流（R-P75 / R-P76）

  G50 / G51 實作與合成 fixture
  findings 分流：阻斷類與待人工裁決類分節輸出
  以合成之 R-P42(b) 觸發案例驗證分流確實生效
    （該案例須使「待裁決」節有內容而 exit **仍為 0**）

### B3. `feature.yaml` 訂正（R-P77）

  兩項改動，並納入 G46
  改動後重跑 G46，確認 repo 現況通過

### B4. 首批 pilot 三項發現之回覆

工作簿為 BLANK、無 done region，依 canon §1.1 三者現為**候選**，
回覆後定性為 defect / style-divergence / note。

**F1 —— `002` 「No splash screen when TLM passes to Standby or Bench」**
  §5.7 之拆分準則為「不同 **trigger**」。轉入 Standby 與轉入 Bench
  為兩個不同觸發，非同一觸發之兩個後果。
  §8.3 壓力測試：Standby 抑制正確而 Bench 誤顯示 →
  兩個獨立之部分失效落在同一個 fail 上。
  **應拆為二條，或逐字說明為何二者構成同一觸發。**

**F2 —— `009` 「Normal operation resumes 10 seconds after recovery」**
  §8.4.1 禁止造值。§4.4 對 `SplashScreen_Time` 已謹慎未編秒數，
  此處之「10 秒」出處為何？
  若 `4942354` 有明文，**附逐字引用即結案**；
  若無，須改為「與設定值比對」之表述。

**F3 —— `006` / `008` 判為決策表**
  §12 為 first-match，而**狀態轉換排在決策表之前**。
  Load Shed 啟動 → 音量受限、Battery Critical → 最小化耗電，
  二者外觀皆為狀態變化。
  **須附 §12 之逐條 first-match 走查**，說明為何未於狀態轉換一列命中。
  執行層自身於 09 §七第 4 項已示警「first-match 順序理解偏差
  會系統性偏向同一值」—— 此即該檢查之處。

三項回覆須逐項載明「接受並修正」或「不接受並附依據」。
若修正 TC，須重跑完整 lint 並更新 `batch_001_power_down.json`。

## C. 抽取規格

  §C rule 1 / 2 / 3 / 4 正則不變。
  R-P17 文字層定義不變。
  `MIN_FINGERPRINT = 40` 不變（R-P62）。

## D. 閃點

G0 為前置閘。G0–G16、G13b、G18–G49 沿用（G17 已移除），期望值不變。

| # | 項目 | 期望值 |
|---|---|---|
| **G52** | 三方 r9 交叉比對（R-P73） | 【實測填入】三者一致之欄數、Power 獨有差異之欄清單 |
| **G53** | 兩個 `Estimated Test Time` 之權威（R-P74） | 【實測填入】Comfort / Privacy 已交付列實際填寫者為 P 或 R |
| **G50** | §11 閘門（R-P75） | fixture 正常 PASS、違規實際 FAIL（trailing period 一例、方括號 UI 標籤一例） |
| **G51** | §4.4 閘門（R-P75） | fixture 正常 PASS、違規實際 FAIL（Pre-Condition 含動作一例） |
| **G54** | findings 分流（R-P76） | 合成之 R-P42(b) 觸發案例使「待裁決」節有內容且 exit **= 0** |
| **G55** | 首批 lint 重跑（B4 修正後） | 全閘 PASS；若 TC 數改變，G47 之 leaf 涵蓋仍為 3 |

G50 / G51 / G54 之驗證條件同 G33：**須確認其在該階段確實可能失敗**。

## E. framework

§E 已定版（R-P35），本包不動。

## F. Anomaly 異動

  A-PW40 → 依 R-P73 之交叉結果更新為成立或訂正；**現階段標記為「單一來源，待第二來源佐證」**
  A-PW41 → 依 R-P74 之結果更新
  新增 A-PW43：`done_region.author_value` 填佔位值會靜默匹配零列
               （Comfort 既有結論，本 feature 沿用；R-P77(a)）
  新增 A-PW44：分析層無法獨立驗證 A-PW40 —— 沙箱之 Project 附件
               已更換為 Comfort 素材，Power 之 FW036 不在其中。
               覆核方之驗證能力受工具環境限制，此限制本身須登記，
               不得以「執行層已自陳」代替第二來源
  新增 A-PW45：G45 之合成 fixture 全數通過而真實檔名全滅
               （第二次「合成通過、真實全滅」，前次為 07 包之 `\b` bug）；
               二次皆證 fixture 驗邏輯不驗現實

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
  2. 產出 B1 三方欄位交叉比對，驗 G52 / G53 —— **最優先**
  3. 依 R-P75 補 G50 / G51，fixture 驗證
  4. 依 R-P76 實作 findings 分流，驗 G54
  5. 依 R-P77 訂正 `feature.yaml` 兩項，重跑 G46
  6. 依 B4 回覆 F1 / F2 / F3；若修正 TC 則重跑 lint，驗 G55
  7. 以 §D 全表自驗
  8. §A 六條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
  9. 上繳 features/power/docs/upstream/10_column_verify.md，更新 docs/INDEX.md

## I. 禁區

  **不得寫回 FW036 workbook（R-P73 未取得結論前一律不開放）**
  不得執行任何 git 操作（全數屬 Pei）
  不得以 openpyxl save 寫任何 xlsx（R16 凍結）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得修改任何已落檔裁決條文之內文（R-P36）
  不得測試未被引用之錨點（R-P42）
  不得解析任何 RTF 或 OLE stream 之內容（R-P39、R-P48）
  不得續行章節層反向缺口調查（R-P37）
  不得變更 §E 之分布數字（R-P35）
  不得以 A-PW29 之存在逕行填寫車型欄（R-P54）
  不得調整 `MIN_FINGERPRINT`（R-P62）
  **不得擴大批次範圍超出 `Power Down` 3 leaf** —— 第二批於 11 包另議
  **不得以 repo 現況作為任何 fixture 之測試對照**
  **B1 讀 Comfort / Privacy 工作簿一律 `read_only=True`，不得寫入**
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P73 `workbook.columns` 須第二來源佐證，為寫回之阻斷條件
  R-P74 兩個 `Estimated Test Time` 之權威併入 R-P73 查明
  R-P75 §11 與 §4.4 入 lint（G50 / G51）
  R-P76 lint findings 分流為阻斷類與待人工裁決類
  R-P77 `feature.yaml` 兩項可疑值訂正
  R-P78 anomaly 編號重整追認

  逐條確認：**六條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 6、§J 列數 = 6、§H 步驟 8 寫「六條」，三處一致。
