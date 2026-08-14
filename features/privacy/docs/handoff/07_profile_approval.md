# 下放包 07 — profile 核可（附三項修訂）、A-PV14 結論、B1 前置條件

分析層 → 執行層。2026-08-13。承接上繳包 03 / 04。

---

## 1. 裁決條文

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

---

## 2. profile 三項修訂（核可之附帶條件）

以下三項寫入 profile 後，R28-1 之核可方為定案。

```text
[修訂 1] §3.3 —— -005 之 design method 須明列其取代之首match順序

現行條文：「-005（valid vs invalid $VolumeSCV$ values）is Equivalence
Partitioning on both sides of the partition, not Functional.」

問題：canon §12 為 **first-match** 表，第一列即
「Invalid input / illegal op → Negative / Invalid」。-005 之負向側
（invalid 值 → AMP 不動作）會先命中該列。現行條文只排除了
`Functional`，未處理 `Negative / Invalid` 這個實際的競爭者，
review 時必生爭議。

修訂為：
  「-005 以 Equivalence Partitioning 為準，**明確取代 §12 之
   first-match 順序**：該葉之驗證目標是 valid / invalid 兩個等價類
   的劃分本身，而非單一非法輸入之處置，故不適用第一列
   `Negative / Invalid`。若 -005 因 §8.2.2 拆為多個 TC，
   **每個 TC 各自適用 §12**：只驗 invalid 側處置者仍為
   `Negative / Invalid`，驗劃分者為 `Equivalence Partitioning`。」

[修訂 2] §0 / §3 —— 欄 S（Functional Safety）填值政策未定義

問題：範本 rev C 之欄 S 為 `Functional Safety`（範本樣本列 S10 = `NA`，
已依 R23-4 清除）。profile §1 已裁「SYS2/SYSRA 不進 trace chain」，
但**未說明欄 S 生成時填什麼**。inputs/ 內確有一份 SYSRA
（`CFTS022_Privacy_mode-FM-WI-FSM-035-A02 … SYSRA.xlsx`），
不定義填值政策，B1 生成時必然出現逐列臆測。

修訂為（**擇一，執行層不得自裁；本包列為待裁 P-4**）：
  (a) `UNRULED_BLANK` —— 同欄 Q 之處置（§3.7），留白並於 dry-run
      summary 列為 blank-by-decision
  (b) 一律填 `NA` —— 依範本樣本列之原廠形態
  (c) 依 SYSRA 逐葉判定 —— 需先確認該 SYSRA 是否涵蓋本 037 之
      10 片葉子；未確認前不得採用

[修訂 3] §0 —— 車型欄（T–Z）填值政策未定義

問題：rev C 之欄位位移使車型欄落在 T–Z 區（AMFM rev 前為 S–Y，
標頭為 `HDCC27 Atl-Hi` / `DT27 Atl-Hi` / `VF(ProMaster)637 Atl-Mi` 等）。
profile 未定義 Privacy 之車型適用範圍。
**此項與 A-PV14 同源**：本專案為 HDCC28 平台，而 `inputs/` 曾混入
DT28 平台之 VF —— 車型欄若填錯，錯誤方向與 A-PV14 相同。
Projection 之 DR#14（Atlantis Mid 車型範圍）為同類先例。

修訂為（**待裁 P-5**）：先由執行層**實測**範本 rev C 之 T–Z 實際標頭
文字並回報，再據以裁定填值政策。**在裁定前 B1 不得填寫任何車型欄**。
```

---

## 3. 需 Pei 動手（權限攔截）

執行層之覆寫動作被權限分類器攔下兩次（`shutil.copyfile`、`cp`），
已停止嘗試、未繞過 —— **處置正確**。

請 Pei 執行：

```bash
cd /Users/peihe/Work_Projects/TC_Generator
cp "/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/VF/VF_Split document/HDCC28_Split/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx" \
   "features/privacy/inputs/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx"
shasum -a 256 "features/privacy/inputs/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx"
```

預期 SHA256 為 `e20ba7a4f8f7…`（不符即停手回報）。

換檔完成後之三處連動（執行層辦）：

1. `BASELINE.sha256` 該行改為 `e20ba7a4f8f7…`，檔頭記 R24-2(2) / R28-2
2. `ANOMALIES.md` A-PV14 → **RESOLVED**，記入 hunk 8 之 revision-note 佐證
3. framework Part VI 注 3、profile §5 marker 表、profile §6 之
   「不得引用 V6_R2」一律解除；§5 之 `[A-PV14]` marker **整條移除**
   （其存在理由已消滅）

**換檔完成前，V6_R2 仍不得列為 `specification_reference`。**

---

## 4. B1 前置條件（三項，全部完成方可下放 B1 生成包）

```text
[B1-GATE-1]  PROF → artifact 對映之獨立重驗 —— 全 10 筆
  執行層指出：framework Part VI 之 8 筆對映係分析層實測結果照抄，
  未經獨立重驗；profile §1 只把 -001/-002 列為引用前硬性條件。
  **分析層裁定：此項不得留到 P2。**
  理由：B1 之五片葉子（-001…-005）全部需要 specification_reference，
  其中 -001/-002 未驗、-003/-004/-005 為分析層單一來源之主張 ——
  **B1 的五筆引用全部落在未獨立驗證的對映上**。
  作業：獨立自 CFTS022 與 037 兩側重算全 10 筆對映（不得引用
  framework Part VI 之表），逐筆比對後回報。不符即停手。

[B1-GATE-2]  ENTRY 001 工作簿之 Excel 實開確認（Tier 3，僅 Pei）
  執行層指出：B1 生成將往一份未經 Excel 開啟驗證的工作簿寫入 ——
  順序上不合理。**採納。**
  請 Pei 開啟 `features/privacy/output/` 之 ENTRY 001 工作簿，確認：
    1. 無「檔案已損毀，Excel 已修復」提示
    2. R 欄設計方法下拉可用，選項為 下拉選單 之 9 條
    3. D5 範圍 Scope 顯示 `SWE1_CFTS_022-Privacy_Features`
    4. 第 10–11 列五格已空，B 欄序號未顯示殘值
  四點全過後，DELIVERY.sha256 之 ENTRY 001 加註「Excel 開啟確認：
  Pei, 2026-08-13, 四點全過」。

[B1-GATE-3]  §2 修訂 2 / 3 之裁定（欄 S、車型欄 T–Z）
  未裁定前 B1 不得填寫該兩區欄位。
```

---

## 5. 待 Pei 裁定

```text
[PENDING] P-4  欄 S（Functional Safety）填值政策 —— §2 修訂 2 之三案
  裁：[ ] (a) UNRULED_BLANK  [ ] (b) 一律 NA  [ ] (c) 依 SYSRA 逐葉判定
  分析層建議 **(a)**：與欄 Q 同型（rev C 新增/未定政策之欄），
  且 (b) 之 `NA` 在本欄語意為「無功能安全需求」，是一項**斷言**
  而非留白 —— 在未確認 SYSRA 涵蓋範圍前作此斷言即 §8.4 型臆測。
  (c) 需先確認 SYSRA 涵蓋範圍，成本高於其收益（10 片葉子）。

[PENDING] P-5  車型欄（T–Z）填值政策
  裁：待執行層回報 rev C 之 T–Z 實際標頭後另裁。
```

---

## 6. 執行層作業（依序）

1. 貼入 §1（R28）至 `features/privacy/RULINGS.md`
2. 依 §2 修訂 1 改寫 profile §3.3；修訂 2/3 於 profile 內標為
   **待裁（P-4 / P-5）**，不自行選案
3. 移除 profile 檔頭 DRAFT，改記「Approved 2026-08-13, R28-1
   （附 §2 三項修訂；修訂 2/3 待裁）」
4. 依 R28-3 補 framework 首句之 Part V
5. 實測範本 rev C 之 T–Z 欄實際標頭文字並回報（P-5 之前置）
6. 執行 **B1-GATE-1**（全 10 筆對映獨立重驗）
7. 換檔完成後（Pei 執行 §3）辦理 §3 之三處連動

**不做**：不執行 B1 生成、不填欄 S 與車型欄、不自選 P-4 / P-5、
不繞過權限攔截、不執行任何 git 操作。

---

## 7. 停手條件

1. `RULINGS.md` R28 編號已占用 → 停止貼入，續行第 2–6 項
2. **B1-GATE-1 任一筆對映與 framework Part VI 不符** → 停止全部後續，
   續行回報。理由：對映錯誤會使全部 specification_reference 失效，
   且 framework Part VI 已 append，須連同修訂
3. §3 換檔後之 SHA256 不等於 `e20ba7a4f8f7…` → 停止三處連動，續行回報
4. 第 5 項實測發現 T–Z 並非車型欄（標頭語意不符）→ 停止該項，
   續行其餘，回報實際標頭全文

---

## 8. 本包產生之新條文清單（自檢表）

- [x] R28-1 profile 核可 + 繼承粒度須逐條聲明（§5a）—— §1
- [x] R28-2 A-PV14 換檔條件成立 + 方向性論證 + 限縮聲明之處置（§5a）—— §1
- [x] R28-3 授權外之事實性補正得逕行（§5a）—— §1
- [x] profile 修訂 1（-005 design method 取代 first-match）—— §2，區塊形式
- [x] B1-GATE-1 / 2 / 3 三項前置條件 —— §4，區塊形式
- [ ] P-4 欄 S 填值政策 —— §5，**未簽署**
- [ ] P-5 車型欄填值政策 —— §5，**未簽署**
- [x] 停手條件四項（已依 R17-1 明列標的與續行標的）—— §7

<!-- HANDOFF-LINK: 07 -> upstream:07 -->
