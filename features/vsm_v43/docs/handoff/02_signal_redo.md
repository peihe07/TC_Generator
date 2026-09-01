# 下放包 02 — vsm_v43：R-VT9／R-VT10 落地，§K 收斂，W-5′ 重做，P3 前置

日期：2026-09-01
取號：`docs/handoff/` 實測有 00、01，取 02
對象：執行層。00 包禁區、01 包 W 定義**續有效**；本包只載差異。本線仍止於 P0–P3（R-VT4）。
前提：vsm_v42 02 包之 W-0（台帳重生）**不為本包前提** —— sha8 取樹外 `--out`（R-VT10(a) 裁可），台帳到位後於下一包改自台帳讀。

---

## 一、上繳 01 之覆核

| 項 | 判 |
|---|---|
| W-1′～W-6 全數執行；五件 sha 搬移前後全等；037／SYSAD 三方全等不另建 doc_id；MANIFEST 手工附加不用 `--refresh-manifest` | **核實**，處置皆對 |
| 停 1（E10 R-VT2 sha8 異、body_sha8 同） | 分析層之誤（A-VT14(a)）→ **R-VT10(a)**：比 body_sha8，停 1 解除 |
| 停 2（E15 B-1 = 29） | 值域漏列 R-13（A-VT14 另記）→ **R-VT9**：型態一 22 ＋型態二 6 = 28 列改「訊息名不符(R-13)」，保留規格原名，DR-VT3 已登記；型態三 1 列先查 LID `CAN` 欄。停 2 解除 |
| E2 判準字面（A-VT10）／E9 = 4（A-VT11） | 分析層之誤 → **R-VT10(b)**，兩條 RESOLVED，以上繳 01 實測為基線 |
| A-VT13 台帳無 R-VT 列 | 樹外量測裁可；台帳由 vsm_v42 02 包 W-0 重生 |
| A-VT9 Melco ID 全空 | 併 DR-VT2（已加佐證） |
| 「查無(R-G13)」102 列偏嚴、PROXI 只抽 2 名（§十-1／-2） | 執行層自報正確 → **R-VT10(c)(d)**，本包 W-5′ 重做 |
| WMF 內嵌圖 | → R-VT10(e)，P3 待辦 |
| A-VT7／A-VT8 共用腳本 | 併 Pei「共用腳本一裁」（§四） |
| `Out of scope` 二拼法不另開 A | 裁可（DR-VT2 涵蓋） |
| 三支存量紅 | 與本線無關，核實 |

## 二、裁決引用

R-VT9／R-VT10 全文在 `RULINGS.md`；DR-VT3 在 `DATA_REQUESTS.md`。本包 sha8 一律報 **body_sha8**，sha8 併列觀測值。

## 三、作業清單

**W-5′ 訊號解析重做（R-VT9／R-VT10(c)(d)）** —— 本包主體
1. 抽名：三式之外，自 docx `<w:tbl>` 逐列抽 PROXI 參數名與 `.Req`／`.Info` 名（表格第一欄或含 `PROXI`／`parameter` 之列）；新增名併入，181 為下界。
2. 段 1：逐字比對之外施作 R-P368(b) 擴充比對 —— 對 LID 全分頁之 `Logical Identifier`／`Description` 欄，容許前後綴／底線差異（規則明寫：去 `MESSAGE.` 前綴、去 `_Req`／`_Sts`／`_Info` 後綴、底線↔空白、大小寫不敏感）；每一擴充命中另欄記「檔/分頁/r{列}c{欄}/規則」。七檔命中數重報。
3. 結果值域（取代 01 包）：`解得 | 未解得(止於段1) | 未解得(止於段2) | 訊息名不符(R-13) | B-1 衝突 | UI路徑(R-P375b) | PROXI路徑(R-P375b/c) | 查無(R-G13)`。「查無(R-G13)」只在段 1 擴充比對已做、段 3 實查、且登 `forms/LOOKUP_MISSES.md` 三者皆滿足時用。
4. 型態三 `BRAKE1.VehicleSpeedVSOSig`：讀 LID 命中列之 `CAN` 欄，載明匯流排則取該 DBC、另一本記旁證，結果記「解得」；未載才列 §K。
5. 現有 `data/signal_chain_v43.tsv` 不覆寫，另存 `signal_chain_v43_v2.tsv`，附兩版結果分布對照。
6. V42↔V43 差集：仍只讀 `features/vsm_v42/data/signal_chain_v42.tsv`；不存在則記「待 vsm_v42」。

**W-6**：A-VT10／A-VT11 轉 RESOLVED（R-VT10(b)）；A-VT12 轉 RESOLVED（R-VT9，DR-VT3）；A-VT13 於台帳到位後轉。

**P3 前置（不鎖、不寫 profile）**：
- `RECON.md` §7 未決表更新（B-1 → 依 R-VT9 重分類；E9 基線 56）。
- 自 `data/sysra_v43_functional.tsv` 分母 295 列取 `chapter_for_vf` 前二階分布（供 Layer 2 對照，非依據）。
- `word/media/image1.wmf` 轉 png 放 `data/`，一句話記其內容（R-VT10(e)）。

## 四、待 Pei

1. **共用腳本一裁**（與 vsm_v42 02 包 §四同一份，五項：recon.py null guard／extract_source .docx／§F-6 判空／new_feature.py 裸 §3 與模板 null／--refresh-manifest 抹 metadata）。建議准，條件同。
2. **DR-VT1／VT2／VT3 三項併送**。VT1 之「差異列」舉證待 vsm_v42 W-5；不必等，送時說明。

## 五、預期數字

| # | 項 | 判準 |
|---|---|---|
| E10′ | R-VT1–R-VT8 body_sha8 | 與上繳 00 §七／01 §五逐字相同 |
| E15′ | B-1 衝突列 | 0；「訊息名不符(R-13)」為觀測值（上繳 01 對應 28） |
| E16 | 段 1 擴充比對後「未解得(止於段1)」 | < 102（觀測值；≥ 102 即擴充比對無效，回報規則） |
| E17 | 型態三處置 | LID `CAN` 欄有載 → 解得；無載 → §K 1 列 |
| E18 | 表格抽取後 PROXI 名 | > 2（觀測值） |
| E9′ | Verification Method 非空相異值（Functional 507，正規化） | 56 |

## 六、上繳要求（`docs/upstream/02_signal_redo.md`）

W-5′ 六項逐項；兩版結果分布對照；擴充比對規則與每筆依據；§K（空亦列並註）；P3 前置三項；A／DR 清單；R-VT9／R-VT10 body_sha8；獨立判斷；gate_all 輸出與歸因。

## 七、升級條件

E10′ 任一不同；E15′ ≥ 1；擴充比對規則需超出第 2 項所列（新規則不得自創，回報）；任何試圖以 SYSRA 建母體。

## 八、未結 DR 清單

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 建議送出 |
| DR-VT2 | SYSRA DocID `VF655`／R3 vs R4／Melco ID 全空／二拼法 | no | 未送出 |
| DR-VT3 | 規格訊息名與 forms/ DBC 不符 28 列 | no | 建議送出 |
