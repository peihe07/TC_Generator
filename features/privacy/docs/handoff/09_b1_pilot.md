# 下放包 09 — B1 pilot 生成（leaves -001…-005）

分析層 → 執行層。2026-08-13。三道 gate 全數通過，**B1 生成授權**。

---

## 1. 裁決條文

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

---

## 2. B1 生成規格

### 2.1 批次組成

| leaf | Test Set | CFTS022 artifact | 條文（節錄） |
|---|---|---|---|
| -001 | Input Monitoring | **4914955** | When the A&T System exits 'SLEEP MODE', the HU and external DVD player shall monitor the button pressed status |
| -002 | Personalization Display | **4915158** | Each time the Interior CAN wakes up, the HU shall recall the last known state for the configured set of personalization features to be displayed |
| -003 | Speed-Controlled Volume | **4915168** | When the HU wakes up on Interior CAN, the HU shall recall the state of the speed controlled volume |
| -004 | Speed-Controlled Volume | **4915169** | When the HU wakes up, the HU shall send the status of the speed controlled volume in the `$VolumeSCV$` signal within `<Tsend>` |
| -005 | Speed-Controlled Volume | **4915170** | Valid signals for `$VolumeSCV$` are shown below. All other signals shall be considered invalid by the AMP and no action shall be taken |

`specification_reference` 形式 `CFTS022-{artifact_id}`（profile §3.5）。

### 2.2 逐葉範圍指示（§8.2.1 —— 分析層已查相鄰條文，逐葉列出應排除者）

**-001（4914955）**
- **排除 4914956** —— 「按鍵連續按壓超過 120 秒 → HU 設 stuck button DTC
  並送 not pressed 值」。這是**另一條 SFR**，不是 4914955 的細節。
  -001 的驗證目標僅止於「退出 SLEEP MODE 後，按鍵狀態監測**恢復**」。
  120 秒門檻、DTC、not pressed 值一律不得進入本 TC。
- **ECU 範圍**：條文寫 `the HU and external DVD player`，而 DVD 為另一
  ECU（tag `ETM, RRM, ICS, DVD, LTM`）。本交付件之 ECU 為 **LTM**，
  TC 只驗 HU 側；external DVD player 之行為屬該 ECU 自身之驗證
  （§8.4.2）。此點寫入 `reasoning`。

**-002（4915158）**
- **排除 4915159** —— 「features 須在 splash screen 完成時間內備妥顯示」，
  且其 Note 指向 `{VF169}`。那是**時序需求**，與「recall 上次狀態」
  是兩件事。
  ⚠️ 此條正是分析層先前誤填的 id（R30-1），**相鄰且語意相近，是本批
  最容易被吸收的一條**。TC 不得出現任何 splash screen 或時間門檻。
- **4915157**（`Artifact Type: Description`，「HU 決定車上存在哪些
  features」）為**描述型**非 SFR，僅供背景，不得列為
  `specification_reference`。
- 「configured set of personalization features」之**具體清單未在本條
  給出** → §8.4.1，不得自行列舉功能項；以 spec 措辭表述。

**-003（4915168）** 與 **-004（4915169）** —— 觸發條件不同，不得合併
- -003 觸發為 `wakes up on Interior CAN`，-004 為 `wakes up`（未限定
  Interior CAN）。**照條文原樣寫，不得互相補齊**。
- -004 之 `<Tsend>` **未定義具體值** → §8.4.1，保留 `<Tsend>` 原樣或
  「spec 定義之值」，**嚴禁填入任何秒數**。
- 兩者同為 SCV Set，`distinguishing_axis` 須指出：recall（內部狀態
  復原）vs send（對外訊號傳送）。

**-005（4915170）** —— 自足，**不 BLOCKED**
- 有效值表**存在於條文內**（分析層實測）：
  `$VolumeSCV$ = [Off]` / `[level 1]` / `[level 2]` / `[level 3]`
  —— 依 framework Part I 之 blocked-parent proportion test，本條自足，
  正常生成。
- **方括號保留**：`[Off]` / `[level 1]` 等為 source-quoted signal value，
  適用 profile §3.4 之 §11 例外；作者自撰的 UI label 仍用 `"..."`。
- **設計方法**：依 profile §3.3 修訂 1 —— 驗劃分本身者為
  `等價劃分 (Equivalence Partitioning, EP)`；若拆為多 TC，
  **只驗 invalid 側處置者仍適用 §12 第一列** `負向測試 (Negative /
  Invalid)`。逐 TC 各自判定，不得全批一律。
- **⚠️ ECU 範圍需於 pilot review 裁定，本輪先產出並在 `reasoning`
  明列問題**：條文的 outcome 主詞是 **AMP**（"considered invalid by
  the AMP and no action shall be taken"），而本交付件 ECU 為 LTM。
  可觀察面有兩種讀法 ——
    (i) HU 側：HU 只送出有效值集合內之值（本 ECU 可觀察）
    (ii) AMP 側：AMP 收到無效值不動作（另一 ECU 之行為）
  **執行層依 (i) 產出**（本 ECU 可觀察者優先），並在 `reasoning`
  完整陳述 (ii) 及其歸屬問題，**不自行結論**。pilot review 裁定。

### 2.3 欄位政策（本批適用，profile 已核可）

- Test Group `Privacy`（G 欄）、Test Set 依 §2.1（H 欄）
- 欄 S Functional Safety = **`NA`**（profile §3.8 / R30-3）
- 車型欄 T–Z = **全部留白**（profile §3.9 / R30-4）
- 欄 Q Estimated Test Time = **留白**（UNRULED_BLANK, profile §3.7）
- Author = `PeiPYHsu`；tc_id `NR1L-Privacy-{NNN}` 自 001
- Remarks = 空字串（本批預期無 BLOCKED、無 marker）
- **本 feature 目前無 marker**（profile §5）—— 若本批產生新的
  assumption 需求，**停手回報**，不自行創設 marker

### 2.4 預期規模（參考，不是配額）

五片葉子預估 **5–7 TC**：-001…-004 各 1；-005 因 §7「列舉之支援項須配
至少一負向」預期 ≥2。**不得為湊數而拆，也不得為省事而併** —— 實際數
由 §8.3 / §8.2.2 判準決定，於 digest 說明。

---

## 3. 上繳包要求（P5 pilot digest）

寫入 `features/privacy/docs/upstream/09_b1_pilot.md`：

1. 生成之 JSON 全文（5 leaves）
2. **一頁 digest**：TC 數與分布、每葉之切分理由與所引 §-條號、
   design_method 分布、priority 分布、`distinguishing_axis` 清單
3. **§2.2 逐葉範圍指示之遵守自證** —— 逐項說明「排除了什麼、
   在哪裡說明的」。特別是 -002 對 4915159 之排除
4. -005 之 ECU 範圍兩種讀法之陳述（依 §2.2 不自行結論）
5. lint 結果
6. 台帳兩條指令之輸出
7. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略

**本批不寫回 workbook。** 生成與 review 通過後另包下放 P6 / P7。

---

## 4. 停手條件

1. 任一葉之 `specification_reference` 需要 §2.1 表以外之 artifact id →
   停止該葉之生成，續行其餘四葉，回報所需 id 與理由
   （id 一律**查得**，不得由任何規律推算 —— profile §3.5 / R30-1）
2. 本批產生任何 assumption 或 BLOCKED 需求 → 停止該葉，續行其餘，回報
3. -005 之 ECU 範圍若在生成中發現 (i) 讀法無法產生可觀察之 Final Step →
   停止該葉，續行其餘，回報
4. 台帳任一條指令 FAILED → **停止全部生成**，續行回報

---

## 5. 本包產生之新條文清單（自檢表）

- [x] R31-1 chat 直下裁決之編號得由執行層暫配 —— §1，區塊形式
- [x] R31-2 證據型別須逐項標明（§5a）—— §1，區塊形式
- [x] R31-3 台帳首次實測有效 —— §1，區塊形式
- [x] B1 逐葉範圍指示（含五組應排除之相鄰條文）—— §2.2
- [x] -005 之 ECU 範圍兩讀法，本輪不結論 —— §2.2
- [x] 停手條件四項（已依 R17-1 明列標的與續行標的）—— §4

<!-- HANDOFF-LINK: 09 -> upstream:09 -->
