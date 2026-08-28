# 下放包 15 —— Pei 裁丙、framework 起草（Layer 1 定稿／Layer 2 部分定稿）、T28

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`14_reverse_sample.md`；對應上繳：`docs/upstream/14_layer2_material.md`
- 裁定狀態：**Pei 2026-08-28 裁丙**；R-SU18（framework 之效力分級）—— 分析層即裁

---

## 一、Pei 之裁定（丙）

下放包 14 §六提三案，**Pei 裁丙**：

> 先以現有證據定稿 Layer 1／Layer 2，**Layer 3 標為 provisional**
> 並隨階段二逐列修正。

據此，錨定之嚴謹化（GT-A2／GT-C、機制 4）**與 TC 撰寫並行**，
不再是 framework 之前置。T27 照跑，其結果改為並行線之產出。

---

## 二、R-SU18（新條，抄入 RULINGS.md，逐字）

```
R-SU18（framework 之效力分級 —— 依 Pei 2026-08-28 裁丙）

`framework.md` 之三層具**不同之效力與修改成本**，須於檔內分別標明：

(a) **Layer 1（Test Group）—— 定稿**。值為 `SW Update`（R-SU1）。
    進工作簿。變更須 Pei 裁。

(b) **Layer 2（Test Set）—— 定稿**。進工作簿。
    其切分**不依賴逐列錨定**，依據為 037 Heading 群之結構、
    各群之能力性質、與已裁之跨章事實。
    變更須分析層裁並記其依據；已寫回工作簿者之變更視同修訂。

(c) **Layer 3（spec 章節分群）—— provisional**。**不進工作簿**（IN §4.1.5）。
    其值為現階段之最佳推定，**得於階段二逐列人裁時就地修正**，
    修正不須另發裁決，但須記於該列之 `reasoning` 並回寫 `framework.md`。

    **拘束**：Layer 3 之 provisional 狀態**不得外溢**至
    `specification_reference`。後者一律走階段二之逐列裁定
    （R-SU14 v5），**不得以 Layer 3 之章推定其錨**。
    二者之關係為導航與交付面之別 —— Layer 3 錯了只是導航繞路，
    `specification_reference` 錯了是交付缺陷。

(d) **揭露義務**：`framework.md` 檔首須載本條之三級標示，
    並載「Layer 3 於 {日期} 之覆蓋狀態」（已裁列數／provisional 列數）。
```

---

## 三、Layer 1 —— 定稿

`Test Group = SW Update`（R-SU1、R-SU2 之 `fill_test_group_set = true`）。

---

## 四、Layer 2 —— 切分原則與部分定稿

### 4.1 切分原則（本輪確立，供後續一致套用）

1. **分群鍵為 Heading id**，命名另裁（R-SU10(a)(b)）
2. **跨章之 Heading 群必拆** —— 已實證者 `309`、`170`
3. **純 Service 群之健康判準**改以「共同觸發面與共同觀察面」
   （下放包 06 §3.3；IN §4.1.3 之 UI 入口路徑只在 17 個含 HMI 列之群成立）
4. 單群列數上限以「可作為索引」為度 —— 逾 40 列者須檢視其是否實為多能力
5. 不設 `Misc`／`General`／`Unclassified`（IN §4.1.3）

### 4.2 已可定稿之群（不依賴 `309`／`170` 之拆分結果）

| Test Set | 所轄 Heading id | 列數 |
|---|---|---:|
| `Wi-Fi Download` | 038, 058, 055 | 29 |
| `Update Policy` | 009, 024 | 17 |
| `Silent Update` | 178 | 6 |
| `Session Flows` | 016, 017, 018, 137, 168, 185, 188, 271, 278, 287 | 42 |
| `Client Architecture` | 072, 073, 192, 200, 202, 251, 259, 263, 266, 280, 285 | 35 |
| `Bearer Selection` | 291 | 16 |
| `ROV Installation` | 085, 086, 091, 096 | 20 |
| `TBM Update` | 110, 214 | 50 |
| `USB Update` | 020, 074, 076, 078 | 5 |
| `Update HMI` | 129 | 6 |
| `Configurable Parameters` | 125, 127 | 2 |
| `FOTA Overview` | 001 | 6 |

**與下放包 06 草案之差異**：`291 Bearer selection:`（16 列）
自 `Client Architecture` 析出自成一群（51→35 + 16）。
依據：`292` 之人裁正解為 `4907460`（4.7.3 configurable network priorities）
與 `4907403`（4.6.1 network selection），與 `Client Architecture`
所轄之 4.4／4.5 架構條文分屬不同能力；且其群列數 16 足以自立。

小計 **234 列**。餘 **77 列**（`309` 之 70 + `170` 之 7）待 §五 之材料後切分。

### 4.3 待切分之二群 —— 已知事實

**`SWE1-FOTA-309`（70 列，310–383）** —— 已裁之列所屬章：
`4.8.2`(310, 311)、`4.8.3`(312)、`4.12`(313, 315–324)、
`4.12.1`(328, 329)、`4.12.2`(332)、`4.10.3`(347) ——
**至少 6 章**。其 Heading 標題 `OMA-DM Security` 只描述其前二列。

**`SWE1-FOTA-170`（7 列）** —— 已裁之 `176` 正解在 `4.7.3.2`，
與其 Heading 標題 `Deployment Package Security` 無關。

二群皆須依**列之能力性質**重切，不得沿用其 Heading 標題。

---

## 五、任務（T28）

| # | 任務 |
|---|---|
| T28a | **`309` 群列標題傾印**：`SWE1-FOTA-310`–`383` 全 70 列之 id、`Requirement Title`、`Sub Categorization`。**僅此三欄，不附分數、不附候選** —— 本項供分析層依能力性質切分，附分數會使切分受路徑 A 影響 |
| T28b | **`170` 群列標題傾印**：同格式，`171`–`177`（7 列） |
| T28c | **全 45 Heading 群之列數與 HMI 列數對照表**：Heading id、標題、所轄列數、其中 HMI 列數、Service 列數。供 §4.1 原則 3、4 之複核 |
| T28d | **`framework.md` 骨架建置**：依 R-SU18 建檔首（三級標示 + Layer 3 覆蓋狀態欄），寫入 Layer 1 定稿值與 §4.2 之 Layer 2 定稿表（含 Heading id 與其標題原文，R-SU10(c)）。**Layer 3 節暫留空並標 `PROVISIONAL — 待下放包 16`**。`309`／`170` 二群於 Layer 2 表中標 `PENDING — 待下放包 16 切分` |
| T28e | **T-抄**：R-SU18 逐字 append；索引表同步（18 條現行）。PLAYBOOK 追加：「導航面之推定與交付面之依據須分層，前者可 provisional，後者不可」（出處：R-SU18(c)） |

**併行線（T27）照跑，不因本包改期。**

**不在本輪**：Layer 3、TC、寫回、git。

---

## 六、上繳包要求（`docs/upstream/14_layer2_material.md`）

1. T28e 核對結果 + 索引表
2. T28a／T28b 之列標題表 —— **本輪核心，分析層據以切分**
3. T28c 之對照表
4. T28d 之 `framework.md` 全文
5. 未結 DR
6. 獨立自評 —— 特別回答：**T28a 只給標題不給描述，是否足以支撐能力性質之判斷**
   （若不足，指出其不足之處，但**不要自行補描述** —— 由分析層裁是否加碼）
