# 上繳包 14 —— marker 枚舉、未涵蓋清單程式化與 batch 1 第三輪

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/14_marker_enumeration.md`
- 執行狀態：**步驟 1–6 全部執行完畢。九條停止條件全未觸發**
  （第 8 條之差異已查明，見 §3.2）。
  **零寫回工作簿**；**改狀態 git 零次**；未動 `docs/runtime/` 與他 feature。

---

## 0. 一項事實回報（R-PMH48）

14 §八稱「13／14 兩包之提交未授權」。**13 包已提交為 `d583d9e`**
（Pei 於 14 落檔前指示提交，13 檔 +1838/−144，帶 pathspec）。
依 **R-PMH48**，提交狀態一律由執行層於上繳回報；此處即為該回報。

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH54 | marker 枚舉為權威；句級 diff 降為輔助 | 437 | `96653ba4141df0c0` | `96653ba4141df0c0` | 逐字相符 |
| R-PMH55 | 無 leaf 之內容得限縮不得新增涵蓋 | 598 | `2ed40ce75a1234a6` | `2ed40ce75a1234a6` | 逐字相符 |
| R-PMH56 | 未涵蓋清單須由程式產生 | 356 | `68cd3f7735af913e` | `68cd3f7735af913e` | 逐字相符 |

6 個 placeholder 各命中 1（預期 6）。

---

## 2. 步驟 2 —— marker 枚舉：**30／2，與分析層相符**

**程式**：`scripts/marker_coverage.py`（無門檻、無取樣、無相似度參數）。

### 2.1 ⚠ 首版正規式漏了 `SU1.)` 形態 —— 只得 18／1

首版之 `SU\d+(?:\.\d+)?\)` 要求括號緊接數字或 `.數字`，
而 `SU1.)` 為**數字後尚有一個句點才接括號**。結果：

| | 首版 | 修正後 |
|---|---|---|
| marker 全集 | **18** | **30** |
| 缺漏 | 1（`SU9.1)`） | **2**（`SU9.)`、`SU9.1)`） |
| 章 12 | **全數落空** | `OFF1.)`／`OFF2.)`／`OFF3.)` |

修正為 `(?:\.\d+)?\.?\)`（`(?:\.\d+)?` 收 `SU9.1)`，其後 `\.?` 收 `SU1.)` 之尾點）。
**若未與分析層之 30／2 對照，18／1 會被當成結果收下** ——
**先算後比之價值於此。**

### 2.2 結果（先算後比）

```
PDF marker 全集 = 30；SYS1 缺 = 2

  章  PDF marker                                                    缺
   7  SU1.) SU1.1) SU2.) SU2.1) SU3.) SU4.) SU5.) SU6.) SU7.) SU8.)  2
      SU9.) SU9.1)
   8  SSND 1) SSND 2) SSND 2.1) SSND 2.2) SSND 2.3) SSND 3)          0
   9  PM1)                                                          0
  10  PITA4: PITA5: PITA6: PITA6.1: PITA8: PITA9: PITA10:            0
  11  VRLP1:                                                        0
  12  OFF1.) OFF2.) OFF3.)                                          0

缺漏清單：['SU9.)', 'SU9.1)']
```

**與 14 §3.2 之 30／2 逐項相符。停止條件 7 未觸發。**
**截斷非系統性** —— 其餘五章之末則（`SSND 3)`／`PM1)`／`PITA10:`／
`VRLP1:`／`OFF3.)`）全部對得上。13 包 §8 第 4 項之疑慮**解除**。

### 2.3 must-hit

自 SYS1 側移除一個已知存在之 marker（`SU1.)`，測試替身）：
**缺漏由 2 增為 3 且 `SU1.)` 在清單內 → 攔下 ✅**。`--self-test` exit 0。

### 2.4 §3.3 之 PITA 跳號 —— 複驗屬實，惟其探針法有一處假象

枚舉所得之 PITA 編號為 **`4, 5, 6, 6.1, 8, 9, 10`** —— **跳 1–3 與 7**，
與 §3.3 相符。

**惟**：以子字串探 `PITA1` 會得 `True`，因 **`PITA10:` 含 `PITA1`**。
**枚舉值為權威，子字串探針在此不可用** —— 記此以免日後複驗時被該假象誤導。

依 R-PMH26 之精神，**只登記不開 DR**（上游之編號形式問題）。

---

## 3. 步驟 3 —— 未涵蓋清單之程式化（R-PMH56）

**程式**：`scripts/canon_coverage.py`
**canon**：`docs/runtime/ASPICE_SWE6_AI_Instruction.md`（713 行）

### 3.1 結果

| 項 | 值 |
|---|---|
| canon 節號全集 | **58** |
| lint 宣告涵蓋（`COVERED`） | **10** |
| **未涵蓋** | **48** |

`COVERED` 為 `lint_batch.py` 之常數，`canon_coverage.py` **匯入它**
而非另存副本（R-PMH40 之同一原則）。

### 3.2 與 §5.4 七節之比對 —— **停止條件 8 之差異已查明**

| 清單 | 節數 | 在程式化清單內 |
|---|---:|---|
| 13 包所列九節（實為 10 個節號） | 10 | **10/10** ✅ |
| 14 §5.4 所列七節 | 7 | **6/7** —— **`§5.2` 不在** |

**`§5.2` 不在之原因是我自己造成的**：我在 `COVERED` 中先宣告了 `5.2`
（預備本輪要加之字數檢查）**而該檢查當時尚未實作** ——
清單遂稱「已涵蓋」而實際沒有。

> **這是 R-PMH56 所防之**反向**錯誤**：
> 漏列使人以為未查者已查；**誤列使人以為未查者已查**。
> 前者由 §5.4 抓到，後者由本輪之程式化比對抓到。

**已修**：`§5.2` 之檢查本輪已實作（§5），且將 lint **實際檢查而未宣告**者
（`§5.5`／`§8.4.3`／`§10.2`／`§10.3`／`§10.7`）一併補入 `COVERED`，
由 5 節增為 **10 節**。

### 3.3 程式化多出之 38 節 —— 逐類具名

| 類 | 數 | 節號 |
|---|---:|---|
| meta（非欄位規則） | 5 | §0 Purpose／§1 Language／§2 Core Principles／§3 Workflow／§13 Final Rule |
| parent（其子節另列） | 5 | §4／§5／§6／§8／§10 |
| **其餘欄位／規則節** | **28** | §4.1.x（6）／§4.2／§4.5／§4.6／§5.3／§5.4／§5.6／§8.1／§8.2.x（2）／§8.4／§8.4.2／§8.6／§8.7.x（5）／§9／§10.1／§10.6／§12 等 |

**人讀清單（17 節）為「可由 lint 檢查者」之**策展子集**；
程式化清單（48 節）為「未宣告涵蓋者」之**全集**。** 二者定義不同，
非矛盾 —— 惟 **R-PMH56 令以程式為準**，故 lint 之輸出改為指向該程式，
不再手寫節號。

---

## 4. 步驟 5 —— lint 再擴充：§5.2 步驟字數

新增 **C8**：`normal step <= 12 words`／**`final step <= 18 words`**。

### 4.1 must-hit —— 以第二輪之 batch 1 為天然反例

fixture 保全於 `tests/fixtures/batch01_r2.json`。

```
canon §5.2 步驟字數（normal <=12／final <=18）  **FAIL**  5 處
  -001 step2  25 > 18
  -003 step2  26 > 18
  -004 step1  35 > 12
  -007 step1  30 > 12
  -008 step2  23 > 18
28/29 PASS
```

**⚠ 命中 5 處而下放包 §5.1 列 4 處** —— 多出者為 **`-008` step 2（23 字）**。
下放包所列之四處（`-001`／`-003`／`-004`／`-007`）**全部命中**，
`-008` 為機械檢查所增。**停止條件 8 未觸發。**

---

## 5. 步驟 4 —— batch 1 第三輪修正：**29/29 PASS**

### 5.1 §5.1 步驟字數 —— 五處全拆為三步

| tc | 修正前 | 修正後 |
|---|---|---|
| `-001` | 2 步（step2 = 25 字） | **3 步**（record／wait／check） |
| `-003` | 2 步（step2 = 26 字） | **3 步**（record／no-input／check） |
| `-004` | 2 步（step1 = 35 字） | **3 步**（no-input／wait+read／press+check） |
| `-007` | 2 步（step1 = 30 字） | **3 步**（deliver／read+record／remove+check） |
| `-008` | 2 步（step2 = 23 字） | **3 步**（record／press／read+check） |

### 5.2 §5.2 之單引號 —— 已改直雙引號

`-001` 之 ER：`'loading...'`／`'Loading...'` → **`"loading..."`／`"Loading..."`**。
同一條 TC 內兩種引號並存之情形已消除。

### 5.3 §5.3 priority 逐條重判 —— **P0 4／P1 3／P2 1**

**未為求分布而改值** —— 逐條依 §10.2 之 rubric 重判並於 `reasoning` 首句
載其級別與依據：

| tc | 判 | 依據（reasoning 首句之摘要） |
|---|---|---|
| `-001` | **P0** | **boot/recovery** —— 其失效使開機停在載入畫面而無從進入 last mode |
| `-002` | **P0** | boot/recovery —— Accept 為離開免責畫面之唯一**主動**路徑 |
| `-003` | **P0** | boot/recovery —— 逾時為**被動**路徑；其失效使無人操作之車輛永遠停在免責畫面 |
| `-004` | P1 | **非 P0** —— 其失效使畫面提前消失，而 Accept 路徑仍在（`-002` 已驗），**開機仍可完成** |
| `-005` | P1 | 非 P0 —— comfort controls 之可及性為便利性功能，不阻斷開機亦無安全後果 |
| `-006` | **P2** | **次要／支援** —— 其失效為多顯示一組重複控制，對主要功能影響有限；**與 `-005` 不同級**（該條驗功能之存在，本條驗其抑制） |
| `-007` | P1 | 非 P0 —— pop-up 抑制影響免責畫面之可讀性（legal 要求），**惟其失效不阻斷開機** |
| `-008` | **P0** | boot/recovery —— 免責畫面為 legal 要求，其未顯示即以**未取得使用者確認**之狀態進入 last mode |

**§5.3 之疑慮（「rubric 未被實際套用」）已解** —— 八條不再同值，
且四條**不落 P0** 者各自載明「為何不是 P0」。

### 5.4 ⚠ 重判時之一處自錯 —— **正是 R-PMH41 之形態**

我先替換了 `-008` 之 `reasoning`（改寫為 P0 之依據）**而未改其 `pri` 欄位值**
—— 於是該條之欄位為 `P1` 而理由寫 P0。

**由本輪自加之一致性複驗抓到**（比對每條之 `priority` 與其 `reasoning`
首句所宣告之級別）：

```
  -001  欄位 P0  reasoning 首句 P0  ✅
  …
  -008  欄位 P0  reasoning 首句 P0  ✅
八條全部一致: True
```

**該複驗非下放包所令，為執行層依 R-PMH41「驗證標的須為所欲狀態」自加。**

### 5.5 lint 輸出

```
29/29 PASS
```

另跑：`marker_coverage --self-test` exit 0、`canon_coverage` exit 0、
`check_state_consistency` exit 0、`check_granularity --check-doc-sync` exit 0、
`check_write_back --self-test` exit 0。**六支全綠。**

**停止條件 9 未觸發。**

---

## 6. 步驟 6 —— `DR-PMH3` 之連帶預先登記

已於 `DECISIONS.md` 加一列：若上游回覆 `SU9.)`／`SU9.1)` **應在 037**，
則 `Disclaimer Screen` 組自 **7 leaf 增為 9**，連帶須重驗四項：

| # | 連帶 |
|---|---|
| (a) | Layer 2 之八組計數與 **48 總數**（R-PMH36 之定版數字） |
| (b) | granularity **G1–G5 之分母由 48 變 50** —— `check_granularity.py` 之 `n_leaf` 須改 |
| (c) | `layer3_sections.tsv` 與 `outline_map.json` 之 48 列 |
| (d) | batch 1 須增 2 條 TC |

**本包不預改任何數字。**

---

## 7. 未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為 | **OPEN** | **交付**（§8.4.3） |
| **DR-PMH2** | Power Moding State Matrix Excel | **OPEN** | `Power Transitions` 批之 ch 9 |
| **DR-PMH3** | `SU9.)`／`SU9.1)` 是否應在 037 | **OPEN** | `Disclaimer Screen` 之覆蓋完整性 |

**合計未結 3 筆**（本輪 +0）。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，六項。**

1. **marker 之形態清單本身是列舉**（`SU`／`SSND`／`PM`／`PITA`／`VRLP`／`OFF`）。
   **若規格另有第七種前綴而我未列，枚舉法會靜默漏掉整章** ——
   與 A-PMH08／A-PMH13 同族。**未以「PDF 中所有 `\w+\d+[.):]` 形態」反向掃描
   驗其完備性。** 這是 marker 枚舉法之唯一盲區，且它取代了句級 diff 之判定
   責任，**盲區之代價因而更高**。

2. **`COVERED` 之 10 節係我宣告，未經檢核。** §3.2 已證「宣告可能與實作不符」
   —— 本輪修正了 `5.2`，**但另外九節之宣告是否與其檢查真正對應，
   無任何機制驗證**。應加一項：每個 `chk()` 呼叫附其節號，`COVERED` 由此
   自動產生而非手寫。**本包未做。**

3. **priority 重判為我一人所為，無第二意見。** §5.3 之八條依據皆為我之解讀
   （例如「pop-up 抑制不阻斷開機故非 P0」）。**§10.2 之 P0 含 `safety`**，
   而免責畫面之 legal 性質是否構成 safety，**我判為否，未經覆核**。

4. **`-006` 由 P1 改 P2 使該批出現三個級別，恰好「看起來合理」。**
   我須指出：**我無法排除自己是因為「八條同值看起來不對」而去找理由拆開**。
   §5.3 之下放包措詞（「rubric 未起分辨作用」）本身即帶此暗示。
   **重判之依據我認為站得住，但其動機不純，據實記載。**

5. **第三輪之修正未再經人讀覆核。** 29/29 只證已編碼之規則通過；
   拆步後之步驟是否仍「一步一意圖」（§5.7）、ER 是否仍對應，**須人讀**。

6. **canon 之 58 節係以 `^#{2,4}\s+數字` 抽取。** 若有節以其他形態編號
   （如 `## Appendix A`），**不會被計入全集，遂不會出現在未涵蓋清單** ——
   與第 1 項同型之盲區，未驗。

---

## 9. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1–6 | canon §0 六條 | 未觸發（§5.3 之 priority 依 rubric 重判，非造值） |
| 7 | marker 枚舉 ≠ 30／2 | **未觸發** —— **30／2**（首版 18／1 已查明為正規式缺陷並修正） |
| 8 | 程式化清單與 §5.4 七節不符**且差異未查明** | **未觸發** —— 不符 1 節（`§5.2`），**差異已查明**（我先宣告後實作），已修 |
| 9 | 第三輪修正後 lint 仍有 FAIL | **未觸發** —— **29/29 PASS** |

---

## 10. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 14 — marker enumeration, canon coverage programmatic, batch 1 r3
```

```
git add -- features/power_moding/DECISIONS.md \
           features/power_moding/RULINGS.md \
           features/power_moding/generated/batch01.json \
           features/power_moding/tests/fixtures/batch01_r2.json \
           features/power_moding/scripts/canon_coverage.py \
           features/power_moding/scripts/gen_batch01.py \
           features/power_moding/scripts/lint_batch.py \
           features/power_moding/scripts/marker_coverage.py \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/14_marker_enumeration.md \
           features/power_moding/docs/upstream/14_marker_enumeration.md
```

- **未動 `docs/runtime/`**（含 canon —— `canon_coverage.py` 只讀它）。
- **未動任何他 feature 之檔案。**
- ⚠ index 內仍有併行 session 之 20 個 `vehicle_setting` 檔，**本次仍須帶 pathspec**。

### 10.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | `git status --short`／`git diff --cached --name-only` | 3 |
| **改狀態 git** | `git add` ＋ `git commit`（**13 包**，Pei 指示，帶 pathspec） | 2 |

**13 包已提交為 `d583d9e`。14 包尚未授權。**

---

## 11. 待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| **三筆 DR 之發出** | `DR-PMH1`／`DR-PMH2`／`DR-PMH3` —— **若不發，48 leaf 之母體與 ch 9 之判讀背景皆有已知缺口而無人在追** | DR-PMH1 阻斷交付 |
| **§8 第 1 項** | **marker 前綴清單之完備性未驗** —— 該法已取代句級 diff 之判定責任，其盲區代價更高。建議以「PDF 中所有 `\w+\d+[.):]` 形態」反向掃描驗之 | 建議：優先 |
| **§8 第 3、4 項** | priority 重判為我一人所為；`-006` 改 P2 之動機我已自陳不純 | 建議：覆核 |
| 第三輪 batch 1 之人讀覆核 | 29/29 只證已編碼之規則通過 | 下一批之前 |
| 14 包之 commit 授權 | pathspec 見 §10（11 路徑） | 否 |
