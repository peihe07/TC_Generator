# RULINGS — Time Management (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Time Management 之裁決權威；
跨 feature 條文承接時註明來源包。

來源包：`docs/handoff/00_intake_scaffold.md`（rev B, 2026-08-20）§1。

---

## R-TM1（Pei, 2026-08-20）—— feature 定名

```
R-TM1（Pei, 2026-08-20）—— feature 定名

feature 目錄 slug = `time_management`
feature.yaml `feature` = "Time Management"

素材四種名稱並存：
  - Pei 指定之 feature 名 = "Time Management"（本條採用）
  - spec 文件標題        = "CFTS_015 Time and Date"
  - SWRA 檔名            = "SWE1_Secure_DateTime"
  - 需求 ID family       = "TIME&DATE"（SYS-RA-TIME&DATE-* / SWE-RA-TIME&DATE-*）

「Time and Date」「Secure DateTime」「TIME&DATE」均為別名，不進目錄路徑。
ID family 之字面值當然照原樣使用於 req_id 欄與 traceability。

slug 一律小寫加底線，不得含空格 —— 依據 A-TM01 / A-TM04（見 §5）。
```

**執行層回報（2026-08-20）**：已套用。`features/time_management/` 建成，
無空格孿生目錄（下放包 §3 步驟 5 驗證通過）。`feature.yaml` 之 `feature:`
已由腳本產出值 `"Time_Management"` 手動改為 `"Time Management"`。

**執行層回報 —— 本條所列 SWRA 檔名與實測不符**：本條記為
`SWE1_Secure_DateTime`，repo 內實際檔名為 `SWE1_Secure_Date&Time.xlsx`
（含 `&`）。屬別名之字面差異，不影響本條之裁定內容（該名本就不進目錄路徑），
但該字面值已寫入 `feature.yaml` 之 `a03_report:`，其 `&` 之下游風險登記為
A-TM06。

---

## R-TM2（Pei, 2026-08-20）—— test_group 暫定值與其推翻條件

```
R-TM2（Pei, 2026-08-20）—— test_group 暫定值與其推翻條件

feature.yaml `test_group` 暫定 = "Time Management"。

本值為 [PROVISIONAL]，非最終。推翻條件（recon 時自動判定，Tier 0）：
  若 036 工作簿之 Test Group 欄（G 欄，實測為準）已存在非空值，
  則以工作簿實測值為準，直接覆寫本欄，不需再問。

理由：canon §4.1.1 之通則為 Test Group 等同 spec 文件標題（本例即
"Time and Date"），與 R-TM1 之 feature 名不同。工作簿既有值優先於兩者，
因為那是客戶已接受之欄位內容。三者若三不相同，於 Phase 2 升 Tier 2。
```

**執行層回報（2026-08-20）**：已套用，`feature.yaml` `test_group:` =
`"Time Management"`，行內註記 `# [PROVISIONAL] 見 R-TM2`。

**推翻條件目前無法判定**：036 工作簿缺件（見 DATA_REQUESTS #1 / A-TM07），
故 G 欄實測值不存在，本值維持 [PROVISIONAL]。036 落地後於 recon 自動判定。

---

## R-TM3（分析層自裁，2026-08-20）—— CLI 參數字面值與 anomaly 縮寫

```
R-TM3（分析層自裁，2026-08-20）—— CLI 參數字面值與 anomaly 縮寫

1. `intake.py` / `new_feature.py` 之 feature 參數一律使用 `Time_Management`
   （底線，非空格）。理由見 A-TM04：兩支腳本之目錄名推導為
   `feature.lower()`，無 slugify，空格會原樣進路徑。
2. 因 (1)，scaffold 產生之 `feature.yaml` 之 `feature:` 值會是
   `"Time_Management"`，與 R-TM1 不符 —— 執行層須於 scaffold 後手動改為
   `"Time Management"`（見 §3 步驟 5）。
3. anomaly 縮寫固定為 **TM**，不用腳本推導之 `TI`
   （`abbr = feature[:2].upper()`）。理由：本包已以 A-TM01…A-TM05 落檔，
   縮寫換寫會使既有編號失效。同一形態之先例：`home` 用 `A-H`、
   `user_profiles` 用 `A-UP`，皆非腳本推導值。

本條屬「量測與作業之技術性選擇」，分析層自裁範圍；其判準與風險已於本節揭露。
```

**執行層回報（2026-08-20）**：三項全數套用。

1. 兩支腳本均以 `Time_Management` 呼叫，未產生空格目錄。
2. `feature.yaml` 之 `feature:` 已手動改正（見 R-TM1 回報）。
3. 縮寫已由腳本產出之 `A-TInn` 改為 `A-TMnn`，改動點三處：
   `ANOMALIES.md` L4、L14，`PLAYBOOK.md` L97。改後全庫 `grep "A-TI"`
   無殘留。
