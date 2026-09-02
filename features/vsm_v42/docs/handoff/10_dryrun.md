# 下放包 10 — vsm_v42：三欄交付本實測＋b1 dry-run lint 實跑（R-VL24(b)(c)）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–09，取 10
台帳不重生；DR 不送。**仍不寫 sandbox/b1/、不建 delivered/**；寫入僅限 `sandbox/wb_trial/` 與 `data/`。

## 一、W 清單

**W-1 三欄交付本實測（R-VL24(b)）**：讀 `features/{vehicle_setting,popup,power}/delivered/` 各取最新一本，實測其資料列之 Q（Estimated Test Time）／車型欄群（T–Z 型）／AB（Test Version）實際值分布（相異值×列數，逐本逐欄）；有一致慣例→依慣例定 b1 之填法並更新 `writeback_map_b1.tsv` 對應欄；無→留空並報。逐字引所見值。

**W-2 trial_D dry-run（R-VL24(c)）**：`wb_trial/trial_D_b1.xlsx` = base 複本＋b1 17 條實內容（依 `writeback_map_b1.tsv` 全欄，含 W-1 之三欄結論）＋surgical 出件＋(a) 之強制複驗三斷言＋回讀 17 列逐欄比對 JSON。

**W-3 lint 實跑**：`lint036.py trial_D_b1.xlsx --profile vsm_v42`，輸出全文；**逐紅歸因三分**（工法產物／假設缺陷／b1 內容缺陷——內容缺陷者逐列引出交裁，不自修：b1 已凍，改須新裁決）。P／I-cross／W 三項特別逐項列。

## 二、E

| # | 項 | 判準 |
|---|---|---|
| E78 | W-1 | 三本×三欄之分布表；結論（慣例／留空）逐欄 |
| E79 | trial_D 複驗 | x14 逐字存活；member 48；differing 僅 sheet6；回讀 17×全欄 = JSON |
| E80 | lint | 全文＋逐紅三分歸因；b1 內容缺陷數（0 則直接可請 Pei 授權寫回） |
| E81 | 禁區 | `sandbox/base/` sha 不變；b1 35 檔 cmp 0 |

## 三、上繳（`docs/upstream/10_dryrun.md`）

E78–E81；writeback_map_b1 更新 diff；lint 全文；獨立判斷；gate_all 歸因。**E80 = 0 時本上繳即為「可寫回」之證據包，待 Pei「寫」。**
