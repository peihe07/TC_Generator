# 上繳包 16：PM 全面改寫（軌 A 套用 ＋ 軌 B 改寫）

下放：`docs/fw036/handoff/16_pm_full_rewrite.md`（附件 A–F）
日期：2026-08-21　　**止於工作副本，未送達、未覆寫交付本。**

| 項 | 值 |
|---|---|
| 來源工作副本 | `features/power/sandbox/b10/pm_10a5b.xlsx`（SHA256 `94419a2f4186f25ab4bc…`） |
| 產出工作副本 | `features/power/sandbox/b16/pm_16.xlsx`（SHA256 `6c849fef89dc9064670d…`） |
| 寫回路徑 | `features/power/scripts/b16/apply.py` —— `surgical_save` 唯一路徑 |
| 驗收腳本 | `features/power/scripts/b16/verify.py` |
| 改動列數 | **253**（軌 A 56 ＋ 軌 B 197）；軌 C 30 列零變動 |
| 改動格數 | 四欄 1,012 格 ＋ `test_item` 不可見字元 163 格 |

---

## 一、範圍與分工實況

| 軌 | 列 | 來源 | 本包處置 |
|---|---:|---|---|
| A | 56（rows 10–65） | 附件 A–E 已逐列寫全 | **逐字套用**（一處訂正，見 §五） |
| B | 197 | 無既成文字 | **本包改寫**（下表逐列） |
| C | 30 | 分析層進行中 | **未動**（實測四欄零變動） |

軌 C 之 30 列：124–127、149、181、233、234、265–282、289–291、293。
`verify.py` 之 `軌 C 四欄變動列: []` 為其證明。

---

## 二、軌 B 197 列改動清單

處置代碼：
`T` 工具行改 `LIN and CAN tool is available on HU` 並移至 PC 末項（R-12(a)）／
`S` 內部訊號改可觀察 CAN 訊號（R-1 v3(d)）／
`V` `Send CAN:` 或三件組改 v3 `$MESSAGE.Signal$`（R-1 v3(a)）／
`I` Input 內聯後改 `NA`（R-11(c)）／
`X` 一觀察點一步驟之拆步（R-11(a)）／
`R` `Read` 補寫應觀察之值（R-11(b)）／
`N` PC 未編號行補編號（R-9(a)）／
`P` 含 `PENDING: DR-PW20`

分布：`T` 166、`R` 150、`X` 124、`I` 85、`S` 63、`V` 22、`P` 4、**`N` 0**。
`N` 為 0 係因 13 包所載之 23 列未編號 PC（rows 10–32 連續段）**全部落在軌 A**，
軌 B 之 PC 本已逐行編號 —— 此點於下放時未區分，於此登記。

PROC 步數合計 **422 → 606**（+184），即 R-11(a)(b) 之拆步與補值所致。
Input 原帶內容者 **85 列**，全數內聯後為 `NA`。

| 列 | TC ID | 步數 | 處置 |
|---:|---|---|---|
| 66 | 057 | 3→4 | TSVX |
| 67 | 058 | 3→5 | TSVXR |
| 68 | 059 | 2→3 | TSXR |
| 69 | 060 | 2→2 | TSR |
| 70 | 061 | 2→2 | TS |
| 71 | 062 | 2→3 | TSXR |
| 72 | 063 | 2→3 | TSIXR |
| 73 | 064 | 2→3 | TSXRP |
| 74 | 065 | 2→4 | TSXRP |
| 75 | 066 | 2→2 | TS |
| 76 | 067 | 2→2 | TSR |
| 77 | 068 | 2→2 | TS |
| 78 | 069 | 2→3 | TSXR |
| 79 | 070 | 3→3 | TSV |
| 80 | 071 | 2→2 | TSR |
| 81 | 072 | 2→2 | TS |
| 82 | 073 | 3→4 | TSVXR |
| 83 | 074 | 2→3 | TSVXR |
| 84 | 075 | 2→2 | TSV |
| 85 | 076 | 2→2 | TSV |
| 86 | 077 | 2→2 | TSV |
| 87 | 078 | 2→3 | TXR |
| 88 | 079 | 2→4 | TX |
| 89 | 080 | 3→3 | TSR |
| 90 | 081 | 2→4 | TXR |
| 91 | 082 | 2→4 | TXR |
| 92 | 083 | 3→3 | TSR |
| 93 | 084 | 2→4 | TXR |
| 94 | 085 | 2→4 | TXR |
| 95 | 086 | 2→3 | TXR |
| 96 | 087 | 2→3 | TXR |
| 97 | 088 | 2→5 | TSX |
| 98 | 089 | 3→3 | TSVR |
| 99 | 090 | 2→2 | TSIR |
| 100 | 091 | 2→2 | TSIR |
| 101 | 092 | 2→3 | TSXR |
| 102 | 093 | 2→5 | TSXR |
| 103 | 094 | 2→4 | TSXR |
| 104 | 095 | 2→3 | TSXR |
| 105 | 096 | 2→3 | TSXR |
| 106 | 097 | 3→5 | TSVXR |
| 107 | 098 | 2→3 | TSXR |
| 108 | 099 | 2→4 | SXR |
| 109 | 100 | 3→5 | XR |
| 110 | 101 | 2→3 | X |
| 111 | 102 | 2→2 | SR |
| 112 | 103 | 2→3 | SXR |
| 113 | 104 | 2→2 | SR |
| 114 | 105 | 2→3 | SXR |
| 115 | 106 | 2→3 | IX |
| 116 | 107 | 2→2 | SR |
| 117 | 108 | 2→3 | SXR |
| 118 | 109 | 2→3 | IX |
| 119 | 110 | 2→2 | TSRP |
| 120 | 111 | 2→2 | TSR |
| 121 | 112 | 2→2 | TSR |
| 122 | 113 | 2→3 | TXR |
| 123 | 114 | 2→3 | TXR |
| 128 | 119 | 2→2 | T |
| 129 | 120 | 2→3 | TXR |
| 130 | 121 | 2→3 | TSXR |
| 131 | 122 | 2→3 | TSXR |
| 132 | 123 | 3→4 | TSVXR |
| 133 | 124 | 3→4 | TSVXR |
| 134 | 125 | 2→4 | TSXR |
| 135 | 126 | 2→4 | TSXR |
| 136 | 127 | 2→3 | TXR |
| 137 | 128 | 2→3 | TXR |
| 138 | 129 | 2→4 | TSXR |
| 139 | 130 | 2→4 | TSXR |
| 140 | 131 | 2→3 | TSXR |
| 141 | 132 | 2→3 | TSXR |
| 142 | 133 | 2→2 | TSR |
| 143 | 134 | 2→2 | TSR |
| 144 | 135 | 2→2 | TR |
| 145 | 136 | 2→4 | TSXR |
| 146 | 137 | 2→3 | TSXR |
| 147 | 138 | 2→4 | TSXR |
| 148 | 139 | 2→4 | TSXR |
| 150 | 141 | 2→3 | TIXR |
| 151 | 142 | 2→3 | TIXR |
| 152 | 143 | 2→3 | TIXR |
| 153 | 144 | 2→3 | TIXR |
| 154 | 145 | 2→2 | TIR |
| 155 | 146 | 2→2 | TIR |
| 156 | 147 | 2→3 | TIXR |
| 157 | 148 | 3→6 | XR |
| 158 | 149 | 3→6 | XR |
| 159 | 150 | 3→6 | XR |
| 160 | 151 | 2→3 | TXR |
| 161 | 152 | 2→3 | TSIXR |
| 162 | 153 | 2→6 | TSIXR |
| 163 | 154 | 2→3 | X |
| 164 | 155 | 2→3 | X |
| 165 | 156 | 2→4 | X |
| 166 | 157 | 2→4 | X |
| 167 | 158 | 3→4 | XR |
| 168 | 159 | 3→4 | XR |
| 169 | 160 | 3→4 | XR |
| 170 | 161 | 3→5 | X |
| 171 | 162 | 2→2 | I |
| 172 | 163 | 2→2 |  |
| 173 | 164 | 2→3 | X |
| 174 | 165 | 2→3 | X |
| 175 | 166 | 2→3 | TIX |
| 176 | 167 | 2→3 | TIX |
| 177 | 168 | 2→3 | TIX |
| 178 | 169 | 2→3 | TIX |
| 179 | 170 | 2→4 | TIXR |
| 180 | 171 | 2→4 | TIXR |
| 182 | 173 | 2→3 | X |
| 183 | 174 | 2→3 | X |
| 184 | 175 | 2→3 | X |
| 185 | 176 | 2→3 | X |
| 186 | 177 | 3→3 | I |
| 187 | 178 | 3→7 | TVIXR |
| 188 | 179 | 3→6 | TXR |
| 189 | 180 | 3→8 | TVIXR |
| 190 | 181 | 2→5 | TVIX |
| 191 | 182 | 3→5 | TVIX |
| 192 | 183 | 2→3 | TVIX |
| 193 | 184 | 2→2 | TV |
| 194 | 185 | 3→8 | TVIXR |
| 195 | 186 | 3→4 | TVIX |
| 196 | 187 | 3→6 | TVIX |
| 197 | 188 | 3→5 | TVIX |
| 198 | 189 | 2→3 | TIXR |
| 199 | 190 | 2→3 | TIXR |
| 200 | 191 | 2→3 | TIXR |
| 201 | 192 | 2→3 | TXR |
| 202 | 193 | 2→3 | TXR |
| 203 | 194 | 2→2 | TIR |
| 204 | 195 | 3→5 | TIXR |
| 205 | 196 | 2→2 | TI |
| 206 | 197 | 2→2 | TIR |
| 207 | 198 | 2→2 | TIR |
| 208 | 199 | 2→2 | TIR |
| 209 | 200 | 2→2 | TIR |
| 210 | 201 | 2→2 | TR |
| 211 | 202 | 2→3 | TIXR |
| 212 | 203 | 2→2 | TIR |
| 213 | 204 | 2→2 | TIR |
| 214 | 205 | 2→2 | TIR |
| 215 | 206 | 2→2 | TIR |
| 216 | 207 | 2→2 | TIR |
| 217 | 208 | 2→2 | TIR |
| 218 | 209 | 2→2 | TIR |
| 219 | 210 | 2→2 | TIR |
| 220 | 211 | 2→2 | TIR |
| 221 | 212 | 2→2 | TIR |
| 222 | 213 | 2→2 | TIR |
| 223 | 214 | 2→2 | TIR |
| 224 | 215 | 2→2 | TIR |
| 225 | 216 | 2→2 | TR |
| 226 | 217 | 2→3 | TIXR |
| 227 | 218 | 2→2 | TIR |
| 228 | 219 | 2→2 | TIR |
| 229 | 220 | 2→2 | TIR |
| 231 | 221 | 2→2 | TIR |
| 232 | 222 | 2→2 | TIR |
| 235 | 225 | 2→2 | TIR |
| 236 | 226 | 2→2 | TIR |
| 237 | 227 | 2→2 | TIR |
| 238 | 228 | 2→2 | TI |
| 239 | 229 | 2→3 | TIXR |
| 240 | 230 | 2→3 | TIXR |
| 241 | 231 | 2→3 | TIXR |
| 242 | 232 | 2→3 | TIX |
| 243 | 233 | 2→4 | TXR |
| 244 | 234 | 2→3 | TXR |
| 245 | 235 | 2→3 | TSXRP |
| 246 | 236 | 2→2 | TIR |
| 247 | 237 | 2→2 | TIR |
| 248 | 238 | 2→2 | TIR |
| 249 | 239 | 2→2 | TIR |
| 250 | 240 | 2→3 | TXR |
| 251 | 241 | 2→3 | TXR |
| 252 | 242 | 2→3 | TIXR |
| 253 | 243 | 2→3 | TXR |
| 254 | 244 | 2→3 | TXR |
| 255 | 245 | 2→3 | TIX |
| 256 | 246 | 2→3 | TX |
| 257 | 247 | 2→3 | TIX |
| 258 | 248 | 2→3 | TXR |
| 259 | 249 | 2→3 | TIXR |
| 260 | 250 | 2→3 | TIXR |
| 261 | 251 | 2→3 | TIXR |
| 262 | 252 | 2→3 | TIXR |
| 263 | 253 | 2→2 | TIR |
| 264 | 254 | 2→2 | TIR |
| 283 | 273 | 2→2 | TIR |
| 284 | 274 | 2→2 | TIR |
| 285 | 275 | 2→6 | TXR |
| 286 | 276 | 2→2 | TR |
| 287 | 277 | 2→2 | TR |
| 288 | 278 | 2→2 | TR |
| 292 | 282 | 2→3 | TIX |

---

## 三、`PENDING: DR-PW20` 之四列與逐列理由

**DR-PW20（本包新開）**：*轉態之目標值於 CFTS009／010 原文僅載為
「另一個值」「不同於 SNA 之值」一類之類別，未載具體值。*

| 列 | TC ID | 原文所載 | 何以不得填值 |
|---|---|---|---|
| 73 | -064 | `LTM_OperationalModeSts.Info has a transition from "Ignition Off" to another value` | 「another value」為 `OperationalModeSts` 之 15 個非 `2` 值之任一；擇其一即為依情境推定（路線 (c) 所禁） |
| 74 | -065 | 同 73（另加 `RemStActvSts == Remote Start Not Active` 條件） | 同上 |
| 119 | -110 | `IF TLM receives LTM_OperationalModeSts.Info equal to "SNA" ... THEN TLM has to behave as an Ignition Pre Off or Ignition Off event occurs` | 送出值 `15 (SNA)` 明載可填；**結果之 `PowerSts_Telematic` 值**未載，須跨章引「TLM Operative state management」始能得出，屬跨 clause 推定 |
| 245 | -235 | `As soon as LTM_OperationalModeSts.Info becomes different from "SNA" value again` | 「different from SNA」同 73 之類別式，具體值未載 |

四列之 PC 與 ER 其餘各項皆已完成；僅該一格待值。
`lint036` 之 M 檢查對 `PENDING:` 免計，故 M=0 不受影響。

---

## 四、lint 前後

| | A | B | C | D | E | F | G | H | I | I-sib | J | K | L | M | N | P |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 前（pm_10a5b） | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **23** |
| 後（pm_16） | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |

**E 為 0**（PROC↔ER 編號數逐列相等）。

P 之 23 → 10：消去者為 `input` 欄之 13 筆（Input 內聯後全為 `NA`）。
**殘存 10 筆全部落在 `test_item` 括號下半**（rows 57、59 等之
`Radio_btn0 in CLIMATIC_PANEL on BH-CAN` 三件組），**本包依下放明令不動該半**，
故四個作者欄之 P 為 **0**。

> ⚠ **lint P 仍為 R-1 v2 判準，未依 09 包 §四／12 包改寫。**
> 本包未改 `scripts/lint036.py` —— 該檔為八本共用，改之即動及其餘七本
> 之報告基線，逾本包範圍。**具體待辦**：(a) P 之
> 「Procedure 之 CAN 賦值行缺 `Send CAN:` 前綴」須改為認可 v3 之
> `Send the signal $MESSAGE.Signal$ = <raw> (<label>)`；(b) 13 包所立之
> **檢查 Q**（不可見字元）與 **檢查 R**（PC 編號／並列）尚未進 lint。
> 本包以 `verify.py` 代行 (a)(b) 之判定，見 §五。

---

## 五、驗收（`verify.py`，改動範圍 253 列）

```
[OK] input_not_na: 0          [OK] listed_in_input: 0
[OK] triplet: 0               [OK] send_can: 0
[OK] pre_unnumbered: 0        [OK] pre_multi: 0
[OK] pre_first_is_tool: 0     [OK] pre_last_not_tool: 0
[OK] step_multi_obs: 0        [OK] read_without_value: 0
[OK] nbsp: 0                  [OK] proc_er_mismatch: 0
```

全 283 列口徑下之 FAIL 全部落在軌 C 之 30 列
（`input_not_na` 9、`listed_in_input` 9、`pre_last_not_tool` 30、
`step_multi_obs` 14、`read_without_value` 21）——**即未改之列**，
非本包遺漏。

**附件 A 之一處訂正（row 17）**：附件 A 之 row 17 PROC 第 1 步作
`Send CAN: STATUS_BH_BCM2.RemStActvSts = 1 (Remote Start Active)`（R-1 v2 舊式），
而 rows 41–44 之同一動作皆已作 v3 `Send the signal $STATUS_BH_BCM2.RemStActvSts$ = …`。
下放之驗收明列「`Send CAN:` 舊式 = 0」，二者不可並存。
**執行層依 R-1 v3(a) 與該驗收條，將 row 17 統一為 v3 式**，
ER 側原已為 v3、未動。**此為對「逐字可貼」之唯一偏離，請分析層追認。**

### 下拉（x14）讀回

```
Product Document 記錄封面頁: 1 個 DV
Test Case Specification&Result: 3 個 DV
```
`surgical_save` 回報 `dv: {'…sheet5.xml': (1, 0), '…sheet6.xml': (3, 1)}`，
差異成員僅 `xl/worksheets/sheet6.xml`，壓縮成員 42 個未變。

---

## 六、diff 證明（僅四欄）

| 欄 | 變動格數 | 說明 |
|---|---:|---|
| `test_item`（I） | 163 | **僅不可見字元**（NBSP／全形空格／行尾空白，R-10(a)）。`strip_invisible(before) == after` 逐列成立，**內容變動 0** |
| `pre`（J） | 253 | 本包改寫 |
| `input`（K） | 92 | 內聯後改 `NA`（其餘列原已為 `NA`） |
| `proc`（L） | 253 | 本包改寫 |
| `er`（M） | 247 | 本包改寫；6 列（128、246–249、286）改寫後與原文逐字相同，故不計入 |
| `spec_reference`（N） | **0** | 零變動 |
| 其餘各欄 | 0 | 零變動 |

`test_item` 之引號、方括號、行尾句號、破折號**一律未動**（R-10(c)）。

---

## 七、本包是否仍有該驗而未驗者 —— 執行層獨立判斷

**有，六項。**

1. **lint P／Q／R 未依 09、12、13 包改寫**（§四）。現行 lint 之 P 判準
   與 R-1 v3 相牴觸；本包以 `verify.py` 代行，**但 `verify.py` 非共用閘**，
   下一包若換人執行即失去該保障。
2. **「一步一觀察點」與「Read 須寫值」之判定為啟發式**。
   `verify.py` 以「`Read <對象> and check that …`，對象內不得含 `,`／` and `」
   為準；語意上仍可能有一步兩觀察而未被字面命中者，未逐列人工複核。
3. **`PowerModeSts_Telematic`（row 72）之 DBC 對應未經裁決。**
   BH-CAN DBC 有 `STATUS_BH_BCM1.PowerModeSts`，其
   `VAL_ 0 Standard_Power／1 Logistic_Mode_ON` 與原文之值**逐字相符**，
   然訊號名多一 `_Telematic` 尾綴。12 包 §三之對照表僅裁 `TLM_Status.Info`
   與 `LTM_OperationalModeSts.Info` 二者。**本包不逕自對應**，
   row 72 維持來源名 `PowerModeSts_Telematic`，值則逐字取自來源。
   **請分析層裁定是否併入對照表。**
4. **11 種未解析內部訊號沿用附件 A 之作法**（`Front_Panel_OnOff.Req`、
   `Phone_Call.Info`、`Antitheft_*` 等保留來源名）。12 包 §二(d) 之條文為
   「查無對應者**不得留內部訊號名**，改以 HMI／實體可觀察現象書寫」——
   **附件 A 之 56 列並未如此，本包為一致性從之**。二者不合，須擇一。
5. **row 186 移除了兩個非來源值。** 原 Input 載
   `Event burst: 20 events injected at 100 ms intervals`，而錨點原文僅載
   「Any event occurring during the boot」。依路線 (c)，本包改寫為不帶數值之
   「inject events … while the boot is still completing」。
   **此為刪去既有之推定值，非新增** —— 但確係對既有內容之實質變更，於此明列。
6. **`$Radio_Theme$`／`$Day_Night_Mode$`／`$Themed_Sound$` 等未查得所屬 message**，
   維持來源之 `$Signal$` 單名式，未寫成 v3 之 `$MESSAGE.Signal$`。
   其 message 歸屬未經查證，故不補。

另二項為**已知且非本包所生**：
- 軌 C 30 列仍為舊式（分析層進行中）。
- `test_item` 括號下半之 10 筆三件組殘留（下放明令不動）。

---

## 八、引用之裁決編號

R-1 v2（09 包）、**R-1 v3（12 包，現行）**、R-6／R-6b、R-7、
**R-8**（spec_reference 一值一行）、**R-9**（PC 一條件一行一編號）、
**R-10(a)(b)(c)**（空白與字元正規化之分區）、
**R-11(a)(b)(c)**（一觀察點一步驟／須寫值／Input 一律 NA）、
**R-12(a)**（PC 句式與排序、工具行置末）、R-12(b)（本包不涉，spec_ref 已撤）、
R-TM13（撤銷不刪除）、R-P310(三)（寫回後驗證）、R-P96（往返索引）。

**撤銷／已解除者**：R-1 v1 三件組、v2(c) 之 PROXI 加 `$`、
M16-PM 與 DR-PW19（spec_ref 凍結，已撤）、A-PM09（已撤）。

**本包新開**：**DR-PW20**（轉態目標值未載於原文，阻斷 4 列之一格）。

---

## 九、未做之事

- 未送達客戶目錄、未覆寫任何交付本、未改 `output/`。
- 未改 `scripts/lint036.py`（理由見 §四）。
- 未改 `test_item` 括號下半、未改 `spec_reference`、未改軌 C。
- 未增列、未刪列、未拆列。
