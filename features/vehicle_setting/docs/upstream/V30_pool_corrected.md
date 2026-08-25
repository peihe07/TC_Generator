# 上繳 V30 —— W-VF70：母體重算、R-VF81 之射程遠大於其設想、DR-34 十分之九為偽陽

對應下放包：`docs/handoff/V30_pool_correction.md`
（7160 bytes，mtime 2026-08-24 12:12:50，sha256 前 16 碼 `aae3ef1473017bc7`）。

**產出**：`vf230_batch01/02/03.json` **重生**，150 條、seq 268–417 不變。
**落檔**：R-VF80／R-VF81／R-VF82、A-VF27／A-VF28、DR-39／DR-40；DR-34 之範圍更正。

**本輪有二項須裁方能續行**，列於 §8。

---

## 1. ⚠ DR-34 之 11 個標的中 **10 個為偽陽**（A-VF27）

`vf230_wvf44_writability.py:proxi_known()` 讀 PROXI 表時寫死 `max_row=800`，
而 `Format` 分頁 **實有 1060 列**。

| DR-34 所列之未解參數 | 實況 |
|---|---|
| `Blindspot_Trailer_Detection` | 列 **810** |
| `Paddle_Shifter_Menu` | 列 **863** |
| `Trailer_Light_Check` | 列 **899** |
| `AUX_Switch_Types` | 列 **911** |
| `INVM_LIN_Module` | 列 **914** |
| `Turn_Signal_Camera_View` | 列 **924** |
| `Parksense_Camera_View` | 列 **925** |
| `Utility_Lighting` | 列 **947** |
| `Digital_CHMSL_Camera_Prsnt` | 列 **991** |
| `FOA_Presence` | 表內逐字名為 **`FOA _Presence`**（名中多一空格） |
| `Greeting_Light` | **表內確無** ← 唯一真陽 |

**修正後**：`W1 28 → 2`、標 `PENDING: DR-34` 之 leaf `28 → 2`，
逐級差異 **W1→W0 26 筆**。

### 1.1 更重的一重：**一個錨點在為它該攔的缺陷背書**

W-VF44 之 PROXI 三錨點中，「必不命中」為 `AUX_Switch_Types`、
「鑑別」之不在表側為 `Blindspot_Trailer_Detection` ——
**二者實皆在表內（列 911／810），其「不在表內」全來自該截斷**。

即該二錨點每輪都通過，而**其通過正是缺陷的產物**。

**已換錨點並具名其理由**：
```
必命中    Heated_Seats             （不變）
必不命中  Greeting_Light           （真正表內所無者，全池僅此一個）
鑑別      Blind_Spot_Monitoring ＋ Blindspot_Trailer_Detection
          —— 改為「二近名參數須**皆**被讀入」，即讀全表之證
正規化    FOA _Presence 須被 pnorm() 吸收
```

**通則（本層之獨立判斷）**：**一個「必不命中」錨點，若其不命中之原因未被獨立確認，
它可能只是在複述缺陷。** 錨點須驗其「不命中」是因資料如此，而非因讀不到。

**同一錯誤本輪犯了兩次** —— 我新寫的 `vf230_wvf70_proxi_values.py`
一開始也複製了 `max_row=800`。

---

## 2. §3／§4 分級重跑與母體算式

`B8-signal-incomplete` **命中 46**；`B9-proxi-value-absent` **命中 0**
（其前提「9 條既無條文值亦無表值」於修好截斷後不成立）。

| | 重跑前 | 重跑後 |
|---|---|---|
| W0 | 592 | **572** |
| W1 | 28 | **2** |
| W2 | 7 | **53** |

逐級差異 **72 筆**：`W0→W2 (B8) 46`／`W1→W0 26`。

**母體算式（逐項可稽，`vf230_wvf69_isolate.py`）**：

```
選池（writability W0+W1）                574
扣 pilot #1／#2                          −20
扣隔離：純 propId 式                      −22
扣隔離：<Name>.Info 式                    −4
扣隔離：事實不足以書寫                     −24
扣隔離：R-VF81 三（未指名值且無語意對應）   −128
**可直接書寫                              376**
```

**與 R-VF80 之 497 之關係**：497 = 「扣 A 類 46 之後、**未扣 R-VF81 三之 128**」之數
（574 − 20 − 57 = 497，本輪曾實得此數）。二者非矛盾 ——
**R-VF81 於 R-VF80 之後施行，其 128 條之隔離使可寫數再降至 376。**
批數 **8 批**（末批 26 條），上繳 3 次。

---

## 3. §5.1／R-VF82：放寬之回收 7、誤收 0，**但另有一個錨點射程外的假陽**

**本輪之放寬**：值之終點改由 **DBC 值域**界定，不再由散文界定。
六錨點（三收三防）全過：

```
✅ 假陰回收  `1st Press`／`Dynamic Gridlines ON`／`Level1`（首版截為 1st／Dynamic／Level）
✅ 假陽之防  `LATCHING and send the signal to IPC within.` → 仍只取 `Latching`
✅ 假陽之防  `Disable` ≠ `Disabled` —— 字義差異不得被吸收
✅ 假陽之防  `Level` 本身非任一標籤 → 不得取 `Level1`
```

C 類 **15 → 8**，回收 7 條，**誤收 0**。

### 3.1 ⚠ 而錨點沒攔到另一個假陽（A-VF28）

首版於值對不上時另加了一條「改取同條文內值域能容納該值之另一訊號」。
實測 `SWE1-VC-TrailerBrakeType032`：

```
條文逐字：TELEMATIC_VEHICLE_SETUP.Trail_Brk_Type_Req signal value as One.
該訊號 DBC 值域：Heavy_Electric／Light_Electric／…（制動型別）
`One` 實屬同條文**後句另一情境**之 Trail_Num_Req（值域 One/Two/…）
```

該機制遂**把條文明寫之訊號偷換掉，產出驗錯訊號之 TC**（4 條）。**已撤回。**

**R-VF82 之錨點攔不到它** —— 錨點驗的是「值之邊界」，換訊號在其射程之外。
**一個放寬可以同時含二種副作用，而錨點只對得上其中一種。**
**其由逐條人讀「回收者」發現**（leaf 名為 `TrailerBrakeType` 而取 `Trail_Num_Req`）。

---

## 4. ⚠ R-VF81 之射程為 **128 條**，而非其所設想之 23 條

依 R-VF81 三，條文未指名值而無語意對應者標 PENDING。**實測命中 128 條**：

| 形態 | 條數 |
|---|---|
| **訊號上行型** | **100** |
| 訊號送出型 | 28 |

**其成因為結構性**：訊號上行型之刺激來自 HW，**顧客不執行任何動作**，
故其條文本就不會有 `chooses to enable/disable` 之動作動詞 ——
**R-VF81 第一款對該形態恆不適用，第三款遂恆成立。**

**其後果**：pilot #2 已核可之 **seq 264（`Susp_Tire_Jack`）與 seq 265
（`Trailer_detection_blind_spot`）正屬此類**。照 R-VF81 字面，該二條須改為 PENDING
—— **即該條回頭否定了兩條已通過覆核之 pilot 條。**

**本輪之處置（具名待裁）**：
- 128 條**列入隔離、不生成**，非生成「全欄 PENDING」之空殼 ——
  一條刺激值與斷言值皆為 PENDING 之 TC，其可執行部分為零，**與未生成不可分辨**。
- **pilot #2 之 seq 264／265 不動**（本層不回頭改動已核可之交付物）。
- 已開 **DR-39** 詢「條文未指名值時該送何值」，並列三個可能之解。

**依本條第一、二款成功取值者：本組 150 條中 0 條** ——
凡有動作動詞之條文，其值多已逐字指名，故第一款實際上無用武之地。

---

## 5. §2 C 類 8 條逐條成因（只判不改）

逐條表：`docs/reports/vf230_wvf70_cclass.md`。

| 成因 | 條數 | 例 |
|---|---|---|
| **(a) DBC 值域拼字** | 1 | `Eng_Off_Pwr_Delay_Req`：條文 `Forty_Five_Sec`／DBC **`Fourty_Five_Sec`** ——`Fourty` 非英文正詞，**DBC 側誤** |
| **(b) 條文誤植** | 7 | `Power_Tailgate_Enable_Req` 條文 `Disable`／DBC `Disabled`（2）；`DRLEnable_Req` 條文 `Early` 而值域為 `False`／`True`，且其動作句自相矛盾「chooses to **disable** … **to Early**」（1）；`Trail_Brk_Type_Req` 條文 `One`～`Four` 而值域為制動型別（4） |
| (c) 本層抽錯 | 7（已修正，不計入） | 值之終點由散文界定；自動換訊號 |

→ **DR-40**。

---

## 6. §5／§6 之三項

**§5 形態→條目對照表**：`docs/reports/vf230_wvf70_form_index.md` ——
每批之形態、條數、seq 區間、建議抽樣條目，另附逐條明細（可摺疊）。

**§6-1 退為條文全文之 1 條已人讀**：`seq 275`（`PowerLiftgate/TailgateAlert-021`）。
**其退為全文為正確** —— 該條文本身無任何管路句，全文即需求句
（「The default value … shall be [On]. When the HMI receives the value [On] via
signal, $IPC_VEHICLE_SETUP.PLGAlert$, the HMI shall display …」）。**非缺陷。**

**§6-2 句界逐條確認**：含實作層名詞之 `test_item` **61 條**（批次內容重生後由 22 增為 61），
**逐句比對條文原文，句界不符者 0／61** ——
即該等名詞皆在條文之原句內，非本層拼接所致。

---

## 7. §7 產出與自檢

| 批 | seq | 形態 | priority | writable |
|---|---|---|---|---|
| `batch01` | 268–317 | PROXI 29／送出 20／上行 1 | P0(a) 29／P0(c) 13／P1 8 | W0 50 |
| `batch02` | 318–367 | PROXI 34／送出 15／上行 1 | P1 50 | W0 48／W1 2 |
| `batch03` | 368–417 | PROXI 27／送出 22／上行 1 | P1 50 | W0 50 |

合計：PROXI 90／送出 57／**上行 3**；leaf 唯一 150/150；Test Set 9 個；
`dr_dependent = DR-34` **2 條**（原 11 條，隨 A-VF27 之修正而降）。

**自檢**：三批 canon 判準 **0／0／0**、增項 10 項 **0／0／0**、
可失效測試 **11/11 各批**。pilot #1／#2 回歸 **0／0**。

**⚠ 一項須具名之涵蓋退步**：訊號上行型由 26 條降為 **3 條**
（100 條入 R-VF81 三之隔離）。**R-VF76 之「涵蓋該批之全部書寫形態」仍成立
（三形態俱在），惟上行型每批僅 1 條，抽樣之代表性極低。**
`設定顯示與修改型` **0 條**（全池僅 4 條，皆在選池序後段）。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有六項，其中二項本層判為須裁方能續行。**

1. **⚠ R-VF81 之射程（§4）。** 128 條隔離、上行型形同停產、且該條與已核可之
   pilot #2 seq 264／265 直接抵觸。**本層不自行調和**，DR-39 已開。
   **在其裁定前，量產之形態涵蓋是偏斜的。**
2. **⚠ 母體之數本輪第三度變動**（574 → 497 → 376）。
   **三次皆因本層之量測而非因資料變動。** 本層判其為 blocking：
   **一個每輪都在變的母體數，其上之批數與排程皆不可信。**
   建議在 DR-37／39／40 有答之前，**不宣告任何批數與完成期**。
3. **`test_item` 之管路句刪除規則已量測二側**：全 150 條共刪去 **454 句**（去重 155 種），
   其起首集中於 `VehicleConfigManager shall communicate` 90／`The response shall` 53／
   `The Vehicle HAL` 52／`CarPropertyManager shall invoke` 51／
   `CarPropertyService shall forward` 51 等。
   **刪去句中含 `shall display／update／show／maintain` 之需求語者：0**
   —— 即無「應留而被刪」。**仍未測者**：`PLUMBING` 之列舉是否漏掉某種管路句
   （「應刪而未刪」），其表徵為 `test_item` 偏長；本輪只驗了保留句為條文逐字。
4. **B 類 11 條（PROXI 無值或無參數名）之處置未定。**
   其中 2 條連參數名都抽不出（條文自句中起，如 `Turn_Signal_Camera_View PROXI
   configuration.`），**本輪只隔離未開 DR** —— 其與 DR-39 之性質不同（PROXI 側）。
5. **A' 類 27 條（抽不出訊號名，含純 propId 22 條）之訊號來源仍待 DR-37。**
6. **`Greeting_Light`（DR-34 唯一真陽）已補查**：**LID 內無**；
   DBC 內有 `GreetingLightsEnable` 與 `GreetingLightsEnable_Req` 二**訊號**
   —— 惟其為訊號而非 PROXI 參數，**二者之對應未經來源證實**。
   受影響之 leaf 為 `SWE1-VC-GreetingLights-008`／`-009`，現判 **W1**。
   **本層不以名近推定其對應**（A-VF28 之教訓：以推測消解不符即為換標的）。
   DR-34 之所詢就此二條仍然成立。
