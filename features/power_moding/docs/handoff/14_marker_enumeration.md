# 下放包 14 —— marker 枚舉法、SU9 缺口之處置與 batch 1 第二輪覆核

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/14_marker_enumeration.md`
- 前一包：[13_batch1_rework.md](13_batch1_rework.md)
  （上繳 [../upstream/13_batch1_rework.md](../upstream/13_batch1_rework.md)）

---

## 一、13 包之覆核結果 —— **通過，停止條件 7 為正確觸發**

雙向複驗、lint 擴充（20→28）、七項 must-hit 全 FAIL、重寫後 28/28、
`tc_id` provisional 防護四項全攔，皆有實據。

**三項特別記明**：

1. **R-PMH53 之檢查「首版只驗存在性 → PASS」而自行加強至語意相容** ——
   `-004`／`-003` 確實存在，只是所指者無關。**若停在存在性，該檢查會永遠
   綠燈而永遠抓不到它要抓的東西。**
2. **§6 之自錯揭露**（`self_test()` 誤用 `ROOT` 致 `NameError`，自測 exit 1）
   —— 「它自己攔下自己」，且修正時仍依 R-PMH41 驗命中數。
3. **§5.3 為 R-PMH50 之第二次實證**：`SU9.1` 載「按 Power Off／Screen Off
   於 splash 或 disclaimer 期間**會重設逾時**」，該子句於 SYS1 不存在 ——
   若依 SYS1 產出，`-003`／`-004` 會在按鍵情境下給出錯誤結果。

---

## 二、SU9 缺口 —— 分析層獨立複驗，**成立**

**量測條件**：PDF 以 `pymupdf` 抽全文；SYS1 以 `openpyxl` `read_only`
讀 `Basic Report` 之 `Description` 欄全 52 則。

PDF p8 逐字（`pm.txt` 行 315–316）：

```
SU9.) Pressing "Screen Off" or "Power Off" hard key will not do anything when pressed during animation.
SU9.1) Pressing Power Off or Screen Off hard keys during the splash screen(s) or disclaimer will reset the timeout and the radio shall display the screen the next time …
```

| 探針 | SYS1 全 52 則 |
|---|---|
| `SU8` | 1 |
| **`SU9`** | **0** |
| **`reset the timeout`** | **0** |

**執行層之指認完全成立。**

---

## 三、「每章末則是否系統性被截斷」—— **分析層已查，答案為否**

執行層 §8 第 4 項稱此為「本輪最該追而未追者」。**我追了**，並且用了一個
比句級 diff 更乾淨的方法。

### 3.1 方法：**規格 marker 枚舉**（無門檻）

規格之需求單位在 PDF 中各有其標記（`SU\d`／`SSND \d`／`PM\d`／`PITA\d`／
`VRLP\d`／`OFF\d`）。以正規式枚舉 PDF 之全部 marker，逐一檢查其是否
出現於 SYS1 之 `Description` 全文。

**此法無門檻、無取樣、無相似度** —— 與 6-gram 之 30% 判準不同，
它不需要任何可調參數（§六）。

### 3.2 結果：**PDF 30 個 marker，SYS1 缺 2 個**

| 章 | PDF marker | 缺於 SYS1 |
|---|---|---|
| 7 | `SU1.) SU1.1) SU2.) SU2.1) SU3.) SU4.) SU5.) SU6.) SU7.) SU8.) SU9.) SU9.1)`（12） | **`SU9.)`、`SU9.1)`** |
| 8 | `SSND 1) 2) 2.1) 2.2) 2.3) 3)`（6） | 無 |
| 9 | `PM1)`（1） | 無 |
| 10 | `PITA4: 5: 6: 6.1: 8: 9: 10:`（7） | 無 |
| 11 | `VRLP1:`（1） | 無 |
| 12 | `OFF1.) OFF2.) OFF3.)`（3） | 無 |
| **合計** | **30** | **2** |

**截斷不是系統性的** —— 只發生在章 7 之末尾，且恰為最後兩個 marker。
**其餘五章之末則（`SSND 3)`／`PM1)`／`PITA10:`／`VRLP1:`／`OFF3.)`）
全部對得上。**

執行層 §8 第 4 項之疑慮**已解除**，且解除之依據為枚舉而非抽樣。

### 3.3 一項附帶所見（**屬上游，不處置**）

PDF 之 `PITA` 編號為 `4, 5, 6, 6.1, 8, 9, 10` —— **無 `PITA1–3`、無 `PITA7`**
（`PITA7` 於 PDF 全文 0 命中）。此為**上游規格自身之編號跳號**，
非抽取缺漏。依 R-PMH26 之精神（上游之形式問題不在本 feature 範圍），
**只登記不開 DR**。

---

## 四、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH54（規格覆蓋以 marker 枚舉為權威判準）
規格文件與其結構化匯出之覆蓋比對，以**需求 marker 之枚舉**為權威判準：
自 PDF 枚舉全部需求標記（本 feature 為 `SU\d`／`SSND \d`／`PM\d`／
`PITA\d`／`VRLP\d`／`OFF\d`），逐一檢查其是否出現於匯出之描述全文。

此法**無門檻、無取樣、無相似度參數**，其結果為二值（在／不在），
故不受任何可調參數之影響。

句級雙向 diff（13 包）**降為輔助** —— 其用於發現 marker 內部之子句缺漏
（如 7.1 之時序子句），不用於判定需求單位之覆蓋。二者分工：
  marker 枚舉 → 需求單位是否存在
  句級 diff  → 已存在之單位其內容是否完整

實測（分析層 14 包 §3.2）：PDF 30 個 marker，SYS1 缺 2 個
（`SU9.)`、`SU9.1)`），**截斷非系統性，限於章 7 末尾**。
```

```
R-PMH55（以無 leaf 之規格內容限縮既有 TC 之條件）
自規格取得、但於 037 無對應 leaf 之內容，**得用於限縮既有 TC 之條件，
不得用於新增涵蓋**。

判準（三項須同時成立）：
(a) 該內容之作用為**使既有 leaf 之驗證正確**（排除會使該 leaf 之
    預期結果不成立之情境），而非**驗證該內容自身之行為**；
(b) 其於 TC 中僅出現於 `pre_conditions` 或步驟之限定子句，
    **不得出現於 `expected_result`** —— ER 一旦斷言該內容，
    即成為對無 leaf 之行為之驗證（§8.4.2）；
(c) 其來源與缺 leaf 之事實須於 `reasoning` 具名，並開 DR。

現行適用：`-003`／`-004` 之「不按任何硬鍵」限定，源自 PDF `SU9.1`
（按 Power Off／Screen Off 會重設逾時），該 marker 於 SYS1 缺失
（A-PMH14、DR-PMH3）。三項判準皆成立：其作用為排除會使逾時不發生之
操作、只出現於步驟之限定子句、已於 reasoning 具名。

**若 DR-PMH3 回覆為「SU9／SU9.1 應在 037」**，則該二 marker 將成為
新 leaf，本條之適用即告終止，其內容改以獨立 TC 涵蓋。
```

```
R-PMH56（未涵蓋清單本身須經完整性檢查）
R-PMH52 所要求之「lint 未涵蓋之 canon 節號」具名清單，**其自身須以
canon 之節號全集為母體逐節核對**，不得以人工回想列舉。

實施：以 canon 之節標題產生節號全集，減去 lint 已涵蓋者，
其差集即為應具名之清單；清單由程式產生，不手寫。

依據：13 包所具名之未涵蓋清單列了九節，**而 §5.2（步驟字數上限）、
§5.3（標準片語）、§5.6（baseline）、§6.1（多階段 ER 版面）、
§10.4（reasoning 2–5 句）、§10.6、§12（design method first-match）
七節既未被檢查、亦未被具名** —— 清單漏列使「已具名」產生虛假之完整感
（14 包 §5.4）。
```

---

## 五、batch 1 第二輪人讀覆核 —— **三項新發現，仍不通過**

13 包之六類違規**已全部修正**（逐條複核相符）。以下為**第二輪**之發現，
皆屬 lint 28 項與其未涵蓋清單**兩者皆未涵蓋**者。

### 5.1 【嚴重】canon §5.2 —— Final Step 字數逾 18 字，四處

§5.2B 定 Final Step ≤ 18 words（其得延長至 18 以承載 action ＋ check target）。

| tc | 步驟 | 字數 |
|---|---|---|
| `-001` | step 2 | **25** |
| `-003` | step 2 | **26** |
| `-004` | step 1 | **≈35** |
| `-007` | step 1 | **≈30** |

`-004` step 1 逐字：`Without pressing any hard key or the "Accept" button, wait
for a period longer than the timeout used on a non-Maserati application, then
read the screen and check that the disclaimer screen is still displayed`
—— **一步之內含限定、等待、讀取、檢查四件事**，應拆為兩步。

### 5.2 【中】canon §11 —— ER 內之 UI 文字用單引號

| tc | 逐字 | 應為 |
|---|---|---|
| `-001` ER 1 | `'loading...' is displayed …` | `"loading..." is displayed` |
| `-001` ER 2 | `'Loading...' is removed …` | `"Loading..." is removed` |

§11 明列 `Press 'Screen Off' button`（單引號）為 ✗。
`"Accept"` 已改對，**同一條 TC 內兩種引號並存**。

### 5.3 【中】§10.2 —— 全批八條皆 `P1`，rubric 未起分辨作用

八條之 `priority` 全為 `P1`，無任何 P0／P2／P3。

**對照語料**：Power Management 之 284 條中 P0 180／P1 59／P2 7／P3 37；
其 `Startup Display` 組 59 條亦非單一值。

**至少 `-001`（免責畫面之載入→就緒切換）與 `-008`（開機顯示免責畫面）
落在 §10.2 之 P0 定義「boot/recovery」之射程內**，而免責畫面本身為
legal 要求（`as defined by legal/CFTS009`）。

**本項不是「應為 P0」之斷言，而是「rubric 未被實際套用」之疑慮** ——
八條同值且無一條之 reasoning 說明為何不是 P0。須逐條重判並於 reasoning
載其依據。

### 5.4 **R-PMH52 之未涵蓋清單本身漏列七節** —— 本輪最要緊者

13 包 §4.3 具名之未涵蓋節號為九節（§4.3／§4.4／§5.7／§7／§8.2/§8.3／
§8.4.1／§8.5／§8.7.3／§10.2）。

**而 §5.1 所指之 §5.2 違規，既不在 28 項檢查內，也不在該九節清單內。**

逐節核對後，**漏列者七節**：

| 漏列之節 | 內容 |
|---|---|
| **§5.2** | 步驟字數上限（本輪四處違規） |
| §5.3 | 標準設定片語之逐字重用 |
| §5.6 | baseline 之措詞 |
| §6.1 | 多階段 ER 之版面 |
| §10.4 | `reasoning` 2–5 句 |
| §10.6 | `duplicate_of` 之編碼 |
| §12 | design method 之 first-match 走查 |

**「已具名未涵蓋」若其清單不完整，反而製造虛假之完整感** ——
讀者會以為清單外者皆已檢查。→ R-PMH56。

---

## 六、6-gram 之 30% 門檻（13 包 §8 第 2 項）—— **降為輔助即解**

執行層自陳該門檻無來源，與 G1 之 `0.35` 同型。**其正確處置不是替它找依據，
而是讓它不再承擔判定責任**：R-PMH54 已將需求單位之覆蓋判定移交
marker 枚舉（無門檻），6-gram 僅用於已存在單位之子句比對，
且其輸出為**候選清單供人讀**，非通過／失敗之判定。

**故不為該門檻另立依據，亦不刪除** —— 其角色改變，責任解除。

---

## 七、作業步驟

1. **抄錄** —— §四之 R-PMH54 ~ R-PMH56 逐字抄入 `RULINGS.md`，附核對表
   （依 R-PMH41 驗命中數）。

2. **marker 枚舉之實作** —— 將 §3.1 之方法寫成
   `scripts/marker_coverage.py`，輸出 PDF marker 全集、SYS1 命中表、
   缺漏清單。**須與分析層之 30／2 相符**（先算後比）。
   加 must-hit：自 SYS1 側移除一個已知存在之 marker（測試替身）→ 須 FAIL。

3. **未涵蓋清單之程式化（R-PMH56）** —— 自 canon 之節標題產生節號全集，
   減去 lint 已涵蓋者，差集即為具名清單。**與 §5.4 之七節比對**，
   若程式產生之清單與人讀所得不同，以程式為準並回報差異。

4. **batch 1 第三輪修正** —— 依 §5.1／§5.2／§5.3 逐項修正：
   - 四處逾 18 字之 Final Step 拆步或縮寫；
   - `-001` ER 之單引號改直雙引號；
   - **八條之 priority 逐條重判**，於 `reasoning` 載其依據；
     **不得為求分布而改值** —— 若重判後仍全為 P1，
     則於 reasoning 逐條說明為何不落 P0（§10.2 之 boot/recovery 射程）。

5. **lint 再擴充** —— 新增 §5.2 步驟字數檢查（normal ≤12／final ≤18／
   §5.1 例外 ≤18），must-hit 以本輪四處違規為天然反例
   （保全於 `tests/fixtures/`）。

6. **`DR-PMH3` 之影響面登記** —— 若上游回覆 `SU9`／`SU9.1` 應在 037，
   `Disclaimer Screen` 組將自 7 leaf 增為 9 leaf，Layer 2 之計數與
   granularity 均須重驗。**於 `DECISIONS.md` 預先登記該連帶**，
   不預改任何數字。

---

## 八、停止條件

canon §0 六條，另加本包三條：

7. 步驟 2 之 marker 枚舉結果 ≠ 30／2
8. 步驟 3 之程式化清單與 §5.4 之七節不符且差異未查明
9. 第三輪修正後之 lint 仍有 FAIL

**本包零寫回工作簿。** 13／14 兩包之提交**未授權**。
**不得改動 `scripts/new_feature.py`、`docs/runtime/` 下任何檔案、
任何他 feature 之檔案。**

---

## 九、上繳包要求（`docs/upstream/14_marker_enumeration.md`）

1. §四三條之抄錄核對表（含命中數）
2. `marker_coverage.py` 之輸出（全集、命中表、缺漏）＋ must-hit 實跑
3. 程式化之未涵蓋清單 ＋ 與 §5.4 七節之比對
4. **第三輪修正後之 batch 1 全文** ＋ lint 輸出 ＋ priority 逐條依據
5. 未結 DR 清單（現應為 3 筆）
6. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
7. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 十、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| **DR-PMH3** | `SU9.)`／`SU9.1)` 是否應在 037 —— **若應，48 leaf 之母體即為低估，`Disclaimer Screen` 由 7 增為 9** | 覆蓋完整性 |
| **DR-PMH2** | Power Moding State Matrix Excel（規格稱 `shall not be developed without following`） | `Power Transitions` 批 |
| **DR-PMH1** | CFTS009 之 Off Road+ 行為 | 交付 |
| 13／14 之 commit 授權 | 13 之 pathspec 見其上繳 §10（13 路徑） | 否 |
| Q10、`PROFILE_INTEGRATION.md` | | 否 |

**三筆 DR 皆須向上游發出** —— 其中 DR-PMH2、DR-PMH3 為本輪雙向複驗與
marker 枚舉所生，**若不發，48 leaf 之母體與 ch 9 之判讀背景皆有已知缺口
而無人在追**。

---

## 十一、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §四 |
|---|---|---|
| R-PMH54 | 規格覆蓋以 marker 枚舉為權威（無門檻）；句級 diff 降為輔助 | ✅ |
| R-PMH55 | 無 leaf 之規格內容得限縮條件、不得新增涵蓋（三項判準） | ✅ |
| R-PMH56 | 未涵蓋清單須由程式自 canon 節號全集產生 | ✅ |

三條各管一事。
