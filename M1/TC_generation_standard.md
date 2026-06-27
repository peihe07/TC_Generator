# TC 生成標準與覆蓋哲學(內部標準)

> 定位:這份文件定義「**這套系統該怎麼生成測試案例、以什麼為『好』、覆蓋要對齊什麼**」。
> 讀者:Pei 與 Claude(跨 session 參考用的標準 artifact)。
> 最後更新:2026-06-27

---

## 0. 一句話核心

**測項要對齊的是 SPEC 原文,不是衍生出來的需求清單。** 需求是 SPEC 的「拆解結果」,而拆解本身會漏東西——SPEC 裡有些行為根本沒被拆成任何一個需求,但測項仍然要主動去想、去寫。

---

## 1. 黃金標準 = review 校正後的拆解(但前提是 review 可信)

系統的終點是「**生成 TC**」,而生成要趨近的「好」,就是 **review 校正後的結果**。但這有個前提:**review 本身要可信**。

2026-06-27 這次,我們在一份「已完成(done)」的 Player 檔上,發現 review 工具的原始輸出 **~85% 是假警報**,來自 8 個量測缺陷(見附錄 A)。修正後,first_pass_rate 從「0%」一路被還原到「51%」——**沒有改過任何一條 TC**。

> 教訓:**用 review 結果當生成標準之前,先確認 review 沒有在說謊。** 任何一條規則打到 >80% 的項目,優先懷疑「規則/基準錯」,而不是「東西全寫壞」。

校正後的可信 baseline(這份 Player 檔的真實品質)見附錄 B。

---

## 2. 兩層覆蓋模型(本標準最重要的部分)

現行 `requirement_coverage` 只量「對 SWE1 需求母體」的覆蓋,會給出**誤導性的 100%**。真正要管的是兩層:

| 層級 | 對齊基準 | 現況 KPI | 問題 |
|---|---|---|---|
| **L1 需求覆蓋** | 94 個 SWE1 需求 | `requirement_coverage` 100% | 看不到「需求本身漏掉的 SPEC 行為」 |
| **L2 SPEC 覆蓋** ★ | SPEC 原文(PC 規則等) | **尚未建立** | 這才是真正的覆蓋前沿 |

### 2.1 實測:L1 的 100% 其實只是 SPEC 的 78%

對 Player 的 Media HMI 原文(`Media HMI Logic and Flow ... .pdf`)做初版自動比對:

```
SPEC PC 規則總數:        55 條
被任一需求涵蓋:          43/55 = 78%   ← 12 條 SPEC 行為沒被拆成需求
被任一 TC 涵蓋:          ~44%(候選)   ← 需語意驗證
```

> ⚠️ 這 78%/44% 是 token-Jaccard 初版估計(門檻 0.12),與我們修過的其他 KPI 一樣**需要語意驗證**才能定論——部分「未覆蓋」可能只是措辭不同而實際有覆蓋(同孿生需求低估問題)。但**「SPEC 才是真正覆蓋基準、L1 的 100% ≠ 測全了 SPEC」這個結論是穩的。**

### 2.2 具體案例:被漏掉的 SPEC 行為(候選)

自動比對標出「SPEC 有、沒對到任何需求」的 PC 行為,包含:

- `PC4) Repeat has 3 states: 1) Off 2) Repeat Song 3) Repeat All` — **SPEC 明寫 3 態含 Off**,但需求/domain pack 寫「只有 All/Song 兩態」。(USB vs BTSA 的 Repeat Off 待細查;BTSA 側 PLA-033/034 確有 Off/Unavailable,USB 側被簡化掉)
- `PC5.2.1 / PC5.2.2` — Shuffle 清單的延遲生效、到底不重洗
- `PC6.x` — 進度條/時間格式 HH:MM:SS、'<n> Songs Found' 顯示、進度條移除條件
- `PC2.2.x` — 長按 FF/Rewind 放開後的續播、到頭停止行為

這些是「**生成 TC 時要主動考慮、即使沒有對應需求**」的行為。

---

## 3. 生成要逼近「好拆解」的機制(從這次學到的)

| 機制 | 作用 | 狀態 |
|---|---|---|
| **Domain Pack(審一次)** | 提供 domain 接地,解決「background 不夠→拆解淺」 | 已有(Player/Dealer)|
| **SPEC-driven 深拆** | 拆解時讀 SPEC 原文(PC 規則),不只讀需求句 | **待強化(本標準新增)** |
| **§6.3 列舉矩陣** | 模式 × 來源 × 狀態 系統性補齊(Repeat/Shuffle/Source…) | review 已能抓缺口 |
| **reality-gap 對 SPEC** | expected_result 對 SPEC 實際行為,不臆測未定義行為 | review §7.6 已有 |
| **跨文件引用解析** | 需求若「Refer to CFTSxxx」,要把被引文件行為納入(如 PLA-052→DEAL-026/028/030) | 已示範,待自動化 |
| **Tier 1 錨在需求/SPEC** | 不要求 TC 自帶 shall 句;需求用 will/陳述句也算 | 已修(§6.6)|

---

## 4. 具體待辦(讓生成趨近標準)

1. **建 L2 SPEC 覆蓋分析**:把 SPEC PC 規則 ↔ 需求 ↔ TC 做三層對照,標出「SPEC-only(沒對應需求)」與「未測」的行為清單。這是生成時要額外覆蓋的來源。(初版腳本已能跑,需語意驗證層)
2. **查 Repeat Off**:確認 USB 側到底有沒有 Repeat Off 態(SPEC PC4 說有、需求說沒有)。若有,domain pack + 測項都要補。
3. **生成端讀 SPEC 切片**:Stage 3 深拆時,除了需求 + domain pack,再餵該需求對應的 SPEC PC 原文,讓拆解能涵蓋「需求沒寫但 SPEC 有」的分支。
4. **把 L2 SPEC 覆蓋做成 KPI**:與 L1 並列,Gate 同時看兩層。

---

## 附錄 A:這次修掉的 8 個量測假象(為何舊結果不可信)

| # | 假象 | 修正前→後 | 根因 |
|---|---|---|---|
| 1 | §8.5.2 Design Method 缺漏 | 199→0 | parser 讀錯欄(off-by-one)|
| 2 | §8.3.5 Final Step 無檢查 | 152→5 | regex 漏認 Check/Verify |
| 3 | §8.1.1 Test Item 過長 | 137→8 | 門檻不合「需求句即測項」寫法 |
| 4 | §8.4.1 模糊用語 | 69→2 | EN 漏了 ZH 已有的 connected-successfully 豁免 |
| 5 | requirement_coverage | 73%→100% | 孿生/父子需求低估 |
| 6 | Repeat All softkey OFF | 已修正為 ON | domain pack 內容(HMI 優先於 CFTS)|
| 7 | §7.6 Demo Video 無法佐證 | 已補跨文件知識 | Player domain pack 缺 CFTS012 知識 |
| 8 | §6.6 逼 TC 帶 shall 句 | 5→0 | 規則設計錯(該錨在需求)|

## 附錄 B:校正後的可信 baseline(Player CFTS025, gpt-4.1)

```
first_pass_rate          51.0%  (80/157)   ← 唯一未達 80% 門檻
requirement_coverage     100%   (94/94)    PASS(但見 §2:這是 L1,非 SPEC 覆蓋)
traceability_completeness 100%  (157/157)  PASS
field_completeness       100%   (157/157)  PASS
design_method_accuracy   99.4%  (156/157)
reality_gap_rate         16.6%  (26/157)
tier1_critical_req_rate  31.3%  (26/83)    ← 真實的 §6.3 列舉缺口
req_id_mismatch_rate     5.1%   (8/157)
§6.6 無 spec句            0
```

> 真實待改善:`first_pass_rate 51%` 的缺口 = §6.3 列舉缺口 + §7.x 對齊,見 `player_review_worklist.md`。這些 finding 現在可信。
