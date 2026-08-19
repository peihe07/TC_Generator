# 52 上繳 — 上游素材、Table EDPR1 之比對、缺件清單之收斂

- 產出層：執行層｜2026-08-19｜對象：分析層
- 來源包：`docs/handoff/52_upstream_materials.md`
- **git 未執行**；**語料未動、交付件未動**；**對 comfort 唯讀**；
  交付與 RD 寄出屬 Pei

## 0. 一頁摘要

| 作業 | 結果 |
|---|---|
| 素材 | Pop Up List **已入 `inputs/` 並列入 BASELINE**（`shasum -c` 8/8 OK）。**Tutorials PDF 不在檔案系統中**（見 §1.1）|
| 3.1 | **未做** —— 其所需之 Tutorials L&F 節次無法查證（見 §2）|
| 3.2 | **已做** —— `INTR2.)` 具名於交付說明 §3.0 |
| 3.3 | **已做** —— p14 之 Table EDPR1 **含 `"Tutorials"`（第 9 列），而我方 ER 已列之** → **既非 defect 亦非 anomaly**（見 §3）|
| 第 4 項 | **已解** —— Pop Up List **確有**逐步對映；四個 popup id 可具名（見 §4）|
| DR #4 | 證據更新（1341 raw／1339 normalised，本層獨立重現）|
| **新發現** | **A-UP14**：`PU1089`／`PU1090`／`PU1091` 之角色在兩份文件間**整體錯開一位**（見 §5）|
| 附帶 | **RD #8 已由本輪證據解答**（`PU0626` 與 `PU0129` 為兩種車輛配置各用其一）|
| §五 | `DATA_REQUESTS.md` 已改為單一清單（§0 為操作面，歷史記載原文保留）|

---

## 1. 素材

### 1.1 **Tutorials L&F 之 PDF 不在檔案系統中**

52 包 §一記其狀態為「**到齊**」。**本層遍尋不獲**：

| 找過 | 結果 |
|---|---|
| `spec-index/sources/`（33 份 PDF）| 無 Tutorials |
| `spec-index/cache/` | 無 |
| `features/*/inputs/`、`_intake/`、`docs/` | 無 |
| 全 repo `find -iname '*Tutorial*'` | **0 命中** |
| 全 repo `grep -rl 'CR22839\|INTR1\|INTR2\|INTR3'` | **只命中 52 包自身** |

**故 3.1 未做**（§2），而 3.2、3.3 之 Tutorials 側所需之字句
**52 包本身已逐字給出**，該兩項不受影響。

### 1.2 Pop Up List —— **它不是新到的檔**

`inputs/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`，
SHA `b0827f02c1a0a69b…`，已列入 `BASELINE.sha256`。

**repo 內原已有兩份**：`features/comfort/inputs/…`（SHA `b0827f02…`，
即 **R-U9 於 02 輪所指名之候選**）與 `docs/test/Player/SPEC/…`
（SHA `fdc8196a…`，位元組不同）。本輪之複本逐位元組取自前者（`cmp` 相同）。

**身分以內容確認，不以檔名**（52 包所載之檔名為上傳正規化形式）：

| 52 包所載 | 本層於複本上重現 |
|---|---|
| 全三分頁 | `Main`／`Templates`／`Drop Down Fields` ✓ |
| 唯一 PU id **1341** | **原始字串相異 1341** ✓（正規化後 1339 —— 差 2 為 `PU_0129` 之類之異寫，兩者映射到同一 id）|
| `PU1087`／`PU1088` = 0 / 0 | ✓ 皆不在 |
| `PU1089`／`1090`／`1091` = 1 / 1 / 1 | ✓ 皆在 |
| `PU0626`／`PU_0129`／`PU0588`／`PU0580`／`PU0841`／`PU0611`／`PU0091` 各 1 | ✓ 七者皆在 |

**兩份 SPEC 副本亦得同樣數字** —— 即該量測與副本無關，是文件本身的性質。

```
shasum -a 256 -c BASELINE.sha256
  … 8 個項目全部 OK（WARNING: 4 lines 為空白分隔行，同 DELIVERY.sha256 之既有特性）
```

### 1.3 **R-U9 之單一來源要求未達成 —— 具名**

R-U9 逐字：「採用後比照 Comfort R-C11 移入 `spec-index/` 作單一來源，
**不在各 feature `inputs/` 各留一份**」。

而 52 包指示落 `inputs/`，且**移動 comfort 之檔屬寫入他 feature**
（R-U24／R-U30 禁止）。**現況為三份並存。**

**本層依 52 包執行（落 `inputs/`），並在此具名該衝突。**
建議：待 Comfort 下次開輪次時一併整併至 `spec-index/`
（同 N-XF01／N-XF02 之處置形態）。

---

## 2. 3.1 —— **未做，且不宜以現有資訊代做**

52 包已逐字給出所需字串（Video Bank 標題 `Tutorials`、副標
`Learn about new features`），**但 `specification_reference` 之併列需要節次**，
而節次只能自該 PDF 讀得。

**以「Tutorials L&F」作為引用而不帶節次，會違反三件事**：
`G11`（引用欄之形態為 `<stem>_<節次>`）、`R-U1`（一律用 Source ID 字串）、
以及 `G18`（ER 之字面值須溯得到**被引之節之 `pdf_text`**，
而該 PDF 不在 `outline_map` 內，無 `pdf_text` 可溯）。

**故本層不寫。** 檔案到位後，本項為一次小改：
`TC-167` 之 ER4 由 `Tutorials begin and no Connected Personal Account login
is launched` 改為併述 Video Bank 之標題與副標，並於引用欄加該節 ——
**估計影響 1 條、連帶 `48_review_pack_33a` 重出一次**。

---

## 3. 3.3 —— Table EDPR1 之逐列比對

以 `render_spec_region.py` 之同一 PDF 讀 p14，取其文字行之座標排序，
Table EDPR1 之十列逐字如下（x = 312.5 之欄）：

| # | 逐字 |
|---|---|
| 1 | `“Resume Setup” (only if not complete)` |
| 2 | `“Edit Name”` |
| 3 | `“Edit Avatar”` |
| 4 | `****“ Stellantis Account”` |
| 5 | `“Memory Seat” (If applicable)` |
| 6 | `“Welcome Pop Up”` |
| 7 | `“Delete Profile”` |
| 8 | `“What is linked to my Profile?”` |
| **9** | **`"Tutorials"`** |
| 10 | `“More Settings”` |

**含。** 而 `TC-017` 與 `TC-074` 之 ER2 逐字皆為：

> `… Delete Profile, What is linked to my Profile?, **Tutorials**, More Settings;
> and a circled number 1 is shown next to Resume Tutorials`

**即：含，而我方 ER 已列之。**

52 包列了兩個分支（含→defect／不含→anomaly），
**實際落在第三種：含且已列 → 無事。** 具名於此，不改任何一條。

**另查一處**（順手，因其在同一句）：ER 之
`a circled number 1 is shown next to Resume Tutorials` ——
9.1 之條文逐字為 `there will be a circled number 1 next to **Resume Tutorials**`，
**我方為逐字轉錄，無誤**。

`INTR1.1)` 所述（`“Tutorials” will be a list item in the “Edit Profile” section`）
**與本 feature 之 spec 一致**，兩份文件在此項無分歧。

---

## 4. 第 4 項 —— Pop Up List 之逐步對映：**有**

`Main` 分頁之 `Description` 欄即帶流程位置。與 `8.3` 相關者：

| id | Description（逐字）| 對應 |
|---|---|---|
| `PU0585` | `Profile Setup or "Edit username" > keyboard` | 8.7 之 username 步驟 |
| `PU0586` | `Profile Setup or "Edit Avatar" >"Select an Avatar" screen` | 8.8 之 avatar 步驟 |
| `PU0587` | `Profile Setup … start and then try to exit without saving: "Are you sure you want to cancel your Profile Setup?"` | **8.3.1 之丟棄確認** |
| `PU0612` | `Profile Setup > **Step 4**: "Do you want to apply the current preferences to your profile? …"` | **8.9 之最終步偏好詢問** |

**故 `TC-169`（8.3）得補其 popup id，`TC-170`（8.3.1）與 `TC-184`（8.9）
亦各得具名一個。**

### 4.1 **本輪不改該三條 —— 理由具名**

1. 52 包 §五之作業為「**查驗**」（「有則 `TC-169` 得補」為其後續，非本輪之指令）
2. G-J（成批落地）：改動會使 `48_review_pack_33a`／`33b` 過期並觸發重出與重判；
   而**餘 3 條之覆核（`165`／`181`／`182`）尚未讀畢**
3. 若同時採 A-UP14 之處置，`TC-142`／`143` 亦在同一批 —— **一次改完較省**

**建議與餘 3 條之覆核發現、3.1（待 PDF）一併落地。**

---

## 5. 新發現 —— **A-UP14：三個 popup id 之角色整體錯開一位**

| id | Pop Up List 之 `Description` | 本 feature 之 spec `5.13.2` |
|---|---|---|
| `PU1089` | `Displayed if HU or TBM do not confirm complete default restoring`（**失敗**）| 確認清除時顯示（**進行中**）|
| `PU1090` | `Displayed when users confirm data clearing by pressing Yes/Ok in pop-up PU_0129`（**進行中**）| 清除成功後顯示（**完成**）|
| `PU1091` | `Displayed when data have been succesfully cleared`（**完成**）| HU／TBM 未確認完成時顯示（**失敗**）|

**且 `PU1089` 之字串為 `Settings Restore failed / Some settings may have not
been restored`** —— 其文義屬**回復預設設定**（4.1.1），不是清除個人資料。
即：Pop Up List 可能把該 id 指給了另一個功能，**也可能是我方 spec 借用了
不屬於它的 id**。**兩種可能本層都不排除。**

**受影響**：`TC-142`（`041-03`）、`TC-143`（`041-04`）之三個 id 斷言 ——
**在裁定前有假失敗之風險**。

**處置**：登記 `ANOMALIES.md` **A-UP14** ＋ `DATA_REQUESTS.md` §0.1，
**不改 TC**。依 52 包 §3.3 之原則：兩份 spec 記載不一致者，
**登記並列入 RD，不自行裁決何者為準** ——
本項雖非 Tutorials，其形態完全相同，故沿用該原則。

**降低風險之可選作法已列於 A-UP14**（ER 改述為「進行中之 popup」而不寫 id），
**未執行** —— 那會使 ER 失去 id 級精確度，是否值得由分析層定。

---

## 6. 附帶 —— **RD #8 已由本輪證據解答**

| id | Module | Description（逐字節錄）|
|---|---|---|
| `PU0129` | Settings | `Displayed when the user selects yes to Clear Personal Data`（Core HMI 之通用者）|
| `PU0626` | Settings | `New "Clear Personal Data" popup **for vehicles with Profiles**. Clearing Personal Data will also delete all Profiles from the vehicle` |

**兩者為不同 popup，各對應一種車輛配置** —— 即 RD #8 三種讀法中之第三種。

**我方現行寫法（「於每一個確認 popup `PU0626`/`PU_0129` 按 Yes」）在該讀法下正確**：
有 Profiles 之車輛出現 `PU0626`，其餘出現 `PU0129`。**五條 TC 無須改動。**

**RD #8 是否結案由分析層定** —— 本層只提出證據，不自行關閉
（同 A-UP09 之先例：條件成就者回報，落槌屬另一層）。

---

## 7. §五 —— `DATA_REQUESTS.md` 改為單一清單

`§0` 為操作面之四項表（每項附**卡住哪幾條 TC／替代作法／答覆會改變什麼**），
另有 `§0.1`（A-UP14）、`§0.2`（RD #8 之證據）、`§0.3`（選配之 Market Config Table，
含 7 × 5 之最小充分形式）。

**§1 以下之歷史記載原文保留不刪**，並於檔首具名該分界。

**四項之現況**：第 1 項缺（真缺口）、第 2／3 項缺（查詢單已備未寄）、
**第 4 項已解**。

---

## 8. 全閘與附件

```
lint_tcs 64/64（語料 189，違規 0）    audit_consistency 56/56
audit_delivery_fields 7/7（違規 0）   audit_pending 5/5（新命中 0，違規 0）
audit_enums 7/7   audit_verbs 5/5    audit_variant_pairs 7/7
audit_assignment 6/6                 audit_delegation 8/8（紅 0）
lint_variant_labels 11/11            lint_outbound_doc 8/8
verify_dv_integrity 6/6              build_review_pack 4/4
stamp_static_doc 5/5                 write_back 12/12（未重寫回）
```

**review pack**（四份現行）：`44_24a` 11／0、`48_24b` 11／0、
`48_33a` 17／0、`47_33b` 16／0。

**靜態轉錄**：`27_rd_queries_v2` 0、`28_provenance4` 0、`34_provenance5` 0、
**`48_delivery_note` 0（本輪新標，28 條）**。

**交付件 ENTRY 001 未動**（`shasum -c` OK）；`generated/` 未動。

---

## 9. 未執行之既有作業 —— **51 包之 remarks 三分類量測**

51 包之作業（把 143 條 remarks 分 (i)／(ii)／(iii) 三類並計數）
**至今未執行** —— 50、51 兩包本層皆未收到執行指令，
其上繳於 `docs/upstream/` 亦不存在。

52 包 §六稱「remarks 之變更待 51 輪量測與 Pei 裁定」，
**即該量測是 Pei 裁定之前置**。**具名於此，等候指示。**

---

## 10. 現況

| 項 | 值 |
|---|---|
| TC | 189 ／ leaf 180 / 180（本輪未動）|
| 交付件 | ENTRY 001，未交付 |
| 已覆核 | 186 / 189（餘 3：`165`／`181`／`182`）|
| 閘 | 18 支 |
| 缺件 | **3 項**（原 4 項，第 4 項本輪已解）|
| 待 Pei | 交付與否、remarks 之處置、**A-UP14 之裁決**、RD v2＋#8 之寄出 |

---

## 11. 獨立判斷

1. **「素材到齊」與「素材在檔案系統上」是兩件事，而本輪兩者都出現了。**
   Pop Up List 之狀態記為「待驗」，**而它其實三份都在 repo 裡，只是沒人查**；
   Tutorials 之狀態記為「到齊」，**而它不在**。
   兩者剛好相反 —— 這不是誰記錯，是**「素材狀態」目前沒有一個可執行的判準**。
   建議：素材清單之每一項附**其在檔案系統上之路徑與 SHA**；
   「到齊」定義為 `shasum -c` 對得上。**沒有路徑的「到齊」不算到齊。**

2. **A-UP14 是本 feature 第一個「兩份上游文件互相矛盾」之發現，而它是查別的東西時掉出來的。**
   52 包要我查的是「有沒有逐步對映」（第 4 項），
   而逐格讀 `Description` 時三個 id 的角色錯位自己跳出來。
   **若只用程式比對「id 在不在」，這件事永遠不會被發現** ——
   1089／1090／1091 三個都在，數量對，涵蓋率 100%。
   **錯的是它們各自指誰。** 這與 AB-1（兩端未指名）、
   AC-1（欄內先後矛盾）同屬一類：**「都在」不等於「對得上」。**

3. **3.3 之答案落在 52 包沒有列的第三個分支，而那是好消息裡的壞消息。**
   包預期「含→我方漏列」或「不含→兩份不一致」，
   實際是「含且已列」。**我方之所以已列，是因為 `must_carry` 把 p14 之表逐列灌了進來**
   —— 即那一條之正確性來自 07 輪之補句表，不是來自 9.1 之條文
   （條文只說「依 Table EDPR1 之順序」，沒有列出十列）。
   **一條 TC 之正確性來自一份三十五輪前建立的資料表，而那張表沒有指紋。**
   `data/*.tsv` 與 `outline_map.json` 目前只有 `BASELINE.sha256` 保護其**位元組**，
   沒有東西保護「它與 PDF 現況一致」。**具名此缺口。**

4. **第 4 項從「待驗」到「已解」只花了一次逐格讀取，而它卡了本 feature 五十輪。**
   `TC-169`（8.3）自第六批生成起就寫著「popup 之逐步對映不在我方輸入內，
   依 §8.4.1 只驗形態」—— **而那份輸入其實一直在 `features/comfort/inputs/` 裡。**
   §7.4（先查他 feature 之交付件）救了 T:Z；
   **這一次要救的是「先查他 feature 之 `inputs/`」** ——
   建議把該常規由「交付件」擴為「他 feature 之全部素材」。
