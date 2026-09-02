# framework — Vehicle Setup Management R1L TBM（vsm_v43）

日期：2026-09-02（P3，下放包 05 W-9）
**Layer 1 鎖定；Layer 2 未鎖、且不得預填** —— 037 = 0（R-VT4），DR-VT1 依 Pei 裁未送。
依 IN §4.1.5：Layer 1／2 寫入工作簿（Test Group／Test Set 欄），Layer 3 僅存本檔。

## Layer 1 — Test Group（**鎖定**）

`Vehicle Setup Management R1L TBM`（R-VT3）

工作簿 G 欄逐字取此值；`feature.yaml` 之 `test_group` 已同步（R-VT3）。
交付檔名之 feature 段為 `VehicleSetupManagementR1LTBM`（R-VT3，R-G42 五禁尾綴）。

## Layer 2 — Test Set（**暫代鎖定，R-VT19，Pei 2026-09-02「准」**；正式版待 037 重錨時重議）

> **加註（2026-09-02，R-VT22(b)）—— v2 重組中，鎖定待 Pei**
> Pei 裁「甲」（R-VT22）後，暫代母體改為 **v2（`data/leaves_interim_v2.tsv`，實測 336 列）**。
> **下表為 v1（295 列）之鎖定，依 R-TM13 不刪只標**；v2 之分組實測見
> `docs/upstream/10_mother_v2.md` §W-2（**19 組** ＝ 十六舊組 ＋ 三新組
> `EPB Maintenance Mode` 19／`Auto Park Brake` 5／`Rearview Camera` 10）。
> **v2 之表由分析層定、Pei 准後方鎖**；執行層只出列數，不定表、不命名。
> Layer 3 於 v2 另帶 `spec_section` 欄（`direct` 42／`segment_map` 195／`none` 99，R-VT22(c)）。

### Layer 2 **v2 表**（R-VT23(d)，**待 Pei 准後鎖**）

母體：`data/leaves_interim_v2.tsv` 之 `status ∈ {active, stale_ref_r4}` = **325** 列
（v2 336 − superseded 2 − deprecated_r4 9）。列數為執行層實測（上繳 11 §W-2）。

| # | Test Set | leaf | 對 v1 之變動 |
|---|---|---|---|
| 1 | PROXI Configuration | **65** | 67 → 65（R-VT23(c) 去 `-824`／`-825`／`-844` 三列，＋`-1278`） |
| 2 | Exterior Lighting | **32** | 不變 |
| 3 | Door Lock and Access | **30** | 不變 |
| 4 | Units | **27** | +1 |
| 5 | Clock and Time | **25** | +1 |
| 6 | **EPB Maintenance Mode** | **19** | **新組**（R-VT22(b)） |
| 7 | Lane Departure Warning | **18** | 不變 |
| 8 | Park Sense | **17** | +2 |
| 9 | Forward Collision Warning | **15** | 不變 |
| 10 | Privacy and Service Data Reset | **14** | 不變 |
| 11 | Setup Acknowledge and Recovery | **13** | 不變 |
| 12 | **Side Distance Warning** | **10** | 原 `Side and Blind Spot Warnings` 16；去 BSD 6 列後**改名**（R-VT23(b)(d)） |
| 13 | Interior Ambient Lighting | **10** | 不變（**已凍 b1 之組，10 列全 `active`**） |
| 14 | **Rearview Camera** | **10** | **新組**（R-VT22(b)） |
| 15 | Wiper and Sensor | **5** | 7 → 5（`-472`／`-473` 依 R-VT23(a) 轉 `superseded`） |
| 16 | **Auto Park Brake** | **5** | **新組**（R-VT22(b)） |
| 17 | Language | **4** | 不變 |
| 18 | Phone and Navigation Repetition | **4** | 不變 |
| 19 | Menu Access and Persistence | **2** | 不變 |
| | **合計** | **325** | |

**隔離列不入本表**（不刪只標，037 重錨終裁）：
`superseded` **2**（`-472`／`-473`）、`deprecated_r4` **9**（Blind Spot `-577`〜`-582` 六列；
組態表列 `-824`／`-825`／`-844` 三列）。
`stale_ref_r4` **3**（`-897`／`-899`／`-907`）**計入本表**，但生成時**被刪條件子句不入 TC**（R-VT23(c)）。

---

### v1 表（295 列，R-VT19；**依 R-TM13 不刪只標**）

| # | Test Set | leaf | Layer 3（chapter_for_vf，不入工作簿） |
|---|---|---|---|
| 1 | Exterior Lighting | 32 | 01.11.01.01.01／.02／.12／.13／.14／.25 |
| 2 | Lane Departure Warning | 18 | .03／.04 |
| 3 | Forward Collision Warning | 15 | .06 |
| 4 | Side and Blind Spot Warnings | 16 | .05／.15 |
| 5 | Park Sense | 15 | .24 |
| 6 | Units | 26 | .10／.10.01／.10.02／.10.03／.10.04 |
| 7 | Clock and Time | 24 | .08.01／.08.02／.08.03／.21 |
| 8 | Language | 4 | .11 |
| 9 | Door Lock and Access | 30 | .09／.16／.17／.18／.19／.20 |
| 10 | Interior Ambient Lighting | 10 | .26 |
| 11 | Wiper and Sensor | 5 | .07 |
| 12 | Phone and Navigation Repetition | 4 | .22／.23 |
| 13 | Privacy and Service Data Reset | 14 | .27／.28／.29／.30 |
| 14 | Setup Acknowledge and Recovery | 13 | .31／.32／01.13.02.01.01〜03 |
| 15 | Menu Access and Persistence | 2 | 01.11.01.01（根；真離群，IN §4.2） |
| 16 | PROXI Configuration | 67 | 01.14.01（38）／01.14.02.01.01〜29（29） |

合計 295（= 暫代母體）。命名與 vsm_v42 重疊處對齊（Park Sense／Units／Wiper and Sensor）。
單一 chapter 入單一 Test Set，無跨組拆列；新列（DR-VT2 增補批）依 chapter 落入既有組，無處可放先修本表。

### 舊狀態（保留對照，R-TM13）

**現況：無母體。** 037（SWE1 分析報告）於本線為 **0**：
現有兩份 037 之 `Source Requirement ID` 152/152 皆為 V42，`V43` 字串命中 0（上繳 01 E7 實測）。

依 **R-VT4**，Layer 2 須自 **037 家族**聚合（沿 `vsm_v42` framework §Layer 2 之做法）；
**不得以 SYSRA 或規格代之**（00 包禁區 §零-5）。
DR-VT1 為其唯一解，Pei 現裁先不送 —— 故本節在 037 到齊前保持空白。

> **本節留白是裁決結果，不是待辦遺漏。** 下放包 05 §五 明列
> 「framework Layer 2 被填入任何內容（待 037，不得預填）」為升級條件。

> **加註（2026-09-02，R-VT18(e)）—— 改走 SYSRA 暫代線**
> Pei 裁「送＋三」：**DR-VT1 裁定送出**（發送屬 Pei），**同時本線不等回覆**，
> 以 SYSRA 暫代母體進 P4。R-VT4 之「止於 P0–P3」與 R-VT17(b) 之掛起**均已解除**。
> - **暫代母體 = 295 列**（Functional 507 扣 DocID `VF655_V43_R3` 171 ＋ DocID 空 41；
>   兩批隔離待 DR-VT2，確認誤植者屆時以增補批併入，**不回溯改已生成之 TC**）。
>   落 `data/leaves_interim.tsv`；隔離清單 `data/isolated_vf655.tsv`／`data/isolated_nodocid.tsv`。
> - **Layer 2 之聚合材料**（`chapter_for_vf` 完整值 **72 組** ＋ 標題例 ＋ 詞頻 ＋ 訊號可執行度）
>   落 `data/layer2_material_v43.md`（執行層出材料）；**草案歸分析層，鎖定歸 Pei**。
> - **本節仍不填任何 Test Set** —— 06 包 §四明列「任何聚類命名出現於執行層產出」為升級條件。
> - **重錨條款（R-VT18(c)）**：暫代期間 TC 之 D 欄用 `Sys-RA-VF665_V43_VSM-…` 實名，
>   Remarks 逐列註 `Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1)`；
>   **重錨完成前不得交付**，除非 Pei 另裁。

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

暫代期 Layer 3 = `chapter_for_vf` 完整值（上表末欄）。chapter ↔ V43 R4 規格章節號之對應為假說，
逐章實測後方得加列 spec 錨（R-VT19(b)，P4 包 W 項）。

## 訊號書寫

依 `docs/runtime/profiles/FW036_R1L_VSM_V43_Profile.md`：
canon IN §8.7.5 v3（無 OVERRIDE）＋ R-P353／R-P355／R-P368／R-P375；
三段鏈之本線綁定見 R-VT13／R-VT15／R-VT16。
現行事實表：`data/signal_chain_v43_v5.tsv`（解得 81，全 CAN 形、全部有 VAL_）。
