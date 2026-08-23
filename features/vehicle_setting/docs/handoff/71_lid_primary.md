# 71 下放包 — R-VS67（LID 為主）、全數送出、45 輪

分析層寫入，2026-08-23。Pei 裁定：**先以 LID 為主；DR 全送。**

---

## 1. R-VS67 —— 訊號名與值域一律取 LID 之 Atlantis High 欄組

```
R-VS67（Pei 2026-08-23）
訊號名、所屬 message、值域，**一律取 `Logical Identifiers and CAN Mapping
v1.76` 之 `Atlantis High` 欄組**（`Proxi & Configuration` 分頁則為
`Atlantis & Atlantis High` 欄組）—— **依本專案之架構，不依條文之架構標籤**。

CFTS044 條文內嵌之訊號名（如 `shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm`）
與 LID 之他欄組（`Atlantis`／`CUSW`／`PowerNet`），**僅作旁證，不作取值來源**。

**推翻**：R-VS51(2) 之「條文標 `Atlantis Mid` → 取 LID `Atlantis` 欄組」
—— 其分流依條文之架構標籤，而 R-VS19″ 已定該標籤為**來源沿革**而非適用性。
**沿革不應決定取值。** R-VS51(1)(3) 不變。

**實例**：`$FL_VS_RQ_TGW$`
  條文（Atlantis Mid）內嵌   `TELEMATIC_VEHICLE_SETUP.FL_VS_Cmd_Tlm`  ← 旁證
  LID `Atlantis` 欄組        `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm` ← 旁證
  **LID `Atlantis High` 欄組  `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm`（1 bit，
                              `0 = Not_Pressed`／`1 = Pressed`）← 取此**

**連帶**：
(a) 該 65 leaf 之訊號**存在於基線 DBC**（`SETUP3` 於 `PDT27_E2A_R4_BHCAN` 內），
    L-VS2 判 **PASS**，其 `dr_dependent = DR-25` **解除**，`impl_gap` **不設**。
(b) DR-25′ **撤回** —— 其前提（訊號不在基線 DBC）依本條不再成立。
(c) **但四階行為之描述無法以 1 bit 訊號斷言** —— 該衝突即 DR-15′ 之標的。
    **本條為暫行處置**，DR-15′ 維持送出；其覆後須複檢所有以
    `*_Tlm` 斷言循環降階之 TC。
(d) 依 (c)，`dr15_exposed` 之範圍**擴大**：原 6 條 ＋ 依本條新寫者。
    **每一條以 `*_Tlm` 為斷言標的之 TC 皆須標 `dr15_exposed = yes`。**
```

**這是 Pei 之裁定，不是分析層對 DR-15 之作答**（R-VS44）——
DR-15′ 仍送出，覆後以其答覆為準。

---

## 2. R-VS66 —— 規格明確而實作未見之處置（保留，惟本例已不適用）

```
R-VS66（分析層裁定 2026-08-23）
規格與實作不一致時，依「規格是否明確」而分：

(a) **規格明確而實作未見** → 依規格撰寫測項，**不阻塞、不撤回、不開 DR**；
    執行階段測不到即為實作缺口，開 issue 予 RD。
    TC 標 `impl_gap = <訊號名>`，交付揭露列為「預期發現實作缺口」。
(b) **規格本身有兩讀或自相矛盾** → 開 DR，其標的為規格之釐清。

理由：SWE.6 之測項依需求而立，不依實作而立；
以實作之缺席否決需求，等同讓實作定義驗證範圍。

**本例（`*_Cmd_Tlm`）依 R-VS67 改由 LID 取名，已無實作缺口，(a) 不適用。**
本條備日後同型之用。
```

---

## 3. DR 全數送出 —— **十份**（DR-25′ 撤回後）

| # | DR | 型 | 標的 |
|---|---|---|---|
| 1 | **DR-15′** | 規格兩讀 | 請求訊號之階數 vs 1 bit（160 leaf，含依 R-VS67 新寫者） |
| 2 | **DR-19** | LID／CFTS 不一致 | `$EngRun_Stat$` 四值無對應（7 leaf） |
| 3 | DR-17 | 規格缺件 | Comfort 無單階座椅條文（14 leaf） |
| 4 | DR-18 | 確認型 | 座椅值域之四類書寫問題（前綴交叉／值退化／大小寫／`Steats`） |
| 5 | DR-20 | 素材缺件 | 未具名之 HMI 需求（`4858560`） |
| 6 | DR-21 | 值域無對應 | B2 類殘餘 |
| 7 | DR-22′ | 素材缺件 | PROXI 表之四參數（是非題，附我方推定值） |
| 8 | DR-23 | 素材缺件 | `TLM HMI Document`／`PDO graphics` 之具名 |
| 9 | DR-24′ | 規格未給值 | `<Tsend>`／`<Tdisplay>`（43 leaf） |
| 10 | DR-26 | 規格未載 | Rear View Camera 按鍵於非 `IGN_RUN` 之狀態 |
| 11 | DR-27 | 規格冗餘 | 四 leaf 之可測內容無法分辨 |
| — | ~~DR-25′~~ | — | **撤回（R-VS67(b)）** |
| — | ~~DR-8′~~ | — | 已撤回（R-VS62′） |
| — | DR-11 | — | `SWE1-VC-HeatedSteeringWheel-009` 之 CFTS100 歸屬（1 leaf） |

**共十一份**（含 DR-11）。**送件文以 70 包 §2 為底，補入 §4 之新增證據段。**

---

## 4. 送件文之補充證據段（加於 DR-15′ 之末）

> **補充證據（2026-08-23）**：我方另查 `PDT24_E2A_R3.3_BHCAN2`
> （VersionYear 22／Week 23）與 `PDT24_E2A_R8.5_FDCAN8`（Week 42）兩份資料庫。
> 併同基線之 `PDT27_E2A_R4_BHCAN`／`R5_FDCAN8`（皆 25 年第 50 週），**四份中**：
>
> - `TELEMATIC_VEHICLE_SETUP2` **一次都不存在**
> - `FL_HS_Cmd_Tlm`／`FR_HS_Cmd_Tlm`／`FL_VS_Cmd_Tlm`／`FR_VS_Cmd_Tlm`／
>   `HSW_Cmd_Tlm` 五者 **一次都不存在**
> - `TELEMATIC_VEHICLE_SETUP3` 之 `FL_HS_Tlm`／`FR_HS_Tlm`／`FL_VS_Tlm`／
>   `FR_VS_Tlm`／`HSW_Tlm` **自 2022 年第 23 週起即為 1 bit**、
>   值表 `0 = Not_Pressed`／`1 = Pressed`，**三年四版未變**
>
> 即請求訊號為 1 bit 在本平台上為**跨版本一致**。
> 我方現依 `Logical Identifiers and CAN Mapping v1.76` 之 `Atlantis High`
> 欄組撰寫測項（即 `TELEMATIC_VEHICLE_SETUP3.*_Tlm`，1 bit），
> **循環降階之四階行為因而無法以該訊號斷言**。請依此確認上開三選項。

---

## 5. 45 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/69_review_round43.md   ← 44 輪（未執行）
  features/vehicle_setting/docs/handoff/71_lid_primary.md      ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/39_lid_primary.md，六節先留空。
D-2  逐字轉錄 71 包 §1 之 **R-VS67**、§2 之 **R-VS66**、
     69 包 §1 之 **R-VS65** 入 RULINGS.md；
     **R-VS51(2) 標「經 R-VS67 推翻」**（原文保留）。
D-3  `DATA_REQUESTS.md`：**DR-25′ 標「撤回，R-VS67(b)」**（原文保留）；
     其餘十一份標「送出 2026-08-23／待覆」**（依 Pei 之實際送出回報，不推定）**。
D-4  `delivery_disclosure.md` 依 69 包 §3 分兩節。
     ANOMALIES.md 依 R-VS35 分線列兩數。D-6 照做。

## 作業（三項，R-VS25）

W-127 **依 R-VS67 全量重跑**
      (1) 訊號名／message／值域之來源一律改取 LID `Atlantis High` 欄組
          （`Proxi & Configuration` 則為 `Atlantis & Atlantis High`）
      (2) **錨點（R-VS54，兩側皆須有標的）**：
            必命中 —— `$FL_VS_RQ_TGW$` 須解出 `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm`
                       且 L-VS2 判 **PASS**（其於基線 DBC 存在）
            必不命中 —— 任一 token 若仍解出 `*_Cmd_Tlm`，即本條未生效
      (3) 全量重跑分級，列 W0／W1／W2 與 **138/2/97** 之對照；
          `generatable` 與 **池** 之新規模
      (4) **`dr_dependent = DR-25` 之標記全數解除**；
          **凡以 `*_Tlm` 為斷言標的者標 `dr15_exposed = yes`**（R-VS67(d)）

W-128 **已交付 143 條之訊號名複檢**
      依 R-VS67 逐條檢查其 procedure／ER 之訊號名是否取自 LID `Atlantis High`；
      不符者列出並改寫，產 `_v{n+1}`，原版保留。
      **必列**：需改寫之條數、逐條之「原名 → 新名」。

W-129 **batch20**
      自 W-127 後之池選取，依 R-VS58 優先序。
      **批次規模 ＝ 池扣 held_out**（依 R-VS64，不寫死）。
      套 profile ＋ 各現行條文 ＋ Sibling Rows；
      §9 十七項自檢 ＋ 值表核對 ＋ 錨點。

**W-124／W-125／W-126（44 輪）順延** —— 其分級對照數將因 R-VS67 而全面改變。

## 禁區

git 不執行。**不實寫 036 母本**。不執行備份（屬 Pei）。
不補素材、不代擬條文、不自行調和數字。各版保留不刪。
**不得以條文內嵌之訊號名或 LID 他欄組為取值來源**（R-VS67）。

## 升級條件

W-127(2) 之任一錨點未命中；
W-127(3) 之 `generatable` 較 138 增加 < 40（則 R-VS67 之解鎖不如預期）；
W-128 之需改寫條數 > 80（則過半已交付 TC 之訊號名須換）。
```

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| **1** | **十一份 DR 送出**（70 包 §2 之送件文 ＋ 71 包 §4 之補充證據段） |
| 2 | 兩份 PDT24 DBC 是否入 `inputs/`（標 `evidence-only`，**不得作為訊號名或值域之來源**） |
| 3 | **G2 pilot #3＋#4 之 28 條** —— 分析層次包出建議分類 |
| 4 | **G3 母本備份 ＋ sha256**（母本現 `ebe5a65f…`） |
| 5 | `AA` 欄之作者姓名 |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| **R-VS67** | 訊號名與值域一律取 LID `Atlantis High` 欄組；推翻 R-VS51(2) | **Pei** |
| R-VS66 | 規格明確而實作未見者照寫並開 issue 予 RD；規格兩讀者開 DR | 分析層 |
