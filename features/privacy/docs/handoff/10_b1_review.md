# 下放包 10 — B1 pilot review

分析層 → 執行層。2026-08-13。依 canon §1.2 分層取樣覆核，六條 TC 全讀。

**結論：B1 不整批退回。** -001…-004 通過（附兩項小缺陷修正）；
**-005 兩條待 Pei 裁定 ECU 讀法後定案**。

---

## 1. 發現分類（canon §1.2）

### D1 —— defect，結構性，阻塞 -005

**-005 TC2 之 design_method 與其程序不相稱。**

TC2 之 `test_procedure` 為：啟動 trace → 走訪 HU 上每一個可選狀態 →
睡眠喚醒 → 讀取 trace 內所有 `$VolumeSCV$`。
**全程未注入任何無效值。** §12 第一列之條件是
`Invalid input / illegal op`，本程序沒有非法輸入，只有對輸出集合之觀察。

根因不在措辭，在讀法：**在讀法 (i) 之下，負向測試不可構成** ——
HU 是 `$VolumeSCV$` 的**發送端**，測試者無從令其送出無效值。
能注入無效值的位置在 AMP 的輸入側，那正是讀法 (ii)。

連帶後果：§7「列舉之支援項須配至少一負向」在讀法 (i) 下**無法滿足**。
執行層依 §7 拆出 TC2 是正確的推論，但推論之前提（本 ECU 可構成負向）
不成立。這一項執行層未察覺，屬本次覆核之新發現。

### D2 —— defect，輕微，可即修

**單一步驟綁多個動作**（§5.2 A：action + target only）：

- `-003` 步驟 4：`Set the speed controlled volume to a different state,
  put the HU to sleep and trigger the wake-up of the HU on Interior CAN
  again` —— **三個動作**
- `-002` 步驟 4：`Trigger the Interior CAN to sleep and wake it up a
  second time` —— **兩個動作**

拆為獨立步驟，ER 同步 1:1 展開。

### D3 —— defect，輕微，可即修

**-004 之 Pre-Condition 與步驟重複**（§4.5 欄位歸屬）：
PC #3 已宣告 `A CAN interface tool is connected and logging with
timestamps`，步驟 2 又是 `Start the CAN trace`。
擇一 —— 建議 PC 收為 `A CAN interface tool is connected` 並保留步驟 2，
與 -005 兩條之 PC 措辭一致。

### N1 —— note，037 Description 之額外主張（§6.2）：三葉分別處置

執行層之提問成立且重要。分析層逐條查證後，**三葉結論不同**：

**-003 —— 執行層之排除正確，且有獨立佐證。**
SYSAD 於 `SYS-RA-PROF-172` 之 Note 明寫：
「See {VF651} for the AMP present configuration requirements and
**{CFTS019} for speed controlled audio behavior requirements**」。
即「音量隨車速調整之行為」由 **CFTS019** 擁有，屬外部 spec；
依 §8.4.2「Defined only in external spec → out of scope, belongs to that
spec's owner」，排除正確。此佐證請寫入 -003 之 `reasoning`。

**-002 —— 實質已覆蓋，無缺口。**
037 之「不得顯示預設值或錯誤值」在生成之 ER 已被涵蓋：ER 3 / ER 5 為
「displayed in the state recorded in step 1」，若顯示預設值即 fail。
「無需使用者互動」亦已涵蓋 —— 程序中喚醒後未有任何使用者操作。
毋須改寫，於 `reasoning` 加一句說明該兩點如何被現有 ER 涵蓋即可。

**-001 —— 確為 037 獨有之主張，需 Pei 裁定。**
分析層對 CFTS022 全文掃描：涉及 `SLEEP MODE` 之 artifact 僅三條 ——
`4914954`（SCCM 版）、`4914955`（HU 版）、`4915104`（Lock Out State
初始化），**無任何一條述及「轉換階段中按鍵輸入不得被處理」**。
該主張只存在於 037 之 Description。見 §2 待裁 P-6。

### N2 —— note，-001 之 P0 維持

執行層自陳「本批唯一 P0 出自我的判斷」——揭露正確。
分析層裁定**維持 P0**：§10.2 之 P0 涵蓋 `boot/recovery`，而
「每次退出睡眠後實體按鍵全數失效」正是 recovery 路徑之全失，
非顯示層缺陷。判準是失效面而非批次配額，執行層之推理與 framework
Part I 一致。
（執行層引「AMFM 同類用 P1」作為反向參考 —— 該比較**無法查證**，
AMFM 之 `inputs/` 已不存在；不採為依據，亦不記入。）

### N3 —— note，lint 缺席（§6.1）

執行層自陳「那份機械檢查不是 lint，權威來源是我對 profile 的閱讀」——
**此揭露本身是本包最有價值的一項**。分析層裁定：

- **B1 不因此阻塞** —— 六條 TC 已由分析層逐條人工覆核
- **B2 之前必須建立 `features/privacy/scripts/lint_tcs.py`**，
  且不得直接沿用 AMFM 版（其 gate 讀 `data/stla_to_cfts.json`，
  Privacy 之對映結構不同且已知不可算術推定）
- gate 至少須涵蓋 profile §3.3 / §3.5 / §3.8 / §3.9 與 §11 之格式規則

### N4 —— note，CAN trace 工具能力（§6.5）

`-004` / `-005` 兩條之步驟假定實驗室具備 CAN interface 記錄能力。
分析層裁定：**非需求假定，不登 assumption**（執行層判斷正確），
但**登 anomaly A-PV16**（測試可執行性），狀態 PENDING，
待與測試團隊確認。不阻塞任何批次。

### N5 —— note，Pre-Condition 措辭未回溯原文（§6.4）

承認為未辦項，維持在 P2 清單。B1 六條之 PC 措辭經分析層覆核，
語意與條文相符，**不阻塞**；但 P6 寫回前須完成回溯。

---

## 2. 待 Pei 裁定

```text
[PENDING] P-6  -005 之 ECU 讀法（D1 之根因）

事實：CFTS022-4915170 之 outcome 主詞為 AMP
      （"considered invalid by the AMP and no action shall be taken"），
      本交付件 ECU 為 LTM（HU）。HU 為 $VolumeSCV$ 之發送端。

選項 A（建議）：維持讀法 (i)，並修正 TC2
  (a) TC2 之 design_method 由 `負向測試 (Negative / Invalid)` 改為
      `功能測試 (Functional based ; no specific technique)`
      —— 程序未注入非法輸入，只觀察輸出集合，不合 §12 第一列
  (b) TC2 之 tc_title 與 test_item 改寫為輸出集合之封閉性
      （HU 不送出集合外之值），不再以「無效值處置」為名
  (c) 真正之負向（向 AMP 注入集合外之值，驗 AMP 不動作）
      **明列為 out of scope，歸 AMP ECU 之驗證**，於 -005 `reasoning`
      載明，並列入 RD-1
  (d) §7 之負向配對要求，於本葉**以範圍歸屬解除**而非以 TC 滿足；
      此為 §7 與 §8.4.2 衝突時之處置，記為先例

選項 B：改採讀法 (ii)，-005 兩條全部改寫，並確認該行為是否
        本就不應分配給本 037（若是，則屬 037 分配問題，需 RD-1）

選項 C：其他 ____

裁：[ ] A（建議）  [ ] B  [ ] C：____

[PENDING] P-7  -001 之 037 獨有主張

事實：037 Description 主張「轉換階段中按鍵輸入不得被處理，只有在達到
      active 狀態後才處理」；CFTS022 全文無此語（涉 SLEEP MODE 之
      artifact 僅 4914954 / 4914955 / 4915104 三條，經全文掃描確認）。

分析層評估：SWE.6 驗的是 SWE.1 軟體需求（037 葉子），CFTS022 是其
      上游系統需求；037 之細化本身合法。但該句若為分析者之闡釋而非
      需求，據以生成 TC 會產生對合規實作之誤判（§7 FF）。
      不對稱錯誤代價指向「補測」（擴範圍）而非「不測」（縮範圍），
      但補測之對象必須先確認是需求。

選項 A（建議）：
  (a) -001 現行 TC **不改**（其驗證目標與 CFTS022 條文一致）
  (b) 於 `reasoning` 明列該 037 主張未被本 TC 覆蓋及其理由
  (c) 登 anomaly A-PV17：037 Description 含 CFTS022 未載之行為主張
  (d) 列入 RD-1：請上游確認該句為需求或闡釋；若為需求，
      請指出其 CFTS022 出處或補充條文

選項 B：逕行補測（於 -001 增加轉換階段之驗證步驟與 ER）
選項 C：其他 ____

裁：[ ] A（建議）  [ ] B  [ ] C：____
```

---

## 3. 執行層作業（P-6 / P-7 裁定前可辦者）

1. 貼入本包裁決至 `RULINGS.md`（編號由執行層暫配，依 R31-1）
2. **修 D2** —— `-002` 步驟 4、`-003` 步驟 4 拆為獨立步驟，ER 1:1 同步
3. **修 D3** —— `-004` PC #3 收為 `A CAN interface tool is connected`
4. **-003 `reasoning` 加入 N1 之 CFTS019 佐證**（SYSAD 之
   SYS-RA-PROF-172 Note），使排除理由由「條文未及」升為「外部 spec 擁有」
5. **-002 `reasoning` 加一句**，說明 037 之兩項主張如何被現有 ER 涵蓋
6. 登 **A-PV16**（CAN trace 工具能力，PENDING，不阻塞）
7. **不動 -005 兩條**，不動 -001 之 P0

**不做**：不改 -005、不改 -001 之 priority、不建 lint（另包）、
不寫回 workbook、不執行任何 git 操作。

---

## 4. 停手條件

1. D2 拆步驟後，任一 TC 之步驟與 ER 條數不再 1:1 → 停止該葉之修改，
   續行其餘，回報
2. 第 4 項於 SYSAD 內查無 `{CFTS019}` 之 Note → **停止該項**，
   續行其餘，回報實際措辭
   （分析層引自先前對 SYSAD 之掃描，執行層須獨立複驗後方可寫入）
3. 修改後台帳任一條指令 FAILED → 停止全部，回報

---

## 5. 覆核意見（供執行層參考，非作業）

- §2 之「遵守自證」逐項附機械檢查（`splash` / `VF169` / 秒數
  皆 0 命中）—— 這是把「我照辦了」轉為可驗證陳述，體例正確
- §4 主動聲明「這不是 lint」並列出未涵蓋之五類 —— 若未聲明，
  本包極可能被當成已 lint 通過
- §6.2 為本輪最重要之發現，且執行層正確地停在「不自行裁定」
- §1.3 之 priority 表以「失敗時偵測不到什麼」為欄位標題，
  而非以級別為欄位標題 —— 這使判準可被檢查，非僅可被引用

---

## 6. 本包產生之新條文清單（自檢表）

- [x] D1 -005 TC2 設計方法與程序不相稱（結構性）—— §1
- [x] D2 單一步驟綁多動作（-002 / -003）—— §1
- [x] D3 -004 PC 與步驟重複 —— §1
- [x] N1 037 額外主張三葉分別處置（含 CFTS019 佐證）—— §1
- [x] N2 -001 之 P0 維持 —— §1
- [x] N3 lint 為 B2 之阻塞條件 —— §1
- [x] N4 A-PV16 CAN trace 工具能力 —— §1
- [x] N5 PC 措辭回溯維持 P2 —— §1
- [ ] P-6 -005 之 ECU 讀法 —— §2，**未簽署**
- [ ] P-7 -001 之 037 獨有主張 —— §2，**未簽署**
- [x] 停手條件三項（已依 R17-1 明列標的與續行標的）—— §4

<!-- HANDOFF-LINK: 10 -> no-upstream-required -->
