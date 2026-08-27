# 27 — 全域收尾包（tsv 重產・目錄政策・sources 集中・清理制・空白 lint・canon_refs 擴充）

日期：2026-08-24
前置：**26 已上繳且 Pei 已 commit**（§D-0 實測確認，未達即停）
上繳：`docs/fw036/upstream/27_global_wrapup.md`
本包為改善案延伸收尾；收訖後 `docs/fw036/` 全域線暫停發包，回產線節奏。

**裁定記錄（Pei 2026-08-24 chat）**：目錄政策、清理規則、sources 集中制
—— 「請幫我做好規劃和寫好規範，然後交由claude code去執行」，三案照
分析層提案通過；行首空白規制已由 Pei 裁定並落 IN §11（同日）；
R-G23′（逐線單一來源＋live 取號）已於 V33 輪裁定，本包補 FO 落點。
新條文文字之第二確認點照例為 Pei 之 commit 前 diff 過目。

---

## A. 禁區

- git 寫入操作一律屬 Pei（R-G5@`9814d24c`）；git **唯讀**（status／log／
  show）本包明示允許（R-G6），前置檢查與清理候選清單需要它
- 歷史 handoff／upstream 不改寫（R-G18@`8f61f9fd`）
- **xlsx 不得以 openpyxl 開啟寫入（R-G3）；本包對 xlsx 僅允許
  read_only 讀取與整檔複製（copy），逐位元組不變，複製後以 sha256 驗證**
- `features/vehicle_setting/generated/` **本包不清理**（V33 在途，§D-6）
- 已交付件內容不動；delivered/ 只複製不修改
- 各 feature 既有檔案一律不搬移（政策管新檔；唯一回溯動作為 §D-5 之複製）

## B. 背景

改善案 22–26 已完成條文與工具基建。本包收五件懸掛事項＋兩件 V33 輪
移交事項（R-G23′ 落點、canon_refs verbatim 判準擴充），全部一輪做完。

## C. 新條文（Pei 已裁方向；可直接貼入 FO）

> **換號註記（Pei 裁定 2026-08-27）**：本包成於 08-24，當時預配 `R-G24`／
> `R-G25`／`R-G26`。08-26 bed_lowering 01 包已 **live 取號**佔用 `R-G24`
> （下放指示之路徑實在性）。依 R-G23′「取號一律 live」，本包三條順延為
> **`R-G25`／`R-G26`／`R-G27`**，全文（§C／§D-2／§E／§H）同步換號。
> **此即 R-G23′ 所描述之失效模式本身**：預配之號在落檔時已經不是空號 ——
> R-G23 撞號為其第一例，本包為第二例，且**本包正是寫下 R-G23′ 的那一包**。

### R-G25 — 產出物目錄政策（FO 新節落點由執行層依整併後結構定，錨點唯一）

```
R-G25：產出物目錄政策如下表。政策自生效日管新檔；既有檔案不搬移。
| 位置 | 內容 | 版控 |
|---|---|---|
| features/<f>/generated/ | LLM 產出 json | 入 |
| features/<f>/data/ | 量測中間物（tsv、manifest） | 入 |
| features/<f>/sandbox/<tag>/ | 工作簿作業副本（xlsx 只准在此修改） | 入 |
| features/<f>/delivered/ | 交付定稿唯一位置；定稿以複製入內，附 sha 對照表 | 入 |
| features/<f>/reports/ | 該 feature 之 lint 報告 | 入 |
| docs/reports/ | 跨 feature／全域報告 | 入 |
| output/ | 拋棄式暫存 | 不入 |
新產出落點不符者由 lint 路徑檢查判紅。delivered/ 內 xlsx 之 sha 須與
其對照表（delivered/MANIFEST.tsv）一致。
```

### R-G26 — 工作區清理制

```
R-G26：superseded 產出（被新版取代之 json、舊 lint 報告）得自工作區
移除，git 歷史為其歸檔。移除前必跑引用懸空檢查 —— 被現行條文、異常、
waiver、對照表指名之檔不得移除。移除以專門 commit 為之，訊息列明
清單，不混入其他變更。現行有效版、delivered/、被引用檔一律留。
output/ 不入版控，隨時可清。
```

### R-G27 — 來源集中制（sources/）

```
R-G27：共用來源文件集中於頂層 sources/：raw/<doc_id>/ 放原檔
（xlsx／pdf／dbc，全 repo 一份）；extracted/<doc_id>/ 放 intake 抽取之
文字形（逐 sheet tsv／md，逐檔帶來源 sha 對照）；MANIFEST.tsv 記
doc_id、檔名、sha256、版本、使用 feature。feature 端不再存原檔副本，
feature.yaml 以 doc_id 引用。內容爭議以 raw 為準（FO §8.6 同精神）。
既有 feature 之舊副本不搬，新 feature 一律走 sources/。
```

## D. 作業清單

0. **前置實測**：`upstream/26_wp3_closeout.md` 存在；
   `git status --porcelain docs/fw036/ scripts/` 無未提交改動
   （26 之 tsv、FO、腳本皆已 commit）。任一不成立 → 停，回報現況
1. **tsv 統一重產**：`rulings_hash.py` 全跑。應併入：R-VF91–95、
   R-VF83（但書後新 sha）、V33 C-1 之兩條換發、R-VS82／83、R-G22／23。
   產出「sha 變動對照表」（舊 sha8 → 新 sha8 → 變動原因），逐條與
   handoff 25／26／V33 之引用比對，變動皆須可歸因；不可歸因者停（§F-2）
2. **R-G23′ 與 R-G25／26／27 入 FO**：R-G23′ 全文自 V33 §裁定記錄 4 轉錄
   入 FO §9.2；R-G25–27 依 §C 落 FO（節位由執行層定，`canon_refs` 全綠
   為準）；§9.2 導覽表同步加列
3. **canon_refs 擴充**（V33 C-2 移交）：`verbatim-ruling-text` 判準擴至
   feature RULINGS 之條文圍籬（``` 區塊）內；R-VF94 該筆 ambiguous 應
   自動歸類，ambiguous 11 → 實測回報（預期 ≤10）。測試：圍籬內不紅、
   圍籬外同型引用紅（G-K）
4. **空白 lint**（IN §11 新段之檢測面）：lint036 新增檢查（取下一個
   未用字母，實測 lint_defs 後定）—— 七欄位逐 cell 逐行掃
   `^[ \t]+`／`^\s+$`／`[ \t]+$`；適用兩層：
   (a) 各 feature `generated/` **現行版** json；
   (b) 已寫回工作簿（openpyxl read_only）。
   產出**量化矩陣**（簿 × 欄位 × 命中數）入 `docs/reports/`，
   G-D：未掃之簿標未掃，不以 0 代。**本包只量化不修語料**；
   寫回組裝碼側：定位引入縮排之組裝點，修之並以字面案例釘入測試
   （json 乾淨 → 寫回 cell 乾淨）
5. **目錄政策落地**：各 feature 建 `delivered/`＋`delivered/MANIFEST.tsv`
   模板；本包僅複製一份定稿 —— `features/power/sandbox/b29/pm_29.xlsx`
   → `features/power/delivered/`，複製後 sha256 實測須為
   `35305835…`（不符即停，§F-4）；其餘 feature 之定稿由各線下次開輪
   自行入列。lint 路徑檢查（R-G25 表）接入，僅對**新檔**判紅
6. **清理首輪**：`scripts/workspace_gc.py`（候選列舉＋引用懸空檢查＋
   輸出專門 commit 清單，**本身不刪檔**）。首輪僅對**已結案 feature**
   （amfm、power_moding、home、media、projection、power 等）列候選；
   `vehicle_setting` 延至 V33 收訖後由 VS 線自跑。候選清單入上繳，
   刪除動作由 Pei 依清單 commit 執行
7. **sources/ 落地**：建 `sources/{raw,extracted}/`＋`MANIFEST.tsv`
   模板＋`scripts/extract_source.py`（xlsx → 逐 sheet tsv；pdf → md；
   輸出帶來源 sha）；`intake.py` 增 sources 讀取路徑（既有 feature
   之舊路徑 fallback 保留，既有測試不得轉紅）。若 Pei 已將 Driver
   Distraction 五檔置入 `sources/raw/`，順跑首次抽取為適用例；未置入
   則僅交付機制，不造例
8. 全套 pytest＋`gate_all.py`；上繳

## E. 預期數字

| # | 指標 | 預期 |
|---|---|---|
| 1 | 前置 git status（§D-0 範圍）| 乾淨（不淨即停）|
| 2 | tsv sha 變動對照表 | 每筆可歸因；不可歸因 **0** |
| 3 | `canon_refs --waiver` | unresolved 0；FAIL 0；ambiguous ≤10（實測回報）|
| 4 | 空白 lint 量化矩陣 | 全簿全欄位有值或標未掃；`vf230` 現行版 json 預期 **0**（分析層抽測為淨；非 0 即回報非停）|
| 5 | 寫回組裝修復測試 | 字面案例：json 乾淨 → cell 乾淨，綠 |
| 6 | `pm_29.xlsx` delivered 複製 | sha256 = `35305835…` 逐位元組一致 |
| 7 | 清理候選清單 | 逐檔列（含引用檢查結果）；本包實刪 **0** |
| 8 | `gate_all.py` | exit 0 |
| 9 | 全套 pytest | 失敗 **8**（既有，不得增減；intake fallback 不得使既有測試轉紅）|
| 10 | 新檔路徑 lint | 本包自身產出全綠 |

## F. 升級條件

1. §D-0 前置不成立
2. tsv sha 變動不可歸因（有未經裁定之條文改動 —— R-G22 之攔截對象）
3. 空白 lint 在**現行版** generated json 發現命中（與分析層抽測矛盾，
   root cause 需重定位）
4. `pm_29.xlsx` 複製後 sha 不符
5. 清理候選之引用懸空檢查發現「被引用但檔已不存在」（既有懸空，非本包
   所致 —— 具名回報，不修）
6. `extract_source.py` 對任一 sheet 抽取後行數／非空儲存格數與
   read_only 實測不符（抽取失真）

## G. 上繳要求

23 包 §G 全項＋R-G13 引用表（R-G5@`9814d24c`、R-G13@`abdc56e3`、
R-G18@`8f61f9fd`、R-G22@`bca29f8f`；本包後 sha 以新 tsv 為準）＋
sha 變動對照表＋空白量化矩陣＋清理候選清單＋sources 模板路徑清單＋
獨立判斷＋**全域線收尾註記**（22–27 之遺留具名總表，含：
whitespace 語料修復待各線、VS 清理待 V33 後、其餘 feature delivered/
待各線、IN 副本 sha 待 Pei 更新）。

## H. 新條文清單（自檢）

- [x] R-G25 目錄政策 — 區塊已列
- [x] R-G26 清理制 — 區塊已列
- [x] R-G27 sources 集中制 — 區塊已列
- [x] R-G23′ 落點（轉錄，非新裁）— §D-2
- [x] 空白規制（已落 IN §11，本包為檢測面）— §D-4

本包引用：R-G3、R-G5、R-G6、R-G9、R-G13、R-G17、R-G18、R-G22、R-G23、
G-D、G-K、G-N、FO §8.6、IN §11、V33 §C、25 上繳、26 包。
