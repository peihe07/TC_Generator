# Camera（FW036 R1L）—— 交付狀態

**一頁式閘表**，供 Pei 作 Phase 7 之依據。日期 2026-09-24（CAM-24 §4 建檔；CAM-26 §3 更新；**CAM-27 §4 終態**；CAM-28 來源改版核對）。
日後 DR 結案／bench 驗畢時由執行層更新本檔，並於該輪上繳包記其新 sha。

---

## 1　兩本候選

| 本 | 檔（`features/camera/sandbox/`）| 列數 | TC | D 欄佔位 | sha256 |
|---|---|---:|---:|---:|---|
| **A** | `a_dryrun/…_RearViewCamera_A_20260924_dryrun4.xlsx` | **249** | 249 | 0 | `a4ad6cf3112d5e31…` |
| **B** | `b_dryrun/…_RearViewCamera_B_20260924_dryrun4.xlsx` | **216** | 216 | 0 | `a279e6fa2106541b…` |
| | **合計** | **465** | **465** | 0 | |

**工作簿列數 ＝ TC 數**（**R-CAM19(e)**：D 欄佔位列形制作廢）。
**兩本分交**（**R-CAM1(a)**）；合併與否由 Pei 定。
交付檔名依 workflow 模板事實：`…_SWQT_RearViewCamera_A_<YYYYMMDD>.xlsx`／`…_B_<YYYYMMDD>.xlsx`
（`delivered/` 只放客戶檔名定稿、無 `dryrun` 尾綴，**R-G42 五**）。
候選沿革：A 本 dryrun2（244 列）→ dryrun3（249 列，6-78）→ **dryrun4**（CAM-26）；
B 本 dryrun2 → dryrun3（CAM-26）→ **dryrun4**（CAM-27：`NR1L-RVCHMI-087` 之車型補正，三格）。

## 2　TC 總數與來源覆蓋

| 本 | 037 列 | leaf | **有 TC 之 leaf** | umbrella | **TC** |
|---|---:|---:|---:|---:|---:|
| A（SWRA_V02）| 25 | 25 | **25/25** | 0 | **249** |
| B（RVC-HMI_V0.1）| 230 | 203 | **203/203** | 27 | **216** |
| | | **228** | **228/228** | | **465** |

**每條 leaf 需求 ≥ 1 TC：A 25/25、B 203/203**（**R-CAM19(a)**，Pei 2026-09-24「有需求就要有產出」）。
逐列對照：`data/traceability.tsv`（228 leaf → tc_ids）；umbrella 27 列另表 `data/traceability_umbrella.tsv`
（037 `Categorization = Heading`，不入 R-CAM19(a) 之母體，其子 leaf 皆有 TC）。
**R-CAM19(f)**：已有 TC 之需求，其與他列共引之來源不再各自出 TC（§8.2.1）—— 補生成之射程止於原零 TC 之十列。

**A 本之 1:10**（25 SWE 列 → 249 TC）因其拆解全在執行層；
**B 本之 1:1.06**（203 leaf → 216 TC）因 037 已自行前拆 39.1%（**DECISIONS 6-77**）。

### 原零 TC 之十列（R-CAM19 後各出一列）

| 原形制 | 原條（已撤銷／修訂）| 列 | 本輪之 TC |
|---|---|---|---|
| 全來源委派 | R-CAM16 → R-CAM19(b)(c) | `SWE-CAM-007`／`-013`／`-025` | `NR1L-RVC-246`／`-247`／`-249` |
| BLOCKED（缺件）| 6-52 → R-CAM19(d) | `SWE-CAM-024` | `NR1L-RVC-248`（六欄 `PENDING: DR-CAM-a`）|
| 來源自陳 `N/A` | R-CAM16(b) → R-CAM19(c) | `SWE1-RVC-069` | `NR1L-RVCHMI-211` |
| 逐字重複／純交叉引用 | R-CAM16(c) → R-CAM19(c) | `-086`／`-091`／`-102`／`-136`／`-139` | `NR1L-RVCHMI-212`～`-216` |

## 3　PENDING ↔ DR（**Phase 7 之閘**）

**13 條阻交付**，共 **81／465 列**（A 46／B 35）：

| DR | 題 | A 列 | B 列 | 合計 |
|---|---|---:|---:|---:|
| DR-CAM-a | SYS2 VF617_V5 缺件 | 1 | 0 | 1 |
| DR-CAM-f | 缺件之 DBC 三類（`BED_EXTENDER`／HDCC27 之 FD-CAN8 全本 等）| 10 | 0 | 10 |
| DR-CAM-g | HMI 入口路徑之逐字來源（Controls page／Status bar Shortcut menu）| 5 | 7 | 12 |
| DR-CAM-h | Pop Up List 之 camera 相關缺件（out-of-position／`connecting`）| 1 | 4 | 5 |
| DR-CAM-i | `LTM_OperationalModeSts` ↔ `CmdIgnSts` 值對應表 | 4 | 0 | 4 |
| DR-CAM-j | Auxiliary Cameras 之訊號定義（四項）| 7 | 0 | 7 |
| DR-CAM-k | VF664 全文件 | 1 | 0 | 1 |
| DR-CAM-m | EVS HAL 支援之影像格式 | 1 | 0 | 1 |
| DR-CAM-p | LVDS 訊息之傳送週期 | 2 | 0 | 2 |
| DR-CAM-q | DTC 之識別碼 | 14 | 0 | 14 |
| DR-CAM-r | `Camera App`／`Enhanced Camera App` 配備旗標 | 0 | 26 | 26 |
| DR-CAM-s | 熱保護關顯示之進入法 | 0 | 1 | 1 |
| DR-CAM-t | LVDS `diagnosticRequest`／`diagnosticResponse` 之訊息定義（CAM-26 新開；**由 Pei 送**，CAM-26 審閱 §一-2）| 1 | 0 | 1 |
| **合計（相異 TC 列）** | | **46** | **35** | **81** |

**DR 共 20 條**（`DR-CAM-a` ～ `-t`）；阻交付 13 條，其餘 7 條（b／c／d／e／l／n／o，含已結案者）於現行 465 列無 PENDING。
A 本 Test Set 由 9 組增為 **10 組**（`AUX Camera` 1 列，即 `-248`）。
逐列對照：`data/pending_by_dr.tsv`（A）／`data/pending_by_dr_b.tsv`（B）。

**Pei 之裁**（三選一，可逐 DR 不同）：① 結案 ② 裁降 NA ③ 帶 PENDING 不出貨。
**R-G42 七**：`delivered/` 內 PENDING 須為 **0**；例外須有 R- 號記入 MANIFEST note。

## 4　實機驗證

`features/camera/data/bench_verify.md` —— **105 列**
（A 本 11 ＋ batch05 4 ＋ batch06 2、B01a 3、B01b 8、B02a 11、B02b 12、B03 16、B04a 10、B05 20、B06 6、b08 2）。
非缺陷清單；其 lint 與 selfcheck 皆已全綠，此處記「紙面可判、實機待證」者。

## 5　RD 回饋

**RDF-01 ～ RDF-18，18 條**（`features/camera/RD_FEEDBACK.md`）。**RDF-18**（SYS1 §30.1.3 `NRL-188130` 之 `or‘X’to` 缺空格）
於 CAM-27 落檔；**RDF-12** 於 CAM-26 改題「`SWE1-RVC-069` 自陳 N/A 但仍須追溯」。
**回 RD 作者為交付前置**（不阻 Phase 7）。

## 6　全域待辦

**GCB-01 ～ GCB-13，13 項**（`docs/fw036/handoff/GC_BACKLOG.md`），皆 **OPEN**。
**GCB-13**（selfcheck 第 11 項「一列多點／多觸發」，WARN，下一 feature pilot 前實作；Camera 不回跑）於 CAM-27 落檔。
其中 **GCB-01**（`gates_tsv.py` 未登 `Z` 檢查）於註記「**Camera 交付前必須完成**」；
**GCB-04**（`RULINGS.sha.tsv` 未重生）與 **GCB-11**（lint `X` 之入口清單）為非本線可改。

## 7　品質狀態（全 465 列）

```
selfcheck_camera.py   ERROR 級十項  全 0（錨 468／反查失敗 0／常數錨 2／共引錨 3／缺件佔位 1）
                      第 10 項（WARN）候選 41（8.8%），已知以偽陽為主（6-80 不逐列覆核）
lint036 --profile camera
  A dryrun4（249 列）  ERROR 類全 0｜J 37（profile §5.1 逐字豁免）／U 65／I-cross 249／X 3
  B dryrun4（216 列）  ERROR 類全 0｜J 0／U 45／I-cross 216／X 23（GCB-11）
render_tc.py --verify  二十二目錄 465 份 md 逐位元相符 465／相異 0
```

「共引錨」（R-CAM19(b)）與「缺件佔位」（R-CAM19(d)）為 CAM-26 於 selfcheck 第 1 項新增之計數類別，非違反。

## 8　Phase 7 前置條件

1. §3 之 13 條 DR **結案或裁降 NA**（**R-G42 七**）。
2. §4 之 **105 列實機驗證**（其結果可能改寫 ER 或新增 PENDING）。
3. **GCB-01** 完成（`Z` 檢查入閘登錄簿，R-G56）。
4. Pei 之准：`--write`／tag／寫 `features/camera/delivered/`；
   內容物依 **R-G42 六**：xlsx ＋ MANIFEST ＋ DELIVERY_NOTE ＋ 未結 DR 清單 ＋（PARTIAL）tc_id 對照表。
5. 兩本分交或合併之決定（**R-CAM1(a)** 為兩本）。

## 沿革

- 2026-09-23 建檔（CAM-24 §4）。A 245 ＋ B 206 ＝ 451 TC；11 條 DR 阻交付。
- 2026-09-23 更新為**終態**（CAM-25 §4）。B 本形制補正 ＋4（`b07/`，**A-CA37**），
  A 245 ＋ B 210 ＝ **455 TC**；B 候選改指 `dryrun2`。
- 2026-09-24 **R-CAM19 追溯補齊**（CAM-26，§9 之「下放包明文指派」）。原零 TC 十列各出一列（`batch06/` 4、`b08/` 6），
  A 249 ＋ B 216 ＝ **465 TC**，D 欄佔位 10 → 0；A 候選改指 `dryrun4`、B 改指 `dryrun3`；
  阻交付 DR 11 → 13（DR-CAM-a 之 `-248` 由佔位列轉為 TC 列、DR-CAM-t 新開）。
  A dryrun4 另帶入 CAM-25 已改而 dryrun3 未含之 `NR1L-RVC-245` `Remarks`（6-85）。
- 2026-09-24 **終態**（CAM-27）。6-87 落定、立 **R-CAM19(f)**（6-88）；`NR1L-RVCHMI-087` 車型補正（A-CA39 RESOLVED）；
  B 候選改指 `dryrun4`；RDF-18／GCB-13 落檔。TC 數不變（465）。
- 2026-09-24 **來源改版核對**（CAM-28，§9 第四種觸發）。REF 之 VF551_V2／V3／CFTS092 dependency 本與 V2 R2 docx 登 MANIFEST；
  V2 被引用 17 ID 之 Description 差異全為 `_x000D_`／空白（(a) NO-OP 94／(b) 0／(c) 0），**TC 0 列改動**，
  兩本候選不變（A dryrun4／B dryrun4）。RD 驗證標準對帳 `data/rd_vc_crosscheck.tsv`、七車型欄對帳 `data/vm_crosscheck.tsv`，
  其 PARTIAL／RD-ONLY 與車型差異**待 Pei 裁**，未改任何列。

## 9　生成階段結束

**Camera 之 TC 生成階段結束於 2026-09-24（CAM-27）**（下放包 CAM-01 ～ CAM-27，執行層 27 輪；
CAM-26 為 R-CAM19 之追溯補齊、CAM-27 為收尾）。**CAM-26 時開立之「下放包明文指派」例外條款自此關閉。**
本檔自此**只因下列三者變更**：

1. **DR 結案或裁降 NA** —— §3 之 13 條；結案時該列之 `PENDING` 改為實值、本檔重算；
2. **Pei 之實機回饋** —— §4 之 105 列；其結果可能改寫 ER 或新增 PENDING；
3. **Phase 7 之執行** —— §8 之五項前置齊備後，寫 `features/camera/delivered/` 並 tag；
4. **來源改版**（DECISIONS **6-89**，CAM-28 增）—— 既有 TC 所引來源出新版時，依 (a) NO-OP／(b) verbatim 改新版逐字／(c) Procedure／ER 依新版重寫處置，不生成新 TC。

**不再因生成而變更。**
