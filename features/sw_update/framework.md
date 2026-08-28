# framework.md — SW Update

狀態：**分層效力（R-SU18，Pei 2026-08-28 裁丙）** ——
**Layer 1 定稿**／**Layer 2 全定稿（21 組，311 列，三重閉合全過）**／
**Layer 3 PROVISIONAL**。
Feature slug：`sw_update`
規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、
FO §0（Tier 2：framework Test Set derivation 屬 Pei 簽核）、
R-SU1／**R-SU10 v2**／R-SU18／**R-SU19**

---

## 效力分級（R-SU18(d) 之揭露義務）

| 層 | 效力 | 進工作簿 | 變更成本 |
|---|---|:--:|---|
| **Layer 1**（Test Group） | **定稿** | ✅ | 須 Pei 裁 |
| **Layer 2**（Test Set） | **全定稿**（21 組，無 PENDING） | ✅ | 須分析層裁並記依據；已寫回者視同修訂 |
| **Layer 3**（spec 章節分群） | **PROVISIONAL** | ❌（IN §4.1.5） | 階段二逐列人裁時就地修正，不須另發裁決；須記於該列 `reasoning` 並回寫本檔 |

> ⚠ **R-SU18(c) 之拘束**：Layer 3 之 provisional 狀態**不得外溢至
> `specification_reference`**。後者一律走階段二之逐列裁定（R-SU14 v5），
> **不得以 Layer 3 之章推定其錨**。
> 二者為導航與交付面之別 —— Layer 3 錯了只是導航繞路，
> `specification_reference` 錯了是交付缺陷。

**Layer 3 於 2026-08-28 之覆蓋狀態**：

| | 值 |
|---|---:|
| 21 組中有 **GT** 支持者 | **8 組 / 21** |
| 21 組中有值但非 GT（推定／標題重疊） | 2 組 / 21 |
| 21 組中 TBD 者 | 11 組 / 21 |
| 逐列已裁者（GT-A1 28 + GT-B 4） | **32 / 311（10.3%）** |
| PROVISIONAL（未裁之列） | 279 / 311 |

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

## Part II — Layer 2（Test Set，寫入工作簿）—— 全定稿

分群鍵為 **Heading id**；**跨章之 Heading 群，其鍵細化為
(Heading id, 037 列區間)**（**R-SU10 v2(a)**）。
本表逐組列出其所轄之 (Heading id, 列區間) 與該 Heading 之標題原文
（R-SU10 v2(c)），俾碰撞與跨章皆可見。
依 IN §4.2：英文名詞片語、不重複 Test Group 前綴、
**不設 `Misc`／`General`／`Unclassified`**（IN §4.1.3）。

### 切分原則

1. 分群鍵為 Heading id；跨章群細化為 (Heading id, 列區間)（R-SU10 v2(a)）
2. **跨章之 Heading 群必拆** —— 已實證者 `309`（7 組）、`170`（2 組）
3. 純 Service 群之健康判準為「共同觸發面與共同觀察面」
   （下放包 06 §3.3；IN §4.1.3 之 UI 入口路徑只在 17 個含 HMI 列之群成立）
4. **逾 40 列者須檢視其是否實為多能力，射程及於 Test Set**（**R-SU19**）
   —— 40 為檢視之觸發值，非上限
5. 不設 `Misc`／`General`／`Unclassified`（IN §4.1.3）

### 定稿之 21 組（311 列，45 群）

| # | Test Set | 能力叢集 | 所轄 (Heading id, 列區間) | 列數 | HMI | Service |
|---:|---|---|---|---:|---:|---:|
| 1 | `Wi-Fi Download` | Wi-Fi 下載路徑：連線建立、經 Wi-Fi 之軟體下載、非關鍵更新 | (`SWE1-FOTA-038`, 全群)、(`SWE1-FOTA-055`, 全群)、(`SWE1-FOTA-058`, 全群) | 29 | 12 | 17 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：038 OTA download via Wi-Fi；055 Non-Critical Updates；058 Connection to Wi-Fi network | | | | |
| 2 | `Update Policy` | 更新之關鍵性政策：Critical／Regular／Silent 之分級與其套用 | (`SWE1-FOTA-009`, 全群)、(`SWE1-FOTA-024`, 全群) | 17 | 4 | 13 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：009 Critical Updates；024 Critical Updates | | | | |
| 3 | `Silent Update` | 靜默更新之執行與其通知限制 | (`SWE1-FOTA-170`, 175–177)、(`SWE1-FOTA-178`, 全群) | 9 | 2 | 7 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：170 Deployment Package Security；178 For a silent update, the OTA client follows these steps for the download | | | | |
| 4 | `Deployment Flow` | 部署流程本體（037 `137` 群） | (`SWE1-FOTA-137`, 全群) | 26 | 9 | 17 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：137 Deployment flow | | | | |
| 5 | `Session Flows` | 各類 session 之總覽與流程骨架 | (`SWE1-FOTA-018`, 全群)、(`SWE1-FOTA-168`, 全群)、(`SWE1-FOTA-185`, 全群)、(`SWE1-FOTA-188`, 全群)、(`SWE1-FOTA-271`, 全群)、(`SWE1-FOTA-278`, 全群)、(`SWE1-FOTA-287`, 全群)、(`SWE1-FOTA-016`, 0 列)、(`SWE1-FOTA-017`, 0 列) | 16 | 2 | 14 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：016 Session Flows；017 Deployment Flow；018 Installation and Download Conditions；168 Vehicle-Initiated Session Flow；185 OTA client sessions；188 User initiated sessions；271 OTA server initiated sessions；278 User initiated sessions；287 OTA client Flows | | | | |
| 6 | `Client Architecture` | OTA client 架構面：介面定義、匯流排、組態選項、車輛屬性、效能 | (`SWE1-FOTA-192`, 全群)、(`SWE1-FOTA-200`, 全群)、(`SWE1-FOTA-202`, 全群)、(`SWE1-FOTA-251`, 全群)、(`SWE1-FOTA-259`, 全群)、(`SWE1-FOTA-263`, 全群)、(`SWE1-FOTA-266`, 全群)、(`SWE1-FOTA-280`, 全群)、(`SWE1-FOTA-285`, 全群)、(`SWE1-FOTA-072`, 0 列)、(`SWE1-FOTA-073`, 0 列) | 35 | 4 | 30+1 blank |
| | | *Heading 標題原文*（R-SU10 v2(c)）：072 OTA Client Architecture；073 Operating Environment；192 Bus communications；200 OTA Client Configuration options；202 OTA Architecture Requirements；251 High Level FOTA Diagram；259 Vehicle Properties；263 OTA Architecture Requirements；266 OTA Client Configuration options；280 Interface Definitions；285 OTA Client Performance Requirements | | | | |
| 7 | `Bearer Selection` | 承載選擇：網路優先序組態與網路選擇 | (`SWE1-FOTA-291`, 全群) | 16 | 0 | 16 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：291 Bearer selection: | | | | |
| 8 | `ROV Installation` | ROV 安裝三階段：安裝前、安裝進度、安裝後 | (`SWE1-FOTA-086`, 全群)、(`SWE1-FOTA-091`, 全群)、(`SWE1-FOTA-096`, 全群)、(`SWE1-FOTA-085`, 0 列) | 20 | 16 | 4 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：085 FOTA ROV Reflash Requirements；086 Post-Installation；091 Installation Progress；096 Pre-Installation | | | | |
| 9 | `TBM Reflash` | TBM 自身之 FOTA reflash | (`SWE1-FOTA-110`, 全群) | 14 | 11 | 3 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：110 TBM FOTA Reflash | | | | |
| 10 | `HU FOTA via TBM` | HU 經 TBM 路徑之 FOTA | (`SWE1-FOTA-214`, 全群) | 36 | 20 | 16 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：214 HU FOTA with TBM | | | | |
| 11 | `USB Update` | 本地／媒體部署路徑（USB reflash） | (`SWE1-FOTA-078`, 全群)、(`SWE1-FOTA-020`, 0 列)、(`SWE1-FOTA-074`, 0 列)、(`SWE1-FOTA-076`, 0 列) | 5 | 0 | 5 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：020 Re-Flashing Requirements；074 Over The Air (OTA) Deployment of Software；076 Local Deployment of Software；078 Media Reflash Requirements | | | | |
| 12 | `Update HMI` | 更新之使用者體驗與 HMI 呈現 | (`SWE1-FOTA-129`, 全群) | 6 | 5 | 1 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：129 User Experience (UX)/HMI | | | | |
| 13 | `Configurable Parameters` | 可組態參數與 Download Descriptor 格式 | (`SWE1-FOTA-125`, 全群)、(`SWE1-FOTA-127`, 全群) | 2 | 0 | 2 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：125 Appendix B Configurable Parameters；127 Download Descriptor Format | | | | |
| 14 | `FOTA Overview` | FOTA 總覽層之需求 | (`SWE1-FOTA-001`, 全群) | 6 | 2 | 4 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：001 Firmware Over-the-air Updates (FOTA) | | | | |
| 15 | `Integrity Verification` | 驗證與加密：OMA-DM 訊息完整性、DM Tree 加密、部署包完整性與簽章 | (`SWE1-FOTA-170`, 171–174)、(`SWE1-FOTA-309`, 310–312/338)、(`SWE1-FOTA-022`, 0 列) | 8 | 0 | 8 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：022 Communication Security；170 Deployment Package Security；309 OMA-DM Security | | | | |
| 16 | `Interruption Handling` | 中斷處理與續傳：六種中斷、復原、儲存、併發 | (`SWE1-FOTA-309`, 313/315–329/357/360) | 18 | 0 | 18 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 17 | `Status Reporting` | 回報：session 完成／重試／重送、backchannel 狀態 | (`SWE1-FOTA-309`, 330–334/339/358) | 7 | 0 | 7 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 18 | `Deployment Conditions` | 部署前條件：可組態安裝條件、評估、車輛條件提供 | (`SWE1-FOTA-309`, 336–337/340–341/343–346) | 8 | 0 | 8 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 19 | `Session Management` | 輪詢與 session 管理：間隔、前提、伺服器發起流程、佇列 | (`SWE1-FOTA-309`, 347–356/359/361/368–369) | 14 | 0 | 14 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 20 | `Telematics Client` | TC 介接：通訊建立、訂閱、session 接收與轉送 | (`SWE1-FOTA-309`, 363–367) | 5 | 0 | 5 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| 21 | `Update Agent` | Update Agent：目標選擇、相依序、API、A/B、failsafe、差分 | (`SWE1-FOTA-309`, 370–383) | 14 | 0 | 14 |
| | | *Heading 標題原文*（R-SU10 v2(c)）：309 OMA-DM Security | | | | |
| | **小計** | | **21 組／45 群** | **311** | **87** | **223**（+1 blank） |

### R-SU19 之套用記錄（本輪拆分）

| 原組 | 列數 | 拆為 | 拆後列數 |
|---|---:|---|---|
| `TBM Update` | 50 | `TBM Reflash` + `HU FOTA via TBM` | 14 + 36 |
| `Session Flows` | 42 | `Deployment Flow` + `Session Flows` | 26 + 16 |

拆後之最大組為 `HU FOTA via TBM`（36 列）與 `Client Architecture`（35 列），
**皆未逾 40**。

### 命名之偏離記錄

`HU FOTA via TBM` 為 4 token，逾 IN §4.2 之「典型 1–3 字」。
依據（下放包 16 §4.2）：`110`（TBM 自身之 reflash）與 `214`
（HU 經 TBM 路徑之 FOTA）之區別即在 `via TBM`，縮短會使二組不可分。
IN §4.2 之「典型」為傾向非硬限，本例記其依據後採用。

### 三重閉合（R-SU10 v2）—— 全過

實測 2026-08-28，`python3 scripts/layer2_close.py`（不符即非零碼退出）：

| 判準 | 實測 | 應為 | |
|---|---:|---:|:--:|
| **(i) 列數**：21 組列數和 | **311** | 311（R-SU3） | ✅ |
| **(ii) 群數**：所涵蓋 Heading id 之聯集 | **45** | 45 | ✅ |
| ＿未被任何組涵蓋之群 | 0 | 0 | ✅ |
| ＿組中出現而不存在之群 | 0 | 0 | ✅ |
| **(iii) 列 id 集合**：聯集大小 | **311** | 311 | ✅ |
| ＿母體有而 Layer 2 無（漏） | 0 | 0 | ✅ |
| ＿Layer 2 有而母體無（溢） | 0 | 0 | ✅ |
| ＿**相交之組對** | **0** | 0 | ✅ |

跨章群之內部分割：

| Heading 群 | 列數 | 分屬之 Test Set | 各組列數和 |
|---|---:|---|---:|
| `SWE1-FOTA-309` | 70 | `Integrity Verification`(4)、`Interruption Handling`(18)、`Status Reporting`(7)、`Deployment Conditions`(8)、`Session Management`(14)、`Telematics Client`(5)、`Update Agent`(14) | **70** ✅ |
| `SWE1-FOTA-170` | 7 | `Silent Update`(3)、`Integrity Verification`(4) | **7** ✅ |

> (i) 對 0 列群無感、(ii) 對跨章群之內部錯分無感 —— **三者缺一不可**
> （R-SU10 v2）。`SWE1-FOTA-022`（0 列）已納入 `Integrity Verification`
> （下放包 16 §二 #1），`UNASSIGNED` 標記解除。

---

## Part III — Layer 3（規格章節分組，**不寫入工作簿**）

```
PROVISIONAL — 得於階段二逐列人裁時就地修正（R-SU18(c)）
```

依 IN §4.1.5：Layer 3 僅存本檔。其值為現階段之最佳推定。
**不得用以推定任何 `specification_reference`**（R-SU18(c)）。

| Test Set | Layer 3 provisional（CFTS 章） | 依據強度 |
|---|---|---|
| `Silent Update` | `4.7.3.2` | **GT**（`176`,`179`,`180`） |
| `Interruption Handling` | `4.12`, `4.12.1`, `4.12.2` | **GT**（`313`,`315`–`324`,`328`,`329`,`332`） |
| `Integrity Verification` | `4.8.2`, `4.8.3` | **GT**（`310`,`311`,`312`） |
| `Client Architecture` | `4.4`, `4.4.1`, `4.5` | **GT**（`257`,`260`,`261`,`262`） |
| `Bearer Selection` | `4.6`, `4.6.1`, `4.7.3` | **GT**（`292`，信度 M） |
| `Update Policy` | `4.7.3`, `4.7.3.1` | **GT**（`034`；GT-B `030`,`031`） |
| `Session Management` | `4.10.2`, `4.10.3` | **GT**（`347`）+ 推定 |
| `TBM Reflash` | `5`（TBM FOTA Reflash Requirements） | 標題全詞重疊（下放包 07 §1.4） |
| `HU FOTA via TBM` | `4.2.3` + `5` | **GT**（`215`,`216`） |
| `USB Update` | `3`（Media Reflash Requirements） | 推定 |
| 其餘 11 組 | **TBD** | 待階段二 |

**覆蓋狀態（2026-08-28）**：本表 10 組有值，其中**標為 GT 者 8 組**
（`TBM Reflash` 為標題全詞重疊、`USB Update` 為推定，二者非 GT）；
**TBD 11 組**。10 + 11 = 21 ✅。
逐列已裁者 GT-A1 28 列 + GT-B 4 列 = **32／311（10.3%）**。

> ⚠ 下放包 16 §五 之結語稱「有 GT 支持者 **9** 組／21；TBD **11** 組」——
> 逐列數其表中標 **GT** 者為 **8** 組（上繳包 15 §3.1）。本檔採 **8**。

### GT 材料之現況

| 來源 | 已裁 | 用途拘束 |
|---|---:|---|
| GT-A1（定向人裁） | 28 列 | 不得單獨用於任何比率之估計（R-SU17 v1(a)） |
| GT-A2（分層隨機，材料 30 列） | **0** | 回測之比率以本帳為準（R-SU17 v2(a)） |
| GT-C（CFTS 側反向，材料 50 物件） | **0** | 偵測路徑 A 系統性看不見之區塊（R-SU17 v2(d)） |
| GT-B（區塊導出） | 4 列 | 不得用於路徑 A 之回測（R-SU16 v2(h)） |

台帳見 `GROUND_TRUTH.md`。

> **R-SU17 v2(e) 之揭露**：GT-A2 與 GT-C 現無一列經裁，
> **本 feature 現無任何合法之比率估計**；GT-A1 上所得之各比率
> 一律為描述性數字，不得作為母體之估計。
