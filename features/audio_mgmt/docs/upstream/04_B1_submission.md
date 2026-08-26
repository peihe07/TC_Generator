# Audio Management — 上繳包 04：Batch B1 交付

- Feature slug：`audio_mgmt`
- 日期：2026-08-26
- 對應下放包：`docs/handoff/03_batch_B1_handoff.md`（B1 生產指令）
- 執行層：Claude Code
- 依據裁定：R-AM1–R-AM12、R-AM2′（Pei 2026-08-26「2採 R-AM2′准 DR-AM3發」）

---

## 一、交付摘要

| 項目 | 值 |
|---|---|
| 批次 | B1 |
| 葉數 | 50／50（Source Transition 34 ＋ Audio Arbitration 16） |
| TC 數 | 70 |
| Test Set 分佈 | Source Transition 48，Audio Arbitration 22 |
| Priority 分佈 | P0 33，P1 37 |
| 帶 PENDING 之 TC | 8（DR-AM4 五條、DR-AM5 三條） |
| 池外錨（R-AM2′） | 7 |
| TC JSON | `features/audio_mgmt/generated/B1.json`（十鍵全備） |
| 寫回簿 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext_B1.xlsx` |
| 寫回簿 SHA256 | `5cb02ecd1933a3890897f6c157ed376520c2f3b2b5453e46113d861951a239af` |

**產出量（rev 2，2026-08-26）：** 首版交 57 條，低於 03 包 §六 之 60–75 估計。
經加密至 **70 條**，落入估計區間。加密之取捨原則：只在條款本身帶有分支、
列舉成員或方向而首版僅覆蓋其一處增列，**不為湊數而拆**——每一條新增皆命名
一個「其 sibling 通過時它仍可能單獨失敗」之行為。實例：

- 4866875 之來源對應表三列（DAB／FM／SDAR）補齊第三列；
- 4866726 之三種 SOS call type 由二種補至三種，回復側亦同；
- 4866452 補反向（低優先權不得取代高優先權）與 4866879 補不允許之組合，
  二者皆為負向測試——只驗正向者，一個「照單全收」之實作會通過；
- 4866465 之佇列兩個出口（取得優先權／來源轉為非作用）補齊第二個；
- 4866468／4866493 之媒體功能清單補至三種（seek／scan／disc、PTY seek／tuning）；
- 4866715 之 pause 與 mute 兩種處置補齊；
- 4866844 之 Information 分支補入（該分支錨值可解，不必如 Entertainment
  分支掛 DR-AM5 之 PENDING）。

未加密者亦有理由：單一 shall 陳述之葉強拆會產生逐字相同之括號下半而違 R-S4。

## 二、§9 自檢通過聲明

`features/audio_mgmt/scripts/selfcheck_b1.py`，70 條全數通過。檢查項：

尾句號禁令、ER 無情態動詞、canon §5.1 步驟禁用動詞、canon §5.5 末步須持
可觀察標的、步數↔ER 對齊、design_method 屬下拉選單詞彙、spec_reference
一 ID 一行且前綴齊、req_id 為 R-AM7 底線式、test_item 兩段式、
Test Group 恆為 `Audio Management`、Priority 值域、交付欄無 CJK、
同 req_id 括號內容不得逐字相同。

**自檢曾攔下執行層自身之錯誤，記於此以留痕：** 初版自檢要求末步以 `Verify`
開頭，與 canon §5.1 之禁用動詞條文**直接牴觸**（誤將 §5.5「末步須持有可
觀察之驗證標的」讀為字面 Verify）。加入 §5.1 檢查後暴露 76 個違規步驟、
散在 57 條中之 50 條，已全數改寫為 Read／Measure／Record／Compare／Confirm
（均不在禁詞表），非同義詞規避。`gen_b1.py` 現於產出前即擋，違規步驟無法生成。

**步驟 1 提示之校準：** 初版判準「步驟 1 非 Confirm/Read/Record」於本批命中
53/57、於 time_management 語料命中 27/35 —— 係在標記主流合法寫法，判為雜訊
而非訊號。改為「pre_conditions 為 NA **且** 步驟 1 直接施加刺激」後，
time_management 語料 0/35（不誤報），本批隔離出 22 條真缺口，已逐條補上
pre_conditions，現提示為 0。

## 三、Lint 報告

`features/audio_mgmt/scripts/lint_tcs.py --profile audio_mgmt` → **green**。

**十六項全實作**（rev 2）：A（§5.1 步驟禁用動詞）、B（ER 情態詞）、
C（test_item hedge 與情態詞）、D（Pre-Condition 形態 §4.4）、E（步驟↔ER 對齊）、
F（方括號 §11）、G（test_set 封閉詞彙）、H（ER 模糊詞 §6）、I（括號尾）、
J（行首大寫 R-4）、K（交付欄 CJK）、L（verbatim 上半 token 上限 R-3）、
M（必填欄三態）、N（行尾句號）、O（spec_reference 格式）、P（§8.7.5 **v3**）。

**首版之揭露：** rev 1 交付時 C／D／F／H／J／L **六項尚未實作**，
故當時之「lint green」所涵蓋之範圍小於其字面。六項補實作後 B1 重跑
——**七十條在十六項下全綠，無新違規**。八個 must-hit 反證確認六項各自
攔得住其標的且不誤報正常條目（未曾觸發過之檢查不構成證據）。

**`--profile` 為必填之理由：** 共用 lint 之檢查 P 仍以 §8.7.5 **v2** 判準
實作（`Send CAN:` 前綴，該版已於 2026-08-21 撤銷）。本 feature 用全域 v3
預設、未宣告 `[OVERRIDE §8.7.5]`；以 v2 判準跑 v3 文本會把每一行正確寫法
報成違規。故本腳本要求明示 profile，profile 不符即拒跑，不猜。

**檢查 P 之 must-hit 反證**（防止永遠通過之 gate）：v1 三件組、v2 `Send CAN:`
前綴、PROXI 加 `$`、DBC 有此訊號卻未寫全名、值非 `= <raw> (<label>)`
—— 五種全數攔下；正確 v3 寫法放行。

Lint 之 24 條 note 全為 DR-AM4／DR-AM5 項目，無其他。

## 四、寫回驗證

寫回**一律走 XML 手術**（`backend.xlsx_surgical.surgical_save`），
openpyxl 僅作記憶體內之 diff 來源、絕不 `save` —— openpyxl 存檔會剝除
`xmlns:x14` / `xmlns:xm`，毀掉受控表單之 data validation。

| 驗證項 | 結果 |
|---|---|
| zip 成員集 | 48／48 不變 |
| 受改成員 | 僅 `xl/worksheets/sheet6.xml` |
| `<dataValidation>`（classic） | sheet6 = 3，不變 |
| `x14:dataValidation` | sheet6 = 1，不變 |
| `<conditionalFormatting>` | 不變 |
| 追溯性 | 57 列 req_id 逐列回讀比對，全符 |
| 完整性 | 葉集合前後一致，無增減 |

**兩點必須揭露：**

1. 本次母本之 `<conditionalFormatting>` 計數為 **0**，故該檢查為
   vacuously true，**實際上未被考驗**。其價值在於未來換用含 CF 之母本時
   能攔下，不宜以本次綠燈為其有效性之佐證。
2. 共用模組 `verify_structure` **不計** `<conditionalFormatting>`，且該缺口
   無法由其既有三項補起（目標 sheet 本就允許位元組差異）。已於 feature 端
   自補，未逕改共用模組（十五個 feature 共用，新增 raise 型硬 gate 可能
   使他 feature 既有寫回失敗）。登記 A-AM06，建議由掌握全案者評估上收。

## 五、池外錨登記表（R-AM2′ 要求）— **rev 3：本表作廢，B1 無池外錨**

> **更正（A-AM13）**：本節原列七葉為池外，係執行層池抽取之缺陷所致 ——
> `fullmatch` 只認整格單一 ID，漏掉 58 個多值格共 86 個 ID。以展開池 v2
> （891 ID）複驗，**七葉之錨全部在池內**，B1 之池外錨數為 **0**。
> 該七葉即 A-AM03 之原始證據與 R-AM2′ 之立法事實基礎，兩者對 B1 皆前提落空。
> 交付欄摘要重生前後一致（`1385996c…`），工作簿未重寫。
> 以下原表保留供追溯，**不再具效力**。

七葉之錨不在 R-AM2 主池（兩本 Basic Report），取自全文 PDF 之
`State:Approved` 物件，已雙路核驗。各條 reasoning 均註明「池外錨，全文佐證」。

| SWE ID | 錨 | Title |
|---|---|---|
| SWE1_AMM_138 | CFTS019-4866479 | Entertainment Source Transition Timing |
| SWE1_AMM_156 | CFTS019-4866520 | Entertainment to Information Transition Timing |
| SWE1_AMM_157 | CFTS019-4866522 | Information 1 to Information 2 Transition Timing |
| SWE1_AMM_200 | CFTS019-4866839 | Non-Arbitrated Source Transition |
| SWE1_AMM_205 | CFTS019-4866850 | Entertainment-to-Entertainment Source Transition |
| SWE1_AMM_240 | CFTS019-4866956 | Arbitrated Signal Source Transition |
| SWE1_AMM_241 | CFTS019-4866967 | Arbitrated Information Source Transition |

七者均為「Refer to figure」型：行為序列以圖說附文＋SWE.1 Description 為據；
時序值循 IN §8.4.1 不造值 —— 僅於具名參數可解者（4867766／4867767／
4867768／4867769／4867773）引用，其餘只驗相位順序。

## 六、PENDING 清單（IN §8.4.3；出貨前須清）

| SWE ID | DR | 內容 |
|---|---|---|
| SWE1_AMM_136 | DR-AM4 | DR-AM4 $HUModeStatus$ not found in the supplied DBC |
| SWE1_AMM_203 | DR-AM5 | DR-AM5 <Temp Ramp Down> value not defined in available sources |
| SWE1_AMM_206 | DR-AM5 | DR-AM5 <Temp Ramp Down> value not defined in available sources |
| SWE1_AMM_208 | DR-AM5 | DR-AM5 <Temp Ramp Down> value not defined in available sources |
| SWE1_AMM_212 | DR-AM4 | DR-AM4 $HUModeStatus$ not found in the supplied DBC |
| SWE1_AMM_213 | DR-AM4 | DR-AM4 $HUModeStatus$ not found in the supplied DBC |
| SWE1_AMM_213 | DR-AM4 | DR-AM4 $HUModeStatus$ not found in the supplied DBC |
| SWE1_AMM_216 | DR-AM4 | DR-AM4 $HUModeStatus$ not found in the supplied DBC |

## 七、未結 DR 清單

| DR | 內容 | 狀態 | 卡批？ |
|---|---|---|---|
| DR-AM1 | SWE1↔CFTS ObjectID 正式對照表缺失 | 待 Pei 送出 | 否（R-AM2 內容對位過渡） |
| DR-AM2 | SWE1_AMM_076 編號碰撞（-242/-246 同號） | 待 Pei 送出 | 否（076 不在 B1） |
| DR-AM3 | Basic Report 系統性遺漏圖表型物件（在池率 7.7% vs 39.0%） | **Pei 已裁發 2026-08-26** | 否（R-AM2′ 解） |
| DR-AM4 | 供應之 DBC 缺 `$HUModeStatus$` 與 `$VolumeENT$` | 待 Pei 送出 | 否（R-13 (g) 保留原文名） |
| DR-AM5 | `<Temp Ramp Down>` / `<Temt Ramp Down>` 全文未定義（疑為 `<Tent Ramp Down>` 拼寫錯誤） | 待 Pei 送出 | 否（行為面已驗，僅界值待補） |

## 八、本批之 reasoning 彙整（要點）

逐條 reasoning 存於 `generated/B1.json` 各 TC 之 `reasoning` 鍵。共通判斷：

1. **sibling 區分**：同文異錨之近重複組（130／139 queue 判定、198／199 與
   218／219 之 SOS 靜音回復、211／215 之啟動情境、166／167 之 activate/re-mix）
   一律令兩條各取條款之不同可觀察面，使括號內容與 ER 均可辨，非改寫措辭充數。
   SOS 四條並分取 Manual／Automatic／Callback 三種 call type，避免重複同一值。
2. **邊界值**：275–278 各拆下界／上界兩條（IN §12），值取 4867766–4867769
   之 25ms／50ms 實值。
3. **時序值一律溯源**：凡引用數值者均指回具名參數之定義列，未定義者填 PENDING，
   不以鄰近值代入。
4. **訊號**：`$SOSCallType$` 於 DBC 查得 `TBM_FD_1.SOSCallType`，`VAL_` 標籤
   與 CFTS 原文逐字相符，依 §8.7.5 v3 全式寫入；`$HUModeStatus$`／`$VolumeENT$`
   查無（已掃 2,260 個訊號），依 R-13 (g) 保留原文名，未以近似訊號代換。
5. **verbatim 上半**：由 `gen_b1.py` 自 `B1_context.json` 直讀 SWE.1 原文，
   不手抄，逐字性由程式保證。唯一之改動為剝除結尾句號（交付欄禁尾句號），
   比照 time_management 語料（其 B1 十九條上半無一以句號結尾）。
   超過 R-S4 之 50 token 者三條（223／224／225），縮寫並以
   specification_reference 指回原條款。

## 九、待分析層裁定

1. DR-AM4／DR-AM5 是否送出上游。
2. 產出密度是否加密（現 57 條 vs 估 60–75，理由見 §一）。
3. A-AM06 之共用模組 CF 檢查是否上收為通案。
4. B2 之下放：Audio Arbitration 剩餘 13 葉 ＋ 下一個 Test Set 之葉/錨表尚缺
   （§四 型表格屬分析層產出；執行層不得自行改錨）。執行層已備妥候選錨表，
   見 `docs/upstream/05_B2_anchor_proposal.md`，僅為提案，不具裁定效力。
