# 上繳包 39 —— T57 執行結果（下放包 44）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`44_rov_b.md`
- **ROV-B lint：20 項全 0 ＋ U=0 ＋ `I-cross=5`**（**惟首跑 `R=6`，已逕行修正**）
- **遮蔽測試擴至全 38 個 TC：逐字相同 0 組**

---

## 1. T57a —— ROV-B 產出與 lint

| 列 | TC ID | 037 | 錨 | 設計法 |
|---|---|---|---|---|
| 10 | `newR1L-SU-032` | `097` | `4907880` | 決策表 |
| 11 | `newR1L-SU-033` | `099` | `4907882` | 功能測試 |
| 12 | `newR1L-SU-034` | `100`（逾時） | `4907883` | 功能測試 |
| 13 | `newR1L-SU-035` | `100`（取消） | `4907883` | 功能測試 |
| 14 | `newR1L-SU-036` | `101` | `4907884` | 決策表 |
| 15 | `newR1L-SU-037` | `102` | `4907885` | 決策表 |
| 16 | `newR1L-SU-038` | `103` | `4907886` | 功能測試 |

**`PENDING` 0｜涵蓋 037 列 6｜TC 7。**

### 1.1 ⚠ **首跑 `R=6` —— pre_conditions 以 `and` 併二條件於同一行**

```
| 11 | newR1L-SU-033 | pre | 多條件並列於同一行 | 3. An ROV forced update campaign is staged for this vehicle and the "ROV Forced …
```

六列皆同型（`033`／`034`／`035`／`036`／`037`／`038`）——
下放包 44 §二之 pre_conditions 第 3 行寫成
`… campaign is staged for this vehicle **and** the … pop-up is displayed on the head unit`，
**二個條件併於一行**，觸發 R 檢查（R-9(a)：一行一條件）。

**執行層逕行拆為二行**，四條件逐項核對：

| 條件 | |
|---|:--:|
| 不改變驗證單元 | ✅ 同二個條件，只是各佔一行 |
| 不改變錨 | ✅ |
| 不增刪 `PENDING` | ✅ |
| 理由可自既有條文直接導出 | ✅ **R-9(a)**，且 lint 之 R 檢查即其機器化 |

**修正後 `R=0`。**

### 1.2 lint 全輸出（修正後，逐字）

```
python3 scripts/lint036.py <rov_b 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=0  V=0  I-cross=5   exit 0
```

**20 項全 0 ＋ U=0**，與 §三 之預期相符。

`I-cross=5` **全為半窗，零配對**：`032`／`035`／`036`／`037`／`038` 無 `until` 子句；
`033`（`until the installation ends`）與 `034`（`until it closes`）為完整窗。

> **執行層驗證時預估 4，實測 5** —— 其差在 `034`／`035`：
> 二者同為 `100` 之拆分，而**只有 `034` 之 procedure 帶 `until it closes`**
> （`035` 之觸發為使用者主動取消，無等待段）。**預估把二者當同形，實際不同。**

---

## 2. T57b —— 七份 `test_item` 上半之逐字核對

| TC | 037 | 結果 |
|---|---|---|
| `032` | `097` | ✅ 逐字（含 `Not_Prohibited` 底線寫法） |
| `033` | `099` | ✅ 逐字 |
| **`034`** | `100` | **非單一連續段** —— 見下 |
| `035` | `100` | ✅ 逐字（s1＋s2，**相鄰**） |
| `036` | `101` | ✅ 逐字（含 `Not Prohibited` 空格寫法、`popup` 非 `pop-up`） |
| `037` | `102` | ✅ 逐字 |
| `038` | `103` | ✅ 逐字（含 `then ROV Update Service` 之語法殘留） |

### 2.1 `034` 之上半為 **s1 ＋ s3**（跳過 s2），**合法而須記其委派**

037 `100` 實測五句：

```
s1. …shall start a response timer upon displaying the … pop-up.
s2. If the user cancels the pop-up, …shall notify…          ← `035` 取此
s3. If no user selection is received within the configured timeout, …shall notify…   ← `034` 取此
s4. Upon receiving the cancellation or timeout notification, …shall set FOTA_Install to Not Accepted…
s5. ( $FOTA_Install$ = [Not Accepted]) After setting…, shall reset FOTA_Install to Nothing to report.
```

**二句各自逐字**，其拼接依下放包 41 §二-1 之先例（`131` 之 s1＋s5）為**合法摘句**。

**且此處之情形比 `131` 更清楚**：s2 **不是未涵蓋，是委派給 `035`** ——
二 TC 各持其一。**已記入 `REASONING.md`**（T57d 未令，執行層自補）。

### 2.2 ⚠ **s4／s5 二句無 TC 涵蓋 —— 依 `132` s2 之先例記為間接涵蓋**

其內容為「收到取消或逾時通知後，將 `$FOTA_Install$` 設為 `[Not Accepted]`
再重設為 `Nothing to report`」——**全屬車輛屬性之內部狀態變化，不可觀測**。

**與 `132` 之 s2 同族**：**有自己的點但該點不可觀測，
且其失效必然表現在外部後果上**（不設 `Not Accepted` 則安裝仍會開始，
而「安裝不開始」正是 `034`／`035` 之 ER）。

**故記為間接涵蓋，不另開 DR。** 已入 `REASONING.md`。

---

## 3. T57c —— 遮蔽測試（全 **38** 個 TC）

`scripts/mask_test.py` 擴至六個產出腳本（pilot／batch01／batch02a／batch03／rov_a／rov_b）。

| 項 | 值 |
|---|---:|
| 回測集 | **38 個 TC** |
| 配對 | **703 組** |
| **Final Step 逐字相同** | **0 組** |
| 僅差 `PENDING` 佔位 | **21 組** |

**21 組全部出自 batch02a（`011`–`017` 兩兩，`C(7,2)=21`）** ——
即下放包 38 §3.4 之**已知暫態**（六列 Final Step 現皆為 `PENDING: DR-SU4 …`），
**其恢復條件為 DR-SU4 回覆後依 R-SU41(c) 重建區分**。

**ROV-B 未新增任何相同配對** —— §五 所指之二對皆通過：

| 對 | 其 Final Step 之判定對象 |
|---|---|
| `034` vs `035` | `after the pop-up has closed **without any user selection**` vs `after the user **has cancelled** the pop-up` |
| `036` vs `037` | `returns to the screen shown before the pop-up`（**取消成功**） vs `remains displayed and offers no skip / ignore / dismiss control`（**取消不可得**） |

---

## 4. T57d —— `REASONING.md` 補記

依 T57d 令記四項，**另自補二項**（§2.1／§2.2 之 `100` 句分配與 s4／s5 之間接涵蓋）。

其中 `037` 之一項值得單獨提出：

> **不取首選為錨**：路徑 A 之**首選 `4907884` 分 0.566**，而其述**允許**取消或忽略之條件
> —— **與本列之規定相反**。錨取候選 **#4 `4907885`（分 0.407）**。
>
> ⚠ **本例比 `177` 難抓**：`177` 之首選分僅 **0.174**（低分易察覺），
> **本列之首選分 0.566 而內容相反 —— 高分而錯。**

**執行層已實測覆核該三數**（0.566／0.407／排名 #4），與下放包所載逐項相符。

---

## 5. T57e —— ROV-C 五列之材料索引與屬性

| 037 | `25a` 起始行 | Description 中之 `$…$` 屬性 |
|---|---:|---|
| `089` | 99 | `$Speedometer$` |
| `098` | 379 | **無** |
| `107` | 739 | `$HU_Scheduled_Install$` |
| `108` | 779 | `$Cellsignal$` = `[0 OR 1 OR SNA]`／`$LTE_Status$` |
| `109` | 819 | `$FOTA_Status$` |

### 5.1 ⚠ **ROV-C 之屬性與 ROV-B 不同族，其可觀測性須逐個判**

ROV-B 之三屬性皆為 CarPropertyManager 之 FOTA 狀態（一律不可觀測）。
**ROV-C 之五屬性中至少二個性質不同**：

- **`$Speedometer$`（`089`）** —— 車速。**其為車輛之物理狀態，台架上可控亦可讀**
  （儀表板即其顯示），**與 FOTA 內部狀態不同族**。
- **`$Cellsignal$` = `[0 OR 1 OR SNA]`（`108`）** —— **其值域寫成一個析取式字串**，
  **不是三個值之列舉**。`[0 OR 1 OR SNA]` 究竟是「值可為 0、1 或 SNA」
  抑或字面即為該字串，**037 自身答不出** —— **同 B-12 之形態**（值域數不清）。
- `$LTE_Status$`／`$HU_Scheduled_Install$`／`$FOTA_Status$` —— 疑同 ROV-B 族。

**故 ROV-C 起草前，五屬性須逐個判其可觀測性**，
**不可比照 ROV-B 一律排除**（`$Speedometer$` 若可觀測，排除它反而會失去一個真實之判定對象）。

已入 `BACKLOG.md` **B-13**。

---

## 6. 未結 DR 清單（**5 筆**，不變）

| DR | 阻斷 | Urgency |
|---|---|---|
| DR-SU1 | `001`／`002`／`003`；`005` 待釐清 | High |
| DR-SU2 v3 | (d) 第四型 4 列 | High |
| DR-SU3 | `017` | Medium |
| DR-SU4 | `011`–`016` | High |
| DR-SU5 | `021` ＋ `131` s4 | Medium |

**全案 `PENDING` 43 行**（不變）｜**可交付候選 21 列**（14 ＋ ROV-B 之 7），與 §三 相符。

---

## 7. 獨立自評（入 BACKLOG）—— §五-6：`deferral policy` 之前提是否可驗

**答：現況不可驗，但它不是一個「無從確認」之前提 —— 其可觀測之代理就在本批內。**

**(甲) 題目之診斷正確。** `032`／`036`／`037` 之 pre_conditions 寫
`whose deferral policy permits／prohibits deferral`，而該政策實為
`$FOTA_Delay$` 之值 —— **CarPropertyManager 屬性，台架不可觀測**。
**測試者無法確認自己佈置的前提已生效。**

**(乙) 但本批恰好提供了它的外部代理，而且是雙向的。**

| `$FOTA_Delay$` | 其外部表徵 | 出處 |
|---|---|---|
| `[Not Prohibited]` | 彈窗**提供** cancel 控制項 | `036` 之 ER 1（`offers a cancel control`） |
| `[Prohibited]` | 彈窗**不提供** skip／ignore／dismiss | `037` 之 ER 2 |

**即：`036` 與 `037` 各自之判定對象，正是對方之前提的可觀測代理。**

**(丙) 惟不可逕以其為 pre_conditions —— 那會構成循環。**
若 `036` 之 pre 寫「彈窗提供 cancel 控制項」，而其 ER 也驗「彈窗提供 cancel 控制項」，
**該 TC 即自我驗證**（前提與結論同一）。**這是本題真正的難處，而非可觀測性本身。**

**(丁) 三個可行方向（不裁）**：
- **(甲解)** pre 保持以政策描述，**但於 `REASONING.md` 明記其為不可驗之前提**，
  並記其代理在 `036`／`037` 之 ER —— **承認限度，不假裝**；
- **(乙解)** pre 改以**佈置動作**表述（`Stage a campaign with deferral permitted`）——
  **測試者能確認自己做了什麼，即使不能確認系統收到了什麼**；
- **(丙解)** 求 `$FOTA_Delay$` 之診斷讀取手段（DR-SU2 第二型）——
  **惟其為 High 之 DR 再加一列，而 (乙解) 已足以執行**。

**執行層傾向 (乙解) ＋ (甲解) 併用** —— 前者使步驟可執行，後者使限度可見。
**本輪未改**（其為 pre_conditions 之文字，屬分析層）。

**(戊) 一項通則**：本例顯示**「前提不可驗」與「前提不可佈置」是兩回事**。
測試者可以**佈置**一個政策（在伺服器端設定），只是不能**確認**它已生效。
**現行條文（R-SU25／R-SU39）只分「可觀測」與「可觸發」，
未分「可佈置而不可確認」這一種。** 已入 `BACKLOG.md` **B-14**。

---

## 8. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **pre_conditions 之 `and` 併行**（執行層已逕行拆二，請追認） | §1.1 |
| 2 | **`deferral policy` 前提之處置**（執行層傾向 (乙)＋(甲) 併用） | §7 |
| 3 | **ROV-C 之五屬性須逐個判可觀測性** —— `$Speedometer$` 疑可觀測 | §5.1 |
| 4 | **`$Cellsignal$` = `[0 OR 1 OR SNA]`** —— 值域數不清，同 B-12 | §5.1 |
