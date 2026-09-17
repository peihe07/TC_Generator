# Diagnostics —— 佔位填值請求（asset request）

依 **R-DIAG15**（比照 R-SEC21）。對應 `sandbox/placeholder_summary.tsv`（**394 行／245 條 TC**）。
母體：`diagnostics_v06.xlsx` 合併本 **432 列**（Layer 2 19 組全產／318 個 037 列，81.7%）。

---

## ⚠ 執行前提

**佔位填入前不得執行。** 交付本之 `test_procedure` 與 `expected_result` 含
`<…>` 佔位者，測試者知道**要送什麼服務、選什麼項目、讀哪個 DID**，
但**不知道要送哪些位元組**。在下列**五**項到件前，這些用例只可用於評審，不可派工。

lint `U`（PENDING 佔位）於合併本 `v06` 為 **3**（`-281` 二行、`-297` 一行，皆 `DR-DIAG-1`）——
佔位不是 PENDING；PENDING 是**無法書寫**之步驟，佔位是**已定形但缺值**之欄位。

---

## 一　`DR-DIAG-4` —— I/O Control 之 controlOptionRecord／controlEnableMask（**61 行**）

**缺件**：`$5000`／`$5001`／`$5002`–`$5006`／`$5008`／`$5009`／`$500A`–`$500D`／`$5100`
等 15 個 I-O Control DID 之 controlOptionRecord 與 controlEnableMask **全表**，
含每個可選項對應之位元組值。

**來源現況**：CFTS004 以自然語言列出可選項 ——

| 節 | 列 | 原文（節錄）| 缺 |
|---|---:|---|---|
| `$5000` | r330–r337 | `The 7 kHz Tool controlled tone shall be selectable in this DID.` 等九條 | 各音調之位元組值 |
| `$5000` | r328 | `The following tones shall be selectable in this DID:` | **列表未隨匯出帶出** |
| `$5001` | r315／r316／r318／r319 | `The Rear Right speaker outputs shall be selectable using this DID.` 等四條 | 各象限之位元組值 |
| `$5001` | r320 | `The following speaker outputs shall be selectable using this DID:` | **列表未隨匯出帶出** |

**典型佔位**：`<7 kHz Tool controlled tone selection>`、`<Front Left speaker selection>`、
`<enable in-motion menu>`、`<video input selection>`、`<volume step = 38>`。

---

## 二　`DR-DIAG-5` —— 資料位元組之值域與 record 版面（**139 行**）

**缺件**：

| 佔位 | 所屬 DID | 缺 |
|---|---|---|
| `<brightness byte>` | `$283F` | 亮度值域（CFTS004 `$283F` 四列皆未載）|
| `<AV Channel Number>` | `$0312` | 通道號之列舉（CFTS004-4940474 只述其「portion 指示哪一個輸入」）|
| `<module version record>` | `$2843` | **19** 個子欄位之 record 版面與位移（SXI／RF／Mod SW／HDEC Rev 各 Major/Minor/Inc、Module Type ID A–C、Module HW Type B/C ＋ HW Rev A、Capability）。CFTS004-4939842 只書「the following items」而未給版面 |
| `<signal quality record>` | `$2841` | 16 個子欄位之 record 版面與位移 |
| `<push button status record>` | `$1820` | 12 個按鍵之位元對應 |
| `<steering wheel button status record>` | `$1821` | 同上 |
| `<routine results>` | `$0312` | Video／Audio Left／Audio Right 三訊號之結果編碼 |
| `<…設定 byte>` 各式 | `$280C`／`$2870`／`$5002`–`$5006` 等 | 各設定之位元組表示 |
| `<Sirius XM subscription data record>` | `$2844` | 8 個子欄位（Suspend year／month／day、Reason Text／code、Radio ID、Phone Number、Subscription status）之 record 版面與位移 |
| `<CA Pellet status record>`／`<CA Pellet validation status record>`／`<Event data record>` | `$2848`／`$2846`／`$2845` | 各自之回報編碼 |
| `<package select routine results>`／`<package validation routine results>` | `$0309`／`$0307` | 結果 record 之版面（Indication Code 之位元組位置）|

---

## 三　`DR-DIAG-6` —— **不支援之 SID 與 DID 清單**（R-DIAG22(amend) 改題）

**缺件**：本 ECU **不支援之 UDS 服務識別碼**至少一個，**以及不受支援之 DID 至少一個**。

unsupported 型之 037 列（93 列）要求「送出不支援之服務請求並回 `serviceNotSupported`」，
但**哪一個 SID 不被支援**是 ECU 實作事實，CFTS004、037、SYSAD 三處皆未載。
SYSAD §4.5 只正面列出**支援**之三項（`0x22`／`0x2E`／`0x31`），未給不支援清單。

**佔位**：`<unsupported SID>`（Procedure 與 ER 各一）與 `<unsupported DID>`（R-DIAG22(amend) 後之讀類值域軸）。

**`<unsupported DID>` 之由**：R-DIAG22(amend) 裁定 `0x22` 讀類之 negative 第二軸改為「unsupported DID」型 ——
`22 <DID>` 請求本無資料位元組，「值域」無處可填；而 037 negative 列原文之第三種失效型態正是 `unsupported DID`，
ISO 14229-1 之 `31 requestOutOfRange` 亦即「DID 不受支援」之碼。

**問**：請提供本 ECU 之 **UDS 服務支援矩陣**與 **DID 支援清單**，或各指定一個確定不支援之 SID／DID 供測試使用。

---

## 四　`DR-DIAG-7` —— `KeySense HMI Logic and Flow`（**文件缺件，非佔位**）

`CFTS004-4940469`（`$030A - Clear Key Sense PIN`）明引該件為常式行為之唯一定義來源，
而該件不在來源集、CFTS004 亦未載其文件編號與版本。名稱逐字取自引用處。

**影響**：`NR1L-DIAG-290` 之 ER 目前只斷言常式正回應與完成（R-DIAG19）。到件後以 `_Revise{n}` 補實。

---

## 五　`DR-DIAG-8` —— `SX-9830-0095` 本文 ＋ PkgIndex 對照（**PARTIAL**：流程圖已到）

`CFTS004-4940451`／`-4940461`／`-4940450`／`-4940462` 明引兩件為 `$0307`／`$0309` 兩常式之處理步驟與重試路徑之來源。

**`CIP Radio Tables` 已於 2026-09-16 置於 `forms/`，CDD-12 登錄為 `cip_radio_tables_v6_7`**（v6.7，2023-03-03）——
兩張 MPFA 流程圖已逐節點轉錄（`features/diagnostics/data/cip_mpfa_flowcharts.md`），retry 之五種結局據以產出。
**本項改 PARTIAL，餘下列兩件：**

| 仍缺之件 | 為何需要 |
|---|---|
| `SX-9830-0095` "Sirius XM Multi-Package Factory Activation OEM Requirements" 本文 | `Package Indication value` 之編碼定義於此；流程圖只書「依 vehicle sales codes 決定 PkgIndex」，未給值 |
| vehicle sales code → PkgIndex 對照表 | 同上；`CIP_Radio_Tables_v6.7` 之 12 分頁均無此表 |

**佔位**：`<Package Indication value>` —— 該值之編碼定義於 `SX-9830-0095`，流程圖不含，故佔位維持。

**已可寫者**：Indication Code **不缺** —— `CFTS004-4940456` 逐字列出全表八碼
（`$00`／`$03`／`$0C`／`$0D`／`$0E`／`$0F`／`$10`／`$FF`），`$0309` 另明載 `$10` 無效。
故 results 型 TC 之 ER 直接列舉，未用佔位。

**已解之部分**：retry 路徑之五種結局（600 ms timeout ×3 → `$FF`／`$03`／`$0D`／`$0F` 各 ×3 → 該碼／混合 → `$FF`）
已依流程圖 NOTE 逐字產出，`$0307`／`$0309` 各 5 條（CDD-12）。

**仍受限者**：`Package Indication value` 之實值；流程圖之 `Store the OpCode`／`CA Pellet Creation` 後續不在本 feature 範圍（§8.2.1）。

---

## 六　`DR-DIAG-1` —— 殘餘 3 列之 NRC（**非佔位，記此備查**）

`SWE1-Diagnostics-156`／`-157`（037 row 163／164）／`-237`（row 244）之 NRC 於 CFTS004、037 皆未載，
且 037 未述失效型態，故 R-DIAG5(amend)(d) 之封閉五碼無可對應者。
`-156`（`NR1L-DIAG-281`）與 `-237`（`NR1L-DIAG-297`）已產出並寫 `PENDING: DR-DIAG-1`。

---

## 七　到件後之處置

依 **R-G72**：已交付本不就地改，以 `_Revise{n}` 本發出；
`placeholder_summary.tsv` 逐行對照填值，填畢後該行自表移除。
