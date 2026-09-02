# framework — Vehicle Setup Management R1L TBM（vsm_v43）

日期：2026-09-02（P3，下放包 05 W-9）
**Layer 1 鎖定；Layer 2 未鎖、且不得預填** —— 037 = 0（R-VT4），DR-VT1 依 Pei 裁未送。
依 IN §4.1.5：Layer 1／2 寫入工作簿（Test Group／Test Set 欄），Layer 3 僅存本檔。

## Layer 1 — Test Group（**鎖定**）

`Vehicle Setup Management R1L TBM`（R-VT3）

工作簿 G 欄逐字取此值；`feature.yaml` 之 `test_group` 已同步（R-VT3）。
交付檔名之 feature 段為 `VehicleSetupManagementR1LTBM`（R-VT3，R-G42 五禁尾綴）。

## Layer 2 — Test Set（**待 037，本節不得填入任何內容**）

**現況：無母體。** 037（SWE1 分析報告）於本線為 **0**：
現有兩份 037 之 `Source Requirement ID` 152/152 皆為 V42，`V43` 字串命中 0（上繳 01 E7 實測）。

依 **R-VT4**，Layer 2 須自 **037 家族**聚合（沿 `vsm_v42` framework §Layer 2 之做法）；
**不得以 SYSRA 或規格代之**（00 包禁區 §零-5）。
DR-VT1 為其唯一解，Pei 現裁先不送 —— 故本節在 037 到齊前保持空白。

> **本節留白是裁決結果，不是待辦遺漏。** 下放包 05 §五 明列
> 「framework Layer 2 被填入任何內容（待 037，不得預填）」為升級條件。

## 附：SYSRA `chapter_for_vf` 分布（**對照用，非 Layer 2 依據**）

自 `data/sysra_v43_functional.tsv` 之分母 295 列（Functional 507 列扣除
`VF655_V43_R3` 171 列與 DocID 空 41 列，DR-VT2）：

| 前二階 | 列數 |
|---|---|
| `01.11` | 223 |
| `01.14` | 67 |
| `01.13` | 5 |
| 合計 | **295** |

第一階恆為 `01`（295/295），無鑑別力。
**此分布僅供 037 到齊後之對照，不得作為 Layer 2 之依據**（R-VT4）。

## Layer 3 — 規格章節號

待 Layer 2 鎖定後回填（回填為量測非裁決，不解鎖 Layer 2）。

## 訊號書寫

依 `docs/runtime/profiles/FW036_R1L_VSM_V43_Profile.md`：
canon IN §8.7.5 v3（無 OVERRIDE）＋ R-P353／R-P355／R-P368／R-P375；
三段鏈之本線綁定見 R-VT13／R-VT15／R-VT16。
現行事實表：`data/signal_chain_v43_v5.tsv`（解得 81，全 CAN 形、全部有 VAL_）。
