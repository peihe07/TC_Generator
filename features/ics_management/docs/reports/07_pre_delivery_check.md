# 交付前體檢 v2 — b01 ~ b05 全 25 條（2026-08-29）

> 下放包 07 作業 G，依 **R-ICS28(b)**。**取代 `05_pre_delivery_check.md`**
> （舊報告與其產生器皆保留不刪，回溯用）。
> 未錨定斷言之判準、規則與例外表**全部寫在 `scripts/gen_pre_delivery_07.py` 檔頭與常數表**，
> 可逐行覆核 —— 這是人工判，不偽裝成機械輸出。

## §1 未錨定斷言檢查 —— 總計

- ER 行總數 **118**（25 條 TC）
- **已錨** 84／**已標明**（乙類，指回已登 A-）6／**非斷言**（記錄行）21／**未錨定** 7

## §2 【E6】未錨定斷言 —— 逐行具名（**未自行刪改該 ER 行**）

| 批 | tc_title | ER 行 | 內容 | 理由 |
|---|---|---|---|---|
| b02 | Press ignored during stuck condition | 5 | The HU state is the same as the baseline recorded in step 2 | 4819617 之來源句為 `the HU shall ignore the press request`。本行斷言「HU 狀態與基線相同」—— 同上之不作為問題；且來源句未載「忽略」之可觀察後果為何。 |
| b02 | Button responsive after release | 5 | The HU state changes from the baseline recorded in step 4 | 4819617 之後半為 `until a signal has been received that the button has been released`，只說「恢復處理」，**未載恢復後必產生可見變化**。本行斷言「HU 狀態改變」逾其所載。 |
| b04 | Knob 2 held stationary | 4 | The HU screen content is unchanged | 4819582 之來源句為 `the value ... shall be ignored by the receiving components and no action taken on the value` —— **「不做事」**。本行斷言「畫面內容不變」，是以一個**可觀察之無變化**承載一個**不可觀察之不作為**；來源句未承諾畫面必然不變。 |
| b04 | Knob 2 signals acted on by the HU | 4 | The HU state differs from the state recorded in step 1 | 4819586 之來源句自帶 **`if any`** —— 規格明示可能無對應畫面。本行斷言「HU 狀態與步驟 1 不同」，在 `if any` 為真（無對應）時即為 **False Fail**（IN §7）。 |
| b04 | Enter button pressed | 4 | The screen shown differs from the screen recorded in step 1 | 4819555 之來源句自帶 **`if any`**。本行斷言「畫面與步驟 1 不同」，在無對應畫面時為 False Fail。R-ICS30(b) 已裁「目標畫面未具名維持現狀」，但**該裁定治的是「不得自行指定畫面名」，未治本行之斷言逾越**。 |
| b05 | Knob 2 rotated on a scrollable screen | 4 | The screen content differs from the content recorded in step 1 | 同上之 `if any` 問題（4819586）。本行斷言「畫面內容不同」。 |
| b05 | Knob 2 rotated on a tuner source | 4 | The Entertainment Audio state differs from the state recorded in step  | 同上之 `if any` 問題（4819586）。本行斷言「Entertainment Audio 狀態不同」。 |

**共通形態**：七行分屬兩族 ——
(i) **不作為之可觀察化**（B3／I1／I2）：來源句說「忽略」「不做事」，TC 以「狀態不變／改變」承載；
(ii) **`if any` 之逾越**（B6／Scroll／Tune／N1）：來源句自帶 `if any`，即規格明示可能無對應後果，而 TC 斷言必有可觀察之差異 —— **此四行為潛在 FF**（IN §7）。

## §3 已標明者（乙類，指回已登之 A-）

| 批 | tc_title | ER 行 | 已登異常 |
|---|---|---|---|
| b01 | VOLUME knob rotated clock-wise | 1 | A-ICS16（popup 之顯示條件未載，已登異常） |
| b01 | VOLUME knob rotated clock-wise | 3 | A-ICS16（popup 之顯示條件未載，已登異常） |
| b01 | VOLUME knob rotated counter clock-wise | 1 | A-ICS16（popup 之顯示條件未載，已登異常） |
| b01 | VOLUME knob rotated counter clock-wise | 3 | A-ICS16（popup 之顯示條件未載，已登異常） |
| b01 | Three detents rotated clock-wise | 1 | A-ICS16（popup 之顯示條件未載，已登異常） |
| b01 | Three detents rotated clock-wise | 3 | A-ICS16（popup 之顯示條件未載，已登異常） |

## §4 Test Set／priority／trace 覆蓋

| Test Set | 條數 |
|---|---|
| Browse Control | 8 |
| Display Control | 8 |
| Menu Navigation | 1 |
| Stuck Button | 5 |
| Volume Control | 3 |

| priority | 條數 |
|---|---|
| P0 | 11 |
| P1 | 14 |

| RD | TC 數 |
|---|---|
| SWE-ICS-001 | 2 |
| SWE-ICS-002 | 1 |
| SWE-ICS-003 | 4 |
| SWE-ICS-004 | 4 |
| SWE-ICS-005 | **0** |
| SWE-ICS-006 | 4 |
| SWE-ICS-007 | 4 |
| SWE-ICS-008 | 1 |
| SWE-ICS-009 | **0** |
| SWE-ICS-010 | 5 |
| SWE-ICS-011 | **0** |
| SWE-ICS-012 | **0** |

## §5 佔位分佈（`pending_census.py` 之口徑；**區分缺值與待回填**，R-ICS27(d)）

| DR | 佔位處數 | 涉 TC 數 | 態 |
|---|---|---|---|
| DR-ICS4 | 1 | 1 | **缺值**（CFTS019 版本未確認） |
| DR-ICS6 | 4 | 4 | **缺值**（HMI L&F 畫面流未提供） |
| DR-ICS8 | 12 | 8 | **缺值**（`$TGW_DISP_STAT$`；b07 作業 C 判 E3，先決不成立） |
| **合計** | **17** | | |

**b07 後已無「待回填」態之佔位** —— DR-ICS10／DR-ICS12 之 6 處已於作業 B 回填。

