# 上繳包 14 — vsm_v43：b2-3 生成　Lane Departure Warning（18 leaf）＋ 台帳重生

日期：2026-09-02　執行層
**無對應下放包** —— 本包依 **Pei 2026-09-02 之直接指示**（「要」）執行兩事：
(1) 授權執行層重生 `docs/fw036/RULINGS.sha.tsv`（R-VT14(c) 原指定歸 Pei）；(2) b2-3 開跑。
契約沿 12／13 包（R-VT25(d) 序位三）。產出止於 `generated/`；**未寫工作簿、已凍 b1／b2-1／b2-2 一位元未動**。

> **編號說明**：FO 之第 8.7 節定「一次往返共用同一 NN」。本包無下放包，
> 取下一個未用之 NN = 14。若日後補下放包 14，請沿用本號。

---

## 〇、一句話結論

**台帳重生：`rulings_hash` FAIL → PASS，gate 由 4 支紅降為 3 支。**
**b2-3：18 leaf → 18 TC，E 全項通過。綠色通道 3／3。**

| # | 項 | 實測 | 判 |
|---|---|---|---|
| E38 | 覆蓋 | **18/18** | ✅ |
| E39 | R-S4 括號下半 | 18/18；重複 0 | ✅ |
| E40／E41／E45 | 尾句號／`[...]`／modal | 0／0／0 | ✅ |
| E42 | `$…$` 可回溯 v5 解得 | 4 名，皆解得 | ✅ |
| E43 | PENDING | 本批 0（逐一實測，§三） | ✅ |
| E44 | reasoning | 18 則，3–4 句 | ✅ |
| E51 | Remarks provisional | 18/18 | ✅ |
| E56 | test_item 上半逐字全等 | **18/18** | ✅ |
| — | 雙錨前綴一致 | 18/18，前綴唯一 | ✅ |

## 一、台帳重生（Pei 授權）

**重生前之安全檢查**（因該檔為共用件，且他線持續作業）：

| 項 | 實測 |
|---|---|
| 重生前工作區狀態 | **乾淨**（無他線未提交之修改） |
| 現行台帳 → 重生 | 652 → **697** 列（`ruling`），總錨點 728 |
| **消失之列** | **0** |
| 新增 | **45**（`R-VT` 16／`R-VL` 17／`R-VS` 12） |
| `sha8` 變動 | **5**（來源：`features/vehicle_setting/RULINGS.md` 2、`features/vsm_v42/RULINGS.md` 3 —— 他線條文之現況，非本線） |

**確認零資料遺失後方寫入。** 寫入後：

```
rulings_hash   FAIL → PASS: docs/fw036/RULINGS.sha.tsv 與現行條文相符（728 條）
gate_all       4 支紅 → 3 支紅（canon_refs／gates_tsv／lint_paths，皆與本線無關）
```

**本線 R-VT 由 10 條入帳增為 26 條**，且 **R-VT1–R-VT18 之 `body_sha8` 與我歷包所報逐條相同**
（`R-VT1 93666dae` … `R-VT18 04399f1c`）—— 即前十四包之樹外替代量測全部獲台帳追認。
R-VT19–R-VT26 之台帳值：`24430b0e`／`f9c03380`／`928ec94b`／`c7cbddb3`／`05c1aaf7`／`a2927860`／`027fb43e`／`9f29c833`。

> **R-VT14(c) 之「重生歸 Pei」自本次起由 Pei 授權執行層代行**；條文更新屬分析層，本包只記事實。

## 二、b2-3 母體與規格節

母體：v2 之 `test_set = Lane Departure Warning` 且 `status = active`，**18 列**，
**跨兩個 chapter**：`01.11.01.01.03`（9 列，`spec_section 1.11.1.1.3` Lane Sense Warning）
與 `01.11.01.01.04`（9 列，`1.11.1.1.4` Lane Sense Strenght）。

| 規格段 | 內容 | leaf |
|---|---|---|
| 501–503 | `Half_Torque_Sensibility = "Leve 3"` → `" Lanse Sense Warning 1 "`，選項 `Early, Late` | `-420` |
| 504–509 | 兩選項之送出 | `-421`／`-422` |
| 511–512 | 收訊 `IPC_VEHICLE_SETUP2.LDW_Sensibility` → 顯示更新 | `-423` |
| 514–516 | `= "Leve 2"` → `" Lanse Sense Warning 2"`，選項 `Early, Med, Late` | `-424` |
| 518–525 | 三選項之送出 | `-425`／`-426`／`-427` |
| 527–528 | 收訊 → 顯示更新 | `-428` |
| 530–532 | `Half_HMI_Setting = "Leve 3"` → `" Lanse Sense Strenght 1 "`，選項 `Low, High` | `-430` |
| 534–537 | 兩選項之送出 | `-431`／`-432` |
| 538–539 | 收訊 `IPC_VEHICLE_SETUP2.LDW_Intensity` → 顯示更新 | `-433` |
| 540–542 | `= "Leve 2"` → `" Lanse Sense Strenght 2"`，選項 `Low, Med, High` | `-434` |
| 543–550 | 三選項之送出 | `-435`／`-436`／`-437` |
| 552–553 | 收訊 → 顯示更新 | `-438` |

**18 leaf 一對一對映，無未對映者。**

## 三、產出（`generated/b2_ldw/`，37 檔）與訊號

**一 leaf 一 TC，TC 總數 18。** Priority 全批 `P1`（同 b2-1／b2-2 之理由）。
`design_method`：邊界值分析 **8**（各分支值域之兩端 Early／Late、Low／High）／決策表 **4**／
功能測試 **4**／等價劃分 **2**（中間值 Med）。

訊號四名皆 v5「解得」，`<label>` 逐字取 `val_tables_v43.tsv`：
`LDW_Sensibility` 族 `0=Early｜1=Med｜2=Late`；`LDW_Intensity` 族 `0=Low｜1=Med｜2=High`。**無 VAL_ 缺值。**

### PENDING —— 本批 0，逐一實測（不沿用前批，R-VT20(d)）

| 內部訊號 | v5 | 本批實測之 UI 面 | 判 |
|---|---|---|---|
| `LDW_Sensibility_Setting.Req` | 未解得(止於段1) | 規格 **para 502／515** 逐字具名 `" Lanse Sense Warning 1 "`／`" … 2"`，選項由 503／516 逐字給出；**HMI r288B `"Lane Departure Warning Sensitivity"`（TR `VF230/665`，選項 `Early / Late`）** 為錨 | **可走 UI 路徑** |
| `LDW_Intensity_Setting.Req` | 未解得(止於段1) | 規格 **para 531／541** 具名 `" Lanse Sense Strenght 1 "`／`" … 2"`，選項由 532／542 給出；**HMI r282B `"Lane Departure Warning"`（TR `VF230/VF665, CFTS022`）** 為錨 | **可走 UI 路徑** |
| `TLM_Vehicle_Setup_Menu.Info` | 未解得(止於段1) | 規格 **para 512／528／539／553** 同句載「on its display」 | **ER 觀察具名選單項**（R-P353 (ii)） |

**UI 名逐字取規格**（含其拼字瑕疵），未採 HMI 清單之較正確拼法（IN §8.6 source spec wins）。

## 四、規格拼字與內部矛盾（DR-VT2 佐證，逐字保留不改）

| # | 規格逐字 | 應為 | 出現處 |
|---|---|---|---|
| 1 | `Lanse Sense` | `Lane Sense` | para 502／515／531／541（**4 處**；節標題 500／529 反而是正確之 `Lane Sense`） |
| 2 | `Strenght` | `Strength` | para 529／531／541 |
| 3 | `Leve 3`／`Leve 2` | `Level 3`／`Level 2` | para 501／514／530／540 |
| 4 | **`updates the LDW Sensibility information`** 出現於 **Strenght（Intensity）** 節 | 應為 `LDW Intensity` | **para 539／553** —— **語意矛盾，非單純拼字** |

> **第 4 項值得單獨看**：`1.11.1.1.4`（Strenght／Intensity）之兩個收訊列，
> 其 THEN 子句寫的是「updates the **LDW Sensibility** information」，
> 而該節通篇處理的是 `LDW_Intensity`。SYSRA 之 `-433`／`-438` 逐字承襲此矛盾。
> **本包依 R-13／R-6 逐字保留於 `test_item` 上半**，而 ER 依該節之實際訊號
> （`IPC_VEHICLE_SETUP2.LDW_Intensity`）與其選單項書寫 —— **兩者之落差已入 §五 K-21**。

## 五、§K

| # | 項 | 待裁 |
|---|---|---|
| **K-21**（新） | 規格 para 539／553 之 THEN 子句誤寫 `LDW Sensibility`（該節為 Intensity）。本包 `test_item` 上半逐字保留，ER 依實際訊號書寫 | 確認此處置；或應於 `reasoning` 額外標註矛盾（本包已於 §四揭露但未逐列入 reasoning） |
| **K-22**（新，程序） | 本包**無下放包**（Pei 直接指示），編號取 14 | 確認編號；若補下放包 14 請沿用 |

## 六、anomaly／DR

**本包無新登 anomaly。**

| DR | 狀態 | 本包新增佐證 |
|---|---|---|
| DR-VT1 | 裁送出，**待發** | — |
| DR-VT2 | 建議併送 | **4 類**（`Lanse Sense` ×4、`Strenght` ×3、`Leve` ×4、**LDW Sensibility／Intensity 語意矛盾 ×2**） |
| DR-VT3／DR-VT4 | 暫持／先不送 | 本批 0 PENDING |

---

## 七、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 509
PASS      exit 0   rulings_hash     OK: docs/fw036/RULINGS.sha.tsv 與現行條文相符（728 條）
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 5 檔，基線 4 列）

總判：**FAIL** —— 3 支未過：canon_refs、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `rulings_hash` | **本包轉綠** | 台帳重生（§一），728 條相符 |
| `lint_delivery_spec` | **PASS** | K-20 之修正（`c5f471b`）生效 |
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 見下方實測 |
| `gates_tsv`／`lint_paths` | **無關** | 紅列全屬他 feature |

---

## 八、獨立判斷

1. **台帳重生之後，我歷包所報之 sha8 全部獲得追認 —— 這件事值得記一次。**
   自 00 包起，R-VT 之 sha8 一直以「樹外 `--out`」為替代量測（R-VT10(a) 裁可），
   而台帳直到本包才含這些列。重生後 **R-VT1–R-VT18 逐條相同、零差異** ——
   替代量測與台帳為同一值，十四包之報告無一需修正。

2. **綠色通道 3／3 達成，但我建議先別直接進第四批。**
   b1／b2-1／b2-2 三批零修訂，加上本批（待覆核）即滿。
   然而**至今 36 + 18 = 54 個 TC 全在 `generated/`，一個字都沒進工作簿** ——
   寫回是另一條路徑（R-VL20 型「待分析層覆核與 Pei 再授權」），
   而 K-20 已把 lint 的那道障礙拆掉。**建議先做一次寫回試跑（dry-run）**，
   讓 `lint036.py` 真的看過本線的內容，再繼續量產。
   理由：目前所有品質保證都是我自己的自檢表，`lint036` 從未跑過本線任何一列。

3. **K-21 是我這批唯一猶豫的地方。**
   規格說「updates the LDW **Sensibility** information」，但那一節整節都是 Intensity。
   我照 R-13 逐字保留上半，ER 則依該節實際的 `LDW_Intensity` 訊號寫 ——
   **等於 test_item 與 ER 在字面上不一致**。
   另一種寫法是 ER 也照抄「Sensibility」，但那會讓 TC 驗證一個該節不存在的東西。
   我選了前者並揭露，但這是判斷不是規則。

4. **本包未驗而下放包亦未要求者**：
   (a) `-423`／`-428` 與 `-433`／`-438` 兩對之 `Description` 逐字相同（同 FCW 之情形），
       本包以分支軸區別，未用 `duplicate_of`；
   (b) HMI r282B 之 TR 含 `CFTS022`，該 CFTS 是否適用本 VF 未查（同 13 包 §九-4(c) 之未竟項）；
   (c) `Half_Torque_Sensibility`／`Half_HMI_Setting` 之其他取值（規格只列 Leve 3／Leve 2）未查值域全集。

---

## 九、禁區遵守聲明

| 禁區 | 遵守 |
|---|---|
| 00 包 §零 1 | **git 未動**（本包未跑任何 git 寫入指令） |
| 00 包 §零 2／3／4／6 | 未寫 `vehicle_setting`／`vsm_v42`／profiles；`sources/raw/` 唯讀；**未代發 DR** |
| 對象限制 | **未寫工作簿**；**已凍 b1／b2-1／b2-2 一位元未動**；未開 `sandbox/base/` |
| 共用檔 | `docs/fw036/RULINGS.sha.tsv` 之重生**經 Pei 直接授權**，且重生前確認零消失、零資料遺失 |

本包寫入之檔：`docs/fw036/RULINGS.sha.tsv`（重生）、
`features/vsm_v43/generated/b2_ldw/`（37 檔，新）、`features/vsm_v43/docs/upstream/14_b2_ldw.md`（新）。
`data/`、`framework.md`、`RULINGS.md`、`DATA_REQUESTS.md`、`ANOMALIES.md`、`DECISIONS.md`、
既有三批 `generated/` **未動**。

---

## 十、下一步

1. **建議：寫回試跑**（§八-2）—— 讓 `lint036.py --profile vsm_v43` 首次看到本線內容
2. 裁 K-21（規格語意矛盾之處置）與 K-22（本包編號）
3. 條文落檔：K-18／K-19／K-20／§九-1 四項之裁決（Pei 2026-09-02「以上皆準」）尚未入 `RULINGS.md`
4. Pei：**發送 DR-VT1**（併 DR-VT2，本包新增 4 類佐證）
5. b2-4 = EPB Maintenance Mode 19 leaf（序位四）
