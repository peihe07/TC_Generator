# FW036 R1L VSM V42 Profile（vsm_v42 — Vehicle Setup Management R1 Low）

適用：`features/vsm_v42/` 全部 TC 生成與 lint。條文全文一律讀
`features/vsm_v42/RULINGS.md`（R-G13 引用制）；本檔只載綁定與差異，無全文者以條號指回。
Canon：`docs/runtime/ASPICE_SWE6_AI_Instruction.md`（IN）＋ `docs/fw036/FEATURE_ONBOARDING.md`（FO）。

## 身分（R-VL1／R-VL3）

- Test Group：`Vehicle Setup Management R1 Low`；TC ID `NR1L-VSM42-{n:03d}`
- 母體：兩份 037 之 Functional leaf 128（R-VL4）；SYSRA 其餘 191 列不入範圍
- framework：`features/vsm_v42/framework.md`（Layer 2 十組，R-VL17 鎖定）
- EE Architecture：**ATL-Mi**（P637 ProMaster）；交付本車型欄 V

## [ADD §8.7.5] 訊號解析與書寫綁定（無 OVERRIDE，書寫格式依 canon v3 (a)–(g)）

1. **不承襲** `FW036_R1L_VehicleSetting_Profile.md` 之 `[OVERRIDE §8.7.5]`（R-VL2(a)）。
2. 併採 PM 之 R-P353／R-P355／R-P368＋R-P375（R-VL2(b)、R-VL6）。
3. **三段鏈之本線綁定**（R-VL12／R-VL14／R-VL15，蓋過 R-P368 之 Atlantis High 綁定）：
   - 段 1：LID v1_78 **`Atlantis` 欄組（P–T）為主**，`Atlantis High`（Z–AD）旁證；
     比對欄 `Logical Identifier`／`Function`／`Object Text` ＋ 目標欄；
     對象檔含 HMI Settings List（設定名在 B／C 欄）與 PROXI `Format`（F 欄）；
     規則 R1–R6（含 Unicode 去重音，命中必註「重音正規化」）；
     儲存格多值切分＋逐字，禁子串；**目標欄 R1 逐字 > 名稱欄 R2–R6**（R-VL15(a)(b)）。
   - 段 3：**`forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`**
     （latin-1、CRLF、行首錨定；SG_ 定義行 844）；Atlantis High R1 DBC 降旁證（R-VL14）。
   - 規格原名已為 `MESSAGE.Signal` 形者段 1 不適用，正確 DBC 逐字即解得（R-VL12(c)）。
4. 「解得」方得寫 `$MESSAGE.Signal$`，`<label>` 逐字取本線 DBC 之 VAL_；
   內部形之解得須有段 1 依據，僅段 3 同名不算（R-VL16(b)）。
5. 未解類之 TC 寫法：`訊息名不符(R-13)`／`規格拼字疑誤`→保留規格原名不加 `$`（R-VL16(a)）；
   內部訊號無對照者 `PENDING: DR-{n} <名>`（R-P355；本線 DR 依 Pei 裁先不送，P4 遭遇即 PENDING）。
6. `input_test_data` 一律 NA，資料內聯（R-VL2(d)）。
7. lint 檢查 P 以 `--profile vsm_v42` 走 v3 判準（R-VL2(c)）。
8. 現行訊號鏈事實表：`data/signal_chain_v42_v3.tsv`（R-VL15(d)；K-1 依 R-VL15(a) 改判後）。

## 其他綁定

- 交付檔名：`…_SWQT_VehicleSetupManagementR1Low_{YYYYMMDD}.xlsx`（R-VL3）
- 工作簿：`sandbox/base/` 之 R-G1 母本副本；欄位映射依 feature.yaml（r9 實測，R-VL8）
- spec_reference 型態：**未裁**（VF 類母件之 IN §10.7 型態，P3 議程；定案前 `spec_reference_template: null`）
- 台帳重生歸 Pei 提交前（R-VL13，Pei 追認）
