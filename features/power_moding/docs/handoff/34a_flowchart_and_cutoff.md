# 下放包 34a —— A-PMH28 定案與 R-PMH121 核可（與 34 同一往返）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- **本檔不另佔往返編號** —— 與 [34_leaf_realign.md](34_leaf_realign.md) 同屬第 34 輪
- 34 本文未改一字

---

## 一、Pei 之裁定（2026-08-25，逐字）

> 「裁 出34」

### 1.1 解讀

**採「照分析層之提案裁定」** —— 34 §七所列之待裁三項中，
第 1、2 項各有分析層之提案，第 3 項為發文之動作。

| # | 事項 | 本檔之處置 |
|---|---|---|
| 1 | A-PMH28（流程圖之規範性） | 依提案定案 → R-PMH131 |
| 2 | R-PMH121（DR 未覆之交付截止規則） | 核可生效 → R-PMH132 |
| 3 | `DR-PMH8` 之發出 | **不視為已發** —— 無日期即為 `DRAFT`（R-PMH82）。**待 Pei 告知實際日期與對象。** |

**若原意與此不同，一句話可反轉。**

---

## 二、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH131（A-PMH28 定案 —— 流程圖之未涵蓋行為）
PDF p3–p7 流程圖文字層所載、而散文（p8–p11）**0 命中**之五類行為，
**不為其撰寫 TC**，登記為覆蓋缺口並併入 `DR-PMH8`。

依據：該五類行為於 037 **無對應 leaf**（其來源為流程圖而非散文，
037 之 `HMI Source ID` 皆指向散文之 outline），
依 **R-PMH55(b)**，無 leaf 之規格內容不得為其撰寫 TC。

**其與 R-PMH129 之 `-024` 同型且同時裁定**：
二者皆為「規格文件中存在、而 037 未納入」之內容；
其別在於 `-024` 之句因 SYS1 匯出漏句而未入 037（A-PMH03），
本五類因其載體為流程圖而未入 037（A-PMH04／A-PMH28）。
**處置相同：不寫 TC、登記缺口、入 DR。**

**其中 `toggle them one after another`（splash 之輪替順序）
直接落在 `-026`／`-033`／`-034` 之標的內** ——
該三條**維持不斷言其輪替順序**（§8.4.1 不造值），
其 `reasoning` 已具名，本條使該具名成為裁定而非暫置。

**流程圖之規範性本身仍未決** —— 本條只裁「不為其撰寫 TC」，
未裁「流程圖是否為規範性來源」。後者繫於 `DR-PMH8` 之答覆，
**須登記於 `PENDING-ON-DR`**：若上游確認流程圖為規範性且該五類應入 037，
則其成為新 leaf，屆時另批撰寫。
```

```
R-PMH132（R-PMH121 核可生效）
Pei 於 2026-08-25 核可 R-PMH121。DR 未覆之交付截止規則即刻生效：

(a) 交付日至而 `DR-PMH5`／`6`／`7`／`8` 有任一未 `ANSWERED` 者，
    **以現況交付**，其 TC 不因未覆而延；
(b) `PENDING-ON-DR` 登記簿之各筆**全數轉為交付揭露事項**，
    隨交付附一份「已知未決清單」，逐筆載其判定、所繫之問、
    及答覆為何值時該判定改為何；
(c) 停手之三筆（`-002`／`-023`／`-028`）另列一節，
    載其停手依據與其所需之上游輸入。

**連帶（本條生效後即須辦者）**：
`PENDING-ON-DR` 現有 10 筆，**須補入本輪所生之三筆**：
  `-024` 之撤除（繫於 `DR-PMH8` 之「該句是否應納入 037」）；
  A-PMH28 之五類（繫於 `DR-PMH8` 之流程圖規範性一問）；
  `-023` 之停手（繫於 `DR-PMH5`(1)(2)）—— **其狀態詞依 R-PMH130 維持，
  故其於未決清單中之出現理由為「待答」而非「已接受」**。
```

---

## 三、對 34 包之影響

| 34 之節 | 原狀態 | 本檔之後 |
|---|---|---|
| §四 步驟 5（`DR-PMH8` 增問） | 「與 A-PMH28 之第六問合為一節或分立，由執行層擇一」 | **維持該擇一**，惟二問**皆須入**（R-PMH129 ＋ R-PMH131） |
| §七 待 Pei 第 1、2 項 | 待裁 | **已裁**（R-PMH131／R-PMH132） |
| §七 待 Pei 第 3 項 | `DR-PMH8` 之發出 | **維持待 Pei** —— 無日期即 `DRAFT` |
| 其餘步驟 | | 不受影響，照原文執行 |

### 3.1 增列之作業步驟

8. **`PENDING-ON-DR` 補入三筆（R-PMH132）** —— 四欄齊備，
   第 (3) 欄逐值列出。

9. **`DR-PMH8` 之最終形態** —— 現 5 問，增二問：

```text
  Q6: The following clause appears in the logic and flow document but not in the
      SYS1 structured export, and consequently has no requirement in the SWE.1
      analysis report:

          SU1.) ... after the animation (3 sec) a splash screen is presented
          timeout (1.5 each).

      Should it be included in the analysis report? At present no test case
      covers it, because we do not author test cases for behaviour that has no
      requirement of its own.

  Q7: The flow diagrams on pages 3 to 7 contain statements that do not appear in
      the prose sections. One example, verbatim:

          If vehicle supports more than 1 Splash screen, toggle them one after
          another with a 1.5 timeout each

      Two questions: are the flow diagrams normative, and should the statements
      they contain that are absent from the prose be added as requirements? We
      have found five such statements and can list them all if useful.
```

   **狀態維持 `DRAFT`、`SENT` 欄留空。**

---

## 四、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH131 | A-PMH28 定案：不寫 TC、登記缺口、入 DR；流程圖之規範性本身仍未決 | ✅ |
| R-PMH132 | R-PMH121 核可生效；`PENDING-ON-DR` 補三筆 | ✅ |

二條各管一事。**本檔未新增任何檢查程式或檢查項**（符合 R-PMH104）。

**待 Pei 者一項**：`DR-PMH8`（7 問 ＋ 首段更正句）之發出日期與對象。
