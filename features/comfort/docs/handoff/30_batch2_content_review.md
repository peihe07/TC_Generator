# 30 — Comfort HMI / 批次 2 內容覆核：-024 拆分、-019 維持、R-C31

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/18_batch2.md` §2–§5、`19_batch2_complete.md`
- 判定：**14 條中 13 條通過，`-024` 須拆為四條。**

---

## 1. `-024`（`SWE1-HVAC-024-07`）—— **拆為四條**，推翻執行層之不拆判斷

### 1.1 §8.2.2 之控制實體判準為「條件」，非「許可」

執行層之依據為「§8.2.2 允許 RD sub-id ≠ TC count，**允許不等於要求**」。
該讀法漏了同條之後半，那一段不是許可而是判準：

> **Split condition when a sub-id bundles controls**: the same
> physical/logical control element → keep one TC with a multi-row ER;
> **different control entities → split into independent TCs**;
> independent partial failures under one sub-id → split and record.

溫度控制、RECIRC 鍵、mode 控制、MAX DEF 鍵為**四個不同的控制實體**，
且四者各自獨立可失效（執行層 §4.2 自己寫了「改溫度會破壞而改 RECIRC
不破壞，是可能的」）。兩個條件同時成立，**拆為條件所要求，非可選**。

### 1.2 locatability 不是 §8.3 之判準

執行層以「編號 ER 保證定位性，第 4 行失敗即知是 RECIRC 那一路」為不拆之
理由。**§8.3 之壓力測試問的不是定位性**：

> If only part of the behaviour fails, is my **pass/fail verdict** still
> unambiguous?

編號 ER 解決的是**失敗報告之粒度**，不是**判定之粒度**。四個獨立行為
共用一個 verdict，該 TC 之 pass 仍然只有一個意思、fail 也只有一個意思
——「其中某項壞了」。這正是 §7 所稱之 bundling。

### 1.3 與同批 `-021`／`-022`／`-023` 之不一致，是最直接的證據

同節之 A/C、AUTO、MAX A/C 三個破壞源各自成為一條 TC（`-021`／`-022`／
`-023`），因為 037 把它們各給了一個 leaf。而溫度／RECIRC／mode／再按
MAX DEF 四者**性質完全相同**（「按下 X → MAX DEF 關閉」），只因 037 把
它們併在一個 leaf，就變成一條。

**TC 之切分因此取決於上游的分節習慣，而非行為之獨立性** —— 這正是
§8.2.2 前半（不得再分解、合併 RD）與後半（TC 數不受 RD 數拘束）並存
的理由：前者管**溯源**，後者管**驗證粒度**，兩者不互相決定。

### 1.4 處置

拆為四條，`tc_id` 續編，**四條同溯 `SWE1-HVAC-024-07`**（§8.2.2
workbook handling：同一 leaf 之多條 TC 列相同 Requirement ID，tc_id 獨立
遞增）。每條之 `split_flag` 為真，`split_reason` 具名 §8.2.2 之控制實體
判準。

拆後之 title 須逐條帶其破壞源 token（§4.3 sibling-distinction）。
`design_method` 於拆後重新指派 —— 四條各自為單一狀態遷移，
**「決策表」於拆後不再適用**（§12 之 tie-break：多條件 → 決策表；
單一條件 → 狀態轉換）。

`-025`（風速改變**不**破壞）維持一條，且其 negative 配對關係改為對應
拆後之四條全體（§7）。

**其餘 10 條不受影響，不重跑。**

---

## 2. `-019`（`SWE1-HVAC-024-02`）—— **維持一條**，判斷正確

七項為**同一次按壓之同時後果**，spec 未將其區分為七個行為。

執行層之理由與 §5.7 明文一致，且該條正是為此形態而寫：

> **One trigger → multiple consequential outcomes belong in ONE TC, not
> split.** The trigger is the verification unit; outcomes that necessarily
> follow from the same trigger are facts to be checked, not separate TCs.
> Split criterion remains: different **triggers**, different **inputs**,
> different **scopes** — not different outcomes of the same trigger.

**§1 與 §2 之對照即 §5.7 之判準本身**：`-024` 是四個不同的 trigger，
`-019` 是一個 trigger 的七個 outcome。同一節、同一 parent、外觀相近，
**拆與不拆之方向相反**，而判準只有一條。

「拆成七條會產生 spec 不存在的區別，而每條都要重按一次 MAX DEF ——
那是測試設計上的重複，不是需求上的區別」一句，寫入 `RUNBOOK.md`。

---

## 3. `-023` 之 PC2（`MAX A/C 有無`，spec-derived）—— **通過**，並立條文

執行層自陳為「本包最可能被推翻者」，且已寫明其與 TC-007 之差別。
**該差別成立，判斷維持。**

```
R-C31  R-C28 第一問所謂「明文對應」，含句子自身之執行前提

第一問之通過條件，包含條文句子**執行上必然預設之裝備存在**：
條文描述對某裝備之操作，該裝備之存在即為該句之執行前提，非作者之補充。

不含由歷史、慣例或常態推得之**執行期狀態**。

判別：
- 「pressing MAX A/C turns MAX DEF off」→ 無 MAX A/C 則該句無從執行，
  裝備存在為句子所蘊含（R-C15 之蘊含判準）→ **通過**，標 spec-derived
- 「the user last selected …」→ 曾發生選擇行為，不蘊含恆有選定項；
  推的是歷史而非執行前提 → **不通過**（TC-007 前例）

推論：裝備類前提失敗於第一問時，其替代方案**不是移入 procedure**
（步驟裝不上裝備），而是該 TC 退回待軸之裁定。落點三問於此類止於第一問。
```

執行層指出之「真正的替代方案是該條退回」一句，即本條之末段，逐字採納。

---

## 4. 其餘 13 條 —— 通過

- **R-C29 首次適用（`-026`／`-027`）**：同一條 TC 之兩行 PC 指向兩個不同
  的他節（3.2 與 3.4），三項義務逐項落實。`specification_reference`
  **每項各帶完整 stem 而非只帶一次** —— 該作法正確且理由正確：
  「只檢查第一項再假設其餘相同，正是這條 pipeline 反覆栽的形態」
- **`-027` 之設計變更**（刪除「按其他 climate 功能鍵」之步驟）：正確且
  重要。初稿之 ER 與 2.10 明文牴觸，而**它會通過所有 gate，因為沒有任何
  gate 讀得到 2.10**。此為 §8.2.1 之正面案例：讀了 sibling 節才知道自己
  要寫的東西是錯的
- **climate off 落點於 procedure**：R-C28 第三問之正確適用，且為**生成時
  即照此處理**，非事後被抓
- **soft top 措辭**：`-028` 之 PC 寫 soft top、JL/JT 以 `such as` 引為例示
  —— 未犯反向造值
- **§9 自評 17 項依 R-C23 重做**：第 10 項明說「lint 依據為 `proc-er-1to1`
  ／`er-modal`，故另查可觀察」並逐行讀 49 行 ER；第 14／15 項明說 gate
  之涵蓋邊界並補查其外者。此即 R-C23 所要求之形態

---

## 5. 執行層作業指示

1. R-C31 原文貼入 `RULINGS.md`。
2. `-024` 依 §1.4 拆為四條，四條同溯 `SWE1-HVAC-024-07`；
   `design_method` 重新指派；title 逐條帶破壞源 token；
   `-025` 之 negative 配對關係更新。
   **後續 tc_id 順移**（`-025` → `-028` 之編號重排），
   於上繳包列出新舊對照表。
3. §2 之「測試設計上的重複，不是需求上的區別」寫入 `RUNBOOK.md`。
4. 全批重跑 lint 與 §9 自評（依 R-C23），僅回報變動項。
5. **不寫回 workbook。**
6. 其餘事項見下放包 31。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C31 第一問含句子自身之執行前提 | ✅ §3 | 已簽 2026-08-15 |

R-C31 適用全 feature，安置位置待 canon re-sync。§1 之拆分為 Part N 以下之
TC 切分，不入 `RULINGS.md`。
