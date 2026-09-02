# 下放包 12 — vsm_v42：修訂落地 → b1 寫回執行 → 交付候選（R-VL26）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–11，取 12
台帳不重生；DR 不送。**本包獲准寫入 `sandbox/b1/` 與建立交付候選**（Pei「寫」預授權，R-VL25(b)／R-VL26(h)）；`delivered/` 仍不建（待「出貨」）。

## 一、修訂落地（順序執行）

1. **-057 解凍修一列**：括號下半 → `(Fdbk = 11: exit process reported as complete)`；重跑 E39／E56／hedge 掃描；INDEX 記「-057 amended per R-VL26(a); refrozen」。
2. **b2 錨層修訂**：Volume 13 條 spec_reference 改雙錨（`Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29` 一行在前＋原 Sys-RA 行保留在後）；-006 remarks 追加 `; upstream duplicate suspected (verbatim same as -002 and spec paras 1203-1204 / 1214-1215) — DR-VL2 evidence`。b2 其餘一位元不動；E 判準：修訂僅此 14 檔、E39–E45／E56 重跑全過（**零它項 → 綠色通道計數 1／3 成立**）。
3. **writeback_map_b1.tsv 對調**：D 欄 = `SWE1-VC-EPBMaintenanceMode-{nnn}`、C 欄留空（欄名同步改 `swe_id_D`／`empty_C`）；S 欄 = `NA` 補入映射。
4. **`data/lint_p_waivers_b1.tsv` 新建**：11 個賦值（Fdbk 2–11 九項＋VehicleSpeedVSOSig 64／65）｜依據 `R-VL21(c)/R-VL26(c): DBC has no VAL_ entry for this raw value; disclosed in remarks`。

## 二、b1 寫回執行（R-VL24(a) 工法）

1. `sandbox/base/` → `copy2` → `sandbox/b1/vsm42_b1.xlsx`；openpyxl 計算層依修訂後 map 填 17 列（列 10–26，含 -057 修正內容）→ `surgical_save`。
2. 強制複驗三斷言＋回讀 17 列逐欄比對修訂後 JSON（不符 0 為要件）。
3. lint 實跑 `--profile vsm_v42`：預期 C=0、**P 之紅逐列對 waivers 清單對銷（對銷後淨 0，未對銷上者列出交裁）**、U=6（計數）、I-cross＝基線（R-VL26(d)，全數為「窗未宣告」型）、其餘 0。
4. 交付候選：`sandbox/b1/candidate_vsm42_b1.xlsx` = `copy2` ＋ sha256 相等斷言。

## 三、E

| # | 項 | 判準 |
|---|---|---|
| E89 | 修訂範圍 | -057 2 檔＋b2 14 檔＋map＋waivers；其餘 diff = 0 |
| E90 | b2 重跑 | E39–E45／E56 全過（綠色通道 1/3 要件） |
| E91 | 寫回複驗 | 三斷言＋回讀 0 不符 |
| E92 | lint 淨紅 | C=0；P 對銷後 0；I-cross 全屬基線型；其餘 0（U 除外） |
| E93 | 交付候選 | sha256(candidate) = sha256(b1 出件) |

## 四、上繳（`docs/upstream/12_write_b1.md`）

E89–E93；lint 全文＋對銷表；凍結更新（-057 新 sha8）；候選檔 sha256；獨立判斷；gate_all 歸因。**全過即待 Pei「出貨」；b2-2 = Camera Gridlines 10 leaf 之生成包隨覆核後發。**
