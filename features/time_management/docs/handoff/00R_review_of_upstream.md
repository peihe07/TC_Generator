# 00R — 下放包 00 之上繳覆核（分析層 → 執行層）

覆核對象：`features/time_management/docs/upstream/00_intake_scaffold.md`
仍屬 `00` 往返，不佔用 `01`。

**結論：受理，但 A-TM09 之數字更正，且補登 A-TM10。**
在 A-TM09 更正落檔前，其 59.5% / 51 不得被任何下游引用。

---

## 1. 已獨立複驗且相符者

- §3 三處手動修正：`feature.yaml` 實測 `feature: "Time Management"`、
  `test_group: "Time Management"  # [PROVISIONAL] 見 R-TM2`，`ANOMALIES.md`
  marker 為 `A-TMnn`。相符。
- A-TM06 檔名：對 repo 實測 `features/time_management/inputs/` 得
  `SWE1_Secure_Date&Time.xlsx`，確認含 `&`。不改檔名、下游 `shlex.quote()`
  之處置採納。R-TM1 不動之判讀正確 —— 別名字面差異不影響定名裁定。
- A-TM08：表頭字面為 `SYS2 EE Architecture (All,ATL-Hi,ATL-Mi)`，實測值集
  `{ATL-Hi, All, ATL-Mid, Atl-Hi}`，`ATL-Mi` 零命中。成立。
- A-TM03 重測相符（227 / 101-61-55-10 / 126-70-30-1）。
- A-TM02 之兩層拆分（版本問題 vs 內容缺口）判讀正確，採納。

---

## 2. A-TM09 —— 數字更正：**78 / 48**，非 75 / 51

分析層獨立重算（量測條件全列如下，供反驗）：

- 來源：`Analysis Report` 分頁第 9 列起、第 1 欄非空者，共 22 列
- 展開：第 2 欄字串，先將 U+2013 / U+2014 正規化為 `-`，以
  `(\d{3})\s*-\s*(\d{3})` 抓範圍並展開為閉區間，抽掉範圍字串後再抓剩餘
  `\d{3}`，聯集去重
- 對照：`Basic Report` 第 2 列起 227 列，第 2 欄尾碼三位數 → 第 10 欄
  `Category`；227 筆 id 解析成功、無重號

結果：

```
037 引用之相異 SYS-RA id      78
其中 Category = FR           78   （Heading / Information 命中 0）
懸空引用（SYS2 無此 id）       0
SYS2 FR 總數                126
FR 未被任何 SWE leaf 引用     48
78 + 48 = 126
覆蓋率 78/126 = 61.9%
```

**人工逐列點數交叉驗證**（非抽樣，22 列全列舉，用以排除正則失誤）：

```
001:4  002:6  003:3  004:4  005:2  006:3  007:4  008:7
009:9  （029–033 為 5 筆 + 046,047,080,081）
010:2  011:3  012:2  013:1  014:3
015:6  （076–077 為 2 筆 + 083–085 為 3 筆 + 154）
016:2  017:4  018:3  019:3  020:4  021:1  022:2
合計 78，且 22 列之間無重號（故相異數亦為 78）
```

差額 3 筆落在範圍展開。上繳包未公布其展開後之 id 清單，僅給計數，
故確切成因無法從上繳包判定 —— **執行層須於下一包公布其 75 筆之完整 id
清單，與本節 78 筆逐筆對差**，不得只回報修正後的計數。

### 2.1 兩項推論本身不成立（比數字更重要）

**(a)「75 筆全部命中 FR，故該啟發式只會高估，59.5% 是上界」——
方向性搞反了。**「全部命中 FR」證明的是**零偽陽性**，而零偽陽性與**低估**
完全相容；本例即是低估。真值 61.9% > 59.5%，「上界」之主張被自身證據推翻。
零偽陽性只能支持「引用集是真集之子集」，那推出的是**下界**。

**(b)「75 + 51 = 126 恰好等於 FR 總數」不是檢查，是恆等式。** 未覆蓋數
既定義為 `126 − 引用命中數`，則兩者相加必然為 126，無論引用集對錯。
78 + 48 = 126 同樣成立。此式對解析正確性之鑑別力為零。

以上屬 canon §5a「代理判準（自資料推導之統計範圍）不得凌駕實質判準」之
同型失誤。實質判準是逐筆對照，本包 §2 之人工點數即是。登記於此，
因該形態會重演。

### 2.2 實質結論不變

48 筆 FR 無 SWE leaf 對應，缺口性質與量級不因 3 筆之差而改變：

- **覆蓋稽核分母不得取 22**（SWE leaf 數）。取 22 會得出「已全覆蓋」之假象。
- A-TM02 之兩層必須分開裁：縱使 Pei 裁定手上這件即權威 037，48 筆內容
  缺口依然存在。
- 分母之正確取法本身屬 Tier 2，於 A-TM02 裁定時一併裁。

**執行層須以 78 / 48 / 61.9% 覆寫 `ANOMALIES.md` A-TM09 全文，並在該條
內保留本次更正之經過**（不是抹掉舊數字換新數字 —— 更正經過本身是稽核軌跡）。

---

## 3. A-TM10（新登記）—— `spec_pdf` 仍為佔位符，CFTS docx 未進 `feature.yaml`

實測 `feature.yaml`：

```yaml
spec_pdf: "inputs/<spec pdf>"            # null if spec_mode E
```

而 `inputs/` 內確有
`R1LR_Atl-H_25PI3.5_Cabin_CFTS _015 Time and Date _SR26_20250909-1851.docx`。

成因：`intake.py` 之 `KIND_TO_YAML` 無 `cfts_doc` 鍵 ——

```python
KIND_TO_YAML = {
    "workbook": "workbook", "swra_report": "a03_report",
    "polarion_export": "sys1_export", "spec_pdf": "spec_pdf",
    "popup_list": "popup_list",
}
```

故 `cfts_doc` 之檔案被移入 `inputs/` 但**不會回填任何 yaml 路徑**，且不報錯。
`spec_mode = D` 正是以這份 docx 為 spec 來源，Phase 4 會在此處找不到 spec。

同型先例：`features/vehicle_setting/feature.yaml` 之 `spec_pdf` 指向一份
`.docx`，該值是手填的，非腳本產出。

**處置**：填 `spec_pdf: "inputs/R1LR_Atl-H_25PI3.5_Cabin_CFTS _015 Time and
Date _SR26_20250909-1851.docx"`。此為既有先例之機械套用，Tier 1，逕行補填，
不必等裁。腳本本身之修法（`KIND_TO_YAML` 加 `cfts_doc`）跨 feature，Tier 2，
不得逕改。

**本條屬 §7(6) 應盤到而未盤到者。** 上繳包之「未驗項」列了 036 缺件導致的
4 項與範圍外 2 項，但 `spec_pdf` 是**已在 inputs/、可立即驗、且本包範圍內**
的欄位。盤點時之全集應為 `feature.yaml` 全部 path 鍵，逐鍵確認其值是否仍為
佔位符 —— 該全集本包未使用。

---

## 4. 未驗項之覆核

上繳包所列 7 項（036 缺件 4 + 範圍外 2 + 判定為無 1）覆核如下：

- 036 缺件之 4 項（14 欄、header_row、sheet 名、done_region.author_value）
  —— 成立。援引 `vehicle_setting` 位移先例（design_method Q→R、author Z→AA）
  作為「不得引為基線」之理由，正確。
- 「037 leaf 無缺號」判定為無，依據為列 9–30 第 1 欄全集列舉得 001–022 連續
  —— 分析層獨立確認 22 列、`SWE-RA-TIME&DATE-001…-022`，成立。**這是本包
  唯一一項有交代全集依據的「無」，形式正確。**
- 遺漏者見 §3。

---

## 5. 執行層下一步（本包不開 01）

1. 以 78 / 48 / 61.9% 更正 A-TM09，附更正經過與 75 筆之完整 id 清單對差
2. 補填 `spec_pdf`，登記 A-TM10
3. 更新 `ANOMALIES.md` 索引表為 10 條
4. 以上完成後回一份極短之上繳（僅差異，不重述全包）

`01`（recon 範圍）待 Pei 裁 A-TM02 之兩層分拆、以及 036 是否取得後再下放。

---

## 6. 呈報 Pei（非執行層事項）

- **A-TM09 更正後之 48 筆缺口**：分母裁定請與 A-TM02 一併下。
- **git 狀態異常**：上繳包報 `features/vehicle_setting/docs/handoff/
  02_coverage_baseline_correction.md` 現為單獨 untracked，而 session 起始時
  整個 `features/vehicle_setting/` 為 untracked。**全部 git 操作屬 Pei，
  分析層與執行層皆未動，亦不查。** 若非你在別視窗操作，請確認。

---

## 7. 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| A-TM09 更正（78 / 48 / 61.9%） | 數字更正 + 論證缺陷登記 | ✅ §2 |
| A-TM10 | anomaly，PENDING，補填屬 Tier 1、修法屬 Tier 2 | ✅ §3 |

分析層本包未動 git、未動 `_intake/`、未改任何腳本、未改執行層產出之任何檔案。
