# 上繳包 11 — Bed Lowering Mode：B3 批（Lowering Operation，33 leaf）

日期：2026-08-27
對應下放包：`features/bed_lowering/docs/handoff/11_b3_lowering_operation.md`
（sha256 `f19b6a406e6ea5dd08e936e47e021f9a8cdbad2b51255c0c4d4aa30ac54e7d0d`）
執行層：Tier 1

**結論：B3 三十三條生成完成，31 條寫回（列 55–85），2 條依 IN §8.4.3 保留。
機檢與交付 lint（全簿 76 列）皆 clean。§〇 B2 收尾已做。
一項須裁：PROXI 之 `Vehicle_Line_Configuration` **有 DT 而無 DJ/D2**（§三）。**

---

## 〇、B2 收尾

A-BLM11 之處置已落地：006-03／006-05／020-03／020-05 四條各加 per-TC 鏡映註，
句型逐條具名對應 leaf、引 §8.2.1 與「不製造差異」之理由。TC 本文未動，未重驗全批。

- `b2_tcs.json` → `c3da51f4f642694ebbeb38e84da552e4948c98f6fd9e2f3bf00d376b59240534`
- `B2/manifest.json` → `e796b5ac036dd8f4a16df85fce721a0c56901aa19c4ab8ffa97e9b0530b22cd1`（加 `resolution`）

---

## 一、範圍

`Lowering Operation`，母號 001／002／003／021／035／040／041，
**33 leaf（HMI 18／Service 15）**，整組取用未手挑。
機器對帳：批內 33 個 req_id 與 context 之 33 leaf **集合完全一致**（assert）。
母號分佈實測 001×4／002×6／003×4／021×5／035×4／040×4／041×6 = 33。

---

## 二、DR-1 命中：2 條，**與估算相符**

021-04（`below XX MPH` 之保持條件）與 021-05（`vehicle speed below XX MPH` 為保持條件）
落 PENDING，不入寫回。影響清單載 021-04/05，**實測亦為 2 條 —— 本批估算與實測相符**
（B2 曾消掉 2 條估算，本批沒有）。

---

## 三、**須裁：PROXI 有 DT 而無 DJ/D2**

### 3.1 實測

`PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁列 466：

```
Parameter Group : Car_Configuration_15
Parameter Name  : Vehicle_Line_Configuration   (byte 105)
值域 33 項，逐項列出：
  0 = Invalid
  51 = 343 (33 Hex)  …  106 = 560 (6A Hex)
  124 = DT (7C hex)          ← 命中
  130 = HDCC (82 Hex)
```

**DT 命中 1 項；DJ 與 D2 零命中。** 另查 `Suspension_Configuration_Front`（6 項）
與 `Suspension_Configuration_Rear`（5 項）之值域，亦無 DJ/D2。

### 3.2 本包之處置

下放包 §二-1 令車型建立「Pre-Condition 狀態句」或「Procedure PROXI 設定步」
**擇一、全批一致**。DJ/D2 既無 PROXI 表示法，**能全批一致者只剩狀態句**，
故 33 條一律以 Pre-Condition 書寫：

```
2. The vehicle is a DT configuration
2. The vehicle is a DJ/D2 configuration
2. The vehicle configuration is either DT or DJ/D2
```

用語取自 037 原文（`DT vehicle configuration`／`DJ/D2 vehicle configuration`），
**未造 DJ/D2 之 PROXI 參數值**（下放包 §二-1 之停止條件）。

### 3.3 待裁

DT 之已驗值 `124` 目前**未被使用**。兩種可能，皆屬 Tier 2：

1. 維持現狀：全批狀態句，一致性優先，DT 之 PROXI 值僅記於 manifest 備查。
2. DT 條改帶 `PROXI Vehicle_Line_Configuration = 124 (DT)`（IN §8.7.5(c) 之形式，
   不加 `$`），DJ/D2 條維持狀態句 —— 但這樣**全批就不一致了**，
   而下放包明文要求一致。

**執行層採 1，因為它是唯一同時滿足「全批一致」與「不造值」的寫法。**
若分析層認為 DT 應帶 PROXI 而一致性可讓步，逕改，本包已備妥該值。

---

## 四、另兩項預查

| 預查 | 結果 |
|---|---|
| **前角落訊號**（DT 前升需前軸）| **查有**：`$ASCM_FD_1$` 帶 `FL_Lvl`／`FR_Lvl`／`RL_Lvl`／`RR_Lvl` 四支（0x52F）。DT 之「前升後降」因而可由四角落前後比較觀察 |
| **air suspension LED 狀態訊號** | **查無**：dbc_fd 323 訊息／2,037 訊號、dbc_b 155／914、LID CAN Mapping 2,629 列，三處皆 0 命中 |

LED 查無之後果：040 群四條依下放包 §二-3 以**實體觀察句**書寫
（`Check that all air-suspension LED indicators are off`），不造訊號。
**這使該四條成為本 feature 首批「非匯流排可判」之 TC** ——
台架須以目視或影像確認。已記入 manifest 與 §七 自陳。

---

## 五、入口紀律與 R-BLM13

- **33 條無一條注入 `$ASCM_*$`**（機器複核：`Send the signal $ASCM_` 命中 0）。
  進入一律 HU 按鍵，ASCM 側訊號僅觀察。
- R-BLM13 用了兩處 (a)：035-01（與 035-02 同 trigger，斷言按壓被登錄而非致動送出）、
  041-05（與 002-03 皆驗「前軸不升」，以 §8.2.1 之範圍界線分——
  002-03 在操作層、041-05 在 ride-height 控制策略層，各自追溯其 leaf）。
- 全批括號下半**相異數 33**，唯一性成立。

---

## 六、機檢與寫回

```
TC 數 33
N 欄相異值數 1  (R-BLM5 預期 1)
priority 分布 {'P1': 25, 'P2': 8}
design_method 分布 {'Functional Based': 16, 'State Transition': 8, 'Negative / Invalid': 4,
                    'Scenario / Use Case': 2, 'Boundary Value Analysis': 1,
                    'Decision Table': 1, 'Equivalence Partitioning': 1}
Input Test Data == NA 之比例 33/33
機檢項全數 PASS
```

§5.2 首跑抓到 **4 條 Final Step 超 18 words**（001-04 22w、021-02 19w、
040-04 19w、041-03 24w），已逐條收斂，ER 保留完整陳述（§5.2 規制對象為 step）。
複核全批 PASS。

寫回：

| 項 | 值 |
|---|---|
| 輸出 | `workbook/bed_lowering_06.xlsx` sha256 `c4bf218b01fc7896ddfe6a67a9e498c8fb4e2ea89fa5bff84b487b72734f7da6` |
| 列 | 55–85（31 條）|
| TC ID | `newR1L-BLM-046` … `newR1L-BLM-076` |
| patched 儲存格 | 434（31 × 14）|
| round-trip | 31 列 × 14 欄，**差異 0** |
| 保全計數 | zip 48／sheet 9／legacy DV 4／**x14 DV 1**／extLst 3 —— 全等 |
| 交付 lint | **全簿 76 列 clean — 0 findings** |

工作簿鏈：`00 → 01 pilot → 02 B1 → 03 清兩欄 → 04 B1 修訂 → 05 B2 → 06 B3`（現行）

累計：**76 列已寫回**（pilot 13 + B1 6 + B2 26 + B3 31），未寫回之 PENDING **7 條**（B1×3、B2×2、B3×2）。生成總數 83 條 = 176 leaf 之 47.2%（分母 176 leaf，R-G8）。

---

## 七、執行層自陳

1. **040 群四條非匯流排可判**（見 §四）。台架須目視／影像確認 LED。
   **這是本 feature 首次出現這種形態**，若台架不具此能力，該四條之
   可執行性須另議 —— 屬 Tier 2。
2. **002-04／002-05 之「posture」判準是我定的**。037 只寫
   「supports spraying out」「supports debris and water draining out」，
   未給角度或高度值。我以「後角落低於記錄值」與「後低於前」作可觀察替代。
   **這是把定性描述轉為可判準則，非規格明載**，請審。
3. **041-01／041-02 之「highest／lowest reported value」**：037 寫
   `Off-Road 2` 與 `Easy Entry Mode`，但 `$ASCM_FD_1.*_Lvl$` 之 VAL_ 只有
   `254 NOT_INIT`／`255 SNA`，其餘為物理值 —— **無列舉可對應該兩個模式名**。
   故以「達到其最高／最低回報值」書寫。若日後查得模式對映表，該兩條可收緊。
4. **completion 仍非模型產出**（第四次記載）。
5. **台架可執行性未驗**（第八次記載）。
6. **003-04 之「只由 ASCM 回報」為推論式斷言**：驗的是「沒有別的模組報 ride-height」，
   而「沒有」在匯流排上難以窮舉。實作上只能就已綁 DBC 之訊號集合判斷。

---

## 八、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行。累計 7 條以 PENDING 承接未寫回（B1×3、B2×2、B3×2）；另各批 `provisional_inputs` 之暫定車速值全數待其結案複驗 |

---

## 九、停點

**已停。** 交分析層複審。**本批為 R-G14 計數第 2 批候選**（B2 已計 1）。
執行層不自評 —— §三之 PROXI 處置是否構成 A 類，由分析層裁。
