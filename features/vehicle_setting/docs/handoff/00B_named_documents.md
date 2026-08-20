# 00B 下放包補篇 — 具名文件查證（**修正 00A 之 DR-4，收斂 DR-5**）

分析層寫入，2026-08-20。同一往返（NN = 00）。
本篇因 Pei 之查問「文件內有沒有提到明確的文件名稱」而作，
**結論改變了 00A 的第 4 項與第 5 項**。

---

## 0. 本篇撤回之陳述（**自我更正，canon §5a 第 15／16 條**）

00A §2 第 4 項寫：

> `$HSW_StatFailSts$` 在 CFTS044 全文命中 **0** → 需要外部 CAN 字典，Urgency **High**

**該陳述為誤。** 成因：抽取式只掃 `$var$` 形態，而規格對同一訊號另以
**訊號路徑記法**書寫（`STATUS_CSWM.HSW_StatFailSts`），`$` 包夾之形態
在規格內本就不出現。**抽取式少抽不會報錯**（canon §5a 第 12 條），
本例即該條之標準形態。

更正後之實測：

| token | 037 引用 | 規格內之記法 | 值域 |
|---|---|---|---|
| `$HSW_StatFailSts$` | 16 | `STATUS_CSWM.HSW_StatFailSts == "…"` | `Fail_Not_Present`／`Fail_Present`（同族 `*_STATFailSts` 共 86 處，兩值） |
| `$Heated_Steats_Levels$` | 6 | `$Heated_Steats_Levels$ == "…"` | `Two Levels`／`Three Levels` |

**故 30 個 token 中有 29 個之值域可自 CFTS044 取得**（00A 誤指之
`$HSW_StatFailSts$` 亦在其中），**唯一仍無值域者為 `$TGW_DISP_STAT$`**
（8 處命中，條文形態皆為「shall not alter」，本就不需值域，需要的是
訊號讀取途徑）。

**DR-4 除名，改列 DR-4b 一項。**

---

## 1. 查問之直接回答：**沒有任何一處給出明確檔名**

掃描條件：CFTS044 轉檔全文（805,517 字元）、SYS3 SYSAD 全文
（69,583 字元）、四份 037 之 `封面`／`ChangeHistory`／`Product Document`
三張表；正則 `[A-Za-z0-9_\-\.\(\) ]{3,80}\.(docx?|xlsx?|xls|pdf|dbc|pptx?)`，
另以字面掃 `Refer to`、`Document`、`參考`。

| 來源 | 具名檔名 | 結果 |
|---|---|---|
| CFTS044 | 全文僅 **1 個**：`RAR_LTM-R1L_SR21_1A_r8.xlsx`（出現 6 次） | **全數位於 Revision Notes 之歷史修訂敘述內**（2018 年 CR），非需求條文之引用，**與本 feature 之 leaf 無關** |
| CFTS044 之外部引用 | `TLM HMI Document`（24 處）、`PDO graphics`（2 處）、`the DBC file`（3 處） | **皆為類別名，無檔名、無版本、無日期** |
| SYS3 SYSAD §6 參考文檔 | 三條，全為類別敘述：「corresponding SYS2/feature requirement/interface documents」「Corresponding HMI Implementation Document」「corresponding SYS2 Documents」 | **無任何具名檔案**；`PDO` 命中 0、`TLM` 命中 4（皆為模組名非文件名） |
| 037 ×4 封面 | `文件名 Document name: STLA 報告_SWRA STLA Report_SWRA` | 只有自身文件名；四份**封面完全相同**（版本 C、核准 劉安哲、審查 吳冠麒、2026-02-05／02-09），**四份在封面上無法彼此區分** → A-VS03 |

### 1.1 但規格內有另一種具名體系

CFTS044 以**大括號**攜帶跨文件與跨條款引用，共 **313 種**：

| 形態 | 例 | 次數 |
|---|---|---|
| VF 系文件 | `{VF664}` 80、`{VF728}` 7、`{VF651}` 6、`{VF451}` 6 | 最大宗 |
| CFTS 系文件 | `{CFTS020}` 19、`{CFTS048}` 5、`{CFTS022}` 4、`{CFTS081}` 3、`{CFTS009}` 3、`{CFTS043}` 3、`{CFTS088}` 2、`{CFTS026}` … | —— |
| 同／他文件之條款 | `{CFTS044-443}` 5、`{CFTS044-2165}` 5、`{CFTS025-4863}` 2 … | —— |
| 章節錨點 | `{4859374}` 等 7 位數 | 見 §2 |

`{CFTS043}` 出現 3 次——**即 Comfort 之來源規格**，為 R-VS7 之委派界線
提供文件層之佐證，執行層應於 W-9 逐處取其上下文。

`{CFTS044-xxxx}` 出現 1 次（字面 `xxxx`），為上游未填之佔位 → A-VS04。

---

## 2. 意外收穫：`specification_reference` 之章節號可解析

規格內文帶有 **章節號 + 標題 + `{7位數}`** 之錨點：

```
1.3.3.3.2 Two Stages Heated Seats Management {4859374}
1.3.1.1.1 Hazard Switch Button {4857917}
```

實測：此形態 **435 處，涵蓋 254 個相異 7 位數 ID**。

以位置法（每個 `**7位數:` 需求區塊歸屬於其前方最近之章節錨點）回推 leaf：

| 結果 | leaf 數 |
|---|---|
| **解析到 CFTS044 章節號** | **245** |
| 取得 7 位數 ID 但落不進任何章節 | 25 |
| 無 7 位數 ID（SYS2 該列 `Source Requirement items` 為空） | 1 |

例：`SWE1-VC-Stop-StartSystem-002` → `4858549` → `1.3.2.1.3.12.1`；
`SWE1-VC-SwitchLHD/RHDConfiguration-009` → `4858560` → `1.3.2.1.3.13`。

**這使 R-VS2(c) 之 PENDING 有解**：`specification_reference` 之末段
不必等外部對照表，章節號在規格自身內。但**位置法是代理判準**
（canon §5a 第 13 條）：它假設「需求區塊必屬其前方最近之章節」，
該假設在轉檔文字上未經獨立驗證，**須待 DR-1 之原始 docx 以樣式階層
（Heading 1–7）重建 outline map 後複驗**，兩者不一致者逐條追因。

---

## 3. 收斂後之 DATA_REQUESTS（**取代 00A §2**）

| # | 項目 | 為何需要 | 阻塞 | Urgency |
|---|---|---|---|---|
| 1 | **CFTS044 原始 `.docx` 二進位** | ①以樣式階層重建 outline map，複驗 §2 之位置法；②複驗本篇全部數字 | `specification_reference` 全欄之最終形式 | **High** |
| 2 | SYS3 SYSAD 原始二進位 | 範圍界定佐證 | —— | Medium |
| 3 | 六份素材入 `inputs/` 並取 SHA | G-L | 全部 | **High** |
| ~~4~~ | ~~`$HSW_StatFailSts$` 值域~~ | **除名**（§0：規格以訊號路徑記法給出） | —— | —— |
| **4b** | `$TGW_DISP_STAT$` 之**訊號讀取途徑**（CAN 工具／診斷手段），非值域 | 4 個引用之 ER 需可觀察；條文形態為「shall not alter」 | 4 個引用之可執行性 | Medium |
| **5** | **`TLM HMI Document`** —— **無檔名，須先向上游問「這是哪一份」** | CFTS044 內文 24 處點名（其中 `Refer to TLM HMI Document` 9 處）；經 leaf 回溯得 **16 leaf**（HeatedSeat 8／VentedSeat 6／HSW 2），其畫面行為與失效彈窗全押在此文件 | 該 16 leaf 之畫面文字與版面斷言 | **High（RD-1 提問，非索檔）** |
| **5b** | **`PDO graphics`** —— 同上，無檔名 | 內文 2 處；回溯得 **1 leaf**（HSW 圖示左右鏡像置放） | 1 leaf 之圖示位置斷言 | Medium（併入同一則 RD-1 提問） |
| ~~5c~~ | ~~Pop Up List／HMI Settings List／Market Configuration~~ | 撤回（CFTS044 對 `Pop Up`／`Settings List` 命中 0） | —— | **不請求** |
| **6** | Comfort 43 個重疊 leaf 之委派界線 | 見 00A §3；本篇新增佐證：CFTS044 內文以 `{CFTS043}` 顯式引用 Comfort 規格 3 處 | §8.2.1 委派句、leaf 範圍 | **High（裁決）** |

**第 5／5b 之性質已改變**：原以為是「repo 裡沒有、去要一份」，
實測後是「**上游從未具名，連要什麼都問不出來**」。故其正確形式為
**RD-1 提問**（Tier 3，Pei 送出），問法應為：

> CFTS044 於 24 處引用 `TLM HMI Document`、2 處引用 `PDO graphics`，
> 兩者於 CFTS044 與 SYS3 SYSAD 內皆無檔名、版本或日期。
> 請指明其確切文件（檔名 + 版本 + 發行日）。
> 影響範圍：16 個 SWE leaf 之畫面行為與失效彈窗斷言、1 個 leaf 之圖示位置。
> 若無此文件，該 17 leaf 之 ER 只能寫到訊號層，畫面層須標 BLOCKED。

---

## 4. 本篇新開之 anomaly（登記，未裁定）

| id | 內容 | 證據 |
|---|---|---|
| **A-VS03** | 四份 037 之 `封面` 內容完全相同（同文件名、同版本 C、同核准／審查者與日期），**封面無法區分四份** | 逐格比對四份 `封面` 表 |
| **A-VS04** | CFTS044 內存在未填之引用佔位 `{CFTS044-xxxx}`（1 處） | 大括號抽取 |
| **A-VS05** | `$Heated_Seat_Levels$`／`$Heated_Seats_Levels$`／`$Heated_Steats_Levels$` 三種拼寫並存（`Steats` 疑為 typo），其值域亦不一致（`1/2/3` vs `Two Levels/Three Levels`） | token 抽取 + 值域抽取 |

A-VS05 併入 RD-1；A-VS03／A-VS04 為 FYI 類。

---

## 5. 本篇之盲區（R-G11）

1. 仍全跑在**轉檔文字**上。`.docx` 之欄位、頁首頁尾、文字方塊、內嵌圖說
   在轉檔時可能整段消失——**若 TLM HMI Document 之檔名寫在圖說或表格內，
   本篇會報「沒有」而其實有**。此為本篇結論最脆弱之處，DR-1 到位後必須
   以原始 docx 重跑同一組正則
2. 章節號位置法為代理判準（§2 末段），未經樣式階層驗證
3. 大括號抽取式以 `\{([A-Za-z0-9_\-\. ]{2,40})\}` 為準，**含非 ASCII 或
   換行之引用會漏抽**（canon §5a 第 12 條之同一形態，本篇已因此錯過一次）
4. 值域抽取現用兩式（`$var$ = [值]`、`路徑.名稱 == "值"`）。
   **兩式皆不命中不等於規格未定義**——第三種記法若存在，本篇同樣看不見
