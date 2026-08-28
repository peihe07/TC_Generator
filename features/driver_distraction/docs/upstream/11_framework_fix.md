# 上繳包 11 —— framework.md 落檔、Test Set 更正、T20a–e、T-登

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`14_framework_fix.md` §六（T20a–e、T-登）
- 本輪**未生成 `-017`~`-028`、未寫回、未執行 git、未寫入他 feature 任何檔**
- 共用路徑：**未寫入一字**；**T17b 維持停止**

> **三件事**：
> **`framework.md` 落檔**，B1 之 Test Set 依經核准之 Layer 2 更正（`Speed Monitoring`／`Lockout Tables`）。
> **自檢第 1 項改為真讀 framework.md 比對**，並附**反向對照** —— 四種壞值皆能使其變紅（§3.2）。
> **T20c 之答案是第三種**：負向面 **CFTS022 載、037 未載**，但**樣本不可自綁定來源決定**
> —— p7 十六列全為 `L/O`，而 CFTS022 之表以圖片參照且該 xlsx **無任何嵌入物件**。
> 故登 `COVERAGE_GAPS.md` [CG-DD1]，**不造樣本**。

---

## 1. T20a —— `framework.md` 落檔

### 1.1 全文

```markdown
# framework.md — Driver Distraction

狀態：**LOCKED**（Pei 裁准鎖定：下放包 03 §五；Layer 1 之 `Driver Distraction`
另由 **R-DD1** 定）。
Feature slug：`driver_distraction`
規範依據：IN §4.1（三層框架）、§4.1.5（僅 Layer 1 ＋ Layer 2 ＋ Layer 3）、
§4.2（Test Set）；FO §0（Tier 2：framework Test Set derivation 屬 Pei 簽核）

**落檔註記（2026-08-28，下放包 14 §1.3）**：本檔於包 03 §五 提請、Pei 准，
惟包 04 起未列入任何一輪之任務表，**故遲至本輪始落**。
成因在分析層（未下落檔指令），非執行層漏做。
**pilot 4 則與 B1 10 則係在本檔不存在之下產出** —— 其 Test Set 已依
下放包 14 §六 T20a 對齊本檔（見 §變更紀錄）。

---

## Part I — Layer 1（Test Group，寫入工作簿）

```
Driver Distraction
```

依 **R-DD1**：取 037（FM-WI-FSM-037-A03）`Project Name` 欄實值。
CFTS022 章名 `Driver Distraction Lockout` 與 HMI spec 題名 `Driver Lockout`
**均不採** —— 037 為生成主驅動，Layer 1 從其命名。
寫入工作簿 Test Group 欄，全簿逐字一致。

---

## Part II — Layer 2（Test Set，寫入工作簿）

**六組，28 leaf 全分掛。** 下列六列逐字取下放包 01 §三 之草案、
經下放包 03 §五 提請並由 Pei 准鎖，下放包 14 §二 重申。

| # | Test Set | leaf | 能力叢集 |
|---|---|---|---|
| 1 | `Body Off Init` | 001–002 (2) | 出眠初始化：Lock Out State 復位、process 終止後冷啟 |
| 2 | `Speed Monitoring` | 003–008 (6) | `$Speedometer$` 監看、≥5MPH 上鎖、≤3MPH 解鎖、訊號失效 |
| 3 | `Lockout Enforcement` | 009–012 (4) | Locked 態之存取阻擋、使用中之強制退出 |
| 4 | `Lockout Tables` | 013–016 (4) | Lockout Table 所列 feature 之逐項套用 |
| 5 | `Hong Kong Market` | 017–024 (8) | `Country_Code`=HK：自排 P 檔閘、手排手煞閘、輸入失效 |
| 6 | `Market Speed Gating` | 025–028 (4) | 5/3 MPH 門檻於市場條件下 —— **PENDING（DR-DD1）** |

### 組 6 之 PENDING 拘束

組名為**市場中立之佔位措辭**。DR-DD1 回覆前：

- **組名不寫入工作簿任何列**
- DR-DD1 裁 HK → 併入組 5（`Hong Kong Market` 成 12 leaf，六組併五組）
- DR-DD1 裁 LATAM → 更名 `LATAM Market`

（下放包 01 §三；A-DD1／DR-DD1 之凍結另使 `-025`~`-028` 不入任何批次。）

### 反模式自查（IN §4.1.3）

- 28 leaf 分 6 組，**平均 4.7 leaf/組**
- 最小組 2 leaf（`Body Off Init`）為**真 outlier** —— 唯一之電源域行為，
  非逐 RD 立組（IN §4.1.3「Too granular」不成立）
- **無** `Misc`／`General`／`Unclassified`（「Too coarse」不成立）
- Decision test：以任一 Test Set 篩選工作簿，得 2–8 條之有意義叢集，
  非 1 條、非全簿

### 修訂途徑（下放包 14 §二）

對 Layer 2 之組名或邊界有實質異議者，**循 framework 修訂提出**，
**不得以 TC 欄位之既成事實變更之**。

---

## Part III — Layer 3（規格章節分組，**不寫入工作簿**）

依 IN §4.1.5：Layer 3 僅存本檔，不入工作簿、不併入 Test Set 名。
用途見 IN §4.1.4（TC 排序／sibling 判定／覆蓋分析／範圍漂移防制）。

座標為 **CFTS022 SYSRA 之 Heading 母號**（上游正式欄逐字值，可驗）：

| Layer 2 | CFTS Heading | 涵蓋 FR |
|---|---|---|
| `Body Off Init`／`Speed Monitoring`／`Lockout Enforcement` | `-110` Driver Distraction Lockout (SR23+) | 113–118 |
| `Lockout Tables` | `-119` Driver Distraction Lockout Tables | 120–121 |
| `Hong Kong Market` | `-123` Hong Kong Market Regulations | 125–129 |
| `Market Speed Gating` | `-130` LATAM Market Regulations（**依 CFTS 結構**；SWE1 內文歸 HK，見 A-DD1）| 132–133 |

### 範圍外之 CFTS 內容

CFTS022 另有 Volume／Personalization 等 **134 條 FR 不屬本 feature**：
SWE1 未分解即不生成（`bed_lowering` R-BLM6 同型之先例）。
惟本案之未分解者明顯屬他 feature 已有工作簿之範圍，**非懸置項，不登 coverage gap**。

`-112`（適用性總則）與 `-136`（Out of scope，Embedded NAV）SWE1 未引 ——
recon 時列覆蓋台帳註記即可。

---

## 變更紀錄

| 日期 | 變更 | 依據 |
|---|---|---|
| 2026-08-28 | **初版落檔**（LOCKED）。Layer 2 六組逐字取經核准之草案 | 下放包 03 §五 Pei 准；下放包 14 §六 T20a |
| 2026-08-28 | 據本檔更正 B1 之 Test Set：`-003`~`-008` `Speed Threshold Judgment` → **`Speed Monitoring`**；`-013`~`-016` `Lockout Enforcement` → **`Lockout Tables`** | 下放包 14 §二 |
```

### 1.2 據其更正 B1 之 Test Set

| leaf | 更正前 | **更正後** | 依據 |
|---|---|---|---|
| `-003`~`-008` | `Speed Threshold Judgment` | **`Speed Monitoring`** | framework Part II 組 2（經核准）|
| `-013`~`-016` | `Lockout Enforcement` | **`Lockout Tables`** | framework Part II 組 4（經核准）|
| `-009`~`-012`（pilot）| `Lockout Enforcement` | 不變 | 組 3，本即相符 |

更正落於**生成器**（`scripts/gen_batch_b1.py`）而非產物之後製，
並於該處註明「**不以 TC 欄位既成事實變更之**」（包 14 §二）。

**未對 `Speed Monitoring` 提出異議** —— 若日後有實質理由，
循 framework 修訂途徑（framework.md Part II 末節已載該拘束）。

### 1.3 ⚠ 落檔註記寫入 framework.md 檔首

本檔遲至本輪始落，**成因在分析層**（包 03 §五 Pei 准，包 04 起未列入任務表）。
該事實已寫入 `framework.md` 檔首之「落檔註記」，並明記
**pilot 4 則與 B1 10 則係在本檔不存在之下產出**。

> 不寫這一行，日後看檔會以為 framework 一直都在，
> 而 14 則 TC 之 Test Set 是照它寫的。**實際順序相反。**

---

## 2. T20e —— `-003` 之 reasoning 更正

**刪去 IN §5.7 之引據**（該條要求「同一 trigger」，而本則有二：raw 129 之上升、
raw 77 之下降 —— 引據確實不成立）。**改依包 14 §3.1**：

> `-003` 之 source `-114` 所命者為「**監看 `$Speedometer$` 以啟閉受限 feature**」
> 之能力，其驗證對象為**規則整體**。**5/3 之雙門檻即遲滯（hysteresis）** ——
> 遲滯之定義為「上行門檻 ≠ 下行門檻」，**任一單邊皆無法承載該性質**；
> 故本則之驗證點為**一**，非二，步驟 2 與步驟 4 合為該單一驗證點之組成，
> 不拆（`split_flag: false`）。
>
> 刻意略過：…個別方向之轉換分由 `-007`（`-116`，上鎖）與 `-005`（`-115`，解鎖）
> 依其各自 source 承載 —— **拆本則即產出與該二者幾近重複之 TC，
> 而 `-114` 所命之遲滯性質反而無人驗**。

**結論未變（不拆），理由已換。**

> 我上一輪引 §5.7 是**引錯條而結論對**。這正是 R-G19 所指之形態
> ——「一個正確的數字配一個未經驗證的理由，其危害大於一個明顯錯誤的數字」。
> 理由會被拿去推論別的事：若 §5.7 之引據成立，則任何「一個能力之多個後果」
> 都可以不拆，**而那不是 §5.7 說的**。

---

## 3. T20b —— 自檢第 1 項改為對 `framework.md` 實際比對

### 3.1 改法

前版之標籤誠實載明其**未**比對 framework（該檔當時不存在）。
本版**讀檔**取 Part II 之 `(Test Set, leaf 範圍)` 集合，逐 TC 驗：

1. `test_set` **∈** framework Layer 2 之集合
2. 該 TC 之 leaf 號**落在該 Test Set 所轄之範圍內**（非只驗名稱存在）
3. 無 Test Group 前綴、無 `Misc`／`Unclassified`／`General`

**檔不存在時直接 FAIL**（而非略過）—— IN §4.1：framework 為 Test Set 之前提。

```python
FW = ROOT / "framework.md"
if not FW.exists():
    add(1, …, False, "**framework.md 不存在** —— IN §4.1：… 須先於 TC 撰寫存在")
else:
    L2 = {}   # 自 Part II 之表列讀 `| # | `Test Set` | 003–008 (6) | …`
    for m in re.finditer(r"^\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(\d{3})[–-](\d{3})", _fw, re.M):
        L2[m.group(1)] = set(range(int(m.group(2)), int(m.group(3)) + 1))
```

實讀結果：**framework Layer 2 共 6 組**
`['Body Off Init', 'Hong Kong Market', 'Lockout Enforcement', 'Lockout Tables',
 'Market Speed Gating', 'Speed Monitoring']`

### 3.2 ⚠ 反向對照 —— 全綠的檢若不能變紅，證明不了什麼

以 `-003`~`-008` 之 `test_set` 注入四種壞值（暫存檔，跑完即刪，正式產物未動）：

| 注入值 | 第 1 項 |
|---|---|
| `Speed Threshold Judgment`（本輪更正前之舊值）| **FAIL** |
| `Body Off Init`（framework 內之他組，leaf 不符）| **FAIL** |
| `Driver Distraction Speed Monitoring`（含 Test Group 前綴）| **FAIL** |
| `Misc` | **FAIL** |

**第 2 種是關鍵**：名稱在 framework 內，只是 leaf 不屬該組。
**只驗「名稱存在」之檢會放行它** —— 而 B1 更正前正是這一型
（`-013`~`-016` 掛 `Lockout Enforcement`，該名確實在 framework 內）。

### 3.3 重跑結果

| 產物 | 檢數 | 結果 | 所用 Test Set |
|---|---|---|---|
| pilot（4 TC）| **24** | **22 PASS ／ 2 N/A ／ 0 FAIL** | `Lockout Enforcement` |
| B1（10 TC）| **24** | **22 PASS ／ 2 N/A ／ 0 FAIL** | `Lockout Tables`／`Speed Monitoring` |

---

## 4. T20c —— Lockout Table 之負向面

### 4.1 量測原始輸出（二母體）

| 母體 | 命中 | 判讀 |
|---|---|---|
| (a) 037 `Analysis Report` `-013`~`-016`，**全 20 欄** | **4** | **皆非負向面** —— `-014`／`-016` 之 `unavailable`／`Exception`，係 AC2 逾時之措辭 |
| (b) CFTS022 `Basic Report` `-119`／`-120`／`-121`，**全 63 欄** | **12** | **`-120`／`-121` 各 6，皆為負向面** |

**即：037 未載，CFTS022 載。**

**CFTS022 `-120` c38（SYS2 驗證標準）逐字**：

```
Features not listed in the table remain accessible and unaffected.
```

**CFTS022 `-121` c38 逐字**：

```
Features not included in the table remain accessible and function normally.
```

**二者 c39（SYS2 驗證方法）逐字**：

```
4. Verify allowed features
   Access features not in the table
   Verify normal operation
```

### 4.2 ⚠ 位階之精確陳述（A-DD2 之教訓）

上述文字位於**驗證標準／驗證方法欄**，**非規範欄**。
規範欄（c3 `Description`）逐字為：

```
The HU shall apply lockout to the features in the The Driver Distraction Lockout Table.
Note:  The Driver Distraction Lockout Table indicates the features which are locked-out
       by the HU for a specific combination of Vehicle Architecture, System, Component and Market.
```

**c3 未明文書出負向面**；其選擇性由 `in the table` 之限縮與該 Note 之
`indicates the features which are locked-out` **隱含支持**。

> 二者合起來：**負向面明載於來源需求自身之驗證欄，隱含於其規範欄。**
> **皆非本層所造** —— 故驗之不違 IN §8.4.2。
> 但 c38／c39 不是 c3，**這一點必須寫清楚**（A-DD2 即因位階混同而生）。

### 4.3 為何仍未補 —— **第三種情形：載而樣本不可定**

下放包 §3.2 給了二個分支（**載**→補；**未載**→登 gap）。實測落在**第三種**：

**行為已知屬上游所有，但補之所需之樣本取不到。** 二個獨立成因：

**成因一 —— p7 只列 `L/O` 側。** 本輪逐列傾印 `Driver Lockout Tables`：

```
16 個 feature 列，Video 欄**全部標 `L/O`**（末列 SXM 360L 全欄為 `Inv.`）
```

**表內無「非 L/O」之列** → 樣本必須來自**表外**，而 p7 不列表外之物。

**成因二 —— CFTS022 之表本體不可機讀。** c3 以

```
(image: 1-_3bc8e108-12c5-4694-a9e9-80b1f915b9af.rtf)
```

參照該表，而該 xlsx **無任何嵌入物件**（實測：`media`／`embed`／`.rtf`／`.emf`
命中 **0**），三個分頁亦無該表之文字列（命中 0）。

**故無從確認任一具名 feature「不在表內」。** 而 profile §2.1 禁泛稱 ——
寫「a feature not listed in the table」即泛稱，具名則須先知道表的內容。
**二條路都通不過，寫下去就是造值（§8.4.1）。**

### 4.4 處置 —— 登 `COVERAGE_GAPS.md` [CG-DD1]

新檔 `features/driver_distraction/COVERAGE_GAPS.md`，登 **[CG-DD1]**，載明：

- 缺口內容、**該行為由誰所有**（CFTS022，逐字引二欄）、位階之精確陳述
- **未涵蓋之成因是「樣本不可定」，非「規格未要求」** —— 二者性質不同：
  **前者登記後可能永遠不必補；後者一旦樣本可得即應補**
- 解除之三條件（甲：表之可機讀版本／乙：分析層指定樣本／丙：上游確認不屬範圍）
- **未登 DR 之理由**：甲案之標的為**素材**，性質同 DR-DD3 之 MCT，
  是否索取屬分析層（不代登）

`-013`／`-015` 之 `reasoning` 已載該面未涵蓋及其理由（機器驗：二則皆含 `CG-DD1`）。

---

## 5. T20d —— `-001`／`-002` 之激勵：三項唯讀查證

### 5.1 (1) CFTS022 全表

**57 格命中**（`Body OFF`／`Sleep`／`wake`／`ignition` 等）。
與 `-001`／`-002` 直接相關者為其 source **`-113`**（r114）：

```
c3  [Description]
    Upon exit from Body OFF HU System Sleep Mode the HU shall initialize
    the "Lock Out State" variable to "Unlocked"
c14 [SYS2 System-SW]
    …shall set the "Lock Out State" variable to "Unlocked" state.
    When HU initialized from Body OFF Mode
c39 [SYS2 驗證方法]
    1. Verify Lock Out State after wake-up
       Put system into System Sleep Mode
       Wake/initialize the HU
       Monitor "Lock Out State" variable
```

**具名識別碼：無。** CFTS022 命名的是一個**模式**
（`Body OFF HU System Sleep Mode`），**不是任何 LID／訊號／PROXI 參數**。

### 5.2 (2) 037 全 28 leaf

**命中 leaf 數 = 2，即 `-001`／`-002` 本身。**
**`-001`／`-002` 以外之列，無一提及該激勵。** 具名識別碼候選：無。

### 5.3 (3) `features/power/`／`features/power_moding/` —— **只回報，不判同一性**

| | 存在 | Body OFF 相關命中 |
|---|---|---|
| `features/power/RULINGS.md` | ✓ | **78** —— 含 `BODY ON`／**`BODY OFF-TIMED`**／`BODY OFF` |
| `features/power/feature.yaml` | ✓ | 0 |
| `features/power/framework.md` | **不存在** | — |
| `features/power_moding/RULINGS.md` | ✓ | 8（`IGN`／`ignition`／`wake`）|
| `docs/runtime/profiles/FW036_R1L_Power_Profile.md` | ✓ | `Sleep`／`Wake` |
| `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` | ✓ | `IGN`／`ignition` |

**該線如何施加電源狀態**（逐字回報，**不作同一性判斷**）：

1. **以具名 status 訊號上報／讀取** —— `power` 之 `R-P5` 逐字：

   ```
   [R-P5] Layer 2 之 `Power State` 與 `Power State Reporting` 合併，
          為單一 Test Set `Power State`，64 leaf。
          Layer 3 隨之合併，含 CFTS009 §1.6.2.1.15
          （`TLM_Status.Info` / `$Telematic_Power$` 訊號上報）。
   ```

2. **status 之值域取自 CFTS009 §1.6.2.1.1–.13**（`power` profile §3.3 逐字）：

   ```
   Full-Operation / Idle / Partial Operation / Stolen Vehicle Mode / Timed /
   Standby / Sleep / Bench / Logistic Idle / Logistic Standby / Logistic Sleep / Init ×2
   ```

   ER 之形態實例（`power` R-P142 所引）：`TLM_Status.Info reads "Standby"`

3. **其他電源事件以 CAN 訊號之十六進位值施加**（`power` profile §3.2 逐字）：

   ```
   STATUS_LIN.PN14_LS_Actv=[1h]、STATUS_LIN.Batt_ST_Crit=[1h]
   ```

**執行層不判斷** CFTS022 之 `Body OFF HU System Sleep Mode` 與
`power` 線之 TLM status `Sleep`／`BODY OFF-TIMED` 是否為同一概念。
**該線之綁定是其對其自身需求所裁**（包 14 §四判準）。
**本輪未讀寫他線任何檔以外之物，未改他線任何檔。**

### 5.4 三項之合判

| 判準（包 14 §四）| 結果 |
|---|---|
| (1)(2) 查得具名識別碼 → 內部可解 | **未查得** —— CFTS022 與 037 皆只給模式名，無識別碼 |
| (3) 查得 → **不得逕用**，須分析層確認同一性 | **查得該線之施加機制**（§5.3），**同一性未判** |
| 三者皆無 → 登 DR（乙式） | **(1)(2) 為無；(3) 為有但不可逕用** |

**故：內部來源已窮盡而未得具名識別碼。**
依 §四，**應登 DR（乙式），文稿由分析層擬**，問二事：
該激勵之具名識別碼為何、台架上如何施加 Body OFF 電源時序與終止 DD process。

**執行層未代擬、未代登。** `-001`／`-002` **維持不入批次**。

> ⚠ 惟 §5.3 之發現使該 DR 之第二問**可能已有內部答案** ——
> 若分析層確認二者為同一概念，`TLM_Status.Info` 即為施加路徑，
> **DR 只剩第一問（識別碼）甚或不必發**。**該確認非執行層可為。**

---

## 6. T-登 —— DR-DD7 文稿整段替換

| 項 | 結果 |
|---|---|
| 舊稿（包 10 §四）| 19 行／1,112 字元 —— **已移除，殘留 0** |
| **新稿（包 14 §五）** | **25 行／1,233 字元 —— 落檔 1 次，逐字** |
| 條目標題 | `-010` 與 `-012` 之 AC2 逐字全等 → **AC2 逐字全等（4 組、11/28 leaf）** |
| 文稿節之註記 | 新增「舊稿只問 `-010`／`-012`…**稿由分析層改**，本輪整段替換」|
| A-DD7 條目 | **維持**（已載 4 組 11 leaf，上繳 09 §5）|

---

## 7. 修訂後之 B1 十則

### newR1L-DD-B001 —— `SWE1-RA-Driver_Distraction-003`（P1／Speed Monitoring）

> 上半：037 Analysis Report r11 c3 (Requirement Description)；`excerpt(Case..Then)`；35/50 token

```json
{
  "tc_id": "newR1L-DD-B001",
  "req_id": "SWE1-RA-Driver_Distraction-003",
  "test_group": "Driver Distraction",
  "test_set": "Speed Monitoring",
  "test_item": "Case [Normal]vehicle speed changes within the valid range\nThen DD Service outputs the restriction state according to the 5/3 MPH rule, and HMI can control the corresponding features based on the state output by DD\n(Both boundaries of the 5/3 MPH rule, exercised in one sequence)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Select \"Reconfigurable menu bar\" and check that it does not open\n3. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 77 (4.8125 km/h)\n4. Select \"Reconfigurable menu bar\" again and check that it opens",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. \"Reconfigurable menu bar\" does not open and the screen stays as it was before the attempt\n3. The vehicle-speed signal is carried on the bus at raw 77, which is 4.8125 km/h [ASSUMPTION A-DD6]\n4. \"Reconfigurable menu bar\" opens and its view is displayed",
  "spec_reference": "CFTS022-4915105",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：037 本列之 `5/3 MPH rule`。其 source `-114` 所命者為「**監看 `$Speedometer$` 以啟閉受限 feature**」之能力，驗證對象為**規則整體**。**5/3 之雙門檻即遲滯（hysteresis）** —— 遲滯之定義為「上行門檻 ≠ 下行門檻」，**任一單邊皆無法承載該性質**；故本則之驗證點為一，非二，步驟 2 與步驟 4 合為該單一驗證點之組成，不拆（`split_flag: false`）。關鍵情境條件：raw 129 與 raw 77 皆取 profile §3.1（R-DD7(c)），標 [ASSUMPTION A-DD6]；取樣 feature 取 \"Reconfigurable menu bar\"（p7 top=356（Menu Bar 列）），非黃標、非 NAV 系。**未取「above 3 MPH」之任意中間值** —— profile §3.1 只給 129 與 77 二個 spec 溯源之格，另擇一值即造值（IN §8.4.1）；raw 129（5.0097 MPH）本身即在 3 MPH 之上，足以起算。刻意略過：BVA 之另一側（raw 128／78）037 未書，不擴入（IN §8.2.1）；個別方向之轉換分由 `-007`（`-116`，上鎖）與 `-005`（`-115`，解鎖）依其各自 source 承載 —— **拆本則即產出與該二者幾近重複之 TC，而 `-114` 所命之遲滯性質反而無人驗**。"
}
```

### newR1L-DD-B002 —— `SWE1-RA-Driver_Distraction-004`（P1／Speed Monitoring）

> 上半：037 Analysis Report r12 c3 (Requirement Description)；`full`；45/50 token

```json
{
  "tc_id": "newR1L-DD-B002",
  "req_id": "SWE1-RA-Driver_Distraction-004",
  "test_group": "Driver Distraction",
  "test_set": "Speed Monitoring",
  "test_item": "AC2:\nWhen DD Service can no longer obtain a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed-input timeout monitoring and fail-safe restriction capability\nCase [Exception]the speed input is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED after the input timeout\n(Fail-safe: the speed message is stopped and the menu-bar view is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Reconfigurable menu bar\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Reconfigurable menu bar\" again and check that it does not open",
  "expected_result": "1. \"Reconfigurable menu bar\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Reconfigurable menu bar\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915105",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Reconfigurable menu bar\"（p7 top=356（Menu Bar 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-114`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B003 —— `SWE1-RA-Driver_Distraction-005`（P1／Speed Monitoring）

> 上半：037 Analysis Report r13 c3 (Requirement Description)；`full`；46/50 token

```json
{
  "tc_id": "newR1L-DD-B003",
  "req_id": "SWE1-RA-Driver_Distraction-005",
  "test_group": "Driver Distraction",
  "test_set": "Speed Monitoring",
  "test_item": "AC1:\nWhen DD Service receives a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed monitoring, restriction-state judgment, and state notification capabilities\nCase [Normal]vehicle speed decreases from above 3 MPH to 3 MPH or below\nThen DD Service sets the Lock Out State to NOT_RESTRICTED\n(Unlock at the 3 MPH boundary, approached from above)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 77 (4.8125 km/h)\n3. Select \"Edit phone book (speller input)\" and check that it opens",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h, above the 3 MPH threshold [ASSUMPTION A-DD6]\n2. The vehicle-speed signal is carried on the bus at raw 77, which is 4.8125 km/h [ASSUMPTION A-DD6]\n3. \"Edit phone book (speller input)\" opens and its view is displayed",
  "spec_reference": "CFTS022-4915106",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：車速自 3 MPH 之上降至 3 MPH 或以下時，受限解除 —— 斷言錨取 profile §2.1 觀察面 A，取樣 feature \"Edit phone book (speller input)\"（p7 top=291（Phone 列））。關鍵情境條件：解鎖側取 raw **77**（4.8125 km/h＝2.9903 MPH），為 profile §3.1 依 R-DD7(c) 所定之 ≤3 MPH 側第一個可表示格，標 [ASSUMPTION A-DD6]。起始值取 raw 129 而非任意「3 MPH 以上」之值 —— 後者無 spec 來源，寫入即造值。一條 TC 即足：037 本列只有一條解鎖路徑。刻意略過：raw 78（不應解）為 BVA 之另一側，037 未書，不擴入（§8.2.1）；037 VC 第 2 項之 `\"Lock Out State\" variable to \"Unlocked\"` 依 profile §2.3 不得入 ER，改以 HMI 之可及性承載。"
}
```

### newR1L-DD-B004 —— `SWE1-RA-Driver_Distraction-006`（P1／Speed Monitoring）

> 上半：037 Analysis Report r14 c3 (Requirement Description)；`full`；45/50 token

```json
{
  "tc_id": "newR1L-DD-B004",
  "req_id": "SWE1-RA-Driver_Distraction-006",
  "test_group": "Driver Distraction",
  "test_set": "Speed Monitoring",
  "test_item": "AC2:\nWhen DD Service can no longer obtain a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed-input timeout monitoring and fail-safe restriction capability\nCase [Exception]the speed input is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED after the input timeout\n(Fail-safe: the speed message is stopped and the phone book is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Edit phone book (speller input)\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Edit phone book (speller input)\" again and check that it does not open",
  "expected_result": "1. \"Edit phone book (speller input)\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Edit phone book (speller input)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915106",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Edit phone book (speller input)\"（p7 top=291（Phone 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-115`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B005 —— `SWE1-RA-Driver_Distraction-007`（P0／Speed Monitoring）

> 上半：037 Analysis Report r15 c3 (Requirement Description)；`full`；46/50 token

```json
{
  "tc_id": "newR1L-DD-B005",
  "req_id": "SWE1-RA-Driver_Distraction-007",
  "test_group": "Driver Distraction",
  "test_set": "Speed Monitoring",
  "test_item": "AC1:\nWhen DD Service receives a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed monitoring, restriction-state judgment, and state notification capabilities\nCase [Normal]vehicle speed increases from below 5 MPH to 5 MPH or above\nThen DD Service sets the Lock Out State to RESTRICTED\n(Lock at the 5 MPH boundary, approached from below)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 77 (4.8125 km/h)\n2. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n3. Select \"DND Customize auto reply message\" and check that it does not open",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 77, which is 4.8125 km/h, below the 5 MPH threshold [ASSUMPTION A-DD6]\n2. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n3. \"DND Customize auto reply message\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915107",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：車速自 5 MPH 之下升至 5 MPH 或以上時，受限生效 —— 斷言錨取 profile §2.1 觀察面 A，取樣 feature \"DND Customize auto reply message\"（p7 top=317（DND 列））。關鍵情境條件：上鎖側取 raw **129**（8.0625 km/h＝5.0097 MPH），為 profile §3.1 之 ≥5 MPH 側第一個可表示格，標 [ASSUMPTION A-DD6]；起始值取 raw 77（2.9903 MPH）—— 其為 profile §3.1 中唯一低於 5 MPH 之 spec 溯源格。一條 TC 即足：037 本列只有一條上鎖路徑。刻意略過：raw 128（不應鎖）037 未書，不擴入（§8.2.1）。"
}
```

### newR1L-DD-B006 —— `SWE1-RA-Driver_Distraction-008`（P1／Speed Monitoring）

> 上半：037 Analysis Report r16 c3 (Requirement Description)；`full`；45/50 token

```json
{
  "tc_id": "newR1L-DD-B006",
  "req_id": "SWE1-RA-Driver_Distraction-008",
  "test_group": "Driver Distraction",
  "test_set": "Speed Monitoring",
  "test_item": "AC2:\nWhen DD Service can no longer obtain a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed-input timeout monitoring and fail-safe restriction capability\nCase [Exception]the speed input is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED after the input timeout\n(Fail-safe: the speed message is stopped and the auto reply editor is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"DND Customize auto reply message\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"DND Customize auto reply message\" again and check that it does not open",
  "expected_result": "1. \"DND Customize auto reply message\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"DND Customize auto reply message\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915107",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"DND Customize auto reply message\"（p7 top=317（DND 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-116`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B007 —— `SWE1-RA-Driver_Distraction-013`（P0／Lockout Tables）

> 上半：037 Analysis Report r21 c3 (Requirement Description)；`excerpt(Case..Then)`；29/50 token

```json
{
  "tc_id": "newR1L-DD-B007",
  "req_id": "SWE1-RA-Driver_Distraction-013",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Tables",
  "test_item": "Case [Normal]HMI has selected the applicable lockout table and judgment Type for the All architecture\nThen DD Service outputs RESTRICTED and HMI locks features marked L/O in the table\n(Lockout of a table entry sampled from the Player row)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Select \"Player Song, artist, title, etc. (speller search)\" and check that it does not open",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. \"Player Song, artist, title, etc. (speller search)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915112",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：受限態下，Lockout Table 標 `L/O` 之 feature 被鎖 —— 取樣 \"Player Song, artist, title, etc. (speller search)\"，所據為 HMI spec p7 top=330（Player 列），**非黃標（黃標三項為 Player / RSE、Messaging、SRT Options，以 PDF 填色實測定位）、非 NAV 系（p7 註記逐字 `Embedded NAV for R1L is applicable to LATAM region only`）**。關鍵情境條件：037 本列之 Method 逐字 `send a speed above 5 MPH`，故取 profile §3.1 之上鎖側 raw 129，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**不逐一遍歷表列全部 feature** —— 037 本列未要求窮舉，以具名單一樣本承載（profile §2.1 禁泛稱，未禁單樣本）；解鎖方向與 BVA 另一側不擴入（§8.2.1）。**負向面（不在表內之 feature 仍可存取）本則未涵蓋** —— 見 `COVERAGE_GAPS.md` [CG-DD1]：該行為明載於 CFTS022 `-120`／`-121` 之驗證標準欄（`Features not listed in the table remain accessible`），**屬上游所有而非本層所造**；惟其樣本須具名一個「不在表內」之 feature，而 HMI spec p7 之 16 列**全部標 L/O**（表內無非 L/O 之列），CFTS022 之表本體又以圖片參照且該 xlsx 無任何嵌入物件（實測 0）——**權威表之內容於綁定來源中不存在，故無從確認任一 feature 不在表內**，具名即造值（§8.4.1）。表可機讀後即應於本則加該斷言（同一 trigger 之另一後果，§5.7）。"
}
```

### newR1L-DD-B008 —— `SWE1-RA-Driver_Distraction-014`（P1／Lockout Tables）

> 上半：037 Analysis Report r22 c3 (Requirement Description)；`full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-B008",
  "req_id": "SWE1-RA-Driver_Distraction-014",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Tables",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and the player search is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Player Song, artist, title, etc. (speller search)\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Player Song, artist, title, etc. (speller search)\" again and check that it does not open",
  "expected_result": "1. \"Player Song, artist, title, etc. (speller search)\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Player Song, artist, title, etc. (speller search)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915112",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Player Song, artist, title, etc. (speller search)\"（p7 top=330（Player 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-120`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B009 —— `SWE1-RA-Driver_Distraction-015`（P0／Lockout Tables）

> 上半：037 Analysis Report r23 c3 (Requirement Description)；`full`；44/50 token

```json
{
  "tc_id": "newR1L-DD-B009",
  "req_id": "SWE1-RA-Driver_Distraction-015",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Tables",
  "test_item": "AC1:\nWhen the signal simulation tool sends vehicle signals that change the Lock Out State to RESTRICTED\nAnd DD Service provides restriction-state judgment and notification, and HMI provides feature lockout\nCase [Normal]DD Service outputs RESTRICTED and HMI locks features marked L/O in the table\n(Lockout of a table entry sampled from the Phone row)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Select \"Pairing (1st time)\" and check that it does not open",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. \"Pairing (1st time)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915115",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：受限態下，Lockout Table 標 `L/O` 之 feature 被鎖 —— 取樣 \"Pairing (1st time)\"，所據為 HMI spec p7 top=304（Phone 列），**非黃標（黃標三項為 Player / RSE、Messaging、SRT Options，以 PDF 填色實測定位）、非 NAV 系（p7 註記逐字 `Embedded NAV for R1L is applicable to LATAM region only`）**。關鍵情境條件：037 本列之 Method 逐字 `send a speed above 5 MPH`，故取 profile §3.1 之上鎖側 raw 129，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**不逐一遍歷表列全部 feature** —— 037 本列未要求窮舉，以具名單一樣本承載（profile §2.1 禁泛稱，未禁單樣本）；解鎖方向與 BVA 另一側不擴入（§8.2.1）。**負向面（不在表內之 feature 仍可存取）本則未涵蓋** —— 見 `COVERAGE_GAPS.md` [CG-DD1]：該行為明載於 CFTS022 `-120`／`-121` 之驗證標準欄（`Features not listed in the table remain accessible`），**屬上游所有而非本層所造**；惟其樣本須具名一個「不在表內」之 feature，而 HMI spec p7 之 16 列**全部標 L/O**（表內無非 L/O 之列），CFTS022 之表本體又以圖片參照且該 xlsx 無任何嵌入物件（實測 0）——**權威表之內容於綁定來源中不存在，故無從確認任一 feature 不在表內**，具名即造值（§8.4.1）。表可機讀後即應於本則加該斷言（同一 trigger 之另一後果，§5.7）。"
}
```

### newR1L-DD-B010 —— `SWE1-RA-Driver_Distraction-016`（P1／Lockout Tables）

> 上半：037 Analysis Report r24 c3 (Requirement Description)；`full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-B010",
  "req_id": "SWE1-RA-Driver_Distraction-016",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Tables",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and pairing is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Pairing (1st time)\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Pairing (1st time)\" again and check that it does not open",
  "expected_result": "1. \"Pairing (1st time)\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Pairing (1st time)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915115",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Pairing (1st time)\"（p7 top=304（Phone 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-121`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

---

## 8. 自檢輸出（機器逐字）

### 8.1 B1（`SC_ARTIFACT=batch_b1.json`）

```
====================================================================================
TC 自檢 —— IN §9 十七項全跑 ＋ 追加項（骨幹；產物由 SC_ARTIFACT 指定）
====================================================================================
[PASS]   1 §4.1/§4.2 + framework.md Test Set ∈ framework.md Layer 2，且與其 leaf 之分組相符；無 Test Group 前綴、無 Misc／Unclassified
         framework Layer 2 共 6 組 ['Body Off Init', 'Hong Kong Market', 'Lockout Enforcement', 'Lockout Tables', 'Market Speed Gating', 'Speed Monitoring']；本產物用 ['Lockout Tables', 'Speed Monitoring']；不符 無；前綴 無；泛稱組 無
[PASS]   2 §4.3.1           test_item 兩段式：上半 verbatim ≤50tok；下半存在且為英文；無 modal
         003: 上半子串 ✓/35tok、下半 有、中文 無、modal 無；004: 上半子串 ✓/45tok、下半 有、中文 無、modal 無；005: 上半子串 ✓/46tok、下半 有、中文 無、modal 無；006: 上半子串 ✓/45tok、下半 有、中文 無、modal 無；007: 上半子串 ✓/46tok、下半 有、中文 無、modal 無；008: 上半子串 ✓/45tok、下半 有、中文 無、modal 無；013: 上半子串 ✓/29tok、下半 有、中文 無、modal 無；014: 上半子串 ✓/47tok、下半 有、中文 無、modal 無；015: 上半子串 ✓/44tok、下半 有、中文 無、modal 無；016: 上半子串 ✓/47tok、下半 有、中文 無、modal 無
[PASS]  2b §4.3.1           同一 Requirement ID 衍生之列，括號下半不逐字相同
         無重複
[PASS]   3 §4.4/§8.5 + R-DD17 Pre-Condition 僅狀態／環境；無系統預設、待測前提、動作、step 可控狀態；訊號源行合 R-DD17 之形式（只書訊號源，不兼述環境）
         0 命中；4 則各 1 項且皆合 R-DD17 之形式（§4.5-1 環境資料）
[PASS]   4 §4.5             Input Test Data 歸屬正確；重複值移入 PC／Procedure 或設 NA
         4 則皆 NA=True；回指 無；跨欄重複 無
[PASS]   5 §5.1/§5.5        步驟無禁用動詞；Final Step 含 ACTION ＋ check target（preferred verb）
         禁用動詞 0 命中；末步缺 `check that` 無
[PASS]   6 §5.2             步驟長度：一般 ≤12 字、Final ≤18 字（含 action+check target）
         字數 {'newR1L-DD-B001': [8, 11, 8, 10], 'newR1L-DD-B002': [7, 11, 12], 'newR1L-DD-B003': [8, 8, 11], 'newR1L-DD-B004': [9, 11, 14], 'newR1L-DD-B005': [8, 8, 13], 'newR1L-DD-B006': [9, 11, 14], 'newR1L-DD-B007': [8, 15], 'newR1L-DD-B008': [11, 11, 16], 'newR1L-DD-B009': [8, 11], 'newR1L-DD-B010': [7, 11, 12]}
[N/A ]   7 §5.3             標準 setup 片語逐字重用
         本 feature 未定義 project-level setup 常數（feature.yaml 無該鍵）—— 無適用對象
[N/A ]   8 §5.4             CLI／tooling 步驟採 description + `$` 指令格式
         4 則皆為 HMI 操作與匯流排施加，無 CLI 步驟
[PASS]   9 §5.6             before／after 需要時建立 baseline
         003: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；004: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；005: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；006: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；007: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；008: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；013: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；014: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；015: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；016: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟
[PASS]  10 §6               Procedure↔ER 1:1；ER 可觀察；ER 無 modal
         步驟 {'newR1L-DD-B001': 4, 'newR1L-DD-B002': 3, 'newR1L-DD-B003': 3, 'newR1L-DD-B004': 3, 'newR1L-DD-B005': 3, 'newR1L-DD-B006': 3, 'newR1L-DD-B007': 2, 'newR1L-DD-B008': 3, 'newR1L-DD-B009': 2, 'newR1L-DD-B010': 3}／ER {'newR1L-DD-B001': 4, 'newR1L-DD-B002': 3, 'newR1L-DD-B003': 3, 'newR1L-DD-B004': 3, 'newR1L-DD-B005': 3, 'newR1L-DD-B006': 3, 'newR1L-DD-B007': 2, 'newR1L-DD-B008': 3, 'newR1L-DD-B009': 2, 'newR1L-DD-B010': 3}；modal 無；非觀察語句 無
[PASS]  11 §7               無 FP／FF：含 setup／transition，不假設隱藏狀態；列舉支援項配負向
         FF：010／012 之 fail-safe 皆先建立正常態再注入故障，未假設隱藏狀態；FP：本 4 leaf 無列舉式支援項（無 format／device／protocol 之列舉），無配對義務
[PASS]  12 §8.1/§8.2/§8.4   追溯 Req/SWRA；不擴入 sibling；無造值；無範圍捏造
         req_id 形制 True；§8.4.2 禁詞 0 命中；數值母體 ['1', '129', '2', '3', '4', '4.8125', '5', '77', '8.0625']，逾 profile §3.1／編號者 無
[PASS]  13 §12              Design Method 於 procedure 定稿後指派，且合 first-match 序
         009/011 觸發為 A→B 狀態轉換，於 Scenario 前命中；010/012 為 simulated fault（停送＋逾時），於 State Transition 前命中；皆為下拉選單實值 True
[PASS]  14 §11 + R-DD11     四欄 numbered item 無作者所書之行尾句號（引號內字串之終端標點保留）
         0 違規
[PASS]  15 §11 + R-DD12(c)  UI 標籤用 `"..."`；方括號僅限 037 逐字之 test_item 上半與 A-DD6 marker
         0 違規；test_item 上半之 `[Normal]`／`[Exception]` 經比對為 037 逐字（R-DD12(a)）；單引號／角括號 無
[PASS]  16 §10.7            spec_reference 列出所驗之每一 spec 節；一行一 ObjectID、無串接
         003=CFTS022-4915105／004=CFTS022-4915105／005=CFTS022-4915106／006=CFTS022-4915106／007=CFTS022-4915107／008=CFTS022-4915107／013=CFTS022-4915112／014=CFTS022-4915112／015=CFTS022-4915115／016=CFTS022-4915115
[PASS]  17 §8.6/§8.7        門檻為 spec 溯源之具體值；相似操作於 ER 具名區辨；來源規格勝於索引匯出
         門檻具名 raw True（profile §3.1 依 R-DD7(c)）；A-DD6 marker True；ER 取樣具名 True
[PASS]   + §11              多行欄位無行首／行尾空白，空行為真空行
         0 違規
[PASS]   + profile §2.3     ER 不含 RESTRICTED／NOT_RESTRICTED／Locked／Unlocked
         0 命中
[PASS]   + §10.2            priority 為 P0–P3 且合 profile §4
         003=P1／004=P1／005=P1／006=P1／007=P0／008=P1／013=P0／014=P1／015=P0／016=P1
[PASS]   + §10.5            test_procedure 至少 2 個編號步驟
         {'newR1L-DD-B001': 4, 'newR1L-DD-B002': 3, 'newR1L-DD-B003': 3, 'newR1L-DD-B004': 3, 'newR1L-DD-B005': 3, 'newR1L-DD-B006': 3, 'newR1L-DD-B007': 2, 'newR1L-DD-B008': 3, 'newR1L-DD-B009': 2, 'newR1L-DD-B010': 3}
[PASS]   + R-DD16(b)        輸出 split_flag／split_reason；未拆者 false／"NA"
         缺鍵 無；值不合 無；鍵名依 R-DD16(a) 用 test_item／spec_reference（既有寫回形制）
[PASS]   + 包 13 §五          ER 不得斷言 128（不應鎖）／78（不應解）之邊界格（037 該列明書者不在此限）；跨越側 129／77 不受限
         0 命中；用及跨越側者 ['003', '005', '007', '013', '015']
====================================================================================
RESULT: PASS 22 ／ N/A 2 ／ FAIL 0　（共 24 檢）
```

### 8.2 pilot 回歸 —— 第 1 項與末行

```
[PASS]   1 §4.1/§4.2 + framework.md Test Set ∈ framework.md Layer 2，且與其 leaf 之分組相符；無 Test Group 前綴、無 Misc／Unclassified
         framework Layer 2 共 6 組 ['Body Off Init', 'Hong Kong Market', 'Lockout Enforcement', 'Lockout Tables', 'Market Speed Gating', 'Speed Monitoring']；本產物用 ['Lockout Enforcement']；不符 無；前綴 無；泛稱組 無
…
====================================================================================
RESULT: PASS 22 ／ N/A 2 ／ FAIL 0　（共 24 檢）
```

---

## 9. 未結 DR 清單（依包 13 §六 級別）

| 級 | DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|---|
| **必發** | **DR-DD1** | DRAFTED（改稿含 SYSAD 引文）| `-025`~`-028`（4）| **凍結** |
| **必發** | **DR-DD5** | DRAFTED | `-017`~`-024`（8）| 不入批次 |
| **必發** | **DR-DD6** | DRAFTED | `-017`~`-024`（8）| 不入批次 |
| 緩發 | DR-DD2 | DRAFTED（格式更正件）| `-021`~`-024`（4）| 不阻斷 |
| 緩發 | DR-DD4 | PARTIALLY ANSWERED／縮為一問 | 9 列書 MPH 者 | 不阻斷 |
| 緩發 | **DR-DD7** | DRAFTED（**本輪整段換新稿**）| **4 組 11 leaf** | 不阻斷 |
| **結案** | ~~DR-DD3~~ | RESOLVED | `-017`~`-028`（12）| 解除 |

**待登（未代登）**：
- `-001`／`-002` 之激勵 DR（乙式，§5.4）—— 內部已窮盡，文稿由分析層擬
- [CG-DD1] 甲案之素材索取 —— 是否立 DR 屬分析層（§4.4）

### 9.1 阻斷疊圖

```
-001 ~ -002  (2)   內部窮盡未得識別碼；應登 DR（乙式），**維持不入批次**
-003 ~ -008  (6)   **B1 已生成**（Test Set = `Speed Monitoring`）
-009 ~ -012  (4)   pilot（Test Set = `Lockout Enforcement`）
-013 ~ -016  (4)   **B1 已生成**（Test Set = `Lockout Tables`）；**[CG-DD1] 負向面未涵蓋**
-017 ~ -024  (8)   DR-DD5 ＋ DR-DD6（+DR-DD2 之 marker 於 021–024）
-025 ~ -028  (4)   僅餘 A-DD1／DR-DD1
```

**已生成 14 TC ／ 28 leaf。** framework 六組中，組 2／3／4 已有產出，
組 1（`Body Off Init`）待 DR，組 5／6 待 DD5／DD6／DD1。

---

## 10. 獨立自評

### 10.1 我做對的

- **自檢加了反向對照。** 第 1 項改完是綠的 —— 但綠不代表它在工作。
  注入四種壞值，四種都變紅才算數。**其中第 2 種（名稱在 framework 內、
  但 leaf 不屬該組）正是 B1 更正前的形態** —— 只驗「名稱存在」的檢會放行它。
- **T20c 沒有硬套二分支。** 下放包給了「載→補／未載→登 gap」，
  實測落在第三種：**載，但樣本不可定**。硬套任一分支都會錯 ——
  套「載」就得造一個樣本，套「未載」就把上游的要求說成不存在。
- **位階寫清楚了。** 負向面在 c38／c39（驗證欄），不在 c3（規範欄）。
  A-DD2 那次就是位階混同才出事，這次先把它標出來。
- **T20d 的 (3) 只回報機制、沒判同一性。** `TLM_Status.Info` 看起來很像答案，
  而且判「是同一概念」會讓 `-001`／`-002` 立刻可做。**但那是 power 線對其自身需求所裁。**

### 10.2 我做糙的

- **上一輪引 IN §5.7 為 `-003` 不拆之依據是引錯條**（該條要求同一 trigger，本則有二）。
  結論對、理由錯 —— 而理由會被拿去推論別的事。**分析層抓到了，我沒有。**
- **cwd 在幾次工具呼叫間掉回 repo root**，同一段腳本重跑了三次才成功。低級。

### 10.3 我拒絕做的

- **不造「不在表內」之樣本**（§4.3）。p7 只有 L/O 側、CFTS022 的表讀不到 ——
  具名即造值，泛稱即違 profile §2.1。
- **不判 Body OFF 與 TLM `Sleep` 之同一性**（§5.3）。
- **不代擬／代登 `-001`／`-002` 之 DR**，也不代登 [CG-DD1] 之素材索取。
- **不改 `Speed Monitoring` 之組名。** 我上一輪取的 `Speed Threshold Judgment`
  其實更貼近那六則在測什麼（門檻判定），但 framework 是經核准的，
  **異議循修訂途徑，不以 TC 欄位既成事實變更之**。

### 10.4 一件我原本會漏的

`framework.md` 落檔後，最省事的做法是**直接改 `batch_b1.json` 的 `test_set` 欄**。
改完自檢一樣全綠。

但那樣**生成器仍會產出舊值** —— 下次重跑 `gen_batch_b1.py` 就打回原形，
而且沒有任何檢會發現，因為產物是對的。
**改在生成器，並在該處寫下「不以 TC 欄位既成事實變更之」**，
才使這個更正是可重現的。

---

## 11. 量測條件揭露（R-G8）

### 11.1 本包所書比率之分子與分母

| 計數 | 分子 | 分母 |
|---|---|---|
| framework Layer 2 六組 | Part II 表列中符合 `\| n \| \`名\` \| 起–迄` 者 | `framework.md` 全文 |
| 反向對照 4/4 變紅 | 注入後第 1 項判為 FAIL 之次數 | 4 種注入值 |
| T20c (a) 4 命中 | 037 `-013`~`-016` 全 20 欄中命中任一正則之格數 | 4 列 × 20 欄 = **80 格** |
| T20c (b) 12 命中 | CFTS022 `-119`／`-120`／`-121` 全欄中命中之格數 | 3 列 × 63 欄 = **189 格** |
| p7 16 列全為 `L/O` | Video 欄為 `L/O` 之 feature 列數 | p7 之 feature 列 17（含末列 `SXM 360L` 全 `Inv.`）|
| CFTS022 嵌入物件 0 | `media`／`embed`／`.rtf`／`.emf`／`.png` 之 zip 條目數 | 該 xlsx 全部 zip 條目 |
| T20d (1) 57 格 | CFTS022 三分頁中命中 8 個關鍵詞任一之格數 | 全表全格 |
| T20d (2) 2 leaf | 命中關鍵詞之 leaf 數 | 037 全 **28** leaf |
| 自檢 22 PASS／2 N/A／0 FAIL | 各判別之檢項數 | **24 檢**（IN §9 十七項 ＋ 追加 7）|

### 11.2 界線

- **T20c 之正則為寬鬆掃描**（19 條，含 `available`／`allow`／`except` 等泛詞），
  **刻意多命中再人讀**。(a) 之 4 命中即為此類偽陽（AC2 之 `unavailable`）。
  **偏寬會多報，不會漏報** —— 與 R-DD15(c) 之「偏嚴」為相反方向，
  因二者所防不同：字數檢怕放過，覆蓋檢怕漏看。
- **framework Layer 2 之解析依表列格式**（`| n | \`名\` | 起–迄 (n) |`）。
  **若日後改版面（如去掉反引號或改用 `~` 為範圍符），解析會靜默得 0 組**
  —— 屆時第 1 項會把**全部** TC 判為「不在 Layer 2」而 FAIL，
  **是紅不是綠**，故不致靜默放行。
- **T20d 之關鍵詞 8 條**（`body off`／`sleep`／`wake`／`cold start`／`power sequence`／
  `power mode`／`IGN`／`ignition`），substring、不分大小寫。
  **若上游以他語彙表述該電源狀態（如 `hibernate`／`S3`），掃不到。**
- **具名識別碼之候選正則 3 條**（`$X$`／`Camel.Signal`／全大寫底線 ≥5 字）。
  **若識別碼為其他形態（如純小寫或帶連字號），會被判為「無」。**
- **他線之查證只讀 3 個檔名**（`RULINGS.md`／`feature.yaml`／`framework.md`）
  ＋ 2 個 profile。**該二線之 `docs/`、`scripts/`、產物皆未讀** ——
  故「該線如何施加」之回報，其嚴格範圍為**該 5 檔之所載**。

### 11.3 檔與開啟方式

| 標的 | 開啟 |
|---|---|
| `framework.md`（新）／`COVERAGE_GAPS.md`（新）| **本輪寫入**（私有路徑）|
| `DATA_REQUESTS.md`／`generated/batch_b1.json`／`scripts/*` | **本輪寫入**（私有路徑）|
| 037／CFTS022／HMI spec p7 | **唯讀** |
| `features/power/*`／`features/power_moding/*` | **唯讀**（§5.3；**未改一字**）|
| `docs/runtime/profiles/*` | **唯讀** |
| `docs/fw036/RULINGS.sha.tsv` | **未開**（T17b 停止）|
| 工作簿 | **未開** |

### 11.4 本輪未量測者

- **`-001`／`-002` 之激勵於四庫中之對應** —— 無識別碼可查（§5.4）。
- **`Body OFF HU System Sleep Mode` 與 power 線 TLM status 之同一性** —— **刻意未判**。
- **Lockout Table 之表外樣本** —— 表不可機讀（§4.3）。
- **`RULINGS.md` 本輪未動**，故錨點數仍為 **19**（上輪已驗）。

---

## 12. 待分析層／Pei

| # | 事項 | 現況 |
|---|---|---|
| 1 | **`-001`／`-002` 之 DR（乙式）** | 內部已窮盡未得識別碼；文稿待分析層擬。§5.3 之發現可能使第二問已有內部答案 |
| 2 | **Body OFF 與 power 線 TLM status 之同一性** | **執行層不判**；確認後 `TLM_Status.Info` 或即施加路徑 |
| 3 | **[CG-DD1] 之解除** | 三案（表之可機讀版本／指定樣本／確認不屬範圍）；是否立 DR 屬分析層 |
| 4 | profile §3 之 PARK_BRK 列回填 | 上繳 10 §9-1，未獲回覆 |
| 5 | profile §3 之 `Country_Code` A-DD5 標記移除 | 上繳 10 §9-2，未獲回覆 |
| 6 | tsv 重生之解除 | T17b 維持停止；本線 **19 列** |
| 7 | 其餘 4 feature 之 `RULINGS.md` 體例 | 未代改 |
| 8 | `-017`~`-028` 之生成 | 待 DD5／DD6／DD1 |
