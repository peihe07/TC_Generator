# 29 — R-G19：寫回作業規定全專案化（rev A, 2026-08-25）

依據：Pei 2026-08-25 指示「這裡的寫回規定要套用到全專案」。
「這裡」＝ time_management 之寫回實務全套（R-TM78 dry-run 前置、
R-TM80 `--out` 另檔、W-TM-26 之 surgical_restyle 衍生通道與
「非受令欄零變更」驗收、A-TM30/31 之基準宣告教訓）。
本包為升格之落檔件；條文逐字如下，供謄入
`docs/fw036/RULINGS_LEDGER.md`（分析層已同步謄入，見 §2）。

## §1 條文（逐字）

```text
R-G19（Pei, 2026-08-25）—— 寫回作業規定全專案化

下列規定自即日起適用於全專案所有 feature 之一切工作簿寫回，
不限 time_management（升格來源：R-TM78／R-TM80／W-TM-26 之寫回實務；
Pei 指示原文：「這裡的寫回規定要套用到全專案」）：

1. dry-run 前置：`--write` 前必跑一次不帶 `--write` 之 dry-run，
   其逐列比對結果附於回繳包（R-TM78 升格）。
2. 輸出另檔：寫回指令一律明寫 `--out`，不得覆寫基準檔；
   輸出落於該 feature 之 output/（R-TM80 升格）。
3. 基準宣告：下放包所宣告之基準檔 SHA256 由腳本對「宣告路徑之檔案」
   實測產出，不得手抄、不得以 repo 內同名檔代替宣告路徑之檔；
   基準檔在 repo 外者，先取複本入 inputs/ 再實測
   （A-TM30／A-TM31 之教訓）。
4. 驗收判準：回繳之逐列 diff 須涵蓋全部欄；非受令欄之任何變更
   即退回。identifier 欄（TC ID、Test Group）之變更一律須先經裁定，
   未經裁定之改名視同缺陷登記 anomaly。
5. 樣式變更走衍生通道：不改既有 <xf>（避免連帶重掛共用該 id 之格），
   由現用 xf 衍生新 cellXfs 附於表尾、只重掛指名之格；通道須明示啟用
   （feature.yaml 鍵），未啟用者行為與變更前逐位元相同
   （W-TM-26 T5 之 surgical_restyle 升格）。
6. 容器完整性依 R18-3 常設規則（xlsx_surgical 為唯一寫回路徑；
   zip 成員集合與 classic/x14 DV 計數不等即 ABORT）——
   本項為既有全域規則之重申，非新增。

各 feature 之既有同義條文（R-TM78/80 等）保留為軌跡不刪；
新 feature 不再逐一另立，逕引本條。
```

字元數 882；SHA256 前 16 碼 `fef0cad264e9ddd2`。

## §2 落檔動作

1. `docs/fw036/RULINGS_LEDGER.md` —— 已由分析層追加 R-G19 條目
   （抄錄方式：與本包 §1 同一字串寫入，SHA 相符）。
2. `docs/fw036/RULINGS.sha.tsv` —— 由執行層以既有工具重生
   （該表為腳本產物，分析層不手編）。
3. 各在辦 feature 之 PLAYBOOK 或 profile 加一行「寫回依 R-G19」：
   vehicle_setting、power、power_moding、display、time_management。
   既有 R-TM78/80 條文保留為軌跡。
4. 與 `CANON_DRAFT_r16_delivery_integrity.md`（§6a 容器完整性草案，
   2026-08-13 執行層草擬、待 Pei 簽）之關係：R-G19 第 6 項重申其
   R18-3 核心，但 §6a 草案之其餘內容（probe、缺損既成之處置判準）
   仍待 Pei 另簽，本條不代簽。

## §3 首個適用

time_management（即刻，W-TM-26-A1 起）；其次為 power 之 ⑤寫回站
（Revise2）與 vehicle_setting 之 036 寫回。
