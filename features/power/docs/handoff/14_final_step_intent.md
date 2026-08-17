# 14 — Final Step 驗證意圖與首批覆核收尾

下放包 | 分析層 → 執行層 | 往返 NN = 14

前置：docs/upstream/13_er_quality.md 已覆核，判定 **ACCEPT**。
R-P96 / R-P97 之修正已完成，G73 / G74 對本批 0 findings。

**惟 R-P96 之「合併步驟」引入第二項退步。** 分析層以三條 leaf 之
`source_clause` 原文對照，覆核 `001`–`005`、`010`（6 / 10），
發現 Final Step 之驗證意圖於合併時被剝除，五條中招。
**根因仍為分析層條文不完整** —— R-P96 只寫「應合併」，
未寫「合併後仍須符 §5.2B / §5.5」。

**寫回仍不開放**，阻斷條件為 R-P101 與 R-P98（未完成之覆核）。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

[R-P101] **Final Step 須含驗證意圖，合併步驟不得剝除之（G77）。**
        R-P96 令「無可觀察結果之步驟應合併」，
        未規定合併後之 Final Step 仍須符 §5.2B / §5.5，
        致 12 包原有之 `and check that ...` 子句於 13 包被剝除：

          `001` `Read the TLM display through SplashScreen_Time and again after SplashScreen_Time has elapsed`
          `002` `Read the TLM display through SplashScreen_Time`
          `003` 同 `002`
          `004` `Read the TLM screen content through StandardScreen_Time and again after StandardScreen_Time has elapsed`
          `010` `Read the volume limit and the audio output state before the measurement window elapses and again at the end of the measurement window`

        五條之 Final Step **皆無 check target**。
        §5.5 要求 Final Step 自身即揭示所檢查者；
        §5.2B 要求含 `check that ...` / `to verify ...` / `... to check ...`，
        且長度得延伸至 ≤ 18 字以承載該子句。
        12 包版本原有 `... and check that the splash screen is loaded`，
        合併時遺失。

        十條全查並修正。補設閘門 G77 ——
        `test_procedure` 之最末步驟須含 §5.2B 所列之驗證意圖措詞。
        判準詞彙須有經驗來源（比照 R-P83 / R-P88 / R-P96），
        以 Comfort / Privacy 已交付之 `test_procedure` 末步為語料。

        **R-P96 依 R-P36 原文不改**，於其下加註指向本條。
        裁決者 Pei，逐字依據：「出」（回應 13 Q1）。

[R-P102] **時序需求之下界斷言為刻意選擇，須於 `reasoning` 明載。**
        `4942337` 原文僅載 `After SplashScreen_Time the splash screen
        is loaded`，**未載在此之前不得顯示**；
        而 `001` / `004` 之 ER 依 R-P97 所建議之形態，
        斷言「到期前不顯示」。

        兩難為真：僅驗「有顯示」則時序需求形同未測（`T=0` 亦通過）；
        加驗「到期前不顯示」則斷言規格未載之事，
        實作若提早顯示將 false fail（§7）。

        **裁定：保留下界斷言**，但其依據**不是**「規格禁止提早顯示」，
        而是**時序需求之可驗證性要求** —— 不設下界，該需求無法被證偽。
        此推理須於各該 TC 之 `reasoning` **逐字記載**，
        使 reviewer 得見其為刻意選擇而非誤讀。
        不得於 ER 中暗示規格明文禁止。
        裁決者 Pei，逐字依據：「出」（回應 13 Q2）。

[R-P103] **`006` 之時序表述須查證。**
        `4942338` 原文為
        `process it according to the transitions ... **while the boot is
        still completing**` 及 `process them as soon as possible,
        depending on boot timings`。
        而 `006` 之 `tc_title` 為
        `Buffered events processed **after boot completes**`。
        規格所載為「開機期間即依轉換處理、儘快處理」，
        非「開機完成後才處理」。
        查證 `006` 全文；若確為誤讀，`tc_title`、`test_procedure`、
        `expected_result` 一併改為與原文相符之表述。
        裁決者 Pei，逐字依據：「出」（回應 13 Q3）。

[R-P104] **`source_clause` 欄位立為常規。**
        13 包之 `batch_001_power_down.json` 於 `leaves` 陣列中
        附各 leaf 之 `source_clause`（規格原文子句）。
        該欄位**使技術覆核成為可能** —— 無之則覆核者僅能檢視
        TC 自我證明之一致性，無法判斷其是否忠於規格。
        往後每批之產出 JSON **必附**此欄位，逐 leaf 給出
        其被引用錨點之規格原文（不得節錄至失去語意；
        若過長，須以 `...` 標明截斷處並另附全文檔）。
        寫入 Power profile。
        裁決者 Pei，逐字依據：「出」（回應 13 Q6）。

[R-P105] **首批覆核之進度與剩餘範圍。**
        分析層已覆核 `001`–`005`、`010`，共 **6 / 10**，
        並以三條 leaf 之 `source_clause` 原文對照。
        **已確認之正面結論**：
          `SWE-PM-071` 之四項規格行為由 `001`–`004` 一一對應，
          無遺漏、無擴張（§8.2.1 / §8.2.2 通過）
          `010` 之「20」與「10 秒」皆有逐字規格出處（§8.4.1 通過）
        **剩餘**：`006` / `007` / `008` / `009` 四條未讀。
        本包上繳須附該四條全文，順序置於最前。
        R-P98 於分析層完成十條覆核前維持有效。
        裁決者 Pei，逐字依據：「出」（回應 13 Q4、Q5）。

[R-P106] 13 §七之其餘各項處置：
        （甲）第 2 項（`008` 未經 G73 任何觸發，品質全靠人工判斷）
              —— 屬 R-P105 之覆核範圍，本包由分析層補讀
        （甲）第 3 項（對著閘門改而非對著規則改）
        （丙）第 7 項（先看答案再定門檻）
              —— **二者登記為結構性限制，不另設機制**。
              執行層已將三次門檻實測值留於報告與程式碼註解，
              使該選擇可被後續檢驗，此處置正確。
              二者無法以更多自我檢查解決 —— 其解方即為
              分析層之獨立覆核（T3 於閘門 0 觸發之情形下由分析層抓出，
              即為此機制生效之實證）。
        （甲）第 4 項（G73 判準與已交付實務不一致）
              —— **登記不阻斷**。依 R-P94 執行層不得判定
              Comfort / Privacy 之交付件有無缺陷；
              G73 觸發時之人工裁決由分析層承擔。
        （乙）第 5 項（G75 完備性原理上不可驗）
              —— **接受「不可驗」之標示**，不得改標 PASS。
        （乙）第 6 項（G74 形態基礎僅二實例）
              —— **接受並明載其強度低於 G73 / G64 / G51**。
        裁決者 Pei，逐字依據：「出」（回應 13 Q5）。

（以上**六條**裁決條文，抄入 RULINGS.md 時逐字保留，
 每條獨立區塊，不得夾於敘述中。）

## B. 本包須產出

### B1. `006`–`009` 四條全文 —— **置於上繳包最前**

十三欄逐條，含 `reasoning` 與該 leaf 之 `source_clause`。
**不得節錄、不得省略換行。**
分析層兩次因讀取上限而覆核不全（A-PW55），故置前。

### B2. R-P96 之加註（R-P101）

依 R-P36 原文不改，於 R-P96 下加註：

  「註記（R-P101，14 包）：本條令『無可觀察結果之步驟應合併』，
   未規定合併後之 Final Step 仍須符 §5.2B / §5.5，
   致 12 包原有之 `and check that ...` 子句於 13 包合併時被剝除，
   六條已讀 TC 中五條之 Final Step 無 check target。
   驗證意圖之要求已由 R-P101 補足。原文保留。」

加註後須以雜湊佐證原文位元組未變。

### B3. 十條之 Final Step 修正（R-P101）

逐條檢查並修正 Final Step，使其含 §5.2B 之驗證意圖措詞。
**須逐條列出「13 包版 / 本包版」對照。**

**注意**：
  §5.2B 允許 Final Step 延伸至 ≤ 18 字以承載該子句
  修正不得破壞 G63（1:1）、G73（不得複述）、§10.5（≥ 2 步）
  修正後重跑完整 lint

### B4. G77 實作（R-P101）

  偵測 `test_procedure` 末步是否含驗證意圖措詞
  判準詞彙以 Comfort / Privacy 已交付之 `test_procedure` **末步**為語料導出
  依 R-P80，僅用其結構性事實（末步為驗證步驟），不引用內容裁決
  回報：語料條數、導出之措詞清單、對本批十條之實測
  合成 fixture ＋ 真實實測二者皆須回報，依 R-P99(c) 明標證據型別

### B5. R-P102 之 `reasoning` 補述

  `001` / `004`（及其他採下界斷言者）之 `reasoning` 逐字補入：
  下界斷言之依據為**時序需求之可驗證性要求**，非規格明文禁止；
  不設下界則該需求無法被證偽。
  ER 措詞不得暗示規格明文禁止。

### B6. `006` 之時序查證（R-P103）

  引 `4942338` 原文逐字
  對照 `006` 之 `tc_title` / `test_procedure` / `expected_result`
  判定：誤讀 / 未誤讀，附逐字依據
  若誤讀，一併修正三欄並重跑 lint

### B7. `source_clause` 入 profile（R-P104）

  Power profile 增訂條款：每批 JSON 之 `leaves` 陣列必附 `source_clause`
  補設閘門或檢查（若可機械化），否則明列為不可機械檢查並說明理由

## C. 抽取規格

  §C rule 1 / 2 / 3 / 4 正則不變。
  R-P17 文字層定義不變。
  `MIN_FINGERPRINT = 40` 不變（R-P62）。

## D. 閃點

G0 為前置閘。G0–G16、G13b、G18–G76 沿用（G17 已移除），期望值不變。

| # | 項目 | 期望值 |
|---|---|---|
| **G77** | Final Step 驗證意圖（R-P101） | fixture 正常 PASS、違規實際 FAIL；**十條修正前之實測數須回報**；修正後 0 findings |
| **G78** | `006` 時序表述（R-P103） | 【實測填入】誤讀與否；若誤讀則修正後與 `4942338` 原文相符 |
| **G79** | `source_clause` 必附（R-P104） | `leaves` 陣列 3 / 3 皆有 `source_clause` 且非空 |
| **G80** | R-P96 加註後原文位元組未變（B2） | UNCHANGED |
| **G63** | Procedure ↔ ER 1:1（沿用） | 修正後仍 10 / 10 |
| **G73** | ER 複述偵測（沿用） | 修正後仍 0 findings |
| **G70** | 修正後 lint 全閘（沿用） | 全 PASS；leaf 仍 3；TC 仍 10 |

G77 之驗證條件同 G33，且依 R-P99(c) 須明標證據型別。
**G77 對十條修正前之實測數為必報項** —— 若修正前實測數低於 5，
表示分析層之判定或本閘之判準有一方有誤，須停並上繳。

## E. framework

§E 已定版（R-P35），本包不動。

## F. Anomaly 異動

  A-PW59 → 依 R-P101 更新：R-P96 為分析層條文造成實質退步之**第二例**
           （第一例為 R-P87 導致 ER 複述）
  新增 A-PW64：R-P96 之「合併步驟」剝除 Final Step 之驗證意圖，
               五 / 六條已讀 TC 中招，而 G63 / G73 / G70 全數 PASS ——
               **閘門全綠而 §5.5 違反**，為「閘門覆蓋不等於品質」之直接實例
  新增 A-PW65：時序需求之下界斷言為規格未載之事，
               保留係基於可驗證性而非規格明文（R-P102）
  新增 A-PW66：`source_clause` 欄位為技術覆核之必要條件；
               無之則覆核者僅能檢視 TC 之自我一致性（R-P104）

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
  2. 輸出 B1 `006`–`009` 四條全文 —— **置於上繳包最前**
  3. 依 R-P101 為 R-P96 加註（B2），驗 G80
  4. 依 R-P101 修正十條之 Final Step（B3），逐條列前後對照
  5. 實作 B4 G77，含合成 fixture 與真實實測，驗 G77
  6. 依 R-P102 補 `reasoning`（B5）
  7. 依 R-P103 查證並修正 `006`（B6），驗 G78
  8. 依 R-P104 將 `source_clause` 寫入 profile（B7），驗 G79
  9. 修正後重跑完整 lint，驗 G63 / G70 / G73
 10. 以 §D 全表自驗
 11. §A 六條裁決逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
 12. 上繳 features/power/docs/upstream/14_final_step_intent.md，更新 docs/INDEX.md

## I. 禁區

  **不得寫回 FW036 workbook（R-P98 / R-P101 未完成前一律不開放）**
  **不得對任何 workbook 呼叫 `save()`**（R-G3）
  不得執行任何 git 操作（全數屬 Pei）
  不得補齊 SWE-PM-089（R-P1）
  不得沿用純文字衍生物之任何數字（R-P10）
  不得自行調整 §C 正則
  不得修改任何已落檔裁決條文之內文（R-P36）
  不得測試未被引用之錨點（R-P42）
  不得解析任何 RTF 或 OLE stream 之內容（R-P39、R-P48）
  不得續行章節層反向缺口調查（R-P37）
  不得自行調整 §E（R-P35）
  不得因 A-PW46 / A-PW51 改變車型欄之留白處置（R-P54、R-P81）
  不得修改 Comfort 之任何交付物（R-P94）
  不得調整 `MIN_FINGERPRINT`（R-P62）
  不得擴大批次範圍超出 `Power Down` 3 leaf
  **不得於 ER 中暗示規格明文禁止提早顯示（R-P102）**
  **G77 之判準詞彙不得憑印象列舉，須有經驗來源**
  不得以 repo 現況作為任何 fixture 之測試對照
  素材補入超出 features/power/inputs/ 需 Pei 裁定

## J. 本包產生之新條文清單（自檢）

  R-P101 Final Step 須含驗證意圖，合併不得剝除（G77）
  R-P102 時序需求之下界斷言為刻意選擇，須於 reasoning 明載
  R-P103 `006` 之時序表述須查證
  R-P104 `source_clause` 欄位立為常規
  R-P105 首批覆核進度：已 6 / 10，剩 `006`–`009`
  R-P106 13 §七其餘各項之處置

  逐條確認：**六條**，皆以獨立區塊呈現於 §A，未夾於敘述中。
  自檢：§A 區塊數 = 6、§J 列數 = 6、§H 步驟 11 寫「六條」，三處一致。
