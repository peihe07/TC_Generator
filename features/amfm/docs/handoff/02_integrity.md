# 下放包 02 — R15 覆核追認 + R16 交付件結構完整性（凍結令）

分析層 → 執行層。2026-08-13。Pei 於本日回覆「照建議」，R15 與 R16 全數簽署。

**落點說明**：R16 為跨 feature 之凍結令，但證據與首個補救標的皆在 AMFM，
故置於此。執行層須依 §4 將對應條目分別登記至 Home / SXM / Projection 之
`ANOMALIES.md`，不另開 handoff。

**本包取代**：2026-08-13 聊天中所述之 R15 條文（當時 MCP 寫入逾時未落檔）。
以本檔為準。

---

## 1. R15 —— AMFM close-out 覆核（分析層自裁，追認上繳包 01）

```text
[RULING] R15 — AMFM close-out 覆核（2026-08-13）

R15-1  §2.6 落點衝突 —— 執行層判斷正確，追認
  歸因：分析層撰寫缺陷。下放包 01 標題之「item 3 增補」係議題歸屬，
        被誤寫為插入位置；區塊自帶之 5. 才是能產生自洽文件之意圖。
  裁：追認置於 item 5，內文一字未改。附帶：新段縮排三格、item 1–4
      二格，統一為二格（純排版）。
  §5a：議題歸屬與插入位置是兩件事，下放包指定落點時必須分開陳述。

R15-2  已裁而結果為延後之狀態表示 —— 追認，並立為通則
  裁：Open PENDING 之語意為「待裁」，不收容「已裁而結果為延後」。
      已裁但需等外部條件者，一律標
      DEFERRED — <等待對象>（<裁決編號>），並移出 Open PENDING。
      適用全 feature。

R15-3  重測方法 —— 未逾界，但須標明證明範圍
  裁：import 純函式唯讀重算未逾「不重跑」之界；該禁令標的為會改動
      output/ 之寫回執行。無需改以獨立實作重寫。
  量測條件須明載：以相同雜湊定義重算，可證「產出未自產生時漂移」，
      不可證「該雜湊定義正確」。
  §5a：重測之獨立性有層級之分，陳述時必須指明是哪一種。

R15-4  legacy hash 之截斷表示
  裁：v1 已封存，不改 annotation。但 PLAYBOOK §6 P7 段須明載
      30d9e4c0719a2929 為前綴截斷、全長 30d9e4c0719a2929 2ff50123…。
      後續 feature 之 tag annotation 一律載全長。

R15-5  A-AM17（4874049 / 4874050 同名異容）—— 撤回裁決請求
  裁：維持 anomaly 登記即可，不另立 RD-1 條目、不重開 #2b。
      下次送 RD-1 時順帶提出。
  併入 §5a：**同名檔一律以 hash 認定**。分析層先前對本例與 V2_R2
      所留之「可能只是重存」餘地，已被 hash 證否（V2_R2 七路徑五內容），
      該類措辭不得再用。
```

---

## 2. R16 —— 交付件結構完整性（Pei 簽署，2026-08-13）

```text
[RULING] R16 — xlsx 寫回破壞交付件結構（凍結令）

證據（分析層 zip 層實測，AMFM）：
  客戶原件  136,004 B / 59 zip members
  已交付檔  171,631 B / 48 zip members   （tag fw036-amfm-regen-v1）
  x14 dataValidation（sheet6）: 6 → 0

  LOST（21）
    xl/diagrams/{colors1,data1,drawing1,layout1,quickStyle1}.xml
    xl/drawings/drawing7.xml + xl/drawings/_rels/drawing7.xml.rels
    xl/printerSettings/printerSettings1..7.bin
    xl/sharedStrings.xml, xl/calcChain.xml
    xl/comments1.xml, xl/drawings/vmlDrawing1.vml
    xl/media/image2.jpeg
    xl/worksheets/_rels/sheet8.xml.rels, sheet9.xml.rels
  ADDED（10）
    xl/comments/comment1.xml, xl/drawings/commentsDrawing1.vml
    xl/media/image2.png（原 jpeg 重新編碼）, xl/media/image3..9.jpeg

  對照：Privacy 空白範本探針（features/privacy/scripts/
  xlsx_roundtrip_probe.py）測得 openpyxl load/save LOSSY、
  zip 層外科手術 LOSSLESS（48 成員零增零減）。AMFM 之實測另多失
  整組 xl/diagrams/（SmartArt 物件）。

  Projection 對照組：NR1L_GEN1(HDCC)_Ver_20260813.xlsx
  inputs/ 與 output/ 皆 574,700 B / 30 members、x14 DV 0 → 0，
  無差異（該工作簿本無 x14 DV）。Home / SXM 未量。

R16-1  AMFM v1 停止送出
  裁：controlled-document submission 暫停（PLAYBOOK §6 記載尚未執行，
      攔截有效）。以修正後之 writer 重產 v2 再交。
      tag fw036-amfm-regen-v1 保留為歷史，不刪不改；v2 另立新 tag。
      RD-1 送出不受此凍結影響，時點由 Pei 決定。

R16-2  全 repo 寫回凍結
  裁：在 writer 改為 zip 層外科手術並通過探針驗證前，
      **所有 feature 之 --write 一律暫停**。
      SXM 尚未寫回，攔得住；Home 已 tag，屬 R16-3 回溯範圍。
      解除條件：§3.1 完成且 §3.2 之新 invariant 上線。

R16-3  回溯檢測
  裁：Home 與 SXM 之已交付件比照 AMFM 做 zip 層比對，
      以 xlsx_roundtrip_probe.py 執行，不另寫實作。
      每件回報：zip 成員增減清單、x14 DV 前後計數、
      傳統 DV 前後計數、位元組數。

R16-4  canon 升格
  裁：本缺陷屬 FM-WI-FSM-036-A01 範本家族之性質，非單一 feature 之
      anomaly。升為 canon 條文，寫入 FEATURE_ONBOARDING（P7 交付段），
      並於各 feature profile 交叉引用。

R16-5  §5a 新增條目
  裁：**lint green 與內容 hash 相符，證明不了交付件結構完整。**
      前者量列內容，後者量 zip 結構，兩者正交。
      R14-C1 之 P7 追認即在此盲區內做出 —— 當時所驗七項數值全對，
      而交付件已缺 21 個 zip 成員。追認本身不撤回（列內容確實正確），
      但其結論之涵蓋範圍須加註本限制。
```

---

## 3. 執行層作業（依序，不得跳號）

### 3.1 修正 writer（凍結解除之前提）

- `backend/writer.py`（或實際寫回路徑）改為 zip 層外科手術：
  只替換目標 sheet 之 XML，其餘 zip 成員 **byte-for-byte 複製**
- 以 `features/privacy/scripts/xlsx_roundtrip_probe.py` 驗證：
  對 AMFM 客戶原件與 FW036 空白範本各跑一次，皆須 LOSSLESS
- **不得**沿用 openpyxl 存檔路徑產出任何交付件

### 3.2 新增寫回 invariant（ABORT 級）

寫回後、輸出前，強制比對輸出檔與輸入檔之 zip 成員集合：

- 成員集合不相等 → **ABORT**（不 warn）
- 各 sheet 之 `<dataValidation ` 與 `x14:dataValidation` 計數不相等 → **ABORT**
- 允許差異者僅限被寫入之 sheet XML 本身

此 invariant 之違反屬 canon §0 第三項，升 Tier 2，不得以放寬 invariant 解決。

### 3.3 AMFM v2 重產

- 前提：3.1 與 3.2 均完成
- 輸入：`features/amfm/inputs/` 之客戶原件（未改）
- 內容：與 v1 完全相同之 158 legacy + 143 regen = 301 列，
  **不重跑生成、不改任何 TC 內容**；本次只換寫回方法
- 產出後回報：zip 成員集合與客戶原件比對結果、x14 DV 計數、
  SHA256、legacy hash（全長）、列數、lint
- **不打 tag、不 commit** —— 全部 git 操作屬 Pei

### 3.4 回溯檢測 Home / SXM

以探針對兩件之「客戶原件 vs 已交付件」比對，格式同 R16-3。
Home 若受損，其 tag `fw036-home-regen-v2` 同 AMFM 處置（保留歷史、
另產 v3），但**是否重產由 Pei 裁**，執行層只回報不動作。
SXM 尚未寫回，僅需確認其範本是否含 x14 DV 並登記。

### 3.5 登記

- `features/amfm/ANOMALIES.md`：新條 A-AM18（v1 結構缺損，含 §2 全部證據）
- `features/home/ANOMALIES.md`、`features/sxm/ANOMALIES.md`：各登一條，
  引用 R16，狀態待 §3.4 結果
- `features/projection/ANOMALIES.md`：登記對照組結果（無差異），
  註明該工作簿本無 x14 DV，不代表 writer 安全
- `features/privacy/ANOMALIES.md`：A-PV09 升級並交叉引用 R16
- 各 feature `PLAYBOOK.md` 加註凍結狀態

### 3.6 canon 條文草案

依 R16-4 撰寫 `FEATURE_ONBOARDING` P7 交付段之增補草案，
**寫成草案供 Pei 簽，不直接改 canon**。

---

## 4. 停手條件（本包特化）

1. `RULINGS.md` 之 R15 或 R16 編號已被占用 → 停手回報，不得改號
2. 3.1 之探針驗證未達 LOSSLESS → 停手回報，**不得降低驗證標準**
3. 3.3 之 v2 產出在任一回報項與 v1 不符（列數、legacy hash、
   TC 內容）→ 停手回報，不得自行調和
4. 3.4 發現 Home 受損 → 回報後停手，重產與否由 Pei 裁

---

## 5. 上繳包要求

寫入 `features/amfm/docs/upstream/02_integrity.md`，須含：

1. §3.1–§3.6 逐項完成狀態
2. 探針對客戶原件與空白範本之兩次驗證輸出（原文）
3. AMFM v2 之全部回報項，與 v1 逐項並列比對
4. Home / SXM 回溯檢測之完整輸出
5. 為 Pei 準備之 commit message（英文，conventional commits），**不執行**
6. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

---

## 6. 本包產生之新條文清單（自檢表）

- [x] R15-1 §2.6 落點追認 —— §1，區塊形式
- [x] R15-2 DEFERRED 狀態通則 —— §1，區塊形式
- [x] R15-3 重測獨立性層級 —— §1，區塊形式
- [x] R15-4 legacy hash 截斷記載 —— §1，區塊形式
- [x] R15-5 A-AM17 撤回裁決請求 + 同名檔以 hash 認定 —— §1，區塊形式
- [x] R16-1 AMFM v1 停止送出，重產 v2 —— §2，區塊形式
- [x] R16-2 全 repo 寫回凍結 —— §2，區塊形式
- [x] R16-3 Home / SXM 回溯檢測 —— §2，區塊形式
- [x] R16-4 canon 升格 —— §2，區塊形式
- [x] R16-5 §5a：lint green + hash ≠ 結構完整 —— §2，區塊形式
- [x] 新增 anomaly A-AM18 —— §3.5
- [x] 新增寫回 invariant（zip 成員集合 / DV 計數，ABORT 級）—— §3.2
- [x] 停手條件四項 —— §4

以上均以可直接貼入之區塊或表格形式出現，非夾敘於段落中。
