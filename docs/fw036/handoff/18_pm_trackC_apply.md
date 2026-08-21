# 下放包 18：軌 C 套用（PM 最後一批內容改寫）

前置：16 包（軌 A＋B）已完成，工作副本
`features/power/sandbox/b16/pm_16.xlsx`（6c849fef…）。
本包基底即該副本。新規 0 條。

## 任務

依附件逐字套用軌 C 之 30 列，改寫 `pre`／`input`／`proc`／`er` 四欄：

- `16g_pm_trackC_part1.md` — rows 124、125、126、127、149、233、234、
  265、266、267、268、269、270（13 列）
- `16h_pm_trackC_part2.md` — rows 181、275、276、277、278、279、280、
  281、282、289、290、291、293（13 列）

**注意**：附件 G 之 rows 125／126／127／234 與附件 H 之 rows 276–281／
290／293 採「與某列相同，僅某處差異」之寫法，須依該註記逐字展開，
不得只改差異處而遺漏其餘欄位之同步。

## 硬性

1. `test_item` 與 `spec_reference` **零變動**（spec_ref 已經
   037＋SYS2 錨鏈驗證為正確，見 `specref_anchor_chain_verified.md`）
2. 不得刪列、增列、合併列 —— A-PM13（265–268＋13）與
   A-PM14（181≡293）之重複列**照原列數各自寫入**
3. 附件中標 ⚠ 之處為分析層之來源限制說明，**不得據以自行補值**
4. `PowerModeSts_Telematic` 一律改
   `$STATUS_TELEMATIC.PowerSts_Telematic$`（Pei 裁定，17 包 §五）
5. PROXI 依 R-1 v3(c)：`PROXI <Param> = <值>`，**不加 `$`**
   （rows 289／290／291 之原列有 `$VC_VEH_BRAND$`／
   `PROXI $TBM_Present$`，須統一）

## 驗收

- 軌 C 30 列：四欄皆有變動；`test_item`／`spec_reference` 零變動
- 全 283 列合計：
  - `input_not_na` = 0；`listed_in_input` = 0
  - `triplet`（in…on）= 0；`send_can` 舊式 = 0
  - `pre_unnumbered` = 0；`pre_multi` = 0；
    `pre_first_is_tool` = 0；`pre_last_not_tool` = 0
  - `step_multi_obs` = 0；`read_without_value` = 0
  - `nbsp` = 0；`proc_er_mismatch` = 0
- lint036：A–N 全零、**E = 0**；P 殘存僅限 test_item 括號下半
- x14 下拉讀回；壓縮成員數未變；`surgical_save` 唯一路徑
- 交付本唯讀，止於工作副本

## 上繳

`docs/fw036/upstream/18_pm_trackC.md`：30 列改動清單、
展開型（「同某列」）之逐列確認、lint 前後、diff 證明、
**「本包是否仍有該驗而未驗者」獨立判斷**、引用裁決編號清單。

另請於上繳補答 17 包 §六之未決項：
**row 186 移除兩處推定值後之現行狀態**（留空／NA／PENDING），
若留空且該步驟已無判準，須標 `PENDING: DR-{n}`。
