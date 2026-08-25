# 下放包 29b —— ch 9 之限縮解凍（與 29 同一往返）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- **本檔不另佔往返編號** —— 與 [29_batch2_review.md](29_batch2_review.md) ＋
  [29a_dr_sent.md](29a_dr_sent.md) 同屬第 29 輪
- 29／29a 本文皆未改一字

---

## 一、Pei 之裁定（2026-08-25，逐字）

> 「乙」

即 29a §3.4 之（乙）案：**ch 9 限縮解凍**。

---

## 二、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH111（ch 9 之限縮解凍）
`Power Transitions` 組**解凍，得開批**。A-PMH18（p9 之能力矩陣無來源）
**維持 PENDING**，其阻斷範圍由「整組不得開批」限縮為下列條件式：

**任一 TC 之任一斷言若倚賴 p9 能力矩陣之內容，該條停並登記，不得產出。**

**判別法**（須逐條套用並具名結果）：該斷言之謂詞是否為
「**某受控對象於某電源狀態下是否可用**」——
受控對象指 `ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／`Headunit`，
電源狀態指 `KEY ON ENGINE ON`／`KEY ON ENGINE OFF (ACC or RUN)`／
`KEY OFF (No ACC position)`／`KEY OFF (ACC position available)` ×
`HEADUNIT POWER ON`／`OFF`。

**是 → 該條停**；否 → 得產出。

依據：ch 9 之 5 leaf 所依之 `PM1)` 其主題為 **IGN OFF 時之 popup 群**
（FOTA／Wi-Fi／Charge Now／`stay awake` 之時序），
**不涉及受控對象於各電源狀態下之可用性**（29a §3.2）。
二者主題不同，故 p9 之缺口不必然阻斷該 5 leaf。

**`DR-PMH5` 之(1)(2)兩問仍待答** —— 其答覆若確立 p9 之權威來源，
本組已產出之 TC 須依 R-PMH94 重掃其斷言。
```

```
R-PMH112（對上游已作陳述之更正義務）
我方於已發出之文件中對上游所作之作業狀態陳述，若其後因裁定而不再成立，
**須於下一次對外通信之首段更正之**，不得靜默改變作法。

現行適用：2026-08-25 發出之 `DR-PMH5` 逐字載
`Until (1) and (2) are clarified we have suspended test case authoring for
section 9 (Power Moding), which covers 5 requirements
(SWE1-HMI-PM-018-01 through -05).`
—— 該陳述因 R-PMH111 之解凍而不再成立。

**更正之載體為 `DR-PMH8`**（其尚未發出，狀態 `DRAFT`），
於其首段加入更正句；**不另發短箋**，以免對上游造成無謂之往返。
其逐字見 29b §三。

**更正之發出仍屬 Pei**（R-PMH83）—— 執行層只落檔。
```

---

## 三、`DR-PMH8` 首段之更正句（逐字，加於 29 包步驟 5 所擬三問之前）

```text
Subject: Power Moding HMI — three points of definition, and an update on our
section 9 status

Hello,

First, an update to our previous message. We wrote that we had suspended test
case authoring for section 9 (Power Moding). We have since resumed it: on
review, the five requirements in that section (SWE1-HMI-PM-018-01 through -05)
concern the pop-ups shown at ignition off and their timing, and do not depend
on the page 9 capability matrix, which is what our question was about. We will
hold back any individual test case whose expected result would depend on that
matrix, and our two questions about the matrix itself still stand.

Second, three points where the documents do not define something we need:

  [此處接 29 包步驟 5 所擬之三問 (a)(b)(c)]
```

---

## 四、對 29 包之影響

| 29 之節 | 原狀態 | 本檔之後 |
|---|---|---|
| §六 停止條件「ch 9 不得開批」 | 生效 | **解除**，改為 R-PMH111 之條件式（逐條判別） |
| §五 步驟 5（`DR-PMH8` 三問） | 待做 | **維持**，惟其首段加 §三之更正句 |
| 其餘步驟 1–4、6 | | 不受影響 |

### 4.1 增列之作業步驟

8. **ch 9 × 矩陣之全對照** —— 該對照因凍結而從未做（26 包 §12 所列）。
   **須先於 batch 3 之產出**，依 R-PMH79／R-PMH84／R-PMH91 為之。
   **發現牴觸即停並上呈。**

9. **batch 3 之產出 —— `Power Transitions`（7 leaf）** ——
   其範圍為 `SWE1-HMI-PM-002`（7.1.1）、`-018-01`～`-05`（9.1）、
   `-023`（10.5），**非只 ch 9 之 5 leaf**（Layer 2 定版之組為 7 leaf，R-PMH36）。

   **三項特別拘束**：
   (a) **9.1 之 `source_clause` 取自 SYS1，非 PDF**（**R-PMH75** —— R-PMH50
       於該 5 leaf 反轉），`source_clause_origin` 逐字記 `sys1_export 9.1`
       並註 `R-PMH75`；**7.1.1 與 10.5 仍取自 PDF**；
   (b) **逐條套用 R-PMH111 之判別法**，結果逐條具名（含「否」者）；
   (c) 依 R-PMH94／R-PMH97／R-PMH101 逐斷言導出限定與掃描；
       新斷言之掃描依 **R-PMH107(a)** 為義務，非新增檢查項。

   `tc_id` 續為 provisional；**零寫回工作簿**。

10. **`DR-PMH8` 之落檔** —— 首段更正句（§三）＋ 三問，
    標 `DRAFT`、`SENT` 欄留空。

---

## 五、停止條件（本包新增，與 29 §六並行）

10. 步驟 8 之 ch 9 × 矩陣對照發現**牴觸**
11. 步驟 9 之任一斷言經 R-PMH111 判別為**倚賴 p9** 而仍被產出
12. 步驟 9 之 9.1 五 leaf 有任一 `source_clause_origin` 非 `sys1_export`

---

## 六、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH111 | ch 9 限縮解凍；A-PMH18 之阻斷改為條件式判別法 | ✅ |
| R-PMH112 | 對上游已作陳述之更正義務；載體為 `DR-PMH8` 首段 | ✅ |

二條各管一事。**本檔未新增任何檢查程式或檢查項**（符合 R-PMH104）。

**待 Pei 者**：`DR-PMH8`（含更正句）之發出 ＋ 其日期與對象。
