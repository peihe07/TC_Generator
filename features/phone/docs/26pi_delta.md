# 26PI delta — MPA11／MPA12（Phone HMI Logic & Flow R1）

> **本檔只抽 MPA11、MPA12 兩條**（下放包 PH-01 §任務 2 第三項）。
> 供 Pei 日後裁增補之用；**本輪不併入**（R-PH2）。

## 出處

| 項 | 值 |
|---|---|
| 來源檔 | `Phone HMI Logic&Flow R1.pdf`（doc_id `phone_hmi_lf_pdf_26pi`） |
| sha256 | `7180b8aff2eaee309679eaeba93867b45a36417c0833d9ab854c2dd0b2dc5ed8` |
| 頁 | p.2「Assumptions ／ Multiphone Assumptions:」章（全檔 21 頁） |
| 抽取法 | `pdfplumber` 取 word 之 `(top, x0)` 重排；**不用 pdftotext**（見 A-PH02） |
| 抽取日 | 2026-09-07 |

## 原文（逐字）

```text
MPA11    Awaiting review    LOGICAL
Multiphone not applicable for R1L-R
```

```text
MPA12    Awaiting review    LOGICAL
(R1L‑R only) Refer to the Device Manager HMI L&F for all device management requirements.
```

> MPA12 之 `R1L‑R` 中之連字為 U+2011（NON-BREAKING HYPHEN），非 U+002D；
> MPA11 之 `R1L-R` 為一般 U+002D。逐字照錄，不統一。

## 變更日誌之對應列

`Phone HMI Logic&Flow R1 Change Log(26PI).xlsx` 分頁 `26PI` 第 9 列（唯一資料列）：

| # | Version | Date | Containing Document | Section | Items | Logic | Description of Changes | Rationale | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 26PI | 05/20/2026 | Phone HMI Logic&Flow | Assumptions | MPA11 and MPA12 created. | X | Added assumptions to clarify device managing and multiphone aspects for R1L-R | Establishing availability of functionality | Under Review |

## 查找結果（下放包 §4 任務 3-5）

| 查詢 | 對象 | 命中 | 預期 |
|---|---|---|---|
| `MPA11` | 037 全欄 | **0** | 0 ✅ |
| `MPA12` | 037 全欄 | **0** | 0 ✅ |
| `MPA11` | SYS1（兩版皆查） | **0** | 0 ✅ |
| `MPA12` | SYS1（兩版皆查） | **0** | 0 ✅ |

## 待裁事項（不自行處置）

1. **MPA11「Multiphone not applicable for R1L-R」與本 feature 之客戶側名稱
   「Bluetooth, Multiple Phones Paired Simultaneously」在方向上相反。**
   若 R1L-R 為本輪目標車型，則 26PI 之後 Multiphone 條文（037 之 MP／MPA／MPS／
   MPP／MPDND／MSMS 前綴列，實測 parent 35 列／含其 child 共 143 列）之效力存疑。
   此為**具名之未決事實**，非本包之裁定；登 `DR-PH02`。
2. 037 V0.1 之基線為 SR24 Post 2A（June 21 2022），**早於 26PI**；
   MPA11／MPA12 未載於 037 係版次落差之必然，非 037 之瑕疵。
3. 變更日誌記 `05/20/2026`，而 PDF p.1 之變更列記 `May 11 2026` —— 二者相差 9 日，
   逐字照錄，不調和（A-PH03）。
