# 15 下放包 — 裁決第二批（R-VS18～R-VS24）與 05 輪指令

分析層寫入，2026-08-20。Pei 指示「裁」，即採各包所附之建議定案。
本檔 §1 為裁決正文，§2 為 05 輪啟動指令。

---

## 1. 裁決正文（執行層須逐字轉錄入 `RULINGS.md`）

### 1.1 R-VS18

```
R-VS18（Pei 2026-08-20）
上繳包不是最後一項，是**第一項**。

每輪開工之第一個動作為：建立 `docs/upstream/NN_<slug>.md`，
寫入標題、本輪作業清單、與 canon §8.2 之六個空節
（預期 vs 實測／不符項目／三分法／掃描條件／新開 anomaly 與 DR／
獨立判斷），各節先留空白。

其後每完成一項作業，**當下就把該項之結果填入對應節**，
`reports/` 之細節報告為其附件而非替代。

理由：`reports/` 逐項落檔會產生「已交付」之錯覺，而上繳包所要求之
六項（尤其「預期 vs 實測逐項對照」與「本包是否仍有該驗而未驗者」）
是**跨項的**，逐項報告不會自然產生它們。
```

### 1.2 R-VS19

```
R-VS19（Pei 2026-08-20）
CFTS044 之值域列舉須連同其條文之 [EE Architecture] 標籤一併取用。
本 feature 僅採 `Atlantis High`（含 `All`）之條文；標記為
`CUSW`／`PowerNet`／`Atlantis Mid` 而未含 Atlantis High 者，
其值域不適用於本 feature，亦不得作為「CFTS044 與 DBC 不一致」之證據。

實例：`$HeatedSeatFL$` 於 CUSW 條文（4857940）列 0h/1h/3h 三階，
於 Atlantis High 之具名式與 LID 表皆為四階（含 MED / 2）。
本 feature 取四階。

推論：值域比對之輸出須加一欄 `arch_scope`，記錄該值域出自哪些
架構標籤之條文；跨架構之差異不列為不一致。
```

### 1.3 R-VS20

```
R-VS20（Pei 2026-08-20）
token 之值域依下列次序取用，前者有值即止：

  第一階  CFTS044 之 in-scope 條文（[EE Architecture] 含 Atlantis High
          或 All）之值域
  第二階  LID 表之對應欄組（CAN Mapping → Atlantis High；
          Proxi & Configuration → Atlantis & Atlantis High）
          ＋ 對應 DBC 之 VAL_ 值表
  第三階  停下回報，登記待判

**他架構條文（CUSW／PowerNet／Atlantis Mid）之值域一律不取用**，
僅得作為旁證記於 reasoning，不得寫入 TC 欄位。

理由：LID 表與 DBC 之值域**無架構條件**（其架構條件在欄組層，已由
R-VS9(1)′ 指定），故第二階不引入架構風險；而他架構條文之值域帶有
該架構之假設，取用等同以 CUSW 之行為描述 Atlantis High。

實例：$HSW_StatFailSts$ 於 CFTS044 之 in-scope 無值域（其值僅見於
Atlantis Mid 條文），依本條走第二階 —— 取 LID 表與 DBC 之
`Fail_Not_Present` / `Fail_Present`（二來源一致）。
該 token 之值域**不因 Atlantis Mid 條文而成立，亦不因之而受質疑**。
```

### 1.4 R-VS21

```
R-VS21（Pei 2026-08-20）
一項作業連續兩輪未執行者，下輪**排入頭部**，且該輪不得於其前方
加入新作業。新發現之事項一律登記為 anomaly／DR 並排入其後輪次。

例外：新事項為**阻塞既有作業之前置**時得插隊，惟須於下放包具名
說明其為何是前置。

本條與 R-VS25（單輪上限三項）併用：頭部由本條決定，長度由 R-VS25 決定。
```

### 1.5 R-VS23

```
R-VS23（Pei 2026-08-20）
入庫作業之阻斷判準為「**暫存區**內出現 pathspec 以外之路徑」，
非「工作區存在 pathspec 以外之變更」。

步驟中之 `git status` 掃描其用途為揭露與留痕，其有輸出時應
**列出並續行**；真正的閘門在暫存區之逐檔核對。

理由：多 feature 並行時工作區幾乎永遠有他 feature 之在途變更，
以「存在」為阻斷判準會使每次入庫都停。
```

### 1.6 R-VS24（追認）

```
R-VS24（Pei 追認 2026-08-20）
附錄 A 入庫之窄口授權，內容如 12 包 §4；該授權已於執行時用畢並失效。
追認其行使正當。

一併確立通則：窄口授權**一次性、用畢即失效**，不因同一指令被再次
貼上而復活。執行層拒絕重跑為正確行為。
```

---

## 2. 05 輪啟動指令（取代 13）

`13_round04_prompt.md` 標為 SUPERSEDED。

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/14_review_round04.md 本輪依據
  features/vehicle_setting/docs/handoff/15_rulings2_round05.md 裁決第二批（本檔）
  features/vehicle_setting/docs/handoff/09_review_round03.md  W-22／W-23 之規格
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入 R-VS25 之三項上限）

D-1  依 R-VS18 建立 docs/upstream/04_extraction_and_overlap.md，
     六節先留空，逐項完成即填。

D-2  逐字轉錄入 RULINGS.md（不摘要、不以編號代替）：
       14 包 §3 之 R-VS9(1)′
       14 包 §4 之 R-VS25
       本檔 §1.1–§1.6 之 R-VS18／R-VS19／R-VS20／R-VS21／R-VS23／R-VS24
     並於 RULINGS.md 之 R-VS9 條目加註：
       「(1) 之權威分工經 R-VS9(1)′ 更正，以 R-VS9(1)′ 為準」

D-3  ANOMALIES.md 套用 14 包之狀態變更：
       A-VS26 → **降級**為我方解析產物（LID 單格載兩個 message 與兩個網段，
                 STATUS_CCAN3=CAN-B、ENGINE_FD_2=FD，與 DBC 一致）；DR-13 撤銷
       A-VS28 → **範圍縮為 1 支**（HDRstRelRq_3rdRow）。
                 FL_HS_Tlm／FL_VS_Tlm／HSW_Tlm 皆在 BHCAN；
                 HeatLeftSeatTgl／FL_HS_Cmd_Tlm_Req／HSW_Cmd_Tlm 屬 Atlantis
                 欄組（非 in-scope），依 R-VS9(1)′ 不取用
       DR-14 → 改寫為 DR-14′（14 包 §2 之全文）

## 作業（**三項，R-VS25 上限；第四項起不得執行**）

W-23  歸因判準化 ＋ **修正 C3 解析式**
      (a) **先修解析式**：LID `Signal Name` 與 `Format` 儲存格得含**多個**
          訊號／多個 message／多個網段（已知形態：以空白或換行分隔之
          `MESSAGE.Signal` 對，CAN 欄同序列出 `CAN-B  FD`）。
          解析須逐對展開，不得只取第一個。
          **驗證錨點**：ESS_ENG_ST 須解出 (STATUS_CCAN3, CAN-B) 與
          (ENGINE_FD_2, FD) 兩對；HSW_Stat 須解出 HSW_STATSts 與
          HSW_STATFailSts 兩支。
      (b) 將 02 上繳 §2.2 之五類寫成可機器判定之規則
          （C1 別名切分／C2 LID 列粒度／C3 Format 解析殘缺／
            C4 規格引用子集／C5 縮寫 vs 全名），套用於 W-19 之 39 項。
          只有不落入 C1–C5 者進待判清單；每輪列 C1–C5 計數證明判準運作，
          不逐筆展開。
      理由（R-VS21 例外條款）：C3 之同一缺陷已三度現身（W-8 之 C3、
      W-15b′ 之交叉配、A-VS26），且 W-22 會用到同一解析器 ——
      **先修工具再比對**，否則第四次踩到。

W-22  餘數驗證 → data/value_extraction_residual.tsv
      逐 token 取其在 CFTS044 之全部出現位置，減去三式已命中者，
      逐筆檢視餘數上下文（前後 200 字元），分類為
        (a) 敘述性提及不帶值域
        (b) 帶值域但記法為三式所不涵蓋  ← 第四式之證據
        (c) 無法判定
      通過條件：**(b) 為 0**，或 (b) 全數化為新式並重跑。
      **不得以「餘數看起來都是敘述」收尾** —— 須逐筆分類並附計數。
      已知：式一 451／式二 45／式三 34 命中。

W-9   Comfort 逐條對照 → docs/reports/comfort_overlap.md
      **本 feature 側母體為 237 個 Functional leaf，非 271**
      逐條列出命中座椅加熱／通風／方向盤加熱之 Comfort leaf（SWE1-HVAC-*）
      與其對應之本 feature leaf，作為 R-VS7 委派句之來源表。
      另附 CFTS044 內文以 {CFTS043} 引用 Comfort 之 3 處上下文。
      必停已由 R-VS7 解除。

**W-17／W-24／DR-14′ 之追問排入 06 輪，本輪不做。**

## 禁區

git 寫入性操作一律不執行（R-VS24 之窄口已用畢失效）。
需入庫者，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
.gitignore 之修改屬 Pei。

## 升級條件

W-23(a) 之驗證錨點未通過（ESS_ENG_ST 未解出兩對，或 HSW_Stat 未解出兩支）；
W-22 之 (b) 類非 0 且無法化為新式；
實測與 14／15 包之數字不符；撞到 §8.4.1 編造壓力；
需要判斷而無條文。
**本輪無「必停」項。**

## 已無待裁之阻塞

R-VS7～R-VS25 全部裁定完畢。framework 之前置條件已備：
  訊號名之寫法 → R-VS9(1)′
  值域之來源   → R-VS20
  母體         → R-VS15（237）
  Test Set     → R-VS4（四個）
本輪完成後即可進 framework Part Vehicle Setting ＋ profile（Tier 2）。
**本輪不做 framework。**
```

---

## 3. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS18 | 上繳包為每輪第一項 | ✔ §1.1 |
| R-VS19 | 值域須連同 `[EE Architecture]` 取用 | ✔ §1.2 |
| R-VS20 | 值域來源之階梯 | ✔ §1.3 |
| R-VS21 | 連兩輪未執行者排入頭部；與 R-VS25 併用 | ✔ §1.4 |
| R-VS23 | 入庫阻斷判準在暫存區而非工作區 | ✔ §1.5 |
| R-VS24 | 窄口授權一次性、用畢失效（追認） | ✔ §1.6 |

六條皆以獨立可貼入之區塊呈現，未夾在敘述中。
