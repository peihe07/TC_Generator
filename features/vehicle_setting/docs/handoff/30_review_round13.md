# 30 下放包 — 13 輪覆核：R-VS19′ 取證完畢、DR-17、Layer 3 建構規則、14 輪指令

分析層寫入，2026-08-20。對象：`docs/upstream/11_arch_scope.md`。

**覆核結論：接受。** 三項作業皆給出可裁定之證據，
且 `(a) = 0、母體 237 完整` 至此**完成舉證**（11 輪只讀 6 筆，本輪補讀 2 筆）。

---

## 1. R-VS19′ —— 證據完整，分析層建議 (c)

### 1.1 決定性證據

| 組 | `Radio` 含 R1L／R1L-R | `ECU` 為頭端 | `Market` |
|---|---|---|---|
| 純 Mid（118 條） | **118 / 118** | **118 / 118** | All |
| 無 Mid（127 條） | 127 / 127 | 127 / 127 | All |

**兩組在三個屬性上完全一致。**

旁證且為逐字：純 Mid 之 `4859399`／`4859463` 全文為
`The requirements in this section are applicable for R1 Low only from SR22 and beyond.`
—— **標記 `Atlantis Mid` 之章節，其自身宣告適用於 R1 Low。**

### 1.2 分析層之建議

**架構標籤在 CFTS044 中不是適用性判準，是條文之來源沿革標記。**
`Atlantis Mid` 之 118 條同時標記 R1L／R1L-R、由 LTM／ETM 執行、
`Market: All` —— 與本專案之 121 條無 Mid 條文在適用性屬性上不可區分。

```
待 Pei 裁：R-VS19′（分析層建議採 (c)）
CFTS044 條文之適用性判準改為：

  in-scope ⟺ `Artifact Type` 含 `Subsystem Functional Requirement`
             ∧ `Radio` 含 `R1L` 或 `R1L-R`（欄為空者視為不限）
             ∧ `ECU` 含 `LTM`／`ETM`／`RRM` 之一

`EE Architecture` **降為輔助資訊，不作為排除判準**。

理由：實測 118 條純 Mid 與 127 條無 Mid 在 `Radio`／`ECU`／`Market`
三屬性上完全一致；且純 Mid 之章節自身宣告 `applicable for R1 Low`。
架構標籤反映條文之來源沿革（自 Atlantis Mid 遷入），非其適用範圍。

連帶效果：
(1) R-VS19 之「他架構條文之值域一律不取用」**縮限為
    `CUSW`／`PowerNet` 專屬者**；`Atlantis Mid` 不再排除。
(2) R-VS20 之第一階範圍擴大：112 個純 Mid leaf 之值域
    **得自其自身 CFTS044 條文取得**，不必落到第二階。
(3) 先前以舊判準算出之 in-scope 數（1,128／294）皆須重算。
(4) **`$HSW_StatFailSts$` 之值域**（R-VS20 實例，原稱 in-scope 無值域、
    走第二階）**須重新檢查** —— 其 Atlantis Mid 條文若入 in-scope，
    第一階即有值。

**本條影響 112 / 237 個 leaf（47%）之值域來源，屬 TC 內容，故送 Pei。**
```

---

## 2. A-VS46 —— 實質缺口，分析層擬 DR-17

Comfort 全母體 129 個 leaf 中，**唯一**明示 `Single-Level` 者為 `SWE1-HVAC-063`，
其主詞為 `heated steering wheel`；以 `single[\s-]?level` ∧ `seats?` 交叉查詢**命中 0**。

即 **Comfort 側沒有任何「單階座椅」之條文**，
而本 feature 有 14 個 `OneStageHeatedSeat` leaf（其中 12 個已委派），
其委派標的之條文開頭逐字為 `For Multi-Level Heated/Vented seats`。

```
DR-17（分析層擬，Urgency High，Pei 送出）
CFTS044 定義單階加熱座椅之配置（`$Heated_Seat_Levels$ = [1]`），
本 feature 有 14 個對應之 SWE leaf。

而 Comfort HMI Logic and Flow（SWE1-HVAC-*，全母體 129 個 leaf）中，
所有座椅加熱／通風之畫面行為條文，其開頭皆逐字為
`For Multi-Level Heated/Vented seats`；
明示 `Single-Level` 者僅 `SWE1-HVAC-063`，且其主詞為加熱方向盤。
以 `single-level` ∧ `seat` 交叉查詢命中 0。

請確認單階加熱座椅之畫面行為：
(a) 由 Comfort 之某條文涵蓋而未明示階數？若是，請指明其 leaf id
(b) 單階座椅無彈窗、直接切換，故 Comfort 無對應條文？
(c) 該行為由第三份文件承載（如 TLM HMI Document）？

影響：14 個 `OneStageHeatedSeat` leaf 之委派界線（R-VS7）。
在答覆前，該 12 個已委派之 leaf 其委派標的與其配置條件矛盾。
```

```
分析層裁定 2026-08-20（DR-17 未決期間之處置）
`delegation_lookup.tsv` 中 Layer 3 為 `OneStageHeatedSeat` 之 12 列，
`delegate` 由 `yes` 改為 **`pending`**（新值），
`basis` 註明「A-VS46／DR-17：所引 Comfort 條文明文限定 Multi-Level，
與本 leaf 之單階配置矛盾」。

**不改為 `no`** —— `no` 表示查無對應，而此處是「有對應但矛盾」，
二者在下游之處置不同。**不改為 `blocked`** —— `blocked` 依 R-VS17
專指 TLM HMI Document／PDO graphics 之缺件。
```

---

## 3. A-VS47 —— Layer 3 之建構規則

`LeftFrontHeatedSeat-004`／`-011` 各引四節四側，是**四側共通需求**，
卻因 SWE ID 中段 token 而掛在左側名下 → Layer 3 左右不對稱（17 vs 15）。

```
R-VS37（Layer 3 之建構，分析層裁定 2026-08-20）
Layer 3 不得純以 SWE ID 中段 token 機械切分。
一個 leaf 之 Layer 3 歸屬，須以其 `reqid_list` 所跨之 CFTS044 章節判定：

  該 leaf 之 reqid 全部落在單一章節      → 依該章節之 Layer 3
  該 leaf 之 reqid 跨越多個同層章節      → 歸 `Common Features`
                                            （其為四側／多側共通需求）

SWE ID 中段 token 僅作為**預設值**，與章節判定衝突時**以章節為準**，
並於 `framework.md` 逐筆記明其原始 token 與改判依據。

理由：037 之 SWE ID 命名反映其撰寫時之歸檔，非其需求之實際範圍。
實例：`LeftFrontHeatedSeat-004` 之 reqid 跨 1.3.2.1.3.1～.4 四節
（左右 × 加熱通風），其內容為 `the HU shall use $Heated_Seat_Levels$
to determine which levels are supported` —— 四側共通。
```

**此規則影響 framework Layer 3 之組成**，故 `framework.md` 之簽核
（P19）**應俟 W-46 全掃後**，不宜先簽。

---

## 4. 14 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/30_review_round13.md 本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/12_layer3_and_convergence.md，六節先留空。
D-2  逐字轉錄 30 包 §3 之 R-VS37 入 RULINGS.md。
D-3  ANOMALIES.md：新開 **A-VS48**（W-42 之四屬性對照在條文層級去重，
     未查同一 leaf 之多 reqid 屬性是否一致；`Model Year` 為唯一有實質
     差異之屬性，未追因）。依 R-VS35 列兩數。
D-4  `DATA_REQUESTS.md` 新開 **DR-17**（30 包 §2 全文）。**不送出。**
     `delegation_lookup.tsv` 之 12 列依 30 包 §2 改為 `pending` 並註 basis。

## 作業（三項，R-VS25）

W-44  委派收斂之重做（08 包 W-34(1) 之 `0 / 174` 撤回後重測）
      依 W-43 之階數橋接（`Single↔One`、`Multi↔{Two,Three}`）重做收斂：
      (1) 逐列判定其所引 Comfort leaf 中，哪些之階數標記與本 leaf 相容
      (2) **實測收斂上限**：11 輪自陳其上限為「14 個 OneStage 可分離、
          其餘 84 個仍不可分」——**該數未實測，本輪須給實測值**
      (3) 側別維度同時併入（2 / 129 明示側別者）
      產出更新後之 `delegation_lookup.tsv`，並列「收斂前／後」兩組計數

W-45  加熱方向盤側之階數委派複核（11 輪 §6-2）
      本側 `HeatedSteeringWheel`(20) 與 `HeatedSteeringWheelManagement`(11)
      之 Layer 3 名稱不帶階數，而 Comfort `-062`（Multi-Level）與
      `-063`（Single-Level）明示。
      (1) 以 `$Heated_Steering_Levels$`（LID 值域 `0=1 Level`／`1=2 Levels`／
          `2=3 Levels`）之引用，判本側 31 個 leaf 之階數歸屬
      (2) 與 `-062`／`-063` 之委派對映交叉，列出矛盾者
      **若出現與 A-VS46 同型之矛盾（單階 leaf 委派至 Multi 條文），
      併入 DR-17 之提問，不另開 DR**

W-46  Layer 3 歸屬之全掃（依 R-VS37）
      (1) 對 237 個 Functional leaf，以其 `reqid_list` 所跨章節重判 Layer 3
      (2) 列出「token 判定」與「章節判定」不一致者，逐筆具名
          （已知至少 2 筆：`LeftFrontHeatedSeat-004`／`-011`）
      (3) 追因 §1.3.2.1.3.4（RF Vented）之 **30 條** 與其餘三節之 29 條
          之差 1
      (4) 更新 `framework.md` 之 Layer 3 表，逐筆記明原始 token 與改判依據。
          **framework 仍不鎖定**（Tier 2 屬 Pei）

## 禁區

git 寫入性操作一律不執行。不補素材、不代擬條文、不自行調和數字。
**不得自行修改 in-scope 判準或 R-VS19**（R-VS19′ 待 Pei，P20）。
**不得鎖定 framework。**

## 升級條件

W-44(2) 之實測收斂上限與 11 輪自陳之「14 / 84」不符；
W-45(2) 出現矛盾；
W-46(2) 之不一致筆數超過 10；
實測與 30 包之數字不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。
```

---

## 5. 待 Pei

| # | 事項 | 建議 |
|---|---|---|
| **P20** | 裁 **R-VS19′**（Atlantis Mid，112 leaf 佔 47%）—— **證據已完整** | 採 (c)，見 §1.2 |
| P18 | 裁 **R-VS7(a)′**（委派句精度） | **俟 W-44 之實測收斂上限後再裁** —— 08 包之前提（資料無可收斂維度）已撤回，選項須重估 |
| P19 | framework 簽核 | **俟 W-46 全掃後** |
| — | **DR-17 送出**（§2 全文，Urgency High） | 與 DR-15 一併 |

**P20 現為唯一證據完整而未裁者。** 其未裁之影響：
112 個 leaf 之值域來源懸置，且 `$HSW_StatFailSts$` 等 token 之
R-VS20 階梯歸屬可能改變。

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS19′ | 適用性判準改以 `Radio`＋`ECU`；架構標籤降為輔助 | **待 Pei（P20）** |
| R-VS37 | Layer 3 以章節判定，token 僅為預設值 | 分析層 |
| DR-17 | Comfort 側無單階座椅條文（14 leaf） | 分析層擬，Pei 送出 |
| `delegate = pending` | DR-17 未決期間之第三種狀態 | 分析層 |
