# RD Feedback — Comfort HMI（FW036 / R1L SWE1）

**產生於**：CMF-06 §3-6，2026-09-22。**收件對象**：RD（由 Pei 送出）。
**性質**：本交付（`…_SWQT_ComfortHMI_20260922.xlsx`，476 TC）在撰寫過程中查得、
**須由上游澄清或修正**之項。每一項皆附其在本交付中之處置 —— 本層**沒有代為修改需求**，
TC 一律依現行條文與實際檔案落地。

依 canon §8.4.1（ambiguous source → preserve ambiguity）與本線之 R-C64，
「條文說不清楚」之處一律保留其模糊並載於 Remarks，不由測試層造值。

---

## 1. `2.1`（C1）之 tab 數與 Massage —— 037 與條文不一致

| | 內容 |
|---|---|
| **條文** | `2.1` 列出 **4 個 tab**（含 `Massage`） |
| **037 leaf** | 寫 **3 個 tab**，且**無 `Massage`** |
| **影響** | `SWE1-HVAC-001-01`／`001-02`（工作簿 4 列） |
| **本交付之處置** | **TC 依條文**（鏈：SR24 條文 → 037 → TC，條文為權威，R-C52）。四列之 Remarks 各載一句自足之 conflict 句，並登 `AMBIGUITY_REMARKS` |
| **請 RD 回覆** | 以哪一份為準？若 037 正確，條文之 `Massage` 應刪；若條文正確，037 之 leaf 應補 |

## 2. `2.13` / `SWE1-HVAC-019-03` —— VF HVAC 缺件

| | 內容 |
|---|---|
| **情形** | 該 leaf 之內容由**另一份文件**承載，本 spec 未給可測之行為 |
| **影響** | 工作簿 row 116（F `NR1L-ComfortHMI-466`） |
| **本交付之處置** | 依 R-C24／R-C51 產 `[BLOCKED-SPEC]` 佔列（L／M 留白），Remarks 首 60 字元內載 `Owner:`。**不產測試步驟** |
| **請 RD 回覆** | 該 leaf 之行為規格在哪一份文件、哪一節？補入後本列即可解封 |

## 3. `037` 之 VC 前提與實際車型不一致

| | 內容 |
|---|---|
| **037** | VC 前提寫 `Vehicle variant is DT or HDCC` |
| **Pei 裁定（2026-09-22）** | 本功能**只有 Alt-Mi 有** —— Promaster／Toro／Fastback |
| **實測旁證** | 三份 Atl-Hi PROXI（`HDCC27_initial`／`HDCC28_ATL_HI`／`DT28_ATL_HI`）之**七個氣候參數全為 `0=Absent`**，與「該功能於 Atl-Hi 不存在」一致，與 037 之 VC 前提相反 |
| **本交付之處置** | 車型欄 T（HDCC27 Atl-Hi）＝0、U（DT27 Atl-Hi）＝0；**TC 內容不因此改動**。登 `A-CMF12` |
| **請 RD 回覆** | 037 之 VC 前提是否應改為 Alt-Mi？ |

## 4. 上游有**三套命名**，而沒有任何一份對照表

這是本線反覆遇到的同一件事，合為一項提出。

| 層 | 名 | 實際檔案中之名 | 出處 |
|---|---|---|---|
| 需求（CFTS043 tree view）| `$RECIRC_STAT$` | `STATUS_CLIMATE2.HVACRecirc_Sts` | LID 對照表 `Atlantis` 欄 r1566 |
| 需求（CFTS043 tree view）| `$EBL_Stat$` | `STATUS_CLIMATE2.HVACRearDef_Sts`（Atlantis MID）| 同上 r587 |
| 需求（CFTS043 NEWR1L-53677）| `$Rear_HVAC_cfg$` | `Rear_Climate` | `forms/proxi/` 六份檔實測，**無 `Rear_HVAC_cfg`** |
| 條文（`2.14` 等）| `ATC`／`MTC`／`ICS` | `Climate_Type`／`Integrated_Climate_Touchscreen` | PROXI 參數；**條文從不展開這些縮寫** |

- **實測**：129 個被引用之節中，**每一個 PROXI 參數名皆 0 命中**；`ICS` 只出現 1 次（`2.14`）且未展開；
  `EMEA` 0 命中。PROXI 之 label（`Manual`／`Automatic`／`3 knobs`／`Trimode`）於條文中
  **不是 0 命中就是同形異義**（例：條文之 `the manual mode` 指氣流模式，非氣候系統型別）。
- `forms/FORMS.md` 對 LID 對照表早有同性質之記載：「LID 之左欄為 Logical Identifier，
  **不是 CAN 訊號名**。以 LID 名直接查 DBC 必然 0 命中」。
- **本交付之處置**：依 **R-C64**，作者側欄位（Pre-Condition／Input Test Data／Procedure／
  Expected Result）一律用**實際檔案之名與值**；`Test Item` 上半之條文逐字保留需求原名。
- **請 RD 提供**：一份「需求 `$…$` 名 ↔ CAN 訊號名 ↔ PROXI 參數名」之對照表。
  目前每一次對映都是測試層自行比對，**沒有任何一份文件背書**。

## 5. `§19`／`§20`／`§21` 未被 037 引用

| | 內容 |
|---|---|
| **情形** | SR24 Comfort HMI L&F 之第 19／20／21 章，037 之 HMI Source ID **未引用任何一節** |
| **本交付之處置** | 依 R-C1（037 所引者為基線），這三章**不在本交付範圍**，未產 TC |
| **請 RD 回覆** | 這三章是刻意不納入 R1L-R scope，還是 037 漏引？若為後者，需追加 leaf 與 TC |

## 6. EMEA ICS（chapter 16）之需求不在販售範圍 —— 建議 037 標註

| | 內容 |
|---|---|
| **Pei 裁定（2026-09-22）** | 「可以的話不寫 EMEA 也沒問題，因為**不含在販售的範圍內**」 |
| **涵蓋面** | 037 之 **99 個 leaf／119 條 TC** —— 其 PC 帶 `The vehicle is an EMEA ICS vehicle, whose climate interface is specified in chapter 16`（對應 SR24 之 chapter 16） |
| **本交付之處置** | **列保留、不刪**（R-C46：既有 `F`／`E` 不重編，119 個 TestRail ID 不作廢；且每個 leaf 仍有 TC 輸出）；**車型欄 V／Y／Z 三台全 0** —— 車型欄本身即為「本輪三台皆不執行」之資訊（R-C63，不加 Remarks）。`coverage.tsv` 之 `out_of_sales_scope` 欄標 `EMEA` |
| **請 RD 回覆／處理** | 037 是否應在這 99 個 leaf 上標註其市場範圍（EMEA-only）？目前 037 無任何市場欄位，**「不在販售範圍」這件事在需求側沒有痕跡** —— 下一個接手的人只會看到 119 條車型欄全 0 而不知其所以然，除非讀到本檔 |

> **另記**：chapter 16 與 chapter 2 之條文大量重疊（`16.2`↔`2.2`、`16.3`↔`2.3` 等）。
> 若 EMEA 確定不出貨，該重疊所產生之維護成本（兩份幾乎相同之條文同步修改）亦可一併檢討。

---

## 7. 其他已登記、不阻塞出貨之未決項

見 `features/comfort/docs/reports/dr_summary.tsv`：

- **DR-47**（`2.3` C2 之 `the manual mode that most closely matches the auto mode exited` 無值）
- **DR-48**（`2.4` C3 之 Recirc 自動開 A/C 是否顯示該變化 —— 037 leaf 寫 `(change not shown)`，
  而條文之 `(Do not show this change)` 只附於 Defrost 一句）
- **DR-49**（`Climate` 畫面之 HMI entry path —— `4.1` 命名表只列 `Comfort`，無 `Climate`／`HVAC`）

三者皆已於 TC 中以「保留條文模糊 ＋ Remarks 載其不可判之處」處置，**不阻塞本次出貨**；
DR-49 之回覆將決定導航步驟改寫（R-C66，另發 Revise）。
