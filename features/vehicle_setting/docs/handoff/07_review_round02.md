# 07 下放包 — 02 輪覆核、值域完整性複驗、殘項

分析層寫入，2026-08-20。對象：`reports/w8_spec_variables.md`、
`reports/w13_hmi_sweep.md`、`RULINGS.md` 之抄錄。

**覆核結論：兩份報告接受。但 02 輪之上繳包未寫（第三次），見 §1。**

---

## 1. 流程缺陷 —— 同一形態第三次

| 輪 | 工作 | 報告 | 上繳包 |
|---|---|---|---|
| W-0c／W-16／W-18 | ✅ | ✅ `w16_w18_leaf_universe.md` | ❌（經催補始寫 `01_leaf_universe.md`）|
| 本輪 W-8／W-13 | ✅ | ✅ 兩份 | ❌ **未寫** |

`docs/upstream/` 實測仍只有 `00`、`01` 兩份。

**成因判斷**：作業清單把「上繳」列在最後一項，而 `reports/` 之逐項報告
在做完該項時即已寫完，於是「已經寫了東西」之感覺取代了上繳包本身。
**這不是遺忘，是清單形狀造成的。**

```
R-VS18（作業流程，Pei 追認前依此執行）
上繳包不是最後一項，是**第一項**。

每輪開工之第一個動作為：建立 `docs/upstream/NN_<slug>.md`，
寫入標題、本輪作業清單、與 canon §8.2 之六個空節
（預期 vs 實測／不符項目／三分法／掃描條件／新開 anomaly 與 DR／
獨立判斷），各節先留空白。

其後每完成一項作業，**當下就把該項之結果填入對應節**，
`reports/` 之細節報告為其附件而非替代。

理由：`reports/` 逐項落檔會產生「已交付」之錯覺，而上繳包所要求之
六項（尤其「預期 vs 實測逐項對照」與「本包是否仍有該驗而未驗者」）
是**跨項的**，逐項報告不會自然產生它們。
```

---

## 2. W-8 覆核 —— 接受，其自我更正之處置正確

**32 / 33 之「不一致」為抽取缺陷而非資料不一致**，且先報自己的錯再報
資料的錯。此處置符合 canon §5a 第 12 條（抽取式之缺陷不會報錯，
須以已知全集驗證），且 00G §7-4 曾具名預警此形態 —— **預警被實際使用了**。

真不一致 1 項：`$VC_VEH_LINE$`，CFTS044 側之 `DT`／`WS`／`HDCC`／`M240`／
`JL`／`K8`／`M182`／`M189`／`DS or DJ or …` 與 LID 表之數字車型碼
**完全無交集**，且 LID 表截斷於 `101 = WL (65 Hex)`。
→ **即 DR-8，維持開啟。** 停下回報正確。

---

## 3. 分析層之複驗推翻自身一項陳述（canon §5a 第 16 條）

分析層於前一則聊天稱：

> CFTS044 之 `$HeatedSeatFL$` 只列 `0h: off`／`1h: low`／`3h: high`，
> **沒有 `2h: medium`**

**該陳述為誤。** 分析層自 `inputs/` 之原始 docx 複驗
（`word/document.xml` body 文字，逐 token 抽 `= [值]`）：

| token | 具名式之值 | 十六進位式之值 |
|---|---|---|
| `$HeatedSeatFL$` | `HS_OFF` 9／**`HS_MED` 5**／`HS_LO` 5／`HS_HI` 5 | `0h: Off` 2／`1h: Low` 2／`3h: High` 2 |
| `$HeatedSeatFR$` | `HS_OFF` 9／**`HS_MED` 5**／`HS_HI` 5／`HS_LO` 5 | 同上 |
| `$VentedSeatFL$` | `VS_OFF` 6／`VS_LO` 4／`VS_HI` 4／**`VS_MED` 4** | 同上 |
| `$HSW_Stat_2$` | `HSW_OFF` 7／`HSW_LO` 4／**`HSW_MED` 4**／`HSW_HI` 4 | —— |

**CFTS044 有 Medium。** 但實測揭出一個**真的、且更精確的問題**：

### 3.1 十六進位式之列舉在 CUSW 條文中確實無 `2h`

該列舉出自 `4857940`：

> `[EE Architecture:CUSW]` Valid values for the `$HeatedSeatFL$` are shown
> below. All other states shall be considered invalid by the HU.
> `$HeatedSeatFL$ = [0h: Off]` `$HeatedSeatFL$= [1h: Low]`
> `$HeatedSeatFL$ = [3h: High]`

全文 `2h :` 之命中 13 處，皆為他訊號（`2h: HWM Fluid ready`、
`2h: Available`、`2h: Hard Mode`、`2h: Pressed`），**無 `2h: Medium`**。

**但該條文之 EE Architecture 為 CUSW，不是 Atlantis High。**
本 feature 之架構為 Atlantis High，其值域來自具名式（四階，含 MED）
與 LID 表之 `ATLANTIS 2 bit signal 0/1/2/3`（四階）。

→ **兩者不衝突**：CUSW 架構之三階列舉與 Atlantis High 之四階並存，
是**架構差異**而非缺漏。

```
R-VS19（值域之架構條件，待 Pei 裁）
CFTS044 之值域列舉須連同其條文之 [EE Architecture] 標籤一併取用。
本 feature 僅採 `Atlantis High`（含 `All`）之條文；標記為
`CUSW`／`PowerNet`／`Atlantis Mid` 而未含 Atlantis High 者，
其值域不適用於本 feature，亦不得作為「CFTS044 與 DBC 不一致」之證據。

實例：`$HeatedSeatFL$` 於 CUSW 條文（4857940）列 0h/1h/3h 三階，
於 Atlantis High 之具名式與 LID 表皆為四階（含 MED / 2）。
本 feature 取四階。

推論：W-8 之三來源比對須加一欄 `arch_scope`，記錄該值域出自哪些
架構標籤之條文；跨架構之差異不列為不一致。
```

**若本條不立，`$HeatedSeatFL$` 三階 vs 四階會在 framework 階段變成
分支數之爭議**，而其真正答案是「問的是哪個架構」。

### 3.2 順帶發現 —— 規格內之筆誤

`$VentedSeatFL$` 之值中出現 **`Vented Seat Off / HS_OFF`** 一處
（`HS_` 為 Heated 之前綴，此處應為 `VS_OFF`）。
→ **A-VS22**，RD-1 FYI 類。不影響取值（同一 `= [值]` 內之左式已定
其為 VentedSeat）。

---

## 4. W-13 覆核 —— 接受，且其處置為本輪最佳

`Core HMI Logic and Flow` 一檔 `pdftotext` 僅得 21 字元，初判「未解析」。
**該檔正是 00D §6-1 具名之候選之一**，故不以「未解析」收尾：
直接 OCR（亂碼）→ 水平鏡像（仍亂）→ **旋轉 180° 後 OCR 得 35,901 字元可讀**。
讀出後 `Fail_Present`／`STATFailSts`／`Heated`／`Seat`／`Fail` 命中皆 0。

此即 canon §9.1 第 6 項（判「不可讀」前須先驗抽取能力，且須跨素材形式
試過）之正面案例。**並自行補了詞界驗證**（`Left Side` 誤命中
`left sideways`），逐檔檢視 4 檔次全部無關。

→ **A-VS10 由「已知未查」轉為「已查為綠」**：107 檔內無失效彈窗、
無圖示左右駕鏡像。**DR-5-B 維持開啟，走 RD-1 提問** —— 其性質更明確了：
不是我方沒找，是該目錄確實沒有。

**RD-1 Q1／Q2 之措辭應據此加強**：

> 我方已對 26PI2.5/HMI 之全部 107 檔（PDF 89／XLSX 15／PPTX 3）
> 做全文掃描，含對一份無文字層之 PDF 施以旋轉 180° 之 OCR。
> `Fail_Present`／`STATFailSts`／`Heated Steering Wheel Icon` 命中皆為 0。
> 故 `TLM HMI Document` 與 `PDO graphics` 所指之內容，不在我方持有之
> 任何 HMI 文件內。

---

## 5. 兩個盲區要在 framework 之前收掉

W-8 §盲區自陳兩項，分析層評估其優先度：

| 盲區 | 分析層評估 |
|---|---|
| **「有交集 ≠ 一致」** | **最高**。其舉例（`$HeatedSeatFL$` 三階 vs 四階）經 §3 複驗後為架構差異，**該例已解**；但**判準本身仍在** —— 有交集而其中一方少列某階，比對式看不見。**W-19 處理** |
| **CFTS044 抽取仍只有兩式** | **高**。徵候為真：`$HSW_StatFailSts$` 之式二只抓到 `Fail_Not_Present`，而 DBC 與 LID 表皆載其另有 `Fail_Present`。**W-20 處理** |
| 橋接依賴 LID 表，其若錯則三來源一致地錯 | 中。W-15b′ 之逐屬性交叉即為此而設，維持原排序 |

---

## 6. 03 輪作業

**第一項：依 R-VS18 先開 `docs/upstream/02_variables_and_sweep.md`**，
補記本輪已完成之 W-8／W-13（含 canon §8.2 之六節），
再往下做並逐項填入。

| 作業 | 內容 |
|---|---|
| **W-19（新）** | **值域完整性複驗**。對 30 個 token，逐 token 逐來源列出**其完整值集合**（非僅交集），並標記「某來源少列某值」之情形。判準改為：**兩來源之值集合不相等即列出**（現行判準為「無交集才列」）。每筆須附 `arch_scope`（R-VS19） |
| **W-20（新）** | **CFTS044 值域抽取之第三式**。以 `$HSW_StatFailSts$` 之 `Fail_Present` 為已知全集之錨點，找出現行兩式漏抽之記法，補為第三式；補後重跑 W-8 與 W-19。**不得以「找不到第三式」收尾而不說明其驗證方式** |
| W-15b′ | DBC ↔ LID 表逐屬性交叉（本 feature 所用之 message／signal） |
| W-17 | LID 列數差 6 之追因；`TRUNCATED_ENUM` 之其他形態 |
| W-9 | Comfort 逐條對照（母體 237 個 Functional leaf）。**必停已由 R-VS7 解除** |
| W-16′ | 補 `Categorization` 值域全集一行 |
| W-21（新，登記） | A-VS22（`Vented Seat Off / HS_OFF` 筆誤）登記入 `ANOMALIES.md`，RD-1 FYI |

**不新增探索性作業。** W-19／W-20 皆為收既有盲區，非新面向。

---

## 7. 待 Pei

| # | 事項 | 狀態 |
|---|---|---|
| P1 | 刪 `features/vehicle setting/` | 未處理 |
| P2 | 入庫（00／01／本輪產物 + 裁決） | 未處理 |
| P10 | `.gitignore` 加 `!inputs/INPUTS.sha256` | 未處理 |
| **P11（新）** | 裁 **R-VS18**（上繳包為第一項）、**R-VS19**（值域之架構條件） | 本包提出 |

**P1／P2／P10 已積五輪。** 目前仍未擋住作業，但 P2 不做，
00～02 三輪之產物全部不在版控中 —— **若工作區出事，三輪工作沒有備份。**

---

## 8. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS18 | 上繳包為每輪第一項，逐項邊做邊填 | ✔ §1 |
| R-VS19 | 值域須連同 `[EE Architecture]` 取用；跨架構差異不列為不一致 | ✔ §3.1 |

兩條皆以獨立可貼入之區塊呈現，未夾在敘述中。
