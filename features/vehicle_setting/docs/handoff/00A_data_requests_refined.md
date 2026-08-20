# 00A 下放包補篇 — DATA_REQUESTS 之收斂（**取代 00 包 §6**）

分析層寫入，2026-08-20。與 `00_intake_and_rulings.md` 同一往返（NN = 00）。
**00 包 §6 之第 4／5／6 項作廢**，以本篇為準；00 包其餘各節不受影響。

作廢理由：原三項為**類別式請求**（「值域來源」「HMI L&F」「Comfort 037」），
未指出缺的是哪一份、缺多少、缺了誰不能做。經逐 leaf 實測後，三項中有一項
幾乎不必請求、一項換了對象、一項根本不是檔案問題。

---

## 1. 量測條件（本篇全部數字）

- **來源**：2026-08-20 聊天附件之沙箱副本 + repo 內
  `features/comfort/inputs/FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx`
  （後者為 repo 實體檔，經 `copy_file_user_to_claude` 取副本後量測）
- **037 token 抽取**：四份 037 之 `Analysis Report`、資料列 8 起、
  D 欄（Requirement Description），正則 `\$[A-Za-z0-9_]+\$`，區分大小寫
- **值域抽取**：對 CFTS044 轉檔文字，逐 token 套
  `re.escape(token) + r'\s*(?:=|is|shall be)?\s*\[([^\]]{1,60})\]'`
- **條文區塊切分**：`\*\*(\d{7}):` 切得 **2030** 個區塊
- **leaf → 區塊**：leaf → SYS-RA-CFTS044-N → SYS2 `Basic Report` 第 N 筆
  資料列 → `Source Requirement items` 7 位數 → 區塊（R-VS2 之鏈）
- **重疊比對**：對 Comfort 037 之 A–E 欄合併字串轉小寫，
  子字串命中 `heated seat` / `vented seat` / `heated steering` /
  `seat heat` / `ventilat` 任一者計為命中（**無詞界**，故為上界）

---

## 2. 收斂後之 DATA_REQUESTS

| # | 項目 | 實測依據 | 阻塞 | Urgency |
|---|---|---|---|---|
| 1 | **CFTS044 原始 `.docx` 二進位** | 附件檔頭非 PK zip，為轉檔文字 | `specification_reference` 全欄、spec 切分、TC 生成，且**本篇全部數字之複驗** | **High** |
| 2 | **SYS3 SYSAD 原始二進位** | 同上 | 範圍界定之佐證 | Medium |
| 3 | 六份素材入 `inputs/` 並取 SHA | G-L | 全部 | **High** |
| **4** | **`$HSW_StatFailSts$` 之值域定義**（CAN 訊號字典／DBC／等價文件）——**只缺這一個 token** | 037 用到 30 個 `$var$`，其中 **29 個之值域由 CFTS044 自身以 `$var$ = [值]` 內嵌給出**（含 `0h: Off` / `1h: Low` / `7h: ENS disabled` 這類 CAN 編碼）。`$HSW_StatFailSts$` 在 037 被引用 **16 次**，在 CFTS044 全文命中 **0** | 該 16 個引用所屬 leaf 之 ER 具體值 | **High** |
| **4b** | `$TGW_DISP_STAT$` 之**訊號讀取途徑**（非值域） | spec 命中 8 次，條文形態為「shall not alter」，無 `= [值]`。TC 要的是「讀得到這個訊號」之手段，不是值清單 | 4 個引用之可執行性 | Medium |
| **5** | **`TLM HMI Document`** | CFTS044 內文逐字點名 **10 次**；經 leaf 逐條回溯，**16 個 leaf**（HeatedSeat 8／VentedSeat 6／HSW 2）之需求條文以此文件承載畫面行為 | 該 16 leaf 之畫面文字與版面斷言 | **High** |
| **5b** | **`PDO graphics`** | CFTS044 內文點名 **2 次**；回溯得 **1 個 leaf**（Heated Steering Wheel 圖示左右鏡像置放） | 1 leaf 之圖示位置斷言 | Medium |
| **5c** | ~~Pop Up List／HMI Settings List／Market Configuration Table~~ | **撤回**。CFTS044 全文對 `Pop Up` 命中 0、`Settings List` 命中 0。`features/comfort/inputs/` 之三份既有檔**不必為本 feature 取用** | —— | **不請求** |
| **6** | **Comfort 之 43 個重疊 leaf 的委派界線** | Comfort 037 共 **498 leaf**，命中座椅加熱／通風／方向盤加熱關鍵詞者 **43 leaf**，其 Source 全部指向 `Comfort_HMI_Logic_and_Flow`（畫面行為）；本 feature 之同題 leaf 指向 CFTS044（訊號與配置）。**缺的是裁決，不是檔案** | §8.2.1 之委派句、本 feature 之 leaf 範圍 | **High（裁決）** |

---

## 3. 第 6 項之具體形態（供 Pei 裁定，不由執行層決定）

實測所見之分層假說：

```
Comfort（CFTS043 / Comfort HMI Logic and Flow）
    擁有：HVAC 畫面上的座椅加熱／通風控制之「畫面行為」
          （HVAC Popup Behavior、Status Bar Behavior、Heated Seat Control 等）
Vehicle Setting（CFTS044 Vehicle Controls）
    擁有：同一批實體功能之「訊號與配置層」
          （$HeatedSeatFL$ 等 CAN 值、$Heated_Seat_Levels$ 等車型配置分支、
            按鍵請求訊號 $FL_HS_RQ$、失效狀態）
```

支持該假說之獨立證據：CFTS044 自身在 16 個 leaf 的條文上寫
`Refer to TLM HMI Document` —— **它把畫面行為外推給別的文件**，
與「CFTS044 不擁有畫面行為」一致。

三種可能裁法（擇一，逐字記為 R-VS7）：

- **(a) 分層委派**：本 feature 只寫訊號／配置層，畫面斷言以 §8.2.1 委派句
  指名 Comfort 之對應 leaf。代價：16 個引 `TLM HMI Document` 的 leaf 仍
  需該文件才能寫出可觀察之 ER（DR-5 不因此解除）
- **(b) 全寫**：本 feature 之 271 leaf 全部依 037 逐條寫，重疊部分接受
  雙重覆蓋。代價：與 Comfort 已交付件產生重複追溯（§8.2.1 之反面）
- **(c) 逐條判**：43 個重疊 leaf 逐條決定。代價：43 次判斷，且判準未言明時
  會在 pilot review 再吵一次

分析層建議 **(a)**，但**不自裁**：本項落在「範圍界定（何者在／不在驗證
範圍）」，屬 Pei 裁定之列。

---

## 4. 對 00 包作業清單之修正

- **W-9 升為阻塞項**：原寫「發現重疊即停下升級」，實測已確認重疊存在
  （43 leaf），故 W-9 之產出改為
  `docs/reports/comfort_overlap.md`，**逐條列出 43 個 Comfort leaf 與其
  對應之本 feature leaf**，供 R-VS7 裁定使用。裁定前不得生成任何座椅／
  方向盤加熱之 TC
- **W-10 取消**：三份既有檔經實測與本 feature 條文無引用關係（DR-5c）。
  改為一句記錄寫入 `DATA_REQUESTS.md`：「已查 `features/comfort/inputs/`
  三份，本 feature 條文不引用，不取用」——**查過而不用，與沒查不同，
  須留痕**（G-D）
- **W-8 縮小**：30 個 token 中 29 個之值域由 CFTS044 內嵌給出，
  `data/spec_variables.tsv` 應**同時輸出其值域**（自 §1 之正則），
  只有 `$HSW_StatFailSts$` 標 `UNRESOLVED`

---

## 5. 本篇之盲區（R-G11）

1. 全部跑在**轉檔文字**上。表格欄位若於轉檔時被吞，值域抽取會少、
   外部文件依賴之 leaf 數會低估 → **DR-1 到位後全部重跑**
2. 切塊得 **2030** 個區塊，而規格內 distinct 7 位數 ID 為 **2302**，
   **差額 272 未追因**。若其中含本 feature 之 leaf，第 5 項之 16／1 為下界
3. 26 個 leaf 因其 SYS-RA 指向 SYS2 之 `Heading` / `Information` 列而
   **未取得條文區塊**，未參與第 5 項比對（A-VS01）
4. 重疊比對用**子字串、無詞界**，43 為上界；且只掃 Comfort 037 之 A–E 欄，
   未掃其交付工作簿之 TC 內容
5. `$var$` 之相異性以**逐字**計：`$Heated_Seat_Levels$`／
   `$Heated_Seats_Levels$`／`$Heated_Steats_Levels$` 被算成三個 token。
   三者疑為上游拼寫不一致（`Steats`），**登記為 A-VS02，RD-1 候選**

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 狀態 |
|---|---|---|
| R-VS7 | Comfort 43 個重疊 leaf 之委派界線 | **PENDING —— 待 Pei 裁定，三選項見 §3** |

本篇未產生任何已生效之新條文；R-VS7 為待裁項，未以生效條文形式書寫。
