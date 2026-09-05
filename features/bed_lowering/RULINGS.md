# RULINGS — Bed Lowering Mode (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄，不改寫、不摘要。
本檔為 Bed Lowering Mode 之裁決權威。裁決前綴 `R-BLM`、異常前綴 `A-BLM`、
資料請求前綴 `DR-BLM`，不與任何既有 feature 共用序號。

來源：`docs/handoff/01_intake_recon.md` §二（下放包 01，Pei 2026-08-26 裁定
Q1 甲／Q2 Heading 納入但註明不寫測項／Q3 裁），及同日 chat 之三次追裁。

**取號警語（本檔自身之撞號實例）**：本檔 2026-08-26 14:34 建立時，
分析層未依 R-G62′ live 取號，自記憶推定「R-BLM3 之後接 4」，
而 `R-BLM4`（PDF 來源本）已於同日 13:15 由執行層落於
`01_intake_recon.md` §二。**號碼簿在那份檔，不在本檔** ——
而分析層因為那份檔是自己 11:21 寫的，就以為自己知道最大號。
同日 15:0x 修正：原 `R-BLM4`（spec_reference）→ `R-BLM5`，
原 `R-BLM5`（SYS 缺號）→ `R-BLM6`，PDF 來源本那條逐字補入為 `R-BLM4`。
**先落檔者優先。** 日後取號一律於落檔當下 grep 本檔與
`docs/handoff/` 全目錄，不得自記憶推定。

---

```
R-BLM1（feature 身分與結構歸屬）

（Pei 2026-08-26 裁定 Q1 甲。）

Bed Lowering Mode 立為獨立 feature。slug = `bed_lowering`，
test_group = `Bed Lowering Mode`。自有工作簿與
`features/bed_lowering/docs/{handoff,upstream}/` 目錄。

不併入 `features/vehicle_setting/`，不附掛 VF230 工作簿 —— 該本 438 TC
已寫回、處於 Pei 手動收尾階段，追加有污染風險。

037 之 `FROP = Vehicle Settings` 為上游程式歸類標籤，不構成目錄歸屬依據，
不進入 test_group、不進入任何 TC 欄位。
```

---

```
R-BLM2（驗證範圍與 Heading 列之處置）

（Pei 2026-08-26 裁定 Q2：「Heading 列納入但註明不寫測項」。）

覆蓋台帳收錄 037 `Analysis Report` 全部 218 列。

42 個 Heading 列（`SWE1-HMI-BLM-001` ~ `-042` 母號）納入台帳並標註
`No TC — Heading; refer to child IDs`，不作為 TC 生成對象。其
Verification Criteria 原文即為 "Please refer to the following IDs:"。

176 個 leaf（Categorization = Functional Requirement）為 TC 生成對象。

人因／可視性群（BLM-013 ~ BLM-017）之處置：可功能化改寫為 HMI 可觀察
行為者生成 TC；純設計驗證性質者不生成，列入 coverage gap disclosure
table 隨工作簿交付。
```

---

```
R-BLM3（036 母本與 workbook_state）

（Pei 2026-08-26 裁定 Q3 裁，從屬 Q1 甲案自動成立。）

036 母本套用 R-G1 全域條文：
`forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
Specification & Result_SWQT_20260817_ext.xlsx`

`workbook_state = BLANK`。不沿用任何既有 036 本，無既有 done region。

母本之 R 欄 design_method 下拉為 x14 擴充。任何以 openpyxl 存回母本之
操作都會摧毀該下拉（R-G1 註）。寫回一律採 XML 外科式修改。
```

---

```
R-BLM4（PDF 來源本）

（Pei 授權 analysis 層裁定，2026-08-26；逐字照錄自
`docs/handoff/01_intake_recon.md` §二。）

裁：以 `features/bed_lowering/inputs/` 那份為準。

實測依據：二者 metadata 同源（Title、Author `T6133SW`、Producer
`Microsoft: Print To PDF`、CreationDate 2021-06-25 18:46:52 全等），
確為同一次輸出之同一份文件。差異來自後手處理——`spec-index/sources/`
那份 ModDate 為 2025-11-04，被線性化（`Optimized: yes`）、加了
metadata stream 與 AcroForm，且 p.3「Change Log」頁被作者 `SD63673`
於 2025-11-04 12:16 加上兩條紅色 Line 標註（寬 3.0，斜跨整頁，
實為一個打叉）。`inputs/` 那份無任何 annotation，
是未經觸碰的原始輸出。

裁定理由：來源本應取未經後手標註者（標註是他人閱讀痕跡，
非交付內容的一部分，且該打叉之意圖無從查證，不得當作規格語意）。
檔案大小之差（665,190 vs 664,990 bytes）純為重存所致，非版次差異
—— 本 feature **不存在 PDF 版次問題**，勿誤記為版本衝突。
```

---

```
R-BLM5（specification_reference 之錨定 —— 採乙案）

（Pei 2026-08-26 裁定「乙」，回應 A-BLM4 之三選一。）

`specification_reference`（工作簿 N 欄）逐字取 037 `HMI Source ID` 欄
原值，不構造、不補章節號：

    SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)

單行。全簿 176 列該欄同值。

本條為 IN §10.7(b) 之 [OVERRIDE]，其啟動載於
`docs/runtime/profiles/FW036_R1L_BedLowering_Profile.md` §1。

override 之理由為**上游正式欄無章節錨**（A-BLM4 之實測：037
`HMI Source ID` 218/218 列相異值數為 1，無章節號後綴），
**非分析層省略**。追溯粒度因而為文件級，交付時於 coverage 說明揭露。

本條與 Vehicle Category 之 R-VC4 為同一條文（「逐字取 037 HMI Source ID
欄原值，不構造」），但**兩者之結果不同** —— Vehicle Category 之 037 該欄
帶章節號，展開得 66 section；本 feature 之 037 該欄不帶，展開得單一常數。
**條文相同而結果相異，其差異來自上游 037 本身，不是條文之歧義。**
```

---

```
R-BLM6（SYS-HMI-RA-BLM 之 24 個缺號 —— 不寫）

（Pei 2026-08-26 裁定：「是 SYS 側本就含非 HMI 項（底盤、電氣）
沒列在 037 就不寫」。）

`SYS-HMI-RA-BLM` 之 001~066 中，037 僅引用 42 個。缺號 24 個：
3, 5, 6, 8, 12, 18, 19, 21, 23, 26, 28, 30, 32, 33, 35, 38, 39, 41, 42,
47, 53, 56, 61, 62。

該 24 號判定為 SYS 側之非 HMI 項（底盤、電氣），未列於 037 即不在
SWE.6 範圍。不生成 TC、不列 coverage gap、不登 DR 向上游查詢。

**本裁定之依據為 Pei 之領域判斷，非自手邊文件驗得。**
分析層先前之實測結論為「二者（SYS 側非 HMI 項／037 未分解之項）在手邊
文件上區別不出來」，該結論不因本裁定而改變 —— 改變的是**由誰承擔該判斷**。
留此註記使日後稽核讀得出本條之來源。
```

---

```
R-BLM7（spec_mode —— 採 D）

（Pei 2026-08-26 裁定，回應 A-BLM7。）

`feature.yaml` 之 `spec_mode = D`（looked up, never constructed）。

理由：A 建不起來 —— 其所需 outline map 需 037 `HMI Source ID` ∩
SYS1 `SYSRE_HMI_Source ID`，實測為空（A-BLM4）。B 技術可行
（PDF 文字層 21/21 頁、8,157 字元）但會為批次語料引入第二真相源，
而 037 每 leaf 已帶完整 Requirement Description。D 與 R-BLM5 已裁之
行為同族（null 編碼，R-VC8），三者中唯一自洽。

後果：批次語料取 `data/leaf_inventory.tsv`（037 側）；規格 PDF 降為
人讀參考，不入 prompt 語料。
```

---

```
R-BLM8（feature.yaml 實際形制與 spec_reference_template: null 之追認）

（Pei 2026-08-26 裁定，回應 A-BLM6。）

追認執行層已落檔之形制：巢狀 yaml（`cfg["workbook"]["columns"]` 與
`cfg["paths"]`，依 `scripts/feature_config.py` 實際 loader），且
`spec_reference_template: null` —— 該值為管線既有之「查得而不構造」
編碼（recon.py:908 之 R-VC8 註），非新增枚舉，不改 schema。

下放包 02 §二之字面指示（扁平鍵 + `literal_037_hmi_source_id`）作廢：
實測該字串不含 `{outline}`，replace 為 no-op，176 列 N 欄會被靜默寫入
字面字串；鍵省略亦非安全（預設 `{outline}` → 裸章節號）。
null 為唯一合於 R-BLM5 之編碼。
```

---

```
R-BLM9（參考資料庫之版本綁定 —— 沿 vehicle_setting）

（Pei 2026-08-26 裁定，回應 A-BLM9。）

`dbc_b`／`dbc_fd`／`lid`／`proxi` 四庫沿 `vehicle_setting` 現綁之版本
（同 FROP、同 N1L 車系）。執行層自 `features/vehicle_setting/feature.yaml`
之 `reference:` 節逐字抄綁定並實算 sha256 回報；
vehicle_setting 若未綁全四項，缺項列出停下回報待 Pei 點名，不得自擇。
```

---

```
R-BLM10（R-G 引用之臨時讀法 —— 本 feature 一律 FO）

（Pei 2026-08-26 裁定，回應 A-BLM8。）

R-G12 ~ R-G20 於 FO 與 RULINGS_LEDGER 兩份權威間撞號（A-BLM8 實測）。
<!-- R-G43：兩側皆可讀／撞號紀錄，未改號；見 docs/reports/rg43_manual_20260905_judged.tsv row 20,21 -->
本 feature 期間，該段號之引用**一律取 FO 讀法**（下放包 02 已如此
執行，追認）。撞號本身屬全域線，另開全域收尾包擇一側重編號，
不在 feature 線解。
```

---

```
R-BLM11（四庫點名 —— 採乙）

（Pei 2026-08-26 裁定，回應上繳包 03 §三之停下請示。）

採讀法乙：四庫綁 `vehicle_setting` 實際在用之四檔 ——

  lid    = Logical Identifiers and CAN Mapping v1_76.xlsx
           ffceac36e9db145dc0311a25435b15249835e077bab264e71a95b0fb37a98ef4
  dbc_b  = PDT27_E2A_R4_BHCAN.dbc
           9ef1ec9830fc8018b23d0e36dbd7ca6023b9b0a03124095726eb5583a01930d0
  dbc_fd = PDT27_E2A_R5_FDCAN8.dbc
           51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2
  proxi  = PROXI_HDCC27_R3_20250424.xlsx
           e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2

（上列雜湊為上繳包 03 §3.3 之實算值，供對帳；寫入時仍自實體檔重算，
不符即停，下放包 03 §三-2 之規定不變。）

與 `display` 現綁版本三項相異（LID v1_76 vs v1_78、兩支 DBC 皆異），
為已知且被接受之後果（R-G15 立條之既存歧異），非新分叉。
台架基線若日後換版，四庫改綁另裁，不回溯本條。
```

---

```
R-BLM12（pilot 審查裁定 —— A／B／C 三類照建議核准）

（Pei 2026-08-26 裁定「准」，回應分析層對 pilot 13 TC 之逐條審。）

A 類（機械修正，執行層逐條執行）：
(1) 禁用動詞 `Observe` 作主動詞之步驟全數改寫為 `Check that ...`／
    `... record ...`（IN §5.1）；037-03 步 1 之 `record whether` 與 ER
    單態斷言之矛盾一併消除。
(2) 011-02 之 $ASCM_FD_1.RL_Lvl$／$RR_Lvl$ 回 DBC 驗名：驗有則補入
    manifest 預查清單；查無則依 IN §8.7.5(d)/(g) 處置，不得以近似
    訊號代入。「沒查」之訊號不得存於交付 TC。
(3) 038-04 design_method 改 `Fault Injection`（IN §12 first-match：
    含 simulated fault 即命中）。
(4) Pre-Condition 之 `DT model` 限定全數改為
    `equipped with the air suspension system`：037 fault 群未分車型，
    限 DT 為縮窄。

B 類（迴路驗證之改錨）：
011-01、011-02、037-02（及 037-01 部分）之最終檢查對象現為自身
注入之 ASCM 訊號，驗的是注入非 DUT。授權執行層查 DBC／LID 之
HU→ASCM 請求訊號（GW_C_I_11 線索）並以 DUT 可觀察物改錨四條；
改錨不得越界至 sibling 持有之觀察物（EVIC 訊息屬 011-03／038-01，
highlight 屬 037-03）。某 leaf 若查到底無獨立可觀察物，
該 leaf 停下個案回報，不硬寫。

C 類（維持現狀之確認）：
(5) 兩對近重複（011-03/038-01、011-04/038-03）保留四條不合併
    （§8.2.1；trigger 相異，括號下半已載區分 token）。
(6) 懸吊角度門檻不登 DR：注入點為故障回報，角度值非本群所需。
(7) EVIC 破折號採 hyphen；038-04 加註文字基準取 SYS1 正規化文字
    （NRL-193702），圖僅供版面。
```

---

```
R-BLM13（「偵測／接收」類 leaf 之錨定 —— 斷言層級錯開）

（Pei 2026-08-26 裁定「准」，回應上繳包 05 §二-5 之三選一；
採出路 2 之限定形。）

「偵測／接收」類 leaf（其 SWE.6 層唯一可觀察證據為下游反應，
而該反應已被拆為別的 leaf 者）得以 sibling 持有之觀察物為錨，
但斷言層級必須錯開：

(a) 本類 TC 只得斷言**反應之存在**（a fault indication appears／
    the highlight state changes）；逐字文字與規定狀態之正確性斷言
    仍歸持有 leaf。
(b) reasoning 必載委派（IN §8.2.1 工作流第 4 步之句式，具名持有
    leaf 號）。
(c) 可用 trigger 區分者優先用 trigger 區分，不動用本條。
(d) 本條不改變上游分解（§8.2.2）；其代價——交付本內出現觀察物
    重疊之 TC 對，靠括號下半與 reasoning 區分——為已知且被接受
    （與 R-BLM12 C(5) 同族）。

落到 pilot 四條：
- 011-01：注入後 EVIC 出現 Bed Lowering 故障指示（不驗文字）
- 011-02：保留角落高度 baseline，final = EVIC unsuccessful 指示出現
- 037-01：以 trigger 區分（fault 先於按鍵 vs 037-03 之 fault 後於
  啟動），錨 highlight 不亮／不維持，不動用 (a)
- 037-02：與 037-03 同 trigger，依 (a) 錯開斷言層級（反應存在 vs
  規定行為）

出路 1（coverage gap）未採：行為可證，宣告不可驗會高報缺口。
出路 3（登 DR）未採：其他 TC 以 HU 實體按鍵觸發，請求訊號對照
除解鎖本四條外無他用，且上游未必給得出。
```

---

```
R-BLM14（pilot 退出、寫回授權、reasoning 單位定式）

（Pei 2026-08-26 裁定「准」，回應分析層對上繳包 06 之複審。）

(1) **pilot 退出審通過**：13/13 過，授權寫回工作簿（XML 外科式，
    R-BLM3 之保全條款不變）。
(2) **reasoning 單位定式**（採上繳包 06 §5.1 選項 3 之定式化）：
    profile 立 [OVERRIDE IN §10.4] —— top-level reasoning 為批次摘要
    （必有）；per-TC reasoning 僅於裁定要求逐 leaf 內容時存在
    （R-BLM13(b) 委派、IN §8.2.1 縮窄委派），其餘 TC 不補。
    per-TC reasoning 之存在本身即為「本條涉及委派」之訊號。
    未採選項 1（對應模糊化）與選項 2（九條補寫屬審後重構，
    內容只能從頂層倒推，造敘事風險）。
(3) 038-04 Pre-Condition 6 改寫為可用性狀態句：
    `The SYS1 normalised text of NRL-193702 is available to the tester
    as the wording baseline`（§4.4：狀態非定義）。
(4) 工程債三件（generator 實跑、lint_tcs、recon）不擋寫回，
    **續批開工前須收**。
```

---

```
R-BLM15（上繳 07 四題之裁）

（Pei 2026-08-26 裁定：「准 2 准 3 准 4 送」。）

(1) recon 兩條 assertion 採選項 1（改宣告）：下放包 02 之
    recon_assertions 兩鍵重宣為 R-BLM5 一致之期望 ——
    `N 欄原值相異數 = 1 且 = R-BLM5 常數`、`可解析章節數 = 0`。
    原宣告量錯對象（解析後 stem 非欄位原值），作廢留痕。
    不動全域腳本（選項 2 屬全域線）、不留恒 FAIL（選項 3 為
    警報疲勞來源）。DECISIONS.md 回復產出，定位為機器摘要；
    RULINGS.md 維持本 feature 裁決權威。
(2) `functional_safety`／`test_version` 兩常數不直接追認：
    執行層自 AMFM 已交付本（v1 tagged）與 SWC 0708 實測該兩欄
    值域回報；查得既定值則 13 列 patch，查無則 Pei 點名。
(3) 續批順序照下放包 07 §四表准（B1 = Restore And Exit 9 leaf 起）。
(4) DR-1 裁定送出。送出動作由 Pei 執行，送出日由 Pei 回填
    DATA_REQUESTS.md；未復前 B1 依 IN §8.4.3 落
    `PENDING: DR-1 BLM operating speed threshold value`。
```

---

```
R-BLM16（上繳 08 四題之裁）

（Pei 2026-08-26 裁定「裁」，四項照分析層建議核准。）

(1) recon 剩餘 1 FAIL：准改 `scripts/recon.py`，將該無條件 assertion
    納入 want 閘控 —— **未宣告時維持現行無條件行為**（與 lint
    `--profile` 前例同型，既有各本基線不動）。驗收條件：
    無宣告之回歸跑須重現現行 1-FAIL 行為；本 feature 宣告後全綠，
    DECISIONS.md 產出。
(2) `test_version` 清空：775 列全案無人填過，`1.0` 為造值。
    現行 19 列 AB 欄 patch 為空。
(3) `functional_safety` 留空：隨交付多數（764/775，含 Arif done
    region 237 列）；privacy 之 `NA` 屬孤例。現行 19 列 S 欄
    patch 為空。
(4) 兩處 5 Km/h（022-01、027-05）追認為**暫定測試輸入**：
    複驗義務掛於 DR-1 結案動作 —— 門檻回覆若 ≤ 5 Km/h，
    該兩條改值。登記於 DATA_REQUESTS.md 與 manifest。

另記：分析層對 B1 審出三項 A 類（022 群入口改 HU 按鍵、
022-02 步 1 指涉、027-03 隱藏狀態前置），屬機械修正隨下放包 09
執行，不另立條。B1 首審含 A 類，不計入 R-G53 連續乾淨批數；
修訂複審通過後亦不回計，計數自 B2 起。B1 修訂複審通過後，
B2 由分析層逐包下放，不另經 Pei 關卡（R-BLM15(3) 已准順序）。
```

---

```
R-BLM17（交付本列序 —— 改依 req_id 升冪）

（Pei 2026-08-27 裁定「乙」。）

交付本 151 列全簿依 `Requirement or Design ID`（D 欄，
`SWE1-HMI-BLM-{nnn}-{mm}`）**升冪重排**；TC ID 隨列重新指派為
`newR1L-BLM-001` ~ `-151`，連續無跳號。

原列序為批次先後（pilot → B1 → … → B7），批內升冪而批間跳號。
該順序出自下放包 07 §四之批次表，其排法理由為「小組暖機、
訊號密集群靠前以早暴露 DBC 缺口」—— 那是為**生成過程**
優化之順序，**分析層未預見其會直接成為交付本列序**，
屬分析層之疏失。

可行性依據：本 feature 為 BLANK 起建、無既有 TestRail 案例，
`testrail_new.tsv` 為新建清單非新舊對照，
**重排不打斷任何既有 ID 對映**。交付後再改則需製 ID 對映表。

Test Set 欄值不變（仍主張其能力叢集），僅列序改變；
同一 Test Set 之列因而不再相鄰，審查者可以該欄篩選。
後續 DR 回覆之 12 條追加寫回，**不插入升冪位置**，仍接於列尾
（`--start-id 152`）—— 插入會使已交付之 TC ID 全面位移。
該例外於 DELIVERY_NOTE §1 具名。
```
