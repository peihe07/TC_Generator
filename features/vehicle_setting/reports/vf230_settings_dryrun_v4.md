# VF230 dry-run **v4** 摘要（VS-SL-04）

日期：2026-09-02　明細：`vf230_settings_dryrun_v4.tsv`（457 列）
二次查找明細：`_v4_branch3_resolution.tsv`（105 列）
產生器：`scripts/vs_sl04_resolve.py`＋`scripts/vs_sl04_report.py`
v1／v2／v3 保留不覆寫；沙盒之 v3 稿另存 `sandbox/vssl/vf230_vssl.v3.bak.xlsx`。
**BL／VC 本包不動。**

---

## §A　(3) 分支 105 列之二次查找

| 判 | 列 | 名 | 處置 |
|---|---:|---:|---|
| **R1** 家族閘 | **54** | 18 | 補 `PROXI AUX_Switch_Types = 1 (Type 1)`／`= 2 (Type 2)` |
| **R1b** 解析器補（**本層新增之值**） | **3** | 1 | 補 `PROXI Auto_Power_Folding_Mirrors = 1 (Present)` |
| **R2** FIP 常數 | **16** | 8 | 不加 PROXI、不 PENDING，掛登記旗 |
| **R3** 維持 PENDING | **32** | 11 | 入 DR 第四節 |
| 合計 | **105** | | assert PASS |

### R1（54 列）之證據

总控表 **No.267 `AUX SWITCH Type`** Atlantis 欄逐字：

```
If AUX_Switch_Types is [Type1]),
 return value is 4.
Else if AUX_Switch_Types is [Type2]),
 return value is 6.
Else return value is 0.
```

`_vf230_proxi_values.json` 之 `AUX_Switch_Types` = `{0: Absent, 1: Type 1, 2: Type 2}`。
故 `SWITCH 1–4` 取 `= 1 (Type 1)`（Type1 → 4 個開關），
`SWITCH 5–6` 取 `= 2 (Type 2)`（Type2 → 6 個開關）。
**label 依 proxi_values 逐字（`Type 1` 含空格），非 FIP 文面之 `Type1`**（審閱 §2 R1 之令）。

### R1b —— **本層新增之判，請 Tier 2 追認**

包內只給 R1／R2／R3。惟實測有一類**不屬三者之任一**：
FIP 列存在、條件明確可取值，但 **v3 之條件式解析器抽不出 term**，
致 v3 誤判為「兩來源皆空」。此類若落 R3 將在 DR 中陳述不實（該條件確實存在）。

實例（唯一一名，3 列）：`Auto Fold Mirrors`，总控表 No.147 逐字

```
If "Auto_Power_Folding_Mirrors" is "Present",
   return value is true.
Other return values are false.
```

其形制為**引號式**（`is "Present"`）而非中括號式（`is [Present]`），
`settings_lookup._parse_terms` 只認後者。`proxi_values['Auto_Power_Folding_Mirrors']['1'] = 'Present'`，
故補 `PROXI Auto_Power_Folding_Mirrors = 1 (Present)`。
**證據不足者一律落 R3，未擴用此判**（見 §B 之 `FIP_PARAM_NOT_IN_VALUES`）。

### R2（16 列 / 8 名）

| subcase | 列 | 名 | 逐字 |
|---|---:|---|---|
| `FIP_ALWAYS_OFF` | 13 | `Suspension Default Ride Height`(No.274)、`Phone Repetition`(No.215)、`Ready to Drive Pop-Up`(No.165)、`Rear Guidance Light Status`(No.275)、`Forward Collision Warning Sensitivity`(No.199) | `Always false`／`Always return value is 0`／`Alwatys return value is 0`（No.275 原文如此，缺字） |
| `FIP_ALWAYS_ON` | 3 | `Distance Unit`(No.115)、`Speed Unit`(No.118)、`Consumption Unit`(No.114) | `Always true` |

`FIP_ALWAYS_ON` **為本層依 R2 之理所加之對稱情形**：恆顯示者本無條件可加，
與 `Always false` 同屬「FIP 列存在但為常數」，故同樣不 PENDING、不入 DR。請 Tier 2 追認。

> `Phone Repetition` → No.215 之綁定**來自審閱 §2 R2 之明指**，非該名自身之 `tier2_evidence`。
> **No.215 之 FIP 名為 `Phone Information on Cluster`**，與設定名不同字，於此具名留痕。

---

## §B　R3（32 列 / 11 名）—— 已補入 DR 第四節

| subcase | 列 | 說明 |
|---|---:|---|
| `NO_FIP_ROW` | 22 | HMI 有對應項，**FIP 无對應列** |
| `NEGATED_CONDITION` | 7 | FIP 條件為否定式（`is not [Australia]`／`is NOT [Absent]`），補集無法落單值 |
| `FIP_PARAM_NOT_IN_VALUES` | 3 | No.148 之 `Easy_Entry_Menù` 於 PROXI 值表查無（表內為 `Easy_Entry_Menu`，差一重音） |
| `NO_MATCH_EITHER` | **0** | —— |

**`NO_MATCH_EITHER` 為 0**：R3 之 11 名**全部於 HMI Settings List 有對應**（逐列驗過列號），
僅 FIP 側缺。故 DR 第四節之問法為「名字對得上、但顯示條件沒人寫」，
**與第一節（名字對不上）不同問**，未與之混寫。

---

## §C　v3 → v4

| 項 | v3 | **v4** |
|---|---:|---:|
| 報告列 | 457 | **457** |
| `PROXI_PENDING` | 105 | **32** |
| 分支 (3) | 105 | **32** |
| 新分支 (2b) 家族閘 | — | **54** |
| 新分支 (2c) 解析器補 | — | **3** |
| 新分支 (2d) FIP 常數 | — | **16** |

其餘 352 列逐欄照抄，未動。

## §D　沙盒稿

`sandbox/vssl/vf230_vssl.xlsx` 就地重生：**457 → 438 列**，改動 **1,084** 處，移除 19 列。
v3 稿存 `vf230_vssl.v3.bak.xlsx`。

lint（`vs_sl03_lint.py`，母體改讀 v4 報告）：三本
`test_item` 括號下半 0／尾句號 0／設定項未加雙引號 0，**PASS**；
`Procedure` 與 `Expected Result` 步數不一致 **0** 列。

抽驗 r14（`SWE1-VC-SWITCH5PowerMode-023`）之 Pre-Condition：

```
1. The HU is in the Full-Operation state
2. FD-CAN8 is connected to the bus simulator with signal tracing enabled
3. The Vehicle Settings menu is open
4. PROXI AUX_Switch_Types = 2 (Type 2)
```
