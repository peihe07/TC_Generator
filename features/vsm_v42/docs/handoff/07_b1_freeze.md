# 下放包 07 — vsm_v42：b1 微修（R-VL22）與凍結

日期：2026-09-02
取號：`docs/handoff/` 實測有 00–06，取 07
對象：執行層。00–06 包續有效。台帳不重生；DR 不送；不寫工作簿。
本包為終驗前最後一輪內容變更；完成即 b1 凍結（R-VL22(e)）。

## 一、修訂清單

1. **-053**（R-VL22(a)）：步 1 之 ER `registered without a bus error` → `The signal value $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On) is received`。僅此一列。
2. **-054**（R-VL22(c)）：先量測——規格節中 Fdbk = 8 之段及其前後各一句，掃 `entering|exiting|request`（不分大小寫），逐字引段上繳。有詞 → 依詞歸側不改結構；皆無 → 改 in-mode 型：刪發起步（P1 Select "Off"）及其 ER，Pre-Condition 第三項維持 `The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On)`，直接注入 Fdbk = 8；括號下半同步改為 in-mode 語（不與他條同文）；remarks 更新歸類依據。
3. **-046**：design_method → `功能測試 (Functional based ; no specific technique)`（下拉逐字，R-VL22(d)）。
4. **同型全批掃描（R-VL22(a) 末句，本包起固定）**：對全 17 條 grep `registered without a bus error`，凡所在步之訊號為 DUT 送出者列出；預期修後 = 0（測試員送出步不在此列）。

## 二、E

| # | 項 | 判準 |
|---|---|---|
| E53 | 修訂檔數 | -053 必改；-054 依量測；-046 必改；其餘 diff = 0 |
| E54 | 同型掃描：DUT 送出步之 bus-error 式 | 0 |
| E55 | E38–E45 重跑 | 全過 |
| E56 | test_item 逐字全等斷言（R-VT20(e) 制度化，本線首跑：對 037 Description 來源欄） | 17/17 過 |

## 三、上繳（`docs/upstream/07_b1_freeze.md`）

-054 量測逐字證據與歸類；逐列 diff；E53–E56；聲明 b1 凍結（此後任何變更須新裁決）；gate_all 歸因。

## 四、升級條件

E54 ≠ 0；-054 量測後兩可（有詞但語意不明——列 §K 不猜）。
