# 01Z — 命名與樣式三裁（`01` 往返結案）

分析層。R-TM8 / R-TM9 / R-TM10 依 Pei 2026-08-20 之指示「裁吧」授權裁定，
內容由分析層擬定，效力等同 Pei 裁定。執行層須逐字寫入 `RULINGS.md`
並於 `DECISIONS.md` 建條目引用。

---

## R-TM8 —— workbook `test_group` 值

```
R-TM8（Pei 授權分析層裁定，2026-08-20）—— test_group = "Time and Date"

workbook Test Group 欄（G）之值定為 "Time and Date"。
feature.yaml `test_group` 由 [PROVISIONAL] "Time Management" 改為
"Time and Date"，並移除 [PROVISIONAL] 標記。

理由：
1. R-TM2 之推翻條件（工作簿既有非空值優先）在 BLANK 下永不觸發，
   故落回 canon §4.1.1 之通則：Test Group 等同 spec 文件標題。
   本 feature 之 spec 文件標題為 CFTS_015 Time and Date。
2. 交付件之讀者為客戶。客戶側之三個識別（spec 標題、req id family
   TIME&DATE、CFTS 編號 015）全部指向 "Time and Date"。
3. "Time Management" 不出現於任何上游文件，僅為 Pei 之內部稱謂。
   採之等於在交付件中新增第四個名稱。

R-TM1 不受影響：feature 名與目錄 slug 維持 "Time Management" /
`time_management`。R-TM1 已言「別名不進路徑」；本條為其反向 ——
路徑名亦不必進工作簿。內部識別與交付識別本即兩層。
```

## R-TM9 —— 母本 Scope 欄（`D5`）之值

```
R-TM9（Pei 授權分析層裁定，2026-08-20）—— Scope 欄值

D5 之 feature 識別段定為 "Time-and-Date-HMI-V0.1"，與 R-TM8 一致。

前綴段不在本條裁定範圍：分析層本次無法對 Home v2 交付件實測，
故不得書寫其字面（§8.4.1，不得捏造來源未述之值）。

執行層須：
1. 開啟 features/home/output/…_Home_20260720.xlsx（FORMS.md 記載其
   SHA256 為 cfc007f3…、tag fw036-home-regen-v2），實測其 D5 全字串
2. 以該字串之前綴段 + 本條之 "Time-and-Date-HMI-V0.1" 組成本 feature 之
   D5 值，回報組成前後之兩個字串
3. 若該檔不存在或 D5 為空，停止並回報，不得自行擬前綴

禁止來源：archive/forms_superseded/…_SWQT_Home_20260809.xlsx。
FORMS.md 之 provenance warning 已載明該複本之 D5 為未修正之
"…AppDrawer-Projection-SWE1HMI-V0.1"（A-H26 缺陷本身）。

A-TM11 於上列三步完成並回報後轉 RESOLVED。
```

## R-TM10 —— 跨 feature 樣式參照

```
R-TM10（Pei 授權分析層裁定，2026-08-20）—— 准以 Home 為樣式參照，三重限縮

准。canon §0 之 cross-feature exemplar admissibility 於本 feature 成立，
但受下列三項限縮，缺一即不得援引：

(a) 來源唯一且須實測
    僅 features/home/output/…_Home_20260720.xlsx
    （tag fw036-home-regen-v2，FORMS.md 載 SHA256 cfc007f3…）。
    援引前須實測該檔之 SHA256 並與 FORMS.md 記載比對，記錄於上繳包。

    明文禁止 archive/forms_superseded/…_SWQT_Home_20260809.xlsx。
    依 FORMS.md provenance warning，該複本相對 Home v2 有四項編輯污染：
    D5 Scope 未修正、F 欄 216 列全填 tc_id、G 欄 216 列全填 "CoreHMI"、
    K 欄 216 列全填 "NA"、Z 欄 author 為 "ArifChen" 而非 "Arif"。
    以其為樣式來源會把 K 欄全 NA 與 G 欄 CoreHMI 一併帶入。

(b) 只及於樣式，不及於內容體系
    可援引：步驟措辭與動詞選用、ER 句式、標點與空白慣例、
            UI 標籤引號慣例、baseline 比對之寫法。
    不得援引：spec_reference 格式（Home 為 spec_mode A 之
            文件名_章節；本 feature 之章節經 SYS2 來源物件 id 錨鏈取得，
            兩者來源不同）、test_group / test_set 值、priority 分佈、
            tc_id 體系、Input Test Data 之填法。

(c) 樣式參照不是證據仲裁者
    canon §1.1 第三層在本 feature 依然不存在，本條不回復之。
    Home 樣式為「可援引之先例」，非「爭議之裁決依據」。
    - pilot 發現不得以「Home 這樣寫」為由駁回
    - 亦不得以「Home 沒這樣寫」為由逕定為 defect
    爭議一律回到條文（§4–§12）與本 feature 之 profile。

連帶：因第三層缺席，pilot review 之發現分類（canon §1.2 之
defect / style-divergence / note）少了 done-region check 這一道過濾，
分類結果直接成立。reviewer 之發現門檻因此相對較低，
pilot 之爭議應預期多於 Home 與 AMFM。
```

---

## 執行層本包待辦

1. 三條裁決逐字寫入 `RULINGS.md`，`DECISIONS.md` 建條目引用
2. `feature.yaml` 之 `test_group` 改 `"Time and Date"`，移除 `[PROVISIONAL]`
   註記（R-TM8）
3. R-TM9 之三步實測與回報；完成後 A-TM11 轉 RESOLVED
4. R-TM10(a) 之 Home v2 SHA256 實測比對
5. 01R §7 之未竟事項：A-TM13 登記（索引 → 13 條）、原始 docx 之錨鏈六項
   數字重跑、5 筆多物件儲存格切分後之逐筆可達性
6. 極短上繳，僅差異

`02`（framework Part N 起草）於本包上繳並覆核後下放。

## 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM8 | 裁決（Pei 授權），test_group = "Time and Date" | ✅ |
| R-TM9 | 裁決（Pei 授權），Scope 值；前綴段留實測 | ✅ |
| R-TM10 | 裁決（Pei 授權），樣式參照准予但三重限縮 | ✅ |

分析層本包未動 git、未改腳本、未改任何既有檔案。
R-TM9 / R-TM10 所引之 `features/home/output/` 路徑，本次因 MCP 逾時
**未能實測其存在**，僅依 FORMS.md 之記載引用 —— 故兩條均以「執行層須實測」
為前置，未書寫任何未經量測之字面值。
