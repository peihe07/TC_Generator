# RULINGS — Security（FW036）

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Security 之裁決權威；
跨 feature 條文承接時註明來源包。

取號依 R-G23／R-G62′：落檔當下 live 取號 —— 本檔建立時全 repo 無既存
`R-SEC` 條號（2026-09-16 現查 `docs/fw036/RULINGS.sha.tsv` 與各 feature
`RULINGS.md` 皆無，`grep -rn "R-SEC" .` 除下放包外 0 命中），故自 1 起，
`{live}` = **1**，與下放包 §2 之期望值相符。

條文來源：`docs/fw036/handoff/down/20260916_SEC-01.md` §2 ＋
`docs/fw036/handoff/down/20260916_SEC-01_A.md` §1／§2。
**R-SEC1(b)(c) 以 addendum §1 之改寫本為準**（addendum 明訂「衝突處以本檔為準」），
主包 §2 之原 (b)(c) 作廢，不另登記。

---

### R-SEC1 — 母體為六本 037（SWRA），全 70 列皆產出；CCVR 五 test item 只決定批次順序（Pei 裁，2026-09-16）

```text
R-SEC{live}  母體為六本 037（SWRA），全 70 列皆產出；CCVR 五 test item 只決定批次順序
  (a) 不變。
  (b) 六本 037 之 70 列**全部**產出 TC（Verification Method = Peer Review 之 29 列仍依 R-SEC{live+1} 待裁後產）。
      trace_matrix.tsv 之 `in_round` 欄改名 `ccvr_batch`：落到 CCVR 五 test item 者 = `1`（前批），
      未落到者 = `2`（後批）。前批對齊 9/18 Dev-Key build 之 CCVR 需求；後批緊接。
  (c) `features/security/data/out_of_round.tsv` 改名 `batch_order.tsv`，欄：
      `swe1_id | ccvr_batch | ccvr_items | reason`；`reason` 記落點依據或未落點理由。
      批次只影響生成順序與 TC ID 序號區段，不影響框架、不影響 Test Group／Test Set 歸屬。
```

(a) 之本文（主包 §2，未被 addendum 取代者）：

```text
  (a) 六本 037 為 Req 母體；SYS3 SYSAD、SYS2 CFTS084、CCVR 為追溯與作者側素材，不得代位為 Req。
```

**執行層回報（SEC-01）**：`ccvr_batch` 實測 batch 1 = **46** 列、batch 2 = **24** 列，
合計 70 列；分析層預判 batch 1 約 45 列，差 **1** 列，未達 addendum §5 之升級門檻（> 8 列）。
差異來源為 `SWE1-CertProvider-006`／`-010`（空格串接之 `Source Requirement ID` 拆解後命中，
見上繳包任務 3-4）。

---

### R-SEC2 — Peer Review 列之處置（Pei 裁，2026-09-16）

```text
R-SEC{live+1}  Peer Review 列之處置
  Verification Method = Peer Review／Document Review／Static Analysis／Inspection 之 29 列
  （ECUCert 13、SWDL 5、LOGENC 8、SAM 0001/0008/0019）：
  (a) 本包只登記、不產 TC；
  (b) 其中 Verification Criteria 可以黑箱手段觀察者（執行層逐列標 `blackbox_possible = Y/N` 並附觀察手段），
      Pei 於 SEC-02 裁定是否轉為 Testing 類 TC；
  (c) 其餘留 RULINGS 待裁，不得自行標 NA。
```

**執行層回報（SEC-01）**：條文所列 29 列逐列核對相符。另有 **2 列**其 Verification Method
非 `Testing` 而條文未列，一併入 `features/security/data/peer_review_rows.tsv`（共 31 列）：

- `SWE1-KeyInsyall-012` —— `Document Review / Static Analysis / Log Observation`（下放包 §1 表已具名，條文之 29 未計入）；
- `SWE1-SAM-0017` —— **Verification Method 欄空白**（原檔缺漏，登 DR-SEC-j）。

`blackbox_possible` 計數：`Y` 7／`Y(部分)` 3／`Y(間接)` 2／`N` 19。

---

### R-SEC3 — SWE1 原檔異常之處置（R-6 verbatim 原則）（Pei 裁，2026-09-16）

```text
R-SEC{live+2}  SWE1 原檔異常之處置（R-6 verbatim 原則）
  (a) `SWE1-KeyInsyall-nnn` 拼字保留原字入 `Requirement or Design ID`，Remarks 註 `RD ID spelling as delivered`；登 DR。
  (b) ECUCert 本無 SWE-Requirement ID：暫以 `Source Requirement ID` 欄之 `SYSAD_SEC_ECUCERT_*`（多值時取首值）
      作 `Requirement or Design ID`，Remarks 註 `SWE ID pending DR`；登 DR 要上游補號。
  (c) `Source Requirement ID` 欄之多值以換行、逗號、**空格**三種分隔並存（CertProvider-006/010 為空格串接）；解析須三者皆拆。
```

**執行層回報（SEC-01）**：(c) 之「空格亦為分隔」與 libLogEncrypt 之「ID 內含空格」
（`SYSAD_SECURITY_ LOGENCRYPT_ENCRYPTION_COMP`）互相衝突 —— 純以空白切會把後者切碎。
實作改以「切在每個 `SYSAD` 起點上」，兩者同時成立（`build_trace_matrix.py` 之
`split_source_ids()`）；切出片段再由 `norm()` 去空白。此為對 (c) 之落地手段，不改條文。

---

### R-SEC4 — Procedure／ER 一律以既有可執行素材落地，不得自造步驟（Pei 裁，2026-09-16）

```text
R-SEC{live+3}  Procedure／ER 一律以既有可執行素材落地，不得自造步驟
  (a) 每一 Procedure 步驟須能回指下列**既有**來源之一，於 reasoning 註明來源與位置：
      1. 該列 037 之 `Verification Criteria` 原文（GIVEN/WHEN/THEN 內之指令、路徑、值）；
      2. `Test_Items.txt` 之 15 條 JUnit 方法（`adb shell am instrument …#<method>` 全式）；
      3. `[NR1L][CCVR]ECU Cert Test Steps.20260826.pdf` 之六步（路徑、`ecucertstatus` 值、`od -t x1`）；
      4. `SYS2_Mapped.xlsx` 之 `Cert Val CS.98` STEPS 欄、`ECU ID CS.165` Test steps／Expected result／Log pattern 欄；
      5. SYS3 SYSAD docx 之 Interface 表 `Flow chart`／`Input Criteria`／`Output Criteria`（介面呼叫順序與參數名）。
  (b) 上列五者皆無者，該步驟寫 `PENDING: DR-SEC-{n} <缺件名>`（IN §8.4.3），登 DR；不得以「合理推測」補步驟。
  (c) 指令、路徑、檔名、狀態值、錯誤碼逐字取自來源（IN §8.4.1）；037 原文之佔位（`<SSN>`、`{TYPE}`、
      `HUssss_YYYYMMDD_HHMMSS_XXXX`、`<configured limit>`）保留佔位，不填實值。
  (d) 步驟用語、欄位寫法、Remarks 格式一律沿用既有交付本（SWC 0708 為 R-1 v2 基準本；
      指令行依 IN §5.4 兩行式；`$` 開頭之指令行不編號）。不得為 Security 另創格式。
  (e) 前批（ccvr_batch=1）之 TC，Procedure 之最終驗證步驟優先採 (a)2 之 apk 方法（可直接執行、可留 log 證據）；
      apk 無對應者退而採 (a)1 之 openssl／adb 指令；ER 以 log／檔案／狀態值為可觀察目標。
```

**執行層回報（SEC-01）**：`trace_matrix.tsv` 新增 `step_sources` 欄（代號 `VC`／`APK:<method>`／
`PDF:<step>`／`CS98:<row>`／`CS165:<row>`／`SYSAD:<table>`）。**70 列皆至少有一個來源**，
「無落地來源」清單（`data/no_step_source.tsv`）為 **0 列**，未達 addendum §5 之升級門檻（> 20 列）。
惟 70 列中有 **20 列僅有 `VC` 一種來源**（其餘 50 列多來源，平均 5.73 個），其可執行性仍受 DR-SEC-c～h 之測試資產阻斷；
(b) 之 `PENDING` 於 Phase 2 仍會大量出現，見上繳包 §7。

#### R-SEC4(a) 增列第 6～8 類（amend，不改號）

```text
R-SEC{live+3}(a) 增列：
  6. DID／RID 讀寫步驟 —— 以 §5.4 兩行式寫，定式見 R-SEC{live+5}。（_B §3）
  7. `R1L_Diag_Software_Qualification_Test_Design.xlsx` 之 `$22_Read_Data`／`$2E_Write_Data`／
     `$31_RoutineCtrl`／`$27_Security`／`Diag基本機能` 各 sheet（R1L 前例本，reference-only）。（_C §1§3）
  8. `CertProfile_BETA_ROW_CS_SUBCA_G1` sheet `CertProfile`（Code Signing 樹 L1 CA／L2 leaf 之欄位規格）——
     僅適用於 Code Signing 場景（FOTA MCPU／VCPU、SWDL、Second Party）；SAM 樹與 ECU Identity 樹另有 profile，
     未到手前該二場景之欄位值寫 `PENDING: DR-SEC-q <tree> cert profile`。（_F §2）
```

**執行層回報**：第 8 類之逐字值 **17 筆**已入 `step_assets.tsv`（`asset = cert_field`，
`source = CertProfile`，`source_loc = CertProfile:r<n>`），列號與 _F §2 表逐列複驗相符。
`CertProfile` sheet 實測 55 列（非空 54），與 _F §1 所載相符。
**OID 尾碼**（`1.3.6.1.4.1.57872.` 之後）sheet 未給實值，保留佔位 `<…>`（IN §8.4.1，不造值）。

---

### R-SEC5 — CS.212 之 CCVR 落點以 037 之 log 斷言直接判定，不經 SYS2（Pei 裁，2026-09-16；SEC-01_B §2）

```text
R-SEC{live+4}  CS.212 之 CCVR 落點以 037 之 log 斷言直接判定，不經 SYS2
  (a) `ccvr_batch` 判定對 `Secure Log CS.212` 改用第二判準：037 列之 Verification Criteria 含
      log／Logdog／logdog／avc／logcat 斷言者，`ccvr_items` 加 `Secure Log CS.212`，`reason` 記 `SWE1-direct`。
  (b) 分析層預判命中：KeyInstall-010（`log a security violation`）、KeyInstall-012（`avc: denied` 不得出現）、
      SAM-0004（`logs an error via logdog`）、CertProvider-005（監看 log 無 CRL 寫檔）、CertProvider-006（Logdog error-level）；
      執行層 grep 全 70 列回報實數。
  (c) CS.212 第 1/7/10/11/12 項（Steven）之 GIVEN/WHEN 步驟為 R-SEC{live+3}(a)4 之合法落地來源，
      對應到 (b) 之列時可引用；其 package 未 release 前（DR-SEC-h），logcat tag／關鍵字保留佔位。
```

**執行層回報（SEC-01）**：初次實作以「全 VC 逐字含五詞」判，得 **11 列**。

**SEC-01 審閱 三-1 改判 → 7 列**（`down/20260916_SEC-01_review.md`）：
`LOGENC-002`／`-003`／`-004`／`-006` 四列為誤判 —— 其 `log` 為受詞或元件名
（`log file encryption`／`encrypt log files`／`logdog could link`／`encryptLogFile` API 識別字），
**不是 log 斷言**；CS.212 為 secure *event* log，與 log *encryption* 無涉。

判準補述（已實作於 `build_trace_matrix.py` 之 `cs212_log_assertion()`）：
只計 **WHEN／THEN 子句**（含 `3.x` 編號之 THEN 續行）內之命中，且該子句須宣稱 log 之產生或觀察；
主詞為 `Log Encryption`／`LogDog` 之元件名、API 識別字、或以 log 為加密受詞者不計。大小寫維持敏感。

現行命中 **7 列**：`CertProvider-005`／`-006`／`-008`、`KeyInsyall-010`／`-012`、`SAM-0004`／`-0015`
（逐列之命中子句記於 `trace_matrix.tsv` 之 `cs212_clause` 欄）。
本條使 `ccvr_batch=1` 由 46 增為 **48** 列；再加審閱 三-2 之 SAM-0007 人工覆寫 → **49** 列、batch 2 **21** 列。

> **執行層對審閱 三-1 之一處回報（`[A-SE12]`）**：審閱之規則文字為「只計 **THEN**／`3.x`／`THEN.` 子句」，
> 惟其所列 7 列含 `SWE1-CertProvider-005` —— 該列之命中在 **WHEN**
> （`WHEN. Monitor system logs during verification.`），其 THEN（`No CRL file I/O operations … shall be observed`）**無命中**。
> 逐字照「THEN only」會得 **6 列**。本包取 **WHEN ∪ THEN** 方能重現審閱指名之 7 列集合。
> 若分析層本意確為 THEN only，則 `CertProvider-005` 應退出，batch 1 為 48（＋SAM-0007 = 49 不變，因 005 本就有 CS.98 落點）。
> **兩解皆不改 batch 總數**，只改 `cs212_direct` 欄之值，故不阻本包；請於 SEC-02 明示。

---

### R-SEC6 — DID／RID 步驟定式（Pei 裁，2026-09-16；SEC-01_C §2，取代 _B §3 末段之 DECISIONS 待定項）

```text
R-SEC{live+5}  DID／RID 步驟定式
  (a) Procedure 步驟：
        n. Send UDS request <SID name> for DID <$XXXX> (<DID name>)
           $ 22 XX XX
      寫入：`Send UDS request WriteDataByIdentifier for DID $F18C (ECU Serial Number)` ＋ `$ 2E F1 8C <15 bytes>`；
      Routine：`Start routine <RID> (<name>)` ＋ `$ 31 01 XX XX`。
  (b) ER：`Positive response is received: 62 XX XX <payload>` 或
          `Negative response is received: 7F 22 <NRC>`；payload 之語意另起一行（例 `00 = INSTALLED`）。
  (c) Session 前提入 Pre-Condition：`Diagnostic session is <Extended (03) | SystemSupplierSpecific (60)>`；
      切換 session 之步驟 `Send UDS request DiagnosticSessionControl` ＋ `$ 10 60` 為 §5.3 常數候選 `ENTER_SUPPLIER_SESSION`。
  (d) 工具：以 bytes 為準，不綁工具語法；`NR1L_UDSTool`／RAFT 之操作方式不入步驟正文，可入 Remarks。
  (e) DID 值來源標記：值取自前例本者，Remarks 寫 `DID value per R1L Diag SWQT (SWTD-IF-DIAG-xxxxx); NR1L CDD pending (DR-SEC-n)`；
      CDD 到手後依 R-G72 發 Revise 本更新。
```

**執行層回報（SEC-01）**：_B §3 末段要求先查既有交付本是否已有 DID 讀寫步驟前例。
**九本交付本 1,700 列全掃，`Procedure` 欄 0 列、`Expected Result` 欄 0 列命中 UDS 樣式**
（bytes 式與服務名皆然）；唯一命中在 `Pre-Condition` 欄 32 列，皆為 SWC 0708 之需求敘述文字，
非步驟。**即本專案無 DID／RID 步驟前例（R-G13：已查，查無）** ——
故 (a)~(e) 之定式為本專案首例，無既有格式可沿用。查證明細見上繳包 §6。

---

### R-SEC7 — 每一 Procedure 步驟與 ER 必須明示執行通道與觀察手段（Pei 裁，2026-09-16；SEC-01_E §1）

```text
R-SEC{live+6}  每一 Procedure 步驟與 ER 必須明示執行通道與觀察手段
  (a) 執行通道為閉合清單，每步擇一並寫出**完整指令或完整操作**：
        ADB   ：`$ adb root` / `$ adb shell <cmd>` / `$ adb push <src> <dst>` / `$ adb pull <src>` /
                `$ adb shell am instrument -w -e class <FQCN>#<method> <runner>` / `$ adb reboot`
        UDS   ：`$ 22 XX XX`、`$ 2E XX XX <data>`、`$ 31 01 XX XX`、`$ 10 XX`（依 R-SEC{live+5}；tester 送 bytes）
        HOST  ：`$ openssl verify …`、`$ openssl x509 -in … -text`、`$ openssl req -in … -noout -verify`、`$ ./logdecrypt_Ver2.sh …`、`$ pytest …`
        CAN   ：`Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)`（§8.7.5(c)）
        PHYS  ：`Insert USB drive containing <資產名> into HU USB port`、`Insert SAM dongle`、`Press H/K "<button>"`、
                `Power cycle HU (IGN OFF → IGN ON)`、`Disconnect network`
        UI    ：`Select "<label>" in Dealer App`（限 HMI L&F／Test Steps PDF 有載之入口）
      指令行依 IN §5.4 以 `$` 起首、獨立一行、不編號；描述行只寫業務意圖，不得只有描述行而無指令行。
  (b) 禁止之寫法（無通道即 FAIL）：
        `Trigger key installation` / `Perform certificate verification` / `Install keys` / `Verify the chain` /
        `Run the test` / `Check the log` / `Corrupt the certificate` —— 皆須改為 (a) 之具體形式，
        例 `Corrupt CERT 0 in ecu.cacert on host (edit PEM body)` ＋ `$ adb push ecu.cacert /data/misc/ecuidentity/`。
  (c) ER 必寫觀察手段，閉合清單：
        LOG   ：`$ adb logcat -s <TAG>` ＋ 期望字串逐字（例 `MelcoCertProviderTest: ECU certificate verification broken chain = ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY`）
        FILE  ：`$ adb shell od -t x1 <path>`／`$ adb shell cat <path>`／`$ adb shell ls -l <path>` ＋ 期望值
        UDS   ：`Positive response is received: 62 XX XX <payload>`／`Negative response …: 7F XX <NRC>`
        RC    ：instrument 之 `OK (1 test)`／`FAILURES!!!` ＋ 方法名
        HOST  ：openssl 之 stdout 逐字（`SAMcert.pem: OK`／`error <n> at <depth> depth lookup: …`）
        CAN   ：`<MESSAGE>.<Signal> = <raw> (<label>) is sent`
        UI    ：`The "<title>" screen is displayed`
      不得寫 `verification succeeds`／`system rejects the certificate`／`log shows error` 而無手段與逐字期望值。
  (d) Pre-Condition 必寫連線與權限狀態：`DUT is connected via ADB with root permission (Dev/Eng build)`、
      `Diagnostic session is <xx>`、`Test runner CertProviderServiceManagerTest.apk is installed`（用 apk 時）。
      這三句為 §5.3 常數候選 `ADB_ROOT_READY`／`DIAG_SESSION_<xx>`／`CP_TEST_RUNNER_INSTALLED`。
  (e) 期望字串、路徑、回應 bytes 一律逐字取自既有素材（R-SEC{live+3}(c)）；素材只給語意不給字串者
      （例 CS.212 第 2~6 項只有 tag 範例），該 ER 寫 `PENDING: DR-SEC-h log keyword`，不得自擬字串。
  (f) 一步一通道。同一步既 `adb push` 又 `reboot` → 拆兩步；ER 1:1 對應。
```

**執行層回報（SEC-01）**：

1. `step_assets.tsv` 加 `channel`／`observe` 二欄，並收入 _E §2 之 **28 句通道句**（逐字）。
   全表 134 列，`channel` 分佈 `ADB` 47／`UDS` 11／`HOST` 7／`PHYS` 3／`CAN` 1／`-` 65（純值與路徑）；
   `observe` 分佈 `FILE` 31／`UDS` 11／`HOST` 9／`RC` 6／`LOG` 6／`CAN` 1／`-` 70。
2. **「每步可配通道」預判**（`trace_summary.md` 4b 節）：`Y` **42** 列／`部分` **8** 列／`N` **20** 列。
   `N` 之 20 列即 R-SEC4(b) 之 `PENDING` 候選，其中 7 列在 batch 1。
3. **lint `C` 對既有交付本之假陽性率**（_E §3 要求之先測）：九本 1,700 列 ——
   Procedure **98.4%**、ER **74.9%**。**既有語料幾乎全不合本條**，
   故 `C` 一律不得入 `PROFILE_CHECKS`，只能入 `FEATURE_CHECKS["security"]`（見 profile 3.4）。

---

### R-SEC8 — DR 從寬處置（Pei 裁，2026-09-16「一 都裁」；SEC-01_G §1）

```text
R-SEC{live+7}  DR 從寬處置
  (a) DR-a  ECUCert 無 SWE ID → 結案。`Requirement or Design ID` = `Source Requirement ID` 首值（SYSAD_SEC_ECUCERT_*），
            Remarks `SWE ID pending; SYSAD used per R-SEC{live+7}(a)`。上游補號後依 R-G72 發 Revise 本。
  (b) DR-b  `KeyInsyall` 拼字 → 結案。原字入 ID 欄，Remarks `RD ID spelling as delivered`。不追。
  (c) DR-i  `SYSAD_SAM_PACKAGE_INTF` 無 SYS2 對應 → 結案。trace_matrix 之 `_COMP`／`_INTF`／`_API`／`_BINDER`
            去尾綴回退基底名為合法對應，`match_kind = base`；追溯欄不因此標 PENDING。
  (d) DR-n  CDD 實作選項 → 結案。NR1L 走 `2955 + 295D + 295E` 三分式（CS.00102 5.2.2.72 將 `295F` 標 OutofScope，
            `SYS-RA-CS00102-410/411`）；`2965` CSR Read 之 ER 寫 `up to 1000 bytes (CS.00102 5.2.2.75, SYS-RA-CS00102-415)`，
            R1L SWQT 之 2048 只入 Remarks。
  (e) DR-o  FF02 兩態 vs 四態 → 結案。037 KeyInstall-011 原文為 Binder `getStatus()` 回 `INSTALLED (2)`／`ERROR (3)`，
            未提 DID。TC 之 ER 以 Binder／log 面為準（四態依 037 KeyInstall-006 逐字）；DID `22 FF 02` 及其回值
            只入 Remarks 作補充觀察，不入 ER、不作 pass/fail 判準。
  (f) DR-j  CRL vs DCL → 結案（取代 _F §3）。兩機制並存，各依母體原文：
            · CertProvider-004／005 依 037 原文寫 **CRL**：004 之本地檔以 037 之 `CRL.r0` 逐字（路徑取 037
              `SecurityAssets/oem-certs/cert-provider/`）；005 之 CDP 取 CertProfile r40 `http://vpki.preprod.stellantis.com/crls/L1CS`
              （PROD 環境以 `<env>` 佔位）。Remarks `DCL (SD.00015/03, DID 2031) is a separate mechanism; see CCVR Cert Val CS.98`。
            · Cert Val CS.98 第 2/5~8 之 CCVR 步驟（若入 TC）依 Steven STEPS 逐字用 `dcl_baseline.json`／`dcl_revoked_l{n}.json`，
              Remarks 互註。
            兩側不互相改寫；不得把 004 改成 DCL、也不得把 CS.98 改成 CRL。
  (g) DR-k  0x9001／0x9003 金鑰佈建規格 → 降級為 reference，不阻任何列。037 KeyInstall-007 原文為 USB/SDCard 匯入，
            CAN 注入不在 037 範圍（§8.4.2）。CS.212 第 10/12 項之 logcat 行逐字可用於 KeyInstall-010/012 之 log 斷言
            （`injectKeysFromJson: transport.key missing or invalid size 0 — was 0x9001 called?`、
             `AIDL injectKeysFromJson: status=5 responseByte=0x01`），Remarks `per CS.212 draft`。
  (h) DR-q  SAM／ECU Identity 樹 cert profile → 降級為 reference。SAM-0007 之 ER 寫至 037 原文粒度
            （`x509 PEM format`／`signed by a certificate chain that anchors to the OEM issued root certificate`／
             `Subject field intended for SAM and specific market`）；ECU Identity 樹名以 CS.165 sheet 逐字
            （`VHL_ROOT_G1`、`ECUID_SUBCA_G1`）；欄位細節（OID、CDP）只在 Code Signing 場景依 CertProfile 寫，其餘不擴張。
  (i) DR-l  `31 01 F0 00` 回應碼 → 結案。ER 逐字引 CCVR Auth-Prog 實測欄：`71 01 F0 00 00`（通過）、
            `71 01 F0 00 01`（`Validation … returns invalid application`）、`71 01 F0 00 02`（lower rollback id）；
            語意標 `per CCVR Auth-Prog CS.93 evidence, row <n>`。`image249.png` 解圖仍做，只作補強，不阻列。
  (j) DR-m  CS.00165 §5.6／SD.00125 §5.1 DTC 碼 → 結案。ECUCert DTC 類 ER 之主斷言為 log
            `ECU_INSTALLATION_STATUS value : 2 -> 1` 與 DID `22 29 66`（Cert Error Enable，Accepted）；DTC 行寫
            `DTC defined in CS.00165 section 5.6 is reported in the 19 02 FF response`，碼以 `<DTC per CS.00165 §5.6>` 佔位（§8.4.1 允許）。
  (k) DR-h  CS.212 package → 結案。第 1/7/10/11/12 項之 tag 與期望字串以 SYS2_Mapped `Secure Log CS.212` sheet 逐字，
            Remarks `per CS.212 draft 20260826`；第 2~6/8/9/13 項無 037 對應，不入本輪。package 正式版到手後依 R-G72 Revise。
```

**執行層回報（SEC-01）**：

1. **(i) 之三個回應值逐字複驗成立**，並補其出處列號與精確語境：
   `Auth-Prog CS.93` r3／r5／r6 → `0x71 01 F0 00 01`（皆附 `DTC in bootloader is: 0xA2 50 00 0F`）；
   r7「Flashing higher rollback id」→ `00`，同列「Flashing lower rollback id」→ **`01`**；
   r8「Flashing same rollback id」→ `00`，同列「Flashing lower rollback id」→ **`02`**。
   → **條文之「`02`（lower rollback id）」須加限定**：r7 與 r8 同稱 lower rollback id 而回值不同
   （r7 為「已遞增版本後回刷舊版」＝`01`，r8 為「未遞增版本後回刷舊版」＝`02`）。
   引用時須連 `row <n>` 一併標，否則同一敘述會對到兩個值。已登 `[A-SE11]`。
2. **(k) 之 tag 與期望字串逐字複驗成立**（`Secure Log CS.212` 第 1/7/10/11/12 項），
   已入 `step_assets.tsv`。
3. **(c) 之 `base` 回退在本 feature 未被觸發** —— 六本 SYSAD 之元素表使 `_COMP`／`_INTF` 自身即為
   `SYSAD_ID`，`match_kind` 實測 **70/70 exact**，`base` 命中 0。(c) 之授權仍登記備用。
4. **§3 之「PENDING 預期為 0」**：`no_step_source.tsv` 依本檔條款重跑後仍為 **0 列**（本就為 0）。
5. **§3 之「Testing 41 列」與實測不符**：70 列中 Verification Method 非 `Testing` 者為 **31 列**
   （Peer Review 家族 29 ＋ `SWE1-KeyInsyall-012` Document Review ＋ `SWE1-SAM-0017` 空白），
   故 `Testing` 實為 **39 列**，非 41。差 2 列即該二列之歸類，見上繳包 §10。

---

### DR-j 改題之歸併（_F §3 → R-SEC8(f)）

`_F` §3 之「DR-j 改題」**已由 R-SEC8(f) 取代**（`_G` 明訂）。
`DATA_REQUESTS.md` 之 DR-j 列以 `CLOSED (R-SEC8(f))` 記，改題文字保留備查、不刪（R-TM13）。
`trace_matrix.tsv` 之 `TERM:CRL|DCL` 標記**保留** —— 其用途由「待裁」轉為
「提示該列須依 R-SEC8(f) 寫 CRL 並於 Remarks 互註 DCL」。

---

### R-SEC9 — SWE1 之 Polarion NRL 對照（Pei 裁，2026-09-16；SEC-02 §1）

```text
R-SEC9  SWE1 之 Polarion NRL 對照
  (a) `trace_matrix.tsv` 加欄 `nrl_swe1`；CertProvider 11 列填 `NRL-349384`～`349394`（逐列自 `Basic Report` A 欄），其餘 59 列填 `-`。
  (b) `specification_reference` **不用 NRL**（六本只有一本有匯出，且 037 xlsx 仍為母體）；NRL 入 Remarks 第二行 `Polarion: NRL-nnnnnn`（有者填）。
  (c) 其餘五本之 Polarion 匯出登 DR-SEC-s（低優先，不阻）。
```

**執行層回報**：投遞檔 `SWE1-CertProvider.xlsx` sha16 `beff84c77c6810f1`、26,778 B，**與下放包相符**。
`Basic Report` 13 列（表頭 ＋ 11 資料列 ＋ 1 空列），`NRL-349384`～`NRL-349394` 對
`SWE1-CertProvider-001`～`-011` **逐列順序對應，無缺無跳**。
**下放包之「11/11 逐字相同」宣稱已複驗成立**：`Description` 11/11、`SWE1 Verification Criteria` 11/11
（空白正規化後逐字相等）。
註：該匯出之欄名為 `SEW1 SWE-Requirement ID`（原檔拼字 `SEW1`），解析逐字照用、不更正（R-6）。

---

### R-SEC10 — framework 與工作簿形制（Pei 裁，2026-09-16；SEC-02 §2）

```text
R-SEC10  framework 與工作簿形制
  (a) Layer 1 = 案 A：一本 workbook，六個 Test Group `Cert Provider`／`Key Install`／`SAM`／`ECU Cert`／`SWDL Secure Lib`／`Log Encrypt`。
  (b) TC ID：`NR1L-CP-nnn`／`NR1L-KI-nnn`／`NR1L-SAM-nnn`／`NR1L-ECUC-nnn`／`NR1L-SWDL-nnn`／`NR1L-LOGENC-nnn`，各組獨立自 001 升冪；
      batch 1 先占號，batch 2 接續（同組內不得交錯）。
  (c) `specification_reference` = `{037 token}_{SWE1-ID}`，一行一筆。token 定義：檔名去副檔名、去前綴 `FM-WI-FSM-037-A03-N1L-`、
      去尾綴 ` STLA 報告_SWRA STLA Report_SWRA`、空白→底線。六個 token 實值（執行層複驗後逐字寫入 profile）：
        `SWE1-CertProvider-SWE1R1-V1.0`／`SWE1-KeyInstall-SWE1R1-V1.0`／`SWE1-SAM-SWE1R1-V1.1`／
        `SWE1_ECUCert_FM-WI-FSM-037-A03`／`SWE1_SwdlSecureLib_FM-WI-FSM-037-A03`／`SWE1_libLogEncrypt_FM-WI-FSM-037-A03`
      ECUCert 之 `{SWE1-ID}` 依 R-SEC3(b) 以 SYSAD 首值代入，例 `SWE1_ECUCert_FM-WI-FSM-037-A03_SYSAD_SEC_ECUCERT_ECUCERT_API`。
  (d) `spec_mode` 新型別 **`F`**（037-SWRA 母體）：錨 = (c)；lint 之 spec_ref 檢查對 `F` 只驗「token ∈ 六值 ＋ `_` ＋ SWE1-ID ∈ 70 列（或 ECUCert 13 個 SYSAD）」。
  (e) Layer 3 = SYSAD ID（SWE1 `Source Requirement ID` 首值），不入工作簿。
  (f) Vehicle Model 七欄：70 列一律五有效車型 `1`、`598`／`5210` `0`（上繳包 7-1 grep 證實無車型條件）。
```

**執行層回報**：(c) 之六個 token 已逐檔依推導規則複驗，**六值全部吻合**（見上繳包）。
(b) 之六個 ABBR 全 repo 現查未被佔用。

---

### R-SEC11 — Peer Review 列之轉換（修正版；Pei 裁，2026-09-16；SEC-02_A §1 取代 SEC-02 §2 之 (b)(c)）

```text
R-SEC11  Peer Review 列之轉換（R-SEC2 之續）—— 修正版
  (a) `peer_review_rows.tsv` 之 `Y` 7 ＋ `Y(部分)` 3 ＋ `Y(間接)` 2 = 12 列轉為 Testing 群（`SWE1-SAM-0017` 在 `Y` 7 之內，不另加）。
  (b) `N` 19 列不產 TC：LOGENC 001/002/003/004/005/007/008/009（8）＋ ECUCert `…SERVICE_BINDER`／`…ECUONLINE_BINDER`／
      `…ECUCERT_JNI`／`…STORAGE_IO`／`…ECUONLINE`／`…ECUONLINE_DOWNLOADCERT_INTF`（6）＋ SWDL 001/002/005（3）＋ SAM 0001/0019（2）。
      `RULINGS.md` 記 `DEFERRED (R-SEC11(b))`，`batch_order.tsv` 加欄 `disposition = D`，`ccvr_batch` 仍照機械判準保留（供日後解凍時排序）；不標 NA。
  (c) 產出群 = 39（原生 Testing）＋ 12（CONVERT）= **51**；D 群 **19**；合計 70。
```

**執行層回報**：(b) 之 19 列逐列與 `peer_review_rows.tsv` 之 `blackbox_possible = N` 集合**完全一致**
（`batch_order.tsv` 之 `disposition = D` 與之互驗，兩集合相等）。(c) 之 51／19 實測相符。

**DEFERRED 19 列（`DEFERRED (R-SEC11(b))`）**：
`SWE1-SAM-0001`、`SWE1-SAM-0019`、
`SYSAD_SEC_ECUCERT_ECUONLINE`、`SYSAD_SEC_ECUCERT_ECUCERT_SERVICE_BINDER`、
`SYSAD_SEC_ECUCERT_ECUONLINE_BINDER`、`SYSAD_SEC_ECUCERT_ECUCERT_STORAGE_IO`、
`SYSAD_SEC_ECUCERT_ECUCERT_JNI`、`SYSAD_SEC_ECUCERT_ECUONLINE_DOWNLOADCERT_INTF`、
`SWE1-SRA-SECURITY-SWDL-001`／`-002`／`-005`、
`SWE1-LOGENC-001`／`-002`／`-003`／`-004`／`-005`／`-007`／`-008`／`-009`。

交叉表（實測）：

| 群 | batch 1 | batch 2 | 計 |
|---|---:|---:|---:|
| Testing（原生）| 28 | 11 | 39 |
| CONVERT | 10 | 2 | 12 |
| DEFERRED | 11 | 8 | 19 |
| **合計** | **49** | **21** | **70** |

---

### R-SEC12 — batch 人工覆寫（Pei 裁，2026-09-16；SEC-02 §2）

```text
R-SEC12  batch 人工覆寫
  (a) `SWE1-SAM-0007` 覆寫 `ccvr_batch = 1`，`reason = manual override: apk samCertTestNormalFlow (Test_Items #04; CS.98 STEPS)`。
  (b) 覆寫只此一列；其餘依機械判準。
```

**執行層回報**：以 `MANUAL_BATCH1` 集合實作，`batch_order.tsv` 之 `reason` 逐字記明其為覆寫；
(b) 之「只此一列」以該集合之基數（1）保證。

---

### R-SEC13 — lint 於 Security 之範圍與代號（Pei 裁，2026-09-16；SEC-02 §2）

```text
R-SEC13  lint 於 Security 之範圍與代號
  (a) `C`（channel／observe）與 `source:` 標記兩項**只入 `FEATURE_CHECKS["security"]`**，不入 `PROFILE_CHECKS`。
  (b) 代號：若 `lint036.py` 之檢查項代號支援多字元，取 **`SC`**（channel）與 **`SS`**（source:）；若只支援單字元，執行層回報現行占用表，Pei 另指派，本包先以 `SC`／`SS` 落 profile。
  (c) Pilot 門檻：`P`(v4)＋`X`＋`SC`＋`SS` 全綠；`Y`／`Z` 連動照既有。
```

---

### R-SEC14 — 雜項（Pei 裁，2026-09-16；SEC-02 §2）

```text
R-SEC14  雜項
  (a) `DR-SEC-j2` 改號 `DR-SEC-r`（SAM-0017 Verification Method 補值）；新增 `DR-SEC-s`（其餘五本 Polarion 匯出）。
  (b) `step_assets.tsv` 剔除 4 列雜訊（`/cfgs`、`/odm`、`/write`、SharePoint 片段）。
  (c) 佔位 `<…>`（§8.4.1）不計 PENDING；`PENDING: DR-…` 才計。lint `SS` 對 `<…>` 不報。
  (d) Harman `Rejected` 解為責任歸屬（MD 承接），ledger 記為推論（53/53 `MD Accepted`），不據此排除任何列。
  (e) R-6 附註：SYSAD docx 之 ID 可帶 U+3000 前綴；正規化去除**所有** Unicode 空白（`\s` 含 U+3000）。
  (f) R-G44′ 實例：`R1L_Diag_SWQT` Desktop 本 vs OneDrive 本 sha 互異，以 `_C §1` 之 sha 為準。
```

**執行層回報**：(b) 之剔除已落，`step_assets.tsv` 由 156 列降為 **152** 列；
`/odm/etc/cert_store`（真路徑）未受影響，只剔除裸 `/odm`。

---

### R-SEC5(a) amend（SEC-02_A §2；[A-SE12] 結案，命中 7 列改 5 列）

```text
R-SEC5(a) amend（CS.212 直連判準補述）
  只計 THEN／`3.x`／`THEN.` 子句內之 `log`／`Logdog`／`logdog`／`avc`／`logcat`，且該 THEN 須宣稱
  **某一資安事件**（驗證失敗、未授權存取、狀態變更、提權、輸入驗證失敗等 CS.212 類別）**被寫入 log**，
  並可以 logcat／Logdog 觀察到；logging 政策、log 檔案處理、非事件性之 I/O 觀察不計。大小寫敏感。
  命中 = CertProvider-008、KeyInstall-010、KeyInstall-012、SAM-0004、SAM-0015，共 5 列。
```

**執行層回報**：實測命中 **5 列**，與條文指名者逐列相符。逐列命中子句：

| SWE1 ID | THEN 子句（逐字）|
|---|---|
| `SWE1-CertProvider-008` | `THEN. Confirm successful end-to-end verification through system logs (Logdog) for both client types.` |
| `SWE1-KeyInsyall-010` | `6.1. THEN the system must REFUSE the request and log a security violation.` |
| `SWE1-KeyInsyall-012` | `- THEN no SELinux denial logs (avc: denied) related to KeyInstall should be present.` |
| `SWE1-SAM-0004` | `3.1. THEN DebugAuth logs an error via logdog, which corresponds to fail reason` |
| `SWE1-SAM-0015` | `3.2. AND DebugAuth prints the log about sending message with sequence ID mentioned` |

剔除之二列依 SEC-02_A §2：`CertProvider-005`（`Monitor system logs` 在 WHEN，THEN 為檔案 I/O 之否定觀察）、
`CertProvider-006`（`logs must align with Logdog requirements` 為 logging **政策**）。
二者之 `ccvr_batch` **不受影響**（經 SYS2 落 `Cert Val CS.98`，機械判準已為 1），
`ccvr_items` 已移除 `Secure Log CS.212`。**batch 1 仍 49。**

**`[A-SE12]` 結案** —— 分析層已於 SEC-02_A §2 明示規則本意為 THEN-only，並據此剔除 CP-005／006。

---

### R-SEC15 — pilot01 所揭違規類型之明文（適用 Security 全 70 列）（Pei 裁，2026-09-16；SEC-03 §2）

```text
R-SEC15  pilot01 所揭違規類型之明文（適用 Security 全 70 列）
  (a) 跨場景字串移植 = 造值。任一 log 字串、指令、方法名、路徑，只能用於其來源所載之同一場景
      （同一 apk 方法／同一元件／同一憑證樹）；移用到他場景視同 §8.4.1 造值。
      例：CS.212 row 1 之 `ECU certificate verification broken chain = ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY`
      只可用於 `ecuCertTestBrokenChainCert`，不得用於 `fotaMcpuCertTestBrokenCert`。
  (b) 觀察不得代替觸發。ER 期待 DUT 側之結果（log／檔案／狀態）者，Procedure 須有一步在 DUT 側觸發該行為
      （apk 方法、USB 插入、UDS 請求、CAN 送出、reboot）；host 端 openssl 不構成 DUT 觸發。
      無可用觸發手段者，該觸發步驟整行寫 `PENDING: X-<n> <variant> + trigger`，ER 對應行同為 PENDING。
  (c) 內部台帳代號（`X-[a-z]`、`DR-SEC-[a-z]`、`R-SEC\d+`、`A-SE`）不得出現於 Pre-Condition／Input Test Data／Procedure／ER；
      只可入 Remarks。PENDING token 例外：`PENDING: X-<n> <缺件名>` 與 `PENDING: DR-SEC-<n> <缺件名>` 皆合法（R-SEC7(e) amend）。
  (d) 字面值一律 `"…"`（IN §11）；反引號、單引號、`<>` 禁用（`<…>` 佔位除外）。
  (e) `Input Test Data` 一律 `NA`（R-1 v2 基準；§1 量測若證實則落 profile）；資料內聯 Pre-Condition 或 Procedure。
  (f) `test_item` 上半 = 037 `Requirement Description` 之首句 verbatim（≤50 token；長句自句首截至第一個句號），非 Title。
  (g) apk 方法只用於 `apk_pairing.tsv` 有列之 SWE1；無列者不得硬配，觸發步驟依 (b) PENDING。
  (h) R-SEC8(e) 重申：DID 值不入 ER；KI-011 之 Binder 呼叫無素材者，Proc 該步 `PENDING: X-f KeyInstall status test runner`。
  (i) `PENDING` 為整行 token，不與散文混寫；一 ER 行只能是「可觀察斷言」或「PENDING token」二者之一。
  (j) Security profile 豁免 lint `I-cross`。
```

**執行層回報（SEC-03）**：

- (e) 之「§1 量測若證實」—— **已證實**：`Input Test Data = NA` 於 SWC 0708 為 **285／286**、
  pm_29 為 **389／389**。落 profile 3 節「欄位形制」。
- (d) 之引號 —— 量測佐證：SWC 0708 之 ER 內 `"…"` **50 次**，`'…'` **0**、反引號 **0**；
  pm_29 三者皆 **0**。**兩本皆無反引號／單引號**，(d) 與既有交付本一致。
- (j) 已於 `lint036.py` 之 `check_order()` 落實（Security profile 略去 `I-cross`）。
- (a)~(i) 之自檢結果見上繳包 §7（逐條「0 處」與其檢查方法）。

---

### R-SEC16 — Security 之 Priority 指派（Pei 裁，2026-09-16；SEC-04 §1）

```text
R-SEC16  Security 之 Priority 指派
  P0  密碼學驗證之「接受／拒絕」決定本身：憑證鏈驗證（CP-001）、撤銷檢查（CP-004/005）、簽章驗證（SWDL-004、SAM-0005/0007）、
      金鑰安裝之驗證與狀態（KI-002/003/004/007）、AuthData 驗證失敗之處置（SAM-0004）—— 失敗即安全機制失效，等同 IN §10.2 之 data-loss risk。
  P1  欄位比對與介面：Subject/Issuer/OID（CP-002/003/011）、狀態查詢（KI-011）、CSR 匯出（ECUCert R18）、
      SAM 通知與 seqId（SAM-0013~0017）、trust store 位置／dev-prod（CP-007/009）、金鑰服務（KI-009/010）、暫時金鑰（KI-001）、
      覆寫保護（KI-005）、安裝狀態四態（KI-006）、持久化（KI-008）、ECUCert 之 lifecycle／verification／diag 各介面。
  P2  非功能與 logging 政策：CP-006/010、KI-012/013、LOGENC 全部、SAM-0001/0002/0008/0018/0019、SWDL-001/002/003/005。
  P3  無。
  同一 SWE1 之 sibling 同 Priority；負向 sibling 不降級。
```

**執行層回報（SEC-04）**：條文之三個層級對 batch 1 之 38 列**完全覆蓋，無列落在條文之外**
（逐列比對見 `sibling_plan.tsv` 之 `priority` 欄與上繳包 §4）。`P3` 依條文為空，實測 **0 列**。

---

### R-SEC15(f) amend — Description 為中英並列者取英文句（Pei 裁，2026-09-16；SEC-04 §1）

```text
R-SEC15(f) amend  Description 為中英並列者取英文句；仍須為原文逐字子字串（ECUC-001 先例）。
```

**執行層回報（SEC-04）**：ECUCert 之七列 Description 全數為中英並列，
依本 amend 一律取其英文句；逐列之英文句皆為原文之**逐字子字串**（未改寫、未合併）。
其必要性為 lint `K`（CJK 字元）—— `test_item` 在 `K_FIELDS` 內，逐字全取必觸發。

---

### R-SEC17 — Test Set 英文定名（Pei 裁，2026-09-16；SEC-05 §1；A-12 更正）

```text
R-SEC17  Test Set 英文定名（取代 framework v01 之五個中文佔位；A-12 更正）
  Cert Provider   `(非功能)`        → `Service Robustness`     （CP-006、CP-010）
  Key Install     `(非功能)`        → `Platform Compliance`    （KI-012、KI-013）
  SAM             `(環境)`          → `Service Environment`    （SAM-0001／0002／0008／0019；執行層以 037 原文複核四列是否皆屬「執行環境與部署前提」，不合者回報，不自行移組）
  ECU Cert        `(IPC／JNI／IO)`  → `Internal Interfaces`    （R14~R17）
  SWDL Secure Lib `(總則)`          → `Library Scope`          （SWDL-001）
  Log Encrypt     `(其餘)`          → `Encryption Services`    （LOGENC-001~005／007~009）
  名稱為能力層（IN §4.2），非分類；不得再以括號註記作 Test Set。
```

**執行層回報（SEC-05）**：六項已改入 `framework.md` v02，Layer 2 名稱之 CJK 計數 **5 → 0**。

**SAM `Service Environment` 四列之複核（條文指定）—— 三列相符，一列不合**：

| SWE1 | 037 Requirement Title | 判 |
|---|---|---|
| `SWE1-SAM-0001` | DebugAuth is under Android 14 environment | ✅ 執行環境 |
| `SWE1-SAM-0002` | DebugAuth should be a native layer daemon service | ✅ 部署形態 |
| `SWE1-SAM-0019` | DebugAuth has following external interfaces: LogDog, Certprovider, BoringSSL, Json library, vehicle... | ✅ 部署前提（外部相依）|
| **`SWE1-SAM-0008`** | **Format of AuthData should follow SAM package definition in System design** | **✗ 不合** —— 其為**資料格式**需求（manifest 檔名、簽章、計數器欄位），非執行環境或部署前提 |

→ **`SWE1-SAM-0008` 不屬 `Service Environment` 之能力面。執行層依條文回報，不自行移組。**
該列在 batch 2 產出群內（`CONVERT`），本包仍依現行歸屬產 TC；
若 Pei 裁定移組（例移入 `AuthData Verification`），須再走一次 R-G72 Revise。

---

### R-SEC7(c) amend — 七類為觀察面之類別（Pei 裁，2026-09-16；SEC-05 §1）

```text
R-SEC7(c) amend  七類為觀察面之類別；各類具體句式由 profile §3 常數表列舉並可增列，增列須附素材出處。
  本次增列：RC 類 `The adb pull command reports "1 file pulled" …`、`The log buffer is cleared`；
            FILE 類 `adb shell procrank|df|ps` 之 stdout（037 KI-013／CP-010／SAM-0002 verbatim）。
```

**執行層回報（SEC-05）**：三式已於 SEC-04 落於 `lint036.py` 之 `SEC_OBSERVE`，本包**不再改**（§0）。
素材出處：前二式為 SEC-03 審閱 §二 指定之修法；後者為 037 之 verbatim 取樣指令。

---

### R-SEC18 — batch 2 之 CAN 通道寫法（SAM-0013／0017 首例）（Pei 裁，2026-09-16；SEC-05 §1）

```text
R-SEC18  batch 2 之 CAN 通道寫法（SAM-0013／0017 首例）
  (a) 觸發以 VHAL Guide R5 之 VHAL→CAN 對照為橋（`forms/VHAL_User_Guide_R5.pdf`）：
      `IGNITION_STATE` ↔ `CmdIgnSts`（Atl-Hi `BCM_FD_10` 0x481 / Atl-Mi `STATUS_BH_BCM2` 0x46C）；
      `POWER_MODE_STS` ↔ `PowerModeSts`（`BCM_FD_9` 0x42A）。
  (b) 步驟依 IN §8.7.5(c)：`Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)`；raw／label 逐字取 `forms/` 之 DBC `VAL_`（R-7、R-17）；
      DBC 查無該訊號或 label 者，raw／label 以 `<…>` 佔位並 Remarks 註 `DBC lookup pending`——不得造值。
  (c) Atl-Hi／Atl-Mi 訊息不同 → 拆 sibling，Vehicle Model 各勾（Hi：HDCC27／DT27 = 1，其餘 0；Mi：VF637／Toro／Fastack = 1，其餘 0）。
  (d) ER：`<MESSAGE>.<Signal> = <raw> (<label>) is sent` 只用於 HU 送出之訊號；SAM 之結果面（`/data/vehicle/dauth/seqId` 歸 0、目標功能 OFF）以 FILE／LOG 類觀察。
```

**執行層回報（SEC-05）**：DBC 查得／佔位之計數與 CAN 首例全文見上繳包 §5。
註：(d) 之路徑寫作 `/data/vehicle/dauth/seqId`，037 SAM-0015／0017 原文為
**`/data/vendor/dauth/seqId`**（`vendor`，非 `vehicle`）—— 本包依 **037 原文**寫，
條文之筆誤逐字回報，不沿用（R-SEC4(c) 逐字取自來源）。

---

### R-SEC16(amend) — batch 2 六列之 Priority 指派（Pei 裁，2026-09-16；SEC-06 §1）

```text
R-SEC16 amend  batch 2 六列指派：SAM-0006／0010／0011／0012 = P0（驗證之接受／拒絕決定）；SAM-0003／0009 = P1（介面與儲存）。
               Remarks 之 `priority assigned by analogy; …` 註移除。
```

**執行層回報（SEC-06）**：與 SEC-05 之類推指派**逐列相同**，故六列之 Priority 值不變；
僅移除六列 TC 之 Remarks 註（`priority assigned by analogy; R-SEC16 does not list this SWE1 row`）。

---

### R-SEC17(v03) — SAM-0008 移組（Revise v03；Pei 裁，2026-09-16；SEC-06 §1；A-17 更正）

```text
R-SEC17 Revise v03  SAM-0008 由 `Service Environment` 移至 `AuthData Verification`；`Service Environment` 剩 SAM-0001／0002／0019。（A-17 更正）
```

**執行層回報（SEC-06）**：`framework.md` 加 `REVISE v03` 段並 `LOCKED v03`；
`layer2_assign.tsv` 同步 1 列。`Service Environment` 之 leaf 由 4 降為 **3**，
`AuthData Verification` 由 5 升為 **6**；**leaf 總數 70 不變**。

---

### R-SEC18(amend) — 刪 `POWER_MODE_STS` 對照；路徑更正（Pei 裁，2026-09-16；SEC-06 §1）

```text
R-SEC18 amend  (a) 刪 `POWER_MODE_STS ↔ PowerModeSts` 對照（A-19：分析層推測橋，DBC 證實無 resume 值）；只留 `IGNITION_STATE ↔ CmdIgnSts`。
               (d) `/data/vehicle/dauth/seqId` 更正為 `/data/vendor/dauth/seqId`（A-14）。
```

**執行層回報（SEC-06）**：(a) 之 `BCM_FD_9` 佔位式已自 batch 2 移除（見 R-SEC19）；
(d) 之路徑本包前即依 037 原文寫 `/data/vendor/dauth/seqId`，**無須改 TC**。

---

### R-SEC19 — SAM-0013 之 resume-from-suspend 分支（Pei 裁，2026-09-16；SEC-06 §1）

```text
R-SEC19  SAM-0013 之 resume-from-suspend 分支：037 未載觸發手段，VHAL Guide 無對應 → `NR1L-SAM-025`／`-026` 之觸發步驟整行
         `PENDING: X-n suspend/resume trigger method`，ER 對應行同為 PENDING；`BCM_FD_9` 之佔位式移除。`X-n` 登 EXEC_ASSETS（15→16）。
```

**執行層回報（SEC-06）**：兩列之觸發步驟與 ER 已改為整行 PENDING token；
`BCM_FD_9` 之 `Send CAN:` 行移除，CAN 步驟由 6 降為 **4**（全部 DBC 逐字，**佔位 0**）。
`X-n` 已登 `EXEC_ASSETS.md`（15 → 16 項）。

---

### R-SEC20 — 原始碼／建置環境類驗證之文件審查定式（Pei 裁，2026-09-17；SEC-08 §1）

```text
R-SEC20  原始碼／建置環境類驗證之文件審查定式（X-i；CP-006、KI-012、KI-013 等以 source code 為受詞之列）
  (a) Design Method 維持 037 之 Verification Method 語意：`功能測試 (Functional based ; no specific technique)`；
      Remarks 首行 `verification: document review (R-SEC20)`。
  (b) Procedure：
        1. Obtain <artifact> from the RD build environment
           $ <取得方式若 037 有載則逐字，否則整步為佔位 `<obtain <artifact> per RD>`>
        2. Review <artifact> against <037 條款逐字之要件>
      每一要件一步；不得寫 `$ grep`／`$ cat` 等執行層自擬之檢查指令（037 未載）。
  (c) ER：`<artifact> contains <要件逐字>`（例 `Android.bp declares the service as START_STICKY`——只在 037 原文有該字串時；
      否則 `<artifact> satisfies <要件逐字>`）。
  (d) Pre-Condition：`Access to the RD build environment for <component> is granted`。
  (e) Priority 依 R-SEC16 = P2 不變；`test_item` 括號下半加 `(document review)` 尾綴，作 sibling token。
  (f) 原 `PENDING: X-i …` 行全部消除；Remarks 保留 `X-i` 代號與 `source:`。
```

**執行層回報（SEC-08）——條文之涵蓋面與實測不符，逐項具名**：

| 條文所載 | 實測 | 處置 |
|---|---|---|
| 「`X-i` 16 行（**12 TC**）」 | 16 行／**8 TC**（每 TC 2 行：Proc ＋ ER）| 依實測之 8 TC 重寫 |
| 條文舉例含 **KI-013** | **`SWE1-KeyInsyall-013`（`NR1L-KI-025`）不帶 `X-i`** —— 其 037 VC 為 `monitoring via procrank and df`，SEC-04 起即以 `$ adb shell procrank`／`$ adb shell df` 落地，無 PENDING | **不動**該列 |
| 同理 **CP-010**（`NR1L-CP-021`）| 亦不帶 `X-i`（`procrank`）| **不動** |
| 條文未列 **CP-008** | `NR1L-CP-017`／`-018` 帶 `X-i`，其 037 VC 為 `Inspect the source code and dependency graph` —— **以 source code 為受詞**，合 (a) 之射程 | **納入**重寫 |

→ 重寫之 8 TC：`NR1L-CP-011`~`-014`（CP-006 四 sibling）、`NR1L-CP-017`／`-018`（CP-008 兩 sibling）、
`NR1L-KI-023`／`-024`（KI-012 兩 sibling）。

---

### R-SEC21 — PENDING 之佔位化（Pei 裁，2026-09-17；SEC-08 §2）

```text
R-SEC21  PENDING 之佔位化（適用 AWAIT_ASSET 96 行；X-i 依 R-SEC20）
  (a) 允許轉換之條件：佔位須**點名值之來源與性質**，格式 `<性質 provided by RD (X-<n>)>`——括號內之 `X-<n>` 為交付欄唯一允許之內部代號
      （R-SEC15(c) 例外擴充），使審查者在交付本內即可回查 `asset_request.md`。
  (b) 三型：
      值型（檔名／字串／憑證）：`<wrong-subject certificate file provided by RD (X-e-2)>`、`<CS.212 log keyword for key injection failure provided by RD (X-h)>`
      觸發型（無執行手段）：步驟整行 `<DUT-side trigger for wrong-OID certificate verification provided by RD (X-e-3)>`，
                          其 `$` 指令行為 `$ <command provided by RD (X-e-3)>`；ER 對應行 `<observable outcome provided by RD (X-e-3)>`
      環境型（實體資產）：Pre-Condition `<ECU certificate chain for the DUT SSN provided by STLA (X-d)> is available`
  (c) 一行只換一處；不得把兩個 PENDING 合併成一個佔位。
  (d) Remarks 保留：`asset: X-<n> — <原 PENDING 全文>`；`placeholder_summary.tsv` 逐行記 `tc_id | field | line | x_token | original_pending | placeholder`。
  (e) lint：`U`（PENDING 計數）預期 0；新增 `SS` 判項——交付欄含 `<… provided by … (X-…)>` 者，Remarks 須含同一 `X-` 代號，否則 FAIL。
      `selfcheck` (b)：觸發型佔位視同觸發位之佔位（與 PENDING 同）。
  (f) 誠實條款：交付本 Cover 之 Remarks 或 Product Document 之備註格（依 SWC 量測有填者）不加註；
      改於 `asset_request.md` 首段明寫「本本含 96 處 RD 資產佔位，執行前須依本清單補值」，隨交付本同送。
```

**執行層回報（SEC-08）**：轉換 96 行；`placeholder_summary.tsv` **96 列**；
`U` 由 112 降為 **0**；新 `SS` 判項 **0**；`selfcheck` 九條 **0**。
(a) 之「交付欄唯一允許之內部代號」為 **R-SEC15(c) 之例外擴充**，
已於 `selfcheck_r_sec15.py` 之 (c) 判項加同一例外，否則兩條互斥。

---

### R-SEC20(amend) — 適用面之更正與引文豁免（Pei 准 SEC-08 review §一 #1／#3／#4，2026-09-17；SEC-10 §1）

```text
R-SEC20(amend)  適用面 = 037 VC 以 source code／build files／dependency graph 為受詞之列
                （CP-006 全部 sibling、CP-008 前兩 THEN、KI-012 之 Android.bp／Static Analysis 兩 sibling）；
                KI-013／CP-010 之 VC 為實機量測（procrank／df），不適用。混合型（CP-008）之 test_item 尾綴
                `(document review + log observation)`。
                (c) 補句：ER 引 037 逐字要件時，引文內之關係模糊語不受 IN §6 校準（lint `H` 對 `"…"` 內豁免，限 security）。
```

**執行層回報（SEC-10）**：8 TC 之適用面與 SEC-08 所執行者相同（A-25 為分析層計數錯登，條文於此更正）。
`NR1L-CP-017`／`-018` 之 `test_item` 尾綴改 `(document review + log observation)`（2 格）。
`H` 之豁免實作於 `FEATURE_EXEMPT["security"]`，**只吞落在 `"…"` 內之命中**，反例已驗（§SEC-10 上繳包 §3）。

---

### R-SEC7(amend2) — 通道與觀察面增列 DOC（Pei 准 SEC-08 review §一 #2，2026-09-17；SEC-10 §1）

```text
R-SEC7(a)(c) amend2  通道加 DOC：`<obtain <artifact> per RD>`／`Review <artifact> against "<要件>"`，免 `$` 行；
                     觀察面加 DOC：`<artifact> are available for review`／`<artifact> satisfy "<要件>"`。
                     出處：037 CP-006／008 VC `Inspect the build files`／`Inspect the source code`；KI-012 Verification Method `Document Review`。
```

**執行層回報（SEC-10）**：本條追認 SEC-08 已實作之 `SEC_DOC_STEP`（通道）與 `SEC_OBSERVE` 之 DOC 兩句式（觀察面），
以及 `selfcheck_r_sec15.py` (b) 之同式豁免。條文落檔後兩者不再是「超出授權之改動」。

---

### R-SEC21(b)(amend) — 第四型「步驟型」（Pei 准 SEC-08 review §一 #5／#6，2026-09-17；SEC-10 §1）

```text
R-SEC21(b) amend  第四型「步驟型」：`<<性質> provided by RD (X-<n>)> is executed` ＋ 次行 `$ <command provided by RD (X-<n>)>`；
                  「性質」逐字取原 PENDING 文字，不補 TC 語境；示例改為 `<log keyword provided by RD (X-h)>`。
```

**執行層回報（SEC-10）**：v04 之四型計數 觸發 30／步驟 **11**／結果 24／值 31 = 96，與本條相符；
v05 不變（本包未改佔位）。

---

### R-SEC22 — CCVR 衝突與範圍之 Remarks 定式（Pei 裁，2026-09-17；SEC-09 review §一／SEC-10 §1）

```text
R-SEC22  CCVR 衝突與範圍之 Remarks 定式
  (a) `conflict: <SYS2 對照> — <十字內短述>; unresolved per CCVR Mapping notes row <r>`
      CP-007／009 全部 sibling（`NR1L-CP-015`／`-016`／`-019`／`-020`）：`conflict: 543/546 vs 226; 517 vs 520 — root & CA lifecycle; unresolved per CCVR Mapping notes row 12`
      SWDL 全部（`NR1L-SWDL-001`~`-006`）：`conflict: 344 vs Auth-Prog item 7 — rollback; unresolved per CCVR Mapping notes row 13`
      KI-009／010 全部 sibling（`NR1L-KI-016`~`-019`）：`conflict: 376/509/511 vs 510 vs 514 — key strength; unresolved per CCVR Mapping notes row 14`
      CP-004／005 全部 sibling（`NR1L-CP-007`~`-010`）：`conflict: 529/383/532/539 — DCL not deployed; unresolved per CCVR Mapping notes row 10`
      ECUCert EXPORTCSR（`NR1L-ECUC-010`）：`conflict: 562~565 — CSR format evidence pending; unresolved per CCVR Mapping notes row 15`
  (b) `scope: service-level validation; reprogramming rejection owned by SWDL (CCVR Cert Val CS.98 rationale)`
      → `NR1L-CP-002`／`-004`／`-006`／`-007`／`-008`／`-009`／`-010`／`-023`
  (c) CCVR 引用一律 `item <n>`；`NR1L-SWDL-005`／`-006` 之 `rows 3/5/6/7/8` → `items 3/5/6/7/8`。
  (d) 皆為 Remarks 增行；lint 不新增判項。
```

**執行層回報（SEC-10）**：19 TC 加 `conflict:`（4＋6＋4＋4＋1）、8 TC 加 `scope:`、2 TC `rows`→`items`；
合計 **29 TC** 之 Remarks 增／改行，交付欄不動。`NR1L-CP-007`~`-010` 同時落 (a) 與 (b)（兩行併存）。

---

### R-SEC23 — DEFERRED 列之產出（R-SEC11(b) 之解凍）（Pei 指示「請先繼續產出」，2026-09-17；SEC-11 §1）

```text
R-SEC23  DEFERRED 列之產出（R-SEC11(b) 之解凍）
  (a) `disposition = D` 之 19 列（LOGENC 001/002/003/004/005/007/008/009；ECUCert SERVICE_BINDER／ECUONLINE_BINDER／
      ECUCERT_JNI／STORAGE_IO／ECUONLINE／ECUONLINE_DOWNLOADCERT_INTF；SWDL 001/002/005；SAM 0001/0019）
      依 R-SEC20 文件審查定式產出 TC；`disposition` 改 `CONVERT_DOC`。
  (b) sibling：037 `Verification Criteria` 之每一可獨立審查之要件（THEN 子句或列舉項）= 1 TC；無 VC 而只有 Description 者，
      以 Description 之每一 `shall` 子句為要件。artifact 依 037 受詞逐字（`source code`／`library`／`interface`／`build files`）。
  (c) Priority 依 R-SEC16 = P2；Design Method `功能測試 (Functional based ; no specific technique)`；`test_item` 下半加 `(document review)`。
  (d) Remarks 首行 `verification: document review (R-SEC23; upstream DR-a/i/r pending)`；ECUCert 六列之 ID 依 R-SEC3(b) 用 SYSAD 首值。
  (e) 上游回覆後之處置：DR-a（ECUCert 補 SWE ID）→ Revise 只改 ID 欄；DR-i／r → 不影響本群；若 037 作者將任一列改為 Testing
      且給出可執行 VC，該列依 R-SEC4 重寫，文件審查 TC 作廢（R-TM13 保留舊本）。
```

---

### R-SEC22(a)(amend) — C3 落點加 LOGENC-004 兩 sibling（Pei 准 SEC-11 review §一 #1，2026-09-17；SEC-12 §1）

```text
R-SEC22(a) amend  C3（金鑰強度）之落點加 `NR1L-LOGENC-007`／`-008`（SWE1-LOGENC-004 之兩 sibling）；
                  Remarks 增 `conflict: 376/509/511 vs 510 vs 514 — key strength; unresolved per CCVR Mapping notes row 14`。
```

**執行層回報（SEC-12）**：`CONFLICT_NOTE` 加 `SWE1-LOGENC-004`；v06 → v07 之逐格 diff 即該兩 TC 之
`remarks` 2 格。C3 之 `tc_ids_found` 6 筆自此全數帶註（A-30 為分析層自報之漏列）。
