# VF230 設定項查找配方 dry-run **v2** 摘要（下放包 VS-SL-02 §2）

日期：2026-09-02　性質：**dry-run，未寫回**
明細：`vf230_settings_dryrun_v2.tsv`（457 列）　產生器：`scripts/vs_sl02_dryrun_v2.py`
附件：`_v2_branch3.tsv`（(3) 分支之列）、`_v2_path_split.tsv`（§2.3 之分流）
v1 保留於 `vf230_settings_dryrun.{md,tsv}`，供對照。

---

## §A　命中統計（v1 → v2）

| 項 | v1 | **v2** | 說明 |
|---|---:|---:|---|
| 報告列 | 457 | **457** | 自檢 1 PASS |
| **(3) 二來源皆空之列** | 207 | **30** | 包內要求「遠小於 207；若仍 ≥ 100 停下來報」—— **30，未觸及停止條件** |
| `ALIAS_UNRESOLVED` | 281 | **179** | 見下「抽取式補正」 |
| `PROXI_PENDING` | 207 | **30** | 與 (3) 同數 |
| `RAW_MISSING` | 26 | **35** | (1) 分支改為 RAW_MISSING 而非 PENDING，數升屬預期 |
| `path_proposed` 產出 | 66 | **79** | 抽取式補正之效 |
| `control_proposed` 產出 | 66 | **79** | 同上 |
| `setting` 欄為空之列 | 95 | **0** | 見下 |

### 分支分布（§2.1 之四分支）

| 分支 | 列數 |
|---|---:|
| (1) 形制改寫（`proxi_now` 非空） | **152** |
| (2) 依总控表／需求原文 | **96** |
| (3) 二來源皆空 → `PENDING` | **30** |
| (4) 別名未解 → 只掛 `ALIAS_UNRESOLVED` | **179** |
| 合計 | 457 |

(1) 之 152 列即 `proxi_now` 非空之列，與 v1 實測之 152 處 PROXI 相符。
**審閱 §2.1 所指之 55 列（`proxi_now` 有值卻 PENDING）與 165 列（別名未解卻 PENDING）在 v2 皆為 0**，見自檢 2、3。

### 執行層自行補正之抽取式（**非包內所令，本層主動**）

v1 只以 `"X" customer setting` 抽設定項名。實測 **95 列**（含 §2.3 之 92 列）
把名寫成**不加引號**的 `… check that the X setting is displayed …`，被整批漏掉。
v2 加一條 fallback 抽取式後：

- 95 列全數補中，`setting` 欄為空之列由 95 → **0**
- 這 95 列所指之 **87 個名全部已在既有 107 名母體內** —— **母體不變，別名表仍為 107 列**
- 連帶 `ALIAS_UNRESOLVED` 由 227（未補正之 v2）降至 **179**

---

## §B　§2.2　別名

`data/settings_alias.tsv` 已併入 Tier 2 之兩欄（現 7 欄）：
`tc_name`｜`hmi_name`｜`fip_name`｜`match_type`｜`evidence`｜**`tier2_proposal`**｜**`tier2_evidence`**

**未經 Pei 逐條認可前，`manual` 者不綁入查找** —— v2 僅以 `exact` **51** 名跑。

| Tier 2 提議 | 名數 | 涉及列 | 說明 |
|---|---:|---:|---|
| `manual` | 44 | **176** | **若 Pei 認可，將解鎖 176 列**（該 176 列現皆無 `path_proposed`；其中 40 列在 (1) 分支、136 列在 (4) 分支） |
| `DR` | 9 | 37 | 見 `DATA_REQUESTS.md` 之未取號 DR 草稿 |
| `drop` | 1 | 19 | `Traffic Sign Assist Offset - non-NAFTA Setting`，依 R-VS84(4) 移除 |
| 合計 | 54 | 232 | 54 名共涉 232 列（其中 179 列落在 (4) 分支，53 列因 `proxi_now` 非空而落在 (1)） |

---

## §C　§2.3　`PATH_ABSENT` 分流

**結論與包內預期不同：92 列全部「需路徑」，行為型 0 列。**

| 分類 | 列數 |
|---|---:|
| 需路徑 | **92** |
| 行為型（不需路徑） | **0** |

**證據**：92 列之 procedure 形制一致 —— 前 1–2 步為 `Send CAN: <signal> = <raw> (<label>)`，
**末步一律為 `Read the Vehicle Settings menu and check that the <X> setting is displayed as <Y>`**
（92／92 逐列命中）。該末步須導覽至該設定項方能執行，故仍需路徑。

例（r14，`SWE1-VC-SWITCH5PowerMode-023`）：

```
1. Send CAN: IPC_VEHICLE_SETUP2.AUX5_PWRMD = 1 (BATTERY)
2. Send CAN: IPC_VEHICLE_SETUP2.AUX5_PWRMD = 0 (IGNITION)
3. Read the Vehicle Settings menu and check that the SWITCH 5 Power Mode setting is displayed as IGNITION
```

逐列清單（含 D 欄）：`_v2_path_split.tsv`。
`PATH_ABSENT` 因此仍為 **457 列**（v1 為 365，差額 92 即本節之列 —— v1 未把它們算進去）。

---

## §D　§2.4　Options 正規化

分隔符 `/`、`,`、`+` 兩側各一空格，字詞逐字不動。套用後
`Off/ Only Warning/Warning+ Active Braking` → `"Off" / "Only Warning" / "Warning + Active Braking"`，
**與下放包 §4 之參考輸出逐字一致**（v1 之空格差已消除）。

---

## §E　(3) 分支之 30 列（D 欄全列）

| 列 | D 欄 |
|---:|---|
| r38, r39, r40 | `SWE1-VC-RearGuidanceLightStatus-086/-087/-088` |
| r90, r91 | `SWE1-VC-Language-059/-062` |
| r146 | `SWE1-VC-SignatureLighting-025` |
| r155 | `SWE1-VC-ForwardCollisionWarningSensitivity-046` |
| r223–r226 | `SWE1-VC-NewSpeedZoneIndication-039/-040/-041/-042` |
| r321–r323 | `SWE1-VC-ReadytoDrivePopUp-028/-029/-030` |
| r326–r328 | `SWE1-VC-AutoFoldMirrors-034/-035/-036` |
| r331–r333 | `SWE1-VC-DriverEasyExitSeat-040/-041/-042` |
| r334–r337 | `SWE1-VC-EngineOffPowerDelay-046/-048/-049/-050` |
| r356–r358 | `SWE1-VC-AutomaticTrailerLight Check-041/-042/-043` |
| r447 | `SWE1-VC-DistanceUnit-021` |
| r448 | `SWE1-VC-SpeedUnit-026` |
| r449 | `SWE1-VC-ConsumptionUnit-031` |

逐列見 `_v2_branch3.tsv`。**30 < 100，未觸及包內之停止條件。**

---

## §F　沿用 v1 且未變之項

`NEG_CONTRA` **3 列**（r150／r153／r156）、`NON_NAFTA` **19 列**（r400–r418）、
`ALWAYS_FALSE` 之登記、`VARIANT_UNRESOLVED`（v2 為 22 列）。
`Test Case ID`（F 欄）仍全 457 列為空。
