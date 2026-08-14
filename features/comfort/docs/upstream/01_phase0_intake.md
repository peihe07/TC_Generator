# 上繳包 01 — Comfort 開案 Phase 0 → Phase 1

執行層 → 分析層。2026-08-14。回應 `docs/handoff/01_phase0_intake.md` §5
與 `docs/handoff/02_rulings_addendum.md`。

**結論：六項作業全部完成，三個 assertion 全部 PASS，無 open PENDING，
Phase 2 可進場。** 下放包 §2 之數字經獨立重測全部復現。

---

## 0. 一句話狀態

| 項目 | 值 | 依據 |
|---|---|---|
| workbook_state | `BLANK` | recon 實測（done 0 列 / draft 2 列，皆為範本樣本） |
| spec_mode | `A` | recon 實測 SYS1 export 齊備；intake 獨立提案亦為 A |
| leaves | **403** | assertion PASS |
| 相異 spec section | **129** | assertion PASS |
| outline map miss | **0**（129/129） | assertion PASS |
| open PENDING | **無** | P-C1／P-C2 已由 R-C6／R-C7 關列 |
| 新登記 anomaly | A-CF01 ~ A-CF07 | §4 |

---

## 1. §5.1 建立 feature 骨架

`scripts/new_feature.py Comfort --adopt-existing --root .`

**下放包指定用 `new_feature.py`，但該腳本原本會拒絕**：
`if feat_dir.exists(): sys.exit("refusing to scaffold")`。而
`features/comfort/docs/handoff/` 已由分析層先行寫入，目錄存在。

**處置（改腳本，不繞過腳本）**：新增 `--adopt-existing` 旗標 —— 補齊缺項、
**逐檔檢查存在性、絕不覆寫**。繞過腳本手工建檔會讓骨架與其他 feature 悄悄
分歧；而讓 scaffold 覆寫既有檔，會在「分析層先下放 handoff」這個必然重演的
情境裡毀掉裁決的唯一副本。兩個都不能接受，所以改的是腳本的能力，不是它的
安全性。實測輸出保留 `kept existing (not overwritten): …` 一行。

**同時補齊腳本缺項**：下放包 §5.1 要求產出七個檔，但 `new_feature.py` 原本
只產五個 —— **`RULINGS.md` 與 `DATA_REQUESTS.md` 從來不由它建立**。這是
AMFM／Projection「裁決只存在於聊天記錄」缺口（見其 `docs/INDEX.md`）的
結構成因之一：檔案不存在，就沒有地方提醒任何人去寫。兩份 skeleton 已加入
腳本，對所有後續 feature 生效。

產出（`docs/handoff/` 二檔完好未動）：

```
features/comfort/
  .gitignore  ANOMALIES.md  DATA_REQUESTS.md  DECISIONS.md
  PLAYBOOK.md  RECON.md  RULINGS.md  RUNBOOK.md  feature.yaml
  batches/ data/ docs/ generated/ inputs/ scripts/
```

## 2. §5.2 素材落位

| 素材 | 位置 | 實測 |
|---|---|---|
| 037 | `inputs/`（intake 搬入） | 143,292 bytes，SHA256 `a8186089a28c9a31…` |
| 036 空白範本 | `inputs/`（自 `forms/` 複製） | rev C，SHA256 `cd876c202c71e74b…`（與 Privacy 同一份） |
| SR24 SYS1 export | `spec-index/cache/`（**未搬移**） | 70,040 bytes，SHA256 `6982d37db81b36e4…` |
| SR24 JSON | `spec-index/cache/` | 11,088,177 bytes |
| SR24 PDF | `spec-index/sources/` | 6,462,311 bytes，SHA256 `fc5d3cd1d524f4d5…` |

三份 SR24 素材依 §5.2 留在 `spec-index/`，`feature.yaml` 以
`../../spec-index/…` 相對路徑回指，`resolve_glob()` 實測可解。

**路徑寫全名而非萬用字元，是 R-C1 的結構性落實**：同目錄有 SR25 CR29359，
一個 `SYS1_HMI_Comfort_*` 會同時命中兩份基線。寫全名讓「取到 SR25」不可能
發生，而不是靠命名運氣或紀律。

## 3. §5.3 recon —— 三個 assertion，PASS/失敗 + 實測值

下放包要求「以通過/失敗 + 實測值形式輸出，不是只印計數」。已實作為
`recon.py` 之 `Assertions` 類別；期望值置於 `feature.yaml`
`recon_assertions`（Comfort 之裁決常數，非 pipeline 常數），未宣告
assertion 之 feature 行為完全不變。

```
- PASS — leaf count == Functional Requirement rows: expected 403, measured 403
  — categorization distribution: {'Functional Requirement': 403, 'Heading': 95};
    the banned id-suffix criterion would have selected 369
    (34 parent-shaped requirements dropped)
- PASS — distinct spec sections after citation parse: expected 129, measured 129
  — 57 citation cells carry extra lines below the section
    (Polarion item ids), not parsed
- PASS — citation stem is the ruled baseline, and only that:
    expected ['SYS1_…_SR24_Post_3A_CR24879_(September_25_2023)'],
    measured ['SYS1_…_SR24_Post_3A_CR24879_(September_25_2023)']
- PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0
  — 129 cited / 180 outline entries in the export
```

第三條為執行層自行加設，非下放包要求：R-C1 說「stem 一律 SR24」，但只查
「SR24 有沒有出現」無法排除「**同時**還引用了別的」。故查的是相異 stem 集合
恰等於 `[SR24]`，不是 SR24 是否在其中。

**assertion 是真正的閘，不是裝飾** —— 反向驗證：把期望值改為 402 重跑，
腳本輸出 `FAIL`、**不寫 `DECISIONS.md`**、以非零碼離開；`RECON.md` 與
`recon.json` 仍寫出（它們是證據）。另測 `sys1_export` 為 null 之情形：
「無基線可查」本身即記為 FAIL，不會因為沒有東西可比對而靜默通過。

### outline map

對 SR24 export 之 `Basic Report` 建立，180 個 outline number、**無重複**
（重複會讓查表不成為函數，此情形為硬中止，非軟性回報）。129 個 cited
section **逐一查得，miss = 0**。map 落於 `data/spec_id_to_outline.tsv`
（403 列 + 表頭，追蹤入版控 —— 它一有 diff 就代表 spec export 在腳下動了）。

**未曾以「SR25 有」代替**：`paths.sys1_export` 只指向 SR24，SR25 未被載入
任何一次。

### 章節分布 —— 與下放包 §2 之數字為不同母體，特此對齊

下放包 §2 末之分布 `2(113)、16(115)、…、6(1)` 合計 **498**，即**全部資料列**
（含 95 列 Heading）。recon 之 `leaves by chapter` 只計 403 列 Functional
Requirement：

```
2(92)、3(14)、6(1)、7(38)、9(8)、10(15)、11(37)、12(22)、13(14)、
14(40)、15(2)、16(99)、17(18)、18(3)                         合計 403
distinct sections by chapter：2(22)、3(4)、…、18(1)          合計 129
```

三個數（498 / 403 / 129）皆正確，母體不同，**不得互推**。同理，R-C4 條文之
「92 列具多行形態」係對 498 列計；限於 403 leaves 內為 **57 列**。兩數皆已
實測復現，不衝突。

## 4. §5.4 / §5.5 anomaly 與 DATA_REQUESTS

A-CF01 ~ A-CF03 依下放包指定照登。A-CF04 ~ A-CF07 為本次執行新發現。

| # | 標題 | 狀態 |
|---|---|---|
| A-CF01 | SR25 含 037 未分析之新章節 | RESOLVED by R-C5 |
| A-CF02 | 客戶交付夾之 spec 為 SR25 | OPEN（Tier 3） |
| A-CF03 | 34 列 parent 形態卻為 FR | RESOLVED by R-C3 |
| A-CF04 | `intake.py` 只掃 drop folder，spec_mode 提案偏低 | OPEN（已知限制） |
| A-CF05 | **`intake.py` 需求清單靜默漏計 57 列** | FIXED |
| A-CF06 | `pymupdf` 未安裝，PDF text-layer 無法探測 | OPEN |
| A-CF07 | 空白範本第 10–11 列樣本待清 | OPEN（P4 前） |

`DATA_REQUESTS.md` 已建，standing rule 寫入首段。**建檔時無已知缺檔** ——
037 引用之唯一文件已在庫，129 節全數查得。表非空，列的是「非檔案」與
「環境」兩類請求（範本代用、表頭五格待賦值、`pymupdf`、交付夾回填）。

### A-CF05 值得分析層注意 —— 一個不報錯的漏計

`intake.py` 第一次跑報「need list 346 leaves」，實為 403。成因：
`cited_documents()` 以 `_[\d.]+$` 判斷文件引用形態卻取整格，那 57 個
「section 之後還有 Polarion item id 行」的儲存格，`$` 錨點落在 item id 上，
匹配失敗，被當成「不是文件引用」略過。

**它不報錯，而且仍指名正確的文件。** 輸出看起來完全正常，只是少了 14%。
本次能發現，唯一原因是 R-C4 已獨立給出 129 / 403 兩個已知值，對數時才暴露。
這與下放包 §7 記載的 `difflib.autojunk` 教訓是同一類：**以正則或相似度為
判準的檢查，其失敗形態是靜默的**，必須以已知全集覆核。

同源第二處：`_swra_profile()` 取到 B 欄 `Source Requirement ID` 而非 C 欄
`HMI Source ID`，把來源形態描述成 "component/architecture ids"，與同檔
`cited_documents()` 實際採用的欄位自相矛盾。兩處皆已修（取第一行、取欄
優先序一致）。其餘六個 feature 之 037 無 `HMI Source` 欄且為單行儲存格，
實測輸出不變。

## 5. §5.6 上繳與索引

本檔即上繳包。`features/comfort/docs/INDEX.md` 已建（依 R-P96 格式，
執行層維護）。

---

## 6. 對共用腳本之修改 —— 影響面告知

本包改了三個共用腳本。除 `new_feature.py` 之新旗標外，其餘皆改變既有
feature 重跑時的輸出，故逐項列出：

| 檔案 | 修改 | 對其他 feature 之影響 |
|---|---|---|
| `new_feature.py` | `--adopt-existing`；scaffold 增 `RULINGS.md`／`DATA_REQUESTS.md` | 無（僅影響新建） |
| `intake.py` | citation 取第一行；`_swra_profile` 取欄優先序 | 實測六個 feature 輸出不變（無 `HMI Source` 欄） |
| `recon.py` | assertion 機制、outline map、citation 解析、BLANK 措辭修正、`[RULED]` tc_id | **會改變輸出**，詳下 |

`recon.py` 對 Privacy 重跑之 diff（於暫存副本實測，**未動 Privacy 本體**）
全為增益：新增 assertion 段（0 checked）、outline map 段（誠實報
「`sys1_export` 無 Outline Number 欄，未建 map」）、`tc_id scheme: [RULED]
NR1L-Privacy-{n:03d}`（與其 R-PV02 相符），以及兩處措辭修正。

**Privacy 之 `DECISIONS.md` 已簽署，本包未重跑其 recon，該檔維持原狀。**
若日後重跑，簽署狀態會被覆蓋 —— 此為既有機制之性質（recon 全檔重寫
`DECISIONS.md`），非本次引入，但既已察覺，記於此。

修正的兩處措辭皆為 BLANK 狀態下會誤導簽署者者：
- `covered nowhere: 403 … — ANOMALIES entries required` → BLANK 下全部
  leaves 本就未覆蓋，要求逐葉登記等於要 403 條「空表單是空的」。改為
  「expected under BLANK … this is the Phase 4 work list, not a gap」。
- `req_ids absent from 037: draft=1 ['xxx'] — RD-1 required` → 該筆是範本
  殘留（A-CF07），不是 traceability orphan。加註提醒先看列本身。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

下放包 §5.6 要求此節。以下為執行層之判斷，**不與下放包之結論綁定**。

### 7.1 已驗、可據以進 Phase 2（六項）

1. 403 leaf 計數 —— 對 037 直接計數，兩次獨立實作得同值。
2. 129 相異 section —— 依 R-C4 解析後計數。
3. 129/129 對 SR24 export 查得，miss = 0，且 export 之 outline 無重複。
4. citation stem 唯一且為 SR24。
5. 34 列 parent 形態 FR —— 條文所舉三例（row 66 / 137 / 183）行號、標題、
   歸屬三者逐一比對相符。
6. workbook 欄位映射 15 欄自 header 文字解析，與 `feature.yaml` 無衝突。

### 7.2 該驗而**未驗**者（三項，皆不阻塞 Phase 2）

| # | 未驗事項 | 為何未驗 | 風險與時機 |
|---|---|---|---|
| 1 | **A-CF02 之交付夾實測** —— SR25 PDF 13.86 MB／SYS1 xlsx 72.80 KB | 該交付樹於本 session 之檔案系統**不可達**（已搜尋，無 `10_Reviewing` 路徑） | 低。此為分析層量測，執行層照登未驗。P7 決定是否回填 SR24 時，宜於可觸及交付樹時重測，不宜僅據本條 |
| 2 | **A-CF01 之 SR25 節次清單** —— 187 節／58 節未引用／四組實質需求 | **刻意不驗**。複測需載入 SR25 export，而 R-C1 禁止 SR25 作為查得依據 | 低。執行層可獨立佐證者僅：SR24 export 180 節、037 引用 129 節、未引用 51 節。180/129/51 與 SR25 之 187/58 是不同文件之統計，**不得互推**。037 升版時才需合流 |
| 3 | **SR24 PDF 之 text layer** | `pymupdf` 未安裝（A-CF06） | 低。spec_mode A 之文字權威為 SYS1 export；PDF 為圖面載體。**但目前無法陳述「PDF 具 text layer」** —— 若 P4 需自 PDF 取圖說或座標，先 `pip install pymupdf` 重跑 recon 即可，無需改碼 |

### 7.3 明確**不屬於**本包範圍、亦未偷做者

- 未產任何 TC、未建 framework Part N、未寫 profile（Phase 3+）。
- 未依 R-C5 把 SR25 之 18.2–21.5 補成 RD 或 TC（條文明文禁止）。
- 未動 `inputs/` 素材（A-CF07 之範本殘留只登記，不清除 —— Phase 1 不改素材）。
- 未執行任何 git 操作。

### 7.4 執行層對「本包可否結案」之判斷

**可結案。** 三個指定 assertion 全 PASS 且以 PASS/FAIL + 實測值形式輸出，
反向驗證確認其為真閘；129 節逐一查得且 fail-loud 路徑實測有效；無 open
PENDING。7.2 之三項未驗事項，兩項（1、2）之未驗係環境不可達與條文禁止，
非疏漏，且皆不影響 Phase 2 之任何輸入；第三項有一行指令可解，記於
`DATA_REQUESTS.md` #3。

**須分析層裁定者一項**：§6 所述 —— recon.py 之修改使既有 feature 重跑時
`DECISIONS.md` 輸出改變，而 Privacy 之該檔已簽署。是否、以及何時重跑既有
feature 之 recon，屬分析層之決定，執行層未動。
