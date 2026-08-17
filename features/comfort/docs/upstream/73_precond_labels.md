# 73 — Comfort HMI / J 欄去標籤、I 欄兩段式（三項全做完）

- 產出層：執行層｜2026-08-17｜對象：分析層／Pei
- 依據：下放包 94 ＋ Pei 2026-08-17 之三項指示
- **lint 55 / 55 PASS，0 finding across 434 TCs；assertion 15 / 15 PASS；寫回 ENTRY 030**
- **未交付** —— 交付夾仍為 ENTRY 026 之 `03663159…`

---

## 一、pre_conditions 移除 source class 標籤

| | |
|---|---|
| 作法 | 移除於**寫入路徑**（`write_back.render`），**JSON 保留** |
| 何以如此 | 標籤仍是 R-C28 第一問（出處）之依據，仍受 `source-class-truthful` 等 gate 檢查；**內部依據與外部呈現分離，兩者皆存在**（94 §2.2）|
| 節次括號 | **保留** —— 那是條文出處，非我方語彙 |
| 實測 | JSON **434 / 434** 帶標籤；工作簿 J 欄 **0 格**帶標籤 |
| 新 assertion | `no-source-class-in-workbook`：J 欄 434 格逐格掃描四種標籤，0 命中 |

**94 §2.3 那句自證成立**：標籤自 pilot 起外露了 434 列，
而**沒有任何檢查問過「這一格裡有沒有我們自己的語彙」**。

---

## 二、test_item 上半 —— 條文原文完整照抄

### 2.1 單位

依你選定：**該 leaf 對應之那一句**。037 把同一句切成多個 leaf 者
（`14.19` 之 8 條、`16.13` 與 `16.8` 各 6 條），**那幾條之上半相同** ——
這正是第三項存在的理由。

### 2.2 對應表怎麼來的 —— 以及它為什麼需要人讀

**leaf → 原句之對應從未被存下來**（現行 test_item 是改寫），只能回推。
`scripts/clause_map.py` 之作法與其被推翻之嘗試：

| 試過 | 結果 |
|---|---|
| 逐字相似度（difflib）| 105/434 弱匹配，`16.13` 明顯配錯 |
| 相似度 ＋ 單調對齊 | **更糟** —— 塌到少數句 |
| IDF 詞彙 **cosine** | 好一些，惟**懲罰長句**：`16.13` 之「turns on Sync」被推去短句 |
| IDF **recall** | **獎勵長句**：`3.2` 之「Pressing A/C」被吸進最長之列舉句 |
| **IDF F1 ＋ 低分時取前後鄰葉之句以 recall 定奪** | **採用** |
| 「低分即全節取 recall 最高者」 | **試過並退回** —— `16.8` 上更糟：短句以兩個高 IDF 詞就贏過真正的列舉句 |

**分數救不了的，逐條讀後具名訂正**：`OVERRIDES` 現有 **7 條**
（`16.8` 之四條列舉項、`7.4` 之四條、`7.6` 之一條），各附一句理由。

另修兩處切句：`(e.g.` 之後不切（`14.3` 曾被切成半句）；
**曾以「括號未閉」為併句條件而退回** —— 它在 `7.4` 把 9 句併成 4 句
（`((hold longer that 500 ms))`）。

### 2.3 可證與不可證，分開講

| 性質 | 誰保證 | 實測 |
|---|---|---|
| **「照抄」** | **機器可證** | `test-item-verbatim` gate：上半逐字等於對應表之句，且該句為該節 `full_text` 之**連續子字串** —— **434 / 434 通過** |
| **「選對句」** | **機器不可證** | 低分（<0.40）之 **47 個 leaf 已逐條讀過**；其中 7 條訂正，餘者確認正確（低分多因 item 太短或 037 之措辭與條文不同）|

**這一點必須寫清楚**：gate 能證明我沒有改動條文的字，
**不能證明我挑對了句子**。後者靠讀，而讀過哪些、改了哪幾條，記在
`OVERRIDES` 與本節。

---

## 三、test_item 下半 —— 該條 TC 之情境

**組成**：該條之配置條件（軸 PC，去除三個排除式 PC）＋ 其觸發步驟。

三個排除式 PC（2.14／16.2／6.3）不入情境：**情境要說的是這一條在什麼狀況下
驗什麼，不是它不在什麼狀況下驗。**

實例（`16.13` 之三條，**上半相同、下半各異**）：

```
MAX A/C automatically turns on A/C, changes airflow modes to Face, increases
fan speed at highest setting (7/7), sets temperature (driver and passenger if
available) at lowest setting (LO), change RECIRC to closed (led on), and turns
on Sync.

(The system supports Max A/C; press "MAX A/C" and read the airflow mode)
(The system supports Max A/C; press "MAX A/C" and read the fan speed)
(The system supports Max A/C; press "MAX A/C" and read both temperatures)
```

---

## 四、gate 之異動

| gate | 異動 |
|---|---|
| `item-modal` | **退場** —— profile §3.1 要求 test_item 帶 modal，而**照抄之句不可能被要求帶 `shall`**。這道 gate 問的是「我們寫得夠不夠規範」，而這一格現在有一半不是我們寫的 |
| **`test-item-verbatim`** | 新增 —— 上半逐字等於對應表之句，且為該節全文之連續子字串 |
| **`test-item-situation`** | 新增 —— 須有空行 ＋ `(…)` |
| `no-source-class-in-workbook` | 新增（寫回後 assertion，第 15 項）|
| 反向驗證 | `verify_b_gates.py` 增 **三案**：改一個字即不等（逐位元組，非模糊）／對應表 434 條有 **281 個相異句**（不是同一句發給所有人）／缺 `(…)` 即偵出 |

lint **54 → 55 道**。

**`test_item_authored`**：原作者所寫之句移入此欄（doc 層，`NOT_IN_WORKBOOK`）
—— **它是當初判讀該 leaf 之依據，日後複判時需要它**，不丟。

---

## 五、profile

- **§3.1** 加前言：其形態已被本裁定改寫，modal 要求退場；G-1 之量測與 `home`
  對照**保留為紀錄**（它們是當時判定之依據），結論已被取代
- **新增 §3.1.1**：兩段式之格式、對應表之出處、
  **「可證與不可證」之分表**、`item-modal` 退場之理由
- **§3.2** 加 94 §2 之裁定：標籤不入工作簿、節次括號保留

---

## 六、寫回 ENTRY 030

| | |
|---|---|
| 產出 | `…_SWQT_Comfort_20260817_itemfmt.xlsx`　`97e469fee8e4d18b…` |
| 來源 | ENTRY 022 之 ext 母本（未動）|
| 列 | row 10–443，**434 列**（筆數未變，變的是 I 與 J 兩欄）|
| 前置 gate | **6 項全 PASS**（BASELINE 11 OK；DELIVERY 驗過 68／已知不存在 1／問題 0）|
| assertion | **15 項全數 PASS** |
| 狀態 | **未經 Excel 確認；尚未交付** |

**附帶**：ENTRY 028 之 `corpus-divergence`（`-382` 之 N 欄版本名）於本輪之
全量重寫中**已帶入 SR25** —— 惟其消解**要到本檔交付後才成立**，
故 ENTRY 030 記其為「附帶」，不逕行改 028 之增註。

---

## 七、待 Pei

1. **Excel 四項確認**，對象 `…_20260817_itemfmt.xlsx`（`97e469fe…`）
2. 確認後複製至交付夾（覆蓋 `…_20260816_extdocs.xlsx`？抑或並存），
   **本層不自行複製**；複製後唯讀驗證並登 `delivered`

**未做**：未複製、未移除交付夾任何檔案；未改 RD-1；git 未執行。
