# 01 下放包 — 00 輪覆核與裁決備妥

分析層寫入，2026-08-20。覆核對象：`docs/upstream/00_intake_and_rulings.md`。

**覆核結論：接受。** 上繳品質高於前例：七項不符逐項回報且未調和，
獨立判斷具名八項未驗者，並以三個獨立向（W-5 對照向、docx 樣式階層、
LID 表列 2 欄組標題）推翻分析層三處陳述。

---

## 1. 分析層之三處錯誤 —— 逐項認錯並記明成因

**依 canon §5a 第 16 條，本節之更正經獨立查證，非照單接受。**

### 1.1 `SWE1-VC-HeatedSteeringWheel-009` 之成因記載錯誤（A-VS12）

分析層於 00C §1、00E、00I 之預期數字表三處寫「SYS2 該列
`Source Requirement items` 為空」。**該敘述為誤，且成因是分析層自身的
抽取式。**

分析層獨立複驗（`inputs/` 實體檔，`Heated_Steering_Wheel.xlsx`
`Analysis Report` 列 16）：

```
swe_id : SWE1-VC-HeatedSteeringWheel-009
src    : SYS-RA-CFTS100          ← 逐字，指向 CFTS100，且無 -N 序號
title  : Heated Steering Wheel
```

**成因**：分析層之正則為 `SYS-RA-CFTS\d+-(\d+)`，`SYS-RA-CFTS100` 無
`-N` 段，故抽取結果為空集合；分析層將「抽不到」寫成「SYS2 那列為空」
—— **把自己工具的沉默，記成了資料的性質**。canon §5a 第 12 條之標準
形態，執行層以寬鬆式 `SYS-RA-CFTS\d+(?:-\d+)?` 抓出 274 vs 273 而發現。

**推論（重於該筆本身）**：本 feature 「上游規格為 CFTS044」此一前提，
**在 1 / 271 上不成立**。CFTS100 未在任何素材清單中，亦未曾被要求。
→ **DR-11（新，見 §4）**。

### 1.2 `Proxi & Configuration` 之欄組結構讀錯（A-VS15）—— **R-VS11 因此撤回**

00G §4 稱「兩種讀法在本表上長得一模一樣」。**該陳述為誤。**

該分頁**列 2** 之欄組標題逐字為 `Atlantis & Atlantis High`
（`CAN Mapping` 分頁則為 `Atlantis` 與 `Atlantis High` 兩個獨立欄組）。
分析層只讀了列 3 之逐欄表頭，未讀列 2 之欄組標題，於是把
**「該分頁沒有這個欄組」誤讀為「這個欄組是空的」**。

**該表自己寫明了答案，而分析層據此開了一條不存在的裁決題。**

```
R-VS11 —— 撤回（withdrawn，非裁定）
「LID 表之 Atlantis 欄能否代 Atlantis High」不是待裁事項。
`Proxi & Configuration` 分頁之列 2 欄組標題逐字為 `Atlantis & Atlantis High`，
即該欄組同時涵蓋兩種架構；`CAN Mapping` 分頁則二者分列。
故該 10 個 PROXI 類參數之 Atlantis 欄值，對 Atlantis High 直接適用，
不需假設、不需 RD-1、不需於 profile 標註為假設。

撤回理由記於此，不以「已裁定」形式記載 —— 它從來不是一個判斷問題，
是一次讀漏。
```

### 1.3 A-VS06 之差額 16 為轉檔產物（A-VS06′）

原始 docx 上 body heading 270、相異 `{7位數}` 270、**差額 0**。
分析層之 254 量自轉檔文字之較寬形態。**A-VS06 除役**，不列入 RD-1。

---

## 2. 兩項「待裁」以既有政策消解 —— **立新規則前先查既有政策**（canon §5a 第 17 條）

### 2.1 DR-10（5 leaf 落多章節）→ **不需裁決**

`ASPICE_SWE6_AI_Instruction.md` §10.7 已明文：

> `specification_reference`：**String list**；
> **List every spec section the TC directly verifies or relies on as setup**；
> Order from most-specific to general；**Multiple specs allowed**。

**單值形式從來不是政策，是分析層在 00E 敘述時的簡化。**
五個 leaf 各列其全部章節即可，順序依 §10.7 由最具體至一般。

```
R-VS14（記載，非新規）
specification_reference 為字串清單，非單值。leaf 對映到多個 CFTS044
章節者（實測 5 個：LeftFrontHeatedSeat-004 / -011、
HeatedSteeringWheelManagement-025 / -026 / -027），逐一列出全部章節，
依 §10.7 由最具體排至一般。DR-10 撤銷。
```

### 2.2 R-VS2(c)「已解除」為過早 —— 分階段記載

執行層之數字：245 解析／25 有 id 無章節／1 無 id；其中 5 個落多章節。

| 群 | leaf 數 | N 欄形式 |
|---|---|---|
| 單一章節 | **240** | 已定：`{spec_filename}_{section}` |
| 多章節 | **5** | 已定：同上，多值（R-VS14） |
| 有 7 位數 ID 但無章節 | **25** | **未定** —— 其 SYS-RA 指向 SYS2 之 Heading／Information 列（A-VS01） |
| 無錨鏈 | **1** | **未定** —— CFTS100（A-VS12／DR-11） |

**245 / 271 已定，26 / 271 未定。** 00E §3 之「解除」改記為
「**主群已定，26 個 leaf 待處置**」。

---

## 3. 一條裁決須加嚴 —— A-VS17 使 R-VS9 草案不足

執行層實測：兩份 DBC 之 **141 個共有 signal 中 128 個起始位元不同（91%）**。

00H §5-3 曾自陳「同名不同定義本篇看不到」，**實測顯示那是常態不是例外**。
意涵：同一個 signal 名在兩條匯流排上是**兩個不同的量測點**；TC 只寫
signal 名，測試者無法確定要在哪裡量、量哪幾個位元。

```
R-VS9（v2，取代 00H §3 之草案 —— 待 Pei 裁）
TC 中書寫 CAN 訊號時：

(1) 訊號逐字名與所屬 message 以 Logical Identifiers and CAN Mapping
    之對應欄組為第一權威：
      - `CAN Mapping` 分頁 → 取 `Atlantis High` 欄組
      - `Proxi & Configuration` 分頁 → 取 `Atlantis & Atlantis High` 欄組
        （該欄組同時涵蓋兩種架構，見 R-VS11 撤回說明）
(2) 值域以同表 Format 欄為準，並與對應 DBC 之 VAL_ 表交叉核對；
    兩者不一致時停下回報，不自行調和
(3) **訊號斷言須同時指明 message 與網段**，三者成組出現，缺一不可：
        <signal 名> in <message 名> on <網段>
    例：`STATUS_CSWM.HSW_StatFailSts in STATUS_CSWM (0x491) on CAN-B`
    理由：兩份 DBC 之 141 個共有 signal 中 128 個起始位元不同（91%），
    只寫 signal 名不足以定位量測點
(4) 網段對應：CAN-B／BH-CAN → PDT27_E2A_R4_BHCAN.dbc；
    CAN-FD → PDT27_E2A_R5_FDCAN8.dbc
(5) `$var$` 形態僅出現於 test_item 上半段之來源逐字內，
    不出現於 procedure／expected_result 之作者自撰文字
    理由：`$PowerMode$` 之匯流排名為 `CmdIgnSts`，DBC 內另有一支
    `PowerModeSts`；以 `$var$` 檢索會抓到錯的訊號
```

lint 對 (3) 之判準：procedure／expected_result 內出現 DBC signal 名而
同句無 message 名者 FAIL。**該規則須附範圍向**（R-G9）：對
`test_item` 上半段之來源逐字不得轉紅。

---

## 4. DATA_REQUESTS 淨變動

| # | 項目 | 狀態 |
|---|---|---|
| DR-9 | `SWE1-VC-HeatedSteeringWheel-009` 之錨鏈 | **併入 DR-11** |
| DR-10 | 多章節之 spec_reference | **撤銷**（§2.1，既有政策已涵蓋） |
| **DR-11（新）** | **CFTS100 之身分**：該 leaf 引用 `SYS-RA-CFTS100`（無序號）。需要 (a) CFTS100 是哪一份規格、(b) 該引用是否為筆誤、(c) 若非筆誤，其對應條款為何。**影響 1 leaf，但同時影響「本 feature 之規格邊界」此一前提** | **RD-1 提問（Q6）** |
| DR-7 | PROXI 表 | **維持**，惟 `See Proxi Table` 之 LID 實測為 **8** 非 6（A-VS16），本 feature 用得到者仍為 4 |
| S3 | Comfort HMI L&F | **已授權（R-VS13）未複製** —— 執行層正確地不動；下輪 W-0c 執行 |

---

## 5. 待 Pei 之事項（**全部 Tier 3，分析層與執行層皆不執行**）

| # | 事項 | 性質 |
|---|---|---|
| **P1** | 刪除 `features/vehicle setting/`（含空白之誤建目錄，A-VS19） | **不可逆操作** |
| **P2** | 本輪產物入庫（指令見上繳包 §10，帶 pathspec） | git |
| **P3** | 裁定 **R-VS9 v2**（§3） | 條文 |
| **P4** | 追認 **R-VS8**（兩份 DBC 並用，同版本不同網段） | 追認 |
| **P5** | 追認 **R-VS11 撤回**、**DR-10 撤銷**、**A-VS06 除役** | 追認 |
| **P6** | 裁定 **R-VS7**（Comfort 43 leaf 委派）—— **W-9 未執行，裁定素材尚未備妥**；建議俟 01 輪 W-9 產出後再裁 | 條文（可延） |
| **P7** | 裁定 **R-VS10**（Pop Up List 基線版本）—— 不阻塞 | 條文（可延） |
| **P8** | 複製 S3（Comfort HMI L&F）入 `inputs/`，或授權執行層於 01 輪代為複製 | 素材 |

**R-VS3 之修正**（A-VS19）：`new_feature.py "Vehicle Setting"` 產生含空白之
目錄，與 R-VS3 同時指定之 `features/vehicle_setting` 衝突。
**條文以目錄名為準**，指令參數改為 `vehicle_setting`；
`new_feature.py` 之名稱正規化缺陷由執行層於 01 輪登記為工具缺陷（A-VS19）。

---

## 6. 01 輪作業（**A 組殘項優先，不開新面向**）

| 作業 | 內容 |
|---|---|
| **W-0c** | 依 R-VS13 複製 `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf` 入 `inputs/`（15 檔）；更新 `INPUTS.sha256` |
| **W-8** | 三來源 `$變數$` 對照（本輪未執行）。**尚缺 CFTS044 內嵌值域之抽取**，兩式並用 |
| **W-9** | Comfort 43 leaf 逐條對照 → **做完必停**，備 R-VS7 素材 |
| **W-13** | 26PI2.5/HMI 全文掃描（112 檔）→ 以餘數驗證 A-VS10 |
| **W-15b′** | DBC ↔ LID 表逐屬性交叉比對（本輪僅做 DBC↔DBC） |
| **W-16（新）** | 追因 `recon.py` leaf 數 46 vs W-2 之 56（A-VS18）。**兩者皆宣稱在數 leaf，差額 10 未追因** —— 在 recon 產物被任何下游使用之前必須解決 |
| **W-17（新）** | 追因 LID 列數差 6（2,626／446 vs 2,629／449）；並補 `TRUNCATED_ENUM` 之其他形態（現僅偵測 `# = Not Used` 結尾） |
| **W-18（新）** | 26 個 N 欄未定 leaf 之處置草案：25 個指向 Heading／Information 列者，其 7 位數 ID 是否仍可落到章節？若否，提 BLOCKED 佔位之措辭草案 |

**不新增探索性作業。** 01 輪之目的是把 00 輪之殘項收乾淨。

---

## 7. 對上繳包 §9.3-2 之回應（**本輪最有價值的一段**）

執行層指出：本輪多數「相符」是**同一批檔案在自我印證** —— 分析層之預期
值與執行層之實測值皆自同一批素材算得，相符只證明兩造讀法相同，不證明
素材正確。真正的獨立檢驗只有兩處：W-5 之對照向、CFTS044 docx 之樣式階層。

**分析層接受此判斷，並據此調整 01 輪之驗證設計**：

1. W-8 之三來源比對**本身就是獨立檢驗**（CFTS044／DBC／LID 表為三個
   不同上游作者之產物），故其優先度高於任何新面向
2. W-13 之全目錄餘數掃描是 A-VS10 之唯一獨立檢驗
3. W-16 之 46 vs 56 是**兩個工具在同一份檔上得出不同答案** ——
   這類差異比任何相符都更有資訊量，不得因「recon 產物暫未使用」而延後

**推廣至 canon 之候選通則**（本包不立，記為候選）：

> 上繳包之「相符」項應標明其**是否為獨立來源之印證**。
> 同源自我印證與跨源交叉印證，在對照表上長得一樣，
> 但前者不構成正確性之證據。
