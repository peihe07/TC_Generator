# 下放包 23 —— pilot-01 收束、揭露義務入條、寫回前之待裁

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/23_pilot01_closeout.md`
- **本包對交付物之推進：pilot-01 之收束與寫回前置**（R-G31）
- **前置（已查證）**：上繳包 22 已回；`generated/pilot-01.json` 三筆
  （rev3）；lint 二十項行計 0；停止條件 56／57／58 皆 PASS；
  R-DM49 抄錄相符（累計 51）

---

## 一、上繳包 22 之覆核

**核可，無退回項。** 兩道閘閉合，三條 TC 之內容分析層逐條複讀，
無異議。四項具名。

### 1.1 A-DM34 —— R-DM48 之第二個實證，且比第一個強

```
DCSD_DISP_STAT      : 4 "DISP_HOT"
FPDM_DISP_STAT      : 3 "DISP_HOT"
TGW_FPDM_DISP_STATSts: 3 "DISP_HOT"
```

**同一個標籤，跨訊號對到不同的 raw 值。**

R-DM48 原以「同一訊號之六個值裡規則就不一致」立論；本條更強 ——
**跨訊號亦不一致**。即：即使某標籤在某訊號上解得，
也不得把該對應搬到另一個訊號上。R-DM48 之條文補一句，見 §三。

### 1.2 04 輪之修正在本輪兌現

`signal_resolution.py` 之選定判準為 **`MESSAGE.Signal` 兩半皆相等**
（04 輪之修正）。執行層指出：若仍用「第一個含該訊號名之 DBC」，
此處極可能取到 FPDM 側，而 FPDM 側之 `DISP_HOT` 是 3 不是 4。

**一個當時只是「做對」的判準，本輪成為擋住實際錯值的那道牆。**
記明 —— 這類事後兌現若不記，下次會有人問「這個判準有必要那麼嚴嗎」。

### 1.3 §6.1 之限定聲明

閘 (a) 驗的是 **leaf 集合相等**（8／8），
**不驗「某 leaf 被分到的那一組是否恰當」**。執行層主動指出
`Pop Up Handling` 單 leaf 是否為 genuine outlier 仍只有人工論述、
未被任何腳本檢查（B8）。

**正確且必要。** 一個 PASS 若不說它證明了什麼，讀者會替它擴權。

### 1.4 §九第 3 項 —— 提請立條而不自行立條

執行層自發於括號下半寫 `the warning popup is deferred`，
並指出「本輪是自發做的，沒有規則要求」，提請分析層考慮立條，
**不自行立**（Tier 2）。

**採納，見 §三 R-G33。** 其自陳之風險判斷亦採認：

> 讀 036 工作簿的人若只看 `test_item` 上半，會以為 popup 已被測。
> 括號下半之 `the warning popup is deferred` 是唯一的防線。

---

## 二、§九三項自陳之處置

| # | 自陳 | 處置 |
|---|---|---|
| 1 | #4 之 ER 3 可驗、#1 之 popup 不可驗，兩者不對稱；且其論據來自同一份互相矛盾之規格 | **判定成立，#4 維持**；列入 §四之「DR-DM10 回覆後重審清單」 |
| 2 | 停止條件 58 之詞表為自訂，完備性無證據 | **維持 B 類**。其拘束（ER 較長時須先擴充詞表）由執行層自訂且合理，予以追認並入條（§三 R-G33 註） |
| 3 | `test_item` 上半保留而 ER 不驗，落差只靠文字揭露 | **立條**，見 §三 R-G33 |

---

## 三、裁決條文

```
R-G33（test_item 上半之未涵蓋面向須於括號下半明寫 —— 全域）
canon R-S4 定 `test_item` 為兩段式：上半為需求／規格原句 verbatim，
下半為作者生成之測試目的或情境標籤。

本條補其一項義務：**上半之 verbatim 若含該 TC 之 ER 不涵蓋之需求面向
（因 deferred、因 DR 未結、因拆分至他條），該未涵蓋須於括號下半明寫**，
使僅閱讀工作簿之人看得見。

三項細則：
(a) 上半**不得因此刪句** —— 刪句會使工作簿上看不出該 leaf 為部分覆蓋。
    保留並揭露優於刪除。
(b) 括號下半之揭露須指名其未涵蓋之物（`the warning popup is deferred`），
    不得只寫泛稱（`partially covered`、`see notes`）。
(c) 該揭露與 `batch_context.md` 之 `deferred` 陣列須一致；
    後者為完整表，前者為工作簿上之單行防線。

**機器化之判準**（供 lint 日後接入）：對每一 TC，若其 `leaf_id`
出現於同批 `batch_context.md` 之 `deferred` 陣列，則其 `test_item`
括號下半須含該 deferred 項之指名 token。不含即為違反。

理由：`lint036` 沒有、也不容易有一個「test_item 所述是否被 ER 涵蓋」
之檢查（語意判斷）。而 036 工作簿是交付面，讀者未必看得到
`batch_context.md`。**上半宣告要測、ER 不測、而工作簿上看不出來** ——
這是部分覆蓋最可能被誤讀為完整覆蓋之路徑。

實例（上繳 22 §2.3）：Display pilot-01 之 #1，其上半保留
`shall trigger warning popup requests`，而 ER 已收斂為訊號側。
執行層自發於括號下半寫 `the warning popup is deferred`，
本條將該自發處置定為規則。

註（自訂判準之拘束）：凡以自訂詞表實作之停止條件檢查
（如本 feature 之停止條件 58），其詞表非自 canon 或規格導出者，
須於使用處具名其非窮盡性；受檢文本規模擴大時，**先擴充詞表再用**，
不得沿用。
```

```
R-DM48 之補充（跨訊號不可外推）
R-DM48 原載：規格值標籤逐字解得 DBC `VAL_` 者始寫入訊號值，
不得以語意相近或前綴規則外推，理由為「同一訊號之六個值裡規則就不一致」。

**本條補一項更強之理由：同一標籤跨訊號亦不一致。**

實測（上繳 22 §6.2.1，A-DM34）：
  `DCSD_DISP_STAT`       : `4 "DISP_HOT"`
  `FPDM_DISP_STAT`       : `3 "DISP_HOT"`
  `TGW_FPDM_DISP_STATSts`: `3 "DISP_HOT"`

即：即使某標籤在某訊號上已逐字解得，**該對應不得搬至另一訊號**。
值之解析一律以 `MESSAGE.Signal` 兩半皆相等為選定判準
（`signal_resolution.py`，04 輪之修正），不得以訊號名單獨匹配。

本補充不改 R-DM48 之處置規則，只加強其理由與適用範圍。
```

---

## 四、DR-DM10 回覆後之重審清單

DR-DM10(a)（組 A／組 B 何者為準）之答覆到達時，**下列各項須重審**，
不得因「當時已通過自檢」而免除：

| 項 | 重審理由 |
|---|---|
| #4 之 ER 3（`No popup is shown`） | 其論據「未觸發時兩組皆無 popup」為真，但與 #1 被 deferred 之論據來自同一份互相矛盾之規格。若答覆顯示存在第三種讀法，該論據須重估 |
| #1 之收斂範圍 | 若答覆為「組 A 為準」，popup 側即可觀測，#1 得回復其 popup ER（增列，非重寫） |
| 原 #2（005 保護性關閉） | deferred 之解除 |
| `batch_context.md` 之 `deferred` 三項 | 逐項複核其是否仍成立 |
| DR-DM10 之阻斷範圍欄 | 004 popup 側與 005 關閉側之狀態同步 |

本清單寫入 `features/display/BACKLOG.md` 之新節
`## DR-DM10 回覆後重審`，**不入 A／B 分流**（其非未驗項，
是條件性之待辦）。

---

## 五、作業步驟

1. 抄錄 §三之 **R-G33** 入 `docs/fw036/RULINGS_LEDGER.md`；
   **R-DM48 之補充**以「補充」形態追加於 `features/display/RULINGS.md`
   之 R-DM48 條下，**原條文不刪不改**（R-TM13）。
   兩者各自獨立核對表。
2. 依 R-G33(c) 複驗現行三條：`leaf_id` 對 `batch_context.md`
   之 `deferred` 陣列，逐條檢其括號下半是否含指名 token。
   **#3（005）之 leaf 亦在 deferred 陣列中**（005 之關閉側與
   multi-stage 兩項）—— 其括號下半現為
   `(Return path of the ON/OFF decision — verifies the recovery side,
   not the protective shutdown)`，**是否已滿足 R-G33(b) 之「指名」
   須逐字判定並回報**；若不足，補寫。
3. §四之重審清單寫入 `BACKLOG.md` 新節。
4. `A-DM34` 之登記複驗（LOW，非阻塞）。
5. 更新 `docs/INDEX.md`。

**仍不寫回 036 母本** —— 寫回待 Pei 覆核三條後另行裁示。

---

## 六、停止條件

沿用 1–58，另加：

59. 步驟 2 若發現任一條之括號下半不含其 deferred 項之指名 token →
    補寫後重跑 lint 與 §9 自檢第 2 項（sibling 相異）；
    **補寫若使任二條之括號下半逐字相同 → 停並回報**。

**全部 git 操作屬 Pei。**

---

## 七、上繳包要求（`docs/upstream/23_pilot01_closeout.md`）

1. R-G33 與 R-DM48 補充之抄錄核對表（各自獨立）
2. R-G33(c) 之三條複驗結果（含 #3 之逐字判定）
3. `BACKLOG.md` 之重審節全文
4. 若步驟 2 有補寫：修訂後之 `test_item` 全文 ＋ 重跑之 lint ＋ 自檢第 2 項
5. 未驗項分流（A／B，R-G29）
6. 建議之 commit 訊息與 pathspec（不執行）
