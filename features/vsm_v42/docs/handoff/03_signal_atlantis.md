# 下放包 03 — vsm_v42：R-VL12／R-VL13 落地，W-5 以 Atlantis 欄組重跑，P3 前置

日期：2026-09-01
取號：`docs/handoff/` 實測有 00–02，取 03
對象：執行層。00–02 包續有效；本包只載差異。sha8 報 body_sha8。台帳不重生（R-VL13(a)，**Pei 已追認**）。

> ## 補遺（2026-09-02，R-VL14 —— 本補遺優先於下文衝突處）
> Pei 已放件 ATL-Mi DBC：`forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`（分析層驗收：BO_ 139／SG_ 5568／VAL_ 619，爭議訊息全在）。
> W-5′ 第 4 項改：段 3 對本件實查（latin-1 讀，CRLF），**「解得」合法**（R-VL14(d)）；Atlantis High R1 DBC 降旁證併記。
> LID Atlantis 欄 `CAN` 為 CAN-C 而本件查無者記「未解得（CAN-C DBC 未到件）」（R-VL14(c)）。
> §五 E27 作廢，改：`解得` 為觀測值；新增 E27′：每一「解得」列須備註段 3 命中之 BO_／SG_ 實名與 VAL_ 有無。
> §七之「E27 ≥ 1 即停」同步作廢。DR 送出事項全數改為「Pei 裁先不送」，§四 1／3／4 中之 DR 部分作廢。

---

## 一、上繳 02 之覆核

| 項 | 判 |
|---|---|
| W-0～W-6 全完成；E1–E25 全相符；副本 x14 DV 完整、未 save；模板三錯值不採（`Z` 為車型欄 Fastback） | **核實**。Z 欄那句是本包最值錢的一行 |
| A-VL8：段 1 幾近全不命中、`637MCA` 0、32 名只靠段 3 | **根因在分析層**（A-VL10）：三包令你只看 `Atlantis High` 欄組，從未令看 LID r2 欄組表頭。實測 LID `CAN Mapping` 有獨立 **`Atlantis`（P–T）** 欄組，本線 ATL-Mi 屬之；forms/ DBC 為 Atlantis High 之件 → **R-VL12**，DR-VL3 |
| 「解得 35」拆分（3 三段皆過／32 段 3 逐字） | R-VL12(c) 裁「段 1 不適用」之原則；但因 DBC 家族不對，35 與 27 全數待重判 |
| 一次自我撤回（子字串比對致 68 筆假 B-1） | 對，R-P368(b) 明禁語意跳接；記入 W-5 之守門 |
| 抽名範圍只認 `_VEHICLE_SETUP` 家族 | → R-VL12(d) 通式 |
| 圖之流向未文字化（A-VL9） | → R-VL12(e) P4 逐 TC 依圖判，RESOLVED |
| A-VL5／6／7 併一 DR | 併 → **DR-VL2** |
| 台帳兩線並行必被追平 | → **R-VL13(a)**：執行層不重生，Pei 提交前跑一次；待 Pei 追認 |
| R-VL5 投遞區 | → R-VL13(b)：inputs/ 為實然，`_intake/` 廢 |
| `\xa0` 測法 | 揭露即可，不改判 |
| `recon.py` DECISIONS 裸 `§4` | 併共用腳本一裁第 6 項 |

## 二、裁決引用

R-VL12／R-VL13 全文在 `RULINGS.md`；DR-VL2／DR-VL3 在 `DATA_REQUESTS.md`。新引 R-P369(b)（拼法不一二名皆入）。

## 三、作業清單

**W-5′ 訊號解析重跑（R-VL12）** —— 在現有 251 名基礎上
1. 抽名補跑 R-VL12(d) 通式；新增名併入；報偽陽性率（人工抽 20 名判）。
2. 段 1：LID `CAN Mapping` **改以 `Atlantis` 欄組（P–T：Signal Name P、CAN Q）為主**，`Atlantis High`（Z–AD）併記旁證；三欄（`Logical Identifier`／`Function`／`Object Text`）逐字＋四規則擴充（去 `MESSAGE.` 前綴、去 `_Req`／`_Sts`／`_Info` 後綴、底線↔空白、大小寫）；LID 其他分頁（含 `637MCA Specific Signals`）同法；HMI Settings List（設定名在 B／C 欄，vsm_v43 上繳 03 §二-2 已實測表頭）與 PROXI `Format` F 欄加第五規則（去 `_Menu`／`_Setting`）。命中記 `檔/分頁/r{列}c{欄}/欄名/規則`。
3. 段 2：Atlantis 欄之 `MESSAGE.Signal` 為主值，Atlantis High 之值併記；兩者不同者記「架構差異」（非 B-1）。
4. 段 3：對 forms/ Atlantis High DBC 實查**只作旁證**；結果欄一律 `段3待ATL-Mi DBC`（R-VL12(b)），不得記「解得」。規格原名已為 `MESSAGE.Signal` 形者備註「段 1 不適用（R-VL12(c)）」。
5. 結果值域：`段3待ATL-Mi DBC | 未解得(止於段1) | 未解得(止於段2) | 訊息名不符(R-13) | B-1 衝突 | UI路徑(R-P375b) | PROXI路徑(R-P375b/c) | UI+PROXI 雙路徑 | 查無(R-G13)`。
6. 輸出 `data/signal_chain_v42_v2.tsv`，v1 不覆寫；同母體（251）對 v1 分布差；Atlantis vs Atlantis High 命中數並列。
7. `VehicleSpeedVSOSig` 類兩弧（若本線亦有）依 R-VT12(a) 同法各自解析，不互為旁證。

**W-7 A-VL5／6／7 處置落地**：leaves.tsv 之 `-051` 標 UNCATEGORIZED（不入母體不排除）、`-063` 入母體並 Remarks 註 DR-VL2(c)；A-VL5／6／7 狀態改「併 DR-VL2」。A-VL9 轉 RESOLVED。

**P3 前置（不鎖）**：以 leaves.tsv 之 `Requirement Title` 24 家族重列 00 包 §九 Layer 2 草案之 leaf 數（實測取代草案數）；列出各家族之 037 `Sub Categorization` 與 SYSRA `Chapter for VF` 前二階，供 Layer 3 對映。

## 四、待 Pei

1. **DR-VL3：手上有無 ATL-Mi（P637／CAN-B／CAN-C）DBC？** 有 → 投 `forms/`，我落綁定條文；無 → 送出（與 V43 DR-VT5 同件）。**這件阻塞兩線 P4。**
2. **R-VL13(a) 追認**：台帳重生歸你提交前一次。
3. **`_intake/Vehicle_Setup_VF665/` 空目錄刪除**。
4. 共用腳本一裁（六項）；DR-VL1／VL2 送出。

## 五、預期數字

| # | 項 | 判準 |
|---|---|---|
| E18″ | R-VL1–R-VL11 body_sha8 | 與上繳 02 逐字相同 |
| E26 | 段 1 Atlantis 欄逐字命中數 ≥ Atlantis High 欄逐字命中數 | 性質（vsm_v43 實測 21 ≥ 10） |
| E27 | 結果 `解得` | **0**（DBC 未到；≥1 即違 R-VL12(b)，停） |
| E28 | B-1 衝突 | 0 |
| E29 | 抽名偽陽性率（人工抽 20） | 觀測值 |
| E30 | `未解得(止於段1)` 同母體（251）對 v1 | 觀測差值 |

## 六、上繳要求（`docs/upstream/03_signal_atlantis.md`）

W-5′ 七項；Atlantis vs Atlantis High 逐名對照表（命中處、`MESSAGE.Signal`、CAN 欄值）；同母體分布差；W-7；P3 前置兩表；A／DR 狀態；R-VL12／R-VL13 body_sha8；獨立判斷；gate_all 與歸因（rulings_hash 紅依 R-VL13 記「待 Pei 重生」）。

## 七、升級條件

E27 ≥ 1；E28 ≥ 1；E18″ 任一不同；需第六規則（回報不自創；Unicode 去重音一案見 vsm_v43 A-VT20，本線遇同型即記，待裁）。

## 八、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VL1 | SYSRA 191 列無 037 覆蓋 | no | 未送出 |
| DR-VL2 | 037／SYSRA 標註完整性三面 | no | 未送出 |
| DR-VL3 | ATL-Mi DBC | **yes（P4）** | 先問 Pei 有無 |
