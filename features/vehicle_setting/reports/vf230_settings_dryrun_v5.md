# VF230 dry-run **v5** 摘要（VS-SL-05，送抽前修正）

日期：2026-09-02　明細：`vf230_settings_dryrun_v5.tsv`（457 列）
Pre 修正清單：`_v5_pre_fix.tsv`（52 列）　二次查找：`_v4_branch3_resolution.tsv`（已改判 R4）
產生器：`scripts/vs_sl05_fix.py`
沙盒之 v4 稿另存 `sandbox/vssl/vf230_vssl.v4.bak.xlsx`；v3 稿仍存 `.v3.bak.xlsx`。
**BL／VC 本包不動。**

---

## §A　Pre「menu is open」矛盾修正（審閱 VS-SL-04 §3）

| 項 | 列 |
|---|---:|
| Pre 含 `The Vehicle Settings menu is open` | **90** |
| 其中 Procedure 已插本輪之 `Press "Settings" on Menu Bar` → **修正** | **52** |
| 未插導覽段 → **不動** | **38** |

**Tier 2 所測之 52 與本層實跑相同。**
修法：刪該 Pre 行並重編號。理由：Pre 斷言之狀態隨後由步驟建立，
且該句屬步驟可控狀態，依 IN §4.4 不得為 Pre。
未插導覽之 38 列不動 —— 原稿無導覽段時該 Pre 行自洽（此為插入邏輯之遺漏，非原稿既有病）。

修正後複驗：**「Pre 含該句且已插導覽」之列 = 0**；仍含該句者 **38** 列，與預期相符。
每列刪除之行數皆為 1（assert PASS）。

樣本 r14（`SWE1-VC-SWITCH5PowerMode-023`）修正後之 Pre：

```
1. The HU is in the Full-Operation state
2. FD-CAN8 is connected to the bus simulator with signal tracing enabled
3. PROXI AUX_Switch_Types = 2 (Type 2)
```

---

## §B　R4 否定式代表值（審閱 VS-SL-04 §2，7 列）

`_v4_branch3_resolution.tsv` 就地改判：`NEGATED_CONDITION` → `resolution = R4`，
`subcase = NEGATED_EP_REPRESENTATIVE`。

| 設定項 | 列 | 总控表 | 提議 | 註記 |
|---|---:|---|---|---|
| `Engine Off Power Delay` | 4 | No.149 `If Country_Code is not [Australia]` | `PROXI Country_Code = 2 (United States of America)` | EP 代表值；**值表 15 個值中無 Australia**，故其補集即全表 |
| `Automatic Trailer Light Check` | 3 | No.268 `If Trailer_Light_Check is NOT [Absent])` | `PROXI Trailer_Light_Check = 1 (Type 1 (Radio))` | EP 代表值；兄弟值 `2 (Type 2)`／`3 (Type 3)` |

值表為本層複驗：`Country_Code` 15 值、`2 = United States of America`、**無 Australia**；
`Trailer_Light_Check = {0: Absent, 1: Type 1 (Radio), 2: Type 2, 3: Type 3}`。

> 報告之 schema 無 `reasoning` 欄；註記寫於 `proxi_proposed` 之 `｜` 之後，
> 與既有之 `EP 兄弟` 註記同法。

沙盒稿複驗：`PROXI Country_Code` **4 列**；`PROXI Trailer_Light_Check` **5 列**
（R4 之 3 列 ＋ r354／r355 本已於分支 (1) 帶該參數者 2 列）。

---

## §C　v4 → v5

| 項 | v4 | **v5** |
|---|---:|---:|
| 報告列 | 457 | **457** |
| `PROXI_PENDING` | 32 | **25** |
| 分支 (3) | 32 | **25** |
| 新分支 (2e) 否定式 EP 代表值 | — | **7** |

分支全表：**(1) 152／(2) 系列 200／(2b) 54／(2c) 3／(2d) 16／(2e) 7／(3) 25／(4) 43**。

---

## §D　沙盒稿與 lint

`sandbox/vssl/vf230_vssl.xlsx`：**457 → 438 列**，改動 **1,084** 處（重生），
再套 Pre 修正 **52** 列。

lint 四項，三本全 **PASS**：

| 本 | 列 | 括號下半 | 尾句號 | 雙引號 | Proc↔ER 步數 |
|---|---:|---:|---:|---:|---:|
| vf230 | 438 | 0 | 0 | 0 | **0** |
| bl | 151 | 0 | 0 | 0 | 0 |
| vc | 126 | 0 | 0 | 0 | 0 |

## §E　DR 稿

第四節由 11 名 32 列縮為 **9 名 25 列**；`Engine Off Power Delay` 與
`Automatic Trailer Light Check` 已解，自 DR 移除，不再問上游。既有一～三節不動。
