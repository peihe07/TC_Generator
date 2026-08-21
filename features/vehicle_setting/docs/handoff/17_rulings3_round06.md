# 17 下放包 — R-VS26 裁定、DR-15 登記、06 輪指令

分析層寫入，2026-08-20。Pei 指示「都照你建議」。

---

## 1. 裁決正文（執行層逐字轉錄入 `RULINGS.md`）

```
R-VS26（Pei 2026-08-20）
(1) 衍生檔（`data/*.tsv` 等）之寫出，**不得改變來源之語義分隔符**。
    來源以換行區分多個條目者，衍生檔須保留該區分
    （逐條目一列，或以不出現於資料中之逸出序列表示），
    不得以 `" ".join(cell.split())` 之類壓平。

(2) **凡需要語義結構之比對，一律自來源重建，不以衍生檔為輸入。**
    衍生檔之定位為「供人讀之快照」與「跨輪次之對照基準」，
    不是比對之輸入。

(3) 一份衍生檔若經證實有損，須於檔頭首行加註
        # SUPERSEDED — lossy, do not use as input; rebuilt by <script>
    並於同輪次之上繳包具名列出其下游使用者。
    **實際刪除屬 Pei**（版控範圍），分析層與執行層皆只標記。

理由：C3 之四次現身中，第 1–3 次修的是讀取，第 4 次證明
**寫出端與讀取端是同一條鏈**；只修一端，缺陷會在另一端重現。
```

---

## 2. DR-15（新，**Urgency High**，排在 framework 之前）

### 2.1 兩造證據（皆 in-scope，逐字）

**CFTS044 側** —— 條文 `4858356`（`$FR_HS_RQ$`）與 `4858386`
（`$FL_VS_RQ_TGW$`），標籤逐字為 `[EE Architecture:Atlantis High]`：

> the HU shall send an on change `$FR_HS_RQ$` **depending on the current
> status of `$HeatedSeatFR$`**. The signal value to be sent is detailed below
>
> | Current status | Signal to be sent |
> |---|---|
> | High | `$FR_HS_RQ$ = [Medium]` |
> | Medium | `$FR_HS_RQ$ = [Low]` |
> | Low | `$FR_HS_RQ$ = [Off]` |
> | Off | `$FR_HS_RQ$ = [High]` |

即**請求訊號承載階數，且為循環降階**。

**LID ＋ DBC 側** —— LID 之 Atlantis High 欄組將 `$FL_HS_RQ$` 等對映至
`TELEMATIC_VEHICLE_SETUP3.<X>_Tlm`；基線 DBC 實測：

| signal | bit 寬 | `VAL_` |
|---|---|---|
| `FL_HS_Tlm` | **1** | `0 "Not_Pressed"  1 "Pressed"` |
| `FR_HS_Tlm` | **1** | 同上 |
| `FL_VS_Tlm` | **1** | 同上 |
| `HSW_Tlm` | **1** | 同上 |

即**請求訊號為 1 bit 二值**。

**`Pressed / Not Pressed` 之四階對照另見於 `4857991` 等條文，
其標籤為 `[EE Architecture:CUSW]`，依 R-VS19 不取用** ——
故本衝突**不是架構差異可吸收者**：兩造皆在 in-scope。

### 2.2 為何是 High

兩種讀法產生不同形狀之 TC：

| 讀法 | procedure | ER | 設計方法 | TC 數 |
|---|---|---|---|---|
| 請求為 1 bit | 按一次 → `FL_HS_Tlm in TELEMATIC_VEHICLE_SETUP3 on BH-CAN` 之值為 `Pressed` | 驗 `$HeatedSeatFL$` 狀態訊號之變化 | Functional Based | 少 |
| 請求帶階 | 逐一設定目前狀態，按一次，讀請求訊號之值 | 驗四列對照表 High→Medium→Low→Off→High | **Decision Table** | 四分支 |

**`Heated Seat`（88 leaf）與 `Vented Seat`（72 leaf）兩個 Test Set 之
分支結構取決於此**，故排在 framework 之前。

### 2.3 RD-1 提問（可直接送出）

> CFTS044 條文 4858356 與 4858386（`[EE Architecture:Atlantis High]`）
> 定義 `$FR_HS_RQ$` / `$FL_VS_RQ_TGW$` 依目前座椅狀態送出
> `Medium` / `Low` / `Off` / `High` 之循環降階值。
>
> 惟基線 CAN 資料庫 `PDT27_E2A_R4_BHCAN.dbc` 中，
> `TELEMATIC_VEHICLE_SETUP3` 之 `FL_HS_Tlm` / `FR_HS_Tlm` /
> `FL_VS_Tlm` / `HSW_Tlm` 皆為 **1 bit**，值表為
> `0 = Not_Pressed`、`1 = Pressed`；
> `Logical Identifiers and CAN Mapping v1.76` 之 Atlantis High 欄組
> 亦將該等請求對映至上述 1 bit 訊號。
>
> 請確認 Atlantis High 之實作為何者：
> (a) 請求訊號為 1 bit，階數之循環由 HU 內部狀態機決定；或
> (b) 請求訊號承載階數，則其實際 signal 名／bit 寬／值表為何。
>
> 影響：Heated Seat 與 Vented Seat 兩個 Test Set 之 procedure、
> expected_result 與設計方法（Functional Based vs Decision Table），
> 涉及 160 個 Functional leaf。

**本項不排入 06 輪**（R-VS25 三項已滿），單獨走 RD-1；
答覆到位再排入輪次。

---

## 3. 06 輪指令

見 §4 之區塊。頭部順序依 16 包 §3 之裁定，**不再更動**。

---

## 4. 貼入 Claude Code 之內容

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/16_review_round05.md 本輪依據
  features/vehicle_setting/docs/handoff/17_rulings3_round06.md 裁決與 DR-15（本檔）
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入 R-VS25 之三項上限）

D-1  依 R-VS18 建立 docs/upstream/05_parser_fix_and_residual.md，
     六節先留空，逐項完成即填。
D-2  逐字轉錄 17 包 §1 之 R-VS26 入 RULINGS.md。
D-3  登記 DR-15（17 包 §2 全文）入 DATA_REQUESTS.md，Urgency High，
     並於 ANOMALIES.md 開 A-VS30 與之配對
     （in-scope 之 CFTS044 與 in-scope 之 LID/DBC 對請求訊號之
       值域與 bit 寬相衝突）。

## 作業（三項，R-VS25 上限；第四項起不得執行）

W-27  修正 A-VS29 ＋ 依 R-VS26 標記有損衍生檔
      (a) 修 lid_pairs.tsv 之寫出端：不得以 " ".join(split()) 壓平
          Format 欄之換行；依 R-VS26(1) 保留來源之語義分隔。
      (b) 依 R-VS26(3) 於 data/lid_map.tsv 與（若仍有損）
          data/lid_pairs.tsv 之檔頭首行加註
              # SUPERSEDED — lossy, do not use as input; rebuilt by <script>
          並於上繳具名列出其下游使用者。**不刪除**（屬 Pei）。

      驗收錨點（須可失敗，不得標「未實測」）：
        (a) 自 lid_pairs.tsv 讀回 ESS_ENG_ST 之 fmt 欄，須切得 11 個鍵值
            （`4 bit signal` 行 ＋ 1~9 ＋ `F = SNA`）；壓平則切不出
        (b) 自 lid_pairs.tsv 讀回 HSW_Stat，須為兩列（兩支 signal），
            第二列之 can 欄為空
        (c) 重跑 attribution.py，**C3 須為 0**；非 0 即未修好
        (d) C1／C2／C4／C5 與待判之計數須列出，並與 04 輪之
            1／2／8／6／16 逐項比較；**任一項變動須說明成因**
            （防止把 C3 壓成 0 卻推進別類）

W-28（併入 W-27，不佔順位）判準之反向樣本
      以三個已知為真差異之錨點，每次重跑須確認其仍在待判清單、
      未被任何 C 類吸收：
        DR-8   $VC_VEH_LINE$   完全無交集（字母碼 vs 數字車型碼）
        A-VS23 $TGW_DISP_STAT$ LID 側拼字錯 `diplay closed`
        DR-12  $PowerMode$     `IGN OFF` 於 CmdIgnSts 不存在
      任一錨點落入 C1–C5 即為判準過寬，停下回報。

W-22  餘數驗證 → data/value_extraction_residual.tsv
      逐 token 取其在 CFTS044 之全部出現位置，減去三式已命中者，
      逐筆檢視餘數上下文（前後 200 字元），分類為
        (a) 敘述性提及不帶值域
        (b) 帶值域但記法為三式所不涵蓋  ← 第四式之證據
        (c) 無法判定
      通過條件：(b) 為 0，或 (b) 全數化為新式並重跑。
      不得以「餘數看起來都是敘述」收尾 —— 須逐筆分類並附計數。
      已知：式一 451／式二 45／式三 34 命中。
      **依 R-VS26(2)，其輸入須自 CFTS044 原始 docx 重建，不得取衍生檔。**

W-9   Comfort 逐條對照 → docs/reports/comfort_overlap.md
      本 feature 側母體為 237 個 Functional leaf，非 271。
      逐條列出命中座椅加熱／通風／方向盤加熱之 Comfort leaf
      （SWE1-HVAC-*）與其對應之本 feature leaf，作為 R-VS7 委派句
      之來源表。另附 CFTS044 內文以 {CFTS043} 引用 Comfort 之 3 處上下文。
      連續四輪未執行；必停已由 R-VS7 解除。

**DR-15 不排入本輪**（R-VS25 三項已滿），單獨走 RD-1 提問。

## 禁區

git 寫入性操作一律不執行。需入庫者，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
衍生檔之刪除屬 Pei（R-VS26(3)）；.gitignore 之修改屬 Pei。

## 升級條件

W-27 之任一驗收錨點未通過；
W-28 之任一反向錨點落入 C1–C5；
W-22 之 (b) 類非 0 且無法化為新式；
實測與 16／17 包之數字不符；撞到 §8.4.1 編造壓力；
需要判斷而無條文。
本輪無「必停」項。

## 完成後

W-17／W-24／DR-14′ 追問排 07 輪。
DR-15 答覆到位後，framework Part Vehicle Setting ＋ profile（Tier 2）
方可開始 —— Heated Seat 與 Vented Seat 之分支結構取決於它。
```

---

## 5. 待 Pei

| # | 事項 |
|---|---|
| — | 03／04／05 三輪產物之入庫；推送（分支領先 origin 11） |
| — | DR-15 之 RD-1 提問送出（§2.3 之全文可直接用） |

**無待裁條文。** R-VS7～R-VS26 全數裁定完畢。

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS26 | 衍生檔紀律（裁定） | ✔ §1 |
| DR-15 | 請求訊號之階數 vs 1 bit 衝突（登記＋提問全文） | ✔ §2 |
