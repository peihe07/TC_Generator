# 下放包 22 —— pop-up 組改判為牴觸、`VP` 之未定義與 batch 1 之連帶

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/22_popup_conflict.md`
- 前一包：[21_predicate_criterion.md](21_predicate_criterion.md) ＋
  [21a_dr_dispatch.md](21a_dr_dispatch.md)
  （上繳 [../upstream/21_predicate_criterion.md](../upstream/21_predicate_criterion.md)）

---

## 一、21 包之覆核結果 —— **通過**

五條抄錄逐位相符；七項重記依 R-PMH79 三分；`--export-residue` 首跑 FAIL 5 條
→ 補引後 0；DR 狀態機落地且「**（從未發出）**」已記入表。

**三項特別記明**：

1. **§3.1 之 `Radio OFF` 誤命中** —— 不敏感比對使其誤中 `Radio Off Delay`
   **15 次**，改大小寫敏感後歸零。**這是「探針本身會說謊」之實例**，
   且是在自己的範圍向裡抓到的。
2. **§6 之停止條件自檢** —— 三條皆判「一致」而**各自具名其弱點**
   （8 為列舉式只攔兩詞；9 只驗「有引用」不驗「切題」）。
   **判過關而仍指出其限度，這是自檢該有的樣子。**
3. **§13 第 6 項之當場更正** —— 自陳 `matrix_vs_chapter.py` 無 must-hit，
   依 R-PMH35(c) 其結果**只得標「未實測」**，
   **「而我在 §10 之總表裡標了 PASS。據實更正於此。」**

---

## 二、§13 第 1 項 —— `VP` 我查了：**規格全文 0 命中**

執行層自陳「`VP` 這個詞在矩陣裡出現數十次而我從未查明它指什麼」，
並指出若 `VP` 即 ch 7 所說之螢幕，則其 30 列之判定基礎動搖。

**量測條件**：PDF 全文（`pymupdf`，11 頁 15,751 字元）與 Excel 全簿
（`openpyxl` `read_only`）各以 `VP` 為子字串掃描。

| 來源 | `VP` 之命中 |
|---|---|
| **規格 PDF（全 11 頁）** | **0** |
| Excel State Matrix | **30 格** |

### 2.1 由用法可定其功能，但不可定其指涉

矩陣中之 `VP` 有三種用法：

```
VP Stays ON / VP Turns OFF
VP display pop-up: "Power OFF System. Continue call on mobile phone? Yes or NO"
(R1Low) VP Stays ON  (R1High) VP display pop-up: …
If Radio Off Delay = 0 minutes then VP turns OFF Else VP stays ON
```

**其功能明確**：`VP` 是**會開關、且會顯示 pop-up 之物**。
**其指涉不明確**：規格未定義該縮寫，本 feature 之六筆素材亦無定義。

**執行層之疑慮成立**：若 `VP` 即螢幕，則
`VP display pop-up` 與 `SU3.)` 之 `No pop-ups will appear` **為同一謂詞**，
其 30 列之「未對照」判定即須重看。

**但「由用法推定其為螢幕」是我們不該做的推定** ——
**規範性素材使用了一個規格未定義之術語**，該事實本身即應上呈。
→ R-PMH85、`DR-PMH7`。

---

## 三、§13 第 2 項 —— **執行層之自我質疑成立，pop-up 組改判為「牴觸」**

執行層自陳：

> 我說「矩陣之軸不含 disclaimer 狀態，故二者不在同一命題上」——
> **但全稱否定之涵蓋範圍是所有時刻**，矩陣之無條件肯定落在其中一個時刻
> 即為牴觸。**我把「矩陣沒說是否在 disclaimer 期間」當成「矩陣不涉及
> disclaimer 期間」，那是兩件事。**

**該自我質疑成立，我採之。**

### 3.1 逐項

`SU3.)`（outline 7.4，`Disclaimer Screen` 組之 `-007` 所依）逐字：

> `No pop-ups will appear until the disclaimer screen has been removed…`

**全稱否定，其範圍為「免責畫面移除前之所有時刻」。**

矩陣之 pop-up 諸格（`r6`／`r15`／`r24`／`r25`／`r48`）為**無條件肯定**，例：

| 格 | 內容 | 其條件 |
|---|---|---|
| `r6`（`Key-on` × `ON/OFF button Pressed`） | `VP Stays ON Pop-up: Cannot Power Off System during active phone call.` | Key-on × HU on × **Call Active** |
| `r24`（`Key-off` × `ON/OFF button Pressed`） | `VP display pop-up: "Power OFF System. Continue call on mobile phone? Yes or NO"` | Key-off × HU on × Call Active |
| `r48`（`Gear = Reverse` × HVAC 硬控） | `Show Pop-Up …` | Key On × Gear = Reverse × Power Button OFF |

### 3.2 共同謂詞成立，且條件**未被證明互斥**

- **共同謂詞**：pop-up 是否顯示。`SU3.)` 取「不顯示」，矩陣取「顯示」。
- **條件互斥？** 免責畫面出現於開機序列（Key-on）。
  `r6` 之條件為 Key-on × Call Active —— **開機時電話已在通話中，是可發生之情形**
  （使用者於上車前已通話）。**二者可同時成立。**

**故依 R-PMH79，此為牴觸，非未對照。**

### 3.3 判準之補強：**條件互斥須被證明，不得被假定**

執行層之原判定並非草率 —— 它是被 R-PMH79 之「無共同謂詞 → 未對照」
這一支所吸收。**R-PMH79 沒有處理「有共同謂詞、而條件是否重疊未知」之情形。**

→ R-PMH84 補之。

### 3.4 **這直接命中 batch 1**

`-007` 之 ER 斷言「免責畫面顯示期間無 pop-up」，而規範性矩陣載有
「該期間可能出現之 pop-up」。**`-007` 須依 R-PMH80 之形態處置**
（限縮 ＋ 揭露），不得維持無條件之斷言。

**lint 30/30 全綠而此事未被攔** —— 與 A-PW68 同一形狀之第三次。

---

## 四、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH84（條件互斥須被證明，不得被假定）
二陳述有共同謂詞而取相反值時，**除非其條件已被證明互斥，否則判為牴觸**。

「素材未提及某條件」**不等於**「素材不涉及該條件」——
前者是素材之沉默，後者是一個關於素材涵蓋範圍之主張，須有依據。

具體：一方為**全稱否定**（`No X will appear until Y`）而另一方為
**無條件肯定**（`Show X`）時，全稱否定之範圍涵蓋所有時刻，
無條件肯定落於其中任一時刻即成牴觸。**判為「未對照」者，
須具名指出使二者條件互斥之依據**；無依據即為牴觸。

R-PMH79 之「未對照」一支自此限縮為：**無共同謂詞**，
或**有共同謂詞而條件已證互斥**。

依據：21 包 §3.3 將 `SU3.)`（`No pop-ups will appear until the disclaimer
screen has been removed`）與矩陣 `r6`／`r15`／`r24`／`r25`／`r48` 之
pop-up 諸格判為「未對照」，其理由為「矩陣之軸不含 disclaimer 狀態」——
而免責畫面出現於開機序列（Key-on），`r6` 之條件為 Key-on × Call Active
（使用者上車前已通話），**二者可同時成立**。
由執行層於 21 包 §13 第 2 項自陳（22 包 §三）。
```

```
R-PMH85（素材使用規格未定義之術語）
規範性素材若使用**規格全文 0 命中**之術語，該術語之指涉**不得由分析層或
執行層推定**，縱其用法可推知其功能。

處置三項：
(a) 登記於 `ANOMALIES.md`，載其命中數（素材側／規格側各若干）與其用法之逐字；
(b) **開 DR 詢問其定義**；
(c) 在該 DR `ANSWERED` 前，**凡以該術語為據之對照判定，一律標「待定義」**，
    不得判為「牴觸」或「未對照」——**該判定所需之語意尚未存在。**

現行適用：`VP` —— 規格 PDF 全 11 頁 **0 命中**，Excel State Matrix **30 格**。
其用法為 `VP Stays ON`／`VP Turns OFF`／`VP display pop-up: "…"`，
可知其為「會開關且會顯示 pop-up 之物」，**惟其指涉未定義**。
→ **`DR-PMH7`**。

**與 R-PMH84 之關係**：本條優先。若某對照之判定倚賴 `VP` 之指涉，
則其記法為「待定義」而非 R-PMH84 之「牴觸」；
**惟 §三之 pop-up 組不倚賴 `VP` 之指涉** —— `r48` 之
`Show Pop-Up` 未用 `VP` 一詞，其牴觸獨立成立。
```

```
R-PMH86（`matrix_vs_chapter.py` 之結果標未實測）
`matrix_vs_chapter.py` 於補上 must-hit 前，其結果**只得標「未實測」**，
不得標 PASS（R-PMH35(c)）。**採認執行層 21 包 §13 第 6 項之自我更正。**

其 must-hit 之最低要求：
(a) 將一組已知之真牴觸（`10.3` × `r48c10`）餵入，**檢查須報「牴觸」**；
(b) 將一組已知之真印證（`10.1` × `r40`／`r44` 之 `Event ignored`）餵入，
    **檢查須報「印證」**；
(c) 將一組無共同謂詞者餵入，**檢查須報「未對照」**。

三者皆為**正向錨點**（must-hit 於此為「須報出該記法」而非「須 FAIL」）——
本檢查之輸出為三分類而非二值，故其錨點形態隨之。
```

---

## 五、作業步驟

1. **抄錄** —— §四之 R-PMH84 ~ R-PMH86 逐字抄入 `RULINGS.md`，附核對表
   （依 R-PMH41 驗命中數）。

2. **pop-up 組之改判（R-PMH84）** —— `r6`／`r15`／`r24`／`r25`／`r48`
   五格對 `SU3.)` 之記法由「未對照」改為 **「牴觸」**，
   `VERDICT` 逐格具名其共同謂詞與「條件未證互斥」之理由。
   **21 包 §3 之「牴觸 0／未對照 30」須連帶更正**，其原文保留（R-PMH44）。

3. **`-007` 之處置（比照 R-PMH80）** —— **本輪只出處置方案，不改 TC**：
   回報 `-007` 若加 Pre-Condition「無進行中之通話」（或其他可使 `SU3.)`
   之斷言成立之限定）之可行性，並列出其所需之來源依據。
   **不自行選定限定條件** —— 其選擇涉及規格解讀，交分析層。

4. **`DR-PMH7` 之開立（R-PMH85）** —— 索取 `VP` 之定義。
   問題全文須含：規格側 0 命中、素材側 30 格、三種用法之逐字，
   並問「`VP` 是否即 head unit 之顯示螢幕」。
   **依 R-PMH82 標 `DRAFT`**，發出授權待 Pei。

5. **`matrix_vs_chapter.py` 之 must-hit（R-PMH86）** ——
   依 §四之 (a)(b)(c) 三項正向錨點實作並實跑；
   **§10 之總表於錨點通過前，該列標「未實測」**。

6. **章 8 × 矩陣之對照（21 §13 第 3 項）** —— `Startup Sounds`（6 leaf）
   為 batch 2 之候選，其對照為開批前置。
   依 R-PMH84 之補強判準為之，**發現牴觸即停**。

7. **停止條件 8 之偽陰抽樣（21 §13 第 4 項，R-PMH67）** ——
   該條為列舉式（只攔「無矛盾」「非牴觸」二詞）。
   自本 feature 之上繳包中隨機抽 10 處對照結論，
   人讀判其是否為「應被攔而未被攔」之措詞（如「相容」「未發現問題」
   「一致」），回報偽陰率之點估計與 Wilson 區間。

---

## 六、停止條件

canon §0 六條，另加本包三條：

7. 步驟 6 之章 8 × 矩陣發現**新的**牴觸（未經登記者，R-PMH77(a)）
8. 步驟 5 之三項正向錨點有任一項未報出其應報之記法
9. 步驟 2 之改判後，`VERDICT` 有任一格之「牴觸」未具名其共同謂詞

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**ch 9（`Power Transitions`）不得開批**（`DR-PMH5` 未 `ANSWERED`）。
**`-007` 於其處置定案前，batch 1 不得提交寫回。**
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 七、上繳包要求（`docs/upstream/22_popup_conflict.md`）

1. §四三條之抄錄核對表（含命中數）
2. 步驟 2 之改判表 ＋ 21 包 §3 之連帶更正（原文保留之證明）
3. 步驟 3 之 `-007` 處置方案與其來源依據（**不改 TC**）
4. `DR-PMH7` 全文（標 `DRAFT`）
5. 步驟 5 之三項正向錨點實跑
6. **步驟 6 之章 8 × 矩陣全對照表**
7. 步驟 7 之偽陰抽樣（10 處 ＋ 點估計 ＋ Wilson 區間）
8. lint 全跑輸出
9. 未結 DR 清單（現應為 **3** 筆，狀態依 R-PMH82）
10. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
11. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 八、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH5`／`6` 之實際發出 ＋ 日期與對象** | `DR-PMH5` 阻斷 ch 9 |
| 2 | **`DR-PMH7`（`VP` 之定義）之發出授權** | 矩陣對照之判定（R-PMH85(c)） |
| 3 | **`-007` 之限定條件如何選** —— 步驟 3 回報後由分析層擬案、Pei 裁 | **batch 1 之寫回** |
| 4 | 9.1 之 `source_clause` 例外是否寫入 profile | `Power Transitions` 開批前 |
| 5 | 17 §5.4 其餘五項；Q10、`PROFILE_INTEGRATION.md` | 否 |

---

## 九、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §四 |
|---|---|---|
| R-PMH84 | 條件互斥須被證明，不得被假定；R-PMH79 之「未對照」一支限縮 | ✅ |
| R-PMH85 | 素材使用規格未定義之術語 → 標「待定義」並開 DR | ✅ |
| R-PMH86 | `matrix_vs_chapter.py` 標未實測；三分類之正向錨點 | ✅ |

三條各管一事。R-PMH84 為**限縮型**，其所限縮之條文與範圍已於條內明載。
