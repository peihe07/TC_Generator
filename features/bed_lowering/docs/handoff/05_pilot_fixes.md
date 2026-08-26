# 下放包 05 — Bed Lowering Mode：pilot 修正指令（R-BLM12）

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–04，取 05
對象：執行層（Tier 1）
依據：R-BLM12（全文在 `RULINGS.md`，本包為其執行展開）。
下放包 03／04 之其餘條款繼續有效。停點不變：修訂完成後停在
`batches/pilot/`，**仍不寫回工作簿**。

---

## 一、A 類 —— 逐條機械修正

### A1 `Observe` 主動詞改寫（IN §5.1）

受影響步驟（逐條列，執行層改後回報 diff）：

| TC | 步 | 現行 → 改為 |
|---|---|---|
| 011-03 | P3 | `Observe the EVIC area ... and check that it displays "..."` → `Check that the EVIC area of the instrument cluster displays "..."` |
| 011-04 | P4 | 同型改寫 → `Check that the EVIC message contains the wording "..."` |
| 037-03 | P1 | `Press "Bed Lowering" ... and observe the button, then record whether its highlight is shown` → `Press "Bed Lowering" on the HU Controls tab, check that the button highlight is shown and record it` |
| 037-03 | P3 | `Observe the "Bed Lowering" button and check that ...` → `Check that the "Bed Lowering" button highlight is no longer shown` |
| 037-04 | P1, P3 | 同型：P1 → `... check that the button highlight is shown`；P3 → `Check that the button highlight is removed on the fault relay alone, with no further input given` |
| 037-05 | P1, P3 | 同型改寫 |
| 038-01 | P1 | `Observe the EVIC area and check that no Bed Lowering message is displayed` → `Check that no Bed Lowering message is displayed in the EVIC area` |
| 038-01 | P4 | 同 011-03 P3 型 |
| 038-02 | P3 | → `Check that the unsuccessful message is displayed on the EVIC and that no equivalent message is displayed on the HU screen` |
| 038-03 | P4 | 同 011-04 P4 型 |

改寫後逐條複核 §5.2 長度分級（Final Step ≤ 18 words）；超長者拆
動作與檢查為兩步並保持 ER 1:1。**上表之改寫文字為指令非枚舉上限**：
凡 `Observe`／`observe` 作主動詞者一律改，含表列遺漏者。

### A2 011-02 訊號驗名

`$ASCM_FD_1.RL_Lvl$`／`$RR_Lvl$` 回 DBC 逐字驗名：
- 驗有 → 兩訊號補入 manifest 預查清單（含 VAL_ 若有），TC 不動此部分
- 查無 → 不得近似代入（R-13／§8.7.5(g)）；本條 011-02 同時在 B 類
  改錨範圍內，改錨方案可能使該兩訊號整個退場——先驗名再改錨，
  改錨後不再引用者於 manifest 記「已退場」而非「查有」

### A3 038-04 `design_method` → `Fault Injection`

### A4 Pre-Condition 車型限定

13 條之 `The vehicle is a DT model equipped with the air suspension system`
→ `The vehicle is equipped with the air suspension system`。

---

## 二、B 類 —— 迴路驗證改錨（011-01、011-02、037-01、037-02）

1. **先查**：DBC／LID 找 HU→ASCM 方向之 BLM 請求訊號。線索：LID 之
   `GW_C_I_11`（上繳 04 §二-3 曾命中，pre-FD 名，回 DBC 定位實名）。
   逐字回報：訊息名、訊號名、VAL_ 列舉、發送方
2. **改錨原則**：每條之 Final Step 檢查對象必須是 DUT 輸出
   （HU 發出之匯流排訊號、或 HU/EVIC/cluster 上非 sibling 持有之
   顯示狀態）。自身注入之 ASCM 訊號只得作為 stimulus 與其 ER 之
   `is registered without a bus error` 確認，不得作最終驗證對象
3. **sibling 邊界**（R-BLM12 B 類原文）：EVIC 訊息文字屬 011-03／038-01，
   highlight 屬 037-03。改錨不得取用
4. **個案停**:某 leaf 查到底無獨立 DUT 可觀察物 → 該 leaf 停下回報
   （leaf 號 + 已查路徑 + 查無範圍），其餘照修不連坐
5. 改錨後 reasoning 同步改寫（§10.4 第 3 句：為什麼這樣錨）

## 三、C 類 —— 兩個落點

- 038-04 之 Pre-Condition 5 或 Procedure 加一句文字基準註記：
  比對基準為 SYS1 正規化文字（NRL-193702），reference figure 僅供
  版面（casing／斷行）
- 其餘（近重複保留、角度不登 DR、hyphen）**不動作**，已由 R-BLM12 確認

## 四、修訂後義務

1. 全批重跑機檢 + 括號下半語言檢，回報
2. manifest 重 stamp（R-G19 逐源指紋；上繳 04 已示範過改 yaml 連帶
   變 sha 之歸因，這次改的是 tcs json，同理逐源列）
3. 修訂 diff 逐 TC 列（改了哪步、為什麼、引 R-BLM12 條款號）
4. **停點**：修訂版落 `batches/pilot/`，不寫回。上繳包 05 交審

## 五、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 已登記，未送出 |
