# 26 — W-P3 下放包（改善案結案輪：三裁定落地 + prompt 指紋 + 自查表對映 + 閘簿補全）

日期：2026-08-24
所據上繳：`docs/fw036/upstream/25_wp2.md`（覆核 PASS）
上繳：`docs/fw036/upstream/26_wp3_closeout.md`
本包為改善案（22→23→24→25→26）之**最後一包**；上繳須含結案摘要（§G-4）。

**裁定記錄**：Pei 2026-08-24 chat「1准 2准 3准」。條文見 §C。
另三項定案（同日 chat）：裁定 D 落點依 25 包為正（R-VS82 維持）；
IN §8.7.5 範圍註記經 commit 視為裁定通過，不再標待裁；
`23b_wp2_supplement.md` 為並行 session 所產，標 [SUPERSEDED by 25]。

---

## A. 禁區

- 全部 git 操作屬 Pei（R-G5@`9814d24c`）
- 歷史 handoff / upstream 檔不改寫（R-G18@`8f61f9fd`）；
  23b 之 [SUPERSEDED] 標頭為唯一例外（加註不改內文）
- 已交付件與 done region 不動；xlsx 不碰；`features/user_profiles/`、`_intake` 不碰
- **既有 lint 報告檔案一律不重命名**（裁定 3）
- `generated/vf230_*.json` 之 seq **不重排**（裁定 1）
- seq 成因查證僅唯讀（`output/`、git log、版號紀錄）；查證結果只回報不處置

## B. 背景

W-P2 已交付（25 上繳）。殘項：三項新裁定落地、W-P3 原兩項
（R-G19 prompt 指紋、R-G21 自查表對映）、25 上繳獨立判斷之
閘簿補全與一項回查。本包收齊後改善案結案。

## C. 裁定條文（Pei 2026-08-24「1准 2准 3准」；可直接貼入）

### 裁定 1 — R-VF83 增但書 + 缺號具名（讀取基準 R-VF83@`9d5bfa4d`）

```
R-VF83 增但書：重生作廢之產出所佔用之序號成為具名缺號，登記於
ANOMALIES.md，不補寫、不重編（A-VS02 先例）。「連續遞增」之判準改為
「除具名缺號外連續遞增」。（Pei 裁定 2026-08-24）
```

配套（同包執行）：
- `A-VF{next}` 登記 seq 248–257 十號缺口，狀態依查證結果定
  （成因已證 → RESOLVED-具名缺號；未證 → ACCEPTED-具名缺號，成因待查）
- **一次性成因查證**（唯讀）：`output/`、git log、R-VS81 之版號紀錄中
  找 pilot #2 v1（或任何曾佔 248–257 之產出）。假說：間隙恰為一個
  pilot 之 10 條。查得 → 記入異常；查不得 → 記「無存證，維持具名缺號」。
  **若證據指向寫回偏移（成因 (c)，有實害）→ 停下升級（§F-1）**
- 依 R-G22@`bca29f8f`：R-VF83 因但書而換 sha，新 sha8 於上繳回報，
  tsv 重產

### 裁定 2 — S3 四支閘啟用（expected_numbers 暫緩）

```
S3 啟用（四支）：`lint_docs036.py --gate`、`canon_refs.py --waiver
--gate`、`rulings_hash.py --check`、`gates_tsv.py --check` 接於每次
上繳前（治理文件／條文／登錄簿有變動之包）與每 feature close-out；
任一 exit ≠ 0，該包不得上繳，先修或升級。`expected_numbers.py --gate`
暫不接，俟裁定 1 落地且基準項歸零後另裁。（Pei 裁定 2026-08-24）
```

落地方式：新增 `scripts/gate_all.py`（依序跑四支、逐支列 exit code、
任一非零則總 exit 1）；FO §8.2 上繳包必要成分表增一列
「四支 gate 之實跑輸出（`gate_all.py`，exit 0）」。本包上繳即首次適用。

### 裁定 3 — lint 報告檔名（新產報告起）

```
lint 報告檔名自本裁定後之新產報告起採 `{tag}_{來源檔sha8}_{YYYYMMDD}`；
既有報告檔案一律不重命名（歷史不追改）。回歸判準改為「既有報告檔案
不被重命名」，以字面案例釘入（G-N）。（Pei 裁定 2026-08-24）
```

落地：`report_stem()` 改；測試改向 —— 25 包之
`test_named_tags_are_untouched_by_the_fix` 改為驗「既有報告**檔案**
不被重命名」（新產檔名可含 feature 名與 sha8）；18 組同類碰撞在新式下
應為 0 組，實測回報。

### [DEFAULT] 二條（分析層先裁，Pei 事後追認）

```
R-VS83 [DEFAULT]：量產批 manifest 之 selection 欄自下一批起記載算式
（各項之出處與運算），不得只記結果數。620 之推導式出處由 VS 線下一輪
回查補檔。（分析層 2026-08-24）
```

```
R-G23 [DEFAULT]：同一工單同時只得有一份有效下放包；發現同輪重複下放
（如 23b 與 25 之分歧）時，以分析層指定之單一來源為準，另一份標
[SUPERSEDED] 不刪。全域線（docs/fw036）之下放包由單一分析 session
產出。（分析層 2026-08-24，依 R-VF66 之精神；Pei 得推翻）
```

## D. 作業清單

1. 裁定 1 落地：但書入 `RULINGS.md`、`A-VF{next}` 登記、成因查證（唯讀）、
   tsv 重產（R-VF83 新 sha）
2. 裁定 2 落地：`gate_all.py` + FO §8.2 增列；本包上繳前實跑
3. 裁定 3 落地：`report_stem()` 改 + 測試改向 + 18 組實測
4. [DEFAULT] 落檔：R-VS83 入 `vehicle_setting/RULINGS.md`；R-G23 入 FO §9.2；
   23b 加 [SUPERSEDED by 25] 標頭（不改內文）
5. **W-P3-1（R-G19）**：`make_batch_context.py` 輸出 prompt 模板 sha256 與
   exemplar 集 sha256 入批次 manifest；以 vf230 現行素材實跑一次驗證欄位存在
6. **W-P3-2（R-G21）**：IN §9 自查 17 項逐項對映閘 id 或標「人工項」，
   對映表入 `GATES.tsv`（`selfcheck_item` 欄或附表）；已知案例驗證：
   Home A-H10 之引號規則，其對映之閘須實測轉紅（G-K）
7. **閘簿補全**（25 上繳 §十三-1/2）：`lint_docs036.py` 與 feature 級閘
   （`vehicle_setting` 之 `lint_tcs.py`、`vf230_selfcheck_wvf62.py` 等）入
   `GATES.tsv`；`effective_date` 自 git log／上繳包回填，回填不到者維持
   「未載明」並記已試之來源
8. **回查**（25 上繳 §十三-6）：掃 handoff／upstream 有無以十一-1 之
   15 個新入 tsv 錨點編號帶 sha 之引用（預期 0，R-G13 之前無 sha 可引）
9. 全套 pytest；`gate_all.py`；上繳

## E. 預期數字

| # | 指標 | 預期 |
|---|---|---|
| 1 | `gate_all.py` | exit **0**（四支逐支列出）|
| 2 | R-VF83 sha8 | `9d5bfa4d` → **變**（新值回報）|
| 3 | tsv 錨點數 | 188 → **190**（+R-VS83、+R-G23）|
| 4 | `GATES.tsv` 閘數 | 20 → 回報實測（首量即基線；新入閘之命中數標未知，不以 0 代）|
| 5 | 自查 17 項對映 | 17 項各有閘 id 或「人工項」，無空值；人工項數回報 |
| 6 | 新式檔名下 18 組碰撞 | → **0** |
| 7 | 既有 16 份報告檔案 | **位元組與檔名皆不變** |
| 8 | 回查（步 8）命中 | **0**（非 0 即逐項列）|
| 9 | seq 缺號 | 維持 10（**不補不重排**）；`expected_numbers.py` 於但書後對缺號項轉「具名缺號 10」不再計 FAIL 項 |
| 10 | 全套 pytest 失敗數 | **8**（既有，不得增減）|
| 11 | `canon_refs --waiver` FAIL | 0；`active-backlog` 179 **不變**（本包不得新增活躍積壓）|

## F. 升級條件

1. seq 查證證據指向寫回偏移（成因 (c)）—— 有實害，停下
2. A-H10 已知案例之對映閘**不轉紅** —— R-G21 之對映失真，停下
3. `effective_date` 回填與既有記載矛盾
4. 步 8 回查命中 ≠ 0
5. feature 級閘入簿時發現閘與 lint_defs 語意不一致（R-VS55 之形態）

## G. 上繳要求

1. 23 包 §G 全項 + R-G13 引用表（本包引用：R-G5@`9814d24c`、
   R-G13@`abdc56e3`、R-G18@`8f61f9fd`、R-G22@`bca29f8f`、
   R-VF83@`9d5bfa4d`（讀取基準，改後換發）、R-VS82@`12177e4f`；
   實讀不符即停）
2. seq 成因查證之證據清單（含「查了哪裡、沒查到什麼」）
3. 自查 17 項對映表全文 + 人工項清單
4. **結案摘要**：22→26 全案之交付清單（條文 R-G13~R-G23、工具五支、
   三簿 tsv、canon 整併）、遺留具名清單（active-backlog 179、
   unqualified 盲區、expected_numbers 暫緩之閘、19 處無限定詞引用、
   report 檔名 18 組之舊檔）、及「本案是否仍有該驗而未驗者」

## H. 本包產生之新條文清單（自檢表）

- [x] 裁定 1（R-VF83 但書）— 區塊已列
- [x] 裁定 2（S3 四支啟用）— 區塊已列
- [x] 裁定 3（報告檔名）— 區塊已列
- [x] R-VS83 [DEFAULT] — 區塊已列，待追認
- [x] R-G23 [DEFAULT] — 區塊已列，待追認

本包引用之既有條文：R-G5、R-G9、R-G11、R-G12、R-G13、R-G17、R-G18、
R-G19、R-G21、R-G22、R-VF66、R-VS55、R-VS81、A-VS02、G-D、G-K、G-N、
FO §8.2、25 上繳 §五／§七／§九／§十一／§十三。
