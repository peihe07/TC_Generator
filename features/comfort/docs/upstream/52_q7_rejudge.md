# 52 — Comfort HMI / Q7 以 trigger 重判、CFTS009-010 掃描、25 格逐格閱讀

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 74
- **未生成任何 TC、未修改任何既有 TC、未寫回**；lint **54/54 PASS，383 條**（不變）
- `data/coverage_audit.tsv` 已以新判準重跑（373 列）

---

## 0. 六項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 以 trigger 判準重跑 Q7 全部 373 leaf | ✅ §1 —— **106 → 28 候選，人工判定後 22 應拆** |
| 2 | 唯讀掃描 CFTS009／CFTS010 | ✅ §2 —— **命中 44 處，惟無一涉 comfort 設定之保持** |
| 3 | 7 個缺口記入 DR #17／#31；`047` 併入 RD-1 | ✅ §3 —— **並新增問句 9** |
| 4 | 逐格閱讀 Q1／Q2／Q5／Q6 之 25 格；Q1 增並列名詞候選 | ✅ §4 —— **實為 19 格；新增真缺口 2** |
| 5 | `RUNBOOK` 記「標題數字是 169，可信的數字是 8」 | ✅ |
| 6 | 不生成 TC、不寫回 | ✅ |

---

## 1. Q7 以 trigger 判準重跑

### 1.1 判準之改寫

| | 舊（73 §3 之措辭）| 新（74 §2.3）|
|---|---|---|
| 問 | 兩個獨立之部分失效是否落在同一個 fail 上 | **本 leaf 之 TC 是否涵蓋一個以上之 trigger／input／scope** |
| 讀 | ER 之末行 | **procedure 之動作步驟 ＋ 其對應之 ER 是否斷言後果** |
| 判 | 觀察量之數 | **觸發之數** |

實作上之關鍵一步：**動作步驟只有在其 ER 斷言「後果」時才算 trigger**。
`Turn SYNC on` → `The SYNC button is highlighted` 是**該步自己造成的狀態**，
不是受測需求之後果，故為 setup 而非 trigger。

### 1.2 數量

| | 舊判準 | 新判準 |
|---|---|---|
| 機器判「應拆」 | **106** | **28** |
| 人工判定後 | （已作廢）| **應拆 22、假陽性 5、待裁 1** |

**74 §2 所預期之「遠少於 106」成立。** 且方向與其一致：
**按壓循環類 19 條、`024-02`、`024-03`／`-04`、`110-05` 全部落回「不適用」**
—— 它們都是一次觸發之多個後果。

### 1.3 22 條應拆清單（逐條具名其 trigger）

| leaf | 節 | 觸發 | 型 |
|---|---|---|---|
| `003-06` | 2.3 | A/C／另一氣流模式／風速 —— 三者各自破壞 AUTO | 不同 trigger |
| `010-03`／`112-04` | 2.7／16.7 | 上下鍵／觸碰段／滑動（／硬控）| 不同 input 面 |
| `010-04`／`112-05` | 2.7／16.7 | 畫面風速鍵／硬控／climate power | 不同 trigger |
| `009-05` | 2.6.1 | 滑桿觸點／語音命令 | 不同 input |
| `009-06` | 2.6.1 | 拖曳把手／按壓把手以外之區域（後者應被忽略）| 不同 input |
| `111-03` | 16.6.1 | 箭頭／滑桿拖曳 | 不同 input |
| `111-05` | 16.6.1 | 把手以外之按壓／拖曳把手 | 不同 input |
| `012-05` | 2.8 | AUTO 關 Defrost／Defrost 關 AUTO | 兩個方向＝兩個 trigger |
| `013-03` | 2.9 | AUTO 干擾／FRONT DEF 干擾 | 兩個干擾源 |
| `021-02`／`121-02` | 2.15／16.15 | AUTO 干擾／climate off 干擾 | 同上 |
| `031-01` | 7.3 | LOCK REAR／UNLOCK REAR | 兩個 trigger |
| `032-04` | 7.4 | 改駕駛側溫度／改乘客側溫度 | 兩個 trigger（後者中斷 SYNC）|
| `036-05` | 7.8 | 按壓／長按 | 不同 input |
| `048-03` | 10.5 | 連按 AUTO／改風速／改氣流模式 | 三個 trigger |
| `107-06` | 16.3 | MAX A/C／MAX DEF | 74 §2.2 已裁 ✅ |
| `107-07` | 16.3 | 改氣流模式／改風速 | 兩個 trigger |
| `113-09`／`119-08` | 16.8／16.13 | 改溫度／再按該鍵 | 兩個 trigger |
| `115-05` | 16.10 | REAR DEFROST／heated seat（二者皆不開機）| 兩個 trigger |

**若全數改判：22 條 → 約 52 條（+30 列）。**
`110-01`（English／Metric 兩個 input，74 §2.2 已裁應拆）**未被新判準捕獲** ——
其兩次「Set the temperature units…」之 ER 為狀態確認而非後果，
故判準漏掉它。**已知漏報 1 條，列此以免其消失。**

### 1.4 五個假陽性與一個待裁

| leaf | 判定 | 理由 |
|---|---|---|
| `084`（14.1.1）、`103-02`（14.18）、`106-03`（16.2）、`118-07`（16.12.1）| **不拆** | 其第二個「觸發」是**等待逾時**（`Wait 3 seconds`）—— 逾時是同一次互動之延續，不是另一個觸發 |
| `061-04`（11.7）| **不拆** | 其第一個「觸發」是把座椅關掉以使鍵變灰，屬 setup |
| **`009-03`（2.6.1）：溫度上箭頭／下箭頭** | **待裁** | 同一控制之兩個方向。**與 74 §2.2 裁為不拆之 `023-03`（MODE 控制 UP／DOWN）同型** —— 若 `023-03` 不拆，則本條亦不拆；本層依該前例**暫判不拆**，惟兩者之判準界線請明示 |

### 1.5 一個仍未解決之界線（**本節最重要者**）

74 §2.2 將 `023-01`（tri-mode 三鍵各自 toggle）與 `036-01`（後排三模式）
裁為**維持不拆**，其形態為「一個列舉集合之各項各按一次」。
而本輪之 22 條裡，`013-03`（AUTO 與 FRONT DEF 兩個干擾源）判為**應拆**。

> **兩者之外觀相同：對同一個受測物，依序施加集合中的每一個成員。**
> 其分野只能是：`023-01` 之集合是**該需求本身所列舉者**（「三個鍵各自獨立」
> 即需求），而 `013-03` 之兩個干擾源是**我們挑的例子**（條文只說
> 「independent of any other climate functions」）。
>
> **若此分野成立，則「條文列舉之集合」不拆、「我方選樣之集合」應拆。**
> 該判準本層未見於任何條文，故不自行採用為通則 —— **請裁**。

---

## 2. CFTS009／CFTS010 唯讀掃描（74 §3.1）

**方法**：讀 SYS.2 之兩份 Polarion 匯出 xlsx（**未動 `features/power/` 任何檔案**，
亦未寫入任何檔案）：

- `CFTS_009_Wake_Up_Power_UP/SYS2_CFTS_009_…_04_13_2026.xlsx`（3 sheets，11,772 個文字格）
- `CFTS_010_Power_Down/SYS2_CFTS_010_…_04_13_2026.xlsx`（3 sheets，1,425 個文字格）

pattern：`comfort|climate|HVAC|seat|retain|restore|last state`（大小寫不敏感）。

### 2.1 命中：**CFTS009 41 處、CFTS010 3 處**

| 類 | 例（節錄）|
|---|---|
| **climate pop-up 於 IDLE 狀態**（CFTS009）| `The HU shall display climate pop-ups during IDLE mode, the HU shall turn on the backlight in order to display them`／`Disclaimer screen can be temporarily skipped for … climate pop-ups …` |
| **HVAC 於 power-down 狀態仍作用**（CFTS010）| `Minimize current consumption while keeping: Display ON, HVAC controls active, Phone active for ACN` |
| **restore（15 處）** | 全數為 **audio source／TLM 設定**：`restore last active source before phone call`、`restore Auto_SwitchOn_Setting.Req to the previous value`、`restore the last user settings and the last variables values`（TLM 之變數）|
| **seat（8 處）** | 全數為 **settings seat graphic**（依 PROXI／車型選圖），與座椅加熱狀態無關 |

### 2.2 判定：**無**

> 該二 spec **確有 comfort 相關之條文**，惟其所管者為
> **「電源狀態下 climate 介面是否仍運作」**（IDLE 顯示 pop-up、power-down 保持
> HVAC 控制可用），**不是「使用者設定是否被保留」**。
> 其 `restore` 條款逐條具名 audio 與 TLM 之變數，**沒有一條提到氣候或座椅設定**。

依 74 §3.1 之分支二：**加入 RD-1 為第 9 個問句**，一句、不列 222 條、阻塞數 0。
**並記其已查證之部分**（見 §3.2），使上游知道我們問之前查過哪裡。

---

## 3. 缺口之歸位

### 3.1 7 個缺口記入 DR #17／#31

| DR | 增記 |
|---|---|
| **#17**（tab 集合）| 本項亦使已產出之 `001-03` 缺其反向側：`If only Front climate is available … the tabs will not be displayed` 之否定側與 `up to 4 tabs` 之計數上限皆無 TC。**該二反向 TC 於解答後與 `001-01`／`-02` 一併生成，不另立項** |
| **#31**（4 模式配置）| 本項亦使 5 個已產出之 leaf 缺其反向側：`017-01`／`017-02`（5 狀態）與 `023-01`～`023-03`（tri-mode 三鍵）之反向側即 4 模式配置。**該五條之反向 TC 於解答後與 `016`／`018` 系列一併生成，不另立項** |

### 3.2 RD-1 新增兩個問句

| # | 問句 | 阻塞 |
|---|---|---|
| **8** | **When is AUTO unavailable?**（`047`／10.4）—— 條文以 `and available` 為前件而全 129 節未定義其反面 | **1** |
| **9** | **Which document defines whether comfort settings survive an ignition cycle?** | **0** |

問句 9 之措辭載明我們查過哪裡（逐字）：

> We checked the power-management specifications (CFTS009 Wake-up and
> Power-up, CFTS010 Power Down) before asking. They state that climate
> pop-ups are shown and HVAC controls stay active in certain power states,
> and they require the restoring of *audio and telematics* settings by name —
> **but they say nothing about retaining climate or seat settings**.

RD-1 之總計由 25 改為 **26**（問句 9 不阻塞任何 leaf，於表內明記）。

---

## 4. Q1／Q2／Q5／Q6 之逐格閱讀

### 4.1 實為 **19 格**（非 25）

74 §5 稱 25 格；扣除本層已於上繳 51 §2 複核並列表者（`2.1`×2、`2.12.1`×2、
`3.1`×3、`10.4`、`2.14`、`10.2`、`17.1`×3、`7.1`×3、`7.3`×3、`2.7.1`、`2.10`×6、`11.6`×2）
後，**尚未閱讀者為 19 格**。全部已讀。

### 4.2 結果：**真缺口 2、假陽性 17**

| 格 | 判定 | 理由 |
|---|---|---|
| **`105-01`／`105-02`（15.1，concurrency）** | ✅ **真缺口** | 條文為 `when a user **enters** (starts a function) **or exits** (breaks a function) that function`，**兩條 TC 皆只驗「進入」**（開 FRONT DEF），**離開側無 TC** |
| `079-01`／`-02`（13.3.1）| ❌ | `during a keycycle` 屬保持而非並行，TC 已跑 keycycle |
| `085`（14.2）／`092`（14.9）／`094`（14.10.1）／`095-01`／`-02`（14.11）| ❌ | 其 TC 正是「RVC 作用中／intro 動畫中／idle 模式中／點火循環中」之案例 —— 判準未辨識該措辭 |
| `117-01`～`-03`（16.12，boundary ＋ concurrency 共 6 格）| ❌ | `Only one … at a time` 已由 `117-01` 驗（Feet 作用且 Face 不作用）|
| `120-03`（16.14）| ❌ | `120-02`／`-03` 本身即否定式 ER |
| `123`（16.17）| ❌ | ER 為「fan speed indicator is unchanged」，即該否定側 |
| **`127-01`／`-02`（17.4，boundary）** | ❌ **且為判準之瑕疵** | 「限值 `4/10`」實為正規式 `\\d+/\\d+` 誤命中**螢幕尺寸字串 `8.4/10.1/12`** |

**真缺口累計：8（51 §2）＋ 2（本節）＝ 10。**

### 4.3 Q1 之並列名詞候選產生器

新增規則：節之條文含**逗號分隔之三項以上並列名詞**者，亦為列舉句候選。

| | 值 |
|---|---|
| 現行詞集未命中而並列規則命中之**節** | **29** |
| 其所涉之 leaf（Q1 現為「不適用」）| **101** |

**惟逐句讀其片段後，其中真為「支援項／有效值之列舉」者僅 7 節**：
`2.5.1`（Auto, Manual, Open）、`9.2`（level number, AUTO, OFF）、
`13.2.1`（四個腰靠選項）、`14.3`／`14.13`（三類 popup）、
`16.4`（五個按鍵之 on/off）、`17.2`（widget 內容）。

其餘 22 節之並列為**受影響項之列舉**（`AUTO affects Fan speed, Modes, AC`）
或**後果之列舉**（`the button is no longer highlighted, and 3 arrows are shown`）
—— **不是「支援項」，不觸發 §7**。

> 換言之：**新規則之召回率提高，代價是約 75% 之誤報**。
> 本層**未**把 101 個 leaf 改判為 Q1 候選，只回報其數與其中 7 節之名單。
> 該 7 節之反向配對是否齊備，**本輪未逐條判**（下一步）。

---

## 5. 「本包是否仍有該驗而未驗者」（R-C30）

1. **§1.3 之 22 條為人工判定，其判準界線未定**（§1.5）——
   若「條文列舉之集合不拆／我方選樣之集合應拆」不成立，
   則 `013-03`／`021-02`／`121-02` 三條之判定會反轉。
2. **`110-01` 之漏報已具名**（§1.3 末）；同型（兩次設定不同 input 而 ER 為狀態確認）
   **未全面掃描**，故漏報數 ≥1 而非 =1。
3. **§2 之掃描為關鍵詞**，其 pattern 由 74 §3.1 指定；
   **若該二 spec 以別的詞述及氣候設定之保持（如 `HVAC settings`、`user profile`），
   本掃描看不到**。已試 `retain|restore|last state` 三詞，命中皆非氣候。
4. **§4.3 之 7 節未逐條判其反向配對**，只回報節名。
5. **Q3／Q4 之 222 個「無明文」未複核**（其判準 `stateful` 偏寬，51 §6.3 已記）——
   問句 9 以「222」為其規模陳述，**該數字是上限**。

---

## 6. 待分析層

1. **§1.5 之判準界線** —— 「條文列舉之集合」vs「我方選樣之集合」，請裁。
   其影響及於 `013-03`／`021-02`／`121-02`／`009-03`／`023-01`／`023-03`／`036-01`。
2. **§1.3 之 22 條是否改判** —— 若是，本層需一輪重生成（22 → 約 52 條，+30 列）
   並重跑寫回。
3. **§4.2 之 `105-01`／`105-02`（15.1 之「離開」側）** —— 應補 TC 抑或另有處置。
4. **§4.3 之 7 節**（真列舉）—— 是否逐條判其 §7 反向配對。
5. **RD-1 問句 8／9 之措辭**請覆核（已寫入草案，仍未送出）。
