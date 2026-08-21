# 下放包 05：PM 第二批（M17 禁用動詞 20 列 + DR-PW12 增列）

承批 1（已通過覆核，見 03／04）。PM 一次修足再寫回，避免二次交付。
基底：**批 1 之工作副本** `features/power/sandbox/b02/pm_remediated.xlsx`
（非交付本原檔）。新規 0 條。

## 一、M17：A 禁用動詞 20 列（canon §5.1）

命中全集（行計 20 = 列計 20，每列各 1 行，皆位於 `proc`）：

**型 A —— `to check whether` 目的子句（18 列）**
rows 15、86、128、178、205、238、242、255、256、257、275–281、292

§5.1 之 `verify` 例外明訂為 `... to verify **that** ...`。
`whether` 為疑問補語，將判準推給測試者，`that` 為斷言補語。
**修法：`to check whether` → `to check that`，並依該列 ER 之實際
極性調整述語**，不得機械替換。

已核對之 ER 極性（分析層實測，全 18 列皆為肯定式，無否定分支）：

| 列 | 現行 | 依 ER 應改為 |
|---|---|---|
| 15 | to check whether the images are provided | to check that the images are provided |
| 86 | …whether the transition of this clause occurs | …that the transition occurs |
| 128 | …whether it stays off | …that the backlight is off |
| 178、292 | …whether the disclaimer appears | …that the disclaimer appears |
| 205 | …whether a reset occurs | …that a reset occurs |
| 238、242 | …whether an animation is played | …that the animation is played |
| 255–257 | …whether a new day is granted | …that a startup sound accompanies the animation |
| 275–281 | …whether the startup screens appear | …that the disclaimer and splash screen are skipped |

⚠ rows 255–257 與 275–281 之現行述語與其 ER **語意相反或不對應**
（ER 為「skipped」而 proc 問「appear」）。改寫須以 ER 為準，
上表已據 ER 逐列給定。

**型 B —— `Observe` 作主動詞（2 列）**
rows 210、225，逐字相同：`1. Observe the bus traffic while the CAN
network stays awake`。ER 為 `The HU sends $Radio_Theme$ on the bus`。
**修法**：`1. Read the bus traffic while the CAN network stays awake
and record the $Radio_Theme$ message`（§5.1 preferred verb `Read`／
`Record` + 具體可觀察標的）。

**不得順帶改動**：該 20 列之 step 2 以外行、ER 欄、test_item 欄。

## 二、DR-PW12 增列（不新開 DR）

批 1 覆核發現**第六對**同型情形，不在 DR-PW12 現載五對之內：

```
【批 1 覆核增列】第六對：`SWE-PM-080` ≡ `SWE-PM-086`。
工作簿 rows 210/225（TC `PowerManagement-201`/`216`）與
rows 211/226（TC `-202`/`-217`）之 test_item 上半、括號下半、
pre／input／proc／er 四欄**逐字全同**，僅 Requirement ID 與
row210 之 Priority（P0 vs P1）相異。依 §8.2.1 不得由 TC 側合併或
刪列 —— 刪任一側將使該 leaf 失去覆蓋。TC 側維持現狀，待上游答覆。
（分析層 04 包覆核；原登記編號 A-PM04 撤銷，併入本 DR。）
```

寫入 `features/power/DATA_REQUESTS.md` 之 DR-PW12 列末，
比照該檔既有增列格式（如 R-P270(b)）。**不改 Urgency、不改編號。**

## 三、驗收

- lint036 對修後工作副本：**A = 0**（前 20）
- **不得變動**：B0 C2 D0 E0 F0 G0 H0 I0 I-sib0 J0 K0 L0 M0 N0 P0
  （批 1 完成後之值，見上繳 02 §1）
- 逐格 diff：變動格數 = 20，皆於 `proc` 欄；非目標欄零變動
- x14 下拉讀回驗證；`surgical_save` 唯一寫入路徑
- 抽驗：255–257、275–281 兩組共 10 列逐列確認改寫後與 ER 對應

## 四、上繳

`docs/fw036/upstream/05_pm_batch2.md`：改動列清單、lint 前後、
diff 證明、DR-PW12 增列後之該列全文、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。

## 五、完成後 Pei 動作（勿代執行）

PM 至此四項回修完成（M3／M15／M10／M11／M17）。
```bash
cp "features/power/sandbox/b02/<最終副本>" "/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Power Management/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260821(Revise).xlsx"
shasum -a 256 "<寫回檔>" >> <LEDGER>
```
ChangeHistory 增列：
`M3/M15/M10/M11/M17: signal notation (R-1), sibling tokens (S4),
test_item excerpt (R-3), capitalization (R-4), forbidden verbs (§5.1)`

**PM 未結項（不阻塞本次交付）**：M16-PM（spec_reference 283 列
R-2 遷移，需先建 SWE-PM→ObjectID 對照表）、DR-PW12 等 12 項 live DR。
