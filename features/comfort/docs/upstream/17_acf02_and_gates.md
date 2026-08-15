# 17 — Comfort HMI / A-CF02 交付夾一致化 ＋ 三項待補檢查

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 26（寫回覆核、三項檢查）＋ 27（A-CF02 裁定）
- 結果：三個 gate 全數加入並反向驗證，**lint 35/35 PASS**；SR24 兩檔已放入
  交付夾且逐位元組相符；A-CF02 轉 RESOLVED。**SR25 兩檔待 Pei 移除。**

---

## 1. ENTRY 002 狀態更新（26 §1）

`DELIVERY.sha256` ENTRY 002 之狀態欄改為
**`Excel-confirmed by Pei 2026-08-15（四項）`**，並依下放包 28 §1 同時增記
**`not delivered（Pei 2026-08-15）`**。hash 與內容未動（append-only）。

另於該 ENTRY 末補一句，防止日後混讀：

> **本台帳為「已產出」之帳，非「已交付」之帳**（28 §1）。兩者不得混用：
> ENTRY 有 hash 只證明該位元組存在過，不證明它送出去了。交付與否一律
> 讀狀態欄。

複驗 `shasum -a 256 -c --ignore-missing DELIVERY.sha256` → **4 行全 OK**。

---

## 2. 三項檢查 —— 全數加入，全數反向驗證

lint 由 32 增至 **35 gate**。

### 2.1 `json-key-coverage`（26 §4.1）

TC 之每個 key 必須**映到欄位**或**具名於 `NOT_IN_WORKBOOK`**，二者居一。
名單即下放包所給之八項，直接引用；增列須經裁定（同 R-C26 之理）。
每次執行皆印出具名行：

```
- PASS — TC keys deliberately not in the workbook (26 §4.1): ['distinguishing_axis',
  'duplicate_of', 'estimated_test_time', 'keywords', 'reasoning', 'split_flag',
  'split_reason', 'tc_title']
```

**反向驗證（兩個方向，因為它有兩種壞法）**：

| 注入 | 結果 |
|---|---|
| 由 `write_back.py` 之 `COLS` 移除 `"N": "specification_reference"` | **FAIL ×14**，逐條指名 `specification_reference` 未落欄 |
| 於某 TC 之 JSON 加入未具名之 `test_environment` | **FAIL ×1**，指名 `NR1L-ComfortHMI-001` |

第一個方向才是這個 gate 真正要防的：**`COLS` 少一欄，寫回會靜默漏填一整欄，
而所有既有 assertion 都只比對 `COLS` 之內容 —— 它們用同一份清單，
所以一起瞎掉。** 這個 gate 從 JSON 那一側看，才看得見。

### 2.2 `anomaly-id-registered`（26 §4.2）

掃 `features/comfort/docs/` 全部 `*.md`（handoff 與 upstream 皆含）之
`A-CF\d+`，凡未見於 `ANOMALIES.md` 者即 FAIL，並回報**首次出現之檔名**。

**反向驗證**：於 `16_writeback.md` 末加一行，內含一個未登記之編號
（實測用 `A-CF` 加兩位數字，本文以 `<NN>` 代之，理由見下）→

```
[FAIL] anomaly-id-registered: anomaly id(s) cited in docs/ but absent from
ANOMALIES.md: A-CF<NN> (first seen docs/upstream/16_writeback.md)
```

移除後回 PASS。這正是 A-CF16 該被抓到而未被抓到的那一次。

**本文以 `<NN>` 代替實際數字，是被這個 gate 逼的** —— 初稿逐字寫了該編號，
lint 隨即 FAIL 並指名 `17_acf02_and_gates.md`。**gate 沒有錯**：它的規則是
「docs/ 內引用之編號須已登記」，而上繳包也在 `docs/` 內。
代價是**反向驗證之過程無法逐字記載於上繳包**。此為已知副作用，
非缺陷 —— 但下次有人想在文件裡舉例一個假編號時會再撞到，故記於此。

### 2.3 `residue-scan-window`（26 §4.3）

`write_back.py` 之殘留掃描由固定 24–35 改為 `range(last, ws.max_row + 1)`。
量測值：`ws.max_row = 59`，故實際掃 row 24–59（原本只掃 12 列）。

**該項屬 `write_back.py` 而非 lint**，但下放包要求 lint 為 35 gate。作法：
lint 加一個**讀原始碼**之 gate —— 若 `write_back.py` 內不含 `ws.max_row`，
或仍存在 `range(last, last + N)` 形式之固定窗，即 FAIL。

理由：把它做成「跑一次 write_back 看結果」會使 lint 依賴一次寫檔；
做成靜態檢查則**每次 lint 都在確認那個窗沒有被改回去**。

**反向驗證**：把 `range(last, end + 1)` 改回 `range(last, last + 12)` →

```
[FAIL] residue-scan-window: write_back.py's post-write residue scan does not
run to ws.max_row (a fixed-width window leaves the tail unchecked)
```

還原後 PASS。

### 2.4 一個實測，順帶回報

改窗之前，我已另行手測 row 36–59 之 D／F／I／J／L／M／AH：**零殘留**。
故本項改動**未改變既有產出檔之結論**，改變的是「下次會不會有人看」。

---

## 3. A-CF02 —— 交付夾基線一致化（27）

### 3.1 放入 SR24（執行層，已完成）

| 檔案 | 來源 | bytes | `cmp` 逐位元組 |
|---|---|---|---|
| `Comfort HMI Logic and Flow R1 SR24 Post 3A CR24879 (September 25 2023).pdf` | `spec-index/sources/` | 6,462,311 | **identical** |
| `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx` | `spec-index/cache/` | 70,040 | **identical** |

比對以 `cmp` 逐位元組執行，**非以檔名或大小標籤代替**（R-C14）。
兩端 SHA256 亦相符（PDF `fc5d3cd1d524f4d5…`、xlsx `6982d37db81b36e4…`）。
複製前先確認目的地無同名檔，避免覆蓋。

### 3.2 待 Pei 移除之兩個檔名（Tier 3，執行層不動）

```
Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf
SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025).xlsx
```

兩份**非資料遺失** —— `spec-index/sources` 與 `cache` 皆留有其副本。
已依 **先放後移**：現時點交付夾內 SR24 與 SR25 並存，任一時點皆有完整 spec。

### 3.3 交付夾現況（複製後實測）

| 檔案 | bytes | 基線 |
|---|---|---|
| `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx` | 144,163 | SR24（引） |
| SR24 PDF | 6,462,311 | **SR24（本次放入）** |
| SR24 SYS1 xlsx | 70,040 | **SR24（本次放入）** |
| SR25 PDF | 14,538,298 | SR25（待移除） |
| SR25 SYS1 xlsx | 74,545 | SR25（待移除） |
| `Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf` | 3,560,705 | SR24（**下放包未列**） |

**最後一列須回報**：交付夾另有一份 Device Manager 之 SR24 PDF，下放包 27 §1
之清單未列。它與本項處置無關（非 Comfort HMI spec，且已是 SR24），
**未動**；列此僅為使清單完整 —— 下放包所列三檔不是資料夾之全部。

### 3.4 A-CF02 轉 RESOLVED

條目載明：現象、裁定（Pei 2026-08-15 選項 1）、037 之 498 列重測結果
（相異 stem 數 = 1，無 SR25 無空值）、處置與待辦分工、`BASELINE.sha256`
不變之理由（R-C20：涵蓋 pipeline 來源檔，交付夾附件不在其列；已複驗 8 檔全 OK）。

**重審條件**：

> 若日後基線改採 SR25（需先推翻 R-C1），本項須同步重做 —— 交付夾附件、
> `feature.yaml` 之 `sys1_export`／`spec_pdf`、`data/section_fulltext.tsv`
> 與全批 `specification_reference` 皆須一併換基線。
> 本項之處置繫於 R-C1，**不獨立成立**。

### 3.5 原條目之「不可達」是誤判 —— 據實更正

A-CF02 原文寫「該交付樹於本 session 之檔案系統不可達（已搜尋，無
`10_Reviewing` 路徑）」。**那次搜尋只掃了 repo 內**（自 `TC_Generator/`
起之 `find .`）。交付樹實際在

```
~/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Climate Control Interface/ComfortHMI/
```

—— **在 repo 之外**，本輪擴大搜尋範圍後一次命中。

**零命中被當成「不存在」，而它其實只是「不在我搜的地方」** —— R-C13 同型。
原條目自己寫了「宜於可觸及交付樹時重測」，那句是對的；錯的是「不可達」
這個結論下得太早。已於 ANOMALIES 條目內劃線更正並記其成因。

**這與上一包之 A-CF16 是同一件事的兩面**：一個是引用了不存在的編號，
一個是宣告了其實存在的東西不存在。兩者皆為靜默失敗，且都由「我沒去看」
而非「我看錯」造成。`anomaly-id-registered` 擋得住前者；後者目前**仍無機制**。

---

## 4. 全批複跑

```
35 / 35 gates PASS; 0 finding(s) across 25 TCs
```

（25 條 = pilot 14 ＋ 批次 2 之 11，見上繳 18。）

---

## 5. 「本包是否仍有該驗而未驗者」

1. **`json-key-coverage` 只覆蓋 TC 層之 key，未覆蓋 doc 層。**
   下放包白名單八項中，`reasoning`／`keywords`／`duplicate_of`／
   `distinguishing_axis` 實際位於 **doc 層**而非 TC 層。doc 層另有
   `assumptions`／`batch`／`outline`／`parent`／`source_clause`／`tcs`
   六個結構性 key **不在白名單內**。
   我**未自行增列**（26 §4 明寫增列須經裁定），因此把 gate 限縮於 TC 層。
   **待裁**：是否擴及 doc 層，並將該六項一併列入白名單。
2. **搜尋範圍本身無機制。** §3.5 之誤判成因是「`find` 的起點」，而目前沒有
   任何檢查會問「這次搜尋涵蓋了什麼」。R-C13 要求零命中須換路徑，但**換到
   哪裡由我判斷，且判斷不留痕跡**。此為結構性缺口，非本包可補。
3. **SR25 之移除未驗** —— 依 27 §3 屬 Pei，執行層備妥後停下。移除後之
   交付夾清單須另行複測，本包未列。
4. **交付夾無台帳。** `DELIVERY.sha256` 記 `output/`，不記交付夾。本次放入
   兩檔於任何台帳皆無紀錄；下次有人問「交付夾裡那份 SR24 是哪來的」，
   答案只在本上繳包裡。**建議**：交付夾另立一份台帳，或於 `DELIVERY.sha256`
   增一類 ENTRY。列此待裁，未自行建立。

---

## 6. 建議 commit message（git 未執行）

```
feat(comfort): add three coverage gates; align delivery folder to SR24

- json-key-coverage: every TC key maps to a column or is named
- anomaly-id-registered: an anomaly id cited in docs must be registered
- residue-scan-window: the post-write scan must reach ws.max_row
- all three reverse-verified; lint 32 -> 35 gates
- copy SR24 pdf/xlsx into the delivery folder, byte-compared
- A-CF02 RESOLVED with its re-review condition; BASELINE unchanged
- DELIVERY ENTRY 002: Excel-confirmed, not delivered
```

---

## 7. 待 Pei

**移除交付夾之 SR25 兩檔**（檔名見 §3.2）。移除後交付夾即與 037 及
工作簿同基線。
