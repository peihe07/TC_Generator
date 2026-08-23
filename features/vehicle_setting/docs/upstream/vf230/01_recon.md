# 上繳 62 —— VF230 覆核之執行：W-116–W-120、條文落檔、A-VS 撞號

執行層寫入。依據：`docs/handoff/62_vf230_recon_review.md` §5（5 項工單）。canon §8.2 六節。

**本輪未生成任何 TC，未寫回任何工作簿。** Part 1 之交付內容、`framework.md`、
既有批次產物**一律未觸及**。

> **編號**：同上繳 61 之例外（62 包 §6 確認不改），本檔之 `62` 為**下放包號**，
> 非往返輪次（`docs/upstream/` 之輪次序現至 34）。

---

## 1. 交付總表

| 工單 | 狀態 | 產物 |
|---|---|---|
| W-116 正規化複驗（R-VS66） | **完成** | `scripts/vf230_layer2.py`（`key()` 改寫）、`docs/reports/vf230_layer2_candidates.md` |
| W-117 `-(\d+)$` 容錯清單 | **完成（列出未改）** | 本檔 §4 |
| W-118 A-VS130 是否成 DR | **完成** | **DR-29** |
| W-119 DR 波及三分類（R-VS65） | **完成** | `scripts/vf230_w119_dr_impact.py`、`docs/reports/vf230_dr_impact.md` |
| W-120 `Verification Criteria` 二欄（**優先**） | **完成（未採用）** | `scripts/vf230_w120_vcrit.py`、`docs/reports/w120_verification_criteria.md` |
| 條文落檔 | **完成** | `RULINGS.md` +R-VS64／65／66（逐字） |
| anomaly 落檔 | **完成** | +A-VS129／130（62 包開立，本層複驗）／A-VS135／136 |

---

## 2. ⚠ A-VS 撞號 —— 本層已讓號

62 包 §2.3／§2.4 開 **A-VS129／A-VS130**，而本層於 `6b0d2f3`
（2026-08-23 11:23）已用 **A-VS129／130／131**（62 包之 mtime 為 11:17，
其覆核對象為上繳 61 之**補篇前版本**，故未見）。

**處置：本層之三筆讓號，改編為 A-VS132／133／134。**

| 原 | 新 | 內容 |
|---|---|---|
| A-VS129 | **A-VS132** | 037 之 8 列判 Heading 而 035 判 Functional（leaf 母體可能為 627） |
| A-VS130 | **A-VS133** | 037 只涵蓋 035 之 Functional 之 57.7%，460 條無 SWE.1 分析 |
| A-VS131 | **A-VS134** | DR-28 之前提不成立 |

**讓號之理由**：62 包之 **R-VS66 逐字引用「理由見 A-VS129」**，而條文一經
落檔即不得改其逐字；本層之三筆僅為本層文件所引，改號之波及面小。
與 DR-27→DR-28 之處置**方向相反而準則相同** ——
**改動代價較小之一方讓號**。

**此為本線第三次撞號**（W-102–W-107、DR-27、A-VS129–130）。
R-VS64 已令「開新 W 號前須先查最大已用號」；**該令未及於 A-VS 與 DR**。
建議推廣為通則。

---

## 3. W-116 —— 正規化複驗（R-VS66）

```
複驗前                exact 103 ／ 無對應 3
依 R-VS66 逐字實作     exact 103 ／ 無對應 3     ← 無變化
加解序列化後           exact 104 ／ 無對應 2
```

**62 包 §2.3 之推論成立**：`Rear Guidance Lights with Cargo Lights`（5 leaf）
之「無對應」為**正規化產物**，非規格缺口。

**R-VS66 逐字所列之正規化不足以達成其目的** —— `vf230_leaves.tsv` 將換行
序列化為**字面兩字元** `\n`，`[\r\n\t]` 不匹配；而後續之 `[^a-z0-9]+`
摺疊會把 `n` 視為英數字保留，致 `with\nCargo` → `with ncargo`。
須先解序列化。見 **A-VS135(a)**。

**複驗後仍無對應者（真缺口）**：`E-Save` 6 leaf ／
`CHMSL CAMERA DYNAMIC CENTERLINE` 5 leaf。
另有 2 簇同名歧義（`Speed Unit`／`Charge Power Level`）未變。

**`E-Save` 之三源皆無**（spec 目次無、`SYS2_VF230.xlsx` 無、
037 有而 035 有）—— 見上繳 61 §12.4。

---

## 4. W-117 —— `-(\d+)$` 之受影響清單（列出，未改）

**量測條件**：`grep -rn` 對 `features/vehicle_setting/scripts/`（28 支）
與 repo 根 `scripts/`，搜 `-\d+$`／`-\d\d$`／`rsplit("-"`／`split("-")`。
命中 **3 處**，逐處以兩 feature 之 leaf 清單實測。

| # | 位置 | 形態 | Part 1（271） | VF230（619） |
|---:|---|---|---:|---:|
| 1 | `features/vehicle_setting/scripts/layer3_w46.py:41` | `re.match(r"SWE1-VC-(.+)-\d+$", swe_id)` | 受影響 **0** | 受影響 **17** |
| 2 | `scripts/recon.py:628-629` | `re.search(r"-\d\d$", rid)` | 命中 **0** | 命中 **0** |
| 3 | `scripts/recon.py:635-636` | `re.search(r"-\d\d$", r)` | 命中 **0** | 命中 **0** |

**第 2、3 處與本項無關**：其式要求「連字號 ＋ **恰二位**數字」，而兩 feature
之 ID 皆為三位（`-001`），故 `naive_leaf_shape` 於兩 feature **本即恆為 0**。
該處為 R-C3 所禁之啟發式與判準並陳之**證據測量**，非選取路徑。
（**附帶發現，未列為 anomaly**：該證據測量之數字既恆為 0，其作為「判準之差距」
之證據力為零。是否改為 `-\d+$` 屬 Part 1 之事，本輪不動。）

**第 1 處未改**（62 包 §5.2 令先列清單）。改法具名：`-?(\d+)$`。
**Part 1 之既有產物未受影響，不修。**

---

## 5. W-118 —— A-VS130 為上游書寫瑕疵，已開 DR-29

**回原始 037 儲存格逐字實測**：`SWE1-VC-TrailerBrakeType024`～`037`（14 列）
與 `SWE1-VC-MaxPowerLevel139`～`143`（5 列），**原始儲存格即無連字號**，
共 19 列（含 2 列 Heading），全數出自
`_STLA_Trailer_Name - Max_Power_Level_Report.xlsx` 一檔。同檔其餘 ID
（如 `SWE1-VC-TrailerName-001`）皆為正常形態。

→ **上游所書，非本層抽取所致。已開 DR-29**（型 A，Urgency Low，未送出）。
開號前已查最大已用號為 DR-28。

**本層未補連字號**（改值即造值）。

---

## 6. W-119 —— DR 波及三分類（R-VS65）

**掃描定義逐字遵行**：掃 `title` ＋ `desc`（619 leaf）；大小寫不分；
以詞界為準不作子字串命中；token 由各 DR 正文機械取得，不自創。

```
波及    1        DR-21（7 leaf，token `Hybrid_Type`）
不波及  11       DR-8／12／14′／15／17／18／19／20／25／26／27
待判    1        DR-11
```

**DR-21 之命中**（示例）：`ChargePowerLevel-044`／`-045`／`ConsumptionUnit-032`。

**DR-15 判不波及** —— 其 25 個 token 於 VF230 之 619 leaf 命中 **0**。
（DR-15 影響 Part 1 之 160 leaf。）61 包 §4.6 之「不得以 DR-15 為由阻塞
VF230 之 P1」因而有實測支持，非僅程序性禁令。

**DR-11 判待判，理由具名**：`DATA_REQUESTS.md` 之「仍開啟」表以**表列編號**
（5-A／5-B／7／8／9／10）記之，與內文之 `DR-N` 為**兩套編號**。
DR-11 僅於行 136 以交叉參照出現（`即 DR-11`），指向表列第 9 項
（`HeatedSteeringWheel-009` 之 Source Requirement ID 更正）。
**其提問為單一 leaf 之 reqid 更正，非 token 型，掃描無從施力。**

> **依 R-VS65 末段**：上列 11 個「不波及」**不是不波及之證明**，
> 僅證其 token 未出現於 leaf 之 title/desc。確認型 DR（DR-18）
> 之提問不繫於 VF230 之任何條文形態，其真實波及須待覆文方能定。

**判準三度修正**，最終數方為上列 —— 見 **A-VS135(b)(c)**。

---

## 7. W-120 —— `Verification Criteria`／`Method`（**優先項**，未採用）

### 7.1 三問逐答

**問 1（Part 1 是否亦有此二欄、非空率）**：

```
CFTS044  leaf 237   Verification Criteria 非空 237 (100.0%)   Method 237 (100.0%)
VF230    leaf 619   Verification Criteria 非空 619 (100.0%)   Method 619 (100.0%)
```

→ **此二欄非 VF230 獨有，Part 1 自 00 輪起即有，且同為 100% 非空。**

**問 2（既有作業曾否取用）—— 零命中**：

| 標的 | 命中 |
|---|---:|
| `RULINGS.md`（66 條）／`framework.md`／`PLAYBOOK.md`／`RUNBOOK.md` | 0 |
| `features/vehicle_setting/scripts/`（28 支）＋ repo 根 `scripts/` | 0 |
| `docs/runtime/`（canon ＋ 本 feature 之 profile） | 0 |
| `docs/handoff/`＋`docs/upstream/`（62 包與上繳 61 除外） | 0 |

`recon.py::survey_a03` 自 037 抽取之欄僅四（`categorization`／`asil`／`ftti`／
`hmi source`），**此二欄不在其列**。

唯一之全庫命中為**他 feature** 之 profile
（`docs/runtime/profiles/FW036_R1L_BT_Profile.md:82`），其令
「`Verification Method` 所述之情形須有明示之 recovery phase」——
**證明該欄在別處已被視為可用之輸入。**

**問 3（取樣並陳）**：10 對見 `docs/reports/w120_verification_criteria.md` §3。
**通例上 VC 較已交付之 ER 模糊**（例：`HeatedSteeringWheel-003` 之 VC 為
「Power cycle the HU and verify … defaults to OFF」，而已交付 ER 為
「1. The HU enters a sleep state on the BH-CAN bus／2. The heated steering
wheel state is OFF」）—— **就 ER 而言，該欄不構成較優之權威。**

### 7.2 但有一個決定性之反例

**A-VS118 之 4 leaf 之值域逐字載於該欄。**

A-VS118（37 輪）判 `HSW_Cmd_Tlm` 於 LID 兩欄組與 DBC 皆無值域，其 4 leaf
於 38 輪 W-108(1) 判 **W2／`B6-value-absent`**。W-120 實測：037 中提及
`HSW_Cmd_Tlm` 者**恰為同 4 個 leaf**，其 `Verification Method` 末行逐字為

```
4859496   * verify that TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON"
4859497   * verify that TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "OFF"
4859500   * HMI shall update to TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON"
4859501   * HMI shall update to TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "OFF"
```

**A-VS118 之判斷未誤（LID 與 DBC 確實無），誤在搜尋範圍未含該欄** ——
而該欄之未被搜尋非疏忽，是全庫從未有人知其存在（問 2）。見 **A-VS136**。

### 7.3 該欄之內容品質不齊一

| | CFTS044（237） | VF230（619） |
|---|---:|---:|
| 上游自述 `not clear` | 14（5.9%） | **90（14.5%）** |
| VC/VM 含訊號路徑引用 | 6（2.5%） | **232（37.5%）** |
| VC/VM 含 `CAN simulation` | 8 | 1 |

→ VF230 之該欄遠比 CFTS044 豐富，**但同時有 90 leaf 之上游自述「不清楚」**。
**不可整欄一體採信。**

### 7.4 判斷

**是一個未被使用之來源；其是否為「權威」不由本層認定。**

- 就 `expected_result` 而言 —— **不是**較優之權威（§7.1 問 3）。
- 就**值域**而言 —— **至少在 4 個實例上，其為唯一之逐字來源**（§7.2）。

採用與否屬 TC 內容書寫慣例之變更（62 包 §5.5 末句）。
**本層未採用、未改任何 TC、未改任何條文、未改該 4 leaf 之分級。**

**請裁**：(a) 該欄是否得作為**值域**之來源（若可，A-VS118 之 4 leaf
由 W2 轉 W0）；(b) `not clear` 之 90＋14 leaf 是否構成一類新的 blocker。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，三項。**

1. **上繳 61 §12.3 之兩件（A-VS132／A-VS133）於 62 包完全未獲處理** ——
   62 包成文於本層補篇之前，其 §0 逐字稱「§11 之獨立判斷列出三項」，
   即未見補篇。故 **8 列錯配（leaf 母體 619 vs 627）與 460 條無 SWE.1 分析
   （交付範圍之界）二事，至今無任何裁決**。二者皆會改變 Layer 2 之
   簇數與 leaf 分布，**而 62 包 §4.2 正在問 Layer 2 之起點** ——
   **在 A-VS132 未裁前定 Layer 2，其簇數可能須重算。**

2. **`output/` 三檔之對帳由分析層執行（62 包 §2.2），本層未複驗其結果。**
   本層對「619 之 src_ref 逐值全等」一句僅為照錄。

3. **W-120 §7.3 之 90 個 `not clear` leaf 未逐一查其內容。** 其是否與
   現行之 `writability` 分級相符（該 90 個是否已被判 W1/W2）**未測** ——
   若上游自述不清楚而本層判其可寫，二者不一致須解釋。

**另有一項非「未驗」而是「本輪三度出現」**：判準之第一版不足以達成其目的
（A-VS135 之 (a)(b)(c)），且**其中兩次之判準係由條文逐字所定**。
建議：條文所定之判準須附必命中／必不命中之錨點（R-VS54 之精神），
否則其充分性在落筆時無從檢驗。
