# 下放包 11 — vsm_v42：b2 生成 —— Park Sense（18 leaf，R-VL25(a)）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–10，取 11
台帳不重生；DR 不送；不寫工作簿。與 10 包（dry-run）可並行；寫回執行包依 R-VL25(b) 待 E80 判。

## 一、契約

生成規約全面沿用 05 包 W-2 契約＋R-VL21〜R-VL23 全部教訓，明列固定自檢：E56 型逐字全等斷言（037 Description 完整原句，摘句以句為單位不剪接）；bus-error 式限測試員送出步、DUT 送出用 is received 式；回饋／狀態型先量測歸類（entry／exit／in-mode 三分，詞證）；VAL_ 缺值寫 `= <raw>` 揭露；UI 名取規格具名註來源；詞界比對；發起態入 Procedure 不入 Pre-Condition。

## 二、V42 b2 專屬

1. 母體：`leaves.tsv` 之 `test_set = Park Sense` **18 列**（三家族：PARK SENSE w/o HC 5、Rear PS Volume 6、Front PS Volume 7）。
2. spec_reference：PARK SENSE 家族 = `…_V42_R6_1.11.1.1.29`；**Rear／Front PS Volume 13 leaf 依 R-VL19(b) 以 `Sys-RA-VF665_V42_VSM-{nnn}` 錨**（規格無章節標題），Remarks 註依據；`-051` 未分類列不入（DR-VL2(a)）。
3. 規格節切出 `1.11.1.1.29` 同 05 包 W-1 法；Volume 二家族之需求文本以 037 Description 為主源（規格無節）。
4. 訊號依 v3＋val_tables；PROXI（`CAN node 24 (PAM)` 型）入 Pre-Condition；內部訊號 UI 路徑或 `PENDING: DR-VL4`。
5. 輸出 `generated/b2_park_sense/`（json＋md＋INDEX），契約同 b1。

## 三、E

E38–E45／E51 型同判準重跑（編號沿用）＋E56（18/18）＋**E86**：Volume 13 leaf 之 D 欄與 spec_reference 全為 Sys-RA 實名、無臆造章節號。覆蓋 18/18。

## 四、上繳（`docs/upstream/11_b2_park_sense.md`）

同 05 包上繳結構；§K 不猜；獨立判斷；gate_all 歸因。**本批為綠色通道計數之第一批（R-VL25(a)：三批零修訂後啟動）。**
