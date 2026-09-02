# 下放包 06 — vsm_v42：pilot b1 修訂輪（R-VL21 REV-1／2／4）

日期：2026-09-02
取號：`docs/handoff/` 實測有 00–05，取 06
對象：執行層。00–05 包續有效。台帳不重生；DR 不送；仍不寫工作簿。
覆核結論：四 §K 處置全對、兩自修核可、二裁題皆准（R-VL21(a)(b)）；修訂限十條，其餘七條**逐字不動**。

---

## 一、修訂清單（就地改 generated/b1_epb/ 之 md＋json，逐列 diff 上繳）

**-046（R-VL21(d)(e)）**：
1. 先查規格節（`data/pilot_epb_spec.md`）有無「等候 IPC 回應期間 Initializing popup 持續顯示」之逐字依據：有 → 步驟 4 改「等待期間檢查 popup 持續」之可觀察式；無 → 刪步驟 4 與 ER 4，reasoning 補「T_EPB_MM 到期效果由 -053 驗（§8.2.1 委任）」。
2. 補 ER：setting status 顯示 On（UI 觀察，元件名依 R-VL21(a) 註來源）；對應 Procedure 步（讀設定狀態）。
3. 刪 ER1（bus error 式）；「is received」式保留。Procedure↔ER 重排後仍 1:1。
4. reasoning 補方向註記一句（037 文字之 receives 與 DBC 方向）。

**Fdbk 族九條 -048〜-052、-054〜-057（R-VL21(f)）**：
1. Procedure 前置發起步：進入側（-048〜-052）`Select "EPB Maintenance Mode" = "On"`（-050/-051 若規格載確認 popup 之 Yes，則含 `Press "Yes" in the popup`，逐字有據才寫）；退出側（-054〜-057）同理 `= "Off"`。
2. 發起步之 ER 依規格可觀察現象寫（如請求訊號送出或 popup 出現），逐字有據；無據則發起步 ER 寫請求訊號 `is received` 式（v3 解得之 `EPB_MaintenanceMode_Req`）。
3. 回讀步（`Read … check it is <raw>`）依 R-VL21(f) 末句：削去或保留皆可，全族**一致**（擇一，INDEX 記選擇）。
4. 括號下半、priority、design_method 不動。

**七條不動**：-044、-045、-047、-053、-058、-059、-060（逐字 diff = 0 為 E 判準）。

## 二、預期數字

| # | 項 | 判準 |
|---|---|---|
| E46 | 修訂檔數 | 10（md）＋10（json）；其餘 14 檔 diff = 0 |
| E47 | E38–E45 重跑 | 全過（E39 括號下半不得因修訂而同文化） |
| E48 | -046 之 ER 涵蓋 | test_item 上半三結果（status On／popup／訊號）全數有對應 ER；timer 依 1 之分支處置 |
| E49 | Fdbk 九條 | 各含發起步且位於送 Fdbk 之前；Procedure↔ER 1:1 |
| E50 | 「registered without a bus error」出現處 | 僅限測試員送出之訊號步（Fdbk 送出步可用；DUT 送出步 0） |

## 三、上繳要求（`docs/upstream/06_pilot_rev.md`）

逐條 diff；E46–E50；1 之分支查證結果（逐字引段）；§9 機讀重跑；獨立判斷；gate_all 歸因。

## 四、升級條件

E46 之不動 14 檔任一 diff ≠ 0；發起步需臆造 popup 文字方能寫（回報列 §K，不造）。

## 五、之後

上繳過 → 分析層終驗 → 交 Pei 授權寫回工作簿（寫回工法屆時另包：含 x14 DV 保全查證）→ 續批 b2（R-VL17 批次序另裁）。
