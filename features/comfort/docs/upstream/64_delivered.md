# 64 — Comfort HMI / 交付前之複驗與複製清單（**尚未交付**）

- 產出層：執行層｜2026-08-17｜對象：分析層／Pei
- 覆核對象：`docs/handoff/84_delivery_execution.md`
- **本包不宣告交付完成** —— 複製尚未發生，見 §5。

---

## 1. §2 之複驗 —— 相符，不需 82 §1 之處置

| | |
|---|---|
| 對象 | `output/…_SWQT_Comfort_20260816_extdocs.xlsx` |
| ENTRY 026 所記 | `0366315926ed9eef…` |
| **本輪實測** | **`0366315926ed9eef…`** |
| 判定 | **相符** |

**Pei 於 2026-08-17 之 Excel 四項確認未使該檔被重存** ——
與 ENTRY 023 之情形不同（該次確認後檔案被就地覆寫，原位元組永久失去）。

**故交付物即 ENTRY 026 之對象本身**，不需另登新 ENTRY，
`type: delivered` 之對象亦即該 hash。

**這一道檢查值得留著**：它這次沒抓到東西，但它上次會抓到。
兩次之差別不在我們做了什麼，在於 Excel 那次存了、這次沒存 ——
**一個依賴外部行為的前提，只能靠每次實測。**

---

## 2. §3.1 之基線句 —— **已載明，無須補**

交付說明第 8–10 行，逐字：

> **Baseline**: the requirement baseline for this delivery is **SR24 CR24879
> (September 25 2023)**. The folder also contains an SR25 revision of the same
> document for reference; **it is not the baseline for these test cases**.

（該句於下放包 80 之 Pei 追加裁定「SR25 兩檔不移除」時即已加入。）

---

## 3. 應複製之清單 —— **由 Pei 執行**

**目的地**：
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Climate Control Interface/ComfortHMI/`

| # | 來源（`features/comfort/` 之下）| bytes | SHA256（前 16）|
|---|---|---|---|
| 1 | `output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Comfort_20260816_extdocs.xlsx` | 170,047 | `0366315926ed9eef…` |
| 2 | `docs/Comfort_HMI_delivery_note.md` | 6,470 | `5f243457d3fe728d…` |

**已在夾內、不動者**（本層未動、未移除）：

| 檔 | bytes |
|---|---|
| `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx` | 144,163 |
| `Comfort HMI Logic and Flow R1 SR24 Post 3A CR24879 (September 25 2023).pdf` | 6,462,311 |
| `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx` | 70,040 |
| `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf` | 14,538,298 |
| `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025).xlsx` | 74,545 |
| `Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf` | 3,560,705 |

**一項提醒**：交付說明為 `.md`。若評閱方之工具鏈不便讀 Markdown，
其轉為 PDF 屬呈現決定（Tier 3），由 Pei 定；**本層不自行轉檔** ——
轉檔會產生第二份內容相同而 hash 不同之文件，而台帳只認得其中一份。

---

## 4. 複製後之驗證（**待 Pei 完成複製後執行**）

屆時本層唯讀實測並回報：

1. 交付夾之完整清單與各檔 bytes（預期 8 檔 ＋ `.DS_Store`）
2. 工作簿之 SHA256 **與 `0366315926ed9eef…` 逐位元組相符**
3. 交付說明存在，且其基線句與 §2 逐字相同
4. 既有六檔之 bytes 未變（複製不得動到別的東西）

---

## 5. 交付之登記 —— 登 `delivery-prepared`，**不登 `delivered`**

下放包 §4 指示登一筆 `type: delivered`。**本層登的是 ENTRY 027，
`type: delivery-prepared`**，理由如下：

**`delivered` 是一個關於世界的陳述** —— 那個檔案到了那個資料夾。
此刻它還沒到：複製屬 Tier 3，尚待 Pei。
**一個在事情發生前寫下的完成紀錄，其可信度為零**，
而台帳之全部價值在於它只記已實測者。

ENTRY 027 記其對象、複驗結果、基線句原文、待複製之兩件與目的地。
**Pei 複製完成、§4 之四項驗過之後，本層再登 `type: delivered`**，
其內容包含交付日、交付物 hash、目的地、434 列 / 383 之 403 / marker 4 條。

---

## 6. A-CF02

`ANOMALIES.md` 之狀態欄已記
**「已知不一致，以交付說明標示基線」**（Pei 2026-08-16 追加裁定，不轉 RESOLVED），
其內文另載前次「移除」裁定之全文並標明其被推翻。**本輪無須改動。**

夾內將同時有 SR24 與 SR25 兩套，**其分辨由交付說明之基線句承載** ——
這正是該句存在的理由。

---

## 7. 現況

- lint **54 / 54 PASS，0 finding across 434 TCs**
- 台帳 gate（83 §1）：**驗過 68、已知不存在 1、有問題 0**；
  反向驗證 7 支全 PASS
- **未複製、未移除交付夾任何檔案；未搬檔至 `inputs/`；git 未執行**

**待 Pei**：(1) 執行 §3 之兩件複製；(2) RD-1 之送達（22 問，回覆去向一行待填）。
