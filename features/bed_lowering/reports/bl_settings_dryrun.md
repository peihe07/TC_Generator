# BedLowering 設定項 dry-run 摘要（下放包 VS-SL-01 §5）

日期：2026-09-01　性質：**dry-run，未寫回**　明細：`bl_settings_dryrun.tsv`（151 列）
本 feature **不套 §2 任務 1 之 `path` 段**（入口非 Settings List），只套 `proxi`／`coopen` 段。

## §A　實測

| 項 | 數 |
|---|---:|
| 工作簿資料列 | **151**（`output/…_SWQT_BedLowering_20260827.xlsx` r10–r160） |
| 報告列 | **151**（自檢 PASS） |
| `Pre-Condition` 含 `PROXI` 之列 | **0** —— 存在性條件全以散文寫在 Pre-Condition |
| `PROSE_PRECOND` | 151 |
| `BODY_TYPE_CONFLICT` | 151（全掛） |

散文條件之分布（逐行去序號後計數）：

| 散文 | 列數 |
|---|---:|
| `The vehicle is equipped with the air suspension system` | **151** |
| `The vehicle configuration is either DT or DJ/D2` | **16** |
| `The vehicle is a DJ/D2 configuration` | **8** |
| `The vehicle is a DT configuration` | **7** |

## §B　`BODY_TYPE_CONFLICT`（**須 Pei 裁**）

总控表 `FeatureSet(Gen4-5)` **No.36 `Bed Lowering Mode`**，Atlantis（DT）欄逐字為：

```
If "CAN node 27 (ASM/ASCM)" is [Present] and "Body_Types" is ([Type 1] or [Type 4])
, return value is true.
Other return values are false.
```

`Body_Types` 之值表（`data/_vf230_proxi_values.json`）：
`1 = Type 1 - D2`、`4 = Type 4 - DJ`、**`7 = Type 7 - DT`**。

**即：条件不含 Type 7 (DT)。** 依 R-VS{live+3}（架構只取 Atlantis、車型先以 DT 為主），
本 feature 在 DT 上永不顯示，而工作簿有 7 列明寫 `The vehicle is a DT configuration`。

> **HMI Logic and Flow 原文（SR24 1A）之車型適用範圍，本層未查，不斷言。**

選項（下放包 §5 原列，本層不自選）：

- **(a)** BedLowering 例外，以 DJ/D2 為主
- **(b)** 維持 DT，Pre-Condition 寫 `PROXI Body_Types = 4 (Type 4 - DJ)` 並登 anomaly
- **(c)** 向上游確認总控表 No.36 是否漏列 Type 7

## §C　提議（待裁後方可寫回）

151 列一律提議加入 `PROXI CAN node 27 (ASM/ASCM) = 1 (Present)`
（`_vf230_proxi_values.json` 之 `CAN node 27 (ASM/ASCM)` = `{0: Absent, 1: Present}`）。
`Body_Types` 之提議**懸置於 §B 之裁定**。

> **注意**：总控表寫 `[Type 1]`／`[Type 4]`，值表寫 `Type 1 - D2`／`Type 4 - DJ`，
> **標籤非逐字相同**。本層以「不猜值」處理，raw 由裁定確定後再綁。
