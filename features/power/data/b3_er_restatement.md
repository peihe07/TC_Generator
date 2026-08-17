# B3 / B4 —— G73 複述判準與 G64 詞彙之經驗導出

> R-P96：G73 之詞彙基礎須有經驗來源，比照 R-P83 / R-P88。
> R-P99(a)：G64 須以 Comfort / Privacy 已交付之 `pre_conditions` 補測。
> 依 **R-P80** 僅用其結構性事實，不引用任何內容裁決。
> 三份皆 `read_only=True`，**未呼叫 `save()`**。
> 產生指令：`python features/power/scripts/build_er_restatement.py`

## 1. 語料

| 來源 | proc 與 ER 皆非空之 TC | 其中 1:1 對齊者 | `pre_conditions` 行數 |
|---|---|---|---|
| Comfort | 461 | **461** | 1798 |
| Privacy | 11 | **11** | 25 |
| **合計** | 472 | **472** | 1823 |

對齊語料共 **1076** 組 (procedure 步驟, ER 行)。

## 2. 重疊率之經驗分佈

`overlap = |ER 實詞 ∩ proc 實詞| / |ER 實詞|`（實詞 = 去停用詞）

| 分位 | overlap |
|---|---|
| P50 | 0.500 |
| P75 | 0.750 |
| P90 | 1.000 |
| P95 | 1.000 |
| P99 | 1.000 |
| 最大 | 1.000 |

- overlap ≥ 0.60 者 **477** 組（44.3%）
- overlap ≥ 0.70 者 **276** 組（25.7%）
- overlap ≥ 0.80 者 **157** 組（14.6%）
- overlap ≥ 0.90 者 **120** 組（11.2%）
- overlap ≥ 1.00 者 **120** 組（11.2%）

### overlap 最高之 12 組（已交付件中最接近複述者）

| 來源 | overlap | procedure 步驟 | ER 行 |
|---|---|---|---|
| Comfort | 1.00 | Turn Sync on | Sync is on |
| Comfort | 1.00 | Set the temperature unit to Celsius | The temperature unit is Celsius |
| Comfort | 1.00 | Set the temperature unit to Fahrenheit | The temperature unit is Fahrenheit |
| Comfort | 1.00 | Turn the driver side AUTO on | The driver side AUTO is on |
| Comfort | 1.00 | Press the RECIRC button until RECIRC is in the Open stat | RECIRC is in the Open state |
| Comfort | 1.00 | Set the temperature to the highest possible position | The temperature is at its highest possible position |
| Comfort | 1.00 | Set the temperature to the lowest position | The temperature is at its lowest position |
| Comfort | 1.00 | Turn SYNC on | SYNC is on |
| Comfort | 1.00 | Turn SYNC on | SYNC is on |
| Comfort | 1.00 | Turn "REAR DEFROST" off from the climate screen and read | The exterior rear-view mirror defrost is off |
| Comfort | 1.00 | Turn "REAR DEFROST" on and read the exterior rear-view m | The exterior rear-view mirror defrost is on |
| Comfort | 1.00 | Read the power button | The power button reads ON |

## 3. 可觀察標的之經驗詞庫

ER 行有而其對應 procedure 步驟無之實詞，共 **288** 個相異詞。

出現 ≥ 5 次者：

| 詞 | 次數 |
|---|---|
| `highlight` | 191 |
| `display` | 159 |
| `show` | 144 |
| `button` | 138 |
| `shown` | 109 |
| `active` | 77 |
| `longer` | 68 |
| `climate` | 51 |
| `pop-up` | 50 |
| `fan` | 43 |
| `off` | 41 |
| `current` | 37 |
| `chang` | 36 |
| `state` | 35 |
| `spe` | 32 |
| `screen` | 32 |
| `set` | 28 |
| `face` | 26 |
| `auto` | 25 |
| `step` | 25 |
| `mode` | 24 |
| `feet` | 23 |
| `one` | 22 |
| `passenger` | 22 |
| `system` | 22 |
| `popup` | 22 |
| `new` | 21 |
| `degree` | 21 |
| `airflow` | 21 |
| `led` | 21 |
| `arrow` | 20 |
| `grey` | 20 |
| `widget` | 20 |
| `temperature` | 19 |
| `hi` | 18 |
| `mod` | 18 |
| `rear` | 17 |
| `front` | 17 |
| `mov` | 17 |
| `remain` | 17 |
| `comfort` | 17 |
| `seat` | 16 |
| `bar` | 16 |
| `only` | 16 |
| `increment` | 15 |
| `unchang` | 15 |
| `doe` | 15 |
| `windshield` | 15 |
| `lo` | 14 |
| `increas` | 14 |
| `half` | 13 |
| `value` | 13 |
| `level` | 13 |
| `sett` | 12 |
| `control` | 11 |
| `statu` | 11 |
| `follow` | 11 |
| `available` | 11 |
| `back` | 11 |
| `down` | 10 |
| `instead` | 10 |
| `def` | 10 |
| `open` | 10 |
| `heat` | 10 |
| `category` | 9 |
| `driver` | 9 |
| `manual` | 9 |
| `select` | 9 |
| `small` | 9 |
| `next` | 9 |
| `eco` | 9 |
| `vent` | 9 |
| `sync` | 8 |
| `change` | 8 |
| `held` | 8 |
| `pop` | 8 |
| `max` | 8 |
| `cushion` | 8 |
| `previou` | 7 |
| `reflect` | 7 |
| `feature` | 7 |
| `awake` | 7 |
| `mtc` | 6 |
| `vehicle` | 6 |
| `move` | 6 |
| `unit` | 6 |
| `above` | 6 |
| `loop` | 6 |
| `hvac` | 6 |
| `toggl` | 6 |
| `tab` | 6 |
| `red` | 6 |
| `lumbar` | 6 |
| `bolster` | 6 |
| `carri` | 6 |
| `side` | 5 |
| `being` | 5 |
| `indicator` | 5 |
| `match` | 5 |
| `switch` | 5 |
| `jump` | 5 |
| `place` | 5 |
| `size` | 5 |
| `press` | 5 |
| `c` | 5 |
| `blank` | 5 |
| `med` | 5 |
| `blue` | 5 |
| `clos` | 5 |

## 4. G64 之經驗量測（R-P99(a)）

| 項目 | 實測 |
|---|---|
| 語料行數（已交付 `pre_conditions`） | **1823** |
| `ENV_STABILITY_RE` 觸發行數 | **0** |
| 偽陽性率 | 0.00% |

### 觸發明細（全列，供判別真偽陽性）

（無觸發）

## 5. 閘門邏輯對已交付語料之實測（R-P99）

| 分支 | 判準 | 觸發 / 1076 | 比率 |
|---|---|---|---|
| tier 1 | 動作述語 ＋ overlap ≥ 0.50 | **69** | 6.4% |
| tier 2 | overlap = 1.00 | **120** | 11.2% |

**該等觸發於已交付件中屬合法之狀態回讀**（§6「prove condition established」），形如
「Select the rear Feet mode → The rear Feet mode is selected」。
**故 G73 全部列為待人工裁決類，不阻斷** —— 比照 R-P76 之 R-P42(b)。

### tier 1 觸發之前 15 例（已交付件）

| 來源 | overlap | procedure 步驟 | ER 行 |
|---|---|---|---|
| Comfort | 0.67 | Turn AUTO on and read the fan speed and the airflow  | The fan speed and the airflow mode are set by the sy |
| Comfort | 0.50 | Change the driver temperature | The passenger temperature changes with the driver te |
| Comfort | 0.50 | Press the temperature down arrow once | The temperature moves down by 1 increment |
| Comfort | 0.50 | Press the temperature slider handle and move it | The temperature slider position moves |
| Comfort | 0.50 | Turn "FRONT DEF" on and read the fan speed | The fan speed is changed by the system |
| Comfort | 1.00 | Read the power button | The power button reads ON |
| Comfort | 0.50 | Read the RECIRC state and its LED | RECIRC is open and its LED is off |
| Comfort | 0.75 | Change the climate setting using a front hard contro | The front climate setting changes |
| Comfort | 0.50 | Change the driver temperature using the driver tempe | The front driver temperature changes |
| Comfort | 0.60 | Set a rear temperature different from the current ca | The rear temperature is set to the requested value |
| Comfort | 0.71 | Read the three rear airflow mode buttons | The three rear airflow mode buttons are turned off |
| Comfort | 0.67 | Change the rear temperature | The rear temperature changes |
| Comfort | 0.75 | Read the button text while the rear climate is unloc | The button reads "LOCK REAR" |
| Comfort | 0.50 | Read the button text | The button reads "UNLOCK REAR" |
| Comfort | 1.00 | Set the rear temperature to a value inside the range | The rear temperature is set to a value inside the ra |

## 6. 對本批十條之真實實測（R-P99(c)：證據為「合成＋真實」）

| 版本 | G73 tier 1 | G73 tier 2 | G74 |
|---|---|---|---|
| 12 包修正後（本包修正前） | **7** | **4** | **2** |
| 13 包再修正後 | **0** | **0** | **0** |
