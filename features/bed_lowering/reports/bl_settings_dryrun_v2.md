# BedLowering dry-run **v2** 摘要（VS-SL-02 §2.5）

日期：2026-09-02　**dry-run，未寫回**　明細：`bl_settings_dryrun_v2.tsv`（151 列）
本 feature 不套 `path` 段（入口非 Settings List）。

## §A　實測

| 項 | 數 |
|---|---:|
| 報告列 | **151**（自檢 1 PASS） |
| `PROSE_PRECOND` | 151 |
| `DT_APPLICABILITY` | **23** = DT 專屬 **7** ＋「DT 或 DJ/D2」**16** |
| `DJD2_ONLY`（DJ/D2 專屬，**不掛** `DT_APPLICABILITY`） | **8** |

## §B　提議（151 列一致）

```
PROXI CAN node 27 (ASM/ASCM) = 1 (Present)
PROXI Body_Types = PENDING（待 VS-SL-02 §1 之裁定）
```

`Body_Types` 行懸置之理由：§1 之查證彙總為 **有 1／無 1／未提及 6**，兩造未在同一份文件內取捨。
詳見 `bl_dt_applicability.md`。

> 總控表寫 `[Type 1]`／`[Type 4]`，`_vf230_proxi_values.json` 寫 `Type 1 - D2`／`Type 4 - DJ`，
> **標籤非逐字相同**。本層不猜值，raw 待裁定後綁。

## §C　§1 查證之要點（全文見 `bl_dt_applicability.md`）

- **檔 1 `Appendix_BV`（总控表之原始來源，在磁碟上）**：`FeatureSet list(Gen4_Gen5)` r41
  Atlantis **DT 欄** 條件不含 `Type 7`；PNet **DT 欄** 逐字 `Always false`；
  PNet **D2/DJ 欄** 方為條件式 → **無**
- **檔 7 `037 報告`**：r8–r12 五條 DT 專屬 `shall` 需求（DT 入口、前升、後降、協調動作）→ **有**
- 其餘 6 檔**未提及**
