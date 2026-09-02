# 上繳包 04 — vsm_v42：P3（framework Layer 3 回填、W-5 收尾落地、DECISIONS 簽核準備、P4 預備）

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/04_p3_framework.md`

## 結果分類（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | §一 五項條文落地（v3 就地更新，逐列 diff 見第 1 節）；W-8 Layer 3 回填；W-10 DECISIONS 四欄；W-11 `test_set` 欄；W-12 兩表 |
| 核實無誤 | **E32 = 0**、**E34 十組全相符（128）**、E36 六條；R-VL16(b) 審計三列**全數存活** |
| 正確地不動 | 台帳不重生（R-VL13）；`profiles/` 未讀寫以外之動作；**W-9 未照下放包字面辦**（見第 3 節）；3 個未對映家族**不硬配**；DECISIONS **不代簽**；DR 不送 |

**總判：W-8～W-12 全數完成。E33／E37 各有一項與下放包公式不符（皆可歸因，見第 6 節），不調和。**

---

## 1. §一 五項條文落地 —— v3 就地更新之逐列 diff

`data/signal_chain_v42_v3.tsv` 就地更新（本包例外授權）。**逐列 diff 共 9 列**：

| # | 名 | 原 | 新 | 依據 |
|---|---|---|---|---|
| 1 | `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req` | B-1 衝突 | **解得** | R-VL15(a) |
| 2 | `TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req` | 未解得(止於段3) | **未解得（規格拼字疑誤）** | R-VL16(a) |
| 3 | `SERVICE_SETUP.RestoreDefaulSetting` | 未解得(止於段3) | **未解得（規格拼字疑誤）** | R-VL16(a) |
| 4 | `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq` | 未解得(止於段3) | **未解得（規格拼字疑誤）** | R-VL16(a) |
| 5 | `PrivacyMode.Info` | 解得 | 解得（**審計存活**） | R-VL16(b) |
| 6 | `Country_Code` | 解得 | 解得（**審計存活**） | R-VL16(b) |
| 7 | `External_Light_Sensor_Level.Req` | 解得 | 解得（**審計存活**） | R-VL16(b) |
| 8 | `IPC_VEHICLE_SETUP.PassiveEntry` | 未解得(止於段3) | 未解得(止於段3)（**僅加備註**） | R-VL16(c) |
| 9 | `TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req` | 未解得(止於段3) | 未解得(止於段3)（**僅加備註**） | R-VL16(c) |

### 1.1 R-VL15(a) K-1 改判

第 1 列之 `seg2` 收斂為目標欄逐字之 `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req`
（`LID/CAN Mapping/r1112cP/Atlantis Signal Name/R1 逐字`），
段 3 證據 `BO_158 TELEMATIC_VEHICLE_SETUP / SG_ LanguageSelection_Req / VAL_ 有 22 項`；
備註記 Sts 孪生對偶 `IPC_VEHICLE_SETUP.LanguageSelection`（`BO_1468`，`VAL_` 23 項）。
**E32：B-1 = 0。**

### 1.2 R-VL16(b) 非 CAN 形審計 —— 三列逐列出段 1 依據

| 名 | 段 1 依據（逐字引欄／列／規則） | 判 |
|---|---|---|
| `PrivacyMode.Info` | `LID/CAN Mapping/r1398cA/Logical Identifier/R2′ 去 .Info 後綴` | **存活** |
| `Country_Code` | `LID/Proxi & Configuration/r43cA/Logical Identifier/R1 逐字`；`PROXI/Format/r468cF/R1 逐字`；另 `LID/CAN Mapping/r46cB/Function/R4` | **存活** |
| `External_Light_Sensor_Level.Req` | `LID/CAN Mapping/r751cA/Logical Identifier/R4 R2′ 去 .Req 後綴+底線/大小寫`；同列 `r751cB/Function` | **存活** |

**三列皆有段 1 依據，無一退回**（R-VL16(b) 之「僅段 3 同名不算」未命中任何一列）。

### 1.3 R-VL16(a) 全掃 —— **下放包只知兩例，實測為三例**

掃描條件：對 v3 全表之「未解得(止於段3)」逐列，取其段 2 標的之 `Signal` 部，
對主 DBC 之 794 個相異 `SG_` 名做**編輯距離 ≤ 2** 之比對（機讀，非語意）。

| 規格原名 | 主 DBC 之近似名 ＋ 佐證位置 |
|---|---|
| `SERVICE_SETUP.RestoreDefaulSetting`（少 `t`） | `SERVICE_SETUP.RestoreDefaultSetting`（`BO_1446`，`VAL_` 2 項） |
| `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq`（`Settimg`） | `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettingReq`（`BO_`，`VAL_` 有） |
| **`TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req`** | **`SVC_Guidelines_Req`** |

> **第三例之方向與前二例相反，須指出**：`Gridlines`（格線）為攝影機領域之正確用語，
> DBC 寫 `Guidelines`（指引）—— **看起來是 DBC 拼錯，不是規格拼錯**。
> R-VL16(a) 之條件（「規格原名於正確拼法下於主 DBC 存在」）字面仍成立，故三列同記該值域；
> 但其**成因方向不同**。**本包不分立值域、不改判**，據實記明交分析層。
> 三列皆依 R-13／R-6 **保留規格原名**，備註記正確拼法與 `BO_`／`VAL_` 佐證，佐證留檔不送。

### 1.4 R-VL16(c) PassiveEntry ＋ A-VL11

第 8／9 列僅加備註（LID 對映指向 `RFHUB3.RFReq`，他 ECU，本 DBC 查無；P4 遭遇時 PENDING）。
**A-VL11 → RESOLVED**（R-VL14 加註：`SG_ 5568` 為字串出現數，訊號定義數 844／相異 794）。
**A-VL12 → RESOLVED**（R-VL16(a)），並於該條補記本包全掃所得之第三例。

### 1.5 更新後之結果分布（v3 現行）

| 結果 | 總 | CAN(112) | Req(69) | Info(32) | GUI(2) | PROXI(36) |
|---|---|---|---|---|---|---|
| **解得** | **99** | 96 | 1 | 1 | 0 | 1 |
| 未解得(止於段1) | 94 | 0 | 62 | 28 | 2 | 2 |
| 訊息名不符(R-13) | 7 | 7 | 0 | 0 | 0 | 0 |
| 未解得(止於段3) | 6 | 6 | 0 | 0 | 0 | 0 |
| **未解得（規格拼字疑誤）** | **3** | 3 | 0 | 0 | 0 | 0 |
| PROXI路徑(R-P375b/c) | 35 | 0 | 3 | 2 | 0 | 30 |
| UI+PROXI 雙路徑 | 4 | 0 | 1 | 0 | 0 | 3 |
| UI路徑(R-P375b) | 3 | 0 | 2 | 1 | 0 | 0 |
| **B-1 衝突** | **0** | 0 | 0 | 0 | 0 | 0 |
| 查無(R-G13) | 0 | — | — | — | — | — |

---

## 2. W-8 Layer 3 章節號回填

規格 docx **無編號式標題文字**（`^n.n(.n) ` 之段落實測 **0**），
章節號須自 `word/styles.xml` 之 outline 階層推得：
`styleId` 1／21／31／41／51／6／7 → `heading 1`–`heading 7`（`outlineLvl` 0–6，逐一實測）。
據此對 1,744 段掃出 **115 個非空標題段**並逐級編號。

對映方式：家族名 ↔ 標題文字之**逐字**或**正規化逐字**（去非英數、小寫）。
**未做語意比對**（下放包第 5 節升級條件：需語意猜測即列未對映，不猜）。

**E35：已對映 21 ／ 24 家族。** 回填入 `framework.md` **最末欄，其餘欄未動**
（diff 實測：變動 10 列、非表列之變動 **0**）。

| Test Set | 規格章節號 |
|---|---|
| 1 Park Sense | `PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2` = **1.11.1.1.29**；其餘二家族 **未對映** |
| 2 Camera Gridlines | Dynamic Gridlines = 1.11.1.1.31；Surround Camera Gridlines = 1.11.1.1.38 |
| 3 Lighting | Auto High Beam = 1.11.1.1.30；Headlight Sensitivity = 1.11.1.1.13 |
| 4 Speed Assist | 1.11.1.1.32／1.11.1.1.33／1.11.1.1.35／1.11.1.1.36 |
| 5 Driver Warning | Side Distance Warning = 1.11.1.1.5；Audio Repetition = 1.11.1.1.28 |
| 6 Wiper and Sensor | Rain Sensor = 1.11.1.1.7 |
| 7 Units | Units = 1.11.1.1.10；**Distance = 未對映**；Fuel Consumption = 1.11.1.1.10.5.2 |
| 8 EPB Maintenance Mode | 1.11.1.1.19 |
| 9 Personal Data and Defaults | 1.11.1.1.37；1.11.1.1.40／**1.11.2.1.2**；1.11.1.1.41／**1.11.2.1.3**；1.11.1.1.39／**1.11.2.1.1** |
| 10 Time and Navigation | 1.11.1.1.25；1.11.1.1.27 |

**三個未對映家族，逐一附證據（不硬配）**：

| 家族 | 實測 |
|---|---|
| `Distance` | 規格有 **`1.11.1.1.10.5.1 Distances`**（複數）。**單複數之差非逐字**，故列未對映。**但結構上高度可疑**：其同層兄弟 `1.11.1.1.10.5.2 Fuel Consumption` 已逐字對映，且二者同屬 `1.11.1.1.10 Units`——與 Test Set 7「Units（Units／Distance／Fuel Consumption）」之組成完全吻合。**證據列出，不自行填。** |
| `Rear Park Sense Volume/ ParkSense Volume` | 規格**全篇無任何含 `Volume` 之標題**（掃 115 個標題，含 `Volume` 者 0）。真未對映。 |
| `Front Park Sense Volume` | 同上。 |

> **另記**：Test Set 9 之三個家族**各有兩處章節**（`1.11.1.*` 與 `1.11.2.*`），
> 已並列不擇一。`Geolocation`／`Clear Personal Data`／`Restore Default Setting`
> 在規格中出現兩次為結構事實，非重複標題之錯。

---

## 3. W-9 —— **未照下放包字面辦，理由如下**

下放包令「HMI Settings List／SR24 Market Config／SR26 Default Settings 各補 (a)–(f)，
(f) 首個採用 = `vsm_v42,vsm_v43`」。

**實測：三件皆已於 `forms/FORMS.md` 完整登錄**（§`共用參考件 —— Pop Up`，
行 553／570／585），(a)–(f) 六項齊全，**(f) 首個採用 = `power`，2026-08-30（R-P375）**
—— 早於本線。**照辦即覆寫他線之正確記載**（FO 第 8.5 節之三：不越權；R-G15 之記載真實性）。

**改為執行層之處置（加法，非覆寫）**：於三條目之
`> **使用中之 feature（R-G15 反向記載）**` 行**追加** `vsm_v42`／`vsm_v43`，
並附本線 W-5′ 之實測事實：

| 檔 | 追加之實測 |
|---|---|
| `HMI Settings List R1 SR25` | `Settings` 分頁 **B／C 欄**命中 **10** 個訊號名（含第五規則去 `_Menu`／`_Setting`）；為 `UI路徑` 3 列與 `UI+PROXI 雙路徑` 4 列之依據 |
| `SR26 Default Settings` | `Default Parameters` 命中 **1** 名；屬 (d) 之靜態組態範圍，未代運行時狀態（R-P375(e)） |
| `SR24 Market Config v1.6` | **0 命中** —— 與 power 同，屬 (d) 之預期範圍，**非缺漏**（R-G13）；本線 251 名對該分頁零交集，登記為已查之檔 |

**另發現 `FORMS.md` 之內部矛盾並加註（不刪原文，R-TM13）**：
該檔 §`本節之範圍限制（誠實揭露）` 之「3 件未登錄」表**與同檔上方之三個已登錄小節互相矛盾**
——成因為該節落檔於補登之前而未隨補登更新。已於該表下加註失效說明，
並記明本包未照 W-9 字面辦之理由。

> **這是下放包 04 之一項事實誤**：W-9 之前提（三件未登錄）取自 `FORMS.md` 之**過時段落**。
> 據實回報，不代改條文。

---

## 4. W-10 DECISIONS 簽核準備

補齊四欄實值，**未代簽**（`Sign-off` 之 `Reviewed by`／`Date` 留空，狀態標「待 Pei 簽」）：

| 欄 | 值 |
|---|---|
| `spec_mode`（§1） | **D** —— 母 spec 為 OOXML docx（R-VL5；magic `50 4B 03 04`，上繳 02 E22） |
| `workbook_state`（§2） | **BLANK** —— R-VL1 自 R-G1 母本起建；副本 cmp 全等、zip 48、x14 DV 1 |
| **母體**（§3） | **128**（R-VL4；跨源 128／128；`data/leaves.tsv` 152 列已帶 `test_set` 欄）。原 `[AUTO] 68` 保留並註明其為 recon 代表檔之數 |
| `Test Set table`（§6） | **[RULED] R-VL17** 十組全列，並註 Layer 3 已回填 21／24 |

另更新 §7 `batch plan` 之母體數（68 → 128）與 pilot 提案（`EPB Maintenance Mode` 17）。

**一項 `[PEI]` 未填**：`profile [OVERRIDE] clauses` ——
`docs/runtime/profiles/FW036_R1L_VSM_V42_Profile.md` 已由分析層落檔，
惟該目錄為**執行層禁區（讀可寫不可）**，故不代填該欄。

---

## 5. W-11 `leaves.tsv` 加 `test_set` 欄

`data/leaves.tsv` 加 `test_set` 欄（位於 `tc_status` 之後），**152 列全數填妥**
（Heading 與 UNCATEGORIZED 列亦依其家族填，便於覆蓋台帳）。

### E34 逐組對測

| Test Set | framework | 實測 leaf | 判 |
|---|---|---|---|
| Park Sense | 18 | **18** | 相符 |
| Camera Gridlines | 10 | **10** | 相符 |
| Lighting | 11 | **11** | 相符 |
| Speed Assist | 21 | **21** | 相符 |
| Driver Warning | 13 | **13** | 相符 |
| Wiper and Sensor | 5 | **5** | 相符 |
| Units | 15 | **15** | 相符 |
| EPB Maintenance Mode | 17 | **17** | 相符 |
| Personal Data and Defaults | 14 | **14** | 相符 |
| Time and Navigation | 4 | **4** | 相符 |
| **合計** | **128** | **128** | **相符** |

未對映家族 **0**（24 家族全數落入十組）。

---

## 6. W-12 P4 預備（只建表不生成）＋ 預期數字對照

### `data/val_tables_v42.tsv`

自主 DBC 之 `VAL_` 逐字取值，欄：`spec_name`／`kind`／`message`／`signal`／`msg_id`／`raw`／`label`。
涵蓋 **98 個訊號**、**300 個 `raw → label`** 值對。

### `data/ba_sendtype_v42.tsv`

自主 DBC 之 `BA_ "<attr>" SG_ <msgid> <sig> <value>;` 取，**99 列**（解得全數）。
欄：`spec_name`／`message`／`signal`／`msg_id`／`GenSigSendType`／`GenSigStartValue`／`其他BA_屬性`。

| `GenSigSendType` | 列數 |
|---|---|
| `1` | 38 |
| `3` | 57 |
| `7` | 4 |

`GenSigStartValue` **99／99 皆有值**。（此表僅供 P4 之 Procedure `Send`／`Hold` 寫法參考，
**本包不生成任何 TC**。）

### 預期數字逐項

| # | 項 | 判準／預期 | 實測 | 判 |
|---|---|---|---|---|
| **E32** | v3 更新後 B-1 | 0 | **0** | **過** |
| **E33** | v3 更新後「解得」 | 95 ＋ 審計存活數（≤ 98） | **99** | **不符公式** |
| **E34** | W-11 十組合計 | 逐組 = framework，總 128 | **十組全相符，總 128** | **過** |
| **E35** | W-8 已對映家族數 | 觀測 | **21 ／ 24**（未對映：`Distance`、`Rear Park Sense Volume/ ParkSense Volume`、`Front Park Sense Volume`） | 觀測 |
| **E36** | R-VL12–R-VL17 `body_sha8` | 與 `RULINGS.md` 現檔一致（樹外 `--out`） | **六條全數取得**（見下表） | **過** |
| **E37** | `VAL_` 表列數 | ＝ E33 之解得數 | **98**（解得 99） | **不符** |

**E33 不符公式之歸因（不調和）**：公式「95 ＋ 審計存活數」中之 95 為 v3 原有之 CAN 解得數，
**未計入 R-VL15(a) 使 K-1 由 B-1 轉入解得之 +1**。
實際＝ CAN 95 ＋ K-1 之 1 ＝ **96**，加審計存活之非 CAN **3** ＝ **99**。
公式與條文本身一致，是公式漏列了同包之另一條裁定。**本包不改判、不調公式。**

**E37 不符之歸因（不調和）**：`VAL_` 表以「有 `VAL_` 之訊號」為列，
而解得之 99 名中 **`Country_Code` 一名於主 DBC 無 `VAL_` 表**
（其段 3 標的 `META_DATA.ADAS_Meta_CountryCode`，`BO_1865`，`VAL_ 無`）。
故 98 ＝ 99 − 1。此名於上繳 03 即已標明為「解得而無 `VAL_`」之唯一一列。
**P4 遭遇時該列只能寫 `= <raw>` 而無 `(<label>)`，須於 TC 註明。**

### E36 — `body_sha8`

| 條號 | `body_sha8` | `sha8`（觀測值） |
|---|---|---|
| R-VL12 | `34577e46` | `2d62ac95` |
| R-VL13 | `782082cf` | `c0264dff` |
| R-VL14 | `3cc6e581` | `413b5c3b`（上繳 03 為 `6f362276`；A-VL11 加註所致，`body_sha8` 未動） |
| R-VL15 | `f4fc955a` | `9f53b0de` |
| R-VL16 | `eba576d3` | `c6f4af8e` |
| R-VL17 | `8d75a0a2` | `d4836946` |

**R-VL1–R-VL11 之 `body_sha8` 續驗，11／11 與上繳 02／03 逐字相同**（本包未受令重驗，主動附）。

---

## 7. A／DR 狀態

| 編號 | 狀態 |
|---|---|
| A-VL1／2／3／4／9／10／**11**／**12** | RESOLVED（11／12 為本包所轉） |
| A-VL5／6／7 | 併 DR-VL2(a)/(b)/(c) |
| A-VL8 | 阻塞面已解除；**段 1 命中率之問仍 PENDING**（CAN 112 名中段 1 命中 30，其餘依 R-VL12(c) 直入段 3） |

**本包未新開 anomaly。** 三項新發現（W-9 之 FORMS.md 矛盾、W-8 之 `Distance`／`Distances`、
R-VL16(a) 第三例之方向相反）**皆已在既有條目或本上繳內具名**，
未另立 A 號 —— 前者為文件維護問題非資料異常，後二者屬既結案條目之補記。
若分析層認為須立號，請指示。

| DR | 狀態 |
|---|---|
| DR-VL1（191 列揭露）／DR-VL2（標註三面） | 已登記，**未送出**（Pei 裁先不送） |
| DR-VL3 | 結案（到件） |

**本包未送出任何 DR。**

---

## 8. 獨立判斷

1. **一項下放包之事實誤已回報**：W-9 之前提（三件 xlsx 未登錄）取自 `FORMS.md`
   之過時段落；三件實已登錄且首採為 `power`（第 3 節）。
2. **一項公式漏列已回報**：E33（第 6 節）。
3. **三項待裁**：
   - `Distance` ↔ `1.11.1.1.10.5.1 Distances` 之單複數差是否認定為對映
     （結構證據強，但屬語意/形態判斷，本包不填）；
   - R-VL16(a) 第三例（`SVC_Gridlines` vs DBC `SVC_Guidelines`）**方向相反**，
     是否分立值域或加註；
   - `profile [OVERRIDE] clauses` 之 DECISIONS 欄由誰填（`profiles/` 為執行層禁區）。
4. **一項本包未做且指得出理由**：`framework.md` 之 Layer 3 欄只填章節**號**，
   未附章節**標題文字**。下放包令「只填該欄，不動其他」，欄寬已含家族名，
   再加標題會使該欄失去可讀性。若需標題，建議另建 `data/layer3_map_v42.tsv`。
5. **一項提醒 P4**：`ba_sendtype_v42.tsv` 之 `GenSigSendType` 三值（1／3／7）
   **本包未解其語意**（DBC 之 `BA_DEF_` 列舉未查）。P4 若要據以決定
   `Send`／`Hold` 寫法，須先解該列舉，**不得憑數值猜測**。

---

## 9. `gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 505
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash` —— 依 R-VL13 記「待 Pei 重生」。**
id 級實測（樹外 `--out`，未寫入 repo）：

| 類 | 內容 |
|---|---|
| 新增 id（17） | `R-VL12`–`R-VL17`（本線 6）；`R-VT11`–`R-VT16`（vsm_v43 6）；`R-VS84`–`R-VS88`（vehicle_setting 5） |
| 移除 id | **0** |
| `sha8` 變動（3） | `R-VL2`／`R-VL5`／`R-VL9`（R-TM13 加註） |
| 其中 `body_sha8` 亦變者 | **0** |

**依 R-VL15(c) 修訂後之判準（「無刪除列，且既有列之 `body_sha8` 無變動」）——
本包實測完全滿足，可上繳。** 上繳 03 所提之但書問題已由 R-VL15(c) 解決。

**(乙) `canon_refs` 505**（上繳 03 為 504，+1）—— 逐檔逐行歸因，含 `vsm_v42` 者 **3 列**，
與上繳 02／03 **逐字相同**（`ANOMALIES.md:62` 之 `R-G40`、`RUNBOOK.md:9` 裸 `§3`、
`DECISIONS.md:3` 裸 `§4`，後二者為共用腳本模板）。
本包所改之 `forms/FORMS.md` **命中 0 列**。+1 落於本線之外。

**(丙) `gates_tsv`／(丁) `lint_paths` = 4** —— 與本線無關，先在，四筆與前三包逐字相同
（driver_distraction 兩本工作簿落點、ics_management 與 sw_update 之 delivered sha）。
本包新增之檔皆為 `.tsv`／`.md`，未觸該閘。

**無一支肇因於本包之寫入。**

---

## 10. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `features/vsm_v42/data/signal_chain_v42_v3.tsv` | **就地更新**（9 列，本包例外授權；逐列 diff 見第 1 節） |
| `features/vsm_v42/framework.md` | **只填 Layer 3 欄**（10 列；非表列變動 0） |
| `features/vsm_v42/data/leaves.tsv` | 加 `test_set` 欄（152 列全填） |
| `features/vsm_v42/data/val_tables_v42.tsv` | **新建**（98 訊號／300 值對） |
| `features/vsm_v42/data/ba_sendtype_v42.tsv` | **新建**（99 列） |
| `features/vsm_v42/DECISIONS.md` | W-10 四欄 ＋ §7；**未簽** |
| `features/vsm_v42/ANOMALIES.md` | A-VL11／A-VL12 → RESOLVED；A-VL12 補第三例 |
| `forms/FORMS.md` | 三條目補 R-G15 反向記載；§範圍限制 加註失效（**本包例外授權此一檔**） |
| `features/vsm_v42/docs/upstream/04_p3_framework.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：`docs/fw036/RULINGS.sha.tsv`（R-VL13）、**`docs/runtime/profiles/`（禁區，只讀）**、
`scripts/`、`forms/` 之其餘檔（DBC 等只讀）、`docs/runtime/` 其餘、`features/vsm_v43/`、
`features/vehicle_setting/`、`sources/`、`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md,
feature.yaml, sandbox/, RECON.md, data/signal_chain_v42.tsv, data/signal_chain_v42_v2.tsv,
data/atlantis_vs_high_v42.tsv, data/p3_families_v42.md}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 11. 待 Pei／分析層之五項

1. **`Distance` ↔ `1.11.1.1.10.5.1 Distances`** 是否認定對映（E35 由 21 → 22）。
2. **R-VL16(a) 第三例方向相反**（`SVC_Gridlines` vs DBC `SVC_Guidelines`）之處置。
3. **`Rear/Front Park Sense Volume` 兩家族無規格章節** —— 規格全篇無 `Volume` 標題；
   其 13 個 leaf（6＋7）之 `specification_reference` 於 P4 將無來源可引，**須先裁**。
4. **DECISIONS 之 `profile [OVERRIDE] clauses`** 由誰填（`profiles/` 為執行層禁區）。
5. **`GenSigSendType` 1／3／7 之語意**（第 8 節第 5 項）—— P4 之 `Send`／`Hold` 寫法所需。
   ＋ 台帳重生時機、共用腳本一裁（六項）、`_intake/Vehicle_Setup_VF665/` 空目錄刪除。
