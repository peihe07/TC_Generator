# 26 — Pei 交付後審查之缺陷量化與整改下放（rev A, 2026-08-25）

緣起：Pei 於 2026-08-25 對交付件
`ASW-R2/Time Management/FM-WI-FSM-036-A01 …_SWQT_20260822.xlsx`
（SHA256 前綴 `2afd87be418e8559`（§6 C1 更正），Test Case Specification 分頁 59 條 TC，
列 10–68）提出四項批評：(1) Setting 操作應放步驟並給入口路徑；
(2) Ignition／CAN 可用性之 Pre-Condition 寫法未修；(3) Pre-Condition
未編號；(4) 數字編號前出現空格。分析層逐列稽核（openpyxl
read_only+data_only，另以 raw XML 反驗），量化如下。依 R-TM4，
凡計數皆附完整列清單。TC 號以 `#NNN` 縮寫 `NR1L-TimeAndDate-NNN`（§6 C2 更正）。

---

## §1 缺陷量化清單

### D1 — Pre-Condition 未編號：59/59

全部 59 條之 J 欄無 `1.` 起首編號（含單行者）。canon §11「one item
per line」與交付基準（UserProfiles 0824 之 189/189 皆編號）均要求編號。
**處置**：全數補 `1.`、`2.` … 編號。

### D2 — 本 feature 自身之設定狀態寫於 Pre-Condition：35 條

`"Sync Time with GPS" is set to ON/OFF`、`"Sync Time with GPS" is not
available`、`"Time Format" was set to …` 等寫於 J 欄。Clock 設定即本
feature 之受測物，此屬 canon §4.4 禁止之「feature under test as
premise」＋「step-controlled state」，且未給任何入口路徑（Pei：
「怎麼按 Sync Time with GPS」）。

完整清單（35）：#001 #002 #003 #004 #005 #006 #014 #018 #019 #021
#023 #024 #025 #026 #027 #028 #029 #030 #031 #036 #037 #038 #040
#043 #044 #045 #046 #047 #050 #052 #053 #054 #055 #056 #057

**處置（R-TM81）**：遷移至 Procedure 首段，措辭固定為兩步：

```
1. Open the "Clock" settings
2. Set "Sync Time with GPS" to OFF
```

入口路徑來源：HMI Settings List R1L-R (Feb 13 2026) §7 Clock 項 1
`Sync Time with GPS`（On/Off Checkbox，Technical Ref CFTS015）。
頁名沿用既有常數字面 `"Clock"`（DR-12b 之佔位語意不變，A-TM28 未裁前
照留）。其中 25 條之 Procedure 已有 `Open the "Clock" settings` 步驟，
僅需併入 Set 步驟；**12 條需補入口**：#004 #005 #018 #019 #023 #024
#025 #027 #028 #043 #052 #053。ER 須 1:1 補對應行（§6）。

**排除**：#048 #049 之 `Proxi Cluster_Display_Type is set to …` 與
#020 #022 之 `Proxi NAV_Presence is set to …` 為車輛配置（外部環境），
屬合法 PC，**不遷移**；僅記法正規化為 canon §8.7.5(c)：
`PROXI Cluster_Display_Type = 3 (High Display)`（前綴大寫 PROXI，不加 $）。

### D3 — System-default／步驟可控狀態寫於 Pre-Condition：59 條全中

J 欄行別頻次（執行層可逐列複核 `data/` 稽核輸出）：

| 行 | 次數 | 處置 |
|---|---|---|
| `Ignition is ON` | 56 | **刪除**（§4.4 system default，同 `HU is powered on` 型） |
| `The CAN bus is awake` | 18 | **刪除**（同上） |
| `Ignition is OFF` | 3（#004 #019 #025） | 步驟可控之起始狀態 → 轉 Procedure 首步 `Switch the ignition off`，或既有步驟已含轉換者逕刪 |
| `The CAN bus is asleep` | 7（#012 #035 #041 #042 #048 #049 #051） | 同上 → 轉 sleep 建立步驟（其可觀察終止條件仍為 DR-9 佔位） |

**保留不動**（合法 PC）：`GPS signal is available/unavailable`（§4.4
明列之外部環境）、`The vehicle is an Atlantis High/Mid architecture
variant`（R-TM76）、Proxi 配置行（見 D2 排除）。#009 #015 #017 #019
#032 #041 #042 #045 #051 #052 #053 #054 等其餘狀態行由執行層逐列按
§8.5 判準分類：spec trigger → 留；步驟可控 → 轉步驟；環境穩定前提 → 刪。
判定結果逐列列表回繳，不得只回計數（R-TM4）。

### D4 — 訊號記法仍為已撤銷之 v1 三件組：22 條 29 處

`$DateTmHour$ in TELEMATIC_FD_1.Hour1_TLM / … on FD` 型。
完整清單（條：處數）：#006:1 #007:1 #008:1 #011:2 #012:2 #013:1
#014:1 #025:1 #027:3 #028:2 #035:1 #036:1 #037:1 #038:1 #040:1
#042:1 #046:2 #047:1 #055:2 #056:1 #058:1 #059:1。
（`on FD` ×25、`on CAN-B` ×3，另 1 處 segment 為 `PENDING: DR-6`。）

**依據（R-TM82）**：R-TM48 之生效客體是 repo canon 之 §8.7.5 本身，
charter 明訂 repo 版為權威且持續演進；canon 已於 2026-08-21 撤銷 v1/v2
改行 v3，且 `docs/runtime/profiles/` 無 TimeManagement profile、無
cited override，依 FO §0 本 feature 從現行 v3。**處置**：

- 三件組改寫為 `$<MESSAGE>.<Signal>$ = <raw> (<label>)`；**網段一律不寫**
- LID 名（`$DateTmHour$` 等）依 v3(d) 轉為可觀察 CAN 訊號全名，對映
  取 `data/lid_atlantis_high.tsv`（R-VS67 同型：以 LID Atl-H 欄為準）；
  例：`$DateTmHour$ in TELEMATIC_FD_1.Hour1_TLM on FD` →
  `$TELEMATIC_FD_1.Hour1_TLM$`
- 一位一訊號分寫（Hour1/Hour2 各自成名），值域之 raw/label 取 DBC；
  DBC 無 VAL_ 列舉之數值訊號寫 `= <raw>` 不附 label，不得造 label（§8.4.1）
- **DR-6 之唯一佔位（#035）隨 v3 消滅**（v3 不寫網段，segment 缺件
  不復存在）；DATA_REQUESTS #6 之 Atl-Mid 側缺網段一事同步降轉為
  「僅供追溯，不再阻塞」，於 DATA_REQUESTS.md 加註、不刪列（R-TM13）

### D5 — 內容欄置中對齊（「編號前空格」之成因）：59×5 格

I–M 欄資料列（10–68）全為 horizontal=center + vertical=center。
多行換行文字置中後，每行編號前出現寬窄不一之視覺空白 —— **文字層無
前導空白**（raw sharedStrings 逐字驗證 0 筆，`&#10;` 後接空格 0 筆）。
交付基準（UserProfiles 0824）同欄為預設靠左。
**處置**：I–M 資料列改 left + top（wrap 保留）；openpyxl 改樣式須
非 read_only 開檔且不可經 openpyxl 存檔破壞 x14 驗證 —— 依既有
write_back 工具鏈之樣式通道為之，w/ dry-run（R-TM78）與 `--out`（R-TM80）。

### D6 — 未結 PENDING 佔位：19 條（§8.4.3 不得出貨）

| DR | 條數 | 列 |
|---|---|---|
| DR-10（GPS 訊號控制四能力） | 9 | #004 #005 #018 #019 #023 #024 #028 #052 #053 |
| DR-20（無效訊號注入） | 7 | #015 #016 #017 #039 #043 #058 #059 |
| DR-8（ECU 軟體重置） | 1 | #033 |
| DR-9（CAN sleep 終止條件） | 1 | #034 |
| DR-6（網段） | 1 | #035 —— 依 D4 隨 v3 消滅，不待答覆 |

另 Remarks 側存 `PENDING: DR-12b 設定頁名` 佔位（值照留 `Clock`）。
**裁定點（Pei）見 §3。**

### 通過項（本次稽核無缺陷）

ER 無 modal verbs（0/59）；四欄無尾句號（0 行）；輸出欄無方括號；
test_item 括號下半 59/59 齊備。

---

## §2 條文落檔

**R-TM81（分析層裁定，2026-08-25，依 Pei 同日指示）**：本 feature 之
Clock 設定項狀態（Sync Time with GPS、Time Format 等 §7 Clock 節項目）
不得寫於 Pre-Condition；一律以 Procedure 步驟建立，入口固定
`Open the "Clock" settings` → `Set "<項名>" to <值>`，項名逐字取
HMI Settings List R1L-R (Feb 13 2026) §7。Proxi 配置行不在射程
（車輛配置屬外部環境）。

**R-TM82（分析層裁定，2026-08-25）**：§8.7.5 於本 feature 之適用版本
隨 repo canon 現行版（v3）。R-TM48 之引用為動態引用（charter：repo 版
權威且演進）；R-TM49 之 segment 缺件處理隨 v3 失所附麗，條文保留為
軌跡不刪（R-TM13）。DR-6 佔位依 D4 處置。

兩條待謄入 RULINGS.md（含 Pei 異議則先改後謄）。

---

## §3 裁定點（Pei）

唯一：**D6 之出貨時序** —— DR-8/9/10/20 皆為設備能力缺件（阻塞執行、
不阻塞措辭），答覆時程不在我方。選項：
(a) 先出格式整改版（D1–D5 全修，PENDING 照留，工作簿標註不可出貨）；
(b) 等 DR 答覆一併 Revise。
分析層建議 (a)：格式缺陷與設備缺件無耦合，分開修可先消 Pei 之審查退回項。

---

## §4 下放工作單 W-TM-26（執行層，待 Pei 對 §3 表態後啟動）

基準檔：交付件 20260822（SHA256 `2afd87be418e8559…`（§6 C1）），輸出另檔
（`--out`，R-TM80），dry-run 先行（R-TM78），lint036 全檢後回繳。

T1 D1：J 欄 59 條補編號。
T2 D2：35 條設定狀態遷移＋12 條補入口＋ER 1:1 補行；#020 #022 #048
    #049 之 Proxi 行正規化為 `PROXI <Param> = <raw> (<label>)`。
T3 D3：`Ignition is ON` ×56、`The CAN bus is awake` ×18 刪除；
    OFF/asleep 10 條轉步驟；其餘狀態行逐列判定並列表回繳。
T4 D4：29 處 v1→v3 改寫（對映表 `data/lid_atlantis_high.tsv`）；
    #035 之 DR-6 佔位移除；DATA_REQUESTS #6 加註。
T5 D5：I–M 資料列對齊改 left+top。
T6 回繳包附：逐列 diff 清單、lint 報告、未結 DR 清單。

## §5 未結 DR 清單（本包上繳之隨附義務）

DR-2（037 正式件身分，High）、DR-4（037 覆蓋缺口 48 筆，High）、
DR-5（CFTS015 缺件物件 ×2，中）、DR-6（Atl-Mid 網段 —— 依 D4 降轉
追溯用）、DR-8（High）、DR-9（High）、DR-10 四分項（High）、
DR-12（其餘 UI 標籤，開放）、DR-12b（設定頁名，High）、DR-20（High）。
DR-7 空號、DR-11 已取消（軌跡保留）。

---

## §6 執行層反驗回報（2026-08-25，W-TM-26 啟動前）

依 (a) 啟動 W-TM-26 前，先對基準檔逐列反驗 §1 全部量化。**D1／D3／D4／
D5／D6／通過項六項完全吻合**，其中 D4 之 22 條 29 處逐條處數亦與清單
一一相符。以下四項不符，於動工前先行更正。

### C1 — 基準檔 SHA256 不符（阻塞 §4 之基準宣告）

§0 與 §4 記為 `088a44765082feab…`，實測交付件為

```
2afd87be418e85599a99670db74457c3a629220583d39db195870a61093833c1
```

repo 內無任何檔案雜湊為 `088a…`。該檔 mtime 為 2026-08-22 16:27（早於
本次稽核），且 `output/` 於 `.gitignore` 第 17 行，無版本歷史可資比對 ——
故非「稽核後被改動」，判為謄錄錯誤。**§0／§4 之 SHA 更正為 `2afd87be…`。**
本項亦顯示基準宣告未經回讀驗證即落檔，登記為 A-TM30（下放包之 SHA
應由腳本產出而非手抄）。

### C2 — TC 號前綴誤植

§0 記 `#NNN` 縮寫 `NR1L-TimeManagement-NNN`，實測 59 條全為
`NR1L-TimeAndDate-NNN`（前綴計數 59/59）。`TimeManagement` 為目錄
slug（R-TM1）而非 TC ID family。**§0 之縮寫定義更正為
`NR1L-TimeAndDate-NNN`。**

### C3 — D2 清單短少 2 條，且入口有無之分割誤判 2 條（R-TM4）

D2 之敘述文字已明列 `"Time Format" was set to …` 為射程內型態，但
**完整清單（35）漏列 #041 #042**：

```
#041 PC: "Time Format" was set to "12 hrs" before sleep
#042 PC: "Time Format" was set to "24 hrs" before sleep
```

二者 Procedure 為 `1. Wake the CAN bus / 2. Read …`，**不含**
`Open the "Clock" settings`。故實測分割為：

| 項 | 文中 | 實測 |
|---|---|---|
| D2 總條數 | 35（清單）／37（25+12 之和） | **37** |
| 已有入口，僅併 Set 步 | 25 | **23** |
| 需補入口 | 12 | **14**（原 12 條 + #041 #042） |

文中 25+12=37 與清單之 35 自相矛盾 —— 計數與其所附清單不一致，正是
R-TM4 所欲攔下之型態。**總數 37 為正，清單與分割依上表更正。**

**#041 #042 之遷移含次序約束，非 R-TM81 之定式兩步可涵蓋**：Time Format
須於 sleep **之前**建立，而 sleep 又是該二條之受測前置。所需為三段
（開設定 → 設值 → 建立 sleep → 喚醒），且 sleep 建立步驟本身仍受 DR-9
（可觀察終止條件）未結之限。**列為裁定點，見 §7。**

### C4 — D2 排除清單（Proxi）短少 1 條

D2 排除段列 #020 #022（NAV_Presence）與 #048 #049（Cluster_Display_Type）
共 4 條。實測 **#021 亦含 `Proxi NAV_Presence is set to 1 (Present)`**
（#021 同時含 Clock 設定行，故既在 D2 遷移射程、其 Proxi 行又在排除射程，
二者不衝突）。**正規化對象為 5 條：#020 #021 #022 #048 #049。**

### C5 — T5 所依賴之「既有 write_back 樣式通道」不存在

D5 處置記為「依既有 write_back 工具鏈之樣式通道為之」。實測
`scripts/` 全域無 `Alignment` / `horizontal=` / `wrap_text` 任一命中，
`write_back.py:253 write_rows` 僅寫 `value`，不觸樣式。**該通道不存在**，
T5 需先於 `write_back.py` 新增樣式通道 —— 屬工具變更而非資料變更，
與 A-TM29（同檔之預設值修改）同族。**列為裁定點，見 §7。**

---

## §7 追加裁定點（Pei）

C1／C2／C4 為事實更正，已逕改，不需裁定。餘二：

**Q1（C3）** #041 #042 之遷移形式。選項：
(a) 比照 R-TM81 定式，於 sleep 建立步驟前插入兩步，成四步式；
(b) 該二條之 Time Format 前提改由 Input Test Data 承載，PC 僅留 sleep；
(c) 暫緩該二條，隨 DR-9 答覆一併處理（其 sleep 步驟本就受 DR-9 阻塞）。
執行層建議 (a)：與 R-TM81 同形，且 DR-9 只阻塞 sleep 步驟之**執行**，
不阻塞其**措辭**，與 §3 選 (a) 之理由一致。

**Q2（C5）** `write_back.py` 新增樣式通道之層級。選項：
(a) 視為 W-TM-26 射程內之工具附隨變更，逕改並於本包回報；
(b) 比照 A-TM29 登記為 Tier 2，T5 本輪不做，D5 留待工具修畢。
執行層建議 (a)：A-TM29 之所以列 Tier 2 是因其改**既有預設值**而牽動
其他 feature；本項為**新增**一條僅在明示啟用時生效之通道，不改既有行為，
跨 feature 風險與之不同族。

**T1／T3／T4 不受 Q1／Q2 影響，可即刻開工；T2 待 Q1、T5 待 Q2。**
