# 下放包 14 —— framework.md 缺檔（分析層之漏）、D7 Test Set 分歧、B1 審查、-001/-002 裁定、T20

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`13_dr_triage.md`；對應上繳：`09_batch_b1.md`
- **B1 十則不退回重做**：追溯、訊號、marker、拆分判斷、取樣紀律皆正確；缺陷集中於 Test Set 之歸屬與一項覆蓋疑點
- **仍不寫回、不 git**

---

## 一、分析層之誤（本輪三項）

### 1.1 `-013` 之方向寫錯（包 12 §6.2-4）

我書「解鎖方向（`-005`／`-013` 之 ≤3 MPH）用 raw 77」。
037 之 `-013` Method 逐字為 `send a speed above 5 MPH` —— **上鎖**。
執行層查證後更正並據更正值生成，正確。

> 該處若照抄，`-013`／`-014` 兩則之 raw 全錯，而**自檢抓不到**
> ——「用及 §3.1 raw 者標 A-DD6」只驗有無標記，不驗方向。

### 1.2 DR-DD7 文稿之範圍窄於實情

我所擬之稿只問 `-010`／`-012`。執行層以 18 欄為鍵之分組實測：
**4 組、11/28 leaf**，且**其中 5 則在本輪 B1 之內**。
執行層不改待發稿而回報為正確 —— 稿是我寫的，**由我改**（§六）。

### 1.3 **`framework.md` 從未落檔**（本輪最重之一項）

包 03 §五 提請鎖定，Pei 准。包 03 §六 之任務表將其列為
「（待裁後）framework.md 落檔（§五 准後）」——**而包 04 起，
我未將其列入任何一輪之任務表**。執行層未收到落檔指令，故未落。

**實測**：`features/driver_distraction/` 全樹搜 `**/framework*` → **0 命中**。

**後果二**：

1. **IN §4.1 明定** framework 為「prerequisite for Test Set」、
   「must exist before TC writing begins」。**14 則 TC 已在其不存在之下產出。**
2. **自檢第 1 項之標籤逾越** —— 其文書「Test Set 名詞片語、能力層級、
   無 Test Group 前綴、拼寫一致」，**未宣稱比對 framework**（標籤誠實）；
   惟 IN §9-1 之原文為「matches `framework.md`」。
   **該項無從執行，因為比對標的不存在。**

**歸屬**：漏在分析層（未下指令），非執行層漏做。

---

## 二、D7 —— Test Set 名與經核准之 Layer 2 分歧（6/10）

包 01 §三 之 Layer 2，經包 03 §五 提請、Pei 准鎖：

| # | Test Set（**經核准**）| leaf |
|---|---|---|
| 1 | `Body Off Init` | 001–002 |
| 2 | **`Speed Monitoring`** | 003–008 |
| 3 | `Lockout Enforcement` | 009–012 |
| 4 | **`Lockout Tables`** | 013–016 |
| 5 | `Hong Kong Market` | 017–024 |
| 6 | `Market Speed Gating`（PENDING）| 025–028 |

B1 實際所用：

| leaf | B1 所用 | 經核准者 | 判 |
|---|---|---|---|
| 003–008 | `Speed Threshold Judgment` | **`Speed Monitoring`** | **不符** |
| 013–016 | `Lockout Enforcement` | **`Lockout Tables`** | **不符** |
| 009–012（pilot）| `Lockout Enforcement` | `Lockout Enforcement` | 符 |

**成因非執行層擅改** —— 比對標的不存在（§1.3），無從對齊。
**惟結果須更正**：`013`~`016` 若掛 `Lockout Enforcement`，
該 Test Set 將橫跨 `-117`/`-118`（存取阻擋與通知）與 `-120`/`-121`
（Lockout Table 之表適用）二個不同能力，**IN §4.1.3 之「過粗」反模式**。

**裁定**：依經核准之 Layer 2 更正（T20a）。
若執行層對 `Speed Monitoring` vs `Speed Threshold Judgment` 有實質理由，
**循 framework 修訂提出**，不以 TC 欄位既成事實變更之。

---

## 三、B1 審查 —— 通過，一處理由更正、一處待量測

### 3.1 `-003` 不拆 —— **結論採納，理由更正**

執行層引 IN §5.7「one trigger → multiple consequential outcomes」。
**該條要求「同一 trigger」，而本則有二**（raw 129 之上升、raw 77 之下降）
——**引據不成立**。

**成立之理由如下，取代之**：

> `-003` 之 source `-114` 所命者為「**監看 `$Speedometer$` 以啟閉受限 feature**」
> 之能力，其驗證對象為**規則整體**。5/3 之雙門檻為**遲滯（hysteresis）**——
> 遲滯之定義即「上行門檻 ≠ 下行門檻」，**任一單邊皆無法承載該性質**。
> 故本則之驗證點為一，非二；step 2 與 step 4 合為該單一驗證點之組成。
> 拆之則產出二則與 `-007`（`-116`）／`-005`（`-115`）幾近重複之 TC，
> 而 `-114` 所命之遲滯性質**反而無人驗**。

執行層自評 §13.4 之判斷正確，**理由改依本節**（T20b：更新該則 reasoning）。

### 3.2 ⚠ Lockout Table 之負向配對（**待量測，勿逕補**）

`-013`／`-015` 各取一個標 `L/O` 之樣本，斷言其被鎖。

**問題**：如此無法區辨「表被正確套用」與「**全部都鎖**」。
Lockout Table 之要義為**選擇性**（L/O 與非 L/O 之別）；
IN §7 逐字：「Enumerated supported items → ALWAYS pair with at least one
unsupported negative TC」。

**不逕補** —— 補之須先確認該負向面**由誰所有**（IN §8.2.1／§8.4.2）：

- **T20c**：037 之 `-013`~`-016` 全 20 欄、CFTS022 之 `-120`／`-121` 全欄，
  逐字搜是否載非 `L/O` 側之行為（如 `not marked`／`remain available`／
  `no lockout` 之類）
- **載**：屬本 leaf 所有 → 於同則加一負向斷言（取一非 `L/O` 樣本，
  ER 斷言其仍可存取），**不另立 TC**（同一 trigger 之另一後果，IN §5.7）
- **未載**：**登 `COVERAGE_GAPS.md`**，不造、不擴入（§8.4.2）；
  於 `-013`／`-015` 之 reasoning 載明該面未涵蓋及其理由

### 3.3 通過之項（不修）

| 項 | 判 |
|---|---|
| T18b 之 token 掃描給「12 leaf、0 未涵蓋」，回讀 037 原文推翻為 10 | **正確，且 §10 保留誤導性機器輸出並在旁註明其何以錯 —— 此為本輪最佳實踐** |
| `-001`／`-002` 未臆造施加路徑（未去 LID 搜 `Body`／`Sleep` 近似名）| **正確**（R-13）|
| A-DD7 由「眼熟」轉為 18 欄分組之量測 | **正確**。「眼熟不是結論，分組才是」採為一般拘束 |
| 自檢由硬編改為推導（AC 別／profile §1／§4 P0 集合／procedure 之 raw）| **正確**，且 pilot 回歸仍 21 PASS 即其證 |
| `Database Entry - License Key Entry` 未查即不取 | **正確** |
| §5.2 超限依 R-DD15(d) 改步驟不改尺 | **正確** |
| 自檢第 9 項假 FAIL 之歸因（檢查器過時，非 TC 缺陷）| **正確**，且記錄以免日後誤讀 |
| `-005`／`-007` 未取「3 至 5 MPH 之間」之任意值 | **正確**（§8.4.1）|

---

## 四、`-001`／`-002` —— 裁定：**先窮盡內部，再登 DR**

三案（甲索取具名識別碼／乙逕登 DR／丙判為台架能力）之前，
**尚有未查之內部來源**。此為 SYSAD 一案之同型處置（下放包 13 §一：
查遍內部方知 DD5／DD6 無內部解）。

**T20d**（逐項唯讀，查得亦不逕用）：

1. **CFTS022 全表**搜 `Body OFF`／`Body Off`／`sleep`／`wake`：
   其是否載該電源狀態之定義，及是否給出**具名識別碼**
2. **037 全 28 leaf**：`-001`／`-002` 以外之列是否於他處給該激勵之名
3. **`features/power/` 與 `features/power_moding/`** 之
   `RULINGS.md`／profile／`feature.yaml`：是否已有 Body OFF 電源時序之
   **已裁綁定**（唯讀，**不得代改他線任何檔**）

**判準（重要）**：

- (1)(2) 查得具名識別碼 → 循 R-DD5／R-DD6 v2 四庫查對，**內部可解**
- **(3) 查得 → 不得逕用。** 他 feature 之綁定是**該線對其需求**所裁；
  本線之 `-001`／`-002` 是否為同一概念，**須分析層確認**後方得引用。
  執行層只回報「該線如何施加 Body OFF」，不作同一性判斷
- 三者皆無 → **登 DR（乙式）**，文稿由分析層擬，問二事：
  該激勵之具名識別碼為何、台架上如何施加 Body OFF 電源時序與終止 DD process

`-001`／`-002` **維持不入批次**至上述有結果。

---

## 五、DR-DD7 改稿（範圍擴至 4 組 11 leaf）

原稿（包 10 §四）**整段替換**為下稿：

> **DR-DD7 — Identical AC2 text across multiple leaf pairs in FM-WI-FSM-037-A03**
>
> Four groups of leaves in FM-WI-FSM-037-A03 are byte-identical across all
> 18 content columns, differing only in the leaf id and the Source
> Requirement ID:
>
> - `-004` / `-006` / `-008` — sources `SYS-RA-Driver_Distraction-114`,
>   `-115`, `-116`
> - `-010` / `-012` / `-014` / `-016` — sources `-117`, `-118`, `-120`, `-121`
> - `-018` / `-020` — sources `-125`+`-126`, `-125`+`-127`
> - `-022` / `-024` — sources `-125`+`-128`, `-125`+`-129`
>
> In total 11 of the 28 leaves, all of them AC2 rows. The corresponding AC1
> rows do differ from one another, each following the wording of its own
> source requirement.
>
> The effect is most visible for `-012`: its source `-118` specifies the
> lockout-notification behaviour, but its AC2 text states
> `HMI keeps the corresponding feature locked`, which is the `-117` outcome.
>
> Question: are these AC2 rows intended to be identical (i.e. a single
> fail-safe behaviour restated once per source requirement), or should each
> follow the outcome of its own source requirement? As written, each group
> yields test cases with the same verification target, distinguished only by
> traceability.

**狀態**：DRAFTED（未發送）。**必發等級不變**（品質旗標，非阻斷）。

---

## 六、任務（T20）

| # | 任務 |
|---|---|
| **T20a** | **落 `features/driver_distraction/framework.md`**（IN §4.1.5：僅 Layer 1 ＋ Layer 2 ＋ Layer 3 對照表）。Layer 2 逐字取 §二 之經核准六組；組 6 標 `PENDING（DR-DD1）`；Layer 3 依包 01 §三 之 CFTS Heading 母號（-110／-119／-123／-130）。**落檔後依其更正 B1 之 Test Set**：`-003`~`-008` → `Speed Monitoring`；`-013`~`-016` → `Lockout Tables` |
| T20b | 自檢第 1 項改為**對 `framework.md` 實際比對**（讀檔取 Layer 2 集合，逐 TC 驗其 `test_set` ∈ 該集合且與其 leaf 之分組相符）。pilot ＋ B1 全數重跑 |
| T20c | §3.2 之量測（037 `-013`~`-016` 全欄 ＋ CFTS022 `-120`／`-121` 全欄，搜非 `L/O` 側之表述）。**載→補負向斷言於同則；未載→登 `COVERAGE_GAPS.md` 並於 reasoning 載明** |
| T20d | §四 之三項唯讀查證。**(3) 只回報，不作同一性判斷；不得代改他線任何檔** |
| T20e | `-003` 之 reasoning 依 §3.1 更正（遲滯為單一驗證對象；刪去 §5.7 之引據）|
| T-登 | DR-DD7 文稿**整段替換**為 §五 之稿（逐字）；A-DD7 條目已載 4 組 11 leaf，維持 |

**不在本輪**：`-017`~`-028` 之生成、寫回、git、他 feature 之任何寫入、
`RULINGS.sha.tsv`（T17b 維持停止）。

## 七、上繳包要求（`docs/upstream/11_framework_fix.md`）

`framework.md` 全文、T20a 更正後之 Test Set 對照、T20b 重跑之自檢輸出
（含新第 1 項之實際比對）、T20c 量測原始輸出與其處置、T20d 三項查證原始輸出、
T20e 更正後之 reasoning、T-登 結果、未結 DR 清單、獨立自評、R-G8 揭露。
