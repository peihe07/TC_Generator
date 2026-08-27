# DELIVERY_NOTE — Bed Lowering Mode (FW036)

日期：2026-08-27
工作簿：`features/bed_lowering/workbook/bed_lowering_11.xlsx`
sha256 `353b87f59a19121d23d1018330b043b8957699f156273b675f979f31995574a1`
工作簿鏈：`00 起建 → 01 pilot → 02 B1 → 03 清 S/AB → 04 B1 修訂 → 05 B2 → 06 B3 → 07 B4 → 08 B5 → 09 B6 → 10 B7 → 11 B7 文法修正`（下放包 16 §一-1）
狀態：**三項交付前置全數完成（見 §8）。交付授權可請求 —— 該請求屬 Pei（Tier 3），執行層不代為請求。**

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

### 3.2 同族形態：013/014 與 015/016 之驗證重疊（B7 全查所見）

`013-01~03`／`014-01~03`（依**內容類型**切：資訊／軟鍵／訊息，各分日夜）與
`015-03`／`016-03`（依**顯示裝置**切：HU／EVIC 文字之日夜可讀性）在驗證面上重疊 ——
同一塊畫面內容在日夜兩條件下之可讀性被兩組 leaf 各驗一次。

**成因同 §3.1：切分來自上游 037 本身**（一組依內容類型、一組依裝置）。
**保留未合併、未製造差異**，兩組各自追溯其 leaf，括號下半已載區分 token。

---

## 4. 最終判定之判別方式（量級揭露）

### 4.1 本 feature 與同儕基準之對照

母體逐欄標明（R-G8）。判準三分，分子定義如下：

- **A**：最終 ER 之判定對象為訊號
- **B**：最終 ER 之判定對象為人（目視／可聽），但流程含訊號注入或讀取
- **C**：全程不出現任何訊號

| 本 | 母體 | A | B | C | **B+C（判定需要人）** |
|---|---|---|---|---|---|
| **bed_lowering（本交付）** | 151 | **29（19.2%）** | 80（53.0%）| 42（27.8%）| **122（80.8%）** |
| audio_mgmt B1 | 70 | 0（0.0%）| 6（8.6%）| 64（91.4%）| **70（100.0%）** |
| vehicle_setting VF230 | 457 | 0（0.0%）| 296（64.8%）| 161（35.2%）| **457（100.0%）** |

**兩本同儕之 A 類皆為 0。** 本交付為三本中唯一有訊號級最終判定者。
**80.8% 是 HMI 工作簿之常態形狀，非本 feature 之異常**（上繳 15）。

判定方式細分（B+C 122 條）：目視 120、可聽 2。
逐條清單 `data/nonbus_verdict.tsv`；全 151 列分類 `data/bus_class_all.tsv`。

### 4.2 一個結構性事實

兩本同儕之 A=0 **並非因為它們不用訊號**：

| 本 | 訊號出現於 Procedure | 出現於 ER | ER 含訊號之列 | 落在 ER **最末行**者 |
|---|---|---|---|---|
| VF230 | 572 次 | 388 次 | 296 列 | **0** |
| audio_mgmt B1 | 9 次 | 6 次 | 6 列 | **0** |

訊號一律落在 ER 中段（設定確認），最末行一律是 HMI 觀察。
本交付沿用同一慣例，差別只在另有 29 條之最終判定確實就是訊號值。

### 4.3 本基準之限制（必讀）

1. **可分類之同儕僅 2 本，且皆為本管線產出。**
2. **唯一之非本管線人寫本（`vehicle_setting` CFTS044，191 列）套不上判準** ——
   其 ER 為自由散文，結構化訊號記法 0 列，
   樣本 `CAN signal to be trigger System update CAN value to HMI HU show...`
   同一句同時是訊號斷言與畫面斷言，機器無從區分判定對象。
   **故本基準未涵蓋「人手寫的 HMI 工作簿長什麼樣」。**
3. AMFM v1 tagged 交付本於本機取不到（`inputs/` 不入版控）。
4. 逐本之訊號識別規則不同（v3 `$MSG.Sig$` vs vehicle_setting 之 R-VS52 override
   `Send CAN:`／裸 `MSG.Signal`）。**判準未變，變的是「什麼字串算訊號」**，
   逐本記錄於上繳 15 §二；若對 VF230 套 v3 正則，命中為 0，會得出假結論。

### 4.4 本節數字之更正始末（R-TM13，不刪原文脈絡）

上繳 13 §六-2 曾載「非匯流排可判 **38 條、25.2%**」。**該數字為估值而非量測** ——
按整批粗估，B5／B7 整批計、B3／B4 只計特定母號、其餘四批一條未計，
**各批判準不一致且未載分子定義**，即 R-G8 所禁之形態。

上繳 14 以逐條機檢重算為 **122 條、80.8%**，低報逾三倍；逐批亦全錯
（B5 記 20 實 18、B3 記 4 實 22、pilot／B1／B2／B6 記 0 實 13／3／13／29）。
原文於上繳 13 保留並標明為錯，未刪。

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

**四筆 DR 皆於 2026-08-27 送出**（`DATA_REQUESTS.md` 送出日已回填），待上游回覆。

**DR 回覆後之動作**（逐條相同）：代入實值 → 機檢 + lint → 以
`scripts/write_back.py --start-id 152` 追加寫回（**不覆蓋既有 151 列**）。
DR-3 另牽動 `033-02`／`034-02` 之複驗（其比對基準為草稿圖，PDO 完稿後基準會變）。

---

## 6. coverage gap 13 條

全表見 `features/bed_lowering/COVERAGE_GAPS.md`（leaf id／037 原文摘句／
不生成之理由／建議驗證方式四欄）。此處不重抄，**但依下放包 14 §一-6
轉載其判準模稜之揭露**：

### 6.1 判準與其模稜之處（轉載自 `COVERAGE_GAPS.md`）

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
散見各批上繳之自陳節，於此集中：

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

## 8. 交付前置 —— **三項全數完成**

| # | 前置 | 完成方式 |
|---|---|---|
| 1 | R-G14 抽樣覆核 | **已完成**。Pei 指定 **B7 全查**（執行層於上繳 13 §四之二所建議者），分析層 2026-08-27 執行完畢：16 條生成 TC 與 13 條 coverage gap 逐條讀畢，**判定通過、無 A 類項**。分流之兩條分界複核成立，`coverage_gap` 13 筆與 `COVERAGE_GAPS.md` 13 列逐 req_id 相符，PENDING 四條之標記與 DR-4 對應正確，per-TC reasoning 僅見於兩條委派條（合 profile §4）|
| 2 | 判定方式量級處置 | **已解消，無需裁定**。上繳 15 之同儕量測顯示兩本同儕 B+C 皆 100%，本交付 80.8% 反而更佳（§4.1）。執行層原於上繳 14 建議「重評目視判定可接受之裁定」，**該建議已撤回** |
| 3 | 四筆 DR 送出 | **已完成**。Pei 於 2026-08-27 全數送出 |

**B 類機械修正一項**（B7 全查所出）：`information` 為不可數名詞，
`013-01`／`014-01` 之 `test_procedure` 與 `expected_result` 共 4 處 `are` → `is`，
已以 `patch_cells.py --set-from` 僅改該 4 格寫回（工作簿 `10` → `11`），
round-trip 不符 0、保全計數全等、全簿 151 列 lint clean。

**交付授權屬 Pei（Tier 3）。執行層不請求、不預作。**

### 未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | **Pei 已送出 2026-08-27**；7 條 PENDING ＋ 各批暫定車速值待複驗 |
| DR-2 | Off-Road 2／Easy Entry ride-height 對映 | **Pei 已送出 2026-08-27**；牽動 §7-2，不阻斷交付 |
| DR-3 | Bed Lowering cluster graphics definition（PDO）| **Pei 已送出 2026-08-27**；1 條 PENDING ＋ 2 條連動複驗 |
| DR-4 | 三份 HMI_BP 指引（W-01／X-01／L-34）| **Pei 已送出 2026-08-27**；4 條 PENDING；017-05 不因此重新分流 |

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

---

## 10. 交付檔（Tier 1 產出，2026-08-27）

| 項 | 值 |
|---|---|
| 檔名 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_BedLowering_20260827.xlsx` |
| 落點 | `features/bed_lowering/output/`（gitignored，FO §6 守則 2）|
| SHA256 | `efa1da4c8f59c98d3dc2096041df87fded93c9e7173731003c9ed8ea46bc4b69` |
| 產生器 | `scripts/emit_delivery.py`（來源 `workbook/bed_lowering_11.xlsx`）|
| sidecar | 同名 `.sha256`，同目錄 |

### 10.1 產出後驗收

| 檢查 | 結果 |
|---|---|
| 正規化前後結構計數 | members 48／sheets 9／legacy DV 4／**x14 DV 1**／extLst 3 —— **全等** |
| digest 冪等 | 重跑正規化後 SHA256 不變 —— 可重現，足以綁定 tag |
| 交付檔 lint（跑在 `output/` 之檔，非工作副本）| **clean — 0 findings**，151 列 |
| 逐列 vs `data/testrail_new.tsv` | 151／151，差異 **0** |
| `PENDING` 殘留 | **0**（IN §8.4.3 成立，可出貨）|
| FO §6 守則 2 | `output/` 由 `.gitignore:35` 排除，產出未碰任何 tracked 檔 |

**正規化會重建整個 zip**（成員依檔名重排、時戳歸零），故結構計數於正規化**之後**
再驗一次 —— 一次靜默掉了 x14 下拉之重建，其產物與正常產物同樣讀得開，
差別只在客戶開啟時 R 欄下拉不見了。

### 10.2 Tier 3 —— 尚未執行

**受控文件提交與 release tag 均屬 Pei（FO §0 Tier 3，不可委派）。**
執行層產出交付檔並備妥 tag 所需之值，未請求授權、未代為提交、未建 tag。

tag 建議名 `fw036-bedlowering-v1`，annotation 應載：
輸出檔名、上表之 SHA256、`done-region hash: N/A - BLANK start (R-BLM3)`、
`rows: 0 preserved / 151 new (0 placeholder) / 151 total`、
`coverage: 176/176 leaves`、lint 結果、四筆未結 DR、
以及 §2 之文件級追溯粒度。

**tag 應指向本交付紀錄所在之 commit**，非分支 tip ——
tip 隨時可能被併行 session 推進（`fw036-display-v1` 即為此特意往回指一個 commit）。

