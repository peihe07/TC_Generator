# 01R — 上繳包 01 之覆核（分析層 → 執行層）

覆核對象：`docs/upstream/01_recon.md`。仍屬 `01` 往返，不佔用 `02`。

**結論：受理。** 但 `spec_reference` 之路徑（A-TM12）方向須更正 ——
兩案皆非正解，正解為第三案，見 §3。另新增 A-TM13（實質 spec 缺口）。

---

## 1. 下放包之瑕疵：指令錯誤是分析層的

`01` 包 §5 給的 `python scripts/recon.py time_management` 不可執行。
實測 `recon.py:1090` 之 argparse 為 `--feature`（required），且
`feature_dir = Path(args.root).resolve() / args.feature` 取**相對 root 之
路徑**。正確指令即上繳包所改者：

```bash
python scripts/recon.py --feature features/time_management
```

執行層之修正正確，逕行修正而未升 Tier 2 亦正確（R-TM3 同型）。

**這是分析層連續第二次在指令上出錯**：`00` rev A 根本沒給指令，`01` 給了
未查 argparse 的指令。形態相同 —— **以腳本「應該長什麼樣」代替「實際長
什麼樣」**，與 A-TM09 首版之代理判準、與 §4(4) 之雙空格誤判，同屬一族。

```
R-TM7（分析層自裁，2026-08-20）—— 下放包之指令須經實測

下放包所載之任何指令，其 CLI 介面（參數名、必填性、參數語意）須先讀該
腳本之 argparse 定義後方可寫入，不得依既有印象或他腳本之慣例類推。
無法實測時，寫「指令待執行層依 argparse 確認」，不得寫一條看似可執行
但未經查證之指令。

依據：01 包 §5（recon.py 之 --feature）與 00 包 rev A 之同型缺失。
```

## 2. 已複驗且相符者

分析層對沙箱副本獨立實測（內容解析，非檔案狀態）：

| 項 | 上繳值 | 分析層實測 | |
|---|---|---|---|
| 037 header row | 8 | 第 8 列，`D8 = 'Requirement  Description'`（雙空格） | ✅ |
| Categorization 欄 | col 31 = `AE` | 第 31 欄表頭 `'Categorization'` | ✅ |
| Categorization 分佈 | `{Functional: 22}` | `Counter({'Functional': 22})` | ✅ |
| ASIL / FTTI | ABSENT | 表頭無任何 `ASIL`／`FTTI` 命中 | ✅ |
| 037 形態歸屬 | AM/FM 型（8 / col 31） | 與 FORMS.md 所載相符 | ✅ |
| **48 筆缺口 id 全集** | 48 筆清單 | **逐筆比對：only-mine 0、only-theirs 0** | ✅ |

48 筆清單之逐筆比對為 R-TM4 之首次雙向履行 —— 分析層亦公布自身清單並對差，
非僅要求對造公布。

§4(4) 之雙空格自查（以 `recon.py` 自身之 `norm()` 重驗，而非自製比對）
定性正確：驗證他人規則須用該規則自身之比對函式。若當時逕報首次結果，
會誤報一個不存在的 §6 升級條件。此條與 R-TM7 同族，一併記入。

§3.1 之 openpyxl 禁令三重證據（複本 SHA 不變、zip members 48、母本 SHA
不變）形式正確 —— 特別是 zip members 48 這一項，正是 FORMS.md 所述
「損壞是選擇性的」之唯一可靠判別點。

## 3. A-TM12 —— **兩案皆非正解**；正解為第三案

上繳包提之兩案：(a) `recon.py` 增 spec_mode D 路徑自 CFTS docx 解析章節；
(b) 改 `spec_reference_template`。

**(a) 不可行，且其不可行之理由比「工具缺路徑」更根本。**

`survey_a03()` 之 citation 欄尋找為
`find("hmi source")` → `find("source", forbid=("description", "requirement id"))`。
本件 037 之來源欄表頭為 `Source System Requirement ID`，含 `requirement id`
故被 forbid 排除 —— **`citation column: NOT FOUND` 不是解析失敗，是本 037
根本不含文件章節引用**。它引用的是 SYS-RA 需求 id，不是 spec 章節。

因此，縱使把 CFTS docx 解析成一份完整的章節索引，**仍然沒有任何欄位能把
leaf 接到章節上**。(a) 建的是索引的一端，缺的是連結本身。

**(b) 為時過早** —— 在確認 `{outline}` 真的接不上之前就改掉 template，
等於放棄可追溯性。

### 3.1 第三案：經由 SYS2 之 Source Requirement items 欄建錨鏈

錨鏈為（與 Project 既有之 SWE.1→SWE.6 錨鏈形態一致）：

```
SWE-RA-TIME&DATE-nnn  →  SYS-RA-TIME&DATE-nnn  →  CFTS 物件 id  →  CFTS 章節號
   （037 第 2 欄）          （SYS2 第 2 欄）        （SYS2 第 5 欄）    （docx 標題 {id}）
```

**分析層已實測其可行性**（量測條件全列）：

| 步 | 量測 | 結果 |
|---|---|---|
| SYS2 第 5 欄 `SYS2 來源需求項目ID  Source Requirement items` | 227 列逐列取值，計非空者 | **227 / 227，零空白** |
| 78 筆被引用之 SYS-RA id 是否皆有來源物件 id | 逐筆查表 | **缺 0 筆** |
| CFTS 章節標題 → 物件 id | 標題正則 `^(\d+(?:\.\d+)*)\s+.*\{(\d+)\}$` | 88 個標題 |
| 物件 id → 所屬章節 | 標題 + 物件行 `^\*\*(\d{7})\s*:` 之歸屬 | **358 個物件** |
| 78 筆之章節可達性 | 逐筆解析 | **71 筆直接可達；7 筆見下** |
| 可達之相異章節數 | 去重 | **21 節** |

7 筆未直接可達者，分兩類：

- **5 筆為多物件儲存格**（如 `139 → '4814088\n,4814089'`、
  `154 → '4814113,\n4814114,\n4814115,\n4814116'`）—— 以逗號／換行切分後
  即全數可達，屬解析細節，非缺口
- **2 筆為真缺口** —— 見 §4 之 A-TM13

**重要限制**：以上章節解析跑在 **Project 附件之轉換文字副本**上，
非 `inputs/` 之原始 docx。依 spec_mode D 之基線紀律（沙箱轉換 Markdown
不得視為權威），**執行層須對 `inputs/` 之原始 docx 重跑並回報數字**；
若與上表不符，以原始 docx 為準並回報差異。上表僅證明「路徑存在且量級合理」，
不作為基線。

### 3.2 對 A-TM12 之處置意見（提請 Pei）

- `spec_reference_template` **暫不改**
- `recon.py` 之修法不是「增 docx 章節解析」，而是「增一條 leaf→章節之
  間接解析路徑（經 SYS2 來源物件 id）」。跨 feature，Tier 2
- 本 feature 可先以獨立腳本產出 `data/leaf_to_section.tsv`，
  不動 `recon.py` —— 此路線不需 Tier 2，Phase 4 亦不必等腳本修法

## 4. A-TM13（新登記）—— 2 筆被引用之需求，其來源物件不在 CFTS 基線內

實測：

| SYS-RA id | 來源物件 id | 於 CFTS docx 之出現次數 |
|---|---|---|
| `SYS-RA-TIME&DATE-221` | `6151328` | **0** |
| `SYS-RA-TIME&DATE-224` | `6151331` | **0** |

全檔搜尋 `615\d{4}` 形態之物件 id：**零命中**。CFTS015 全篇之物件 id 皆為
`481xxxx` 區段，`615xxxx` 為另一區段。

兩者之 SYS2 描述（節錄，非全文）：221 為 `$GPS_Presence$ = [Absent]` 時之
內部時鐘精度；224 為 `$GPS_Presence$ = [Present]` 時之個人化設定。
兩者分別被 `SWE-RA-TIME&DATE-005`（Internal Clock Accuracy）與
`SWE-RA-TIME&DATE-002`（GPS Sync Enable/Disable Logic）引用。

**性質**：這不是解析缺陷，是**基線缺口** —— SYS2 引用了現行 CFTS 版本
（SR26 20250909-1851）所不含之物件。可能為 SYS2 較新、CFTS 較舊，或物件
遷自他份 CFTS。**Tier 2**，且屬 RD-1 候選；與 A-TM02a（037 版本身分）
同屬「上游版本對齊」一族，宜併問。

**對 TC 之立即影響**：005 與 002 兩個 leaf 之 `specification_reference`
在該兩筆上無章節可寫。**不得以鄰近章節填充**（§8.4.1 禁止捏造來源未述之值）。

## 5. 其餘覆核意見

- **§4(6) 之「無項可解析 ≠ 項解析失敗」定性正確**，§6 升級條件確實未觸發。
  已核對 `run_assertions()`：outline 檢查僅在 `a03res["distinct_sections"]`
  非空時才 assert，本件為空故不觸發 —— 工具行為與其陳述一致。
- **§8.3 之 `write_back.author_value` / `tc_ref_id_value` 未驗**：定性正確，
  且「本 feature 內部無法驗證」之判斷正確（BLANK 無既有 author 可比對）。
  處置：於 framework 階段對照他 feature 慣例確認，不必現在裁。
- **assertions 未宣告**：本 feature `recon_assertions` 為空，故
  `spec_reference_template` 等值不受任何機械檢查保護。**建議於 Phase 3
  宣告至少三項**：leaf 數 = 22、Categorization 分佈 = `{Functional: 22}`、
  表頭格數 = 33。此為 Tier 2，隨 framework 一併裁。
- **索引 12 條**（預期 11 + A-TM12）正確；本包再加 A-TM13 → **13 條**。
- **§7 對 §3 之知悉確認**四點皆準確複述，無誤讀。

## 6. 呈報 Pei

**命名決定宜一次裁完（三項綁在一起）**：

| 項 | 現況 | 選項 |
|---|---|---|
| R-TM2 `test_group` | `"Time Management"` [PROVISIONAL] | 母本 BLANK，無既有值可覆寫，推翻條件永不觸發 → 須實裁 |
| A-TM11 母本 `D5` Scope | 空 | `Time-Management-HMI-V0.1` / `Time-and-Date-HMI-V0.1` |
| 跨 feature 樣式參照 | 未裁 | 是否准以 Home done region 為樣式參照（canon §0 Tier 2 boundary case）|

前兩項為同一組別名取捨（feature 名 vs spec 標題），第三項獨立但同屬
Phase 3 前置。**三項不裁，framework 無法起草。**

另待裁：A-TM12 之修法路線（§3.2）、A-TM13 之上游對齊（併 A-TM02a 入 RD-1）。

## 7. 執行層下一步

1. 登記 A-TM13，索引更新為 13 條
2. **對 `inputs/` 之原始 docx** 重跑 §3.1 之錨鏈量測，回報六項數字
   （227/227、缺 0 筆、88 標題、358 物件、71+7、21 節），與本包對差
3. 5 筆多物件儲存格之切分後可達性，逐筆列出（R-TM4）
4. 回一份極短上繳，不重述 01 包

`02`（framework）待 §6 三項命名裁定後下放。

## 8. 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM7 | 分析層自裁（下放包指令須經實測） | ✅ §1 |
| A-TM13 | anomaly，PENDING，Tier 2 + RD-1 候選 | ✅ §4 |
| A-TM12 方向更正（第三案：SYS2 來源物件 id 錨鏈） | 覆核意見，處置待 Pei | ✅ §3 |

分析層本包未動 git、未改腳本、未改執行層產出之任何檔案。
§3.1 與 §4 之量測跑在沙箱轉換副本上，已於文內標明其非基線地位。
