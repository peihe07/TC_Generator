# 63 下放包 — Pei 五項裁定（R-VS59～R-VS62）、40 輪

分析層寫入，2026-08-23。**交付 109／池餘 1 → 本包後預估池 ≥ 60。**

---

## 1. R-VS59 —— 委派不等於不寫（**取代 R-VS7(a) 之效果**）

```
R-VS59（Pei 2026-08-23）
**委派不免除產出 TC 之義務。**

R-VS7(a) 原令「本 feature 之 TC 不重複驗證 Comfort 已擁有之畫面行為」，
其實際效果為該類 leaf 標 `delegate = blocked/pending` 而**不產 TC**。
**該效果撤回。**

改為：
(1) 凡 037 之 Functional leaf，**一律產 TC**，不因委派而免。
(2) 其畫面層之內容，**取自 Comfort feature 之素材**：
      `features/comfort/inputs/FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx`
      `features/comfort/inputs/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`
      `features/comfort/inputs/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`
      `docs/reports/delegation_lookup.tsv`（本 feature leaf → Comfort leaf 之對照）
(3) `reasoning` 仍記委派句（R-VS7(a)′ 之群層級指名），
    **其作用由「故不寫」改為「其畫面層之來源為此」**。
(4) Comfort 素材中查無對應者，該畫面層斷言標 `PENDING: DR-{n}` 並登記；
    **不得以「已委派」為由略去該 TC**。

`delegate` 欄之語意隨之改變：
  `yes`     → 畫面層取自 Comfort 素材，**仍產 TC**
  `pending` → 委派對象未定（DR-17），**仍產 TC**，畫面層標 PENDING
  `blocked` → **廢除該值**；其原標的改依 (2)(4) 處置

`generatable` 之推導式改為：`writable ∈ {W0, W1}`（**不再扣 delegate**）。
```

**預估效果**：`delegate ∈ {blocked, pending}` 之 leaf 重回池內。
16 個 `Fail_Present` leaf ＋ 12 個 `OneStageHeatedSeat` ＋ 其餘 blocked 者。

---

## 2. R-VS60 —— A-VS103：跨列引入，准

```
R-VS60（Pei 2026-08-23）
`FR_VS_Cmd_Tlm` 之值域**得自 `FL_VS_Cmd_Tlm` 之 LID 列跨列引入**。

依據：52 包 §3 已依 R-VS38 判 LID 列 770／790 之 `Heated_seat_*` 前綴為
轉錄錯誤，其正確前綴為 `Vented_Seat_*`；`FL_VS_Cmd_Tlm`（列 769）
之四階值域為同一對稱側之正確記載。

引入後 `spec_variables.tsv` 之該列須標 `value_source = cross-row(FL_VS_Cmd_Tlm)`，
並保留 `suspect_prefix` 標記。**14 leaf 之值域就此解。**
DR-18 之該項維持（確認型，不阻塞）。
```

---

## 3. R-VS61 —— DR-19：無匯流排對應者，寫分析所載之名

```
R-VS61（Pei 2026-08-23）
規格或 037 分析報告所載之值，於 LID 與 DBC 皆無對應時，
**仍產 TC，其值取分析／規格所載之逐字名**，不做對映、不留空。

書寫形式：`<MESSAGE>.<Signal> = <來源逐字值>`
  —— **不附 `(<label>)`**（無 raw 碼可附，附之即造值）
`reasoning` 須記「該值於 LID 與 DBC 皆無對應，取 CFTS044／037 之逐字」，
並標 `dr_dependent = DR-{n}`。

實例：`$EngRun_Stat$` 之 `IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN`
  → 寫作 `STATUS_CCAN3.EngineSts = IDLE_STBL`，標 `dr_dependent = DR-19`。

**本條與 R-VS57 同源**：來源說有而快照沒有，以來源為主。
**與 §8.4.1 之界線**：寫來源之逐字為轉錄；**推一個 raw 碼出來才是造值**。

DR-19 維持送出（覆後補 raw 碼），其性質由阻塞轉確認。**解 7 條。**
```

---

## 4. R-VS62 —— DR-8′：車型碼取自 PROXI 表

```
R-VS62（Pei 2026-08-23）
`$VC_VEH_LINE$` 之車型碼取自 `PROXI_HDCC27_R3_20250424.xlsx`
之 `Format` 分頁列 466（`Car_Configuration_15` ／ `Vehicle_Line_Configuration`）。

其值表較 LID v1.76 之列舉為長 —— LID 截斷於 `101 = WL (65 Hex)`，
PROXI 表續至 `130 = HDCC (82 Hex)`。

已解之對應（逐字自該表）：
    332  → 105 (69 Hex)
    WS   → 104 (68 Hex)
    DT   → 124 (7C hex)
    HDCC → 130 (82 Hex)

**仍未解**：`M182`／`M189`／`M240` —— 三者於該表命中 0。
DR-8′ 縮限為此三碼。

適用範圍限 `VC_VEH_LINE` 一參數（同 R-VS49 之限縮方式）。
```

---

## 5. DR-15 之改寫（Pei 指示「說明更詳細一點」）

```
DR-15′（取代 17 包 §2.3；已送出者以本文補送）

**問題**：加熱／通風座椅之請求訊號，其承載階數或為單一位元？

**背景**：本專案（R1LR，Atlantis High）之 TC 撰寫中，
同一個邏輯識別碼在三份文件上得到互相矛盾之描述。

**證據一 —— CFTS044 之條文（標記 `[EE Architecture:Atlantis High]`）**
條文 `4858325`（`$FL_HS_RQ$`）／`4858355`（`$FR_HS_RQ$`）／
`4858385`（`$FL_VS_RQ_TGW$`）／`4858416`（`$FR_VS_RQ_TGW$`）
令 HU 依座椅**目前狀態**送出循環降階之值：

    目前 High   → 送出 Medium
    目前 Medium → 送出 Low
    目前 Low    → 送出 Off
    目前 Off    → 送出 High

即該請求訊號**承載四個階數值**。

**證據二 —— 基線 CAN 資料庫**
`PDT27_E2A_R4_BHCAN.dbc`（VersionYear 25／VersionWeek 50）之
`TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm`／`FR_HS_Tlm`／`FL_VS_Tlm`／`HSW_Tlm`
皆為 **1 bit**，值表為 `0 = Not_Pressed`／`1 = Pressed`。
即該請求訊號**只有二值**。

**證據三 —— LID v1.76 之同一列（列 769）**
同一個 LID `FL_VS_RQ_TGW` 於兩個欄組對映至不同訊號：

    `Atlantis` 欄組      → `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm`
                           2 bit，四階（Off／Low／Medium／High）
    `Atlantis High` 欄組 → `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm`
                           1 bit（Not_Pressed／Pressed）

且該表對請求類 LID 之 `Format` 欄**無位元寬宣告**，
而對狀態類 LID（如 `HeatedSeatFL`）明載 `2 bit signal`。

**我方之觀察**：三份證據可以一致地解釋為 ——
**四階者屬 Atlantis Mid 架構，二值者屬 Atlantis High**；
而 CFTS044 描述循環降階之四條條文標記為 `Atlantis High`，
**其架構標記疑為自 Atlantis Mid 遷入時未更新**。

**請確認（擇一）**：
(a) 請求訊號為 1 bit，階數之循環由 HU 內部狀態機決定
    → 則 `4858325` 等四條之描述應改；
(b) 請求訊號承載階數
    → 請提供其實際 signal 名、bit 寬、值表；
(c) 兩者皆是，依 EE Architecture 分流
    → 則 `4858325` 等四條之 `[EE Architecture]` 標記應為 `Atlantis Mid`。

**另請確認**：該行為是否隨 `$Heated_Seat_Levels$`（1／2／3）之配置而不同？

**影響**：Heated Seat 88 ＋ Vented Seat 72 共 160 個 SWE leaf 之
測試步驟、預期結果與測試設計方法（Functional Based vs Decision Table）。
其中已交付 **6 條** TC 之斷言落在該五個 token 上，覆後須逐條複檢。
```

---

## 6. DR-25′ —— 依 R-VS59 照寫，性質轉為確認

Pei 指示「就算算是 comfort 在這裡也是要寫，請去參考 comfort feature 之資料」。

**其 23 條之阻塞依 R-VS59 解除**：畫面層取自 Comfort 素材，
訊號層依 R-VS57 之 WARN 路照寫並標 `dr_dependent = DR-25`。
**DR-25′ 維持送出，性質由阻塞轉確認。**

---

## 7. 40 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/62_review_round38.md   ← 39 輪（W-110，未執行）
  features/vehicle_setting/docs/handoff/63_rulings_round39.md  ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/35_delegation_reopen.md，六節先留空。
D-2  逐字轉錄 63 包 §1–§4 之 **R-VS59／R-VS60／R-VS61／R-VS62** 入 RULINGS.md；
     **R-VS7(a) 標「其『不寫』之效果經 R-VS59 撤回」**（原文保留）。
D-3  `DATA_REQUESTS.md`：**DR-15 改寫為 DR-15′**（63 包 §5 全文）；
     **DR-8′ 縮限為 `M182`／`M189`／`M240` 三碼**；
     DR-19／DR-25′ 標「性質轉確認，不阻塞」。
D-4  `upstream/61_vf230_intake.md` **誤落於本 feature 之 upstream**，
     且編號與本序列衝突 —— **回報其正確歸屬，不自行搬移**。
D-5  ANOMALIES.md 依 R-VS35 列兩數。D-6 骨架對照照做。

## 作業（三項，R-VS25）

W-111 **依四條新裁重跑分級**
      (1) R-VS59：`generatable` 之推導式去除 `delegate` 之扣除；
          `delegate = blocked` 之值廢除，其標的改標 `screen_source = comfort`
      (2) R-VS60：`FR_VS_Cmd_Tlm` 跨列引入 `FL_VS_Cmd_Tlm` 之值域
      (3) R-VS61：`$EngRun_Stat$` 四值改判可寫，標 `dr_dependent = DR-19`
      (4) R-VS62：`VC_VEH_LINE` 之 `332`／`WS`／`DT`／`HDCC` 改判已解；
          `M182`／`M189`／`M240` 維持未解
      **錨點（R-VS54，須可失敗）**：
        16 個 `Fail_Present` leaf 須由 `generatable = no` 轉 `yes`
        `M182` 相關 leaf 須維持未解
      **必列**：W0／W1／W2 與 **126/2/109** 之對照；`generatable` 與 **110** 之對照；
      **池之新規模**

W-112 **Comfort 素材之畫面層對照表**（R-VS59(2) 之前置）
      以 `delegation_lookup.tsv` 為底，對每個 `delegate ∈ {yes, pending}` 之 leaf，
      自 Comfort 三份素材查其畫面層內容，產
      `docs/reports/screen_source.tsv`：
        leaf_id / comfort_leaf_ids / 畫面層內容之逐字節錄 / 來源檔與列 /
        查無對應者標 `PENDING`
      **必列**：查得／查無兩數。**查無者即 R-VS59(4) 之 PENDING 標的。**

W-113 **batch16 —— 10 條**
      自 W-111 後之池，依 R-VS58 之優先序（P0 優先）選取。
      **`Fail_Present` 類若入池，須優先納入**（A-VS116 之標的）。
      畫面層依 W-112 之對照表撰寫；套 profile ＋ R-VS52／R-VS56／R-VS57／
      R-VS59～62 ＋ Sibling Rows ＋ 無效值優先序；
      §9 十七項自檢 ＋ 值表核對 ＋ 錨點。

**W-110（未解值清單）順延** —— 其標的 40 leaf 中，
「前件無已解條件」16 者多因 `delegate = blocked`，本輪解除後須重算。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**R-VS61 之值不得附 `(<label>)`**（無 raw 碼可附）。
R-VS62 限 `VC_VEH_LINE` 一參數。不得合併 A-VS119／123 之 leaf。

## 升級條件

W-111 之二錨點任一未命中；
W-111 後之池 < 40（則四條新裁之解鎖不如預期，須逐條追因）；
W-112 之查無數 > 查得數（則 Comfort 素材不足以支撐 R-VS59(2)）。
```

---

## 8. 待 Pei

| 項 | 狀態 |
|---|---|
| **DR-15′ 補送**（已送出者補本文） | 63 包 §5 |
| **DR-25′**（23，性質轉確認）／DR-19（7，轉確認）／DR-8′（縮為三碼） | 待送 |
| DR-21／22′／17／18／20／23／24′／26／27 | 待送 |
| pilot #3 之 13 條分類 | 分析層次包出 |
| batch14＋15 共 23 條不在任何 pilot 範圍 | pilot #4 時機另定 |

---

## 9. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS59 | 委派不免除產出；畫面層取自 Comfort 素材；`blocked` 廢除 | **Pei** |
| R-VS60 | `FR_VS_Cmd_Tlm` 跨列引入 | **Pei** |
| R-VS61 | 無匯流排對應者取分析所載逐字名，不附 label | **Pei** |
| R-VS62 | `VC_VEH_LINE` 取 PROXI 表列 466；DR-8′ 縮為三碼 | **Pei** |
| DR-15′ | 三證據並陳、三選項、含架構分流之觀察 | 分析層擬 |
