# 下放包 38 —— Table 4-6 之衝突、R-SU43、六列判定核心之改判、DR-SU4

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`37_er_sources.md`；對應上繳：`docs/upstream/33_batch2a_pending.md`
- 裁定狀態：R-SU43 —— 分析層即裁
- **batch 2a 六列之判定核心全部改判 `PENDING`；成因非尾句無來源，是判定核心本身可能誤判合規系統**

---

## 一、上繳包 32 審查判定

**收。§T50a-2 是本 feature 至今最重要的單一發現 —— 它推翻的不是一句 ER，是六列之判定核心。**

### 1.1 §T50a-1 —— 一個物件裡兩句、射程不同，且未逕自拼接

`4907673` 之 **Table 4-6**（`RECOMMENDED`，射程「解除**之後**」）與
**表前 `however` 子句**（`shall`，射程「中斷本身須被 gracefully handled，
使 OTA client 得以繼續運作」）。

執行層之判定正確：**表答否**（時間軸兩端 + 情態為 RECOMMENDED）；
**`however` 子句時點對、情態對、內容也對，惟主詞為 OTA client 而非 head unit**；
`4907440` 恰好講另一半（client 不得影響 host system）而時點為 `when active`。

> **兩個物件各覆蓋一半，交集為空 —— 把它們拼起來是綜合不是引用，
> 我不做，那等於代上游寫需求。**

**此節制正確。** 拼接二個射程互補之物件以造出一個都沒說過的斷言，
其偽裝性極高（二錨皆真實存在、皆可查證），**而合成之命題無人主張過**。

**DR-SU4 之問法採執行層收窄之版本**，見 §四。

### 1.2 §T50a-2 —— **判定核心與 Table 4-6 相衝突**

六列全部斷言 `Version_after equals Version_initial`，
而 Table 4-6 依中斷落在哪個階段給不同要求：

| 階段 | 要求 | 版本 |
|---|---|---|
| download session **之前** | abort + retry next polling | 不變 |
| download session **之中** | save state, abort, 恢復後 retry | 可能變 |
| **deployment or update process 之中** | **Complete the deployment** | **會變** |

而六列 Procedure 第 3 步只寫 `while the update session is in progress`，**未釘死階段**。

**執行層之三項推論全部成立**：

1. 中斷若落在 deployment 階段，**現行 ER 會把一個合規系統判 fail**
2. `015`／`016` 更危險 —— 其 Procedure **主動解除中斷**（reconnect），
   依表列恢復後 client 應續傳，而 TC 恢復後**立刻讀版本並斷言未變，
   未給任何時間界限** —— **讀得早通過、讀得晚失敗，兩者都合規**
3. **與 TC-8 同源**：階段界線在外部不可區辨（R-SU32(iii) 已裁），
   測試者**既無法控制適用哪一列，也無法事後判定適用了哪一列**

### 1.3 分析層之精確化 —— 衝突之強度為「可能誤判」而非「必然衝突」

Table 4-6 為 **`RECOMMENDED`**（SHOULD 級），
故「deployment 中斷後完成部署」為**建議行為**，
不採納者亦不違規。

**但這不使問題變小**：採納該建議之系統**是合規的**，
而現行 ER 會把它判 fail。**一個會把合規系統判 fail 的 ER，
就是一個錯的 ER** —— 其病名為**誤判**，不是「衝突」。

**此精確化不改變處置，但改變 DR 之問法**（§四）。

---

## 二、R-SU43（新條，抄入 RULINGS.md，逐字）

```
R-SU43（判定核心不得斷言一個規格允許其為他值之結果）

實測（上繳包 32 §T50a-2）：`newR1L-SU-011`–`016` 六列之 Final Step
斷言 `Version_after equals Version_initial`，
而 CFTS `4907673` 之 `Table 4-6` 對「中斷落於 deployment 階段」
之情形要求 `Complete the deployment` —— **版本會變**。
即：一個依該建議實作之系統，**會被本 ER 判 fail，而它是合規的**。

裁定：

(a) **ER 之判定核心，其所斷言之結果，須為該情境下規格所允許之唯一結果。**
    規格對同一情境允許多個結果者，斷言其一即為**誤判之源** ——
    合規系統會被判 fail。

(b) **撰寫前之檢定**：對判定核心所斷言之值，回查規格
    「在本 TC 所設之情境下，該值是否可以是別的？」
    **答是 → 該斷言不得作為判定核心。**

(c) **情境未釘死時，須以最寬之情境檢定** —— 本案六列之 Procedure
    只寫 `while the update session is in progress`，
    故其情境涵蓋 Table 4-6 之全部三階段，**檢定須對三者皆成立**。

(d) **釘死情境為一種解法，惟其前提為該情境可控且可判定**。
    本案之階段界線不可觀測（R-SU32(iii)），
    **測試者既無法控制落在哪一階段，也無法事後判定落在哪一階段** ——
    **故釘死之路於本案不通**。

(e) **析取式不是解法**：把 ER 寫成「版本未變**或**版本已更新」
    使任何結果皆通過，**該 TC 即不驗任何事**。
    **涵蓋全部合規結果之斷言，與沒有斷言等價。**

(f) **降階之作法**：原判定核心若因本條不可用，
    **得降為記錄步驟**（`Read … and record …`），
    其值仍為證據而不作判定；**判定核心另尋**。
    無可另尋者依 R-SU42 v2(e) 掛 `PENDING`。
```

---

## 三、六列之改判

### 3.1 版本比對 —— 由判定核心**降為記錄**（R-SU43(f)）

六列之 Procedure 末步與 ER 末行**不再斷言 `Version_after equals Version_initial`**。
版本之讀取與記錄**保留**（其為證據），惟不作判定。

> **併記一項早該看見的事**：上繳包 31 §8 已指出
> 「前半（版本未變）是中斷之後果，**不是『處理得好』的證據**」。
> 本輪證明它連「後果」都不是必然 —— **deployment 階段之中斷，
> 規格反而要求完成**。該句從一開始就不該是判定核心。

### 3.2 判定核心 —— 改為「中斷後系統續行」，掛 `PENDING: DR-SU4`

**test_procedure 末步**（六列同）
```
PENDING: DR-SU4 step to check the observable state showing that the head unit continues operation after the interruption
```
**expected_result 末行**（六列同）
```
PENDING: DR-SU4 observable state showing that the head unit continues operation after the interruption
```

**版本記錄之行改置於末步之前**：
```
(倒數第二步) Read the software version shown on the head unit and record it as Version_after
```
```
(倒數第二行) Version_after is recorded
```

### 3.3 `015`／`016` 之時序問題一併解消

其病為「恢復後立刻讀版本並斷言未變，未給時間界限」（§1.2-2）。
**版本降為記錄後，讀取之時點不再影響判決** —— 該病隨之消失，
**不需另立時間界限**（立之即造值，規格未給任何時間值）。

### 3.4 sibling 區分之暫態

六列之 Final Step 現皆為同一句 `PENDING: DR-SU4 …`，
**字面相同，違 R-SU41(b)**。

**裁定為暫態，明記其恢復條件**：
- 依 R-SU42 v2(e)／R-SU32(d)，掛 `PENDING` 之列本就待上游確認，
  **其 sibling 區分於 DR-SU4 回覆後重建**
- 各列之觸發側狀態（(a2)）**仍留於 Procedure 與 ER 之前段**，未刪
- **DR-SU4 一經回覆，六列之 Final Step 須即依 R-SU41(c) 重建其區分**，
  並重跑遮蔽測試
- **此暫態須逐包揭露** —— 不得因 lint 之 `I-sibling`／`I-cross`
  對 `PENDING` 行不敏感而視為已通過

### 3.5 `PENDING` 行數之變動

| TC | 原 | **新** | 差 |
|---|---:|---:|---:|
| `011` | 3 | **5** | +2（末步、末行） |
| `012` | 0 | **2** | +2 |
| `013` | 0 | **2** | +2 |
| `014` | 3 | **5** | +2 |
| `015` | 0 | **2** | +2 |
| `016` | 0 | **2** | +2 |
| `017` | 3 | 3 | — |
| **合計** | 9 | **21** | **+12** |

**batch 2a 現無一列可交付。** 此為誠實之結果 ——
其成因是規格對本組之驗證面未定義到可判之程度，不是產出品質不足。

---

## 四、DR-SU4 之開立

| 欄 | 值 |
|---|---|
| 事項 | 中斷處理之判定準據 |
| 對象 | `SWE1-FOTA-315`–`320`（batch 2a 六列） |
| 理由 | (i) `4907673` 之 `however` 子句要求 `interrupts shall be gracefully handled so that OTA client continues operation`，惟其主詞為 OTA client，**於 HU 上之可觀測表徵未載**；(ii) `4907440` 述 client 不影響 host system，惟其時點為 `when active`（更新進行中），與「中斷之後」射程不符；(iii) 二者交集為空，拼接即為代上游綜合 |
| **請求 1** | **`OTA client continues operation` 於 HU 上之可觀測表徵為何？**（執行層收窄之問法） |
| **請求 2** | `Table 4-6` 依中斷所落之階段給不同要求，而**階段界線於 HU 外部無可觀測之表徵**。請確認：系統測層級應如何判定中斷處理是否正確，**在測試者無法控制亦無法判定中斷落於哪一階段之前提下** |
| Urgency | **High** —— 阻斷 batch 2a 全部六列 |

**DR 總數由 3 增為 4。** DR 文本同步（T51d）。

---

## 五、任務（T51）

| # | 任務 |
|---|---|
| T51a | **六列之改判產出**（§三）：`011`–`016` 之末步、末行、版本記錄行之改置。`017` 不動。跑 lint，**預期 U=21**。**併報**：`I-sibling`／`I-cross` 之值，及其對本批之覆蓋狀況（§3.4 之暫態揭露） |
| T51b | **`ER_ASSERTIONS.md` 之重掃**：改判後，(b) 無來源之 2 句（`remains operable`／`responds to user input`）是否已自 ER 中移除？**若仍存於非判定之行，其分類與處置為何** —— 陳報，不裁定 |
| T51c | **R-SU43(b) 之回溯檢定**：對現有 17 個 TC 之全部判定核心，逐一回查「該值於本 TC 所設之情境下，規格是否允許其為別的」。**batch 1 之 10 列尤須檢**（其判定核心多為「無提示／無畫面」之否定式，**否定式亦可能有規格允許之例外** —— 如 `176` facet B 之安全通知即為 `175`／`176`A 之例外）。輸出待裁清單 |
| T51d | **DR-SU4 開立與 DR 文本**：`DATA_REQUESTS.md` 新增 DR-SU4（§四之表）；`DR-SU1_SU2_request.md` 增 DR-SU4 節，**其舉證須含 `4907673` 二句之射程對照與 `4907440` 之時點差**（三者皆已實測，可覆核）。**發送者為 Pei** |
| T51e | **T-抄**：R-SU43 逐字 append；索引表現行 42 → **43**。PLAYBOOK 追加二則：(1)「兩個物件各覆蓋一半，拼起來是綜合不是引用 —— 二錨皆真實存在，而合成之命題無人主張過」（出處：上繳包 32 §T50a-1）；(2)「涵蓋全部合規結果之斷言，與沒有斷言等價」（出處：R-SU43(e)） |
| T51f | **git** |

**不在本輪**：`Interruption Handling` 其餘 12 列、`Update HMI` 6 列、寫回。

---

## 六、上繳包要求（`docs/upstream/33_batch2a_pending.md`）

1. T51e 核對結果 + 索引表（現行 43）
2. T51a 之 lint 全輸出（**預期 U=21**）與 §3.4 之暫態揭露
3. **T51c 之回溯檢定 —— 本輪核心**（batch 1 十列之判定核心是否同病）
4. T51b／T51d／T51f 之結果
5. 未結 DR 清單（**4 筆**）
6. 獨立自評 —— 特別回答：**R-SU43(a) 要求判定核心所斷言者為「規格所允許之唯一結果」。
   而規格對多數行為只寫「應如何」未寫「不得如何」——
   嚴格套用之下，是否幾乎所有肯定式判定核心都會因「規格未排除其他結果」而失格？
   若是，(a) 之措辭須收窄；若否，其分界在哪裡**
