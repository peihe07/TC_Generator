# Audio Management — 上繳包 17：Batch B4 交付（綠色通道首批）

- 日期：2026-08-26
- 對應下放包：`13_B4_anchor_candidates.md`（第一路）、`16_B4_final_anchors.md`（定案）
- 對應對帳：`15_B4_route2_reconciliation.md`（第二路）
- 依據：R-AM1–R-AM20

---

## 一、交付摘要

| 項目 | 值 |
|---|---|
| 批次 | B4（Volume Control 後 13，含自 B3 遞延之 194 ＋ Audio Sources 37） |
| 葉數 | 50／50，**零無錨葉** |
| TC 數 | 51 |
| Test Set | Audio Sources 35，Volume Control 16 |
| Priority | P0 9，P1 42 |
| 設計方法 | 功能測試 20，狀態轉換 14，決策表 12，邊界值分析 3，負向測試 2 |
| 池外錨 | **6**（見 §五之爭點） |
| 併列雙錨 | 1（SWE1_AMM_020） |
| PENDING | DR-AM4 21 項次（訊號）、DR-AM5 2 項次（204／207 之時序值）；**無葉級 PENDING** |
| 交付簿 | `SWQT_AudioMgmt_B1-B4.xlsx`，**250 列**，tc_id `NR1L-AMM-001`–`250` |
| SHA256 | `042be1ceadf8a051c97acfc682ea5191b5091a72a267b8821698d048f313cb9c` |

累計 B1–B4：250 條／200 葉（318 葉之 **63%**）。

## 二、§9 自檢與 Lint

自檢 51 條全過；`lint_tcs.py --batch B4 --profile audio_mgmt` **green**（十六項）。

**自檢／lint 於本批之攔截**：R-3 逾限一條（003，摘句處理）。
另於撰寫 256 時發現**檢查本身之缺陷**，見 §六。

## 三、§7 列舉配對三組（全數成對交付）

| 組 | 兩支 | 分野 |
|---|---|---|
| 306 兩分支 | 座艙音量高 → 取「低於座艙 15 dB」／座艙音量低 → 取 step 6 底線 | `whichever is greater` 之兩側；只驗其一則底線分支未受檢，而底線正是保障可聞度者 |
| 264／266 | Surround 存在 → 選單啟用／不存在 → 選單移除且不可變更 | 忽略設定之實作會通過與其預設相符之一半 |
| 256／257 | LHD → 駕駛側音訊導左／RHD → 導右 | §7 列舉，包 13 §四.4 要求成對 |

**負向缺口之揭露（不擴編）**：4867568 處理 `$DriverSide$` 無效值→
{CIP Default Settings} 預設，**無對應 SWE.1 葉**。屬上游分解之負向路徑
缺口，已於 256／257 之 reasoning 揭露；依 IN §8.2.1 上游分解為權威，
執行層不自行補葉。

## 四、逐案落實（對應包 16 §二、§三）

| 葉 | 定案 | 落實 |
|---|---|---|
| 002 | 改錨 4865913 | 已採。TC 觀察路徑指派，與 001 之立體聲再現分工 |
| 122 | 改錨 4866444，部分覆蓋 | 已採。僅驗仲裁依表執行，未寫 Routing Table 內容 |
| 145 | 4866497 | 第二路解出；與 B1 之 144（4866494）不同物件，無須共錨論證 |
| 155 | 4866513 | 同上；與 B1 之 154（4866512，音量位準）分屬通道面向 |
| 020 | 併列 4865981 ⏎ 4866286 | 已採，升冪兩行。TC 驗路由（前聲道最低要求），不驗 {CFTS024} 之啟用細節，不掛 DR |
| 024 | 4866001 | 已採。reasoning 註明錨為**內嵌表格物件**（匯出 Description 為 image 參照），輸出對映表內容不轉抄 |
| 146 | 4866498 | 已採。`<Tent Ramp Down>` 有定義（4867767），實值 25–50 ms 入 TC；**與 204／207 之 `<Temp Ramp Down>` 不同參數，後者掛 DR-AM5** |
| 210 | 複合 ER 一條 | 依包 13 §四.5，五訊號同一觸發不拆 |
| 148/149、151/152、162/163、164/165 | 啟停分支四組 | 依 §8.2.2 判準各自成條：每葉各有其物件與訊號，且系統可能置旗標而遺留舊 type，括號下半註明本列觀察 Active 或 Type |
| 272/273/274 | 變數定義錨 | 包 13 §四.1 之續查已執行：sleep-resume 段 4867742–4867749 實為 VirtualConcertHall／ANC，**無行為物件**，維持變數錨單列 |

## 五、池外錨登記表 —— **與包 16 §一 不一致，待裁（A-AM10）**

執行層交付之池外集合為 **6 葉**：

| 葉 | 錨 | Title | 佐證 |
|---|---|---|---|
| SWE1_AMM_264 | CFTS019-4867598 | Audio Management - Enable Surround Sou | 單源佐證 |
| SWE1_AMM_266 | CFTS019-4867604 | Audio Management - Disable Surround So | 單源佐證 |
| SWE1_AMM_306 | CFTS019-4866207 | Audio Management - Default Alert Volum | 單源佐證 |
| SWE1_AMM_307 | CFTS019-4866208 | Audio Management - Default Alert Volum | 單源佐證 |
| SWE1_AMM_308 | CFTS019-4866242 | Audio Management - Speed Volume Contro | 單源佐證 |
| SWE1_AMM_311 | CFTS019-4866914 | Audio Management - Navigation Audio Pr | 單源佐證 |

包 16 §一 記為 5 葉（撤除 264）。**執行層複驗不支持該撤除**：

> 方法：逐格掃描兩本 Basic Report 之**每一儲存格**（非僅 ObjectID 欄），
> 比對字串 `4867598`。Part 1（245 物件）0 命中，Part 2（566 物件）0 命中。

包 16 所述之覆核依據為「匯出與全文同文」，惟該觀察**無法區分**
「兩處皆有且一致」與「僅全文有」。研判所讀者為全文。

**待裁**：以何者為準。若包 16 另有依據（如 `inputs/` 以外之匯出版本），
請指明；否則建議更正 §一，將 264 併回池外集合。交付暫依實測維持 6 葉。

**包 16 §一 對 311 之指正全盤接受**：15 包 §一 將 A 級 30 葉整批掃入
逕寫段而未先過池籍過濾，確違 R-AM20 除外條款。程序已改 ——
逕寫集合先過池籍過濾再併入，A 級標記不豁免池外檢查。

## 六、執行層自身缺陷之攔截與更正（本批兩件）

### 六.1 sibling 區分檢查取錯字串（已修，四批複驗）

自檢與 lint 之「同 req_id 括號下半不得逐字相同」以
`test_item.split("(", 1)[1]` 取括號尾。**當 verbatim 上半自帶括號時，
該式會伸進規格原文**——SWE1_AMM_256 之上半含
`(navigation prompts, warnings, chimes, etc.)`，檢查遂以規格片段互比，
而非它存在的目的：比對作者所寫之括號尾。

修正：改自最後一個 `\n\n(` 切分。**B1–B4 四批以修正後之檢查全部重驗，
仍全綠**（無先前被遮蔽之真違規）。

### 六.2 第二路三次漏查之共通機理（A-AM11）

包 16 §三 推翻執行層對 020／024／146 之「維持 PENDING」建議。
三次原因各異，但同屬檢索方法層級：

| 葉 | 漏查原因 |
|---|---|
| 020 | **讀取截斷**。4865981 全文為「can be played on all channels, **but at a minimum shall be played on the front channels**」；輸出截於 135 字，只見前半即判範圍不符。**駁回理由建立在未讀完之句子上** |
| 024 | **未搜葉本身**。該葉 SWE.1 描述原文即載 `CFTS019-4866001`；且該物件為內嵌表格，匯出 Description 為 `(image: ….rtf)`，文字檢索本不可達 |
| 146 | **詞形單一**。搜「remaining channel」，原文為「remaining **audio** channels」 |

連同 A-AM08（`<Vent off>` 大小寫敏感）共四例。共通處：
**以單一詞形／單一視窗之檢索結果作為否定結論之依據**。
否定結論比肯定脆弱 —— 肯定只需一個命中，否定需窮盡。

改善（執行層自酌，未立條）：route2 腳本輸出不截斷；檢索前先掃葉之
SWE.1 描述中之 `CFTS019-\d+`；檢索詞加單複數與同義擴充；
匯出 Description 為 image／wrapper 者另行標記。

## 七、寫回驗證

48 成員不變、僅 `sheet6.xml` 受改、`<dataValidation>` classic 3 ／ x14 1 不變、
`<conditionalFormatting>` 不變（母本計數 0，vacuously true）、
逐列回讀 51 列追溯性與完整性全符、累積 250 列 tc_id 001–250 無重複無缺號。

## 八、未結 DR（八件）

DR-AM1（另收 122 之 Routing Table）、AM2、AM3（全文件重匯）、AM4、AM5、
AM6、AM7、AM9。DR-AM8 已撤（R-AM17）。

## 九、待分析層

1. **A-AM10：264 之池籍**（§五）——本包唯一待裁項。
2. DR 送出與否。
3. B5 之下放（Tones and Alerts 32 ＋ Audio Processing 前 18）。
