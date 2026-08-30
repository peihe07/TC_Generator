# ANCHOR_POOL — CFTS_57 Reflash 錨點池結構驗證（T10／T12）

依 R-SU4 v2 (a2) 與 R-SU7（`RULINGS.md`）：裸 7 位數之 regex 命中**不逕入池**，
須逐一以其在 `word/document.xml` 之結構脈絡驗證後分類。本檔為該驗證之全記錄。

- 素材：`inputs/R1LR_Atl-H_25PI4.5 Dec Release-xOTA_CFTS_57 Reflash_20251202-2111.docx`
  sha256 `9aa9400b3c97bfd893d13a4ba583c402e39ef415f5c517bcc4a0c9fe47336fb6`（133,530 B，真 OOXML）
- 方法：以 `<w:p>` 為段落單位切分（1,742 段），取 `w:pStyle` 為結構判準。
  heading style `1`–`4` 之 `{7位}` 為章節物件；TOC style `10`–`40` 為其鏡像，
  **不獨立入池**（否則每章重複計數）；其餘 7 位數依其右鄰之
  `: [Artifact Type:…]` 宣告歸類，無宣告者依左鄰文句歸「不可歸類」。
- **宣告優先於文序**（下放包 03 T12 之修正）：凡文件中任一處帶
  `[Artifact Type:…]` 宣告之 id，一律以該宣告定其類，不論其是否先以
  內文引用形態出現。初版（上繳包 01 T10）採「首見為準」，
  致 `4907923`、`4907934` 二者因先以 `Requirement ID {id}` 之內文形態
  出現而誤歸「不可歸類」。本檔為修正後之數，詳見 §七。
- **只分類不對應** —— 037 列與錨點之對應屬 Phase 2/3（R-SU4 v2 末段）。
- 偽陽性風險揭露（R-G8）：`w:pStyle` 為版面屬性，理論上可被手動套用而與語意脫節；
  已以「每個章節物件皆在 TOC 有對應 PAGEREF 項」交叉驗證（87 = 87）。

## 一、分類計數

| 類型 | unique id | 入池 |
|---|---:|---|
| 章節物件 | 87 | ✅ 入池 |
| 需求物件 | 487 | ✅ 入池 |
| Description 物件 | 137 | ❌ 排除 |
| 不可歸類 | 10 | ❌ 排除 |
| **合計** | **721** | 入池 **574** |

錨點池 = **574 個**（章節物件 87 + 需求物件 487）。
TC 錨定以需求物件 ID 為先；驗證對象為章節整體時方用章節物件 ID（R-SU4 v2 (a2)）。
Description 物件依 R-SU7 **不入池**，其對照見 §六。


## 二、章節物件（87）

| ObjectID | 所屬章節 | 驗證脈絡 |
|---|---|---|
| `4907230` | 1 Reflash [CFTSMV057_CIP_R1] | heading style 1：`1 Reflash [CFTSMV057_CIP_R1] {4907230}` |
| `4907231` | 1.1 Revision Notes | heading style 2：`1.1 Revision Notes {4907231}` |
| `4907233` | 1.2 Introduction | heading style 2：`1.2 Introduction {4907233}` |
| `4907241` | 2 Common Reflash Requirements | heading style 1：`2 Common Reflash Requirements {4907241}` |
| `4907259` | 3 Media Reflash Requirements | heading style 1：`3 Media Reflash Requirements {4907259}` |
| `4907261` | 4 FOTA Reflash Requirements | heading style 1：`4 FOTA Reflash Requirements {4907261}` |
| `4907267` | 4.1 This Document | heading style 2：`4.1 This Document {4907267}` |
| `4907269` | 4.1.1 Related Documents and Specifications | heading style 3：`4.1.1 Related Documents and Specifications {4907269}` |
| `4907272` | 4.2 Use Cases for OTA client | heading style 2：`4.2 Use Cases for OTA client {4907272}` |
| `4907273` | 4.2.1 Over The Air (OTA) Deployment of Software | heading style 3：`4.2.1 Over The Air (OTA) Deployment of Software {4907273}` |
| `4907275` | 4.2.2 Local Deployment of Software | heading style 3：`4.2.2 Local Deployment of Software {4907275}` |
| `4907277` | 4.2.3 HU FOTA with TBM | heading style 3：`4.2.3 HU FOTA with TBM {4907277}` |
| `4907282` | 4.2.4 Software Configuration Reporting | heading style 3：`4.2.4 Software Configuration Reporting {4907282}` |
| `4907284` | 4.3 High Level FOTA Diagram | heading style 2：`4.3 High Level FOTA Diagram {4907284}` |
| `4907287` | 4.4 OTA Client Architecture | heading style 2：`4.4 OTA Client Architecture {4907287}` |
| `4907313` | 4.4.1 OTA Architecture Requirements | heading style 3：`4.4.1 OTA Architecture Requirements {4907313}` |
| `4907337` | 4.4.2 OTA Client Configuration options | heading style 3：`4.4.2 OTA Client Configuration options {4907337}` |
| `4907344` | 4.4.3 Operating Environment | heading style 3：`4.4.3 Operating Environment {4907344}` |
| `4907353` | 4.5 Interface Definitions | heading style 2：`4.5 Interface Definitions {4907353}` |
| `4907354` | 4.5.1 OTA Communication Protocols | heading style 3：`4.5.1 OTA Communication Protocols {4907354}` |
| `4907358` | 4.5.2 User initiated sessions | heading style 3：`4.5.2 User initiated sessions {4907358}` |
| `4907362` | 4.5.3 Vehicle initiated sessions | heading style 3：`4.5.3 Vehicle initiated sessions {4907362}` |
| `4907369` | 4.5.4 OTA server initiated sessions | heading style 3：`4.5.4 OTA server initiated sessions {4907369}` |
| `4907371` | 4.5.4.1 SMS/MQTT Push Support | heading style 4：`4.5.4.1 SMS/MQTT Push Support {4907371}` |
| `4907382` | 4.5.5 Bus communications | heading style 3：`4.5.5 Bus communications {4907382}` |
| `4907395` | 4.6 OTA download via Wi-Fi | heading style 2：`4.6 OTA download via Wi-Fi {4907395}` |
| `4907401` | 4.6.1 Connection to Wi-Fi network | heading style 3：`4.6.1 Connection to Wi-Fi network {4907401}` |
| `4907413` | 4.6.2 Non-Critical Updates | heading style 3：`4.6.2 Non-Critical Updates {4907413}` |
| `4907416` | 4.6.3 Software Download via Wi-Fi | heading style 3：`4.6.3 Software Download via Wi-Fi {4907416}` |
| `4907434` | 4.7 OTA Client Application | heading style 2：`4.7 OTA Client Application {4907434}` |
| `4907436` | 4.7.1 OTA Client Performance Requirements | heading style 3：`4.7.1 OTA Client Performance Requirements {4907436}` |
| `4907441` | 4.7.2 OTA client Flows | heading style 3：`4.7.2 OTA client Flows {4907441}` |
| `4907448` | 4.7.3 Main Update Configuration Options | heading style 3：`4.7.3 Main Update Configuration Options {4907448}` |
| `4907465` | 4.7.3.1 Critical Updates | heading style 4：`4.7.3.1 Critical Updates {4907465}` |
| `4907474` | 4.7.3.2 Silent Updates | heading style 4：`4.7.3.2 Silent Updates {4907474}` |
| `4907488` | 4.7.3.3 Regular Updates | heading style 4：`4.7.3.3 Regular Updates {4907488}` |
| `4907490` | 4.8 Security | heading style 2：`4.8 Security {4907490}` |
| `4907498` | 4.8.1 Communication Security | heading style 3：`4.8.1 Communication Security {4907498}` |
| `4907507` | 4.8.2 OMA-DM Security | heading style 3：`4.8.2 OMA-DM Security {4907507}` |
| `4907512` | 4.8.3 Deployment Package Security | heading style 3：`4.8.3 Deployment Package Security {4907512}` |
| `4907522` | 4.9 Re-Flashing Requirements | heading style 2：`4.9 Re-Flashing Requirements {4907522}` |
| `4907523` | 4.9.1 Update Agent Requirements | heading style 3：`4.9.1 Update Agent Requirements {4907523}` |
| `4907542` | 4.9.2 ECU Module specific considerations | heading style 3：`4.9.2 ECU Module specific considerations {4907542}` |
| `4907551` | 4.10 Session Flows | heading style 2：`4.10 Session Flows {4907551}` |
| `4907555` | 4.10.1 Self Registration Flow | heading style 3：`4.10.1 Self Registration Flow {4907555}` |
| `4907564` | 4.10.2 Server-Initiated Session Flow | heading style 3：`4.10.2 Server-Initiated Session Flow {4907564}` |
| `4907578` | 4.10.3 Vehicle-Initiated Session Flow | heading style 3：`4.10.3 Vehicle-Initiated Session Flow {4907578}` |
| `4907593` | 4.10.4 User-Initiated Session Flow | heading style 3：`4.10.4 User-Initiated Session Flow {4907593}` |
| `4907598` | 4.10.5 Deployment Flow | heading style 3：`4.10.5 Deployment Flow {4907598}` |
| `4907608` | 4.10.5.1 Installation and Download Conditions | heading style 4：`4.10.5.1 Installation and Download Conditions {4907608}` |
| `4907651` | 4.11 User Experience (UX)/HMI | heading style 2：`4.11 User Experience (UX)/HMI {4907651}` |
| `4907664` | 4.12 Interrupt Handling | heading style 2：`4.12 Interrupt Handling {4907664}` |
| `4907678` | 4.12.1 Resuming a Download | heading style 3：`4.12.1 Resuming a Download {4907678}` |
| `4907685` | 4.12.2 Report Persistency | heading style 3：`4.12.2 Report Persistency {4907685}` |
| `4907692` | 4.13 OMA-DM Management Object Support | heading style 2：`4.13 OMA-DM Management Object Support {4907692}` |
| `4907693` | 4.13.1 SCOMO Support | heading style 3：`4.13.1 SCOMO Support {4907693}` |
| `4907711` | 4.13.2 LAWMO Support | heading style 3：`4.13.2 LAWMO Support {4907711}` |
| `4907721` | 4.13.2.1 Lock | heading style 4：`4.13.2.1 Lock {4907721}` |
| `4907730` | 4.13.2.2 Unlock | heading style 4：`4.13.2.2 Unlock {4907730}` |
| `4907734` | 4.13.2.3 Wipe Data | heading style 4：`4.13.2.3 Wipe Data {4907734}` |
| `4907738` | 4.13.3 Additional Support Objects | heading style 3：`4.13.3 Additional Support Objects {4907738}` |
| `4907741` | 4.13.4 FCA Specific Tree structure (DDF) | heading style 3：`4.13.4 FCA Specific Tree structure (DDF) {4907741}` |
| `4907743` | 4.13.4.1 Appendix A Download Descriptor Format | heading style 4：`4.13.4.1 Appendix A Download Descriptor Format {4907743}` |
| `4907764` | 4.13.4.2 Appendix B Configurable Parameters | heading style 4：`4.13.4.2 Appendix B Configurable Parameters {4907764}` |
| `4907768` | 4.13.4.3 Appendix C OTA Commands | heading style 4：`4.13.4.3 Appendix C OTA Commands {4907768}` |
| `4907772` | 4.13.4.4 Appendix D Terms and Abbreviations | heading style 4：`4.13.4.4 Appendix D Terms and Abbreviations {4907772}` |
| `4907775` | 5 TBM FOTA Reflash Requirements | heading style 1：`5 TBM FOTA Reflash Requirements {4907775}` |
| `4907798` | 6 TBM Algorithm Requirements | heading style 1：`6 TBM Algorithm Requirements {4907798}` |
| `4907815` | 7 Firmware Over-the-air Updates (FOTA) | heading style 1：`7 Firmware Over-the-air Updates (FOTA) {4907815}` |
| `4907824` | 7.1 Critical Updates | heading style 2：`7.1 Critical Updates {4907824}` |
| `4907833` | 8 Maps Over-the-air Updates (MOTA) | heading style 1：`8 Maps Over-the-air Updates (MOTA) {4907833}` |
| `4907840` | 8.1 Non-Critical Updates | heading style 2：`8.1 Non-Critical Updates {4907840}` |
| `4907863` | 8.2 Route Planning Updates | heading style 2：`8.2 Route Planning Updates {4907863}` |
| `4907866` | 8.3 User Initiated Updates | heading style 2：`8.3 User Initiated Updates {4907866}` |
| `4907871` | 8.4 MOTA Client Initiated Updates | heading style 2：`8.4 MOTA Client Initiated Updates {4907871}` |
| `4907878` | 9 FOTA ROV Reflash Requirements | heading style 1：`9 FOTA ROV Reflash Requirements {4907878}` |
| `4907879` | 9.1 Pre-Installation | heading style 2：`9.1 Pre-Installation {4907879}` |
| `4907897` | 9.2 Installation Progress | heading style 2：`9.2 Installation Progress {4907897}` |
| `4907905` | 9.3 Post-Installation | heading style 2：`9.3 Post-Installation {4907905}` |
| `4907911` | 9.4 TBM FOTA Rest of Vehicle Requirements | heading style 2：`9.4 TBM FOTA Rest of Vehicle Requirements {4907911}` |
| `4907912` | 9.4.1 Pre-Installation | heading style 3：`9.4.1 Pre-Installation {4907912}` |
| `4907916` | 10 Wi-Fi Only Yard Hold Reflash | heading style 1：`10 Wi-Fi Only Yard Hold Reflash {4907916}` |
| `4907917` | 10.1 Shipping/Logistic mode | heading style 2：`10.1 Shipping/Logistic mode {4907917}` |
| `4907919` | 10.2 Wi-Fi | heading style 2：`10.2 Wi-Fi {4907919}` |
| `4907930` | 10.3 Installation | heading style 2：`10.3 Installation {4907930}` |
| `4907935` | 10.4 Post-Installation | heading style 2：`10.4 Post-Installation {4907935}` |
| `4907938` | 10.5 Security (Hopefully remove and reference to Rej | heading style 2：`10.5 Security (Hopefully remove and reference to Rejani/Ansaf spec) {4907938}` |

## 三、需求物件（487）

| ObjectID | 所屬章節 | 驗證脈絡 |
|---|---|---|
| `4907243` | 2 Common Reflash Requirements | `4907243: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907244` | 1.1 Revision Notes | `4907244: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907245` | 2 Common Reflash Requirements | `4907245: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907246` | 2 Common Reflash Requirements | `4907246: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907247` | 2 Common Reflash Requirements | `4907247: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907248` | 2 Common Reflash Requirements | `4907248: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907249` | 2 Common Reflash Requirements | `4907249: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907250` | 2 Common Reflash Requirements | `4907250: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907251` | 2 Common Reflash Requirements | `4907251: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907252` | 2 Common Reflash Requirements | `4907252: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907253` | 2 Common Reflash Requirements | `4907253: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907254` | 2 Common Reflash Requirements | `4907254: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907255` | 2 Common Reflash Requirements | `4907255: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907256` | 2 Common Reflash Requirements | `4907256: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907257` | 2 Common Reflash Requirements | `4907257: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907258` | 2 Common Reflash Requirements | `4907258: [Artifact Type:Subsystem Functional Requirement]` 於「2 Common Reflash Requirements」下 |
| `4907278` | 4.2.3 HU FOTA with TBM | `4907278: [Artifact Type:Subsystem Functional Requirement]` 於「4.2.3 HU FOTA with TBM」下 |
| `4907279` | 4.2.3 HU FOTA with TBM | `4907279: [Artifact Type:Subsystem Functional Requirement]` 於「4.2.3 HU FOTA with TBM」下 |
| `4907280` | 4.2.3 HU FOTA with TBM | `4907280: [Artifact Type:Subsystem Functional Requirement]` 於「4.2.3 HU FOTA with TBM」下 |
| `4907281` | 4.2.3 HU FOTA with TBM | `4907281: [Artifact Type:Subsystem Functional Requirement]` 於「4.2.3 HU FOTA with TBM」下 |
| `4907291` | 4.4 OTA Client Architecture | `4907291: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907292` | 4.4 OTA Client Architecture | `4907292: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907293` | 4.4 OTA Client Architecture | `4907293: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907294` | 4.4 OTA Client Architecture | `4907294: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907295` | 4.4 OTA Client Architecture | `4907295: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907296` | 4.4 OTA Client Architecture | `4907296: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907297` | 4.4 OTA Client Architecture | `4907297: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907298` | 4.4 OTA Client Architecture | `4907298: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907299` | 4.4 OTA Client Architecture | `4907299: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907300` | 4.4 OTA Client Architecture | `4907300: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907301` | 4.4 OTA Client Architecture | `4907301: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907302` | 4.4 OTA Client Architecture | `4907302: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907303` | 4.4 OTA Client Architecture | `4907303: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907304` | 4.4 OTA Client Architecture | `4907304: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907305` | 4.4 OTA Client Architecture | `4907305: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907306` | 4.4 OTA Client Architecture | `4907306: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907307` | 4.4 OTA Client Architecture | `4907307: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907308` | 4.4 OTA Client Architecture | `4907308: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907309` | 4.4 OTA Client Architecture | `4907309: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907310` | 4.4 OTA Client Architecture | `4907310: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907311` | 4.4 OTA Client Architecture | `4907311: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907312` | 4.4 OTA Client Architecture | `4907312: [Artifact Type:Subsystem Functional Requirement]` 於「4.4 OTA Client Architecture」下 |
| `4907314` | 4.4.1 OTA Architecture Requirements | `4907314: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907315` | 4.4.1 OTA Architecture Requirements | `4907315: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907316` | 4.4.1 OTA Architecture Requirements | `4907316: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907317` | 4.4.1 OTA Architecture Requirements | `4907317: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907320` | 4.4.1 OTA Architecture Requirements | `4907320: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907321` | 4.4.1 OTA Architecture Requirements | `4907321: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907322` | 4.4.1 OTA Architecture Requirements | `4907322: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907323` | 4.4.1 OTA Architecture Requirements | `4907323: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907326` | 4.4.1 OTA Architecture Requirements | `4907326: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907327` | 4.4.1 OTA Architecture Requirements | `4907327: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907328` | 4.4.1 OTA Architecture Requirements | `4907328: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907329` | 4.4.1 OTA Architecture Requirements | `4907329: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907330` | 4.4.1 OTA Architecture Requirements | `4907330: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907331` | 4.4.1 OTA Architecture Requirements | `4907331: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907332` | 4.4.1 OTA Architecture Requirements | `4907332: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907333` | 4.4.1 OTA Architecture Requirements | `4907333: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907334` | 4.4.1 OTA Architecture Requirements | `4907334: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907335` | 4.4.1 OTA Architecture Requirements | `4907335: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907336` | 4.4.1 OTA Architecture Requirements | `4907336: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907338` | 4.4.2 OTA Client Configuration options | `4907338: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.2 OTA Client Configuration options」下 |
| `4907339` | 4.4.2 OTA Client Configuration options | `4907339: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.2 OTA Client Configuration options」下 |
| `4907340` | 4.4.2 OTA Client Configuration options | `4907340: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.2 OTA Client Configuration options」下 |
| `4907341` | 4.4.2 OTA Client Configuration options | `4907341: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.2 OTA Client Configuration options」下 |
| `4907342` | 4.4.2 OTA Client Configuration options | `4907342: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.2 OTA Client Configuration options」下 |
| `4907343` | 4.4.2 OTA Client Configuration options | `4907343: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.2 OTA Client Configuration options」下 |
| `4907345` | 4.4.3 Operating Environment | `4907345: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907346` | 4.4.3 Operating Environment | `4907346: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907347` | 4.4.3 Operating Environment | `4907347: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907348` | 4.4.3 Operating Environment | `4907348: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907349` | 4.4.3 Operating Environment | `4907349: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907350` | 4.4.3 Operating Environment | `4907350: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907351` | 4.4.3 Operating Environment | `4907351: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907352` | 4.4.3 Operating Environment | `4907352: [Artifact Type:Subsystem Functional Requirement]` 於「4.4.3 Operating Environment」下 |
| `4907355` | 4.5.1 OTA Communication Protocols | `4907355: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.1 OTA Communication Protocols」下 |
| `4907359` | 4.5.2 User initiated sessions | `4907359: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.2 User initiated sessions」下 |
| `4907360` | 4.5.2 User initiated sessions | `4907360: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.2 User initiated sessions」下 |
| `4907361` | 4.5.2 User initiated sessions | `4907361: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.2 User initiated sessions」下 |
| `4907364` | 4.5.3 Vehicle initiated sessions | `4907364: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.3 Vehicle initiated sessions」下 |
| `4907365` | 4.5.3 Vehicle initiated sessions | `4907365: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.3 Vehicle initiated sessions」下 |
| `4907366` | 4.5.3 Vehicle initiated sessions | `4907366: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.3 Vehicle initiated sessions」下 |
| `4907367` | 4.5.3 Vehicle initiated sessions | `4907367: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.3 Vehicle initiated sessions」下 |
| `4907368` | 4.5.3 Vehicle initiated sessions | `4907368: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.3 Vehicle initiated sessions」下 |
| `4907370` | 4.5.4 OTA server initiated sessions | `4907370: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4 OTA server initiated sessions」下 |
| `4907372` | 4.5.4.1 SMS/MQTT Push Support | `4907372: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907373` | 4.5.4.1 SMS/MQTT Push Support | `4907373: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907374` | 4.5.4.1 SMS/MQTT Push Support | `4907374: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907375` | 4.5.4.1 SMS/MQTT Push Support | `4907375: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907376` | 4.5.4.1 SMS/MQTT Push Support | `4907376: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907377` | 4.5.4.1 SMS/MQTT Push Support | `4907377: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907378` | 4.5.4.1 SMS/MQTT Push Support | `4907378: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907379` | 4.5.4.1 SMS/MQTT Push Support | `4907379: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907380` | 4.5.4.1 SMS/MQTT Push Support | `4907380: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907381` | 4.5.4.1 SMS/MQTT Push Support | `4907381: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.4.1 SMS/MQTT Push Support」下 |
| `4907385` | 4.5.5 Bus communications | `4907385: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907386` | 4.5.5 Bus communications | `4907386: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907387` | 4.5.5 Bus communications | `4907387: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907388` | 4.5.5 Bus communications | `4907388: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907389` | 4.5.5 Bus communications | `4907389: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907392` | 4.5.5 Bus communications | `4907392: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907393` | 4.5.5 Bus communications | `4907393: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907394` | 4.5.5 Bus communications | `4907394: [Artifact Type:Subsystem Functional Requirement]` 於「4.5.5 Bus communications」下 |
| `4907396` | 4.6 OTA download via Wi-Fi | `4907396: [Artifact Type:Subsystem Functional Requirement]` 於「4.6 OTA download via Wi-Fi」下 |
| `4907397` | 1.1 Revision Notes | `4907397: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907398` | 4.6 OTA download via Wi-Fi | `4907398: [Artifact Type:Subsystem Functional Requirement]` 於「4.6 OTA download via Wi-Fi」下 |
| `4907399` | 4.6 OTA download via Wi-Fi | `4907399: [Artifact Type:Subsystem Functional Requirement]` 於「4.6 OTA download via Wi-Fi」下 |
| `4907400` | 4.6 OTA download via Wi-Fi | `4907400: [Artifact Type:Subsystem Functional Requirement]` 於「4.6 OTA download via Wi-Fi」下 |
| `4907402` | 4.6.1 Connection to Wi-Fi network | `4907402: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907403` | 4.6.1 Connection to Wi-Fi network | `4907403: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907404` | 4.6.1 Connection to Wi-Fi network | `4907404: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907405` | 4.6.1 Connection to Wi-Fi network | `4907405: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907406` | 4.6.1 Connection to Wi-Fi network | `4907406: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907407` | 4.6.1 Connection to Wi-Fi network | `4907407: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907408` | 4.6.1 Connection to Wi-Fi network | `4907408: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907409` | 4.6.1 Connection to Wi-Fi network | `4907409: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907410` | 4.6.1 Connection to Wi-Fi network | `4907410: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907411` | 4.6.1 Connection to Wi-Fi network | `4907411: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907412` | 4.6.1 Connection to Wi-Fi network | `4907412: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.1 Connection to Wi-Fi network」下 |
| `4907414` | 4.6.2 Non-Critical Updates | `4907414: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.2 Non-Critical Updates」下 |
| `4907415` | 4.6.2 Non-Critical Updates | `4907415: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.2 Non-Critical Updates」下 |
| `4907417` | 4.6.3 Software Download via Wi-Fi | `4907417: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907418` | 4.6.3 Software Download via Wi-Fi | `4907418: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907419` | 4.6.3 Software Download via Wi-Fi | `4907419: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907420` | 4.6.3 Software Download via Wi-Fi | `4907420: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907421` | 4.6.3 Software Download via Wi-Fi | `4907421: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907422` | 4.6.3 Software Download via Wi-Fi | `4907422: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907423` | 4.6.3 Software Download via Wi-Fi | `4907423: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907424` | 4.6.3 Software Download via Wi-Fi | `4907424: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907425` | 4.6.3 Software Download via Wi-Fi | `4907425: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907426` | 4.6.3 Software Download via Wi-Fi | `4907426: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907427` | 4.6.3 Software Download via Wi-Fi | `4907427: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907428` | 4.6.3 Software Download via Wi-Fi | `4907428: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907429` | 4.6.3 Software Download via Wi-Fi | `4907429: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907430` | 4.6.3 Software Download via Wi-Fi | `4907430: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907431` | 4.6.3 Software Download via Wi-Fi | `4907431: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907432` | 4.6.3 Software Download via Wi-Fi | `4907432: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907433` | 4.6.3 Software Download via Wi-Fi | `4907433: [Artifact Type:Subsystem Functional Requirement]` 於「4.6.3 Software Download via Wi-Fi」下 |
| `4907435` | 4.7 OTA Client Application | `4907435: [Artifact Type:Subsystem Functional Requirement]` 於「4.7 OTA Client Application」下 |
| `4907437` | 4.7.1 OTA Client Performance Requirements | `4907437: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.1 OTA Client Performance Requirements」下 |
| `4907438` | 4.7.1 OTA Client Performance Requirements | `4907438: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.1 OTA Client Performance Requirements」下 |
| `4907439` | 4.7.1 OTA Client Performance Requirements | `4907439: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.1 OTA Client Performance Requirements」下 |
| `4907440` | 4.7.1 OTA Client Performance Requirements | `4907440: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.1 OTA Client Performance Requirements」下 |
| `4907442` | 4.7.2 OTA client Flows | `4907442: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.2 OTA client Flows」下 |
| `4907443` | 4.7.2 OTA client Flows | `4907443: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.2 OTA client Flows」下 |
| `4907444` | 4.7.2 OTA client Flows | `4907444: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.2 OTA client Flows」下 |
| `4907447` | 4.7.2 OTA client Flows | `4907447: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.2 OTA client Flows」下 |
| `4907449` | 4.7.3 Main Update Configuration Options | `4907449: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907450` | 4.7.3 Main Update Configuration Options | `4907450: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907451` | 4.7.3 Main Update Configuration Options | `4907451: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907452` | 4.7.3 Main Update Configuration Options | `4907452: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907453` | 4.7.3 Main Update Configuration Options | `4907453: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907454` | 4.7.3 Main Update Configuration Options | `4907454: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907455` | 4.7.3 Main Update Configuration Options | `4907455: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907456` | 4.7.3 Main Update Configuration Options | `4907456: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907457` | 4.7.3 Main Update Configuration Options | `4907457: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907458` | 4.7.3 Main Update Configuration Options | `4907458: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907459` | 4.7.3 Main Update Configuration Options | `4907459: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907460` | 4.7.3 Main Update Configuration Options | `4907460: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907461` | 4.7.3 Main Update Configuration Options | `4907461: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907462` | 4.7.3 Main Update Configuration Options | `4907462: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907463` | 4.7.3 Main Update Configuration Options | `4907463: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907464` | 4.7.3 Main Update Configuration Options | `4907464: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3 Main Update Configuration Options」下 |
| `4907466` | 4.7.3.1 Critical Updates | `4907466: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907467` | 4.7.3.1 Critical Updates | `4907467: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907468` | 4.7.3.1 Critical Updates | `4907468: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907469` | 4.7.3.1 Critical Updates | `4907469: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907470` | 4.7.3.1 Critical Updates | `4907470: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907471` | 4.7.3.1 Critical Updates | `4907471: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907472` | 4.7.3.1 Critical Updates | `4907472: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907473` | 4.7.3.1 Critical Updates | `4907473: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.1 Critical Updates」下 |
| `4907475` | 4.7.3.2 Silent Updates | `4907475: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907476` | 4.7.3.2 Silent Updates | `4907476: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907477` | 4.7.3.2 Silent Updates | `4907477: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907478` | 4.7.3.2 Silent Updates | `4907478: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907479` | 4.7.3.2 Silent Updates | `4907479: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907480` | 4.7.3.2 Silent Updates | `4907480: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907481` | 4.7.3.2 Silent Updates | `4907481: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907482` | 4.7.3.2 Silent Updates | `4907482: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907483` | 4.7.3.2 Silent Updates | `4907483: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907484` | 4.7.3.2 Silent Updates | `4907484: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907485` | 4.7.3.2 Silent Updates | `4907485: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907486` | 4.7.3.2 Silent Updates | `4907486: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907487` | 4.7.3.2 Silent Updates | `4907487: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.2 Silent Updates」下 |
| `4907489` | 4.7.3.3 Regular Updates | `4907489: [Artifact Type:Subsystem Functional Requirement]` 於「4.7.3.3 Regular Updates」下 |
| `4907491` | 4.8 Security | `4907491: [Artifact Type:Subsystem Functional Requirement]` 於「4.8 Security」下 |
| `4907492` | 4.8 Security | `4907492: [Artifact Type:Subsystem Functional Requirement]` 於「4.8 Security」下 |
| `4907493` | 4.8 Security | `4907493: [Artifact Type:Subsystem Functional Requirement]` 於「4.8 Security」下 |
| `4907494` | 4.8 Security | `4907494: [Artifact Type:Subsystem Functional Requirement]` 於「4.8 Security」下 |
| `4907495` | 4.8 Security | `4907495: [Artifact Type:Subsystem Functional Requirement]` 於「4.8 Security」下 |
| `4907496` | 4.8 Security | `4907496: [Artifact Type:Subsystem Functional Requirement]` 於「4.8 Security」下 |
| `4907497` | 4.8 Security | `4907497: [Artifact Type:Subsystem Functional Requirement]` 於「4.8 Security」下 |
| `4907499` | 4.8.1 Communication Security | `4907499: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907500` | 4.8.1 Communication Security | `4907500: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907501` | 4.8.1 Communication Security | `4907501: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907502` | 4.8.1 Communication Security | `4907502: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907503` | 4.8.1 Communication Security | `4907503: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907504` | 4.8.1 Communication Security | `4907504: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907505` | 4.8.1 Communication Security | `4907505: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907506` | 4.8.1 Communication Security | `4907506: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.1 Communication Security」下 |
| `4907508` | 4.8.2 OMA-DM Security | `4907508: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.2 OMA-DM Security」下 |
| `4907509` | 4.8.2 OMA-DM Security | `4907509: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.2 OMA-DM Security」下 |
| `4907510` | 4.8.2 OMA-DM Security | `4907510: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.2 OMA-DM Security」下 |
| `4907513` | 4.8.3 Deployment Package Security | `4907513: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907514` | 4.8.3 Deployment Package Security | `4907514: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907515` | 4.8.3 Deployment Package Security | `4907515: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907516` | 4.8.3 Deployment Package Security | `4907516: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907517` | 4.8.3 Deployment Package Security | `4907517: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907518` | 4.8.3 Deployment Package Security | `4907518: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907519` | 4.8.3 Deployment Package Security | `4907519: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907520` | 4.8.3 Deployment Package Security | `4907520: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907521` | 4.8.3 Deployment Package Security | `4907521: [Artifact Type:Subsystem Functional Requirement]` 於「4.8.3 Deployment Package Security」下 |
| `4907524` | 4.9.1 Update Agent Requirements | `4907524: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907525` | 4.9.1 Update Agent Requirements | `4907525: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907526` | 4.9.1 Update Agent Requirements | `4907526: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907527` | 4.9.1 Update Agent Requirements | `4907527: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907528` | 4.9.1 Update Agent Requirements | `4907528: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907529` | 4.9.1 Update Agent Requirements | `4907529: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907530` | 4.9.1 Update Agent Requirements | `4907530: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907531` | 4.9.1 Update Agent Requirements | `4907531: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907532` | 4.9.1 Update Agent Requirements | `4907532: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907533` | 4.9.1 Update Agent Requirements | `4907533: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907534` | 4.9.1 Update Agent Requirements | `4907534: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907535` | 4.9.1 Update Agent Requirements | `4907535: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907536` | 4.9.1 Update Agent Requirements | `4907536: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907537` | 4.9.1 Update Agent Requirements | `4907537: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907538` | 4.9.1 Update Agent Requirements | `4907538: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907539` | 4.9.1 Update Agent Requirements | `4907539: [Artifact Type:Subsystem Functional Requirement]` 於「4.9.1 Update Agent Requirements」下 |
| `4907552` | 4.10 Session Flows | `4907552: [Artifact Type:Subsystem Functional Requirement]` 於「4.10 Session Flows」下 |
| `4907553` | 4.10 Session Flows | `4907553: [Artifact Type:Subsystem Functional Requirement]` 於「4.10 Session Flows」下 |
| `4907554` | 4.10 Session Flows | `4907554: [Artifact Type:Subsystem Functional Requirement]` 於「4.10 Session Flows」下 |
| `4907556` | 4.10.1 Self Registration Flow | `4907556: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907557` | 4.10.1 Self Registration Flow | `4907557: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907558` | 4.10.1 Self Registration Flow | `4907558: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907559` | 4.10.1 Self Registration Flow | `4907559: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907560` | 4.10.1 Self Registration Flow | `4907560: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907561` | 4.10.1 Self Registration Flow | `4907561: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907562` | 4.10.1 Self Registration Flow | `4907562: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907563` | 4.10.1 Self Registration Flow | `4907563: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.1 Self Registration Flow」下 |
| `4907565` | 4.10.2 Server-Initiated Session Flow | `4907565: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907566` | 4.10.2 Server-Initiated Session Flow | `4907566: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907567` | 4.10.2 Server-Initiated Session Flow | `4907567: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907568` | 4.10.2 Server-Initiated Session Flow | `4907568: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907569` | 4.10.2 Server-Initiated Session Flow | `4907569: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907570` | 4.10.2 Server-Initiated Session Flow | `4907570: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907571` | 4.10.2 Server-Initiated Session Flow | `4907571: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907572` | 4.10.2 Server-Initiated Session Flow | `4907572: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907573` | 4.10.2 Server-Initiated Session Flow | `4907573: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907574` | 4.10.2 Server-Initiated Session Flow | `4907574: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907575` | 4.10.2 Server-Initiated Session Flow | `4907575: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907576` | 4.10.2 Server-Initiated Session Flow | `4907576: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907577` | 4.10.2 Server-Initiated Session Flow | `4907577: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.2 Server-Initiated Session Flow」下 |
| `4907579` | 4.10.3 Vehicle-Initiated Session Flow | `4907579: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907580` | 4.10.3 Vehicle-Initiated Session Flow | `4907580: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907581` | 4.10.3 Vehicle-Initiated Session Flow | `4907581: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907582` | 4.10.3 Vehicle-Initiated Session Flow | `4907582: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907583` | 4.10.3 Vehicle-Initiated Session Flow | `4907583: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907584` | 4.10.3 Vehicle-Initiated Session Flow | `4907584: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907585` | 4.10.3 Vehicle-Initiated Session Flow | `4907585: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907586` | 4.10.3 Vehicle-Initiated Session Flow | `4907586: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907587` | 4.10.3 Vehicle-Initiated Session Flow | `4907587: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907588` | 4.10.3 Vehicle-Initiated Session Flow | `4907588: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907589` | 4.10.3 Vehicle-Initiated Session Flow | `4907589: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907590` | 4.10.3 Vehicle-Initiated Session Flow | `4907590: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907591` | 4.10.3 Vehicle-Initiated Session Flow | `4907591: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907592` | 4.10.3 Vehicle-Initiated Session Flow | `4907592: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.3 Vehicle-Initiated Session Flow」下 |
| `4907594` | 4.10.4 User-Initiated Session Flow | `4907594: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.4 User-Initiated Session Flow」下 |
| `4907595` | 4.10.4 User-Initiated Session Flow | `4907595: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.4 User-Initiated Session Flow」下 |
| `4907596` | 4.10.4 User-Initiated Session Flow | `4907596: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.4 User-Initiated Session Flow」下 |
| `4907597` | 4.10.4 User-Initiated Session Flow | `4907597: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.4 User-Initiated Session Flow」下 |
| `4907599` | 4.10.5 Deployment Flow | `4907599: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907600` | 4.10.5 Deployment Flow | `4907600: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907601` | 4.10.5 Deployment Flow | `4907601: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907602` | 4.10.5 Deployment Flow | `4907602: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907603` | 4.10.5 Deployment Flow | `4907603: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907604` | 4.10.5 Deployment Flow | `4907604: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907605` | 4.10.5 Deployment Flow | `4907605: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907606` | 4.10.5 Deployment Flow | `4907606: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907607` | 4.10.5 Deployment Flow | `4907607: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5 Deployment Flow」下 |
| `4907609` | 4.10.5.1 Installation and Download Conditions | `4907609: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907610` | 4.10.5.1 Installation and Download Conditions | `4907610: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907611` | 4.10.5.1 Installation and Download Conditions | `4907611: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907612` | 4.10.5.1 Installation and Download Conditions | `4907612: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907613` | 4.10.5.1 Installation and Download Conditions | `4907613: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907614` | 4.10.5.1 Installation and Download Conditions | `4907614: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907615` | 4.10.5.1 Installation and Download Conditions | `4907615: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907616` | 4.10.5.1 Installation and Download Conditions | `4907616: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907617` | 4.10.5.1 Installation and Download Conditions | `4907617: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907618` | 4.10.5.1 Installation and Download Conditions | `4907618: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907619` | 4.10.5.1 Installation and Download Conditions | `4907619: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907620` | 4.10.5.1 Installation and Download Conditions | `4907620: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907621` | 4.10.5.1 Installation and Download Conditions | `4907621: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907622` | 4.10.5.1 Installation and Download Conditions | `4907622: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907623` | 4.10.5.1 Installation and Download Conditions | `4907623: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907624` | 4.10.5.1 Installation and Download Conditions | `4907624: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907625` | 4.10.5.1 Installation and Download Conditions | `4907625: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907626` | 4.10.5.1 Installation and Download Conditions | `4907626: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907627` | 4.10.5.1 Installation and Download Conditions | `4907627: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907628` | 4.10.5.1 Installation and Download Conditions | `4907628: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907629` | 4.10.5.1 Installation and Download Conditions | `4907629: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907630` | 4.10.5.1 Installation and Download Conditions | `4907630: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907631` | 4.10.5.1 Installation and Download Conditions | `4907631: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907632` | 4.10.5.1 Installation and Download Conditions | `4907632: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907633` | 4.10.5.1 Installation and Download Conditions | `4907633: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907634` | 4.10.5.1 Installation and Download Conditions | `4907634: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907635` | 4.10.5.1 Installation and Download Conditions | `4907635: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907636` | 4.10.5.1 Installation and Download Conditions | `4907636: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907638` | 4.10.5.1 Installation and Download Conditions | `4907638: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907639` | 4.10.5.1 Installation and Download Conditions | `4907639: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907640` | 4.10.5.1 Installation and Download Conditions | `4907640: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907641` | 4.10.5.1 Installation and Download Conditions | `4907641: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907642` | 4.10.5.1 Installation and Download Conditions | `4907642: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907643` | 4.10.5.1 Installation and Download Conditions | `4907643: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907644` | 4.10.5.1 Installation and Download Conditions | `4907644: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907645` | 4.10.5.1 Installation and Download Conditions | `4907645: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907646` | 4.10.5.1 Installation and Download Conditions | `4907646: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907647` | 4.10.5.1 Installation and Download Conditions | `4907647: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907648` | 4.10.5.1 Installation and Download Conditions | `4907648: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907649` | 4.10.5.1 Installation and Download Conditions | `4907649: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907650` | 4.10.5.1 Installation and Download Conditions | `4907650: [Artifact Type:Subsystem Functional Requirement]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907652` | 4.11 User Experience (UX)/HMI | `4907652: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907653` | 4.11 User Experience (UX)/HMI | `4907653: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907654` | 4.11 User Experience (UX)/HMI | `4907654: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907655` | 4.11 User Experience (UX)/HMI | `4907655: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907656` | 4.11 User Experience (UX)/HMI | `4907656: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907657` | 4.11 User Experience (UX)/HMI | `4907657: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907658` | 4.11 User Experience (UX)/HMI | `4907658: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907659` | 4.11 User Experience (UX)/HMI | `4907659: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907660` | 4.11 User Experience (UX)/HMI | `4907660: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907661` | 4.11 User Experience (UX)/HMI | `4907661: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907662` | 4.11 User Experience (UX)/HMI | `4907662: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907663` | 4.11 User Experience (UX)/HMI | `4907663: [Artifact Type:Subsystem Functional Requirement]` 於「4.11 User Experience (UX)/HMI」下 |
| `4907665` | 4.12 Interrupt Handling | `4907665: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907666` | 4.12 Interrupt Handling | `4907666: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907667` | 4.12 Interrupt Handling | `4907667: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907668` | 4.12 Interrupt Handling | `4907668: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907669` | 4.12 Interrupt Handling | `4907669: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907670` | 4.12 Interrupt Handling | `4907670: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907671` | 4.12 Interrupt Handling | `4907671: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907672` | 4.12 Interrupt Handling | `4907672: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907673` | 4.12 Interrupt Handling | `4907673: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907676` | 4.12 Interrupt Handling | `4907676: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907677` | 4.12 Interrupt Handling | `4907677: [Artifact Type:Subsystem Functional Requirement]` 於「4.12 Interrupt Handling」下 |
| `4907679` | 4.12.1 Resuming a Download | `4907679: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.1 Resuming a Download」下 |
| `4907680` | 4.12.1 Resuming a Download | `4907680: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.1 Resuming a Download」下 |
| `4907681` | 4.12.1 Resuming a Download | `4907681: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.1 Resuming a Download」下 |
| `4907682` | 4.12.1 Resuming a Download | `4907682: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.1 Resuming a Download」下 |
| `4907683` | 4.12.1 Resuming a Download | `4907683: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.1 Resuming a Download」下 |
| `4907684` | 4.12.1 Resuming a Download | `4907684: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.1 Resuming a Download」下 |
| `4907686` | 4.12.2 Report Persistency | `4907686: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.2 Report Persistency」下 |
| `4907687` | 4.12.2 Report Persistency | `4907687: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.2 Report Persistency」下 |
| `4907688` | 4.12.2 Report Persistency | `4907688: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.2 Report Persistency」下 |
| `4907689` | 4.12.2 Report Persistency | `4907689: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.2 Report Persistency」下 |
| `4907690` | 4.12.2 Report Persistency | `4907690: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.2 Report Persistency」下 |
| `4907691` | 4.12.2 Report Persistency | `4907691: [Artifact Type:Subsystem Functional Requirement]` 於「4.12.2 Report Persistency」下 |
| `4907700` | 4.13.1 SCOMO Support | `4907700: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907701` | 4.13.1 SCOMO Support | `4907701: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907702` | 4.13.1 SCOMO Support | `4907702: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907703` | 4.13.1 SCOMO Support | `4907703: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907704` | 4.13.1 SCOMO Support | `4907704: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907705` | 4.13.1 SCOMO Support | `4907705: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907706` | 4.13.1 SCOMO Support | `4907706: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907707` | 4.13.1 SCOMO Support | `4907707: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.1 SCOMO Support」下 |
| `4907742` | 4.13.4 FCA Specific Tree structure (DDF) | `4907742: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.4 FCA Specific Tree structure (DDF)」下 |
| `4907744` | 4.13.4.1 Appendix A Download Descriptor Format | `4907744: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907765` | 4.13.4.2 Appendix B Configurable Parameters | `4907765: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.4.2 Appendix B Configurable Parameters」下 |
| `4907769` | 4.13.4.3 Appendix C OTA Commands | `4907769: [Artifact Type:Subsystem Functional Requirement]` 於「4.13.4.3 Appendix C OTA Commands」下 |
| `4907776` | 5 TBM FOTA Reflash Requirements | `4907776: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907777` | 5 TBM FOTA Reflash Requirements | `4907777: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907778` | 5 TBM FOTA Reflash Requirements | `4907778: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907779` | 5 TBM FOTA Reflash Requirements | `4907779: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907780` | 5 TBM FOTA Reflash Requirements | `4907780: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907781` | 5 TBM FOTA Reflash Requirements | `4907781: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907782` | 5 TBM FOTA Reflash Requirements | `4907782: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907783` | 5 TBM FOTA Reflash Requirements | `4907783: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907784` | 5 TBM FOTA Reflash Requirements | `4907784: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907785` | 5 TBM FOTA Reflash Requirements | `4907785: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907786` | 5 TBM FOTA Reflash Requirements | `4907786: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907787` | 5 TBM FOTA Reflash Requirements | `4907787: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907788` | 5 TBM FOTA Reflash Requirements | `4907788: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907789` | 5 TBM FOTA Reflash Requirements | `4907789: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907790` | 5 TBM FOTA Reflash Requirements | `4907790: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907791` | 5 TBM FOTA Reflash Requirements | `4907791: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907792` | 5 TBM FOTA Reflash Requirements | `4907792: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907793` | 5 TBM FOTA Reflash Requirements | `4907793: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907794` | 5 TBM FOTA Reflash Requirements | `4907794: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907795` | 5 TBM FOTA Reflash Requirements | `4907795: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907796` | 5 TBM FOTA Reflash Requirements | `4907796: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907797` | 5 TBM FOTA Reflash Requirements | `4907797: [Artifact Type:Subsystem Functional Requirement]` 於「5 TBM FOTA Reflash Requirements」下 |
| `4907801` | 6 TBM Algorithm Requirements | `4907801: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907802` | 6 TBM Algorithm Requirements | `4907802: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907803` | 6 TBM Algorithm Requirements | `4907803: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907804` | 6 TBM Algorithm Requirements | `4907804: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907805` | 6 TBM Algorithm Requirements | `4907805: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907806` | 6 TBM Algorithm Requirements | `4907806: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907807` | 6 TBM Algorithm Requirements | `4907807: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907808` | 6 TBM Algorithm Requirements | `4907808: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907809` | 6 TBM Algorithm Requirements | `4907809: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907810` | 6 TBM Algorithm Requirements | `4907810: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907811` | 6 TBM Algorithm Requirements | `4907811: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907812` | 6 TBM Algorithm Requirements | `4907812: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907813` | 6 TBM Algorithm Requirements | `4907813: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907814` | 6 TBM Algorithm Requirements | `4907814: [Artifact Type:Subsystem Functional Requirement]` 於「6 TBM Algorithm Requirements」下 |
| `4907816` | 1.1 Revision Notes | `4907816: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907817` | 7 Firmware Over-the-air Updates (FOTA) | `4907817: [Artifact Type:Subsystem Functional Requirement]` 於「7 Firmware Over-the-air Updates (FOTA)」下 |
| `4907818` | 7 Firmware Over-the-air Updates (FOTA) | `4907818: [Artifact Type:Subsystem Functional Requirement]` 於「7 Firmware Over-the-air Updates (FOTA)」下 |
| `4907819` | 7 Firmware Over-the-air Updates (FOTA) | `4907819: [Artifact Type:Subsystem Functional Requirement]` 於「7 Firmware Over-the-air Updates (FOTA)」下 |
| `4907820` | 7 Firmware Over-the-air Updates (FOTA) | `4907820: [Artifact Type:Subsystem Functional Requirement]` 於「7 Firmware Over-the-air Updates (FOTA)」下 |
| `4907821` | 7 Firmware Over-the-air Updates (FOTA) | `4907821: [Artifact Type:Subsystem Functional Requirement]` 於「7 Firmware Over-the-air Updates (FOTA)」下 |
| `4907822` | 7 Firmware Over-the-air Updates (FOTA) | `4907822: [Artifact Type:Subsystem Functional Requirement]` 於「7 Firmware Over-the-air Updates (FOTA)」下 |
| `4907823` | 7 Firmware Over-the-air Updates (FOTA) | `4907823: [Artifact Type:Subsystem Functional Requirement]` 於「7 Firmware Over-the-air Updates (FOTA)」下 |
| `4907825` | 7.1 Critical Updates | `4907825: [Artifact Type:Subsystem Functional Requirement]` 於「7.1 Critical Updates」下 |
| `4907826` | 7.1 Critical Updates | `4907826: [Artifact Type:Subsystem Functional Requirement]` 於「7.1 Critical Updates」下 |
| `4907827` | 7.1 Critical Updates | `4907827: [Artifact Type:Subsystem Functional Requirement]` 於「7.1 Critical Updates」下 |
| `4907828` | 7.1 Critical Updates | `4907828: [Artifact Type:Subsystem Functional Requirement]` 於「7.1 Critical Updates」下 |
| `4907829` | 7.1 Critical Updates | `4907829: [Artifact Type:Subsystem Functional Requirement]` 於「7.1 Critical Updates」下 |
| `4907830` | 1.1 Revision Notes | `4907830: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907831` | 7.1 Critical Updates | `4907831: [Artifact Type:Subsystem Functional Requirement]` 於「7.1 Critical Updates」下 |
| `4907832` | 1.1 Revision Notes | `4907832: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907837` | 8 Maps Over-the-air Updates (MOTA) | `4907837: [Artifact Type:Subsystem Functional Requirement]` 於「8 Maps Over-the-air Updates (MOTA)」下 |
| `4907838` | 8 Maps Over-the-air Updates (MOTA) | `4907838: [Artifact Type:Subsystem Functional Requirement]` 於「8 Maps Over-the-air Updates (MOTA)」下 |
| `4907839` | 1.1 Revision Notes | `4907839: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907841` | 8.1 Non-Critical Updates | `4907841: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907842` | 8.1 Non-Critical Updates | `4907842: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907843` | 8.1 Non-Critical Updates | `4907843: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907844` | 8.1 Non-Critical Updates | `4907844: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907845` | 8.1 Non-Critical Updates | `4907845: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907846` | 8.1 Non-Critical Updates | `4907846: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907847` | 8.1 Non-Critical Updates | `4907847: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907848` | 8.1 Non-Critical Updates | `4907848: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907849` | 8.1 Non-Critical Updates | `4907849: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907850` | 1.1 Revision Notes | `4907850: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907851` | 1.1 Revision Notes | `4907851: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907852` | 8.1 Non-Critical Updates | `4907852: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907853` | 8.1 Non-Critical Updates | `4907853: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907854` | 8.1 Non-Critical Updates | `4907854: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907855` | 8.1 Non-Critical Updates | `4907855: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907856` | 8.1 Non-Critical Updates | `4907856: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907857` | 8.1 Non-Critical Updates | `4907857: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907858` | 8.1 Non-Critical Updates | `4907858: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907859` | 8.1 Non-Critical Updates | `4907859: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907860` | 8.1 Non-Critical Updates | `4907860: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907861` | 8.1 Non-Critical Updates | `4907861: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907862` | 8.1 Non-Critical Updates | `4907862: [Artifact Type:Subsystem Functional Requirement]` 於「8.1 Non-Critical Updates」下 |
| `4907864` | 8.2 Route Planning Updates | `4907864: [Artifact Type:Subsystem Functional Requirement]` 於「8.2 Route Planning Updates」下 |
| `4907865` | 8.2 Route Planning Updates | `4907865: [Artifact Type:Subsystem Functional Requirement]` 於「8.2 Route Planning Updates」下 |
| `4907867` | 8.3 User Initiated Updates | `4907867: [Artifact Type:Subsystem Functional Requirement]` 於「8.3 User Initiated Updates」下 |
| `4907868` | 8.3 User Initiated Updates | `4907868: [Artifact Type:Subsystem Functional Requirement]` 於「8.3 User Initiated Updates」下 |
| `4907869` | 8.3 User Initiated Updates | `4907869: [Artifact Type:Subsystem Functional Requirement]` 於「8.3 User Initiated Updates」下 |
| `4907870` | 8.3 User Initiated Updates | `4907870: [Artifact Type:Subsystem Functional Requirement]` 於「8.3 User Initiated Updates」下 |
| `4907872` | 8.4 MOTA Client Initiated Updates | `4907872: [Artifact Type:Subsystem Functional Requirement]` 於「8.4 MOTA Client Initiated Updates」下 |
| `4907873` | 8.4 MOTA Client Initiated Updates | `4907873: [Artifact Type:Subsystem Functional Requirement]` 於「8.4 MOTA Client Initiated Updates」下 |
| `4907874` | 8.4 MOTA Client Initiated Updates | `4907874: [Artifact Type:Subsystem Functional Requirement]` 於「8.4 MOTA Client Initiated Updates」下 |
| `4907875` | 8.4 MOTA Client Initiated Updates | `4907875: [Artifact Type:Subsystem Functional Requirement]` 於「8.4 MOTA Client Initiated Updates」下 |
| `4907876` | 8.4 MOTA Client Initiated Updates | `4907876: [Artifact Type:Subsystem Functional Requirement]` 於「8.4 MOTA Client Initiated Updates」下 |
| `4907877` | 8.4 MOTA Client Initiated Updates | `4907877: [Artifact Type:Subsystem Functional Requirement]` 於「8.4 MOTA Client Initiated Updates」下 |
| `4907880` | 9.1 Pre-Installation | `4907880: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907881` | 9.1 Pre-Installation | `4907881: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907882` | 9.1 Pre-Installation | `4907882: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907883` | 9.1 Pre-Installation | `4907883: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907884` | 9.1 Pre-Installation | `4907884: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907885` | 9.1 Pre-Installation | `4907885: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907886` | 9.1 Pre-Installation | `4907886: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907887` | 9.1 Pre-Installation | `4907887: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907888` | 9.1 Pre-Installation | `4907888: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907889` | 9.1 Pre-Installation | `4907889: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907890` | 9.1 Pre-Installation | `4907890: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907891` | 9.1 Pre-Installation | `4907891: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907892` | 9.1 Pre-Installation | `4907892: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907894` | 9.1 Pre-Installation | `4907894: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907895` | 9.1 Pre-Installation | `4907895: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907896` | 9.1 Pre-Installation | `4907896: [Artifact Type:Subsystem Functional Requirement]` 於「9.1 Pre-Installation」下 |
| `4907898` | 9.2 Installation Progress | `4907898: [Artifact Type:Subsystem Functional Requirement]` 於「9.2 Installation Progress」下 |
| `4907899` | 9.2 Installation Progress | `4907899: [Artifact Type:Subsystem Functional Requirement]` 於「9.2 Installation Progress」下 |
| `4907900` | 9.2 Installation Progress | `4907900: [Artifact Type:Subsystem Functional Requirement]` 於「9.2 Installation Progress」下 |
| `4907901` | 9.2 Installation Progress | `4907901: [Artifact Type:Subsystem Functional Requirement]` 於「9.2 Installation Progress」下 |
| `4907902` | 9.2 Installation Progress | `4907902: [Artifact Type:Subsystem Functional Requirement]` 於「9.2 Installation Progress」下 |
| `4907903` | 9.2 Installation Progress | `4907903: [Artifact Type:Subsystem Functional Requirement]` 於「9.2 Installation Progress」下 |
| `4907904` | 9.2 Installation Progress | `4907904: [Artifact Type:Subsystem Functional Requirement]` 於「9.2 Installation Progress」下 |
| `4907906` | 9.3 Post-Installation | `4907906: [Artifact Type:Subsystem Functional Requirement]` 於「9.3 Post-Installation」下 |
| `4907907` | 1.1 Revision Notes | `4907907: [Artifact Type:Subsystem Functional Requirement]` 於「1.1 Revision Notes」下 |
| `4907908` | 9.3 Post-Installation | `4907908: [Artifact Type:Subsystem Functional Requirement]` 於「9.3 Post-Installation」下 |
| `4907909` | 9.3 Post-Installation | `4907909: [Artifact Type:Subsystem Functional Requirement]` 於「9.3 Post-Installation」下 |
| `4907910` | 9.3 Post-Installation | `4907910: [Artifact Type:Subsystem Functional Requirement]` 於「9.3 Post-Installation」下 |
| `4907913` | 9.4.1 Pre-Installation | `4907913: [Artifact Type:Subsystem Functional Requirement]` 於「9.4.1 Pre-Installation」下 |
| `4907914` | 9.4.1 Pre-Installation | `4907914: [Artifact Type:Subsystem Functional Requirement]` 於「9.4.1 Pre-Installation」下 |
| `4907915` | 9.4.1 Pre-Installation | `4907915: [Artifact Type:Subsystem Functional Requirement]` 於「9.4.1 Pre-Installation」下 |

## 四、Description 物件（137）

| ObjectID | 所屬章節 | 驗證脈絡 |
|---|---|---|
| `4907234` | 1.2 Introduction | `4907234: [Artifact Type:Description]` 於「1.2 Introduction」下 |
| `4907235` | 1.2 Introduction | `4907235: [Artifact Type:Description]` 於「1.2 Introduction」下 |
| `4907236` | 1.2 Introduction | `4907236: [Artifact Type:Description]` 於「1.2 Introduction」下 |
| `4907237` | 1.2 Introduction | `4907237: [Artifact Type:Description]` 於「1.2 Introduction」下 |
| `4907238` | 1.2 Introduction | `4907238: [Artifact Type:Description]` 於「1.2 Introduction」下 |
| `4907239` | 1.2 Introduction | `4907239: [Artifact Type:Description]` 於「1.2 Introduction」下 |
| `4907240` | 1.2 Introduction | `4907240: [Artifact Type:Description]` 於「1.2 Introduction」下 |
| `4907242` | 2 Common Reflash Requirements | `4907242: [Artifact Type:Description]` 於「2 Common Reflash Requirements」下 |
| `4907260` | 3 Media Reflash Requirements | `4907260: [Artifact Type:Description]` 於「3 Media Reflash Requirements」下 |
| `4907262` | 4 FOTA Reflash Requirements | `4907262: [Artifact Type:Description]` 於「4 FOTA Reflash Requirements」下 |
| `4907263` | 4 FOTA Reflash Requirements | `4907263: [Artifact Type:Description]` 於「4 FOTA Reflash Requirements」下 |
| `4907264` | 4 FOTA Reflash Requirements | `4907264: [Artifact Type:Description]` 於「4 FOTA Reflash Requirements」下 |
| `4907265` | 4 FOTA Reflash Requirements | `4907265: [Artifact Type:Description]` 於「4 FOTA Reflash Requirements」下 |
| `4907266` | 4 FOTA Reflash Requirements | `4907266: [Artifact Type:Description]` 於「4 FOTA Reflash Requirements」下 |
| `4907268` | 4.1 This Document | `4907268: [Artifact Type:Description]` 於「4.1 This Document」下 |
| `4907270` | 4.1.1 Related Documents and Specifications | `4907270: [Artifact Type:Description]` 於「4.1.1 Related Documents and Specifications」下 |
| `4907271` | 4.1.1 Related Documents and Specifications | `4907271: [Artifact Type:Description]` 於「4.1.1 Related Documents and Specifications」下 |
| `4907274` | 4.2.1 Over The Air (OTA) Deployment of Software | `4907274: [Artifact Type:Description]` 於「4.2.1 Over The Air (OTA) Deployment of Software」下 |
| `4907276` | 4.2.2 Local Deployment of Software | `4907276: [Artifact Type:Description]` 於「4.2.2 Local Deployment of Software」下 |
| `4907283` | 4.2.4 Software Configuration Reporting | `4907283: [Artifact Type:Description]` 於「4.2.4 Software Configuration Reporting」下 |
| `4907285` | 4.3 High Level FOTA Diagram | `4907285: [Artifact Type:Description]` 於「4.3 High Level FOTA Diagram」下 |
| `4907286` | 4.3 High Level FOTA Diagram | `4907286: [Artifact Type:Description]` 於「4.3 High Level FOTA Diagram」下 |
| `4907288` | 4.4 OTA Client Architecture | `4907288: [Artifact Type:Description]` 於「4.4 OTA Client Architecture」下 |
| `4907289` | 4.4 OTA Client Architecture | `4907289: [Artifact Type:Description]` 於「4.4 OTA Client Architecture」下 |
| `4907290` | 4.4 OTA Client Architecture | `4907290: [Artifact Type:Description]` 於「4.4 OTA Client Architecture」下 |
| `4907318` | 4.4.1 OTA Architecture Requirements | `4907318: [Artifact Type:Description]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907319` | 4.4.1 OTA Architecture Requirements | `4907319: [Artifact Type:Description]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907324` | 4.4.1 OTA Architecture Requirements | `4907324: [Artifact Type:Description]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907325` | 4.4.1 OTA Architecture Requirements | `4907325: [Artifact Type:Description]` 於「4.4.1 OTA Architecture Requirements」下 |
| `4907356` | 4.5.1 OTA Communication Protocols | `4907356: [Artifact Type:Description]` 於「4.5.1 OTA Communication Protocols」下 |
| `4907357` | 4.5.1 OTA Communication Protocols | `4907357: [Artifact Type:Description]` 於「4.5.1 OTA Communication Protocols」下 |
| `4907363` | 4.5.3 Vehicle initiated sessions | `4907363: [Artifact Type:Description]` 於「4.5.3 Vehicle initiated sessions」下 |
| `4907383` | 4.5.5 Bus communications | `4907383: [Artifact Type:Description]` 於「4.5.5 Bus communications」下 |
| `4907384` | 4.5.5 Bus communications | `4907384: [Artifact Type:Description]` 於「4.5.5 Bus communications」下 |
| `4907390` | 4.5.5 Bus communications | `4907390: [Artifact Type:Description]` 於「4.5.5 Bus communications」下 |
| `4907391` | 4.5.5 Bus communications | `4907391: [Artifact Type:Description]` 於「4.5.5 Bus communications」下 |
| `4907445` | 4.7.2 OTA client Flows | `4907445: [Artifact Type:Description]` 於「4.7.2 OTA client Flows」下 |
| `4907446` | 4.7.2 OTA client Flows | `4907446: [Artifact Type:Description]` 於「4.7.2 OTA client Flows」下 |
| `4907511` | 4.8.2 OMA-DM Security | `4907511: [Artifact Type:Description]` 於「4.8.2 OMA-DM Security」下 |
| `4907540` | 4.9.1 Update Agent Requirements | `4907540: [Artifact Type:Description]` 於「4.9.1 Update Agent Requirements」下 |
| `4907541` | 4.9.1 Update Agent Requirements | `4907541: [Artifact Type:Description]` 於「4.9.1 Update Agent Requirements」下 |
| `4907543` | 4.9.2 ECU Module specific considerations | `4907543: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907544` | 4.9.2 ECU Module specific considerations | `4907544: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907545` | 4.9.2 ECU Module specific considerations | `4907545: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907546` | 4.9.2 ECU Module specific considerations | `4907546: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907547` | 4.9.2 ECU Module specific considerations | `4907547: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907548` | 4.9.2 ECU Module specific considerations | `4907548: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907549` | 4.9.2 ECU Module specific considerations | `4907549: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907550` | 4.9.2 ECU Module specific considerations | `4907550: [Artifact Type:Description]` 於「4.9.2 ECU Module specific considerations」下 |
| `4907637` | 4.10.5.1 Installation and Download Conditions | `4907637: [Artifact Type:Description]` 於「4.10.5.1 Installation and Download Conditions」下 |
| `4907674` | 4.12 Interrupt Handling | `4907674: [Artifact Type:Description]` 於「4.12 Interrupt Handling」下 |
| `4907675` | 4.12 Interrupt Handling | `4907675: [Artifact Type:Description]` 於「4.12 Interrupt Handling」下 |
| `4907694` | 4.13.1 SCOMO Support | `4907694: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907695` | 4.13.1 SCOMO Support | `4907695: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907696` | 4.13.1 SCOMO Support | `4907696: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907697` | 4.13.1 SCOMO Support | `4907697: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907698` | 4.13.1 SCOMO Support | `4907698: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907699` | 4.13.1 SCOMO Support | `4907699: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907708` | 4.13.1 SCOMO Support | `4907708: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907709` | 4.13.1 SCOMO Support | `4907709: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907710` | 4.13.1 SCOMO Support | `4907710: [Artifact Type:Description]` 於「4.13.1 SCOMO Support」下 |
| `4907712` | 4.13.2 LAWMO Support | `4907712: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907713` | 4.13.2 LAWMO Support | `4907713: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907714` | 4.13.2 LAWMO Support | `4907714: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907715` | 4.13.2 LAWMO Support | `4907715: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907716` | 4.13.2 LAWMO Support | `4907716: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907717` | 4.13.2 LAWMO Support | `4907717: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907718` | 4.13.2 LAWMO Support | `4907718: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907719` | 4.13.2 LAWMO Support | `4907719: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907720` | 4.13.2 LAWMO Support | `4907720: [Artifact Type:Description]` 於「4.13.2 LAWMO Support」下 |
| `4907722` | 4.13.2.1 Lock | `4907722: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907723` | 4.13.2.1 Lock | `4907723: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907724` | 4.13.2.1 Lock | `4907724: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907725` | 4.13.2.1 Lock | `4907725: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907726` | 4.13.2.1 Lock | `4907726: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907727` | 4.13.2.1 Lock | `4907727: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907728` | 4.13.2.1 Lock | `4907728: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907729` | 4.13.2.1 Lock | `4907729: [Artifact Type:Description]` 於「4.13.2.1 Lock」下 |
| `4907731` | 4.13.2.2 Unlock | `4907731: [Artifact Type:Description]` 於「4.13.2.2 Unlock」下 |
| `4907732` | 4.13.2.2 Unlock | `4907732: [Artifact Type:Description]` 於「4.13.2.2 Unlock」下 |
| `4907733` | 4.13.2.2 Unlock | `4907733: [Artifact Type:Description]` 於「4.13.2.2 Unlock」下 |
| `4907735` | 4.13.2.3 Wipe Data | `4907735: [Artifact Type:Description]` 於「4.13.2.3 Wipe Data」下 |
| `4907736` | 4.13.2.3 Wipe Data | `4907736: [Artifact Type:Description]` 於「4.13.2.3 Wipe Data」下 |
| `4907737` | 4.13.2.3 Wipe Data | `4907737: [Artifact Type:Description]` 於「4.13.2.3 Wipe Data」下 |
| `4907739` | 4.13.3 Additional Support Objects | `4907739: [Artifact Type:Description]` 於「4.13.3 Additional Support Objects」下 |
| `4907740` | 4.13.3 Additional Support Objects | `4907740: [Artifact Type:Description]` 於「4.13.3 Additional Support Objects」下 |
| `4907745` | 4.13.4.1 Appendix A Download Descriptor Format | `4907745: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907746` | 4.13.4.1 Appendix A Download Descriptor Format | `4907746: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907747` | 4.13.4.1 Appendix A Download Descriptor Format | `4907747: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907748` | 4.13.4.1 Appendix A Download Descriptor Format | `4907748: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907749` | 4.13.4.1 Appendix A Download Descriptor Format | `4907749: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907750` | 4.13.4.1 Appendix A Download Descriptor Format | `4907750: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907751` | 4.13.4.1 Appendix A Download Descriptor Format | `4907751: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907752` | 4.13.4.1 Appendix A Download Descriptor Format | `4907752: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907753` | 4.13.4.1 Appendix A Download Descriptor Format | `4907753: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907754` | 4.13.4.1 Appendix A Download Descriptor Format | `4907754: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907755` | 4.13.4.1 Appendix A Download Descriptor Format | `4907755: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907756` | 4.13.4.1 Appendix A Download Descriptor Format | `4907756: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907757` | 4.13.4.1 Appendix A Download Descriptor Format | `4907757: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907758` | 4.13.4.1 Appendix A Download Descriptor Format | `4907758: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907759` | 4.13.4.1 Appendix A Download Descriptor Format | `4907759: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907760` | 4.13.4.1 Appendix A Download Descriptor Format | `4907760: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907761` | 4.13.4.1 Appendix A Download Descriptor Format | `4907761: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907762` | 4.13.4.1 Appendix A Download Descriptor Format | `4907762: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907763` | 4.13.4.1 Appendix A Download Descriptor Format | `4907763: [Artifact Type:Description]` 於「4.13.4.1 Appendix A Download Descriptor Format」下 |
| `4907766` | 4.13.4.2 Appendix B Configurable Parameters | `4907766: [Artifact Type:Description]` 於「4.13.4.2 Appendix B Configurable Parameters」下 |
| `4907767` | 4.13.4.2 Appendix B Configurable Parameters | `4907767: [Artifact Type:Description]` 於「4.13.4.2 Appendix B Configurable Parameters」下 |
| `4907770` | 4.13.4.3 Appendix C OTA Commands | `4907770: [Artifact Type:Description]` 於「4.13.4.3 Appendix C OTA Commands」下 |
| `4907771` | 4.13.4.3 Appendix C OTA Commands | `4907771: [Artifact Type:Description]` 於「4.13.4.3 Appendix C OTA Commands」下 |
| `4907773` | 4.13.4.4 Appendix D Terms and Abbreviations | `4907773: [Artifact Type:Description]` 於「4.13.4.4 Appendix D Terms and Abbreviations」下 |
| `4907774` | 4.13.4.4 Appendix D Terms and Abbreviations | `4907774: [Artifact Type:Description]` 於「4.13.4.4 Appendix D Terms and Abbreviations」下 |
| `4907799` | 6 TBM Algorithm Requirements | `4907799: [Artifact Type:Description]` 於「6 TBM Algorithm Requirements」下 |
| `4907800` | 6 TBM Algorithm Requirements | `4907800: [Artifact Type:Description]` 於「6 TBM Algorithm Requirements」下 |
| `4907834` | 8 Maps Over-the-air Updates (MOTA) | `4907834: [Artifact Type:Description]` 於「8 Maps Over-the-air Updates (MOTA)」下 |
| `4907835` | 8 Maps Over-the-air Updates (MOTA) | `4907835: [Artifact Type:Description]` 於「8 Maps Over-the-air Updates (MOTA)」下 |
| `4907836` | 8 Maps Over-the-air Updates (MOTA) | `4907836: [Artifact Type:Description]` 於「8 Maps Over-the-air Updates (MOTA)」下 |
| `4907893` | 9.1 Pre-Installation | `4907893: [Artifact Type:Description]` 於「9.1 Pre-Installation」下 |
| `4907918` | 10.1 Shipping/Logistic mode | `4907918: [Artifact Type:Description]` 於「10.1 Shipping/Logistic mode」下 |
| `4907920` | 10.2 Wi-Fi | `4907920: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907921` | 10.2 Wi-Fi | `4907921: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907922` | 10.2 Wi-Fi | `4907922: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907923` | — | 章節物件 | 10.2 | **A-SU5 更正**：原表誤歸宿主 `4907907`（T12 游標被文件前置之 `Requirement ID nnn` 清單移動）；以宣告段位置定歸屬應為章節級 |
| `4907924` | 10.2 Wi-Fi | `4907924: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907925` | 10.2 Wi-Fi | `4907925: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907926` | 10.2 Wi-Fi | `4907926: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907927` | 10.2 Wi-Fi | `4907927: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907928` | 10.2 Wi-Fi | `4907928: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907929` | 10.2 Wi-Fi | `4907929: [Artifact Type:Description]` 於「10.2 Wi-Fi」下 |
| `4907931` | 10.3 Installation | `4907931: [Artifact Type:Description]` 於「10.3 Installation」下 |
| `4907932` | 10.3 Installation | `4907932: [Artifact Type:Description]` 於「10.3 Installation」下 |
| `4907933` | 10.3 Installation | `4907933: [Artifact Type:Description]` 於「10.3 Installation」下 |
| `4907934` | — | 章節物件 | 10.3 | **A-SU5 更正**：原表誤歸宿主 `4907907`（T12 游標被文件前置之 `Requirement ID nnn` 清單移動）；以宣告段位置定歸屬應為章節級 |
| `4907936` | 10.4 Post-Installation | `4907936: [Artifact Type:Description]` 於「10.4 Post-Installation」下 |
| `4907937` | 10.4 Post-Installation | `4907937: [Artifact Type:Description]` 於「10.4 Post-Installation」下 |
| `4907939` | 10.5 Security (Hopefully remove and reference to Rej | `4907939: [Artifact Type:Description]` 於「10.5 Security (Hopefully remove and reference to Rejani/Ansaf spec)」下 |
| `4907940` | 10.5 Security (Hopefully remove and reference to Rej | `4907940: [Artifact Type:Description]` 於「10.5 Security (Hopefully remove and reference to Rejani/Ansaf spec)」下 |
| `5423873` | 1.1 Revision Notes | `5423873: [Artifact Type:Description]` 於「1.1 Revision Notes」下 |

## 五、不可歸類（10）

| ObjectID | 所屬章節 | 驗證脈絡 |
|---|---|---|
| `1234567` | 4.13.4.1 Appendix A Download Descriptor Format | 內文散見：`…&lt;size&gt;1234567&lt;/size&gt;…` |
| `3369439` | 1.1 Revision Notes | 內文散見：`…WS3369439…` |
| `3440351` | 1.1 Revision Notes | 內文散見：`…WS3440351…` |
| `4615844` | 4.5.5 Bus communications | 圖檔名：`4615844- CFTSMV057_CIP_R1_O3485_91_inline.rtf` |
| `4615845` | 4.4 OTA Client Architecture | 圖檔名：`4615845- CFTSMV057_CIP_R1_O3486_90_inline.rtf` |
| `4615846` | 4.3 High Level FOTA Diagram | 圖檔名：`4615846- CFTSMV057_CIP_R1_O3487_88_inline.rtf` |
| `4615847` | 7 Firmware Over-the-air Updates (FOTA) | 圖檔名：`4615847- CFTSMV057_CIP_R1_O3579_92_inline.rtf` |
| `4615848` | 4.3 High Level FOTA Diagram | 圖檔名：`4615848- CFTSMV057_CIP_R1_O3714_89_inline.rtf` |
| `4762830` | 4.6 OTA download via Wi-Fi | 內文散見：`…rement Kindly see section ID4762830 : Wi-Fi Client Mode Connect…` |
| `4915105` | 9.3 Post-Installation | 內文交叉引用：…vior defined in Requirement ID 4915105… |


## 六、Description 物件 → 所屬物件對照（T12，R-SU7 配套）

R-SU7 裁定 Description 物件不入池；其內容被取用時錨落**所屬之需求／章節物件**。

判定法：依文件序維持「當前章節物件」與「當前需求物件」兩游標；遇 heading
style `1`–`4` 即更新章節游標並**清空需求游標**（跨章不繼承）。Description
歸於同章節內其前方最近之需求物件；該章尚未出現需求物件者，歸該章節物件。

偽陽性風險揭露（R-G8）：本法以**文件序鄰接**為依據，非 Polarion 之 parent
欄位 —— 該欄未出現於本 docx 之任何 XML part（已查 `word/*.xml` 全部七份）。
表格內之 Description 若其宿主需求排在表格之後會被誤歸前一需求；已以
「跨章清空游標」限制誤差不越章。取用前仍應以下表「判定脈絡」欄覆核。

| 統計 | 數 |
|---|---:|
| Description 物件總數 | 137 |
| 歸需求物件 | **43** ⚠A-SU5 更正（原 45） |
| 歸章節物件 | **94** ⚠A-SU5 更正（原 92） |
| **不可解** | **0** |

| Description ID | 所屬物件 | 上位型 | 所屬章節 | 判定脈絡 |
|---|---|---|---|---|
| `4907234` | `4907233` | 章節物件 | 1.2 Introduction | 章節「1.2 Introduction」下、該章第一個需求物件之前 |
| `4907235` | `4907233` | 章節物件 | 1.2 Introduction | 章節「1.2 Introduction」下、該章第一個需求物件之前 |
| `4907236` | `4907233` | 章節物件 | 1.2 Introduction | 章節「1.2 Introduction」下、該章第一個需求物件之前 |
| `4907237` | `4907233` | 章節物件 | 1.2 Introduction | 章節「1.2 Introduction」下、該章第一個需求物件之前 |
| `4907238` | `4907233` | 章節物件 | 1.2 Introduction | 章節「1.2 Introduction」下、該章第一個需求物件之前 |
| `4907239` | `4907233` | 章節物件 | 1.2 Introduction | 章節「1.2 Introduction」下、該章第一個需求物件之前 |
| `4907240` | `4907233` | 章節物件 | 1.2 Introduction | 章節「1.2 Introduction」下、該章第一個需求物件之前 |
| `4907242` | `4907241` | 章節物件 | 2 Common Reflash Requirements | 章節「2 Common Reflash Requirements」下、該章第一個需求物件之前 |
| `4907260` | `4907259` | 章節物件 | 3 Media Reflash Requirements | 章節「3 Media Reflash Requirements」下、該章第一個需求物件之前 |
| `4907262` | `4907261` | 章節物件 | 4 FOTA Reflash Requirements | 章節「4 FOTA Reflash Requirements」下、該章第一個需求物件之前 |
| `4907263` | `4907261` | 章節物件 | 4 FOTA Reflash Requirements | 章節「4 FOTA Reflash Requirements」下、該章第一個需求物件之前 |
| `4907264` | `4907261` | 章節物件 | 4 FOTA Reflash Requirements | 章節「4 FOTA Reflash Requirements」下、該章第一個需求物件之前 |
| `4907265` | `4907261` | 章節物件 | 4 FOTA Reflash Requirements | 章節「4 FOTA Reflash Requirements」下、該章第一個需求物件之前 |
| `4907266` | `4907261` | 章節物件 | 4 FOTA Reflash Requirements | 章節「4 FOTA Reflash Requirements」下、該章第一個需求物件之前 |
| `4907268` | `4907267` | 章節物件 | 4.1 This Document | 章節「4.1 This Document」下、該章第一個需求物件之前 |
| `4907270` | `4907269` | 章節物件 | 4.1.1 Related Documents and Specifications | 章節「4.1.1 Related Documents and Specifications」下、該章第一個需求物件之前 |
| `4907271` | `4907269` | 章節物件 | 4.1.1 Related Documents and Specifications | 章節「4.1.1 Related Documents and Specifications」下、該章第一個需求物件之前 |
| `4907274` | `4907273` | 章節物件 | 4.2.1 Over The Air (OTA) Deployment of Softw | 章節「4.2.1 Over The Air (OTA) Deployment of Software」下、該章第一個需求物件之前 |
| `4907276` | `4907275` | 章節物件 | 4.2.2 Local Deployment of Software | 章節「4.2.2 Local Deployment of Software」下、該章第一個需求物件之前 |
| `4907283` | `4907282` | 章節物件 | 4.2.4 Software Configuration Reporting | 章節「4.2.4 Software Configuration Reporting」下、該章第一個需求物件之前 |
| `4907285` | `4907284` | 章節物件 | 4.3 High Level FOTA Diagram | 章節「4.3 High Level FOTA Diagram」下、該章第一個需求物件之前 |
| `4907286` | `4907284` | 章節物件 | 4.3 High Level FOTA Diagram | 章節「4.3 High Level FOTA Diagram」下、該章第一個需求物件之前 |
| `4907288` | `4907287` | 章節物件 | 4.4 OTA Client Architecture | 章節「4.4 OTA Client Architecture」下、該章第一個需求物件之前 |
| `4907289` | `4907287` | 章節物件 | 4.4 OTA Client Architecture | 章節「4.4 OTA Client Architecture」下、該章第一個需求物件之前 |
| `4907290` | `4907287` | 章節物件 | 4.4 OTA Client Architecture | 章節「4.4 OTA Client Architecture」下、該章第一個需求物件之前 |
| `4907318` | `4907317` | 需求物件 | 4.4.1 OTA Architecture Requirements | 同章節「4.4.1 OTA Architecture Requirements」內，緊接於需求物件 `4907317` 之後 |
| `4907319` | `4907317` | 需求物件 | 4.4.1 OTA Architecture Requirements | 同章節「4.4.1 OTA Architecture Requirements」內，緊接於需求物件 `4907317` 之後 |
| `4907324` | `4907323` | 需求物件 | 4.4.1 OTA Architecture Requirements | 同章節「4.4.1 OTA Architecture Requirements」內，緊接於需求物件 `4907323` 之後 |
| `4907325` | `4907323` | 需求物件 | 4.4.1 OTA Architecture Requirements | 同章節「4.4.1 OTA Architecture Requirements」內，緊接於需求物件 `4907323` 之後 |
| `4907356` | `4907355` | 需求物件 | 4.5.1 OTA Communication Protocols | 同章節「4.5.1 OTA Communication Protocols」內，緊接於需求物件 `4907355` 之後 |
| `4907357` | `4907355` | 需求物件 | 4.5.1 OTA Communication Protocols | 同章節「4.5.1 OTA Communication Protocols」內，緊接於需求物件 `4907355` 之後 |
| `4907363` | `4907362` | 章節物件 | 4.5.3 Vehicle initiated sessions | 章節「4.5.3 Vehicle initiated sessions」下、該章第一個需求物件之前 |
| `4907383` | `4907382` | 章節物件 | 4.5.5 Bus communications | 章節「4.5.5 Bus communications」下、該章第一個需求物件之前 |
| `4907384` | `4907382` | 章節物件 | 4.5.5 Bus communications | 章節「4.5.5 Bus communications」下、該章第一個需求物件之前 |
| `4907390` | `4907389` | 需求物件 | 4.5.5 Bus communications | 同章節「4.5.5 Bus communications」內，緊接於需求物件 `4907389` 之後 |
| `4907391` | `4907389` | 需求物件 | 4.5.5 Bus communications | 同章節「4.5.5 Bus communications」內，緊接於需求物件 `4907389` 之後 |
| `4907445` | `4907444` | 需求物件 | 4.7.2 OTA client Flows | 同章節「4.7.2 OTA client Flows」內，緊接於需求物件 `4907444` 之後 |
| `4907446` | `4907444` | 需求物件 | 4.7.2 OTA client Flows | 同章節「4.7.2 OTA client Flows」內，緊接於需求物件 `4907444` 之後 |
| `4907511` | `4907510` | 需求物件 | 4.8.2 OMA-DM Security | 同章節「4.8.2 OMA-DM Security」內，緊接於需求物件 `4907510` 之後 |
| `4907540` | `4907539` | 需求物件 | 4.9.1 Update Agent Requirements | 同章節「4.9.1 Update Agent Requirements」內，緊接於需求物件 `4907539` 之後 |
| `4907541` | `4907539` | 需求物件 | 4.9.1 Update Agent Requirements | 同章節「4.9.1 Update Agent Requirements」內，緊接於需求物件 `4907539` 之後 |
| `4907543` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907544` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907545` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907546` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907547` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907548` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907549` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907550` | `4907542` | 章節物件 | 4.9.2 ECU Module specific considerations | 章節「4.9.2 ECU Module specific considerations」下、該章第一個需求物件之前 |
| `4907637` | `4907636` | 需求物件 | 4.10.5.1 Installation and Download Condition | 同章節「4.10.5.1 Installation and Download Conditions」內，緊接於需求物件 `4907636` 之後 |
| `4907674` | `4907673` | 需求物件 | 4.12 Interrupt Handling | 同章節「4.12 Interrupt Handling」內，緊接於需求物件 `4907673` 之後 |
| `4907675` | `4907673` | 需求物件 | 4.12 Interrupt Handling | 同章節「4.12 Interrupt Handling」內，緊接於需求物件 `4907673` 之後 |
| `4907694` | `4907693` | 章節物件 | 4.13.1 SCOMO Support | 章節「4.13.1 SCOMO Support」下、該章第一個需求物件之前 |
| `4907695` | `4907693` | 章節物件 | 4.13.1 SCOMO Support | 章節「4.13.1 SCOMO Support」下、該章第一個需求物件之前 |
| `4907696` | `4907693` | 章節物件 | 4.13.1 SCOMO Support | 章節「4.13.1 SCOMO Support」下、該章第一個需求物件之前 |
| `4907697` | `4907693` | 章節物件 | 4.13.1 SCOMO Support | 章節「4.13.1 SCOMO Support」下、該章第一個需求物件之前 |
| `4907698` | `4907693` | 章節物件 | 4.13.1 SCOMO Support | 章節「4.13.1 SCOMO Support」下、該章第一個需求物件之前 |
| `4907699` | `4907693` | 章節物件 | 4.13.1 SCOMO Support | 章節「4.13.1 SCOMO Support」下、該章第一個需求物件之前 |
| `4907708` | `4907707` | 需求物件 | 4.13.1 SCOMO Support | 同章節「4.13.1 SCOMO Support」內，緊接於需求物件 `4907707` 之後 |
| `4907709` | `4907707` | 需求物件 | 4.13.1 SCOMO Support | 同章節「4.13.1 SCOMO Support」內，緊接於需求物件 `4907707` 之後 |
| `4907710` | `4907707` | 需求物件 | 4.13.1 SCOMO Support | 同章節「4.13.1 SCOMO Support」內，緊接於需求物件 `4907707` 之後 |
| `4907712` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907713` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907714` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907715` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907716` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907717` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907718` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907719` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907720` | `4907711` | 章節物件 | 4.13.2 LAWMO Support | 章節「4.13.2 LAWMO Support」下、該章第一個需求物件之前 |
| `4907722` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907723` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907724` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907725` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907726` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907727` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907728` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907729` | `4907721` | 章節物件 | 4.13.2.1 Lock | 章節「4.13.2.1 Lock」下、該章第一個需求物件之前 |
| `4907731` | `4907730` | 章節物件 | 4.13.2.2 Unlock | 章節「4.13.2.2 Unlock」下、該章第一個需求物件之前 |
| `4907732` | `4907730` | 章節物件 | 4.13.2.2 Unlock | 章節「4.13.2.2 Unlock」下、該章第一個需求物件之前 |
| `4907733` | `4907730` | 章節物件 | 4.13.2.2 Unlock | 章節「4.13.2.2 Unlock」下、該章第一個需求物件之前 |
| `4907735` | `4907734` | 章節物件 | 4.13.2.3 Wipe Data | 章節「4.13.2.3 Wipe Data」下、該章第一個需求物件之前 |
| `4907736` | `4907734` | 章節物件 | 4.13.2.3 Wipe Data | 章節「4.13.2.3 Wipe Data」下、該章第一個需求物件之前 |
| `4907737` | `4907734` | 章節物件 | 4.13.2.3 Wipe Data | 章節「4.13.2.3 Wipe Data」下、該章第一個需求物件之前 |
| `4907739` | `4907738` | 章節物件 | 4.13.3 Additional Support Objects | 章節「4.13.3 Additional Support Objects」下、該章第一個需求物件之前 |
| `4907740` | `4907738` | 章節物件 | 4.13.3 Additional Support Objects | 章節「4.13.3 Additional Support Objects」下、該章第一個需求物件之前 |
| `4907745` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907746` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907747` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907748` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907749` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907750` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907751` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907752` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907753` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907754` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907755` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907756` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907757` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907758` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907759` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907760` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907761` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907762` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907763` | `4907744` | 需求物件 | 4.13.4.1 Appendix A Download Descriptor Form | 同章節「4.13.4.1 Appendix A Download Descriptor Format」內，緊接於需求物件 `4907744` 之後 |
| `4907766` | `4907765` | 需求物件 | 4.13.4.2 Appendix B Configurable Parameters | 同章節「4.13.4.2 Appendix B Configurable Parameters」內，緊接於需求物件 `4907765` 之後 |
| `4907767` | `4907765` | 需求物件 | 4.13.4.2 Appendix B Configurable Parameters | 同章節「4.13.4.2 Appendix B Configurable Parameters」內，緊接於需求物件 `4907765` 之後 |
| `4907770` | `4907769` | 需求物件 | 4.13.4.3 Appendix C OTA Commands | 同章節「4.13.4.3 Appendix C OTA Commands」內，緊接於需求物件 `4907769` 之後 |
| `4907771` | `4907769` | 需求物件 | 4.13.4.3 Appendix C OTA Commands | 同章節「4.13.4.3 Appendix C OTA Commands」內，緊接於需求物件 `4907769` 之後 |
| `4907773` | `4907772` | 章節物件 | 4.13.4.4 Appendix D Terms and Abbreviations | 章節「4.13.4.4 Appendix D Terms and Abbreviations」下、該章第一個需求物件之前 |
| `4907774` | `4907772` | 章節物件 | 4.13.4.4 Appendix D Terms and Abbreviations | 章節「4.13.4.4 Appendix D Terms and Abbreviations」下、該章第一個需求物件之前 |
| `4907799` | `4907798` | 章節物件 | 6 TBM Algorithm Requirements | 章節「6 TBM Algorithm Requirements」下、該章第一個需求物件之前 |
| `4907800` | `4907798` | 章節物件 | 6 TBM Algorithm Requirements | 章節「6 TBM Algorithm Requirements」下、該章第一個需求物件之前 |
| `4907834` | `4907833` | 章節物件 | 8 Maps Over-the-air Updates (MOTA) | 章節「8 Maps Over-the-air Updates (MOTA)」下、該章第一個需求物件之前 |
| `4907835` | `4907833` | 章節物件 | 8 Maps Over-the-air Updates (MOTA) | 章節「8 Maps Over-the-air Updates (MOTA)」下、該章第一個需求物件之前 |
| `4907836` | `4907833` | 章節物件 | 8 Maps Over-the-air Updates (MOTA) | 章節「8 Maps Over-the-air Updates (MOTA)」下、該章第一個需求物件之前 |
| `4907893` | `4907892` | 需求物件 | 9.1 Pre-Installation | 同章節「9.1 Pre-Installation」內，緊接於需求物件 `4907892` 之後 |
| `4907918` | `4907917` | 章節物件 | 10.1 Shipping/Logistic mode | 章節「10.1 Shipping/Logistic mode」下、該章第一個需求物件之前 |
| `4907920` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907921` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907922` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907923` | `4907907` | 需求物件 | 1.1 Revision Notes | 同章節「1.1 Revision Notes」內，緊接於需求物件 `4907907` 之後 |
| `4907924` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907925` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907926` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907927` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907928` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907929` | `4907919` | 章節物件 | 10.2 Wi-Fi | 章節「10.2 Wi-Fi」下、該章第一個需求物件之前 |
| `4907931` | `4907930` | 章節物件 | 10.3 Installation | 章節「10.3 Installation」下、該章第一個需求物件之前 |
| `4907932` | `4907930` | 章節物件 | 10.3 Installation | 章節「10.3 Installation」下、該章第一個需求物件之前 |
| `4907933` | `4907930` | 章節物件 | 10.3 Installation | 章節「10.3 Installation」下、該章第一個需求物件之前 |
| `4907934` | `4907907` | 需求物件 | 1.1 Revision Notes | 同章節「1.1 Revision Notes」內，緊接於需求物件 `4907907` 之後 |
| `4907936` | `4907935` | 章節物件 | 10.4 Post-Installation | 章節「10.4 Post-Installation」下、該章第一個需求物件之前 |
| `4907937` | `4907935` | 章節物件 | 10.4 Post-Installation | 章節「10.4 Post-Installation」下、該章第一個需求物件之前 |
| `4907939` | `4907938` | 章節物件 | 10.5 Security (Hopefully remove and referenc | 章節「10.5 Security (Hopefully remove and reference to Rejani/Ansaf spec)」下、該章第 |
| `4907940` | `4907938` | 章節物件 | 10.5 Security (Hopefully remove and referenc | 章節「10.5 Security (Hopefully remove and reference to Rejani/Ansaf spec)」下、該章第 |
| `5423873` | `4907231` | 章節物件 | 1.1 Revision Notes | 章節「1.1 Revision Notes」下、該章第一個需求物件之前 |

**不可解者：0 筆** —— 137 個 Description 全數有上位物件可歸。


## 七、與上繳包 01 T10 之差異（分類法修正）

| 類型 | 上繳包 01 T10（首見為準） | 本檔（宣告優先） | 差 |
|---|---:|---:|---|
| 章節物件 | 87 | 87 | — |
| 需求物件 | 478 | **487** | **+9** |
| Description 物件 | 135 | **137** | **+2** |
| 不可歸類 | 21 | **10** | **−11** |
| 合計 | 721 | 721 | — |
| **錨點池** | **565** | **574** | **+9** |

移動之 11 個 id 全部自「不可歸類」移出，成因單一：其在 §4 區先以內文
`Requirement ID {id}` 形態出現，`[Artifact Type:…]` 宣告排在後方，
初版之「首見為準」因而誤歸。

| ObjectID | 初版 | 修正後 | 首見脈絡 |
|---|---|---|---|
| `4907244` | 不可歸類 | 需求物件 | `Requirement ID 4907244` |
| `4907397` | 不可歸類 | 需求物件 | `Requirement ID 4907397` |
| `4907816` | 不可歸類 | 需求物件 | `Requirement ID 4907816` |
| `4907830` | 不可歸類 | 需求物件 | `Requirement ID 4907830` |
| `4907832` | 不可歸類 | 需求物件 | `Requirement ID 4907832` |
| `4907839` | 不可歸類 | 需求物件 | `Requirement ID 4907839` |
| `4907850` | 不可歸類 | 需求物件 | `Requirement ID 4907850` |
| `4907851` | 不可歸類 | 需求物件 | `Requirement ID 4907851` |
| `4907907` | 不可歸類 | 需求物件 | `Requirement ID 4907907` |
| `4907923` | 不可歸類 | Description 物件 | `Requirement ID 4907923` |
| `4907934` | 不可歸類 | Description 物件 | `Requirement ID 4907934` |

**兩項須裁**（執行層不逕改裁決正本）：

1. **錨點池由 565 改為 574。** R-SU7 條文載「池維持 565 = 章節 87 + 需求 478」
   —— 該數承自上繳包 01 T10 之誤分類。正確值為
   **574 = 章節 87 + 需求 487**。R-SU4 v2 (a2) 未載具體數字，不受影響。
2. **R-SU7 之「Description 物件 135 個」應為 137。**

二者皆為分類法之修正，非素材變動；`ANCHOR_POOL.md` 已改記正確值，
裁決正本待分析層修訂。

---

## 附記 —— CFTS057 之六個嵌入物件不在本池之語料內（T65b，下放包 53 §2.2）

下放包 53 §2.2 令複查六個嵌入物件之 ObjectID 是否已被任一列錨定。**複查結果為零，
且其零比「未曾發生」更強** —— 該六個 id **不在本池所據之語料中**：

| ObjectID | 於 `word/document.xml` 之出現次數 | 於本池 | 於 88 個 TC 之 `specification_reference` |
|---|---:|---|---|
| `4907974` | **0** | 未收 | 0 |
| `4907975` | **0** | 未收 | 0 |
| `4907976` | **0** | 未收 | 0 |
| `4907977` | **0** | 未收 | 0 |
| `4907980` | **0** | 未收 | 0 |
| `4908702` | **0** | 未收 | 0 |

（語料即本檔 §前言所載之 `…CFTS_57 Reflash_20251202-2111.docx`，
sha256 `9aa9400b…`；全庫 grep 亦僅命中下放包 53 自身。）

**其號段確實落在池內**（池之 id 範圍 `4907230`–`4915105`），**而號段內不等於語料內**。

> ### 其後果不只是「錨沒錯」
>
> **路徑 A 之語料為 docx 之文字**，而**這六張圖之內容從未進入語料**，
> **連其 ObjectID 都不在文字裡**。故一列若其正解係某張圖所載之流程，
> **路徑 A 在原理上不可能找到它，機制 3 亦不會攔它**
> —— 因為它不是「分數低」，而是**不在候選集合中**。
>
> 本項為 R-G8（能力界線）之一個具體實例：**本池之覆蓋止於文字層。**

> **追認（下放包 55，T67e）**：本附記所載之事實已於 2026-08-30 升格為全域條文
> **`R-G28`**（`FO §9.2`）—— 其令「嵌入物件之 ObjectID 落於錨點池號段內而
> **不在錨定語料內**，錨定之三機制對其一律無效」之事實**須記入該 feature 之
> `ANCHOR_POOL.md` 附記（R-G8）**。**本附記即該要求之落點，措辭已相符。**
