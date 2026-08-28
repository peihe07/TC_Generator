# framework.md — SW Update

狀態：**分層效力（R-SU18，Pei 2026-08-28 裁丙）** ——
**Layer 1 定稿**／**Layer 2 定稿（77 列待切分）**／**Layer 3 PROVISIONAL**。
Feature slug：`sw_update`
規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、
FO §0（Tier 2：framework Test Set derivation 屬 Pei 簽核）、
R-SU1／R-SU10／R-SU18

---

## 效力分級（R-SU18(d) 之揭露義務）

| 層 | 效力 | 進工作簿 | 變更成本 |
|---|---|:--:|---|
| **Layer 1**（Test Group） | **定稿** | ✅ | 須 Pei 裁 |
| **Layer 2**（Test Set） | **定稿**（77 列 PENDING） | ✅ | 須分析層裁並記依據；已寫回者視同修訂 |
| **Layer 3**（spec 章節分群） | **PROVISIONAL** | ❌（IN §4.1.5） | 階段二逐列人裁時就地修正，不須另發裁決；須記於該列 `reasoning` 並回寫本檔 |

> ⚠ **R-SU18(c) 之拘束**：Layer 3 之 provisional 狀態**不得外溢至
> `specification_reference`**。後者一律走階段二之逐列裁定（R-SU14 v5），
> **不得以 Layer 3 之章推定其錨**。
> 二者為導航與交付面之別 —— Layer 3 錯了只是導航繞路，
> `specification_reference` 錯了是交付缺陷。

**Layer 3 於 2026-08-28 之覆蓋狀態**：

| | 列數 |
|---|---:|
| 已裁（GT-A1 人裁） | **28** |
| 區塊導出（GT-B，不入回測） | 4 |
| **PROVISIONAL（未裁）** | **279** |
| 合計（R-SU3 母體） | 311 |

---

## Part I — Layer 1（Test Group）—— 定稿

```
SW Update
```

依 IN §4.1.1 與 **R-SU1**：Layer 1 = feature 名。
037 檔名作 `SoftwareUpdate`、SYSAD 作 `Software Update`、CFTS 母件為
CFTS_57 Reflash —— 交付面統一取 `SW Update`（Pei 2026-08-27 裁定 Q6）。
依 **R-SU2** 之 `fill_test_group_set = true`，寫入工作簿 Test Group 欄，
全簿逐字一致。**變更須 Pei 裁**（R-SU18(a)）。

---

## Part II — Layer 2（Test Set，寫入工作簿）—— 定稿

分群鍵為 **Heading id**（R-SU10(a)），命名另裁（R-SU10(b)）；
本表同時記 Heading id 與其標題原文（R-SU10(c)）。
依 IN §4.2：英文名詞片語、不重複 Test Group 前綴、
**不設 `Misc`／`General`／`Unclassified`**（IN §4.1.3）。

### 切分原則（下放包 15 §4.1，供後續一致套用）

1. 分群鍵為 Heading id，命名另裁（R-SU10(a)(b)）
2. **跨章之 Heading 群必拆** —— 已實證者 `309`、`170`
3. 純 Service 群之健康判準改以「共同觸發面與共同觀察面」
   （下放包 06 §3.3；IN §4.1.3 之 UI 入口路徑只在 **17 個含 HMI 列之群**成立
   —— 實測相符，見上繳包 14 §T28c）
4. 單群列數上限以「可作為索引」為度 —— **逾 40 列者須檢視其是否實為多能力**
5. 不設 `Misc`／`General`／`Unclassified`（IN §4.1.3）

### 定稿之 12 組（234 列）

| # | Test Set | 能力叢集 | 所轄 Heading id | 列數 | HMI | Service |
|---:|---|---|---|---:|---:|---:|
| 1 | `Wi-Fi Download` | Wi-Fi 下載路徑：Wi-Fi 連線建立、經 Wi-Fi 之軟體下載、非關鍵更新之下載 | `SWE1-FOTA-038`、`SWE1-FOTA-058`、`SWE1-FOTA-055` | 29 | 12 | 17 |
| | | *Heading 標題原文*（R-SU10(c)）：038 OTA download via Wi-Fi；058 Connection to Wi-Fi network；055 Non-Critical Updates | | | | |
| 2 | `Update Policy` | 更新之優先序與關鍵性政策：Critical／Regular／Silent 之分級與其套用 | `SWE1-FOTA-009`、`SWE1-FOTA-024` | 17 | 4 | 13 |
| | | *Heading 標題原文*（R-SU10(c)）：009 Critical Updates；024 Critical Updates | | | | |
| 3 | `Silent Update` | 靜默更新之流程與其通知拘束 | `SWE1-FOTA-178` | 6 | 1 | 5 |
| | | *Heading 標題原文*（R-SU10(c)）：178 For a silent update, the OTA client follows these steps for the download | | | | |
| 4 | `Session Flows` | 工作階段流程：部署流程、車端／使用者／伺服器發起之各 session 與其前置條件 | `SWE1-FOTA-016`、`SWE1-FOTA-017`、`SWE1-FOTA-018`、`SWE1-FOTA-137`、`SWE1-FOTA-168`、`SWE1-FOTA-185`、`SWE1-FOTA-188`、`SWE1-FOTA-271`、`SWE1-FOTA-278`、`SWE1-FOTA-287` | 42 | 11 | 31 |
| | | *Heading 標題原文*（R-SU10(c)）：016 Session Flows；017 Deployment Flow；018 Installation and Download Conditions；137 Deployment flow；168 Vehicle-Initiated Session Flow；185 OTA client sessions；188 User initiated sessions；271 OTA server initiated sessions；278 User initiated sessions；287 OTA client Flows | | | | |
| 5 | `Client Architecture` | OTA client 之架構面：介面定義、匯流排通訊、組態選項、車輛屬性、效能需求 | `SWE1-FOTA-072`、`SWE1-FOTA-073`、`SWE1-FOTA-192`、`SWE1-FOTA-200`、`SWE1-FOTA-202`、`SWE1-FOTA-251`、`SWE1-FOTA-259`、`SWE1-FOTA-263`、`SWE1-FOTA-266`、`SWE1-FOTA-280`、`SWE1-FOTA-285` | 35 | 4 | 30+1 blank |
| | | *Heading 標題原文*（R-SU10(c)）：072 OTA Client Architecture；073 Operating Environment；192 Bus communications；200 OTA Client Configuration options；202 OTA Architecture Requirements；251 High Level FOTA Diagram；259 Vehicle Properties；263 OTA Architecture Requirements；266 OTA Client Configuration options；280 Interface Definitions；285 OTA Client Performance Requirements | | | | |
| 6 | `Bearer Selection` | 承載選擇：網路優先序組態與網路選擇 | `SWE1-FOTA-291` | 16 | 0 | 16 |
| | | *Heading 標題原文*（R-SU10(c)）：291 Bearer selection: | | | | |
| 7 | `ROV Installation` | ROV（Rest of Vehicle）安裝之三階段：安裝前、安裝進度、安裝後 | `SWE1-FOTA-085`、`SWE1-FOTA-086`、`SWE1-FOTA-091`、`SWE1-FOTA-096` | 20 | 16 | 4 |
| | | *Heading 標題原文*（R-SU10(c)）：085 FOTA ROV Reflash Requirements；086 Post-Installation；091 Installation Progress；096 Pre-Installation | | | | |
| 8 | `TBM Update` | TBM 相關之更新：TBM FOTA reflash 與 HU-TBM 協同 | `SWE1-FOTA-110`、`SWE1-FOTA-214` | 50 | 31 | 19 |
| | | *Heading 標題原文*（R-SU10(c)）：110 TBM FOTA Reflash；214 HU FOTA with TBM | | | | |
| 9 | `USB Update` | 本地／媒體部署路徑（USB reflash） | `SWE1-FOTA-020`、`SWE1-FOTA-074`、`SWE1-FOTA-076`、`SWE1-FOTA-078` | 5 | 0 | 5 |
| | | *Heading 標題原文*（R-SU10(c)）：020 Re-Flashing Requirements；074 Over The Air (OTA) Deployment of Software；076 Local Deployment of Software；078 Media Reflash Requirements | | | | |
| 10 | `Update HMI` | 更新之使用者體驗與 HMI 呈現 | `SWE1-FOTA-129` | 6 | 5 | 1 |
| | | *Heading 標題原文*（R-SU10(c)）：129 User Experience (UX)/HMI | | | | |
| 11 | `Configurable Parameters` | 可組態參數與 Download Descriptor 格式 | `SWE1-FOTA-125`、`SWE1-FOTA-127` | 2 | 0 | 2 |
| | | *Heading 標題原文*（R-SU10(c)）：125 Appendix B Configurable Parameters；127 Download Descriptor Format | | | | |
| 12 | `FOTA Overview` | FOTA 總覽層之需求 | `SWE1-FOTA-001` | 6 | 2 | 4 |
| | | *Heading 標題原文*（R-SU10(c)）：001 Firmware Over-the-air Updates (FOTA) | | | | |
| | **小計** | | **12 組** | **234** | **86** | **147**（+1 blank） |

**與下放包 06 草案之差異**：`291 Bearer selection:`（16 列）自
`Client Architecture` 析出自成一群（51 → 35 + 16）。
依據（下放包 15 §4.2）：`292` 之人裁正解為 `4907460`（4.7.3 configurable
network priorities）與 `4907403`（4.6.1 network selection），
與 `Client Architecture` 所轄之 4.4／4.5 架構條文分屬不同能力；
且其群列數 16 足以自立。

### PENDING —— 待下放包 16 切分（77 列）

| Heading id | 標題原文 | 列數 | HMI | Service | 狀態 |
|---|---|---:|---:|---:|---|
| `SWE1-FOTA-309` | OMA-DM Security | **70** | 0 | 70 | **PENDING — 待下放包 16 切分** |
| `SWE1-FOTA-170` | Deployment Package Security | **7** | 1 | 6 | **PENDING — 待下放包 16 切分** |
| | **小計** | **77** | **1** | **76** | |

二群皆須依**列之能力性質**重切，**不得沿用其 Heading 標題**（下放包 15 §4.3）：

- `309`：已裁之列橫跨 **至少 6 章**（`4.8.2`／`4.8.3`／`4.12`／`4.12.1`／
  `4.12.2`／`4.10.3`），其 Heading 標題 `OMA-DM Security` 只描述其前二列。
  且其 70 列**逾原則 4 之 40 列界**（全 45 群中唯一者）。
- `170`：已裁之 `176` 正解在 `4.7.3.2`（Silent Updates），
  與其 Heading 標題 `Deployment Package Security` 無關。

材料見 `docs/upstream/14_layer2_material.md` §T28a／§T28b。

### ⚠ 未歸屬之 Heading 群（1 群，0 列）

| Heading id | 標題原文 | 列數 | 狀態 |
|---|---|---:|---|
| `SWE1-FOTA-022` | Communication Security | **0** | **UNASSIGNED — 下放包 15 §4.2 未列入任何 Test Set，亦不在 PENDING 之二群** |

其所轄 in-scope 列為 **0**，故列數閉合（234 + 77 = 311）不受影響。
**執行層不自行歸屬**（Test Set 之切分屬 R-SU18(b) 之分析層裁定）；
列此以免其於「列數閉合通過」之下被靜默略過。

### 閉合檢查

| 判準 | 實測 | 應為 | |
|---|---:|---:|:--:|
| 定稿 12 組所轄列數 | 234 | — | |
| PENDING 二群列數 | 77 | — | |
| 合計 | **311** | 311（R-SU3） | ✅ |
| 45 個 Heading 群之歸屬 | 12 組轄 **42** 群 + PENDING **2** + UNASSIGNED **1** = **45** | 45 | ✅ |

**雙重閉合皆通過**：列數 234 + 77 = **311 / 311**；
群數 42 + 2 + 1 = **45 / 45**。
（\`022\` 若未列為 UNASSIGNED，群數即為 44/45 而列數仍 311/311 ——
**列數閉合不會揭出它**，此即本檔專列該群之理由。）

---

## Part III — Layer 3（規格章節分組，**不寫入工作簿**）

```
PROVISIONAL — 待下放包 16
```

依 IN §4.1.5：Layer 3 僅存本檔。其值為現階段之最佳推定，
**得於階段二逐列人裁時就地修正**（R-SU18(c)）。

本節於下放包 16 填入。現階段之已裁材料：

| 來源 | 列數 | 用途拘束 |
|---|---:|---|
| GT-A1（定向人裁） | 28 | 不得單獨用於任何比率之估計（R-SU17 v1(a)） |
| GT-A2（分層隨機，材料 30 列） | **0 已裁** | 回測之比率以本帳為準（R-SU17 v2(a)） |
| GT-C（CFTS 側反向，材料 50 物件） | **0 已裁** | 偵測路徑 A 系統性看不見之區塊（R-SU17 v2(d)） |
| GT-B（區塊導出） | 4 | 不得用於路徑 A 之回測（R-SU16 v2(h)） |

台帳見 `GROUND_TRUTH.md`。

> **R-SU17 v2(e) 之揭露**：GT-A2 與 GT-C 現無一列經裁，
> **本 feature 現無任何合法之比率估計**；GT-A1 上所得之各比率
> 一律為描述性數字，不得作為母體之估計。
