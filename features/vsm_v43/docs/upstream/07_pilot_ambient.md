# 上繳包 07 — vsm_v43：P4 pilot　Interior Ambient Lighting（10 leaf）暫代生成

日期：2026-09-02　執行層　對應下放包：`docs/handoff/07_pilot_ambient.md`
產出止於 `generated/`（文字形）；**未寫工作簿、未寫 `delivered/`、未動 `sandbox/base/`**。
台帳不重生；**DR 不代發**。

---

## 〇、一句話結論

**W-A 判「不成立」（只寫 Sys-RA 錨）；W-B 出 10 leaf／11 TC；W-C 全項通過；W-D 之 43% 不變。**

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E38 | 覆蓋 | 10 leaf 各 ≥1 TC | **10/10**，TC 總數 **11** | ✅ |
| E39 | R-S4 括號下半 | 每 TC 有；同 req_id 內不逐字相同 | **11/11 有；重複 0** | ✅ |
| E40 | 尾句號違規 | 0 | **0** | ✅ |
| E41 | `[...]`／`'...'`／`<...>` UI 標籤 | 0 | **0** | ✅ |
| E42 | `$…$` 之列 | 全數可回溯 v5「解得」 | **2 名，皆解得** | ✅ |
| E43 | PENDING 格式 | 全為 `PENDING: DR-VT4 <名>` | **本批 0 處**（理由見 §五） | ✅ |
| E44 | reasoning | 每 req_id 一則、繁中、2–5 句、含切分依據 | **10 則，4–5 句** | ✅ |
| E45 | modal 於 ER／test_item 下半 | 0 | **0** | ✅ |
| E51 | Remarks provisional 註 | 10/10 齊 | **10/10** | ✅ |
| E52 | W-A 對應結果明判 | 成立／不成立，逐字引標題 | **不成立**（§一） | ✅ 已明判 |

**§四升級條件皆未觸**：W-A 未以語意猜測強行對應（判不成立）；11 個 TC 之 D 欄全為 `Sys-RA-VF665_V43_VSM-{nnn}` 實名。

## 一、W-A —— 章節對應實測：**不成立**

### 實測程序（V42 W-8 同法：styles outline）

`sources/raw/vf665_v43_spec_r4/…R4.docx` → `word/document.xml`，1781 個非空段落。
`word/styles.xml` 實測六個標題樣式之 `outlineLvl`：

| pStyle | name | outlineLvl | numId | 段落數 |
|---|---|---|---|---|
| `1` | heading 1 | 0 | 1 | 1 |
| `21` | heading 2 | 1 | 1 | 17 |
| `31` | heading 3 | 2 | 1 | 25 |
| `41` | heading 4 | 3 | 1 | 4 |
| `51` | heading 5 | 4 | 1 | 68 |
| `6` | heading 6 | 5 | 1 | 11 |

### 判定：**不成立**（兩個理由，皆為實測）

**理由一：規格標題不帶字面章節號。**
實測「標題段落之文字以 `數字.數字` 起首」者 **0 個**；標題段落亦**無 `<w:numPr>`**
（編號來自 style 之 `numId=1` 多階清單，由 Word 算繪）。
故「查 `1.11.1.1.26` 一節之標題」**無字面可查** —— 章節號須由大綱階層重建，
而重建是推算，不是逐字讀取。

**理由二：即使重建，也對不上。**
以 `outlineLvl` 之兄弟序推算（`1.11.1.1.*` 共 **42** 節）：

| 推算章節號 | para | 標題（逐字） |
|---|---|---|
| `1.11.1.1.24` | 971 | `Nav Turn by Turn` |
| `1.11.1.1.25` | 976 | `PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2` |
| **`1.11.1.1.26`** | 1016 | **`Auto High  Beam`** |
| `1.11.1.1.27` | 1027 | **`Interior Ambient Lights`** |
| `1.11.1.1.28` | 1048 | `Rearview Camera Dynamic Gridlines` |

**推算之 `1.11.1.1.26` 為 `Auto High  Beam`，不是 Ambient/Interior Ambient Lights。**
`Interior Ambient Lights` 落在 `1.11.1.1.27`。

### 偏移之旁證（**列出，不據以對應**）

SYSRA `chapter_for_vf` 與推算章節號比對，呈**系統性 +1 偏移**：

| SYSRA `chapter_for_vf` | 該組內容（自 Description 讀） | 推算之同號規格節 | 推算之 +1 節 |
|---|---|---|---|
| `01.11.01.01.24` | `CAN node 24 (PAM)` 之 Park Sense | `Nav Turn by Turn` | `PARK SENSE w/o HC.1…` ✓ |
| `01.11.01.01.25` | `AHBM_Feature_Menu` | `PARK SENSE…` | `Auto High  Beam` ✓ |
| `01.11.01.01.26` | **Ambient**（本 pilot） | `Auto High  Beam` | `Interior Ambient Lights` ✓ |
| `01.11.01.01.27` | `CAN Node 35 (TBM)`／`Geolocation_Menu` | `Interior Ambient Lights` | `Geolocation` ✓ |

**四組皆吻合 +1。但確立此偏移須靠「內容語意相符」**（Ambient 對 Ambient），
**而 07 包 §四明列「W-A 若需語意猜測方能對應 → 列不成立，不猜」**。
故本包**不寫 spec 錨**，只寫 Sys-RA 錨；偏移證據列此交分析層／Pei 裁（§六 K-1）。

## 二、W-B —— `generated/b1_ambient/`

母體：`data/leaves_interim.tsv` 之 `chapter_for_vf = 01.11.01.01.26`，**10 列**。
產出：每 leaf 一 `.json` ＋ 一 `.md`（人讀形），另 `INDEX.md`。

| req_id | TC 數 | tc_title | PENDING |
|---|---|---|---|
| `Sys-RA-VF665_V43_VSM-651` | 1 | Ambient Lights Level menu shown when function present and dimmer absent | 0 |
| `…-652` | 1 | Ambient lighting level 1 request sent on user selection | 0 |
| `…-653` | 1 | Ambient lighting level 2 request sent on user selection | 0 |
| `…-654` | 1 | Ambient lighting level 3 request sent on user selection | 0 |
| `…-655` | 1 | Ambient lighting level 4 request sent on user selection | 0 |
| `…-656` | 1 | Ambient lighting level 5 request sent on user selection | 0 |
| `…-657` | 1 | Ambient lighting level 6 request sent on user selection | 0 |
| `…-658` | 1 | Ambient lighting level 7 request sent on user selection | 0 |
| `…-659` | 1 | Ambient light information updated on reception of level message | 0 |
| `…-661` | **2** | Ambient Lights Level menu hidden when function absent／…when dimmer switch present | 0 |
| **合計** | **11** | | **0** |

### 訊號處置（v5 事實表 ＋ `val_tables_v43.tsv`）

| 規格原名 | v5 結果 | 本批寫法 |
|---|---|---|
| `TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req` | **解得** | `$…$ = <raw> (<label>)`；`<label>` 逐字取 VAL_（`0=Level_1`…`6=Level_7`） |
| `IPC_VEHICLE_SETUP.AmbientLightingLevel` | **解得** | 同上（-659 之注入步） |
| `Ambient_Lighting_Function`／`Ambient_Dimmer_Switch` | PROXI路徑 | `PROXI <Param> = <值>` 入 Pre-Condition（IN §8.7.5(c)，不加 `$`） |
| `Ambient_Lighting_level_Setting.Req` | 未解得(止於段1) | **走 UI 路徑**（R-P375(b)／R-VL21(a)），見下 |
| `TLM_Vehicle_Setup_Menu.Info` | 未解得(止於段1) | **走 UI 觀察面**（R-P353 白名單 (ii)），見下 |

**UI 元件名之來源（入 Remarks）**：取規格 `1.11.1.1.27` para 1029 逐字
`the Interior Ambient Lights Level menu item` → UI 標籤 `"Interior Ambient Lights Level"`。
HMI Settings List `Settings` **r488C** 另載 `"Interior Ambient Lighting*"`，
其 `Technical Reference` = **`VF665`**（字面，非 `VF230/665`）、template `-/+ selector with value in middle`、
options `0-6`（＝ 7 級，與規格 Level_1–Level_7 一致）。
**兩名不同，依 IN §8.6「Source spec wins」取規格名**，HMI 錨列 Remarks。

### D 欄與 Remarks（R-VT18(c)）

D 欄（`specification_reference`）全 11 條 = `Sys-RA-VF665_V43_VSM-{nnn}`（一 ID 一行）。
Remarks 逐 leaf 起首為 `Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1)`，
其後以 `; ` 續接該列之他註（raw↔VAL_ 對照、UI 名來源、ELSE 分支說明）。

### `test_item` 上半之逐字保證

**上半一律自 `data/leaves_interim.tsv` 之 `title_source_description` 直接取用，不經任何重組。**
複驗：10 leaf ×（`test_item_verbatim` ＋ 各 TC 之 `test_item` 上半）與 TSV **逐字全等，不符 0**。

> **執行層自誤（已修正，記明）**：初版以模板重建該逐字欄，產生
> `equal to "Level_Level_ 3 "` 之訛誤（模板之 `Level_{v}` 與值 `Level_ 3 ` 重疊）。
> 逐字欄不得經任何重組 —— 已改為直接取用並加逐字複驗斷言。

## 三、W-C —— 自檢

E38–E45／E51／E52 見 §〇（全通過）。另附機讀項：

| 項 | 實測 | 判 |
|---|---|---|
| `design_method` 皆屬 `下拉選單` 九詞 | 等價劃分 5／邊界值分析 2／負向測試 2／決策表 1／功能測試 1 | ✅ |
| IN §10.5 每 TC ≥2 步 | 最小 **2** | ✅ |
| Procedure ↔ ER 1:1（IN §6） | 全 11 條相等 | ✅ |
| `input_test_data` 全 `NA`（profile 6） | 11/11 | ✅ |
| D 欄皆 Sys-RA 實名 | 11/11 | ✅ |

**`lint036.py` 不適用**：其 positional 參數為 `.xlsx`（`usage: lint036.py … FILES [FILES ...]  一個或多個 .xlsx 路徑`），
不吃 `generated/` 之文字形。依 V42 05 包 W-3 之明文「不支援則記明並以自檢表代」，
本包以上表與 `INDEX.md` 之自檢彙總代之。**未寫任何 xlsx。**

### IN §9 十七項之人判部分（機讀不到者）

| # | 項 | 自評 |
|---|---|---|
| 1 | Test Set 名詞片語、對得上 framework | `Interior Ambient Lighting`＝ R-VT19 十六組之第 10 組，逐字一致 |
| 2 | tc_title 3 型之一、2–14 words、sibling token 可見 | 全 11 條 8–12 words；level 族之 sibling token 為 `level N` |
| 3 | Pre-Condition 只收狀態 | PROXI 組態 ＋「選單項可達」；**無步驟控制態**（R-VL21(f) 之教訓） |
| 5／6 | 步驟可執行、Final Step 擁驗證 | 每條末步為讀值／讀選單並比對 |
| 7 | 標準片段 | 本 feature 尚無 `ENTER_<STATE>` 類片段，未套 |
| 9 | baseline | -659 以「起始 Level_1 → 注入 Level_3」使更新可觀察，未用 `_initial/_after` 記法（單次比對足夠） |
| 11 | supported 配 negative | -651（正）↔ -661（負，2 條） |
| 12 | 追溯、尊重上游分解 | 一 SYSRA 列一需求單位，未分解未合併（R-VT18(d)） |
| 13 | design_method 於 procedure 定案後指派 | 是 |
| 16 | `specification_reference` 列出直接驗證之節 | 暫代期只列 Sys-RA 錨（R-VT19(b)） |
| 17 | 來源規格勝過索引匯出 | UI 名取規格而非 HMI 清單（§二） |

## 四、W-D —— E40 詞界重算

以詞界 `(?<![A-Za-z0-9_.])<名>(?![A-Za-z0-9_.])` 重掃 295 列，取代上繳 06 之子串比對：

| 項 | 子串（上繳 06） | **詞界（本包）** | 差 |
|---|---|---|---|
| 含 v5 訊號名之列 | 263 | **262** | −1 |
| **含「解得」訊號之列** | 126 | **126** | **0** |
| 含解得占 295 | 43% | **43%** | **不變** |

**兩法有差之列 14 條**，全為子串多配（前綴／後綴假陽性），例：
`Cornering_Light` 配到 `Cornering_Lights`、`Rain_Sensor` 配到 `Rain_Sensor_Sensibility` 型、
`SERVICE_SETUP.PrivacyMode` 配到 `TELEMATIC_SERVICE_SETUP.PrivacyModeReq`、
`TLM_Display.GUI` 配到 `TLM_Display.GUI…`。

> **結論：交付說明之 43% 成立，不需修正。** 14 條差異全落在「含訊號」一欄，
> 且皆為未解得之名，故不影響「含解得」之計數。上繳 06 §八-4 所稱之「上界」風險已排除。

## 五、PENDING 清單 —— **本批 0**

兩個內部訊號皆未掛 `PENDING: DR-VT4`，理由逐一：

| 內部訊號 | v5 | 本批處置 | 依據 |
|---|---|---|---|
| `Ambient_Lighting_level_Setting.Req` | 未解得(止於段1) | Procedure 寫 `Select "Interior Ambient Lights Level" = "Level_N"` | R-P375(b) UI 路徑；R-VL21(a)「規格具名即非臆造、可執行即非 PENDING」。規格 para 1029/1030 明載該選單項與使用者設定動作 |
| `TLM_Vehicle_Setup_Menu.Info` | 未解得(止於段1) | ER 觀察具名選單項之顯示值，不寫該訊號名 | R-P353 白名單 (ii)；規格 para 1045 同句明載「updates the Ambient light information **on its display** through … internal signal」，顯示面即其效果面 |

> **這不是把 DR-VT4 的缺口變不見。** 本 Test Set 恰好兩個內部訊號都有規格具名之
> UI 驅動面與觀察面，故可執行。**其餘 15 組未必如此** ——
> 全母體 88 名內部訊號中，能循此路者需逐組實測，不得由本批推廣。

## 六、§K —— 交裁

| # | 項 | 執行層處置 | 待裁 |
|---|---|---|---|
| **K-1** | W-A 判不成立，但 SYSRA `.24`〜`.27` 對推算章節號呈**系統性 +1 偏移**（四組內容皆吻合） | 不寫 spec 錨（§四「不猜」） | 是否認可 +1 偏移為 R-VT19(b) 所稱之「逐章實測」？若認可，本批 11 條可加 spec 錨 `…_VF665_V43_R4_1.11.1.1.27`；若不認可，暫代期一律只寫 Sys-RA 錨 |
| **K-2** | `-661` 出 **2** 條（ELSE 之兩個否定支，依 -651 合取式之德摩根律讀出） | 出 2 條並於 `split_reason`／`reasoning` 揭露 | 是否應合為 1 條？規格之 ELSE 未逐一列舉否定支 |
| **K-3** | 規格與 SYSRA 之拼字瑕疵：`TLM shal set`（缺 `l`）、規格側 `THENTLM`（缺空格）、值 `"Level_ 1 "`／`"Level_ 3 "`（多空格，同族其餘為 `"Level_N "`） | `test_item` 上半逐字保留（R-6／R-13） | 是否併入 DR-VT2 之上游拼寫清單 |
| **K-4** | DBC `VAL_` 有 **16** 級（`0=Level_1`…`15=Level_16`），規格只述 **7** 級，HMI 清單 options `0-6` | 只生成規格所述之 7 級，未擴至 16 | 規格與 DBC 之值域差異是否需上問（Level_8–16 是否本 VF 不適用） |

## 七、anomaly／DR

**本包無新登 anomaly。** §六四項皆為待裁事項（K），非異常；
§二之逐字訛誤為執行層自誤，已於同包內修正並加斷言，依 A-VT15 同型處理但不另立號
（未進入任何上繳數字，且已有防再犯之機制）。

| DR | 狀態 | 本包 |
|---|---|---|
| DR-VT1 | Pei 裁送出，**待發**（執行層未代發） | 重錨註記已逐列落於 Remarks |
| DR-VT2 | 建議併送 | **新增佐證 K-3**（`shal`／`THENTLM`／`"Level_ 1 "` 多空格） |
| DR-VT3 | 暫持 | 未變 |
| DR-VT4 | 先不送 | **本批 0 PENDING**（§五）；全母體 88 名之缺口不變 |

---

## 八、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 505
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **505**。將本包產出（`generated/b1_ambient/` 21 檔與本檔）移出樹外後重跑**仍為 505** |
| `rulings_hash` | **相關，為預期狀態** | R-VT11–R-VT19 九條未入台帳；重生歸 Pei 提交前一次（R-VT14(c)） |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`／`driver_distraction`／`ics_management`／`lint_docs036` |
| `lint_paths` | **無關** | 紅項全在 `driver_distraction/workbook/`、`ics_management/delivered/`、`sw_update/delivered/`。本包新增之 `generated/b1_ambient/*` 未判紅 |

---

## 九、獨立判斷

1. **K-1 是本包最該先裁的一項，因為它影響全母體 295 條而非只有這 11 條。**
   +1 偏移之證據強（四組連續吻合，且每組內容與標題語意一一對應），
   但確立它需要「內容相符」這一步，而那正是 §四禁止的語意猜測。
   **若認可，295 條全部可加 spec 錨；若不認可，暫代期全案只有 Sys-RA 錨** ——
   對交付本之 `Specification Reference` 欄影響是全有或全無。
   **建議認可，但以「逐章列表」形式一次驗完 42 節再鎖**，而非逐包零星判斷。

2. **本批 0 PENDING 是這個 Test Set 的運氣，不是 DR-VT4 缺口的縮小。**
   Interior Ambient Lighting 的兩個內部訊號恰好都有規格具名之 UI 面。
   我特意在 §五把理由逐條寫出，就是為了**避免下一批照抄「內部訊號都能走 UI」**。
   其餘 15 組要逐組實測；88 名的缺口一名未減。

3. **`test_item` 逐字欄我犯了一次錯，值得留為制度教訓。**
   用模板重建逐字欄，產生了 `Level_Level_ 3 `。
   這類錯誤**不會被任何 E 項攔下**（E39 只看括號下半、E40 看句號），
   是我自己逐條讀輸出才發現。
   **已改為直接取用 TSV ＋ 逐字全等斷言**（10/10 通過）。
   建議此斷言納入往後每一生成包之固定自檢項。

4. **W-D 的結果是「不需修正」，但那不表示 06 包的揭露多餘。**
   43% 不變是因為 14 條差異全落在未解得之名上 —— 這是巧合而非必然。
   若換一批訊號名（例如短名多、前後綴共用多者），子串與詞界之差可能落在解得側。
   **詞界比對應成為預設**，不是本包一次性的修正。

5. **本包未驗而下放包亦未要求者**：
   (a) `-659` 之注入值 `Level_3` 為我所選（規格未指定注入哪一級），
       其選擇理由（與起始值相異以使更新可觀察）已入 reasoning，但**選值本身是設計決定**；
   (b) 規格 para 1046 之 `ELSE` 與 para 1028 之 `IF` 之對應範圍未逐字驗證
       （ELSE 是否涵蓋整節或僅最後一個 IF），K-2 之兩條切分即繫於此；
   (c) DBC `GenSigSendType` 於本批兩訊號之值未查（R-VT17(d)：037 到件後首包併查），
       故 Procedure 未依 SendType 決定是否需 `Hold`。

---

## 十、禁區遵守聲明

| 禁區 | 遵守 |
|---|---|
| 00 包 §零 1／3／4 | git 未動；未寫 profiles；`sources/raw/` 唯讀 |
| 00 包 §零 2 | 未寫 `vehicle_setting`／`vsm_v42`；**讀** `vsm_v42` 之 05 包與 R-VL21（07 包 §一-6 明令沿用） |
| 00 包 §零 5′（R-VT18(b)） | TC 母體為 SYSRA 暫代 295 之第 10 組，合規；隔離之 171／41 未入 |
| 00 包 §零 6 | **未代發任何 DR** |
| V42 05 包 §零 1 | **未開 `sandbox/base/`**（連唯讀都未開） |
| V42 05 包 §零 2 | 未生成 pilot 家族以外之 TC |
| V42 05 包 §零 3 | 工作簿欄位全 English；`reasoning` 繁中 |
| V42 05 包 §零 4 | 語意不明處未補洞 —— 列 §K（K-1／K-2／K-4） |
| 07 包 對象限制 | **未寫工作簿、未寫 `delivered/`** |

本包寫入之檔（全在 `features/vsm_v43/` 之下）：
`generated/b1_ambient/`（10 × `.json` ＋ 10 × `.md` ＋ `INDEX.md`，共 **21** 檔）、
`docs/upstream/07_pilot_ambient.md`。
`data/`、`framework.md`、`DECISIONS.md`、`ANOMALIES.md`、`RULINGS.md`、`DATA_REQUESTS.md`、
`sandbox/`、`forms/`、`sources/`、`docs/fw036/`、`docs/runtime/`、`scripts/` **未寫入**。

---

## 十一、下一步

1. **分析層／Pei 覆核 b1_ambient 11 條**（pilot 之人判閘，FO 之第 1.1 節第 2 層）
2. **裁 §六 K-1〜K-4** —— K-1 影響全母體 295 條之 spec 錨，建議一次驗完 42 節再鎖
3. Pei：發送 DR-VT1（併 DR-VT2，K-3 為新佐證）；台帳重生（R-VT11–R-VT19 九條）
4. 覆核通過後：其餘 15 組之生成包；寫回工作簿待分析層覆核與 Pei 再授權（同 V42 R-VL20）
5. 037 到件 → 逐 TC 重錨（舊→新 ID 對映表隨包）→ **重錨完成前不得交付**（R-VT18(c)）
