# 19 — Comfort HMI / pilot 五項裁示

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/10_pilot_and_exhaustiveness.md`
- 結論：**PASS**。停手正確。五問全裁；**pilot 維持 14 leaves，Part N 不變**。

---

## 1. §2.3 路徑衝突 —— 分析層指示自相矛盾

17 §5.3 同時寫「於 `features/home/DATA_REQUESTS.md` 開列」與「不逕改 home
之任何檔案」，而該檔不存在，開列即須新建。**指示自相矛盾，責在分析層。**
執行層未在兩者間自行取捨而是停下回報，處置正確。

**裁定：採 (b)** —— 列於 Comfort 之 `DATA_REQUESTS.md`，具名對象為 home。

```
R-C21  跨 feature 發現之登記位置

於 A feature 之作業中發現 B feature 之缺陷者，登記於 A 之 ANOMALIES.md 與
A 之 DATA_REQUESTS.md，並於該列具名對象 feature。

不代 B feature 建檔、不改 B 之任何既有檔案。B 之處置由 B 自身之 workstream
決定。

理由：跨 feature 寫入使「誰在維護這個檔」失去單一答案；而登記之目的是讓
發現不遺失，該目的在發現者之帳上即已達成。
```

A-CF14 依此列入 Comfort 之 `DATA_REQUESTS.md`，內容採 10 §2.3 所擬，
`Urgency` 維持 Medium。

**FORMS.md 與 A-CF14 各自獨立發現同一事實**，此點值得保留於 anomaly 內文：
同一缺陷被兩條不相干路徑各撞一次，表示它不是邊緣情形。

---

## 2. §4.1 `lower screen` —— 兩層分開處置，(a) 納入配置軸

執行層之分層正確且必要：**(a) lower screen 之有無 = 車輛配置；
(b) stowed／retracted = 執行期狀態。** 混寫會使 `pre_conditions` 承載本應
在 `test_procedure` 的東西（§4.5 欄位歸屬、§4.4 禁 step-controlled state）。

### 2.1 (a) 納入 profile §3.2 之設備配置軸

新增第九軸：**secondary lower screen 之有無**。

其 source class **逐節判定，不由本包代定**：讀該節之 `full_text`，
若條文出現該配置之字面表述則標 `spec-verbatim` 並照錄其措辭；
若係由條文推得則標 `spec-derived`。**不得沿用 6.3 之
`non-foldable secondary lower screen` 措辭套用於 13.x** —— 那是另一節的
文字（R-C18 之同型風險：措辭正確地屬於別處）。

### 2.2 (b) 預設為 procedure 步驟，例外始得入 Pre-Condition

```
判定測試（§8.5）：該 TC 之驗證目標，是否就是「螢幕處於該狀態時之行為」？

是 → 該狀態為 spec 定義之 trigger condition，入 pre_conditions，標 source class
否 → 該狀態係為使測試可執行而設置，入 test_procedure 之步驟
```

不得因「寫在 Pre-Condition 比較省事」而上移；亦不得因「它是狀態」而一律
歸 Pre-Condition —— §4.4 明禁 step-controlled state。

---

## 3. §4.2 `(-, +)` —— 不需新例外，既有規則已能決斷

`(-, +)` 為條文自有記法。profile §3.4 與 §11 之界線既已寫明
「作者自身之敘述（procedure 之按壓目標、非引用之 ER）一律用 `"..."`」，
本案依該界線分割即可，**不新增例外**：

| 位置 | 寫法 |
|---|---|
| `test_item`（承載需求原文，profile §3.1） | **照錄 `(-, +)`** |
| ER 中之引用片段（`... as defined by LS4 ...`） | **照錄** |
| `test_procedure` 之按壓目標 | **`Press "-"` / `Press "+"`** |
| 非引用之 ER 敘述 | **`"-"` / `"+"`** |

profile §3.4 增列第五列記此分割。lint 對照 `section_fulltext.tsv` 之來源列
驗證保留 token，不逕行禁用。

§9 第 2、15 項之繫屬即由此解除。

---

## 4. §4.3 擁有者 —— **兩節皆在範圍內，但範圍收窄**

R-C17／§8.4.2 之判定測試問的是「**該規則**定義於何處」，不是「該節是否
引用外部文件」。逐節適用：

### 4.1 `13.4`（LS3.）—— in scope，收窄

條文自身即陳述行為：長按 `(-, +)` 或觸控螢幕 → 啟動快速增減。
**該行為定義於本節**，`(See HMI Core Logic and Flow, requirement N0)` 係
交叉參照其通用長按機制。

- **在範圍**：長按 → 快速增減之啟動
- **不在範圍**：長按之判定門檻、重複速率、加速曲線等通用參數 —— 由 Core
  擁有。**不得測、不得補值**
- `reasoning` 須明列此委派（§8.2.1）

### 4.2 `13.5`（LS4.）—— in scope，收窄

條文自身陳述：短按 `(-, +)` → 腰靠／側靠增加一個級距。
**該行為定義於本節**；`(See CFTS044)` 所定者為該級距之**量值**及其與舊款
4-way rocker 之等效性。

- **在範圍**：短按 → 產生一次級距變化
- **不在範圍**：級距之量值、與 rocker 之等效性 —— 由 CFTS044 擁有。
  **不得測、不得補值**
- `reasoning` 須明列此委派

### 4.3 連帶結論

**pilot 維持 14 leaves，`Seat Control Tab` 之 Part N leaf 數不變，
coverage 分母不變。** 執行層所慮之「降為 10 條並連動 Part N 變更」不發生。

HMI Core Logic and Flow 與 CFTS044 **不需補入 `inputs/`** —— 兩者所擁有之
內容既已判為 out of scope，取得它們反而會誘使測試越界。二者登為
`DATA_REQUESTS` 之 Low（僅供日後查考），**不阻塞**。

---

## 5. §4.4 補值 —— 兩節皆不標 BLOCKED

```
R-C22  不可量化 ≠ 不可觀察

ER 之判準為「可觀察、可判定」，非「可量化」。條文未給數值者，ER 以條文
自身命名之可觀察量表述，不得補具體量值（§8.4.1），亦不得因無法量化而
標 BLOCKED。

BLOCKED 保留給「該行為完全由他方執行，本 ECU 無任何可觀察端」之情形
（Privacy `[BLOCKED-ECU]` 前例）。「值不知道但變化看得見」不屬之。
```

適用：

- **`13.5`**：ER 不得寫任何級距量值。改以條文自身命名之可觀察量表述
  —— **該可觀察量須自 13.2 ~ 13.6 之 `full_text` 取得**（如條文提及之
  level／狀態指示），**不得由本包指定**，亦不得假定某個 UI 元件存在。
  若通讀五節後確無任何條文命名之可觀察量，回報停下（屆時才是 BLOCKED
  之候選）。
- **`13.6`**：`error tone` **照錄**。「An error tone is played」為可判定
  （有無），合於 §6；其頻率、時長、視覺回饋一律不寫。另併列可觀察之 UI
  事實（達上限後級距不再變化）。**不標 BLOCKED。**

---

## 6. 掃描之後續（10 §7.2 第 1 項）

同意其建議：**先裁軸，再以裁定後之判準做一次全 129 節機械複掃**，
不逐節上呈。

複掃之判準為本包 §2.1 所增之第九軸，加上 profile §3.2 既有八軸，
共九軸之字面表述全集。輸出未匹配任何軸而含條件句式者，供分析層第二輪裁。

**紀律重申**：詞彙型掃描之陰性結果只是索引層事實（R-C13）；15 節抽樣中
即找到三個未列軸，故複掃之「無其他軸」不得作為結論，只得作為「已盡機械
之力」之記錄。

---

## 7. 執行層作業指示

1. R-C21、R-C22 原文貼入 `RULINGS.md`。
2. profile §3.2 增第九軸（§2.1）、§3.4 增第五列（§3）。
3. A-CF14 依 R-C21 列入 **Comfort** 之 `DATA_REQUESTS.md`；
   **home 之任何檔案仍不得動**。
4. HMI Core Logic and Flow、CFTS044 列入 `DATA_REQUESTS.md`，Urgency **Low**，
   註明「所擁有之內容已判 out of scope，取得僅供查考」。
5. 依 §2 ~ §5 之裁示生成 pilot **14 條**。
   - 13.4／13.5 之 `reasoning` 須明列委派之外部擁有者（§8.2.1）
   - 13.5 之可觀察量自五節全文取得；若確無，回報停下
6. lint（PASS/FAIL + 實測值）；§9 self-check 17 項逐條自評。
7. 全 129 節依九軸機械複掃（§6）。
8. **不寫回 workbook**（18 §3.4）。
9. 上繳 `docs/upstream/11_pilot.md`。git 不執行。

---

## 8. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C21 跨 feature 發現之登記位置 | ✅ §1 | 已簽 2026-08-15 |
| R-C22 不可量化 ≠ 不可觀察 | ✅ §5 | 已簽 2026-08-15 |

兩條適用全 feature，安置位置待 canon re-sync。§2 ~ §4 之裁示為 profile
增補與範圍界定，隨 profile 與 `reasoning` 落地，不入 `RULINGS.md`。
