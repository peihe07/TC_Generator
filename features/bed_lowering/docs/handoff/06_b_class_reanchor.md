# 下放包 06 — Bed Lowering Mode：B 類四條改錨（R-BLM13）

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–05，取 06
對象：執行層（Tier 1）
依據：R-BLM13（全文在 `RULINGS.md`）。下放包 03／04／05 其餘條款繼續有效。
停點不變：改錨完成後停在 `batches/pilot/`，不寫回。

---

## 一、四條逐條錨點規格

共同規則：ASCM 注入訊號只作 stimulus，其 ER 止於
`is registered without a bus error`；Final Step 之檢查對象依下表。
reasoning 依 R-BLM13(b) 逐條載委派句（具名持有 leaf 號）。

### 011-01（偵測故障，R-BLM13(a)）

- Final：`Check that a Bed Lowering fault indication appears in the EVIC area`
- ER 對應：`A Bed Lowering fault indication appears in the EVIC area, showing the fault condition is detected`
- **不驗文字**。委派句：verbatim 文字歸 011-03
- 括號下半改為呈現斷言層級（例：`(Fault indication presence only; message wording is owned by 011-03)` 型），與 011-03 之區分 token 因而更實

### 011-02（角度未達成之偵測，R-BLM13(a)）

- 保留 P1 之後角落高度 baseline 與其比較步（拆步後之讀取/比較兩步不動）
- Final：EVIC unsuccessful 指示**出現**（presence，不驗文字）
- `$ASCM_FD_1.RL_Lvl$`／`$RR_Lvl$` 因 baseline 保留而**續用**（A2 已驗有），manifest 維持「查有」

### 037-01（request 時被拒，R-BLM13(c) —— trigger 區分，不動用 (a)）

- trigger：fault **先於**按鍵（`ASCM_SysFail` = 1 在 Press 之前）——此即與 037-03（fault 後於啟動）之區分軸
- Final：`Check that the "Bed Lowering" button highlight is not shown after the press`（不亮／不維持）
- 括號下半載 trigger token（`Pre-existing fault at request time` 型）
- 委派句：mid-cycle 撤除行為歸 037-03

### 037-02（接收故障回饋，R-BLM13(a)）

- trigger 與 037-03 同（fault 後於啟動）
- Final：`Check that the HU reacts to the fault relay: the "Bed Lowering" button highlight state changes`（反應存在）
- **不斷言** highlight 之規定終態（off 之正確性歸 037-03）
- 括號下半載斷言層級 token（`Reaction presence only; specified highlight behavior is owned by 037-03` 型）

## 二、連帶修改

1. 四條之 `ASCM_Stat` 讀取步：作為 stimulus 生效之確認可保留
   （`Read ... and check that it is 10 (SYSFAIL)` 屬注入生效證明），
   但不得再是 Final Step；ER 措辭去掉「showing the fault condition is
   detected」類之結論性子句——結論只在 Final ER 出現一次
2. 四條 reasoning 重寫（§10.4 全四句），第 3 句引 R-BLM13 與所採分支
   （(a) 或 (c)）
3. 括號下半改動後跑 sibling 區分複核：011-01 vs 011-03、037-01 vs
   037-03、037-02 vs 037-03 三對逐字比對，區分 token 可見
4. 長度分級（§5.2）對改動步複核；超限照上繳 05 拆法處理

## 三、修訂後義務

1. 全批機檢 + 括號下半語言檢重跑，回報
2. manifest 重 stamp（R-G19 逐源），`b_class_halted` 四筆改記
   `resolved: R-BLM13`，保留原停下紀錄不刪（R-TM13 加註不刪除）
3. 修訂 diff 逐 TC 列，引 R-BLM13 條款分支
4. **停點**：13 條完整版落 `batches/pilot/`，不寫回。上繳包 06 交審——
   此輪過後即是 pilot 退出審（R-G15，FO 讀法）與工作簿寫回授權，
   由 Pei 裁

## 四、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 已登記，未送出 |
