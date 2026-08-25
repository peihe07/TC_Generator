# 上繳包 13 —— 三處宣稱補測、綁定收束（**停止條件 34 觸發**）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/13_honest_guards.md`
- 結果：**步驟 1、2、4、5、6 完成；步驟 3 觸發停止條件 34，已停於待裁**
- 全部 git 操作屬 Pei —— §7 只備妥訊息與 pathspec，未執行

---

## 0. 先講兩件

1. **停止條件 34 觸發**：R-DM39 之 10 項比對中，1 項不符、
   另 1 項之**映射根本不成立**（上輪之偽陽性）。未擇一、未調和。
2. **上輪之「10 項 recon 有測」須更正為 8 項**（A-DM29）。
   其分類以**子字串比對**判斷「recon 有沒有測這個」，
   而子字串會在無關句子裡命中 —— 與 R-DM13 所禁之 bag-of-words 同型，
   只是這次我用它來判斷**兩個概念是不是同一個**。

---

## 1. §四三條之抄錄核對表（步驟 1，腳本產出）

## 抄錄核對表 — 13_honest_guards.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 40 | R-DM38 | `features/display/RULINGS.md` | 646 | `638ce8409e56613d` | 是 |
| 41 | R-DM39 | `features/display/RULINGS.md` | 581 | `153f7cebef5e7d06` | 是 |
| — | R-G25 | `docs/fw036/RULINGS_LEDGER.md` | 447 | `dc9a4256970d342f` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **41** 個，與各下放包原檔逐字元比對 **全數相符**（41 vs 41）。

---

## 2. R-G25 之三處補測（步驟 2）

R-G25 要求二事：(a) 連跑兩次，第二次仍應出現同一訊息；
(b) 被宣稱不會被動之標的其內容逐字未變。

### 2.1 補測 A —— `verify_reference_binding.py` 之「不更新宣告值」

蓄意將 `lid` 之宣告值改為 `cafebabe…`：

| 項 | 第 1 次 | 第 2 次 |
|---|---|---|
| MISMATCH 行 | 出現（宣告 `cafebabe0000…` / 實際 `a01e1679c706…`） | **出現，逐字相同** |
| `Do NOT update the declared value` | 出現 | **出現** |
| 退出碼 | 1 | **1** |

**(b) `feature.yaml` 逐字未變 ✓**（`cmp -s` 比對執行前後）。

### 2.2 補測 B-1 —— `intake.py` 覆寫之「sha256 不符 → 不套用並警示」

以 SYS2 之 xlsx 冒名頂替 037 之檔名：

| 項 | 第 1 次 | 第 2 次 |
|---|---|---|
| WARNING（含兩側雜湊） | 出現 | **出現，逐字相同** |
| 分類結果 | `polarion_export`（signature 結果保留） | **同** |

**(b) `feature.yaml` 逐字未變 ✓；該 xlsx 逐字未變 ✓**。

### 2.3 補測 B-2 —— `intake.py` 覆寫之「缺 sha256 → 不套用並警示」

移除宣告中之 `sha256` 一行：

| 項 | 第 1 次 | 第 2 次 |
|---|---|---|
| WARNING `has no sha256 — NOT applied (R-DM24(a))` | 出現 | **出現，逐字相同** |
| 分類結果 | `spec_xlsx`（即 R-DM5(a) 之預期偏差） | **同** |

**(b) `feature.yaml` 逐字未變 ✓**。

### 2.4 三處皆通過；`intake.py` 一行未改

全部狀態已還原並複驗（037 回到
`a03_report [kind_source: override]`，綁定 9/9）。
**停止條件 33 未觸發。**

`scripts/intake.py` 為共用腳本，本項為測試不是修改 —— `git status`
對該檔無異動。

---

## 3. R-DM39 之 10 項逐項比對（步驟 3）—— **停止條件 34 觸發**

### 3.1 比對表

| # | 項 | `recon.py` 之值 | 自測之值 | 判定 |
|---|---|---|---|---|
| 1 | Missing referenced specs | `outline_misses=[]`；cited-NOT-in-export **0** | **CFTS_009**（`{CFTS009-722}`）→ DR-DM1 | **不符 —— 見 §3.2** |
| 2 | Header row index | **不報此值** | r9 | **映射不成立 —— 見 §3.3** |
| 3 | `feature.yaml` column conflicts | `col_conflicts=[]`；`(none)` | none | **相符** |
| 4 | Regen-region segments | `segments=[]` | 全表（r10 起） | **相符**（空 segment ⇒ 全表為 regen） |
| 5 | Draft-region disposition | `draft_reqs=[]`；`done rows: 0 / draft rows: 0` | 不適用（無 draft 列） | **相符** |
| 6 | Categorization 欄與分布 | 欄 **F**；`{'Functional Requirement': 8}` | 第 6 欄 = F；同分布 | **相符** |
| 7 | Covered by done region | `done_reqs=[]`；covered **0** | 0 | **相符** |
| 8 | Parent/child both-leaf duplications | `parent_child_dupes=[]` | 無 | **相符** |
| 9 | Priority rubric deviations | `compliance_notes=[]`；`(none)` | 不適用（無 done region） | **相符** |
| 10 | Authors present | `authors={}`；`author_used=None`；`(none)` | 無 | **相符** |

**8 項相符、1 項不符、1 項映射不成立。**

### 3.2 第 1 項之不符 —— 兩側量的是不同的量

| | 定義 | 值 |
|---|---|---|
| recon | leaf 所引之 **outline 章節**不在受裁匯出中者 | `[]`，0 |
| 自測 | CFTS_020 **本文**以 `{CFTSnnn-mmm}` 引用之**外部文件** | CFTS_009（→ DR-DM1）、CFTS_013（→ DR-DM4），另 6 份未評估 |

兩者皆存在，皆非計算錯誤，**但不是同一個量**。

且須記明：**recon 之 0 是空的 0** —— 本 feature 之 `citation column:
NOT FOUND`、`sections: 0`（上繳 09 §4 第 15 項），故「所引章節不在匯出中」
者必然為 0。依 canon §5a，不可能失敗之檢查不應被讀成 PASS。

**未擇一、未調和**（停止條件 34：不得逕以任一方為準）。
請裁示此項應如何登記 —— 兩個量都要留、留哪一個為 `DECISIONS.md` 之
「Missing referenced specs」，或改名以區分。

### 3.3 第 2 項之映射不成立 —— 上輪之偽陽性

上輪判「`Header row index`：recon 有測」，依據是我以子字串 `"header"`
掃 `RECON.md` 得命中。**實際命中的是**：

```
column mapping: 15 fields resolved from header text
```

以確切詞組 `"header row"` 重掃 `RECON.md` 與 `recon.json`：**0 命中**。
**recon 不報表頭列號。**

### 3.4 A-DM27 之更正

上輪之「10 項 recon 有測 / 7 項自測獨有」更正為：

| 判定 | 項數 |
|---|---|
| recon 有測**且量同一件事** | **8** |
| recon 有同名概念但**量不同的東西** | **1**（`Missing referenced specs`） |
| 自測獨有 | **8**（原 7 + `Header row index`） |

**「停止條件 30 未觸發」之結論仍成立**（無 recon 漏測），
但其依據中有兩項是錯的映射而非正確的判定。

以 **A-DM29** 登記，並記其成因：我在判斷「兩個概念是不是同一個」時
**用了非逐字之方法**（子字串），而那正是 R-DM13 對 bag-of-words 之
禁令所針對的思路，只是換了一個對象。

---

## 4. `verify_reference_binding.py` 九項輸出（步驟 4，R-DM38）

```
# reference binding check (R-G23)
feature.yaml: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml
entries: 9

| key | file | declared | actual | verdict |
|---|---|---|---|---|
| a03_report | `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | `ab3198e81fb21d21…` | `ab3198e81fb21d21…` | MATCH |
| cfts_doc | `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` | `8696d1f596e33677…` | `8696d1f596e33677…` | MATCH |
| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |
| dbc_fd | `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71…` | `2a86c4bf3e670d71…` | MATCH |
| lid | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` | `a01e1679c706cd45…` | MATCH |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | `e7c2020f01c3d58d…` | MATCH |
| sys2_export | `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` | `421c8eef3f5cb01a…` | `421c8eef3f5cb01a…` | MATCH |
| sys3_sysad | `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | `be9c97af0211a703…` | `be9c97af0211a703…` | MATCH |
| workbook_master | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc…` | `6372fb6be02f48dc…` | MATCH |

**9 of 9 match.**
```

**9/9 相符。停止條件 35 未觸發。**

`feature.yaml` 之該節加註 `paths:` 與 `reference:` 之分工：

```
paths:      記「檔在哪」（供腳本開檔）
reference:  記「檔是哪一份」（供 verify_reference_binding.py 比對）
同一個檔出現在兩節不是重複，是兩個不同的問題。
```

### 4.1 一項自查出之缺陷（A-DM30）—— 綠燈檢查了錯的東西

首次插入時，四個新鍵**落在檔案末段，成了 `lint:` 之子鍵**。

- **YAML 解析無誤、無任何警告**
- `verify_reference_binding.py` 照常輸出 **`5 of 5 match.`**
- 即：一個通過的檢查，**檢查的卻不是我以為的東西**

發現方式：以 `yaml.safe_load` 印出 `reference` 與 `lint` 之鍵清單。
修正後 `reference` 9 鍵、`lint` 回復其原有 3 鍵，輸出 **9/9**。

> 這與 A-DM28 同族而不同型：A-DM28 是**訊息說謊**，
> 本條是**對象錯了而結果仍是綠的**。
>
> `entries: N` 那一行是唯一能察覺此錯的線索（5 vs 9）。
> 引用綁定結果時應連同該行，**不得只引「N of N match」** ——
> 「5 of 5」與「9 of 9」都是全綠。

---

## 5. subprocess 成本量測（步驟 5，量測不優化）

各三次取中位數：

| 腳本 | 總耗時（含守衛） | 守衛佔比 |
|---|---|---|
| `signal_resolution.py` | 0.50 s | 7.8% |
| `dbc_probe.py` | **0.08 s** | **46.4%** |
| `proxi_candidates.py` | 4.49 s | 0.9% |
| `lid_version_diff.py` | 0.66 s | 5.9% |

守衛本身（`verify_reference_binding.py`）中位數 **0.04 s** ——
一次 Python 啟動 ＋ 9 個檔之 sha256（合計約 6.6 MB）。

**判定：現況可接受，不優化。** 絕對成本 0.04 s，對最慢之
`proxi_candidates.py` 為 0.9%。

**惟須記明其形狀**：對 `dbc_probe.py` 這種本身只需 0.04 s 之腳本，
守衛**幾乎等於把執行時間加倍**。若日後有逐 leaf 迴圈呼叫這些腳本
（8 leaf × 4 支 = 32 次），守衛之累計為約 1.3 s ——
仍可接受，但**成本隨呼叫次數線性成長，而非隨資料量**。
本數字即為日後比較之基準。

---

## 6. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 4 項。**

1. **§3.2 之不符未裁**，`DECISIONS.md` 之 `Missing referenced specs`
   一項目前記的是自測值（CFTS_009），而管線之同名概念記 0。
   **兩個量並存於同一個名字之下**，這狀態不宜久留。
2. **A-DM29 之成因未一般化。** 我提了「判斷兩份產出是否在講同一件事
   須以確切詞組或欄位鍵比對」，但**沒有把本 feature 既有之其他映射
   回頭檢一遍** —— 上繳 09 §4 之 17 項交叉檢查同樣是我手動對應的，
   其中是否另有偽陽性，未查。
3. **`reference:` 九項之外仍有未綁者。** `forms/FORMS.md` 與
   `forms/LOOKUP_MISSES.md` 是 tracked 之台帳，其內容變動不會使既有
   產出失效（它們是記錄而非輸入），故未納入 —— 但**這個判斷是我做的，
   未經裁示**。R-DM38 之判準是「變了以後我們的東西還對不對」，
   而台帳變了確實不影響數字。
4. **守衛之 0.04 s 未含最壞情況。** 量測時九個檔皆在本機且已被作業
   系統快取；**首次冷讀（6.6 MB）之成本未量**。

另記本輪**已驗而下放包未要求**者：A-DM30 之 YAML 巢狀錯置
（連同其「綠燈檢查錯對象」之性質）；`Header row index` 之偽陽性追查；
`entries: N` 作為唯一線索之觀察。

---

## 7. 建議之 commit 訊息與 pathspec（**未執行**）

```
test(display): honest-guard retests, binding scope, two self-caught flaws

- R-DM38/39 + R-G25 verbatim (3/3, 41/41 cumulative)
- R-G25 applied to the three existing claims: the binding check and both
  intake.py override branches. Each run twice, same message both times,
  and the thing each claims not to touch is byte-identical afterwards.
  intake.py itself is unchanged
- STOP CONDITION 34: of the ten items R-DM39 asked me to compare, eight
  agree, one disagrees and one mapping does not hold. Missing referenced
  specs measures different quantities on the two sides - recon counts
  cited outline sections absent from the export (vacuously 0 here, since
  there is no citation column), mine counts external CFTS documents the
  body cites. Neither was adopted
- A-DM29: last round's 'recon measures this' classification used
  substring matching, and 'header' matched 'from header text'. recon does
  not report a header row index. The 10/7 split is corrected to 8/1/8.
  The conclusion that nothing was a recon miss still holds, but two of
  its supporting mappings were wrong
- A-DM30: the four new reference: keys first landed under lint:. YAML
  parsed cleanly and the check reported '5 of 5 match' - a green check
  looking at the wrong thing. Fixed; now 9 of 9. The 'entries: N' line is
  the only thing that distinguishes the two
- inputs/ material joins reference: per R-DM38, with paths: vs
  reference: documented as 'where the file is' vs 'which file it is'
- guard cost measured, not optimised: 0.04s median, 0.9% of the slowest
  script and 46% of the fastest
```

pathspec：

```
git add docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/feature.yaml \
        features/display/docs/
```

**`DECISIONS.md` 不在其中** —— §3.2 之不符未裁，本輪未改該檔。
共用 `scripts/`、`forms/`、`.gitignore` 未動；`data/` 本輪無變更。
