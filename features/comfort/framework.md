# FW036 Comfort HMI — Framework Part N

- Layer 1 Test Group：**`Comfort`**（R-C6）
- Layer 2 Test Set：**15 組**，見 §2
- Layer 3：spec section，**不入工作簿**（§4.1.5）
- 依據：下放包 `docs/handoff/12_partN_final.md`（Pei 簽署 2026-08-14），
  取代 `11_partN_draft.md` §2 之草案表；11 之 §1／§3／§5／§6 仍有效
- 驗算：`scripts/verify_partn.py`（四個 assertion，見 §5）
- 母體：**403 leaves ／ 129 sections**（`data/layer3_map.tsv`）

---

## 1. 三層之定義與去向

| Layer | 值 | 進工作簿？ |
|---|---|---|
| 1 Test Group | `Comfort` | ✅ G 欄 |
| 2 Test Set | 15 組之一（§2） | ✅ H 欄 |
| 3 spec section | outline 節次（如 `2.3.1`） | ❌ **不入** |

**Layer 3 不入工作簿之意義（§4.1.5）**，兩件事都禁止：

1. 不得存入工作簿任何欄位作為 Layer 3 之欄值。
2. 不得串接進 Test Set 名稱（不寫 `Climate Modes 2.3`）。

section 與 TC 之關聯另有去處 —— `specification_reference`（N 欄）依 §10.7
以 `{spec_filename}_{section_id}` 形式承載，其查表為
`data/spec_id_to_outline.tsv`。**那是 traceability 欄位，不是 Layer 3 欄位。**

Test Set → section 之對照存於 `data/test_set_map.tsv`（129 列），
供 Phase 4 查用，同樣不是工作簿內容。

---

## 2. Layer 2 —— 15 個 Test Set

| # | Test Set | Layer 3（spec sections） | leaves | 佔比 |
|---|---|---|---|---|
| 1 | `Front Climate Anatomy` | 2.1, 2.2, 6.3 | 12 | 3.0% |
| 2 | `Climate Modes` | 2.3, 2.3.1, 2.4, 2.5, 2.5.1, 2.10, 2.11, 2.13, 2.14, 2.16 | 41 | 10.2% |
| 3 | `Temperature and Fan` | 2.6, 2.6.1, 2.7, 2.7.1 | 17 | 4.2% |
| 4 | `Airflow and Defrost` | 2.8, 2.9, 2.12, 2.12.1, 2.12.2, 2.15 | 23 | 5.7% |
| 5 | `Tri-Mode Climate` | 3.1 ~ 3.4 | 14 | 3.5% |
| 6 | `Rear Climate` | 7.1 ~ 7.10, 9.1 ~ 9.4.1 | 46 | 11.4% |
| 7 | `ECO HVAC` | 10.1 ~ 10.9.1 | 15 | 3.7% |
| 8 | `Heated Vented Seats` | 11.1 ~ 11.11.1, 12.1 ~ 12.9 | 59 | 14.6% |
| 9 | `Seat Control Tab` | 13.2 ~ 13.6 | 14 | 3.5% |
| 10 | `Climate Popups` | 14.1 ~ 14.19, 15.1 | 42 | 10.4% |
| 11 | `ICS Anatomy` | 16.2, 16.16 | 14 | 3.5% |
| 12 | `ICS Climate Modes` | 16.3, 16.4, 16.5, 16.10, 16.11, 16.13, 16.14, 16.17 | 40 | 9.9% |
| 13 | `ICS Temperature and Fan` | 16.6, 16.6.1, 16.7 | 16 | 4.0% |
| 14 | `ICS Airflow and Defrost` | 16.8, 16.9, 16.12, 16.12.1, 16.15 | 29 | 7.2% |
| 15 | `Home Screen Widget` | 17.1 ~ 17.5, 18.1 | 21 | 5.2% |

**合計 403 leaves ／ 129 sections。** 區間 12–59，最大者佔 **14.6%**。

§2 之範圍寫法（`7.2 ~ 7.10` 等）於 `scripts/verify_partn.py` 內展開為明列
節次；展開錯誤會在該腳本之第一個 assertion 失敗，不會靜默改變分組。
逐節明細見 §6。

---

## 3. 分組判準

### 3.1 一體適用之測試（12 §1）

> **該組是否隱含共用之 setup pattern 與 UI 進入路徑？**

| 案例 | 判定 | 理由 |
|---|---|---|
| ICS（ch16）vs 觸控面（ch2） | **分立** | 車輛須為 EMEA ICS 變體，操作走實體控制堆疊；setup 與進入路徑皆不同 |
| ch12 carryover vs ch11 | **合併** | 同畫面、同控制，僅座椅等級（Multi-Level／Single-Level／Standard）與 program baseline 不同 |

設備等級為能力**之內**之變體軸（§8.3 sibling axis），非不同進入路徑。
依 §4.2「Prefer broader shared capability when unsure」→ 合併。

此判準使 ICS 之分立與 ch11／ch12 之合併互相一致 —— 兩者依同一條測試得出
相反結論，因為它們在該測試上的事實不同。

### 3.1.1 ch11／ch12 合併 —— 全文複核後維持（2026-08-15）

12 §1 之合併結論原係讀 `layer3_map.tsv` 之 60 字截斷標題得出，13 §3 自承
該依據違反 R-C18，要求以全文複核。**複核完成，合併維持不變。**

**分析層裁定**：兩章為**同一進入路徑**；`opens popup` 是**輸出回饋**，
不是入口。

執行層所供之事實（上繳 07 §4、08 §3），供本判定之依據：

| 事實 | 內容 |
|---|---|
| 唯一實質差異 | `opens popup and` 一個片語，ch11 有、ch12 無（11.1/12.1、11.2/12.2 各一處）。其餘為標點與一處錯字 |
| 操作元件 | 兩章**逐字相同**：`a press of the heated/vented seat button`，且以 `the soft button` 指涉同一物 |
| 顯示位置 | 兩章**逐字相同**：按鈕變色、顯示 arrows／fan 與 LED |
| 其餘 18 節之元件掃描 | **無任何一節以實體鍵、旋鈕、ICS 或觸控面為操作元件**。`hard control` 僅 2 處且皆為**組態條件**（決定是否顯示軟鍵），非操作方式 |
| 標籤配對 | 5 個 `HVS*` 標籤跨兩章重複，其中 `HVS4`（11.3↔12.4）與 `HVS5`（11.4↔12.5）**逐位元組相同** |

**合併之效力**：`Heated Vented Seats`（59 leaves）維持單一 Test Set。
近似重複落於同一組，Phase 4 之 sibling 判定（§4.6）與 `duplicate_of` 得以
見效 —— 分立則兩者分屬兩組，審閱者看不到彼此。

**Phase 4 之注意**：`opens popup` 既為回饋而非入口，ch11 之該兩節與 ch12
對應節之差異應以**預期結果**（是否出現 popup）表達，不得寫成不同的操作
步驟或前置條件。

### 3.2 章 2 與章 16 刻意鏡像

| 概念 | 觸控面 | ICS |
|---|---|---|
| anatomy | #1 `Front Climate Anatomy` | #11 `ICS Anatomy` |
| 模式開關 | #2 `Climate Modes` | #12 `ICS Climate Modes` |
| 溫度與風量 | #3 `Temperature and Fan` | #13 `ICS Temperature and Fan` |
| 氣流與除霜 | #4 `Airflow and Defrost` | #14 `ICS Airflow and Defrost` |

使審閱者在兩面之間移動時面對同一組概念邊界（§4.1.4）。

**11 §1 已裁定不做章 2／16 之逐條等價覆核**：兩章不合併，故該覆核不在關鍵
路徑上；鏡像即使個別條文對不齊也不失效。若日後改採合併型切法，該覆核才
成為前置，屆時屬 Tier 2。

### 3.3 命名（11 §4.3，Pei 已簽）

Title Case、不展開縮寫（`ICS`、`ECO HVAC` 保留原文）、無標點。
`Heated Vented Seats` 不寫 `Heated/Vented Seats` —— 斜線在欄值中易生比對歧義。

`ICS` 前綴不違反 §4.2：該條禁的是重複 Test Group（`Comfort`），而 `ICS`
是 UI 進入路徑之限定詞，正是 §4.2 所要的標記。

**#15 之更名（13 §2，2026-08-15）**：原簽署名為 `Comfort Widget`，
已更名為 **`Home Screen Widget`**。

執行層原主張該名非 Layer 1 前綴，理由是 spec 自身稱該元件為 "the Comfort
widget"（17.1／18.1：`W0.) The Comfort widget will have two screens`）。
**分析層裁定更名**：§4.2 之範例為 Test Group = `Bluetooth` 時用
`Connection`／`Pairing` 而非 `Bluetooth Pairing`；spec 同樣稱該功能為
"Bluetooth pairing"，§4.2 禁的正是這個形態。直接類推即得本組應為
`Home Screen Widget`。

Layer 3 不變（17.1 ~ 17.5、18.1），leaves 仍 21。更名後**無任何 Test Set
以 `Comfort` 起首**，`verify_partn.py` 之第四項回報應為空；若非空即為未同步。

### 3.4 章 6（1 leaf）併入 #1 而非自成一組

單一 leaf 自成 Test Set 會使 Test Set 欄淪為 TC ID 之副本（§4.1.3「過細」）。
其落位之查證見 §4。

---

## 4. 6.3 之落位查證（12 §3 指示）

12 §3 將 `6.3` 暫置 `Front Climate Anatomy`，並指出分析層僅憑 60 字截斷判斷，
「non-foldable second row」語意偏後座，要求執行層讀全文確認。

**全文（`spec-index/cache/` SR24 export，`Basic Report`，outline 6.3）**：

> CM1.) When a vehicle is configured with a **non-foldable secondary lower
> screen** that contains comfort information, the comfort section will be
> removed from the head unit except for comfort popups.

**確認落位，維持 `Front Climate Anatomy`。** 理由二：

1. **前提有誤，且誤在截斷處。** 原文是 "non-foldable **secondary lower
   screen**"（次要下方螢幕），不是 "second row"（後座）。60 字截斷恰好切在
   `...non-foldable secon` —— `secondary` 被腰斬成看似 `second`。此條與後座
   無關，不屬 `Rear Climate`。
2. **其內容是 anatomy**：規定在特定配置下 comfort section 是否出現於 head
   unit。#1 之另兩節同型 —— 2.1 規定 comfort category 有幾個分頁、2.2 規定
   硬鍵變更如何反映；6.3 規定整個 section 在不在。三者皆為「有什麼、在哪裡」。

**不屬 `Seat Control Tab`**：該組為 13.2 ~ 13.6，主題是座椅控制分頁之內容；
6.3 不涉座椅。**不屬 `Climate Popups`**：`except for comfort popups` 是例外
子句，非主詞。

Phase 4 之注意事項：6.3 與 13.1（`assumption`，未被 037 引用）及 Home Screen
`HSD13`（outline 4.11）同指「lower screen 存在時移除 comfort 呈現」之家族。
13.1 與 HSD13 皆不在本 Part N 之母體內（前者未被引用、後者屬 Home Screen
spec，R-C17），但撰寫 6.3 之 TC 時應併看，以免前置條件互相矛盾。

---

## 5. 驗算（`scripts/verify_partn.py`）

期望值 —— 15 組之 section 清單、各組 leaf 數、逐章分布 —— **全部寫死於腳本**，
取自下放包 12 §2 與上繳 01 §3，不由 `layer3_map.tsv` 回推。自己導出的期望值
不可能失敗。

```
- PASS — each Test Set's leaf_count matches handoff 12 §2:
    expected `all 15 equal`, measured `all 15 equal`
- PASS — Test Set leaf totals sum to 403: expected 403, measured 403
- PASS — all 129 mapped sections assigned: expected 129, measured 129
    — unassigned: none; not in layer3_map: none
- PASS — no section assigned to two Test Sets: expected {}, measured {}
- PASS — per-chapter round-trip (ch2==92, ch16==99, +12 others):
    expected `all 14 chapters equal`, measured `all 14 chapters equal`
    — 2:92、3:14、6:1、7:38、9:8、10:15、11:37、12:22、13:14、14:40、
      15:2、16:99、17:18、18:3
- PASS — Test Set names: no Misc/General/Unclassified, no stray whitespace,
    no duplicates: expected [], measured [] — 15 names checked
- PASS — no Test Set name starts with the Test Group word (§4.2):
    expected [], measured [] — 15 names checked against prefix 'Comfort'
```

Part N 已簽署，故此處失敗**不代表分組該調整**，而代表轉錄或 Layer 3 map
有誤 —— 腳本之離開訊息即如此措辭。

---

## 6. Layer 3 對照表 —— 逐 Test Set 之 section 明細

129 節，與 §2 之範圍寫法等價。機讀版本：`data/test_set_map.tsv`。
**再次提醒：本表不入工作簿**（§4.1.5）。

### 1. `Front Climate Anatomy` — 3 sections / 12 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `2.1` | R1C1.) The comfort category will have up to 4 tabs depending | 3 |
| `2.2` | C1.) Whenever changes to the climate system are made via har | 8 |
| `6.3` | CM1.) When a vehicle is configured with a non-foldable secon | 1 |

### 2. `Climate Modes` — 10 sections / 41 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `2.3` | C2.) AUTO has on/ off state. The fan speed indicator shows A | 9 |
| `2.3.1` | C2.1) Some vehicles with dual zone climate with dual airflow | 2 |
| `2.4` | C3.) AC has on/ off state. Auto can automatically turn on AC | 4 |
| `2.5` | C4.) Recirc has on/ off state. RECIRC is not available in ce | 4 |
| `2.5.1` | C4.1) Some vehicles have a configuration for a 3 state toggl | 2 |
| `2.10` | C11.) Climate off has on/off state that is indicated on HC,  | 6 |
| `2.11` | C12.) SYNC has on/ off state that is indicated on climate sc | 5 |
| `2.13` | C14.) MAX A/C screens/popups are to be used when CCM relays  | 3 |
| `2.14` | C15.) MTC screens/popups are to be used when CCM relays MTC  | 4 |
| `2.16` | C18.) If blower reduction occurs automatically due to an act | 2 |

### 3. `Temperature and Fan` — 4 sections / 17 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `2.6` | C5.) Temperature ranges: LO, 60-84, HI (English), LO, 16-28, | 5 |
| `2.6.1` | C5.1) If SYNC is ON, adjusting driver temperature affects pa | 6 |
| `2.7` | C6.) Fan ranges: Off, 1-7, 15h (denoting to show AUTO instea | 5 |
| `2.7.1` | C6.1) In some vehicles fan speed ranges for front hvac are:  | 1 |

### 4. `Airflow and Defrost` — 6 sections / 23 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `2.8` | C7.) Defrost has on/ off state. Defrost can automatically tu | 6 |
| `2.9` | C8.) Rear Defrost has on/ off state. REAR DEFROST is not ava | 4 |
| `2.12` | C13.) There are 4 Airflow Mode displayed in this order (1) F | 3 |
| `2.12.1` | C13.0) In some non-tri mode equipment types, airflow modes h | 2 |
| `2.12.2` | C13.1) If the Mode hard control is pressed the user will be  | 6 |
| `2.15` | C16.) EXTERIOR REAR-VIEW MIRROR DEFROST has on/ off state. E | 2 |

### 5. `Tri-Mode Climate` — 4 sections / 14 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `3.1` | C19) Tri-Mode Climate: On vehicles with Tri-Mode climate, th | 3 |
| `3.2` | C20.) MAX DEFROST: On vehicles with MAX DEF, MAX DEF replace | 8 |
| `3.3` | C21.) MAX DEF and REAR DEF are available during climate off. | 2 |
| `3.4` | C22.) For soft top vehicles such as JL/JT, when configured,  | 1 |

### 6. `Rear Climate` — 16 sections / 46 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `7.1` | CR1.) Hard controls do not switch to controlling the rear cl | 3 |
| `7.1.1` | CR1.1) Rear hard controls changes will not provide popups on | 3 |
| `7.2` | CR2.) Rear AUTO has on/ off state. The fan speed indicator s | 5 |
| `7.3` | CR3.) LOCK REAR has on/ off state. Rear lock will lockout th | 3 |
| `7.4` | CR4.) Temperature ranges: LO, 60-84, HI. The status is indic | 4 |
| `7.5` | CR5.) Fan ranges: Off, 1-7, 15h (denoting to show AUTO inste | 4 |
| `7.6` | CR6.) Rear climate off has on/off state that is indicated on | 5 |
| `7.7` | CR7.) SYNC has on/ off state that is indicated on climate sc | 3 |
| `7.8` | CR8.) The Rear Airflow Modes has 3 states: 1) Feet, 2) Face  | 5 |
| `7.9` | CR9.) AC has on/ off state. | 1 |
| `7.10` | CR10.) 4 Zone Climate includes two temperature zones in the  | 2 |
| `9.1` | CR11.) On some vehicles (See CFTS043 for details), there are | 1 |
| `9.2` | CR12.) Alternative fan speed pop up: in these variants, when | 2 |
| `9.3` | C12.1.) The pop up will have text labels, «Front» for front  | 1 |
| `9.4` | CR13.) Alternative Status Bar Dropdown: in these variants, t | 3 |
| `9.4.1` | CR13.1.) The button label will read «Rear». | 1 |

### 7. `ECO HVAC` — 10 sections / 15 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `10.1` | EH1.) ECO HVAC is an HVAC Mode, used on EV Vehicles only, to | 2 |
| `10.2` | EH2.) For BEV vehicles, the AUTO functionality can have 3 st | 1 |
| `10.3` | EH3.) Button label will read AUTO ECO. | 1 |
| `10.4` | EH4.) When the AUTO function is off and available, the user  | 1 |
| `10.5` | EH5.) The second press will switch to AUTO on. A third press | 3 |
| `10.6` | EH6.) When AUTO ECO is on, deselect airflow modes as in stan | 2 |
| `10.7` | EH7.) HVAC AUTO shall keep the selected setting through igni | 1 |
| `10.8` | EH8.) The Comfort main Menu Bar icon shall reflect the AUTO  | 1 |
| `10.9` | EH9.) The comfort pop ups triggered by hard controls interac | 1 |
| `10.9.1` | EH9.1) When ECO HVAC is equipped on a vehicle, the AUTO pop  | 2 |

### 8. `Heated Vented Seats` — 22 sections / 59 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `11.1` | HVS1. For Multi-Level Heated/Vented seats, a press of the he | 4 |
| `11.2` | HVS2. For Multi-Level Heated/Vented seats, a press of the ve | 4 |
| `11.3` | HVS4. When climate is OFF, the status bar should still show  | 1 |
| `11.4` | HVS5. Heated seats buttons when activated will be shown red. | 2 |
| `11.5` | HVS6. Refer to HMI Settings List for the details on the Auto | 1 |
| `11.6` | R1HVS1.) If the independent seat zone feature is available,  | 6 |
| `11.6.1` | R1HVS1.1) On vehicles that are equipped with the seat zone f | 2 |
| `11.7` | R1HVS1.2.) For independent seat zones soft control, when the | 4 |
| `11.8` | W1HVS2.) For Multi-Level Heated steering wheel, a press of t | 4 |
| `11.9` | R1HVS2.) For Single-Level heated steering wheel, a press of  | 2 |
| `11.10` | R1HVS3.) Heated/vented seat, heated wheel, and seat zone pop | 3 |
| `11.11` | R1HVS4.) Heated/vented seat, heated wheel will not be displa | 3 |
| `11.11.1` | R1HS4.1.) When comfort controls are not active, they will be | 1 |
| `12.1` | HVS1. For Multi-Level Heated/Vented seats a press of the hea | 4 |
| `12.2` | HVS2. For Multi-Level Heated/Vented seats a press of the ven | 4 |
| `12.3` | HVS3. Active button state text/icon color is white. Inactive | 2 |
| `12.4` | HVS4. When climate is OFF, the status bar should still show  | 1 |
| `12.5` | HVS5. Heated seats buttons when activated will be shown red. | 2 |
| `12.6` | HVS6. Refer to HMI Notes for the details on the Auto Comfort | 1 |
| `12.7` | HVS7. Whenever pop ups are shown, images should be shown in  | 2 |
| `12.8` | SHVS1. For Standard Heated/Vented seats a press of the heate | 3 |
| `12.9` | SHVS2. For Standard Heated/Vented seats a press of the vente | 3 |

### 9. `Seat Control Tab` — 7 sections / 14 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `13.2` | LS1.) When the (-, +) seat control buttons are pressed from  | 3 |
| `13.2.1` | LS1.1) The 4 types of adjustments the user will be able to a | 1 |
| `13.3` | LS2.) When the (-, +) seat control buttons are pressed, it w | 2 |
| `13.3.1` | LS2.1) The user last selected lumbar/bolster selection will  | 2 |
| `13.4` | LS3.) The user will be able to long press on the hard button | 2 |
| `13.5` | LS4.) A short press of the (-, +) button will increase the l | 2 |
| `13.6` | LS5.) Once the minimum or maximum level has been reach, the  | 2 |

### 10. `Climate Popups` — 23 sections / 42 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `14.1` | HVACP1.) HVAC pop-ups should follow the pop-up list. | 1 |
| `14.1.1` | HVACP1.2) If there is an HVAC pop-up displayed (e.g. fan pop | 1 |
| `14.2` | HVACP2.) HVAC pop-ups are not displayed while RVC screen is  | 1 |
| `14.3` | HVACP3.1) HVAC popups will be interactive (e.g. Temp popups, | 2 |
| `14.4` | HVACP4.) If head unit is in simulated off/idle mode and HVAC | 2 |
| `14.5` | HVACP5.) HVAC pop-ups should display over NAV, 3rd Party App | 1 |
| `14.6` | HVACP6.) When an HVAC popup is displayed over another popup, | 1 |
| `14.7` | HVACP7.) When an HVAC popup is displayed over another popup, | 2 |
| `14.8` | HVACP8.) When an HVAC popup is displayed over another popup, | 1 |
| `14.9` | HVACP9.) HVAC popups will not be displayed during intro/outr | 1 |
| `14.10` | HVACP10.) When head unit is in simulated off/idle mode HVAC  | 1 |
| `14.10.1` | HVACP10.1) If Climate is located in the main category bar, f | 1 |
| `14.11` | HVACP11.) HVAC pop ups will only be displayed based on direc | 2 |
| `14.12` | HVACP12.) The style of HVAC popups should match the type of  | 3 |
| `14.13` | HVACP13.) For vehicles with a lower hvac screen, interaction | 1 |
| `14.14` | HVACP14.) For vehicles with dual zone climate versions with  | 1 |
| `14.15` | HVACSB1.) Available comfort controls (driver/passenger heate | 1 |
| `14.16` | HVACSB2.) Driver and Passenger comfort seat features will sh | 3 |
| `14.16.1` | HVACSB2.1.) Seat zone will show currently active or last use | 3 |
| `14.17` | HVACSB3.) Driver comfort seat feature and Passenger comfort  | 1 |
| `14.18` | HVACSB5.) Popup will have a 5 sec timeout and restart with a | 2 |
| `14.19` | HVACSB6.) When the Climate widget is shown on the currently  | 8 |
| `15.1` | HVACP11.1) For different Climate features (Defrost/Max Defro | 2 |

### 11. `ICS Anatomy` — 2 sections / 14 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `16.2` | ICE1.) Whenever changes to the climate system are made via h | 9 |
| `16.16` | ICE15.) Always show 'Driver' or 'Passenger'. Off icon of sea | 5 |

### 12. `ICS Climate Modes` — 8 sections / 40 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `16.3` | ICE2.) AUTO has on/ off state. The fan speed indicator shows | 9 |
| `16.4` | ICE3.) MAX A/C, A/C, RECIRC, MAX DEF, and REAR DEFROST have  | 1 |
| `16.5` | ICE4.) The recirc icon will display the vehicle model specif | 2 |
| `16.10` | ICE9.) Climate off has on/off state that is indicated on HC, | 8 |
| `16.11` | ICE10.) SYNC has on/ off state that is indicated on climate  | 4 |
| `16.13` | ICE12.) If the system supports Max A/C it will be displayed  | 12 |
| `16.14` | ICE13.) MTC screens/popups are to be used when CCM relays MT | 3 |
| `16.17` | C16.) If blower reduction occurs automatically due to an act | 1 |

### 13. `ICS Temperature and Fan` — 3 sections / 16 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `16.6` | ICE5.) Temperature ranges: LO, 60-84, HI (English), LO, 16-2 | 6 |
| `16.6.1` | ICE5.1) If SYNC is ON, adjusting driver temperature affects  | 5 |
| `16.7` | ICE6.) Fan ranges: Off, 1-7 (denoting to show AUTO label ins | 5 |

### 14. `ICS Airflow and Defrost` — 5 sections / 29 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `16.8` | ICE7.) MAX DEF automatically turns on A/C, changes airflow m | 12 |
| `16.9` | ICE8.) Rear Defrost has on/ off state. Gray out the REAR DEF | 2 |
| `16.12` | ICE11.) Airflow Modes has 5 states (1.Face, 2.Mix of Face &  | 3 |
| `16.12.1` | ICE11.1) If the Mode hard control is pressed the user will b | 10 |
| `16.15` | ICE14.) EXTERIOR REAR-VIEW MIRROR DEFROST has on/ off state. | 2 |

### 15. `Home Screen Widget` — 6 sections / 21 leaves

| outline | section 標題（前 60 字） | leaves |
|---|---|---|
| `17.1` | W0.) The Comfort widget will have two screens: Comfort and S | 3 |
| `17.2` | CW1.) The default screen for the Comfort widget is the Clima | 8 |
| `17.3` | CW2.) The second Comfort widget screen includes all Comfort  | 3 |
| `17.4` | CW3.) For 8.4/10.1/12 landscaped screens, there will be a to | 2 |
| `17.5` | CW4.) For dual zone climate with dual airflow modes equipped | 2 |
| `18.1` | W0.) The Comfort widget will have two screens: Comfort and S | 3 |

---

## 7. 未入 Part N 者（12 §4）

- **17 節 in-baseline substantive**：`in_scope` 4 節（16.1、18.2 ~ 18.4）依
  R-C16 為 **RD-1 覆蓋缺口項**；`undetermined` 13 節（20.1 ~ 20.4.3 DEFERRED、
  19.1 ~ 19.3 待 DR #6）尚無處置。**皆不入 Test Set、不入 coverage 分母、
  不指派 tc_id。**
- **章 21（6 節）**：out of scope（R-C5，基線為 SR24，SR24 無第 21 章）。

### 插入邊界（07 §5 之要求，本 Part N 已預留）

| 若日後 in_scope | 插入點 | 是否需重整既有切分 |
|---|---|---|
| 章 20 Alternate Rear Blower | **新增** Test Set `Rear Blower` | 否 |
| 章 19 7" widget | 併入 #15 `Home Screen Widget` | 否 |

章 20 **不併入 #6 `Rear Climate`** —— 進入路徑與市場變體不同，依 §3.1 之
同一判準。

---

## 8. 本檔之權威範圍

本檔為 **Layer 1／2／3 之定義與對照**，其內容於 Pei 簽署下放包 12 時定案。
**落位變更須回分析層**，執行層不自行搬移 section。

本檔**不含**：
- profile `[OVERRIDE]` 條款 —— 仍為 Tier 2，未定（`DECISIONS.md` §6）
- TC 內容、tc_id 指派 —— Phase 4
- sibling 判定與 `duplicate_of` —— Phase 4（11 §6 就 `W0.)` 之 6 leaves
  已預告須做此判定）
