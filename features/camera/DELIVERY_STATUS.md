# Camera（FW036 R1L）—— 交付狀態

**一頁式閘表**，供 Pei 作 Phase 7 之依據。日期 2026-09-23（CAM-24 §4 建檔）。
日後 DR 結案／bench 驗畢時由執行層更新本檔，並於該輪上繳包記其新 sha。

---

## 1　兩本候選

| 本 | 檔（`features/camera/sandbox/`）| 列數 | TC | D 欄佔位 | sha256 |
|---|---|---:|---:|---:|---|
| **A** | `a_dryrun/…_RearViewCamera_A_20260923_dryrun3.xlsx` | **249** | 245 | 4 | `c11e1840a0216d53…` |
| **B** | `b_dryrun/…_RearViewCamera_B_20260923_dryrun.xlsx` | **212** | 206 | 6 | `3724671b88fbe17c…` |
| | **合計** | **461** | **451** | 10 | |

**兩本分交**（**R-CAM1(a)**）；合併與否由 Pei 定。
交付檔名依 workflow 模板事實：`…_SWQT_RearViewCamera_A_<YYYYMMDD>.xlsx`／`…_B_<YYYYMMDD>.xlsx`
（`delivered/` 只放客戶檔名定稿、無 `dryrun` 尾綴，**R-G42 五**）。
**A 本之交付候選自 dryrun2（244 列）改指 dryrun3**（DECISIONS 6-58 之更新，6-78）。

## 2　TC 總數與來源覆蓋

| 本 | 037 列 | leaf | PRODUCED leaf | 零 TC leaf | umbrella | **TC** |
|---|---:|---:|---:|---:|---:|---:|
| A（SWRA_V02）| 25 | 25 | 21 | 4 | 0 | **245** |
| B（RVC-HMI_V0.1）| 230 | 203 | 197 | 6 | 27 | **206** |
| | | | | | | **451** |

**A 本之 1:9.8**（25 SWE 列 → 245 TC）因其拆解全在執行層；
**B 本之 1:1.02**（197 leaf → 206 TC）因 037 已自行前拆 39.1%（**DECISIONS 6-77**）。

### 零 TC 之四形制（**R-CAM16／16(b)／16(c)** ＋ Heading）

| 形制 | 條 | A 本 | B 本 | 列 |
|---|---|---:|---:|---|
| 全來源委派 | R-CAM16 | 3 | 0 | `SWE-CAM-007`／`-013`／`-025` |
| BLOCKED（缺件）| DR-CAM-a | 1 | 0 | `SWE-CAM-024` |
| 來源自陳 `N/A` | R-CAM16(b) | 0 | 1 | `SWE1-RVC-069` |
| 逐字重複／純交叉引用 | R-CAM16(c) | 0 | 5 | `-086`／`-091`／`-102`／`-136`／`-139` |
| Heading（umbrella）| R-G42 一之外 | 0 | 27 | 不入工作簿（**6-73**）|

零 TC leaf **各補一列僅填 D 欄**，`AH` 註其形制（**6-52**／**6-73**）。

## 3　PENDING ↔ DR（**Phase 7 之閘**）

**11 條阻交付**，共 **77／451 列**（A 43／B 34）：

| DR | 題 | A 列 | B 列 | 合計 |
|---|---|---:|---:|---:|
| DR-CAM-f | 缺件之 DBC 三類（`BED_EXTENDER`／HDCC27 之 FD-CAN8 全本 等）| 9 | 0 | 9 |
| DR-CAM-g | HMI 入口路徑之逐字來源（Controls page／Status bar Shortcut menu）| 5 | 7 | 12 |
| DR-CAM-h | Pop Up List 之 camera 相關缺件（out-of-position／`connecting`）| 0 | 3 | 3 |
| DR-CAM-i | `LTM_OperationalModeSts` ↔ `CmdIgnSts` 值對應表 | 4 | 0 | 4 |
| DR-CAM-j | Auxiliary Cameras 之訊號定義（四項）| 7 | 0 | 7 |
| DR-CAM-k | VF664 全文件 | 1 | 0 | 1 |
| DR-CAM-m | EVS HAL 支援之影像格式 | 1 | 0 | 1 |
| DR-CAM-p | LVDS 訊息之傳送週期 | 2 | 0 | 2 |
| DR-CAM-q | DTC 之識別碼 | 14 | 0 | 14 |
| DR-CAM-r | `Camera App`／`Enhanced Camera App` 配備旗標 | 0 | 26 | 26 |
| DR-CAM-s | 熱保護關顯示之進入法 | 0 | 1 | 1 |
| **合計（相異 TC 列）** | | **43** | **34** | **77** |

另 **DR-CAM-a**（VF617_V5 缺件）阻 `SWE-CAM-024` 全條（0 TC，已佔位）。
**未結 DR 共 19 條**（`DR-CAM-a` ～ `-s`）；其餘 8 條（b／c／d／e／l／n／o ＋ 已解消者）於現行 451 列無 PENDING。
逐列對照：`data/pending_by_dr.tsv`（A）／`data/pending_by_dr_b.tsv`（B）。

**Pei 之裁**（三選一，可逐 DR 不同）：① 結案 ② 裁降 NA ③ 帶 PENDING 不出貨。
**R-G42 七**：`delivered/` 內 PENDING 須為 **0**；例外須有 R- 號記入 MANIFEST note。

## 4　實機驗證

`features/camera/data/bench_verify.md` —— **101 列**
（A 本 11 ＋ batch05 4、B01a 3、B01b 8、B02a 11、B02b 12、B03 16、B04a 10、B05 20、B06 6）。
非缺陷清單；其 lint 與 selfcheck 皆已全綠，此處記「紙面可判、實機待證」者。

## 5　RD 回饋

**RDF-01 ～ RDF-17，17 條**（`features/camera/RD_FEEDBACK.md`）。
本階段新開：RDF-11（X 鍵位置）／-12（`N/A` 列不應為 leaf）／-13（設定名大小寫）／
-14（§34.3／§34.4 重複）／-15（`PU0456` 之 `<Nol>`）／-16（橫幅時限 5 vs 10）／
-17（`Make Favorite`／`Edit Favorite`）。**回 RD 作者為交付前置**（不阻 Phase 7）。

## 6　全域待辦

**GCB-01 ～ GCB-12，12 項**（`docs/fw036/handoff/GC_BACKLOG.md`），皆 **OPEN**。
其中 **GCB-01**（`gates_tsv.py` 未登 `Z` 檢查）於註記「**Camera 交付前必須完成**」；
**GCB-04**（`RULINGS.sha.tsv` 未重生）與 **GCB-11**（lint `X` 之入口清單）為非本線可改。

## 7　品質狀態（全 451 列）

```
selfcheck_camera.py   ERROR 級十項  全 0
                      第 10 項（WARN）候選 37（8.3%），已知以偽陽為主（6-80 不逐列覆核）
lint036 --profile camera
  A dryrun3（249 列）  ERROR 類全 0｜J 37（profile §5.1 逐字豁免）／U 54／I-cross 245／X 3
  B dryrun（212 列）   ERROR 類全 0｜J 0／U 44／I-cross 206／X 23（GCB-11）
render_tc.py --verify  十九目錄 451 份 md 逐位元相符 451／相異 0
```

## 8　Phase 7 前置條件

1. §3 之 11 條 DR **結案或裁降 NA**（**R-G42 七**）。
2. §4 之 **101 列實機驗證**（其結果可能改寫 ER 或新增 PENDING）。
3. **GCB-01** 完成（`Z` 檢查入閘登錄簿，R-G56）。
4. Pei 之准：`--write`／tag／寫 `features/camera/delivered/`；
   內容物依 **R-G42 六**：xlsx ＋ MANIFEST ＋ DELIVERY_NOTE ＋ 未結 DR 清單 ＋（PARTIAL）tc_id 對照表。
5. 兩本分交或合併之決定（**R-CAM1(a)** 為兩本）。

## 沿革

- 2026-09-23 建檔（CAM-24 §4）。A 245 ＋ B 206 ＝ 451 TC；11 條 DR 阻交付。
