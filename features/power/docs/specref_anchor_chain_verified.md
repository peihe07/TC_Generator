# spec_reference 錨鏈查證結論（Pei 指示方法，2026-08-21）

Pei 指示：「參考 FW037 原始檔案裡面的 source ID，然後回頭去查 SYS2
文件裡面對應的是哪個」。分析層依此重建錨鏈，結論如下。

## 一、錨鏈成立

```
036 Requirement or Design ID（SWE-PM-nnn）
  → 037「SWE1 Requirements」分頁 B 欄 `Source Requirement ID`
    （值為 Sys-RA-PM-nnnn，可多個）
      → SYS2「Basic Report」B 欄 `SYS2 Sys-RA-Feature-ID`
        → E 欄 `SYS2 來源需求項目ID Source Requirement ID`（7 位 object）
           + F 欄 `SYS2 文件識別碼 Document ID`（CFTS009／CFTS010）
             → `CFTS{nnn}-{ObjectID}`
```

實測：037 有 115 條 SWE-PM；SYS2 兩本合計 410 筆 Sys-RA 對照；
**串接成功 114/115，未匹配之 Sys-RA 參照 0 筆**
（`SWE-PM-115` 之 Source Requirement ID 欄為空，屬 037 側缺漏，
登記 **A-PM12**）。

## 二、現有 spec_reference 為正確，無須改寫

逐列比對 283 列之現有 spec_ref 與錨鏈串接結果：

| 結果 | 列數 |
|---|---|
| **完全相同（含順序）** | **274** |
| 內容相同、**順序不同** | 9 |
| SWE 無對照（A-PM12） | 1 |

9 列之差異僅為排列順序（例 row 157：現況依 object id 升冪、
錨鏈依 037 之 Sys-RA 列舉順序），**集合完全相同**。

**結論：spec_reference 現況正確，M16-PM 無工可做。**

## 三、據此撤銷三項先前判斷

### 1. ~~R-12(b)：spec_ref 條數上限 4，超過須收斂~~

> **撤銷。** 上限 4 係自 SWC 分佈推得，屬以他 feature 之語料
> 反推通則。PM 之條數係「一個 SWE 對應多個 Sys-RA、一個 Sys-RA
> 對應多個 CFTS object」之多對多結構的正確結果，非未收斂。
> 條數應由錨鏈決定，**不設上限**。

### 2. ~~A-PM06 §一：spec_ref 條數 = attribution 候選數，
即候選全集代替選定~~

> **撤銷。** 兩者數字吻合係因同源（attribution 之候選亦自
> Sys-RA 集合展開），非因果。spec_ref 來自錨鏈，是結論不是候選。

### 3. ~~M16-PM：283 列 spec_reference 家族遷移~~ ／ ~~DR-PW19~~

> **撤銷。** 現況已為 `CFTS{nnn}-{ObjectID}` 家族 A 格式且內容正確。
> DR-PW19（請上游提供權威對照）無必要 —— 對照一直存在於
> 037 + SYS2，只是先前未循此路徑查詢。

**A-PM06 §二（attribution anchor 跨文件錯配）維持成立**：
`anchor_attribution_53.json` 之 anchor 確實不可用，
但正確來源不是「上游未提供」，而是 037＋SYS2 這條既有鏈。

## 四、分析層方法錯誤之檢討

先前為求收斂，採 `anchor_attribution_53.json`（本地演算法產物）
為錨點來源，並據以推論「spec_ref 是候選全集」。
**未先查 037 原始檔之 Source Requirement ID 欄** —— 該欄為
037 交付物之正式欄位，是錨定之第一來源。

此與 R-1 v1 之錯誤同型：**自演算或他處語料推導理想值，
而未先查既有正式文件之實際記載**。已納入 09 包 §五之原則，
擴充如下：

```
錨定與追溯類問題，第一來源恆為上游交付物之正式欄位
（037 Source Requirement ID → SYS2 Basic Report），
本地演算法產物（attribution／相似度計分）僅得作為輔助檢核，
不得作為錨點來源。
```

## 五、後續影響

- **軌 C 之 30 列**：其 spec_ref 亦無須改，僅改四欄內容
- 9 列順序差異：屬排序慣例，**建議依 037 Sys-RA 列舉順序統一**，
  惟屬 Tier 1 格式事項，標 `[DEFAULT]` 待 Pei 追認或推翻
- A-PM12：`SWE-PM-115` 之 037 Source Requirement ID 欄為空，
  登記待上游補；該 SWE 對應之 036 列 spec_ref 現況維持不動
