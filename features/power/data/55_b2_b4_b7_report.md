# 55 包 B2 / B4 / B7 —— 執行層回報（承 56 包 §H）

56 包 §H 第 1 步已完成：R-P352–R-P362（11 條）逐字抄入 `RULINGS.md`，
R-P356 / R-P358 依 R-P36 加註，§F 入 `ANOMALIES.md`（A-PW340–A-PW348）。

本檔為 §H 第 2–3 步之回報。**B3 / B5 未施作**，理由見 §4。

## 1. B2 —— `ENTER_<STATE>` 片段表

落檔 `data/enter_state_55.md`。**八態中六可用、二 PENDING。**

| 片段 | 判定 |
|---|---|
| `ENTER_FULL_OPERATION` / `ENTER_IDLE` / `ENTER_TIMED` / `ENTER_PARTIAL_OPERATION` | **可用** |
| `ENTER_STANDBY` | 可用（`Timeout1` 值須由 ITD 給定）|
| `ENTER_BENCH` | 可用（措辭待站④ 人審）|
| `ENTER_SLEEP` | **PENDING** —— CAN 睡眠後無法再以 CAN 讀確認值 |
| `ENTER_INIT` | **PENDING** —— `VAL_` 無 INIT 值；門檻與時序外指 SIS，SIS 不在台帳 |

### 三項須裁

1. **A-PW350 —— R-P354 之八態與 DBC `VAL_ 1470` 之八值不相等，
   而 R-P354(c) 令以 `VAL_` 為唯一拼法。** `INIT` 不在 `VAL_`；
   `Logistic_On`（raw 5）在 `VAL_` 而不在八態；`VAL_` 拼法為 `Full_Operation`（底線）
   而 R-P354 自身寫 `Full-Operation`。**條文與其自身之判準互斥。**
   本層照八態產出、`ENTER_INIT` 標 PENDING、`ENTER_LOGISTIC_ON` 列附錄，不自行增刪。
   ⚠ 此形態 **R-P348 之 21 對相容性檢查查不到** —— 該檢查只查七條彼此，
   未查條文與既有 canon（R-7 / DBC `VAL_`）之相容性。
2. **A-PW351 —— G246 之「100%」不可能達成。** 二態之觀察方法在現有素材內不存在。
   不以降低判準求綠（R-P187）。請裁 G246 是否改為
   「可用片段 100% ＋ PENDING 者逐條列 DR」。
3. **A-PW349 —— 判準所依之 DBC 不在 G0 台帳。**
   `ENTER_<STATE>` 之訊號名與 `VAL_` 全取自
   `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`（`9ef1ec98…`），
   即 DR-PW21（20 包）所實查者，**自 20 包起即為判準來源而從未登記**。
   G0 之「9 / 9 通過」不涵蓋本包最重要之素材。請裁是否納入台帳。

### 新開 DR-PW26（High）

四問：`$PowerMode$` 之 DBC 歸屬（Body ON/OFF 之驅動）、`Sleep` 態之觀察方法、
`INIT` 態之 SIS 章節或觀察量、`$PwrAccDelayAct$` 之歸屬。
**阻斷 G246，不阻斷其餘六片段。**

## 2. B4 —— DR-PW23 附表

落檔 `data/dr_pw23_internal_signals_55.md`，已掛入 `DATA_REQUESTS.md` DR-PW23 條下。

- 全案內部訊號 **13 個相異名、845 次出現**
- **DBC 對照 0 / 13**（兩份 DBC 逐名實查）→ R-P355(b) 在本 feature **無適用對象**
- 十三名**全數在素材內有出處**，非自造
- `TLM_Status.Info`（97 條）循 R-P354 之 `Apply ENTER_<STATE>` 解消，不落 PENDING
- 其餘十二名全落 R-P355(c)

### 56 包 §L 之未估項，現已定量

| 量 | 值 |
|---|---|
| C3 家族 | 111 / 283 |
| 其中依 R-P354 可解 | 45 |
| 其中必落 PENDING | 66 |
| **全 corpus 施作後帶 PENDING 者** | **105 / 283（37.1%）** |

「逾百條 PENDING」為真，**精確值 105**。分析層之擔憂方向正確而量偏高（45 條由 R-P354 吸收）。
**57 包之寫回在 DR-PW23 未結前不可能成立**（S6 衝突，56 包 §K-2）。

### 素材自身之拼法不一致（非執行層所生）

`Phone_Call.Info`（82）／`PhoneCall.Info`（11）；
`SwitchOff_Timeout_Setting.Req`（35）／`SwitchOffSetting.Req`（8）。
**二者皆為素材原文**，R-7 令以單一拼法為準而本層不得擇一（擇一即代上游認定）。
已併入 DR-PW23 之詢問項。

## 3. B7 —— 家族 K 之實際規模

R-P360(b) 依 14 對重複之誤判定其規模。**實測 158 / 283（55.8%）**。

| 分類 | 數 | 處置 |
|---|---|---|
| 單行 ITD ≤ 60 字元 | **135** | 內聯無虞 |
| 單行 ITD > 60 字元 | 15 | 內聯後恐逾 §5.2B 字數上限，須逐條檢 |
| **多行 ITD** | **8** | 疑為 **IN §4.5 第 3 類獨立資料集**，依 R-P360(c) 應**保留 ITD 並逐列說明**，不內聯 |

14 對誤判所涉之 22 條 TC 中，20 條落在「單行 ≤ 60 字元」，**全部可內聯**。

**須裁**：R-P360(b) 之「ITD 改 `NA`」是否適用於全部 158 條。
本層讀 R-P360(c) 之但書（「ITD 非 `NA` 者須逐列說明其為第 3 類獨立資料集」）
為**已預留例外**，故建議：135 條內聯改 `NA`、15 條逐條檢、8 條保留並說明。
**惟 158 與 14 相差一個數量級，條文所本之規模估計失準，故請裁而不逕行。**

## 4. B3 / B5 未施作之理由

- **B3（代理量表）** 涵蓋 260 條之非白名單 `<X>`，其每一條須引
  CFTS009 / SYS1 之錨點。**本 feature 無 SYS1**（`feature.yaml`：`sys1_export: null`）——
  R-P353 與 R-P354(b) 所給之「得併用 SYS1」在本 feature 上為空。
  代理量之錨點只能取自 CFTS009 / SYS3，**可及性須先確認**。
- **B5（機器改寫）** 依 B2–B4，而 B2 有二態 PENDING、B4 有 105 條 PENDING、
  B7 之規模與條文差一個數量級。**在 §1 三問、§3 一問未裁前施作，
  等於以未定判準改寫 283 條**，違 §I 之精神。

## 5. 待裁清單

1. A-PW350：R-P354 八態 vs DBC `VAL_` 八值（`INIT` / `Logistic_On` / `Full_Operation` 拼法）
2. A-PW351：G246 之期望值是否改寫
3. A-PW349：DBC 是否納入 G0 台帳（納入則 G0 改 10/10，並須定版本凍結規則）
4. R-P360(b) 之適用範圍：158 條或僅可內聯之 135 條
5. B3 之錨點來源：本 feature 無 SYS1，代理量錨點是否限 CFTS009 / SYS3

**五項未裁前，執行層停在本步。**
