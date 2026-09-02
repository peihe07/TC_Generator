# 下放包 13 — vsm_v42：b2-2 生成 —— Camera Gridlines（10 leaf，R-VL27(f)）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–12，取 13
台帳不重生；DR 不送；不寫工作簿；b1（含寫回產物）／b2-PS 凍結件不動。

## 一、契約

全同 11 包（含全部固定自檢：E56 逐字全等以程式取子字串、hedge／J／K／Q／V／M 預檢、bus-error 方向、詞界比對、發起態入 Procedure、VAL_ 缺值揭露、UI 名註來源）。**D 欄依 R-VL26(b)：SWE-Requirement ID；C 欄概念留空**（生成物之 JSON 不出 C 值）。spec_reference 依 R-VL19：章節號單錨（本組二家族皆有標題節）。

## 二、本批

1. 母體：`leaves.tsv` 之 `test_set = Camera Gridlines` **10 列**（Dynamic Gridlines 4、Surround Camera Gridlines 6；章節 1.11.1.1.31／1.11.1.1.38）。
2. 規格節二節分切（同 05 包 W-1 法）；訊號依 v3＋val_tables；VAL_ 缺值者照 K-1 處置＋waiver 候補清單（`data/lint_p_waivers_b2.tsv` 起檔，遇則記）。
3. 輸出 `generated/b2_camera_gridlines/`；E 同 11 包（E38–E45／E56 10/10）＋E86 型（spec_ref 全章節號、二節各歸各）。

## 三、上繳（`docs/upstream/13_b2_camera.md`）

同 11 包結構；§K 不猜；獨立判斷；gate_all 歸因（R-VL15(c) 他線但書已立，R-VF83 型不再須專節說明，僅一句歸因）。**綠色通道計數第二批。**
