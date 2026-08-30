# 作業 A — 世代錯配之量測（A-ICS93）｜2026-08-30

## §1 dbc 清單重建 —— 【E29 未觸發】確為四支

自 `forms/` 與各 feature `inputs/` 全樹重建（`find -iname "*.dbc"`，排除 `.git`）：

| 代號 | 路徑 | sha256（前 16）| 世代 | 綁定 |
|---|---|---|---|---|
| **A** | `forms/PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f` | **R1** | 未綁（Pei 已裁）|
| **B** | `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` | `9ef1ec9830fc8018` | R4 | 已綁 |
| **C** | `features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd6092925071` | R5 | 已綁 |
| **D** | `forms/PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71` | **R1** | 未綁 |

**無第五支 → E29 未觸發。**

## §2 本線已用訊號之全集 —— **17 個**

自 `generated/b01..b07/*_tcs.json`（`$MESSAGE.Signal$` 式）與 `docs/reports/*.md`
（`SG_ ` 與 `$MESSAGE.Signal$` 式）抽取後去重：

| 訊號 | 出處 |
|---|---|
| `Radio_btn0` | b03、b07、報告 |
| `Radio_btn1` | b04、報告 |
| `Radio_btn2` | b03、b07、報告 |
| `Radio_btn3` | b07 |
| `Radio_btn4` | b01、b02、b06 |
| `Radio_Knob1_DIR`／`Radio_Knob1_VAL` | b07 |
| `Radio_Knob2_DIR` | b04、b05、報告 |
| `Radio_Knob2_VAL` | b04 |
| `RQ_DISP_INTS` | b03、報告 |
| `DCSD_DISP_STAT`／`DCSD_Enter`／`DCSD_Screen_Off`／`DCSD_VOLKNOB_DIR`／`DCSD_VOLKNOB_VAL` | 報告 |
| `TGW_DISP_STATSts`／`PowerSts_Telematic` | 報告 |

## §3 逐訊號跨世代比對（11 個欄位：`BO_` 號／名、發方、起始位元、長度、位元組序、
factor/offset、值域、單位、收方、`VAL_`）

### 3-1 結論先行 —— **位元佈局與值域四支之間無任何差異**

| 比對面 | 結果 |
|---|---|
| **起始位元** | 17／17 **全部相同**（A vs B；C／D 僅載其中 2 個，該 2 個 C＝D）|
| **長度** | 17／17 全部相同 |
| **位元組序、factor／offset、值域、單位** | 17／17 全部相同 |
| **`VAL_` 列舉** | **17／17 逐字相同**（A vs B）|
| **發方（`tx`）／收方（`rx`）** | **17／17 全部不同** |

**即：世代之間唯一的差異在發收方，而發收方之差正是閘道轉發之必然結果。**

### 3-2 差異分類（自列舉長度取得）

| 類 | 實數 | 訊號 |
|---|---|---|
| 四支一致 | **0** | — |
| 僅 R1 與 R4／R5 有差 | **0** | — |
| **僅存於 BHCAN 族（A、B），FDCAN 族（C、D）查無** | **15** | `Radio_btn0~4`、`Radio_Knob1/2_DIR/VAL`、`RQ_DISP_INTS`、`DCSD_*` 五個 |
| **四支皆載，但承載訊息隨匯流排而異** | **2** | `TGW_DISP_STATSts`、`PowerSts_Telematic` |

> **分類名稱之修正**：機械分桶原將 15 個標為「僅存於某世代」，**該標籤會誤導** ——
> 它們同時存在於 A（R1）與 B（R4）二支 **BHCAN**，只是不存在於二支 **FDCAN**。
> 差別在**匯流排族**，不在世代。已於上表改述，具名此更正。

### 3-3 逐訊號詳表

**`BO_ 1050 CLIMATIC_PANEL` 之九個 ICS 訊號**（起始位元／長度 A＝B 逐一相同）：

| 訊號 | 起始位元 | 長度 | A（R1_BHCAN2）發→收 | B（R4_BHCAN）發→收 |
|---|---|---|---|---|
| `Radio_btn0` | 44 | 1 | `SGW`→**`LTM`** | `ICS`→`SGW` |
| `Radio_btn1` | 43 | 1 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |
| `Radio_btn2` | 42 | 1 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |
| `Radio_btn3` | 41 | 1 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |
| `Radio_btn4` | 40 | 1 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |
| `Radio_Knob1_VAL` | 21 | 6 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |
| `Radio_Knob1_DIR` | 23 | 2 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |
| `Radio_Knob2_VAL` | 29 | 6 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |
| `Radio_Knob2_DIR` | 31 | 2 | `SGW`→`ETM,LTM` | `ICS`→`SGW` |

**方向一致可解釋**：B 檔為 `ICS`（面板）發出 → `SGW`；A 檔為 `SGW` 轉發 → `ETM,LTM`（含本 DUT）。
**同一條鏈的上下游兩段，非矛盾。** `Radio_btn0` 於 A 檔收方**僅 `LTM`**（無 `ETM`），
與其餘八個不同 —— **具名，未推定其意義**。

**其餘六個**：

| 訊號 | `BO_` | 起始位元／長度 | A 發→收 | B 發→收 |
|---|---|---|---|---|
| `RQ_DISP_INTS` | `1283 RADIO_B3` | 55／8 | `ETM`→`SGW` | `SGW`→`DCSD` |
| `DCSD_DISP_STAT` | `1445 DIS_CENTERSTACK` | 7／3 | `SGW`→`ETM,LTM` | `DCSD`→`SGW` |
| `DCSD_Enter` | `1445` | 11／1 | `SGW`→`ETM` | `DCSD`→`SGW` |
| `DCSD_Screen_Off` | `1445` | 12／1 | `SGW`→`ETM` | `DCSD`→`SGW` |
| `DCSD_VOLKNOB_DIR` | `1445` | 9／2 | `SGW`→`ETM` | `DCSD`→`SGW` |
| `DCSD_VOLKNOB_VAL` | `1445` | 21／6 | `SGW`→`ETM` | `DCSD`→`SGW` |

**跨匯流排族之二個**：

| 訊號 | A／B（BHCAN）| C／D（FDCAN）|
|---|---|---|
| `TGW_DISP_STATSts` | `BO_ 1500 TELEMATIC_DISPLAY2`，起始 0、長 4 | `BO_ 1427 TELEMATIC_FD_4`，起始 **79**、長 4 |
| `PowerSts_Telematic` | `BO_ 1470 STATUS_TELEMATIC`，起始 12、長 3 | `BO_ 1427 TELEMATIC_FD_4`，起始 **103**、長 3 |

C 與 D 就此二訊號**逐欄相同**。

## §4 對既有 31 條之影響 —— 【E26 觸發】

### 4-1 交付欄 —— **受影響 0 條**

31 條之 `pre_conditions`／`input_test_data`／`test_procedure`／`expected_result` 中，
**無一條斷言任何訊號之發送節點或接收節點**。其寫法一律為
`Read the signal $MESSAGE.Signal$ ... on the CAN trace` 與
`The signal value $MESSAGE.Signal$ = n (Label) is observed on the CAN trace`。

**而位元佈局與 `VAL_` 在四支之間逐一相同**（§3-1）——
故交付欄之訊號名、位元位置、值與標籤**在任一世代上皆成立**，**受影響 0 條**。

### 4-2 但 `reasoning` 受影響 —— **3 條**

`b03` 之三條（`Power hardkey pressed while HU screen on`、
`Power hardkey pressed at Telematic Power full operation`、
`Three second period completed after screen off hardkey`）之 `reasoning` 逐字載：

> `SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" DCSD`，**發送節點為 SGW 而非 ICS**（已具名，見 upstream-04 §三）

該行末之 `DCSD` 為**收方**，與「發送節點為 SGW」二者合起來，
**逐字取自 B 檔（R4_BHCAN）**。而於 Pei 所裁之 **A 檔（BHCAN2）**，
`RQ_DISP_INTS` 為 **`ETM`→`SGW`** —— **發送節點是 ETM（本 DUT 側），不是 SGW；收方是 SGW，不是 DCSD。**

**即：這三條之 `reasoning` 引述了一行 DBC 原文，該行在裁定之匯流排上是另一個樣子。**

### 4-3 【E26】判定與其與下放包設想之差異

E26 之字面：「若判出**任何一條既有 TC 受世代差異影響**，停下回報，不進入作業 B／C」。
**依字面：觸發（3 條）。本作業依令停下，未進入作業 B／C。**

**但須明白區分二事，不令分析層誤讀：**

| | 下放包 §7 所慮 | 實測 |
|---|---|---|
| 位元佈局悄悄不同 | 擔心 | **不成立** —— 17／17 相同 |
| 值域／`VAL_` 悄悄不同 | 擔心 | **不成立** —— 17／17 逐字相同 |
| 交付欄之值填錯而看不出來 | 擔心 | **不成立** —— 受影響 0 條 |
| `reasoning` 引述之 DBC 原行過時 | **未預料** | **成立 —— 3 條** |

**下放包 §7 所述之風險（「回填的卻是錯的值，而且錯得看不出來」）經量測不成立。**
實際觸發 E26 者，是一個**性質不同、且較輕**的問題：三條 TC 的 `reasoning`
引了 R4 檔的原行，該引述在裁定之匯流排上不再正確。

**執行層不自行判斷此差異是否足以放行作業 B／C** —— 依 E26 字面停下，交分析層裁。
**若分析層認為 §4-1 之「交付欄受影響 0 條」已滿足 E26 之立法理由
（「綁定與回填皆以訊號解析正確為前提」，而訊號解析經量測正確），
則作業 B／C 可於下一包直接執行，本包之量測不需重做。**

## §5 下放包未預料之事

1. **§4-2：三條 b03 之 `reasoning` 引述 R4 檔原行，該引述於裁定之匯流排上不正確。**
2. **§3-1：世代之間唯一差異在發收方**，位元佈局與 `VAL_` 完全相同 ——
   十四包建立於 R4／R5 上之訊號解析**就數值面而言全部有效**。
3. **§3-2：15 個訊號之差別在匯流排族（BHCAN vs FDCAN），不在世代。**
   機械分桶之「僅存於某世代」標籤會誤導，已具名更正。
4. **§3-3：`Radio_btn0` 於 A 檔收方僅 `LTM`**（其餘八個為 `ETM,LTM`）。
5. **已綁之 C 檔（R5_FDCAN8）對本線 17 個已用訊號只貢獻 2 個**，
   其餘 15 個全部來自 B 檔（R4_BHCAN）。**世代錯配之實際爭點只在 R1 vs R4 之 BHCAN，
   R5 幾乎不參與。**

## §6 已知局限

- 已用訊號全集自 TC 與報告之字面抽取；若有以其他寫法提及而未被 regex 命中者會漏。
- 未比對四支 dbc 之全檔差異（僅比對 17 個已用訊號）；
  upstream-14 §10-1 所列之「D 檔全檔差異盤點」仍未做。
- `Radio_btn0` 收方僅 `LTM` 之意義未查（可能為 R-ICS39 相關之變體事實，亦可能為登錄疏漏）。
