# 05 — Test Set 定版與判讀單位訂正（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 05
結果：**十二步全部完成，無停止。§E 已定版 63 / 24 / 16 / 8 / 3。**
G21–G27 全數量測完成，無 MISMATCH。

---

## 0. 結論摘要

| 步驟 | 狀態 |
|---|---|
| 建立 `handoff/05_testset_lock.md` | DONE（§A 9 區塊 / §J 9 列 / §H 12 步，自檢一致） |
| 1 G0 前置閘 | **PASS 7 / 7** |
| 2 §E 更新（R-P33/34/35），驗 G21 / G22 | DONE —— **G21 PASS 63/24/16/8/3、G22 PASS** |
| 3 R-P36 三處註記，驗 G27 | DONE —— **G27 PASS，三處原文雜湊完全相同** |
| 4 B2 v2 重做九章（R-P38），驗 G23 | DONE —— **一章判定實質改變** |
| 5 嵌入物件清點（R-P39），驗 G24 | DONE —— **結論與條文推測之形態不同** |
| 6 EE Architecture（R-P40），驗 G25 | DONE |
| 7 各欄相異值數（R-P41(b)），驗 G26 | DONE |
| 8 補腳本（R-P41(a)） | DONE，另自行補 `build_b4_b5.py` |
| 9 G17 於 06 包移除 | 記錄；本包未執行移除，亦未對章節層缺口做任何新量測（R-P37） |
| 10 §D 全表自驗 | DONE |
| 11 §A 九條抄入 RULINGS.md、§F 入 ANOMALIES.md | DONE（RULINGS R-P1–R-P41 連續無缺；ANOMALIES A-PW01–A-PW25） |
| 12 上繳 ＋ 更新 INDEX.md | DONE（本檔） |

### 本包三項最重要之結果

1. **R-P38 的訂正立刻兌現。** §1.6.2.1.15.1 由「部分涵蓋」改為「**涵蓋**」——
   v1 判讀所依據的兩個錨點**根本未被任何 leaf 引用**。見 §四。
2. **R-P39 的清點推翻了條文自身的推測形態。** 不是「藏在嵌入物件裡」，
   而是「**不存在於交付文件之中**」—— CFTS009 零嵌入物件。見 §五。
3. **§E 已定版**（G21 PASS），惟同時查出其 Layer 3 清單漏了父章節 `§1.6.2.1`
   （9 leaf 觸及）與 `§1.6.2.1.17`（1 leaf）。不影響分布數字。→ A-PW24

---

## 一、§E 定版（G21 / G22）

`python features/power/scripts/build_testsets.py`

```
  裁定 SWE-PM-008: Power State（R-P33），候選 = ['Power State', 'Timeout Settings', '未歸類 009 §1.6.2.1']
  裁定 SWE-PM-057: Timeout Settings（R-P34），候選 = ['Power State', 'Timeout Settings', '未歸類 009 §1.6.2.1.17']

G22 逐條裁定驗證：
  SWE-PM-008   → Power State        期望 Power State        PASS  （R-P33）
  SWE-PM-057   → Timeout Settings   期望 Timeout Settings   PASS  （R-P34）

G21 §E 定版分布（R-P35）：
  Power State          實測  63  定版  63  PASS
  Startup Display      實測  24  定版  24  PASS
  Branding and Theme   實測  16  定版  16  PASS
  Timeout Settings     實測   8  定版   8  PASS
  Power Down           實測   3  定版   3  PASS
  合計 114  定版 114  PASS
```

逐 leaf 指派見 `data/leaf_testset.tsv`（114 列，含「依據」欄）。
該腳本**不含任何 tie-break**：若遇未裁定之跨 Test Set leaf，直接 `SystemExit`。
（首次執行時即因下述缺漏而正確拒絕，見 §1.1。）

### 1.1 登記：§E Layer 3 清單之兩處缺漏（A-PW24）

腳本首次執行時對九個 leaf 報「未裁定且跨 Test Set」。查明原因並非待裁項，
而是 **§E 之 Layer 3 清單漏列章節**：

| 缺漏章節 | 標題 | 觸及之 leaf |
|---|---|---|
| CFTS009 **§1.6.2.1**（父章節） | TLM algorithm requirements | **9 個**：`SWE-PM-001`–`009` |
| CFTS009 **§1.6.2.1.17** | Proxi Parameters management | 1 個：`SWE-PM-057` |

§E 之 Power State 列僅載 `§1.6.2.1.1–.15`，未含其父 `§1.6.2.1` 本身。
處置：於指派時將「未歸類」視為**非 Test Set 候選**（清單缺漏 ≠ 待裁），
逐一登記後排除於歧義判定之外。**不影響 R-P35 之定版分布** ——
相關 leaf 之其餘章節皆指向單一 Test Set。

### 1.2 §E 之異動

`docs/handoff/01_intake.md` §E：標題「待定版」→「**已定版（R-P35）**」；
Power State `64` → **`63`**；Timeout Settings `7` → **`8`**；
結語加註 R-P35；並新增 05 包異動註記（含 A-PW24 之缺漏登記）。

---

## 二、§D 全表實測值對照（**上繳項三**）

G0–G16、G13b 沿用 03 / 04 包，期望值不變，本包 G0 復驗 PASS。

| # | 項目 | 期望值 | 實測值 | 判定 |
|---|---|---|---|---|
| G0 | 七份原始檔 SHA256 | 7 / 7 | 7 / 7 | PASS |
| G13 | 跨多章節 leaf 數 | 11 | 11 | PASS |
| G13b | Layer 3 相異章節總數 | 46 | 46 | PASS |
| G17 | 章節層反向缺口 | （R-P37 停止，本包最後保留為紀錄） | 04 包值原樣保留，未新增量測 | 記錄 |
| G18 | A-PW06 複驗 | 36 / 35 / 27 / 16 / 1 = 115 | 相同（04 已驗，本包沿用） | PASS |
| G19 | 037 全 18 欄空值率 | 18 欄皆 115/115 非空 | 相同 | PASS |
| G20 | SYS3 交叉比對結論 | 否 | 否（04 已得確定結論） | PASS |
| **G21** | §E 定版分布 | **63 / 24 / 16 / 8 / 3，合計 114** | **63 / 24 / 16 / 8 / 3，合計 114** | **PASS** |
| **G22** | 兩條 leaf 之 Test Set | Power State / Timeout Settings | 相同 | **PASS** |
| **G23** | B2 v2 錨點必填欄 | 九章皆有且非空 | **9 / 9**，且皆列出未被引用者 | **PASS** |
| **G24** | 嵌入物件清點 | 【實測填入】 | CFTS009：`w:object`/`w:drawing`/`w:pict`/`o:OLEObject` **各 0**、`embeddings/` **0 檔**、`media/` 1 檔；`WrapperResource` 字樣 **16**。CFTS010：`<img>` 0、`<object>` 0、`WrapperResource` **15**。合計 **31 處**，分布 **16 章** | 已填空 |
| **G25** | EE Architecture 分布 | 【實測填入】 | 238 個被引用 item **全數帶此欄**；`High+Mid` 162、`All` 61、**`Mid` 單值 13**、`High+Mid+CUSW+PowerNet` 1、**`High` 單值 1** | 已填空 |
| **G26** | 037 各欄相異值數 | 【實測填入】 | 相異值 = 1：**3 欄**；≥ 100：**4 欄**。詳見 §七 | 已填空 |
| **G27** | R-P36 首次適用 | 三處皆加註且原文位元組未變 | **三處雜湊完全相同** | **PASS** |

**無 MISMATCH。**

---

## 三、R-P36 首次適用 —— 三處註記與原文雜湊佐證（**上繳項一**）

方法：加註前計各條文原文之 SHA256；加註（新增獨立段落，不觸及原文）後重算。

| 目標 | 加註前 SHA256 | 加註後 SHA256 | 判定 |
|---|---|---|---|
| R-P7 條文（`RULINGS.md` fenced block） | `080166ef5591da7e1ca853f9725b46d02eed8dec1928551eb04e987c5e79d984` | `080166ef…79d984`（同） | **UNCHANGED** |
| A-PW05 列（`ANOMALIES.md`） | `c1073e437e4680f2d984e8b1727c82e4cb5629a9a6bce58f776c7060baf3e4b3` | `c1073e43…f3e4b3`（同） | **UNCHANGED** |
| 04 下放包 §前言 | `dee13eea6d757fb0cd92897ef075c03984094d25df5dd83ff97bfbf77e7abaf0` | `dee13eea…7abaf0`（同） | **UNCHANGED** |

**G27 PASS —— 三處原文位元組未變。**

### 3.1 加註全文

**R-P7 之下**（`RULINGS.md`，原 fenced block 與其後之「狀態：live。」皆未動）：

> **註記（R-P36 首次適用，05 包加註）**
> 註記（04 包實測，A-PW19）：本條內嵌之「547 條」為失效值。
> 以原始檔重測，CFTS009 本文未被引用之需求錨點實為 669 條。
> 量測條件見 04 上繳包 §六。原文保留，依 R-P36 不改。

**A-PW05 之下**（`ANOMALIES.md` 表格之後）：

> **註記（R-P36，05 包加註）**：本條原描述之 `-ANT-` 證據出處為誤植，
> 來源實為 A-PW01（`SWE-PM-089` 之 `Source Requirement ID` 欄）。見 A-PW18。
> （本條內文已於 04 包依 R-P29 之逐字指定替換；R-P36 自 05 包起生效，
> 此後之訂正一律走註記。）

**04 下放包 §前言之下**：

> **註記（R-P36，05 包加註）**：本節稱「03 包所提之 R-P29」有誤。
> 03 上繳包之待裁項為 Q1–Q8，未提出任何編號 R-P29 之條文，亦未提出該議題。
> 該敘述所指者為分析層自身之 04 草稿，該草稿從未落檔。
> 見 04 上繳包 §一之登記。原文保留，依 R-P36 不改。

> **執行層之附帶說明**：A-PW05 之情形與另二處不同 —— 其內文已於 04 包依
> **R-P29 之逐字指定整條替換**，而 R-P36 尚未存在。本包之註記係附加於
> 替換後之現行文字，並在註記中明載此一時序，以免日後誤讀為
> 「R-P36 生效後仍被改寫」。

---

## 四、B2 v2 —— 九章重做（R-P38，**上繳項二之一**）

`data/b2_v2_uncovered_chapters.md`（61,432 bytes），
由 `scripts/build_b2.py` 產生；判讀欄為人工，以該腳本之 `JUDGEMENTS` 常數保存並版控。
舊檔 `b2_uncovered_chapters.md` 保留不刪，檔首已標註「已由 v2 取代（R-P38）」。

| 章節 | 標題 | 錨點總數 | **被引用** | 未被引用 | 引用之 leaf | v1 判定 | **v2 判定** |
|---|---|---|---|---|---|---|---|
| §1.6.2.1 | TLM algorithm requirements | 2 | 2 | 0 | `001`–`009`（9 條） | 無法判定 | 無法判定 |
| §1.6.2.1.4 | Stolen Vehicle Mode | 2 | **1** | 1 | `SWE-PM-003` | 未涵蓋 | 未涵蓋 |
| §1.6.2.1.9 | Logistic Idle | 4 | **3** | 1 | `SWE-PM-008` | 部分涵蓋 | 部分涵蓋 |
| §1.6.2.1.10 | Logistic Standby | 2 | 2 | 0 | `SWE-PM-008` | 部分涵蓋 | 部分涵蓋 |
| §1.6.2.1.11 | Logistic Sleep | 2 | 2 | 0 | `SWE-PM-008` | 部分涵蓋 | 部分涵蓋 |
| §1.6.2.1.14 | TLM modules … operative state | 8 | **1** | **7** | `001`–`009`（9 條） | 部分涵蓋 | 部分涵蓋 |
| §1.6.2.1.15.1 | ICS Wakeup Reasons by POWER Button Pressed | 3 | **1** | 2 | `SWE-PM-004` | 部分涵蓋 | **涵蓋** |
| §1.6.3.1.1 | SwitchOff_Timeout_Setting.Req management | 3 | 3 | 0 | `SWE-PM-057` | 涵蓋（一分支例外） | 涵蓋（一分支例外） |
| §1.8.1.1.1 | ID 1 Description | 5 | **3** | 2 | `SWE-PM-057` | 涵蓋 | 涵蓋 |

**九章合計 31 個錨點，僅 18 個被引用（58%）。**

### 4.1 §1.6.2.1.15.1 —— 訂正單位後判定實質改變

v1 之判讀依據為 `4941661`（ICS POWER 按鍵 wakeup 路徑、CAN 喚醒、
`CLIMATIC_PANEL.Radio_Btn0` 250 ms、`ActiveLoadSlave`）與 `4941662`。
**此二錨點未被任何 leaf 引用。**

實際被引用者為 **`4941663`**（`SWE-PM-004`），其內文**全文**為：

> In "Timed Mode" the Customer setting screens shall be disabled.

`Radio` 欄為 `R1L-R, R1L`（本專案車型專屬）。
`SWE-PM-004`（Timed）Description 末句「User settings option shall be disable
in Timed power state」與之**逐句對應**。

→ 判定 **涵蓋**。v1 所指之未涵蓋內容不在本 feature 範圍內，不構成 coverage hole。

**R-P38 之判斷因此獲得直接驗證**：判讀單位錯誤會產出實質錯誤的結論，
不只是「意義改變」。

### 4.2 §1.6.2.1.14 —— 8 個錨點中僅 1 個被引用

`4941453`（TLM 狀態 × 模組對照表）被九條 leaf 共同引用；
`4941452`、`4941454`–`4941459` 共 7 個未被任何 leaf 引用。
v2 之判讀已限縮至 `4941453`。

---

## 五、B3 —— 嵌入物件清點（R-P39，**上繳項二之二**）

`data/b3_embedded_objects.md`，由 `scripts/build_b3.py` 產生。

### 5.1 CFTS009 `.docx` 部件實測（`zipfile.namelist()`）

| 項目 | 實測 |
|---|---|
| `word/embeddings/` | **0 個檔案（目錄不存在）** |
| `word/media/` | **1 個** —— `image1.png`（3,253 B），由 `header2.xml.rels` 引用，屬頁首圖 |
| `w:object` / `w:drawing` / `w:pict` / `o:OLEObject` | **各 0 個** |
| `document.xml.rels` 關聯型別 | 無 `oleObject`、無 `package` |
| `WrapperResource` 字樣 | **16 處** |

### 5.2 結論 —— 不是「藏在嵌入物件裡」，是「根本不在檔案裡」

`CFTSMV009_CIP_R4_O829_4_inline.rtf WrapperResource` 這類字串
**是純字面文字**，不是任何嵌入物件的錨。它是 Polarion 匯出時留下的**懸空參照** ——
其所指之 RTF 資源**並未隨文件一同匯出**。

**故 R-P39 條文所本之推測（「規格內容可藏於文字層看不見之處」）方向正確但形態不同：
內容不是看不見，是不存在於交付文件之中。**

| 文件 | 懸空參照數 | 所在章節數 |
|---|---|---|
| CFTS009 | 16 | 8 |
| CFTS010 | 15 | 8 |
| **合計** | **31** | **16** |

其中 **8 章之非錨點內文 < 200 字元**，即該章可讀內容幾乎只剩這些參照。
受影響最嚴重者為 **CFTS009 §1.6.2.1 `TLM algorithm requirements`**
（非錨點內文 101 字元、2 個需求錨點、2 處懸空參照）—— 該章正是 A-PW16 九章之一，
且被九個 leaf 共同引用；其兩個被引用錨點 `4941354` / `4941355` 之內文即為該二參照，
故 B2 v2 判為「無法判定」。

**對 R-P39 之問題「G8 = 904 之規格覆蓋率有無上界保證」之回答**：
904 個需求錨點**本身完整存在於文字層**；不可得者是這 31 處參照所指之外部資源。
覆蓋率之缺口是**有界且已清點的**（16 章），不是無上界。

A-PW23 之描述已依實測整條訂正。CFTS010 為 OLE2，無 OOXML 部件可查，
其數字係由 `textutil -convert html` 輸出計得，為**下界**，已於 B3 檔內明示。

---

## 六、B4 —— EE Architecture 分布（R-P40，**上繳項二之三**）

`data/b4_ee_architecture.md`，由 `scripts/build_b4_b5.py` 產生。
母體：238 個被引用 item。

| EE Architecture 值組 | item 數 |
|---|---|
| `Atlantis High, Atlantis Mid` | 162 |
| `All` | 61 |
| **`Atlantis Mid`（單值）** | **13** |
| `Atlantis High, Atlantis Mid, CUSW, PowerNet` | 1 |
| **`Atlantis High`（單值）** | **1** |
| 無此欄 | **0** |

FW036 c21–c27 七個車型欄實測世代：**Atl-Hi 2 欄**（c21 `HDCC27 Atl-Hi`、
c22 `DT27 Atl-Hi`）、**Atl-Mi 5 欄**（c23–c27）。

**明確回答：不存在「兩世代皆不含」之被引用 item。**
224 / 238 兩世代通用；**14 個為單世代專屬**（Mid 專屬 13、High 專屬 1）。
逐 leaf 層級：114 個 leaf 中僅 **2** 個之 item 聯集僅含單一世代。

> 01 包 §F 已載 c21 標頭沿用 A-PV15 與 R30-3 / R30-4（車型欄留白）。
> 本檔僅提供實測分布，未改變該政策，未建議如何填欄。

---

## 七、B5 —— 037 各欄相異值數（R-P41(b)，**上繳項二之四**）

`data/b5_column_entropy.md`，同上腳本。母體 115 leaf。

**相異值數 = 1（3 欄）** —— 與空欄實際效果相同：

| 欄 | 標頭 | 唯一值 |
|---|---|---|
| c5 | Release Version | `1.0.0` |
| c6 | Categorization | `Functional Requirement` |
| c8 | Feasibility | `Yes` |

> c6 即 **G2 之內容，且一路被判為 PASS** —— 04 §九第 6 項所指之情形獲證實：
> 一個閘門在驗一個沒有鑑別力的欄位。

**相異值數 ≥ 100（4 欄）** —— 近乎逐列唯一，無分群價值
（作為內容來源仍有價值）：`SWE-Requirement ID` 115、`Requirement Description` 115、
`Verification Method` 114、`Source Requirement ID` 112。

**可分群者（≤ 8 值）**：`Sub Categorization` 5、`Impact` 3、`Reusable` 3、
`Risk Factor` 2、`Priority` 2。其中 `Sub Categorization` 已由 A-PW06 判定
不可作分批判準；`Priority` 已由 R-P8 判定不具映射權威。
**即 037 十八欄中，可用於分批之欄位實質為零。**

### 7.1 附帶查出：§E 弱點段之統計為失效值（A-PW25）

§E「本分組之已知弱點」稱：「`Requirement Title` 於 115 leaf 中出現 **20+ 種**，
多數僅出現 1 次（`Timeout` 7、`Phone Call` 5 為**僅有例外**）」。

實測：相異值 **99** 種、僅出現 1 次者 **94** 種。出現 > 1 次者：

| 值 | 次數 |
|---|---|
| `Timeout` | 7 |
| `Phone Call` | 5 |
| `Splash Screen logo visualization` | 4 |
| `Power down` | 3 |
| `FOTA` | 2 |

「20+ 種」大幅低估（實為 99），「僅有例外」為誤（另有三組）。
**該節之結論（無分組價值）不受影響，反而更強。**

---

## 八、獨立判斷：本包是否仍有該驗而未驗者（**上繳項四**）

04 上繳包 §九之六項，本包處置：第 1 項→R-P38（已重做，且判定實質改變）；
**第 2 項→未處置**；第 3 項→R-P39（已清點，形態訂正）；第 4 項→R-P40（已量測）；
第 5 項→R-P41(a)（已補腳本，另自行補 B4/B5）；第 6 項→R-P41(b)（已量測）。

### 8.1 就第 2 項之嚴重性判斷（下放包指定）

**第 2 項**：Layer 3 之邊界由副作用定義（「有 leaf 觸及」），非由設計定義。
R-P37 停止章節層調查後，該問題失去了原本唯一的探查途徑。

**執行層判斷：嚴重性為中，且 R-P37 並未使其惡化 —— 但它現在是無解的，而非待解的。**

理由三點：

1. **R-P37 的推理成立。** 04 §六已證章節層缺口（499 錨點）完全內含於 R-P7
   所免除的需求層缺口（814 錨點）。若續行章節層調查，實際上就是把 Pei
   已裁定不追的東西換個單位再追一次。停止是對的。
2. **但「停止調查」不等於「問題消失」。** Layer 3 現在記 46 個章節，
   而這 46 個之所以是這 46 個，唯一理由是「錨點鏈碰到了它們」。
   沒有任何文件說「Power Management 的規格範圍是這些章節」。
   R-P28 曾是唯一會逼出這個定義的動作。
3. **然而本包的兩項實測顯示，這個問題的實際風險比想像中低：**
   - **G25**：238 個被引用 item 全部落在本專案適用之 EE Architecture 內，
     且 04 包已驗車型軸零例外 —— 即 SYS2 匯出**已完成範圍過濾**，
     「哪些規格屬於本 feature」實際上是由 SYS2 的收錄規則決定的，
     不是由 Layer 3 決定的。
   - **R-P7 正是裁定「不追 SYS2 收錄規則」。** 所以 Layer 3 邊界的定義權
     早已隨 R-P7 一併交出去了；R-P37 只是把這件事講明白。

**結論**：這不是一個「該驗而未驗」的缺口，而是一個**已被裁決放棄驗證的範圍問題**。
建議登記為長期已知限制（而非待辦），並在 Phase 4 之交付說明中明載：
本 feature 之規格涵蓋範圍由 SYS2 收錄規則決定，Layer 3 為其投影，非獨立界定。
**若日後有人問「為什麼某章沒有 TC」，正確答案是 R-P7，不是 Layer 3。**

### 8.2 新增未驗項（五項）

**1. B2 v2 之「部分涵蓋」五章，其未涵蓋部分是否需要 TC —— 仍未答。**
   v2 把判讀單位修對了，但判讀的**輸出**仍只有四個標籤。
   「§1.6.2.1.10 與 §1.6.2.1.11 之唯一差異是 network active/off，
   而 Description 不含 network 一詞」—— 這句話的下一步是什麼？
   是「TC 需自行補出 network 條件」還是「該差異不測」？**無條文、無閘門。**
   這直接決定 Phase 4 的 TC 數量，比 A-PW16 的處置更迫切。

**2. 31 處懸空參照之影響範圍只算了章節，未算 leaf。**
   §五已知 16 章受影響，但**這 16 章被幾個 leaf 引用、涉及幾個被引用錨點**，
   本包未交叉。§1.6.2.1 是 9 個 leaf —— 其餘 15 章可能牽連更多。
   這是 Phase 4 產生 TC 時會直接撞上的（規格文字不完整）。

**3. `Verification Criteria` / `Verification Method` 兩欄從未被任何閘檢視內容品質。**
   G26 顯示 `Verification Method` 114/115 相異（近乎逐列唯一），
   但 `SWE-PM-008` 之 Verification Criteria 全文僅「Vehicle equiped with CAN」
   （含拼字錯誤）。這兩欄是 Phase 4 產生 TC 的直接輸入，
   而現有閘門只驗「非空」與「相異值數」，**未驗其是否可執行**。

**4. B2 v2 之 `JUDGEMENTS` 常數雖已版控，但仍無第二意見機制。**
   R-P41(a) 把事實部分腳本化了，判讀仍是單一來源。
   本包自己就在 §1.6.2.1.15.1 上推翻了上一包的判讀 ——
   **推翻它的是單位訂正，不是覆核**。若單位正確而判讀仍錯，目前無機制可發現。

**5. CFTS010 之嵌入物件清點為下界，未取上界。**
   §五之 CFTS010 數字（15 處）係由 `textutil html` 之輸出計得。
   R-P3′ 已解除 `olefile` 之禁令，故技術上可直接檢視 OLE2 之 storage 結構取得上界，
   本包依 R-P39「只清點、不解 RTF」之限制未做。
   **「不解 RTF」與「不檢視 OLE2 目錄」是兩件事**，本包採較保守之讀法，於此登記。

---

## 九、禁區遵守聲明

| 禁區 | 遵守情形 |
|---|---|
| 不得寫回 FW036 workbook | 僅 `read_only=True` 開啟 |
| 不得執行任何 git 操作 | 本包執行期間未執行任何 git 指令 |
| 不得以 openpyxl save 寫任何 xlsx | 未呼叫 `save()` |
| 不得補齊 `SWE-PM-089`（R-P1） | 未補；`leaf_testset.tsv` 114 列不含該 leaf |
| 不得沿用純文字衍生物之任何數字（R-P10） | 全部數字自原始檔重生 |
| 不得自行調整 §C 正則 | `SEC_RE` / `REQ_RE` 一字未改 |
| **不得修改任何已落檔裁決條文之內文（R-P36）** | **G27 以雜湊證明三處原文位元組未變。** 本包所有訂正（A-PW23 之框架、A-PW25 之統計）皆走 ANOMALIES 之狀態欄或新增條目，未動任何 `[R-Pnn]` 區塊內文 |
| **不得為 A-PW16 之 9 章建議處置** | `b2_v2_uncovered_chapters.md` 全檔無處置建議；判讀欄僅四個標籤＋逐字依據 |
| **不得解 RTF、不得改 R-P17 之文字層定義** | 未讀取任何 RTF；`extract_textlayer.py` 未改。B3 僅列 `zipfile.namelist()` 與 XML 標籤計數 |
| **不得續行章節層反向缺口調查（R-P37）** | 本包未對 288 章做任何新量測；G17 沿用 04 包值 |
| §E 定版後不得再自行變更分布數字 | 定版即 R-P35 所裁之 63/24/16/8/3，未再變更。A-PW24 之清單缺漏僅登記，未改分布 |
| 素材補入超出 `inputs/` 需 Pei 裁定 | 未補入任何素材 |

---

## 十、待裁

- **Q1 A-PW16 之 9 章處置**（R-P27，素材已備齊）。判定分布：涵蓋 2、
  涵蓋（一分支例外）1、部分涵蓋 5、未涵蓋 1、無法判定 1。
- **Q2 §1.6.2.1 之處置** —— 其兩個被引用錨點之內文為懸空參照，內容不存在。
- **Q3（新，可能最迫切）§八第 1 項：五章「部分涵蓋」之未涵蓋部分是否需要 TC。**
  判讀已到位，但「然後呢」無條文。此項直接決定 Phase 4 之 TC 數量。
- **Q4 31 處懸空 `WrapperResource` 是否列 DR**（A-PW23）——
  向上游索取缺漏之 RTF 資源。併請裁定是否先做 §八第 2 項之 leaf 層交叉。
- **Q5 A-PW24：§E Layer 3 清單漏列 `§1.6.2.1` 與 `§1.6.2.1.17`** 是否補列。
- **Q6 A-PW25：§E 弱點段之「20+ 種／僅有例外」** 是否依 R-P36 精神走註記
  （該段非裁決條文）。
- **Q7 §八第 5 項：CFTS010 之嵌入物件是否取上界**（`olefile` 已由 R-P3′ 解禁；
  「不解 RTF」是否涵蓋「不檢視 OLE2 目錄」需釐清）。
- **Q8 §八第 3 項：`Verification Criteria` / `Method` 兩欄是否補設品質閘**
  （Phase 4 之直接輸入）。
