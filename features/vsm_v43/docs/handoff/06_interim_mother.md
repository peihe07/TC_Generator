# 下放包 06 — vsm_v43：R-VT18 暫代母體建檔、Layer 2 暫代材料

日期：2026-09-02
取號：`docs/handoff/` 實測有 00–05，取 06
對象：執行層。00–05 包續有效（**R-VT4「止於 P0–P3」與 R-VT17(b) 掛起已由 R-VT18 解除**）。
sha8 報 body_sha8；台帳不重生；DR 之發送屬 Pei（DR-VT1 已裁送出，執行層不代發）。
**本包只建母體與框架材料，不生成任何 TC**（Layer 2 待 Pei 裁後方有 P4 生成包）。

---

## 零、禁區（00 包 §零之第 5 條改寫）

原「不以 SYSRA 建母體」由 R-VT18(b) 取代：**得且僅得**以 SYSRA 295 列（乾淨分母）建暫代母體；
`VF655` 171 列與 DocID 空 41 列仍不得入（隔離待 DR-VT2）。TC 生成仍禁（待 Layer 2 裁）。
其餘禁區不變。

## 一、作業清單

**W-1 暫代母體建檔**：`data/leaves_interim.tsv` —— 自 `data/sysra_v43_functional.tsv`（分母 295）逐列取：
`Sys-RA-Feature-ID`／標題（SYSRA 之需求標題欄，欄名實測回報）／`chapter_for_vf` 完整值／`Description` 有無訊號名（∩ v5 事實表之計數）／`tc_status = interim_leaf`。
另出兩張隔離清單：`data/isolated_vf655.tsv`（171 列）、`data/isolated_nodocid.tsv`（41 列），各帶同欄位，標 `ISOLATED (DR-VT2)`。

**W-2 Layer 2 暫代材料**（分析層據以出草案，執行層不聚類、不命名）：
- `chapter_for_vf` **完整值**分組：每組列數、章節路徑；
- 每組抽 **3 個標題例**（首、中、末列，逐字）；
- 標題詞頻前 30（正規化小寫、去停用詞 the/of/and/for/to/is/in）；
- 295 列 ∩ v5「解得」訊號之分組分布（P4 可執行度預估）。
落 `data/layer2_material_v43.md`。

**W-3 框架加註**：`framework.md` Layer 2 節依 R-VT18(e) 加註（原「留白為裁決結果」保留，下加「2026-09-02 R-VT18 改走 SYSRA 暫代線，草案待分析層／Pei」）；不填任何 Test Set。

**W-4 DECISIONS 加註**：P3 節之母體列「0，待 037」下加「R-VT18：暫代母體 295（SYSRA），重錨條款生效」；Sign-off 不動（已簽）。

## 二、預期數字

| # | 項 | 判準 |
|---|---|---|
| E37 | `leaves_interim.tsv` 列數 | **295** |
| E38 | 兩隔離清單 | 171／41；三檔合計 507 |
| E39 | `chapter_for_vf` 完整值組數 | 觀測（前二階應仍為 01.11×223／01.14×67／01.13×5 之細分） |
| E40 | 295 列中描述含 v5「解得」訊號者 | 觀測值（P4 可執行度） |
| E41 | R-VT18 body_sha8 | 與 RULINGS.md 現檔一致 |

## 三、上繳要求（`docs/upstream/06_interim_mother.md`）

W-1～W-4；E37–E41；標題欄名實測；A／DR 狀態；獨立判斷；gate_all 歸因。

## 四、升級條件

E37 ≠ 295 或 E38 三檔合計 ≠ 507（分母漂移即停）；任何聚類命名出現於執行層產出（材料歸執行層、草案歸分析層）。

## 五、未結 DR

DR-VT1（**Pei 裁送出，待發**）／DR-VT2（建議併送）／DR-VT3（暫持）／DR-VT4（先不送；P4 內部訊號 PENDING 錨）。
