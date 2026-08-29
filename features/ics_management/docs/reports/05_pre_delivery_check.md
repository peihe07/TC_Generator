# 交付前體檢 — b01 ~ b04 全 23 條（2026-08-29）

> 下放包 05 作業 E。**本包不改任何 TC 內容，只出報告。**
> 機械部分（分佈、覆蓋、佔位、錨）由 `scripts/gen_pre_delivery_05.py` 自
> `generated/b0*/b0*_tcs.json` 實測產生；**驗證強度自評與出貨判斷為執行層之判斷**，
> 不偽裝成機械輸出，其判準見 §5／§6 檔頭。

## §1 總數：**23** 條

| 批 | 條數 |
|---|---|
| b01 | 6 |
| b02 | 2 |
| b03 | 8 |
| b04 | 7 |

## §2 Test Set 分佈

| Test Set | 條數 | 對應 RD |
|---|---|---|
| Browse Control | 6 | SWE-ICS-003、SWE-ICS-004 |
| Display Control | 8 | SWE-ICS-006、SWE-ICS-007 |
| Menu Navigation | 1 | SWE-ICS-008 |
| Stuck Button | 5 | SWE-ICS-010 |
| Volume Control | 3 | SWE-ICS-001、SWE-ICS-002 |

## §3 priority 分佈

| priority | 條數 |
|---|---|
| P0 | 11 |
| P1 | 12 |

## §4 trace 覆蓋（SWE-ICS-001 ~ 012）

| RD | TC 數 | Test Set |
|---|---|---|
| SWE-ICS-001 | 2 | Volume Control |
| SWE-ICS-002 | 1 | Volume Control |
| SWE-ICS-003 | 4 | Browse Control |
| SWE-ICS-004 | 2 | Browse Control |
| SWE-ICS-005 | 0 | **無** |
| SWE-ICS-006 | 4 | Display Control |
| SWE-ICS-007 | 4 | Display Control |
| SWE-ICS-008 | 1 | Menu Navigation |
| SWE-ICS-009 | 0 | **無** |
| SWE-ICS-010 | 5 | Stuck Button |
| SWE-ICS-011 | 0 | **無** |
| SWE-ICS-012 | 0 | **無** |

## §5 佔位分佈（`scripts/pending_census.py` 之口徑）

| DR | 佔位處數 | 涉 TC 數 |
|---|---|---|
| DR-ICS4 | 1 | 1 |
| DR-ICS6 | 2 | 2 |
| DR-ICS8 | 12 | 8 |
| DR-ICS10 | 2 | 2 |
| DR-ICS12 | 4 | 4 |
| **合計** | **21** | **16** |

## §6 `specification_reference` 之錨分佈

| 文件 | 條數 | 相異 ObjectID 數 |
|---|---|---|
| CFTS020 | 17 | 14 |
| CFTS022 | 9 | 6 |

## §7 驗證強度自評（**執行層判斷**）

判準 —— **強**：末步之主錨可單獨判定通過與否，且其執行不依賴未解之佔位。
**弱**：主錨依賴未解之佔位，或以「不變／相同」承載，或其斷言之前提未載。

| 批 | tc_title | 強度 | 理由 |
|---|---|---|---|
| b01 | Stuck button held over 120 s | **強** | 主錨為診斷工具上之 DTC B14DA-2A 置位，可單獨判定；訊號名已實名 |
| b01 | Stuck fault held until de-bounced not-pressed | **強** | 主錨為 DTC 清除，可單獨判定 |
| b01 | Button held exactly 120 s | **強** | 主錨為 DTC 未置位，可單獨判定 |
| b01 | VOLUME knob rotated clock-wise | **弱** | ER 斷言 "VOLUME POP_UP" 顯示，而其顯示條件四包追索仍查無（A-ICS16／DR-ICS4）—— 若該 popup 僅特定條件出現，該行即為潛在 FF |
| b01 | VOLUME knob rotated counter clock-wise | **弱** | 同上 |
| b01 | Three detents rotated clock-wise | **弱** | 同上，另有 DR-ICS4／DR-ICS12 二處佔位落於 pre_conditions |
| b02 | Press ignored during stuck condition | **弱** | 門檻 `<Tstuck_button>` 於 TC 內仍為 DR-ICS10 佔位（**值已於 `CFTS020-4819541` 逐字查得 `120 sec`，b05 未回填 —— A-ICS34 交 b06**）；主錨另以「狀態不變」承載 |
| b02 | Button responsive after release | **弱** | 門檻同上（`4819541` 載 `120 sec`，未回填）；主錨為「狀態改變」雖可判，但觸發步驟於 TC 內仍為佔位 |
| b03 | Power hardkey pressed while HU screen on | **強** | b05 作業 A 後主錨為 HMI 現象（螢幕暗），可單獨判定；TGW 佔位僅及於輔助觀察行 |
| b03 | Power hardkey pressed at Telematic Power full operation | **強** | 同上 |
| b03 | Power hardkey pressed while HU screen off | **強** | 主錨為前一畫面之回復，可單獨判定 |
| b03 | Power hardkey pressed at Telematic Power idle | **強** | 同上 |
| b03 | Screen off hardkey starts the three second timer | **強** | 主錨為 "TOUCH SCREEN TO TURN ON" 之持續顯示，可單獨判定 |
| b03 | Screen off hardkey pressed again within three seconds | **強** | 主錨為前一畫面之回復，可單獨判定 |
| b03 | Three second period completed after screen off hardkey | **強** | 主錨為螢幕轉暗，可單獨判定 |
| b03 | Screen off hardkey pressed while HU screen off | **強** | 主錨為前一畫面之回復，可單獨判定 |
| b04 | Knob 2 rotated clock-wise | **弱** | 訊號已實名且主錨可判，但觀察時點依 `<TPeriodToSendNoChange>`（DR-ICS12 佔位）。**`4819541` 逐字載其為 `20 msec`**，遠小於本條所用之 2 秒觀察點 —— 即該觀察點**實際上是安全的**，然值未回填前不得如此宣稱 |
| b04 | Knob 2 rotated counter clock-wise | **弱** | 同上（`20 msec` < 2 秒，觀察點實際安全，惟未回填） |
| b04 | Knob 2 held stationary | **弱** | 末步以「畫面不變」承載條文之 `ignored by the receiving components` —— 「不做事」無直接訊號面可觀察 |
| b04 | Knob 2 no change sent periodically | **強** | 末步為再次轉動後 `$CLIMATIC_PANEL.Radio_Knob2_DIR$` = 1 (Knob_increment)，訊號已實名且可單獨判定 |
| b04 | Three detents counted in one rotation | **弱** | `= 3` 之正確性繫於 detent 計數窗（DR-ICS12 佔位）。**`4819541` 載 `initial value 50 msec` 且明標待 parameter tuning 優化** —— 即該值本身為暫定，回填後仍須注意其非定值 |
| b04 | Knob 2 signals acted on by the HU | **弱** | 末步之預期行為為 DR-ICS6 佔位 —— **主錨本身依賴未解之 DR** |
| b04 | Enter button pressed | **弱** | 末步之目標畫面為 DR-ICS6 佔位 —— **主錨本身依賴未解之 DR** |

**強 12 條／弱 11 條**。

## §8 出貨判斷 —— 假設上游 17 條 DR **全部無回覆**（**執行層判斷**）

| 批 | tc_title | 可否現狀出貨 | 理由 |
|---|---|---|---|
| b01 | Stuck button held over 120 s | 可 | 無佔位；DTC 號與 120 s／8 ms 皆自 DTCs Matrix r57 逐字取得 |
| b01 | Stuck fault held until de-bounced not-pressed | 可 | 同上 |
| b01 | Button held exactly 120 s | 可 | 同上 |
| b01 | VOLUME knob rotated clock-wise | **不可** | 無佔位而仍不可 —— 其 ER 有 2 行斷言 popup 顯示，顯示條件未載即為潛在 FF（IN §7）。**無佔位不等於可出貨** |
| b01 | VOLUME knob rotated counter clock-wise | **不可** | 同上 |
| b01 | Three detents rotated clock-wise | **不可** | 同上，另有二處佔位 |
| b02 | Press ignored during stuck condition | **不可** | 步驟 3 之門檻於 TC 內為佔位，照現狀交付台架無從執行。**理由已更正**：非「無值」（`4819541` 載 `120 sec`），而是「值查得而未回填」——回填屬 b06 |
| b02 | Button responsive after release | **不可** | 同上（值查得而未回填） |
| b03 | Power hardkey pressed while HU screen on | 可 | R-ICS22(b) 明裁「不因 (a) 之佔位而阻出貨」；主錨為 HMI 現象，佔位僅及輔助行。**出貨時該輔助行應標明未解** |
| b03 | Power hardkey pressed at Telematic Power full operation | 可 | 同上 |
| b03 | Power hardkey pressed while HU screen off | 可 | 同上 |
| b03 | Power hardkey pressed at Telematic Power idle | 可 | 同上 |
| b03 | Screen off hardkey starts the three second timer | 可 | 同上；3 秒為 4819572 逐字之 spec 值 |
| b03 | Screen off hardkey pressed again within three seconds | 可 | 同上 |
| b03 | Three second period completed after screen off hardkey | 可 | 同上 |
| b03 | Screen off hardkey pressed while HU screen off | 可 | 同上 |
| b04 | Knob 2 rotated clock-wise | **不可** | TC 內帶未回填之佔位。**惟其風險已知為低**：`4819541` 之 `20 msec` 遠小於 2 秒觀察點，回填後本條預期即可出貨 |
| b04 | Knob 2 rotated counter clock-wise | **不可** | 同上 |
| b04 | Knob 2 held stationary | 可（弱） | 無佔位，可執行；但其主錨為「不變」，通過不足以證成條文，**出貨時應標為弱驗證** |
| b04 | Knob 2 no change sent periodically | 可 | 無佔位，訊號實名，主錨可單獨判定 |
| b04 | Three detents counted in one rotation | **不可** | 計數窗於 TC 內為佔位；`4819541` 之 `50 msec` 為 **initial value 且待調校**，回填後仍非定值 |
| b04 | Knob 2 signals acted on by the HU | **不可** | 主錨即佔位 |
| b04 | Enter button pressed | **不可** | 主錨即佔位 |

**可出貨 13 條／不可 10 條**。

