# 上繳包 04 —— R-SU8／R-SU9 抄錄、Phase 3 前置量測（T18a–e）

- 日期：2026-08-27
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/05_framework_survey.md`
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**｜PENDING 裁決：**0 項**
- 量測腳本：`features/sw_update/scripts/framework_survey.py`（可重跑，含閉合檢查）
- **三項閉合檢查全部通過**（T18a 311／T18b 120／T18c 87 + 487）

---

## 一、T-抄 核對結果

核對法同前：程式自下放包抽 ``` 圍籬區塊，寫入後回讀該檔逐字元比對。

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU8 | 333 | **OK** | `d4bf0589a63a` |
| R-SU9 | 340 | **OK** | `893d85dab1d4` |

**既有 9 個條文區塊未受索引表插入影響**：R-SU1～R-SU7 v2 之
sha256[:12] 逐一回讀比對，與上繳包 01／02／03 所記**全部相同** ✅
（`78248cd16f79`／`f2d1b7663a1a`／`d01d11cb4f19`／`0fa953653415`／
`94791d3d5e0b`／`037742490af2`／`d99834f40411`／`c957b2d21f24`／`419eb8aadd08`）。

`RULINGS.md` 條文區塊序（11 個）：
`R-SU1` → `R-SU2` → `R-SU3` → `R-SU4 v2` → `R-SU5` → `R-SU5 v2`
→ `R-SU6 v2` → `R-SU7` → `R-SU7 v2` → `R-SU8` → `R-SU9`

### 索引表全文（依 R-SU8(b) 新建於 `RULINGS.md` 檔首）

> 判準（R-SU8(a)）：同一條號有多版本時，**v 字尾最大者為現行**；無 v 字尾者視為 v1。
> 被取代之版本僅供沿革查考，其所載之數值、形態陳述、拘束**一律不得引用**。
> 本表與條文區塊不一致時，**以條文區塊為準**，並即修本表。

| 條號 | 現行版 | 主旨 | 來源下放包 |
|---|---|---|---|
| R-SU1 | v1 | feature 身分與 test_group（`SW Update`／`sw_update`；前綴 R-SU／A-SU／DR-SU） | 01 §二 |
| R-SU2 | v1 | 036 母本與 workbook_state = BLANK；寫回採 XML 外科式修改 | 01 §二 |
| R-SU3 | v1 | 驗證母體 311 = FR 307 + NFR 4；範圍以 037 實際納入為準 | 01 §二 |
| R-SU4 | **v2** | spec_reference 雙家族錨點（CFTS057-{ObjectID}／SYS1 章節 token）+ 錨點池範圍 (a2) | 02 §二 |
| R-SU5 | **v2** | 037 Source Requirement ID 欄之三形態；該欄不取為 spec_reference | 03 §2.1 |
| R-SU6 | **v2** | HMI 規格本文為真 PDF，全文字層；一律機器抽取，p.{n} 為覆核義務 | 02 §二 |
| R-SU7 | **v2** | Description 物件不入池；錨點池 574 = 章節 87 + 需求 487，Description 137 | 04 §1.2 |
| R-SU8 | v1 | 本表之判準：v 字尾最大者為現行；檔首須維持索引表 | 05 §二 |
| R-SU9 | v1 | recon 產物之重生條件（未簽佔位得刪檔重生並揭露；已簽或含人手內容不得刪） | 05 §二 |

**留存之被取代條文（依 R-TM13 不刪不改，不得引用）**：

| 條號版本 | 已被取代於 | 其所載之失效值 |
|---|---|---|
| `R-SU5`（v1） | R-SU5 v2 | 「欄形態為 `SYS-RA-FOTA-{n}`」單一形態陳述；非空 373／unique 364 |
| `R-SU7`（v1） | R-SU7 v2 | 池 565、需求 478、Description 135 |

---

## 二、T18a–e 量測結果

以下為 `python3 scripts/framework_survey.py` 之原始輸出（去 openpyxl warning）。

## T18a —— 037 分群（Heading 為分節點）

| # | Heading id | 標題原文 | FR | NFR | 小計 | 所轄 id 範圍 |
|---:|---|---|---:|---:|---:|---|
| 0 | — | (前言 —— 首個 Heading 之前) | 0 | 0 | 0 | — |
| 1 | `SWE1-FOTA-001` | Firmware Over-the-air Updates (FOTA) | 6 | 0 | 6 | 3–8 |
| 2 | `SWE1-FOTA-009` | Critical Updates | 6 | 0 | 6 | 10–15 |
| 3 | `SWE1-FOTA-016` | Session Flows | 0 | 0 | 0 | — |
| 4 | `SWE1-FOTA-017` | Deployment Flow | 0 | 0 | 0 | — |
| 5 | `SWE1-FOTA-018` | Installation and Download Conditions | 1 | 0 | 1 | 19 |
| 6 | `SWE1-FOTA-020` | Re-Flashing Requirements | 0 | 0 | 0 | — |
| 7 | `SWE1-FOTA-022` | Communication Security | 0 | 0 | 0 | — |
| 8 | `SWE1-FOTA-024` | Critical Updates | 11 | 0 | 11 | 25–37 |
| 9 | `SWE1-FOTA-038` | OTA download via Wi-Fi | 15 | 0 | 15 | 39–54 |
| 10 | `SWE1-FOTA-055` | Non-Critical Updates | 2 | 0 | 2 | 56–57 |
| 11 | `SWE1-FOTA-058` | Connection to Wi-Fi network | 12 | 0 | 12 | 59–71 |
| 12 | `SWE1-FOTA-072` | OTA Client Architecture | 0 | 0 | 0 | — |
| 13 | `SWE1-FOTA-073` | Operating Environment | 0 | 0 | 0 | — |
| 14 | `SWE1-FOTA-074` | Over The Air (OTA) Deployment of Software | 0 | 0 | 0 | — |
| 15 | `SWE1-FOTA-076` | Local Deployment of Software | 0 | 0 | 0 | — |
| 16 | `SWE1-FOTA-078` | Media Reflash Requirements | 5 | 0 | 5 | 80–84 |
| 17 | `SWE1-FOTA-085` | FOTA ROV Reflash Requirements | 0 | 0 | 0 | — |
| 18 | `SWE1-FOTA-086` | Post-Installation | 3 | 0 | 3 | 88–90 |
| 19 | `SWE1-FOTA-091` | Installation Progress | 4 | 0 | 4 | 92–95 |
| 20 | `SWE1-FOTA-096` | Pre-Installation | 13 | 0 | 13 | 97–109 |
| 21 | `SWE1-FOTA-110` | TBM FOTA Reflash | 14 | 0 | 14 | 111–124 |
| 22 | `SWE1-FOTA-125` | Appendix B Configurable Parameters | 1 | 0 | 1 | 126 |
| 23 | `SWE1-FOTA-127` | Download Descriptor Format | 1 | 0 | 1 | 128 |
| 24 | `SWE1-FOTA-129` | User Experience (UX)/HMI | 6 | 0 | 6 | 130–136 |
| 25 | `SWE1-FOTA-137` | Deployment flow | 26 | 0 | 26 | 138–167 |
| 26 | `SWE1-FOTA-168` | Vehicle-Initiated Session Flow | 1 | 0 | 1 | 169 |
| 27 | `SWE1-FOTA-170` | Deployment Package Security | 7 | 0 | 7 | 171–177 |
| 28 | `SWE1-FOTA-178` | For a silent update, the OTA client follows these steps  | 6 | 0 | 6 | 179–184 |
| 29 | `SWE1-FOTA-185` | OTA client sessions | 1 | 0 | 1 | 187 |
| 30 | `SWE1-FOTA-188` | User initiated sessions | 3 | 0 | 3 | 189–191 |
| 31 | `SWE1-FOTA-192` | Bus communications | 3 | 0 | 3 | 195–199 |
| 32 | `SWE1-FOTA-200` | OTA Client Configuration options | 1 | 0 | 1 | 201 |
| 33 | `SWE1-FOTA-202` | OTA Architecture Requirements | 10 | 0 | 10 | 203–213 |
| 34 | `SWE1-FOTA-214` | HU FOTA with TBM | 36 | 0 | 36 | 215–250 |
| 35 | `SWE1-FOTA-251` | High Level FOTA Diagram | 7 | 0 | 7 | 252–258 |
| 36 | `SWE1-FOTA-259` | Vehicle Properties | 3 | 0 | 3 | 260–262 |
| 37 | `SWE1-FOTA-263` | OTA Architecture Requirements | 2 | 0 | 2 | 264–265 |
| 38 | `SWE1-FOTA-266` | OTA Client Configuration options | 4 | 0 | 4 | 267–270 |
| 39 | `SWE1-FOTA-271` | OTA server initiated sessions | 6 | 0 | 6 | 272–277 |
| 40 | `SWE1-FOTA-278` | User initiated sessions | 1 | 0 | 1 | 279 |
| 41 | `SWE1-FOTA-280` | Interface Definitions | 0 | 4 | 4 | 281–284 |
| 42 | `SWE1-FOTA-285` | OTA Client Performance Requirements | 1 | 0 | 1 | 286 |
| 43 | `SWE1-FOTA-287` | OTA client Flows | 3 | 0 | 3 | 288–290 |
| 44 | `SWE1-FOTA-291` | Bearer selection: | 16 | 0 | 16 | 292–308 |
| 45 | `SWE1-FOTA-309` | OMA-DM Security | 70 | 0 | 70 | 310–383 |

**閉合檢查**：所轄列數總和 = **311**；驗證母體（R-SU3）= **311** —— 閉合 ✅

Heading 節數 = 45（另 1 個前言偽節，所轄 0 列）

## T18b —— SYS1 分群（28 頂層章）

| Outline | Description 首句 | 2 層 | 3 層 | 子節 Outline 清單 |
|---|---|---:|---:|---|
| **1** | FEATURE HMI SCOPE | 8 | 0 | `1.1`, `1.2`, `1.3`, `1.4`, `1.5`, `1.6`, `1.7`, `1.8` |
| **2** | HIGH LEVEL DISPLAY HMI SCOPE | 1 | 0 | `2.1` |
| **3** | FEATURE SCOPE ASSUMPTION | 4 | 0 | `3.1`, `3.2`, `3.3`, `3.4` |
| **4** | POP UP REQUIREMENTS | 1 | 0 | `4.1` |
| **5** | HEAD UNIT REQUIREMENTS | 8 | 0 | `5.1`, `5.2`, `5.3`, `5.4`, `5.5`, `5.6`, `5.7`, `5.8` |
| **6** | HEAD UNIT WIREFRAMES: General Requirements | 6 | 1 | `6.1`, `6.2`, `6.3`, `6.3.1`, `6.4`, `6.5`, `6.6` |
| **7** | LOGIC & FLOW: HU USB Software Update (SUP) | 6 | 0 | `7.1`, `7.2`, `7.3`, `7.4`, `7.5`, `7.6` |
| **8** | LOGIC & FLOW: HU USB Error Popup | 1 | 0 | `8.1` |
| **9** | LOGIC & FLOW: HU FOTA Update Now | 5 | 0 | `9.1`, `9.2`, `9.3`, `9.4`, `9.5` |
| **10** | LOGIC & FLOW: HU Forced FOTA Update Now | 2 | 0 | `10.1`, `10.2` |
| **11** | LOGIC & FLOW: HU Schedule Update | 1 | 0 | `11.1` |
| **12** | LOGIC & FLOW(HU): Forced FOTA Schedule Update | 1 | 0 | `12.1` |
| **13** | LOGIC & FLOW: HU FOTA Error Popups | 2 | 0 | `13.1`, `13.2` |
| **14** | LOGIC & FLOW: HU FOTA Download via Wi-Fi | 14 | 0 | `14.1`, `14.2`, `14.3`, `14.4`, `14.5`, `14.6`, `14.7`, `14.8`, `14.9`, `14.10`, `14.11`, `14.12`, `14.13`, `1 |
| **15** | LOGIC & FLOW: HU Silent Install Indication (Does not | 2 | 0 | `15.1`, `15.2` |
| **16** | LOGIC & FLOW: FOTA ROV Update | 4 | 0 | `16.1`, `16.2`, `16.3`, `16.4` |
| **17** | LOGIC & FLOW: FOTA ROV Schedule Update | 1 | 1 | `17.1`, `17.1.1` |
| **18** | LOGIC & FLOW: FOTA ROV Error Popups | 2 | 0 | `18.1`, `18.2` |
| **19** | LOGIC & FLOW: FOTA ROV Schedule Update | 1 | 1 | `19.1`, `19.1.1` |
| **20** | LOGIC & FLOW: TBM FOTA | 1 | 0 | `20.1` |
| **21** | LOGIC & FLOW: TBM General Requirements | 3 | 0 | `21.1`, `21.2`, `21.3` |
| **22** | LOGIC & FLOW: TBM FOTA –with notification and Radio  | 3 | 0 | `22.1`, `22.2`, `22.3` |
| **23** | LOGIC & FLOW: TBM FOTA –with notification and radio  | 2 | 0 | `23.1`, `23.2` |
| **24** | LOGIC & FLOW: TBM FOTA Ongoing Update -radio Power O | 2 | 0 | `24.1`, `24.2` |
| **25** | LOGIC & FLOW: TBM FOTA Update finished -radio Power  | 2 | 0 | `25.1`, `25.2` |
| **26** | LOGIC & FLOW: TBM FOTA Ongoing Update –radio Power O | 1 | 0 | `26.1` |
| **27** | LOGIC & FLOW: TBM FOTA Update Error -radio Power OFF | 1 | 0 | `27.1` |
| **28** | LOGIC & FLOW: TBM FOTA –silent update | 4 | 0 | `28.1`, `28.2`, `28.3`, `28.4` |

**閉合檢查**：頂層 28 + 子節 92 = 120；`Basic Report` 資料列 = 120 —— 閉合 ✅

## T18c —— CFTS_57 章節（87 章節物件）

| 章節號 | ObjectID | 標題原文 | 所轄需求物件 |
|---|---|---|---:|
| 1 | `4907230` | Reflash [CFTSMV057_CIP_R1] | 0 |
| 1.1 | `4907231` | Revision Notes | 0 |
| 1.2 | `4907233` | Introduction | 0 |
| 2 | `4907241` | Common Reflash Requirements | 16 |
| 3 | `4907259` | Media Reflash Requirements | 0 |
| 4 | `4907261` | FOTA Reflash Requirements | 0 |
| 4.1 | `4907267` | This Document | 0 |
| 4.1.1 | `4907269` | Related Documents and Specifications | 0 |
| 4.2 | `4907272` | Use Cases for OTA client | 0 |
| 4.2.1 | `4907273` | Over The Air (OTA) Deployment of Software | 0 |
| 4.2.2 | `4907275` | Local Deployment of Software | 0 |
| 4.2.3 | `4907277` | HU FOTA with TBM | 4 |
| 4.2.4 | `4907282` | Software Configuration Reporting | 0 |
| 4.3 | `4907284` | High Level FOTA Diagram | 0 |
| 4.4 | `4907287` | OTA Client Architecture | 22 |
| 4.4.1 | `4907313` | OTA Architecture Requirements | 19 |
| 4.4.2 | `4907337` | OTA Client Configuration options | 6 |
| 4.4.3 | `4907344` | Operating Environment | 8 |
| 4.5 | `4907353` | Interface Definitions | 0 |
| 4.5.1 | `4907354` | OTA Communication Protocols | 1 |
| 4.5.2 | `4907358` | User initiated sessions | 3 |
| 4.5.3 | `4907362` | Vehicle initiated sessions | 5 |
| 4.5.4 | `4907369` | OTA server initiated sessions | 1 |
| 4.5.4.1 | `4907371` | SMS/MQTT Push Support | 10 |
| 4.5.5 | `4907382` | Bus communications | 8 |
| 4.6 | `4907395` | OTA download via Wi-Fi | 5 |
| 4.6.1 | `4907401` | Connection to Wi-Fi network | 11 |
| 4.6.2 | `4907413` | Non-Critical Updates | 2 |
| 4.6.3 | `4907416` | Software Download via Wi-Fi | 17 |
| 4.7 | `4907434` | OTA Client Application | 1 |
| 4.7.1 | `4907436` | OTA Client Performance Requirements | 4 |
| 4.7.2 | `4907441` | OTA client Flows | 4 |
| 4.7.3 | `4907448` | Main Update Configuration Options | 16 |
| 4.7.3.1 | `4907465` | Critical Updates | 8 |
| 4.7.3.2 | `4907474` | Silent Updates | 13 |
| 4.7.3.3 | `4907488` | Regular Updates | 1 |
| 4.8 | `4907490` | Security | 7 |
| 4.8.1 | `4907498` | Communication Security | 8 |
| 4.8.2 | `4907507` | OMA-DM Security | 3 |
| 4.8.3 | `4907512` | Deployment Package Security | 9 |
| 4.9 | `4907522` | Re-Flashing Requirements | 0 |
| 4.9.1 | `4907523` | Update Agent Requirements | 16 |
| 4.9.2 | `4907542` | ECU Module specific considerations | 0 |
| 4.10 | `4907551` | Session Flows | 3 |
| 4.10.1 | `4907555` | Self Registration Flow | 8 |
| 4.10.2 | `4907564` | Server-Initiated Session Flow | 13 |
| 4.10.3 | `4907578` | Vehicle-Initiated Session Flow | 14 |
| 4.10.4 | `4907593` | User-Initiated Session Flow | 4 |
| 4.10.5 | `4907598` | Deployment Flow | 9 |
| 4.10.5.1 | `4907608` | Installation and Download Conditions | 41 |
| 4.11 | `4907651` | User Experience (UX)/HMI | 12 |
| 4.12 | `4907664` | Interrupt Handling | 11 |
| 4.12.1 | `4907678` | Resuming a Download | 6 |
| 4.12.2 | `4907685` | Report Persistency | 6 |
| 4.13 | `4907692` | OMA-DM Management Object Support | 0 |
| 4.13.1 | `4907693` | SCOMO Support | 8 |
| 4.13.2 | `4907711` | LAWMO Support | 0 |
| 4.13.2.1 | `4907721` | Lock | 0 |
| 4.13.2.2 | `4907730` | Unlock | 0 |
| 4.13.2.3 | `4907734` | Wipe Data | 0 |
| 4.13.3 | `4907738` | Additional Support Objects | 0 |
| 4.13.4 | `4907741` | FCA Specific Tree structure (DDF) | 1 |
| 4.13.4.1 | `4907743` | Appendix A Download Descriptor Format | 1 |
| 4.13.4.2 | `4907764` | Appendix B Configurable Parameters | 1 |
| 4.13.4.3 | `4907768` | Appendix C OTA Commands | 1 |
| 4.13.4.4 | `4907772` | Appendix D Terms and Abbreviations | 0 |
| 5 | `4907775` | TBM FOTA Reflash Requirements | 22 |
| 6 | `4907798` | TBM Algorithm Requirements | 14 |
| 7 | `4907815` | Firmware Over-the-air Updates (FOTA) | 8 |
| 7.1 | `4907824` | Critical Updates | 8 |
| 8 | `4907833` | Maps Over-the-air Updates (MOTA) | 3 |
| 8.1 | `4907840` | Non-Critical Updates | 22 |
| 8.2 | `4907863` | Route Planning Updates | 2 |
| 8.3 | `4907866` | User Initiated Updates | 4 |
| 8.4 | `4907871` | MOTA Client Initiated Updates | 6 |
| 9 | `4907878` | FOTA ROV Reflash Requirements | 0 |
| 9.1 | `4907879` | Pre-Installation | 16 |
| 9.2 | `4907897` | Installation Progress | 7 |
| 9.3 | `4907905` | Post-Installation | 5 |
| 9.4 | `4907911` | TBM FOTA Rest of Vehicle Requirements | 0 |
| 9.4.1 | `4907912` | Pre-Installation | 3 |
| 10 | `4907916` | Wi-Fi Only Yard Hold Reflash | 0 |
| 10.1 | `4907917` | Shipping/Logistic mode | 0 |
| 10.2 | `4907919` | Wi-Fi | 0 |
| 10.3 | `4907930` | Installation | 0 |
| 10.4 | `4907935` | Post-Installation | 0 |
| 10.5 | `4907938` | Security (Hopefully remove and reference to Rejani/Ansaf s | 0 |

**閉合檢查**：章節 87（應 87）；所轄需求物件總和 = **487**（應 487） —— 閉合 ✅

## T18e —— Heading × Sub Categorization 交叉表

| Heading id | 標題原文 | Service | HMI | blank | 小計 |
|---|---|---:|---:|---:|---:|
| `SWE1-FOTA-001` | Firmware Over-the-air Updates (FOTA) | 4 | 2 | 0 | 6 |
| `SWE1-FOTA-009` | Critical Updates | 5 | 1 | 0 | 6 |
| `SWE1-FOTA-018` | Installation and Download Conditions | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-024` | Critical Updates | 8 | 3 | 0 | 11 |
| `SWE1-FOTA-038` | OTA download via Wi-Fi | 5 | 10 | 0 | 15 |
| `SWE1-FOTA-055` | Non-Critical Updates | 1 | 1 | 0 | 2 |
| `SWE1-FOTA-058` | Connection to Wi-Fi network | 11 | 1 | 0 | 12 |
| `SWE1-FOTA-078` | Media Reflash Requirements | 5 | 0 | 0 | 5 |
| `SWE1-FOTA-086` | Post-Installation | 1 | 2 | 0 | 3 |
| `SWE1-FOTA-091` | Installation Progress | 0 | 4 | 0 | 4 |
| `SWE1-FOTA-096` | Pre-Installation | 3 | 10 | 0 | 13 |
| `SWE1-FOTA-110` | TBM FOTA Reflash | 3 | 11 | 0 | 14 |
| `SWE1-FOTA-125` | Appendix B Configurable Parameters | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-127` | Download Descriptor Format | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-129` | User Experience (UX)/HMI | 1 | 5 | 0 | 6 |
| `SWE1-FOTA-137` | Deployment flow | 17 | 9 | 0 | 26 |
| `SWE1-FOTA-168` | Vehicle-Initiated Session Flow | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-170` | Deployment Package Security | 6 | 1 | 0 | 7 |
| `SWE1-FOTA-178` | For a silent update, the OTA client follows these  | 5 | 1 | 0 | 6 |
| `SWE1-FOTA-185` | OTA client sessions | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-188` | User initiated sessions | 1 | 2 | 0 | 3 |
| `SWE1-FOTA-192` | Bus communications | 3 | 0 | 0 | 3 |
| `SWE1-FOTA-200` | OTA Client Configuration options | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-202` | OTA Architecture Requirements | 6 | 4 | 0 | 10 |
| `SWE1-FOTA-214` | HU FOTA with TBM | 16 | 20 | 0 | 36 |
| `SWE1-FOTA-251` | High Level FOTA Diagram | 7 | 0 | 0 | 7 |
| `SWE1-FOTA-259` | Vehicle Properties | 2 | 0 | 1 | 3 |
| `SWE1-FOTA-263` | OTA Architecture Requirements | 2 | 0 | 0 | 2 |
| `SWE1-FOTA-266` | OTA Client Configuration options | 4 | 0 | 0 | 4 |
| `SWE1-FOTA-271` | OTA server initiated sessions | 6 | 0 | 0 | 6 |
| `SWE1-FOTA-278` | User initiated sessions | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-280` | Interface Definitions | 4 | 0 | 0 | 4 |
| `SWE1-FOTA-285` | OTA Client Performance Requirements | 1 | 0 | 0 | 1 |
| `SWE1-FOTA-287` | OTA client Flows | 3 | 0 | 0 | 3 |
| `SWE1-FOTA-291` | Bearer selection: | 16 | 0 | 0 | 16 |
| `SWE1-FOTA-309` | OMA-DM Security | 70 | 0 | 0 | 70 |

**合計**：Service 223、HMI 87、blank 1 —— 總和 311

**HMI 列集中處**（17 個 Heading 承載全部 87 個 HMI 列）：

1. `SWE1-FOTA-214` HU FOTA with TBM —— **20** 列
2. `SWE1-FOTA-110` TBM FOTA Reflash —— **11** 列
3. `SWE1-FOTA-038` OTA download via Wi-Fi —— **10** 列
4. `SWE1-FOTA-096` Pre-Installation —— **10** 列
5. `SWE1-FOTA-137` Deployment flow —— **9** 列
6. `SWE1-FOTA-129` User Experience (UX)/HMI —— **5** 列
7. `SWE1-FOTA-091` Installation Progress —— **4** 列
8. `SWE1-FOTA-202` OTA Architecture Requirements —— **4** 列
9. `SWE1-FOTA-024` Critical Updates —— **3** 列
10. `SWE1-FOTA-001` Firmware Over-the-air Updates (FOTA) —— **2** 列
11. `SWE1-FOTA-086` Post-Installation —— **2** 列
12. `SWE1-FOTA-188` User initiated sessions —— **2** 列
13. `SWE1-FOTA-009` Critical Updates —— **1** 列
14. `SWE1-FOTA-055` Non-Critical Updates —— **1** 列
15. `SWE1-FOTA-058` Connection to Wi-Fi network —— **1** 列
16. `SWE1-FOTA-170` Deployment Package Security —— **1** 列
17. `SWE1-FOTA-178` For a silent update, the OTA client follows these st —— **1** 列

## T18d —— 三源對照草表（草料，非結論）

| Heading id | 037 標題 | SYS1 候選 | 分 | CFTS 候選 | 分 |
|---|---|---|---:|---|---:|
| `SWE1-FOTA-001` | Firmware Over-the-air Updates (FOTA) | **?** | 0.12 | 7 Firmware Over-the-air Updates  | 1.00 |
| `SWE1-FOTA-009` | Critical Updates | **?** | 0.00 | 4.7.3.1 Critical Updates | 1.00 |
| `SWE1-FOTA-016` | Session Flows | **?** | 0.00 | 4.10 Session Flows | 1.00 |
| `SWE1-FOTA-017` | Deployment Flow | **?** | 0.20 | 4.10.5 Deployment Flow | 1.00 |
| `SWE1-FOTA-018` | Installation and Download Conditions | **?** | 0.14 | 4.10.5.1 Installation and Download Cond | 1.00 |
| `SWE1-FOTA-020` | Re-Flashing Requirements | **?** | 0.00 | 4.9 Re-Flashing Requirements | 1.00 |
| `SWE1-FOTA-022` | Communication Security | **?** | 0.00 | 4.8.1 Communication Security | 1.00 |
| `SWE1-FOTA-024` | Critical Updates | **?** | 0.00 | 4.7.3.1 Critical Updates | 1.00 |
| `SWE1-FOTA-038` | OTA download via Wi-Fi | **?** | 0.33 | 4.6 OTA download via Wi-Fi | 1.00 |
| `SWE1-FOTA-055` | Non-Critical Updates | **?** | 0.00 | 4.6.2 Non-Critical Updates | 1.00 |
| `SWE1-FOTA-058` | Connection to Wi-Fi network | **?** | 0.00 | 4.6.1 Connection to Wi-Fi network | 1.00 |
| `SWE1-FOTA-072` | OTA Client Architecture | **?** | 0.00 | 4.4 OTA Client Architecture | 1.00 |
| `SWE1-FOTA-073` | Operating Environment | **?** | 0.00 | 4.4.3 Operating Environment | 1.00 |
| `SWE1-FOTA-074` | Over The Air (OTA) Deployment of Softwar | **?** | 0.10 | 4.2.1 Over The Air (OTA) Deployment  | 1.00 |
| `SWE1-FOTA-076` | Local Deployment of Software | **?** | 0.12 | 4.2.2 Local Deployment of Software | 1.00 |
| `SWE1-FOTA-078` | Media Reflash Requirements | **?** | 0.00 | 3 Media Reflash Requirements | 1.00 |
| `SWE1-FOTA-085` | FOTA ROV Reflash Requirements | **?** | 0.33 | 9 FOTA ROV Reflash Requirements | 1.00 |
| `SWE1-FOTA-086` | Post-Installation | **?** | 0.00 | 9.3 Post-Installation | 1.00 |
| `SWE1-FOTA-091` | Installation Progress | **?** | 0.00 | 9.2 Installation Progress | 1.00 |
| `SWE1-FOTA-096` | Pre-Installation | **?** | 0.00 | 9.1 Pre-Installation | 1.00 |
| `SWE1-FOTA-110` | TBM FOTA Reflash | `20` LOGIC & FLOW: TBM FOTA | 0.40 | 5 TBM FOTA Reflash Requirements | 1.00 |
| `SWE1-FOTA-125` | Appendix B Configurable Parameters | **?** | 0.00 | 4.13.4.2 Appendix B Configurable Parame | 1.00 |
| `SWE1-FOTA-127` | Download Descriptor Format | **?** | 0.14 | 4.13.4.1 Appendix A Download Descriptor | 0.75 |
| `SWE1-FOTA-129` | User Experience (UX)/HMI | **?** | 0.20 | 4.11 User Experience (UX)/HMI | 1.00 |
| `SWE1-FOTA-137` | Deployment flow | **?** | 0.20 | 4.10.5 Deployment Flow | 1.00 |
| `SWE1-FOTA-168` | Vehicle-Initiated Session Flow | **?** | 0.14 | 4.10.3 Vehicle-Initiated Session Flow | 1.00 |
| `SWE1-FOTA-170` | Deployment Package Security | **?** | 0.00 | 4.8.3 Deployment Package Security | 1.00 |
| `SWE1-FOTA-178` | For a silent update, the OTA client foll | **?** | 0.17 | **?** | 0.22 |
| `SWE1-FOTA-185` | OTA client sessions | **?** | 0.00 | 4.4 OTA Client Architecture | 0.50 |
| `SWE1-FOTA-188` | User initiated sessions | **?** | 0.00 | 4.5.2 User initiated sessions | 1.00 |
| `SWE1-FOTA-192` | Bus communications | **?** | 0.00 | 4.5.5 Bus communications | 1.00 |
| `SWE1-FOTA-200` | OTA Client Configuration options | **?** | 0.00 | 4.4.2 OTA Client Configuration optio | 1.00 |
| `SWE1-FOTA-202` | OTA Architecture Requirements | **?** | 0.00 | 4.4.1 OTA Architecture Requirements | 1.00 |
| `SWE1-FOTA-214` | HU FOTA with TBM | `20` LOGIC & FLOW: TBM FOTA | 0.50 | 4.2.3 HU FOTA with TBM | 1.00 |
| `SWE1-FOTA-251` | High Level FOTA Diagram | **?** | 0.29 | 4.3 High Level FOTA Diagram | 1.00 |
| `SWE1-FOTA-259` | Vehicle Properties | **?** | 0.00 | **?** | 0.25 |
| `SWE1-FOTA-263` | OTA Architecture Requirements | **?** | 0.00 | 4.4.1 OTA Architecture Requirements | 1.00 |
| `SWE1-FOTA-266` | OTA Client Configuration options | **?** | 0.00 | 4.4.2 OTA Client Configuration optio | 1.00 |
| `SWE1-FOTA-271` | OTA server initiated sessions | **?** | 0.00 | 4.5.4 OTA server initiated sessions | 1.00 |
| `SWE1-FOTA-278` | User initiated sessions | **?** | 0.00 | 4.5.2 User initiated sessions | 1.00 |
| `SWE1-FOTA-280` | Interface Definitions | **?** | 0.00 | 4.5 Interface Definitions | 1.00 |
| `SWE1-FOTA-285` | OTA Client Performance Requirements | **?** | 0.00 | 4.7.1 OTA Client Performance Require | 1.00 |
| `SWE1-FOTA-287` | OTA client Flows | **?** | 0.00 | 4.7.2 OTA client Flows | 1.00 |
| `SWE1-FOTA-291` | Bearer selection: | **?** | 0.00 | **?** | 0.00 |
| `SWE1-FOTA-309` | OMA-DM Security | **?** | 0.00 | 4.8.2 OMA-DM Security | 1.00 |

**對應率**：SYS1 2/45、CFTS 42/45；其餘標 `?` 不強配。

> 本表為**草料**。分數為詞集重疊比（Jaccard，去停用詞、門檻 0.34），
> **不是語意判定**；`?` 只表示自動比對不達門檻，不表示無對應。
> Test Set 名稱與 Layer 2 分群由分析層起草，執行層不逕定（下放包 05 §三 T18d）。

---

## 三、量測所見之三項結構事實（記錄，非結論）

### 3.1 037 之 Heading 標題**重複**，不可逕作 Test Set 名

45 個 Heading 之標題僅 **41 個 unique** —— **4 組共 8 個** Heading 標題逐字相同
而轄不同區間（實測，非抽樣）：

| 標題 | Heading id | 所轄 |
|---|---|---|
| `Critical Updates` | `SWE1-FOTA-009` / `SWE1-FOTA-024` | 14 列 / 13 列 |
| `OTA Architecture Requirements` | `SWE1-FOTA-202` / `SWE1-FOTA-263` | 10 列 / 2 列 |
| `OTA Client Configuration options` | `SWE1-FOTA-200` / `SWE1-FOTA-266` | 1 列 / 4 列 |
| `User initiated sessions` | `SWE1-FOTA-188` / `SWE1-FOTA-278` | 3 列 / 1 列 |

即 037 之 Heading 為**文件章節標題**，非唯一鍵。Layer 2 若以標題為
Test Set 名將產生碰撞；分群鍵須為 Heading id 或「標題 + 序」。
**執行層不逕定**，記錄供起草。

### 3.2 037 章節結構與 CFTS_57 高度對應，與 SYS1 幾乎不對應

T18d 之自動比對（詞集重疊比，門檻 0.34）：

| 對照源 | 命中 | 對應率 |
|---|---|---|
| **CFTS_57 章節** | **42 / 45** | **93%** |
| SYS1 章 | 2 / 45 | 4% |

CFTS 未命中之 3 筆：`SWE1-FOTA-178`（`For a silent update, the OTA client
follows these steps` —— 句子而非標題）、`SWE1-FOTA-259`（`Vehicle Properties`）、
`SWE1-FOTA-291`（`Bearer selection:`）。

SYS1 命中之 2 筆皆對到同一章 `20 LOGIC & FLOW: TBM FOTA`
（`SWE1-FOTA-110` 0.40、`SWE1-FOTA-214` 0.50）。

**結構解讀**：037 之章節骨架承自 **CFTS_57**（其上游母件），
而非 SYS1 HMI 規格。SYS1 之 28 章為 HMI 畫面／流程視角
（`LOGIC & FLOW: …`、`POP UP REQUIREMENTS` 等），與 037 之
需求功能視角是**兩種切法**，非同一骨架之兩份副本。

**對 Layer 2 起草之影響**（供分析層判斷，執行層不裁）：
以 037 Heading 為主鍵時，CFTS 側可逐章對應，SYS1 側則須改以
**Sub Categorization == HMI 之 87 列**為橋接（見 3.3），
而非以章標題對章標題。

### 3.3 HMI 列高度集中：17 / 45 個 Heading 承載全部 87 列

前 5 個 Heading 即承載 60 / 87 列（69%）：

| Heading | 標題 | HMI 列 |
|---|---|---:|
| `SWE1-FOTA-214` | HU FOTA with TBM | **20** |
| `SWE1-FOTA-110` | TBM FOTA Reflash | **11** |
| `SWE1-FOTA-038` | OTA download via Wi-Fi | **10** |
| `SWE1-FOTA-096` | Pre-Installation | **10** |
| `SWE1-FOTA-137` | Deployment flow | **9** |

其餘 28 個 Heading（轄 224 列）**完全無 HMI 列** —— 即
IN §4.1.3 之「UI 入口路徑一致性」只在這 17 群內成立；
另 28 群為 Service 層行為，其 Layer 2 之入口敘述須另有體例。
**執行層不逕定，記錄供起草。**

### 3.4 Sub Categorization 於驗證母體內之分布

| 值 | 列數 |
|---|---:|
| Service | 223 |
| HMI | 87 |
| blank | **1** |
| **合計** | **311** ✅ |

全 383 列中 Sub Cat 空白 73 列，其中 **72 列為 Heading/Information 等
非母體列**，落在驗證母體內者僅 **1 列**。該列須於 Phase 3/4 個案處理
（Layer 2 歸屬無 Sub Cat 可依）。與上繳包 01 §三 3.7 之
「Priority 空白 72 ∩ SubCat 空白」完全一致。

---

## 四、未結 DR 清單

**空表。** 本輪 0 筆、無變動。休眠線索（VF747 export 二檔）狀態不變：
未開檔、未納素材、未登記。

---

## 五、獨立自評

**應驗而未驗者：一項。**

1. **T18d 之「對應候選」只做了字面比對，沒做語意比對。**
   下放包 T18d 令「依標題語意標註對應候選」。執行層實作為**詞集重疊比**
   （Jaccard，去停用詞、門檻 0.34）—— 那是字面重疊，不是語意。
   後果具體可見：`SWE1-FOTA-178` 之標題是一整句
   （`For a silent update, the OTA client follows these steps`），
   語意上明確屬於「靜默更新流程」，字面比對卻因句子詞多而稀釋分數，
   標為 `?`。同理 SYS1 側之 2/45 對應率，有多少是真的無對應、
   多少是切法不同導致字面不重疊，字面比對答不出來。

   **未改用語意比對之理由**：語意判定會使執行層實質參與 Layer 2 之
   分群決策，而 T18d 明令「執行層不得逕定 Test Set 名稱」、
   本表為「草料非結論」。字面比對之偏差**方向可預期且可揭露**
   （只會漏配、不會錯配成看似合理者），語意比對之偏差則會混入
   執行層的判斷而難以被分析層識別。

   **請分析層留意**：`?` 之 3 筆與 SYS1 側之 43 筆 `?`，
   **不表示無對應**，只表示自動比對不達門檻。若需語意層對照，
   請明令並指定其邊界（例如：只標候選不排序、或附信心等級）。

**兩項本包主動選擇之作法，聲明備查：**

- T18a 之「前言偽節」：Heading 之前若有 in-scope 列會被靜默丟棄而使
  閉合檢查**假性通過**，故另設一節承接。實測該節為 0 列，
  但檢查邏輯保留 —— 閉合式因此是真閉合，不是恰好對上。
- 量測腳本落於 `features/sw_update/scripts/framework_survey.py` 而非
  一次性指令，理由：T18 之五項數字將被 framework 起草反覆引用，
  須可重跑復現。腳本支援指定項次（`python3 scripts/framework_survey.py 18a`）。

---

## 六、量測條件揭露（R-G8）

| 項 | 方法／工具 | 偽陽性風險 |
|---|---|---|
| T18a 分群 | openpyxl `read_only/data_only`，`AnalysisReport_FULL` 列 8 起；以 `Categorization == "Heading"` 為分節點，依**文件序**走訪 | 分群依賴「Heading 列在其所轄列之前」此一版面慣例。若 037 有 Heading 置於區塊末者會錯分 —— 已以閉合檢查（311 = 311）與前言偽節（0 列）雙路守住總數，但**組內歸屬**之正確性僅靠版面慣例，未另證 |
| T18b SYS1 | `Outline Number` 之 `.` 數判層級 | Outline 若有 `1.10` 形態，字串排序會亂序 —— 已改以 `[int(p) for p in o.split(".")]` 數值排序 |
| T18c CFTS | `<w:p>` 切段 + `w:pStyle` 判 heading + `[Artifact Type:Subsystem Functional Requirement]` 宣告計數 | 需求物件歸章依**文件序鄰接**（同 T12 之限制，非 Polarion parent 欄）。閉合檢查（87 章／487 需求）守總數，組內歸屬同 T18a 之限制 |
| T18d 對照 | 詞集重疊比（Jaccard），停用詞表 12 字，門檻 0.34 | **見 §五 1 —— 這是字面比對，不是語意比對。** 偏差方向為只漏配不錯配；`?` 不等於無對應 |
| T18e 交叉表 | Counter over `Sub Categorization`，空值歸 `blank` | `\xa0`（U+00A0）若存在會被當非空值 —— **已實測**：本欄 383 格之型態為 `str` 310 + `NoneType` 73，空白類之實際值全為 `None`，含 `\xa0` 者 **0**（與 vehicle_category 之 `\xa0` 情形不同） |
| §3.1 重複標題 | 以 `Categorization == "Heading"` 取 45 列之 `Requirement Title`，`strip()` 後計 unique | 逐字比對，大小寫與內部空白差異會被視為不同標題 —— 實測 41 unique / 45，4 組重複皆為**完全逐字相同**，無邊界案例 |
