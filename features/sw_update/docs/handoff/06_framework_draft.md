# 下放包 06 —— 上繳包 04 審結、T18d 體例裁定、framework 草案與定稿前置量測

- 日期：2026-08-27
- 方向：分析層 → 執行層
- 前一包：`05_framework_survey.md`；對應上繳：`docs/upstream/05_framework_data.md`
- 裁定狀態：R-SU10（Layer 2 分群鍵）、R-SU11（SYS1 之橋接軸）——分析層即裁；
  T18d 之字面比對選擇 —— **採認**；framework —— **草案，未定稿**

---

## 一、上繳包 04 審查判定

**收。** 三項閉合檢查（311／120／87+487）全通過，量測腳本可重跑。

### 1.1 T18d 之「字面比對而非語意比對」—— 採認，且判斷正確

執行層之推理成立且重要：語意判定會使執行層實質參與 Layer 2 分群決策，
而 T18d 明令不得逕定；字面比對之偏差方向可預期（只漏配、不錯配成
看似合理者），語意比對之偏差則混入判斷而難以識別。

**此為「工具選擇本身即是權限邊界」之正確操作，記入本案例。**
下放包 05 §三 T18d 之措辭「依標題語意標註」與其後之「不得逕定」相衝突 ——
**衝突為分析層之措辭瑕疵**，執行層取嚴解為正。往後同型任務，
分析層應直書比對方法（字面／詞集／向量），不以「語意」一詞含混帶過。

語意層對照由**分析層自行執行**（見 §三），不下放。

### 1.2 三項結構事實 —— 全部採認為起草前提

(1) Heading 標題 45 個僅 41 unique（4 組碰撞）→ R-SU10
(2) 037 章節骨架承自 CFTS_57（93%）而非 SYS1（4%）→ R-SU11
(3) HMI 87 列集中於 17 個 Heading，另 28 群（224 列）純 Service → §三 3.3

---

## 二、裁決條文（抄入 RULINGS.md，逐字；索引表同步）

```
R-SU10（Layer 2 分群鍵）

037 之 `Categorization == Heading` 45 列，其標題僅 41 unique ——
`Critical Updates`、`OTA Architecture Requirements`、
`OTA Client Configuration options`、`User initiated sessions`
各出現兩次而轄不同區間（上繳包 04 §3.1 實測）。

裁定：
(a) framework 之分群鍵一律為 **Heading id**（`SWE1-FOTA-{n}`），
    不得以標題字串為鍵。
(b) Test Set 名稱由分析層另行命名（IN §4.2：能力叢集名詞，1–3 字），
    **不得逕取 Heading 標題**；Heading 標題僅為命名之素材。
(c) `framework.md` 之 Layer 3 欄須同時記 Heading id 與其標題原文，
    俾碰撞可見。
```

```
R-SU11（SYS1 之橋接軸）

037 Heading 與 SYS1 章之標題對照率僅 2/45（上繳包 04 §3.2 實測），
且 2 筆同對一章。成因：SYS1 之 28 章為 **HMI 畫面／流程視角**，
037 之 45 Heading 為**需求功能視角**，兩者非同一骨架之兩份副本。

裁定：
(a) framework 之 Layer 3 **主軸為 CFTS_57 章節**（對照率 42/45）。
(b) SYS1 **不作章對章之橋接**。SYS1 之接點為 037 之 **HMI 87 列**
    ——逐列（非逐 Heading）對 SYS1 之 120 個 outline entry 定位。
    此定位屬 Phase 2/3 之錨定協定，本條只定其軸，不定其方法。
(c) 純 Service 之 28 個 Heading 群（224 列）無 SYS1 接點，
    其 spec_reference 走 CFTS 家族單軌（R-SU4 v2(a)）；
    此為**預期狀態**，不因缺 HMI 錨而登記異常。
```

---

## 三、framework 草案（**草案，未定稿；不得據以撰寫任何 TC**）

Layer 1 Test Group = `SW Update`（R-SU1）。

Layer 2 之候選叢集如下，各群之列數已閉合至 311。**名稱為暫定**，
定稿條件見 §四。

| # | Layer 2 候選 | 所轄 Heading id | 列數 |
|---:|---|---|---:|
| 1 | `Wi-Fi Download` | 038, 058, 055 | 29 |
| 2 | `Update Policy` | 009, 024 | 17 |
| 3 | `Silent Update` | 178 | 6 |
| 4 | `Session Flows` | 016, 017, 018, 137, 168, 185, 188, 271, 278, 287 | 42 |
| 5 | `Client Architecture` | 072, 073, 192, 200, 202, 251, 259, 263, 266, 280, 285, 291 | 51 |
| 6 | `ROV Installation` | 085, 086, 091, 096 | 20 |
| 7 | `TBM Update` | 110, 214 | 50 |
| 8 | `Security` | 022, 170, 309 | 77 |
| 9 | `USB Update` | 020, 074, 076, 078 | 5 |
| 10 | `Update HMI` | 129 | 6 |
| 11 | `Configurable Parameters` | 125, 127 | 2 |
| 12 | `FOTA Overview` | 001 | 6 |

閉合：29+17+6+42+51+20+50+77+5+6+2+6 = **311** ✅

### 3.1 草案之兩個已知弱點（定稿前必須解決，不得帶入 Phase 4）

**(a) 第 8 群 `Security` 之 77 列由單一 Heading `SWE1-FOTA-309`
（70 列）主導，而該 Heading 標題為 `OMA-DM Security`。**
CFTS_57 之對應章 `4.8.2 OMA-DM Security` 僅轄 **3** 個需求物件
（上繳包 04 T18c 實測）。70 ≫ 3 —— 強烈提示該 Heading 之標題
**不描述其所轄之全部區間**（310–383 很可能跨越 CFTS §4.9／§4.10／
§4.13 等多章）。此群在 IN §4.1.3 之意義下等同「Misc」，**不可交付**。

**(b) 第 5 群 `Client Architecture` 之 51 列吸收了
`Bearer selection:`（16 列）、`Vehicle Properties`（3 列）、
`Interface Definitions`（NFR 4 列）等異質內容**，同有 Misc 之嫌。

兩者皆須待 §四 之列標題實測後重切。

### 3.2 CFTS 未命中之 3 筆 —— 分析層之語意判定（§1.1，不下放）

| Heading | 037 標題 | 分析層判定之 CFTS 對應 | 依據 |
|---|---|---|---|
| `SWE1-FOTA-178` | `For a silent update, the OTA client follows these steps` | **4.7.3.2 Silent Updates**（13 需求物件） | 037 標題為 CFTS 該節之內文引導句；其下 6 列為靜默更新步驟 |
| `SWE1-FOTA-259` | `Vehicle Properties` | **待驗**（候選 4.4 OTA Client Architecture） | 無足夠字面線索，不臆斷 |
| `SWE1-FOTA-291` | `Bearer selection:` | **待驗**（候選 4.5 Interface Definitions／4.6） | 16 列之內容未知，不臆斷 |

178 之判定為分析層對自身可見證據所作，仍須 T19 之列標題複核；
259、291 **不判定** —— 缺證據而給對應即為造值（IN §8.4.1）。

### 3.3 HMI 集中之結構後果（記錄，供 Layer 2 命名參考）

17 個 Heading 承載全部 87 個 HMI 列，前 5 群佔 69%。IN §4.1.3 之
「同 Test Set 應蘊含共同 UI 入口路徑」**只在該 17 群內成立**；
其餘 28 群為 Service 層行為，其 Test Set 之健康判準改以
「共同觸發面與共同觀察面」為之（R-SU11(c) 之延伸，不另立條文）。

---

## 四、任務（T19：定稿前置量測）

**目的**：解 §3.1 之兩個弱點與 §3.2 之兩筆待驗。**只量測，不分群、不命名。**

| # | 任務 |
|---|---|
| T19a | **`SWE1-FOTA-309` 群（310–383，70 列）逐列傾印**：id、`Requirement Title`、`Sub Categorization`、`Source Requirement ID`。**併**：以每列標題對 T18c 之 87 個 CFTS 章節做同一詞集重疊比（門檻與 T18d 一致），輸出每列之最佳候選章與分數 —— 用以測定該 70 列橫跨幾個 CFTS 章 |
| T19b | 同法傾印 **`SWE1-FOTA-291` 群（292–308，16 列）** 與 **`SWE1-FOTA-259` 群（260–262，3 列）** |
| T19c | 同法傾印 **`SWE1-FOTA-214` 群（215–250，36 列）** 與 **`SWE1-FOTA-137` 群（138–167，26 列）** —— 此二群列數次大，須確認其未同樣跨章 |
| T19d | **全 311 列之 CFTS 逐列對照**（非逐 Heading）：輸出每列之最佳候選 CFTS 章與分數，並統計「列所屬 Heading 之 CFTS 對應章」與「列自身之最佳候選章」**不一致**之列數與清單。此為跨章問題之全域測度 |
| T19e | **`SWE1-FOTA-178` 群（179–184，6 列）逐列傾印**，供複核 §3.2 之 178 判定 |

方法拘束：詞集重疊比之參數（停用詞表、門檻 0.34）與 T18d **完全一致**，
於上繳包揭露；**不得改用語意比對**（§1.1）。分數僅為排序工具，
不作對應之結論 —— 結論由分析層下。

輸出置 `docs/upstream/05_framework_data.md`；腳本沿用
`scripts/framework_survey.py`（加項次，不改既有項之行為）。

---

## 五、任務彙總

| # | 任務 |
|---|---|
| T-抄 | R-SU10、R-SU11 逐字 append 入 `RULINGS.md`；索引表依 R-SU8(b) 同步（11 條現行 + 2 條留存）。程式回讀逐字元核對 |
| T19a–e | §四 之五項量測 |

**不在本輪**：framework 定稿、Test Set 命名、錨定協定、任何 TC、寫回、git。

---

## 六、上繳包要求（`docs/upstream/05_framework_data.md`）

1. T-抄 核對結果 + 索引表全文
2. T19a–e 逐項量測結果（原始輸出）
3. T19d 之不一致列清單（此為本輪最關鍵之產出）
4. 未結 DR 清單
5. 獨立自評
6. 量測條件揭露（R-G8）：詞集參數須與 T18d 逐項對照確認一致
