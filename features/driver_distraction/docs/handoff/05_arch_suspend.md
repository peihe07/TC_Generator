# 下放包 05 —— T9 審結、分析層二誤自認、profile §3 停用、Q7/Q8 待裁、T10、DR-DD3

- 日期：2026-08-27
- 方向：分析層 → 執行層（T10、T-登）＋ Pei（Q7、Q8 待裁）
- 前一包：`04_priority_profile.md`；對應上繳：`docs/upstream/03_signal_binding.md`
- **pilot 暫不開** —— profile §3 前三列已 SUSPENDED，解除前不得撰寫 TC

---

## 一、上繳包 03 審查判定 —— 收，且 profile §3 之三列錯誤全屬分析層

執行層之三列不符逐項成立。**二誤分屬不同家族，分開記，不合併成一句「抄錯」。**

### 1.1 誤一 —— 轉抄時刪去限定詞（verbatim 降級）

上繳包 01 T6 之原始輸出本已載分頁名（`Proxi & Configuration r421`、
`Proxi & Configuration r43`）。分析層寫 profile §3 時壓縮為
「LID r421」「LID r43」，**刪去唯一能消歧之限定詞**。

LID 具二分頁（`CAN Mapping`／`Proxi & Configuration`），同號不同列：
`r43` 於前者為 `ACV_FailType`、於後者才是 `Country_Code`。
**來源正確，精度於轉抄時遺失。**

拘束（隨本包生效，全 feature 適用）：**凡引 LID 之列號，一律書
`LID {分頁名} r{n}`，不得只書 `LID r{n}`。** 既有 profile 依 T10 回填時一併補齊。

### 1.2 誤二 —— 未量測即斷言施加路徑（full-claim 家族）

T6 明載五訊號於 DBC 皆 0 命中，分析層判為「預期狀態（`$…$` 為邏輯識別碼）」
—— 該判**正確**。錯在其後一步：自 LID r1738／r1397 取 **Powernet 欄**之名
寫成 `Send the signal $GW_C1.VEH_SPEED$`，**未回驗該名是否存在於綁定之二 DBC**。

實測：155 + 323 個訊息中無 `GW_C1`／`VehCfg7`。**照 profile 寫的步驟施加不出來。**

此誤之危害形態值得記：它不會在生成時報錯，會在 **pilot 執行台架時**才炸，
且炸起來像 TC 的錯而非 profile 的錯。

### 1.3 執行層之查法記入案例

執行層係「照 profile 查 → 查不到 → 回頭驗 profile」。
**若改以「找得到就好」直接於 DBC 撈速度訊號，會命中
`VehicleSpeedVSOSig` 並逕填，二誤永久隱形。**
「回頭驗上游指示」與「達成本步目標」在此分岔，前者為正。

### 1.4 A-DD2 —— 證據變強而處置不變，正確

候選對應於二 DBC 皆查得，`VAL_ 0 "OFF" 1 "ON"` 與 CFTS022 之 `[ON]`／`[OFF]`
逐字相合。**證據強度不改變位階問題**（規範欄 vs 註記欄、`-129` 未更正）。
維持保留 `$PARK_BRK_EGD$`，DR-DD2 續開。

---

## 二、A-DD4（新立）—— 共用路徑之寫入歸屬

`docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md` 檔首出現
一行**非分析層所寫**之落檔註記，且其所述之「ENOENT 後重寫」對該檔不成立
（該情形發生於下放包 04，非 profile）。

**Pei 2026-08-27 告知：三個 feature session 平行進行中。**

- 事實：分析層送出之稿與磁碟內容差一行；`features/driver_distraction/docs/handoff/` 無競包
- **成因未量測，不臆斷寫入者**
- 已於 profile 檔首更正該行（保留痕跡，非刪除；R-TM13 精神）

### 處置拘束（隨本包生效）

`features/{slug}/` 為該線私有，撞寫風險低；
**`docs/runtime/`、`docs/fw036/`、`forms/`、`scripts/` 為共用路徑**，
三線皆可觸及。於共用路徑之寫入：

1. **一律 `edit_file` 局部改，不得整檔 `write_file` 覆寫** —— 覆寫會湮滅他線之字
2. 改動前 `read_multiple_files` 回讀現況，改動後回讀驗 diff
3. 發現非本線所寫之內容：**保留並註記**，不刪除、不逕改其語意

狀態：OPEN（成因未明；拘束已生效，不待成因查明）。

---

## 三、待 Pei 裁

### Q7 —— 架構選定（**pilot 之前置**）

綁定之二 DBC（`PDT27_E2A_R4_BHCAN`／`PDT27_E2A_R5_FDCAN8`）為 **ATLANTIS 側**；
LID r1738 為多架構對照表，Powernet 欄與 ATLANTIS 欄並列。

**提案**：profile §3 全面改採 **ATLANTIS 欄**之訊號名
（速度側實測為 `STATUS_CCAN3.VehicleSpeedVSOSig`，13 bit、factor 0.0625、Km/h），
`$VC_Trans_Equipped$`／`$PresentGear$` 之 ATLANTIS 名由 T10 量得後回填。

執行層拒絕自行改用 ATLANTIS 名為正確 —— 架構選定屬裁定，非量測。

### Q8 —— 5／3 MPH 之 raw 邊界不落於整數格

分析層先更正執行層之一項定性：**`1 MPH = 1.609344 km/h` 為單位定義，
屬 IN §8.4.1 之 domain constant，非造值**，換算本身可為。
但換算之結果暴露真問題（依實測 factor 0.0625）：

| spec 門檻 | km/h | raw |
|---|---|---|
| 5 MPH | 8.04672 | **128.7475** |
| 3 MPH | 4.828032 | **77.2485** |

**二門檻皆不落於整數 raw** —— 「transitions to equal or greater than 5MPH」
於此匯流排上不存在「等於」之格。

**選項**：
- （甲）取跨越側之最近整數（5 MPH → raw 129；3 MPH → raw 77），
  TC 內具名該 raw 並註明其對應之 km/h 實值；BVA 之 limit±1 依此定義
- （乙）登 DR 問上游「門檻之判定單位為 MPH 或 km/h、邊界取整規則為何」
- （丙）甲乙並行：先依甲生成並標 assumption marker，DR 回覆後回修

分析層傾向（丙），但**不逕定** —— 取整規則影響全部速度類 leaf 之 ER 數值。

---

## 四、DR-DD3（標的為具名檔，非問句）

- **標的**：`CIP Market Configuration Table v*.xlsx`（最新版）
- **指名來源**：LID `Proxi & Configuration` r43 c7 逐字
  `See latest version of 'CIP Market Configuration Table v*.xlsx'`
- **由來**：T9b —— LID 之 Country_Code 值表**無 Hong Kong**，
  且其自陳為部分列舉（`See Country Code Table`）
- **阻斷**：`Country_Code` 之值寫不出 → HK 全段（leaf 017–028）之
  Pre-Condition 缺值

**⚠ 與 DR-DD1 為二個獨立阻斷，不可互抵**（執行層所指，成立）：
DR-DD1 裁 HK 只定「市場為何」，**仍不給出 `Country_Code` 之值**。
即使 DR-DD1 先回，HK 段仍卡於 DR-DD3。二者須分別追。

執行層：`DATA_REQUESTS.md` 建 DR-DD3 條目（狀態 DRAFTED），
並於 DR-DD1 條目加註「與 DR-DD3 為獨立阻斷，不互抵」。

---

## 五、任務（T10；Q7/Q8 裁定不阻本輪量測）

| # | 任務 |
|---|---|
| T10a | LID r1738（`$Speedometer$`）**逐欄全傾印**：所有架構欄之欄名與值，標明何欄為 Powernet、何欄為 ATLANTIS，不做選擇 |
| T10b | 同法傾印 `$VC_Trans_Equipped$`（`Proxi & Configuration` r420 **與** r421 兩列全欄）與 `$PresentGear$`（`CAN Mapping` r1397）—— **r420／r421 何者為準由分析層裁，執行層只給兩列全貌** |
| T10c | 對二 DBC 查 T10a／T10b 所列各架構名之存在性：逐名輸出「在／不在」與其 `BO_` 歸屬、bit 長、factor／offset／unit、`VAL_` 列舉逐字。**含 ATLANTIS 側之 `STATUS_CCAN3.VehicleSpeedVSOSig` 與檔速類、檔位類候選** |
| T10d | LID 二分頁之 `Country_Code`（`CAN Mapping` r43 與 `Proxi & Configuration` r43）兩列全欄傾印，供誤一之更正回填 |
| T-登 | A-DD4 登入 `ANOMALIES.md`（§二 逐字）；DR-DD3 建檔（§四）；DR-DD1 加註不互抵 |

**不在本輪**：改 profile §3（待 Q7）、任何 TC、pilot、寫回、git。

## 六、上繳包要求（`docs/upstream/04_arch_binding.md`）

T10a–d 原始輸出、T-登 結果、未結 DR 清單（DD1/DD2/DD3）、獨立自評、
量測條件揭露（R-G8）。
