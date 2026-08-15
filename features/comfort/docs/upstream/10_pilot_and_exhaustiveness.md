# 上繳包 10 — 窮盡性掃描 ＋ pilot **stop-and-report**（未生成）

執行層 → 分析層。2026-08-15。回應下放包
`17_g1_baseline_exhaustiveness.md` §5 與 `18_phase4_pilot.md` §3／§4。

**結論：17 §5 之五項全部完成。兩份掃描已產。
pilot 之 14 條 TC 未生成 —— 18 §3.3 之五個 stop-and-report 條件中，
四個由 pilot 批自身觸發，涉 14 leaves 中之 11 條。**

---

## 0. 置頂：為什麼停在生成之前

18 §4 建議「先掃描、後生成」，理由是掃描若發現 profile §3.2／§3.4 有缺，
pilot 之 `pre_conditions` 與 token 處理即受影響。**該建議正中要害** ——
但受影響的不只是措辭，而是 18 §3.3 之四個停手條件在 ch13 上同時成立：

| 18 §3.3 條件 | 觸發？ | 憑據 |
|---|---|---|
| 需要新 marker | ✗ | 未遇 |
| **profile §3.2 未列之配置軸** | **✓** | `lower screen` 之有無與 stowed／retracted 狀態（13.2、13.3.1） |
| **profile §3.4 未列之 source token** | **✓** | `(-, +)` —— **7 節中 6 節出現** |
| **補值即構成 §8.4.1 造值** | **✓** | 13.5「a small set amount」無值；13.6「error tone」無規格 |
| **擁有者疑為其他 spec** | **✓** | 13.4 →「See HMI Core Logic and Flow, requirement N0」；13.5 →「See CFTS044」 |

受影響 leaves：13.2(3) ＋ 13.3.1(2) ＋ 13.4(2) ＋ 13.5(2) ＋ 13.6(2) = **11 / 14**。
未受影響者僅 13.2.1(1) ＋ 13.3(2) = 3 條。

**產 3 條當 pilot 沒有意義** —— pilot 之用途是在小樣本上暴露判斷漂移
（05 §4 選第 13 章正是因為它含 variant 判斷），而漂移點恰好全落在被擋下的
11 條裡。故整批停下，不做部分交付。

18 §3.3 之措辭是「**不得自行決定，回報後停**」。生成那 11 條，就是對這四項
各做一次自行決定。

---

## 1. 17 §5 —— 五項全部完成

| # | 項目 | 狀態 |
|---|---|---|
| 1 | R-C20 貼入 `RULINGS.md` | ✅ 現 22 條（R-C1~R-C20 ＋ R-C4-1 ＋ R-C5-1） |
| 2 | profile §3.1 標註改 `G-1 PASS 2026-08-15`，但書移腳註 | ✅ |
| 3 | A-CF14 登記 | ✅（home 檔案未動，見 §2.3） |
| 4 | §3.1／§3.2 兩項掃描 | ✅ 見 §3 |
| 5 | `INDEX.md` 標 09a／09b | ✅ |

另完成 18 §1：**A-CF07 CLOSED**，`DELIVERY.sha256` ENTRY 001 狀態欄改為
`Excel-confirmed by Pei 2026-08-15（四項）`；hash 與內容未動（append-only），
台帳仍 2 筆 OK。

### 1.1 R-C20 之接受

17 §2 指出這是**分析層自身造成的副作用**（R-C11 移出 spec、gitignore 使該處
不入版控），並升格為條文。我原記為「執行層判斷，可駁回」——
現改記為 R-C20 之實例。既有 feature 之 BASELINE 是否補齊屬另案，
**本包未擴及任何其他 feature**。

## 2. 三項狀態更新之細節

### 2.1 G-1 但書已降為腳註

profile §3.1 之標註由 `G-1 PASS（附 provenance 但書）` 改為
**`G-1 PASS 2026-08-15`**；但書全文移至該段末之 † 腳註，**事實記載保留，
不再具阻卻效力**。17 §1.1 之理由（R-C15：判準為蘊含 —— 「一次把 `shall`
引入 144 列中 143 列之編修並非可信之情形」）已一併寫入腳註。

### 2.2 A-CF14 已登

`features/home/feature.yaml` 之 `done_region.author_value: Arif`，
實際 done region 為 `ArifChen`，以前者選取得 **0 列**。

**FORMS.md 已獨立記載同一事實**（provenance warning 第 2 點）—— 兩處各自
發現、結論一致，這件事本身值得記：同一缺陷被兩條不相干的路徑各撞到一次，
表示它在流程上不是邊緣情形。

### 2.3 ⚠️ 17 §5.3 之路徑衝突 —— home 檔案本輪未動

17 §5.3：「登 A-CF14 …，**並於 `features/home/DATA_REQUESTS.md` 開列**。
**不逕改 home 之任何檔案。**」

**實測：`features/home/DATA_REQUESTS.md` 不存在。** 開列即須**新建**該檔，
而同句禁止改動 home 之任何檔案。兩者衝突，且新建檔案比新增一列更重 ——
故**本輪未動 home 之任何檔案**，A-CF14 只登記於 Comfort 自身。

擬列之內容備於此，裁示後即補：

```
| # | 項目 | Status | 影響 | Anomaly | Urgency |
|---|---|---|---|---|---|
| — | `feature.yaml` 之 `done_region.author_value` | ❌ 為 `Arif`，
  實際 done region 作者為 `ArifChen`（forms/…_Home_20260809.xlsx Z 欄，
  144 列）。以現值選取得 0 列 —— `build_remaining.py` 與 `write_back.py`
  之 content-hash invariant 均會誤選 | home 全批 | A-CF14（Comfort 登記）
  ／FORMS.md provenance warning 第 2 點 | Medium |
```

請裁示：**(a)** 新建 `features/home/DATA_REQUESTS.md` 並列入；
**(b)** 改列於 Comfort 之 `DATA_REQUESTS.md` 並標明對象為 home；
**(c)** 只留 A-CF14，不另開列。

## 3. 兩份窮盡性掃描（17 §3）

`features/comfort/scripts/scan_exhaustiveness.py`，可重跑。
輸入為 `section_fulltext.tsv` 全部 **129 節**（非截斷欄位，R-C18）。

### 3.1 §3.4 token 全集 —— `data/source_tokens.tsv`

**189 個相異 token。** 依 17 §3.1「不判斷是否應照錄，僅列全集」。

**非 ASCII 全集（7 類）**：

| token | 次數 | 出現節次 |
|---|---|---|
| `«` U+00AB / `»` U+00BB | 8 / 8 | **9.2、9.3、9.4.1、10.9.1、11.7** |
| `°` U+00B0 DEGREE SIGN | 2 | 2.10、16.10 |
| `–` U+2013 EN DASH | 2 | **17.1** |
| `’` U+2019 RIGHT SINGLE QUOTATION MARK | 1 | **16.8** |

**數字形態全集**：

| token | 次數 | 出現節次 |
|---|---|---|
| `15h` | 5 | 2.3、2.7、7.2、7.5 |
| `1-7` | 3 | 2.7、7.5、16.7 |
| `60-84` | 3 | 2.6、7.4、16.6 |
| `7/7` | 3 | 3.2、16.8、16.13 |
| `16-28` | 2 | 2.6、16.6 |
| `1-8` | 1 | 2.7.1 |
| `1/12`、`4/10` | 各 1 | **17.4** |

**對 profile §3.4 之落差（陳述，不判定）**：

1. **`«»` 之出處欄不完整** —— profile 記「9.3、9.4.1」，實測另有
   **9.2、10.9.1、11.7** 三節。
2. **`–` EN DASH（17.1）與 `’`（16.8）未列** —— 兩者皆為非 ASCII，
   §3.4 之四列未涵蓋。
3. **`60-84`、`16-28`、`1/12`、`4/10` 未列於範例** —— `\d+-\d+`／`\d+/\d+`
   之類別已列，但 profile 之例只到 `1-7`／`1-8`／`7/7`。若「照錄」之依據是
   類別則已涵蓋；若是列舉則有缺。**此為判定，屬分析層。**

**ALLCAPS 前十**：`AUTO`(38)、`MAX DEF`(32)、`HVAC`(30)、`HI`(24)、`LO`(23)、
`MAX A/C`(23)、`OFF`(22)、`A/C`(21)、`SYNC`(20)、`FAN`(13)。
全集見 TSV。

### 3.2 §3.2 配置軸候選 —— `data/config_axis_candidates.tsv`

**18 筆匹配，橫跨 14 節**（129 節中 **115 節無匹配**）。

依 **R-C13**，「115 節無匹配」只是索引層事實，**不等於該 115 節無配置條件**。
17 §3.2 要求之隨機 15 節人工過目即為此而設。

### 3.3 隨機 15 節人工過目（seed = 20260815，固定可重現）

抽樣：`3.1、2.6、16.8、12.8、2.12.2、17.2、12.2、2.8、2.15、16.3、2.11、
9.2、6.3、14.19、7.7` —— 其中 **14 節為 no-pattern-hit**，僅 `14.19` 命中。

**過目所見、pattern 未捕捉之配置條件**：

| 節 | 原文片段 | pattern 為何漏 |
|---|---|---|
| `3.1` | **On vehicles with** Tri-Mode climate | pattern 只有 `For vehicles with` |
| `3.1` | If the MODE button **is a multi-directional toggle or a hard control that allows 2 controls** | 硬鍵型別軸，無對應 pattern |
| `2.6` | for **ATC systems**；**English / Metric** 單位切換 | ATC 已列於 profile；**量測單位軸未列** |
| `16.8` | (driver and passenger **if available**) | pattern 為 `is available`，漏 `if available` |
| `12.8` | For **Standard** Heated/Vented seats | 軸已列於 profile，pattern 漏 |
| `17.2` | **12' Portrait 50%** widget also includes fan speed | **螢幕尺寸／widget 尺寸軸未列** |
| `2.8` | Recirc **may or may not be available**（依 CCM 之 availability status） | 執行期訊號驅動，非靜態配置 —— 形態不同 |
| `16.3` | (AUTO is not shown in **MTC configurations**) | 軸已列，pattern 漏 |
| `2.11` | Sync is not shown for **single zone climate configurations** | 軸已列，pattern 漏 |
| `9.2` | **in these variants** | 指涉他處定義之 variant 集合，本節未界定 |
| `6.3` | configured with a **non-foldable secondary lower screen** | **lower screen 軸未列** |

**對 profile §3.2 之落差（陳述，不判定）—— 三個候選新軸**：

1. **lower screen 之有無**（6.3、13.2、13.3.1、14.13、13.1[未引用]）
2. **螢幕尺寸／widget 尺寸**（17.2、17.4、14.14）
3. **量測單位 English／Metric**（2.6、16.6）

另有兩項形態不同者，一併陳述：`2.8` 之「執行期 availability 訊號」不是配置
軸而是狀態；`9.2` 之「in these variants」是**未界定之指涉**。

**「這算不算一個配置軸」屬分析層**（17 §3.2），執行層不判。

### 3.4 掃描本身之侷限，如實記

pattern 表由 17 §3.2 逐字給定，我未增補。實測顯示它**漏掉了 profile 自己
已列的軸**（Standard 座椅、MTC、單區）——「pattern 沒抓到」與「該節沒有
配置條件」之間的距離，比預期更大。15 節抽樣中 14 節 no-pattern-hit，
而其中至少 8 節實際帶有配置條件。

**若僅憑 TSV 而不做人工過目，結論會是「115 節無配置條件」**，而那是錯的。
R-C13 所防的正是此事，本次是它生效的實例。

## 4. pilot 之四個 stop-and-report —— 逐項憑據

ch13 全文取自 `section_fulltext.tsv`（未讀截斷標題，R-C18）。
**13.1 不在批內**（categorization 為 `assumption`，未被 037 引用）。

### 4.1 未列之配置軸：`lower screen`（13.2、13.3.1 —— 5 leaves）

> **`13.2`（LS1.）**：When the (-, +) seat control buttons are pressed from
> the door control for lumbar & bolster, **if the lower screen is not in the
> stowed position**, switch the tab on the lower screen to the Seats tab.
> **If the lower screen is in the stowed position**, display the Seat Control
> Popup on the head unit (popup times out after 5 seconds of not interaction).
> If the lower screen is in the stowed position, and the user is already in
> the climate section on the main head unit, switch the user to the Seats tab.

> **`13.3.1`（LS2.1）**：… latching during a keycycle, after a keycycle,
> and **after the lower screen has been stowed/retracted**. …

profile §3.2 之設備配置軸列有八項，**`lower screen` 不在其中**。
且此處有兩層：**(a) lower screen 之有無**（車輛配置）與
**(b) stowed／retracted 狀態**（執行期狀態）。前者是 pre-condition 之配置軸，
後者是 procedure 之操作狀態 —— **兩者分類不同，混寫會使 pre_conditions
承載本應在 procedure 的東西**。

**需裁示**：(a) 是否納入 §3.2 之設備配置軸清單；(b) 之 source class
（`spec-verbatim` / `spec-derived` / `test-setup`）如何標。

### 4.2 未列之 source token：`(-, +)`（6 / 7 節）

`13.2`、`13.3`、`13.3.1`、`13.4`、`13.5`、`13.6` 皆以 **`(-, +)`** 指涉
座椅控制鍵（`13.2.1` 無）。profile §3.4 之四列未涵蓋此形態。

**兩種寫法之差異是實質的**：照錄 `(-, +)` 與改寫為 `"-"` 與 `"+"` 兩鍵，
在 procedure 的可執行性與 lint 的 UI-label 規則（§11：UI label 用 `"..."`）
上結果不同。§3.4 說「作者自身之敘述一律用 `"..."`」，但 `(-, +)` 是**條文
自己的記法**，落在 §3.4 之例外範圍還是 §11 之通則，**我判不了**。

### 4.3 擁有者疑為其他 spec（13.4、13.5 —— 4 leaves）

> **`13.4`（LS3.）**：The user will be able to long press on the hard button
> (-, +) or on the touch screen itself to initiate fast increases/decreases.
> **(See HMI Core Logic and Flow, requirement N0.)**

> **`13.5`（LS4.）**：A short press of the (-, +) button will increase the
> lumbar/bolster by a small set amount, that would be equivalent to a short
> press of the previous 4-way rocker hard control **(See CFTS044)**.

**R-C17 之判定測試**：「該規則定義於 Comfort spec，或定義於他 spec？
定義於後者即 out of scope，縱使 Comfort spec 引用之。」

- `13.4` 之 long-press 快速增減行為，其定義在 **HMI Core Logic and Flow
  requirement N0**。Comfort 只是引用。
- `13.5` 之增量等效性，其基準在 **CFTS044**。

**兩份文件皆不在 `inputs/`，亦不在 `spec-index/`**（已查）。
故除了擁有者問題，也構成 §4.4 之補值問題。

**需裁示**：此二節是否 out of scope（R-C17）；若在範圍內，其行為之權威
來源如何取得。

### 4.4 補值即造值（13.5、13.6 —— 4 leaves）

- **`13.5`**：「increase the lumbar/bolster by **a small set amount**」——
  spec 未給數值，其基準在 CFTS044（不在手）。ER 若寫「lumbar increases by
  a small amount」不可觀察（§6 要求 ER observable）；若寫任何具體級距即
  **§8.4.1 造值**。
- **`13.6`**：「pressing the (+) button again will result in **error tone**
  being triggered」—— 「error tone」無規格（頻率、時長、是否有視覺回饋皆無）。
  ER 寫「an error tone is triggered」是照錄但不可觀察；寫任何具體描述即造值。

**需裁示**：此二者之 ER 應如何處理 —— 照錄 spec 措辭並接受其不可觀察性、
標為 BLOCKED、或以 RD-1 回上游。

### 4.5 未觸發者

**新 marker**：未遇。profile §5 之「目前無 marker」維持。

## 5. 本包**未做**者

- **未生成任何 TC**、未指派任何 tc_id（含 `NR1L-ComfortHMI-001`）。
- **未寫回 workbook**（18 §3.4 本就禁止，本包更未到該步）。
- 未動 `framework.md`、profile、`RULINGS.md` 之既有條文
  （R-C20 為新增，profile §3.1 標註為 17 §5.2 指定之更新）。
- 未跑 lint —— **無 TC 可 lint**。
- **§9 self-check 17 項未逐項自評** —— 該自評之對象為「每一條 emit 前之
  TC」（canon §9 標題：before emitting each TC），無 TC 即無對象。
  自評表之骨架備於 §6，待生成後填。
- 未動 home 之任何檔案（§2.3）。

## 6. §9 self-check —— 17 項之骨架與本批之預判

canon §9 為「emit 前逐條自檢」，無 TC 則無從自評。惟四個停手條件已可預判
其中五項會直接受影響，先標出，使裁示時可一併考量：

| # | §9 項目 | 本批預判 |
|---|---|---|
| 1 | Test Set 合 framework、無 Test Group 前綴 | 可通過 —— `Seat Control Tab` 已在 Part N |
| 2 | tc_title 2–14 words、無 modal、sibling token 可見 | 需 §4.2 之 `(-, +)` 裁示方能定 token 形態 |
| 3 | Pre-Condition 為 spec trigger、非隱含環境前提 | **受 §4.1 阻** —— `lower screen` 軸未列 |
| 4 | Input Test Data 歸屬正確 | 可通過 |
| 5 | 步驟可執行、Final Step 擁有驗證 | **受 §4.3／§4.4 阻**（13.4／13.5 之操作與級距） |
| 6 | 步驟長度與意圖層級 | 待生成 |
| 7 | 標準 setup 片段逐字重用 | 待生成 |
| 8 | CLI 步驟格式 | 不適用（無 CLI 步驟） |
| 9 | 需要 before/after 時給 baseline | 13.5／13.6 需要，**受 §4.4 阻** |
| 10 | Procedure ↔ ER 1:1、ER 可觀察、無 modal | **受 §4.4 阻** —— 13.5／13.6 之 ER 不可觀察 |
| 11 | 無 FP／FF；supported 配 negative | 13.6 本身即 negative，可通過 |
| 12 | 追溯至 Req/SWRA、不擴張、無造值、無造範圍 | **受 §4.3／§4.4 阻** |
| 13 | Design Method 於 procedure 定案後指派 | 待生成 |
| 14 | 四欄無行尾句點 | 待生成 |
| 15 | UI label 用 `"..."` 不用 `[...]` | **與 §4.2 之 `(-, +)` 直接相關** |
| 16 | `specification_reference` 列全每個直接驗證之節 | 可通過 —— 節次已定 |
| 17 | 原始 spec 勝過 index export；閾值為 spec 來源之具體值 | **受 §4.4 阻** —— 13.5 無具體值可取 |

**17 項中 6 項受四個停手條件直接阻擋**（3、5、9、10、12、17），
另 2 項（2、15）繫於 `(-, +)` 之裁示。

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 7.1 已驗

1. 17 §5 五項與 18 §1 之落地。
2. 兩份掃描之產出與其數字（129 節、189 token、18 筆軸候選、115 節無匹配）。
3. 15 節抽樣之逐節閱讀，並逐項比對 profile §3.2 之八軸清單。
4. ch13 七節全文，及四個停手條件之逐節憑據。
5. `13.4`／`13.5` 所引之兩份外部文件**不在 `inputs/` 亦不在 `spec-index/`**。
6. `DELIVERY.sha256` 狀態更新後仍 2 筆 OK；`BASELINE.sha256` 8 檔 OK。

### 7.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **其餘 114 節之配置軸與 token** | 抽樣為 15 節（17 §3.2 指定），非全查 | **中** —— 15 節中就找到 3 個未列軸；全查幾乎必然再找到。但全節人工過目成本高，且「算不算軸」屬 Tier 2，逐節上呈反而低效。**建議**：先裁三個候選軸，再以裁定後之判準做一次全節機械複掃 |
| 2 | **`(-, +)` 以外之條文自有記法** | 只在 ch13 察覺 | 中 —— 189 token 全集已在 TSV，但「哪些是條文自有記法」需逐一判斷 |
| 3 | **HMI Core Logic and Flow／CFTS044 之取得可能性** | 兩者不在 repo，未查客戶樹（不可達） | 中 —— 影響 13.4／13.5 之最終處置 |
| 4 | pilot 其餘 14 組之同類問題 | 只查了 ch13 | **中** —— 若 `lower screen`／`(-, +)` 之裁示具一般性，其他組可能同受影響 |

### 7.3 未做、亦未偷做者

- **未生成 TC、未指派 tc_id、未寫回 workbook**。
- **未自行決定四個停手條件中的任何一個**。
- 未增補 17 §3.2 之 pattern 表（如實記其漏抓，不逕改）。
- 未動 home 之任何檔案。
- 未重跑任何既有 feature 之 recon（R-C8）。
- 未執行 git。

### 7.4 執行層對「本包可否結案」之判斷

**掃描部分可結案；pilot 部分待裁示後續行。**

四項裁示（§4.1 ~ §4.4）加一項路徑衝突（§2.3），共五問。其中
**§4.3 之擁有者問題最可能改變批次組成** —— 若 13.4／13.5 判 out of scope，
pilot 由 14 leaves 降為 10，而 `Seat Control Tab` 之 Part N leaf 數
（14）與 coverage 分母亦須連動處理，屬 Part N 變更。

裁示到位後，14 條（或調整後之條數）可即刻生成 —— 條文全文、Part N、
profile、lint 規則皆已就位，缺的只有這五個判斷。
