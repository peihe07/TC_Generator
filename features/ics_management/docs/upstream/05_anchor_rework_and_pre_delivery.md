# 上繳包 05 — 佔位補齊、Display ER 主錨改寫、Volume 收尾（2026-08-29）

對應下放包：`docs/handoff/05_anchor_rework_and_pre_delivery.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `0bb12f960ec7fd058113cbe9d57595a542107a916ad3655d9f593067908b6e42`**
—— 與執行層自身記錄相符，未停。

**禁區遵守**：git 全數未執行；分析層四簿與 `ANALYSIS_LOCK.md`、`docs/handoff/**`
**一字未寫**（但見 §7-1 之重大例外事實 —— 該檔於本包執行期間**由他者**變動）；
`$TGW_DISP_STAT$` 12 處佔位維持、未自選匯流排；009／005 之 TC 各 0；
`<Tpress>`／`<TPeriodToSendNoChange>`／`SIS-5161` **未臆值亦未回填**；
未以「ICS 收得到此訊號」書寫任何 ER。**本包未新增任何 TC，總數維持 23。**

**並行執行**：作業 D 以並行執行層實例進行（可寫檔限
`docs/reports/05_coverage_gaps.md` ＋ `scripts/gap_probe_05.py`）；A／B／C／E 由主實例執行。

---

## §0 量測基礎

沿 upstream-04 §0 全部條件。本包新增：

| 項 | 條件 |
|---|---|
| 佔位計數 | `scripts/pending_census.py`：對六欄套 `re.findall(r'PENDING: (DR-ICS\d+) <([^>]+)>')`，**禁人工列舉**（下放包 §4）。該腳本即此禁令之工具面 |
| 符號值之搜法（**本包新立**）| 對 CFTS020 全文搜 `<符號>\s*=`，**不只搜需求句**。理由見 §8 —— 連續三包之誤正出於「只查需求句、未搜節前定義塊」 |
| 強度／出貨判斷 | **執行層之判斷，非機械輸出**。判準寫於報告檔頭；`gen_pre_delivery_05.py` 以常數表承載，不偽裝成量測 |

---

## §1 裁決指紋（R-ICS1 ~ R-ICS23）

**24 錨點**（相異 ruling_id 23）。**R-ICS1 ~ R-ICS21 之 sha8 與 upstream-04 §1 逐項相同**
—— R-ICS19(b) 之圍籬 diff 程序本包無須動用。

| 條 | sha8 | 條 | sha8 |
|---|---|---|---|
| R-ICS1 | `3e48552b` | R-ICS13 | `273e1dbb` |
| **R-ICS2 v1** | `4a8819f0` | **R-ICS2 v2** | `b6ddfe90` |
| R-ICS3 | `b10318e0` | R-ICS14 | `6f9e4686` |
| R-ICS4 | `85de9871` | R-ICS15 | `545928c0` |
| R-ICS5 | `e6a4790d` | R-ICS16 | `4d0eb301` |
| R-ICS6 | `77478a91` | R-ICS17 | `ed8d8f0c` |
| R-ICS7 | `2c51cc80` | R-ICS18 | `ab6dc8ea` |
| R-ICS8 | `bf473e9c` | R-ICS19 | `1c841773` |
| R-ICS9 | `7e7aa921` | R-ICS20 | `b0e7170f` |
| R-ICS10 | `a2cda337` | R-ICS21 | `bf7ae107` |
| R-ICS11 | `e16c88e3` | **R-ICS22** | `81ac21cd` |
| R-ICS12 | `558acc83` | **R-ICS23** | `57bc646f` |

### 1.1 前提驗證 —— P1／P3 相符，**P2 開工時相符、完工時已不成立**

| # | 前提 | 開工時 | 完工時 | 判 |
|---|---|---|---|---|
| P1 | 相異 23、錨點 24 | 23／24 | 23／24 | 相符 |
| P2 | A-ICS 至 **33**；DR-ICS 至 **17** | A-ICS **33**、DR-ICS **17** | A-ICS **34** | **開工相符，完工不成立**（§7-1）|
| P3 | `holder: analysis-A`、`released: null` | 同 | 同 | 相符 |

---

## §2 作業 A — b03 八條之 ER 主錨改寫（R-ICS22(b)）

### 2-1 改寫後之末步（＝主錨）

| # | 末步（主錨） |
|---|---|
| P1 | `Check that the HU screen is dark and shows no content` |
| P2 | 同上 |
| P3 | `Check that the screen shown is the same as the screen recorded in step 2` |
| P4 | `Check that the screen shown is the same as the screen recorded in step 1` |
| S1 | `Check that the "TOUCH SCREEN TO TURN ON" graphic is still shown 2 seconds after the button press` |
| S2 | `Check that the screen shown is the same as the screen recorded in step 1` |
| S3 | `Check that the HU screen is dark and shows no content` |
| S4 | `Check that the screen shown is the same as the screen recorded in step 1` |

**八條之主錨皆為 HMI 可觀察現象且皆可單獨判定 → E2 未觸發。**
P1／P2／S1／S3 原末步為訊號讀取，本包**新增一 HMI 末步**；
P3／P4／S2／S4 原末步已為 HMI 現象，僅改訊號行措辭。

### 2-2 訊號面降為輔

顯示狀態／亮度之 ER 行加標 `(supporting observation)`；觀察位置一律書為
**CAN trace**，**不書為「HU／ICS 收到」**（R-ICS22(c)：該三訊號之 DBC 接收清單均不含 ICS）。

### 2-3 每條 reasoning 增之句（R-ICS22(b) 明令）

載明：主錨為 HMI 現象、訊號面為輔且 `$TGW_DISP_STAT$` **現仍為佔位**、
故該條之訊號面**目前無法實跑** —— **不得以外觀上之完整掩蓋驗證強度**。

### 2-4 驗核

`$TGW_DISP_STAT$` 佔位 **12（不變）**；Procedure↔ER **1:1 全保**；
23 條合檢 PASS、逐字比對 23/23。

---

## §3 作業 B — B1／B2 之佔位（R-ICS23(b)）

各增 `pre_conditions` 第 4 行：
`The no-change resend period of the ICS is PENDING: DR-ICS12 <no-change resend period>`
（寫為系統組態之狀態而非動作，IN §4.4）。其餘欄位未動。

**⚠ 本作業之前提於同日被推翻**：`<TPeriodToSendNoChange>` 之值**實存於 CFTS020**
（`= 20 msec`，§8）。**佔位仍依禁區維持不回填**，但其存在理由已由「值不存在」
變為「值查得而未回填，回填屬 b06」。

---

## §4 作業 C — 佔位口徑統一（A-ICS31）

`scripts/pending_census.py`（新腳本）實測：

| DR | 佔位處數 | 涉 TC 數 | 缺件（相異）|
|---|---|---|---|
| DR-ICS4 | 1 | 1 | `CFTS019 volume level range` |
| DR-ICS6 | 2 | 2 | knob2 之 browse/scroll/tune 對照；`Enter_Button` 之畫面對照 |
| DR-ICS8 | **12** | **8** | `TGW_DISP_STAT CAN signal` |
| DR-ICS10 | 2 | 2 | `Tstuck_button value` |
| DR-ICS12 | 4 | 4 | `detent counting time window`；`no-change resend period` |
| **合計** | **21** | **16** | |

逐批：b01 **2**、b02 **2**、b03 **12**、b04 **5**。四份 manifest 已改為腳本值並增
`counts.pending_source`；**`b03` 之 `counts_correction` 保留未刪**。

**E3 未觸發**：改前 manifest 值為 2／2／12／3，差異僅 b04 之 **2 處**（作業 B 剛加者），
未超「> 2 處」門檻。

---

## §5 作業 D — 覆蓋缺口清單（`docs/reports/05_coverage_gaps.md`）

**7 筆缺口**（`G1`～`G7` 為報告行號，非台帳號；除 A-ICS33 外一律寫 `A-ICS?`，**未自取號**）：

| # | 台帳號 | 摘要 | 受影響 TC | DR |
|---|---|---|---|---|
| G1 | **A-ICS33** | Short／Long Press **行為定義**於 ICS 側無母條 | 9 條（10 個裸按壓步驟）| DR-ICS6 |
| G2 | `A-ICS?` | SWE-ICS-005 完全無 TC | 0 | DR-ICS1 |
| G3 | `A-ICS?` | SWE-ICS-009 完全無 TC（Market 軸凍結）| 0 | DR-ICS13 |
| G4 | `A-ICS?` | SWE1-ICS-011 無 TC 且需求分頁缺列 | 0 | DR-ICS2 |
| G5 | `A-ICS?` | SWE1-ICS-012 無 TC 且需求分頁缺列 | 0 | DR-ICS2 |
| G6 | `A-ICS?` | SWE-ICS-004 之 VC 三操作僅涵蓋 browse，**scroll／tune 無 TC** | 2 | DR-ICS6 |
| G7 | `A-ICS?` | SWE-ICS-008 之 VC navigation flow **目標畫面未具名** | 1 | DR-ICS6 |

A-ICS33 之 `1.8.1.3` 逐物件表為自跑 `cfts020_probe.py --section 1.8.1.3 --json` 之輸出
（非抄既有報告），另做全文複驗（母數 2180）：`Short Press` 16 命中、`Long Press` 31 命中，
**判適用者皆 0**。全檔無「可暫用 FPDM 條文」之建議（R-ICS23(a) 明令）。

### 5-1 RD 覆蓋（全集以 `SYS2 Traceability` 為準 = 12；`SWE1 Requirements` 分頁實測僅至 010）

**有 TC 8 個**：001(2)、002(1)、003(4)、004(2)、006(4)、007(4)、008(1)、010(5)。
**無 TC 4 個**：005（DR-ICS1）、009（DR-ICS13）、011／012（DR-ICS2，需求分頁缺列）。
**成因為「實質不適用」者 0 個** —— 四個都是資料缺口，不是範圍判定。

### 5-2 Verification Criteria 對照：**有 2 條「有 TC 但 VC 未涵蓋」**

- **SWE-ICS-004**：VC 明載 `browse, scroll and tune operations`，而 B6 之 Pre-Condition
  逐字限定於 `list screen on which browse behavior is defined` ——
  **scroll 與 tune 無任何具名 TC**，browse 亦僅以 `PENDING: DR-ICS6` 承載。
- **SWE-ICS-008**：VC 明載 `HMI navigation flow`，而 N1 之 ER 4 只斷言「畫面有變」。

002／010 屬「驗證點已涵蓋、所需**數值**為佔位」，性質不同，未計入。

---

## §6 作業 E — 交付前體檢（`docs/reports/05_pre_delivery_check.md`）

23 條逐條有評。**強 12／弱 11**。

**強（12）**：b01 之 S1／S2／S3、b03 全 8 條、b04 之 B4。
**弱（11）**：V1／V2／V3（popup 顯示條件未載，潛在 FF）、I1／I2（門檻於 TC 內為佔位）、
B1／B2（觀察時點）、B3（以「畫面不變」承載）、B5（`= 3` 繫於計數窗）、
**B6／N1（主錨本身即佔位）**。

**E4 觸發，具名二條**：B6 與 N1 之主錨依賴未解之 DR-ICS6。依 E4 之令**未自行降階或刪除**。

---

## §7 預期數字對照（下放包 §5，11 項）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；24（相異 23）、A-ICS 33、DR-ICS 17 | 全數相符 | 相符 |
| 2 | TC 總數 | 23，不變 | **23** | 相符 |
| 3 | b03 八條之 ER | 主錨皆 HMI；訊號行標為輔 | 8/8（§2-1）| 相符 |
| 4 | `$TGW_DISP_STAT$` 佔位 | 12，不變 | **12** | 相符 |
| 5 | 新增佔位 | 2 處 | **2** | 相符 |
| 6 | 全批佔位總數 | 21 | **21** | 相符 |
| 7 | manifest 修訂 | 4 份；`counts_correction` 保留 | 4 份；保留 | 相符 |
| 8 | 覆蓋缺口清單 | ≥ 1 筆 | **7 筆** | 相符 |
| 9 | 強度自評 | 23 條逐條；弱者具名 | 23 條；弱 11 具名 | 相符 |
| 10 | `ledger_guard` 完工後 | exit 0，**與開工前逐字相同** | exit **0**，但**輸出不相同** | **不符 —— §7-1** |
| 11 | 四支 gate | 差皆 0；基線外 2 | 差皆 0；基線外 2，皆 `driver_distraction` | 相符 |

### 7-1 【重】不符 1 項：`ledger_guard` 前後**不逐字相同**

```
37c37
<   登記列 33 列，相異 33，最大號 **A-ICS33**
---
>   登記列 34 列，相異 34，最大號 **A-ICS34**
46c46
<   28b64a4b69b7107d  2026-08-29 15:03:50  features/ics_management/ANOMALIES.md
>   f37e20f2e08b4bea  2026-08-29 15:10:33  features/ics_management/ANOMALIES.md
```

exit code 二次皆 **0**（無 DUPLICATE／INCONSISTENT），但 `ANOMALIES.md` 於本包執行期間
**由他者新增 A-ICS34**。執行層未寫任何台帳檔；權杖持有者為 `analysis-A`，故此為**合法**寫入。

**但這是 R-ICS17 所防之事的另一面**：R-ICS17 治「二個分析層實例同寫」，
而本次是「分析層於執行層執行期間寫入」——**上繳包所依之前提在其產出期間發生變動**。
`ledger_guard` 之**逐字比對**抓到了它；**只比 exit code 會漏**（二次皆 0）。
下放包 §5-10 之「逐字相同」為此設，**其失效本身即該檢查之有效性證明**。

---

## §8 【本包最重之發現】A-ICS34 —— 連續三包之斷言為誤，本包獨立複驗其為誤

A-ICS34 稱 CFTS020 有 time-variables 定義塊。**本包不採信其陳述，獨立全文搜
`<符號>\s*=` 複驗**，不僅證實，另補三項該異常未載之事實：

### 8-1 定義塊在**四個節**各一份，且 **§1.8.1 那一份與其餘三份不同**

| 所屬節 | `<Tpress>` 之值 |
|---|---|
| §1.5.1 ICS HMI Communication | `defined for each specific button/softkey. See PDO HMI Screen Rules for "Long Press' behavior` |
| **§1.8.1 ICS HMI Communication（本 DUT）** | **`500 msec`** |
| §1.11.1 DCSD120_wICS_Port HMI Communication | 同 §1.5.1 |
| §1.14.1 ICS HMI Communication | 同 §1.5.1 |

其餘六符號四份一致：`<Tsend> = 150 msec`、`<Tbutton> = 100 msec`、
`<TPeriodToCountKnobDetents> = initial value 50 msec`（**明標待 parameter tuning 優化**）、
`<Tpower> = 1.5 sec`、**`<Tstuck_button> = 120 sec`**、**`<TPeriodToSendNoChange> = 20 msec`**。

### 8-2 承載物件為 **`CFTS020-4819541`**，且**可充錨**

`Artifact Type` = `Subsystem Functional Requirement`、`ECU` 軸缺、
`Radio` 含 `R1L`／`R1L-R`、`EE` 含 `Atlantis High` → **v2 判適用**。
（並行之作業 D 獨立追到同一物件；連同分析層之 A-ICS34，**三條路徑收於一點**。）
全 repo grep `4819541` 僅 1 處命中（v1→v2 差異表），**從未在任何 handoff／upstream／台帳被討論**。

### 8-3 本包**未回填任何佔位**

依 A-ICS34 自身之處置（「適用屬性之逐物件驗證交 b06」）與下放包 §1 禁區。
**但受影響之陳述已逐處更正**：體檢報告之強度與出貨欄，「門檻無值」一律改為
「值查得而未回填」，並補其實質影響：

- `<TPeriodToSendNoChange> = 20 msec` **遠小於** B1／B2 所用之 2 秒觀察點
  → **該二條之觀察時點實際上是安全的**（upstream-04 §10-2-2 所述之風險，實測為低）
- `<TPeriodToCountKnobDetents> = initial value 50 msec` **明標暫定且待調校**
  → 回填後 B5／V3 之數值面**仍非定值**
- `<Tstuck_button> = 120 sec` **與 CFTS022-4914956 之 120 s 同值** → 二面互證

### 8-4 成因（自承）

「只查需求句、未搜節前之定義塊」。**符號類之 DR 發出前須全文搜 `<符號> =`** ——
已寫入 §0 之掃描條件。此誤連續出現於 upstream-02 §六-3、A-ICS17、upstream-03、upstream-04，
**且無任何 gate 會紅** —— 因為它不是格式錯，是事實錯。

---

## §9 【第二個自承之誤】「23 皆為 `[ECU:FPDM]`」與實測不符

upstream-04 §4-4 書「**皆為 `[ECU:FPDM]`**」，R-ICS23(a) 沿用。
並行之作業 D 提出不符，本包獨立複驗：

| 排除成因 | 物件數 | ObjectID |
|---|---|---|
| `ECU` 含 `FPDM` | **16** | — |
| `ECU` 僅 `CCDMF` | **2** | 4819602、4819606 |
| **`ECU` 軸缺，因 `Radio`／`EE` 落空** | **5** | 4819594、4819596、4819600、4819607、4819613 |

**判定結果（23 不適用）相符，成因分類不符。** 那 5 個之排除**不是** v2(b)(ii) 的 ECU 判定，
而是 v2(b)(i) 的 Radio／EE 實值落空。A-ICS33 之成立不受影響，
但 R-ICS23(a) 之條文載有一個不成立的事實描述。

---

## §10 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | b03 八條之 ER 主錨改寫；B1／B2 之佔位；四份 manifest 之口徑統一；`pending_census.py`／`gen_pre_delivery_05.py`／`gap_probe_05.py` 三支新腳本；覆蓋缺口清單；交付前體檢；受 A-ICS34 影響之理由逐處更正 |
| **核實無誤** | R-ICS1~21 之 sha8 與 upstream-04 逐項相同；`$TGW_DISP_STAT$` 佔位仍 12；1:1 全保；23 條逐字命中 23；A-ICS34 之時間變數（獨立複驗並補三項新事實）；A-ICS33 之核心（全文複驗，判適用者 0）|
| **正確地不動** | 佔位一處未回填；`$TGW_DISP_STAT$` 未自選匯流排；009／005 之 TC 各 0；N1 之內容未改；`counts_correction` 未刪；未自取 `A-ICS?` 編號；E4 之二條未降階未刪除；分析層五簿一字未寫 |

---

## §11 待分析層裁定

1. **【最重】A-ICS34 之回填範圍與方式（§8）**：`4819541` 可充錨，其六值直接對應
   DR-ICS10／DR-ICS12。**二者是否即可結案？** `initial value` 與 `parameter tuning`
   之保留字如何處置（回填後其值仍為暫定）？
2. **R-ICS23(a) 之事實描述須更正（§9）**：實為 16／2／5。條文結論不變但理由有誤 ——
   依 R-ICS17(d) 是否須另立 `R-ICS23 v2`。
3. **`ledger_guard` 前後不相同之處置（§7-1）**：是否須立「執行期間之台帳凍結」
   或「上繳包以開工時之快照為準」之條文。
4. G6／G7 二個 VC 未涵蓋之缺口（§5-2）：`scroll`／`tune` 是否須補 TC。
5. G2～G7 之 `A-ICS?` 取號。
6. SWRA `Verification Method`（006 之 `Integration Test`、010 之 `Robustness Test`）
   與 TC `design_method` 是否須對應 —— 現行台帳無條文。
7. `SWE-ICS-001` 之二條以 `VOLUME POP_UP` 音量階承載「方向偵測」，
   而 `SWE-ICS-003` 讀 `Radio_Knob2_DIR` 訊號 —— 同為 direction 而觀察面不一致。

---

## §12 獨立判斷

### 12-1 【下放包 §7-5 指定】17 條 DR 全無回覆時，哪幾條可現狀出貨

**可出貨 13 條／不可 10 條。** 判準：主錨可單獨判定 **且** TC 內無未回填之佔位。

**可（13）**：b03 全 8 條（R-ICS22(b) 明裁不因 (a) 之佔位阻出貨；主錨為 HMI 現象，
佔位僅及輔助行 —— **出貨時該輔助行應標明未解**）、b01 之 S1／S2／S3、b04 之 B4、
b04 之 B3（**可（弱）**：無佔位可執行，但主錨為「不變」，通過不足以證成條文，
**出貨時應標為弱驗證**）。

**不可（10）**：V1／V2／V3、I1／I2、B1／B2、B5、B6／N1。

**其中最須留意者是 V1／V2 —— 它們無任何佔位而仍不可出貨。**
其 ER 各有 2 行斷言 `"VOLUME POP_UP"` 顯示，而顯示條件五包追索仍查無
（CFTS022／020／019 七件／HMI L&F 六本全掃遍，線索指向不在 repo 之
`Pop-up List Notification`）。**「無佔位」不等於「可出貨」** ——
佔位擋得住的是「我知道我不知道」，擋不住「我不知道我不知道」。
V1／V2 正是後者：外觀完整、機檢全綠、逐字命中，而其 ER 有 2 行可能永遠判不出對錯。

### 12-2 本包是否仍有該驗而未驗者 —— **有，五項**

1. **A-ICS34 之六個值尚未逐物件驗適用性**（交 b06）。回填前，21 處佔位中有 **6 處**
   （DR-ICS10 2 ＋ DR-ICS12 4）是「值已在手而未用」——
   **這種佔位比真正缺值的佔位更危險**：它看起來與後者無異，卻早可解。
2. **`4819541` 從未被討論過**。同一份 CFTS020 已用了四包，而其 §1.8.1 節前之定義塊
   直到第五包才被讀到 —— **同類「節前定義塊」是否還有其他**，本包未做全面掃查
   （只搜了時間符號）。
3. **G6 之 `scroll`／`tune` 無 TC**。SWE-ICS-004 之 VC 明載三操作，現只涵蓋 browse
   且其本身亦為佔位。**這是覆蓋面的缺，不是資料的缺。**
4. **`$TGW_DISP_STAT$` 之 12 處仍未解**（DR-ICS16）。b03 八條雖可出貨，
   但其訊號面**至今無一次可實跑**。
5. **V1／V2／V3 之 popup 面連續五包無進展**，且本包確認答案不在 repo。
   **繼續在 repo 內找是浪費**；只能由上游提供 `Pop-up List Notification`。

---

## §13 未結 DR 清單

**DR-ICS1 ~ DR-ICS17，17 條全開。** 新事實：

| DR | 新事實 |
|---|---|
| DR-ICS4 | 五包追索確認答案不在 repo |
| DR-ICS6 | 佔位 2 處；G1／G6／G7 三缺口皆掛此 DR |
| DR-ICS8 | 佔位 12 處，與 DR-ICS16 為同一問題之兩面 |
| **DR-ICS10** | **疑可結** —— `4819541` 載 `<Tstuck_button> = 120 sec` |
| **DR-ICS12** | **疑可結** —— `4819541` 載 `50 msec`／`20 msec`；惟前者標 `initial value` 待調校 |
| DR-ICS13 | Menu Navigation 之組別存續仍繫於此 |
| DR-ICS16 | b03 八條之訊號面繫於此 |
| DR-ICS1／2 | G2／G4／G5 三個無 TC 之 RD 掛此二 DR |

---

## §14 本包引用之編號清單

R-ICS1 ~ R-ICS23（sha8 見 §1；`R-ICS2` v1 `4a8819f0`／v2 `b6ddfe90`、
R-ICS22 `81ac21cd`、R-ICS23 `57bc646f`）；
A-ICS16、A-ICS17、A-ICS25、A-ICS29、A-ICS31、A-ICS32、A-ICS33、**A-ICS34**；
DR-ICS1 ~ DR-ICS17；
R-G13、R-G23、R-G25；R-DD3 同族、R-DD26 v2；R-TM13；R-6；
FO §8.2、FO §8.4、FO §8.5、FO §8.8；
IN §4.4、IN §5.5、IN §7、IN §8.4.1、IN §8.4.3、IN §9、IN §11。

**本包未產生任何新裁決條文，亦未自取任何 A-／DR- 編號。**
建議登錄之 anomaly 三則（編號由分析層取）：
§7-1（分析層於執行層執行期間寫台帳，`ledger_guard` 逐字比對抓到而 exit code 抓不到）、
§9（`1.8.1.3` 之排除成因為 16／2／5 而非全數 FPDM，R-ICS23(a) 之理由有誤）、
§12-2-2（CFTS020 之「節前定義塊」四包未讀，同類是否尚有其他未查）。
另作業 D 提出之 G2～G7 六筆缺口待取號。
