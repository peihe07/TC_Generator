# REVISIONS — Vehicle Category

已交付之下放包／上繳包，其原文**一律不改**（R-TM13：不刪除，加註保留）。
事後查明之錯誤與修訂記於本檔，以裁決條文為據。
讀舊包時須先讀本檔 —— 舊包之數字未必仍然有效。

---

## REV-01 —— 下放包 01 §3.3「第 10–18 欄全為 `\xa0`」作廢

- **修訂依據**：R-VC6（下放包 02 §二）
- **原文**：037 `Analysis Report` 第 10–18 欄全 145 列皆為 `\xa0`，無內容。
- **正解**：該九欄於 **117 個 leaf 皆有實質內容**，於 28 個「有子之父」
  為 `\xa0`；欄 16／17 之該 28 列中另有 3 列為 `None`
  （VC-034 / VC-052 / VC-063）。
- **成因**：分析層之全稱斷言未經全表掃描 —— 起草時之量測程式只取索引
  `0, 1, 3, 5, 6, 7, 8` 七欄，索引 `9`–`17` 未被讀取過一次。
- **連帶**：A-VC1 撤銷。九欄改為**有效上游輸入**，並生 R-VC6(a)–(d) 四項拘束。
- **軌跡**：`docs/upstream/01_intake_recon.md` §3 之比對表第 23 項判 `≠`
  即此事之攔截點；同包 §9 為當時之後記。

## REV-02 —— 下放包 01 §3.1 規格 PDF 之位元組數

- **修訂依據**：R-VC7（下放包 02 §二）
- **原文**：規格 PDF 為 3,552,260 B。
- **正解**：該為分析層 Project 附件之**衍生物**
  （SHA256 `216cfa84…3275a455`）。**repo `inputs/` 之複本為權威**：
  2,828,253 B，SHA256 `3a6752c8…12776a76`（全機 7 份複本一致）。
- **連帶**：A-VC7 RESOLVED；衍生物不得作為任何判準之來源。

## REV-03 —— 下放包 01 §五 T9「reference 七項」

- **修訂依據**：R-VC10（下放包 02 §二）
- **原文**：`reference:` 須綁定七項。
- **正解**：**六項**（三份素材 + 036 母本 + Pop Up List + HMI Settings List）。
  「七項」為分析層計數錯誤，**本無第七項**。
- **連帶**：明文排除 `dbc_b` / `dbc_fd` / `lid` / `proxi` 四項，
  理由已寫入 `feature.yaml` 註解。

## REV-04 —— 下放包 01 §五 T1「forms/ 兩份不複製，僅綁定」作廢

- **修訂依據**：R-VC10（下放包 02 §二）
- **正解**：素材一律複製入 `inputs/`，`paths:` 以本 feature 目錄為基準。
  執行層當時留 `null` 為正確之保守處置。

## REV-05 —— 下放包 01 §八 `recon_assertions` 四鍵

- **修訂依據**：R-VC9（下放包 02 §二）
- **原文**：宣告 `leaf_count: 117`、`functional_requirement_count: 145`、
  `distinct_spec_sections: 66`、`uncovered_content_sections: 18`。
- **正解**：`leaf_count` 與 `uncovered_content_sections` **刪除** ——
  `recon.py` 之 `run_assertions()` 無其實作，宣告不生效。
  留 `functional_requirement_count` 與 `distinct_spec_sections`。
- **連帶**：117 與 18 之守護改由 T4／T12 之集合相等重測承擔，
  並負 R-VC9 之逐包揭露義務。A-VC8 記其工具面缺口。

## REV-06 —— 下放包 01 §4.2 之分類計數（24 ＋ 18 → 25 ＋ 17）

- **修訂依據**：R-VC12 一（下放包 03 §二）
- **原文**：未引用 42 節 ＝ 非需求性質 **24** 節 ＋ 有實質內容 **18** 節。
- **正解**：未引用 42 節 ＝ 非需求性質 **25** 節 ＋ 有實質內容 **17** 節。
- **異動之單一節**：**§16.1 由 (b) 改列 (a)**。其 SYS1 `Description` 為
  「Refer to the Vehicle Category - Cabrio Rooftop and Cabrio Wind Draught
  Deflector HMI sections for complete logic.」—— 交叉引用，非該節自身之
  實質需求內容。
- **連帶**：**R-VC3 之「表 B｜覆蓋落差揭露」母體由 18 節改為 17 節**：
  8.1, 8.2, 8.3, 8.4, 8.5, 9.1, 9.2, 10.1, 10.2,
  11.9, 11.9.1, 11.9.2, 11.9.3, 14.2, 15, 16.2.1, 16.2.2
  R-VC3 之其餘部分（117 leaf 全取、表 A、兩表為出貨門檻）**不變**。
- **42 之總數不變** —— 本次只動 (a)／(b) 之切分，未動未引用章節之集合。

## REV-07 —— 下放包 01 §4.2(b) 之摘要文字，三節作廢

- **修訂依據**：R-VC12 二（下放包 03 §二）
- **作廢者**：
  - §15 —— 「PU0132…PU0275 之訊息文字與逾時」
  - §10.1／10.2 —— 「Type / Power Source / Last State 之四種組合、
    Last State 之可用條件（Latching + Ignition）」
- **理由**：該等文字係讀 Project 附件之衍生 PDF 所得（R-VC7 所禁）；
  repo 權威素材（SYS1 `Description`、repo PDF 文字層）皆不載之，
  其內容僅存於 `(image: imageNN.png)` 佔位之後。
- **補正**：§8.3 為**摘要漏列**而非錯誤，表 B 補入
  「A graphic representation of the vehicle status will be present on pop up」
  （來源：SYS1 `Description`）。
- **其餘 13 節**之摘要經 T17 驗為「與 SYS1 所載相符」，保留 ——
  惟其效力僅及於「與 SYS1 相符」，**非「與規格原件相符」**
  （FO §3 Mode A 之盲點）。
- **連帶**：DR-VC6 新立；表 B 該三節之「內容」欄一律書
  「該節內容僅存於圖，SYS1 匯出未帶文字」。

## REV-08 —— 下放包 01 §五 T5「16 列」之口徑

- **修訂依據**：`docs/upstream/01_intake_recon.md` §1 T5（執行層實測，未經另裁）
- **原文**：`SWE1-HMI-VC-057` ~ `-064`（含子，**16 列**）。
- **正解**：該 id 區間共 **22 列**。「16」對應的是 `FROP = Power Management`
  之子集（章節 13.1 / 13.1.1 / 13.2 / 13.3 / 13.4 / 13.5），
  與下放包 01 §4.4 逐項相符；其餘 6 列（`-062`、`-063` 及其子，
  章節 13.4.1 / 13.4.2）之 `FROP = Vehicle Settings`。
- **性質**：二者不矛盾，是同一段落的兩個口徑；記於此以免日後誤讀。

---

## 通則（R-VC12 三）

分析層日後對任何規格內容之摘要，其來源須為 repo `inputs/` 之權威複本；
以 Project 附件、衍生 PDF、OCR 或圖之視覺判讀所得者，
一律不得以實測值之格式寫入下放包。
如確需引用圖內內容，須標為「圖內內容，未經文字層確認」並登記 DR。
