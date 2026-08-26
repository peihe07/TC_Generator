# Audio Management — 上繳包 23：B6 第二路對帳（R-AM15）

- 日期：2026-08-26
- 下放包：`docs/handoff/22_B6_anchor_candidates.md`（第一路，無 A 級）
- 池基準：展開池 v2，891 ID
- 方法：四關全備；C 級三簇依包 22 §二 之授權以**第四關區段掃描**裁定

---

## 一、簇 (a) 存在偵測群（7 葉）：**5 解、2 回**

區段 1.5.2 逐條讀（4867486–4867520）。

| 葉 | 錨 | 池 | 錨文 |
|---|---|---|---|
| SWE1_AMM_249 | 4867486 | ✓ | `IF $AMPPresent$ = … THEN the HU shall switch to "Fixed-Gain" output mode as defined in {SIS-5380}` |
| SWE1_AMM_250 | 4867487 | ✓ | `… "Variable-Gain" output mode as defined in {SIS-5543}` |
| SWE1_AMM_251 | 4867507 | ✓ | `IF $BSSPresent$ = … THEN the **LBSS** shall be considered present` |
| SWE1_AMM_252 | 4867508 | ✓ | `… the **RBSS** shall be considered present` |
| SWE1_AMM_254 | 4867517 | ✓ | `IF $ICSPresent$= … THEN the ICS shall be considered **present**` |
| SWE1_AMM_255 | 4867518 | ✓ | `IF $ICSPresent$= … THEN the ICS shall be considered **not present**` |

**249／250 為 §7 配對**（Fixed／Variable Gain），成對交付；
**251／252 亦為 §7 配對**（L／R）。四葉皆池內，兩路一致，依 R-AM20 逕寫。

**255 之預警成立。** 包 22 疑匹配器候選 4867712（B3 之 296 錨）係詞面撞題
（"not present"）——實查：4867712 為 `$Reverse_Mute_Enable$` 缺席，
與 ICS 無關；正解 4867518 就在 254 之錨（4867517）**次一句**。
預警之判斷與定位線索兩者皆正確。

### 回分析層（2 葉）

- **SWE1_AMM_248**（Amplifier Presence Detection）：1.5.2.5 段自 4867486 起
  即為 `$AMPPresent$` 之**後果**條款（Fixed/Variable Gain、各項診斷啟停），
  **無「AMP shall be considered present」之判定句**（對照 LBSS 4867507、
  ICS 4867517 皆有）。葉之「determine amplifier presence …and configure」
  或錨於該段之前置句，或該判定句在 CFTS019 缺漏。**單件回**。
- **SWE1_AMM_258**（Read Cabin EQ Configuration）：`$CabinEQ$` 之命中皆為
  **有效性**（4867474–4867477）或**忽略**（4867498）條款，未見「初始化時
  讀取 PROXI 之 CabinEQ 並採用」之句。**單件回**。

## 二、簇 (b) Surround 狀態細分（5 葉）：**全解，三撞化解**

包 22 記 094／096／097 三葉同撞 4866260、104 撞 095 之 4866257。
區段 4866255–4866272 逐條讀後，四者各有其物件，**無一需共錨**：

| 葉 | 錨 | 池 | 錨文 |
|---|---|---|---|
| SWE1_AMM_094 | 4866256 | ✓ | `IF the HU receives $AMPSurroundSTS$ = [CFG_ST] THEN the HU shall update display HMI within <Tdisp>` |
| SWE1_AMM_095 | 4866257 | ✓ | `IF the user selects to enable surround sound THEN the HU shall send $SurroundOnOff$ = [ON]`（維持） |
| SWE1_AMM_096 | 4866259 | ✓ | `… = [CFG_VID_SURR or CFG_AUD_SURR] THEN … update display HMI` |
| SWE1_AMM_097 | 4866260 | ✓ | `… = [SNA] THEN the HU shall **assume Stereo Mode** and update display HMI` |
| SWE1_AMM_104 | 4866268 | ✓ | `Following requirements **for AMP** are valid only IF $Surround$ == Present` |

三撞之成因可辨：4866256／4866259／4866260 為**同句型三變體**
（`$AMPSurroundSTS$` 三種值 → 更新 HMI），匹配器對三者評分近乎相同。
區辨依據為**訊號值**（CFG_ST／CFG_VID_SURR｜CFG_AUD_SURR／SNA），
與葉描述逐一對應。

`<Tdisp>` 有定義（Max 100 ms），094／096／097 依 IN §8.7.1 以實值入 TC。

## 三、簇 (c) 儲存／回復（5 葉）：**2 解、3 回**

### 三.1 SWE1_AMM_269／271 — 同文異錨對，**非 duplicate**

271 於 SWE.1 自題「(Duplicate Requirement)」。第四關實查：

> **4867641**：`- loudness menu item is not present on HU IF $AudioSystemType$
> == "Fiat Booster" and both HU and AMP_BSTR shall not manage any loudness
> adjustment on …`
> **4867648**：**逐字相同**

兩者為**兩個獨立物件**（分屬不同系統型別段落之重複條列）。依包 22 §二.b
之判準「異物件 → 各錨各條」：**269 → 4867641、271 → 4867648，各自成條**，
**不標 `duplicate_of`**（§10.6 嚴格等價判準要求同觸發＋結果＋輸入＋驗證標的；
此處兩葉之驗證標的分屬兩物件，不成立等價）。

括號下半須各異（同文異錨，比照 058／066 之處置）。

### 三.2 回分析層（3 葉）

**140／161／170／171／172 之儲存／回復序列**：CFTS019 含**至少四組**
store／recall 對，分屬不同子章節：

| 物件對 | 所屬 | 現況 |
|---|---|---|
| 4866602 / 4866632 | Park Assist／Blind Spot 信號來源序列 | 未指派 |
| 4866629 / 4866632 | Blind Spot 序列 | 未指派 |
| 4866659 / 4866662 | — | **已為 B4 之 175／176** |
| 4867457 | 1.5.1 Initialization（`recall the last known configuration settings`） | 未指派 |

**包 22 之預警成立**：170／171 之匹配器候選 4866659 確為 B4 之 175 錨，
不得默用。惟第二路**無法單憑區段掃描判定五葉各屬哪一組**——
SYS-RA 序（371／404／458／463／467）跨越初始化與信號來源兩個語境，
而兩語境之 store／recall 文字近乎相同。

**處置：140、161、170、171、172 五葉單件回**，建議分析層以 SWE.1 之
Categorization／Sub Categorization 欄或上游 SYS-RA 之章節歸屬判定語境，
再指派物件對。**執行層不以序列推定填錨**（R-AM15）。

（172 之候選 4866298 顯錯——Balance 句——第二路同意棄用。）

## 四、零星預警之判別

### 四.1 SWE1_AMM_120 → **4866310**（改錨，池內）

包 22 疑正解為 4866306／4866307，二者實為 **AMP 側**條款
（`IF the AMP receives a $ToneBAL$ …`）。正解：

> **4866310**：`Both fader and balance level shall be distributed in **19 equal
> steps, between level negative 9 to level positive 9**.`

與葉「normalized 19-step range from -9 to +9」逐字對應。
原候選 4866308（B3 之 119 錨）確不適用，預警成立。

### 四.2 SWE1_AMM_121 — **共錨申報**（依包 22 §三 新制）

| 項 | 內容 |
|---|---|
| 錨 | **CFTS019-4866311** |
| 兩葉 | **121（B6）** 與 **025（B5，已交付）** |
| 性質 | **跨批共錨**，R-AM21 涵蓋 |
| 121 括號下半（草案） | `Confirm the configured fade and balance settings reach the amplifier` |
| 025 括號下半（已交付） | `Confirm a fade or balance change is transmitted to the amplifier` |
| 分野 | 025 觀察**變更觸發之傳遞**；121 觀察**設定值本身之送達**，與包 22 §三 所述之分工一致 |

**另案可能**：4866312（`HU shall set these signals according to the
respective internal signal values and according to the table`）亦可承 121，
如此則不需共錨。第二路傾向共錨 4866311（4866312 之題旨偏編碼對映，
與 049 之領域相近），**惟依新制不逕寫，待核可**。

註：葉 121 寫 `$ToneFADES$`／`$ToneBALS$`（**帶 S**），錨文為
`$ToneFADE$`／`$ToneBAL$`。依 R-13(g) 交付欄保留葉之原文名，
差異登記為 DR-AM4 之附項。

## 五、B 級其餘（33 葉中之 30）

除 104、120、121 三葉（已於 §二、§四 處理）外，其餘 30 葉之候選經
第二路以匯出本文覆核，**未見不一致**，依 R-AM20 逕寫。

## 六、統計

| 段 | 葉數 |
|---|---|
| 逕寫（兩路一致，池內） | **41** |
| 共錨申報待核（121） | 1 |
| 單件回分析層 | **8**（248、258、140、161、170、171、172，＋B5 遺留之 293 已裁） |
| 合計 | 50 |

## 七、待分析層

1. §一 之 248／258（存在偵測群無判定句 / CabinEQ 讀取句）。
2. §三.2 之五葉語境判定（140／161／170／171／172）。
3. §四.2 之共錨申報核可（121／025）。
4. §三.1 之 269／271 採認（同文異錨，非 duplicate）。
5. §四.1 之 120 改錨採認。
