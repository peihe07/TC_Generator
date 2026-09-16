# trace_summary —— Security 三段追溯實測

由 `features/security/scripts/build_trace_matrix.py` 產生，可重跑。
來源一律 `sources/raw/<doc_id>/`。

## 1　每本 037 之 match_kind 計數

| 037 | exact | base | mixed | none | 列 |
|---|---|---|---|---|---|
| `swe1_037_certprovider_v1_0` | 11 | 0 | 0 | 0 | 11 |
| `swe1_037_keyinstall_v1_0` | 13 | 0 | 0 | 0 | 13 |
| `swe1_037_sam_v1_1` | 19 | 0 | 0 | 0 | 19 |
| `swe1_037_ecucert` | 13 | 0 | 0 | 0 | 13 |
| `swe1_037_swdlsecurelib` | 5 | 0 | 0 | 0 | 5 |
| `swe1_037_liblogencrypt` | 9 | 0 | 0 | 0 | 9 |
| **合計** | 70 | 0 | 0 | 0 | 70 |

查詢條件：SWE1 `Analysis Report` row 9 起，A 或 B 欄非空；B 欄以換行／逗號／空格三分隔拆；SYSAD 去所有空白後比對；`base` 只在 `exact` 落空時試（去 `_COMP`／`_INTF`／`_API`／`_BINDER`）。
`mixed` = 同列多個 SYSAD，部分命中部分未命中。

## 2　SYS2 命中

- 鏈上 SEC ID 併集：**161**
- 在 `SYS2 traceability`（A 欄）命中：**161／161**，缺 0
- `SYS2 traceability` 總列（A 欄非空且為 SEC）：737

`Existing test relationship`（I 欄）分佈：

- No existing test mapped：103
- Partial / conditional test link：35
- Direct test link：8
- Reference / information：8
- Reference / information linked：4
- Conflict：1
- Heading：1
- Source: out of scope：1

`HARMAN status`（G 欄）分佈：

- Accepted：88
- Rejected：53
- (空)：20

## 3　ccvr_batch 計數（R-SEC1(b)）

- batch 1（落 CCVR 五 test item）：**52** 列
- batch 2（未落）：**18** 列
- 合計：70 列

| 元件 | batch 1 | batch 2 |
|---|---|---|
| CertProvider | 11 | 0 |
| KeyInstall | 13 | 0 |
| SAM | 6 | 13 |
| ECUCert | 13 | 0 |
| SwdlSecureLib | 5 | 0 |
| libLogEncrypt | 4 | 5 |

## 4　無落地來源清單（R-SEC4(b)：PENDING 候選）

共 **0** 列（清單 `data/no_step_source.tsv`）。


## 4b　每步可配通道之預判（R-SEC7／_E §3）

判準：`Y` = 有 APK／PDF／CS98／CS165 任一外部可執行素材；
`N` = VC 受詞為 source code／build environment 且無具體指令；`部分` = 其餘。

- `Y`：**42** 列
- `部分`：**8** 列
- `N`：**20** 列 —— 即 batch 內之 `PENDING` 候選（R-SEC4(b)）

| SWE1 ID | 元件 | batch | 預判 | 依據 |
|---|---|---|---|---|
| `SWE1-SAM-0001` | SAM | 1 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-SAM-0002` | SAM | 1 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0003` | SAM | 2 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-SAM-0004` | SAM | 1 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0005` | SAM | 2 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0006` | SAM | 2 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0007` | SAM | 2 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0008` | SAM | 2 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-SAM-0009` | SAM | 2 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-SAM-0010` | SAM | 2 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-SAM-0011` | SAM | 2 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-SAM-0012` | SAM | 2 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0013` | SAM | 2 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0014` | SAM | 2 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0015` | SAM | 1 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-SAM-0016` | SAM | 2 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-SAM-0017` | SAM | 2 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-SAM-0018` | SAM | 1 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-SAM-0019` | SAM | 1 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-LOGENC-001` | libLogEncrypt | 2 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-LOGENC-002` | libLogEncrypt | 1 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-LOGENC-003` | libLogEncrypt | 1 | **N** | VC 無具體指令／路徑／值，且無外部素材 |
| `SWE1-LOGENC-004` | libLogEncrypt | 1 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-LOGENC-005` | libLogEncrypt | 2 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-LOGENC-006` | libLogEncrypt | 1 | **部分** | VC 含具體指令／路徑／值，惟無外部素材補齊全部步驟 |
| `SWE1-LOGENC-007` | libLogEncrypt | 2 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-LOGENC-008` | libLogEncrypt | 2 | **N** | VC 受詞為 source code／build environment，無外部入口 |
| `SWE1-LOGENC-009` | libLogEncrypt | 2 | **N** | VC 受詞為 source code／build environment，無外部入口 |

## 4c　CertProfile 之欄位斷言落地（_F §2／§5）

- CertProvider 共 **11** 列。
- 其中 **5** 列之欄位斷言可由 `CertProfile` **逐字**落地（`SWE1-CertProvider-001`、`SWE1-CertProvider-002`、`SWE1-CertProvider-003`、`SWE1-CertProvider-005`、`SWE1-CertProvider-011`）。
- 其餘 **6** 列只掛「全」列適用之演算法／Validity 斷言。
- 標 `REF:DR-SEC-q`（SAM 樹／ECU Identity 樹 profile 未到手；**R-SEC8(h) 已降級為 reference，不作 PENDING 理由**）：**16** 列 —— CertProvider 之 SAM 分支 2 列、`SWE1-SAM-0007`、ECUCert 全 13 列。

> **限制**：CertProfile 為 **BETA/preprod ROW** 本。PROD 樹（CS.98 第 10 項）之 CN 與 CDP 必不同，
> PROD 場景之值一律 `PENDING: DR-SEC-c/… PROD cert profile`。
> OID 尾碼（`1.3.6.1.4.1.57872.` 之後）sheet 未給實值 → 保留佔位 `<…>`，不造值（IN §8.4.1）。


## 5　apk 方法交叉核對（任務 3 規則 7）

- `Test_Items.txt` 之方法：**15** 條
- `Cert Val CS.98` STEPS 抽出：**2** 條
- 交集：**2** 條

- 交集清單：ecuCertTestSelfSignedChain, samCertTestNormalFlow
- 只在 `Test_Items.txt`：ecuCertTestBrokenChainCert, ecuCertTestNormalFlow, fotaMcpuCertStressTest, fotaMcpuCertTestBrokenCert, fotaMcpuCertTestNormalFlow, fotaMcpuCertVerifyStressTest, fotaMcpuVcpuCertStressTest, fotaMcpuVcpuVerifyCertStressTest, fotaVcpuCertTestNormalFlow, secondPartyLevelThreeCertATestNormalFlow, secondPartyLevelThreeCertBTestNormalFlow, secondPartyLevelThreeCertCTestNormalFlow, secondPartyLevelTwoCertTestNormalFlow
