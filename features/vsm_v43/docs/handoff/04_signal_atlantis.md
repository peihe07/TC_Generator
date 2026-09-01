# 下放包 04 — vsm_v43：R-VT13／R-VT14 落地，W-5‴ 以 Atlantis 欄組重跑，P3 前置

日期：2026-09-01
取號：`docs/handoff/` 實測有 00–03，取 04
對象：執行層。00–03 包續有效；本包只載差異。sha8 報 body_sha8；R-VT11–R-VT14 未入台帳前取樹外 `--out`；台帳不重生（R-VT14(c)）。

---

## 一、上繳 03 之覆核

| 項 | 判 |
|---|---|
| W-5″ 三欄／三檔擴充：`未解得(止於段1)` 113→108；HMI 4；PROXI 39；內部訊號 83→83 | **核實**。「內部訊號三次擴充零變動」為結論 → R-VT14(d) DR-VT4 升與 DR-VT1 同級 |
| K-1：SYSAD 非拓撲文件（AOSP 軟體架構），無從定 LTM 匯流排 | 執行層對；**指你去讀 SYSAD 是我的誤判**（A-VT22）。答案在 LID `CAN Mapping` r2 **`Atlantis`（P–T）欄組** —— 我實測：Atlantis 欄 `Speedometer` 列 = `STATUS_CCAN3.VehicleSpeedVSOSig`，無 `BRAKE_FD_2` → **R-VT13(c)** K-1 結案，`STATUS_CCAN3.*` 為 LTM 觀察弧；A-VT16／A-VT19 RESOLVED |
| DR-VT3 之 28 列「訊息名不符」 | **同源**：拿 Atlantis High DBC 解 ATL-Mi 規格。實測 28 列中 Atlantis 欄逐字命中 6（`TELEMATIC_SERVICE_SETUP.*`／`SERVICE_SETUP.*`），Atlantis High 0 → **R-VT13(d)** DR-VT3 重寫暫持；**DR-VT5** ATL-Mi DBC |
| v3「解得 41」 | 全數重判為 `段3待ATL-Mi DBC`（R-VT13(b)），DBC 未到件不得寫 `$…$` |
| A-VT20 第六規則（`ù`） | R-VT13(e)：準，備註記「重音正規化」，列 DR-VT2 佐證 |
| 雙路徑值域 | R-VT14(a) 增 `UI+PROXI 雙路徑` |
| `Technical Reference (CFTS/VF)` 欄含 VF665 先篩 | R-VT14(b) 採 |
| W-8 Polarion 分頁交集 0，為中繼資料 | 核實，結案 |
| `Description` 欄擴充邊際 +1 | 核實；照令做並如實報，正確 |
| 六偽陽性不刪、不重抽 | 對 |

## 二、裁決引用

R-VT13／R-VT14 全文在 `RULINGS.md`；DR-VT3 重寫、DR-VT5 在 `DATA_REQUESTS.md`。

## 三、作業清單

**W-5‴ Atlantis 欄組重跑（R-VT13／R-VT14）** —— 在 v3（230 名）基礎上
1. 抽名：排除 A-VT21 六偽陽性（標記不刪）；不重抽。
2. 段 1 LID `CAN Mapping`：**主取 `Atlantis` 欄組（Signal Name P、CAN Q）**，`Atlantis High`（Z／AA）併記旁證；三欄（`Logical Identifier`／`Function`／`Object Text`）逐字＋五規則（含第六：Unicode 去重音，命中者備註「重音正規化」）。其他分頁同法。
3. HMI Settings List：先以 F 欄 `Technical Reference (CFTS/VF)` 含 `VF665` 篩候選集（報列數），對候選集比；未命中再對全表；命中列 F 值入備註。
4. 段 2：Atlantis 欄之 `MESSAGE.Signal` 為主值；與 Atlantis High 值不同者記「架構差異」（非 B-1，非 R-13）。
5. 段 3：對 forms/ Atlantis High DBC 實查只作旁證；結果一律 `段3待ATL-Mi DBC`；規格原名已為 `MESSAGE.Signal` 形者備註「段 1 不適用」。
6. 結果值域：`段3待ATL-Mi DBC | 未解得(止於段1) | 未解得(止於段2) | 訊息名不符(R-13) | B-1 衝突 | UI路徑(R-P375b) | PROXI路徑(R-P375b/c) | UI+PROXI 雙路徑 | 查無(R-G13)`。原 28 列 R-13：Atlantis 欄命中者改記段 2 主值＋`段3待ATL-Mi DBC`；未命中者維持 R-13。
7. 輸出 `signal_chain_v43_v4.tsv`；同母體（230）對 v3 分布差；Atlantis vs Atlantis High 逐名對照表（命中處、`MESSAGE.Signal`、CAN 欄值）。
8. 兩弧：`STATUS_CCAN3.VehicleSpeedVSOSig` 備註「LTM 觀察弧（R-VT13(c)）」，`BRAKE1.*` 備註「上游弧」。

**W-6**：A-VT16／A-VT19 RESOLVED（R-VT13(c)）；A-VT12 備註改指 R-VT13(d)；A-VT20 RESOLVED（R-VT13(e)）；A-VT21 維持。

**P3 前置**：`RECON.md` §7 更新（欄組綁定、K-1 結案、DBC 待件）。

## 四、待 Pei

1. **DR-VT5／DR-VL3：手上有無 ATL-Mi（P363／P637；CAN-B／CAN-C）DBC？** 有 → 投 `forms/`；無 → 送出。阻塞兩線 P4。
2. **DR-VT1／VT2／VT4 三項併送**（VT3 暫持，重驗後再定）。
3. R-VL13(a) 追認（台帳歸你提交前）；`_intake/` 空目錄刪；共用腳本一裁（六項）。

## 五、預期數字

| # | 項 | 判準 |
|---|---|---|
| E10‴ | R-VT1–R-VT12 body_sha8 | 與上繳 03 逐字相同 |
| E25 | 段 1 Atlantis 欄逐字命中（CAN 形） | ≥ 21（分析層實測下界；< 21 即回報掃描條件差異） |
| E26 | 原 R-13 28 列中 Atlantis 欄命中 | ≥ 6 |
| E27 | 結果 `解得` | **0**（≥1 即停） |
| E28 | B-1 衝突 | 0 |
| E29 | `Technical Reference` 含 VF665 之候選集列數 | 觀測值（0 即回報，並確認 F 欄格式） |
| E30 | 同母體（230）`未解得(止於段1)` 對 v3 | 觀測差值 |

## 六、上繳要求（`docs/upstream/04_signal_atlantis.md`）

W-5‴ 八項；Atlantis vs Atlantis High 逐名對照；v3→v4 同母體分布差；E10‴–E30；A／DR 狀態；R-VT13／R-VT14 body_sha8；獨立判斷；gate_all 與歸因（rulings_hash 紅記「依 R-VL13 待 Pei 重生」）。

## 七、升級條件

E27 ≥ 1；E28 ≥ 1；E10‴ 任一不同；需第七規則（回報不自創）。

## 八、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 建議送出 |
| DR-VT2 | SYSRA DocID／版次／Melco ID／拼法（＋重音三名） | no | 未送出 |
| DR-VT3 | （重寫）待 DR-VT5 重驗 | no | 暫持 |
| DR-VT4 | 內部訊號對照總表 83 名 | **yes** | 建議送出 |
| DR-VT5 | ATL-Mi DBC | **yes（P4）** | 先問 Pei 有無 |
