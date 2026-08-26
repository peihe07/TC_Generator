# 下放包 31 —— 讀那 71 條漏網（主任務）、自陳即驗入條、DR-DM10 補充二

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/31_missed_clauses.md`
- **本包對交付物之推進：全 feature 之條文母體修正**（R-G31）
- **前置（已查證）**：上繳 30 已回；停止條件 79／80／81 皆未觸發；
  `pilot-01`／`rvc-01` 一字未動；R-DM 區塊 57、R-G37 已抄錄；
  `{CFTS013-930}` 複核成立；DR-DM7 CLOSED、A11 關閉

---

## 一、上繳包 30 之覆核

**核可，無退回項。** 四項具名。

### 1.1 §1.7 之補測 —— 本輪最有價值之產出

假說否證了，而**否證之方式產生了比假說更強的東西**：

| 三元組之成員 | 角色 | 對本專案 |
|---|---|---|
| `{4819862}`／`{4820951}` | DCSD 決定關背光 → 送 `[DISP_OFF]` | **`noSys` —— 不適用** |
| **`{4819863}`／`{4820952}`** | **HU 見 `[DISP_HOT]→[DISP_OFF]` → 送 `[DISP_OFF]`＋`[0%]`** | **適用** |
| `{4819864}`／`{4820953}` | DCSD 見 HU 之 `[DISP_OFF]` → 停顯示、關背光 | **`noSys` —— 不適用** |

**multi-stage 流程之 HU 側對本專案有定義，DCSD 側沒有；
而 CFTS_013 §1.5.3（13/13 適用）補的正是 DCSD 側。**

`noSys` 之語意在此是關鍵 —— 它不是「不存在」，是**「不由此檔定義」**。
CFTS_020 在 DCSD 側留了空格，CFTS_013 §1.5.3 填了那個空格。
**兩份文件之分工在此對得上。**

分析層不裁定（DR-DM10(a) 屬上游），但**該三項實測足以改寫問法**，
見 §四之補充二。

其比對限度之自我具名亦正確：key 為後件之子字串（A-DM29 之形態），
故並列兩條前件全文使差異可見，不宣稱同一條。

### 1.2 §1.6 —— 更正做得完整，而 B25 之自陳是本輪最該記住的

上繳 29 之「CFTS_020 之 `EE Architecture` 值域不含 `All`」，
**是用來證明 21／28 兩輪未受 A-DM40 影響的整個依據**，而它沒被量過。
本輪一量：`All` 83 次、漏網 71 條。

執行層之自陳逐字採認：

> **結論僥倖仍成立**（兩輪之標的不在漏網內），**但那是運氣，不是我的工作。**
> R-G22 立於 12 輪，規制的正是這件事，**而我在一份宣告自己在做回溯檢查
> 的文件裡犯了。**

**不另立條** —— R-G22 已規制且其文字足夠。改於 R-G22 條下留指標
（見 §五步驟 2），記其「在回溯檢查文件內犯之」之形態，
使該條之讀者看得見它最容易被繞過的地方。

**重做之方式正確**：不是再寫一句斷言，而是全檔重跑（2,169 條、
舊 700／新 771、漏網 71），並如實記「結論仍成立，但理由是假的」。

### 1.3 §九第 3 項 —— 第二次了，立條

> 初稿之第 3 項是「⋯我沒有查」。**那句話寫完，我去查了，五分鐘的事。**
> 本輪這是第二次「自陳未驗」在寫下的當下就變成可驗。
> **自陳欄不該是待辦清單的傾倒處。**

**採納並立條**（§三 R-G38）。第一次為 27 輪之反向查證（24-4 之
popup 判準由 1 列改為 4 列）。**兩次皆在寫自陳時發現，兩次皆五分鐘可驗。**

### 1.4 A-DM40 之狀態 —— 維持 `[CLOSED]`

執行層問「若分析層要求改標未結，請明示」。**不改。**
缺陷已更正、回溯已重做，**其重要性由 R-G37 承載，不需以未結狀態代表。**
異常之狀態欄記的是該異常本身是否處置完畢，不是其教訓的份量。

---

## 二、【主任務】讀那 71 條漏網（B24）

### 2.1 為何這是現在最該做的

那 71 條之共同形態為 **`EE Architecture: All`**，而其 `Radio` 多為
`R1H, R1L, R1L-R, R1M` 之 R1 系列通條 —— **那正是最可能與本專案
相關的形狀**（CFTS_013 §1.5.3 之 13 條就是這個形狀）。

而它們**被舊判準排除了整整十輪**。本 feature 迄今之每一次
「CFTS_020 內某行為之條文有幾條適用」之量測，其母體都少了這 71 條。

**這不是某一個 leaf 的問題，是全 feature 之條文母體問題。**

### 2.2 任務

**T1.** 逐條取 71 條之**逐字全文**與完整屬性行
（`Artifact Type`／`State`／`ECU`／`Radio`／`EE Architecture`／
`Market`／`Model Year`），並標其**章節位置**。

**T2.** 逐條標其 `Artifact Type`。**Description／Heading 與
Subsystem Functional Requirement 分列計數** ——
前者不產生需求，其份量不同。

**T3.** 逐條標其**是否觸及本 feature 之 8 個 leaf 之主題**，
分類為五組（本 feature 之 framework 四組 ＋ 「其他」）：
`Operative State`／`Thermal Management`／`Pop Up Handling`／
`Rear View Camera`／其他。
**只分類不判定覆蓋** —— 是否構成新的 TC 需求由分析層裁。

**T4.** **重跑既有之三項量測**，以新判準（R-G37）為之，
並與舊值逐項對照：

| 量測 | 舊值 | 出處 |
|---|---:|---|
| RVC × `$DCSD_DISP_STAT$` 之適用條文 | **24** | 上繳 28 §3.7 |
| `1.11.2.2` 之組 A／組 B 適用性 | 組 A 7 條／組 B 4 條 | 上繳 21 |
| 適用本專案且含 `turn off … backlight` | 2 | 上繳 30 §1.7 |

**不符即具名**，並標其是否影響 `pilot-01`／`rvc-01` 之任一條。
**影響則停並回報，不得逕改**（停止條件 76 續用）。

**T5.** `coverage_sys2_vs_swe_dm.tsv` 之覆蓋量測是否以舊判準為之？
**若是，重跑並存為新版**（舊版依 R-TM13 保留，加 `.PRE_R_G37` 後綴）。
**若否，具名其判準為何。**

### 2.3 拘束

- **不得改動 `pilot-01`／`rvc-01` 之任一 TC**（停止條件 76）
- **不得解除任何 deferred**
- 新發現之適用條文一律**登記為材料**，不逕生 TC

---

## 三、裁決條文

```
R-G38（自陳未驗項若於本輪可驗，須當場驗 —— 全域）
上繳包之「本包是否仍有該驗而未驗者」一節，其功能為**留痕**，
不是待辦清單之傾倒處。

**凡寫入該節之項，須先自問一句：這一項現在驗得了嗎？**
驗得了則當場驗，其結果寫入本文對應之節，該項自自陳欄移除
或改記為「初稿時未驗，本輪補驗，見 §X」。

三項細則：
(a) 「驗得了」之判準：其所需素材已在手、無待裁項阻斷、
    無停止條件禁止、且不需另立判準。四者皆備即為可驗。
(b) 可驗而不驗者，須於該項具名其**不驗之理由**
    （停止條件禁止／素材不在手／屬 Tier 2），
    **不得以「未查」二字了事**。
(c) 停止條件禁止者即為不可驗，**不得以本條為由逾越停止條件**
    —— 本條不創造任何新的許可。

理由：自陳之價值在於它記下了作者知道而讀者不知道的事。
**但若那件事作者當場就能查清楚，寫下來反而是把工作推給下一輪的人**
—— 而下一輪的人手上的資訊比作者當時少。

實例二則，皆為執行層自行發現並自行更正：
- 27 輪：24-4 之 popup 判準初版以編號為準只得 1 列，
  寫自陳時想到「一列是實測，『一列就是全部』不是」，
  回頭反向查證得 4 列。
- 30 輪（上繳 30 §九第 3 項）：初稿寫「一個適用本專案之 multi-stage
  DCSD 關閉序列是否存在於他處，我沒有查」，**寫完就去查了，五分鐘**
  —— 結果是 HU 側有、DCSD 側無，而那正好說明兩份文件如何分工，
  成為該輪最有價值之產出（§1.7）。

**兩次皆在寫自陳時發現，兩次皆五分鐘可驗。**
```

---

## 四、DR-DM10 之補充二（**Pei 發**）

三十輪之實測使 (a) 之問法可再收斂一次。**已發之補充一不撤回**，
本件為其續：

> **Supplement 2 to DR-DM10 — the two documents appear to divide the work**
>
> Further to our previous supplement, we have now traced the three clauses
> that CFTS_013 `{4943104}` defers the shutdown behaviour to
> (`{4821589}`, `{4821590}`, `{4821591}`), together with `{4821587}` and
> `{4821592}`.
>
> **All five are declared `[Radio:VP4R84] [EE Architecture:CUSW]`**, in
> section `1.15.5.5.2`. They do not apply to R1H / Atlantis High.
>
> However, the same five sentences recur verbatim across **five parallel
> "Multi-stage' DCSD Display Hot Algorithm" sections** (`1.8.2.5.2`,
> `1.15.1.5.2`, `1.15.2.5.2`, `1.15.4.5.2`, `1.15.5.5.2`). Examining the
> variants that **do** carry `R1H` and `Atlantis High`:
>
> | Role in the sequence | Clause | Applies to R1H / Atlantis High |
> |---|---|---|
> | DCSD decides to turn off its backlight, sends `[DISP_OFF]` | `{4819862}` / `{4820951}` | **No — `Radio:noSys`** |
> | HU sees `[DISP_HOT]` → `[DISP_OFF]`, sends `$TGW_DISP_STAT$ = [DISP_OFF]` and `$RQ_DISP_INTS$ = [0% Intensity]` | **`{4819863}` / `{4820952}`** | **Yes** |
> | DCSD sees the HU's `[DISP_OFF]`, stops displaying and turns off backlight | `{4819864}` / `{4820953}` | **No — `Radio:noSys`** |
>
> That is: **within CFTS_020, the multi-stage algorithm's HU side is defined
> for this programme and its DCSD side is marked `noSys`.** Meanwhile
> CFTS_013 §1.5.3 — thirteen clauses, all `[EE Architecture:All]` and all
> naming `R1H` — defines exactly that DCSD side: the once-per-minute
> monitoring, the 50 / 51–55 / 56–below-60 staging, the 10 second timer, and
> `Note: Only DCSD shall implement 10 sec timer.`
>
> **Revised question (a):** are CFTS_020 and CFTS_013 intended to **compose**
> for R1H / Atlantis High — CFTS_020 defining the HU side and CFTS_013 §1.5.3
> the DCSD side — with `{4820289}`–`{4820292}` (the single 85 °C threshold)
> being an alternative rather than the governing behaviour? Or does
> `{4820289}` govern and CFTS_013 §1.5.3 not apply despite its `All`?
>
> **New question (e):** `{4820283}` states that the HU sends
> `$TGW_DISP_STAT$ = [DISP_OFF]` when it `has finished displaying the Display
> Hot warning screen and determines that the DCSD display should now be
> 'Turned Off'`. `{4821590}` states the **same consequent, word for word**,
> with the antecedent `When the HU sees the transition from
> $DCSD_DISP_STAT$ = [DISP_HOT] to $DCSD_DISP_STAT$ = [DISP_OFF]`.
> Is the latter the criterion the former leaves unstated?

---

## 五、作業步驟

1. **§二之 T1–T5**（主任務）。
2. 抄錄 **R-G38** 入 `docs/fw036/RULINGS_LEDGER.md`（置放依 R-G34）；
   **R-G22 條下留指標**（非 fence，不入核對表母體）：
   > **最易被繞過之處（下放包 31 §1.2）—— 不改本條原文**：
   > 本條要求斷言由腳本產出。**其最易失守之處恰為「回溯檢查」類文件**
   > —— 該類文件之語氣已在宣告自己在查證，讀者（含作者）遂不再問
   > 「這一句本身量過沒有」。實例：上繳 29 §2.2 之
   > 「CFTS_020 之 `EE Architecture` 值域不含 `All`」，
   > 為該輪回溯結論之整個依據，未經量測；30 輪實測 `All` 83 次、
   > 漏網 71 條（結論仍成立，理由為假）。
3. **DR-DM10 補充二**（§四）寫入 `DATA_REQUESTS.md`，標「待 Pei 發」。
   **補充一不撤回**，兩者並列。
4. `BACKLOG.md`：B24 改為「本輪執行中」；B25 記其已由 §5.2 之指標承載。
5. 更新 `docs/INDEX.md`。

**仍不寫回 036 母本。**

---

## 六、停止條件

沿用 1–83，另加：

84. T4 之重跑若顯示 `pilot-01` 或 `rvc-01` 之任一條所依之條文
    **適用性判定改變** → 停並回報，**不得逕改任何 TC**。
85. T3 若發現 71 條中有**適用本專案且落在 8 leaf 主題內之
    Subsystem Functional Requirement** → 具名列出，**不逕生 TC**；
    其數量若逾 10 條 → 停並回報（母體變動之份量屬 Tier 2）。
86. T5 若 `coverage_sys2_vs_swe_dm.tsv` 係以舊判準產出 →
    重跑並保留舊版；**兩版之差集逾 20 列 → 停並回報**。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/31_missed_clauses.md`）

1. T1–T5 之全部產出：71 條逐字全文、`Artifact Type` 分列計數、
   五組分類表、三項量測之新舊對照、覆蓋表之判準與重跑結果
2. R-G38 抄錄核對表；R-G22 指標之置放
3. DR-DM10 補充二全文
4. `BACKLOG.md` 之 B24／B25 更新
5. 未驗項分流（A／B，R-G29）**——依 R-G38，可驗者當場驗**
6. 建議之 commit 訊息與 pathspec（不執行）
