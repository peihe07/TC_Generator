# 09 下放包 — 03 輪覆核、`$PowerMode$` 之複驗、餘數驗證

分析層寫入，2026-08-20。對象：`docs/upstream/02_variables_and_sweep.md`。

**覆核結論：接受。** 本輪為迄今最完整之一次上繳：六節齊備、
未執行之三項具名列出、三項界線自陳且其中一項被自評為「本輪最弱一環」。
R-VS18 之效果經其 §6.3 自證 —— **前三輪漏寫，是因為那兩節只能跨項產生。**

---

## 1. `$PowerMode$` 之複驗 —— A-VS24 成立，但其範圍比回報**小**

上繳 §2.1 第 2 項稱 CFTS044 之 in-scope 值含 `IGN OFF`／`IGN OFF ACC`，
而 `CmdIgnSts` 無 OFF，判為「狀態不存在」。

分析層自 `inputs/` 原始 docx 複驗（條文以 `\d{7}\s*:\s*\[Artifact Type` 切
2030 塊，逐塊取 `[EE Architecture:…]` 首次命中，逐塊抽
`$PowerMode$ = [值]`）：

| 架構標籤 | 值 | 次數 |
|---|---|---|
| `All` | `IGN_RUN` | 7 |
| `Atlantis High` | `Ignition lock / IGN_LK` | 3 |
| `All` | `Ignition lock / IGN_LK` | 3 |
| `CUSW` | `Ignition lock / IGN_LK` | 2 |
| `Atlantis High, PowerNet` | `IGN_RUN` | 2 |
| `PowerNet` | `Ignition lock / IGN_LK` | 2 |
| `PowerNet, Atlantis High` | `Ignition run / IGN_RUN` | 2 |
| `Atlantis High` | `Ignition start / IGN_START` | 1 |
| `Atlantis High` | `Ignition run / IGN_RUN` | 1 |
| `Atlantis High, PowerNet` | `Ignition start / IGN_START` | 1 |
| **`All`** | **`IGN_OFF`** | **1** |
| `CUSW` | `Ignition start / IGN_START`／`Ignition run / IGN_RUN`／`IGN_RUN` | 各 1 |

含 `$PowerMode$` 之條文區塊 **59** 個。

### 1.1 逐一檢視 OFF 系之出處

| 值 | 出處條文 | 架構 | 主題 |
|---|---|---|---|
| `Ign. off & acc. (4 position switch) / IGN_OFF_ACC` | 4858156 | **CUSW** | Third Row Headrest Dump |
| 同上 | 4858978 | **Atlantis High** | Second Row Headrest Dump |
| 同上 | 4858995 | **Atlantis High, PowerNet** | Third Row Headrest Dump |
| `Ignition off (5 position switch) / IGN_OFF` | 4859xxx | **All** | **Charging schedule 送 SDP server** |
| `IGN_OFF` | 4859664 | **All** | **充電排程之 end time 比較** |

**兩項更正**：

1. **`IGN_OFF`（純 OFF）之兩處，主題皆為 PHEV 充電排程**，
   而非座椅／方向盤加熱。其是否落在本 feature 之 237 個 Functional leaf
   內，上繳未查，分析層亦未查 → **W-24**。
2. **`IGN_OFF_ACC` 有一處確在 `Atlantis High`**（4858978，Second Row
   Headrest Dump），且 Headrest Dump 屬 Common Features。
   **故 A-VS24 於 in-scope 內成立，但成立點是 `IGN_OFF_ACC` 而非 `IGN_OFF`。**

### 1.2 對映之可能性 —— **不由本層認定**

LID 表之 `PowerMode` 對映至 `CmdIgnSts`，其值域
（`Initialization`／`IGN_LK`／`ACC`／`RUN`／`START`／`SNA`）**含 `ACC`**。
`IGN_OFF_ACC` 之語意（四段式開關之 off&acc）與 `ACC` **可能**對應，
但 CFTS044 之 `IGN_OFF_ACC` 與 `CmdIgnSts` 之 `ACC` 是否同一狀態，
**無任何素材明載**。

**執行層未自行對映，正確**（§8.4.1）。
DR-12 之提問須據此改寫：

> CFTS044 於 `[EE Architecture:Atlantis High]` 條文（如 4858978）以
> `$PowerMode$ = [Ign. off & acc. (4 position switch) / IGN_OFF_ACC]`
> 作為 Headrest Dump 軟鍵可選之條件；而 LID 表將 `PowerMode` 對映至
> `STATUS_BH_BCM2.CmdIgnSts`，其值域為
> `Initialization / IGN_LK / ACC / RUN / START / SNA`，**無 IGN_OFF_ACC**。
> 請確認 `IGN_OFF_ACC` 對應之訊號值（是否即 `ACC`，或另有他訊號承載
> 四段式開關之 off&acc 狀態）。
> 影響：引用 `$PowerMode$` 之 in-scope 條文，其 Pre-Condition 無法以
> 單一訊號值表達。

---

## 2. R-VS19 之缺口 —— 上繳 §5 末段指出者成立，補立條文

上繳指出：`$HSW_StatFailSts$` 之值域**全部出自 `[EE Architecture:Atlantis Mid]`
條文，Atlantis High 側無任何值域**；R-VS19 只說「跨架構差異不列為不一致」，
**未說「他架構之值可否取用」**。

該缺口為真。但本例之答案不必動用架構問題：

```
R-VS20（值域來源之階梯，待 Pei 裁）
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
R-VS9(1) 指定），故第二階不引入架構風險；而他架構條文之值域帶有
該架構之假設，取用等同以 CUSW 之行為描述 Atlantis High。

實例：$HSW_StatFailSts$ 於 CFTS044 之 in-scope 無值域（其值僅見於
Atlantis Mid 條文），依本條走第二階 —— 取 LID 表與 DBC 之
`Fail_Not_Present` / `Fail_Present`（二來源一致）。
該 token 之值域**不因 Atlantis Mid 條文而成立，亦不因之而受質疑**。
```

---

## 3. 本輪最弱一環 —— 上繳自評正確，處置如下

上繳 §6.2-3：第三式以**單一錨點**反推，「驗證了式三能抓到該錨點，
未驗證三式已窮盡」。**分析層同意此為本輪最弱一環，且其形態即 §5a 條 12。**

正確之收法不是找第四式，是**餘數驗證**：

```
W-22（餘數驗證，03 輪首項）
對 30 個 token 逐一：

1. 取該 token 在 CFTS044 全文之**全部出現位置**（區分大小寫，token
   兩端即 `$`，無詞界問題）
2. 減去三式各自已命中之位置，得**餘數集合**
3. 逐筆檢視餘數之上下文（前後 200 字元），分類為：
     (a) 敘述性提及，不帶值域
     (b) 帶值域但記法為三式所不涵蓋  ← **即第四式之證據**
     (c) 無法判定
4. 產出 `data/value_extraction_residual.tsv`：
     token / 總出現數 / 式一命中 / 式二命中 / 式三命中 / 餘數 /
     餘數分類計數 / (b) 類之逐筆節錄

通過條件：**(b) 類為 0**，或 (b) 類已全部化為新式並重跑。
**不得以「餘數看起來都是敘述」收尾** —— 須逐筆分類並附計數。

已知量：式一 451／式二 45／式三 34 命中（全 token 合計）。
```

---

## 4. 38 項「值集合不相等」須寫成判準，否則下輪重演

上繳 §6.2-2 自陳：§2.2 之歸因為**人讀分類，未寫成判準**，
下輪重跑會再次全部列出。

```
W-23（歸因判準化）
將 §2.2 之五類歸因寫成可機器判定之規則，套用於 W-19 之輸出：

  C1 別名切分產物 —— CFTS044 值形如 `<全名> / <代碼>`，我方以 ` / `
     切為二值所致。判準：差集之元素為同一原始字串之另一半
  C2 LID 列粒度差 —— LID 該列之 signal 欄含二個以上訊號名
     （如 `FL_HS_STATSts` ＋ `FL_HS_STATFailSts`）
  C3 LID Format 解析殘缺 —— 解析結果之鍵或值含另一訊號名之片段
  C4 規格引用子集 —— CFTS044 側之值集合為他來源之真子集
  C5 縮寫 vs 全名 —— 二值正規化後其一為另一之前綴或首字母縮寫

分類後，**只有不落入 C1–C5 者進入待判清單**。
每輪重跑時，C1–C5 之計數須列出（證明判準仍在運作），
但不逐筆展開。

**C3 為我方缺陷，判準化之同時應修正解析式**，不是長期以分類遮蓋。
```

---

## 5. 三項作業連續兩輪未執行 —— 排程之觀察

`W-15b′`／`W-17`／`W-9` 自 06 包（02 輪）列入，**連續兩輪未執行**。

成因非怠工：兩輪皆有臨時加入之高優先項（W-19／W-20 由 07 包加入），
而該三項排在其後。**但清單若持續在頭部加項，尾部三項會永遠不到。**

```
R-VS21（排程，待 Pei 裁）
一項作業連續兩輪未執行者，下輪**排入頭部**，且該輪不得於其前方
加入新作業。新發現之事項一律登記為 anomaly／DR 並排入其後輪次。

例外：新事項為**阻塞既有作業之前置**時得插隊，惟須於下放包具名
說明其為何是前置。
```

依本條，**04 輪之頭部為 W-15b′／W-17／W-9**，其後才是 W-22／W-23／W-24。

---

## 6. 04 輪作業（順序即優先序）

| # | 作業 | 備註 |
|---|---|---|
| 0 | 開 `docs/upstream/03_*.md`（R-VS18） | 第一個動作 |
| 1 | **W-15b′** DBC ↔ LID 逐屬性交叉 | 連兩輪未執行；收 W-8 盲區 3 |
| 2 | **W-17** LID 列數差 6；`TRUNCATED_ENUM` 其他形態 | 連兩輪未執行 |
| 3 | **W-9** Comfort 逐條對照（母體 237） | 連兩輪未執行；R-VS7 委派句來源 |
| 4 | **W-22** 餘數驗證（§3） | 收本輪最弱一環 |
| 5 | **W-23** 歸因判準化 ＋ 修正 C3 解析式（§4） | |
| 6 | **W-24** `IGN_OFF` 兩處條文是否落在 237 個 Functional leaf 內（§1.1） | 小項 |

**不新增探索性作業。**

---

## 7. 待 Pei

| # | 事項 | 狀態 |
|---|---|---|
| P1 | 刪 `features/vehicle setting/` | **未處理（六輪）** |
| P2 | 入庫 —— 指令草稿已備於上繳 §7 | **未處理（六輪）** |
| P10 | `.gitignore` 加 `!inputs/INPUTS.sha256` | **未處理（六輪）** |
| P11 | 裁 R-VS18／R-VS19 | 未處理 |
| **P12（新）** | 裁 **R-VS20**（值域來源階梯）、**R-VS21**（排程） | 本包提出 |

**R-VS20 阻塞 W-22 之後之任何值域定案**：在其未裁前，
`$HSW_StatFailSts$` 這類「in-scope 無值域」之 token 無合法取值路徑。
本 feature 之 17 個 BLOCKED leaf 之訊號層 ER 依賴該 token。

**P2 仍是最實在的一項**：三輪產物、十九條裁決、四份 data 產出，
目前全部不在版控中。

---

## 8. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS20 | 值域來源之階梯；他架構條文之值域不取用 | ✔ §2 |
| R-VS21 | 連兩輪未執行者排入下輪頭部 | ✔ §5 |
| W-22 | 餘數驗證（作業，非條文） | ✔ §3 |
| W-23 | 歸因判準化（作業，非條文） | ✔ §4 |

兩條條文皆以獨立可貼入之區塊呈現，未夾在敘述中。
