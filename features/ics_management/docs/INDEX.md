# ICS Management — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-29（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| — | 2026-08-29 | 建檔前之偵察與四項判斷（Pei 准①命名②DR 即發③首波動工面④骨架） | **未落檔**（聊天）† | — | R-ICS1 ~ R-ICS4 | A-ICS1 ~ A-ICS7 | — |
| 01 | 2026-08-29 | 建檔與首批 TC（b01，6 條） | [handoff/01_onboarding_first_batch.md](handoff/01_onboarding_first_batch.md) | [upstream/01_onboarding_first_batch.md](upstream/01_onboarding_first_batch.md) | **無**（執行層不代擬） | 建議登錄 4 則（上繳 §十一） | **已審結**（b01 收下不退件；分析層即裁 R-ICS5～8，Pei 裁 R-ICS9／R-ICS10） |
| 02 | 2026-08-29 | 訊號解佔位、ignore 面（b02，2 條）、CFTS020 三面偵察 | [handoff/02_signal_resolution_and_ignore_face.md](handoff/02_signal_resolution_and_ignore_face.md) | [upstream/02_signal_resolution_and_ignore_face.md](upstream/02_signal_resolution_and_ignore_face.md) | **無**（執行層不代擬） | 建議登錄 3 則（上繳 §十二） | **已審結**（b02 收下；即裁 R-ICS11～17 與 R-ICS2 v2）｜註：其 §8 追補未隨包執行，改由 03 之作業 F 補做 |
| 03 | 2026-08-29 | 並行防護、CFTS020 全域 v2 重判、Display 面解鎖（b03，8 條） | [handoff/03_parallel_guard_and_display_unlock.md](handoff/03_parallel_guard_and_display_unlock.md) | [upstream/03_parallel_guard_and_display_unlock.md](upstream/03_parallel_guard_and_display_unlock.md) | **無**（執行層不代擬） | 建議登錄 6 則（上繳 §十四） | **已審結**（b03 收下；即裁 R-ICS18～21，登 A-ICS21～27，新開 DR-ICS14／15） |
| 04 | 2026-08-29 | profile 落檔、四訊號解佔位、Browse／Navigation 面（b04，7 條） | [handoff/04_profile_signals_and_navigation.md](handoff/04_profile_signals_and_navigation.md) | [upstream/04_profile_signals_and_navigation.md](upstream/04_profile_signals_and_navigation.md) | **無**（執行層不代擬） | 建議登錄 5 則（上繳 §十二） | **已審結**（b04 收下；即裁 R-ICS22／23，登 A-ICS28～33，新開 DR-ICS16／17） |
| 05 | 2026-08-29 | 佔位補齊、Display ER 主錨改寫、交付前體檢（**不新增 TC**，維持 23 條） | [handoff/05_anchor_rework_and_pre_delivery.md](handoff/05_anchor_rework_and_pre_delivery.md) | [upstream/05_anchor_rework_and_pre_delivery.md](upstream/05_anchor_rework_and_pre_delivery.md) | **無**（執行層不代擬） | 建議登錄 3 則＋G2~G7 六筆待取號（上繳 §14） | **已審結**（即裁 R-ICS22 v2／24～30，登 A-ICS34～45） |
| 06 | 2026-08-29 | 佔位回收、005／009 解鎖、CFTS022 改綁、Notifications 偵察 | [handoff/06_placeholder_recovery_and_unlock.md](handoff/06_placeholder_recovery_and_unlock.md) | **無上繳** | — | — | **作廢**（E1 開工前觸發：`ledger_guard` exit 1 報 11 筆 DUPLICATE，實為掃描定義有缺而非台帳有錯。執行層一項作業未動、一個檔未寫、未自改工具而上報 —— 判為合式，記於 R-ICS29(e)；成因為分析層之誤 A-ICS45。內容併入 07 並刷新） |
| 07 | 2026-08-29 | 解封（掃法修正）、佔位回收、scroll／tune（b05，2 條） | [handoff/07_unblock_and_recovery.md](handoff/07_unblock_and_recovery.md) | [upstream/07_unblock_and_recovery.md](upstream/07_unblock_and_recovery.md) | **無**（執行層不代擬） | 建議登錄 5 則（上繳 §14） | **已審結**（即裁 R-ICS19 v2／R-ICS25 v2／R-ICS31～33，登 A-ICS46～50）|
| 08 | 2026-08-29 | §1.18 對比、005 生成（b06，2 條）、if-any 改寫、候選篩常設化 | [handoff/08_s118_comparison_and_rework.md](handoff/08_s118_comparison_and_rework.md) | [upstream/08_s118_comparison_and_rework.md](upstream/08_s118_comparison_and_rework.md) | **無**（執行層不代擬） | 建議登錄 4 則（上繳 §12） | **已審結**（Pei 裁 ③ 二節並存 → R-ICS35；另落 R-ICS34、A-ICS51～56、DR-ICS18）|
| 09 | 2026-08-29 | TLM 指涉量測、§1.18 獨有面覆蓋清點（**TC 新增 0、錨變動 0**） | [handoff/09_tlm_referent_measurement.md](handoff/09_tlm_referent_measurement.md) | [upstream/09_tlm_referent_measurement.md](upstream/09_tlm_referent_measurement.md) | **無**（執行層不代擬） | 建議登錄 5 則（上繳 §10） | **已審結**（R-ICS35 改題＋v2、R-ICS36；R-ICS35(b)(c) **廢止**；登 A-ICS57～61）|
| 10 | 2026-08-29 | 變體歸屬量測（**TC 新增 0、錨變動 0**） | [handoff/10_variant_attribution.md](handoff/10_variant_attribution.md) | [upstream/10_variant_attribution.md](upstream/10_variant_attribution.md) | **無**（執行層不代擬） | 建議登錄 6 則（上繳 §10） | **已審結**（Pei 裁 §1.18 算數 → R-ICS39；另落 R-ICS37／38、A-ICS62～69、DR-ICS19）|
| 11 | 2026-08-29 | **009 與三缺口生成（b07，4 條）**、NBSP 重跑、probe 三層、CFTS022 變體軸 | [handoff/11_generation_and_rerun.md](handoff/11_generation_and_rerun.md) | [upstream/11_generation_and_rerun.md](upstream/11_generation_and_rerun.md) | **無**（執行層不代擬） | 建議登錄 6 則（上繳 §12） | 待覆核 |

---

## 2. 註記

### † 01 以前之往返未落檔

R-ICS1～4 與 A-ICS1～7 之產生過程只存在於 2026-08-29 之聊天；
`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`framework.md`
由分析層於下放包 01 同日寫入 repo，條文本身已落檔，
**其往返包未落檔**。與 AMFM／Projection 之同類缺口一致，不追補。

### 01 之未結事項

01 之待裁 6 項全數由 R-ICS5～R-ICS10 裁結（見 `RULINGS.md`）。

### 02 之未結事項

02 之待裁 6 項全數由 R-ICS11～R-ICS17 與 R-ICS2 v2 裁結。

### 03 之未結事項

03 之待裁 8 項由 R-ICS18～R-ICS21 裁結其六；出貨資格已由 R-ICS18 解鎖。

### 04 之未結事項

04 之待裁 7 項由 R-ICS22／R-ICS23 裁結其五。

### 05 之未結事項

05 之待裁 7 項由 R-ICS22 v2／R-ICS24～R-ICS30 裁結。

### 06 —— **作廢，無上繳包**

E1 於開工前觸發而封鎖整包。診斷、三選一之解封方案與 P1／P2 過期之具名，
見對話紀錄與 R-ICS29／A-ICS45。**06 之作業內容併入 07 並刷新。**

### 07 之未結事項

07 之待裁 8 項由 R-ICS19 v2／R-ICS25 v2／R-ICS31～R-ICS33 裁結其六。

### 08 之未結事項

08 之待裁 6 項由 Pei 裁 ③（R-ICS35）與 R-ICS34 裁結其四。

### 09 之未結事項

09 之待裁 8 項由 R-ICS35 v2／R-ICS36 裁結其七。

### 10 之未結事項

10 之待裁 8 項由 R-ICS37／38／39 裁結其六。

### 11 之未結事項（詳見 upstream-11）

- **八包以來第一次真的寫 TC**：009 ＋ G2／G3／G9 共 **4 條**（先導閘通過，E13 未觸發）；
  **TC 27 → 31**；Test Set 仍 5 組（E12 未觸發）；既有 27 條之錨**一條未改**
- **009 之 Market 註不照抄**：R-ICS25 v1(b) 之「必載 Market 限 NAFTA」繫於舊候選錨 `4819554`，
  本條二錨實測皆 `Market = All` —— **照載即與實測不符**
- **A-ICS66 之因果陳述有誤（自我更正）**：NBSP 缺陷之後果**只落在錨層對應集合，
  不落在 09 之覆蓋清點**（09 走 `tokens()` 路徑，結構性免疫）。
  **09 之判定改變者 0 個**；upstream-10 §3-5-1 之推論已更正
- **加錨指示表已備**：15 條 TC／24 錨行／13 個相異新 ObjectID，b12 可逐條照抄。**E14 未觸發**
- **CFTS022 無變體軸，7 條不受影響（E10 未觸發）**；更準的讀法是
  **CFTS022 把變體敏感行為全數外包給 CFTS020** —— 外引是否反噬，本線從未問過
- **快照法首次落地**：`11_rulings_snapshot.md`；**本包 git 執行次數 0**（b10 之違規未再發生）
- 預期數字 **18／19 相符**；不符者為下放包「6 個物件」而其列舉為 7 個
- probe 三層分列（軸層回歸 `True`）；另揭 **87 個「軸層適用、變體不合、範圍隨變體層」之物件無人裁過**

### 10 之未結事項（已作廢，保留於下）

- **結論：本 DUT = `Disassociated`（'Silver Box'，外接 DCSD）**。E7／E8 皆未觸發。
  十項支持證據**全部脫離 §1.8／§1.18**（禁循環論證之要求達成，循環不計入者 0）
- **交辦之三條主路徑全部落空**（後綴綁定 0、四個配置參數節 0 適用、DBC 收發有已證實盲區）；
  結論由未指定之三項撐起：**SYSAD Definitions 表、SYS2 之 Category 邊界、分支配對檢定 46:0**
- **【最重】§2-4 之衝突**：本 DUT 之 SYS2 把 §1.18 之 **29 列收為在案需求**（8 列為 FR），
  **與「Disassociated ⇒ §1.18 整批退出」之外推不符**。
  **量得變體 ≠ 量得「§1.18 之地位」，二者被默認為同一件事，而 SYS2 說不是**
- 影響估：Disassociated **改 0 條**；Associated **改 20 條、b03 退 7／救 1、退回 6 處佔位**
- **【違規，自承】主實例執行了一次唯讀 `git show`** —— 並揭出
  **§1 禁 git 與作業 C-5（圍籬 diff）互斥**：圍籬舊版只存在於 git 歷史。建議改快照法
- 預期數字 **14／15 相符**，唯一不符者為上項違規 —— **連續兩包零不符於此中斷，
  而中斷者是紀律不是量測**
- 另揪出工具缺陷：`s118_compare_08.py` 之 NBSP 分詞使 **09 §1 之三條覆蓋判可能有誤**（發現而未逕改）

### 09 之未結事項（已作廢，保留於下）

- **【E5 觸發】`TLM` = DUT**。五項獨立證據收於一點；`TLM` 47 次／20 物件**只在 §1.18**、
  `HU` 1741 次／940 物件而 **§1.17／§1.18 為 0**、**同物件併現 0** —— 互補分佈而非併現區辨。
  主實例已獨立複驗五個實數，與並行實例逐一相符。**未生成 009、未改錨、未結案。**
- **【最重】問題已變形（§2-5）**：`§1.8` 標題為 `… ICS, **Silver Box HU**, …`、
  `§1.18` 為 `… ICS and **Associated HU**`，而 `4819134` 逐字界定二者為
  **同一顆 HU 的兩種硬體變體**（`_DDspl` 外接 DCSD／`_ADspl` 觸控整合）。
  **R-ICS35(a)「二節並存」之依據（互不重疊）另有更簡單的解釋：一顆 DUT 只會是其中一種。**
  待裁之問題應改為「**本 DUT 是 Associated 還是 Disassociated**」—— 可量測，量到後前者自動有解。
- **【E6 觸發】** §1.18 獨有面 9 個缺口，「現在即可生成」4 個 —— **一條未生成**
- **一項禁區違規（自承）**：並行實例執行了一次唯讀 `git status --short`；
  **成因為主實例下派時未把「唯讀亦不可」寫死**，已具名不減輕
- 預期數字 **13 項全部相符（連續第二包零不符）**；TC 27、佔位 17、可出貨 23／不可 4 皆不變

### 08 之未結事項（已作廢，保留於下）

- **預期數字 13 項全部相符 —— 八輪來第一次零不符**。但實質產出都落在該表之外：
  E2 觸發、對 upstream-07 之自我更正、候選篩首版失敗
- **【E2 觸發】DR-ICS13**：§1.18 有判適用之 `Back_Button` 母條
  （`4821681` ＋ `4821683`~`4821689` 七個泛用母條），而 §1.8／§1.5 之對應物皆判不適用
  —— **未結案、未生成 009**
- **DR-ICS16 之出路已窮**：`ETM = DUT` 不成立（b07）＋ **§1.18 對 DISP_STAT 家族零承載**（b08）
  → 12 處佔位在現有素材下**確定無解**，建議升為阻斷件
- **§1.18 三種結果之影響估**：0／20／13 條。**結果 ② 之真正代價不是重錨，是「無錨可重」**
  —— 7 條之錨在 §1.18 零承載，且 `4819541`（唯一定值來源）一併失去
- **自我更正**：upstream-07 §13-2 之「§1.18 更具體」為整體印象，
  逐物件實測後**只在旋鈕／訊息名上成立**；POWER／SCREEN OFF 上 §1.18 反而更抽象且主詞為 TLM
- 未錨定斷言 **7 → 3**；TC 25 → **27**；可出貨 **23／不可 4**；佔位 **17**（不變）

### 07 之未結事項（已作廢，保留於下）

- **解封**：`ledger_guard` 掃法依 R-ICS29(c)(d) 修正（剔除 `LEDGER-IGNORE` 區塊、
  合併列不計入、docstring 同步），exit 0
- **三個機制各擋下一件**：作業 C **E3 觸發**（`ETM = DUT` **不成立**，
  12 處 `$TGW_DISP_STAT$` 佔位維持）、作業 D 之 009 **錨判不適用**（Radio／EE 二軸皆落空）、
  005 **E4 觸發**（不符純為列舉順序，內容零變動）
- **作業 G 首次執行**：118 行 ER 中 **7 行未錨定斷言**，其中 4 行為 `if any` 之潛在 FF
- **§1.18「ICS Management」七包未讀** —— 37 物件、29 適用，且其條文
  **逐字點名 `CLIMATIC_PANEL` 與 `Knob_increment` 等值**，較 §1.8 更具體
- 全批佔位 21 → **17**；TC 23 → **25**；可出貨 **17／不可 8**
- DR-ICS1 ~ DR-ICS17 **17 條全開**（狀態實測見 upstream-07 §10）

### 05 之未結事項（已作廢，保留於下）

- **本輪自承二誤**：(1) 連續三包斷言「時間符號於 CFTS020 無值」為誤 ——
  值實存於 **`CFTS020-4819541`**（§1.8.1，v2 判適用，SFR 型）：`<Tstuck_button> = 120 sec`、
  `<TPeriodToSendNoChange> = 20 msec`、`<TPeriodToCountKnobDetents> = initial value 50 msec`；
  **DR-ICS10／DR-ICS12 疑可結**。(2) 「`1.8.1.3` 之 23 皆為 `[ECU:FPDM]`」實為 **16／2／5**，
  R-ICS23(a) 之理由有誤（結論不變）
- **`ledger_guard` 前後不逐字相同** —— `ANOMALIES.md` 於執行期間由分析層新增 A-ICS34；
  exit code 二次皆 0，**只比 exit code 會漏**
- 交付前體檢：23 條**強 12／弱 11**，**可出貨 13／不可 10**
- DR-ICS1 ~ DR-ICS17 **17 條全開**；覆蓋缺口 7 筆
- 該驗而未驗者 5 項

### 04 之未結事項（已作廢，保留於下）

- 待裁 7 項（§9），最重者為 **`$TGW_DISP_STAT$` 之 E1** —— 其為**匯流排變體**
  （B-CAN vs CAN-FD）而非 ECU 變體，R-ICS13 之「取 ICS 面板」語意無對應物；
  **b03 之 12 處佔位與 Display 面八條之訊號面驗證強度全繫於此**
- DR-ICS1 ~ DR-ICS15 **15 條全開**；建議新開 1 條（`Pop-up List Notification`）
- 該驗而未驗者 6 項（§10-2）
- **`VOLUME POP_UP` 之四包追索首次收斂**：CFTS 系列（022／020／019）與 HMI L&F 六本
  全數掃遍皆查無，線索指向一份具名而**不在 repo** 之 `Pop-up List Notification`

### 03 之未結事項（已作廢，保留於下）

- 待裁 8 項（上繳 §十），其中二項卡住出貨：
  **(1) R-G13 與 R-ICS17(d) 之交互**（改題即改指紋，`R-ICS2 v1` 由 `ad557b5d` → `4a8819f0`，
  圍欄內容 diff 0）；**(2) 方括號／單引號之 profile 缺口** —— IN §11 之 Exception 為
  profile-scoped 而本 feature 無 profile，**b03 八條之出貨資格繫於此**
- DR-ICS1 ~ DR-ICS13 **13 條全開**
- 該驗而未驗者 5 項（上繳 §12-2），首項仍是 `VOLUME POP_UP` 之 6 行 ER
  —— 連續三包具名，本包窮盡 CFTS019 七件仍查無

### 02 之未結事項（已作廢，保留於下）

- 待裁 6 項（上繳 §十）：**CFTS020 之 `ECU` 軸 87% 不存在使 R-ICS2 三軸判準幾近不可用**、
  R-ICS8(c) 同 DBC 多名之決斷、CFTS020 得否繞過 SWRA 位移、S1 未增等待步驟之處置、
  `SIS-5161` 之 DR、CFTS020 物件母數之口徑（407 vs 2180）
- DR-ICS1 ~ DR-ICS10 **10 條全開**；另建議新開 1 條（`SIS-5161`）
- 該驗而未驗者 5 項（上繳 §十一），首項為 b01 之 `VOLUME POP_UP` 顯示條件（FF 風險 6 行）

### 產出物落點

| 物 | 路徑 |
|---|---|
| b01 之 TC JSON | `generated/b01/b01_tcs.json`（02 輪修訂：訊號實名、DTC 具名、de-mature 步驟）|
| b01 之 manifest | `generated/b01/manifest.json` |
| b02 之 TC JSON | `generated/b02/b02_tcs.json`（ignore 面 2 條）|
| b02 之 manifest | `generated/b02/manifest.json`（含 `signal_resolution` 之逐步實測）|
| b03 之 TC JSON | `generated/b03/b03_tcs.json`（Display Control 8 條）|
| b03 之 manifest | `generated/b03/manifest.json` |
| b04 之 TC JSON | `generated/b04/b04_tcs.json`（Browse Control 6 條＋Menu Navigation 1 條）|
| b04 之 manifest | `generated/b04/manifest.json` |
| b05 之 TC JSON | `generated/b05/b05_tcs.json`（scroll／tune 2 條；**批號與輪次自此不同步**）|
| b05 之 manifest | `generated/b05/manifest.json` |
| b06 之 TC JSON | `generated/b06/b06_tcs.json`（005 Mute，2 條）|
| b06 之 manifest | `generated/b06/manifest.json` |
| b07 之 TC JSON | `generated/b07/b07_tcs.json`（009＋G2／G3／G9，4 條）|
| b07 之 manifest | `generated/b07/manifest.json` |
| 9 個 LID → CAN 對照 | `generated/b03/lid_dbc_map.json` |
| **累計** 12 個 LID → CAN 對照 | `generated/b04/lid_dbc_map.json`（b03 八筆沿用＋b04 四筆實測）|
| feature profile | `docs/runtime/profiles/FW036_R1L_ICS_Profile.md`（R-ICS18(e)，逐字取 R-ICS18(a)(b)(c)）|
| CFTS020 三面偵察（v1，**已作廢**）| `docs/reports/02_cfts020_face_recon.md` |
| CFTS020 全域重判（v2，現行）| `docs/reports/03_cfts020_recon_v2.md` |
| HMI L&F ／ CFTS019 偵察 | `docs/reports/03_source_recon.md` |
| Pop Up List ／ Camera 偵察 | `docs/reports/04_source_recon_2.md` |
| 覆蓋缺口清單 | `docs/reports/05_coverage_gaps.md`（7 筆）|
| 交付前體檢（v1，**已被取代**）| `docs/reports/05_pre_delivery_check.md` |
| 交付前體檢（v2，**已被取代**）| `docs/reports/07_pre_delivery_check.md` |
| **交付前體檢 v3（現行）** | `docs/reports/08_pre_delivery_check.md`（候選篩＋人工複核二層式，R-ICS32(c) 常設項）|
| **§1.8 vs §1.18 逐物件對比** | `docs/reports/08_s118_vs_s18.md`（639 行）|
| **TLM 指涉量測** | `docs/reports/09_tlm_referent.md`（E5：`TLM = DUT`）|
| **§1.18 獨有面覆蓋缺口** | `docs/reports/09_s118_coverage_gap.md`（9 缺口、三分類）|
| **變體歸屬量測** | `docs/reports/10_variant_attribution.md`（結論：Disassociated）|
| **二種結論之影響估** | `docs/reports/10_variant_impact.md` |
| NBSP 重跑與加錨指示表 | `docs/reports/11_s118_coverage_gap_rerun.md`（**b12 之直接輸入**）|
| CFTS022 變體軸 | `docs/reports/11_cfts022_variant_axis.md` |
| **RULINGS 快照（圍籬 diff 基準）** | `docs/reports/11_rulings_snapshot.md`（R-ICS38(a) 首次落地）|
| `ETM = DUT` 三路交叉 | `docs/reports/07_etm_dut_crosscheck.md` |
| CFTS022 新舊版覆驗 | `docs/reports/07_cfts022_reverify.md` |
| 節前定義塊掃查 | `docs/reports/07_predef_blocks.md` |
| Notifications 偵察 | `docs/reports/07_notifications_recon.md` |
| 036 表單工作副本 | `sandbox/ics_management_00.xlsx`（不入版控）|
| 自檢 | `scripts/selfcheck_b01.py`（02 輪起合檢 b01+b02，增非 ASCII 與角括號列示）|
| 逐字比對 | `scripts/verify_verbatim_b01.py`（02 輪起兼比 CFTS020）|
| CFTS020 物件抽取／三軸判定 | `scripts/cfts020_probe.py`（03 輪起 v1／v2 並存，預設 v2）|
| 偵察報告產生器 | `scripts/gen_face_recon.py`（v1）、`scripts/gen_recon_v2.py`（v2，現行）|
| 台帳並行防護 | `scripts/ledger_guard.py`（R-ICS17(f)，每包上繳須附前後二次輸出）|
| LID → DBC 對照 | `scripts/lid_dbc_probe.py` |
| 來源偵察 | `scripts/src_recon_03.py`、`scripts/src_recon_04.py` |
| LID → DBC（四訊號）| `scripts/lid_dbc_probe_b04.py` |
| 佔位普查（口徑統一）| `scripts/pending_census.py`（A-ICS31；禁人工列舉）|
| 覆蓋缺口量測 | `scripts/gap_probe_05.py` |
| 交付前體檢產生器 | `scripts/gen_pre_delivery_05.py` |

落點取 `generated/`／`sandbox/` 而非下放包所令之 `batches/`／`workbook/`，
依 R-G25 與 `scripts/lint_paths.py` 之實跑；理由與證據見上繳包 §二。

---

## 第 12 輪（2026-08-30）加錨 15 條、87 物件之 SYS2 收錄面、CFTS022 外引

| 項 | 落點 |
|---|---|
| 上繳包 | `docs/upstream/12_anchor_addition.md` |
| 87 物件之 SYS2 收錄面（**E15 觸發**）| `docs/reports/12_87_objects_sys2.md` |
| CFTS022 外引與第三種變體表達（E16 未觸發）| `docs/reports/12_cfts022_crossref_and_third_variant.md` |
| RULINGS 快照（快照法第二次；b13 之圍籬 diff 基準）| `docs/reports/12_rulings_snapshot.md` |
| 新腳本 | `scripts/sys2_87_probe_12.py`、`scripts/crossref_probe_12.py` |

本輪改 15 條 TC 之 `specification_reference`（＋24 錨行、13 個相異新 ObjectID，照抄
upstream-11 §4-2，E17 未觸發）與 G2／G3 之 `reasoning`；**未生成任何 TC，總數仍 31**。
**git 執行次數 0**（含唯讀）。

三件須分析層處置者：**87 個實為 §1.4 架構共通節 × 86 ＋ §1.5 × 1，非 Associated 分支**
（根因為執行層 probe 之 `variant_fits_dut` 併「未分類」入「Associated」，
upstream-11 §4-3 與 A-ICS74 之敘述須更正）；**SYS2 有 23 列在案 FR 無 CFTS020 來源**
（以 CFTS020 為起點之掃描結構性掃不到）；**A-ICS73 所慮已經由本包之加錨成為事實**
（b06 二條 Mute TC 現帶 §1.18 錨）。

---

## 第 13 輪（2026-08-30）收尾包：probe 三值化、SYS2 反向掃、**凍結**

| 項 | 落點 |
|---|---|
| 上繳包 | `docs/upstream/13_freeze.md` |
| **凍結記錄（解凍者先讀此檔）** | `docs/reports/13_freeze_record.md` |
| SYS2 反向掃（**E19 觸發**）| `docs/reports/13_sys2_reverse_scan.md` |
| PDT27 dbc 對 DR-ICS16（E21 未觸發）| `docs/reports/13_pdt27_dbc_vs_dr16.md` |
| **凍結基準快照**（解凍時圍籬 diff 之基準）| `docs/reports/13_rulings_snapshot.md` |
| 新腳本 | `scripts/sys2_reverse_scan_13.py`、`scripts/pdt27_probe_13.py` |
| 改動之腳本 | `scripts/cfts020_probe.py`（`variant_fit()` 三值化，軸層零變動）|

本輪**未生成任何 TC、未改任何錨或 reasoning**；TC 仍 31、佔位仍 18 處／14 條。
預期數字 17 項全數相符。**git 執行次數 0**。

四件須分析層處置者：**E19 —— `NRL-180522`（觸控去重／CarPlay 認證）為 HMI 軟體側可驗證之行為**；
**SYS2 自帶 `Verifiability`／`Verification Criteria`／`Verification Method` 三欄，本線十三包從未量過**；
**掃描起點盲區 73 列（21.9%）**；**已綁 FDCAN8 檔載 `BO_TX_BU_ 1427 : ETM,LTM;`，與 upstream-07 之 E3 依據相對**。

---

## 第 14 輪（2026-08-30）窗口式解凍：同一物、發收方向、綁定三件量測

| 項 | 落點 |
|---|---|
| 上繳包 | `docs/upstream/14_signal_identity_and_direction.md` |
| 同一物判定（**E25 觸發**：dbc 為四支非三支）| `docs/reports/14_signal_identity.md` |
| 發收方向（E22 字面未觸發，另具名一件範圍事項）| `docs/reports/14_signal_direction.md` |
| BHCAN2 綁定影響面（E24 未觸發）| `docs/reports/14_bhcan2_binding_impact.md` |
| **回凍基準快照** | `docs/reports/14_rulings_snapshot.md` |

本輪為純量測包：**零 TC 新生／零錨變動／零佔位回填／零步驟或 ER 改寫**；
`FORMS.md`／`feature.yaml`／`features/display/` 一字未改（sha 自證）。**git 執行次數 0**。
預期數字 16 項相符、1 項不符（圍籬 diff 實測新增二條而非一條，成因為快照時點早於 `R-ICS43`）。

四件須分析層處置者：**`$Telematic_Power$` 在裁定之 BHCAN2 上本 DUT 是發送側，
`ICS` 不在該檔 `BU_` 內 —— TC 2／TC 4 之前提可能無法建立**；
**A-DM14 無承載流程**（只登 `display` 一處，對造 `vehicle_setting` 命中 0，未轉 DR）；
**dbc 為四支且 R1／R4／R5 世代錯配**（DUT 為 R1L，已綁者為 R4／R5）；
**CFTS020 不載任何 CAN 訊息名與位元佈局，R-17(c) 三項判準實際只有一項可用**。

---

## 第 15 輪（2026-08-30）世代錯配量測 —— **E26 觸發，綁定與回填未執行**

| 項 | 落點 |
|---|---|
| 上繳包 | `docs/upstream/15_binding_and_backfill.md` |
| 世代錯配量測（**E26 觸發**）| `docs/reports/15_dbc_generation_diff.md` |
| TC 2／TC 4 前提建立法（E28 未觸發）| `docs/reports/15_tc2_tc4_precondition.md` |
| **回凍基準快照** | `docs/reports/15_rulings_snapshot.md` |

**作業 B（綁定 BHCAN2 ＋ 建讀者）與作業 C（12 處回填）依 E26 未執行。**
`feature.yaml` 仍 10 鍵、`FORMS.md` 一字未改、佔位仍 18 處／14 條、TC 仍 31 條。**git 執行次數 0**。

核心量測結果：**世代之間唯一的差異在發收方 —— 位元佈局、值域、`VAL_` 於四支 dbc 上 17／17 完全相同**，
交付欄受影響 **0 條**。下放包 §7 所慮之「回填錯值而看不出來」**經量測不成立**。
實際觸發 E26 者為**三條 b03 之 `reasoning` 引述 R4 檔原行，該引述於裁定之 BHCAN2 上不正確**。

另對 upstream-14 具名更正一項：**A-ICS91 所引之 `4819144`／`4820117` 並非 TC 2／TC 4 之錨，
且未被任何 TC 引用**；二條之前提 `$Telematic_Power$` **從未寫過任何建立方法**。

---

## 第 16 輪（2026-08-30）綁定與讀者、**12 處回填**、reasoning 更正

| 項 | 落點 |
|---|---|
| 上繳包 | `docs/upstream/16_binding_and_backfill_exec.md` |
| Pre-Condition 體例抽查（只量不改）| `docs/reports/16_precondition_style.md` |
| **回凍基準快照** | `docs/reports/16_rulings_snapshot.md` |
| 新腳本 | **`scripts/verify_reference_binding.py`**（移植自 `display`；首跑 11／11）|
| 改動 | `feature.yaml`（`reference:` 10 → 11，增 `dbc_bh2`）、`forms/FORMS.md`（僅 BHCAN2 一列之使用 feature 欄）、`generated/b03/`（12 處回填）|

**E27／E30／E31／E32 全部未觸發，作業 A～E 全數完成。git 執行次數 0。**

**十六包來第一次補完一件缺件**：`DR-ICS8` 之 12 處佔位全數回填為
`$TELEMATIC_DISPLAY2.TGW_DISP_STATSts$`，值取 `VAL_ 1500` 逐字（`0 (Display_off)`／`2 (Normal_mode)`）。
**ICS 佔位由 18 處／14 條降至 6 處／6 條**，殘餘只繫於 DR-ICS6（5 處）與 DR-ICS4（1 處）。

**A-ICS97 解除**：本 feature 之 11 個 sha 首次受程式檢驗，**11／11 相符** ——
即十六包所綁之參考件皆未被改動。

三件須分析層處置者：**「納入 gate 集」無可行載體**（`ics_management` 於 `GATES.tsv` 命中 0 列，
且 `display`／`bed_lowering` 之同名讀者亦均未登錄，讀者入簿在本 repo 尚無先例）；
**回填之副作用 `has_pending` 旗標須同步**（下放包未令，本包自行發現並修正）；
**`VAL_ 1500` 之三值（`7`／`8`／`15`）無任何 TC 涵蓋**而規格側載有此三態。

---

## 第 17 輪（2026-08-30）**SYS2 主鍵對照表**、驗證性欄對照、二件小量

| 項 | 落點 |
|---|---|
| 上繳包 | `docs/upstream/17_sys2_master_table.md` |
| **SYS2 主鍵對照表**（表本體 333×14）| `docs/reports/17_sys2_master_table.tsv` ＋ `.md` |
| `VAL_ 1500` 三值與 `RQ_DISP_INTS` 書寫（E36 未觸發）| `docs/reports/17_val1500_three_states.md` |
| **回凍基準快照** | `docs/reports/17_rulings_snapshot.md` |
| 新腳本 | `scripts/sys2_master_table_17.py`、`scripts/val1500_probe_17.py`（皆唯讀）|

**零 TC 新生／零錨變動／零 ER 改寫／零交付欄改寫。git 執行次數 0。E35／E36 未觸發。**

**以 SYS2 為主鍵之覆蓋率：38／333 ＝ 11.4%**（只計 FR 為 22／80 ＝ 27.5%）。
四桶 260／42／31／0 與 A-ICS86 逐項相符。

**【E33 觸發】** 7 個錨不在 SYS2 —— **七者全屬 CFTS022，而 repo 內查無 CFTS022 之 SYS2 匯出**；
本表結構性地無法回答 CFTS022 側之覆蓋。
**【E34 觸發】**「我方較寬」21 列，二種成因：20 列源於 SYS2 之樣板 Criteria 貼錯（37／75 為逐字相同之樣板），
1 列（`4821022`）為**實質驗證缺口**（screen ON 態之 `$RQ_DISP_INTS$ != 0%` 未驗）。

三件另須處置者：**我方已驗之 38 列中 14 列為 SYS2 判 `Out of Scope` 且理由欄全空**；
**E36 射程過窄** —— 其指名之二物件屬 §1.5（R-ICS2 v2(c) 早載 100% 不適用），
實質條件成立於另 **20 個**物件（適用 ∧ 在案 ∧ 未覆蓋）；
**A-ICS94 有反例**（`4819632` 規格原文並列 `[ON_BLANK / On_blanked_screen]`）。

---

## 第 18 輪（2026-08-30）A-ICS116 之補正（**E39／E40 停**）、收斂軌跡、失敗史附錄

| 項 | 落點 |
|---|---|
| 上繳包 | `docs/upstream/18_criteria_backfill_and_history.md` |
| **254 → 31 收斂軌跡**（R-ICS43(b)②）| `docs/reports/18_convergence_trace.md` |
| **失敗史附錄**（R-ICS43(b)③）| `docs/reports/18_failure_history.md` |
| **回凍基準快照** | `docs/reports/18_rulings_snapshot.md` |

**作業 A 依 E39／E40 停在 A-1，補正未執行。** 零 TC 新生／零錨變動／零交付欄改動；
TC 仍 31、佔位仍 6 處／6 條。**git 執行次數 0。** 作業 B、C、D 全數完成。

**E39**：`$RQ_DISP_INTS$` 全部出現為 **14 行／8 條**（非 6／3）——
多出之 8 行在 `test_item`（規格逐字引，R-17(b) 不得改），**可改寫面仍為 6 行／3 條**，二數並呈。
**E40**：列 39 `4821022` **未被任何 TC 錨命中** —— b17 係以**行為等值**判其已覆蓋
（其 `cover_basis` 欄逐字為 `行為等值：…`，`covering_tcs` 為空）。補正之定性須先裁。

**收斂軌跡對帳成立**：31（錨命中）＋ 223（未覆蓋）＝ **254**；
未覆蓋之最大三類為 §1.4 架構共通節 **86**、觸控／手勢面 **32**、Camera Transition **29**。
**223／295／216 三個「未覆蓋」數不可相加**（分母與判準各異）。

**失敗史七類齊備**，未量即斷七例逐例獨立成則；其「共同形狀」為
**把「我沒看見」當成「不存在」，並當作已量測之事實往下傳**（六類同形，A-ICS101 誠實排除在外）。

---

## 第 19 輪（2026-08-30）**寫回**：19a dry-run（**E42 停**）

| 項 | 落點 |
|---|---|
| 上繳包 19a | `docs/upstream/19a_writeback_dryrun.md` |
| dry-run 報告 | `docs/reports/19_writeback_dryrun.md` |
| 交付清單對照 | `docs/reports/19_delivery_checklist_ics.md` |
| 凍結記錄（§3 掛帳 11→18 項、§4 解凍條件收斂）| `docs/reports/13_freeze_record.md`（**執行層唯一得改之既有報告**）|
| 快照 | `docs/reports/19_rulings_snapshot.md` |

**作業 A／B／D／E 完成；作業 C（sandbox 產出）依令未做**，待分析層審 dry-run。
**repo 內未新增任何 xlsx。git 執行次數 0。TC 內容變動 0。**

**【E42 觸發】`generated/` 之 31 條無 `tc_id`** —— 而 `feature.yaml` 已宣告
`tc_id_format: "NR1L-ICS-{n:03d}"` 與欄位對映（`tc_id: "F"`）：**格式在案，值從未生成**。
依令不自行編號。**E41／E43／E44 未觸發** —— 母本 x14 DV（`R10:R1411`）經
`xlsx_surgical` 實測保留（48 成員一致、DV 計數不變、僅 `sheet6.xml` 有差）。

母本既有資料列 **0**（表頭第 9 列、資料自第 10 列，現場複驗）；投影後 **0 → 31**；
PENDING **6 處全在 `pre_conditions`**（DR-ICS6 五處、DR-ICS4 一處）；
不可出貨 **4 條**（V1／V2／V3 → DR-ICS9；B5 → DR-ICS2）。

另具名一件：下放包稱「本 feature 無既有交付件」，實測 `sandbox/ics_management_00.xlsx` **存在**
（第 01 輪所產，**與母本 sha 逐字相同、資料列 0**）—— 結論正確而前提敘述不精確。
