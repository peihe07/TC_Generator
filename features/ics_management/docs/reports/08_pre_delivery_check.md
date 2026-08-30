# 交付前體檢 v3 — b01 ~ b06 全 31 條（2026-08-29）

> 下放包 08 作業 E，依 **R-ICS32(c)** 之二層式常設項。
> **取代 `07_pre_delivery_check.md`**（舊報告與其產生器皆保留不刪）。
> 候選篩之掃描條件、載具詞表與人工複核之例外表，**全部寫在 `scripts/gen_pre_delivery_08.py` 檔頭與常數區**，可逐行覆核。

## §1 第一層 —— 候選篩（機械，每包必跑）

- ER 行總數 **144**
- **原始命中 140 行**（未涵蓋實詞 ≥ 1）
- 衍生載具詞 **18** 個（跨 ≥ 5 條 TC，自動導出）：
  `baseline`、`button`、`climatic`、`completed`、`differs`、`enters`、`felt`、`increment`、`mode`、`mute`、`panel`、`radio`、`remains`、`rotation`、`screen`、`shown`、`statsts`、`telematic`
- **殘餘候選 68 行** —— 此為人工複核之實際對象

**殘餘率 47%**（基線 53%，R-ICS34(c)：連續三包 > 60% 須重議門檻）。

> **R-ICS34(d)：篩之命中率不得作為品質指標。** 上列原始命中數與殘餘數**量的是篩自身之噪音**，不是 TC 之品質；篩只產候選，未錨定之認定仍為人工（§2）。原始命中率之所以仍列出，是為使門檻之效果可量（R-ICS34(b)：二數必並報，不得以分層掩蓋原始噪音）。

### 殘餘候選（逐行）

| 批 | tc_title | ER 行 | 殘餘實詞 |
|---|---|---|---|
| b01 | Stuck button held over 120 s | 2 | `more` |
| b01 | Stuck button held over 120 s | 3 | `head`、`unit` |
| b01 | Stuck button held over 120 s | 4 | `periodically` |
| b01 | Stuck fault held until de-bounced not-pressed | 1 | `more`、`seconds` |
| b01 | Stuck fault held until de-bounced not-pressed | 2 | `status` |
| b01 | Stuck fault held until de-bounced not-pressed | 4 | `returns` |
| b01 | Stuck fault held until de-bounced not-pressed | 5 | `elapsed`、`mature`、`time` |
| b01 | Button held exactly 120 s | 1 | `status` |
| b01 | Button held exactly 120 s | 3 | `returns` |
| b01 | VOLUME knob rotated clock-wise | 1 | `displayed` |
| b01 | VOLUME knob rotated clock-wise | 3 | `displayed` |
| b01 | VOLUME knob rotated clock-wise | 4 | `above` |
| b01 | VOLUME knob rotated counter clock-wise | 1 | `displayed` |
| b01 | VOLUME knob rotated counter clock-wise | 3 | `displayed` |
| b01 | VOLUME knob rotated counter clock-wise | 4 | `below` |
| b01 | Three detents rotated clock-wise | 1 | `displayed` |
| b01 | Three detents rotated clock-wise | 3 | `displayed` |
| b01 | Three detents rotated clock-wise | 4 | `above`、`levels` |
| b02 | Press ignored during stuck condition | 2 | `after` |
| b02 | Press ignored during stuck condition | 3 | `beyond`、`stuck`、`timeout` |
| b02 | Press ignored during stuck condition | 5 | `same` |
| b02 | Button responsive after release | 1 | `beyond`、`stuck`、`timeout` |
| b02 | Button responsive after release | 2 | `returns` |
| b02 | Button responsive after release | 4 | `after`、`release` |
| b02 | Button responsive after release | 5 | `changes` |
| b03 | Power hardkey pressed while HU screen on | 2 | `pressed` |
| b03 | Power hardkey pressed while HU screen on | 3 | `pressed` |
| b03 | Power hardkey pressed while HU screen on | 6 | `content`、`dark`、`shows` |
| b03 | Power hardkey pressed at Telematic Power full operation | 2 | `pressed` |
| b03 | Power hardkey pressed at Telematic Power full operation | 3 | `pressed` |
| b03 | Power hardkey pressed at Telematic Power full operation | 6 | `content`、`dark`、`shows` |
| b03 | Power hardkey pressed while HU screen off | 2 | `previously` |
| b03 | Power hardkey pressed while HU screen off | 6 | `again` |
| b03 | Power hardkey pressed at Telematic Power idle | 1 | `previously` |
| b03 | Power hardkey pressed at Telematic Power idle | 5 | `again` |
| b03 | Screen off hardkey starts the three second timer | 3 | `graphic` |
| b03 | Screen off hardkey starts the three second timer | 4 | `graphic` |
| b03 | Screen off hardkey starts the three second timer | 5 | `dark`、`graphic`、`still` |
| b03 | Screen off hardkey pressed again within three seconds | 1 | `currently` |
| b03 | Screen off hardkey pressed again within three seconds | 2 | `graphic` |
| b03 | Screen off hardkey pressed again within three seconds | 3 | `graphic`、`removed` |
| b03 | Screen off hardkey pressed again within three seconds | 4 | `display` |
| b03 | Screen off hardkey pressed again within three seconds | 5 | `again` |
| b03 | Three second period completed after screen off hardkey | 1 | `graphic`、`touch`、`turn` |
| b03 | Three second period completed after screen off hardkey | 2 | `black`、`elapses`、`turns` |
| b03 | Three second period completed after screen off hardkey | 5 | `content`、`dark`、`shows` |
| b03 | Screen off hardkey pressed while HU screen off | 1 | `previously` |
| b03 | Screen off hardkey pressed while HU screen off | 5 | `again` |
| b04 | Knob 2 held stationary | 4 | `content`、`unchanged` |
| b04 | Knob 2 no change sent periodically | 3 | `carrying`、`constant`、`cycle`、`frames`、`time` |
| b04 | Knob 2 signals acted on by the HU | 2 | `detent` |
| b05 | Knob 2 rotated on a scrollable screen | 2 | `detent` |
| b05 | Knob 2 rotated on a tuner source | 1 | `current` |
| b05 | Knob 2 rotated on a tuner source | 2 | `detent` |
| b06 | Mute hardkey pressed while audio unmuted | 1 | `unmuted` |
| b06 | Mute hardkey pressed while audio muted | 1 | `muted` |
| b07 | Back button pressed | 2 | `pressed` |
| b07 | Back button pressed | 3 | `pressed` |
| b07 | Two ICS buttons pressed at the same time | 2 | `power` |
| b07 | Two ICS buttons pressed at the same time | 3 | `power`、`while` |
| b07 | Button event change reported within Tbutton | 1 | `pressed` |
| b07 | Button event change reported within Tbutton | 2 | `carrying`、`pressed`、`timestamp` |
| b07 | Button event change reported within Tbutton | 3 | `between`、`interval`、`more`、`msec` |
| b07 | Button event change reported within Tbutton | 4 | `pressed`、`returns` |
| b07 | Button event change reported within Tbutton | 5 | `after`、`carrying`、`more`、`msec`、`pressed` |
| b07 | Knob 1 status sent on BH-CAN | 1 | `change` |
| b07 | Knob 1 status sent on BH-CAN | 2 | `detent` |
| b07 | Knob 1 status sent on BH-CAN | 4 | `message`、`same` |

## §2 第二層 —— 人工複核（每包必做）

| 批 | tc_title | ER 行 | 判 | 理由 |
|---|---|---|---|---|
| b01 | VOLUME knob rotated clock-wise | 1 | 已標明 | A-ICS16 |
| b01 | VOLUME knob rotated clock-wise | 3 | 已標明 | A-ICS16 |
| b01 | VOLUME knob rotated counter clock-wise | 1 | 已標明 | A-ICS16 |
| b01 | VOLUME knob rotated counter clock-wise | 3 | 已標明 | A-ICS16 |
| b01 | Three detents rotated clock-wise | 1 | 已標明 | A-ICS16 |
| b01 | Three detents rotated clock-wise | 3 | 已標明 | A-ICS16 |
| b02 | Press ignored during stuck condition | 5 | **未錨定（弱驗證）** | 來源句 4819617 為 `the HU shall ignore the press request`；本行以「狀態不變」承載。R-ICS32(a)：保留，標**弱驗證**。 |
| b02 | Button responsive after release | 5 | **未錨定（弱驗證）** | 來源句只說「恢復處理」，未載恢復後必產生可見變化。R-ICS32(a)：保留，標**弱驗證**。 |
| b04 | Knob 2 held stationary | 4 | **未錨定（弱驗證）** | 來源句 4819582 為 `no action taken on the value`；本行以「畫面內容不變」承載一個**不可觀察之不作為**。R-ICS32(a)：保留，標**弱驗證**。 |
| b04 | Knob 2 signals acted on by the HU | 4 | 已錨（b08 改寫後） | 作業 C 已將佔位移至 Pre-Condition，`if any` 之否定分支由前提排除，差異斷言方為有據 |
| b04 | Enter button pressed | 4 | 已錨（b08 改寫後） | 作業 C 已將佔位移至 Pre-Condition，`if any` 之否定分支由前提排除，差異斷言方為有據 |
| b05 | Knob 2 rotated on a scrollable screen | 4 | 已錨（b08 改寫後） | 作業 C 已將佔位移至 Pre-Condition，`if any` 之否定分支由前提排除，差異斷言方為有據 |
| b05 | Knob 2 rotated on a tuner source | 4 | 已錨（b08 改寫後） | 作業 C 已將佔位移至 Pre-Condition，`if any` 之否定分支由前提排除，差異斷言方為有據 |
| b07 | Back button pressed | 4 | 已錨（b08 改寫後） | 作業 C 已將佔位移至 Pre-Condition，`if any` 之否定分支由前提排除，差異斷言方為有據 |

**未錨定 3 行**（b07 為 7 行；作業 C 已解 4 行、作業 D 標弱驗證 3 行）；已標明（A-ICS16）6 行。

## §3 Test Set／priority／trace 覆蓋

| Test Set | 條數 |
|---|---|
| Browse Control | 8 |
| Display Control | 10 |
| Menu Navigation | 2 |
| Stuck Button | 5 |
| Volume Control | 6 |

| priority | 條數 |
|---|---|
| P0 | 14 |
| P1 | 17 |

| RD | TC 數 |
|---|---|
| SWE-ICS-001 | 3 |
| SWE-ICS-002 | 1 |
| SWE-ICS-003 | 4 |
| SWE-ICS-004 | 4 |
| SWE-ICS-005 | 2 |
| SWE-ICS-006 | 5 |
| SWE-ICS-007 | 5 |
| SWE-ICS-008 | 1 |
| SWE-ICS-009 | 1 |
| SWE-ICS-010 | 5 |
| SWE-ICS-011 | **0** |
| SWE-ICS-012 | **0** |

## §4 佔位分佈

| DR | 佔位處數 | 涉 TC 數 |
|---|---|---|
| DR-ICS4 | 1 | 1 |
| DR-ICS6 | 5 | 5 |
| **合計** | **6** | |
