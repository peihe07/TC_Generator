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
