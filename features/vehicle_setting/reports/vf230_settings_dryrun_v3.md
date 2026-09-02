# VF230 設定項查找配方 dry-run **v3** 摘要（VS-SL-03 §1）

日期：2026-09-02　性質：**報告為 dry-run；寫回稿另落沙盒（VS-SL-03 §2）**
明細：`vf230_settings_dryrun_v3.tsv`（457 列）　產生器：`scripts/vs_sl03_dryrun_v3.py`
綁定器：`scripts/vs_sl03_bind.py`　附件：`_v3_branch3.tsv`
v1／v2 保留不覆寫。

---

## §A　別名綁定（Pei 2026-09-02 認可 44 名）

`settings_alias.tsv`（107 列）之 `match_type`：**exact 51／manual 46／UNRESOLVED 10**。
（manual 46 = Tier 2 之 44 ＋ v1 自行判定之 2；UNRESOLVED 10 = DR 之 9 ＋ drop 之 1。）

44 名之綁定**一律取自 `tier2_evidence` 之明指**，不以名稱相似度推算：

| 形式 | 判準 | 名數 |
|---|---|---:|
| A | `HMI r311 [4.] …` → Settings 第 311 列 | 22 |
| B | `… Power Source（r583）` → Settings 第 583 列 | 6 |
| C | `Aux n > Type` → 以（parent `Aux n`、item `Type`）綁；n 取自 tc_name 之 `SWITCH n` | 12 |
| D | evidence 只給分類或標「待認」→ **不綁 path**，只綁 FIP | 4 |

**綁定成功 39／44**（有 path）；**5 名不綁 path**（`6 Aux Switches`、`AUX Switches`、
`4 AUX Switches`、`Rearview Camera Dynamic Guidelines`、`Trailer Number`）——
其 evidence 逐字載「對應物待認」或只給分類，故本層不綁，掛 `ALIAS_MANUAL_NO_PATH`（15 列）。

---

## §B　v2 → v3

| 項 | v2 | **v3** | 說明 |
|---|---:|---:|---|
| 報告列 | 457 | **457** | 自檢 1 PASS |
| `ALIAS_UNRESOLVED` | 179 | **43** | 見下之差異說明 |
| `path_proposed` 產出 | 79 | **240** | 綁定之效 |
| **(3) 二來源皆空** | 30 | **105** | 見下之差異說明 |
| `PROXI_PENDING` | 30 | **105** | 與 (3) 同數 |
| `RAW_MISSING` | 35 | **71** | 新綁之 FIP 條件帶入更多 label |
| `OR_VALUE` | 3 | **11** | 同上 |
| `EP_SIBLING` | 3 | **11** | 同上 |

分支：**(1) 152／(2) 157／(3) 105／(4) 43**。

### `ALIAS_UNRESOLVED` 為 43，非包內預期之「約 3」

包內之 179 − 176 = 3 為**列數相減**，惟該 176 列並非全在 (4) 分支：
其中 **40 列之 `proxi_now` 非空**，依 §2.1 優先落 **(1) 形制改寫**，本就不掛 `ALIAS_UNRESOLVED`。
實際落在 (4) 者為 136 列，故 179 − 136 = **43**。43 列即 DR 之 9 名與 drop 之 1 名所涉。

### (3) 由 30 升至 105 —— 綁定之副作用，非回歸

v2 之 30 列為 v3 之**真子集**（`v2 有而 v3 無 = 0`）。新增 75 列全部來自
「原本卡在 (4)、綁定後才第一次被真正評估」之名：

| 設定項族 | 名數 | 新增列 |
|---|---:|---:|
| `SWITCH 1–6 Type`／`Power Mode`／`Hold Last State` | 18 | 54 |
| `Park Sense Front/Rear Volume` | 2 | 8 |
| `Suspension Default Ride Height`／`Service Mode` | 2 | 6 |
| `Navigation Turn by Turn`／`Phone Repetition` | 2 | 6 |
| `Hour Mode` | 1 | 1 |

**成因**：此族之條件在需求原文中以 **CAN 訊號**表述
（`IPC_VEHICLE_SETUP2.AUX5_PWRMD` 等），非 `$var$ = [label]` 之 PROXI 條件式；
且 SWITCH 一族於总控表無對應列。依 §2.1 之 (3) 落 `PENDING`，**不猜值**。

> **本層提請 Tier 2 注意**：此 105 列之 `PENDING` 所指之問題
> （「別名已解，但兩來源皆未載其 PROXI 條件」）與本輪 DR 稿之三節**均不同**。
> DR 稿依包內 §3 只寫三節，**未擅自擴充**；是否另立一節或另開 DR，請裁。

---

## §C　沿用且未變

`NEG_CONTRA` **3 列**（r150／r153／r156）、`NON_NAFTA` **19 列**（r400–r418）、
`PATH_ABSENT` 457 列、`VARIANT_UNRESOLVED` 22 列、`ALWAYS_FALSE` 3 列。

## §D　自檢（四項，同 VS-SL-02 §2.6）

| # | 項 | 結果 |
|---|---|---|
| 1 | 三本列數 457／151／126 | **PASS** |
| 2 | `PROXI_PENDING` ∩ `ALIAS_UNRESOLVED` = 0 | **PASS** |
| 3 | `proxi_now` 非空而提議 PENDING = 0 | **PASS** |
| 4 | 抽 3 條貼 proposed 全文 | **PASS**（r150／r151／r14） |

## §E　執行層自報之更正（`settings_lookup.load_settings`）

原判「第一層之容器」只認 D 欄為 `>` 者。實測 `21. Aux Switches` 之
`Aux 1`–`Aux 6`（r565–r588）**D 欄為空**卻確有 `N.M` 子項，故其子項之 parent 一律落空，
路徑會少一層。已改為「D 欄為 `>` 或為空者皆令其名成為後續 `N.M` 列之 parent」。

- 攤平後之項數**不變（517）**，逐項比對「新版少掉者 0、多出者 0」，只有 `parent` 改對
- FCW 之路徑複驗**不變**：`Settings > Safety & Driving Assistance > Automatic Emergency Braking > Forward Collision Warning`
- v1 §A 曾載「攤平後 519」係 `--list-settings` 之輸出行數（選項字串含換行），**正確數為 517**
