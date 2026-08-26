# 下放包 04 —— Vehicle Category：R-VC11(b) 修訂與 priority 定案

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`vehicle_category`
- 對應上繳：`features/vehicle_category/docs/upstream/04_priority.md`
- 前一包：`docs/handoff/03_rulings.md`
- 對應之上繳包：`docs/upstream/03_rulings.md` §7「待裁」四項

---

## 〇、本包之性質

裁定上繳包 03 §7 之四項。核心為**修訂 R-VC11(b)** ——
其 §6.2 之八筆抬升暴露該條之粒度錯配，**缺陷在條文，不在執行**。

新立 R-VC13、修訂 R-VC11(b)、追認 T24 之判定並定案 117 筆 priority。

---

## 一、R-VC11(b) 之缺陷 —— 分析層之設計錯誤

### 症狀

上繳包 03 §6.2：037=High 之下限把 8 筆抬進 P1，全部是彈窗回饋與返回導覽
（`VC-027`／`031`／`032`／`033-02`／`058-02`／`058-03`／`062-02`／`063-02`），
執行層指出「P1 之語意因此被稀釋」，並照裁執行未自行豁免。**處置正確。**

### 病灶

A-VC9 已證明 037 `Priority` **粒度為章**。而 R-VC11(b) 所寫之
「037 = High → 該 **leaf** 所衍生之 TC 不得低於 P1」，
是拿一個**章級**的量對 **leaf** 設下界 —— **粒度錯配**。

章 4–7、章 13 內既有主流程（PIN 驗證、Key Off 攔阻），
也有善後步驟（確認彈窗、關閉返回）。章級的 High 對章內每個 leaf 設界，
必然把善後步驟一併抬起。八筆之出現不是意外，是該規則的必然輸出。

更難看的是：R-VC11 的立論是「不採機械映射，因為粒度不匹配」，
而 (b) 自己犯了同一個粒度錯 —— 只是從「等於」放寬成「不低於」，
**錯配未解，只是變得不明顯**。

### 修法

下界之粒度必須匹配約束來源之粒度。037 Priority 既為章級，
其約束即應作用於章：**「該章之 leaf 群中至少須有達 P1 者」**，
而非「該章每個 leaf 皆不得低於 P1」。

依上繳包 03 §6.4 之本地判定驗算：

| 章 | 037 | leaf 之本地判 | 至少一筆 ≥ P1 |
|---|---|---|---|
| 4 | High | P1, P1, P1, P2 | **滿足** |
| 5 | High | P1, P1 | **滿足** |
| 6 | High | P1, P2, P3 | **滿足** |
| 7 | High | P1, P2 | **滿足** |
| 13 | High | P1×10, P2×4, P0×2 | **滿足** |
| 16 | Low | P3 | 上限，滿足 |

**五個 High 章全部滿足，八筆抬升全數撤銷。**
037=High 之資訊仍被使用 —— 它驗證了該章確實含高優先項，
這正是章級的量所能承擔的推論，不多也不少。

---

## 二、裁決條文（逐字抄入 `RULINGS.md`）

```
R-VC13（R-VC11(b) 之修訂：上游約束改為章級）

R-VC11(b) 原文「037 = High → 該 leaf 所衍生之 TC 不得低於 P1；
037 = Low → 該 leaf 所衍生之 TC 不得高於 P3」**作廢**。

作廢理由：A-VC9 已證 037 `Priority` 之粒度為**章**（十一章章內單一值，
零例外）。以章級之量對 leaf 設下界為粒度錯配，其必然輸出為
「章內善後步驟被主流程之優先級抬起」—— 上繳包 03 §6.2 之八筆
（VC-027／031／032／033-02／058-02／058-03／062-02／063-02，
全部為彈窗回饋與返回導覽）即為顯影。
R-VC11 之立論本為「不採機械映射，因粒度不匹配」，
原 (b) 自身重犯該錯，僅由「等於」放寬為「不低於」，錯配未解。

**新 (b) —— 上游約束作用於章，不作用於 leaf：**

  037 = High 之章 → 該章之 leaf 群中**至少須有一筆**定案為 P1 或 P0。
                    章內個別 leaf 不設下限。
  037 = Low  之章 → 該章之 leaf 群中**不得有**定案高於 P3 者。
  037 = Medium 之章 → 不設約束（該值含 88 筆語意跨度極大之需求，
                      不具區辨力）。

  某章不滿足其約束時，**不得逐筆抬升以求滿足** —— 應停並回報，
  該情形意味著本地判定與上游對該章之認知有系統性分歧，
  屬須裁事項而非可自動修補之偏差。

R-VC11 之 (a) 主判準與 (c) 分歧揭露**不變**，繼續適用。

依本條驗算：章 4／5／6／7／13 五個 High 章皆已滿足（各有 P1 或 P0），
章 16 之 Low 亦滿足。**八筆抬升全數撤銷，定案回歸本地判定。**
```

```
R-VC14（P0 之判準：攔阻失效與執行失效之區分）

IN §10.2 之 P0 類目含 `data-loss risk`。該款於「使用者資料之清除」
一類需求上，須區分二種失效方向 —— 二者不同級：

(a) **攔阻失效** —— TC 驗證「Cancel／否定路徑確實未變更資料」。
    其失敗意味著資料**被意外清除**。此為 data-loss，**P0**。
(b) **執行失效** —— TC 驗證「Yes／肯定路徑確實清除了資料」。
    其失敗意味著該清而未清。此**非** data-loss ——
    資料仍在，未發生遺失。**P1**。

(b) 之失效在轉售、租賃、還車等情境下構成**隱私外洩**風險，
其嚴重性不因本條而被否認；惟 §10.2 之 P0 類目
（安全／開機復原／連線／音訊輸出／eCall／車輛關鍵 CAN／資料遺失）
未列隱私，**不得以類推方式擴充 rubric 之類目**。
該風險依 R-VC11(c) 記於該 TC 之 `reasoning`。

本條之即時適用：
  SWE1-HMI-VC-036-01（選 Yes 清除個人資料並顯示確認彈窗）
    上繳包 03 §6.3 判 P0，依本條 (b) **改判 P1**。
  SWE1-HMI-VC-035-03（restore-defaults 之 Cancel）—— (a)，維持 **P0**
  SWE1-HMI-VC-036-02（clear-personal-data 之 Cancel）—— (a)，維持 **P0**

037 對此三筆皆為 Medium，依 R-VC13 之新 (b) 章級不設約束，
故 (a) 之二筆定案 P0 不受上游值影響（R-VC11(c) 之分歧揭露義務仍存）。
```

---

## 三、上繳包 03 §7 逐項裁定

### 第 1 項｜priority 草案（117 leaf）

**裁：採納，但依 R-VC13 撤銷八筆抬升、依 R-VC14 調整一筆。**

定案分布：

| | P0 | P1 | P2 | P3 | 合計 |
|---|---|---|---|---|---|
| 上繳包 03 之定案（含抬升）| 6 | 39 | 38 | 34 | 117 |
| **本包定案** | **5** | **32** | **45** | **35** | **117** |

異動共 9 筆：
- **8 筆下修**（R-VC13）：`VC-027` P1→P2、`VC-031` P1→P2、`VC-032` P1→P3、
  `VC-033-02` P1→P2、`VC-058-02` P1→P2、`VC-058-03` P1→P2、
  `VC-062-02` P1→P2、`VC-063-02` P1→P2 —— 全部回歸本地判定
- **1 筆下修**（R-VC14）：`VC-036-01` P0→P1

**定案之 5 個 P0**：

| req_id | 類 | 依據 |
|---|---|---|
| `SWE1-HMI-VC-035-03` | data-loss | restore-defaults 之 Cancel 攔阻失效 → 設定被意外清空 |
| `SWE1-HMI-VC-036-02` | data-loss | clear-personal-data 之 Cancel 攔阻失效 → 個資被意外清除 |
| `SWE1-HMI-VC-062-01` | safety | 行進中 Wi-Fi 軟體下載之攔阻（駕駛分心）|
| `SWE1-HMI-VC-063-01` | safety | FOTA 流程中車輛起步之攔阻（駕駛分心）|
| `SWE1-HMI-VC-065-01` | safety | 行進中煞車服務模式須灰化 |

分析層已讀該五筆及 `VC-036-01`、`VC-033-01`、`VC-029`、`VC-027`、`VC-032`
之 `Requirement Description` 全文（非僅 Title），判定成立。

### 第 2 項｜§6.3 之四筆 P0

**裁：三筆維持（`035-03`／`036-02`／`065-01`），一筆改判（`036-01` → P1，
依 R-VC14）。**

`VC-035-03` 與 `VC-036-02` 之 `Description` 原文僅載
「Selecting cancel will take the user back to the previous screen.」，
其「不變更設定／不清除資料」係 037 `Requirement Title` 所載
（`... without changing any settings` / `... without clearing any data`）。
**Title 為 037 之正式欄位，判定得據之**；惟此處 Title 與 Description
之資訊量有落差，一併記入 A-VC10（見 §四）。

### 第 3 項｜表 B 措辭

**裁：本輪不結**，待 DR-VC3 回覆。`data/tableB_draft.md` 維持草稿狀態。
執行層之處理（17 節、內容一律取自 SYS1 `Description`、
三節書「僅存於圖」、§8.3 依 R-VC12 二(c) 補入）**全數追認**。

### 第 4 項｜Phase 2 之 `DECISIONS.md` 簽署

**裁：可進行。** Phase 1 已於上繳包 02 之 T12（30/30）收斂，
本包之 priority 定案不觸及 recon 之任何量。
`DECISIONS.new.md` 與現行 scaffold 版 `DECISIONS.md` 之合併由執行層
逐項列出差異後**送 Pei 簽署**，執行層不自行合併（Tier 2 不變）。

---

## 四、追認與新立

### 追認 —— T24 之判定經獨立掃描未發現低估

上繳包 03 §8 自陳最大偽陽性風險為「判定依據為 `Requirement Title` 一句，
未讀 `Requirement Description` 全文，若某 leaf 之描述含標題未顯示之
安全條件，本表會低估其優先級」。

分析層以**機械掃描**獨立覆核：對本地判 P2／P3 之 72 筆，
以正則檢出 `Description` ＋ `Title` 中含
`motion|moving|speed|safety|brake|park|clear|delete|erase|reset|default|
personal data|lock|block|disab|unavailab|grey|distract|power|key.?off|ignition`
者，得 **9 筆**，逐筆檢視：

| req_id | 命中詞 | 判讀 |
|---|---|---|
| `VC-001-02` | default | 「預設頁籤為 Controls」，非 restore-defaults —— 誤命中 |
| `VC-007-02` | power | 字串 `Power Panel`（頁籤對照表）—— 誤命中 |
| `VC-025-03` | power | 字串 `Power Side Step`（按鍵對照表）—— 誤命中 |
| `VC-025-04` | lock, power | 字串 `Glove Box Lock`／`Pass Screen Power Off`（對照表列舉）—— 誤命中 |
| `VC-025-05` | clear | 字串 `On (clear roof)`（電控玻璃）—— 誤命中 |
| `VC-034-02` | grey, key-off | 呈現規則（灰化而非隱藏），非安全攔阻 —— 判 P2 正確 |
| `VC-035-02` | default, reset | 回復完成之確認彈窗，屬回饋 —— 判 P2 正確 |
| `VC-038-05` | grey | 語言更新中其餘灰化 —— 判 P3 正確 |
| `VC-055` | motion | 「行進中**仍可用**」而非「行進中禁用」；失效為功能缺失非安全風險 —— 判 P2 正確 |

**九筆全為誤命中或判定正確，無漏網。**
T24 之 117 筆判定經此獨立掃描**未發現低估**，予以追認。

> 揭露：本掃描為**關鍵詞比對**，非語意判讀。其能抓到「描述中出現安全語彙
> 而優先級偏低」之形態，**不能**抓到「安全性隱含於語意而不落於任何關鍵詞」
> 之情形。故本追認之效力為「以該詞表為準未發現低估」，
> 非「已證明無低估」。詞表列於本節，可覆核、可擴充。

### A-VC10（新立）

```
A-VC10（037 Requirement Title 之資訊量大於 Requirement Description）

037 於部分 leaf 上，`Requirement Title` 所載之條件多於
`Requirement Description`。實例：

  SWE1-HMI-VC-035-03
    Title : Selecting 'Cancel' on the restore-defaults prompt returns the
            user to the previous screen **without changing any settings**
    Desc  : Selecting cancel will take the user back to the previous screen.

  SWE1-HMI-VC-036-02
    Title : Selecting 'Cancel' on the clear-personal-data prompt returns the
            user to the previous screen **without clearing any data**
    Desc  : Selecting cancel will take the user back to the previous screen.

二例之 Title 皆含「不變更／不清除」之明文，Description 則僅述
「回上一頁」。該差額正是二筆判定 P0 之依據（R-VC14(a)）。

判讀：Description 疑為規格原文之逐字轉錄，Title 為 037 作者之
需求化改寫，改寫時補入了規格他處或圖中之條件。
**兩欄皆為 037 之正式欄位**，本 feature 之判定以二者之聯集為據，
不以任一單欄為唯一來源。

影響：TC 生成時，`test_item` 上半之 verbatim 取材須同時檢視二欄；
僅取 Description 會遺漏 Title 所載之條件，僅取 Title 則失去規格原句。

處置：不回報為缺陷（Title 補條件可能是上游之刻意作法）。
併入 DR-VC7 之同批查詢（同為 037 欄位語意之說明性問題）。

狀態：PENDING（併 DR-VC7，同批 A）。
```

---

## 五、執行層續作任務

| # | 任務 | Tier |
|---|---|---|
| T25 | 抄錄 R-VC13 / R-VC14 入 `RULINGS.md`，附 byte-level diff。**R-VC11 之 (b) 原文不刪**，依 R-TM13 加註「作廢，見 R-VC13」| 1 |
| T26 | `ANOMALIES.md` 新增 A-VC10（條文逐字）| 1 |
| T27 | `DATA_REQUESTS.md`：A-VC10 併入 DR-VC7 之同批 A；DR 未結數維持七筆 | 1 |
| T28 | 更新 `data/priority_draft.tsv` 為**定案版** `data/priority_final.tsv`：套 R-VC13 撤銷八筆抬升、套 R-VC14 調整 `VC-036-01`。逐筆回報異動前後值，並重出 §6.1 之分布表 | 1 |
| T29 | `docs/REVISIONS.md` 新增 REV-09（R-VC11(b) 作廢，粒度錯配）與 REV-10（上繳包 03 §6.2 八筆抬升撤銷、§6.3 一筆改判）| 1 |
| T30 | 依 §三第 4 項，逐項列出 `DECISIONS.new.md` 與現行 `DECISIONS.md` 之差異，**送 Pei 簽署**。不自行合併 | 1 |

**不在本輪範圍**：`framework.md`（Phase 3）、profile、任何 TC、任何寫回、
任何 git 操作、`DECISIONS.md` 之實際合併。

> priority 定案後，Phase 4／6 之 priority 欄前置條件已解除
> （R-VC6(a) 之凍結由 R-VC11 解除，R-VC13／R-VC14 完成其校準）。
> 但 Phase 3（framework）尚未開始 —— 下一個里程碑為 Layer 2 之切分，
> 屬 Tier 2，待 Pei 指示。

---

## 六、上繳包要求

`features/vehicle_category/docs/upstream/04_priority.md` 須含：

1. T25–T30 逐項結果，附實際指令與原始輸出
2. R-VC13 / R-VC14 之 byte-level diff 核對
3. **T28 之 117 筆定案全表**，含 9 筆異動之前後對照
4. R-VC13 之章級約束驗算（六章逐章）
5. T30 之 `DECISIONS` 差異逐項表
6. 更新後之未結 DR（七筆）與 A（六筆）清單
7. 量測條件揭露（R-G8）：T28 之異動套用方法與其可重現性
