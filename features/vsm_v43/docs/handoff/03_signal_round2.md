# 下放包 03 — vsm_v43：R-VT11／R-VT12 落地，W-5″（三欄＋三檔擴充比對），SYSAD 拓撲實測，P3 前置收尾

日期：2026-09-01
取號：`docs/handoff/` 實測有 00–02，取 03
對象：執行層。00 包禁區、01／02 包 W 定義續有效；本包只載差異。本線仍止於 P0–P3。
sha8 一律報 body_sha8；台帳到位前樹外 `--out` 合法（R-VT10(a)）。

---

## 一、上繳 02 之覆核

| 項 | 判 |
|---|---|
| W-5′ 六項；B-1 = 0、§K 空；型態三經 LID r2321 `CAN=FD` 解得；E10′ 8/8 | **核實**。停 1／停 2 解除 |
| `Description` 欄不存在，只比 `Logical Identifier`、不自創 | **對**。→ **R-VT11(a)**：讀作 `Function`／`Object Text`，三欄皆比；PM 線之字面問題由 PM 線自核 |
| HMI Settings List 命中 0 係未施擴充比對（§八-2） | 對 → **R-VT11(b)**：對象檔擴及 HMI Settings List 與 PROXI `Format`，加第五規則（去 `_Menu`／`_Setting`） |
| `.` 分隔變體只量測不採（+1） | 對 → R-VT11(c)：內部訊號走 R-P375／DR-VT4，不放寬正規化 |
| A-VT15 抽取正則誤配 `<w:tc>`（執行層自誤） | 核實；→ R-VT11(d) 斷言 `</?w:` |
| A-VT16 兩弧疑被合併 | 對 → **R-VT12(a)(b)**：兩規格原名各自解析；HU 所在匯流排自 SYSAD 定 |
| A-VT17 E16 一符一不符 | 分析層之誤（A-VT18）→ **R-VT12(c)**：同母體 97 < 102 相符，113 為觀測值 |
| §八-1 建議 DR-VT4 | 採，已登記 `DATA_REQUESTS.md` |
| `查無(R-G13)` 歸零、`LOOKUP_MISSES.md` 未寫 | 對（三要件未滿足） |
| WMF 轉圖、抽樣核對無圖獨有訊號、不施作 R-G28 二欄表 | 核實 |
| SYSAD 三包未讀 | 本包 W-7 補，限拓撲節 |
| 四支存量紅 | 與本線無關，核實 |

## 二、裁決引用

R-VT11／R-VT12 全文在 `RULINGS.md`；DR-VT4 在 `DATA_REQUESTS.md`。

## 三、作業清單

**W-5″ 擴充比對第二輪（R-VT11）** —— 在 v2 基礎上，不重抽名
1. LID：擴充比對對象自 `Logical Identifier` 一欄擴為 `Logical Identifier`／`Function`／`Object Text` 三欄；命中欄名入 `段1擴充命中` 之記法（`LID/{分頁}/r{列}c{欄}/{欄名}/{規則}`）。
2. HMI Settings List R1 SR25：先實測其表頭，定「設定項名」欄（回報欄名與列數）；對該欄施四規則＋第五規則（去 `_Menu`／`_Setting`）。命中者結果記 `UI路徑(R-P375b)`，段 2 記 HMI 設定項全名與路徑欄（若該檔有）。
3. PROXI_HDCC27_R3 `Format`：對參數名欄施同五規則；命中者結果 `PROXI路徑(R-P375b/c)`。
4. 五規則之外不得自創；遇「明顯該命中卻不中」者列表回報（名、最近似之表內值、差異），不擅自判等同。
5. 輸出 `data/signal_chain_v43_v3.tsv`，v2 不覆寫；結果分布以**同母體（230）**對 v2 列差；`未解得(止於段1)` 之類別拆解（內部／CAN／PROXI）重報。
6. `BRAKE1.VehicleSpeedVSOSig`／`STATUS_CCAN3.VehicleSpeedVSOSig` 兩列依 R-VT12(a) 各記「解得」，備註欄刪「旁證」字樣，改註「兩弧，主旁待 W-7」。

**W-7 SYSAD 拓撲實測（R-VT12(b)）** —— 限定範圍
自 `sources/raw/vf665_sysad_sys3/*.docx` 讀 `word/document.xml`（R-VT11(d) 斷言），只找：LTM／HU 之網路節點所在匯流排（BH-CAN／FD-CAN／其他）、BCM 閘道關係、`STATUS_CCAN3`／`BRAKE_FD_2` 或 `VehicleSpeedVSOSig` 之出現段落。回報：命中段落原文（≤ 3 段，各 ≤ 15 words 之摘句）＋ 節號。**不通讀、不摘要全文**。
若 SYSAD 載明 LTM 所在匯流排 → 兩弧之主旁於 v3 備註欄定；未載 → 記「SYSAD 未載」，列 §K 交 Pei（此時才升級）。

**W-8 SYSRA `Polarion`／`_polarion` 分頁計數**（上繳 02 §八-5(c)，三包未做）：列數、與 `Basic Report` 之 ID 交集數；只計數不分析。

**W-6**：A-VT16 於 W-7 後轉 RESOLVED（SYSAD 有載）或維持 PENDING（未載）；A-VT17 轉 RESOLVED（R-VT12(c)）。

## 四、待 Pei（累計，三包未動）

1. **commit** —— vsm_v42 02 包 W-0 前提；台帳缺 R-VL 11 ＋ R-VT 12 = 23 列
2. **共用腳本一裁**（五項；A-VT3／A-VT7／A-VT8／new_feature.py／--refresh-manifest）
3. **DR-VT1／VT2／VT3／VT4 四項併送**

## 五、預期數字

| # | 項 | 判準 |
|---|---|---|
| E10″ | R-VT1–R-VT10 body_sha8 | 與上繳 02 §三逐字相同 |
| E19 | v3 對 v2 同母體（230）：`未解得(止於段1)` | < 113（觀測差值併列） |
| E20 | HMI Settings List 命中 | > 0（觀測值；= 0 則回報第 4 項之「該命中卻不中」表，不得空） |
| E21 | v3 `UI路徑(R-P375b)` | > 0（同上） |
| E22 | B-1 衝突 | 0 |
| E23 | W-7 SYSAD 命中段落 | 1–3 段（0 段 → 記未載，列 §K） |
| E24 | v3 之 `</?w:` 出現數 | 0 |

## 六、上繳要求（`docs/upstream/03_signal_round2.md`）

W-5″ 六項；HMI Settings List 與 PROXI Format 之表頭實測；v2→v3 同母體分布差；「該命中卻不中」表；W-7 段落與節號；W-8 計數；A／DR 狀態；R-VT11／R-VT12 body_sha8；獨立判斷；gate_all 與歸因。

## 七、升級條件

E10″ 任一不同；E22 ≥ 1；需第六條規則方能命中（回報不自創）；SYSAD 未載 LTM 匯流排（列 §K，其餘續行）。

## 八、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 建議送出 |
| DR-VT2 | SYSRA DocID／版次／Melco ID／拼法 | no | 未送出 |
| DR-VT3 | 規格訊息名與 forms/ DBC 不符 28 列 | no | 建議送出 |
| DR-VT4 | 內部訊號驅動／觀察對照總表（83 名） | no（P4 起 yes） | 建議送出 |
