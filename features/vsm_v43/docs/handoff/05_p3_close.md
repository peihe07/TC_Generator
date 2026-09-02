# 下放包 05 — vsm_v43：P3 —— R-VT16 落地（v5）、framework Layer 1 鎖、DECISIONS 準備

日期：2026-09-02
取號：`docs/handoff/` 實測有 00–04，取 05
對象：執行層。00–04 包續有效。sha8 報 body_sha8；台帳不重生；DR 一律不送。
本包新落檔（分析層）：`docs/runtime/profiles/FW036_R1L_VSM_V43_Profile.md`（執行層讀可寫不可）。
本線止於 P0–P3（DR-VT1 未送）；本包為 P3 收尾，P4 之前不再有例行包。

---

## 一、R-VT16 落地（v4 → v5）

輸出 `data/signal_chain_v43_v5.tsv`（v4 不覆寫），變動限五類，逐列 diff 上繳：
1. A-VT26 五列 → `未解得(止於段1)`（R-VT16(e)）；「解得」= 81 對測。
2. 拼字兩列 → `未解得（規格拼字疑誤）`（R-VT16(d)）。
3. `PROXI.First` 審其抽名脈絡：偽陽性則併 A-VT21 型標記（排除旗標），否則維持 CAN-C 缺口；CAN-C 真缺口收斂數上繳。
4. A-VT23 四名設排除旗標（R-VT16(c)）；PROXI 報表母體 39。
5. E29 寬讀重跑 HMI 候選集（247 列）比對；新增命中逐列列出（預期少量或 0，觀測值）。

## 二、其餘作業

**W-9 framework.md 落檔**：Layer 1 = `Vehicle Setup Management R1L TBM`（R-VT3）；Layer 2 節寫「待 037（R-VT4／DR-VT1 未送）」；附 SYSRA `chapter_for_vf` 三值分布（223／67／5）為將來對照。模板檔不存在則新建。

**W-10 DECISIONS 準備**：四欄實值（spec_mode D、BLANK、母體 0 待 037、Layer 1 鎖），標「待 Pei 簽」。不代簽。

**W-11 P4 預備表**：`data/val_tables_v43.tsv`（解得 81 列之 VAL_ 逐值）；`data/ba_sendtype_v43.tsv`。

## 三、預期數字

| # | 項 | 判準 |
|---|---|---|
| E32 | v5「解得」 | **81**，全 CAN 形 |
| E33 | v5 B-1／查無(R-G13) | 0／0 |
| E34 | v5 合計 | 230；五類變動列數逐項列 |
| E35 | R-VT13–R-VT16 body_sha8 | 與 RULINGS.md 現檔一致（樹外 --out） |
| E36 | VAL_ 表列數 | 81 |

## 四、上繳要求（`docs/upstream/05_p3_close.md`）

§一 1–5 逐項＋diff；W-9～W-11；E32–E36；A／DR 狀態（A-VT23／A-VT26 之 RESOLVED 落 ANOMALIES）；獨立判斷；gate_all 歸因。

## 五、升級條件

E32 ≠ 81；E33 任一 ≥ 1；framework Layer 2 被填入任何內容（待 037，不得預填）。

## 六、未結 DR（皆 Pei 裁先不送）

DR-VT1（**阻塞 P4**）／DR-VT2／DR-VT3（暫持）／DR-VT4（**阻塞 P4 內部訊號**）。DR-VT5 已結案。
