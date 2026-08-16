# DATA REQUESTS — Comfort (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/comfort/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（下放包 01 §5.5；沿用 AMFM／Privacy）**：任何新發現之外部
引用，登記 anomaly 的同時**必須**新增一列於此表；且每次 session opener 與
batch gate 都要按 Urgency 回報。

> 建檔時（2026-08-14 Phase 1）**無已知缺檔** —— 037 所引用之唯一文件
> （SR24 CR24879）已在 `spec-index/`，129 節逐一查得，miss = 0。本表非空，
> 但列的是「非檔案」與「環境」兩類請求，不是缺檔。
>
> **更新 2026-08-14（下放包 06 §3 判讀後）**：**現有兩項真正的缺檔**
> —— #6（R1LR ATL-H 機種／螢幕尺寸配置）與 #7（EMEA 市場適用性）。
> 兩者各自阻擋 6 節與 1 節之適用性判定，合計 7 節維持 `undetermined`。
> **此為缺料，非判定** —— 依 06 §3，讀不到即 `undetermined`，
> 不得以讀不到判 `out_of_scope`。
>
> **更新 2026-08-14（二）（下放包 08 素材落位後）**：#7 **已解**、
> #6 **限縮至 7" 單一問題**（3 節）。兩者皆**非由 #9 之素材解決** ——
> Market Configuration Table 不承載 R1L-R 亦不承載螢幕尺寸；解答來自
> 037 自身之引用結構（詳 A-CF08）。**現行唯一真正缺檔為 #6**。
>
> **次要候選之處置**：08 §3 列 `VINtoArchitecture decoding v3.xlsx` 與
> `Vehicle Category HMI Logic and Flow R1 SR24 Post 2A`。後者已在
> `spec-index/sources/`，依 08 §3「取用前須先驗其確實承載該資訊」實測
> —— **驗不過**（見 #10），不採用。前者全 repo 搜尋**不存在**，
> 若 Pei 判斷其可能承載螢幕配置，需補入（Tier 3）。
>
> **更新 2026-08-14（三）（下放包 09／10）**：#8 轉 **DEFERRED**（Pei 對 RD）、
> #3 **已解**（recon 加 `pdftotext` fallback）、#10 之性質由「不存在」訂正為
> 「**客戶端存在，待 Tier 3 補入**」（09 §4）。10 §3 之 Home Screen HMI L&F
> 已在 repo（`spec-index/cache/`），但**不關閉 #6** —— 其機種列舉與
> `Available Widget Size` 兩表皆為平台配置，非交付範圍宣告。
> **現行唯一真正缺檔仍為 #6，且 09 §5 已改為請 Pei 直接指認來源**：
> 分析層兩次指名候選皆驗不過，再猜只是消耗驗證輪次。
>
> **更新 2026-08-15（三）（下放包 21）**：新增 #16 —— Core N0／CFTS044 之
> **涵蓋**問題。#13／#14 問的是「要不要取得該文件」（答：不需要，已判 out
> of scope）；#16 問的是**不同的問題**：那些行為在本專案有沒有任何 SWE 需求
> 涵蓋。**若無，即為真實 coverage hole**，而那不是範圍界定能解決的。
>
> **更新 2026-08-15（下放包 19）**：新增 #12（跨 feature，依 **R-C21** 登於
> 本帳並具名對象 `home`）、#13／#14（兩份外部 spec，其內容已判 out of scope，
> **Low，不需補入、不阻塞**）。三者皆不影響 Comfort 之生成。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | Comfort 之 FM-WI-FSM-036-A01 TC workbook | ⚠️ **以空白通用範本代替** —— `inputs/…_SWQT_20260121.xlsx`，rev C，SHA256 `cd876c202c71e74b…`（與 Privacy 同一份）。`workbook_state` = BLANK，P4 未阻塞。殘留：非 Comfort 專屬，封面／Scope／Purpose／Reviewer 待填；第 10–11 列樣本待清 | 全 403 leaves | P4 起全部批次 | A-CF07 | Low（僅待確認交付形態） |
| 2 | Scope / Purpose / Reviewer / Project Name / Date 五格之填入值 | ⏳ **待 Pei 給值** —— 非檔案，屬 Tier 2 賦值。執行層提案 Scope = `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1`，其餘不自填 | 交付件表頭 | P7 寫回前必須有值 | A-CF07 | **Medium —— P7 之前** |
| 3 | `pymupdf`（Python 套件，非客戶檔案） | ✅ **已不需要** —— 09 §4 授權後，`recon.py` 之 `survey_spec_text_layer()` 已加 `pdftotext` fallback；RECON.md 現印 `text-layer: 62782 chars (via pdftotext)`。兩者皆不可用時才回報 unknown，且訊息同時指名兩者 | 0（不阻塞） | —— | A-CF06 | 已解 |
| 4 | 客戶交付夾之 SR24 附件回填 | ⏳ **待 Pei 決定** —— 交付夾現放 SR25（PDF 13.86 MB / SYS1 xlsx 72.80 KB），與 R-C1 基線不一致。**執行層未複測**（該樹於本 session 不可達） | 0（不影響取材） | P7 交付一致性 | A-CF02 | Low（P7 之前） |
| 5 | CFTS043 —— `SYS1_CFTS043-HVAC Controls and Displays_Tree view_R1L-R scope.xlsx`（914,043 bytes）＋ `R1LR_Atl-H_25PI3.5_Cabin_CFTS_043 HVAC Controls and Displays _SR26_20250909-1852.doc`（2,469,376 bytes） | ✅ **已入 `inputs/`**（2026-08-14，Pei 放入）—— 20.x 十節之判讀已據此完成 | 10 節（20.1 ~ 20.4.3） | D-C10 裁定 | A-CF08 | ~~High~~ → 已解 |
| 6 | **R1LR ATL-H 之螢幕配置來源** —— 單一問題：**7" 是否屬本次交付之螢幕配置**。**09 §5 改為請 Pei 指認來源** —— 分析層兩次指名（Vehicle Category、VINtoArchitecture）皆驗不過 | ⚠️ **未解** —— Market Config Table 不承載螢幕尺寸軸；10 §3 之 Home Screen HMI L&F **亦不關閉本項**（其 Assumptions 與 `Available Widget Size` 兩表皆為平台配置，不宣告本次交付出哪幾種，與 SR24 §1.1 同型） | 3 節（19.1–19.3） | **不阻塞 Phase 3**（占 403 之 0.7%） | A-CF08 | **High（待 Pei 指認）** |
| 7 | **EMEA 市場適用性來源** | ✅ **已解 —— 但不是靠本項素材** | 1 節（16.1）→ 已判 `in_scope` | —— | A-CF08 | ~~High~~ → 已解 |
| 9 | `SR24 R1 Market Configuration Table v1.6.xlsx` | ✅ **已入 `inputs/`**（2026-08-14，Pei 放入）—— 279,779 bytes，SHA256 `ae4cf0b929b033ac…`，對 25PI3.5 之 `ae4cf0b9…` **PASS**。**判讀結果：不承載 `R1L-R`（0 命中）、不承載螢幕尺寸（0 命中）**；其 variant 軸為市場別非機型別 | 0（未直接解任何節） | —— | A-CF08 | 已解 |
| 8 | CFTS043 4803259 之 NOTE 效力確認（非檔案，屬上游釐清） | 🔵 **DEFERRED 2026-08-14（10 §2）** —— Pei 直接向 RD 反應，不由本 pipeline 追。依 R15-2（open PENDING 意為「待裁決」非「待外部條件」）自 open PENDING 移出、自「阻塞 D-C10」清單移除。**20.x 十節 verdict 不因 DEFERRED 而變動**，依 R-C12 維持 `undetermined` | 10 節（20.1 ~ 20.4.3） | 不阻塞 | A-CF12 | ~~High~~ → **DEFERRED（Pei 對 RD）** |
| 10 | `VINtoArchitecture decoding v3.xlsx` | ⏳ **客戶端存在，待 Tier 3 補入**（09 §4 訂正：08 §3 之「同目錄」指客戶端 `25PI3.5/Reference Docs/ECU Specific Reference Documents/`，非 `inputs/`；執行層「全 repo 不存在」之實測正確，性質是**待補入**而非**不存在**）。惟其為 VIN→architecture 解碼表，回答 7" 螢幕問題之可能性低（09 §4） | 3 節（19.1–19.3） | D-C10 裁定 | A-CF08 | Low（09 §5 已改為請 Pei 指認來源）|
| 11 | **HMI Pop Up List** —— 定義 Comfort 各 popup 之內容與行為者 | ❌ **未入 `inputs/`**，`paths.popup_list` 為 null。**新需求（2026-08-15）**：ch11.1／11.2 之 `opens popup and` 是 ch11 與 ch12 之唯一實質差異，而該 popup 究竟是**進入路徑**（中介畫面）或**回饋**（狀態提示），決定 ch11／ch12 應合併或拆回兩組。僅憑措辭推斷不足 | 59 節（`Heated Vented Seats` 組之存廢） | Phase 4 該組；pilot 不受影響 | A-CF13 | **High** |
| 12 | **`features/home/feature.yaml` 之 `done_region.author_value`（對象 feature：`home`）** | ❌ 現值 `Arif`，實際 done region 作者為 `ArifChen`（`forms/…_Home_20260809.xlsx` Z 欄，144 列）。以現值選取得 **0 列** —— `build_remaining.py` 與 `write_back.py` 之 content-hash invariant 均會誤選。**依 R-C21 登於 Comfort 帳上並具名對象；home 之任何檔案未動、亦不代建檔** | 0（Comfort 不受影響） | 0 | A-CF14 | Medium |
| 13 | `HMI Core Logic and Flow`（requirement N0 —— 長按之判定門檻／重複速率／加速曲線） | ⏳ **不需補入**（19 §4.3）—— 其所擁有之內容已判 **out of scope**，取得反而誘使測試越界。列此僅供日後查考 | 0 | 0（不阻塞） | — | **Low** |
| 14 | `CFTS044`（腰靠／側靠級距之量值，及與舊款 4-way rocker 之等效性） | ⏳ **不需補入**（19 §4.3）—— 同上，已判 out of scope，僅供查考 | 0 | 0（不阻塞） | — | **Low** |
| 15 | **腰靠／側靠調整狀態之呈現位置**（非檔案，屬上游釐清） | ⏳ ch13 五節皆未提及 —— 已命名之可觀察量（`Seat Control Popup`／`Seats tab`／`selected option`／`level`／`greyed out`／`error tone`）皆不含顯示位置。**與 #14 不同**：CFTS044 擁有的是級距**量值**，非顯示位置 | 4 條 TC 之 ER（011/012/013/014） | 不阻塞（20 §4 之修法已使 ER 不依賴之） | A-CF15 | Medium |
| 16 | **Core N0 與 CFTS044 對應行為之 SWE 需求歸屬**（非檔案，屬上游釐清；RD-1 候選） | ⏳ `SWE1-HVAC-080-02`／`-081-02` 已依 **R-C24** 產 `[BLOCKED-SPEC]` row。待確認：長按參數（門檻／速率／加速曲線）與 4-way rocker 等效性，於本專案**是否有其他 feature 之 SWE 需求涵蓋**？**若無，即為真實 coverage hole**（§8.4.2），非僅本 feature 之範圍界定 | 2 leaf（已產 BLOCKED row，未遺失） | **不阻塞** | — | Medium |
| 17 | **`2.1` 之 tab 集合由何種配置決定**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ 條文只寫 `up to 4 tabs **depending on vehicle configuration**`，**未述何種配置產生何種 tab**。故 `-01`（tab 數）與 `-02`（順序）無法寫出一個已知的 tab 集合作為 pre_condition —— 任何具體配置皆為造值（R-C28 第一問／§8.4.1）。**此為內容不足，非軸不足**：第十二軸已於 33 §3 增列並已用於 `-03`，`-01`／`-02` 仍不可生成 | 2 leaf（`SWE1-HVAC-001-01`／`-02`）| **阻塞該 2 leaf** | A-CF21 | **High** |
| 18 | **`2.1` 之 037 leaf 與條文於 tab 數與順序不一致**（非檔案，屬上游釐清；**RD-1 候選**）| ⏳ 條文 `up to 4 tabs`、順序含 `Massage`；037 之 `-01` 為 `up to 3 tabs`、`-02` 之順序無 `Massage`。**037 系統性地少了 Massage tab。** 依 **R-C33** 內容以條文為準、單位以 037 為準，故**處置已定、不阻塞**；呈報之目的為使 037 與 spec 對齊，非等待答案才能開工。**Massage 之委派為行為非存在** —— tab 是否顯示屬 2.1 | 2 leaf（同上，與 #17 併行）| **不阻塞**（R-C33 已定處置）| A-CF21 | Medium |
| 19 | **`2.14` 之例外情形無對應 TC**（覆蓋缺口；待裁是否拆條）| ⏳ `SWE1-HVAC-020-04` 之 leaf 同時含主情形（3 旋鈕 ICS → 不顯示）與例外（`one zone MTC with push button TEMPERATURE` → 例外不適用，即**顯示**）。兩者為**不同車輛配置**，無法共用 pre_conditions，故一條 TC 涵蓋不了。本批依下放包 33 §6 生成 5 條（4 leaf → 4 TC），**例外情形未產生任何 TC** | 0 leaf（不新增 leaf；為既有 leaf 之部分覆蓋）| **不阻塞**（主情形已驗）| — | Medium |
| 20 | **`2.1` 之 `tabs` 是否涵蓋下螢幕之分頁**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ 兩問：(a) `up to 4 tabs` 是否涵蓋下螢幕（13.2 之 `switch the tab on the lower screen`）之分頁？(b)「only Front climate is available」之車輛是否仍有 Seats 內容？**與 #17 同源（皆為 2.1 之內容不足），併同發函。** 依 **R-C28 第一問**本項無裁量空間：13.x 之 full_text 無任何句子支持「本車非僅前排氣候」，補 PC 會把一個對未定義詞語之解讀編碼成事實。**現在不補不是判斷該配置不存在，是判斷條文尚未使它可陳述。** 風險：若答案為「涵蓋」，`Seat Control Tab` 之 14 條在僅前排氣候之車上無對象，屆時須補 PC | 0 leaf（不阻塞生成；影響既有 14 條之 PC 完整性）| **不阻塞** | — | **High** |
| 21 | **`2.6.1` 之 long press 門檻無值**（非檔案，屬上游釐清；**RD-1 候選**）| ⏳ C5.1 載有時間**條件**而無**值**：`long press = fast move`、`Long press = fast move shall also work for temperature HARD CONTROLS`（實測 pattern `\d+\s*(ms|sec)` 於 2.6／2.6.1 **0 命中**）。對照 **7.4（CR4，`Rear Climate`）** 之同一行為載明 `hold longer that **500 ms**`。**依 38 §3 分支二處置**：`-055` 之 ER 不變（寫入 7.4 之值即為以他節數值補值，§8.4.1），登此問。**`-055` 之 ER 恰好等於 2.6.x 所支持之強度，非「比條文所能支持的更弱」** —— 上繳 26 §11.2 之措辭已據此訂正。**方向訂正（上繳 30 §2.3、31 §5）**：本項原記為「後排有值可參考」；`ch2_ch7_mirror_map.tsv` 建成後看清楚的是**前排缺值** —— `7.4` 是同一需求在後排側之完整陳述，`2.6.1` 才是不完整的那一側。問題不是「要不要借後排的值」，而是「前排為何沒有值」 | 0 leaf（影響 `-055` 之 ER 精度）| **不阻塞** | — | Medium |
| 22 | **配備 ECO HVAC 之 BEV 上，按 AUTO 進入者為 `AUTO ECO` 抑或 `AUTO ON`**（非檔案，屬上游釐清；**RD-1 候選**）| ⏳ `3.2`（C20）述「Pressing AUTO breaks MAX DEF … and the system goes to AUTO」，`ch10`（EH2／EH4）述 BEV 之 AUTO 有三狀態且第一次按壓進入 AUTO ECO —— **兩側皆未述此交界**（實測 ch10 全章對 `MAX DEF`／`defrost`／`break` 零命中）。依 §8.4.2 呈報為 coverage hole，**不吸收進現有 TC**：補 PC 無明文（R-C28 第一問）、收緊 ER 會引入 ch10 內容（§8.2.1）。**風險**：解答前 `NR1L-ComfortHMI-022` 於 BEV 上之判定由測試員自行認定，屬 §7 之 FP／FF 風險 | 0 leaf（影響 `-022` 之判定唯一性）| **不阻塞** | — | Medium |
| 23 | **SR24 PDF 之圖片擷取工具**（工具需求，非上游釐清）| ❌ **037 之 Requirement Description 內含 52 個圖片標記（25 個 leaf）**，內容不可讀；`section_fulltext.tsv`（SYS1 export）則 0 命中 —— 登記時之敘述誤記為後者，已訂正（見 A-CF23）。**非上游遺漏 —— 圖片在 037 內，問題在本 pipeline 之讀取能力**，故不列 RD-1 | 25 leaf 之描述帶圖（含已生成之 `SWE1-HVAC-023`／`-076`）| **不阻塞** | A-CF23 | **Low** |
| 24 | **`SWE1-HVAC-044-02` 之 Verification Method 分類**（非檔案，屬上游釐清；**RD-1 候選**）| ⏳ 037 對該 leaf 標 `Manual UI Testing`，而其 Requirement Description 之 `Expected Result` 僅為 `Reduces climate control system power consumption` —— **無任何 UI 可觀察量**。實測（R-C30）：`data/section_fulltext.tsv` 全 129 節、pattern `power|consumption|energy|batter`（不分大小寫）僅 5 節命中，其中 2.7／7.5／16.7 為 `climate power button`（電源鍵），10.9.1 為 pop-up 文字「Press again for lower battery consumption」（其自身之 leaf，已由 `-080` 涵蓋），**耗電量本身於全 spec 無可觀察端**。依 **R-C38** 已產 `[BLOCKED-NON-HMI]` row（`NR1L-ComfortHMI-081`），**leaf 未遺失**。待確認：該 leaf 之驗證方法應否改標（例如量測型而非 `Manual UI Testing`），或其 Expected Result 應否改寫為一個 HMI 可觀察量 | 1 leaf（已產 BLOCKED row，未遺失）| **不阻塞** | — | Medium |
| 25 | **配備 ECO HVAC 之 BEV，其後排氣候是否亦有 AUTO ECO**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ **兩側皆未述。** ch10 全 9 節（10.1 ~ 10.9.1）對 `rear` **零命中**；ch7 之 `CR2` 為 `C2` 之後排逐字重述（見 `ch2_ch7_mirror_map.tsv` 之 7.2↔2.3 `mirrored`），其 AUTO 為兩狀態，不含 `AUTO ECO`／`AUTO ON`／`AUTO OFF` 三狀態。**不由本 feature 補**：補 PC 無明文（R-C28 第一問），收緊 ER 會把 ch10 之內容引入 ch7 之 leaf（§8.2.1）；且此為需求歸屬問題（哪一章擁有後排 ECO 行為），非測試設計問題（§8.2） | 0 leaf（影響 `Rear Climate` 16 leaf 之 PC 完整性）| **不阻塞** | — | Medium |
| 26 | **widget 顯示中時 AUTO ECO 之回饋於何處**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ **三節互相消解。** `14.19`（HVACSB6）列「-Auto Pop-up: do not show (feedback is already on widget)」，使 `10.9`（EH9「The comfort pop ups triggered by hard controls interaction shall reflect the AUTO ECO and AUTO states」）於該情境無對象；而 `17.2`（CW1）列 widget 預設畫面含 `auto button`，**未述該按鈕是否區辨三狀態**。**不由本 feature 補**：三節分屬 `Climate Popups`／`ECO HVAC`／`Home Screen Widget` 三組，任一組單方面補都擴張其驗證範圍（§8.2.1）| 0 leaf（影響已生成之 `-079`／`-080` 之判定唯一性）| **不阻塞** | — | Medium |
| 27 | **tri-mode 車輛上 AUTO 與七種氣流組合之互斥關係**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ `2.3`（C2）把互斥對象寫死為「Auto is mutually exclusive with **the four airflow modes** and front defrost」，而 tri-mode 車**沒有「四模式」**（`3.1` C19 為 3 鍵 7 組合）；C19 全句不提 AUTO。**交叉具名**：本項與 `data/pending_sibling.tsv` 之 `2.12 ↔ 3.1`／`2.12.1 ↔ 3.1`／`2.12.2 ↔ 3.1` 三對 `sibling` **為同一事之兩面** —— 既然氣流模式集合是同一需求的三個配置值（C13 四模式／C13.0 五狀態／C19 tri-mode），C2 對「四模式」宣告的互斥就應有 tri-mode 側的對應物，而條文沒有。**不由本 feature 補**：把 C2 之互斥推廣到七組合是推論而非條文（§8.2：TC 作者不得發明 RD 項目）| 0 leaf（影響已生成之 `-015`／`-016`／`-017` 於配備 AUTO 之 tri-mode 車上之判定，及日後 `2.3` 之 PC）| **不阻塞** | — | Medium |
| 28 | **後排 A/C 與 AUTO／Defrost／Recirc 之連動關係**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ `7.9`（CR9）**全句僅一句**：`AC has on/ off state.`；`2.4`（C3）之四項連動（Auto／Defrost／Recirc 可自動開 AC、AC will break Auto）於 ch7 全 11 節**不存在**，`7.2`（CR2）述 rear AUTO 之中斷條件亦不含 AC。**不由本 feature 補**：ch7 側無句可依，以 C3 補即以前排條文補後排（§8.4.1 造值）| 1 leaf（`SWE1-HVAC-037`，`Rear Climate` 生成時）| **不阻塞** | — | Medium |
| 29 | **`MAX DEF` 之「最高風速」於 `Off, 1-8` 車輛上為 7/7 抑或 8/8**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ `3.2`（C20）與 `16.8`（ICE7）皆把最高風速寫死為 `highest setting (7/7)`，而 `2.7.1`（C6.1）明載「In some vehicles fan speed ranges for front hvac are: **Off, 1-8**」—— 該車之最高為 8。**兩側皆未述此交界。** **不由本 feature 補**：`NR1L-ComfortHMI-019` 之 ER 現寫 `The fan speed is at the highest setting (7/7)`（照 C20 原文），若答案為 8/8 則該 ER 於 1-8 車上為**錯判**；改寫成「最高設定」會弱於條文所給，寫 8/8 則為造值（§8.4.1）。此為 profile §3.2 **第十四軸（前排 HVAC 風速範圍）** 與 MAX DEF 之交界。**本項由 42 §1 之 `provisional` 重新確認機制查出**（`2.7.1 ↔ 3.2` 之逐對判定）| 0 leaf（影響**已生成**之 `-019` 之 ER 正確性）| **不阻塞生成** | — | **High** |
| 30 | **MTC 車輛之溫度呈現行為全 spec 未述**（非檔案，屬上游釐清；**RD-1 候選**）| ❌ `2.6`（C5）明寫 `for **ATC** systems`；`2.14`（C15）只說 MTC「lack of discrete temperature settings and "Auto" control over the set temperature」—— **只說缺什麼，未說是什麼**。故 profile §3.2 **第一軸（ATC／MTC）之 MTC 值在全 feature 內無任何行為條文**，該值下無可驗行為。**不由本 feature 補**：無條文可據，任何 MTC 溫度呈現之陳述皆為造值。**本項由 42 §1 之重新確認查出**（`2.6 ↔ 2.14` 之逐對判定）| 0 leaf（第一軸之 MTC 值無附著點）| **不阻塞** | — | Medium |

## 已量測、無需索取

- **SR24 spec 素材三件**：`spec-index/cache/` 之 SYS1 export（68.40 KB 級，
  SHA256 `6982d37db81b36e4…`）與 JSON（10.57 MB）、`spec-index/sources/` 之
  PDF（6.16 MB，SHA256 `fc5d3cd1d524f4d5…`）。三者齊備，outline map 已建，
  129/129 查得。**不搬入 `inputs/`** —— 共用語料庫留在 `spec-index/`，
  `feature.yaml` 以相對路徑回指。
- **SR25 CR29359**：同目錄存在，但 R-C1 定其為 out-of-scope 參考資料。
  **不索取、不引用、不作為查得依據**（A-CF01）。

## Not requested

- SYS.2 / SYSRA 安全分析件 —— recon 實測 037 **無 ASIL/FTTI 欄位**，
  安全分析層在本 feature 之 403 leaves 上無附著點，不進 trace chain
  （比照 AMFM R6 / Privacy 前例）。
~~- Pop Up List —— 037 未引用；`paths.popup_list` 為 null。~~ **已轉為請求，見 #11。**
