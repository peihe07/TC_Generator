# 21 — Comfort HMI / TC-010・TC-012 裁定 ＋ R-C23 ＋ 第五項發現

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/12_pilot_rev2.md`
- 判定：四個 defect 修正**全數接受**。TC-010／TC-012 裁 BLOCKED，
  需新 marker。另有 defect ×1（系統性，12 條皆涉）。

---

## 1. TC-010／TC-012 —— 三選一皆不採，裁 BLOCKED row ＋ 新 marker

### 1.1 先排除兩項

**「併入 -01 之 coverage」不可行** —— §8.2.2 明文：「TC 作者不得將多個 RD
sub-id 合併為一個 TC。RD 層級之合併屬 RD 作者，非 TC 作者。」一個 TC 掛兩個
Requirement ID 即為該條所禁之形態。

**「維持現狀並於 remarks 標記」不可行** —— 扣除委派後餘留為 ∅，該 TC 之
procedure 只能複製 -01。**一條會通過但不驗證其 leaf 所要求之事的 TC，
即 §7 之 False Pass**，且 remarks 之標記不會使它停止通過。

### 1.2 「餘留為 ∅」之判定成立

複核 §2.1 之全文證據：

- `-080-01` VC Action 已為 `Long press (-, +) hard button **or touchscreen
  control**` —— 兩個操作面本就同屬 -01。rev1 把 -02 寫成觸控面分支確為
  037 未作之區分（§8.4.2 造範圍）
- `-080-02` 全部內容 = `logic as per HMI Core Logic and Flow (requirement
  N0)`；其門檻／速率／加速曲線已於 19 §4.1 判 out of scope
- `-081-02` 全部內容 = `equivalent to short press of previous 4-way rocker`；
  其等效基準由 CFTS044 擁有（19 §4.2）

三者相加，**該二 leaf 於 Comfort 範圍內無任何可獨立驗證之內容**。判定成立。

### 1.3 裁定

```
R-C24  外部 spec 全權委派之 leaf —— BLOCKED row ＋ [BLOCKED-SPEC]

某 leaf 之全部內容為對外部 spec 之委派或等效性宣告，扣除該委派後於本
feature 範圍內無任何可獨立驗證之餘留者：**產出 BLOCKED row，不省略、
不併入 sibling leaf、不以複製 sibling 之 procedure 充數。**

marker：`[BLOCKED-SPEC]`，置於 Remarks 之開頭 token。

BLOCKED row 之內容：
- `test_procedure` / `expected_result`：空
- `specification_reference`：該 leaf 自身之 outline，照常填
- Remarks：`[BLOCKED-SPEC]` ＋ 擁有該內容之文件名 ＋ 一句說明何以無餘留
  （外部可見，不得出現內部 ruling id 或 A-CF 編號，AMFM R10-4）
- 其餘欄位依 profile 常規

**與 Privacy `[BLOCKED-ECU]` 之區別須寫入 profile §5**：前者為「行為由
另一 ECU 執行，本 ECU 無可觀察端」；本條為「行為可觀察，但其規範內容
由另一份 spec 擁有」。兩者外觀相同（皆無 procedure），成因不同，
不得互相類推。

**lint 之豁免必須是具名回報項，不得為條件式中之靜默跳過**（前例：
上繳 06 §2.1 之 `and n != "Comfort Widget"`）。`proc-min-steps`、
`proc-er-1to1` 對 BLOCKED row 之豁免，須以獨立回報行輸出，形如：
`- PASS — rows exempted as BLOCKED-SPEC: ['NR1L-ComfortHMI-010', ...]`
使豁免在每次 lint 輸出中可見。
```

### 1.4 連帶

- **coverage 分母不變**：403 leaves，14 條 pilot，兩條為 BLOCKED row，
  無 leaf 遺失
- `split_flag` / `split_reason` 恢復其本義（是否因 §8.2.2 而拆），
  **不再承載本裁定之說明** —— 那屬 Remarks
- `distinguishing_axis` 之 `delegated-only` 一併移除：該二 TC 已非
  sibling 之一支，而是 BLOCKED row
- **RD-1 候選（新增）**：Core N0 與 CFTS044 之對應行為，於本專案是否有
  其他 feature 之 SWE 需求涵蓋？若無，則為真實 coverage hole（§8.4.2）。
  登 `DATA_REQUESTS`，**不阻塞**

---

## 2. 第五項發現（回答 §8.3 之問）—— DEFECT：baseline 步驟之 ER 陳述行為者錯誤

執行層問「是否還有我未察覺的第五項」。**有，且為系統性。**

TC-012 ER1：`The lumbar/bolster state shown before the adjustment is recorded`
TC-005 同型（§3 記「陳述調整前之狀態已被記下」）。

**「已被記下」陳述的是測試員之動作，不是系統之可觀察狀態。**
§6 要求 ER 為可觀察、可判定之結果；§5.6 明定記錄步驟「describes what is
read」—— 讀到什麼，不是讀了沒有。

此與 `readable` 同屬一類：**主詞跑到觀察者身上**。前者是「可以被讀」，
後者是「已經被讀」，兩者皆非「顯示了什麼」。

修法：凡 `Note …` / `Record …` 型步驟，其 ER 陳述**該步驟所讀到之物**，
例如 `The lumbar/bolster state before the adjustment is shown`。

**全批複查**（不限 §4 所列者）：掃描所有 ER，凡謂語為
`is recorded` / `is readable` / `is noted` / `can be read` 者一律改寫。

---

## 3. 已簽裁決條文

```
R-C23  自評不得以工具未報為依據

§9 self-check 之每一項，其依據須獨立於 lint 之涵蓋範圍。
「lint 未報此項」不構成該項 PASS 之依據。

某項若無獨立依據可具名，標「未實測」，不標 PASS。

理由：rev1 之 §9 自評四項報 PASS 而實際為 FAIL，同時 lint 25/25 全綠 ——
兩者同時錯且錯在同一處，因為自評複述了 lint 之涵蓋範圍。工具與自評若
共用同一涵蓋範圍，其中一者即不提供任何額外保障。
```

此條由執行層 §6.3 之自我批評導出。**該段自我批評是本包最有價值之產出** ——
它指出的不是一個 defect，而是「為什麼那四個 defect 能同時通過兩道檢查」。

---

## 4. 接受、無須處置者

- **四個新 gate 皆為實際違反而非預防性補強**（14 條全缺 `split_flag`/
  `split_reason`、7 份 reasoning 全超長、TC-004 單步、`duplicate_of` 值
  本身違反 digits-only）—— 四項全中，非湊數
- **`reasoning-sentences` 判準修過一次**（中文 `。` 後不接空白，致七份多句
  reasoning 全報為 1 句）—— 「gate 會失敗」與「gate 失敗的理由正確」是兩件
  事，此區分正確且值得保留於腳本註解
- **`readable` 之複查超出 §4 指名範圍**，自行掃到 TC-007 —— 正確
- **未自行決定 TC-010／TC-012 之處置**（未標 BLOCKED、未刪 leaf、
  未虛構區分）—— 正確；BLOCKED 須經裁定方得使用（profile §5）
- **§10.4 四段順序不加關鍵詞 gate** —— 採納其顧慮：形式檢查會製造新的
  假綠燈。該項維持人工審閱，於 §9 自評中具名其依據（R-C23）

---

## 5. 執行層作業指示

1. R-C23、R-C24 原文貼入 `RULINGS.md`。
2. profile §5 增 `[BLOCKED-SPEC]`，並寫明與 `[BLOCKED-ECU]` 之區別
   （R-C24 條文內已備措辭）。
3. TC-010／TC-012 改為 BLOCKED row（R-C24），移除
   `distinguishing_axis.delegated-only` 與 `split_reason` 內之裁定說明。
4. lint 加 BLOCKED row 之**具名豁免回報行**；反向驗證其於非 BLOCKED row
   單步時仍會 FAIL。
5. 依 §2 全批複查並改寫 ER；掃描四種謂語，回報改了幾條、哪幾條。
6. Core N0／CFTS044 之涵蓋問題登 `DATA_REQUESTS`（RD-1 候選，不阻塞）。
7. 全批重跑 lint 與 §9 自評（依 R-C23，每項具名獨立依據）；僅回報變動項。
8. **仍不寫回 workbook。**
9. 上繳 `docs/upstream/13_pilot_rev3.md`。git 不執行。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C23 自評不得以工具未報為依據 | ✅ §3 | 已簽 2026-08-15 |
| R-C24 外部 spec 全權委派之 leaf | ✅ §1.3 | 已簽 2026-08-15 |

兩條皆須貼入 `RULINGS.md`。R-C23 適用全 feature；R-C24 之 marker 為
Comfort 專屬（profile §5），其原則適用全 feature，安置位置待 canon re-sync。
