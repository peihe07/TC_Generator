# W-138 —— PDT24 兩檔之補列準備（48 輪；**未執行複製**）

禁區逐字：「不補素材（PDT24 兩檔之複製屬 Pei）」。本檔只備補列與核對指令。

## 1. 版本核對（R-VS68′）

| 檔 | sha256（本輪就地量得） | 與 R-VS68′ 相符 |
|---|---|---|
| `PDT24_E2A_R3_3_BHCAN2_20260109.dbc` | `877e4cbbb60b87860867e77fe7bcbf8555f4298810224681911b1064ea5a95f4` | ✅ |
| `PDT24_E2A_R8_5_FDCAN8_20260520_CR26320.dbc` | `defc65d0874196401f7d82eb8fa223413ee39af1cfc2a58fbd96922a1faabef5` | ✅ |

## 2. `INPUTS.sha256` 之補列（Part 1，16 → **18** 檔）

> 複製後於 `features/vehicle_setting/inputs/` 執行 `shasum -c INPUTS.sha256` 核對。

```
877e4cbbb60b87860867e77fe7bcbf8555f4298810224681911b1064ea5a95f4  PDT24_E2A_R3_3_BHCAN2_20260109.dbc
defc65d0874196401f7d82eb8fa223413ee39af1cfc2a58fbd96922a1faabef5  PDT24_E2A_R8_5_FDCAN8_20260520_CR26320.dbc
```

**建議之複製指令（屬 Pei）**：

```
cp -p "/Users/peihe/Work_Projects/SQA_AUTO_R1LR_SWE6/cantool/dbc/NOW/PDT24_E2A_R3_3_BHCAN2_20260109.dbc" \
   "features/vehicle_setting/inputs/PDT24_E2A_R3_3_BHCAN2_20260109.dbc"
cp -p "/Users/peihe/Work_Projects/SQA_AUTO_R1LR_SWE6/cantool/dbc/NOW/PDT24_E2A_R8_5_FDCAN8_20260520_CR26320.dbc" \
   "features/vehicle_setting/inputs/PDT24_E2A_R8_5_FDCAN8_20260520_CR26320.dbc"
```

## 3. 71 輪補充證據之重量（R-VS68′ 令以新檔複驗）

> 71 輪之證據段量自 `_melco`／`_melmb` 二檔；R-VS68′ 所取者為**不同檔**。

| 主張（71 輪） | 本輪以新檔重量 | 判 |
|---|---|---|
| 四份 DBC 中 `*_Cmd_Tlm` 皆不存在 | 逐檔 `SG_ *_Cmd_Tlm` 命中：PDT24…0／PDT24…0／PDT27…0／PDT27…0 | ✅ 相符 |
| 四份 DBC 中 `TELEMATIC_VEHICLE_SETUP2` 皆不存在 | 逐檔 `BO_` 命中：PDT24…0／PDT24…0／PDT27…0／PDT27…0 | ✅ 相符 |
| `*_Tlm` 為 1 bit | 逐檔之位元寬集合：PDT24_BHCAN2 [1,2,3]／PDT24_FDCAN8 無／PDT27_BHCAN [1,2,3]／PDT27_FDCAN8 無 | ⚠ **如其字面不成立** |
| 　↳ 逾 1 bit 者為何 | 四檔皆為 `MassageIntensity_D/P_Tlm`（2 bit）與 `MassageType_D/P_Tlm`（3 bit）—— **皆為按摩座椅之訊號，不在本 feature 之範圍** | 具名 |
| 　↳ **五個標的之位元寬** | `FL_HS_Tlm`／`FR_HS_Tlm`／`FL_VS_Tlm`／`FR_VS_Tlm`／`HSW_Tlm` 於 **PDT24 與 PDT27 兩代皆為 1 bit** | ✅ **相符** |

**三項主張之複驗**：一、二相符；**三之字面不成立而其實質相符** ——
「`*_Tlm` 為 1 bit」若讀為**全部** `*_Tlm`，四檔皆有反例（按摩座椅之 2／3 bit）；
若讀為**本 feature 之五個標的**，則兩代 DBC 皆為 1 bit，R-VS67′ 之前提成立。

**本層不擇一讀法**，兩讀並列（升級條件「W-138 之重量結果與 71 輪之補充證據不符」
依字面命中，依實質未命中）。。

**版本核對**：二檔皆與 R-VS68′ 所載相符。