# 02R-A1 — framework 落檔位置之裁定，Part VII 全文與指令

分析層。修正 `02R_framework_lock.md` §4 之 T3。

---

## 1. 裁定

```
R-TM16（Pei 授權分析層裁定，2026-08-20「要併入你裁」）—— framework 併入全域檔

本 feature 之 framework Part 併入 docs/fw036/framework.md，編為 Part VII。
**不建 features/time_management/framework.md。**
02R §4 之 T3（建 feature-local framework.md）撤銷。

依據為實測之既有慣例，非偏好：
1. docs/fw036/framework.md 現含 Part I–VI，六個 feature 之 framework 全在
   該檔（Media / Home / AMFM / SXM / Projection / Privacy）。
2. features/home/ 與 features/amfm/ 目錄實測皆無 framework.md ——
   feature-local framework 檔在本 repo 不存在，一例也沒有。
3. 該檔開頭明載「Part I 之跨領域裁決（orphan routing/attribution、
   lint vs traceability、assumption markers、priority、anchors-as-style、
   blocked-parent proportion）適用於 ALL Test Groups」。framework 落在
   該檔之外，等同不受該六項拘束 —— 那是實質後果，不只是位置問題。

canon §4.1 稱 framework 寫入「framework.md」而未指明路徑，本條以既有
慣例補足：全域檔為唯一位置。
```

`02R` §4 T3 之錯誤與 R-TM7／R-TM11／R-TM12／R-TM13／R-TM14 同族 ——
第六次下放包自身缺陷，成因同型：**未查既有實例即指定作法**。
canon §5a 之「立新規則前先查既有政策」我查了 canon，沒查 repo 現況。

---

## 2. Part VII 全文（貼入 `docs/fw036/framework.md` 檔尾）

```markdown

---

## Part VII — Time and Date (CFTS015)

Ruled by Pei 2026-08-20: feature 名 `Time Management`、目錄 slug
`time_management`（R-TM1）；workbook Test Group 值 `Time and Date`
（R-TM8 —— 落回 canon §4.1.1 通則，因 BLANK workbook 使既有值優先之
條件永不觸發）。下列七 Set 表待簽。

Deliverable workbook: FM-WI-FSM-036-A01 rev C 母本
`…_SWQT_20260817_ext.xlsx`（R-TM5 —— 本 feature 不索取客戶預填件；
交付路徑 `ASW-R2/Time Management/` 實測確無 036，見 A-TM02a）;
RD source `SWE1_Secure_Date&Time.xlsx`（**22 leaf FRs**,
`SWE-RA-TIME&DATE-001…022`）—— **該檔命名不符 037-A03 慣例，身分未定
（A-TM02a，阻塞 D5）**; spec_mode **D** —— clause 權威為 CFTS015 docx
（R1LR Atl-H 25PI3.5, SR26 20250909-1851）; SYS2 export
（`Basic Report`, 227 列）為錨鏈中介。
執行計畫 `features/time_management/RUNBOOK.md`；
rulings `features/time_management/RULINGS.md`（R-TM1–R-TM16）；
anomalies 同目錄 `ANOMALIES.md`（A-TM01–A-TM16）。

**Workbook state**: BLANK —— 無 legacy region、無 done region。
**Style authority: 無。** R-TM10 曾准以 Home done region 為跨 feature 樣式
參照，但其唯一許可來源（Home v2 交付件）經 150 筆 SHA 全域比對確認不在
磁碟上，**R-TM10-A1 全條 SUSPENDED**（A-TM14）。故本 feature 與 SXM／
Privacy 不同：無 fallback chain 可用，TC 生成與 pilot review 一律僅依
條文（§4–§12）與本 feature profile。

**連帶後果（須明記）**：canon §1.1 三層品質結構之第三層（done region
以證據仲裁）在本 feature **不存在**，本 Part 不回復之。reviewer 之發現
不經 done-region check 過濾，分類結果直接成立；pilot 之爭議應預期多於
Home 與 AMFM。

### Layer 2 derivation note — §4.1.2 之第四例退化

與 AMFM／SXM 同型：037 之 `Categorization` 欄實測 **`Functional` 22/22**
（單值），RD 側分群軸零資訊，§4.1.2 之交集退化。

但與 AMFM／SXM 之補救不同。兩者改用「leaf id 機械對映至 spec 章節」，
本 feature **不可行** —— 037 無文件章節引用欄（其 `Source System
Requirement ID` 欄含 `requirement id` 字樣，被 `survey_a03()` 之 forbid
規則排除，`citation column: NOT FOUND` 係「無項可解析」而非「解析失敗」，
A-TM12）。

故 Layer 2 改由 **leaf 標題與 `Requirement Description` 全文之語意軸**
推導，章節僅作外部檢驗。錨鏈另經 SYS2 建立：

```
SWE-RA-nnn → SYS-RA-nnn → CFTS 物件 id → CFTS 章節號
 (037 col2)   (SYS2 col2)   (SYS2 col5)    (docx 標題 {id})
```

實測：SYS2 第 5 欄 227/227 零空白；78 筆被引用 SYS-RA 缺來源物件 id 者
0 筆；docx 88 標題 / 358 物件；71 筆直接可達、5 筆多物件儲存格切分後可達、
**2 筆不可達（A-TM13）**；相異可達章節 **21**。
逐 leaf 對映存於 `features/time_management/data/leaf_to_section_probe.txt`。

### Layer 1 — Test Group

- `Time and Date`（workbook Test Group 欄值 —— BLANK workbook，FILL 適用；
  = spec 文件標題 CFTS_015 Time and Date、= req id family `TIME&DATE`。
  feature 名 `Time Management` 為內部識別，不進工作簿）

### Layer 2 / Layer 3 — Test Sets and their spec sections

Layer 3 = CFTS015 印刷章節號；framework-internal only —— NEVER 寫入 workbook。

| Test Set | 主軸章節（Layer 3） | Leaves (SWE-RA-TIME&DATE-) | n | Status |
|---|---|---|---|---|
| Manual Setting | 1.5.2.3, 1.5.2.6 | 001, 015 | 2 | remaining |
| GPS Sync | 1.3.1.1.3, 1.5.2.4, 1.5.2.5 | 002, 003, 004, 014 | 4 | remaining |
| Master Clock | 1.3.1.1.2, 1.3.1.1.6.2 | 005, 006, 016, 018, 021 | 5 | remaining |
| CAN Transmission | 1.3.1.1.4, 1.5.2.1 | 008, 009, 017, 020 | 4 | remaining |
| Display | 1.3.1.1.1, 1.3.1.1.5, 1.3.1.1.5.1, 1.3.1.1.6.3 | 007, 011, 019 | 3 | remaining |
| Zone and DST | 1.3.1.1.5.3, 1.3.1.1.5.4 | 012, 013 | 2 | remaining |
| Fault Handling | —— 無主軸（見注 2） | 010, 022 | 2 | remaining |

合計 22 = 全 leaf set。

**條件章節不列為任一 Set 之主軸**：`1.5.2.2`（Key Off Status）、
`1.5.2.7`（Output behavior）依 R-TM15 為條件／輸出章節，跨 Set 出現屬預期。

### Granularity check（§4.1.3）

七 Set 範圍 2–5 leaf，皆通過 filter test。**無單葉 Set。**

`Manual Setting`(2)、`Zone and DST`(2)、`Fault Handling`(2) 為三個最小 Set，
皆非 §4.2 之 genuine-outlier 例外而是實質叢集：`Manual Setting` 之兩片呈
時／日結構對稱（`1.5.2.3` Time function setting ／ `1.5.2.6` Date function
setting，同層姊妹節）；`Zone and DST` 之兩片各落單一相鄰姊妹節；
`Fault Handling` 之兩片為同一能力之收送兩端。

**刻意不以時間／日期二分。** 若切為 Time / Date 兩組，`Master Clock` 與
`CAN Transmission` 之每一片都要兩邊各出現一次，Test Set 欄失去索引價值
（§4.1.3「太粗」）。時間與日期在本 spec 共用主控（`1.3.1.1.2` /
`1.3.1.1.6.2` 對稱）、共用傳輸（`1.3.1.1.4` 兼含時日）、共用初始化
（018 跨兩者），是同一能力之兩個資料欄位。
先例同源：AMFM 注 2（band 是切分軸非 Set 邊界）、SXM `Browse`（類別是
資料軸）、Privacy 注 2（Service/HMI 是軸）。

### 相鄰組界線（§8.2.1 —— 寫 TC 時據此避免重複覆蓋）

三處鄰接，由 leaf 描述全文比對浮現：

| 鄰接 | 界線 |
|---|---|
| 004 GPS Fallback ↔ 010 Invalid Data | 004 管 **GPS 來源**不可用時改用內部時鐘；010 管**收到之時間訊號**無效時用最後有效值。觸發源不同 |
| 014 GPS Date/Time Broadcast ↔ 022 SNA Handling | 014 描述含「or SNA if unavailable」，但 **SNA／預設值之送出規則屬 022**；014 只驗 GPS 資料之送出 |
| 018 Default Initialization ↔ 011 Time Format Handling | 018 管 reset／斷電後之時間日期預設值；011 管格式（12H/24H）跨喚醒週期之保存與廣播。兩者皆涉「重開之後」，一者時間值、一者格式 |

### Time and Date notes

1. **`Master Clock` 之章節分散是假陽性（R-TM15）**。五片在章節層無共通節，
   021 更孤立於 `1.5.2.2`；但描述之動詞受詞同型 —— maintain internal
   {clock / time signal / calendar / counters}，018 為該內部狀態之初始化。
   `1.5.2.2 Key Off Status` 是**條件章節**（何時）非能力章節（做什麼），
   spec 依敘述情境分章、Layer 2 依能力分組，兩者不同構是預期的。
   **判讀順序固定：先讀 leaf 描述之語意軸，再看章節；章節證據不得單獨
   推翻語意分組。** 同理 020 留在 `CAN Transmission`（描述明寫 via
   TIME_DATE messages），其與 021 共用 `1.5.2.2` 而分屬兩組是正確結果 ——
   時機相同、能力不同。

2. **`Fault Handling` 之章節證據無鑑別力，非「已檢驗通過」**。異常處理在
   本 spec 中散佈於各功能章節之內，不自成一節，故章節對本 Set 既不支持
   也不反對。成組依據為描述語意：010 收端（用最後有效值）、022 送端
   （發 SNA/預設值），同一能力之兩個方向。

3. **A-TM13 使兩片之章節證據殘缺**：005（`#SYS-RA`=2，可解 1）與
   002（=6，可解 4），缺口來自 `SYS-RA-221 → 6151328`、
   `SYS-RA-224 → 6151331` 兩個物件不在 CFTS015 SR26 基線內
   （全檔 `615\d{4}` 零命中；本 spec 物件 id 全為 `481xxxx` 區段）。
   **該兩筆之 `specification_reference` 無章節可寫，不得以鄰近章節填充**
   （§8.4.1）。framework 之定案改以語意軸為據，不依賴該殘缺章節證據。

4. **`1.5.3.*`（ETM）零命中**：21 個可達章節全落 `1.3.1.*` 與 `1.5.2.*`。
   與 A-TM09 之 48 筆 SYS2 FR 覆蓋缺口是否同源**尚未查證，不主張**。

5. **覆蓋稽核分母為 SYS2 之 Functional Requirement 全集 126，非 SWE leaf
   22（R-TM6）**。037 引用 78 筆 FR、48 筆無對應 leaf（61.9%）。
   48 筆之處置為**宣告**非補生成：TC 生成單位仍為 22 片 leaf，不得為缺口
   自行創設 leaf 或分解 SYS2 條文湊覆蓋（§8.2 / §8.4.1），缺口以 RD-1 上問。

### Batch plan

**未定。** 待 Layer 2 經 Pei 簽核後另行起草。

### Workbook sync

BLANK workbook、FILL 適用：Test Group `Time and Date` 與 Part VII 之
Test Set 值寫入每一生成列之 G / H 欄。

rev C 無 `Test Case Framework` 分頁（9 分頁；R-U10、FORMS.md 實測），
故逐列欄位即足，無分頁同步步驟。

**欄 D5（範圍 Scope）維持空白** —— 該欄語意為「本工作簿所依據之 037 報告
之文件識別」，值即該 037 檔名去副檔名（R-TM9-A2，據交付路徑三例實測：
`Home-HMI-V0.1` / `AppDrawer-HMI-V0.1` / `PersonalAccount-HMI-V0.1`）。
本 feature 之 037 身分未定（A-TM02a），故無值可填，非暫緩填。
**不得以 feature 名、spec 標題或類推形態組出字串填入。**

**寫回一律走 `backend/xlsx_surgical.py`**（R-G3 全域；母本 R 欄
design_method 下拉為 x14 擴充，openpyxl 存回即摧毀且損壞為選擇性）。
```

---

## 3. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — 撤銷 02R 之 T3

若 `features/time_management/framework.md` 已建立：**不刪除**，於檔首
插入下列區塊（R-TM13：作廢加註保留，不刪）：

```markdown
> **⛔ 本檔作廢（2026-08-20，R-TM16）。**
> framework 之唯一位置為 `docs/fw036/framework.md`（Part VII）。
> 本檔係 `02R_framework_lock.md` T3 之誤指派所建，該指派已撤銷。
> 內容以全域檔為準，本檔不再維護，保留為軌跡。
```

若尚未建立：不建，於上繳註明「T3 未執行，直接適用 R-TM16」。

### T2 — Part VII 貼入全域檔

將本包 §2 之區塊（自 `---` 起至檔末）**追加至
`docs/fw036/framework.md` 檔尾**。

追加前 `assert` 該檔尾為 Part VI 之結尾字串
（`若有，填入三個 Set 名稱，否則逐列欄位即足（AMFM 先例）。`），
確認未插錯位置。

### T3 — 全域檔標頭更新

`docs/fw036/framework.md` 第 3–6 行之 Covers 句，逐字替換：

```
改前：**Projection** (Part V), and **Privacy**
      (Part VI, end of file). The cross-cutting rulings in Part I

改後：**Projection** (Part V), **Privacy** (Part VI), and **Time and Date**
      (Part VII, end of file). The cross-cutting rulings in Part I
```

（原文換行位置請以實際檔案為準；以 `assert old in text` 前置，
`replace(old, new, 1)`，改後複查 —— R-TM11。）

### T4 — `RULINGS.md`：追加 R-TM16

於末尾追加本包 §1 之區塊全文，標題行為 `## R-TM16 — framework 併入全域檔`。
追加後 `## R-TM` 條數應為 **19**（18 + 1）。

### T5 — 驗證

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md   # 期望 19
grep -c '^## Part ' docs/fw036/framework.md              # 期望 7
grep -n 'Part VII' docs/fw036/framework.md               # 標頭 + Part 標題，≥2 處
grep -c '^| ' docs/fw036/framework.md | tail -1          # 僅供記錄，無期望值
tail -3 docs/fw036/framework.md
```

前三項不符即回報並停，不自行調整。

### T6 — 上繳

`docs/upstream/02R-A1_corrections.md`，僅差異。須含：

1. T5 前三項結果 + `tail -3` 輸出
2. T1 之處置（已建／未建，及所採路徑）
3. T2 之 assert 結果（貼入前檔尾字串是否命中）
4. T3 之改前／改後實際字串（以檔案實際換行為準）
5. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集
   —— 續用 02 上繳 §5.1 之五全集

### 不得執行者

- 不動 git
- **不生成任何 TC**（Layer 2 待 Pei 簽）
- 不改 Part I–VI 之任何內容（本包只追加 Part VII 與改標頭一句）
- 不刪除 `features/time_management/framework.md`（若已建）
- 不填 `D5`、不組 Scope 值
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED）
- 不以 openpyxl 存回任何工作簿
- 不跑 `recon.py`（A-TM15）

---

## 4. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM16 | 裁決（Pei 授權），framework 併入全域檔 | §1 | ✅ T4 |
| framework Part VII | Layer 2 待 Pei 簽 | §2 | ✅ T2 |
| 全域檔標頭 Covers 句 | 連帶更新 | §3 T3 | ✅ T3 |
| `features/time_management/framework.md` 作廢註記 | 依 R-TM13 保留加註 | §3 T1 | ✅ T1 |

分析層本包未動 git、未改腳本、未寫 `docs/fw036/framework.md`
（該檔之寫入為執行層 T2／T3）。
