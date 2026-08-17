# FW036 User Profiles — Framework Part（**定稿**，仍待分析層覆核方為定案）

- 產出層：執行層｜2026-08-17（08 輪定稿，下放包 08b 作業項 6；草案出於 05 輪）
- **狀態：定稿，待覆核。** Layer 2 由 **R-U20** 定案；Layer 3 之對映與生成分母為本層所擬。
  **08b 明文：定稿後回報，仍待分析層覆核方為定案。**
- 依據：`RULINGS.md` R-U1（Test Group）、R-U4（母體 180）、R-U19（135／133 分立）、R-U20（八組）、R-U25／R-U35（判讀依據面）
- 母體：**180 leaf ／ 133 生成 section**（見 §4 之兩數之別）

## 0. 判讀依據面（R-U25／R-U35）—— 定稿之前提

本表之數字分兩類來源，**不可互推**：

| 數 | 來源 | 說明 |
|---|---|---|
| leaf 數（180）、章別分布、Test Set 之 leaf 分配 | **037** | 與 spec 內文無關；三閘 180／25／2 已驗 |
| 生成 section（133）、section 之內文 | **spec** | **其判讀基準為 `outline_map.json` 之 `pdf_text`（PDF 側）**，非 `text`（xlsx 側）|

**xlsx 側已知會少句**：07／08 輪測得真掉句 **5 節／3.6% 節數／2.1% 字元**
（分子定義：該節 PDF 側有、而全 169 節之 xlsx Description 皆無之片段）。
其七條補句登記於 `data/xlsx_missing_clauses.tsv`，**全部 must_carry**。

**已知例外（R-U38）**：`2.1`（Reference Documentation 表）為**唯一 xlsx 較 PDF
完整**之節 —— 其表於 PDF 為圖。該節屬章 2，不入生成範圍。
**故「PDF 為內文之準」不是無例外之通則。**

---

## 1. 三層之定義與去向

| Layer | 值 | 進工作簿？ |
|---|---|---|
| 1 Test Group | `User Profiles` | ✅ G 欄（R-U6：`fill_test_group_set: true`）|
| 2 Test Set | 八組之一（§2）| ✅ H 欄 |
| 3 spec section | outline 節次（如 `5.13.2`）| ❌ **不入** |

**Layer 1 之值取自 037 之 FROP 欄實測**（R-U1）：`User Profiles` 182 列
（＝180 Functional Requirement ＋ 2 Out of scope），空值 25 列恰為 Heading 列。
**03 輪首次複驗成立。**

Layer 3 之去向為 `specification_reference`（N 欄），依 R-U1 之格式：

```
Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_{section}
```

**不改寫為 `User Profiles`，亦不使用檔名之 `R1L-R (February_10_2023)` 形式**（R-U1）。

---

## 2. Layer 2 —— 八個 Test Set（R-U20 定案，逐字）

| # | Test Set | spec 章 | **leaves** | 生成 section | 佔比 |
|---|---|---|---|---|---|
| 1 | `Preference Storage` | 4 | **28** | 16 | 15.6% |
| 2 | `Profile List` | 5 | **40** | 27 | 22.2% |
| 3 | `Defaults` | 6 | **11** | 10 | 6.1% |
| 4 | `Welcome Flow` | 7 | **14** | 9 | 7.8% |
| 5 | `Setup Flow` | 8 | **25** | 20 | 13.9% |
| 6 | `Editing` | 9 ＋ 10 | **25** | 24 | 13.9% |
| 7 | `Connected Account` | 11 | **6** | 4 | 3.3% |
| 8 | `Valet Mode` | 12 ＋ 13 ＋ 14 | **31** | 23 | 17.2% |
| | | | **180** | **133** | |

**八組之 leaf 數逐組實測相符**（04 輪，量測條件：`Categorization ==
Functional Requirement` 之 180 列，依其 `HMI Source ID` 之章別歸組）。
區間 **6–40**，最大者佔 **22.2%**。

### 2.1 命名判準（R-U20，解 03 輪自陳之不一致）

> canon §4.2 禁止的是重複 Test Group 之**整體** —— 即不得出現
> `User Profiles xxx`；**單一詞 `Profile` 在承載能力語義時允許。**

據此：

| 03 輪草案之疑慮 | R-U20 之處置 |
|---|---|
| `All Profiles Tab` 為 UI widget 名 | 取 **`Profile List`** —— 能力是「多個 profile 之列出、選取、切換、上限、排序」，不是那個分頁 |
| `Profile Overview` 重複前綴 | 取 **`Preference Storage`** —— ch4 之主體為偏好之儲存與跨 key cycle 回復 |
| `New Profile Setup` 重複前綴 | 取 **`Setup Flow`** |
| （ch6）`Default Profiles` 含 `Profiles` | 取 **`Defaults`** |
| （ch7）`Welcome Screen`／`Welcome Popup` 為 UI widget 名 | 取 **`Welcome Flow`** |

### 2.2 三處合併之理由

- **`Editing` = ch9 ＋ ch10**：ch10（Profile Info Page，3 leaf）自成一組會使
  Test Set 欄淪為 TC ID 之副本（§4.1.3 過細）。且 `10.2` 之觸發即
  `Edit Profile` 分頁上之「What is linked to my Profile」列 —— **同一進入路徑**。
- **`Valet Mode` = ch12 ＋ ch13 ＋ ch14**：三章分別為 Valet 之進入、SPAAK 變體、
  退出，§4.2 明文「Different steps, UI paths, or sub-states of the same
  capability should share one Test Set」。
- **`Profile List` 40 leaf 不拆**：§4.2「Prefer broader shared capability when
  unsure」。前例：Comfort 之最大組 59 leaf（14.6%）未拆。

---

## 3. Layer 3 —— 章 4–14 之對映

**章 1–3 不入生成範圍**（01b 裁定），惟 **`3.1`–`3.5`（PLP 表）為
`PROF-001-01` 之 in-scope 依據**（R-U22）—— 其 `specification_reference`
併列 `4.1` 與 `3.x`。**這是章 1–3 唯一得被引用之情形。**

| 章 | 標題（spec）| Test Set | leaf | 生成 section |
|---|---|---|---|---|
| 4 | Profile Overview | `Preference Storage` | 28 | 16 |
| 5 | All Profiles Tab | `Profile List` | 40 | 27 |
| 6 | Default Profiles - No Custom Profiles | `Defaults` | 11 | 10 |
| 7 | Welcome Screen (Custom Profile) | `Welcome Flow` | 14 | 9 |
| 8 | New Profile Setup | `Setup Flow` | 25 | 20 |
| 9 | Editing a Profile | `Editing` | 22 | 21 |
| 10 | Profile Info Page | `Editing` | 3 | 3 |
| 11 | Connected Profile App | `Connected Account` | 6 | 4 |
| 12 | Valet Mode | `Valet Mode` | 25 | 18 |
| 13 | Valet Mode - SPAAK | `Valet Mode` | 4 | 3 |
| 14 | Valet Mode - Exit | `Valet Mode` | 2 | 2 |
| | | | **180** | **133** |

逐 section 之對映見 `data/generation_sections.tsv`（133 列，含 `test_set` 欄）。

---

## 4. 兩個數 —— 135 與 133，**不得互換**（R-U19）

| 數 | 意義 | 檔 |
|---|---|---|
| **135** | **037 引用了哪些 section** —— 該記載正確，不改 | `data/expected_cited_sections.tsv` |
| **133** | **哪些進生成** —— **覆蓋率分母與 batch 排程依據** | `data/generation_sections.tsv` |

差的兩條**逐一具名**：

| outline | 唯一引用者 | 該列之 Categorization |
|---|---|---|
| `4.7` | `SWE1-HMI-PROF-017` | Out of scope（R-U4 排除）|
| `5.11` | `SWE1-HMI-PROF-035` | Out of scope（R-U4 排除）|

> **R-U3 之證據行「037 引用之 135 個 section id 缺漏 0」仍為真** ——
> 135 條確實都在 spec 裡。**但它不是覆蓋率的分子。**
> 引用任一數時一律具名是哪一個。

---

## 5. 生成前之已知阻斷（草案階段即列，非屆時才發現）

| 範圍 | 事由 | 條 |
|---|---|---|
| **spec `4.1.1`** 之 popup 引用 | DR #4：`PU1087`／`PU1088` 不在現有 Pop Up List | **R-U15** |
| **寫回實作（Phase 6）** | A-UP09 之 x14 DV gate 未立且未實跑 | **R-U14** |

**兩者皆不擋 Phase 1／framework。**

`PROF-001-01`（PLP 表）**已解除** —— R-U22 之可讀性查證通過（05 輪 §5）。

---

## 6. 生成階段之強制事項（Phase 2 起適用）

| # | 事項 | 依據 |
|---|---|---|
| 1 | spec 內文一律取 `outline_map.json` 之 **`pdf_text`**；`text` 僅供追溯 | R-U35 (a) |
| 2 | 補句表七條為 **must_carry** —— 其所屬 outline 生成時強制入 prompt context | R-U35 (b) |
| 3 | **R1 High 之 TC 字面值不得出現 `Stellantis Account`**（應為 `Connected Account`）| R-U35 (c)、§8.7.3；lint `lint_variant_labels.py` |
| 4 | Table CPA2（PDF p17）／Table EDPR1（PDF p14）為 ER 列舉之來源，生成時回查 | R-U35 (d) |
| 5 | **spec `4.1.1` 之 popup 內文不寫逐字 ER**（觸發、顯示與否、分支可驗）| R-U15／R-U27 |
| 6 | `3.1`–`3.5`（PLP 表）僅作 `PROF-001-01` 之 in-scope 依據，**不另生成獨立 TC** | R-U22／R-U28 |
| 7 | **寫回不得開工** —— A-UP09 之 x14 DV gate 未立且未實跑 | R-U14 |

## 7. 待覆核之處（本層不自裁）

1. **ch9／ch10 之合併**與 **ch12–14 之合併**（§2.2）—— R-U20 已定 Test Set，
   本表之 Layer 3 逐章對映為本層所擬。
2. **`3.1`–`3.5` 得被引用之範圍**（§3）—— 本層讀 R-U22 為「僅 `PROF-001-01`」，
   若其他 leaf 亦引 PLP 表則須擴充。
3. **Test Set 之工作簿寫入**（R-U6 定 `FILL`）—— 本表未涉 H 欄之實際字串大小寫，
   與 §2 之表逐字相同即可。
