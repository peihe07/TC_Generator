# ERROR_CODES — `Error_Code_List.xlsx` 錯誤碼台帳（SW Update）

來源：`inputs/Error_Code_List.xlsx` 分頁 `Error Code List`｜sha256 `4625753c…`｜**Pei 裁可用**（R-SU35，2026-08-28）。

**本表為引用來源，不是錨點來源** —— `specification_reference` 仍走 CFTS057（R-SU35(b)2）；本表之引用記於 `reasoning`，格式 `Error_Code_List.xlsx <分頁> <碼>`。

**碼值與 Description 一律 verbatim**（R-SU35(b)1），含原文之拼寫殘留（如 `335890` 之 `sessiion`）—— **不改正**，同 D-4 之處置。

> ⚠ **碼有了，看碼的地方還沒有**（R-SU35(b)3）——
> 錯誤碼於 HU 上之呈現途徑為 **DR-SU2 v2(a)** 之未解項；
> 未答前，觀測步驟一律掛 `PENDING: DR-SU2`。二者不得混同。

> ⚠ **`Test Set 候選`欄之粒度**：除下放包 30 §四所補之 5 碼有**逐碼依據**外，
> 其餘為 **R-SU35(a) 之階段級對照**，即一個粗粒度之代理。
> **候選非裁定** —— 逐碼之正解須自碼之 Description 讀出其失敗情境，
> 再對照該 Test Set 所轄之 037 列；本輪未做（80 碼之工作量）。
>
> ⚠ **本表為 USB／SWDL 路徑**（R-SU35(c)1）——
> **不得引用以充當 Wi-Fi FOTA session 之觀測面**（DR-SU2 v2(b) 未解）。

---

## 閉合檢查

| 項 | 值 |
|---|---:|
| 分頁之碼列數 | **80** |
| 本台帳之碼數 | **80** |
| 階段標題數 | **10** |
| 相符 | ✅ |

### 階段別碼數

| 階段（分頁原文） | 碼數 | **Test Set 候選（R-SU35(a)）** |
|---|---:|---|
| `After HU start-up, suddenly` | 4 | `Update Agent` |
| `Precondition` | 7 | `USB Update` |
| `Package Header check & unpack` | 13 | `Integrity Verification` |
| `Rollback Protection *This function supports only user build.` | 3 | `Update Agent` |
| `Security check` | 4 | `Integrity Verification` |
| `Install ( M-CPU )` | 6 | `Interruption Handling`／`Update Agent` |
| `Install ( M-CPU: Redbend ) Note: These error code is not defined by melco` | 1 | `Interruption Handling`／`Update Agent` |
| `Install ( V-CPU )` | 24 | `Interruption Handling`／`Update Agent` |
| `Install ( SXM )` | 17 | **不用**（非本 feature 範圍） |
| `RedBend update engine` | 1 | `Update Agent` |

---

## 逐碼

| 碼 | Description（verbatim） | 階段 | 平台限定 | Test Set 候選 | 註 |
|---|---|---|---|---|---|
| `327680` | General VCPU FW update error | `After HU start-up, suddenly` | — | `Update Agent` | **逐碼依據**（下放包 30 §四）：V-CPU 更新之總括錯誤，其單元為更新執行本身 |
| `393216` | Report PBL mode enter | `After HU start-up, suddenly` | — | `Update Agent` | **逐碼依據**（下放包 30 §四）：前次更新失敗後之復原態（`381` recovery） |
| `393217` | Report HU is in bricked state - two or more VCPU update were failed | `After HU start-up, suddenly` | — | `Update Agent` | **逐碼依據**（下放包 30 §四）：`379`／`380` failsafe 與防磚之失效表現 |
| `393219` | Version sync error | `After HU start-up, suddenly` | — | `Update Agent` | **逐碼依據**（下放包 30 §四）：安裝後版本未登錄，屬 `383` deployed software validation 之失效 |
| `-` | Cannot update software. Software not compatible with vehicle. | `Precondition` | — | `USB Update` |  |
| `1` | ERROR_GENERAL | `Precondition` | — | `USB Update` |  |
| `2` | ERROR_GENERAL_FILE_IO | `Precondition` | — | `USB Update` |  |
| `1048577` | USB memory removed Error | `Precondition` | — | `USB Update` |  |
| `1048578` | Data Size Error | `Precondition` | — | `USB Update` |  |
| `1048579` | Copy Error | `Precondition` | — | `USB Update` |  |
| `1048580` | Too many update packages available on USB device | `Precondition` | — | `USB Update` |  |
| `65537` | Package Header Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65538` | Package Version Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65539` | Format Version Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65540` | M-CPU header Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65541` | M-CPU filelist Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65542` | M-CPU version Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65543` | V-CPU header Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65544` | V-CPU filelist Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65545` | V-CPU version Error | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65552` | Error unpacking FWEK | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65553` | Package contains wrong format version | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65554` | MCPU update binary is missed in the package | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `65555` | VCPU update binary is missed in the package | `Package Header check & unpack` | — | `Integrity Verification` |  |
| `3145729` | Rollback protection error if trying to install older SW | `Rollback Protection *This function` | — | `Update Agent` |  |
| `3145730` | Rollback protection error if trying to install same SW | `Rollback Protection *This function` | — | `Update Agent` |  |
| `3145731` | Update package integrity check is failed | `Rollback Protection *This function` | — | `Update Agent` |  |
| `131073` | M-CPU decryption Error | `Security check` | — | `Integrity Verification` |  |
| `131074` | M-CPU signature Error | `Security check` | — | `Integrity Verification` |  |
| `131075` | V-CPU decryption Error | `Security check` | — | `Integrity Verification` |  |
| `131076` | V-CPU signature Error | `Security check` | — | `Integrity Verification` |  |
| `196634` | Update data incompatible | `Install ( M-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `196659` | Android timestamp check failure | `Install ( M-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `262145` | Redbend result file read/write error *Not support at GEN1 | `Install ( M-CPU )` | **`*Not support at GEN1`** | `Interruption Handling`／`Update Agent` |  |
| `262146` | Update engine failed to apply payload | `Install ( M-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `262147` | Update engine no configuration error | `Install ( M-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `262148` | Redbend update - cannot remove artifacts error *Not support at GEN1 | `Install ( M-CPU )` | **`*Not support at GEN1`** | `Interruption Handling`／`Update Agent` |  |
| `-2147483330` | CRC Signature mismatch | `Install ( M-CPU: Redbend ) Note: T` | — | `Interruption Handling`／`Update Agent` | ⚠ 與 `2147483330` **符號相反、數值相同**，為同一底層錯誤之二種呈現 —— **引用時須連同符號逐字抄**（R-SU35(b)1） |
| `335872` | General Slave Error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `335873` | Sequence Error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `335890` | Download not possible - last sessiion interrupted | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `336384` | General Hardware error on slave | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `336385` | Error deleting flash memory | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `336386` | Error writing flash memory | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `336642` | CRC32 check failed | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `336643` | Failsafe check V-CPU Secure or Non-secure | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `336896` | Interface mixed error (Sequece Error) | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `368640 ~ 369663` | Install(V-CPU) Security Errors. xxx indicates error code from "V-CPU". Major V-CPU errors are the following. | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `368964` | Install(V-CPU) Security Error. SWDL size MAC error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `368994` | Install(V-CPU) Security Error. BOOTMAC ID error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `368995` | Install(V-CPU) Security Error. SWDL data length error (First) | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `368996` | Install(V-CPU) Security Error. SWDL data length error (Second) | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369220` | Install(V-CPU) Security Error. SWDL Root Cert. MAC error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369358` | Install(V-CPU) Security Error. SWDL Cert. MAC error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369371` | Install(V-CPU) Security Error. SWDL Sig. MAC error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369374` | Install(V-CPU) Security Error. SWDL Sig. hash verify error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369490` | Install(V-CPU) Security Error. SWDL RSA public key error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369490` | Install(V-CPU) Security Error. Key protection error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369492` | Install(V-CPU) Security Error. Key empty error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `369495` | Install(V-CPU) Security Error. BOOTMAC update error | `Install ( V-CPU )` | — | `Interruption Handling`／`Update Agent` |  |
| `372736` | SPI Busy (*Not support at GEN1) | `Install ( V-CPU )` | **`*Not support at GEN1`** | `Interruption Handling`／`Update Agent` |  |
| `372992` | SPI Error (*Not support at GEN1) | `Install ( V-CPU )` | **`*Not support at GEN1`** | `Interruption Handling`／`Update Agent` |  |
| `458752` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458753` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458754` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458755` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458756` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458757` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458758` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458759` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458760` | Not an actual error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） | **不作失敗判準**（R-SU35(c)3） |
| `458761` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458762` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458763` | Not an actual error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） | **不作失敗判準**（R-SU35(c)3） |
| `458764` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458765` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458766` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458767` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `458768` | Common SXM installation error | `Install ( SXM )` | — | **不用**（非本 feature 範圍） |  |
| `2147483330` | Source ↔ Target versions mismatch | `RedBend update engine` | — | `Update Agent` | **逐碼依據**（下放包 30 §四）：`382` differential update 之來源／目標相容性失效｜⚠ 與 `-2147483330` **符號相反、數值相同**，為同一底層錯誤之二種呈現 —— **引用時須連同符號逐字抄**（R-SU35(b)1） |

> **逐碼依據已套用 5 / 5 碼**（下放包 30 §四之補裁）。

---

## 引用時之拘束（R-SU35 摘）

1. ER 得寫「對應之 error code 被報告」並具體列碼（如 `error code 335890 is reported`）；**碼值 verbatim，不得自造或改寫**。
2. `specification_reference` **不列本表**；引用記於 `reasoning`。
3. 讀碼位置未定前，該觀測步驟掛 `PENDING: DR-SU2`。
4. 平台限定之碼（`*Not support at GEN1`，**4 碼**）引用時須連同限定一併記。
5. `458760`／`458763`（`Not an actual error`）**不作失敗判準**。
6. **正向路徑不因本表而有觀測面**（R-SU35(d)）——本表解的是「失敗時看什麼」，不是「成功進行中看什麼」。
