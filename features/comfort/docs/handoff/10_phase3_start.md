# 10 — Comfort HMI / Phase 3 開始 ＋ DR #8 DEFERRED ＋ R-C17

- 產出層：分析層｜2026-08-14｜對象：執行層
- 裁定：Pei，2026-08-14（DR #8「空著就好，我會跟 RD 反應」；Phase 3「要」）

---

## 1. 已簽裁決條文

```
R-C17  Home Screen HMI L&F 之定位

Home Screen HMI Logic and Flow（R1 SR24 Post 2A, March 17 2023）於 Comfort
feature 為外部參照 spec，非本 feature 之驗證來源。

Comfort ch17／ch18 所擁有者，僅「Comfort widget 自身之內容與行為」。
Home Screen 之首頁管理行為（HSD1–HSD13、HSS、SW、BSP 各條 —— 新增／刪除／
重排頁面、widget 拖放、Shortcuts 編輯、品牌頁預設配置等）由 Home Screen 之
SWE 需求擁有，不得寫入 Comfort TC（§8.4.2）。

判定測試：該規則定義於 Comfort spec，或定義於 Home Screen spec？
定義於後者即 out of scope，縱使 Comfort spec 引用之。

若 Home Screen 於本專案無對應 SWE 需求，該情形為 coverage hole，於
reasoning 揭露並列 RD-1，不得靜默吸收進 Comfort TC。
```

理由：本輪 Pei 提供該 spec 後，最可能發生之偏移即為把 HSD 系列首頁管理行為
當成 Comfort widget 行為來測。兩者在同一畫面上，但擁有者不同。

---

## 2. DR #8 —— 轉 DEFERRED

Pei 裁定：DR #8（CFTS043 4803259 NOTE 與其 `Radio` 屬性矛盾）由 Pei 直接向
RD 反應，不由本 pipeline 追。

依 R15-2（open PENDING 意為「待裁決」，非「待外部條件」），DR #8 自 open
PENDING 移出，狀態改 **DEFERRED**，並自「阻塞 D-C10」之清單移除。

20.1 ~ 20.4.3 十節維持 `undetermined`（R-C12），`pending_on` 改記
`DEFERRED — Pei 直接向 RD 反應（2026-08-14）`。**不因 DEFERRED 而升為
in_scope**，亦不降為 out_of_scope。

---

## 3. DR #6 —— Home Screen spec 之處置

Pei 提供 `Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023)`。

**實測：該檔已在 repo**，不需補入 —— 
`spec-index/cache/SYS1_HMI_Home_Screen_HMI_Logic_and_Flow_R1_SR24_Post_2A_
(March_17_2023).xlsx`（54.29 KB）與同名 `.json`（6.09 MB）。

**該檔不關閉 DR #6，須明記**：其 Assumptions 列舉之機種
（R1 Low 7"／8.4"／10.1"L／10.1"P／10.25"／12.3"）為**文件涵蓋範圍**，
與 SR24 §1.1、`Vehicle Category HMI L&F` 同型；06 §3 已裁此不構成交付範圍
證據。其 `Available Widget Size` 兩表（VMB：R1 Low 7"／R1 High-Low 10.25"／
R1 High 12.3"；HMB：8.4"／10.1"／12"／12"P／10.1"P）同樣是平台配置表，
不宣告本次交付出哪幾種。

故 19.1 ~ 19.3（7"）維持 `undetermined`。DR #6 保持 open，但**不阻塞
Phase 3**（3 節，占 403 之 0.7%）。

**但該檔對 Phase 4 有實質價值**，登記為 Comfort 之外部參照 spec：
- HS9.4 `Seats & Wheel`、HS9.5 `Comfort` 兩個 widget 之 Reference Document
  皆為 Comfort HMI —— 確認 ch17／ch18 之內容擁有者是 Comfort 而非 Home Screen
- HSD13：有 lower non-articulating screen 時不提供 heated/vented seats、
  heated wheel、comfort 之 widget 與 shortcut —— 與 Comfort 13.1
  （lower comfort screen 條件）相關，Phase 4 寫 ch13／ch17 TC 時須併看
- 引用時 spec_reference 依 §10.7 另列該檔之 section，不併入 Comfort stem

---

## 4. Phase 3 開始 —— 作業指示

Pei 裁定開始。母體為 **403 leaves**（確定）；17 節 substantive 依 R-C16
為 RD-1 覆蓋缺口項，**不入 Part N 之切分母體**，但其所屬章節須留為可插入
之邊界（07 §5，已記入 RUNBOOK）。

### 4.1 先產 Layer 3 map（Part N 之輸入，本包唯一量測作業）

分析層無法在缺 section 級標題與分布下起草 Layer 2，故先產：

`features/comfort/data/layer3_map.tsv`，每列一個 037 所引用之 spec section
（共 129 列），欄位：

| 欄 | 內容 |
|---|---|
| `chapter` | 章號 |
| `chapter_title` | 章標題（自 SR24 export） |
| `outline` | section 節次 |
| `section_title` | 該節標題或首句（前 60 字） |
| `leaf_count` | 該節之 037 leaf 數 |
| `req_ids` | 該節之 SWE1-HVAC-NNN parent id（可多個） |

**驗算 assertion**（PASS/FAIL + 實測值）：
- `leaf_count` 總和 == 403
- 列數 == 129
- 章別分布與上繳 01 §3 之 `leaves by chapter` 逐章相符
  （2:92、3:14、6:1、7:38、9:8、10:15、11:37、12:22、13:14、14:40、
  15:2、16:99、17:18、18:3）

### 4.2 併附兩章之細部分布

章 2（92 leaves／22 sections）與章 16（99 leaves／18 sections）合計 47%，
Layer 2 granularity 成敗集中於此。除 TSV 外另於上繳包列出此二章之
section → 標題 → leaf_count 明細，供分析層起草。

### 4.3 不做者

- **不自行決定 Layer 2 Test Set**。Part N 之推導與 granularity 屬 Tier 2
  （FEATURE_ONBOARDING §0），由分析層起草、Pei 簽署。
- 不寫 profile `[OVERRIDE]`（同屬 Tier 2）。
- 不產 TC、不指派 tc_id。
- 不簽署 `DECISIONS.md`。

### 4.4 上繳

`docs/upstream/05_layer3_map.md`，附「本包是否仍有該驗而未驗者」之獨立
判斷，並更新 `docs/INDEX.md`。git 不執行。

---

## 5. 現況總表

| 項目 | 狀態 |
|---|---|
| 403 leaves | 確定，進 Phase 3 |
| 20.1~20.4.3（10 節） | `undetermined`，DR #8 **DEFERRED**（Pei 對 RD） |
| 16.1、18.2~18.4（4 節） | `in_scope`，依 R-C16 為 RD-1 覆蓋缺口項，不入分母 |
| 19.1~19.3（3 節） | `undetermined`，DR #6 open，不阻塞 |
| 21.x（6 節） | out of scope（R-C5，基線為 SR24） |
| D-C10 | 4 節已有處置；10 節俟 RD 回覆；3 節俟 DR #6 |
| `DECISIONS.md` | 未簽署（Tier 2，含 exemplar 具名 `home`、pilot 取第 13 章兩項建議） |

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C17 Home Screen HMI L&F 之定位 | ✅ §1 | 已簽 2026-08-14 |

R-C17 須貼入 `RULINGS.md`。§2 之 DEFERRED 轉態、§3 之 DR #6 處置皆為狀態
變更，不產生新條文。
