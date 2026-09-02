# 上繳包 13 — vsm_v43：b2-2 生成　Side Distance Warning（10 leaf）

日期：2026-09-02　執行層　對應下放包：`docs/handoff/13_b2_sdw.md`
產出止於 `generated/`；**未寫工作簿、未動 `sandbox/base/`、已凍 b1／b2-1 一位元未動**。
台帳不重生；DR 不代發。**綠色通道計數第二批。**

---

## 〇、一句話結論

**10 leaf → 10 TC，E 全項通過；K-17 補 6 組，`none` 77 → 71。**
**另更正上繳 12 §五之一項誤判（重音類佐證撤回 2 筆）與一項執行層疏漏（R-VT23(d) 改名未寫回資料檔）。**

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E38 | 覆蓋 | 10 leaf 各 ≥1 TC | **10/10** | ✅ |
| E39 | R-S4 括號下半 | 每 TC 有；不逐字相同 | **10/10；重複 0** | ✅ |
| E40／E41／E45 | 尾句號／`[...]`／modal | 0 | **0／0／0** | ✅ |
| E42 | `$…$` 可回溯 v5 解得 | 全數 | **4 名，皆解得** | ✅ |
| E43 | PENDING | 格式齊 | **本批 0**（逐一實測，見 §四） | ✅ |
| E44 | reasoning | 繁中 2–5 句 | **10 則，各 4 句** | ✅ |
| E51 | Remarks provisional | 10/10 | **10/10** | ✅ |
| E56 | test_item 上半逐字全等 | 對 v2 | **10/10** | ✅ |
| **E88** | K-17 重試 | 命中補、仍 none 列出 | **補 6 組**；`none` **77 → 71** | ✅ |

## 一、先行更正兩項（**執行層自誤，本包修**）

### 更正 1 —— R-VT23(d) 之改名未寫回資料檔（11 包之疏漏）

`leaves_interim_v2.tsv` 之 `test_set` 仍為舊名 `Side and Blind Spot Warnings`（16 列），
**改名只落到 `framework.md` 之表，未寫回資料檔**。
13 包 §二-1 令「母體 = `test_set = Side Distance Warning`」時實測得 **0 列**，才發現。

**修**：16 列（`active` 10 ＋ `deprecated_r4` 6）之 `test_set` 一律改為 `Side Distance Warning`。
改後有效母體 19 組合計仍 **325**，`Side Distance Warning` = **10**，舊名殘留 **0**。

> **成因**：11 包 W-2 之改名施於計數用之本地副本（`eff`），而 TSV 早於該步寫出。
> **這類「報告與資料檔不一致」不會被任何 E 項攔下** —— 與 A-VT15／A-VT23 同型。
> **建議**：凡條文規定之欄位改名，上繳包須附「資料檔實測值 = 條文值」之斷言。

### 更正 2 —— 上繳 12 §五之「重音變體」誤判，撤回 2 筆 DR-VT2 佐證

12 包報 `.10` `DRL_Menù_Enable` 與 `.11` `Greeting_Lights_Menù` 為「上游拼法變體（重音 `ù` vs `Menu`）」。
**該判斷錯誤。** 實測規格 `1.14.1` 表內之名**同樣帶重音**：

| ID | 規格表內之名（逐字） | SYSRA 之名（逐字） | 判 |
|---|---|---|---|
| 12 | `DRL_Menù_Enable` | `DRL_Menù_Enable` | **完全相同，非變體** |
| 13 | `Greeting_Lights_Menù` | `Greeting_Lights_Menù` | **完全相同，非變體** |

**真正的成因是我的表格解析式排除了非 ASCII**：
12 包用 `^[A-Za-z][A-Za-z0-9_ ()/]{2,}$` → 解析出 **38** 對；
本包改為 `^[A-Za-z][\w \-()/À-ɏ]{2,}$` → **40** 對（多出 ID 12／13 兩個帶重音者）。
**故 12 包報之「38 對」偏低 2 對，`.10`／`.11` 之無命中是我的抽取式所致，不是上游拼法問題。**

**DR-VT2 之佐證更正**：12 包所報之 5 筆拼法變體，**撤回 2 筆**（`.10`／`.11`），
**維持 3 筆**（皆為空白類，非重音）：

| chapter | SYSRA | 規格表 | 差異 |
|---|---|---|---|
| `.02` | `Odo_Units Change` | `Odo_Units_Change` | 空格 vs 底線 |
| `.15` | `Remote_Door_Unlock _Menu` | `Remote_Door_Unlock_Menu` | 多一空格 |
| `.16` | `Sound_Horn_Remote_Start _Menu` | `Sound_Horn_Remote_Start_Menu` | 多一空格 |

`.17` `Horn_Chirp_Menù` vs 表 ID 19 `Horn_Chirp_Menu` —— **此筆為真重音變體，維持**（合計 **4 筆**）。

## 二、本批母體與規格節

母體：v2 之 `test_set = Side Distance Warning` 且 `status = active`，**10 列**
（`chapter .05`，`spec_section 1.11.1.1.5`，含解得 8）。規格節 para 555–577 已切出。

| 規格段 | 內容 | leaf |
|---|---|---|
| 556–557 | PROXI `Absent` → 不顯示 | `-440` |
| 558–559 | PROXI `Present` → 顯示 `"Setting"` 與 `"Chime Volume"` 兩子項 | `-441` |
| 561–566 | Setting 三選項之送出 | `-443`／`-444`／`-445` |
| 567–568 | 收訊 `IPC_VEHICLE_SETUP.Sdw` → 顯示更新 | `-446` |
| 570–575 | Chime Volume 三音量之送出 | `-448`／`-449`／`-450` |
| 576–577 | 收訊 `IPC_VEHICLE_SETUP.SdwChimeVolume` → 顯示更新 | `-451` |

**兩個收訊面依 13 包 §二-2 分列不併**（`-446` 對 `-451`）：訊號、選單項、值域三者皆不同，
`distinguishing_axis` 逐條標明（`reception arc = Sdw` ／ `= SdwChimeVolume`）。

## 三、產出（`generated/b2_sdw/`，21 檔）

| req_id | tc_title | design_method |
|---|---|---|
| `-440` | Side Distance Warning menu hidden when parameter absent | **負向測試**（-441 之負向配對，§7） |
| `-441` | Side Distance Warning setting and chime volume menus shown when present | 決策表 |
| `-443`／`-444`／`-445` | …request sent for off／sound／sound plus display selection | 等價劃分 |
| `-446` | …display updated on reception of setting message | 功能測試 |
| `-448`／`-450` | …chime volume request sent for low／high selection | **邊界值分析**（值域兩端） |
| `-449` | …chime volume request sent for medium selection | 等價劃分 |
| `-451` | …display updated on reception of chime volume message | 功能測試 |

Priority 全批 `P1`（同 b2-1 之理由：組態一個碰撞告警功能之行為）。
雙錨前綴逐字用 R-VT26(b) 之 canonical 串
`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4`，**10/10**。

### `<label>` 與規格值不同者（逐列揭露）

`-445` 之規格值為 `"Sound+Display"`，而 DBC `VAL_` 之 label 為 **`Sound_Display`**（raw 2）。
依 **R-7**，`<label>` 逐字取 DBC；`test_item` 上半保留規格拼法。**該差異已入該列 Remarks。**

## 四、PENDING —— 本批 **0**，逐一實測（不沿用前批，R-VT20(d)）

| 內部訊號 | v5 | 本批實測之 UI 面 | 判 |
|---|---|---|---|
| `Sdw_Setting.Req` | 未解得(止於段1) | 規格 **para 559** 逐字具名 `"Setting"` 子項（Side Distance Warning 之下）；選項值由 para 561–566 逐字給出 | **可走 UI 路徑** |
| `Sdw_Chime_Volume_Setting.Req` | 未解得(止於段1) | 規格 **para 559** 具名 `"Chime Volume"` 子項；**HMI Settings List r316B `"Side Distance Warning Volume"`，選項 `Low / Medium / High `（TR `CFTS019`）** 為錨 | **可走 UI 路徑，有 HMI 錨** |
| `TLM_Vehicle_Setup_Menu.Info` | 未解得(止於段1) | 規格 **para 568／577** 同句載「on its display」 | **ER 觀察具名選單項**（R-P353 (ii)） |

父選單名 `"Side Distance Warning"` 之錨：**HMI r315B**，TR `VF230/665`。

> **UI 標籤全部取自規格引號內之逐字字串**（`"Setting"`／`"Chime Volume"`／`"Side Distance Warning"`），
> 未自行組合成 `"Side Distance Warning Setting"` 一類之新名（那會是臆造）。
> 子項之脈絡由 Pre-Condition 之「under `"Side Distance Warning"`」承載。

## 五、K-17 順做（E88，R-VT26(c)）

比對鍵加 **Unicode 去重音 ＋ 空白／底線正規化**（`[\s_]+` → `_`，小寫）；
**限比對鍵，未改任何 verbatim 內容**。

| chapter | SYSRA 之名 | 結果 | 對應節 |
|---|---|---|---|
| `.02` | `Odo_Units Change` | **唯一命中** | `1.14.2.1.2` |
| `.10` | `DRL_Menù_Enable` | **唯一命中** | `1.14.2.1.10` |
| `.11` | `Greeting_Lights_Menù` | **唯一命中** | `1.14.2.1.11` |
| `.15` | `Remote_Door_Unlock _Menu` | **唯一命中** | `1.14.2.1.13` |
| `.16` | `Sound_Horn_Remote_Start _Menu` | **唯一命中** | `1.14.2.1.14` |
| `.17` | `Horn_Chirp_Menù` | **唯一命中** | `1.14.2.1.15` |
| `.12` | `CAN node 51 (LBSS)` | **仍無命中** | — |
| `.13` | `CAN node 52 (RBSS)` | **仍無命中** | — |

**補 6 組／6 列。** `spec_section_source = k14_param_match_norm`。

`spec_section` 來源分布（v2 336 列）：
`segment_map` **195**／`direct` **42**／`k14_param_match` **22**／`k14_param_match_norm` **6**／`none` **71**（原 99）。

> **`.12`／`.13` 仍無命中是正確結果**：`CAN node 51 (LBSS)`／`52 (RBSS)` 即 R4 修訂說明
> 「`- Deleted ID14 (CAN node 51(LBSS))`」「`- Deleted ID15 (CAN node 52(RBSS))`」所刪者，
> 規格已無其 ID Description 節，該二列於 v2 之 status 亦為 `stale_ref_r4`（K-13）。
> **這是 K-10／K-13／K-14／K-17 四項獨立量測第三次互證。**

## 六、§K

| # | 項 | 待裁 |
|---|---|---|
| **K-18**（新） | HMI Settings List **r315B** `Side Distance Warning` 之 template 為 **`On/Off Checkbox`**，而規格 para 561–566 給三個選項（`Off`／`Sound`／`Sound+Display`） | 與 R-VT26(d) 之 FCW r251 同型（HMI 清單與規格之選項不符）。本案依 IN §8.6 取規格，入 DR-VT2 佐證；是否併同上問 |
| **K-19**（新） | 上繳 12 之 DR-VT2 佐證更正（§一-2）：撤回 2 筆重音誤判、維持 3 筆空白類 ＋ 1 筆真重音 | 確認更正；DR-VT2 附件以本包之 4 筆為準 |
| **K-20**（新，**前瞻**） | **本線之 TC ID 形制與 `lint_delivery_spec` 之判準衝突**：該閘之 `TC_ID_RE = ^NR1L-([A-Za-z]+)-(\d{3})$`，**ABBR 只允字母**；而 R-VT3／R-VT7 所定之 `NR1L-VSM43-{n:03d}` 帶數字 `43`。本輪 vsm_v42 之交付本即因 `NR1L-VSM42-001` 判紅（`scripts/lint_delivery_spec.py:40`） | **本線寫回工作簿並落 `delivered/` 時必然同樣判紅。** 三擇一：(a) 改 lint 之正則允許數字；(b) 改 TC ID 為純字母 ABBR（但 R-VT3 為 Pei 裁，且 `VC` 已為 vehicle_category 所佔，R-G42）；(c) 立基線例外。**建議在寫回批之前先裁**，屆時改 ID 等於全批重編 |

## 七、anomaly／DR

**本包無新登 anomaly**（§一兩項為執行層自誤，已於同包內修正並揭露成因，同 A-VT15 型處理）。

| DR | 狀態 | 本包 |
|---|---|---|
| DR-VT1 | 裁送出，待發 | 未代發 |
| DR-VT2 | 建議併送 | **佐證更正為 4 筆**（§一-2）；**新增 K-18**（HMI r315B 選項與規格不符） |
| DR-VT3／DR-VT4 | 暫持／先不送 | 本批 0 PENDING，DR-VT4 缺口不變 |

---

## 八、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 509
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
**FAIL**  exit 1   lint_delivery_spec FAIL: 基線外判紅 1（掃 5 檔，基線 4 列）

總判：**FAIL** —— 5 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths、lint_delivery_spec
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **509**。將 `generated/b2_sdw/` 21 檔與本檔移出樹外後重跑**仍為 509** |
| `rulings_hash` | **相關，為預期狀態** | R-VT11–R-VT26 十六條未入台帳；重生歸 Pei 提交前一次 |
| `gates_tsv`／`lint_paths` | **無關** | 紅列全屬他 feature |
| `lint_delivery_spec` | **本輪新紅，屬他線** | 紅列為 `features/vsm_v42/delivered/…_VehicleSetupManagementR1Low_20260902.xlsx`（vsm_v42 之交付本，本輪由他線提交）。**但其成因會咬到本線，見 §六 K-20** |

---

## 九、獨立判斷

1. **更正 1 是本包最值得記的一件，因為它幾乎沒被發現。**
   `test_set` 改名只落到 framework 表、沒寫回 TSV，**兩份產物不一致了整整一包**，
   而 11 包的 E82／E83 全綠 —— 因為那些判準都以 TSV 自身為母體，不對條文值。
   是 13 包令我以新名取母體、實測得 0 列才撞上。
   **建議往後凡條文規定之欄位值（組名、狀態、旗標），上繳包加一條「資料檔 = 條文」之斷言。**

2. **更正 2 提醒：`[A-Za-z]` 這種字元類在有重音的語料上是靜默失效的。**
   38 對 vs 40 對，差的兩個剛好就是我報成「上游拼法變體」的那兩個 ——
   **我把自己的抽取缺陷歸咎於上游**，而且寫進了 DR-VT2 的佐證。
   若 DR 已送出，上游會收到兩個不存在的問題。
   這與 A-VT15（`<w:t>` 正則）同型：**字元類寫窄了，錯誤方向是「少抓」，而少抓看起來像資料有問題。**

3. **K-14 ＋ K-17 合計把 `none` 從 99 降到 71，剩下的 71 列結構已清楚**：
   `1.14.01` 表列 35 已有 `1.14.1` 錨（12 包）、`1.13.*` 5 列屬 TBM 側（09 包 K-8）、
   `1.11.1.1.15` 6 列為 deprecated、其餘為命中不足 3 之弱組。
   **沒有一列是「不明原因」** —— 若要再降，需另立方法而非再調參數。

4. **本包未驗而下放包亦未要求者**：
   (a) `-451` 之 `n_signals` 為 3，但其 `Description` 詞界式只應命中 2 名 ——
       該欄沿用 06 包之子串式計數，未以詞界重算（09 包 W-D 只重算了占比二數，未回寫逐列欄）；
   (b) 規格 para 560／569 之 `SDW Setting`／`SDW Chime Volume` 為無編號小標，
       其與 `1.11.1.1.5` 之階層關係未查（非標題樣式），本批未據以切分；
   (c) HMI r316B 之 TR 為 `CFTS019` 而非 `VF230/665` —— 該錨屬他 CFTS 之件，
       本包仍引為 UI 名之旁證，但**未查該 CFTS 是否適用本 VF**。

---

## 十、禁區遵守聲明

| 禁區 | 遵守 |
|---|---|
| 00 包 §零 1／2／3／4／6 | git 未動；未寫 `vehicle_setting`／`vsm_v42`；未寫 profiles；`sources/raw/` 唯讀；未代發 DR |
| 13 包 對象限制 | **未寫工作簿**；**已凍 b1／b2-1 一位元未動**；未開 `sandbox/base/` |
| R-VT26(c) | 正規化**限比對鍵**，未改任何 verbatim 內容（E56 10/10 為證） |

本包寫入之檔：
`generated/b2_sdw/`（21 檔，新）、`data/leaves_interim_v2.tsv`（`test_set` 改名 16 列 ＋ `spec_section` 回填 6 列）、
`data/section_map_114_v43.tsv`（加 K-17 兩欄）、`docs/upstream/13_b2_sdw.md`（新）。
`generated/b1_ambient/`、`generated/b2_fcw/`、`framework.md`、`RULINGS.md`、`DATA_REQUESTS.md`、
`ANOMALIES.md`、`DECISIONS.md` **未動**。

---

## 十一、下一步

1. **b2-3 = Lane Departure Warning 18 leaf**（R-VT25(d) 序位三）——
   **本批為綠色通道第二批，b2-3 零修訂即達 3／3**
2. 裁 K-18（HMI 選項與規格不符，併 R-VT26(d) 同型）與 K-19（DR-VT2 佐證更正）
3. 建議採 §九-1 之「資料檔 = 條文」斷言，納入往後每包固定自檢
4. Pei：發送 DR-VT1（併 DR-VT2，佐證以本包更正後之 4 筆為準）；台帳重生（R-VT11–R-VT26 十六條）
