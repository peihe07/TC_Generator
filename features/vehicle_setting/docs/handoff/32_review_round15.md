# 32 下放包 — 15 輪覆核：typo 判據定案、值域正規化、DR-18、16 輪指令

分析層寫入，2026-08-20。對象：`docs/upstream/13_contamination_and_symmetry.md`。

**覆核結論：接受。** §2.3 之自陳（「初測 3 筆中有 2 筆是我自己的過濾器造成的」）
與 §2.6 之判據不足指摘，皆為 R-VS29／R-VS32 所欲防之形態，
本輪由執行層自行攔下。

---

## 1. typo／別名判據 —— 分析層之原判據不足，修訂

31 包 §5 之判據逐字為「對稱側一律用另一前綴者判 typo；
對稱側亦用同前綴者判別名」。

`4860015`／`4860021` 兩側**一致地**寫 `HS_OFF` —— 依原判據應判「別名」，
**但同章節內 `4860011`／`4860013`／`4860017`／`4860019` 皆為 `VS_OFF`，
全文 `VS_OFF` 15 次對 `HS_OFF` 2 次。**

**原判據之缺陷**：它假設錯誤不會對稱地發生。而 037／CFTS044 之左右兩節
係複製後修改，**複製錯誤必然對稱** —— 該假設在此類文件上不成立。

```
R-VS38（typo／別名之判據，分析層裁定 2026-08-20）
值之前綴或標籤與其 token 語意不符時，依下列三項聯合判定，
**不得單以任一項定案**：

(a) 對稱側同位條文之值（原 31 包 §5 之判據）
(b) **同章節內**是否兩形態並存 —— 並存即自相矛盾，判 typo
(c) **全文頻次比** —— 少數形態判 typo

判為「別名」須同時滿足：(b) 同章節內**不**並存、且 (c) 兩形態頻次
在同一數量級。**別名須為系統性雙軌命名，不得由少數例外構成。**

理由：左右兩節係複製後修改，複製錯誤必然對稱；
僅以 (a) 判定，會把「兩側一致地抄錯」判成別名。
實例：`4860015`／`4860021` 兩側皆 `HS_OFF`，而同章節內
`4860011`／`4860013`／`4860017`／`4860019` 皆 `VS_OFF`，
全文 15 : 2 —— 判 typo。

A-VS54 依本條關閉。
```

---

## 2. 值域之大小寫雙寫（A-VS52）—— 計數與書寫分離

`$VentedSeatFR$` 之同一值因大小寫與空白差異算成五個
（`VS_LO`／`VS_Lo`；`Vented Seat Medium`／`Vented seat Medium`／`Vented seat medium`）。
**其直接後果是 TC 之列舉分支數虛高。**

```
R-VS39（值域之正規化與書寫，分析層裁定 2026-08-20）
值域之**計數、比對、分支決定**以正規化鍵為準：
    casefold ＋ 連續空白壓為單一空白 ＋ 去除首尾空白
    ＋ 依 R-VS38 判定之 typo 前綴修正
同鍵者視為同一值，**不論其在 CFTS044 中之寫法有幾種**。

TC 工作簿內**書寫**之值，取**基線 DBC 之 `VAL_` 逐字**
（承 R-VS9(1)′：DBC 為匯流排定義本身）。
CFTS044 之寫法僅作來源佐證，記於 `spec_variables.tsv`，不進工作簿。

`spec_variables.tsv` **保留全部原始寫法不合併**，
另增 `normalized_key` 欄；相異值之計數以該欄為準。

理由：CFTS044 之大小寫雜訊是撰寫產物，非語意差異；
以其原樣計數會使 `$VentedSeatFR$` 之四階值域看起來有五至七個分支。
```

**A-VS53（`$Heated_Steats_Levels$`）併入 A-VS05**（00B §5-5 已登記同一 typo），
不另行處理；其正規化鍵依 R-VS39 與 `$Heated_Seats_Levels$` 相同。

---

## 3. DR-18（分析層擬，Urgency Medium，Pei 送出）

W-47 已掃全（14 token × 6 欄，4 筆，別名 0），DR-18 之範圍可定案。

```
DR-18（分析層擬 2026-08-20）
CFTS044 之座椅相關值域中，發現四類書寫問題，請確認其為筆誤或另有語意：

一、加熱／通風前綴交叉（4 筆）
    4858393  §1.3.2.1.3.4  $VentedSeatFR$ = [Vented Seat High / HS_HI]
    4858001  §1.3.1.1.3.4  $VentedSeatFR$ = [Vented Seat High/HS_HI]
    4860021  §1.3.4.12.4   $VentedSeatFR$ = [Vented Seat Off / HS_OFF]
    4860015  §1.3.4.12.3   $VentedSeatFL$ = [Vented Seat Off / HS_OFF]
    對照：同章節內其餘同型條文一律 `VS_`；全文 `VS_OFF` 15 次對
    `HS_OFF` 2 次。我方判為筆誤，請確認。

二、值退化（1 筆）
    4858413  §1.3.2.1.3.4  $CCDMF_FR_VS_RQ$ = [ Pressed]
    其左側對稱條文 4858382 為 [Vented Seat Pressed / VS_PSD]。
    請確認 4858413 應為 [Vented Seat Pressed / VS_PSD]。

三、同一值之多種大小寫寫法
    [Vented Seat Low / VS_LO] 5 次 ／ [Vented Seat Low / VS_Lo] 4 次
    [Vented Seat Medium / VS_MED] 2 ／ [Vented seat Medium / VS_MED] 2
      ／ [Vented seat medium / VS_MED] 4
    請確認其為同一值。

四、參數名筆誤
    $Heated_Steats_Levels$（`Steats`）與 $Heated_Seats_Levels$ 並存，
    前者於 Logical Identifiers and CAN Mapping 之 2,974 個 LID 中無對應。

影響：座椅加熱／通風之值域列舉分支數，涉及 Heated Seat 88 ＋
Vented Seat 72 共 160 個 SWE leaf。
我方已依內部判準處理（正規化計數、原值保留），
本請求為確認而非阻塞。
```

**DR-18 為確認型，不阻塞**；與 DR-15（阻塞）、DR-17（阻塞）分開標示。

---

## 4. §2.1 之 2 vs 3 —— 分析層之計數口徑錯

31 包 §1 將「`HeatedSteeringWheel-009` 加 `UNRESOLVED-SOURCE` 標記」
計入「不一致筆數」。**該筆之 Layer 3 判定結果等於其 token，不構成不一致。**

**執行層之 2 為正確口徑。** 分析層更正，不要求調和。

---

## 5. 16 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/32_review_round15.md 本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/14_normalization_and_lock.md，六節先留空。
D-2  逐字轉錄 32 包 §1 之 **R-VS38** 與 §2 之 **R-VS39** 入 RULINGS.md。
D-3  ANOMALIES.md：A-VS54 依 R-VS38 **關閉**；
     A-VS53 併入 A-VS05（加註交互參照，兩者皆保留 —— R-TM13）。
     依 R-VS35 列兩數。
D-4  `DATA_REQUESTS.md` 新開 **DR-18**（32 包 §3 全文），
     標 Urgency Medium、**確認型不阻塞**。**不送出。**

## 作業（三項，R-VS25）

W-50  值域正規化與剩餘 token 之污染掃描
      (1) 依 R-VS39 於 `spec_variables.tsv` 增 `normalized_key` 欄，
          **保留全部原始寫法**；列出「原始相異值數」與
          「正規化後相異值數」兩組，逐 token 對照
      (2) 13 輪 §6-1 之 16 個無語意前綴 token（`$ESS_ENG_ST$`／
          `$PowerMode$`／`$Hybrid_Type$` 等），改以**反向判準**掃描：
          其值中是否出現**他 token 之語意前綴**（`HS_`／`VS_`／`HSW_`）
      (3) 13 輪 §6-3 之大小寫重複只量過 `$VentedSeat*$`，
          **對全部 30 個 token 重量**，列出受影響者

W-51  CUSW 遷入節族之逐位對照（13 輪 §6-2）
      `1.3.1.1.3.*` 四節（`4858001` 之 typo 出自此節族）逐位對照，
      比對引用狀態與方括號值之對稱性。
      **不得用 `difflib`**；值抽取條件須**不分大小寫**
      （13 輪 §2.3 之假不對稱即源於大小寫敏感）。
      **本節族為 CUSW 架構** —— 依 R-VS19 現行版其值域不取用，
      **但 R-VS19′ 待裁（P20）**；若 P20 採 (c)，其適用性判準改變。
      **本輪只取證，不依任一版判準排除任何條文。**

W-52  framework 鎖定前之最後驗證
      (1) **逐 leaf 驗證 Layer 2 歸屬**：現行以 token 字串判定，
          未以 037 檔界驗證。改以「該 leaf 出自哪一份 037 檔」
          逐筆核對，列出不一致者
          （已知待驗：`CrossZone Common` 之 2 leaf 歸 `Heated Seat`
            係依 32 包文字，其原始檔屬 HeatedSeat.xlsx 一事未驗）
      (2) 更新 `framework.md` 之鎖定前未解項清單，逐項標其
          阻塞／不阻塞與所待之 DR 編號
      (3) **framework 仍不鎖定** —— 鎖定屬 Pei（P19）

## 禁區

git 寫入性操作一律不執行。不補素材、不代擬條文、不自行調和數字。
**不得合併或改寫 `spec_variables.tsv` 之原始值**（R-VS39 僅增欄）。
**不得鎖定 framework。不得依 R-VS19 或 R-VS19′ 排除條文**（P20 未裁）。

## 升級條件

W-50(2) 之反向掃描有命中；
W-50(3) 之大小寫重複影響 `$VentedSeat*$` 以外之 token；
W-51 出現與 Vented／Heated 兩節皆不同型之不對稱；
W-52(1) 之 Layer 2 歸屬有不一致；
實測與 32 包之數字不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。
```

---

## 6. 待 Pei

| # | 事項 | 狀態 |
|---|---|---|
| **P20** | 裁 **R-VS19′**（Atlantis Mid，112 leaf 佔 47%） | 證據完整，**已掛三輪**。W-51 之取證亦受其影響 |
| **P18** | 裁 **R-VS7(a)′**（委派句指名功能群） | 證據完整，已掛兩輪 |
| P19 | framework 簽核 | 俟 W-52 之未解項清單 |
| — | **DR-15／DR-17 送出**（阻塞型） | 二者已定稿未送 |
| — | **DR-18 送出**（確認型，不阻塞） | 本包定稿 |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS38 | typo／別名之三項聯合判據；別名須系統性 | 分析層 |
| R-VS39 | 值域計數以正規化鍵；工作簿書寫取 DBC `VAL_` 逐字 | 分析層 |
| DR-18 | 座椅值域之四類書寫問題（確認型） | 分析層擬，Pei 送出 |
