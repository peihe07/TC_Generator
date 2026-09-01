# 下放包 02 — vsm_v42：R-VL10／R-VL11 落地，W-0 重跑，W-1′～W-6 續行

日期：2026-09-01
取號：`docs/handoff/` 實測有 00、01，取 02
對象：執行層。00 包禁區、§三、§六 E1–E16、§七、§八；01 包 §三 W-1′～W-6 之作業定義**續有效**；本包只載差異。
**前提：Pei 已將 `docs/fw036/RULINGS.sha.tsv` 入庫**（W-0 首步仍實測 `git status --short`，非乾淨即停，不覆寫）。

---

## 一、上繳 01 之覆核

| 項 | 判 |
|---|---|
| 停於 W-0，不覆寫台帳；E19–E22 唯讀預檢先行提出 | **對**。台帳 M 為 Pei 側未入庫，非本線 |
| E17 14 vs 17 | 分析層之誤（A-VL4(a)）→ **R-VL10(b)** 改性質判準 |
| E18 R-VL2 sha8 不同而 body_sha8 相同 | 分析層之誤（A-VL4(b)）→ **R-VL10(a)** 改比 body_sha8 |
| E20 逐欄實測（先驗 6/6 相符；模板值三處錯、sheet 名不存在） | 核實；採為 W-2 先驗（R-VL11(b)） |
| inputs/ 清空次序（第 10 節 4） | → **R-VL11(a)** |
| `estimated_test_time` 是否納入 | → **R-VL11(b)**：納，並納 `tc_id`（F） |
| E23「無數」≠「0」 | 對。本包 E23 判準補「未跑 W-5 記無數」 |
| 上繳 00 `§9` 自造 canon_refs 紅已自改 | 核實 |
| `new_feature.py` skeleton 裸 `§3`、模板欄位值錯 | 共用腳本，併入 Pei 之「共用腳本一裁」（§四） |
| A-VL3 不成對 DR | 裁可 |
| 三支存量紅（canon_refs 501→503、gates_tsv、lint_paths） | 與本線無關，核實 |

## 二、裁決引用

R-VL10／R-VL11 全文在 `RULINGS.md`。本包 sha8 一律報 **`body_sha8`**（R-VL10(a)）；`sha8` 併列為觀測值。
R-VL1–R-VL9 之 body_sha8 須與上繳 00 §9／上繳 01 第 9 節逐字相同。

## 三、作業清單

**W-0 台帳重生（R-VL9，判準改 R-VL10(b)）**
`git status --short docs/fw036/RULINGS.sha.tsv` 乾淨 → `python3 scripts/rulings_hash.py` 寫入。diff 判：
新增列之 `ruling_id` **全數** ∈ {`R-VL*`, `R-VT*`}；修改 0；刪除 0。條數（R-VL 11、R-VT 當下實測）列為觀測值。
不符即停。

**W-1′ feature.yaml**（01 包 W-1′ ＋ R-VL11(c)）：刪 `tc_id_prefix`；`write_back.tc_id_format: "NR1L-VSM42-{n:03d}"`；`done_region.author_value: null`；`spec_reference_template: null`（註「待 P3」）。

**W-2**（01 包 W-2 ＋ R-VL8／R-VL11）：
- 先 sandbox/base：cp 母本、cmp、sha（E19）；`workbook.sheet`＝副本實測分頁名、`header_row 9`、`columns` 逐欄自 r9 回填，含 `tc_id` F、`estimated_test_time` Q（先驗＝上繳 01 第 7 節之逐欄表，仍逐欄重測上繳）。
- inputs/ → `sources/raw/<doc_id>/` 以 `mv`；逐檔 sha 前後全等；MANIFEST **手工附加**（`--refresh-manifest` 會重寫全檔並抹掉既有 version／features／note，vsm_v43 上繳 01 §3.2 已實測，不得用）；三者皆過後確認 inputs/ 為 0 項。
- 037 兩份與 SYSAD：vsm_v43 已落 `sources/raw/vf665_037_parksense`／`vf665_037_sdw`／`vf665_sysad_sys3`（sha `be55d897…`／`c98909e2…`／`469162b8…`）。本線 inputs/ 之同名三檔 sha 比對，相同 → **不重落**，MANIFEST 該三列 `features` 欄已含 `vsm_v42`（實測確認），inputs/ 之三檔逕刪（sha 全等已證）；不同 → 停。
- `extract_source.py` 對 #1 docx 不支援（A-VT7）、對 SYSRA 之 §F-6 誤報型（A-VT8）為已知：docx 依 R-G27 自 raw 直讀 `word/document.xml`；SYSRA 若同樣觸 §F-6 則記其儲存格座標、不改腳本、計數自 raw 直讀。
- R-G28：#1 docx zip members 與 `word/media/` 清點。

**W-3 recon**：`recon.py`（本線 a03_report 有值，可跑）；`sheet` 名不符即 `:431` exit，故 W-2 之 sheet 回填為前提。

**W-4 leaf 母體**：依 00 包；DR-VL1 實數回填。

**W-5 訊號解析預查**（01 包 W-5 ＋ vsm_v43 上繳 01 §十-1／§十-2 之教訓，先於本線施作）：
- 抽名：CAN 形／內部形／PROXI 形三式之外，**PROXI 與 `.Req` 另自 docx 表格結構抽**（`<w:tbl>` 逐列），不只認「X PROXI parameter」句式。
- 段 1 逐字比對之外，**施作 R-P368(b) 之擴充比對**：對 LID `Logical Identifier`／`Description` 欄容許前綴／後綴／底線差異，每一擴充命中另欄記比對依據（哪一欄、哪一列、差異為何）。
- 結果標籤：段 1 擴充比對未做者不得記「查無」，記「未解得(止於段1)」；「查無(R-G13)」只在三要件皆滿足且已登 `forms/LOOKUP_MISSES.md` 時用。
- 段 3 命中之 `SG_` 所屬 `BO_` 與規格訊息名不符者（vsm_v43 之型態一／二）**不記 B-1**，記「訊息名不符(R-13)」，保留規格原名（R-VT9 同判，本線比照）；B-1 僅限 R-VT6(c)／R-VL6(c) 字面（多命中解至不同標的）；兩本 DBC 各解一處者先查 LID `CAN` 欄之匯流排，LID 有載即取該本，無載才列 §K。
- E23 判準：未跑 W-5 記「無數」，不得記 0。

**W-6**：A-VL1 轉 RESOLVED（原檔到齊，上繳 01 第 2 節）；A-VL3 於 W-0 過後轉 RESOLVED；三項候選 anomaly 於 E5／E9／E10 實測後 live 取號登記。

## 四、待 Pei（不阻塞本包，除 W-0 前提）

**共用腳本一裁**（五項同源，一次裁）：
1. `recon.py` 對 `a03_report`／`workbook` null 加 None guard（A-VT3）
2. `extract_source.py` 支援 `.docx`（A-VT7）
3. `extract_source.py` §F-6 判空兩側一致（A-VT8）
4. `new_feature.py` skeleton 裸 `§3` → `FEATURE_ONBOARDING.md §3`；`workbook.columns`／`sheet` 模板值改全 null 附「須自 r9 實測」註
5. `extract_source.py --refresh-manifest` 重寫全檔抹既有 metadata → 改為只補缺列

分析層建議：**准**，條件：pytest 過；對任一既有 feature 改前後輸出 diff = 0；登全域線（`docs/fw036/` A 或 R-G 加註）。裁前執行層一律不改 `scripts/`。

## 五、預期數字

| # | 項 | 判準 |
|---|---|---|
| E17′ | W-0 diff | 新增列 ruling_id 全 ∈ {R-VL*, R-VT*}；修改 0；刪除 0。條數為觀測值 |
| E18′ | R-VL1–R-VL9 body_sha8 | 與上繳 00 §9／01 第 9 節逐字相同（sha8 觀測值併列） |
| E19–E22 | 同 01 包 | E19 副本端須 cmp 全等 |
| E23′ | B-1 衝突列 | 0（R-VL6(c) 字面）；「訊息名不符(R-13)」列數為觀測值；未跑記無數 |
| E24 | inputs/ 於 W-2 後 | 0 項 |
| E25 | MANIFEST 含 `vsm_v42` 之列 | 5（spec_r6、v42_sysra 新增 2；037×2、sysad 既有 3 之 features 欄含 vsm_v42） |
| E1–E16 | 00 包 | 本包首測，逐項附量測條件（欄、判式、分母） |

## 六、上繳要求（`docs/upstream/02_sources_recon.md`）

00 包 §七全部；W-0 diff 摘要；W-1′ 四鍵實值；columns 逐欄實測 vs 先驗；E1–E25 逐項；W-5 之抽名數（三式＋表格）、七檔命中、擴充比對命中與依據、結果分布、§K（空亦列並註「未查」或「查無衝突」）；A／DR 清單；R-VL10／R-VL11 body_sha8；獨立判斷；gate_all 輸出。

## 七、升級條件

W-0 台帳非乾淨或 diff 不符 E17′；E18′ 任一不同；E19 不全等；E22 非 OOXML；W-2 三檔 sha 與 vsm_v43 已落者不同；E23′ B-1 ≥ 1（停該部分列 §K，其餘續）。

## 八、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中約 190 列無 037 覆蓋（W-4 後回填實數） | no | 已登記，未送出 |
