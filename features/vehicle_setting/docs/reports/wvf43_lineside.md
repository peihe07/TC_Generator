# W-VF43 —— `R-VS59`–`R-VS66` 現行引用之線別判定（R-VF49 階段一）

**只判不改。** 階段二（取代）待核可，且須逐處取代不得全域。

## 0. 錨點（R-VF21 ／ R-VF28：以內容定錨）

| 錨點 | 處 | 期望 | 實測 |
|---|---|---|---|
| 必命中 | `R-VS59` 之引用含 `238` | VF230 | VF230 ✅ |
| 必不命中 | `R-VS59` 之引用含「不寫」 | Part 1 | Part 1 ✅ |
| **鑑別** | `docs/handoff/` 之 Part 1 檔而引用 VF230 線者 | **須排除於取代範圍外** | 5 處，皆為歷史包 ✅ |

> **鑑別錨點之意義**：Part 1 檔名之歷史包內引用 VF230 線條文者確實存在，
> **全域取代必誤傷之**。其於本表範圍外（歷史不追改，R-VF45 二），
> 惟階段二之逐處取代須以其為必不取代之標的。

## 1. 判別依據

**依上下文，非依編號**（V17 §5.2）。各號之兩義主題詞取自
`RULINGS.md` 之條文標題逐字，非本層自擬：

| 號 | VF230 義 | Part 1 義 |
|---|---|---|
| `R-VS59` | B 欄／238／序號／續號 | 委派／不等於不寫／R-VS7(a) |
| `R-VS60` | 併入／vehicle_setting／feature slug／另開 | 跨列引入／A-VS103／Vented_seat |
| `R-VS61` | 素材補入／Pei 執行／搬檔／INPUTS.sha256 | DR-19／匯流排對應／分析所載之名／值未解 |
| `R-VS62` | output/／參考素材／非權威 | DR-8／車型碼／PROXI 表／VC_VEH_LINE |
| `R-VS63` | REF 素材／代用／DBC／專案級 | 編號分線／命名空間 |
| `R-VS64` | W 號改編／W-110／W-115 | 升級門檻／常數 |
| `R-VS65` | token 掃描／DR 波及／掃描定義 | 44 輪／69 包 |
| `R-VS66` | 正規化／Layer 2／複驗／NFKC | 規格明確／實作未見／71 包 |

取上下文 260 字元（前後各半），兩義皆命中或皆不命中者標 **待人工**，**不臆測**。

## 2. 結果：146 處

- **VF230 線 31**
- **Part 1 線 42**
- **待人工 73**

| 檔 | 處 |
|---|---:|
| `RULINGS.md` | 71 |
| `ANOMALIES.md` | 16 |
| `DATA_REQUESTS.md` | 9 |
| `scripts/batch16_w113.py` | 7 |
| `scripts/batch17_w116.py` | 5 |
| `scripts/dr_conflict.py` | 4 |
| `scripts/batch19_w122.py` | 4 |
| `feature.yaml` | 3 |
| `docs/INDEX.md` | 3 |
| `scripts/writability_driver.py` | 3 |
| `scripts/vf230_w119_dr_impact.py` | 3 |
| `scripts/batch18_w119.py` | 3 |
| `scripts/impl_gap_w133.py` | 3 |
| `CROSSLINE.md` | 2 |
| `scripts/screen_source_w112.py` | 2 |
| `scripts/screen_layer_w132.py` | 1 |
| `scripts/batch15_w108.py` | 1 |
| `scripts/vehline_anchor_w115.py` | 1 |
| `scripts/vf230_layer2.py` | 1 |
| `scripts/screen_source_w115.py` | 1 |
| `scripts/vf230_crosscheck.py` | 1 |
| `scripts/carry_test_w133.py` | 1 |
| `scripts/selfcheck_w53.py` | 1 |

### 2.1 VF230（31）

| 檔 | 號 | 內容片段 | 依據 |
|---|---|---|---|
| `feature.yaml` | `R-VS59` | `# R-VS59 —— B 欄「No.#/序號」自 238 起連續遞增。` | 命中 VF230 義之主題詞：B 欄／238／序號 |
| `RULINGS.md` | `R-VS59` | `### R-VS59 —— VF230 之 B 欄序號自 238 起（61 包 §3，**Pei 裁定 2026-08-` | 命中 VF230 義之主題詞：B 欄／238／序號 |
| `RULINGS.md` | `R-VS59` | `R-VS59（VF230 序號基準，Pei 裁定 2026-08-23）` | 命中 VF230 義之主題詞：B 欄／238／序號 |
| `RULINGS.md` | `R-VS59` | `4. F 欄「Test Case ID」兩本 workbook 皆為 0 filled；R-VS59 **不**新增` | 命中 VF230 義之主題詞：B 欄／序號／續號 |
| `RULINGS.md` | `R-VS60` | `### R-VS60 —— VF230 併入 `vehicle_setting`，不另開 feature（61 包 §3` | 命中 VF230 義之主題詞：併入／vehicle_setting／另開 |
| `RULINGS.md` | `R-VS60` | `R-VS60（VF230 之 feature 歸屬，Pei 裁定 2026-08-23）` | 命中 VF230 義之主題詞：併入／vehicle_setting／feature slug／另開 |
| `RULINGS.md` | `R-VS61` | `### R-VS61 —— 素材補入由 Pei 執行（61 包 §3，**Pei 裁定 2026-08-23**）` | 命中 VF230 義之主題詞：素材補入／Pei 執行 |
| `RULINGS.md` | `R-VS61` | `R-VS61（VF230 素材補入，Pei 裁定 2026-08-23）` | 命中 VF230 義之主題詞：素材補入 |
| `RULINGS.md` | `R-VS62` | `### R-VS62 —— `output/` 之證據位階（61 包 §3，**Pei 裁定 2026-08-23**）` | 命中 VF230 義之主題詞：output/ |
| `RULINGS.md` | `R-VS62` | `R-VS62（Pei 先前彙整之證據位階，Pei 裁定 2026-08-23）` | 命中 VF230 義之主題詞：output/／參考素材／非權威 |
| `RULINGS.md` | `R-VS59` | `- 其所含之任何列序，**不**構成 R-VS59 之續號依據` | 命中 VF230 義之主題詞：續號 |
| `RULINGS.md` | `R-VS63` | `### R-VS63 —— 專案級 REF 素材得由 CFTS044 代用（**Pei 裁定 2026-08-23**）` | 命中 VF230 義之主題詞：REF 素材／代用／專案級 |
| `RULINGS.md` | `R-VS63` | `R-VS63（VF230 之 REF 素材代用，Pei 裁定 2026-08-23）` | 命中 VF230 義之主題詞：REF 素材／代用／專案級 |
| `RULINGS.md` | `R-VS64` | `### R-VS64 —— W 號改編追認（62 包 §3，分析層裁定 2026-08-23）` | 命中 VF230 義之主題詞：W 號改編 |
| `RULINGS.md` | `R-VS64` | `R-VS64（VF230 進場之 W 號改編，分析層裁定 2026-08-23）` | 命中 VF230 義之主題詞：W 號改編／W-110 |
| `RULINGS.md` | `R-VS65` | `### R-VS65 —— W-115（DR 波及判定）之輸入改以 token 掃描（62 包 §3，分析層裁定 202` | 命中 VF230 義之主題詞：token 掃描／DR 波及 |
| `RULINGS.md` | `R-VS65` | `R-VS65（DR 波及判定之輸入，分析層裁定 2026-08-23）` | 命中 VF230 義之主題詞：token 掃描／DR 波及 |
| `RULINGS.md` | `R-VS66` | `### R-VS66 —— Layer 2 決定前之前置複驗（62 包 §3，分析層裁定 2026-08-23）` | 命中 VF230 義之主題詞：正規化／Layer 2／複驗 |
| `RULINGS.md` | `R-VS66` | `R-VS66（Layer 2 交集之正規化複驗，分析層裁定 2026-08-23）` | 命中 VF230 義之主題詞：正規化／Layer 2／複驗／NFKC |
| `RULINGS.md` | `R-VS60` | `成因：R-VF2（原 R-VS60）令 VF230 併入 `vehicle_setting`，兩條分析線` | 命中 VF230 義之主題詞：併入／vehicle_setting |
| `RULINGS.md` | `R-VS66` | `理由：R-VF8（原 R-VS66）之逐字正規化不足以達成其自身目的 ——` | 命中 VF230 義之主題詞：正規化 |
| `RULINGS.md` | `R-VS60` | `（R-VS60），單一 feature 內之 Test Group 保持單值，優先於 spec 模組名之` | 命中 VF230 義之主題詞：併入／vehicle_setting |
| `scripts/vf230_w119_dr_impact.py` | `R-VS65` | `依 **R-VS65** 之掃描定義（逐字）：` | 命中 VF230 義之主題詞：掃描定義 |
| `scripts/vf230_w119_dr_impact.py` | `R-VS65` | `"**依 R-VS65 之掃描定義（62 包 §3）。**", "",` | 命中 VF230 義之主題詞：掃描定義 |
| `scripts/vf230_layer2.py` | `R-VS66` | `"""比對用鍵 —— R-VS66 之正規化（W-116）。` | 命中 VF230 義之主題詞：正規化／NFKC |
| `scripts/vf230_crosscheck.py` | `R-VS61` | `"**本輪採 035**，其已在 `inputs/` 內（R-VS61 之補入由 Pei 執行）。", "",` | 命中 VF230 義之主題詞：Pei 執行 |
| `DATA_REQUESTS.md` | `R-VS63` | `**不得代用 CFTS044 之 SYS2** —— 其為該 CFTS 專屬（R-VS63 之末段明排除）。` | 命中 VF230 義之主題詞：代用 |
| `DATA_REQUESTS.md` | `R-VS61` | `補入須依 **R-VS61**（由 Pei 執行；2026-08-23 之免除為單次個案）。` | 命中 VF230 義之主題詞：Pei 執行 |
| `ANOMALIES.md` | `R-VS60` | `| **A-VS124** | **61 包所開之 W-102–W-107 與 DR-27 與 Part 1 既有編號全` | 命中 VF230 義之主題詞：併入 |
| `ANOMALIES.md` | `R-VS66` | `| **A-VS129** **【VF230 線舊制編號，R-VF10 前所開，保留】** | **5 個 `swe_i` | 命中 VF230 義之主題詞：複驗 |
| `ANOMALIES.md` | `R-VS66` | `| **A-VS135** **【VF230 線舊制編號，R-VF10 前所開，保留】** | **W-116／W-11` | 命中 VF230 義之主題詞：正規化 |

### 2.2 Part 1（42）

| 檔 | 號 | 內容片段 | 依據 |
|---|---|---|---|
| `RULINGS.md` | `R-VS59` | `> **【(a) 段之「故不寫」效果經 R-VS59（63 包 §1，Pei 2026-08-23）撤回；原文保留不刪】` | 命中 Part 1 義之主題詞：委派 |
| `RULINGS.md` | `R-VS61` | `> 廢止理由：該判準之前提為「值未解即不可寫」，而 **R-VS61 已否定該前提**。` | 命中 Part 1 義之主題詞：值未解 |
| `RULINGS.md` | `R-VS59` | `> **編號說明（Pei 裁定 2026-08-23）**：下列四條為 **CFTS044 本線**之 R-VS59～R` | 命中 Part 1 義之主題詞：委派／不等於不寫 |
| `RULINGS.md` | `R-VS59` | `### R-VS59 —— 委派不等於不寫（63 包 §1，**Pei 裁定 2026-08-23**；取代 R-VS7` | 命中 Part 1 義之主題詞：委派／不等於不寫／R-VS7(a) |
| `RULINGS.md` | `R-VS59` | `R-VS59（Pei 2026-08-23）` | 命中 Part 1 義之主題詞：委派／不等於不寫／R-VS7(a) |
| `RULINGS.md` | `R-VS60` | `### R-VS60 —— A-VS103 之跨列引入，准（63 包 §2，**Pei 裁定 2026-08-23**）` | 命中 Part 1 義之主題詞：跨列引入／A-VS103 |
| `RULINGS.md` | `R-VS60` | `R-VS60（Pei 2026-08-23）` | 命中 Part 1 義之主題詞：跨列引入／A-VS103 |
| `RULINGS.md` | `R-VS61` | `### R-VS61 —— DR-19：無匯流排對應者，寫分析所載之名（63 包 §3，**Pei 裁定 2026-08` | 命中 Part 1 義之主題詞：DR-19／匯流排對應／分析所載之名 |
| `RULINGS.md` | `R-VS61` | `R-VS61（Pei 2026-08-23）` | 命中 Part 1 義之主題詞：DR-19／匯流排對應／分析所載之名 |
| `RULINGS.md` | `R-VS62` | `### R-VS62 —— DR-8′：車型碼取自 PROXI 表（63 包 §4，**Pei 裁定 2026-08-2` | 命中 Part 1 義之主題詞：DR-8／車型碼／PROXI 表 |
| `RULINGS.md` | `R-VS62` | `> **【經 R-VS62′ 取代，2026-08-23；原文保留不刪，見 R-TM13】**` | 命中 Part 1 義之主題詞：DR-8／車型碼／PROXI 表 |
| `RULINGS.md` | `R-VS62` | `R-VS62（Pei 2026-08-23）` | 命中 Part 1 義之主題詞：車型碼／PROXI 表／VC_VEH_LINE |
| `RULINGS.md` | `R-VS63` | `### R-VS63 —— 編號分線（64 包 §4，分析層裁定 2026-08-23）` | 命中 Part 1 義之主題詞：編號分線 |
| `RULINGS.md` | `R-VS63` | `R-VS63（分析層裁定 2026-08-23）` | 命中 Part 1 義之主題詞：編號分線 |
| `RULINGS.md` | `R-VS62` | `### R-VS62′ —— `$VC_VEH_LINE$` 之值域取 PROXI 表列 466；DR-8′ 撤回（65` | 命中 Part 1 義之主題詞：DR-8／PROXI 表／VC_VEH_LINE |
| `RULINGS.md` | `R-VS62` | `R-VS62′（分析層裁定 2026-08-23，取代 R-VS62）` | 命中 Part 1 義之主題詞：DR-8／PROXI 表／VC_VEH_LINE |
| `RULINGS.md` | `R-VS62` | `R-VS62 原文所列之四碼（`332`／`WS`／`DT`／`HDCC`）**於母體命中 0**，` | 命中 Part 1 義之主題詞：DR-8 |
| `RULINGS.md` | `R-VS60` | `R-VS60 之跨列引入只實作於驅動側，致 batch17 首次自檢報 4 項 R-VS39 違規）。` | 命中 Part 1 義之主題詞：跨列引入 |
| `RULINGS.md` | `R-VS64` | `### R-VS64 —— 升級門檻不得以常數表示（68 包 §1，分析層裁定 2026-08-23）` | 命中 Part 1 義之主題詞：升級門檻／常數 |
| `RULINGS.md` | `R-VS64` | `R-VS64（分析層裁定 2026-08-23）` | 命中 Part 1 義之主題詞：升級門檻／常數 |
| `RULINGS.md` | `R-VS65` | `### R-VS65 —— （69 包 §1，44 輪之條文；46 輪 D-2 補轉錄）` | 命中 Part 1 義之主題詞：44 輪／69 包 |
| `RULINGS.md` | `R-VS65` | `R-VS65（分析層裁定 2026-08-23）` | 命中 Part 1 義之主題詞：44 輪／69 包 |
| `RULINGS.md` | `R-VS66` | `### R-VS66 —— 規格明確而實作未見之處置（71 包 §2）` | 命中 Part 1 義之主題詞：規格明確／實作未見／71 包 |
| `RULINGS.md` | `R-VS66` | `R-VS66（分析層裁定 2026-08-23）` | 命中 Part 1 義之主題詞：規格明確／實作未見／71 包 |
| `RULINGS.md` | `R-VS61` | `而 R-VS61 已否定該前提。R-VS47 之 W1／W2 分界依本條重定。` | 命中 Part 1 義之主題詞：值未解 |
| `scripts/dr_conflict.py` | `R-VS61` | `# **R-VS61（63 包 §3，Pei 2026-08-23）**：無匯流排對應者仍產 TC，` | 命中 Part 1 義之主題詞：DR-19／匯流排對應 |
| `scripts/dr_conflict.py` | `R-VS61` | `"DR-19": ("value", set(), r"(?!x)x", "待覆（性質轉確認，R-VS61；不阻塞）")` | 命中 Part 1 義之主題詞：DR-19 |
| `scripts/dr_conflict.py` | `R-VS62` | `# **R-VS62（63 包 §4，Pei 2026-08-23）**：`VC_VEH_LINE` 之車型碼取自` | 命中 Part 1 義之主題詞：車型碼／VC_VEH_LINE |
| `scripts/dr_conflict.py` | `R-VS62` | `"DR-8": ("value", {"VC_VEH_LINE"}, r"M182|M189|M240", "待送（縮為` | 命中 Part 1 義之主題詞：DR-8／車型碼／VC_VEH_LINE |
| `scripts/writability_driver.py` | `R-VS60` | `# **R-VS60（63 包 §2，Pei 2026-08-23）**：`FR_VS_Cmd_Tlm` 之值域` | 命中 Part 1 義之主題詞：跨列引入／A-VS103 |
| `scripts/writability_driver.py` | `R-VS59` | `**R-VS59（63 包 §1，Pei 2026-08-23）**：委派不免除產出 TC 之義務 ——` | 命中 Part 1 義之主題詞：委派 |
| `scripts/screen_source_w112.py` | `R-VS59` | `**必列**：查得／查無兩數。**查無者即 R-VS59(4) 之 PENDING 標的。**` | 命中 Part 1 義之主題詞：R-VS7(a) |
| `scripts/batch17_w116.py` | `R-VS60` | `"`FR_VS_Cmd_Tlm` 之二條為 R-VS60 跨列引入後首次可寫。",` | 命中 Part 1 義之主題詞：跨列引入 |
| `scripts/vehline_anchor_w115.py` | `R-VS62` | `"""W-115(1)（64 包 §5）—— R-VS62 之真錨點。` | 命中 Part 1 義之主題詞：VC_VEH_LINE |
| `scripts/screen_source_w115.py` | `R-VS59` | `# R-VS59 已廢除 `blocked` 之值；`delegation_lookup.tsv` 尚未同步，` | 命中 Part 1 義之主題詞：委派 |
| `scripts/selfcheck_w53.py` | `R-VS60` | `# **R-VS60（63 包 §2，Pei 2026-08-23）**：`FR_VS_Cmd_Tlm` 之值域准自` | 命中 Part 1 義之主題詞：跨列引入／A-VS103 |
| `DATA_REQUESTS.md` | `R-VS61` | `> **40 輪 D-3（依 R-VS61，63 包 §3）**：**性質由阻塞轉確認，不阻塞。**` | 命中 Part 1 義之主題詞：DR-19 |
| `DATA_REQUESTS.md` | `R-VS61` | `> 依 R-VS61 **仍產 TC**，其值取來源逐字（`STATUS_CCAN3.EngineSts = IDLE_` | 命中 Part 1 義之主題詞：DR-19 |
| `DATA_REQUESTS.md` | `R-VS62` | `## DR-8′（**撤回，不送出** —— R-VS62′，65 包 §1；42 輪 D-3。原文保留 —— R-TM` | 命中 Part 1 義之主題詞：DR-8 |
| `DATA_REQUESTS.md` | `R-VS62` | `> **撤回理由（R-VS62′）**：本 DR 縮限後之三碼（`M182`／`M189`／`M240`）` | 命中 Part 1 義之主題詞：DR-8 |
| `DATA_REQUESTS.md` | `R-VS62` | `> **40 輪 D-3 之縮限（依 R-VS62，63 包 §4，Pei 2026-08-23）**：` | 命中 Part 1 義之主題詞：車型碼 |
| `ANOMALIES.md` | `R-VS62` | `| **A-VS140** | **`$VC_VEH_LINE$` 於 237 leaf 僅 2 處引用，其值為 `WL` | 命中 Part 1 義之主題詞：車型碼／VC_VEH_LINE |

### 2.3 待人工（73）

| 檔 | 號 | 內容片段 | 依據 |
|---|---|---|---|
| `feature.yaml` | `R-VS60` | `# 本 feature 含兩份交付（R-VS60）：` | 兩義皆未命中，須讀全段 |
| `feature.yaml` | `R-VS61` | `# 尋得，惟未補入（R-VS61）且缺 6 個 E-Save leaf。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS63` | `第五條（R-VS63）為 Pei 於同日就 61 包 §6 第 3–5 項另行之裁定。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS63` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS63` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS63` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS63` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS63` | `> **⚠ 本條屬 VF230 線，與主線同號者為不同條文**（R-VS63）。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS62` | `> **編號說明（Pei 裁定 2026-08-23）**：下列四條為 **CFTS044 本線**之 R-VS59～R` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS59` | `VF230 線現行之 `R-VS59`～`R-VS63` 五條，其標題加註` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS63` | `VF230 線現行之 `R-VS59`～`R-VS63` 五條，其標題加註` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS59` | `**引用之義務**：跨線引用時須標線名（如「VF230 線之 R-VS59」）。` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `> 並依 R-VS66(a) 標 `impl_gap`。**(推翻 R-VS51(2) 之部分不變。)**` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `並依 **R-VS66(a)** 標 `impl_gap = <訊號名>`` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `該訊號不在基線 DBC → **標 `impl_gap`，依 R-VS66(a) 照寫、開 issue 予 RD**` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `(d) **DR-25′ 維持撤回** —— 其標的（訊號不在 DBC）依 R-VS66 已非 DR 之事由，` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS59` | `**⚠ 檢查二之「必不命中」錨點於現行全檔即失敗** —— 非錨點有誤，是**真違反**：`R-VS59`–`R-VS6` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `**⚠ 檢查二之「必不命中」錨點於現行全檔即失敗** —— 非錨點有誤，是**真違反**：`R-VS59`–`R-VS6` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS61` | `值無對應而來源有逐字   → `= <來源逐字值>`，**不附 raw**（R-VS61），` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS59` | `R-VF45（R-VS59–R-VS66 撞號之處置，分析層裁定 2026-08-23）` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `R-VF45（R-VS59–R-VS66 撞號之處置，分析層裁定 2026-08-23）` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS59` | `A-VF10 實測：`R-VS59`–`R-VS66` 八號各有兩個定義，兩線皆為 Pei 裁定、` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `A-VF10 實測：`R-VS59`–`R-VS66` 八號各有兩個定義，兩線皆為 Pei 裁定、` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS59` | ``R-VS59→R-VF1 … R-VS66→R-VF8`，並註明` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | ``R-VS59→R-VF1 … R-VS66→R-VF8`，並註明` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS59` | `「歷史文件中之 `R-VS59`–`R-VS66` 可能指兩義之任一，` | 兩義皆未命中，須讀全段 |
| `RULINGS.md` | `R-VS66` | `「歷史文件中之 `R-VS59`–`R-VS66` 可能指兩義之任一，` | 兩義皆未命中，須讀全段 |
| `docs/INDEX.md` | `R-VS59` | `| 34 | — | 母體層冗餘掃描、R-VS57(4) 重跑、產能終局盤點 | [61](handoff/61_rev` | 兩義皆未命中，須讀全段 |
| `docs/INDEX.md` | `R-VS61` | `| 34 | — | 母體層冗餘掃描、R-VS57(4) 重跑、產能終局盤點 | [61](handoff/61_rev` | 兩義皆未命中，須讀全段 |
| `docs/INDEX.md` | `R-VS63` | `| 34 | — | 母體層冗餘掃描、R-VS57(4) 重跑、產能終局盤點 | [61](handoff/61_rev` | 兩義皆未命中，須讀全段 |
| `CROSSLINE.md` | `R-VS59` | `| **R-VF10** | `RULINGS.md`／`ANOMALIES.md` 之編號 | 同一編號不得有兩個定義` | 兩義皆未命中，須讀全段 |
| `CROSSLINE.md` | `R-VS66` | `| **R-VF10** | `RULINGS.md`／`ANOMALIES.md` 之編號 | 同一編號不得有兩個定義` | 兩義皆未命中，須讀全段 |
| `scripts/screen_layer_w132.py` | `R-VS59` | `**D-2 圖示變更類**（72 包 §1 之 R-VS59(4) 細化）：` | 兩義皆未命中，須讀全段 |
| `scripts/writability_driver.py` | `R-VS59` | `# R-VS59：`blocked` 之值廢除` | 兩義皆未命中，須讀全段 |
| `scripts/batch15_w108.py` | `R-VS59` | `"**以 pre_conditions 之階數配置分辨**（R-VS59 前之既有慣例）。",` | 兩義皆未命中，須讀全段 |
| `scripts/screen_source_w112.py` | `R-VS59` | `"""W-112（63 包 §7）—— Comfort 素材之畫面層對照表（R-VS59(2) 之前置）。` | 兩義皆未命中，須讀全段 |
| `scripts/batch17_w116.py` | `R-VS59` | `查無者依 R-VS59(4) 標 `PENDING`。` | 兩義皆未命中，須讀全段 |
| `scripts/batch17_w116.py` | `R-VS59` | `axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"` | 兩義皆未命中，須讀全段 |
| `scripts/batch17_w116.py` | `R-VS59` | `+ ("故依 R-VS59(4) 標 `PENDING: DR-5-B`"` | 兩義皆未命中，須讀全段 |
| `scripts/batch17_w116.py` | `R-VS59` | `"screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-` | 兩義皆未命中，須讀全段 |
| `scripts/vf230_w119_dr_impact.py` | `R-VS65` | `# 掃描面：title ＋ desc（R-VS65）` | 兩義皆未命中，須讀全段 |
| `scripts/batch16_w113.py` | `R-VS59` | `（A-VS116 之標的，本輪因 R-VS59 首次入池）。同序內逐 Layer 2 輪流 ＋ reqid 升冪。` | 兩義皆未命中，須讀全段 |
| `scripts/batch16_w113.py` | `R-VS59` | `故本批之畫面層斷言一律標 `PENDING: DR-5-B`（R-VS59(4)）。見上繳 35 §2.2。` | 兩義皆未命中，須讀全段 |
| `scripts/batch16_w113.py` | `R-VS59` | `"reasoning": (why + "；畫面層依 R-VS59(2) 取自 Comfort 素材，"` | 兩義皆未命中，須讀全段 |
| `scripts/batch16_w113.py` | `R-VS59` | `"故依 R-VS59(4) 標 `PENDING: DR-5-B`"),` | 兩義皆未命中，須讀全段 |
| `scripts/batch16_w113.py` | `R-VS59` | `"selection": "W-111 後之池 **35**（R-VS59 解除 delegate 之扣除）。"` | 兩義皆未命中，須讀全段 |
| `scripts/batch16_w113.py` | `R-VS59` | `"screen_layer": "R-VS59(2) 之來源不足 —— 全 10 條之畫面層斷言標 `PENDING: ` | 兩義皆未命中，須讀全段 |
| `scripts/batch16_w113.py` | `R-VS59` | `"自 R-VS59 撤回 `delegate = blocked` 之扣除後首次入池）。"` | 兩義皆未命中，須讀全段 |
| `scripts/batch18_w119.py` | `R-VS59` | `axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"` | 兩義皆未命中，須讀全段 |
| `scripts/batch18_w119.py` | `R-VS59` | `+ ("，故依 R-VS59(4) 標 `PENDING: DR-5-B`"` | 兩義皆未命中，須讀全段 |
| `scripts/batch18_w119.py` | `R-VS59` | `"screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-` | 兩義皆未命中，須讀全段 |
| `scripts/impl_gap_w133.py` | `R-VS66` | `（`Atlantis` → `*_Cmd_Tlm`，四階）並依 **R-VS66(a)** 標 `impl_gap`。` | 兩義皆未命中，須讀全段 |
| `scripts/impl_gap_w133.py` | `R-VS66` | `+ (f"IMPL_GAP: {tc['impl_gap']} —— 依 R-VS66(a) 照寫，"` | 兩義皆未命中，須讀全段 |
| `scripts/impl_gap_w133.py` | `R-VS66` | `"標 `impl_gap`（R-VS66(a)）；`dr15_exposed` 保留")` | 兩義皆未命中，須讀全段 |
| `scripts/carry_test_w133.py` | `R-VS66` | `(2) 不能承載者 → 取**能承載之欄組**（`Atlantis`），並依 R-VS66(a) 標 `impl_gap` | 兩義皆未命中，須讀全段 |
| `scripts/batch19_w122.py` | `R-VS64` | `**依 R-VS64，本批不寫死條數** —— 池扣除 held_out 後有幾條即取幾條。` | 兩義皆未命中，須讀全段 |
| `scripts/batch19_w122.py` | `R-VS59` | `axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"` | 兩義皆未命中，須讀全段 |
| `scripts/batch19_w122.py` | `R-VS59` | `+ ("，故依 R-VS59(4) 標 `PENDING: DR-5-B`"` | 兩義皆未命中，須讀全段 |
| `scripts/batch19_w122.py` | `R-VS59` | `"screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-` | 兩義皆未命中，須讀全段 |
| `DATA_REQUESTS.md` | `R-VS59` | `> **40 輪 D-3（依 R-VS59，63 包 §6）**：**性質由阻塞轉確認，不阻塞。**` | 兩義皆未命中，須讀全段 |
| …（其餘 13 處見 JSON）| | | |

## 3. 階段二之前提（未執行）

1. **逐處取代，不得全域** —— 鑑別錨點已證誤傷風險為實。
2. **僅取代判為 VF230 線者**，且僅於現行有效之陳述（R-VF45 一）；歷史包不動（R-VF45 二）。
3. **待人工之項須先判**，其不得以任一方向預設。
4. `RULINGS.md` 之永久對照表（R-VF45 三）須同時置入。

