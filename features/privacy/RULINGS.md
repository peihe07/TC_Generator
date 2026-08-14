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

## R24 — 前提更正與 Privacy 專注範圍（2026-08-13）

```text
[RULING] R24 — 前提更正與 Privacy 專注範圍（2026-08-13）

R24-1  下放包 01 之背景前提錯誤 —— 分析層過失
  事實：01 包寫「features/ 下現僅存 privacy/，其餘五個 feature 目錄
        已不在」。執行層實測六個 feature 目錄全部存在，追蹤檔數
        amfm 135 / home 68 / media 170 / projection 77 / sxm 230，
        ANOMALIES、RULINGS、PLAYBOOK、scripts 皆在。
        消失者為目錄內**未被 git 追蹤之素材**（各 inputs/ 內容），
        以及 repo 根 output/（此項 01 包所述正確）。
  分析層複核：本日再次以 list_directory 實測，六目錄確實全部存在。
        先前之單次列目錄結果只回傳 privacy，成因未判定（不追）。
  歸因：**錯不在量測失準，錯在以單次量測支撐一項範圍決定**。
        01 包據該次列目錄結果宣告「下放包 08 內容全部作廢」——
        作廢是不可逆之範圍決定，而依據只有一次未複驗的觀察。
  裁：01 包之「其餘一律不追」續行有效（依 Pei 本日裁示），
        但「08 包作廢」之**理由撤回**，改記為「因專注 Privacy 而
        不處理」。兩者結果相同、依據不同，須分辨。
  §5a 新增：**不可逆之範圍決定，其依據不得為單次量測。**
        欲據觀察結果縮減範圍者，須先複驗；複驗成本高於保留範圍時，
        保留範圍。（與既有「擴範圍證據自足即可、縮範圍須重驗」之
        不對稱原則同源，本條將其自 spec 範圍擴及 repo 狀態。）
  執行層之處置正確：依 §4 未做追查，但回報前提不成立 —— 此即
        R17-3 之正確適用。

R24-2  A-PV14 平台一致性 —— specification_reference 來源檔一律取 HDCC28
  事實（執行層稽核副產物）：`inputs/` 之兩份 VF651 分屬不同平台樹 ——
        `…VF651_V2_R2.docx` 命中 `HDCC28_Split`
        `…VF651_V6_R2.docx` 命中 `28DT_2A_LTM / DT28_split`
        V6_R2 之 HDCC28 副本（`e20ba7a4…`）與 `inputs/` 這份
        （`49dd3c31…`）不同內容。
  裁（**由 R23-2 直接導出，非新政策**）：R23-2 已裁定本專案為
        **HDCC28 平台**、`inputs/` 之 V2_R2（`d5813bb7…`）為 HDCC28
        基線。同一原則適用於全部 VF651 引用：
        **`specification_reference` 之來源檔一律取 HDCC28 平台版本。**
        若不如此，-007 / -008 / -010 三筆 AMP-present 之
        `specification_reference` 將指向 DT 平台文件。
  執行順序（先量後換，不得逕行換檔）：
    (1) 對 `e20ba7a4…`（HDCC28 版）與 `49dd3c31…`（inputs/ 現存）
        做全文 diff，範圍限 SCV / AMP 相關條款
        （`CTRL_AMP.*`、`$VolumeSCV$`、`Acustic_Configuration`、
        `Audio_System_Type`、AMP present/not present 敘述）
    (2) **兩版於上述條款零差異** → 換入 HDCC28 版，記為
        「平台標籤更正，實質內容無影響」，不回溯任何已簽裁決
    (3) **任一條款有差異** → **停手回報**，不得自行判定何者為正
        （R-PV01(c) 之簽署依據為「需求本身要求 AMP-present」，
        不涉平台版本，故該裁決不因本項而動搖；但引用來源須另裁）
  A-PV14 狀態：PENDING → 依上述執行結果更新。
  §5a：**「檔案在正確的交付夾裡」不蘊含「檔案來自正確的平台樹」**；
        交付夾可混入他平台副本，須逐檔以 hash 回溯來源樹。

R24-3  Privacy inputs/ 基準之版控保護
  事實：`features/privacy/inputs/` 8 檔本日全數 MATCH，但 `inputs/`
        本身為 gitignored，其完整性目前無任何機制保障。
        8 檔中 7 檔之同名候選不只一種內容（V6_R2 為 7 候選 / 6 內容）。
  裁：建立 `features/privacy/inputs/BASELINE.sha256`（**進版控**），
        逐檔記錄檔名 + SHA256 + 命中之客戶樹路徑 + 稽核日期。
        此後任何素材增刪改皆會在 `git diff` 現形。
        本項為 Privacy 專屬，不推及其他 feature（依 Pei 裁示）。
  註：R15-5 在本 feature 不是保守規定而是必要條件 —— 執行層此判斷
        成立，本裁決即其機制化。
```

---

## R25 — Phase 3 三項簽署（Pei 簽署 2026-08-13）

```text
[RULING] R25 — Phase 3 三項簽署（Pei 簽署 2026-08-13）

R25-1  framework 三層核可
  裁：Layer 1 Test Group = `Privacy`
      Layer 2 三個 Test Set：Input Monitoring / Personalization Display
              / Speed-Controlled Volume
      Layer 3 CFTS022 artifact id 區塊
      全文寫入 docs/fw036/framework.md 之 **Part VI**（草案見 §2）。
      P3 之 framework 部分據此可勾。

R25-2  DECISIONS.md §8 整份簽核
  裁：Pei 簽核整份 DECISIONS.md（2026-08-13）。
      Sign-off 區塊填入簽核人與日期後，PLAYBOOK §6 之 **P2 可勾**。
      「個別裁決已簽」與「整份已簽核」之區分（執行層 01 包判斷）
      正確且已被採納，記為體例：**Sign-off 區塊為獨立動作，
      不因個別裁決簽署而自動成立。**

R25-3  BASELINE.sha256 入版控
  裁：建立 `features/privacy/inputs/BASELINE.sha256` 並納入版控
      （屬版控政策，Pei 裁定事項，已簽）。
      內容逐檔記錄：檔名 + SHA256 + 命中之客戶樹路徑 + 稽核日期。
      **本項為 Privacy 專屬，不推及其他 feature。**
  用途已由「防護」升為「復原能力」：8 檔中 7 檔之同名候選不只一種
      內容（V6_R2 為 7 候選 / 6 內容，且其中混有 DT 平台版）。
      無此清單時，重新取用素材有極高機率取錯且無任何機制告知。
```

### 執行層回報（下放包 04，2026-08-13）

- R25-1：framework Part VI 已 append 至 `docs/fw036/framework.md`；
  檔首 `Covers Test Groups` 一句已加列 Privacy（Part VI）
- R25-2：`DECISIONS.md` Sign-off 區塊已填（Pei / 2026-08-13 / 依據 R25-2）；
  既有裁決內容一字未改。`PLAYBOOK.md` §6 之 P2 已勾
- **R25-3：以 R26-2 取代，未於 `inputs/` 下建檔。**
  Pei 於本包下放後另行裁示：BASELINE 落於
  `features/privacy/BASELINE.sha256`（feature 根，非 `inputs/` 之下），
  並增設 append-only 之 `DELIVERY.sha256`。兩檔已於同日建立並納入版控，
  `shasum -a 256 -c` 實測 8 OK / 1 OK、零警告。
  R25-3 所要求之「檔名 + SHA256 + 命中之客戶樹路徑 + 稽核日期」四項，
  前二項逐行記於檔內，後二項記於檔頭（下放包 01 §2 之稽核，2026-08-13）。
  **落點差異為 Pei 明示，非執行層自裁。**
- R25-3 之「本項為 Privacy 專屬，不推及其他 feature」仍然有效：
  其餘 feature 未建任何 `BASELINE.sha256`

---

## R26 — Privacy 寫回輸出位置與摘要落點（Pei 簽署 2026-08-13）

```text
[RULING] R26 — Privacy 寫回輸出位置與摘要落點（Pei 簽署 2026-08-13）

R26-1  寫回輸出位置
  裁：P7 寫回輸出寫入 **`features/privacy/output/`**（feature 內部），
      不使用 repo 根之 `output/`。
      該目錄已由 `features/privacy/.gitignore` 之 `output/` 一行排除，
      **維持排除** —— 交付 xlsx 為大二進位且可重產，不進版控。
      `.gitignore` **不修改**。

R26-2  摘要落點 —— 移出被排除目錄，改置 feature 根
  事實：`features/privacy/.gitignore` 排除 `inputs/` 與 `output/` 兩個
      目錄。目錄層級之排除使 `!inputs/*.sha256` 形式之反向規則無效
      （git 不進入被排除目錄），欲保留需改寫為 `inputs/*` + 反向規則。
  裁：**不改 `.gitignore`**，改將兩份摘要置於 feature 根目錄（本即追蹤）：

        features/privacy/BASELINE.sha256   ← 素材基準（inputs/ 8 檔）
        features/privacy/DELIVERY.sha256   ← 交付產出摘要（output/）

      兩者皆 **進版控**。
  理由：為兩個小文字檔改寫版控規則，風險大於收益；且目錄層排除之反向
      規則易寫錯而不報錯（與 §5a「詞彙型工具之缺陷不會報錯」同型）。

R26-3  摘要為唯一之交付身分證明
  裁：`DELIVERY.sha256` 於每次 `--write` 後更新，逐次追加不覆蓋，
      欄位：產出檔名 / SHA256 / bytes / 產製日期 / 對應 tag（若已打）/
      lint 結果 / zip 成員數。
  理由（先例，逐字記錄以免日後被當成過度設計）：
      AMFM v2 從未進版控，`output/` 一經清除即不存在；而 v1 因
      `write_back.py` 已改接外科手術路徑、openpyxl 存檔路徑在檔內
      已不存在，**連重產都做不到**，tag `fw036-amfm-regen-v1` 指向一個
      無法再現的產物。
      `output/` 為 gitignored 是正確的；**錯的是沒有任何追蹤中的紀錄
      能證明當初交付的是哪一份**。本裁決即補此缺。
  §5a 新增：**可重產之產物不進版控是對的；但「可重產」本身是一項需要
      維持的能力，工具鏈變更可能使其失效。故產物之身分摘要必須進版控，
      且與產物本身分開存放。**

R26-4  BASELINE.sha256 欄位（承 R25-3，落點更正）
  裁：內容不變 —— 逐檔記錄檔名 / SHA256 / 命中之客戶樹路徑 / 稽核日期；
      落點由 `inputs/BASELINE.sha256` 改為 `features/privacy/BASELINE.sha256`。
      本日稽核之 8 檔全數 MATCH，直接落檔，不需重測。
```

### 執行層回報（下放包 05）

- R26-1 / R26-2 / R26-4 之產物已於同日依 Pei 之聊天指示先行建立：
  `BASELINE.sha256`（8 檔）與 `DELIVERY.sha256`（append-only 台帳），
  兩檔皆於 feature 根、皆已納入版控。`.gitignore` **未修改**
  （曾誤改一次，已還原至原狀）
- 第 4 項確認：`git check-ignore -v` 對兩檔皆無輸出（未被任何層級排除）；
  對 `features/privacy/output/x.xlsx` 則命中 `features/privacy/.gitignore:17`
  —— 排除規則正確作用於 `output/` 而未及於兩份摘要
- 第 5 項：`features/privacy/output/` 已存在（R23-4／R23-5 產物寫入時建立），
  未放 `.gitkeep`
- **第 6 項停手條件 3 觸發**：`feature.yaml` 之 `write_back:` 區段
  **沒有任何寫回輸出路徑欄位**（現有欄位為 `author_value`、
  `tc_ref_id_value`、`tc_id_format`、`fill_test_group_set`、
  `scope_label`、`scope_source`）。依 §3.3「停止該項，續行第 7 項，
  回報實際欄位結構」——**未自行新增欄位**。
  其餘 feature 之 write_back 腳本輸出路徑皆以 `--out` 參數或程式內預設決定，
  非由 `feature.yaml` 指定；Privacy 之寫回腳本尚未建立（R20-5），
  故該欄位要不要存在、叫什麼名字，宜於建立腳本時一併裁定

---

## R27 — 兩份 sha256 台帳之語意（分析層自裁，2026-08-13）

```text
[RULING] R27 — 兩份 sha256 台帳之語意（分析層自裁，2026-08-13）

R27-1  `--ignore-missing` 之採用 —— 追認，並明列其代價
  裁：`shasum -a 256 -c --ignore-missing DELIVERY.sha256` 為正確驗證式。
      執行層之實測（竄改 → FAILED exit 1；不存在 → 靜默略過 exit 0）
      語意正確。
  但須明載其代價：**該旗標使 DELIVERY 台帳無法偵測「產出被刪除」**。
      台帳驗的是「還在磁碟上的產出有沒有被動過」，不驗「產出還在不在」。
      此為 append-only 台帳之必然，不是缺陷 —— 但不得在日後被誤讀為
      「台帳綠燈 = 產出俱在」。
  兩份台帳之非對稱處置成立，逐字記錄其理由：
      BASELINE —— 不加旗標。素材應始終在位，少一個即為停手事由。
      DELIVERY —— 加旗標。舊產出被清屬正常，台帳記的是歷史不是現況。
  §5a：**驗證指令之旗標會改變該驗證所證明的命題**；採用旗標時必須
      同時記載「加了旗標之後這條指令不再證明什麼」。

R27-2  中間產物不入台帳 —— 結論追認，理由更正
  事實：執行層對 `prepared_step1_cleared.xlsx` 採保守處置（不記入），
      理由寫為「記了會讓台帳在任何一次 output/ 清理後失敗」。
  裁：**結論正確，理由不成立且須更正。** R27-1 已採 `--ignore-missing`，
      被清掉的條目會靜默略過而非 FAILED —— 該理由與執行層自身之
      旗標決定互相矛盾。
  正確理由：**台帳之記錄單位為「將被寫回或交付的工作簿狀態」**，
      即每一次 `--write` 之輸入基準與輸出。同一次操作內的中間步驟
      不是一個工作簿狀態，記入只會稀釋台帳的檢索價值。
  判準（立為通則）：
      入台帳 —— 一次 `--write` 的輸入基準、一次 `--write` 的輸出、
                 任何被送出或被 tag 的產物
      不入   —— 同一次操作內的中間檔、探針產物、對照臂輸出
  §5a：**採保守處置時，其理由與結論須分別檢驗**；理由錯而結論對，
      日後援引該先例會把錯誤理由一併帶走。

R27-3  ENTRY 001 之性質標註 —— 追認
  裁：ENTRY 001 標為「準備完成之工作簿、非交付件（P7 未進行、無 tag）」
      並附「未由人以 Excel 開過；此項未完成前不得升格為交付件」——
      追認。
      此標註與 R27-2 之判準一致：它是 B1 寫回的輸入基準，屬工作簿狀態，
      入台帳；其「非交付件」由條目自身標明，不靠排除在台帳之外表達。

R27-4  BASELINE 之已知未決標註 —— 追認
  裁：檔頭明寫「V6_R2 對齊 DT28（A-PV14），本檔只記錄現有那一份，
      不預判它是否為正確平台版本」—— 追認。
      此為 R22-5（分類承載因果假設時停在原始量測）之正確適用：
      台帳記錄事實，不承載平台正確性之判斷。
```

### 執行層回報（下放包 06）

- R27-2 之理由更正已接受。原理由（「記了會讓台帳在 output/ 清理後失敗」）
  確實與自身之 `--ignore-missing` 決定矛盾 —— 該旗標正是為了讓被清掉的條目
  靜默略過。**結論對、理由錯**，已依裁決改為記錄單位判準並寫入
  `DELIVERY.sha256` 檔頭
- R27-1 之代價說明（台帳綠燈 ≠ 產出俱在）已寫入 `DELIVERY.sha256` 檔頭
  與 `PLAYBOOK.md` §6

---

## R28 — profile 核可與 A-PV14 結論（2026-08-13）

```text
[RULING] R28 — profile 核可與 A-PV14 結論（2026-08-13）

R28-1  profile 核可 —— 附三項修訂後生效
  裁：`docs/runtime/profiles/FW036_R1L_Privacy_Profile.md` **核可**，
      移除檔頭 DRAFT 標記，改記「Approved 2026-08-13, R28-1」。
      §2 之三項修訂須一併寫入後方為定案。
  起草取捨之追認：「結構條款繼承、內容條款不繼承」，七個 SXM delta
      逐條重新判斷並於 §7 列對照表 —— **追認，並立為體例**。
      §5a：**profile 之跨 feature 實例化，繼承粒度須逐條聲明**；
      「以 X 為體例」不得作為整份繼承之依據，未逐條聲明者視為未繼承。

R28-2  A-PV14 —— 換檔條件成立，結論不受 hunk 6 影響
  事實（執行層唯讀 diff）：HDCC28 副本 `e20ba7a4…` 404 非空行 vs
      `inputs/` 現存 `49dd3c31…` 403 行，9 個 hunk，SCV/AMP 相關行
      兩側各 33 行，**落在 SCV/AMP 條款之差異 = 0**。
      hunk 8 為獨立佐證：HDCC28 版 revision note 作
      `derived from VF651_V6_R1_PHDCCMCA`，`inputs/` 版作
      `VF651_V6_R1_PDT26` —— 文件內文自證平台歸屬，不再僅靠路徑推定。
  裁：R24-2(2) 條件成立，**換入 HDCC28 版**。

  關於 hunk 6（`VSIM_FD_1.AudioMuteRq` 僅存於 HDCC28 版）：
      執行層未自行重新分類、照實列出九個 hunk —— **處置正確**（R22-5）。
      分析層裁定其**不改變結論**，理由為方向性而非範圍性：
      **換檔方向是 `inputs/`(DT26) → HDCC28，該訊號是「取得」而非
      「失去」。** 依不對稱錯誤代價原則，擴增內容之變更其證據門檻
      低於縮減；hunk 3/4/5/6 四個訊號差異若確屬音訊/電源域，只會
      使換檔更必要，不會使其可疑。
      反向推論同時成立：若沿用 DT26 版，等於引用一份**缺少 HDCC28
      平台訊號**的文件。

  關於「全文 diff」之限縮（僅文字，未比對圖／嵌入物件／頁首頁尾；
      兩份 size 差 7,420 bytes）：
      裁定**不需補做**。理由：diff 的目的是判斷「換檔是否會使任何
      已簽裁決失效」，而換檔後 HDCC28 版為唯一引用來源，未比對之
      區域自動採 HDCC28 值 —— 該區域無論差異為何皆不構成風險。
      且 R-PV01(c) 之簽署依據為 037 葉子文字，不依賴任何 VF 版本，
      故無回溯影響。
      執行層主動聲明此限縮 —— 正確，記為體例：**聲明限縮者不必然
      需要補做；限縮是否要緊，取決於該結論將被如何使用。**

R28-3  framework 首句遺漏 Part V —— 補上，非範圍擴張
  事實：執行層發現 `docs/fw036/framework.md` 首句原本即未列
      Part V（Projection）；授權僅及於加入 Privacy，故未順手補。
  裁：**補上**。首句是該檔之目錄索引，漏列既有 Part 屬事實性遺漏，
      補正不改變任何範圍。執行層之保守處置正確（授權外不自行擴張），
      但此類**純事實性補正**日後得逕行執行並於上繳包載明。
  §5a：**區分「授權外之範圍擴張」與「授權外之事實性補正」**；
      前者須回報待裁，後者得逕行並載明。判準：該動作是否改變任何
      人對範圍、歸屬或結論之理解 —— 否即為事實性補正。
```

### 執行層回報（下放包 07）—— ⛔ **停手條件 2 觸發**

**B1-GATE-1 之獨立重驗發現兩筆對映與 framework Part VI 不符。**
依 07 包 §7.2「停止全部後續，續行回報」，故：

- **R28-1 之 profile 核可未執行** —— DRAFT 標記維持，§2 三項修訂未寫入。
  理由：修訂 1 改的是 §3.3 design method，與對映無關；但 §3 移除 DRAFT
  即為核可定案，而 profile §1 之對映條款正是本次爭點所在，
  不宜在對映未定之前定案
- R28-3 之 framework 首句補 Part V **已執行**（純事實性補正，
  該條明文「得逕行執行並於上繳包載明」，且與對映無關）
- 第 5 項 rev C 之 T–Z 標頭實測**已完成**，見上繳包
- 第 7 項及**下放包 08 全部作業未執行**

詳細證據見 `docs/upstream/07_profile_approval.md`。

---

## R29 — B1 前置條件之兩項確認（2026-08-13）

```text
[RULING] R29 — B1 前置條件之兩項確認（2026-08-13）

R29-1  B1-GATE-2 —— Excel 實開確認通過
  裁：Pei 於 2026-08-13 開啟
      `features/privacy/output/FM-WI-FSM-036-A01 … _Privacy_20260813.xlsx`，
      四點全過：
        1. 無「檔案已損毀，Excel 已修復」提示
        2. R 欄設計方法下拉可用，選項為 下拉選單 之 9 條
        3. D5 範圍 Scope 顯示 `SWE1_CFTS_022-Privacy_Features`
        4. 第 10–11 列已清，B 欄序號未顯示殘值
      **B1-GATE-2 通過。**
  意義（逐字記錄，避免日後被當成形式手續）：本項是 zip 層外科手術
      路徑**第一次**取得人為 Excel 開啟之確認。此前所有驗證皆在程式層
      （zip 成員 48→48、DV 4:2→4:2），程式層驗不到 Excel 之檔案完整性
      判定。R18-3 規則 1 至此取得端到端佐證。
  DELIVERY.sha256 之 ENTRY 001 加註：
      「Excel 開啟確認：Pei, 2026-08-13, 四點全過（R29-1）」。

R29-2  V6_R2 換檔完成 —— A-PV14 事實面結案
  實測（分析層，2026-08-13，對 repo 實體路徑）：
      `features/privacy/inputs/Audio_Output_Management_-_LTM_ETM_
       Amplified_Audio_System_VF651_V6_R2.docx`
      SHA256 = e20ba7a4f8f744e89bfa5c770700ba267ed7f6a0015becc045ef8f63dbeef0f2
      size   = 177,388 bytes
      與 R28-2 之預期值 `e20ba7a4f8f7…` 相符 → 換檔完成。
  裁：**A-PV14 → RESOLVED**。三處連動即刻辦理（見 §2）。
      平台歸屬之佐證有二且互相獨立：路徑（HDCC28_Split）與文件內文
      （revision note `derived from VF651_V6_R1_PHDCCMCA`，hunk 8）。
```

### 執行層回報（下放包 08）

R29-1 / R29-2 於 B1-GATE-1 停手期間未執行；**R30 解除停手後補辦**，
各項見下方 R30 之執行回報。換檔實測值與 R29-2 預期相符
（`e20ba7a4f8f744e89bfa5c770700ba267ed7f6a0015becc045ef8f63dbeef0f2`，
177,388 bytes）。

---

## R30 — B1-GATE-1 對映更正、P-4、P-5（Pei, 2026-08-13，chat）

> **編號由執行層暫配**（R29 之後的下一號）。本裁決自 chat 下達、未經下放包，
> 若分析層另有編號請告知更正。

```text
R30-1  -001 / -002 對映更正 —— 以 ECU tag 定案，非語意判讀
  裁：-001 → 4914955；-002 → 4915158。
      framework Part VI Layer 3 表原填之 4915022（不存在）與
      4915159（splash screen 計時）作廢。
  -001 之判準（量出來的，不是讀出來的）：
      4914954  ECU=SCCM，Radio 清單無 R1L-R
      4914955  ECU=ETM, RRM, ICS, DVD, LTM；Radio=allSys
      本專案 ECU 為 LTM → 4914955。
  歸因（分析層自陳）：framework Part VI 之「offset 恆為 −1」係自 8 個
      同屬一個無缺號區塊之樣本外推，再以該外推算出兩個 id 填入 Layer 3 表。
      **此舉違反分析層自己核可之 profile §3.5「The id is looked up,
      never constructed」。**
  §5a：**自訂規則之違反，最常見的形式不是明知故犯，而是在另一份文件裡
      以「已驗證之規律」為名重新引入被該規則禁止的推定。**
      規則之適用須及於所有產生該類值的場所，不限於規則所在文件。

R30-2  補集判定之獨立性保留 —— 追認並擴及分析層自身之複驗
  裁：執行層指出「4915022 不存在」係對 336 個區塊之補集判定，
      而 336 這個數與 ECU tag 行數同出一支 regex，非獨立驗證 —— 成立。
      分析層之複驗採第三種擷取樣式、同樣得 336，但**同屬一族**，
      亦非真正獨立。兩項保留一併記載。

R30-3  P-4 欄 S（Functional Safety）—— 反轉為一律填 NA
  量測（AMFM 客戶端已交付件，158 列人工撰寫）：
      Functional Safety 欄  158/158 全填 `NA`
      車型欄 S..Y           158 列全空，0 列填值
  裁：**P-4 = (b) 一律 NA**。分析層原建議 (a) UNRULED_BLANK、
      理由為「NA 是斷言不是留白」—— 論理無誤，但被語料推翻。
  §5a（援引 framework.md 既有條文）：不憑直覺立規則，先對 done region 量；
      語料牴觸時記錄量測而非記錄規則（Home 有兩條裁決即如此被翻掉）。
      本案兩個獨立來源同向：Wilson 之 158 列全 NA，
      加上 Privacy 空白範本原廠樣本列 S10 本即為 `NA`。

R30-4  P-5 車型欄（T–Z）—— 全部留白
  裁：**T–Z 一律留白**，先例為 AMFM 之 0/158。
  併裁：rev C 之車型欄停在 **27 世代**（T9 `HDCC27 Atl-Hi`、
      U9 `DT27 Atl-Hi`），而本專案為 **HDCC28** 平台 —— 七欄中無 HDCC28。
      **登 anomaly + RD-1 提問，不自行對應。**
      與 A-PV14 同源：一個是 VF 檔混入 DT 平台，一個是欄位本身沒跟上世代。
      範本 X9 之 `Regengade (5210)` 應為 `Renegade`，原文不動，一併進 RD-1。
```

### 執行層回報（R30）

- **ECU 判準已獨立複驗**：4914954 `ECU=SCCM` / Radio 無 `R1L-R` 亦無 `allSys`；
  4914955 `ECU=ETM, RRM, ICS, DVD, LTM` / `Radio=allSys`。
  4915158 `ECU=RRM, LTM, ETM`、4915159 `ECU=ETM, RRM, LTM` —— 兩者 ECU 皆含
  LTM，故 -002 之判別**不能靠 ECU**，係靠條文語意（Interior CAN 喚醒 →
  recall 個人化狀態 vs splash screen 計時）。**兩筆的判準不同型，分開記載。**
- R30-1 之更正已寫入 framework Part VI 與 profile §1
- R30-3 / R30-4 已寫入 profile；A-PV15 已登記；RD-1 三項已入 `DATA_REQUESTS.md`
- **B1-GATE-1 至此通過**，停手解除，R28 / R29 之擱置項全數補辦

---

## R31 — B1 授權與前輪追認（2026-08-13）

```text
[RULING] R31 — B1 授權與前輪追認（2026-08-13）

R31-1  R30 編號 —— 追認執行層之暫配
  裁：執行層將 chat 直下之裁決暫配為 R30 並於條文上方標明「編號由
      執行層暫配」—— **追認，編號維持 R30**，標註可留可去。
  立為通則：**分析層自 chat 直下而未經下放包之裁決，執行層得逕行
      暫配下一個可用編號並標明**，不必回報待裁；分析層若另有編號
      再更正。理由：編號是登記手續，不是裁決內容；為手續往返一輪
      不符成本。

R31-2  -002 之判準與 -001 不同型 —— 追認，且此區分必須保留
  事實：4915158 與 4915159 之 ECU tag 皆含 LTM（`RRM,LTM,ETM` 與
      `ETM,RRM,LTM`），**ECU tag 在 -002 沒有鑑別力**；-002 靠的是
      條文語意（Interior CAN 喚醒→recall 個人化狀態 vs splash screen
      計時）。-001 則由 ECU tag 定案（4914954 為 SCCM 且 Radio 無
      R1L-R；4914955 含 LTM 且 allSys）。
  裁：追認執行層分開記載之處置。**此區分不得在日後被壓平**成
      「兩筆都是 ECU 定的」—— 兩筆的證據強度不同：一筆是量測
      （tag 比對），一筆是判讀（語意）。
  §5a：**同一次更正內若各項之證據型別不同，必須逐項標明型別**；
      合併敘述會使較弱的那項繼承較強那項的可信度。

R31-3  BASELINE 台帳之實地驗證 —— 記錄
  事實：執行層更新 BASELINE 時腳本選錯行中斷，換檔已完成而台帳未
      更新，`shasum -c` 立即回報 `exit=1 OK=7 FAILED=1`；修正後
      8 OK / exit 0。
  裁：記錄之。**這是 R25-3 / R26-2 建立台帳以來的第一次真實觸發，
      且觸發情境正是它被設計來攔的那一種**（素材已變而紀錄未跟上）。
      台帳自本日起不再是推定有效，而是實測有效。
```

### 執行層回報（下放包 09）

四項停手條件全部未觸發。台帳於生成前後各驗一次，四次皆綠
（BASELINE 8 OK、DELIVERY 1 OK）。**5 leaves → 6 TC**，
`generated/` 五檔，機械檢查 0 findings。**本批未寫回 workbook。**

R31-2 之區分已落實於三處文件（framework Part VI 判準表、profile §1
對映表、本檔 R30-1），三處皆分開記載 -001 之 ECU tag 判準與 -002 之
條文語意判準，未合併敘述。

**一項需 pilot review 裁定者**：037 之 Requirement Description 在
-001 / -002 / -003 三片葉子上主張了 CFTS022 條文沒有的行為
（詳見上繳包 09 §6.2）。執行層依 spec_mode D 之 clause 權威照條文產出，
未把 037 之額外主張寫入 TC，亦未創設 marker 或登記 assumption ——
但該部分目前無 TC 覆蓋，屬「037 Description 是否為獨立需求來源」之
層級問題，不自裁。

---

## R32 — B1 pilot review（分析層自裁，2026-08-13）

> **編號由執行層暫配**（依 R31-1：chat／下放包直下而未載編號者，
> 執行層得逕行取下一個可用編號並標明）。本裁決出自下放包 10。

```text
D1  -005 TC2 之 design_method 與其程序不相稱 —— 結構性，阻塞 -005
  事實：TC2 之程序為「啟動 trace → 走訪每一可選狀態 → 睡眠喚醒 →
        讀取 trace 內所有 $VolumeSCV$」，**全程未注入任何無效值**。
        §12 第一列之條件為 Invalid input / illegal op，本程序無非法輸入，
        只有對輸出集合之觀察。
  根因在讀法不在措辭：**讀法 (i) 之下負向測試不可構成** —— HU 為
        $VolumeSCV$ 之發送端，測試者無從令其送出無效值；能注入之位置
        在 AMP 輸入側，即讀法 (ii)。
  連帶：§7「列舉之支援項須配至少一負向」在讀法 (i) 下無法滿足。
        執行層依 §7 拆出 TC2 之推論正確，但其前提（本 ECU 可構成負向）
        不成立 —— 此項執行層未察覺，為本次覆核之新發現。
  處置：待 P-6 裁定，-005 兩條本輪不動。

D2  單一步驟綁多個動作（§5.2 A：action + target only）—— 輕微，即修
  -003 步驟 4（三個動作）、-002 步驟 4（兩個動作）拆為獨立步驟，
  ER 1:1 同步展開。

D3  -004 之 Pre-Condition 與步驟重複（§4.5 欄位歸屬）—— 輕微，即修
  PC #3 收為 `A CAN interface tool is connected`，保留步驟 2。

N1  037 Description 之額外主張 —— 三葉分別處置
  -003：排除正確，且有外部 spec 歸屬佐證（{CFTS019} 擁有 speed
        controlled audio behavior requirements），依 §8.4.2 成立。
  -002：實質已被現有 ER 涵蓋，毋須改寫，加一句說明即可。
  -001：確為 037 獨有之主張，CFTS022 全文無此語 —— 見 P-7。

N2  -001 之 P0 維持
  §10.2 之 P0 涵蓋 boot/recovery，「每次退出睡眠後實體按鍵全數失效」
  為 recovery 路徑之全失。執行層之推理與 framework Part I 一致。
  執行層所引「AMFM 同類用 P1」之反向參考**無法查證**（AMFM inputs/
  已不存在），不採為依據，亦不記入。

N3  lint 缺席 —— B1 不阻塞，B2 之前必須建立
  執行層自陳「那份機械檢查不是 lint」之揭露為本包最有價值之一項。
  B2 之前須建 features/privacy/scripts/lint_tcs.py，不得沿用 AMFM 版；
  gate 至少涵蓋 profile §3.3 / §3.5 / §3.8 / §3.9 與 §11 之格式規則。

N4  CAN trace 工具能力 —— 非需求假定，登 A-PV16（PENDING，不阻塞）

N5  Pre-Condition 措辭回溯原文 —— 維持 P2 清單，P6 寫回前須完成
```

### 執行層回報（下放包 10）

- **D1 我接受，且成因值得記下來**：我依 §7 拆出負向 TC 的推論本身沒錯，
  錯在沒有檢查「本 ECU 是否具備構成負向的位置」。§7 談的是 TC 的配對，
  §8.4.2 談的是行為的歸屬 —— 兩者在本葉相衝突，而我只套了前者。
- **D2 / D3 已修**，1:1 檢查通過（-002 6/6、-003 7/7、-004 5/5）。
- **N1 之 CFTS019 佐證已獨立複驗**（停手條件 2），且發現一項需修正的
  引用細節：該 Note 掛在 **PROF-172（leaf -006）**，不在 -003 自身之
  條文 4915168 上。已按此精確寫入 -003 之 `reasoning`，未讓它讀起來
  像是本葉條文自帶的限定。佐證有兩處獨立來源（SYSAD 與 CFTS022-4915171）。
- **D2 同類缺陷在 -005 兩條亦存在**，因 §3.7「不動 -005」未修，
  見上繳包 §4.1。
- P-6 / P-7 未裁前，-005 兩條與 -001 之 priority 一字未動。

---

## R33 — B1 review 結案與 §7／§8.4.2 衝突先例（Pei 簽署 2026-08-13）

```text
[RULING] R33 — B1 review 結案與 §7／§8.4.2 衝突先例（Pei 簽署 2026-08-13）

R33-1  P-6 —— -005 維持讀法 (i)，TC2 改寫
  裁：
  (a) TC2 之 design_method 由 `負向測試 (Negative / Invalid)` 改為
      `功能測試 (Functional based ; no specific technique)`。
      理由：其程序未注入任何非法輸入，只觀察輸出集合之封閉性，
      不合 §12 第一列 `Invalid input / illegal op` 之條件。
  (b) TC2 之 tc_title 與 test_item 改寫為**輸出集合封閉性**，
      不再以「無效值處置」為名。改寫後之驗證目標為：
      「HU 於任何可達狀態下，$VolumeSCV$ 皆不攜帶四值集合外之值」。
  (c) 真正之負向（向 AMP 注入集合外之值、驗 AMP 不動作）
      **out of scope，歸 AMP ECU 之驗證**。於 -005 `reasoning` 載明，
      並列入 RD-1。
  (d) **先例（本裁決之主要產物）**：
      **§7 之負向配對要求，當本 ECU 不具備構成該負向之位置時，
        以範圍歸屬解除，不得以形式上的 TC 滿足。**
      判準：該非法輸入之注入點是否落在本交付件所驗之 ECU。
      落在他 ECU → 該負向屬他 ECU 之驗證，本葉以 §8.4.2 排除並
      於 `reasoning` 指名歸屬；**不得**以「觀察本 ECU 未產生非法輸出」
      冒充負向測試。
      成因（逐字收錄執行層之自我歸因，較分析層之原判更準確）：
      「§7 談的是 TC 的配對，§8.4.2 談的是行為的歸屬 —— 兩者在這片
        葉子上相衝突，而我只套了前者。reasoning 裡已寫出 outcome
        主詞是 AMP，卻沒把那個認知接回設計方法的選擇上。」
      §5a：**已寫入 reasoning 之認知，必須回頭檢查它是否改變了
        其他欄位的選擇**；reasoning 不是傾倒觀察的地方，是推導的一環。

R33-2  P-7 —— -001 之 037 獨有主張
  事實：037 Description 主張「轉換階段中按鍵輸入不得被處理，只有在
      達到 active 狀態後才處理」。分析層對 CFTS022 全文掃描：涉及
      `SLEEP MODE` 之 artifact 僅 4914954（SCCM 版）、4914955（HU 版）、
      4915104（Lock Out State 初始化），**無一述及該行為**。
  裁：
  (a) -001 現行 TC **不改** —— 其驗證目標與 CFTS022-4914955 一致
  (b) `reasoning` 明列該 037 主張未被本 TC 覆蓋，及其理由
  (c) 登 **A-PV17**：037 Description 含 CFTS022 未載之行為主張，PENDING
  (d) 列入 RD-1：請上游確認該句為需求或闡釋；若為需求，
      請指出其 CFTS022 出處或補充條文
  理由：不對稱錯誤代價指向補測（擴範圍）而非不測（縮範圍），
      但補測之對象必須先確認是需求 —— 若該句為分析者之闡釋，
      據以生成 TC 會對合規實作產生誤判（§7 FF）。故先問後補。

R33-3  CFTS019 佐證之引用精度 —— 執行層更正成立
  事實：分析層於下放包 10 §1 N1 稱該 Note 可支持 -003 之排除。
      執行層查證後指出：該 Note 掛在 **4915171（PROF-172，-006 之來源）**
      與 SYSAD 之 SYS-RA-PROF-172，**不在 -003 自身之條文 4915168 上**
      —— 4915168 全文僅一句，無任何 Note。
  裁：更正成立。-003 之 `reasoning` 須按執行層之精度表述：該 Note 為
      **「該行為之歸屬」之一般性陳述**，非本葉條文自帶之限定。
  §5a：**佐證之掛載位置決定其效力範圍**；引用他條之 Note 支持本條之
      排除時，必須標明該 Note 不在本條上，否則日後會被讀成本條自帶。
  連字號：引用時取 CFTS022 之 `speed controlled`（無連字號），
      不取 SYSAD 之 `speed-controlled` —— spec_mode D 之 clause 權威
      在 CFTS022。追認。

R33-4  -005 之 D2／D3 同型缺陷 —— 併入改寫，不另立一輪
  裁：分析層於下放包 10 覆核時漏列 -005 之同型缺陷（**分析層過失**，
      執行層依指示未動 -005 而僅回報，處置正確）。併入 R33-1 之改寫：
      - TC1 步驟 1–4 之 `Set … and read …` 各拆為兩步，ER 1:1 同步
      - TC2 步驟 3 `Trigger the HU to sleep and wake it up again` 拆兩步
      - TC2 之 PC 2 收為 `A CAN interface tool is connected`
        （與 -004 之修法一致）

R33-5  `and` 之字面掃描判準 —— 非缺陷，但須寫入 lint 規格
  裁：-004 步驟 4 `Read the first $VolumeSCV$ signal in the CAN trace
      and its timestamp` **不是缺陷** —— 一次觀察讀兩個屬性，非兩個動作。
      §5.2 管的是動作數。
      但該句會被字面掃描命中，故 lint 規格須載明：
      **`and` 之後若為同一觀察之另一屬性，不計為第二動作；
        判準是動詞數而非連接詞。**
```

### 執行層回報（下放包 11）

- R33-1 / R33-4：-005 兩條已改寫（TC2 設計方法改功能測試、標題與 test_item
  改為輸出集合封閉性、真負向歸屬載入 reasoning；TC1 步驟拆為 8 步、
  TC2 步驟拆為 5 步、PC 2 收斂）。priority 未動。
- R33-2：-001 之 TC 本體與 P0 一字未動，`reasoning` 已加未覆蓋說明；
  **A-PV17** 已登記。
- R33-3：-003 之 CFTS019 佐證表述已按掛載位置精度改寫。
- R33-5：`and` 判準已寫入 lint 規格（動詞數而非連接詞），並自帶陽性對照。
- **停手條件 3 觸發於 -008** —— 判定與依據見上繳包 11 §4，
  該葉未生成，其餘四葉照產。

---

## R34 — B2 覆核與 ECU 歸屬判準（Pei 簽署 2026-08-13）

```text
[RULING] R34 — B2 覆核與 ECU 歸屬判準（Pei 簽署 2026-08-13）

R34-1  ECU tag 與行為主詞不一致時之判準（本包主要產物）
  裁：ECU tag 表示「哪些 ECU 的規格文件會收錄此條」（分發範圍）；
      行為主詞表示「誰執行此行為」。**驗證歸屬由後者決定。**
      兩層判準，須同時成立：
        (1) 必要條件 —— ECU tag 含本 ECU
        (2) 充分條件 —— 行為之 trigger 或 outcome 主詞含本 ECU，
            或本 ECU 在該訊號鏈上有可觀察之一端
      (1) 成立而 (2) 不成立 → 排除，並於 reasoning 指名歸屬。
      **tag 含本 ECU 只是「這條與我們相關」，不是「這個行為由我們驗」。**
  先例對照（同一判準、不同結果，兩者皆須保留於 profile）：
      -005 留下 —— HU 為 $VolumeSCV$ 之發送端，訊號鏈上有可觀察之一端
      -008 排除 —— trigger 與 outcome 皆為 AMP，HU 側無任何可觀察行為

R34-2  -008 排除確認
  裁：`SWE1-HMI-PRIVACY_FEATURES-008`（CFTS022-4915173）
      **排除於本交付件之驗證範圍**，歸 AMP ECU。
  證據四項同向（分析層獨立複驗 ECU tag，執行層判定成立）：
      (a) trigger 主詞 = AMP
      (b) outcome 主詞 = AMP
      (c) 條文全文不提 HU
      (d) **ECU tag 含 `AMP` —— 十片葉子中唯一**
          4915171 `RRM, LTM, ETM` / 4915172 `ETM, LTM, RRM` /
          4915173 `ETM, AMP, RRM, LTM` / 4915174 `RRM, LTM, ETM` /
          4915175 `LTM, ETM, RRM`
      執行層照實回報之反向指標（tag 仍含 LTM）依 R34-1 不足以推翻。

R34-3  -008 於交付件之表示 —— 產出 BLOCKED 列
  裁：交付件**為 -008 產出一列**，非略去。
      - tc_id 照序配發（不跳號）
      - Test Group `Privacy`、Test Set `Speed-Controlled Volume`
      - specification_reference = `CFTS022-4915173`
      - 各驗證欄位依 BLOCKED 形式填寫
      - Remarks 帶 marker，內容：
        `[BLOCKED-ECU] Out of scope for this deliverable: both the
         trigger and the outcome of CFTS022-4915173 are performed by
         the AMP; the HU has no observable behaviour in this clause.
         Verification belongs to the AMP ECU. Pending upstream
         confirmation of the leaf allocation (A-PV18 / RD-1 #12).`
  理由：交付件若直接少一片葉子，追溯表會出現**沒有說明的缺口**；
      BLOCKED 列使缺口可見、可審。
  連動：本項為本 feature **第一個 marker**。profile §5 之
      「本 feature 目前無 marker」須改寫為 marker 表，登記
      `[BLOCKED-ECU]` 之定義、適用條件與唯一用例。
      lint 須加一項 gate：Remarks 非空時，其開頭 token 必須為
      profile §5 marker 表內已登記者。
  新登 A-PV18：037 將 outcome 主詞為 AMP 之條文分配予 HMI/HU 之
      SWE.1；狀態 PENDING，待上游確認。
  RD-1 新增 #12：請上游確認 -008 之葉子分配；若確為 HU 側需求，
      請指出 HU 在該行為中之角色與可觀察面。

R34-4  -006／-007 之速度激勵 —— ER 不得斷言音量與車速之關係
  事實：CFTS022-4915171 全文為「If the amp is not present, the HU shall
      adjust the output volume **according to the speed controlled
      level**」，其自帶 Note 明將 speed controlled audio behavior
      交予 CFTS019。
  裁：本條擁有之標的為**歸屬**（amp 不在時由 HU 執行調整），
      非**行為曲線**。故：
      (a) 速度激勵得用於觸發，但 ER 不得斷言任何「音量 vs 車速」之
          具體關係、比例、階數或門檻（屬 CFTS019，§8.4.2）
      (b) -006 之 ER 止於「輸出音量隨之改變」
      (c) -007 之 ER 止於「level 未被 HU 改變」
      (d) 兩者可驗證之差異是**誰在調整**，不是調得對不對
  執行層之疑慮（速度激勵未經規格確認）成立，本裁決即其處置。

R34-5  lint gate 之 Interior CAN 誤判修正 —— 追認
  裁：修 gate 不修標準，界線正確（停手條件 1 之界線）。
      修法（modal 命中若字面全大寫則判為縮寫／訊號名）不改 gate 意圖，
      shall 仍照抓且經陽性對照確認 —— 追認。
  §5a 新增：**對正確輸入誤報的 gate，跟永不觸發的 gate 一樣壞。**
      故每一 gate 須同時具備：
        陽性對照 —— 證明它會抓（違規輸入必 FAIL）
        負向對照 —— 證明它不亂抓（合規之相似輸入必 PASS）
      **缺任一者，該 gate 標「未實測」而非 PASS。**
      本例之負向對照即「Interior CAN 必須不觸發 er-modal」。

R34-6  欄 S 與車型欄標 NOT MEASURED —— 追認
  裁：生成階段不產出該兩區，此處無從失敗，標 NOT MEASURED 正確
      （R18-4 原則）。該兩 gate 於 P6 寫回後方為可實測，屆時須重標。

R34-7  VF651 不進 specification_reference —— 追認
  裁：三項理由皆成立 —— 需求來源為 CFTS022；VF651 於本批為背景理解
      且未給可用值；profile §3.5 明文「No cite-form mechanism」，
      SXM 之 cite-form 明列為不繼承。
      以 spec 自身 token {VF651} 出現於 reasoning 即可。
      **推及全批**（B1 + B2 十葉一致）。

R34-8  -009 與 -003 非 duplicate —— 追認，不標 duplicate_of
  裁：觸發不同（使用者改變 level vs Interior CAN 喚醒），§8.3 之切分
      判準為觸發。-009 借喚醒作為「已存入」之觀察手段，屬**觀察手段
      重用**，非驗證目標重複。
      reasoning 須註明此區分，避免 review 時被誤讀為漏標。
  §5a：**觀察手段之重疊不構成 duplicate**；duplicate 之判準是
      trigger + outcome + input + verification target 四者皆同。

R34-9  PROXI 參數值不可得 —— 追認
  裁：VF651_V6_R2 明文「The characteristics of the PROXI Parameters and
      their related values are defined in the PROXI requirements
      specific for the vehicle project」，該文件不在 inputs/。
      依 §8.4.1 不填任何參數值，Pre-Condition 以條文自身措辭表述
      —— 追認。DATA_REQUESTS #11 已立。

R34-10  兩項延宕事項 —— 停止再延，列為 P6 硬性前置
  (a) **Pre-Condition 措辭回溯 CFTS022 原文** —— 已連續三次列為未辦
      （下放包 10 N5 / 上繳包 04 §6.3 / 09 §6.4），且範圍已自六葉擴為
      十葉。**P6 寫回前必辦，不得再列入「未辦」。**
  (b) **全 10 葉之 spec-reference 語意對應人工覆核** —— lint 只驗
      「id 查得於 CFTS022」，不驗該條文是否真的對應該葉；
      B1-GATE-1 抓到之 -002 指向 splash screen 一類的錯，lint 抓不到。
      **P6 寫回前必辦，不得以 lint 綠燈代替。**
  §5a：**同一未辦項連續三次出現於「該驗未驗」清單者，即刻升為
      下一階段之硬性前置**，不得再以「列入清單」處置 ——
      清單之功能是記住，不是延期。
```

### 執行層回報（下放包 12）

九項作業全數完成。停手條件逐項：#1 **未觸發**（12 個 gate 盤點後
缺負向對照者為 2 個，未達三個之門檻，已改標「未實測」）；
#2 **未觸發**；#3 **未觸發**（10 葉語意對應全部成立）；#4 台帳全綠。

**R34-10 兩項延宕事項本輪已辦**，不再列入未辦清單：
(a) 全 10 葉 Pre-Condition 逐句回溯 CFTS022；
(b) 全 10 葉 spec-reference 語意對應人工覆核。逐葉結果見上繳包 12 §5 / §6。

**一項需分析層知悉之實作決定**：BLOCKED 列使既有 lint gate 全面誤報
（design_method 空、priority 空、步驟 < 2、步驟/ER 不對等）。
執行層於 TC 加 `placeholder: true` 旗標，lint 對該類列改用一組
**placeholder 專屬 gate**（priority 與 design_method 須空、程序與 ER 須為
`BLOCKED - see Remarks`、Remarks 須帶已登記 marker），而非放寬既有 gate。
此旗標與 AMFM `write_back.py` 之 `placeholder` 慣例同名同義。

---

## R35 — 回溯產物與覆核機制化（分析層自裁，2026-08-13）

```text
[RULING] R35 — 回溯產物與覆核機制化（分析層自裁，2026-08-13）

R35-1  placeholder 旗標 —— 追認，且界線正確
  事實：BLOCKED 列會使既有四個 gate 同時誤報（design_method 空、
      priority 空、步驟 < 2、步驟/ER 不對等）。執行層未放寬既有 gate，
      改以 `placeholder: true` 導向一組專屬 gate
      （placeholder-body / placeholder-blank / placeholder-remarks）。
  裁：追認。**為一列而鈍化其餘十列之檢查，是以標準遷就實作**；
      改變實作而保留標準，方向正確。旗標名沿用既有 placeholder 慣例
      亦正確（不創新詞彙）。
  §5a：**當新增之合法列型使既有 gate 誤報時，正確處置是為該列型另立
      gate，不是放寬既有 gate。** 判準：修改後，原本會被抓到的違規
      是否仍會被抓到。

R35-2  [Off] 跨條文借用 —— 非違規，但產生引用義務
  事實：-006／-007 之 PC 2 使用 `[Off]`，其值域定義於 4915170
      （-005 之條文），不在 -006／-007 自身條文內。
  裁：**不構成 §8.4.2 之範圍杜撰** —— §8.4.2 之標的是「外部 spec」，
      而 4915170 與 4915171／4915172 同屬 CFTS022，同一 spec 內之
      跨條文引用為正常。
      但依 **§10.7「List every spec section the TC directly verifies
      or relies on as setup」**，產生引用義務：
      **-006／-007 之 `specification_reference` 加列 `CFTS022-4915170`**，
      排序由最具體到一般（本葉條文在前，被借用之值域定義在後）。
      `reasoning` 須註明該筆為 setup 依賴而非驗證標的。
  §5a：**同一 spec 內之跨條文借用不是範圍問題，是引用完整性問題**；
      兩者處置不同 —— 前者加引用，後者刪內容。

R35-3  `the HU has determined that…` —— 以客觀組態為觸發（保守方向）
  事實：4915174／4915175 之觸發含「HU 已判定 amplifier 不存在／存在」
      這個中間狀態；執行層之 PC 只設定客觀組態（PROXI 側）。
  裁：**PC 維持只設定客觀組態，不得斷言 HU 之內部判定狀態。**
      理由（方向性，非等同性）：
      「HU 已判定」是 HU 自客觀組態導出之內部狀態，測試者無法直接
      設定，亦無規格指定之可觀察指標。以客觀組態為觸發時，
      **判定環節被納入受測範圍** —— 若 HU 未能正確判定，TC 即 fail，
      而那正是應被偵測的失效。故此處置是**保守方向**（多測而非少測），
      符合不對稱錯誤代價原則。
      **禁止**：PC 不得寫「The HU has determined that the amplifier is
      not present」一類措辭 —— 那是對不可觀察內部狀態之斷言。
  `reasoning` 須載明：條文之觸發含 HU 之判定環節，本 TC 以客觀組態
      為起點，判定環節一併納入受測範圍。
  RD-1 新增 **#13**：請上游確認 HU 對 amplifier presence 之判定是否
      有規格指定之可觀察指標；若有，該指標應成為獨立之中間驗證點。
  **本裁決可逆** —— 若 Pei 或上游裁定判定環節應獨立驗證，
      -009／-010 須增加中間步驟，現行 TC 不需重寫，只需擴充。

R35-4  -006 ER 收斂 —— 追認，並記其切法
  事實：收斂前為「The HU has adjusted the output volume according to
      the speed controlled level」，同時斷言「有調整」與「依該 level
      調整」；收斂後只留「The output volume has changed」。
  裁：追認。切點正確 —— **前半是本條之標的（歸屬），後半是 CFTS019
      之標的（行為曲線）**，一句 ER 同時承載兩個 spec 之主張是本次
      最典型之越界形態。
      -007 未改動亦正確（其 ER 本即止於「level 未被 HU 改變」）。

R35-5  負向對照之鑑別力 —— baseline 型可接受，但須補邊界例
  事實：16 個 gate 缺對照 0；其中三個（test-group / step-er-parity /
      step-count）以 baseline 自身為負向對照，程式內標
      `PASS (baseline)` 而非隱去。
  裁：**標示法追認** —— 明標 baseline 型使讀者知悉其性質，優於隱去。
      但補一條原則：
      **負向對照之鑑別力，隨其與違規之距離遞減。** 乾淨之 baseline
      距違規最遠，只能證明 gate 不對「明顯合規」誤報，不能證明它不對
      **邊界合規**誤報。
      作業：該三項於 P6 前各補一個**邊界例**負向對照 ——
        step-count → 恰為 2 步之 TC（下界，須 PASS）
        step-er-parity → 單一步驟對應多行 ER 之合法形態（須 PASS）
        test-group → 與正確值僅差大小寫或尾隨空白之近似值（須 FAIL，
                     屬陽性對照之補強；另備一合法但不同 Test Set 之
                     值須 PASS）
      **非阻塞**，但 P6 前完成。

R35-6  -008 之語意對應正常 —— 此區分必須保留
  裁：追認執行層之註記。-008 之 artifact 與 leaf **語意完全對應**
      （037 標題 `Restore on AMP Wake-Up` 對條文 `the AMP shall
      recall`）；其問題是 **ECU 歸屬**，不是**對映錯誤**。
      兩者必須分開記載，否則日後會被讀成「-008 之
      specification_reference 也有問題」。
  §5a：**同一列上可能同時存在「正確的引用」與「錯誤的歸屬」**；
      覆核結論須逐面向分別陳述，不得以單一「有問題／無問題」概括。

R35-7  語意對應覆核之機制化 —— 一次性人工作業改為 ratchet
  事實：執行層指出 §6 之語意對應表為一次性人工作業，**無任何機制會在
      下次生成時重跑**；若 P6 之後某葉之 `specification_reference` 被
      改動，沒有東西會要求重做。
  裁：**建立 `features/privacy/data/spec_ref_reviewed.json`（進版控）**，
      逐葉記錄：leaf id / artifact id / 覆核日期 / 覆核依據
      （條文要旨 vs 葉子驗證目標之對應說明摘要）。
      lint 新增 gate：**各葉之 `specification_reference` 須與該檔記載
      相符；不符即 FAIL**，訊息指明「該葉之 spec_reference 已變動，
      語意對應覆核須重做」。
      該檔為**只增不改**：覆核重做時新增一筆並保留舊筆（同 DELIVERY
      台帳之 append-only 語意）。
      同 R20-2 之 ratchet 形態 —— 人工判斷之結果被固定下來，
      機制負責偵測它何時失效，而非重做判斷。
  §5a：**一次性人工覆核之結論，必須被固定為可比對之紀錄**；
      否則該覆核只在做完的當下有效。

R35-8  profile §3.2 之 PC 詞彙表未回溯 —— P6 前必辦
  事實：本輪回溯之標的為 **TC 之 PC**，非 **profile §3.2 之詞彙表**；
      而 `An external amplifier is present on the vehicle` 正出自
      分析層於下放包 04 起草、當時即自陳未回溯之該表。
  裁：執行層之區分正確（兩者是不同的東西，前者已辦後者未辦）。
      profile §3.2 詞彙表為 B3+ 與日後 regen 之來源，**P6 前必辦**：
      逐條回溯 CFTS022 原文，措辭不符者以原文為準修訂，
      無原文對應者標明其為測試設定用語而非 spec 措辭。
```

### 執行層回報（下放包 13）

八項作業全數完成，lint 全批 **PASS**。停手條件：#2 / #3 / #4 未觸發。

**#1 觸發並已處置，須分析層追認**：依 R35-2 加列 `CFTS022-4915170` 後，
既有 `spec-reference` gate 立即 FAIL，訊息為

```
'CFTS022-4915171; CFTS022-4915170' is not CFTS022-<7 digits>
```

執行層**未停在該處**，判斷理由如下：此非 gate 誤報（如 `er-modal` 之
`Interior CAN`），而是**規則本身改變** —— R35-2 使多引用成為合法形態，
而該 gate 編碼的是改變前之「單一引用」。故擴充 gate 以支援
`; ` 分隔之多引用，**每個成分仍逐一驗證**（形式須為 `CFTS022-<7 位>`
且該 id 須查得於 CFTS022 全集），並新增重複引用之檢查。
依 R35-1 之判準自檢：**修改後原本會被抓到的違規仍會被抓到** ——
格式錯誤、id 不存在兩類皆未鬆動，只是「一則參考可包含幾個成分」放寬。
若分析層認為應照停手條件字面停在該處，一句話即可回退。

**R35-8 之回溯結果超出預期**：profile §3.2 五個措辭中，
`external amplifier`、`on the vehicle`、`HU has exited` **三者在 CFTS022
全文命中數皆為 0**，`The AMP wakes up on Interior CAN` 漏了冠詞 `the`，
且 sleep-mode 之主詞應為 **A&T System** 而非 HU。已逐條依原文修訂。
停手條件 3 之判準為「三條以上**詞彙無原文對應**」—— 此處三個是**修飾語與
主詞錯誤**，其核心詞（amplifier / wakes up / SLEEP MODE）皆有原文對應，
故判定未達停手門檻，續行修訂。此判定之界線亦請追認。

---

## R36 — 停手條件之界線與起草缺陷（分析層自裁，2026-08-13）

```text
[RULING] R36 — 停手條件之界線與起草缺陷（分析層自裁，2026-08-13）

R36-1  停手條件 1 之處置 —— 追認，且該停手條件本身為起草缺陷
  事實：下放包 13 §2.2 指示為 -006／-007 加列第二個
      specification_reference；§3.1 同時規定「加列後未通過既有格式
      gate → 停止該項」。加列必然使該 gate FAIL（其編碼為單一引用）。
  裁：**執行層之續行正確，追認。** 擴充 gate 以支援 `; ` 分隔、
      各成分仍逐一驗證形式與 id 存在、另加重複引用檢查 ——
      並依 R35-1 判準自檢（原本會被抓到的違規仍會被抓到：
      格式錯誤與 id 不存在兩類皆未鬆動），程序完整。
  執行層之型別區分成立且應記入條文：
      **er-modal 那次** —— 規則未變，實作誤把縮寫當 modal → **修實作**
      **本次** —— 規則已由 R35-2 變更，實作編碼的是變更前的規則
                  → **擴充實作以符合新規則**
      兩者皆非「放寬標準」。
  §5a 新增（其一）：**停手條件所守護者是標準，不是實作。**
      當同一包內之裁決已變更該標準時，編碼舊標準之 gate 失效
      **不構成停手事由**；擴充 gate 使其符合新標準即可，
      但須逐項自檢 R35-1 判準並於上繳包載明。
  §5a 新增（其二，分析層自陳）：**一項停手條件若在所指示之動作下
      必然觸發，它不是停手條件，是自相矛盾的指示。**
      下放包 13 §2.2 與 §3.1 即為此形態。起草時須自問：
      「照這條作業做完之後，這條停手條件會不會必然成立？」

R36-2  停手條件 3 之界線 —— 追認，且門檻設定違反 canon §5a
  事實：profile §3.2 回溯查出三個字串於 CFTS022 命中數為 0，
      字面已達停手條件 3 之「三條以上」。執行層判定未達門檻，
      理由為該條件之**說理**寫的是「多數詞彙為自創時，該表之性質
      須重新裁定，非逐條修補可解」，而三者皆為修飾語或主詞錯誤，
      核心詞（amplifier / wakes up / SLEEP MODE）全有原文對應，
      修補後皆為 spec 逐字。
  裁：**追認。** 說理未成立，續行修訂正確。
  分析層自陳缺陷：「三條以上」是「多數為自創」之**代理判準**，
      而 canon §5a 明文「**代理判準（自資料推導之統計範圍）不得凌駕
      實質判準**」。以計數門檻表達性質判斷，即為該禁令所指之形態。
  §5a 強化：**停手條件之數量門檻若為某實質判準之代理，
      該條件須同時寫出實質判準，並明定衝突時以實質判準為準。**
      本例執行層之讀法正確 —— 說理優先於計數。

R36-3  profile §3.2 之錯誤性質 —— 詞彙表之權威是被假定的
  事實：分析層於下放包 04 起草之 §3.2 寫
      `The HU has exited Sleep Mode` —— **主詞錯**（條文為
      `the A&T System`）且**大小寫錯**（條文為 `'SLEEP MODE'`）。
      而 -001 之 TC 反而寫對（`The A&T System is in 'SLEEP MODE'`）。
  裁：記錄之。執行層之觀察「詞彙表比它產出的東西還不準」成立。
  §5a 新增：**詞彙表、常數表、樣板之權威是被假定的，不是被驗證的。**
      逐條產出會回到來源核對，詞彙表卻只被引用不被回溯 ——
      故未經回溯之詞彙表，其可靠度低於引用它的產出。
      推論：**任何被多處引用之集中式定義，其回溯優先度高於個別產出。**
  連動：profile §3.4／§4／§6 之措辭同樣未回溯（執行層已指出，
      且 §3.2 之三處錯誤顯示自創措辭非偶發）→ 見 §2.2。

R36-4  測試設定用語之明標 —— 追認並立為體例
  裁：CAN tool／audio source playing／default state 三者於 CFTS022
      無對應，明標為**測試設定用語**而非 spec 措辭 —— 追認。
      立為體例：**PC 詞彙表須逐條標明其來源類別**：
        `spec-verbatim`（逐字取自條文）
        `spec-derived`（自條文改寫，須附原文）
        `test-setup`（為使結果可觀察而設，無 spec 對應）
      未標類別者視為未回溯。

R36-5  `spec_ref_reviewed.json` 之覆核依據失效偵測 —— 採納執行層建議
  事實：執行層指出該檔只驗 reference 字串，不驗覆核依據仍成立；
      若 CFTS022 換版（artifact 內容改而 id 不變），字串不變，
      gate 不會發現覆核已失效。`BASELINE.sha256` 抓得到文件換版，
      但兩者目前無連結。
  裁：**採納。** 該檔各筆增記**覆核當時之 CFTS022 SHA256**，
      gate 比對現行 `BASELINE.sha256` 內 CFTS022 之值；
      不符即 FAIL，訊息為「來源文件已換版，語意對應覆核須重做」。
      此即把兩份台帳接起來 —— **素材完整性與判斷有效性之連結**。
  §5a：**基於某文件所做之人工判斷，其有效性繫於該文件之版本；
      紀錄判斷時必須一併記錄所依據之版本識別。**

R36-6  多引用之排序 —— 機制化
  裁：R35-2 所定之排序（本葉條文在前、setup 依賴在後）可機制化：
      **`specification_reference` 之第一成分，須等於
      `spec_ref_reviewed.json` 內該葉所記之 artifact。**
      lint 加此 gate，含陽性（顛倒順序須 FAIL）與負向
      （正確順序須 PASS）對照。

R36-7  test-group 近似值對照 —— 補
  裁：執行層自陳未辦且說明「加測試只是確認既有行為」——
      **仍須加**。理由即 R34-5：確認既有行為正是負向對照之目的；
      「本就會 FAIL」是推定，未實測前不得作為結論。
      加入 `"privacy"`（小寫）與 `"Privacy "`（尾隨空白）兩例，皆須 FAIL。
```

### 執行層回報（下放包 14）

§2 四項與 §3 寫回全數完成。停手條件逐項見上繳包 14 §0。
**未打 tag、未 commit、未交付，亦未宣告 P7 完成**（R29-1 之先例：
外科手術產出須經人以 Excel 實開確認方可升格）。

---

## R37 — 寫回覆核（分析層自裁，2026-08-13）

```text
[RULING] R37 — 寫回覆核（分析層自裁，2026-08-13）

R37-1  來源類別三分法之單一 spec 假設 —— 執行層發現成立，條文修訂
  事實：R36-4 之 `spec-verbatim` / `spec-derived` / `test-setup`
      隱含「只有一份 spec」。本 feature 引用兩份 —— `LTM Non-Amplified`
      與 `Amplified Audio System` 於 CFTS022 命中 0，但它們不是自創，
      是逐字取自 VF651 之檔名。
      若僅以「CFTS022 命中數」判斷，會把它們誤判為自創詞彙。
  裁：**R36-4 修訂** —— 標籤須**點名來源**：
      `spec-verbatim (CFTS022)` / `spec-verbatim (VF651 filenames)` /
      `spec-derived (<來源>)` / `test-setup`。
      執行層之處置正確且已為 §6 施行。
  §5a 新增：**分類標籤若隱含「只有一個來源」之假設，在多來源情境下
      會把「取自另一來源」誤判為「自創」。** 標籤須點名來源，
      而非僅標性質。判準：該標籤在來源數增加時是否仍可判定。

R37-2  bytes 變小不構成結構問題 —— 追認，並更正分析層先前之推理
       ⚠️ 本條「事實」段之 65,823 為**歸屬錯誤**，見 R42。條文結論不受影響，
          原文依例不改（同 R16 x14 計數之處置）。
  事實：寫回後 65,823 → 63,001 bytes，而 zip 成員 48 → 48（零增零減）、
      classic 3+1 / x14 2 前後相同、差異成員僅 `sheet6.xml`。
  裁：**追認。成員集合與 DV 計數為結構完整性之判準，位元組數不是。**
  分析層自陳：R14-C1 追認 AMFM P7 時，曾以「輸出比輸入大 34.79 KB，
      方向與 append 143 列相符」作為佐證。**該推理為代理判準**
      （以體積變化方向推斷內容變化），canon §5a 明文禁止其凌駕
      實質判準；當時所幸未賴以下結論，但該句不應再被援引。
      本例正是反例 —— 內容增加而體積減少（壓縮率隨內容改變）。
  §5a：**壓縮容器之體積變化不指示內容變化方向**；
      涉及 zip 型檔案之結構陳述，一律以成員集合與成員層雜湊為據。

R37-3  寫回腳本兩處設計 —— 追認
  (a) 欄位由**表頭文字**解析而非 `feature.yaml` 之字母
      （後者仍帶 rev C 前之字母，A-PV13）—— 追認。
      表頭文字為工作簿自身之事實，字母是外部記載，兩者衝突時
      以工作簿為準。
  (b) 車型欄由**合併儲存格橫幅**定位得 `T..Z`，橫幅找不到即 ABORT
      —— 追認。**不猜是正確的**：找不到橫幅時，欄位位置已無可靠來源，
      任何預設值都是杜撰。
  §5a：**由外部記載推得之位置資訊，若可自標的物本身讀出，
      一律以標的物為準**；標的物讀不出時 ABORT，不得回退至外部記載。

R37-4  BLOCKED 列四項驗證 —— 通過，追認
  裁：第 18 列 `NR1L-Privacy-009`。placeholder 旗標未進工作簿
      （JSON 層控制欄位，非儲存格值）；P／R／Q 與 T–Z 確為空；
      四個驗證欄位皆 `BLOCKED - see Remarks`；Remarks 288 字元逐字
      相符無截斷；字型／填色／框線／wrap／列高與第 17 列一致。
      **本 feature 第一個 marker 之寫回行為已驗證。**
      顯示層仍未驗（見 §2）。

R37-5  三項未實測項 —— 依 R34-5 標「未實測」，不得標 PASS
  裁：下列三項**不得以 PASS 記載**：
      (a) 寫回腳本自加之兩層 invariant（表頭區第 1–9 列逐格未變、
          其餘 9 分頁逐格相同）**無陽性對照** ——
          「刻意改動表頭時是否確實 ABORT」未驗
      (b) `spec-ref-source-version` gate 之陽性對照用人造 sha，
          真實換版下未觸發過，訊息是否足以引導正確處置未經現場檢驗
      (c) profile 其餘六節未標來源類別，依 R36-4 **形式上皆為未回溯**
      執行層已自行標明三者 —— 追認其判斷，本裁決僅使其成為條文。
  作業：(a) 於 §3.1 補陽性對照；(b)(c) 列為 close-out 項，
      **非交付阻塞**（見 §3.3）。

R37-6  B 欄公式無 cached `<v>` —— 與 AMFM v2 同型，本次即解
  事實：B 欄 11 格皆為公式且無 cached `<v>`，依賴 Excel 開啟時重算。
      AMFM v2 有同型情況，R17-9 至今未解。
  裁：**本次 Excel 實開即為該問題之首次實測**（§2 檢查點 5）。
      結果不論通過與否皆須記入條文 —— 通過則 R17-9 之疑慮於
      外科手術路徑上解除；不通過則寫回腳本須補寫 cached value，
      且 AMFM v2 之同型問題一併確立。
```

---

## R38 — Privacy P7 完成（Pei 確認 2026-08-13）

```text
[RULING] R38 — Privacy P7 完成（Pei 確認 2026-08-13）

R38-1  P7 完成
  裁：Pei 於 2026-08-13 開啟
      features/privacy/output/FM-WI-FSM-036-A01 …_Privacy_20260813_
      regen-v1.xlsx，下放包 15 §2 之七項檢查點全過：
        1. 無「檔案已損毀，Excel 已修復」提示
        2. R 欄設計方法下拉可用，選項為 下拉選單 之 9 條
        3. D5 範圍 Scope = SWE1_CFTS_022-Privacy_Features
        4. 第 10–20 列共 11 列 TC，其餘列為空
        5. B 欄序號顯示 1…11
        6. 第 18 列 Remarks 288 字元完整顯示，無截斷無亂碼
        7. 第 18 列字型／填色／框線與第 17 列一致
      **PLAYBOOK §6 之 P7 可勾。**
      產出：11 TC / 10 葉，SHA256 ad595ed0cad24375…，
      zip 成員 48（零增零減），classic 3+1 / x14 2 前後相同，
      差異成員僅 sheet6.xml。

R38-2  R17-9 / R37-6 —— B 欄 cached value 問題於外科手術路徑上解除
  事實：檢查點 5 通過 —— B 欄 11 格皆為公式且無 cached <v>，
      Excel 開啟時正確重算並顯示 1…11。
  裁：**此為該問題之首次現場實測**（此前皆為推論）。結論：
      **zip 層外科手術寫入之顯式公式，缺 cached <v> 不影響 Excel
        之正確重算。**
      連動：AMFM v2 之同型疑慮（R17-9）於機制層面消解 ——
      同一寫回路徑、同一形態。但 **AMFM v2 本身仍未經 Excel 實開**，
      本裁決不得被讀為「AMFM v2 已驗證」；
      它證明的是機制無此缺陷，不是那份檔案已被檢查。
  §5a：**機制之驗證與實例之驗證是兩件事**；證明機制不產生某類缺陷，
      不等於證明某個實例沒有該缺陷 —— 實例可能另有他因。

R38-3  BLOCKED 列全鏈路驗證完成
  裁：NR1L-Privacy-009（第 18 列，CFTS022-4915173）之
      [BLOCKED-ECU] marker 已通過**生成 → lint → 寫回 → 顯示層**
      全鏈路驗證（R34-3 立、R37-4 寫回層驗、R38-1 檢查點 6/7 顯示層驗）。
      本 feature 第一個 marker 之機制自此為實測有效。
```

### 執行層回報（下放包 15 / 16 合併）

**下放包 15 未曾執行** —— 其 R37 未入本檔、無 `docs/upstream/15_closeout.md`。
16 之 §2.1／§2.3／§2.5 多處引用 R37 之條號，故本輪一併補辦：
R37 已補貼（見上），15 §3 之作業與 16 §2 內容重疊者不重複執行，
結果合併回報於 `docs/upstream/16_p7_done.md`，該檔同時充當 15 之上繳包。

**R37-5(a) 之陽性對照已補**（15 §3.1 / 16 §2.1），三例皆確實 ABORT：
表頭 D5 改動、`下拉選單!A1` 改動、`Cover 封面!D7` 改動。
負向對照（未經破壞之實際產出）兩層皆通過。停手條件 1 未觸發。

**R38-2 之界線已照實施行**：`DELIVERY.sha256` 與 PLAYBOOK 皆記
「機制無此缺陷」而非「AMFM v2 已驗證」—— AMFM v2 本身仍未經 Excel 實開，
R17-9 就該實例而言未解。

---

## R39 — 往返積壓之機制化與交付前收尾（分析層自裁，2026-08-13）

```text
[RULING] R39 — 往返積壓之機制化與交付前收尾（分析層自裁，2026-08-13）

R39-1  下放包 15 未執行 —— 補辦追認，且此為同型第二次，須機制化
  事實：15_closeout.md 之 R37 未入 RULINGS.md、無 upstream/15，而
      下放包 16 之 §2.1／§2.3／§2.5 引用了四處 R37 條號。執行層察覺
      後補貼 R37（置於 R38 之前維持編號順序），重疊項不重複執行，
      本次上繳包兼充 15 之上繳包 —— **處置正確，追認**。
  同型前例：R17-1~R17-4 未入 RULINGS.md（R19-2 補正，起因為
      下放包 03 之作業清單漏列「貼入 RULINGS.md」）。
  裁：**第二次即非偶發。** 依 R19-3（宣稱排他之規則須有機械執行
      機制，非僅紀律），立機制：
      **執行層於每次上繳時，比對 `docs/handoff/` 與 `docs/upstream/`
        之 NN 集合；缺對應者逐一列出於上繳包首節。**
      合併執行者以 `NN → merged into MM` 註記，該註記使該 NN 視為
      已對應。缺對應且無註記者，**停手回報**。
      此檢查與 charter 之「執行層每次上繳更新 INDEX.md」併行 ——
      INDEX 記發生了什麼，本檢查記**該發生而未發生**什麼。
  §5a：**「引用了某條文」不蘊含「該條文存在於 repo」**；
      下放包引用他包條號時，須先確認該包已有上繳紀錄。

R39-2  A-PV13 之誤標 —— 追認更正，但處置方向須改
  事實：A-PV13 原標 `RESOLVED (執行層已處置)`，實測 `feature.yaml`
      仍記 `design_method: "Q"` / `functional_safety: "R"` /
      `author: "Z"`，而 rev C 實際為 `R` / `S` / `AA`，落差從未消失。
      當初之 RESOLVED 指「recon 會回報落差」，非「落差已修」。
      執行層已改 `DEFERRED — 記載與實作不一致，實作以表頭為準
      （R37-3(a)）`。
  裁：**誤標之發現與更正追認。** 但「不修 feature.yaml 以保留
      recon 回報作為證據來源」之理由 **不成立**，處置方向改為修：
      (a) 證據不會因修檔而消失 —— **A-PV13 條目本身即證據載體**，
          其內記載修前值、修後值、量測日期與依據，效力不弱於
          recon 之逐次回報
      (b) 保留已知錯誤之記載作為告警來源，等同**以缺陷充當金絲雀**；
          代價是任何以本 feature 為樣板之後續 feature 會繼承錯誤字母
      (c) R37-3(a) 已裁「位置資訊以標的物為準」，故該三欄之字母
          對產出無效力 —— 修正為低風險
      作業：修 `feature.yaml` 三欄為 `R` / `S` / `AA`；
      A-PV13 改 **RESOLVED**，條目內完整記載修前值、修後值、
      量測依據（範本 rev C 表頭實測）與本裁決編號。
  §5a：**不得以保留缺陷之方式維持告警**；告警之正確載體是登記，
      不是缺陷本身。

R39-3  狀態板自相矛盾之補正 —— 追認，並立為體例
  事實：P7 已勾而 P4／P5／P6 未勾。執行層自行補勾並填入實測值，
      同時清掉兩行過時記載，且**照實聲明該值未經分析層核對**。
  裁：**追認補正**。依 R28-3，狀態板之單調性缺陷屬**事實性補正**
      （後階段已完成而前階段未勾，本身即登記錯誤），得逕行執行
      並於上繳包載明，不必回報待裁。
  分析層核對 P5 之 verdict：與下放包 10（B1 pilot review）之裁定
      相符 —— 「-001…-004 通過（附 D2／D3 修正），-005 待 P-6 裁定」，
      其後由 R33 結案；D1／D2／D3 三項修正亦與 10 §1 之分類一致。
      **P5 之回填值核可。**

R39-4  三層 invariant 之陽性對照 —— 追認，並嘉許加測第三例
  裁：三例皆 ABORT，三層 invariant 自此為實測有效。
      執行層自行加測 `Cover 封面!D7` 之理由成立且重要：
      `下拉選單` 為 lint 詞彙權威、可能享有特殊路徑，
      而 `Cover 封面` 為純文件管制頁 —— 加測後方能排除
      「只有特定分頁被監看」。
  §5a：**陽性對照之選點須涵蓋「可能被特殊處理」與「應無特殊處理」
      兩類標的**；只測前者無法區分「機制生效」與「該標的恰好被顧到」。

R39-5  DELIVERY 台帳條目之狀態讀法 —— append-only 語意細化
  事實：ENTRY 002 標頭寫「非交付件」「執行層不宣告 P7 完成」，
      其後加註寫「P7 完成，本條目自此為交付候選」——
      兩者皆為真（標頭記產出當時、加註記其後確認），
      但只讀標頭會得到相反結論。R27-2 之 append-only 禁止改寫標頭。
  裁：**不改寫標頭**（維持 append-only）。改以讀法規則解決：
      **台帳條目之現行狀態，以該條目之最後一行為準；
        讀取條目時須讀至該條目結束，不得只讀標頭。**
      並要求：**每一次加註之末行須為狀態行**，格式
      `STATUS: <狀態> (<裁決編號>, <日期>)`，
      使「最後一行即狀態」成為可依賴之不變式。
      ENTRY 001／002 各補一行 STATUS 行（追加，不改寫既有內容）。

R39-6  tag annotation 之數值須獨立複驗
  裁：執行層指出 annotation 數值為同一次量測之轉錄而非獨立複驗
      —— 成立。打 tag 前須重跑並產出**獨立數據**供 Pei 比對：
      `shasum -a 256` 對交付檔、zip 成員集合、各 sheet classic／x14
      DV 計數、資料列數與列範圍、lint 全批。
      與 annotation 草案逐項並列；不符即停手，**不得以草案值為準**。
  §5a：**tag annotation 是封存陳述，其每一數值須有獨立於草稿之量測**；
      轉錄不構成驗證（同 R15-3 之「重測獨立性有層級之分」）。
```

### 執行層回報（下放包 17）

**停手條件 4 觸發** —— 首份 handoff／upstream 對應表查出缺對應者
**七個**（05 / 06 / 08 / 10 / 15 / 17 / 18），遠不止 15／16。
依該條「停止其餘，續行回報缺口清單」：**第 5 項（打 tag 前之獨立複驗）
未執行**，第 1–3 項照辦（該三項於本包 §3 之序列中位於第 4 項之前）。
缺口清單與逐項處置見 `docs/upstream/17_predelivery.md` §1。

**R40（下放包 18）未貼入** —— 依 Pei 指示「18 §2 待交付後再辦」，
而貼入 R40 為 18 §2.1。對應表內註記為「待交付後執行」而非
「merged into」，因後者蘊含已執行。

---

## R42 — R37-2 實例之歸屬更正（Pei, 2026-08-14，chat）

> **編號由執行層暫配**（R31-1）。本裁決自 chat 直下、未經下放包。

```text
R42-1  65,823 之性質 —— 歸屬錯誤，非量測錯誤
  事實（雙方獨立量測，值相同）：
      65,823  空白範本 inputs/…_SWQT_20260121.xlsx
         ↓    準備階段（R23-4 清五格 + R23-5 填 D5）
      59,992  ENTRY 001 準備工作簿 —— **寫回之真正輸入**
         ↓    寫回（append 11 列 TC）
      63,001  ENTRY 002 產出
  裁：**65,823 這個數本身沒錯 —— 它是空白範本的大小。
      錯的是歸屬：分析層把它標成了寫回的輸入。**
      故本項為歸屬錯誤，不是量測錯誤；R37-2 之條文結論
      （壓縮容器之體積變化不指示內容變化方向）自始正確。

R42-2  65,823 → 63,001 之實例仍然成立 —— 但其標籤須更正
  裁：該比較作為**跨兩次操作**（準備 + 寫回）之陳述**仍然成立**，
      且仍是「內容增加（多了 11 列 TC）而體積減少」之真實實例 ——
      **它不是假的，只是跨越了準備與寫回兩步，不是寫回那一步。**
      更正後之表述須指明其跨兩步。

R42-3  主實例改採準備階段那一對
  裁：採納執行層之建議，以**準備階段**為 R37-2 之主實例：
        65,823 → 59,992（少 5,831 bytes）
      清五格文字、填一格文字，**淨內容變化極小，體積卻少 5,831 bytes**
      —— 體積變化與內容變化**不成比例**，這比「方向相反」更能說明
      該條要說的事。成因為 sharedStrings 之引用結構改變。

R42-4  源頭與其違反之規則 —— 分析層自陳
  事實：upstream/14 之結構驗證表寫 65,823，handoff/15 將其抄入
      R37-2 之「事實」段，**未回頭核對該數屬於哪個檔案**。
  裁：此違反 **R15-3**（重測之獨立性有層級之分，陳述時必須指明是哪一種）
      —— 抄錄一個數字並將其當作實測陳述，連來源是哪個檔都未確認。
  §5a：**轉錄之數值須連同其標的一併轉錄**；只轉數字不轉標的，
      數字會在下一份文件裡換一個標的而不被察覺。

R42-5  R39-6 之首次執行即命中
  裁：記錄之。R39-6（tag annotation 之每一數值須有獨立於草稿之量測）
      係於本錯誤發生兩包之後方立，而**其首次執行即抓到分析層自身之錯**。
      12 項複驗中 11 項相符、1 項不符，不符者正是唯一一個
      「轉錄而未重新量測」之數。
```

### 執行層回報（R42）

- **R37-2 原文未改**，僅於標題行下加一行指標（同 R16 x14 計數之處置）——
  已簽署條文之更正以附記為之，不改寫。
- 六處落點之處置分三類，見下：

| 落點 | 性質 | 處置 |
|---|---|---|
| `RULINGS.md` R37-2 | 已簽署條文 | 加指標，原文不改 |
| `PLAYBOOK.md` §6 | 現行狀態文件 | **更正** |
| `docs/upstream/14_writeback.md` | 已提交紀錄 | **加註不改寫**（已提交之紀錄不因後續事件而失效）|
| `docs/upstream/16_p7_done.md` §5.2 tag annotation 草案 | **待使用之產出** | **更正**（草案是要拿去用的，不更正等於留錯）|
| `docs/upstream/16_p7_done.md` §3 PLAYBOOK 引用 | 已提交紀錄 | 加註 |
| `docs/handoff/15_closeout.md` | 分析層文件 | **未動** |

**停手條件 1 之狀態**：本裁決解釋並更正了該差異，但**未明示解除停手**。
故 19 §2.2 之 close-out 四項與 §2.3 交付後各項**仍未執行**，待指示。

---

## R41 — 對應檢查之界線與機制化（分析層自裁，2026-08-13）

```text
[RULING] R41 — 對應檢查之界線與機制化（分析層自裁，2026-08-13）

R41-1  順序調換之判準 —— 追認，並精確化
  事實：執行層將 17 §3 第 4 項（對應檢查）提前執行，理由為成本低、
      為停手標的、應在投入後續前先知；停手觸發後仍完成第 1–3 項，
      因「照原序執行時該三項會在停手觸發前完成」，僅停第 5 項。
  裁：**追認**，且此推理應立為 R22-6(c)（執行層得調換順序）之配套判準：
      **順序調換不得改變停手所影響之範圍。**
      判準：照**原序**執行時，該項是否會在停手觸發前完成 ——
      會 → 調換後仍應完成；不會 → 調換後亦不得完成。
      調換與其影響範圍之推理須於上繳包載明。
  §5a：**流程調換之正當性，不在於調換本身有無道理，
      而在於調換後之結果集合與原序相同。**

R41-2  停手條件 4 之解除
  裁：對應表查出七個缺對應（05／06／08／10／15／17／18），
      經執行層分類後，真正之缺口為二：**08** 與 **10**，
      且兩者性質不同（見 R41-3、R41-4）。
      兩者皆不影響交付件之內容或結構 → **停手解除**，
      17 §3 第 5 項（獨立複驗）即刻續辦。

R41-3  10 —— 非缺口，係下放包設計如此；須有明示標記
  事實：下放包 10（B1 pilot review）之 §5 為「覆核意見」，
      本即不要求上繳包。R39-1 之機制無法區分「設計上不要求」與
      「要求了但沒產」。
  裁：**執行層之建議採納。** 下放包若不要求上繳包，
      須於該包明寫標記（格式見 R41-5）。
      **下放包 10 補加該標記**（事實性補正，R28-3）。

R41-4  08 —— 真缺口，但不補產
  事實：下放包 08 有上繳要求、已執行，但因 B1-GATE-1 之停手被切成
      兩段，補辦時未回頭補產上繳包。
  裁：**不補產。** 事後撰寫上繳包等同以記憶重建執行紀錄，
      違反 canon §5a（不以自身先前輸出為來源）與
      「不得重建歷史往返包」之既有處置（下放包 01 §2.7）。
      改以**照實標記**：對應表記
      `08 → no upstream produced（執行被 B1-GATE-1 切分，未回頭補產）`。
      若 08 之執行結果實際已載於其後某包之上繳包，
      改記 `08 → reported within NN` 並指明落點；
      **此二者擇一須以實測認定，不得推定**。
  §5a：**紀錄之缺口應被標記，不應被填補**；填補使缺口消失而未使
      該次執行變得有紀錄，反而妨礙日後查證。

R41-5  對應標記之機器可讀格式
  事實：現行三處合併註記為自然語言敘述，非格式字串；本輪對應表
      係人工讀出而非解析所得。執行層指出此為 R39-1 機制化之前提。
  裁：定格式，各下放包於檔末（自檢表之後）置一行：

        <!-- HANDOFF-LINK: <本包NN> -> <狀態> -->

      `<狀態>` 之合法值：
        `upstream:<NN>`          本包之上繳包編號（常態）
        `merged into <NN>`       本包之上繳併入該包
        `no-upstream-required`   本包設計上不要求上繳包
        `no-upstream-produced`   應產而未產（缺口，照實標）
      既有各包由執行層依實測回填，**不得推定**；
      無法認定者標 `unknown` 並列於上繳包。

R41-6  R39-1 之機制化（承 R19-3）
  裁：R39-1 目前為人工執行，依 **R19-3**（宣稱排他之規則須有機械
      執行機制）須機制化。建常駐測試：
        掃描 `features/privacy/docs/handoff/` 之各檔，解析 R41-5 之
        `HANDOFF-LINK` 行；狀態為 `upstream:<NN>` 者，
        `docs/upstream/` 須存在對應檔；缺標記或標記不合法即 FAIL。
      **初期僅對 `features/privacy` 生效**（其餘 feature 之往返多未
      落檔，非本輪標的；擴及他 feature 需另裁）。
      須自帶陽性對照（移除某包之標記須 FAIL）與負向對照
      （合法之 `no-upstream-required` 須 PASS）。
  §5a：**「本輪用腳本跑過一次」不等於機制化**；
      機制之判準是下一次是否會自動執行，而非本次是否用了工具。

R41-7  STATUS 行位置之更正 —— 追認，並定條目形狀
  事實：首次補入時 ENTRY 001 之 STATUS 落在雜湊行之前、
      ENTRY 002 落在之後，不一致且前者不符「末行即狀態」。
      已移正為「敘述 → 雜湊 → STATUS」。移動者為本次新增內容，
      未改寫既有欄位。
  裁：**追認**，並定 DELIVERY 台帳條目之標準形狀：
      **敘述段 → 雜湊段 → STATUS 行（末行）**。
      加 lint gate：各 ENTRY 之最後一行須符
      `STATUS: <狀態> (<裁決編號>, <日期>)`；不符即 FAIL。
      含陽性對照（STATUS 非末行須 FAIL）與負向對照（合法條目須 PASS）。
      **此 gate 須於 ENTRY 003 新增前上線**（R40-1(c) 已要求
      ENTRY 003 含 STATUS 行，而本輪已發生一次寫錯位置）。

R41-8  A-PV13 之根因在 `new_feature.py` —— 登記，交付前不動
  事實：執行層指出 `new_feature.py` 之樣板仍寫舊字母，
      下一個新 feature 仍會拿到 `Q` / `R` / `Z`；本輪只修了
      Privacy 之實例。
  裁：**成立，但交付前夕不動共用 script。**
      登 **A-PV19**，狀態 `DEFERRED — 待 Pei 裁定（R41-8）`。
      分析層之修正方向建議（供日後裁定，本包不執行）：
      **樣板不應內建欄位字母。** 依 R37-3(a)（位置資訊以標的物為準），
      正解是樣板留空或標 `AUTO`，由 recon／writer 自表頭解析 ——
      而非把 `Q/R/Z` 改成 `R/S/AA`（後者只是把錯誤換一個版本，
      遇到非 rev C 之範本會再錯一次）。
```

---

## R43 — 更正處置之體例化與停手解除（分析層自裁，2026-08-13）

```text
[RULING] R43 — 更正處置之體例化與停手解除（分析層自裁，2026-08-13）

R43-1  停手解除
  裁：19 §3.1 之停手觸發已由 R42 完成裁定與更正，交付件之內容與
      結構自始未受影響（12 項複驗中 11 項相符，唯一不符者為敘述面
      之歸屬錯誤）。**停手解除。**
      19 §2.1 第 2 項（STATUS 格式 gate）與 §2.2 close-out 四項
      即刻續辦；§2.3 交付後各項待 Pei 告知。
  執行層未自行解除 —— **處置正確**。分析層於前一輪解釋並裁定了差異，
      但未明示解除，執行層未以「爭議已澄清」推定解除。
  §5a：**停手之解除須明示。** 爭議之澄清、原因之查明、責任之歸屬，
      三者皆不蘊含停手解除；解除是獨立之裁決動作。

R43-2  更正處置之三分法 —— 追認，並立為通則
  事實：執行層依落點性質將六處分三類處置：
      已簽署條文（RULINGS R37-2）→ 加指標，原文不改
      已提交紀錄（upstream/14、upstream/16 §3、handoff/15）→ 加註不改寫
      現行狀態文件（PLAYBOOK §6）→ 就地更正
      待使用之產出（upstream/16 §5.2 之 tag annotation 草案）→ 直接改內文
  裁：**追認，並立為通則。** 更正之處置依落點性質決定，不依錯誤性質：
      (a) **已簽署條文與已提交紀錄** —— append-only，加註不改寫。
          理由：它們記錄的是「當時作成之判斷」，改寫會使該判斷看似
          從未出錯，妨礙日後查證
      (b) **現行狀態文件**（PLAYBOOK §6、狀態板、對應表）——
          就地更正並註記裁決編號。理由：其功能是陳述現況，
          保留過時陳述即為不實記載
      (c) **待使用之產出**（tag annotation 草案、commit message、
          交付文件）—— **直接改內文**。理由如執行層所述：
          **「它是要拿去用的，加註等於留錯。」**
      三者之判準是「該文件將被讀作歷史、現況、還是被執行」。

R43-3  轉錄之標的 —— 採納執行層所導出之條文
  裁：逐字採納 R42-4 之衍生條文，記入 §5a：
      **轉錄之數值須連同其標的一併轉錄；只轉數字不轉標的，
        數字會在下一份文件裡換一個標的而不被察覺。**
      本例之路徑即為佐證：`65,823` 於 `upstream/14` 已標錯標的
      （「輸入基準」欄），抄入 `handoff/15` 時連錯標的一併帶走，
      再抄入 tag annotation 時已無人記得其來源。
  連動：本條與 R42 之「歸屬錯誤而非量測錯誤」互為表裡 ——
      前者說明錯誤如何傳播，後者說明其處置為何是換標籤而非作廢實例。

R43-4  R39-6 之命中特性 —— 記錄
  裁：12 項獨立複驗中 11 項相符，**唯一不符者正是唯一一個
      「轉錄而未重新量測」之數**；其餘 11 項皆為當場自檔案量出。
      記錄之，作為 R39-6（annotation 數值須獨立複驗）之效力證據。
  §5a：**規則之效力應以其命中之分布評估，不只以命中數評估。**
      本例中，不符項與「未重新量測」之集合完全重合 ——
      這比「抓到一個錯」更能說明該規則抓的是對的東西。

R43-5  R37-2 之主實例更換
  裁：R37-2 之 §5a 條文**不變**（壓縮容器之體積變化不指示內容變化
      方向；zip 型檔案之結構陳述一律以成員集合與成員層雜湊為據）。
      **主實例改採準備階段**：`65,823 → 59,992`，內容變化為
      「清五格 + 填一格」而體積少 5,831 bytes ——
      重點是**不成比例**，非方向相反。
      次要實例保留 `65,823 → 63,001`（空白範本 → 最終產出，
      **跨準備與寫回兩步**）：內容淨增 11 列 TC 而體積淨減 2,822 bytes。
      兩實例皆經分析層獨立複驗（65,823 與 63,001 取自分析層自有副本，
      59,992 與目錄列示之 58.59 KB 一致）。
      三段鏈為：`65,823 空白範本 → 59,992 ENTRY 001 → 63,001 ENTRY 002`。
```

---

## R44 — 對應標記補完與交付放行（分析層自裁，2026-08-13）

```text
[RULING] R44 — 對應標記補完與交付放行（分析層自裁，2026-08-13）

R44-1  STATUS gate 之裝飾行誤判 —— 修實作，追認
  事實：gate 首次上線即報 ENTRY 001 FAIL，訊息「末行是 '#'」。
      該 `#` 為條目間之視覺分隔行（寫 ENTRY 002 時作為前導加入，
      位置落在 ENTRY 001 區塊尾），STATUS 本身位置正確。
      執行層將裸 `#` 排除於「內容行」定義外，標準未動。
  裁：追認。此為 R36-1 型別區分之第三次適用：
        1. er-modal 誤把 `Interior CAN` 當 modal —— 標準未變 → 修實作
        2. spec-reference 拒絕多引用 —— 標準已由 R35-2 變更 → 擴充實作
        3. ledger-status-last 把裸 `#` 當內容 —— 標準未變 → 修實作
  §5a：**一項判準經三次不同情境適用而皆給出明確答案者，
      得由「條文」升格為「已實測有效之判準」**；此後援引時不必
      重新論證其適用性，僅需指出屬何型。R36-1 自此為該等級。

R44-2  `HANDOFF-LINK` 增列第五、第六值
  事實：執行層指出下放包 18 之狀態無合法值可表達 —— 標
      `merged into 17` 是對未發生之事的宣告（違反 R41-5「不得推定」），
      標 `no-upstream-produced` 為不實（它不是應產而未產，
      是尚未到產出的時候）。依停手條件 3 標 `unknown` 不停手，
      但 `unknown` 之語意為「無法認定」，而 18 之狀態完全可以認定。
  裁：**建議採納。** R41-5 之合法值增列：
        `pending:<NN>`            已宣告落點但尚未執行（可認定之未完成態）
        `chat-direct:<裁決編號>`  該輪裁決由 chat 直下、未產下放包
      下放包 18 改標 `pending:17`，交付後由執行層改為 `merged into 17`。
  §5a：**狀態值集合若無法表達一個可明確認定之狀態，
      該集合不完整**；此時應增列值，不得以「無法認定」代替
      「尚未發生」——兩者之後續動作不同。

R44-3  編號 20 之缺口 —— 分析層之責，且揭露一個新型缺口
  事實：執行層指出 `handoff/` 由 19 跳至 21，並正確判定其非缺口
      （測試掃描實際檔案，不假設編號連續）。
  裁：**跳號係分析層編號時之疏失**，非設計。但其對應之輪次確實存在：
      **R42（bytes 歸屬錯誤之更正）係 chat 直下裁決、未產下放包**，
      由執行層依 R31-1 暫配編號並直接記入 `RULINGS.md`。
      故 20 之空位對應該輪。
      作業：對應表增列一行
      `20 -> chat-direct:R42`（R44-2 之新值）。
  §5a：**chat 直下之裁決雖已入 repo（R31-1 合法），
      仍在往返鏈上留下缺口**；該缺口須以標記顯性化，
      否則日後查證該輪之作業依據時無起點可循。

R44-4  parity 測試之反向檢查 —— 追認並立為體例
  裁：執行層自加 `test_no_upstream_is_orphaned`（無人指向之上繳包
      同樣是紀錄鏈斷裂）—— **追認**。R41-6 原僅要求單向
      （handoff 有而 upstream 無）。
  §5a：**對應關係之檢查須雙向。** 單向檢查只能發現「該產而未產」，
      發現不了「產了而無來源」；兩者皆為鏈斷裂。

R44-5  08 之實測認定 —— 追認
  裁：`no-upstream-produced`。依據：`upstream/07` §2 明載
      「下放包 08 全部（R29）→ 未執行」；其後 R30 解除停手時補辦，
      執行結果僅存於 `RULINGS.md` R29／R30 之回報段，無上繳包涵蓋。
      依 R41-4 標記而不補產 —— 正確。

R44-6  tag annotation 不記可變計數
  事實：執行層指出 annotation 內之「gate 數 20」會隨每次新增 gate
      而過時。
  裁：**採納。** annotation 改記
      **「所有 lint gate 均具陽性與負向雙對照」**，不記數量。
  §5a：**封存陳述不得包含會隨後續變動而過時之計數；
      應記述性質，不記數量。** 判準：該陳述在被封存後若因他處變動
      而變假，即不應寫入封存。
      同理適用於 tag annotation 內任何「目前有 N 個…」形態之陳述。

R44-7  HANDOFF-LINK 標記正確性未經驗證 —— 採納方向，列為 close-out
  事實：測試驗「標記存在、格式合法、所指之上繳包存在」，
      不驗標記所述是否為真 —— 05 標 `merged into 07`，
      測試只確認 07 存在，不確認 07 真的涵蓋 05。本輪依據為人工判讀。
  裁：**方向採納** —— 上繳包亦帶標記
      `<!-- UPSTREAM-COVERS: NN[, NN…] -->`，
      parity 測試改為比對兩側標記之互指一致性。
      **非交付阻塞**，列為 close-out（見 §2.3）。

R44-8  `unknown` 之到期 —— 加警示，不 FAIL
  裁：parity 測試對每一 `unknown` 輸出警示（**不 FAIL**），
      並要求上繳包首節逐項列出其認定障礙。
      下放包 18 依 R44-2 改標 `pending:17` 後，此項於本 feature
      暫無用例，但機制須先具備。

R44-9  AMFM 之同型缺口 —— 登記，不處理
  事實：執行層指出 AMFM 之下放包 03 亦無對應上繳包，
      與 Privacy 之 08 同型，且正是 R17-1~R17-4 遭擱置之來源包。
  裁：**登記，本輪不處理。** 依 Pei 2026-08-13 之裁示
      （「只專心做 Privacy」）與 R18-1（做過的不重產），
      AMFM 不在現行工作焦點內。
      記入 `features/privacy/ANOMALIES.md` 之 A-PV20（**跨 feature 觀察**），
      狀態 `DEFERRED — 待 AMFM 重啟時處理`。
      parity 測試維持僅涵蓋 `features/privacy`（R41-6）。
```

### 執行層回報（下放包 22）

§2.1 三項完成，三項停手條件皆未觸發。**交付前之執行層作業至此結束。**
§2.2（交付後）與 §2.3（close-out）未執行。

**R44-3 之一項實作說明**：`20 -> chat-direct:R42` 之落點為**上繳包之對應表**，
非下放包檔內標記 —— `handoff/20_*.md` 不存在，無檔可標。
parity 測試掃描實際檔案，故該行不進測試範圍；它記錄的是
「該編號對應之輪次存在於 `RULINGS.md` R42，而非存在於某個下放包」。

---

## R40 — Privacy 交付檔名與 ENTRY 003（Pei 簽署 2026-08-13）

```text
[RULING] R40 — Privacy 交付檔名與 ENTRY 003（Pei 簽署 2026-08-13）

R40-1  交付檔名
  裁：採選項 A ——
  (a) `features/privacy/output/` 內之產出檔**維持現名**
      `FM-WI-FSM-036-A01 …_SWQT_Privacy_20260813_regen-v1.xlsx`
      理由：`output/` 內已有 `…_SWQT_Privacy_20260813.xlsx`
      （ENTRY 001 之準備工作簿），改名會撞名；且 DELIVERY 台帳
      之路徑記載須與實體一致。
  (b) 交付至 `10_Reviewing/` 時**另存**為
      `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
       Specification & Result_SWQT_Privacy_20260813.xlsx`
      —— 與 AMFM（`…_AMFM_20260810.xlsx`）／
      SXM（`…_SXM_20260813.xlsx`）之命名一致
      （分析層對該兩份交付檔實測確認其不帶後綴）。
  (c) 交付後追加 **ENTRY 003**，欄位：
      交付路徑 / 交付檔名 / SHA256 / bytes / 交付日期 /
      「內容同 ENTRY 002，僅檔名與位置不同」之註記 /
      末行 `STATUS:`（依 R39-5）
      **SHA256 應與 ENTRY 002 相同**。
  (d) 交付後對**交付副本**重算 SHA256 與 ENTRY 002 比對；
      **不符即停手**，不得以「複製應該不會變」為由略過。

R40-2  ENTRY 003 之新增時點
  裁：ENTRY 003 於**交付動作完成後**新增，不得預先寫入。
      理由：台帳記錄之單位為已發生之事實（R27-2、R39-5）；
      預寫之條目在交付未執行時即為不實記載。
      交付屬 Tier 3（僅 Pei），故 ENTRY 003 之新增為交付後之
      執行層作業，須由 Pei 告知交付已完成後方得辦理。

R40-3  交付位置
  裁：`10_Reviewing/00_TestCase/` 之下，**實際路徑由 Pei 於交付時決定**。
      分析層不指定 —— 依 charter，交付形式、交付位置、送達執行
      均屬 Pei 之裁定範圍。
      既有同類路徑供參（分析層實測）：
        `ASW-R2/AMFM/`、`ASW-R2/SiriusXM/`、
        `ASW-R2/Privacy Mode/`（本 feature 素材來源目錄）
```

### 執行層回報（下放包 18，交付後執行，2026-08-14）

交付已完成（Tier 3 動作經 Pei 明確授權後由執行層代為執行，見文末附記）。

- **R40-1(a)**：`output/` 內之產出**維持原名** `…_regen-v1.xlsx`，未改名
- **R40-1(b)**：另存至
  `10_Reviewing/00_TestCase/ASW-R2/Privacy Mode/…_SWQT_Privacy_20260813.xlsx`
  （去 `_regen-v1`，與 AMFM／SXM 命名一致）。交付路徑由 Pei 指定（R40-3）
- **R40-1(d)**：交付副本重算 SHA256 = `ad595ed0cad24375…`，
  與 ENTRY 002 **逐字元相符**；bytes 63,001、zip 成員 48、
  sheet6 DV classic 3 / x14 2 亦一併複驗相符。停手條件 1 未觸發
- **R40-2**：ENTRY 003 於交付動作完成**之後**新增，未預寫

**⚠️ 本裁決之命名規則產生一組同名不同容（A-PV04 型）**，見 A-PV21。

**Tier 3 附記**：本專案 charter 自 00 包起訂「git 與交付操作僅 Pei」，
執行層歷份上繳包均回報「未執行任何 git 操作」。2026-08-14 起有兩次例外，
皆經 Pei 於 chat 明確授權：`git tag -a fw036-privacy-v1`（本輪）與
本次交付複製。commit 仍由 Pei 自行執行。記此以免日後查證時與 charter 對不上。

---

## R45 — 封存陳述之時點限定與 pending 到期（分析層自裁，2026-08-13）

```text
[RULING] R45 — 封存陳述之時點限定與 pending 到期（分析層自裁，2026-08-13）

R45-1  定稿前之全項重量 —— 追認，並立為 §5a
  事實：R44-6 僅要求移除 gate 計數、其餘數值不動。執行層仍將 13 項
      全部重新量測（SHA256 ×2、bytes ×3、zip 成員、差異成員、DV ×3、
      資料列、列範圍、leaf 數），理由為「『不動』是對前輪結果的信任，
      而前一輪正是靠不信任轉錄才抓到 bytes 的歸屬錯誤」。全符。
  裁：**追認，並立為條文。**
      **封存前之最終量測不得繼承任何前輪結果，即使前輪剛驗過。**
      理由：封存之效力及於其後全部引用；一旦封存，錯誤之更正成本
      自「改一行」升為「加註不改寫 + 六處落點追溯」（R42 之實例）。
      故封存前之量測，其獨立性要求高於任何中途檢查。

R45-2  annotation 之 anomaly 計數行 —— 加時點限定，不刪
  事實：執行層指出 annotation 尚有一行可變計數
      `Anomalies: 13 RESOLVED, 1 CLOSED, 6 DEFERRED, 0 open PENDING.`
      A-PV20 登記後 DEFERRED 即變 7，於 R44-6 之判準下同屬
      「會過時的計數」。執行層未自行更動，因其屬 annotation 內容
      之裁定 —— **處置正確**。
  裁：**不刪，加時點限定，並刪除與放行無關之分布。** 改為：

        Anomalies at tag time (2026-08-13): 0 open PENDING.

      兩項處置各有理由：
      (a) **加時點限定** —— 可變計數一旦限定時點即成為歷史事實，
          不會因其後變動而變假。R44-6 之判準
          （「封存後若因他處變動而變假即不應寫入」）
          於限定時點後不再觸發。
      (b) **刪除分布** —— `0 open PENDING` 是**交付放行之判準**；
          RESOLVED／CLOSED／DEFERRED 之分布是**repo 之狀態快照**，
          與被封存物無關。
  §5a 新增：**封存陳述應只含關於被封存物之事實，
      與作成封存時所依據之放行判準；不應含 repo 之全域狀態快照。**
      判準：該陳述所描述的是「這份產物」還是「這個倉庫」——
      後者不屬封存範圍。
      可變計數若確有必要保留，**一律加時點限定**。

R45-3  `chat-direct` 標記之寄生問題 —— 執行層發現成立
  事實：`handoff/20_*.md` 不存在，`20 -> chat-direct:R42` 之標記
      無檔可標，只能存於上繳包之表格；而 parity 測試掃描實際檔案，
      看不到它。
  裁：**成立，且為設計缺陷。**
      **一個描述「某物不存在」的標記，不能寄生於該物。**
      解法採執行層之建議：對應表改為**受版控之資料檔**
      `features/privacy/data/handoff_parity.json`，
      parity 測試改讀該檔並與實際檔案雙向比對 ——
      檔案有而表無 → FAIL；表有而檔無且狀態非
      `chat-direct` → FAIL；`chat-direct` 項豁免檔案存在檢查。
      **列為 close-out，非交付阻塞。**
  §5a：**標記之載體不得是其所描述之對象**；描述缺席者須有獨立載體。

R45-4  `pending` 之到期機制 —— 與 `UPSTREAM-COVERS` 互鎖
  事實：執行層指出 R44-8 之警示機制針對 `unknown`，而
      **`pending` 才是明確宣告了「會發生」的那一個** ——
      若交付完成而無人回頭改標，測試會一直 PASS。
  裁：**成立。** 到期機制不另造，改與 R44-7 之 `UPSTREAM-COVERS`
      互鎖：
        上繳包宣告 `UPSTREAM-COVERS: NN` 而下放包 NN 仍標
        `pending:<該上繳包>` → **FAIL**，訊息
        「上繳包已宣告涵蓋，pending 標記應改為 merged into」。
      故 **R44-7 由 close-out 升為 `pending` 到期機制之必要組件**，
      但**仍不阻塞交付**（本 feature 現有唯一 pending 項即為 18，
      其到期時點即交付後之 §2.2，屆時人工改標亦可）。
  §5a：**「宣告將發生」之狀態必須有到期檢查**，
      否則它與「已發生」在機制上無法區分；
      到期檢查應由該狀態所指向之對象自身提供訊號，
      而非由計時或人工提醒提供。
```

---

## R46 — 交付覆核與 close-out（Pei 簽署 A；其餘分析層自裁，2026-08-13）

```text
[RULING] R46 — 交付覆核與 close-out（Pei 簽署 A；其餘分析層自裁，2026-08-13）

R46-1  交付確認
  裁：交付件已入
      `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/
       ASW-R2/Privacy Mode/FM-WI-FSM-036-A01 …_SWQT_Privacy_20260813.xlsx`
      交付副本重算 SHA256 `ad595ed0cad24375…` 與 ENTRY 002 逐字元相符；
      加驗 zip 成員 48、sheet6 DV classic 3 / x14 2。
      R40-1(d) 之比對為真實比對（非「複製應該不會變」之推定）。
      **Privacy 交付完成。**

R46-2  ENTRY 003 之雜湊行改指交付副本 —— 追認，並立為條文
  事實：原設計之雜湊行指向 repo 內 `output/…`，與 ENTRY 002 同路徑，
      `shasum -c` 會驗兩次同一個檔 ——
      **是一條不可能獨立失敗的檢查行**。
      執行層改指交付副本之絕對路徑，三筆各自獨立；
      客戶樹不可及時由 `--ignore-missing` 靜默略過。
  裁：**追認**，且此為 canon「檢查項須確認其在該階段確實可能失敗；
      不可能失敗者標『未實測』而非 PASS」於台帳上之首次適用。
  §5a 新增：**台帳之每一驗證行須指向獨立標的**；
      兩行指向同一檔案時，其中一行不提供任何額外保證，
      卻會使「N 項全綠」看似 N 項驗證。
      判準：移除該行後，可被偵測之失效集合是否縮小 —— 否即為冗行。

R46-3  A-PV21 —— 採選項 A（改名 ENTRY 001 之檔）
  事實：`…_Privacy_20260813.xlsx` 在 `output/`（ENTRY 001，`ed741d8d…`，
      59,992 bytes）與客戶樹（ENTRY 003，`ad595ed0…`，63,001 bytes）
      basename 相同、內容不同。成因非疏失：R40-1(b) 去 `_regen-v1`
      求命名一致、R40-1(a) 令 `output/` 內維持原名，兩條各自正確，
      合起來撞名。
  裁（Pei 簽署 A）：
      (a) `output/` 內之 ENTRY 001 檔改名為
          `FM-WI-FSM-036-A01 …_SWQT_Privacy_20260813_prepared.xlsx`
      (b) `DELIVERY.sha256` **追加**一行註記路徑變更
          （append，**不改寫** ENTRY 001 既有欄位），
          註記須含改名前後檔名、SHA256（不變）、裁決編號、日期
      (c) 改名後 `shasum -a 256 -c` 須三筆全 OK；
          若 ENTRY 001 該行因路徑變更而 FAIL，
          **停止並回報** —— 不得逕行改寫既有雜湊行
      理由：ENTRY 001 為準備中間檔非交付件，改名成本最低；
      撞名之實害是「有人在 `output/` 找交付件，拿到沒有 TC 的那份」。

R46-4  A-PV21 之真正內容 —— 規則未回頭套用於自身工具
  裁：本 anomaly 之核心非命名衝突，而是：
      **R15-5（同名檔一律以 hash 認定）係為外部素材而立，
        未回頭套用於本 repo 之自有工具** ——
      基準稽核腳本正是 basename 索引。
      A-PV21 之條目須以此為主述，命名衝突為其表徵。
  §5a 新增：**對外部素材所立之規則，須逐條檢查是否同樣適用於
      自有工具與自有產物**；「這條是給上游的」不構成豁免。
      判準：該規則所防範之失效模式，在自有側是否同樣可能發生。
  作業：稽核腳本維持 basename 檢索 + hash 認定之現行設計
      （A-PV04 即以此抓到，設計有效），但須於腳本註解與
      A-PV21 條目內明載該設計之理由，避免日後被「簡化」為純 basename。

R46-5  測試控制組不得取自 repo 現行狀態 —— 立為條文
  事實：`pending` 之負向對照把「下放包 18 是 pending」寫死為 fixture；
      18 一改標 `merged into 17`，對照即失去受測對象。
      **控制組被綁在一個過渡狀態上，正確的轉換反而讓它失敗。**
      執行層改用合成之 `99_synthetic.md`。
  裁：**追認，並立為條文。**
      **測試之控制組不得取自 repo 之現行狀態，須用合成 fixture。**
      理由：取自現行狀態者，測的是「現在剛好長這樣」而非規則；
      且狀態一旦正確演進，測試反而 FAIL ——
      **它會把正確的變更報成錯誤**，這比漏抓更有害
      （漏抓是少一層防護，誤報是主動阻止正確行為）。

R46-6  實作／標準區分之第四次適用 —— 分布值得記錄
  事實：四次分別為 er-modal 誤把 `Interior CAN` 當 modal、
      spec-reference 拒絕多引用、ledger 把裸 `#` 當內容、
      ledger 條目邊界誤切。
  裁：記錄其分布 —— **四次中三次為實作讀得太寬，一次為標準真的變了**。
  §5a：**gate FAIL 之預設歸因應為「實作把規則讀寬了」，而非
      「規則錯了」或「產物錯了」**；三比一之分布支持此預設。
      但預設不等於結論 —— R36-1 之型別區分仍須逐次適用。
      條目邊界之收緊（要求 `— ` 分隔）後，三種違規之陽性對照
      全數仍觸發 —— 收緊未鈍化 gate（R35-1 判準通過）。
```

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
