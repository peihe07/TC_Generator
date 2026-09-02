# FW036 R1L VSM V43 Profile（vsm_v43 — Vehicle Setup Management R1L TBM）

適用：`features/vsm_v43/`。條文全文讀 `features/vsm_v43/RULINGS.md`（R-G13）；本檔只載綁定。
Canon：IN ＋ FO。**本線現況：037 = 0（R-VT4，DR-VT1 依 Pei 裁未送），止於 P0–P3；本 profile 為 P4 預備。**

## 身分（R-VT1／R-VT3）

- Test Group：`Vehicle Setup Management R1L TBM`；TC ID `NR1L-VSM43-{n:03d}`
- 母體：待 037（R-VT4）；SYSRA／規格不得代之
- framework：Layer 1 鎖定；Layer 2 待 037 家族聚合（沿 vsm_v42 §4.1 做法）
- EE Architecture：**ATL-Mi**（P363）

## [ADD §8.7.5] 訊號解析與書寫綁定（無 OVERRIDE，書寫格式依 canon v3 (a)–(g)）

1. 不承襲 VehicleSetting profile 之 `[OVERRIDE §8.7.5]`（R-VT2(a)）；併採 R-P353／R-P355／R-P368＋R-P375（R-VT2(b)、R-VT6）。
2. 三段鏈之本線綁定（R-VT13／R-VT15／R-VT16）：
   - 段 1：LID `Atlantis` 欄組為主、`Atlantis High` 旁證；三欄＋目標欄；對象檔含 HMI Settings List
     （`Technical Reference` 含 `665` 先篩，247 列候選集，R-VT16(b)）與 PROXI `Format`；
     規則 R1–R6（去重音命中必註）；多值切分＋逐字禁子串；目標欄逐字優先（R-VT16(a)）。
   - 段 3：**`forms/P363_BH-CAN [07338]_3A_R2.dbc`**（latin-1、CRLF、行首錨定；SG_ 定義行 688）；
     Atlantis High R1 DBC 旁證（R-VT15）。
   - 兩弧不合併：`STATUS_CCAN3.*` 為 LTM 觀察弧、`BRAKE1.*` 為上游弧（R-VT12(a)／R-VT13(c)）。
3. 「解得」方得寫 `$MESSAGE.Signal$`，`<label>` 取本線 DBC VAL_；解得基線 81（全 CAN 形，R-VT16(e)）；
   內部形須有段 1 依據。
4. 未解類寫法：`訊息名不符(R-13)` 2 名／`規格拼字疑誤` 2 名／`CAN-C DBC 未到件` 6 名 → 保留原名不加 `$`；
   內部訊號 83 名 → `PENDING: DR-VT4 <名>`（DR 未送，P4 起即此；代價已載 DATA_REQUESTS）。
5. `input_test_data` 一律 NA（R-VT2(d)）；lint 檢查 P 以 `--profile vsm_v43` 走 v3（R-VT2(c)）。
6. 現行訊號鏈事實表：`data/signal_chain_v43_v4.tsv` 經 R-VT16(d)(e) 調整後之下一版（v5，P3 包產出）。

## 其他綁定

- 交付檔名：`…_SWQT_VehicleSetupManagementR1LTBM_{YYYYMMDD}.xlsx`（R-VT3）
- 工作簿：`sandbox/base/` 母本副本；欄位映射 r9 實測（R-VT8(b)）
- spec_reference 型態：未裁（與 vsm_v42 同題，一次議）
- 台帳重生歸 Pei 提交前（R-VT14(c)）
