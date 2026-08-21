# 上繳包 18：軌 C 套用

下放：`docs/fw036/handoff/18_pm_trackC_apply.md`（附件 G／H）
日期：2026-08-21　　**止於工作副本，未送達、未覆寫交付本。**

| 項 | 值 |
|---|---|
| 基底 | `features/power/sandbox/b17/pm_17.xlsx`（`c837096b…`） |
| 產出 | `features/power/sandbox/b18/pm_18.xlsx`（`c61a6d55…`） |
| 寫回 | `features/power/scripts/b18/apply.py` —— `surgical_save` 唯一路徑 |
| 改動 | **26 列／104 格**（四欄） |

> 基底取 `pm_17.xlsx` 而非下放所指之 `pm_16.xlsx`：本包硬性第 4 項
> （`PowerModeSts_Telematic` 全案改寫）即 17 包 §五之裁定，
> 該改寫已於 17 包落於 row 72。`pm_17` = `pm_16` ＋ 該 2 格，別無其他差異。

---

## 一、⚠ 停止條件：附件僅載 26 列，軌 C 為 30 列

附件 G 章節數 **13**（124、125、126、127、149、233、234、
265、266、267、268、269、270）；
附件 H 章節數 **13**（181、275、276、277、278、279、280、281、282、
289、290、291、293）。合計 **26**。

**未獲附件者 4 列：`271`、`272`、`273`、`274`**（皆 `SWE-PM-104`，
TC `-261`／`-262`／`-263`／`-264`）。

- 下放 §任務之列舉本身即只列 26 個號碼 —— 兩份清單皆缺 271–274。
- 附件 G 文末之「軌 C 完成統計」載「附件 G 14 列 ＋ 附件 H 16 列 = 30 列」，
  **與其自身章節數（13＋13）不符**；30 之數係由軌 C 範圍反推，非實點。
- 執行層**未自行補寫該四列**（軌 C 之值須取自 CFTS 原文並註明 object id，
  屬分析層作業；逕寫即為推定，違路線 (c)）。四列維持原狀。

**請分析層補出 rows 271–274 之改寫（附件 I 或補發 G）。**
四列現況（`SWE-PM-104`，與已套用之 row 270 同 leaf）為舊式：
工具行在首、`Read … to check …` 未寫應觀察值。

---

## 二、26 列改動清單

`型式` 欄之「展開自 N」即下放 §任務所指之「與某列相同，僅某處差異」——
已依註記**逐字展開全欄**，非只改差異處（逐列確認見 §三）。

| 列 | Req ID | TC ID | 附件 | 型式 | 步數 |
|---:|---|---|---|---|---|
| 124 | SWE-PM-041 | 115 | G | 全文 | 2→8 |
| 125 | SWE-PM-041 | 116 | G | 展開自 124 | 2→8 |
| 126 | SWE-PM-042 | 117 | G | 展開自 124 | 2→8 |
| 127 | SWE-PM-042 | 118 | G | 展開自 126 | 2→8 |
| 149 | SWE-PM-053 | 140 | G | 全文 | 2→3 |
| 181 | SWE-PM-070 | 172 | H | 全文 | 2→6 |
| 233 | SWE-PM-091 | 223 | G | 全文 | 2→2 |
| 234 | SWE-PM-092 | 224 | G | 展開自 233 | 2→2 |
| 265 | SWE-PM-103 | 255 | G | 全文 | 2→3 |
| 266 | SWE-PM-103 | 256 | G | 同 265 | 2→3 |
| 267 | SWE-PM-103 | 257 | G | 同 265 | 2→3 |
| 268 | SWE-PM-103 | 258 | G | 同 265 | 2→3 |
| 269 | SWE-PM-103 | 259 | G | 全文 | 2→3 |
| 270 | SWE-PM-104 | 260 | G | 全文 | 2→4 |
| 275 | SWE-PM-105 | 265 | H | 全文 | 2→4 |
| 276 | SWE-PM-105 | 266 | H | 全文 | 2→4 |
| 277 | SWE-PM-105 | 267 | H | 全文 | 2→4 |
| 278 | SWE-PM-105 | 268 | H | 全文 | 2→4 |
| 279 | SWE-PM-105 | 269 | H | 全文 | 2→4 |
| 280 | SWE-PM-105 | 270 | H | 全文 | 2→4 |
| 281 | SWE-PM-105 | 271 | H | 全文 | 2→4 |
| 282 | SWE-PM-105 | 272 | H | 全文 | 2→4 |
| 289 | SWE-PM-111 | 279 | H | 全文 | 2→3 |
| 290 | SWE-PM-111 | 280 | H | 展開自 289 | 2→3 |
| 291 | SWE-PM-113 | 281 | H | 全文 | 2→4 |
| 293 | SWE-PM-115 | 283 | H | 展開自 181 | 2→6 |

---

## 三、展開型之逐列確認

| 列 | 註記 | 展開結果 |
|---|---|---|
| 125 | 「與 row 124 逐字相同，僅 PROC 1 與 ER 1 之值改 `10 (Ignition_Pre_Off)`」 | PRE 2 行、PROC 8 步、ER 8 行全數自 124 複製；僅 PROC 1／ER 1 之 `2 (Ignition_Off)` → `10 (Ignition_Pre_Off)`。PROC 2–8／ER 2–8 逐字同 124 |
| 126 | 「與 row 124 相同，兩處差異」 | 自 124 複製；PROC 2 → `0 (Sleep)`、PROC 3 → `network is off`、ER 2 → `0 (Sleep)`、ER 3 → `The network is off`。PRE 及其餘各步逐字同 124 |
| 127 | 「同 row 126，PROC 1／ER 1 之值改 `10`」 | 自 **126**（非 124）複製後改 PROC 1／ER 1。即同時帶有 Sleep／network off 與 Ignition_Pre_Off |
| 234 | 「同 row 233，PRE 2 改 Night；PROC 2 與 ER 2 之 `Day theme` 改 `Night theme`」 | 三處全改：`HMI: "Theme Mode" is set to "Night"`、`… it is the Night theme`、`The HU uses the Night theme`。PRE 1／PRE 3／PROC 1／ER 1 逐字同 233 |
| 266–268 | 「四列同文」 | 265 之 PRE／PROC／ER 逐字複製三份 |
| 290 | 「同 row 289，PRE 3 改」 | 自 289 複製；PRE 3 → `PROXI Country_Code = a value that does not require SOS or Geolocation`。PROC／ER 逐字同 289 |
| 293 | 「與 row 181 逐字相同」 | PRE 4 行／PROC 6 步／ER 6 行全數複製 |

`proc` 與 `er` 之編號行數逐列相等，已於寫入前以 assert 檢核。

---

## 四、lint 前後

| | A | B | C | D | E | F | G | H | I | I-sib | J | K | L | M | N | P |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 前（pm_17） | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| 後（pm_18） | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |

**A–N 全零、E = 0**；P 之 10 筆**全部落在 `test_item` 括號下半**
（rows 57／59 等之三件組），四個作者欄之 P 為 **0** —— 符合驗收條
「P 殘存僅限 test_item 括號下半」。

lint P 仍為 R-1 v2 判準（17 包 §四已裁「排入、feature-scoped、另立包」），
本包未動 `scripts/lint036.py`。

---

## 五、驗收（全 283 列口徑）

```
[OK ] input_not_na: 0          [OK ] listed_in_input: 0
[OK ] triplet: 0               [OK ] send_can: 0
[OK ] pre_unnumbered: 0        [OK ] pre_multi: 0
[OK ] pre_first_is_tool: 0     [FAIL] pre_last_not_tool: 4
[OK ] step_multi_obs: 0        [FAIL] read_without_value: 4
[OK ] nbsp: 0                  [OK ] proc_er_mismatch: 0
```

**二項 FAIL 之 4 列全部為 271／272／273／274** —— 即 §一之未獲附件者。
其餘十項全表為零。**除該四列外，全 283 列已達本包驗收。**

x14 讀回：`Product Document 記錄封面頁` 1 個 DV、
`Test Case Specification&Result` 3 個 DV；`surgical_save` 回報
壓縮成員 **42**（未變）、差異成員僅 `xl/worksheets/sheet6.xml`。

---

## 六、diff 證明（自 `pm_10a5b` 起算之累計）

| 欄 | 變動格數 | 說明 |
|---|---:|---|
| `test_item`（I） | 163 | **僅不可見字元**；`strip_invisible(before) == after` 逐列成立，內容變動 **0** |
| `pre`（J） | 279 | 253（軌 A＋B）＋ 26（軌 C） |
| `input`（K） | 101 | 內聯後改 `NA` |
| `proc`（L） | 279 | 同上 |
| `er`（M） | 273 | 6 列改寫後與原文逐字相同，不計入 |
| `spec_reference`（N） | **0** | 零變動 |
| 其餘各欄 | 0 | 零變動 |

軌 C 之 26 列四欄皆有變動（`verify.py` 之「軌 C 四欄變動列」逐列列出）；
271–274 四列四欄零變動。

---

## 七、17 包 §六 之補答：row 186 現行狀態

**既非留空亦非 `PENDING` —— `input` 欄為 `NA`，判準完整，不須標 `PENDING`。**

移除者為事件之**數量（20）與間隔（100 ms）**，二者原文未載。
現行判準為 `every injected event is buffered without loss` 與
`The buffered event count equals the injected event count` ——
相對於「實際注入者」而定義，不依賴被移除的兩個值。故該步驟未失判準。
（同文另見上繳 17 §六。）

---

## 八、本包是否仍有該驗而未驗者 —— 執行層獨立判斷

**有，五項。**

1. **rows 271–274 未獲附件**（§一）。此為本包**唯一之未完成項**，
   且使全表驗收之二項無法歸零。
2. **附件 G 文末統計與其章節數不符**（14＋16 = 30 vs 實際 13＋13 = 26）。
   該統計並稱「來源明載值者 22 列」「保留抽象動作者 8 列」，
   合計亦為 30 —— **整段統計係按軌 C 範圍書寫，未對照附件實際內容**。
   建議分析層於補發時一併訂正，並複查是否另有列被統計而未寫出。
3. **A-PM13／A-PM14 僅登記於附件，未入 `ANOMALIES.md`。**
   附件 G 標 A-PM13（rows 265–268 ＋ row 13 五列同文）、
   附件 H 標 A-PM14（row 181 ≡ row 293）並稱「併入 DR-PW12 作為第七對」。
   執行層已於 `DATA_REQUESTS.md` 之 DR-PW12 補記第七對；
   **A-PM13／A-PM14 之異常條文本身屬分析層，未代擬。**
4. **row 291 之「geolocation pop-up 或 disclaimer」二擇一未收斂。**
   附件 H 自註「原文未載擇一判準，維持二擇一措辭」。
   該列 PROC 2／ER 2 因而含 `or`，**其判準不唯一**，
   嚴格言之未達 R-11(b)「須寫出應觀察之值」。
   `verify.py` 未命中（其判準僅檢查 `check that` 之存在）。
   **建議標 `PENDING` 或補 DR**，本包依附件逐字寫入，未自行處置。
5. **rows 270／275–282 之首步為抽象動作**（`Bring the HU to Timed mode` 等），
   附件已自註「觸發訊號原文未載，不填推定」。此為刻意保留，
   非疏漏，惟該 8 列之 PROC 1 **不可執行至訊號層**，於此登記。

已知且非本包所生者：`test_item` 括號下半之 10 筆三件組殘留
（歷包明令不動）、lint P/Q/R 尚未 feature-scoped 改寫（17 包 §四已排入）。

---

## 九、引用之裁決編號

R-1 v3(a)(c)(d)（12 包；(d) 經 17 包 §三修訂）、R-6／R-6b、R-7、R-8、
R-9、R-10(a)(b)(c)、R-11(a)(b)(c)、R-12(a)、
**17 包 §五**（`PowerSts_Telematic` 全案裁定）、
R-P310(三)、§8.2.1（TC 側不得合併刪列）、§8.3（sibling 軸）、
§8.4.1（不得造值）、§10.6（strict equivalence）、路線 (c)。

關聯異常／DR：A-PM12、**A-PM13**、**A-PM14**、DR-PW12（第七對）、
DR-PW20（軌 B 之 4 列，本包未涉）。

---

## 十、未做之事

- 未送達、未覆寫任何交付本、未改 `output/`。
- 未改 `scripts/lint036.py`。
- 未改 `test_item`（除不可見字元）、未改 `spec_reference`。
- **未自行補寫 rows 271–274。**
- 未增列、未刪列、未合併列（A-PM13／A-PM14 之重複列照原列數各自寫入）。
