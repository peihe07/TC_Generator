# 下放包 05 —— Vehicle Category：DECISIONS 簽署前置 + framework Part N 提案

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）／Pei
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/05_partN.md`
- 前一包：`docs/handoff/04_priority.md`（commit `ecee654`）
- 對應之上繳包：`docs/upstream/04_priority.md` §7「待裁」

---

## 一、`spec_reference: [PROPOSED: None]` 之裁定

**裁：簽署時手動覆蓋，不修腳本。**

理由三項：

1. **覆蓋是終局的。** A-TM15 已證 `recon.py` 不覆寫既存之 `DECISIONS.md`
   （本 feature T14 實測即觸發該保護）。一旦簽入 `DECISIONS.md`，
   該值不再被任何重跑動到。會被覆寫的是 `DECISIONS.new.md` ——
   那是產出檔，本就不該手改。
2. **R-VC8 之授權邊界已明文寫死**：「本條為 Tier 2 工具修法之授權，
   範圍僅限上述。`recon.py` 之其他行為一律不動。」
   本項為**顯示層**（f-string 印出 Python `None`），
   與 R-VC8 所修之**資料層**（TSV 之 `spec_reference` 欄）不同處。
   在同一 feature 生命週期內二度改 `recon.py`，且第二次只為修飾產出檔之
   可讀性，不符該邊界之設立意旨。
3. **本項非本 feature 獨有。** `display` 之 `feature.yaml` 同樣宣告
   `spec_reference_template: null`，其 `DECISIONS.new.md` 應有同樣症狀。
   跨 feature 之共通缺陷，處置屬全域排程，不由單一 feature 之簽署流程決定。

簽入 `DECISIONS.md` 時，該行改為：

```
- spec_reference: 逐字取 037 `HMI Source ID` 欄原值（R-VC4）。
  `feature.yaml` 之 `spec_reference_template: null` 係「查得而非構造」
  之宣告，非空值；資料件見 `data/recon_leaf_to_section.tsv`（145/145 逐字相符，
  R-VC8 修法後之產出）。
```

### A-VC11（新立）

```
A-VC11（recon.py 之 DECISIONS 顯示層將 null 印為字面 None）

`scripts/recon.py` 產生 `DECISIONS.new.md` 之 §4 Style bindings 時，
以 f-string 直接內插 `cfg.get("spec_reference_template")`，
該鍵之值為 `null` 時印出 Python 之 `None`，成為
`- spec_reference: [PROPOSED: None]`。

`None` 非裁定值 —— 它是「未宣告 template」之內部表示被洩漏到產出檔。
簽署者若照簽，簽到的是字面 `None`。

範圍：非本 feature 獨有。凡宣告 `spec_reference_template: null` 之
feature 皆會複現（`display` 之 feature.yaml 同此宣告）。

處置：本 feature 採**簽署時手動覆蓋**（下放包 05 §一），不修腳本。
根治須改顯示層，屬 Tier 2 工具修法，**與 R-VC8 之資料層修法非同一件，
不得併案**（同 A-VC8 之邊界）。與 A-VC4／A-VC8 併入全域排程。

狀態：PENDING（全域排程）。
```

**`DECISIONS.md` 之簽署**：上繳包 04 §6 之送簽內容全數追認，
另依其 §6.4 增列一行指向 `data/priority_final.tsv`，
否則 117 筆 priority 定案不在決策表之視野內。簽署為 Pei 之權（Tier 3）。

---

## 二、framework Part N 提案（Layer 2 切分）

> **本節為提案，非裁定。** Layer 2 之切分屬 Tier 2，須 Pei 簽署後
> 始得寫入 `framework.md`。執行層不得據本節逕自建檔。

### 2.1 §4.1.2 之兩來源：先退化，再救回

IN §4.1.2 要求 Layer 2 候選取二來源之**交集**：
(i) spec table of contents、(ii) RD analysis report grouping。

本 feature 之 (ii) 起初看似退化 —— 037 之 `HMI Source ID` 就是規格章節號，
兩來源同源，交集法失去交叉驗證作用。

**但 037 另有一個獨立於章節之分群軸：`Sub Categorization`。**
實測其對 117 leaf 之分布：

| 章 | HMI | Service | 混章 |
|---|---|---|---|
| 2, 3, 4, 5, 6, 7, 12, 14, 16 | 各章全 HMI | 0 | 否 |
| **11** | **5** | **15** | **是** |
| 13 | 0 | **16** | 否 |

**章 11 為唯一之混章，且其切分為連續、零交錯**：

```
11.1 – 11.6     → Service（15 筆）
11.7 – 11.8.1   → HMI    （5 筆）
```

逐節檢視其語意：

| 段 | 節 | 內容 | 037 之歸類 |
|---|---|---|---|
| 前段 | 11.1 隱藏／灰化、11.2 回復預設、11.3 清除個資、11.4 懸吊互斥、11.5 語言變更、11.6 中文彈窗 | **設定項之行為與可用性** | Service |
| 後段 | 11.7 左選單列、11.7.1 無選單列、11.8 截斷改箭號、11.8.1 括號顯示目前值 | **清單之版面與呈現** | HMI |

即：037 作者在章 11 內部，把「設定做什麼」與「清單長什麼樣」切開了。
**這是規格目次看不見的邊界** —— 二來源於此**不同源**，交集法恢復作用。

> 揭露：除章 11 外，`Sub Categorization` 與章節邊界完全重合，
> 未提供額外資訊。故交集法之交叉驗證效力**僅及於章 11 之一刀**，
> 其餘 Layer 2 邊界仍只有單一來源（規格目次）支撐。
> 這是本提案之主要弱點，據實揭露而非掩飾。

### 2.2 提案：8 個 Test Set

| # | Test Set | Layer 3（spec sections） | Sub Cat | leaves | 佔比 |
|---|---|---|---|---|---|
| 1 | `Category Structure` | 2.2 – 2.6.3 | HMI | **24** | 20.5% |
| 2 | `Controls` | 3.1 – 3.9 | HMI | **17** | 14.5% |
| 3 | `Glove Box` | 4.1, 4.2, 5.1, 5.2, 6.1, 6.2, 6.3, 7.1 | HMI | **12** | 10.3% |
| 4 | `Settings Behavior` | 11.1 – 11.6 | **Service** | **15** | 12.8% |
| 5 | `Settings Presentation` | 11.7, 11.7.1, 11.8, 11.8.1, 12.1 – 12.8 | HMI | **30** | 25.6% |
| 6 | `Ignition Availability` | 13.1 – 13.5 | **Service** | **16** | 13.7% |
| 7 | `Brake Service` | 14.1 | HMI | **2** | 1.7% |
| 8 | `Cabrio Widget` | 16.2 | HMI | **1** | 0.9% |

**合計 117 leaves ／ 66 sections。** 區間 1–30；排除 7、8 後為 12–30。

### 2.3 各邊界之依據

**#4 / #5 之分界（章 11 一刀兩斷）** —— 唯一有二來源支撐者。
`Settings Behavior`（Service）與 `Settings Presentation`（HMI）
之 setup 確實共用（皆自 Settings 頁籤進入），但驗證標的不同：
前者驗「這個設定做了什麼」，後者驗「清單與控制項長什麼樣、怎麼操作」。
037 之 `Sub Categorization` 獨立支持此切分。

**#5 之合併（11.7–11.8.1 併入章 12）** —— 二者同為 `Sub Cat = HMI`、
同為 Settings 頁籤之呈現與互動，setup pattern 與 UI entry path 共用。
若獨立成組僅 5 筆，觸 §4.1.3「too granular」。
依 §4.2「Prefer broader shared capability when unsure」→ 合併。

**#6 之邊界** —— 章 13 全 16 筆為 `Sub Cat = Service`，且**恰等於
FROP = Power Management 之 16 筆**。R-VC3 表 A 之揭露將與此 Test Set
一對一對應，無需跨組拆解。（FROP = Audio Management 之 1 筆
`VC-048-02` 落於 #5 內，表 A 須單獨標註。）

**#7 / #8 之保留（2 筆與 1 筆）** —— 二者皆觸 §4.1.3 之
「filter 後應得有意義之群」測試。仍建議保留，理由**不是** outlier 特許，
而是**二者皆為待補節會使其長大之組**：

| 組 | 現有 | R-VC3 表 B 中之待補節 | 若 DR-VC3 回覆「應補」後之規模 |
|---|---|---|---|
| `Brake Service` | 2 | 14.2（彈窗優先序）、15（11 個 EPB 彈窗）| 約 2 + 1 + N |
| `Cabrio Widget` | 1 | 16.2.1、16.2.2 | 3 |
| （另）Cabrio 本體 | 0 | 8.1–8.5、9.1、9.2 | 7 —— **屆時應另立 `Cabrio Rooftop`**，非併入 #8 |

**現在把它們併入他組，等於為一個已知會逆轉的狀態做結構調整。**
保留其邊界，待 DR-VC3 回覆後一次定案。

### 2.4 已排除之替代案

| 替代 | 內容 | 不採之理由 |
|---|---|---|
| 甲 | `Brake Service` 併入 `Ignition Availability`，成 `Conditional Availability`（18）| 形態雖近（狀態阻擋＋彈窗），但 037 之 `Sub Categorization` 將二者分屬 HMI／Service —— **二來源皆指向分立**，合併等於推翻上游分群 |
| 乙 | 章 11 不切，`Settings`（20）＋`Settings Interaction`（25）| 章 11／12 之邊界僅有規格目次支撐；而 11.1–11.6 與 11.7–11.8.1 之分界有二來源。**捨強從弱** |
| 丙 | `Cabrio Widget` 併入 `Category Structure` | widget 位於 Home Screen，非 Vehicle Category 頁籤內，setup 與 entry path 皆不共用 |

### 2.5 尚未決之事（不在本提案內）

- **Layer 2 名稱之最終用字**。上表為提案用字，皆為 §4.2 所要之
  英文名詞片語、無 Test Group 前綴、無動作標籤。
  若 Pei 對 `Settings Behavior` ／ `Settings Presentation` 之措辭
  另有偏好，改名不動邊界。
- **`framework.md` 之驗算腳本**（比照 comfort 之 `verify_partn.py`）。
  待邊界簽署後始得寫，否則驗算的是未定案之數字。

---

## 三、執行層任務

> **T33 為 Tier 2，須 Pei 簽署 §二之邊界後始得執行。T31／T32 不受此限。**

| # | 任務 | Tier |
|---|---|---|
| T31 | `ANOMALIES.md` 新增 A-VC11（條文逐字）。**不修 `recon.py`** | 1 |
| T32 | 產出 `DECISIONS.md` 之**送簽稿**：以上繳包 04 §6 之內容為底，
`spec_reference` 一行改為 §一之覆蓋文字，並增列指向 `data/priority_final.tsv` 之一行。**產出送簽稿，不簽署、不合併** | 1 |
| T33 | Pei 簽署 §二之邊界後，寫 `features/vehicle_category/framework.md`（比照 comfort 之形制：§1 三層定義與去向、§2 Layer 2 表、§3 分組判準、§6 逐節明細），並產出 `data/layer3_map.tsv`（117 列）與 `data/test_set_map.tsv`（66 列）| 2 |
| T34 | 隨 T33 產出 `scripts/verify_partn.py`，至少四個 assertion：leaf 總數 117、section 總數 66、各 Test Set 之 leaf 數與 §2 表相符、無 leaf 落於二組或零組 | 1 |

**不在本輪範圍**：任何 TC、任何寫回、任何 git 操作、
`DECISIONS.md` 之實際簽署（Tier 3）。

---

## 四、上繳包要求

`features/vehicle_category/docs/upstream/05_partN.md` 須含：

1. T31–T34 逐項結果（T33／T34 若未獲簽署則載明「待簽，未執行」）
2. A-VC11 之 byte-level diff
3. T32 之送簽稿全文
4. §2.2 之 8 組 leaf 數獨立重測（**不得引用本包之數字**，須自 037 重數）
5. §2.1 之 `Sub Categorization` 分布獨立重測，特別是「章 11 為唯一混章
   且切分連續零交錯」之驗證
6. 更新後之未結 DR（七筆）與 A（七筆）清單
7. 量測條件揭露（R-G8）

---

## 五、Pei 之最短回覆格式

```
DECISIONS spec_reference: 准（簽時覆蓋）/ 改修腳本
Layer 2 邊界: 准 / 甲 / 乙 / 丙 / 其他
Test Set 名稱: 准 / 改（列出）
```
