# 下放包 19 —— A-PMH16 之複驗、PDF 原句損壞與 R-PMH66 之未套用側

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/19_broken_source.md`
- 前一包：[18_break_the_circle.md](18_break_the_circle.md)
  （上繳 [../upstream/18_break_the_circle.md](../upstream/18_break_the_circle.md)）

---

## 一、18 包之覆核結果 —— **通過**

三條停止條件全未觸發；章 9／11 殘餘全具名；分割檢查未覆蓋段不含 marker；
偽陰率 50% 已量；doc-sync 改錨後 (a) FAIL／(b) PASS。

**三項特別記明**：

1. **§2.4 為本輪最重要之一段** —— 說明 13 包之全簿雙向 diff 為何漏掉
   A-PMH16：p9 切出之「句」皆為矩陣格與散文之混合串，其 6-gram 覆蓋率
   多 ≥ 30%，**遂被門檻自動判為切分假象而濾掉**。
   **「門檻做了本不該由它做的判定」** —— R-PMH66 之立條理由當場兌現。
2. **§9 末段之自我加碼** —— 主動指出停止條件 7 問的是「與矩陣結論是否一致」
   而非「有沒有新漏」，**並明說「若條件 7 寫成後者，本包會停」**。
   **這是對我所寫之停止條件之缺陷之指認，不是對其之通過。**
3. **§11 第 4 項** —— 自行補上 Wilson 區間（5/10 之 95% 約 19%–81%，
   即「約 16 條」實為「約 6 到 25 條」），並說明點估計
   「**使該數字看起來比它應有的樣子確定**」。

---

## 二、A-PMH16 —— 分析層獨立複驗，**成立，且比所報更嚴重**

**量測條件**：PyMuPDF `get_text("blocks")` 取 p9 之 `PM1)` 單一區塊
（不與矩陣交錯）；SYS1 取 `Basic Report` 之 outline `9.1`。

### 2.1 三處逐字確認

| # | PDF p9 `PM1)` 區塊 | SYS1 `9.1` | 探針 |
|---|---|---|---|
| 1 | `should 'stay awake'` **`for 60 seconds`** `up to 2.5 minutes` | `should 'stay awake up to 2.5 minutes` | `for 60 seconds up to 2.5 minutes`：PDF **1**／SYS1 **0** |
| 2 | `within 60` **`seconds`** `the timeout` | `within 60 the timeout` | `within 60 seconds the timeout`：PDF **1**／SYS1 **0** |
| 3 | `pop-up list,` **`the radio should shut Off the`** `popup should close` | `pop-up list, the popup should close` | `the radio should shut Off the popup`：PDF **1**／SYS1 **0** |

**執行層之指認完全成立。**

### 2.2 **但第 3 處不是時序，是一個獨立的行為結果**

18 包把三處併稱「(1)(2) 皆為時序」而將 (3) 列為「整個子句」。
**(3) 之內容為 `the radio should shut Off`** —— 那是一個**與 popup 關閉並列
之獨立結果**（收音機關機），不是時序修飾。

**其影響大於時序**：依 SYS1 之版本，逾時之後果只有「popup 關閉」；
依 PDF，還有「radio 關機」。**5 個 leaf 引 `9.1`，若依 SYS1 撰寫，
該關機行為在整個 feature 中不會有任何一條 TC 驗到。**

### 2.3 ⚠ **而 PDF 原句本身已損壞 —— 這是 18 包未指出者**

PDF 之該句逐字：

> `If the user does not interact with the popup within 60 seconds the timeout
> defined in pop-up list, the radio should shut Off the popup should close`
> **`aofnd`** `if no other popups are to be shown the radio should shut off.`

三處病徵：

- **`aofnd`** —— 非英文字（`and` 之打字損壞）；
- `the radio should shut Off the popup should close` —— **兩個主謂結構相連而無
  連接詞**，讀不成句；
- `within 60 seconds the timeout defined in pop-up list` —— **兩個時間條件並列
  而無連接詞**。

**該句像是一次未完成之編輯**：舊文字（`within 60 seconds` / `the radio should
shut Off`）與新文字（`the timeout defined in pop-up list` / `the popup should
close`）疊在一起而舊的沒刪掉。

**若此推測成立，SYS1 之版本反而是「編輯之意圖」** ——
它刪掉的正是那兩段舊文字，並把 `aofnd` 改回 `if`。

### 2.4 這使 R-PMH50 在此處失效 —— **兩邊都不可靠**

R-PMH50 定「`source_clause` 取自 PDF，不取自 SYS1」，
其依據是「SYS1 相對 PDF 有偏離」。**該依據預設 PDF 為正確者。**

**此處 PDF 不正確** —— 它是一個讀不成句的破句。
故本處**不得逕以 PDF 為準，亦不得逕以 SYS1 為準**：

| 取 | 風險 |
|---|---|
| PDF | 把一次未完成編輯之**兩個版本疊寫**當成需求，可能寫出「radio 關機」與「popup 關閉」並存之錯誤 ER |
| SYS1 | 若該編輯**尚未被上游確認**，則丟掉了 `60 seconds` 與 `radio shut Off` 兩項真需求 |

**唯一正解是問上游** → **`DR-PMH4`**（§五 R-PMH69）。

**其阻斷範圍**：outline `9.1` 之 **5 個 leaf**（`SWE1-HMI-PM-018-01` ～ `-05`），
屬 `Power Transitions` 組。**該組不得開批，直至 DR-PMH4 結案。**

---

## 三、章 7 之殘餘 —— **最高優先，因為 batch 1 出自該章**

執行層 §11 第 2 項：章 7／10／12 之殘餘未讀，**而 batch 1 之 8 條全部出自
outline 7.1～7.4 與 10.4**。

**A-PMH16 之發現方式已經證明「殘餘裡會有東西」** ——
它就是從章 9 之 15 句殘餘裡讀出來的。

**章 7 之殘餘若含同型漏字，batch 1 之 8 條 TC 即建於失真材料上。**
雖其 `source_clause` 取自 PDF（R-PMH50）而非 SYS1，
**但 §2.3 已證 PDF 本身亦可能損壞**。

列為步驟 2，**先於任何新批次**。

---

## 四、R-PMH66 之未套用側 —— 執行層自己指認，我立條

執行層 §11 第 5 項：R-PMH66 只施行於兩支，
**而 `bidirectional_spec_diff.py`（13 包之全簿雙向 diff）仍以 6-gram 30% 門檻
自動判定 —— 且它正是漏掉 A-PMH16 的那一支**，未被改造、未被停用、未被標註。

**其自評精準：「這是 R-PMH62 之同型 —— 立了條而未回頭套用於它所指認的
那個對象。」**

**R-PMH62 只要求「回頭套用於支持該質疑之其他項」，未要求「處置該條所
指認之對象本身」。** 補之 → R-PMH70。

---

## 五、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH69（來源本身損壞時之處置）
當規格 PDF 之原句本身損壞（非英文字、兩個主謂結構相連而無連接詞、
同一條件之新舊兩版疊寫等），**不得逕以 PDF 為準**，
R-PMH50「source_clause 取自 PDF」於該處**不適用** ——
該條之依據為「SYS1 相對 PDF 有偏離」，其預設 PDF 為正確者，
而此處該預設不成立。

處置三項：
(a) 該處之欄位以 `PENDING: DR-{n} …` 佔位（§8.4.3），不得留空、不得填 NA；
(b) 開 DR 向上游詢問**何者為權威**，並附兩版之逐字對照；
(c) 其所涉之 leaf 所屬 Test Set **不得開批**，直至該 DR 結案。

現行適用：outline `9.1` 之 PDF 句含 `aofnd`（非英文字）、
`the radio should shut Off the popup should close`（兩主謂相連無連接詞）、
`within 60 seconds the timeout defined in pop-up list`（兩時間條件並列
無連接詞）—— 形態為一次未完成之編輯，舊文字與新文字疊寫。
SYS1 之版本恰好刪去該兩段舊文字並將 `aofnd` 改回 `if`，
**故其可能是編輯之意圖而非漏字**。
→ **`DR-PMH4`**；`Power Transitions` 組（5 leaf，`SWE1-HMI-PM-018-01`～`-05`）
**凍結，不得開批**。
```

```
R-PMH70（立條後須處置該條所指認之對象）
新立之條文若其依據指認了某一具體對象（某支程式、某項判準、某份產出）
之缺陷，**該對象須於同一輪或次一輪內被處置**：改造、停用、或具名標註為
「已知不合本條而暫留」三者擇一，**不得只立條而讓該對象照原樣繼續運作**。

處置結果須於上繳具名；未處置者列入下一輪之待辦，不得靜默略過。

本條補 R-PMH62：該條只要求「回頭套用於支持該質疑之其他項」，
**未要求處置該條所指認之對象本身**。

依據：R-PMH66 立於 18 包，其依據即「6-gram 門檻做了本不該由它做的判定」，
而做那件事的 `bidirectional_spec_diff.py` 於同輪未被改造、未被停用、
亦未被標註，仍以門檻自動判定（18 包 §11 第 5 項，執行層自陳）。
```

```
R-PMH71（結論與其量測須可由同一支程式重現）
任何寫入 `RESIDUE_VERDICT`、`ANOMALIES.md` 或上繳包之人讀結論，
其**產生該結論之量測**須可由該檢查之預設設定重現。

若結論係以非預設之來源或參數查出（如 block 層萃取而預設為 `-layout`），
二者擇一：
(a) 將該來源／參數改為預設，並依 R-PMH35 補其 must-hit；或
(b) 於該結論處具名「本結論不可由預設設定重現」，並記其實際所用之設定。

**不得只留結論而不留其可重現之量測** —— 此為「宣告與實作分離」
（A-PMH12 形態）在結論層之同型。

依據：A-PMH16 係以 PyMuPDF block 層萃取查出，
而 `chapter_bidirectional.py` 之預設來源為 `pdftotext -layout`；
該程式此刻重跑**查不出 A-PMH16**（18 包 §11 第 1 項，執行層自陳）。
```

---

## 六、作業步驟

1. **抄錄** —— §五之 R-PMH69 ~ R-PMH71 逐字抄入 `RULINGS.md`，附核對表
   （依 R-PMH41 驗命中數）。

2. **章 7 之殘餘人讀（最高優先）** —— 以 `chapter_bidirectional.py` 跑章 7，
   殘餘逐句具名人讀結論。
   **並依 R-PMH71 先處理其預設來源**（見步驟 4）——
   若以 `-layout` 跑，A-PMH16 型之漏字查不出來。
   **章 7 為 batch 1 之來源章**；其結果決定 batch 1 之 8 條是否須重做。
   章 10、章 12 之殘餘於本輪一併處理（章 10 亦為 batch 1 之來源之一）。

3. **`DR-PMH4` 之開立（R-PMH69）** —— 登記於 `DATA_REQUESTS.md`，
   附 PDF 與 SYS1 兩版之**逐字對照**與 §2.3 之三處病徵。
   `DECISIONS.md` 記 `Power Transitions` 組（5 leaf）**凍結**。
   `ANOMALIES.md` 之 A-PMH16 補記 §2.2（第 3 處為獨立行為結果，非時序）
   與 §2.3（PDF 原句損壞）。

4. **`chapter_bidirectional.py` 之預設來源改 block 層（R-PMH71(a)）** ——
   此為判準變更，**其依據即 R-PMH71**，不另立條。
   **須附 must-hit**：以 `-layout` 為來源跑章 9 → A-PMH16 之三處**查不出**；
   以 block 層跑 → **三處全部進殘餘**。二者輸出並列。
   改後全六章重跑，殘餘數之變化逐章回報。

5. **`bidirectional_spec_diff.py` 之處置（R-PMH70）** —— 三者擇一並具名：
   改造為 R-PMH66 形態（門檻只分流、殘餘須人讀）／停用／
   標註為「已知不合 R-PMH66 而暫留」。
   **分析層傾向「停用」** —— 其功能已由 `chapter_bidirectional.py`
   以更嚴之判準涵蓋，兩支並存只會使人不知該信哪一支。
   **惟執行層得依實況擇定並載其理由。**

6. **120 字元截斷之影響量測（18 §11 第 3 項）** —— 三個數字：
   48 個 `section_title` 中被截者幾個、被截掉之總字數、
   被截掉之內容中含 marker 者幾處。**只量測，不改。**

7. **偽陰率之區間** —— 將 §4.3 之點估計改為附 Wilson 95% 區間之陳述
   （執行層 §11 第 4 項已自行算出 19%–81%），寫入 `challenge_rulings.py`
   之輸出，使其每次執行皆帶區間。

---

## 七、停止條件

canon §0 六條，另加本包三條：

7. 步驟 2 之章 7 殘餘發現**任一漏字或漏句**
   （若觸發，batch 1 之 8 條須全部重做，停並回報）
8. 步驟 4 之 must-hit（`-layout` 查不出／block 層查得出）未如期
9. 步驟 5 之處置為「暫留」而未具名其不合 R-PMH66 之處

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**不得改動 `scripts/new_feature.py`、`docs/runtime/` 下任何檔案、
任何他 feature 之檔案。**
**`Power Transitions` 組不得開批**（R-PMH69）。

---

## 八、上繳包要求（`docs/upstream/19_broken_source.md`）

1. §五三條之抄錄核對表（含命中數）
2. **章 7／10／12 之殘餘逐句人讀結論**（block 層）
3. `DR-PMH4` 全文 ＋ 兩版逐字對照 ＋ `Power Transitions` 凍結之登記
4. 步驟 4 之 must-hit 並列輸出 ＋ 六章重跑之殘餘數變化
5. 步驟 5 之處置與理由
6. 120 字元截斷之三個數字
7. 偽陰率之區間輸出
8. lint 全跑輸出
9. 未結 DR 清單（現應為 **4** 筆）
10. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
11. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 九、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **四筆 DR 之發出**（新增 `DR-PMH4`）—— 執行層已第六度重申前三筆。**`DR-PMH4` 直接凍結 `Power Transitions` 組（5 leaf）** | **DR-PMH1 阻斷交付；DR-PMH4 阻斷 ch 9 開批** |
| 2 | 18／19 之 commit 授權 | 否 |
| 3 | 17 §5.4 其餘五項 | Phase 5 |
| 4 | Q10、`PROFILE_INTEGRATION.md` | 否 |

---

## 十、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §五 |
|---|---|---|
| R-PMH69 | 來源本身損壞時不得逕以 PDF 為準；開 DR ＋ 凍結該組 | ✅ |
| R-PMH70 | 立條後須處置該條所指認之對象（補 R-PMH62） | ✅ |
| R-PMH71 | 結論與其量測須可由同一支程式之預設重現 | ✅ |

三條各管一事。
