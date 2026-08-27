# DELIVERY_NOTE — Bed Lowering Mode (FW036)

日期：2026-08-27
工作簿：`features/bed_lowering/workbook/bed_lowering_10.xlsx`
sha256 `8adbbe864dd2a56ef38c93776dedc34b7ad63e874b72de6c700a5dcb6b31728e`
狀態：**交付準備中，尚未可交付** —— 下放包 14 §四之三項前置未完成（見 §8）。

---

## 1. 交付範圍與計數

母體：037 `Analysis Report` **218 資料列**（分母皆標明，R-G8）。

| 項 | 數 | 分母 | 處置 |
|---|---|---|---|
| Heading 列 | 42 | 218 | 標 `No TC — Heading; refer to child IDs`，不生成（R-BLM2）|
| leaf（TC 生成母體）| **176** | 218 | 下分三路 |
| ├ 生成 TC | 163 | 176 | 其中 151 已寫回、12 PENDING 未寫回 |
| └ coverage gap | 13 | 176 | 不生成，見 §6 |

**覆蓋台帳結清：163 + 13 = 176／176，未歸屬 0、重複歸屬 0**（機器對帳，上繳 13 §二）。

交付本 **151 列**（工作簿列 10–160），TC ID `newR1L-BLM-001` … `newR1L-BLM-151` 連續無跳號。
逐批：pilot 13、B1 6、B2 26、B3 31、B4 12、B5 20、B6 31、B7 12 = 151。

---

## 2. 追溯粒度之揭露（R-BLM5）

**`Specification Reference`（N 欄）151 列同值**，為單行常數：

```
SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)
```

**不帶章節號。** 成因：上游 037 之 `HMI Source ID` 欄 218/218 列相異值數為 **1**，
本身即不帶章節號（A-BLM4 全表實測）；SYS1 側雖有 `{檔名}_{章節號}` 格式之 70 列，
但兩者相交為空 —— 037 之 `SYS-HMI-RA-BLM-nnn` 不出現於 SYS1，
SYS1 之 NRL 號與章節號不出現於 037。錨定原則禁止自行推定章節號。

**交付面之後果**：審查者**無法自 N 欄定位到規格章節**。
定位須經 `Requirement or Design ID`（D 欄，`SWE1-HMI-BLM-nnn-mm`）→ 037 →
`Requirement Description` 之路徑。

**此為已知代價，非缺陷** —— 其成因（A-BLM4）與裁定（R-BLM5、profile §1 之
`[OVERRIDE IN §10.7(b)]`）皆有紀錄。

---

## 3. 上游重複之揭露（A-BLM11）

037 之 **006 群**（`Bed Lowering request`）與 **020 群**（`Bed Lowering Mode enable request`）
在「靜止／0 MPH／任意檔位」三條件上逐條對應，是上游自身之重複。

後果：**兩對 TC 之 `Test procedure` 與最終步驟逐字相同**

| 對 | TC ID |
|---|---|
| `SWE1-HMI-BLM-006-03` / `SWE1-HMI-BLM-020-03` | `newR1L-BLM-022` / `newR1L-BLM-031` |
| `SWE1-HMI-BLM-006-05` / `SWE1-HMI-BLM-020-05` | `newR1L-BLM-024` / `newR1L-BLM-033` |

**處置：保留未合併，且未製造差異。**

- 未合併：IN §8.2.1 尊重上游分解，合併等於替上游決定兩條 leaf 是一條。
- 未製造差異：改用不同邊界值可讓自查全綠，但那是憑空造出上游沒有的區分，
  會使交付本「看起來有兩種覆蓋」而掩蓋「其實測的是同一件事」。

四條各帶 per-TC 鏡映註（`reasoning` 欄，不入工作簿）。區分僅存於
`Test Item` 括號下半與 `Expected Result` 措辭。

---

## 4. 最終判定之判別方式（量級揭露）

**本節之數字曾於上繳 13 §六-2 誤報為「38 條、25.2%」，已更正。**
原數字按整批粗估、各批判準不一致，屬 R-G8 所禁之「未載明分子之比率」。
下表為逐條機檢重算，分子定義逐項寫明。

母體：**已寫回 151 列**。

| 口徑 | 分子定義 | 條數 | 佔 151 |
|---|---|---|---|
| **A** | 最終 ER 之判定對象為 `$MESSAGE.Signal$` | 29 | 19.2% |
| **B** | 最終 ER 之判定對象為人（目視／可聽），但流程含訊號注入或讀取 | 80 | 53.0% |
| **C** | 全程不出現任何訊號 | 42 | 27.8% |
| **B+C** | **最終判定需要人** | **122** | **80.8%** |

判定方式細分（B+C 122 條）：**目視 120、可聽 2**。

逐批分佈（B+C）：

| 批 | 條數 |
|---|---|
| pilot | 13 |
| B1 | 3 |
| B2 | 13 |
| B3 | 22 |
| B4 | 12 |
| B5 | 18 |
| B6 | 29 |
| B7 | 12 |

**這是什麼意思**：台架若僅具訊號注入與擷取能力，**122 條（80.8%）之最終判定
仍需人執行**，其中 **42 條（27.8%）連注入都用不上**（純畫面導覽與目視）。
A 類 29 條可全自動判定。

**本節據實陳述現況，不預設結論**（下放包 14 §一-4）。處置待 Pei 裁。
逐條清單：`data/nonbus_verdict.tsv`（122 列）；全 151 列之分類：`data/bus_class_all.tsv`。

---

## 5. PENDING 12 條（生成而未寫回）

依 IN §8.4.3，含 PENDING 之工作簿不得出貨，故此 12 條**不在交付本內**。
**其未涵蓋於此明列，不默記。**

| req_id | DR | 批 | TC 內容位置 |
|---|---|---|---|
| `SWE1-HMI-BLM-022-02` | DR-1 | B1 | `features/bed_lowering/batches/B1/b1_tcs.json` |
| `SWE1-HMI-BLM-022-03` | DR-1 | B1 | `features/bed_lowering/batches/B1/b1_tcs.json` |
| `SWE1-HMI-BLM-022-04` | DR-1 | B1 | `features/bed_lowering/batches/B1/b1_tcs.json` |
| `SWE1-HMI-BLM-007-03` | DR-1 | B2 | `features/bed_lowering/batches/B2/b2_tcs.json` |
| `SWE1-HMI-BLM-007-04` | DR-1 | B2 | `features/bed_lowering/batches/B2/b2_tcs.json` |
| `SWE1-HMI-BLM-021-04` | DR-1 | B3 | `features/bed_lowering/batches/B3/b3_tcs.json` |
| `SWE1-HMI-BLM-021-05` | DR-1 | B3 | `features/bed_lowering/batches/B3/b3_tcs.json` |
| `SWE1-HMI-BLM-033-04` | DR-3 | B4 | `features/bed_lowering/batches/B4/b4_tcs.json` |
| `SWE1-HMI-BLM-016-04` | DR-4 | B7 | `features/bed_lowering/batches/B7/b7_tcs.json` |
| `SWE1-HMI-BLM-016-05` | DR-4 | B7 | `features/bed_lowering/batches/B7/b7_tcs.json` |
| `SWE1-HMI-BLM-023-01` | DR-4 | B7 | `features/bed_lowering/batches/B7/b7_tcs.json` |
| `SWE1-HMI-BLM-023-02` | DR-4 | B7 | `features/bed_lowering/batches/B7/b7_tcs.json` |

按 DR 歸屬：**DR-1×7、DR-3×1、DR-4×4**。

**DR 回覆後之動作**（逐條相同）：代入實值 → 機檢 + lint → 以
`scripts/write_back.py --start-id 152` 追加寫回（**不覆蓋既有 151 列**）。
DR-3 另牽動 `033-02`／`034-02` 之複驗（其比對基準為草稿圖，PDO 完稿後基準會變）。

---

## 6. coverage gap 13 條

全表見 `features/bed_lowering/COVERAGE_GAPS.md`（leaf id／037 原文摘句／
不生成之理由／建議驗證方式四欄）。此處不重抄，**但依下放包 14 §一-6
轉載其判準模稜之揭露**：

## 判準與其模稜之處

二分判準（R-BLM2）：**可功能化改寫為 HMI 可觀察行為者生成；純設計驗證性質者不生成。**
逐條理由見上表第三欄。下列兩點為判準套用時之模稜處，依下放包 13 §三
「寧可揭露過多，不可默默吸收」一併揭露：

1. **`017-05`（手部觸及包裝符合 HMI_BP_X-01）判為 gap，而形態相近的 `016-04`／`016-05`／
   `023-01`／`023-02`（符合 W-01／L-34）判為 PENDING。** 四者都是「符合某份 HMI_BP 指引」，
   分開的理由是驗證對象不同：016／023 驗螢幕上的文案與軟鍵外觀，指引到手即可目視比對；
   017-05 驗實車手部包裝，指引到手仍需人因試驗。**此一分界為執行層之判斷，非 037 明載。**
2. **`013-01`～`03`／`014-01`～`03` 判為可生成，而同母號之 `-04`～`-07` 判為 gap。**
   前者只說「日／夜條件下可見」，可於台架以環境光設定觀察；
   後者附加「從舒適駕駛姿態」「不需前傾／彎腰／扭身」，那是姿態判準。
   **同一母號之下拆兩邊，界線落在原文有無姿態語彙。**

---

## 7. 操作化判斷清單

下列判準為**執行層將 037 之定性描述轉為可判準則**所定，**非規格明載**。
散見各批自陳，於此集中：

| # | 條目 | 037 原文之限度 | 執行層所定之判準 |
|---|---|---|---|
| 1 | `002-04`／`002-05` 姿態 | `supports spraying out`／`supports debris and water draining out`，無角度或高度值 | 「後角落低於降床前記錄值」「後角落低於前角落」|
| 2 | `041-01`／`041-02` 懸吊設定 | `Off-Road 2`／`Easy Entry Mode` 兩模式名 | 以「達到最高／最低回報值」代替 —— `$ASCM_FD_1.*_Lvl$` 之 VAL_ 僅 `254 NOT_INIT`／`255 SNA`，**無列舉可對應該兩模式名**（DR-2）|
| 3 | B7 日／夜環境光 | `daytime`／`nighttime conditions`，**無 lux 門檻** | 「daytime ambient lighting」「nighttime ambient lighting 且顯示切夜間模式」|
| 4 | `015-02`／`016-02` 字級 | `sufficient text size for reading`，無 pt 值 | 「不小於周邊本文」「不小於其他 EVIC 訊息」|
| 5 | B6 `039` 群選單改動 | `modifiable head unit menu configurations`，**改動途徑未載** | 以 `Open the head unit menu configuration` 泛稱書寫，實際路徑待執行者補 |
| 6 | B6 全批導覽路徑 | 只給入口名稱（APPS menu／Controls tab／Home Screen／app drawer）| 以名稱書寫，不造點擊路徑（R-BLM7 使 PDF concept screens 不入語料）|
| 7 | 各批暫定車速值 | 只寫「非 0 MPH」「moving」 | 1／2／5／10／15 Km/h 諸值，**複驗義務掛 DR-1 結案** |
| 8 | `003-04`／`009-02`／`033-03`／`034-03` | 「不由他處承載」之斷言 | 以「他處不顯示」佐證 —— **「沒有」難以窮舉**，實作上限於 tester 可見畫面與已綁 DBC 之訊號集合 |

---

## 8. 交付前置（未完成，不得請求授權）

依下放包 14 §四，下列三項未完成前不得請求 Tier 3 交付授權：

1. **Pei 之 R-G14 抽樣覆核**（至少 1 批全查 + 其餘批各抽 1 parent）。
   **執行層建議全查批取 B7** —— 其 13/16 分流是本 feature 影響面最大之
   執行層獨力判斷（上繳 13 §四之二）。
2. **§4 之量級問題處置** —— 80.8% 而非原報之 25.2%，量級與分析層當初
   裁定「目視判定可接受」時所據者不同。
3. **四筆 DR 之送出決定**（全部動作在 Pei）。

### 未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；7 條 PENDING + 8 項暫定車速值待複驗 |
| DR-2 | Off-Road 2／Easy Entry ride-height 對映 | 草案已登記，送否 Pei 決；牽動 §7-2 |
| DR-3 | Bed Lowering cluster graphics definition（PDO）| 草擬完成，送出待 Pei；1 條 PENDING + 2 條連動複驗 |
| DR-4 | 三份 HMI_BP 指引（W-01／X-01／L-34）| 執行層登記，草擬待分析層；4 條 PENDING |

---

## 9. 附表

| 檔 | 列數 | 內容 |
|---|---|---|
| `data/testrail_new.tsv` | 151 | TC ID／req_id／test_set／priority／design_method／寫回列號 |
| `data/bus_class_all.tsv` | 151 | 全批之 A／B／C 分類與最終判定方式 |
| `data/nonbus_verdict.tsv` | 122 | B+C 之逐條清單 |
| `data/pending_ledger.tsv` | 12 | PENDING 逐條、所屬 DR、內容位置、結案動作 |

**本 feature 為 BLANK 起建、無既有 TestRail 案例**，故 `testrail_new.tsv` 為
新建清單而非新舊對照。若實有既有案例需對映，**停下回報，不自行推定對映關係**
（下放包 14 §三）。
