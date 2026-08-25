# 下放包 31 —— batch 3 之人讀覆核（不通過）、apparatus 之首次解凍

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/31_batch3_rework.md`
- 前一包：[30_batch3.md](30_batch3.md)
  （上繳 [../upstream/30_batch3.md](../upstream/30_batch3.md)）

---

## 一、30 包之覆核 —— **程序面通過，產出面不通過**

三條抄錄逐位相符；R-PMH111 判別法承載於 `p9_dependency` 欄而非散文；
章 9 規格側全枚舉 30 行、未判定 0；`-023` 依判別法停手且其依據
（**PDF 中該句之前一行逐字為 `HEADUNIT POWER ON:`，即 p9 之欄標題**）
為本輪最有力之一項。

**三項特別記明**：

1. **§2 之 Q5 另立而不併入 Q4** —— 其理由
   「上游若只回一句『是同一個』，Q5 仍未答而我方可能誤以為已答」，
   **是對答覆之形態之預判，非對問題之分類**。正確。
2. **§6.1 之判準改造** —— `source_clause` 之檢查由「看欄位字串」改為
   「**實際回原文件比對**」，**其首次執行即查出 batch 1 之字形差異**。
   且其正規化之代價已具名（若某處引號本身有意義，本檢查看不出來）。
3. **§10 七項自評，第 2 項（`-002` 之停手未經裁定）自陳
   「**這是本包最需要一句話的地方**」** —— 見 §四。

---

## 二、batch 3 之人讀覆核 —— **兩項嚴重，兩項中度**

### 2.1 【嚴重】**五條之 Final Step 無驗證子句**（§5.2B／§5.5）

canon §5.2B 逐字：Final Step **must include verification intent**：
`check that …`／`to verify …`／`… to check …`。

| tc | Final Step 逐字 | 有無 check |
|---|---|---|
| `-017` | `Interact with the pop-up repeatedly beyond ten minutes and record when the radio powers off` | **無** |
| `-018` | `Read the display for the FOTA via Wi-Fi and Charge Now pop-ups` | **無** |
| `-019` | `Repeat the test, dismiss the update on the FOTA pop-up instead, and read the display` | **無** |
| `-020` | `Repeat the test, dismiss the Wi-Fi configuration pop-up instead, and read the display` | **無** |
| `-021` | `Read the radio power state` | **無** |
| `-016` | `Compare the recorded duration with the stated maximum` | **邊界** —— `Compare` 為 §5.1 之 preferred verb，惟未言其判準 |

**六條中五條明確違規、一條在邊界。**

**而 lint 之「§5.2B／§5.5 Final Step 含驗證意圖」標 PASS。**

**這是 13 包 §4.3 已判過之同一違規類型**（當時 `-002`／`-005` 犯之），
**其檢查於 13 包步驟 4 加入，而它現在攔不住這五條。**

→ **R-PMH104(a) 之解凍條件成立**（見 §三）。

### 2.2 【嚴重】`-019`／`-020` 各將兩個獨立分支併於一條（§8.2.2）

`-019` 之兩步為：排程更新 → 顯示後續 popup；取消更新 → 顯示後續 popup。
`-020` 同形（設定 Wi-Fi 完成 vs 取消 Wi-Fi 設定）。

**canon §8.2.2 之壓力測試**：「若只有部分行為失效，我的 pass/fail 判定
是否仍然明確？」——
**排程成功而取消失效時，該 TC 落 fail；取消成功而排程失效時，亦落 fail。
兩個獨立之部分失效落在同一個判定上 → 為 bundling，應拆。**

**其 design_method 標 EP 更使此點清楚** —— EP 之每一等價類各為一條
（batch 2 之 `-012`／`-013`／`-014` 即如此處理）。**同一 feature 內兩種作法。**

→ `-019` 拆為二條、`-020` 拆為二條。**batch 3 由 6 條增為 8 條。**

### 2.3 【中】§4.6 之陳述與 `-016` 之 ER4 自相矛盾

§4.6 記 `-016` 之「未斷言者」為 **`任何逾時秒數`**，理由為權威文本於該處為破句。
**而其 ER4 逐字為 `The head unit stays awake for no longer than 2.5 minutes`** ——
**斷言了一個秒數。**

**分析層複驗權威文本（SYS1 之 9.1，R-PMH75）**：

| 探針 | SYS1 9.1 |
|---|---|
| `2.5 minutes` | **1** |
| `for 60 seconds`（FOTA 句） | **1** |
| `10 minutes` | **1** |

**三個值皆在權威文本內** —— `-016` 之 `2.5 minutes` 與 `-017` 之
`60 秒`／`10 分鐘` **皆有來源，非造值**。

**錯的是 §4.6 之表述**：其應為「**未斷言 `stay awake` 之起算 60 秒**」
（該子句正是 A-PMH16 所查出、SYS1 已刪者），非「任何逾時秒數」。

**形態為同檔內互斥陳述**（R-PMH45）。

### 2.4 【中】`-018` 與 `-019`／`-020` 之 design_method 不一致

執行層 §10 第 4 項已自陳。**分析層判：三者應同為 EP。**

三者同軸（使用者於 FOTA／Wi-Fi popup 上之選擇），
`-018` 之「接受」與 `-019` 之「排程／取消」為同一設定之三個等價類；
**其只因「`-018` 只有一個類」而落 FUNC，是把類之數量當成技術之判準** ——
canon §12 之 first-match 為 `Input partitioned valid / invalid → EP`，
**未要求一條之內須含多類**。

→ 三條（拆分後為四條）之 `design_method` 齊一為 EP。

### 2.5 其餘逐項通過

PC 皆為狀態（R-PMH113 之 `No phone call or projection call is active` 位置正確）；
`source_clause_origin` 六條全為 `sys1_export 9.1`；
`p9_dependency` 逐條具名含「否」；priority P1×6 依據一致。

---

## 三、**apparatus 首次解凍 —— 限於 Final Step 之檢查**

R-PMH104(a) 之條件為「某條已產出之 TC 經**實測**有誤，且該誤為現行檢查所不能攔者」。

**§2.1 即其實例**：五條實測違反 §5.2B／§5.5，而該項檢查標 PASS。

**解凍之範圍嚴格限於該項檢查之強化**，不及其餘。
**新增之檢查須指名其所攔之該項缺陷，不得泛化**（R-PMH104 末句）。

→ R-PMH116。

**⚠ 執行層須先查明其現行判準為何會放行** —— 若其判準為
「含 `check`／`verify`／`record`／`compare` 任一詞」，則 `record` 與 `compare`
之納入即為病灶；**其修正須以本批五條為 must-hit（須 FAIL），
並以 batch 1／2 之現行 final step 為範圍向（須 PASS）**。

---

## 四、`-002` 之停手 —— **裁定：比照 `-028`，不寫入工作簿**

執行層自陳其依 `-028` 之形態停手而該形態之處置是 Pei 裁的。**其停手正確。**

**分析層之裁定**：`SU1.1)` 逐字將行為委於
`based on vehicle architecture. See CFTS009 for clarification.` ——

| 判準（canon §8.4.2） | 結果 |
|---|---|
| 該行為定義於本 spec 抑或外部 spec？ | **外部（CFTS009）** |
| 本 feature 是否持有該外部 spec？ | **否** |
| 不取得而撰寫是否須自行指定架構？ | **是 → 造值（§8.4.1）** |

**三項與 `-028` 完全同型** → **判 out of scope，不寫入工作簿**（比照 R-PMH72）。

**惟其動到範圍**（有 TC 之 leaf 由 47 降為 **46**），
**故須 Pei 核可方生效**（R-PMH1 為範圍條文）。
**核可前 `-002` 維持停手、不產出、不寫入。**

→ R-PMH117（其生效繫於 Pei 之核可）。

---

## 五、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH116（apparatus 首次解凍 —— Final Step 檢查之強化）
依 R-PMH104(a) 解凍，**其範圍嚴格限於 lint 之
「canon §5.2B／§5.5 Final Step 含驗證意圖」一項之強化**，不及其餘。

**解凍之依據（實測，非可能）**：batch 3 之 `-017`／`-018`／`-019`／`-020`／
`-021` 五條，其 Final Step **無任何驗證子句**
（`record when the radio powers off`／`read the display`／
`Read the radio power state`），而該項檢查標 **PASS**。
其為 13 包 §4.3 已判過之同一違規類型，其檢查亦於 13 包加入。

**強化之要求三項**：
(a) 執行層須先查明現行判準為何放行，並具名其病灶；
(b) **must-hit**：本批五條之現行 Final Step 須 **FAIL**；
(c) **範圍向**：batch 1／batch 2 之現行 Final Step 須 **PASS**。

`Compare` 之處置**須具名** —— `-016` 之 `Compare the recorded duration with
the stated maximum` 為 §5.1 之 preferred verb 而未言其判準，
**其屬邊界**；判其通過或不通過皆可，**但須寫出理由並一體適用**。

**本次解凍用畢即恢復凍結。** 新增之檢查不得泛化至其他 canon 節。
```

```
R-PMH117（`-002` 之處置 —— 待 Pei 核可）
`SWE1-HMI-PM-002`（outline 7.1.1，`SU1.1)`）**判為 out of scope，
不寫入交付工作簿**，比照 R-PMH72 對 `-028` 之處置。

依據三項（與 `-028` 完全同型）：
(a) 其逐字將行為委於 `based on vehicle architecture. See CFTS009 for
    clarification.` —— 行為定義於**外部規格**（canon §8.4.2）；
(b) 本 feature **不持有 CFTS009**；
(c) 不取得而撰寫，須自行指定「哪一種架構對應哪一種轉換」，
    **即造值**（canon §8.4.1）。

**本條之效力起於 Pei 之核可** —— 其動到範圍（有 TC 之 leaf 由 47 降為 **46**），
而 R-PMH1 為範圍條文。**核可前 `-002` 維持停手、不產出、不寫入。**

**若 Pei 判其應產出**，則須先取得 CFTS009，或由 Pei 裁定一個架構為準；
**二者皆非分析層可代決。**

`Power Transitions` 組因而為 **5 leaf 有 TC**（`-018-01`～`-05`）、
**2 leaf 停手**（`-023` 依 R-PMH111、`-002` 依本條）。
```

```
R-PMH118（等價類之數量不決定技術）
`design_method` 之選定依 canon §12 之 first-match，
**其判準為輸入是否被劃分為等價類，非該 TC 之內含幾類**。

一條 TC 只涵蓋一個等價類者，其技術仍為 `等價劃分 (Equivalence Partitioning, EP)`；
**不因其只有一類而改判 `功能測試 (Functional based)`。**

依據：batch 3 之 `-018`（接受 FOTA）標 FUNC，而 `-019`／`-020`
（排程／取消、設定／取消）標 EP —— 三者同軸（使用者於同一 popup 上之選擇），
**其差別只在一條之內含幾個類**。canon §12 之
`Input partitioned valid / invalid → Equivalence Partitioning`
**未要求一條之內須含多類**。
執行層 30 包 §10 第 4 項已自陳其一致性可議。
```

---

## 六、作業步驟

1. **抄錄** —— §五之 R-PMH116 ~ R-PMH118 逐字抄入 `RULINGS.md`，附核對表。
   **R-PMH117 標「待 Pei 核可」，核可前不生效。**

2. **Final Step 檢查之強化（R-PMH116）** —— 依 (a)(b)(c) 三項為之，
   `Compare` 之處置具名。**用畢恢復凍結，於上繳明記。**

3. **batch 3 之四項修正（§二）** ——
   (a) 五條之 Final Step 加驗證子句（`-016` 依 §2 之 `Compare` 處置辦理）；
   (b) `-019` 拆為二條、`-020` 拆為二條 —— **batch 3 由 6 條增為 8 條**，
       其 `distinguishing_axis` 逐條具名；
   (c) §4.6 之表述改為「未斷言 `stay awake` 之起算 60 秒」，
       **並記明 `2.5 minutes`／`60 seconds`(FOTA)／`10 minutes` 三值
       經分析層複驗皆在權威文本內**（SYS1 9.1，各 1 命中）；
   (d) `-018`／`-019`／`-020` 之 `design_method` 齊一為 EP（R-PMH118）。
   **修正後重跑 lint。**

4. **`-002` 之登記** —— `ANOMALIES.md` 立一則（比照 A-PMH13 之形態），
   `DECISIONS.md` 記其待 Pei 核可；**`generated/batch03.json` 之 `stopped`
   欄維持該筆並註 R-PMH117。**

5. **`PENDING-ON-DR` 之補登** —— 30 包 §10 第 5 項（`-017` 之二個上限
   何者先到，規格未言）**與第 6 項（A-PMH25）** 依 R-PMH115 補登；
   **其是否須開 DR 由下輪處置，本輪只登記。**

---

## 七、停止條件

canon §0 六條，另加本包三條：

7. 步驟 2 之 must-hit（本批五條之現行 Final Step）**未 FAIL**
8. 步驟 2 之範圍向（batch 1／2 之 Final Step）**有任一 FAIL**
9. 步驟 3(b) 拆分後之 TC 數 ≠ 8

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**R-PMH116 之解凍用畢即恢復凍結** —— 除該一項外不得新增任何檢查。
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 八、上繳包要求（`docs/upstream/31_batch3_rework.md`）

1. §五三條之抄錄核對表（含命中數）
2. 步驟 2 之病灶具名 ＋ must-hit ＋ 範圍向之實跑 ＋ `Compare` 之處置理由
3. **修正後之 batch 3 全文（8 條）** ＋ lint 輸出
4. 步驟 4 之 `-002` 登記
5. 步驟 5 之補登
6. 由程式產生之檢查總表 ＋ **解凍已恢復之聲明**
7. 未結 DR 清單
8. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
9. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 九、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **R-PMH117 之核可** —— `-002` 判 out of scope（leaf 47 → 46）。**若判其應產出，須先取得 CFTS009 或由你裁定一個架構為準** | `-002` |
| 2 | **`DR-PMH8`（5 問 ＋ 更正句）之發出** —— 其更正句未發出期間，上游所知之我方狀態仍與實情不符 | 否，但每日累積 |
| 3 | 9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | 否 |

---

## 十、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §五 |
|---|---|---|
| R-PMH116 | apparatus 首次解凍，限 Final Step 檢查之強化；用畢恢復凍結 | ✅ |
| R-PMH117 | `-002` 判 out of scope，待 Pei 核可 | ✅ |
| R-PMH118 | 等價類之數量不決定技術 | ✅ |

三條各管一事。
