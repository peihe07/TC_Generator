# 下放包 20 —— R-DD25（範圍裁定：LATAM 不在案內）、-025~-028 轉範圍外、DR-DD1 改稿、閉合 24+4、T26

- 日期：2026-08-28
- 方向：分析層 → 執行層 ＋ Pei（§六 出貨閘）
- 前一包：`19_ship_ready.md`
- **Tier 3 範圍事實**（Pei 2026-08-28）：本案只做 **NAFTA**，**不做 LATAM**；
  **Hong Kong 在案內，因其與英國同為右駕（RHD）**
- 本包**解除 `-025`~`-028` 之凍結，改判範圍外**；A-DD1 隨之結案

---

## 一、Pei 所述之理由，於市場表可查（分析層實測）

`forms/SR24 R1 Market Configuration Table v1.6.xlsx` → `Market Config - R1`：

- **c14 表頭逐字**：`Right-Hand Drive \nvs. \nLeft-Hand Drive`
- **c16 表頭**：`Region`

| r | Destination Country | Region | **c14** | Country_Code |
|---|---|---|---|---|
| **97** | **HONG KONG** | **APAC** | **RHD** | **91** |
| 216 | UNITED KINGDOM | EMEA | **RHD** | 5 |
| 104 | IRELAND | EMEA | **RHD** | 98 |
| 19 | AUSTRALIA | APAC | **RHD** | 10 |
| 109 | JAPAN | APAC | **RHD** | 6 |
| 36 | BRAZIL | **LATAM** | LHD | 15 |
| 46 | CANADA | NAFTA | LHD | 4 |
| 138 | MEXICO | NAFTA | LHD | 14 |

Region 分布：EMEA 149／APAC 37／**NAFTA 19**／**LATAM 19**／空 19。
c14 分布：LHD 178／**RHD 45**／n/a 1／空 19。

**要義**：`Hong Kong` 之 Region 為 **APAC 而非 NAFTA** ——
其在案內之依據**不是市場區域，是駕駛側（RHD）**，與英國同組。
**故「只做 NAFTA」不蘊含「香港出局」**；二者為不同之維度。
`-017`~`-024`（8 則，已生成）**維持在案，不撤**。

---

## 二、R-DD25（範圍裁定；T-抄）

```
R-DD25（市場範圍與 -025~-028 之處置 —— Pei 2026-08-28 範圍裁定）

(a) 本案之市場範圍：**NAFTA 在案、LATAM 不在案**（Pei 2026-08-28）。
    `Hong Kong` 在案，其依據為**右駕（RHD）**而非區域 ——
    市場表 `Market Config - R1` c14（`Right-Hand Drive vs. Left-Hand Drive`）
    載 HONG KONG(r97)＝RHD，與 UNITED KINGDOM(r216) 同；
    其 Region(c16) 為 APAC。**區域與駕駛側為二個獨立維度，不得互相蘊含。**

(b) `SWE1-RA-Driver_Distraction-025`~`-028` 判為 **OUT OF SCOPE**，
    不生成 TC。三項獨立依據收斂：
      1. 其 Source 之 `-132`／`-133` 屬 CFTS022 之 LATAM 章
      2. SYSAD 載速度遲滯判定為 `JudgmentProcessorType4to6 … for LATAM`
      3. (a) 之範圍裁定：LATAM 不在案
    即該四列所依之行為**於本案不實作**。此為**不該測**，
    非「該測而資訊不足」—— 與凍結（A-DD1）之性質不同。

(c) A-DD1 由 `OPEN（凍結）` 改 **`CLOSED-BY-SCOPE`**，
    載結案依據為 (a)(b)，並註明其**非以 DR 回覆結案**。

(d) 範圍外**不等於免於記錄**：四列須入 `COVERAGE_GAPS.md`（[CG-DD2]），
    載其 leaf 號、判為範圍外之依據、及「037 仍載該四列」之事實。
    **不得於任何統計中把 28 寫成 24 而不交代差額**（R-DD10(c)）。

(e) 本條不及於 `-017`~`-024`（RHD 依據，(a) 末句）；
    亦不改變 R-DD19 之 A-DD8／A-DD9（其為施加路徑之假設，與市場範圍無涉）。
（Pei 2026-08-28 範圍裁定，分析層落條，下放包 20 §二）
```

---

## 三、DR-DD1 改稿（性質變更：釐清件 → 確認件；**仍必發**）

原稿問「香港還是拉美」。範圍裁定後該問題已由 Tier 3 答；**餘下者為文件缺陷**。
**整段替換**為下稿：

> **DR-DD1 — Rows `-025` ~ `-028` derive from out-of-scope LATAM requirements
> while their text specifies Hong Kong**
>
> `SWE1-RA-Driver_Distraction-025` ~ `-028` in FM-WI-FSM-037-A03 cite
> `SYS-RA-Driver_Distraction-125` together with `-132` / `-133`. In CFTS022,
> `-132` / `-133` belong to the LATAM chapter, and the System Architectural
> Design describes the speed-hysteresis judgment they specify as a
> market-specific processor type for LATAM
> (`ProcessorType4to6 … for LATAM`), whereas the Hong Kong logic is
> described in terms of parking-brake state and gear selection.
>
> This programme covers NAFTA and does not cover LATAM; Hong Kong is in
> scope as a right-hand-drive market (`Market Config - R1`, row 97: RHD,
> Region APAC), not as a LATAM market. The behaviour specified by
> `-132` / `-133` is therefore not implemented in this programme.
>
> However, the Requirement Description, Verification Criteria and
> Verification Method of all four rows read `Country_Code is Hong Kong` /
> `Preset Country_Code to Hong Kong`.
>
> Question: please confirm that rows `-025` ~ `-028` should be removed or
> revised, since they combine an out-of-scope LATAM source requirement with
> Hong Kong wording. SWQT has recorded them as out of scope and has not
> generated test cases for them; the remaining 24 leaves are covered.

**等級**：必發（文件缺陷）。**阻斷**：無 —— 交付不再等其回覆。

---

## 四、framework.md 之第 6 組

`Market Speed Gating`（`-025`~`-028`）由 `PENDING（DR-DD1）` 改：

```
6 | Market Speed Gating | 025–028 | **OUT OF SCOPE（R-DD25(b)）** | 不生成
```

Layer 2 之組數不變（六組），**閉合式改為 24 生成 ＋ 4 範圍外 ＝ 28**。
組名保留（其為 037 分組之事實），**不刪組** —— 刪之則 28 之閉合無從交代。

---

## 五、任務（T26）

| # | 任務 |
|---|---|
| T-抄 | R-DD25 入 `RULINGS.md`；錨點數與停止值同步回報 |
| T-登 | A-DD1 改 `CLOSED-BY-SCOPE`（§二(c) 依據逐字）；DR-DD1 文稿**整段替換**為 §三 之稿並改等級註記；**[CG-DD2] 建條**（§二(d)）|
| T26a | `framework.md` 第 6 組依 §四 改；**閉合式同步改為 24 ＋ 4 ＝ 28** |
| T26b | **T24e 盤點重跑**：應為 **24 可出貨 ＋ 0 不得出貨 ＋ 4 範圍外 ＝ 28**。三項覆核之判準隨之改 —— 「凍結名單」改讀 **範圍外名單**（自 profile §5 與 framework 導出，**不硬編 leaf 號**）|
| T26c | profile §5 之凍結列改述（`-025`~`-028`：凍結 → 範圍外，依 R-DD25）—— **分析層自辦**，執行層勿動 |

**不在本輪**：寫回工作簿、git、tsv、`-025`~`-028` 之任何生成。

---

## 六、待 Pei —— 出貨閘（唯一剩餘決定）

| | |
|---|---|
| 已產出 | **24**（`-001`~`-024`）|
| **可出貨** | **24** |
| 範圍外 | 4（`-025`~`-028`，R-DD25）|
| **阻斷出貨之 DR** | **無** |
| 閉合 | 24 ＋ 4 ＝ **28** ✅ |

**發送清單（本包後）**：

| 級 | DR | 阻斷 |
|---|---|---|
| 必發 | **DD1**（改稿：確認件）、**DD5**、**DD6**、**DD8** | **皆不阻斷** |
| 緩發 | DD2、DD4、DD7、DD9 | 不阻斷 |

**本 feature 之生成工作至此完成。** 餘一項 Tier 3 決定：**何時寫回工作簿**
（甲：等 DR 回覆撤 marker 後寫回；乙：即寫回，marker 隨簿，回覆後機械回修）。
**分析層意見仍為乙。**

## 七、上繳包要求（`docs/upstream/17_scope_close.md`）

T-抄／T-登、`framework.md` 改後全文、T26b 之盤點（24／0／4，三項覆核）、
[CG-DD2] 條目、未結 DR 清單、獨立自評、R-G8。
