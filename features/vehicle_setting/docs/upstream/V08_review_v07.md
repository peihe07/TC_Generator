# 上繳 V08 —— R-VF10–13 補落、覆寫層、34 leaf 結案

執行層寫入。依據：`docs/handoff/V08_review_v07.md` §6（3 項工單）＋ §2–§4 之
R-VF20／21／22。canon §8.2 六節。

**本輪未生成 TC、未寫回工作簿、未改 `writability_driver.py`。**

---

## 1. 交付總表

| 項 | 狀態 | 產物 |
|---|---|---|
| W-VF21 補落 R-VF10–13 ＋ 複驗 R-VF17 | **完成** | `RULINGS.md`；本檔 §2–§4 |
| W-VF22 34 leaf 查明 | **完成（結案）** | 本檔 §5；A-VF5 |
| W-VF23 覆寫層 ＋ 可失敗性實測 | **完成** | `scripts/grade_overrides.py`、`data/grade_overrides.tsv`、`RUNBOOK.md`／`PLAYBOOK.md` |
| R-VF22 之兩項准改 | **已施行** | `feature.yaml:29`、`scripts/vf230_layer2.py:113` |
| 條文落檔 | **完成** | +R-VF10／11／12／13（補）／20／21／22 |
| anomaly | **完成** | +A-VF5（結案） |

---

## 2. W-VF21(1) —— R-VF10–R-VF13 已補落

四條皆自 V04 §2／§4、V05 §2／§3 之 ``` 區塊**逐字**取出（以程式取，不轉錄）。
R-VF14–R-VF19 經查**均已在檔**，無遺漏。現 `RULINGS.md` 含 R-VF10–R-VF22 全 13 條。

**補落時具名之三項現況**：

1. **R-VF10 之檔名一項現況未遵行** —— repo 已收斂於 `docs/upstream/vf230/{NN}_`
   （4 檔），本線之 V06／V07／V08 為 `V{NN}_` 平鋪（3 檔）。V08 §5.1 已建議
   修訂本條，待裁。**本層未動任何檔名。**
2. **R-VF10 所令之 `ANOMALIES.md` 舊制標記尚未施行** —— 其屬 W-VF13，
   而 W-VF13 之改名部分須待目錄命名裁定後方能動。
3. **R-VF12 所令之揭露文字尚未撰寫**（W-VF15，自始未執行）。

---

## 3. W-VF21(2) —— 以 R-VF13 逐字複驗 R-VF17：**未逾越**

| R-VF13 之限縮 | 複驗 |
|---|---|
| 1. 僅及於**值域** | ✅ 本輪僅改 `writable` 分級與 `evidence_note`，未動任何 TC 欄位 |
| 2. **不及於 ER 之措辭** | ✅ 該 4 leaf 尚無 TC，`expected_result` 未曾書寫 |
| 3. **逐字引用，不得推論未載之值** | ✅ `evidence_note` 載該欄之逐字行。值域記為 `{ON, OFF}` —— **此為 R-VF13 自身之錨點所明定**（「`4859496` 之末行 `= "ON"` → **應解出值域 {ON, OFF}**」），非本層之推論 |
| 4. **`not clear` 之列不得為源** | ✅ 該 4 leaf 之 VC/VM 皆非 `not clear` |
| 5. `reasoning` 須具名來源欄名與 leaf id | **部分** —— 見下 |

**第 5 項之部分**：`writability.tsv` **無 `reasoning` 欄**，本層記於
`evidence_note`（含裁決編號、來源欄名、reqid、逐字來源行；leaf id 即列鍵）。
**R-VF13／R-VF17 所指之 `reasoning` 為 TC 物件之欄位**
（`generated/batch*.json` 之 `tcs[].reasoning`），該 4 leaf 尚無 TC，
**故第 5 項於 TC 書寫時方能完全履行**。本層具名此未竟部分，不以現況冒充完成。

### 3.1 R-VF13 之兩個錨點，本輪實測

```
必命中   4859496 之 VM → solvable() 得
         ('TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm', 'ON')                  ✅
必不命中 14 個上游自述 `not clear` 之 leaf → solvable() 回傳非空者 0     ✅
```

（`solvable()` 位於 `scripts/vf230_wvf14_registry.py`，其於 W-VF14 即已
依 R-VF13 第 4 項排除 `not clear` 之列。）

---

## 4. W-VF23 —— 覆寫層（R-VF20 四項）

| R-VF20 | 施行 |
|---|---|
| 1. 改為具名之 driver 後置步驟 | `scripts/grade_overrides.py --apply`；舊之一次性腳本 `vf230_rvf17_apply.py` **已刪除** |
| 2. 清單獨立成檔，清單即證據 | `data/grade_overrides.tsv`，4 列 × 7 欄（`leaf_id`／`from_grade`／`to_grade`／`ruling`／`source_column`／`reqid`／`source_verbatim`）。缺 `ruling` 或 `source_verbatim` 者 `raise` |
| 3. 檢查須能失敗 | `--check`；**可失敗性已實測，見 §4.1** |
| 4. RUNBOOK／PLAYBOOK 明列 | 二檔皆已加「跑 driver 後必跑後置步驟」 |

**`writability_driver.py` 未改**（R-VF20 明令）。

### 4.1 可失敗性實測

```
1. 人為將 -030 之 writable 改回 W2（模擬 driver 重跑）
2. --check  →  「覆寫未生效 —— driver 已重跑而後置步驟未跑：
                 SWE1-VC-HeatedSteeringWheelManagement-030: 現為 W2，應為 W0」
                exit 1
3. --apply  →  覆寫 -030 -> W0
4. --check  →  exit 0
5. 分級欄與步驟 1 前之備份逐列相同
```

### 4.2 本條未令而必要之一項 —— 重跑不得使註記累積

`--apply` 首版重跑會**重複附註**：`-030` 出現兩筆 `R-VF17` 註記。
成因為新舊兩支腳本之註記措辭不同，文字比對之去重失效。

**已改為依覆寫清單單一來源重生註記**（R-VF20 第 2 項「清單即證據」之延伸）——
重跑三次後仍為一筆。

**此為本輪自行補上之要件，非條文所令。** 建議納入 R-VF20。

---

## 5. W-VF22 —— 34 leaf 結案：**(i) 依既有規則之正當排除**

```
leaves.tsv 271  －  writability.tsv 237  =  34      （反差 0）
該 34  ≡  data/non_functional_leaves.tsv 之 34 列   （集合全等，實測 True）
其 categorization：Heading 25 ／ Information 9
```

**明文出處：R-VS15。** `docs/upstream/06_comfort_overlap.md:81` 逐字：
「本 feature 母體 = `data/leaves.tsv` 減去 `data/non_functional_leaves.tsv`
= **237**（R-VS15）」；`RULINGS.md:187` 另令
「**271 僅用於描述 037 之列數，不得作為任何比率之分母**」。

→ **237 即為裁定之母體，非 271 之殘缺子集。**
A-VF5 所慮之「一個非全集之來源被當作全集使用」**不成立**。

**W-VF22 第 5 項（既有判準是否失真）**：**否。** 本線以 `writability.tsv`
為來源之三處（W-VF16 判準 (c)／W-VF18／W-VF14 存查表）皆以 237 為母體，
與 R-VS15 一致。

**附帶 —— A-VF4 於此獲完整解釋**：本輪 W-VF18 與 R-VF17 首版所選之錨點
（`LeftFrontHeatedSeat-001`、`HeatedSteeringWheelManagement-023`）
**皆為該 34 之成員**（Heading／Information），本即不在 237 內。
**錨點選錯之根因是選了非 leaf 者為 leaf 錨點。**

**一項未列為 anomaly 之命名瑕疵**：`leaves.tsv` 之檔名與其內容不符
（含 34 個非 leaf）。**本輪未改名** —— 其為 Part 1 之產物，改名會斷全庫引用。

---

## 6. R-VF22 —— 兩項准改已施行

```
feature.yaml:29
  - # leaf 全集以 data/vf230_leaves.tsv 為準（619 leaf）。
  + # leaf 全集以 data/vf230_leaves.tsv 為準（627 leaf，R-VF16；
  +   其中 8 列標 disagree=1，見 A-VS132）。

scripts/vf230_layer2.py:113
  - assert tot_leaf == 619 or True   # 總數自各簇重算，不硬編
  + assert tot_leaf == 627, f"leaf 合計應為 627（R-VF16），實得 {tot_leaf}"
```

**`or True` 已去除，且可失敗性已實測**：暫將 `vf230_leaves.tsv` 少一列，
腳本 `AssertionError: leaf 合計應為 627（R-VF16），實得 626`，`exit 1`。

`feature.yaml:118`（`388/619`）依 W-VF20 之逐行判別**維持不改**。

**施行前已依本條末段確認**：`git status` 實測 `feature.yaml` 無併行線之
未提交變更。

### 6.1 施行後重跑 W-VF20 —— 須改由 2 降為 **0**

```
R-VF22 施行前   須改 2 ／ 不改 95 ／ 待人工 0
R-VF22 施行後   須改 0 ／ 不改 120 ／ 待人工 0
```

（不改之數增加係因 R-VF22 之施行與本輪之落檔另生若干含 `619` 之歷史陳述。）

**重跑時兩處錨點皆失效，其一為正面、其一為缺陷（A-VF6）**：

- **(a) 正面** —— 必為「須改」錨點指向 `feature.yaml:29`，該行已改為 `627`
  而不再含 `619`，腳本依 **R-VF21 第 1 項**（存在性先驗）停下。
  **「世界已變」被察覺而非被忽略。**
- **(b) 缺陷** —— 逐行覆寫之鍵為 `(檔, 行號)`，而 (a) 之編輯使
  `388/619` 一行**自 118 移至 119**，覆寫鍵失配，該行遂由「不改」
  **靜默改判**為「須改」。已改為 `(檔, 內容片段)` 鍵。

**通則建議（納入 R-VF21）**：判準之覆寫、例外、錨點一律以**內容**定錨，
不以行號 —— **行號是位置，內容才是識別。**

---

## 7. W-VF21(3) —— V04–V08 五包之工單盤點

| 工單 | 下放 | 狀態 |
|---|---|---|
| W-VF13 改名／舊制標記 | V04 | **自始未執行**（改名待目錄裁定；`ANOMALIES.md` 之舊制標記亦未加） |
| W-VF14 存查掃描 | V05→V06 修訂 | 已執行（V06） |
| W-VF15 R-VF12 之揭露文字 | V05 | **自始未執行** |
| W-VF16／17 | V06 | 已執行（V06） |
| W-VF18／19／20 | V07 | 已執行（V07） |
| W-VF21／22／23 | V08 | 已執行（本包） |

**自始未執行者二：W-VF13、W-VF15。** 二者皆非本包工單，本輪未補。
**W-VF15（R-VF12 之揭露文字）之逾期較須注意** —— 其為交付文件之內容，
而 R-VF12 明言「範圍之界定與該界之揭露為兩件事，裁定只解決前者」。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **R-VF13 第 5 項未完全履行**（§3）。`reasoning` 為 TC 欄位，該 4 leaf
   尚無 TC。**其履行時點在 TC 書寫時，現無機制保證彼時不遺漏** ——
   覆寫清單有該資訊，但無任何檢查要求 TC 之 `reasoning` 引用之。

2. **R-VF12 之「1087 為分母」禁令與既有上繳衝突，本輪只作歷史處理**。
   `vf230/00_intake.md` §12.3 與 `V06` 曾以 57.7%／42.3% 表述，分母為 1087。
   依 R-VF18 判為歷史紀錄不追改 —— **惟該判斷是本層所作，未經分析層核可**。
   R-VF12 之禁令未區分「此後不得用」與「既有須追改」。

3. **W-VF15 自始未執行**（§7）。

4. **覆寫層只保護 `writable` 一欄。** driver 重跑時，該 4 leaf 之
   `blocker_class`／`blocker_detail` 亦會回復為 `B6-value-absent`，
   而 `--check` **只驗 `writable`**。本輪之 `--apply` 會清空該二欄，
   但 `--check` 不會察覺其被回復。**檢查面小於變更面，此為一個已知缺口。**

**另有一項為本輪之方法教訓**：A-VF4 之根因（§5）為「選了非 leaf 者為 leaf
錨點」。R-VF21 第 1 項令「錨點須存在於被掃描之集合內」已足以防之 ——
**但若當初 `leaves.tsv` 之檔名與其內容相符（271 非 leaf 全集），
該錯根本不會發生。** 命名之精確性與驗證機制之有效性在此相通。
