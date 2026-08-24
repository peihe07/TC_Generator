# 上繳 V26 —— pilot #2 之前置二項完成；**形態為 6 種而非 4 種**，生成待下一步

執行層寫入。依據：`docs/handoff/V26_pilot2_now.md` §5（W-VF64）。
**本包之 sha256 前 16 碼 `0a966bc4f91da349`**（8125 bytes，10:21:58）——
依上繳 V25 §5 第 1 項之建議記之，供下次同名包比對。

**未寫回**（R-VF26）。**未生成量產批次。** pilot #2 之 TC **未生成**，理由見 §5。

---

## 1. W-VF64(1) —— Part 1 之斷言寫法，逐字回報

Part 1 已交付 TC 中含 `TELEMATIC_VEHICLE_SETUP` 之行 **179 行**。逐字實例：

```
procedure  3. Press the right front vented seat icon and check that
              TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is transmitted
ER         3. TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm = 0 (Vented_Seat_Off) is sent
刺激       3. Send CAN: STATUS_CSWM.FR_VS_STATSts = 1 (Vented_seat_low) without
              pressing any icon and check that TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm
              = 1 (Vented_Seat_Low) is transmitted
讀取記錄   2. Press the left front heated seat switch, read
              TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm and record as FL_HS_Tlm_LHD
```

形式為 **`MESSAGE.Signal = <raw> (<Label>) is transmitted／is sent`**，
與 SWC 0708／R-VS52 一致。**既有範例充分，無須回退至 CAN 斷言式，無須自創。**

---

## 2. ⚠ W-VF64(4) —— 逐條讀全文後，**池之形態為 6 種而非 R-VF72 所列之 4 種**

分類判準逐字見 `scripts/vf230_wvf64_classify.py` 之 docstring。621 條之分布：

| 形態 | 條 | R-VF72 二是否列 |
|---|---:|---|
| **訊號送出型** | 318 | ✅（其稱「訊號斷言型」） |
| **PROXI 型** | 168 | ✅ |
| **訊號上行型** | 124 | **❌ 未列** |
| **設定顯示與修改型** | 6 | **❌ 未列** |
| 其他（未歸類） | 4 | — |
| **無可測內容** | 1 | — 見 §4 |
| **狀態轉換型** | **0** | ✅ → **具名「不存在」** |
| **值域切換型** | **0** | ✅ → **具名「不存在」** |

**訊號送出型／訊號上行型之區別須記**：前者為「顧客操作 → HMI **送出**訊號」
（以操作為刺激、斷言訊號）；後者為「HW **送入**訊號 → HMI 更新畫面」
（以訊號為刺激、斷言畫面）。**二者之測試形狀相反**，不可視為同一形態。

### 2.1 我的分類式錯了兩次，皆自查而得

1. **首版要求 `CarPropertyManager.setProperty()` 之連寫**，
   而條文實為「CarPropertyManager shall **invoke** setProperty()」——
   **170 條（27%）落入「其他」**。改以動詞之呼叫式為準。
2. **首版之 ENUM 判準搶在 PROXI 之前**，致雙參數之 PROXI 條文
   （`retrieve the Hybrid_Type and SRT … PROXI configurations`）因其方括號 ≥3
   而誤歸「值域切換型」。改為 **PROXI 先於 ENUM** —— **取得之來源先於值之個數**。
   修正後值域切換型由 1 降為 **0**。

---

## 3. W-VF64(2) —— 分層取樣之十條

**依 R-VF61 二，分層取樣得偏離選池序**（對 R-VS58 之明示例外，僅適用 pilot 批）。
**已扣 pilot #1 之 10 條**（同一 leaf 不得於二 pilot 重複，否則其第二次之通過
不構成新形態之證據）—— 首版未扣，`seq 259` 曾命中 pilot #1 之
`PowerLiftgate/TailgateAlert-016`。

| seq | leaf | 形態 | W | Pri | Test Set |
|---:|---|---|---|---|---|
| 258 | `Blind Spot with Trailer Detection-046` | PROXI 型 | **W1** | P0 | Trailer and Signage |
| 259 | `ParkSense-085` | PROXI 型 | W0 | P0 | Units and Cameras |
| 260 | `PowerLiftgate/TailgateAlert-018` | 訊號送出型 | W0 | P0 | Approach and Tailgate |
| 261 | `IlluminatedApproach-004` | 訊號送出型 | W0 | P1 | Approach and Tailgate |
| 262 | `SWITCH1Type-002` | 訊號送出型 | W0 | P2 | Auxiliary Switches |
| 263 | `BlindSpotAlert-004` | 訊號送出型 | W0 | P0 | Driver Convenience |
| 264 | `SuspensionServiceMode-006` | 訊號上行型 | W0 | P0 | Suspension and Comfort |
| 265 | `Blind Spot with Trailer Detection-049` | 訊號上行型 | W0 | P0 | Trailer and Signage |
| 266 | `Language-059` | 設定顯示與修改型 | W0 | P2 | Driver Convenience |
| 267 | `TimeandDateSettings-002` | 設定顯示與修改型 | W0 | P2 | Units and Cameras |

**各維度之命中數**：

```
形態        訊號送出型 4 ／ 訊號上行型 2 ／ PROXI 型 2 ／ 設定顯示與修改型 2
            狀態轉換型 **不存在** ／ 值域切換型 **不存在**
writability W1 1 ／ W0 9        （池中 W1 僅存於 PROXI 型，故其必自該型出）
Priority    P0 6 ／ P1 1 ／ P2 3
Test Set    6 個，最大 2（上限 2）
```

**R-VF72 二之約束全部滿足。** 二處偏離已具名：增列 `訊號上行型` 2 條與
`設定顯示與修改型` 2 條（本條未列而同屬未檢），取代原擬之
`狀態轉換型`／`值域切換型`（皆不存在）。

---

## 4. A-VF21 —— 一條無可測內容者現判 W0，且在選池內

`E-Save-095` 之條文**全文逐字**為：

> `Note: This is not HMI setting in radio. This is managed in CFTS 088`

**其為委派之註記，非需求** —— 無觸發、無可觀察之結果。
而 `vf230_writability.tsv` 判其 **W0**，且其在 621 之選池內。

**成因**：W-VF44 之分級**無「無可測內容」之判準** —— 其 W2 僅由
`B4-preamble`／`B5-signal-absent`／`B6-value-absent` 三路徑產生，
而 **R-VS71 所定之 W2(a)「條文無可測內容」於 VF230 之實作中從未被檢查**。

**全池掃描**：同型者 **1 條**（即本項）。**本輪未改 `writability.tsv`**
（其須重跑全量），改於**選樣端排除**並具名。

**其亦揭示委派判定之一個缺口**：W-VF46／W-VF50 之比對以
「11 個候選 feature 之 037 有無同名簇」為判，
**而本條之委派標的為 `CFTS 088`，其不在 `features/` 之目錄內** ——
**委派之標的不限於本 repo 之 feature 目錄。**

---

## 5. W-VF64(3) —— **TC 未生成**，理由

本輪之十條橫跨**四種書寫形態**，其中三種為首次書寫：

```
PROXI 型            pilot #1 已定形（v4），可直接沿用
訊號送出型          §1 之 Part 1 實例可依，惟 VF230 之 propId 式
                    （`setProperty() with propId = X and value = [Y]`）
                    與 Part 1 之 `MESSAGE.Signal` 式**不同層** —— 前者為
                    Android 屬性，後者為匯流排訊號。**其對應關係未查**。
訊號上行型          刺激為訊號、斷言為畫面。Part 1 之實例為
                    `Send CAN: … without pressing any icon and check that …`，
                    **其斷言仍為訊號**，非畫面。**畫面斷言之實例未查**。
設定顯示與修改型     Part 1 有無對應實例**未查**。
```

**依 R-VF72 三之精神**（形式須窮盡既有範例，不得自創；查無者回退並具名；
兩者皆無者停手回報），**其所令之查證僅及於訊號斷言型一種** ——
而本輪實有四種。**其餘三種之範例查證尚未做。**

**若逕行書寫，其中三種為自創。** 本層不自創，回報待示。

**建議之次一步**（不自行執行）：對 `訊號上行型`／`設定顯示與修改型`／
`propId` 式，各實測 Part 1 之既有實例並逐字回報，齊備後一次生成十條。

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **「其他」尚餘 4 條未歸類**（分類修正後由 170 降至 4）。其性質未查。

2. **A-VF21 之修法未施行** —— `writability.tsv` 仍判其 W0。
   本輪僅於選樣端排除，**下一次任何以該檔為據之選池仍會取到它**。

3. **`訊號送出型` 318 條之內部可能仍有次形態** ——
   本輪見二式（`propId = X and value = [Y]` 與
   `TELEMATIC_VEHICLE_SETUP.<Sig> signal value as <V>`），
   **其比例未測**。若二式之書寫形態不同，pilot #2 之 4 條未必涵蓋二者。

4. **本輪之分類式已錯二次且皆為自查**（§2.1）。
   **其第三次錯之可能未被排除** —— 現無任何錨點驗證該分類式，
   **R-VF21／R-VF28 所令之三錨點於本分類式未施行**。此為本輪之判準缺口。
