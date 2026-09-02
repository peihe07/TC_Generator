# 下放包 13 — vsm_v43：b2-2 生成 —— Side Distance Warning（10 leaf，R-VT26(e)）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–12，取 13
台帳不重生；DR 不代發；不寫工作簿；已凍 b1／b2-1 不動。

## 一、契約

全同 12 包（含 〇′ 已辦者免）：Sys-RA 實名 D 欄、Provisional Remarks、雙錨（**前綴逐字用 R-VT26(b) canonical 串**）、E56 型逐字全等、詞界比對、bus-error 限測試員送出步、內部訊號逐一實測 UI 面不沿用前批結論（R-VT20(d)）。

## 二、本批

1. 母體：v2 之 `test_set = Side Distance Warning` 且 `status = active`，**10 列**（chapter .05，spec_section `1.11.1.1.5`，含解得 8）。
2. 規格節切出；注意本組含 `IPC_VEHICLE_SETUP.Sdw` 與 `.SdwChimeVolume` 兩個收訊面（兩列分開，勿併，§8.2.1）。
3. 內部 `Sdw_Setting.Req` 等之 UI 面逐一實測（HMI Settings List `Side Distance Warning` 列上繳 05 曾證 r315B TR=VF230/665，可為錨）。
4. 輸出 `generated/b2_sdw/`；E 同 12 包（10/10）。

## 三、順做（R-VT26(c)，K-17）

K-14 比對鍵加去重音＋空白正規化重試 `.02`／`.10`／`.11`／`.15`／`.16`／`.17`；命中補 `spec_section`（`spec_section_source = k14_param_match_norm`）；仍 none 者列出（E88）。

## 四、上繳（`docs/upstream/13_b2_sdw.md`）

同 12 包結構；E 逐項＋E88；§K；獨立判斷；gate_all 歸因。**綠色通道計數第二批。**
