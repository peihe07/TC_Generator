# Audio Management — 上繳包 19：B5 第二路對帳（R-AM15）

- 日期：2026-08-26
- 對應下放包：`docs/handoff/18_B5_anchor_candidates.md`
- 池基準：**展開池 v2，891 ID**（A-AM12；執行層之抽取缺陷見 A-AM13）
- 工具：`scripts/route2_b5.py`，三關卡已實作並生效

---

## 一、三關卡之實效

包 18 §三 將 A-AM11 之改善清單立為否定結論之前置。本批**三關各命中一次**：

| 關卡 | 命中葉 | 若無該關會發生什麼 |
|---|---|---|
| 3 葉內自引掃描 | **023** | 葉描述自載 `CFTS019-4865986`。不掃即與 B4 之 024 同樣落空 |
| 1 詞形擴充 | **025** | 以 `fade`＋`send` 擴形命中 4866311；原查詞為「audio parameter API」，零命中 |
| 2 不截斷讀取 | **040／107** | 判別依賴錨文末段（`refer to {CFTS024}`、`played on the front speakers`），截斷即失 |

**另有一關卡不及之例（新增建議）**：**168** 之正解由**區段掃描**尋得，
非任一關卡。詳見 §二.4 —— 詞彙完全不同時，詞形擴充無能為力。

## 二、C 級五葉 —— **全數解決，零 PENDING**

### 二.1 SWE1_AMM_023 → **CFTS019-4865986**（池外）

葉描述原文：「…as defined in the applicable **CFTS019-4865986** alert-tone
configuration」。**上游自載 ObjectID**，最強追溯。

4865986 為 Alert 1–8 之波形參數表（Waveform／Frequency／Attack／Decay／
NPulses）。**表格型物件**，池外。TC 以「所選 alert type 之音以其對應參數產生」
為驗證面，**表內容不轉抄**（IN §4.3.1 R-3）。

### 二.2 SWE1_AMM_025 → **CFTS019-4866311**（池內），部分覆蓋

> `HU has to send the customer setting of Fader and Balance to the AMP
> component, through signals: $ToneFADE$ for Fader setup; $ToneBAL$ for
> Balance setup.`

與葉之「處理 Fade／Balance 變更並傳至 HW 介面」對應。
**EQ 半未覆蓋**：tone controls 之傳遞在 **4866090**（`$ToneBASS$` 等），
而該物件為 043／048 之錨。處置建議：025 錨定 4866311 標**部分覆蓋**；
或與 043／048 依 R-AM16 共錨 4866090 併列。**請分析層裁**。

包 18 已排除之 `<Tmute>`（4866007）判斷正確——該物件為調整期間之內部靜音，非傳遞。

### 二.3 SWE1_AMM_040 → **CFTS019-4865982**（池內）—— 惟與 021 衝突，見 §三.1

> `If the entertainment and information alert feature is enabled, the HU shall
> generate the appropriate Entertainment and Information Alert for each
> enabled event type.`

與葉「當功能啟用時，將各已啟用之 alert event 對映至其 alert type 並產生對應音」
**逐句對應**（enabled → each enabled event type → generate）。

### 二.4 SWE1_AMM_168 → **CFTS019-4866594**（池內）

> `When any of the following systems requires HU audio, HU shall **turn off
> surround sound**. When any of the following systems stops to require HU
> audio, HU shall **turn on again** surround sound.`

與葉「獨占音訊事件作用時暫停 Surround、事件結束後回復」逐項對應。

**方法學註記（重要）**：包 18 記「`surround`＋`exclusive/override/emergency`
全文零同現」——該否定為真，但**結論不成立**：規格用語為
`requires HU audio` / `turn off surround sound`，與查詢詞**無任何交集**。
詞形擴充（關卡 1）對此無效，因失效點不在詞形而在**詞彙選擇**。
本葉由**區段掃描**（`--scan 4866591-4866602`，即包 18 所提之位置線索）尋得。

**建議新增第四關**：位置線索存在時，**逐條讀該區段**優先於任何關鍵詞檢索；
關鍵詞之零命中在跨詞彙情形下不構成否定證據。

### 二.5 SWE1_AMM_281 → **CFTS019-4865984**（池內）

> `Appropriate information alert examples are as follows: Alert1 - Sports/Game
> Alert … Alert5 - App Alert Alert6 - Reserved for MIM alerts Alert7 …
> Alert8 …`

與葉之「維持 Alert1–Alert5 供 Information alert types、保留 Alert6–Alert8
供 MIM」**逐項對應**。包 18 疑其為「例列句」故不採；實則該列句即
Alert 識別碼之對映定義，正是葉之題旨。

與 023 之分工：**281 ＝ 事件↔識別碼對映（4865984）**、
**023 ＝ 識別碼↔參數（4865986）**，兩物件不同、兩葉不共錨。

## 三、B 級之對帳（31 葉：29 一致、2 異議）

### 三.1 021／023／040 三葉之錨定衝突 —— **須裁**

| 葉 | 包 18 之錨 | 第二路所見 |
|---|---|---|
| 021 | 4865982 | 葉描述**自載 `CFTS019-4865986`** |
| 023 | （C 級未決） | 葉描述**自載 `CFTS019-4865986`** |
| 040 | （C 級未決） | 4865982 逐句對應 |

021 與 023 **兩葉皆自引 4865986**；而 4865982 之原文與 **040** 逐句對應。
包 18 現況為 021→4865982，恰與自引及文本對應**互換**。

**建議**：021／023 共錨 **4865986**（R-AM16，括號下半各異：021 取「依事件
型別取用定義與參數」、023 取「依所選 alert type 取用音參數」）；
040 錨定 **4865982**。**執行層不逕改**（R-AM15）。

### 三.2 SWE1_AMM_292 → 候選 4866171 **無文本**，正解 **4866173**（池外）

4866171 於全文與匯出**皆無內容**（4866170 之後直接跳至 4866173）。
正解：

> **4866173**：`The Customer Selectable Setting strategy for Park Assist and
> Side Distance volume uses the customer setting values as-is to set the …`

與葉「`$Park_Assist_Volume_Strategy$` ＝ Customer Selectable Setting →
採用者設定值」逐項對應。4866173 **池外**。

（293／294 之 gear-based／default 兩策略請一併確認是否落 4866174／4866176
與其 TeenKey 變體 4866175／4866177 —— 後二者亦池外。）

### 三.3 其餘 29 葉一致

含 029→4866042（範圍前提句，惟葉本身即該範圍判定之 SWE.1 表述，成立）。

## 四、跨批共錨之檢查缺口（新發現，建議補防線）

**107（B5）→ 4866286** 與 **020（B4）→ 4865981 ⏎ 4866286** 共用 4866286。

第二路複讀：4866286「alerts feature, if enabled…shall be played on the
**front speakers**」與 **107**「route alert tones to the front speaker
channels」逐字對應；而 **020**「at least the front channels；全通道區設定時
routed 全通道」對應之是 **4865981**（`all channels, but at a minimum…front`）。

依 R-AM16 共錨合法，惟其硬性條件為**括號下半不得逐字相同**。

**缺口**：執行層之 sibling 區分檢查（selfcheck 與 lint 之檢查 I）
**僅在單一批次內比對**。020 在 B4、107 在 B5，跨批共錨**不會被任何檢查看到**。

**建議**：新增跨批檢查——對全簿之 `spec_reference` 建立錨→TC 反查表，
凡同錨多 TC 者比對其括號下半。執行層可自行實作並回溯掃 B1–B5，
請裁定是否列為出貨前置。

## 五、統計

| 段 | 葉數 |
|---|---|
| A 級（抽核通過） | 14 |
| B 級一致（逕寫） | 29 |
| B 級異議（待裁） | 2（021 之錨、292 之錨） |
| C 級全解（待裁採認） | 5 |
| 合計 | 50 |

池外葉：023（4865986）、292（4865973 → 更正為 4866173）、
285（4867695）等共 **8 葉**（B 級 7 ＋ C 級之 023），依 R-AM18 標單源佐證。

## 六、待分析層裁定

1. 021／023／040 三葉之錨定（§三.1）。
2. 292 改錨 4866173；293／294 一併確認（§三.2）。
3. 025 之部分覆蓋或與 043／048 共錨（§二.2）。
4. 023／168／281 之採認（§二.1、§二.4、§二.5）。
5. **跨批共錨檢查**是否列為出貨前置（§四）。
6. 建議將「位置線索存在時逐條讀該區段」列為否定結論之第四關（§二.4）。
