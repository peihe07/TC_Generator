# RULINGS — Privacy (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄，執行層之回報另起段落。
本檔為 Privacy 之裁決權威；跨 feature 條文承接時註明來源包。

**檔案建立於 2026-08-13**（下放包 01 §4.1）。此前 Privacy 之裁決
（R-PV01(a)(c)、R-PV02）記於 `DECISIONS.md` §8 與 `ANOMALIES.md` 各條，
未另立本檔 —— 兩處內容不因本檔建立而失效，見文末「既有裁決索引」。

---

## R22 — 稽核方法學條文（承接自 07 包上繳，分析層自裁，2026-08-13）

```text
[RULING] R22 — 稽核方法學條文（承接自 07 包上繳，2026-08-13）

R22-1  稽核之時態限縮
  裁：hash 稽核只證明「現在相符」，不證明「從未被覆寫」。
      若某檔曾被覆寫、隨後又自客戶樹重新複製，稽核仍顯示 MATCH。
      結論措辭一律限縮為現在式。
  §5a：**稽核之時態必須寫明。「相符」是現在式陳述，「未曾發生」是
      完成式陳述，前者不蘊含後者。**

R22-2  NO_COUNTERPART 之語意
  裁：其嚴格語意為「客戶樹內**無同名檔**」，**不等於「無對應檔」**。
      先例：SXM 之 inputs 工作簿 SHA256 cd876c202c71… 即 FW036 空白
      範本，對應檔存在但客戶樹內檔名為 …_SWQT_20260121.xlsx，
      basename 索引不命中。
  §5a：**以檔名為索引之比對，其陰性結果只能陳述索引層事實，
      不得升格為內容層結論。**

R22-3  白名單 vs 既存違規清單之性質差異
  裁：`tests/` 之寫回路徑 ratchet 測試中，白名單為**永久豁免**，
      既存違規清單為**待清償之債**。
      入白名單需要「確定不會成為交付件」之積極證據；
      不確定者一律留在債務清單（誤列於此之代價僅為多修一處）。
      `scripts/translate_xlsx.py` 與 `backend/api_server.py:2370`
      維持 ACTIVE，不入白名單。

R22-4  ratchet 測試之三項實作 —— 追認
  (a) 雙向約束（清單陳舊亦 FAIL）：追認。無人修剪之 baseline 會停止
      代表任何東西。
  (b) 以每檔呼叫數而非行號為判準：追認。封存標頭使行號位移。
  (c) 作業順序得由執行層調換並回報：追認，立為通則 ——
      **下放包所列作業順序若與其內容之相互影響衝突，執行層得調換
      並於上繳包載明。**

R22-5  分類承載因果假設時之處置
  裁：當分類架構本身承載因果假設時，**未經裁定不得施加分類**；
      應停在原始量測並回報。
```

### 執行層回報（下放包 01，2026-08-13）

R22-1 ~ R22-5 全數承接生效。本包 §2 之基準確認即為 R22-1 / R22-2 之首次適用：
結論措辭已限縮為現在式，`NO_COUNTERPART` 一類本次為 0 件故未觸發 R22-2，
但方法學限制仍於上繳包載明。

**R22-6 未簽署** —— `backend/api_server.py` 一字未改。

---

## R23 — Privacy 範本相關八條（Pei 簽署 2026-08-13，回覆「照建議」）

```text
[RULING] R23 — Privacy 範本相關八條（Pei 簽署 2026-08-13，回覆「照建議」）

R23-1  A-PV01 交付形態 —— 以通用範本產生 Privacy 交付件即為最終形態
  裁：不另索 Privacy 專屬 workbook。
  依據：範本第 10 列原廠樣本為 NR1L-AntiTheft-001，該範本本即供各
        feature 各自開工之用。
  A-PV01 由 PENDING 轉 RESOLVED。

R23-2  A-PV04 VF651_V2_R2 基線追認
  裁：`inputs/` 現有之 SHA256 `d5813bb7…`（146,929 bytes）為
        **HDCC28 平台基線**，與 `VF/VF_Split document/HDCC28_Split/`
        同源（hash 相同，非僅 size 相同）。
        `28HDCC_2A_LTM/…` 之 `7b5fc875…` 確為不同內容，不得假設為重存。
        DT 系列（DT27 / DT28）另三種內容不列入本專案。
  A-PV04 由 PENDING 轉 RESOLVED。

R23-3  A-PV05 SYSAD 分類
  裁：`SYS3_PrivacyMode_System Architectural Design_SYSAD_V1.docx`
        於 `feature.yaml` 標為 **context-only**。
        **不得**作為 `specification_reference`（§10.7 禁引分析類文件；
        SYSAD 屬設計非規格）。其角色限於背景理解。
  A-PV05 由 PENDING 轉 RESOLVED。

R23-4  A-PV07 殘留樣本列清除計畫 —— 核可修訂版
  裁：核可 2026-08-13 修訂版計畫，即：
        (1) 僅清 **D10 / F10 / G10 / S10 / D11** 五格之值
        (2) 方式為 zip 層就地改寫：
            `<c r="D10" s="81" t="s"><v>44</v></c>` → `<c r="D10" s="81"/>`
            —— 值清除、`s=` 樣式屬性原地保留
        (3) **B 欄不清** —— B10 為公式 `=IF(ISBLANK($D10),"",ROW()-9)`，
            序號自 D 欄推算，清 D10 後自動空白；手動清 B 欄會刪掉
            範本之序號機制
        (4) **不採整列刪除** —— 會使 DV sqref 與 R10 之 x14 DV 移位
        清除後首筆 TC 落第 10 列，`NR1L-Privacy-001` 起算（R-PV02）。
        探針已實測通過（五格讀回全 None、B10 公式完好）。
  A-PV07 由 PENDING 轉 RESOLVED。

R23-5  A-PV08 表頭六格 —— **依 AMFM 已交付件實測修正建議**
  分析層更正：原建議「D3 Reviewer 與 Cover 封面 Reviewer 由 Pei 給值、
        交付件不該帶範本預設人名」**有誤**。實測 AMFM 之客戶端已交付件
        （`10_Reviewing/00_TestCase/Radio/…CFTS024_Radio_20260129.xlsx`）
        後修正如下：

  | cell | 欄位 | AMFM 已交付件實測 | Privacy 裁定 |
  |---|---|---|---|
  | D2 | 專案名稱 | `newR1L` | 維持 `newR1L` |
  | D3 | 審查者 Reviewer | **空** | **留空** |
  | D4 | 目的 Purpose | **空** | **留空** |
  | D5 | 範圍 Scope | `FM-WI-SW-RAD-SWRA-A02` | `SWE1_CFTS_022-Privacy_Features` |
  | J5 | 日期 Date | `2026/1/29`（交付日）| 交付日填，現在不預填 |

  Cover 封面之三格（核准者 / 審查者 / 作者）**一律不動**：
        實測 AMFM 交付件之 Cover 為版本 A、核准者 劉安哲 AllenACLiu、
        審查者 陳禹伸 YuShenChen、作者 張愷霏 ErinKFChang ——
        此為 **FM-WI-FSM-036-A01 表單本身之文件管制區**，記錄的是
        「誰核准了這份表單」，非「誰審查了本次交付內容」。
        Privacy 範本為版本 C，其對應人員即為該版之管制紀錄，
        不得更動。
  §5a：**表單自身之文件管制欄位與交付內容之責任欄位是兩件事**；
        判定某欄屬何者，須以同表單之已交付實例為據，不得由欄位
        名稱推斷。
  D5 Scope 之特別要求：依 PLAYBOOK §4，Scope 欄是 workbook 之身分
        宣告，**intake 與送件前各驗一次**（一週內兩個 feature 在此格
        出錯）。Privacy 之 037 檔內未給文件編號（cell AI2 僅標
        `FM-WI-FSM-037-A03`），故無法比照 AMFM 填
        `FM-WI-SW-xxx-SWRA-Axx` 形式，改填檔案識別碼。
  A-PV08 由 PENDING 轉 RESOLVED（intake 誤讀 Scope 之 bug 另計，
        見 §2.5）。

R23-6  A-PV10 下拉選單範圍不一致
  裁：範本瑕疵屬上游，**登記即可，不修**。
        lint 以 `下拉選單!A1:A9` 之 9 詞條為準
        （`feature.yaml` 之 `lint.design_method_source: dropdown_sheet`）。
        R10 指向 `$A$1:$A$9`、R11:R59 指向 `$A$1:$A$11`（含 2 空項）
        之落差不修，隨 RD-1 回報上游。
  A-PV10 由 PENDING 轉 RESOLVED（處置已定，缺陷續存於上游）。

R23-7  A-PV11 Reference 與 下拉選單 字串不符
  裁：以 **`下拉選單` 為 lint 權威**（DV 實際引用者）；
        `Reference` 分頁視為說明性附表，**不入 lint**。
        第 6 條之落差（`Pair-wise / N-wise` 對 `Pairwise / t-wise`）
        隨 RD-1 回報上游。
  A-PV11 由 PENDING 轉 RESOLVED。

R23-8  A-PV12 Cover_old / ChangeHistory_old
  裁：採**案 1 原樣保留**。兩頁不進 lint、不進 trace、不寫回。
        理由：刪除屬對公司管制表單之結構性修改，且交付件分頁數與
        原範本不符時，稽核反而須解釋「為何少兩頁」。
        佐證：AMFM 之已交付件同樣保留 `Cover_old` /
        `ChangeHistory_old` 兩頁（實測 10 分頁清單）。
  A-PV12 由 PENDING 轉 RESOLVED。
```

### 執行層回報（下放包 02，2026-08-13）

**停手條件 1 觸發**：本包 §2.1 之前提為「`RULINGS.md` 尚不存在，本包為該檔
之首次建立」。**該前提已不成立** —— 本檔於同日稍早由下放包 01 §4.1 建立
（R22 承接 + 既有裁決索引）。依 §3.1「停止新建，改為附加 R23，續行第 2–6 項，
回報既有內容」，本節即為附加，檔案未重建、R22 與索引未受影響。

既有內容為：R22（R22-1 ~ R22-5 承接自 07 包上繳）+ 既有裁決索引
（R-PV01(c)、R-PV01(a)(b)(d)、R-PV02 之登記位置，以及跨 feature 承接條文）。

**R23-4 / R23-5 之寫入標的說明**：兩項皆**未寫入 `features/privacy/inputs/`**。
`inputs/` 為客戶原件，下放包 01 §2 之基準確認剛確認其 8 檔全數 `MATCH`
客戶樹；就地改寫會同時毀掉該基準與客戶原件，正是 R21-2 / R22-6 所指之危害。
兩項改動輸出至 `features/privacy/output/`，來源檔逐 byte 未動
（已以 SHA256 驗證，見上繳包）。R23-4 所稱「就地改寫」解讀為
**儲存格層級之 XML 就地換值**（`<c r="D10" s="81" t="s"><v>44</v></c>`
→ `<c r="D10" s="81"/>`，保留 `s=`），非「就地覆寫檔案」——
該解讀與條文 (2) 所給之逐字範例一致。

---

## 既有裁決索引（本檔建立前之 Privacy 裁決）

| 編號 | 內容 | 登記位置 |
|---|---|---|
| R-PV01(c) | Amplified 在範圍內，V6_R2 入 `inputs/`；ANC 兩份不索取 | `DECISIONS.md` §8、`ANOMALIES.md` A-PV02 |
| R-PV01(a)(b)(d) | 排除 ETM V3_R3 等，**延後至 P2** | `DECISIONS.md` §8、`ANOMALIES.md` A-PV03（DEFERRED）|
| R-PV02 | anomaly 前綴 `A-PV`；TC id `NR1L-Privacy-{NNN}` | `DECISIONS.md` §8、`ANOMALIES.md` A-PV06 |

跨 feature 承接而仍拘束 Privacy 者：**R18-3**（寫回常設規則三項）、
**R20-5**（write_back 自始建於 `xlsx_surgical`，不得複製既有腳本）、
**R15-2**（已裁而延後者標 DEFERRED）、**R22**（本檔上方）。
其條文原文在 `features/amfm/RULINGS.md`。
