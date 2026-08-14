# 上繳包 02 — R-C4-1／R-C8～R-C10 落實 ＋ 51 節分類 ＋ Phase 2 覆核

執行層 → 分析層。2026-08-14。回應下放包 `03_upstream01_review.md` §3
與 `04_rulings_c8_c10.md` §3。

**結論：六項作業全部完成。R-C9 反向驗證三項全 PASS。51 節分類已產。**
另有兩項須分析層／Pei 裁定，皆為實測與既有條文之衝突，執行層未自裁。

---

## 0. 兩項須裁定者（置頂，其餘為執行報告）

| # | 事項 | 執行層之立場 |
|---|---|---|
| **甲** | **R-C5 對其所列 22 節中之 16 節，前提不成立** —— 該 16 節同時存在於 SR24 基線內，非 SR25 獨有。「屬於 SR25 故 out of scope」之推論對它們失效 | 只陳述實測，**未改 R-C5、未納入分母、未產 TC、未列 BLOCKED** |
| **乙** | **下放包 04 §2 之一處前提有誤** —— amfm 與 sxm 之 Sign-off 已填，R-C9 護欄今日即有效，非「一次也不會觸發」 | 04 加 R-C10 之**結論不受影響**；訂正的是理由 |

---

## 1. §3.1 條文貼入

`RULINGS.md` 現載 **R-C1 ~ R-C10 + R-C4-1**，共 11 條，全部原文照錄。

- **R-C4-1** 置於 R-C1~R-C5 區塊之後、R-C6 之前（03 §7「置於 R-C4 之後」）。
  另立小節而未插入 01 §3 之原始區塊內，是因為那個區塊是下放包 01 的逐字
  複製 —— 在別人的逐字區塊裡插入第三方條文會讓「逐字」不再可驗。
- **R-C8 / R-C9 / R-C10** 另立「下放包 04 §1」小節，並標注 R-C9／R-C10
  適用全 feature、其安置位置待 canon re-sync（04 §4）。

R-C4-1 之兩個母體皆已實測復現：498 母體 → 92 列；403 母體 → 57 列。
`RECON.md` 之 `citation cells with extra lines…: 57` 係 403 母體。

## 2. §3.2 R-C9 覆寫防護 —— 實作 ＋ 反向驗證

### 實作

`scripts/recon.py`：`read_signoff()` 讀既有檔，`write_decisions()` 為**唯一
寫入點**。護欄放在 writer 而不是呼叫端 —— 條文指出的失效形態是「任何人在
任何時候重跑」，任何需要呼叫端記得的設計，防的正好是它防不住的那件事。

偵測判準：條文所定之 `Reviewed by:` 非佔位，**或** SXM 形態之
`- Amendment (…): … directive「…」` 條目（R-C10 註「兩者擇一即可」）。
佔位以 `^[\s_]*$` 判定 —— Projection 用的是 `____________` 而非 `____`，
只比對字面 `____` 會漏掉它。

### 反向驗證（人工填 `Reviewed by: TEST  Date: 2026-08-14` 後重跑）

| # | 應然 | 實測 | 結果 |
|---|---|---|---|
| 1 | 拒絕覆寫 | `DECISIONS.md` sha256 前後皆 `e6283e90a266222c` | **PASS** |
| 2 | 寫出 `DECISIONS.new.md` | 已寫出，55 行 | **PASS** |
| 3 | 非零離開 | `exit=1` | **PASS** |
| 4（自加） | 已簽時不誤發 R-C10 警告 | 0 次 | **PASS** |

訊息實測指名兩檔絕對路徑：

```
REFUSED (R-C9): …/features/comfort/DECISIONS.md is signed
(Reviewed by: TEST, 2026-08-14) and was NOT overwritten.
The freshly generated sheet was written to …/features/comfort/DECISIONS.new.md
instead — diff the two and merge by hand if the new survey should supersede
the signed one.
```

**驗畢已還原**：測試填值復原，`diff` 與測試前逐位元組相同，
`DECISIONS.new.md` 已刪除，重跑確認回到正常寫入路徑（exit 0）。

### 量測工具之一次失誤，一併回報

第一次量測把第 3 項報成 FAIL。成因：zsh 的陣列是 `pipestatus` 且索引自 1，
腳本寫 `${PIPESTATUS[0]}` 取到**空字串**，`[ "" -ne 0 ]` 於是判偽。
**實作沒有問題，量測腳本有問題**；改以直接捕捉 `$?` 重測得 `exit=1`。

記此一筆，是因為它與 A-CF05、與下放包 01 §7 之 `autojunk` 屬同一形態：
**工具無聲取到空值，而空值在比較式裡看起來像一個結論。** 差別只在這次
反過來 —— 假陰性讓好的實作看起來壞掉，前兩次是假陽性讓壞的資料看起來好。

## 3. §3.3 R-C10 空簽署警告

非阻塞，於偵測到「`[PROPOSED]` 存在且 Sign-off 為空」時輸出：

```
WARNING (R-C10): DECISIONS.md carries [PROPOSED] items and its Sign-off block
is an unfilled placeholder — this feature's sign-off state is not knowable
from the repo. Not blocking.
```

Comfort 現即觸發（尚未簽署，屬正確狀態）。已簽時不觸發（上表第 4 項）。

### ⚠️ 乙：對 04 §2 第 2 點前提之訂正

該點稱「全部 feature 之該區塊都是空白範本，偵測器永遠回報未簽署，護欄
形同虛設」。以 `read_signoff()` **唯讀**掃描實測（**未重跑任何 recon**）：

| feature | Sign-off | Amendment | 狀態 |
|---|---|---|---|
| home | 空白範本 | 0 | 不可考 |
| **amfm** | **`PeiPYHsu` / 2026-08-09** | 0 | **已簽** |
| **sxm** | **`PeiPYHsu` / 2026-08-10** | **11** | **已簽（兩形態皆備）** |
| projection | 空白範本（`____________`） | 0 | 不可考 |
| media | — | — | **無 `DECISIONS.md`** |
| privacy | 空白範本 | 0 | 不可考 |
| comfort | 空白範本 | 0 | 未簽（Phase 2 進行中） |

**六個有該檔的 feature 中，兩個已簽。** R-C9 對 amfm／sxm **今日即為有效**。

04 加 R-C10 之**裁決結論不受影響** —— 另外三個確為空白範本，R-C10 仍屬
必要。不成立的是「一次也不會觸發」這句理由。此訂正同時使 R-C8 的份量上升：
amfm／sxm 若被重跑，覆蓋的是**有 repo 證據的簽署**，不只是空白範本。

`media` 無 `DECISIONS.md`，是第三種狀態 —— 既非已簽亦非空白範本。其是否
應有該檔，未查，不臆測。

### 執行層先前之錯誤陳述，一併改正

上繳包 01 §6 稱「Privacy 之 `DECISIONS.md` 已簽署」。實測其 Sign-off 為
`- Reviewed by: ____  Date: ____`，**未簽署**。該陳述無 repo 證據支持。
不重跑 Privacy 的**結論不變**（R-C8 之理由是「無數字更正」，與簽署與否
無關），改正的是理由。04 §2 對此之診斷正確。

## 4. §3.4 不重跑既有 feature

**未重跑任何既有 feature 之 recon。** 本包對既有 feature 的全部接觸限於
唯讀：`read_signoff()` 讀 `DECISIONS.md`、`grep` 讀 `RECON.md`。
`features/{home,amfm,sxm,projection,media,privacy}/` 之檔案**零寫入**。

（上繳包 01 所述 Privacy 之 diff 實測，係在 scratchpad 之複本上進行，
未動本體 —— 此次亦未再進行。）

## 5. §3.5 A-CF09 已登記

見 `ANOMALIES.md`。不回溯補簽（補簽等於偽造當時之簽署行為），自 Comfort 起
依 R-C10 執行；既有 feature 之補記屬 Pei 裁定，另案。

## 6. §3.6 / 03 §3 —— 51 節分類（A-CF08）

產出 `data/sr24_uncited_sections.tsv`（51 列，欄位依 03 §3：`outline`｜
`polarion_id`｜`description` 前 80 字｜`分類`，另加 `cited_descendants`｜
`total_descendants`｜`why` 三欄作為判準之逐列佐證）。
`RECON.md` 新增「Uncited baseline sections」段。

判準寫在 `scripts/classify_uncited_sections.py` 內並可重跑；recon.py 會比對
TSV 與當前 export 之節次集合，不一致即在 `RECON.md` 標 **STALE**（分類與
export 脫節是這類清單最容易發生而最難察覺的失效）。

| 分類 | 節數 |
|---|---|
| `container` | 20 |
| `assumption` | 9 |
| `figure` | 5 |
| **`substantive`** | **17** |

`substantive`：`16.1`、`18.2`、`18.3`、`18.4`、`19.1`、`19.2`、`19.3`、
`20.1`、`20.1.1`、`20.1.2`、`20.1.3`、`20.2`、`20.3`、`20.4`、`20.4.1`、
`20.4.2`、`20.4.3`。

**只分類，未做任何 TC 處置** —— 不產 TC、不入 coverage 分母、不列 BLOCKED、
不補 RD 項目（§8.2、§8.4.2）。

### 兩處判斷須分析層知悉（非機械必然）

1. **6 節只滿足 `container` 定義的一半**。定義為「章級容器標題，**其下層節
   已被引用**」。`1`、`4`、`5`、`8`、`19`、`20` 是章級標題，但下層**全數
   未被引用**。四值必須取一，故歸 `container`（它們確實是無行為敘述的標題），
   但 TSV 逐列記 `cited_descendants`／`total_descendants`，使這 6 節一眼可辨。
   若分析層認為它們應另立第五值，判準與資料都在，改一行即可重跑。
2. **`substantive` 偵測刻意排除 `will` 與 `should`**。定義舉例含 `shall`／
   `will`／編號條款前綴；實作採「編號條款前綴 **或** `shall`／`must`」。
   理由：1.2「Differences between the radios **will** be specified」是對
   **文件**的陳述，1.4「the 12" Portrait UI **will** be a scaled up version」
   是縮放慣例 —— 採 `will` 會把全部 8 節 Assumptions 歸為 substantive，
   分類即失去意義。`16.1` 是唯一靠 `must` 進入者（「HC leds activation
   **must** always be coherent with the signal sent by the HVAC software」），
   非靠條款前綴，特此標明。

### ⚠️ 甲：與 R-C5 之衝突

R-C5 列 22 節「SR25 新增而 037 未分析」之實質需求，裁為 out of scope，
理由是「因 R-C1 定基線為 SR24」。逐節對 **SR24** export 實測：

| | 節數 | 節次 |
|---|---|---|
| **存在於 SR24 基線** | **16** | 18.2、18.3、18.4、19.1、19.2、19.3、20.1、20.1.1、20.1.2、20.1.3、20.2、20.3、20.4、20.4.1、20.4.2、20.4.3 |
| 不存在於 SR24 | 6 | 21.1、21.2、21.3、21.3.1、21.4、21.5（SR24 最大 outline 為 20.4.3，無第 21 章） |

該 16 節**全數**被本次分類為 `substantive`，且與 R-C5 之列舉逐節相符，
含「20.1 ~ 20.4.3（10 項）」之項數。

**衝突所在**：R-C5 之推論是「屬於 SR25 → 因基線為 SR24 → out of scope」。
對這 16 節前提不成立 —— 它們同樣在 SR24 裡。「在 SR25 中出現」不使一個
**同時存在於基線**的節超出範圍。R-C5 對其餘 6 節（21.x）之結論不受影響。

**這正是 03 §3 所指的性質差異**：下放包已指出 51 節「性質與 R-C5 所處置之
SR25 新增內容完全不同，且重要得多」。實測顯示兩者不只是性質不同，而是
**有 16 節重疊** —— R-C5 已對其中 16 節下過 out-of-scope 之結論，而它們
正是這 51 節裡最實質的部分。

**執行層未做也不會做的事**：不改 R-C5、不納入分母、不產 TC、不列 BLOCKED、
不補 RD。D-C10（substantive 之處置）本就待裁，本節只是把待裁的對象講清楚。

**可獨立佐證之界線**：以上全部只用 SR24 export 得出（R-C1 允許）。
「SR25 是否也含這 16 節」**未驗亦不驗** —— 複測需載入 SR25。本節不否定
R-C5 稱其為 SR25 內容之陳述，只指出它們**也在 SR24 裡**，而這足以使
out-of-scope 之推論對它們失效。

## 7. Phase 2 —— `DECISIONS.md` [PROPOSED] 逐項覆核

**未簽署**（R-C10：簽署是 Tier 2，執行層不得代填）。以下為覆核意見，
供 Pei 簽署時參考。9 個 `[PROPOSED]`、2 個 `[PEI]`、1 個 `[RULED]`。

| # | 項目 | 提案 | 覆核 |
|---|---|---|---|
| 1 | draft disposition | discard & regenerate | **同意**。2 列 draft 是空白範本原廠樣本（A-CF07），非人工產出，無可 salvage |
| 2 | safety attributes | SYS2/SYSRA 不進 trace chain | **同意**。037 無 ASIL/FTTI 欄，實測；與 AMFM R6／Privacy 前例一致 |
| 3 | style authority | fallback chain — no done region | **同意方向，但未解析到具體對象**，見下 ⚠️ |
| 4 | test item shape | standard §4.3 tc_title | **同意**。BLANK 無自身前例可循 |
| 5 | test group/set columns | FILL per framework Part N | **同意**。canon §2 於 BLANK 下即為 FILL；R-C6 已定 Test Group = `Comfort` |
| 6 | exemplar source | nearest sibling feature done region, cross-feature: style only | ⚠️ **須指名**，見下 |
| 7 | author on new rows | `PeiPYHsu` | **同意**。與全部 sibling 一致 |
| 8 | spec_reference | SR24 全名 `_{outline}` | **同意**。即 R-C1，已於三處機械強制 |
| 9 | split_mode | standard | **同意**。無反證 |
| 10 | batch plan | group 403 by spec chapter, pilot = smallest coherent batch | ⚠️ **「最小」會選到 1 個 leaf**，見下 |
| — | Test Set table (Part N) | `[PEI]` | Phase 3，本包不動 |
| — | profile [OVERRIDE] | `[PEI]` | Phase 3，本包不動 |
| — | tc_id scheme | `[RULED]` | R-C7 已凍結，不在簽署範圍 |

### ⚠️ 第 3／6 項 —— 「nearest sibling done region」目前解析不到對象

實測各 sibling 之 `workbook_state`（讀其已追蹤之 `RECON.md`，唯讀）：

| feature | state | done rows |
|---|---|---|
| home | PARTIAL_INTERLEAVED | **144** |
| amfm | FULL | 158（但其 RECON 自記為 requirement-family mismatch） |
| sxm | BLANK | 0 |
| privacy | BLANK | 0 |
| projection | （其 RECON.md 無該欄） | — |

**時序上最近的兩個 sibling（privacy、sxm）都沒有 done region。** 提案措辭
「nearest sibling feature done region」若照字面取「最近」，取到的是空集合。
真正有 done region 者只有 home（144 列）與 amfm（158 列，但 amfm 自己的
recon 記載那些列所 trace 的需求族已被裁決取代 —— 借它的**樣式**可以，
借它作**任何**別的用途不行）。

**建議**：簽署時把第 6 項寫成具名對象（執行層傾向 `home` 之 done region），
而非「nearest sibling」。理由：A-026 教訓與 handoff 01 §1 已要求每個字面值
必須回溯至 Comfort 自身 spec 並以 lint 強制；exemplar 來源若不具名，
`cross-feature: style only` 這個標記就沒有可稽核的對象。

### ⚠️ 第 10 項 —— 「smallest coherent batch」機械地選到 1 個 leaf

依章分組之實測分布（403 leaves）：

```
ch 2: 92   ch 3: 14   ch 6:  1   ch 7: 38   ch 9:  8   ch10: 15   ch11: 37
ch12: 22   ch13: 14   ch14: 40   ch15:  2   ch16: 99   ch17: 18   ch18:  3
```

「最小」= 第 6 章，**1 個 leaf**（`SWE1-HVAC-027`）。次小為第 15 章 2 個
（`SWE1-HVAC-105-01/-02`）、第 18 章 3 個。**1 個 leaf 的 pilot 幾乎驗證不到
任何東西** —— pilot 的用途是讓 Pei 在小樣本上看出 prompt 與樣式問題，
樣本數 1 連「同一批內是否一致」都測不到。

**建議**：pilot 取第 9 章（8 leaves）或第 13 章（14 leaves）—— 大到能顯示
批內一致性，小到能逐條看完。此為建議，不自行更改提案。

**另**：03 §6 已預告章 2（92）與章 16（99）合計 47%，Layer 2 granularity
成敗集中於此二章。依章分組會讓這兩章各成一個 90+ 的批，這與其說是批次
規劃，不如說是把問題推遲到 Phase 3；兩章之切分應在 Part N 決定，屆時
batch plan 應隨之改寫，而非沿用「依章」。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 8.1 已驗

1. R-C9 三項反向驗證（拒絕覆寫以 sha256 前後比對、`DECISIONS.new.md` 存在
   與行數、離開碼），加自加之第 4 項（已簽時不誤發 R-C10）。
2. R-C9 偵測器對全 7 個 feature 之判定（唯讀）。
3. R-C4-1 兩個母體（92／57）。
4. 51 節分類 51/51，四值合計等於總數（腳本內以 assert 強制）。
5. R-C5 之 22 節逐節對 SR24 export 查存（16 在／6 不在），SR24 無第 21 章。
6. 各 sibling 之 `workbook_state` 與 done rows（讀已追蹤之 `RECON.md`）。

### 8.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **SR25 是否也含該 16 節** | **刻意不驗** —— 複測需載入 SR25，R-C1 禁止 | 無。甲項之結論只需 SR24 一側即可成立 |
| 2 | **Projection 之 `workbook_state`** | 其 `RECON.md` 無該欄位；未深追 | 低。只影響第 3／6 項之候選清單完整性，不影響 home／amfm 兩個已知對象 |
| 3 | **`media` 為何無 `DECISIONS.md`** | 超出本包範圍，未查 | 低。已記於 A-CF09 |
| 4 | **17 節 `substantive` 之條文內容是否真為 R1L 適用** | 分類只看形態（條款前綴／deontic），**未讀懂內容**，也未查 CFTS043（20.x 之 LATAM 條件）／PDO | 中。若 D-C10 要裁「是否進 RD-1」，適用性是必要輸入而本包未提供。建議裁定前補一輪逐條閱讀 |
| 5 | A-CF02 交付夾、A-CF06 PDF text layer | 同上繳包 01 §7.2，狀態未變 | 低 |

第 4 項是本包最實質的未驗項：**分類回答的是「這一節長得像不像需求」，
不是「這一節是否該由 Comfort R1L 驗證」。** 兩者不同，D-C10 需要的是後者。

### 8.3 未做、亦未偷做者

- 未簽署 `DECISIONS.md`（R-C10：Tier 2）。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未對 51 節之任何一節做 TC 處置（不產、不入分母、不 BLOCKED、不補 RD）。
- 未改 R-C5、未改任何既有條文原文。
- 未執行任何 git 操作。

### 8.4 執行層對「本包可否結案」之判斷

**可結案，但甲項須裁定後 Phase 3 才宜開始。** 理由：甲項牽動的是
「Comfort 的驗證範圍到哪裡」——16 節實質需求究竟在不在範圍內，是
framework Part N 切 Test Set 之前必須確定的輸入。若在 Phase 3 之後才裁，
Part N 可能要重切。

乙項與第 7 節之兩個 ⚠️ 不阻塞 Phase 3，但第 6 項（exemplar 具名）宜與
Part N 同時定，因為兩者都要決定「樣式從哪裡來」。
