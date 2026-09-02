# 上繳包 05 — vsm_v43：P3 收尾（v5、framework Layer 1 鎖、DECISIONS 準備、P4 預備表）

日期：2026-09-02　執行層　對應下放包：`docs/handoff/05_p3_close.md`
sha8 報 **`body_sha8`**（樹外 `--out`）；台帳**不重生**；**DR 一律不送**。
本線因 DR-VT1 未送**續止於 P0–P3**。

---

## 〇、一句話結論

**§一 五類變動全數落實，E32–E36 六項全部相符。framework Layer 2 依令留白。**

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E32 | v5「解得」 | **81**，全 CAN 形 | **81**，類別 100% CAN | ✅ |
| E33 | B-1／查無(R-G13) | 0／0 | **0／0** | ✅ |
| E34 | v5 合計 | 230 | **230**；五類變動逐項列於 §一 | ✅ |
| E35 | R-VT13–R-VT16 `body_sha8` 與現檔一致 | 一致 | **4/4**（R-VT13–15 與上繳 04 相同，R-VT16 新增） | ✅ |
| E36 | VAL_ 表列數 | 81 | **81**，無 VAL_ 者 **0**，值數合計 **277** | ✅ |

**§五 三項升級條件皆未觸**：E32 = 81、E33 皆 0、framework Layer 2 **空**（0 列）。

## 一、結果三分法（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | v5 五類變動（7 列改判、11 名排除旗標）；framework Layer 1 落檔；DECISIONS 四欄實值；VAL_／SendType 兩張 P4 預備表 |
| 核實無誤 | E32–E36 六項；`解得 81` 全部有 `VAL_`；PROXI 母體扣排除後 **39**（與 R-VT16(c) 同）；E29 寬讀重跑**結果一列未變** |
| 正確地不動 | **framework Layer 2 留白**（05 包 §五 明令）；**不代簽** DECISIONS；台帳不重生；DR 一律不送；v4 不覆寫；`LOOKUP_MISSES.md` 未寫；`forms/FORMS.md` 未補登 P363 DBC（共用件，非本線可為） |

---

## 二、§一 五類變動逐項（v4 → v5）

輸出 `data/signal_chain_v43_v5.tsv`（**v4 不覆寫**）。**逐列 diff 共 7 列改判 ＋ 5 名新增排除旗標。**

### 1. A-VT26 五列 → `未解得(止於段1)`（R-VT16(e)）

| 規格原名 | v4 | **v5** |
|---|---|---|
| `ClearPersonalData.Info` | 解得 | **未解得(止於段1)** |
| `PhoneRepetition.Info` | 解得 | **未解得(止於段1)** |
| `PrivacyMode.Info` | 解得 | **未解得(止於段1)** |
| `RestoreApp.Info` | 解得 | **未解得(止於段1)** |
| `RestoreDefaultSetting.Info` | 解得 | **未解得(止於段1)** |

逐列備註：`【R-VT16(e)】A-VT26 退回：內部形僅段 3 同名，段 1／2 無 LID 依據，不計入「解得」`。
**「解得」86 → 81，對測 E32 相符。** A-VT26 轉 RESOLVED。

### 2. 拼字兩列 → `未解得（規格拼字疑誤）`（R-VT16(d)）

| 規格原名 | v4 | **v5** |
|---|---|---|
| `SERVICE_SETUP.RestoreDefaulSetting`（漏 `t`） | 未解得（CAN-C DBC 未到件） | **未解得（規格拼字疑誤）** |
| `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq`（`m`） | 未解得（CAN-C DBC 未到件） | **未解得（規格拼字疑誤）** |

逐列備註載明：正確拼法之訊號於 P363 DBC 存在且已解；**不擅自更正規格原名**（R-13／R-6）；列 DR-VT2 佐證。

### 3. `PROXI.First` 之抽名脈絡審查 → **偽陽性**（A-VT29）

**實測定位**：Configuration Parameters 表之每一參數列尾隨兩句 ——
`Range value is indicated in the standard PROXI.` 換行 `First Trial Value depends on the project Configuration`。
上繳 02 之 CAN 形正則於段落串接後**跨句配到 `PROXI` ＋ `.` ＋ `First`**；該句於規格出現 30 次以上。

**判定：抽名偽陽性，非訊號名、非 CAN-C 缺口。** v5 設排除旗標（A-VT21 型，標記不刪）。

**CAN-C 缺口收斂**：

| 項 | 值 |
|---|---|
| v4 之 `未解得（CAN-C DBC 未到件）` | 8 |
| 扣拼字 2 列（改記新值） | 6（**＝ R-VT16(d) 所預期之 6**） |
| 再扣 `PROXI.First`（偽陽性） | **真缺口 5** |

**CAN-C 真缺口 5 名**：`IPC_VEHICLE_SETUP.BSDEnable`／`.CorneringLightsEnable`／`.RainSensorLevel`、
`TELEMATIC_VEHICLE_SETUP.BSDEnable_Req`／`.RainSensorLevel_Req`。

### 4. A-VT23 四名設排除旗標（R-VT16(c)）

`LTM`／`TBM`／`Unit`／`Resolution` 設 `排除 = y`。
**排除旗標合計 11 名**（A-VT21 六 ＋ A-VT23 四 ＋ A-VT29 一）。
**PROXI 報表母體 = 49 − 10 = 39**（實測扣除排除後之 PROXI 類 **39**，與 R-VT16(c) 相符）。

### 5. E29 寬讀重跑（R-VT16(b)）—— **新增命中 4 名，結果一列未變**

候選集：`Technical Reference` 含 `665` → **247** 列（字面 `VF665` 3 列為其子集）。

| 規格原名 | v5 結果（**未變**） | 寬讀所得之錨點 |
|---|---|---|
| `Cornering_Lights` | UI路徑(R-P375b) | HMI `Settings` **r501B** `"Cornering Lights"`，TR=`VF230/665` |
| `Auto_Park_Brake_Menu` | UI+PROXI 雙路徑 | **r509B** `"Auto Park Brake"`，TR=`VF230/665` |
| `Greeting_Lights_Menù` | UI+PROXI 雙路徑 | **r494B** `"Greeting Lights"`，TR=`VF230/665` |
| `Side_Distance_Warning` | UI+PROXI 雙路徑 | **r315B** `"Side Distance Warning"`，TR=`VF230/665` |

> **寬讀補的是錨點，不是命中數**（A-VT30）。R-P353(ii) 之具名 UI 元件需要來源錨點；
> 字面讀法下這四名之 HMI 命中來自**全表**，無法證明該設定項屬本 VF；
> 寬讀後其 `Technical Reference` 逐字載明 `VF230/665`。
> **例外一名**：`Geolocation_Menu`（亦為雙路徑）**不在寬讀候選集內**，
> 其 HMI 命中列之 TR 不含 `665` —— P4 引用其 UI 錨點時須另尋依據。

### v4 → v5 結果分布

| 結果 | v4 | **v5** | 差 |
|---|---|---|---|
| **解得** | 86 | **81** | **−5** |
| 訊息名不符(R-13) | 4 | **4** | 0 |
| **未解得（規格拼字疑誤）** | — | **2** | +2 |
| 未解得（CAN-C DBC 未到件） | 8 | **6** | −2 |
| 未解得(止於段1) | 93 | **98** | +5 |
| UI路徑(R-P375b) | 1 | **1** | 0 |
| PROXI路徑(R-P375b/c) | 34 | **34** | 0 |
| UI+PROXI 雙路徑 | 4 | **4** | 0 |
| **B-1 衝突** | 0 | **0** | 0 |
| **查無(R-G13)** | 0 | **0** | 0 |
| 合計 | 230 | **230** | — |

`未解得(止於段1)` 98 之類別：**內部 88**／PROXI 10／CAN 0。
（內部由 83 增為 88，即 A-VT26 之五列歸隊 —— **內部訊號全 88 名皆未解**。）

---

## 三、W-9 —— `framework.md` 落檔

新建 `features/vsm_v43/framework.md`（本 feature 原無此檔）。

- **Layer 1（鎖定）**：`Vehicle Setup Management R1L TBM`（R-VT3）；
  與 `feature.yaml.test_group`、交付檔名之 feature 段一致。
- **Layer 2**：**留白**。本節僅載「無母體、須自 037 家族聚合、不得以 SYSRA 或規格代之、
  DR-VT1 為唯一解且 Pei 現裁先不送」，並明記
  「本節留白是裁決結果，不是待辦遺漏」。**實測該節表格列數 = 0。**
- **附錄（對照用，非依據）**：SYSRA `chapter_for_vf` 前二階分布
  `01.11` **223**／`01.14` **67**／`01.13` **5**，合計 **295**（分母定義見 DR-VT2）；
  第一階恆為 `01`（295/295），無鑑別力。就地標明「不得作為 Layer 2 之依據」。
- **Layer 3**：待 Layer 2 鎖定後回填。

## 四、W-10 —— DECISIONS 四欄實值（**待 Pei 簽，未代簽**）

附於 `DECISIONS.md` 末之「P3 收尾」節：

| # | 項 | 實值 | 依據 | 標記 |
|---|---|---|---|---|
| 1 | `spec_mode` | **D** | 母 spec 為 `.docx`，magic bytes `50 4B 03 04`（上繳 01 E13） | `[PROPOSED]` |
| 2 | `workbook_state` | **BLANK** | 副本第 10 列起、B 欄以外非空儲存格 **0**（掃 1411 列） | `[PROPOSED]` |
| 3 | 母體（037 leaf） | **0，待 037** | R-VT4；037 兩份之 Source Requirement ID 152/152 皆 V42，`V43` 命中 0（E7） | `[PEI]` |
| 4 | framework Layer 1 | **鎖定** | R-VT3 | `[PROPOSED]` |

Sign-off 區塊留空（`Reviewed by`／`Date` 待填）。**Layer 2 不列入本表**（05 包 §五）。

## 五、W-11 —— P4 預備表

### `data/val_tables_v43.tsv`（E36）

欄位：`規格原名 | BO_(訊息) | SG_(訊號) | VAL_ 值數 | VAL_ 列舉（raw=label）`

| 項 | 值 |
|---|---|
| 列數 | **81**（＝ 解得 81） |
| 無 `VAL_` 者 | **0** |
| `VAL_` 值數合計 | **277** |

例：`IPC_VEHICLE_SETUP.AmbientLightingLevel` → 16 值（`0=Level_1 | 1=Level_2 | …`）；
`IPC_VEHICLE_SETUP.AutoHighBeamEnable` → 2 值（`0=Not_Enable | 1=Enable`）。
**P4 之 `<label>` 可逐字取自本表**（IN §8.7.5(a)／R-7），無待補者。

### `data/ba_sendtype_v43.tsv`

欄位：`規格原名 | BO_ | SG_ | GenSigSendType`，**81** 列。

| `GenSigSendType` | 列數 |
|---|---|
| `3` | 42 |
| `1` | 37 |
| `7` | 2 |

> **本表為原始碼值，未經解釋**：DBC 之 `GenSigSendType` 列舉定義未載於本 DBC 之
> `BA_DEF_` 註解中（本包未查得對照）。**不擅自解讀為 Cyclic／OnChange 等語意** ——
> P4 若要據此決定 Procedure 之 Send／Hold 寫法，須先取得該屬性之列舉定義。列為 §七 未竟項。

## 六、E 對照與 sha

### E32–E36

見 §〇 之表（六項全符）。補充量測條件：
E32 之「全 CAN 形」以 v5 之 `類別` 欄計，解得 81 列類別分布 = `{CAN: 81}`；
E34 之 230 為 v3 以降之固定母體（不重抽名）；
E36 之 81 與 E32 同源（VAL_ 表以解得列建）。

### R-VT13–R-VT16 之 `body_sha8`（E35）

| 條號 | `body_sha8` | `sha8`（觀測） | 來源：列 | 本體列數 | 對上繳 04 |
|---|---|---|---|---|---|
| R-VT13 | **`3e332b48`** | `4fd8102d` | `RULINGS.md`:187 | 16 | 相同 |
| R-VT14 | **`8525adfa`** | `747675c1` | 同上:206 | 9 | 相同 |
| R-VT15 | **`9ace16a9`** | `403f6948` | 同上:218 | 15 | **`body_sha8` 相同**；`sha8` 由 `608e336b` 變（錨點區段增註，本體列數 11 → 15） |
| R-VT16 | **`2567b669`** | `a57a8db3` | 同上:236 | 13 | 本包新增 |

> **R-VT15 之 `sha8` 變動不是漂移**：其 `body_sha8` 逐字未變，變的是錨點區段內新增之加註 ——
> 與 R-VT2 於 R-VT6(d) 加註後之情形同型。**R-VT10(a) 之「比 body_sha8」正是為此而設**，本例再次驗證其必要。

`RULINGS.md` 現檔共 **16** 條 R-VT；台帳內 **10** 條（R-VT11–R-VT16 六條未入，待 Pei 重生）。

---

## 七、anomaly／DR 狀態

### 狀態變更

| id | 變更 | 依據 |
|---|---|---|
| A-VT23 | 四名**准入排除清單**，PROXI 母體 39 → **RESOLVED** | R-VT16(c) |
| A-VT26 | 五列退回 `未解得(止於段1)`，解得基線 81 → **RESOLVED** | R-VT16(e) |

### 本包新登

| id | 一句話 | 狀態 |
|---|---|---|
| **A-VT29** | `PROXI.First` 為跨句誤配之抽名偽陽性（`…standard PROXI.` ＋ `First Trial Value…`）；CAN-C 真缺口 6 → **5** | RESOLVED |
| **A-VT30** | E29 寬讀之實效：**不改結果，只補錨點**（4 名取得 `VF230/665` 之 TR 錨點；`Geolocation_Menu` 例外） | RESOLVED |

### DR —— **一律不送**（Pei 裁）

| DR | 阻塞 | 狀態 | 本包實測 |
|---|---|---|---|
| DR-VT1 | **yes（P4）** | 先不送 | 母體 0；framework Layer 2 因此留白 |
| DR-VT2 | no | 先不送 | 新增佐證：拼字兩列已獨立成值域 `未解得（規格拼字疑誤）` |
| DR-VT3 | no | 暫持 | 名單仍 2 名（`SERVICE_SETUP.TelematicSetupACK`／`TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock`） |
| DR-VT4 | **yes（P4 內部訊號）** | 先不送 | **內部訊號 88 名全數未解**（A-VT26 五列歸隊後） |
| DR-VT5 | — | **結案** | R-VT15 |

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
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **505**，與上繳 04 同。將本包全部產出移除（`ANOMALIES.md`／`DECISIONS.md` 還原至 `HEAD`，`framework.md` 與本檔移出樹外）後重跑**仍為 505** |
| `rulings_hash` | **相關，為預期狀態** | 台帳含 R-VT1–R-VT10；**R-VT11–R-VT16 六條未入**。依 R-VT14(c) 台帳重生歸 Pei 提交前一次，本線不重生 |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`／`driver_distraction`／`ics_management`／`lint_docs036` |
| `lint_paths` | **無關** | 紅項全在 `driver_distraction/workbook/`、`ics_management/delivered/`、`sw_update/delivered/`。本包新增之 `data/*.tsv`、`framework.md` 未判紅 |

---

## 九、獨立判斷

1. **P3 已可視為完成，但「完成」的內容比字面小 —— 這點該講清楚。**
   Layer 1 鎖了、profile 落了、訊號鏈事實表定版了（81 列穩解、277 個 VAL_ 值可逐字取）。
   但 **Layer 2 是空的、母體是 0**。P3 交付的是「P4 一啟動就能用的前置」，
   不是「framework 完成」。若日後有人只看 `framework.md` 而未讀 Layer 2 節之說明，
   會誤以為本 feature 只有一個 Test Group —— 該節已就地寫明「留白是裁決結果，不是待辦遺漏」。

2. **內部訊號現在是 88 全滅，不是 83。**
   A-VT26 五列歸隊後，`X.Req`／`X.Info`／`X.GUI` **無一解得**。
   五輪擴充（規則→欄→檔→欄組→DBC）加上這次的判準收緊，數字從 83 走到 88 ——
   **方向是往「更誠實」走，不是往「更糟」走**，但 P4 的代價也隨之明確：
   88 名全部只能寫 `PENDING: DR-VT4 <名>`。DR-VT4 未送，這是既定結果。

3. **`GenSigSendType` 我只抄了值，沒解讀，這是刻意的。**
   `3`／`1`／`7` 三種值各 42／37／2 列。DBC 內未見該屬性之列舉定義，
   而 Cyclic／OnChange 之別會直接改變 Procedure 要不要寫 `Hold for <n> ms`（IN §8.7.5(e)）。
   **猜一個對照表比不做更危險** —— 表已建好，語意待補。

4. **抽名式的跨句誤配是已知缺陷，且不只 `PROXI.First` 一例。**
   A-VT29 定位到的成因（句號 ＋ 換行 ＋ 大寫開頭）是通用的；
   目前 11 個排除名裡至少 7 個屬同型（`Component`／`Impact`／`Implementation`／
   `LTM`／`TBM`／`Unit`／`Resolution`）。
   **05 包未令重抽名，故未動**；但若 P4 要以 v5 為事實表，
   建議先做一次「抽名重跑 ＋ 偽陽性率回報」，否則 230 這個母體始終帶著 11 個雜訊。

5. **本包未驗而下放包亦未要求者**：
   (a) `GenSigSendType` 之列舉定義（§五）；
   (b) `forms/FORMS.md` **仍未登錄 P363 DBC**（sha256 `a51079be…88abd`）——
       R-P368(e)／R-P365(b) 之台帳要求；共用件，非本線可為，連續兩包提及；
   (c) `Geolocation_Menu` 之 UI 錨點無 VF665 標記（A-VT30 例外一名）；
   (d) `Brand-Specific Names` 分頁仍未用（P4 取 UI 實名時用）；
   (e) `LOOKUP_MISSES.md` 未寫（三要件未滿足，本應不寫）。

---

## 十、禁區遵守聲明（00 包 §零）

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 未跑任何 `git` 寫入指令 |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫、未讀 |
| 3. 不寫 `docs/runtime/profiles/` | **未寫** —— `FW036_R1L_VSM_V43_Profile.md` 為分析層落檔，本包**只讀** |
| 4. 不改寫 `sources/raw/` 原檔 | 全程唯讀 |
| 5. 不以 SYSRA 或規格代 037 建母體或生成 TC | **framework Layer 2 留白**；`generated/`／`batches/` 仍空；SYSRA 分布僅列為對照並就地標明非依據 |
| 6. 不自行送 DR | 未送、未改 `DATA_REQUESTS.md` |

本包寫入之檔（全在 `features/vsm_v43/` 之下）：
`framework.md`（**新建**）、`DECISIONS.md`（附 P3 節）、`ANOMALIES.md`（改）、
`data/signal_chain_v43_v5.tsv`（新）、`data/val_tables_v43.tsv`（新）、
`data/ba_sendtype_v43.tsv`（新）、`docs/upstream/05_p3_close.md`（新）。
v1–v4 TSV、`RECON.md`、`feature.yaml`、`RULINGS.md`、`DATA_REQUESTS.md`、
`docs/runtime/profiles/`、`forms/`、`sources/`、`docs/fw036/`、`scripts/` **未寫入**。

---

## 十一、下一步

1. **Pei**：簽 `DECISIONS.md` 之 P3 四欄；commit；台帳重生（R-VT11–R-VT16 六條）；
   `forms/FORMS.md` 補登 P363 DBC 之 SHA；`_intake/` 空目錄刪；共用腳本一裁（六項）
2. **P4 之唯一阻塞**：**DR-VT1（037）** —— 送出前 Layer 2 無從聚合，母體恆為 0
3. **P4 之品質阻塞**：**DR-VT4** —— 未送則 88 名內部訊號全數 `PENDING`
4. 下包（若有）：抽名重跑並報偽陽性率（§九-4）；`GenSigSendType` 列舉定義（§九-3）；
   `Geolocation_Menu` 之 UI 錨點（§九-5(c)）
5. **本線 P3 至此收尾。** 037 到齊 → Layer 2 裁 → P4
