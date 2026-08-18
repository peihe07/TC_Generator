# DATA REQUESTS — User Profiles (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/user_profiles/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | `FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx` | **MISSING** | 全部（180 母體之唯一來源）| **Phase 1 recon 完全停擺**；作業項 3 不可跑、作業項 4 之 135-id 命中不可驗、作業項 5 之 Layer 2 交集不可取 | A-UP04 | **BLOCKING（最高）** |
| 2 | `HMI Pop Up List`（pattern：`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` 或其 R1L-R 對應版）| **部分到齊 18/20**，見第 4 列 | spec 8.3 明文「Specific popups can be found in the HMI Pop Up List」；spec 全文另有 PU0585／PU0626／PU1573 等 PU id | Phase 3 profile 之 popup 詞彙表與 lint `popup_ids` 無來源；引用 PU 字面值之 TC 無法回溯 | A-UP06 | 高（Phase 3 前）|
| 4 | **Pop Up List 中 `PU1087`／`PU1088` 兩列之 popup 內文**（非整份版本 —— **索取標的已於 06 輪依 R-U27 收窄**）| MISSING | `PROF-002-03`（`4.1.1`）| **不再擋章節**：spec PDF p6 已載該二 popup 之**觸發條件**，故觸發、顯示與否、流程分支皆可驗；**僅其 popup 內文之逐字 ER 不寫**（§8.4.1 不推定內容）| A-UP06 | **MEDIUM**（原 高；R-U27 降級）|
| 3 | spec `3.1`–`3.5`（PLP1–PLP5）等 8 條之上游釐清 | **CLOSED — OUT-OF-SCOPE (R-U56)** ｜**不送出** | 0（現況無 leaf 對應）| 不阻擋生成。**`3.1`–`3.5` 之使用不受本次關閉影響** —— 依 R-U22／R-U46 仍為 `PROF-001-01` 之 in-scope 依據，`specification_reference` 繼續併列 3.x；`10.1`／`11.1`／`11.2` 不生成 TC，狀態 **OUT-OF-SCOPE**（非缺口）| A-UP02（**OUT-OF-SCOPE，已裁；記載未關閉**）| — （不再送出）|

## 第 1 列之實測依據（2026-08-17）

搜尋範圍：repo 全樹，加上 `~`（深度 6，排除 `Library/`、`.Trash/`）。
比對式：`-iname "*037*Personal*"`、`-iname "*Personal Account*"`、
`-iname "*PROF*.xlsx"`（大小寫不敏感，檔名比對，非內容比對）。
命中：**0 個 037 檔**。repo 內既有之 037 僅 `features/power/inputs/`、
`features/comfort/inputs/`、`features/sxm/inputs/` 三個他 feature 的。
`features/user_profiles/inputs/` 於 scaffold 後僅有 036 母本複本 1 檔。

## 第 2 列之實測依據

`data/outline_map.json` 全文（169 條 Description 欄）以 `PU[\s_]?(\d{3,4})`
掃描，得**唯一 PU id 20 個／逐引用 22 次**，與下放包 01_intake.md 之
「spec 全文唯一 PU id 20 個」**相符**。逐 id 與逐 section 對映見
`data/spec_popup_ids.tsv`，已填入 `feature.yaml` `lint.popup_ids`。

**首次量測曾得 18，係本執行層之抽取缺陷**：初版比對式 `PU\s?\d{3,4}` 漏掉
`PU_0118`（4.1.1）與 `PU_0129`（5.13.2）兩個底線分隔形態。此為 canon §5a
第 7 條（假陰性源自詞彙不全）與第 12 條（抽取式之缺陷不會報錯 —— 18 與 20
都不觸發例外）之實例，記於此以備後續同類 gate 檢查。


## 第 4 列之實測依據（R-U9 之涵蓋驗證，2026-08-17）

**量測對象**：`features/comfort/inputs/Pop Up List HMI R1 SR24 Post 2A
(Dec 15, 2023).xlsx`，工作表 `Main`，資料列 row 3–1343（**1341 列**，
A 欄非空 1341）。

**量測條件（自陳，§4.3 之漏抽同型風險）**：

| 抽取式 | 範圍 | 唯一 id |
|---|---|---|
| `\bPU\d{4}\b`（含詞界）| A 欄 | 1330 |
| `PU\d{4}`（**不含**詞界）| A 欄 | 1330 |
| `PU\d{4}` | **全表 17 欄** | 1331 |
| `PU\s*_?\s*\d{3,5}`（涵蓋底線／空白分隔）| 全表 17 欄 | 1340 |

**四式在本 feature 之 20 個 id 上結論相同**，故本次之涵蓋數與抽取式無關 ——
此點須明講：DR #2 之首次量測曾因漏抽底線形態而得 18（該次之 18 是缺陷），
**本次之 18 不是缺陷**，兩者同數而不同因。

**結果：18 / 20 命中，缺 `PU1087`、`PU1088`。**

- 兩者**落在該表之編號區間內**（`PU0001`–`PU1578`），非超出範圍；
  該區間內共 **248 個空號**，`PU1080`–`PU1088` 與 `PU1092`–`PU1095` 全為空號，
  而 `PU1089`／`PU1090`／`PU1091`（本 feature 亦引用）**在表內**
- 該表**確為正確之文件家族**：`Module` 欄 181 個相異值中含
  `Profiles`、`Profile Setup Assistant`、`Personal Account/Driver Profiles`、
  `Connected Personal Account` 等
- 兩個缺者皆出自 spec **`4.1.1`**（Profile Setup），與 `PU1088` 之 2 次引用

**處置**：依 02b 作業項 2 之明文「不足 → 具名列出缺哪幾個 id，轉 DR，
**不以近似版本替代**」——

- **未**移入 `spec-index/`
- **未**更新 `BASELINE.sha256`
- **A-UP06 不結案**

> **不以 18/20 充當到齊**：缺的那兩個正是 Profile Setup 之 popup，
> 而 spec 8.3 明文「The Profile Setup processes is a series of popups」——
> **缺口不在邊陲，在該功能的正中央。**


## 第 3／4 列之性質變更（06 輪，R-U27／R-U28）

**DR #4 之索取標的收窄**：原列「載有 PU1087／PU1088 之 Pop Up List 版本」，
**現改為「該二列之 popup 內文」**。依據：spec PDF p6 逐字載

> `PU1087` is displayed when users confirm Setting restore to default by
> pressing Yes in pop-up `PU_0118`. `PU1088` is displayed when settings have
> been successfully restored to default.

**即觸發條件 spec 自己給了，缺的只是那兩個 popup 上寫什麼。**
故 `4.1.1` 之 TC 得以生成，`PROF-002-03` 解除阻斷，本列由 HIGH 降 **MEDIUM**。

**DR #3 之性質改變**：由「索取缺件」改為「**上游覆蓋缺口**」——
`3.1`–`3.5` 之內容**存在且可讀**（05 輪自 PDF p5 抽出逐項清單），
037 只是沒有為它們產出 leaf。形態同 Comfort **R-C16**。

---

## DR #3 之關閉（26 輪，R-U56）—— **記載全數保留**

> **狀態：CLOSED — OUT-OF-SCOPE (R-U56，Pei 2026-08-18 裁定)。不送出。**

**關閉之理由（逐字取自 R-U56）**：
「037 之 180 leaf 母體即本 feature 之驗證範圍上界。
spec 有內容而 037 未為其產出 leaf 者，不生成 TC、不列覆蓋缺口、不向上游索取釐清。」

**保留之實測記載**（以下皆為事實，不因關閉而失效）：

| 項 | 記載 |
|---|---|
| `3.1`–`3.5` 之可讀性 | 05 輪自 PDF p5 抽出逐項清單，**內容存在且可讀** —— 故 A-UP02 非「內容不存在」 |
| 形態比對 | 與 Comfort **R-C16** 同形（「spec 有而 SWE 未涵蓋」）|
| 性質重估 | R-U28 曾將其由「索取缺件」改為「上游覆蓋缺口」—— **該重估之推理仍成立**，只是該類別現已裁為不屬我方範圍 |
| `10.1`／`11.1`／`11.2` | 為變體覆寫條款且無 SWE 需求 |

**明記：`3.1`–`3.5` 之使用不受本次關閉影響。**
R-U22／R-U46 裁定其為 `PROF-001-01`（**SWE 有寫之 leaf**）之 in-scope 依據；
`TC-001`／`TC-004` 之 `specification_reference` **繼續併列 `3.x`**，
其代價聲明（D-UP17-01：覆蓋率不得以引用欄推定）亦繼續有效。

**關閉的是「向上游索取」這件事，不是那些條文的可用性。** 兩者不同。

---

## RD #5 —— R1 High 之 label 覆寫，其範圍是否及於全章（19 輪，J-7）

> **R-U57 加註（39 輪，Pei 裁定）**：本項之答覆**不回頭改已生成之 TC**，
> 只及於**其後生成者**。所免除者為**字面形式之返工**（label 之兩種寫法、
> remarks 措辭、reasoning 之委派敘述）；**不含判定翻轉** ——
> 若答覆顯示某條已生成之 TC 會**假失敗或假通過**，須具名上報再議。
>
> **Urgency：高 → 低。** 分析層自陳其「返工面積隨時間變大」之催促理由
> **自本裁定起失效** —— 不回頭改，返工面積就不隨批次增長。
> **惟仍應寄**：其價值在於其後批次寫得對，以及交付時上游知道我方問過什麼。


**問題**：`****R1 High Only: "Stellantis Account" to be replaced with
"Connected Account"` 之覆寫，**在版面上為列級** —— 其 `****` 標記與
PDF p14 之 Table EDPR1 中 `****“ Stellantis Account”` 那一列對應
（座標複位：註記於 x=101.4／y=275.9–286.7，該列於 y=289.8；表中其餘列無 `****`）。

**其是否推及全章之同名 label，版面無從判定。** 具體受影響者：

| 節 | 該節自己的字 | 若覆寫及於本節則應為 |
|---|---|---|
| 9.2（EDPR2）| `Stellantis Connected Account button` | `Connected Account button` |
| 9.1（EDPR1）| `Stellantis Connected Account will link to Connected Profile app` | `Connected Account will link to…` |

**現行處置（J-7）**：ER 維持各節之逐字；`PROF-088`（TC-020）之 remarks
註明兩形式指同一按鈕，且該 TC 驗的是**缺席**而非 label 內容，故不影響判定。

**索取標的**：該覆寫之適用範圍 —— 僅 Table EDPR1 之該列，或及於 ch9 全章之同名 label。

**若答案為「及於全章」**，須連帶處理：`lint_variant_labels` 之
`VARIANT_LABEL_OVERRIDES` 適用範圍、`PROF-085`（TC-017）之列項字面值
（現已用 Connected Account，屆時無須改）、以及 9.1／9.2 之 ER 逐字。

**性質**：spec 之歧義，非我方判準問題（§8.4.1「ambiguous source → preserve
ambiguity」）。

**送出方式（26 輪，R-U56 之拆分）**：**獨立送出，不再併 DR #3**。
DR #3 問的是「SWE **沒切**的東西怎麼辦」，已依 R-U56 關閉；
本項問的是**已存在之 leaf**（`085`／`088`）其條文怎麼讀 —— **兩者不同類**。
英文可寄版見 `docs/upstream/26_rd_queries.md`（Tier 3，由 Pei 寄出）。

---

## RD #6 —— 「有 app 之區域 × 不支援 connected profile 功能」之組合是否存在（23 輪，M-4）

> **R-U57 加註（39 輪，Pei 裁定）**：本項之答覆**不回頭改已生成之 TC**，
> 只及於**其後生成者**。所免除者為**字面形式之返工**（label 之兩種寫法、
> remarks 措辭、reasoning 之委派敘述）；**不含判定翻轉** ——
> 若答覆顯示某條已生成之 TC 會**假失敗或假通過**，須具名上報再議。
>
> **Urgency：高 → 低。** 分析層自陳其「返工面積隨時間變大」之催促理由
> **自本裁定起失效** —— 不回頭改，返工面積就不隨批次增長。
> **惟仍應寄**：其價值在於其後批次寫得對，以及交付時上游知道我方問過什麼。

> **本項另有一層**：RD #6 之答覆決定 `TC-077` 之 remarks 是否須記其為
> **「不可佈署之條文條件」** —— 該記載屬**交付內容之一部分**，
> 非僅內部判讀。故本項雖 Urgency 低，其答覆仍會改變一份交付欄位。


**問題**：`9.2`（EDPR2）有兩個獨立條件 ——

1. `for regions without the <Brand> app`
2. `if the vehicle does not support the connected profile feature`

22 輪為條件 2 生成 `TC-077`。為使兩條件不同時成立（否則失敗時分不出是哪一個
沒生效），其 pre-condition 加了 **「The vehicle is in a region with the brand app」**。

**該前提是推得的，spec 未明言該組合存在。** 若實務上「不支援該功能」恆與
「該區域無 app」同時發生，則 `TC-077` 之情境**在實車上造不出來**。

**索取標的**：是否存在（或可佈署）「區域有 `<Brand>` app、而車輛本身不支援
connected profile 功能」之車輛組合？若存在，其典型成因為何（trim／option
package／telematics 訂閱狀態）？

**不論答覆為何，`TC-077` 不刪** —— 條件 2 是條文寫的；
**情境造不造得出來，與該條件該不該被測，是兩件事**（§8.4.1）。
若答覆為「不存在」，則處置改為：於 `TC-077` 之 remarks 記載其為
**不可佈署之條文條件**，並轉為上游澄清請求（該條件是否為贅語）。

**性質**：spec 之情境可佈署性，非我方判準問題。

**送出方式（26 輪，R-U56 之拆分）**：**獨立送出，不再併 DR #3**。
本項之 leaf（`088`）存在、TC（`TC-077`）已生成，**答案會改變已生成之內容** ——
與 DR #3／#7 之「該不該有 leaf」不同類。
英文可寄版見 `docs/upstream/26_rd_queries.md`（Tier 3，由 Pei 寄出）。

---

## RD #7 —— `9.1.1` 之另一側無 leaf：大螢幕之 username／avatar 版面（23 輪，M-5）

> **狀態：CLOSED — OUT-OF-SCOPE (R-U56，26 輪 Pei 裁定)。不送出。**
> 以下**全部實測記載保留為歷史**，包含「037 在 8.8 對螢幕尺寸切兩個 leaf、
> 在 9.1.1 只切一個」之佐證 —— **但不因其不一致而代其補**。
> **037 之 180 leaf 母體即範圍上界；SWE 沒切的，我方不代其決定該不該有。**

**問題**：`9.1.1`（EDPR1.1）逐字只述 8.4 吋螢幕之**差異側**：

> `8.4inch screen size will not show the username and avatar to the left of
> the Edit Profile List`

其**另一側**（大於 8.4 吋之螢幕**會**在清單左側顯示 username 與 avatar）
為該句之必然蘊含，**而 037 之 180 leaf 母體中無對應 leaf**
（本輪以 `build_batch_context.leaf_rows()` 全量查證：`9.1.1` 僅
`SWE1-HMI-PROF-086` 一個 leaf，其標題為 `(8.4") Hide Username/Avatar Left
of Edit List`）。

**037 自己在別處是分兩個 leaf 的** —— 這是本項之關鍵佐證：

| 節 | leaf | 標題 |
|---|---|---|
| 8.8 | `SWE1-HMI-PROF-076-02` | `(8.4"+) Avatar Displayed Above Save & Continue Button` |
| 8.8 | `SWE1-HMI-PROF-076-03` | `(7") Avatar Displayed Next to Save Button` |

**同一份 037，對螢幕尺寸之兩側在 8.8 切了兩個 leaf，在 9.1.1 只切了一個。**
故此非「037 之慣例如此」，而是**該節之覆蓋缺漏**。

**索取標的**：`9.1.1` 之另一側是否應有 leaf（比照 `076-02`／`076-03` 之作法）？
若應有而未有，其 leaf 母體 180 之數字是否須更新？

**我方現況**：**不自行補 leaf**（母體為 037 之權威，§8.2）。
本項不影響現行 78 條之任何判定，亦不列入覆蓋率分母之爭議 ——
但**在 037 補齊之前，大螢幕之該版面無人驗**。

**性質**：~~上游覆蓋缺口~~ → **OUT-OF-SCOPE（R-U56）**。~~併 DR #3 送出。~~
**不送出。** 原判之形態比對（同 DR #3 之 `3.1`–`3.5`）仍然成立 ——
只是那個形態本身現已裁為不屬我方範圍。

## RD #8 —— `5.13.2` 之確認 popup：`PU0626` 與 `PU_0129` 是同一個嗎（40 輪，第五批）

**狀態：未送出（Tier 3，屬 Pei）。Urgency：低。**
**我方已依 41 包 §四逕行修正，不待答覆**（見文末「41 輪之處置」）。

**問題**：`5.13.2`（ALLPR2.2）在同一段內指了**兩個**確認 popup id：

> Using the “Clear Personal Data” setting (**and confirming from popup
> PU0626**) will delete all profiles … **PU1089 is displayed when users
> confirm data clearing by pressing Yes/Ok in pop-up PU_0129.**

037 之 `SWE1-HMI-PROF-041-03` 把兩者並列為
`the confirmation prompt PU0626/PU_0129` —— **即 037 自己也未決**。

**三種可能，其後果不同**：

| 讀法 | 對測試之影響 |
|---|---|
| 同一個 popup 之兩個 id（其一為舊編號）| 現行寫法正確，無須改 |
| 兩段確認（先 PU0626 再 PU_0129）| **procedure 少了一步**，`041-01`／`041-02`／`040` 三條會假失敗 |
| 兩個車型／市場各用其一 | 需切為兩條，或於 pre-condition 具名適用側 |

**我方現況（依 §8.4.1 保留歧義，不推定）**：
- `SWE1-HMI-PROF-041-03`／`-04`（`NR1L-UserProfiles-142`／`143`）之
  procedure 取 **`PU_0129`** —— 條文把「按 Yes/Ok 觸發 PU1089」這件事
  綁在該 id 上
- `SWE1-HMI-PROF-040`／`041-01`／`041-02`（`139`／`140`／`141`）取
  **`PU0626`** —— 條文把「執行清除並確認」綁在該 id 上
- 兩者於 remarks 各自具名其取捨

**注意其與 R-U57 之界線**：若答覆為「兩段確認」，
**受影響之三條會假失敗** —— 依 R-U57 之適用範圍，
那**不屬形式差異**，須具名上報再議，不得逕以「不回頭改」帶過。

### RD #8 之處置（41 輪，依 41 包 §四之授權）

41 包授權：「凡經判定會造成**假失敗或假通過**者，逕行修正並於上繳具名，
不待 RD 答覆」。界線為「不得改變該 TC 之驗證目標」。

**修正**：五條之確認步驟一律改為

> `Press Yes on each confirmation popup PU0626/PU_0129`

**為什麼這樣寫不假失敗**：
- 兩者若為**同一個 popup 之兩個 id**（其一為舊編號）→ 該步驟按一次，與原寫法等價
- 若為**兩段確認** → 該步驟按兩次，原寫法之「少一步」不再發生
- 若為**兩個車型各用其一** → 執行者按其車上出現者，另一個不出現

**驗證目標未變**：五條所驗者仍為
「清除後之落點」（`139`／`140`／`141`）與「進度／完成 popup」（`142`）、
「失敗 popup」（`143`）—— 未換 leaf、未換節、未換觸發，合於 §四之界線。

**RD #8 仍照送**，其價值在上游知道我方問過什麼；但**不作為修正之前提**。
