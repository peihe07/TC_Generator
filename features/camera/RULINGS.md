# RULINGS — Camera（FW036）

裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2），執行層之回報另起段落。
取號依 R-G23／R-G62′：落檔當下 live 取號 —— 本檔建立時全 repo 無既存
`R-CAM` 條號（2026-09-16 現查 `docs/fw036/RULINGS.sha.tsv` 與各 feature
`RULINGS.md` 皆無），故自 1 起。條文來源：下放包 `docs/fw036/handoff/down/20260916_CAM-01.md` §2。

---

### R-CAM1 — 兩本 037 皆須產出；A 本先、B 本後；互為步驟來源（Pei 裁，2026-09-16）

```text
R-CAM1  兩本 037 皆須產出；A 本先、B 本後；互為步驟來源
  (a) A 本（SWRA_V02，25 列）與 B 本（RVC-HMI-V0.1，230 列）各出一本 FW036 工作簿。
  (b) 生成順序 A → B。A 本之畫面入口／設定 hop 一律引 B 本之 SYS1 HeadUnitCameraSystems 匯出，
      不得自造；B 本之訊號／PROXI 前提一律沿用 A 本已定之寫法。
  (c) 追溯各歸各母體（IN §8.4.2）：A 本 spec_reference 引 CFTS092／VF551，B 本引 SYS1 HMI L&F 章節；
      互參只參考寫法，不複製對方之 spec_reference。
```

### R-CAM2 — Vehicle Model 七欄以 1／0 填寫；598／5210 一律 0（Pei 裁，2026-09-16）

```text
R-CAM2  Vehicle Model 七欄以 1／0 填寫；598／5210 一律 0
  (a) 工作簿 `Vehicle Model 車型` 七子欄（HDCC27 Atl-Hi／DT27 Atl-Hi／VF(ProMaster)637 Atl-Mi／
      Commander (598) Atl-Mi／Regengade (5210) Atl-Mi／Toro(2261) Atl-Mi／Fastack (376) Atl-Mi）
      每列填 `1`（適用）或 `0`（不適用），不留空、不用其他符號。
  (b) `Commander (598)` 與 `Regengade (5210)` 已不支援，Camera 兩本一律 `0`。
  (c) 五個有效車型欄每列至少一個 `1`。lint 新增檢查項（本 feature profile [ADD]）。
```

### R-CAM3 — 車型軸之拆分判準（Pei 裁，2026-09-16）

```text
R-CAM3  車型軸之拆分判準
  同一驗證點，若 PROXI 前提值、觸發訊號名（Atl-Hi vs Atl-Mi 之 CAN 訊號）、或 ER 可觀察結果
  任一因車型而異 → 拆 sibling，各列只勾自己的車型（§8.3 mode 軸），
  test_item 括號下半以車型／EE 作區分 token；全部相同 → 一列，勾全部適用車型。
```

**增補 (e) 段見下一條 R-CAM3(e)**；(a)–(d) 逐字不動（fenced sha 不變可證）。

### R-CAM3(e)（增補，2026-09-16，Pei 裁：CAM-03 審閱 §三-1「准」）

```text
R-CAM3(e)  訊息名因 EE 而異，而 PROXI 前提值與 ER 皆相同者，不拆列。
  Pre-Condition 專用一行、固定句式：
    `CAN source: <Atl-Hi signal> (HDCC27, DT27) / <Atl-Mi signal> (637, 2261, 376)`
  Procedure 一律以 Atl-Hi 訊號寫 §8.7.5(c) 之 `Send CAN:` 式；Atl-Mi 依該行代換。
  PROXI 值或 ER 任一相異者仍依 (a)–(d) 拆列。
```

### R-CAM3(f)（增補，2026-09-23，Pei 裁：CAM-07 審閱 §二-1）

```text
R-CAM3(f)  CAN source 行之適用條件。
  R-CAM3(e) 之 `CAN source:` 行只於**兩條件同時成立**時書寫：
    (i)  該 TC 之 Vehicle Model 同時勾 Atl-Hi（`HDCC27`／`DT27`）與
         Atl-Mi（`VF(ProMaster)637`／`Toro(2261)`／`Fastack (376)`）之至少各一；
    (ii) 該 TC 之 Procedure 含 `Send CAN:` 步（該行為其代換對象）。
  單一 EE 之列直接以該平台之訊息名寫 `Send CAN:`，不加該行；
  無 `Send CAN:` 步者該行無代換對象，亦不加。
  CAM-06 審閱 §二-3 對 `NR1L-RVC-023` 之裁定即本條之個案先例。
  施檢：`selfcheck_camera.py` 第 5 項。
```

**執行層落實（CAM-08 §2）**：四目錄 72 列以第 5 項掃描，**命中 17 列**，全數改正 ——
16 列刪該行，`NR1L-RVC-008` 另補正訊息名（只勾 2261／376 而 `Send CAN` 誤用 Atl-Hi 之
`TRANSM_FD_4.ShiftLeverPosition`，改為 `STATUS_CCAN4.ReverseGearSts`）。
修正後第 5 項命中 0。**`-008` 為本條所揭之實質缺陷，非僅版面** —— 其 procedure
於所勾之兩平台皆不可執行。

### R-CAM4 — Test Group 與 TC ID（Pei 裁，2026-09-16；取代審閱 §三-1 之「共用 CAM」）

```text
R-CAM4  Test Group 與 TC ID（取代審閱 §三-1 之「共用 CAM」）
  (a) A、B 兩本之工作簿 Test Group 欄一律為 `Rear View Camera`。
  (b) TC ID 分兩組序號：A 本 `NR1L-RVC-{nnn}`、B 本 `NR1L-RVCHMI-{nnn}`，各自自 001 起連號。
      R-G42 第二項之 ABBR 於本 feature 即為 `RVC`（A）／`RVCHMI`（B）；審閱 §三-1「共用 CAM」作廢。
  (c) 交叉參考索引以 SWE ID 互指，不以 TC ID 互指（兩組序號獨立）。
```

### R-CAM5 — 品牌軸：label 隨品牌而異者拆列，品牌寫入 Pre-Conditions（Pei 裁，2026-09-16）

```text
R-CAM5  品牌軸：label 隨品牌而異者拆列，品牌寫入 Pre-Conditions
  (a) HMI Settings List 標 `*` 之設定項，`*` 不入 hop；hop label 依 `Brand-Specific Names` 分頁取值。
  (b) 同一驗證點若 hop label 因品牌而異 → 拆 sibling（§8.3 mode 軸之品牌分支），
      Pre-Conditions 首行寫明品牌（例：`Vehicle brand is Ram`），Vehicle Model 七欄依該品牌之車型勾 1。
  (c) 品牌 ↔ 車型之對照由執行層自 `forms/SR24 R1 Market Configuration Table v1.6.xlsx` 提候選，
      列 DECISIONS [PROPOSED]，不得自 anchor 前綴或車名推定。
  (d) 本條與 R-CAM3 併讀：車型軸與品牌軸皆為拆分判準，二者同時成立時以車型軸為外層。
```

**(c) 經 R-CAM5(c)′ 取代**（見下一條）。原句依 R-TM13 加刪除線保留：

> ~~(c) 品牌 ↔ 車型之對照由執行層自 `forms/SR24 R1 Market Configuration Table v1.6.xlsx` 提候選，
> 列 DECISIONS [PROPOSED]，不得自 anchor 前綴或車名推定。~~
>
> **作廢理由**：該表之軸為市場／國別，全表無五車型之品牌欄（CAM-02 上繳 §5.1 實測：
> `HDCC27`／`DT27`／`637`／`2261`／`376` 五個代號零命中）。分析層未先查表即指名來源。

### R-CAM5(c)′（修訂，2026-09-16，Pei 裁：CAM-02 審閱 §三-1「准」）

```text
R-CAM5(c)′  品牌 ↔ 車型之對照以 PROXI `Brand_Configuration_2`（byte 130 bit 0–4，Format row 566）
  之各平台實測值為據：HDCC27／DT27／637 = 11 (RAM)、Toro(2261) = 1 (Fiat)、Fastback(376) = 5 (Abarth)。
  `Brand-Specific Names` 分頁無該品牌欄或欄空者，回落基礎 label。
  Camera 設定項之品牌軸實為兩分支：RAM 系 {HDCC27, DT27, 637} vs 基礎 {2261, 376}，與車型軸對齊。
```

取代 R-CAM5(c)。DR-CAM-e 結案（確認型 —— PROXI 值即證據）。

### R-CAM5(e)（增補，2026-09-16，Pei 裁：CAM-03 審閱 §三-2）

```text
R-CAM5(e)  品牌分支之 Pre-Condition 固定句式：
    `The vehicle brand is Ram (HDCC27, DT27, 637)`
    `The vehicle brand is not Ram (2261 Fiat, 376 Abarth)`
  「not Ram」為回落基礎 label 之分支，不逐品牌列名（2261 為 Fiat、376 為 Abarth，
  二者於 `Brand-Specific Names` 皆無 Camera 專屬 label）。
```
逐格實測見 `features/camera/data/brand_proxi.tsv` 與 `brand_labels.tsv`。

### R-CAM6 — B 本追溯母體 ＝ spec-index/cache 之 RVC+PAM 本（Pei 裁，2026-09-16）

```text
R-CAM6  B 本追溯母體 = spec-index/cache 之 RVC+PAM 本
  `SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021).xlsx` 以 `spec-index/cache/` 本
  （sha16 `1a0bef53c6de975c`，64 列）為 B 本 spec_reference 之母體；REF 本（`5a1c0ab24991dcb1`）
  於 MANIFEST note 記「同名異體，cache 本之真子集，不作追溯母體」。DR-CAM-c 結案。
```

### R-CAM7 — V4 Layer 3 以 Description 前導章節號向下繼承（Pei 裁，2026-09-16）

```text
R-CAM7  V4 Layer 3 以 Description 前導章節號向下繼承
  SYS2 VF551_V4 之 Layer 3 章節取 `D` 欄前導號（heading 列）向下繼承（321/321、60 章），
  不回查 docx。DR-CAM-b 結案。
```

### R-CAM8 — ENTER_CAMERA_SETTINGS 常數（Pei 裁，2026-09-16）

```text
R-CAM8  ENTER_CAMERA_SETTINGS 常數
  `ENTER_CAMERA_SETTINGS`（3 hops，§5.3）：
    `Press "Apps" on Menu Bar to open App Drawer` → `Select "Settings" in the App Drawer` → `Select "Camera"`
  第 3 hop 之來源：`forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`，`Settings` 分頁 row 464
  `13. Camera`（序號非 label；canon §5.8(c) 明列 HMI Settings List 為路徑來源）。
  ER：`The "Camera" settings screen is displayed`。DR-CAM-d 結案；FO §4 [ADD] 之 §5.3 承接完成。
```

### R-CAM9 — Out of Scope 來源之處置（Pei 裁，2026-09-16）

```text
R-CAM9  Out of Scope 來源之處置
  SYS2 Category 為 `Out of Scope`（含 `Out of scope`）之 32 個來源一律不作 spec_reference 錨；
  其中 `SYS-RA-VF551_V2-578`／`-580`（Radio 端「RVC display active」條件）得作
  `-010`／`-017`／`-023` 之 Pre-Condition 措辭來源，reasoning 註明出處。上游分類不重判。
```


### R-CAM10 — 多列共引同一來源時，SWE ID 較小者為承接列（Pei 裁，2026-09-16）

```text
R-CAM10  多列共引同一來源時，SWE ID 較小者為承接列
  A 本兩列以上共引同一 SYS-RA 來源時，該來源之驗證由 SWE ID 較小者承接；
  較大者不得再以該來源作 spec_reference 錨，reasoning 註明「委派 SWE-CAM-nnn」（§8.2.1）。
  `SWE-CAM-023` 與六列之交集依此全數委派，`-023` 只承接無他列覆蓋之來源。
  pilot 批實測後若有不合理之委派，重開歸 Pei。
```

### R-CAM11 — VF 家族之 specification_reference 格式（Pei 裁，2026-09-16）

```text
R-CAM11  VF551 家族之 spec_reference 寫法沿用 `features/vehicle_setting/delivered/` VF230 交付本
  （`FM-WI-FSM-036-A01 … SWQT_VF230_20260902.xlsx`）之實際格式，逐字同型；
  執行層先抄該本 M 欄 5 個樣本入上繳包，再據以改寫 Camera 之 VF 型錨。
  CFTS092 型維持 §10.7(a) `CFTS092-{ObjectID}`；HMI L&F 型維持 §10.7(b)。
```

**執行層落實（CAM-04 §2）**：VF230 本之實際格式為 **SYS2 `F` 欄之 VF anchor**
（`VF230_V1_PDT27_VF_6222`／`VF230_V1_PHDCC27_VF_8670`；457 列只有此兩種形態），
**非 SYS-RA ID**。Camera 之 VF 型錨因而改寫為各本之 F 欄逐字值：
`VF551_V2_PHDCC27_VF_nnn`／`VF551_V3_P363_VF_nnn`／`VF551_V33_P226MCA_VF_nnn`／
`VF551_V4_PHDCC27_VF_nnn`／`VF551_V42_P637MCA_VF_nnn`。
CFTS092 之 F 欄即 ObjectID，依 §10.7(a) 寫 `CFTS092-{ObjectID}`。

### R-CAM12 — CFTS092 疊層同句之取錨（Pei 裁，2026-09-16）

```text
R-CAM12  CFTS092 疊層同句之取錨
  CFTS092 於 Cargo/CHMSL（§1.3.5）、Rear Camera（§1.3.6）、Surround View（§1.3.7）、
  Forward Facing（§1.3.8）各節重複出現之逐字同句，Test Group = Rear View Camera 之 TC
  一律取 Rear Camera 節（`SYS-RA-CAM-070`～`-082`，ObjectID 4781635～4781647）之 ObjectID 為錨；
  其他節之同句不得作錨，reasoning 得互參。
```

**執行層落實（CAM-05 §1）**：CFTS092 之節界實測 ——
`SYS-RA-CAM-060`（4781625）`Cargo/CHMSL Camera`、
**`-070`（4781635）`Rear Camera`**、`-083`（4781648）`Surround View Camera`、
`-094`（4781659）`Forward Facing Camera`、`-100`（4781665）`Clearpath Camera`，
五者之 `Category` 皆為 `Heading`。
全本 `Functional Requirement` 列之逐字同句比對：Camera 節界範圍內**只有一組**
—— `SYS-RA-CAM-062`（4781627，Cargo 節）↔ **`SYS-RA-CAM-075`（4781640，Rear 節）**，
即本條所規範者。`NR1L-RVC-001` 之錨依此由 `CFTS092-4781627` 改為 **`CFTS092-4781640`**。

### R-CAM13 — 037 所引之來源一律拆解；§8.4.2 只擋「RD 未引」之外部規格（Pei 裁，2026-09-23）

```text
R-CAM13  037 所引之來源一律拆解；§8.4.2 只擋「RD 未引」之外部規格
  (a) SWE 列所引之每一 SYS-RA 來源（排除 Out of Scope 與 R-CAM10 委派者）皆須落入至少一個 TC 之
      驗證點；TC 作者不得以 Test Group／節別不符為由略過（§8.2 RD 為需求單位之權威）。
  (b) §8.4.2「不測外部規格」僅適用於 037 未引、只出現在被參考文件中之行為。
  (c) 節別與 Test Group 不符者（Cargo/CHMSL、SVC、FFC 節條文）落 Test Set `Auxiliary Cameras`，
      Pre-Condition 以 PROXI 表達該相機之配備（`Digital_CHMSL_Camera_Prsnt = 1`／
      `Surround_View_Camera = 1`／`Forward_Facing_Camera = 1`），reasoning 註明 Atl-Hi default 為 0。
  (d) VC／VM 欄不是來源；其內容對應得到所引來源者一併生成，對應不到者登 RD_FEEDBACK。
  審閱 §三-1「不生成」與 CAM-05 §3 之 A-CA28 處置作廢。
```

**執行層落實（CAM-06 §1）**：A-CA28 之 12 列全數改為生成，落 `batch01b/`，
Test Set `Auxiliary Cameras`，ID `NR1L-RVC-034` 起；逐列對應見
`features/camera/data/batch01b_plan.tsv`。
(c) 之三個 PROXI 參數之平台覆蓋為實測（`forms/proxi/` 六本）——
`Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）只存在於 Atl-Hi 兩本；
`Surround_View_Camera`／`Forward_Facing_Camera`（byte 177 bit 0／1）存在於
Atl-Hi 兩本與 `Promaster_ATL_MI`（637）、`Fastback_ATL_MI`（376），
**`Toro_ATL_MI`（2261）之 PROXI 表止於 byte 172，三個參數皆查無**；
六本之 default 值一律 `0 = Absent`。

### R-CAM13(d)（修訂，2026-09-23，Pei 裁：CAM-14 審閱 §一-2）

```text
R-CAM13(d)  R-CAM13(c) 所定之 Test Set 名 `Auxiliary Cameras` 改為 `Additional Cameras`。
  改名之由：A 本另有 Test Set `AUX Camera`（`SWE-CAM-024`，VF617_V5 之外接 AUX 輸入），
  兩名字面相近而域不同 —— `Additional Cameras` 指車上其他相機（Cargo/CHMSL、
  Surround View、Forward Facing、Clearpath），`AUX Camera` 指外接 AUX 輸入，
  與 B 本 `AUX Camera Access`／`AUX Camera Settings` 同義域，保留不動。
  R-CAM13(c) 之其餘內容（PROXI 前提、reasoning 註 Atl-Hi default 為 0）不變。
```

**原條 R-CAM13(c) 之逐字不動**（R-TM13／GCB-06：修訂段以同級錨自立，原條 fenced sha 不變）。

**執行層落實（CAM-15 §1-2）**：`test_set` 欄實測 **18 筆** json 改名
（`NR1L-RVC-034`～`-045`、`-048`、`-093`～`-097`），其 `.md` 由
`features/camera/scripts/render_tc.py` 重生；`framework.md` VIII.2 第 10 組、
`data/layer2_assign.tsv`、`data/batch02_plan.tsv`、`DATA_REQUESTS.md`（DR-CAM-j）、
`RD_FEEDBACK.md` 同步。`coverage.tsv` 無 `test_set` 欄，不受影響。
`docs/fw036/handoff/` 為唯讀史料，**不改**。

### R-CAM14 — 速度門檻之母錨 ＝ CFTS092-4781643（Pei 裁，2026-09-23）

```text
R-CAM14  速度門檻之母錨 = CFTS092-4781643
  Rear View Camera 之速度退出門檻（8 mph）以 `CFTS092-4781643`（SYS-RA-CAM-078）為錨，
  五車型以 R-CAM3(e) CAN source 行分寫訊息名（`BRAKE_FD_2` Atl-Hi／`BRAKE1` 376／
  `STATUS_CCAN3` 637, 2261），VF 條文留 reasoning 互參。
  2261 因 VF551_V33 為 `>(greater)` 而條文相異，維持分列（`-030`／`-031`）。
  `>` 與 `>=` 於 CAN 解析度不可判（A-CA30）之根本解列 RD_FEEDBACK（標定單位）。
```

**執行層落實（CAM-06 §2-3，CAM-07 §1 更正）**：`NR1L-RVC-009`／`-010` 之錨由
`VF551_V2_PHDCC27_VF_1577`（`SYS-RA-VF551_V2-490`）改為 **`CFTS092-4781643`**，
Vehicle Model 由 Atl-Hi 兩欄擴為 `HDCC27`／`DT27`／`376` **三欄**
（**637 與 2261 皆為 0**，由 `-030`／`-031` 承接 —— 二者之門檻皆為 `MAX_SPEED = 13,0 Km/h`）。
CAM-06 上繳時本段誤書為「四欄」，實際落檔一律為三欄；本輪更正，見上繳包 CAM-07 §5。

**本條 (b)／(c) 兩段之修訂依 R-TM13 以同級錨自立**（GCB-06 —— 寫在本標題下會改本條之
fenced sha）。原條文中關於 376 訊息名之一句依 R-TM13 加刪除線保留：

> 五車型以 R-CAM3(e) CAN source 行分寫訊息名（`BRAKE_FD_2` Atl-Hi／~~`BRAKE1` 376~~／
> `STATUS_CCAN3` 637, 2261）

**作廢理由**：`BRAKE1` 為 VF551_V3 之**文面名**，非可注入之 message ——
`forms/P363_BH-CAN [07338]_3A_R2.dbc`（376）全本無 `BRAKE1`，`VehicleSpeedVSOSig`
位於 `BO_ 994 STATUS_CCAN3`。見 R-CAM14(c)。

### R-CAM14(b)（增補，2026-09-23，Pei 裁：CAM-06 審閱 §二-1）

```text
R-CAM14(b)  637 之速度門檻併入 2261 之分列（`-030`／`-031`），不入 8 mph 之列。
  VF551_V42 之 `MAX_SPEED`（`SYS-RA-VF551_V42-655` 名／`-656` 值 `13,0`／`-659` 單位 `Km/h`）
  與 VF551_V33 同數同單位，觸發訊號同為 `STATUS_CCAN3.VehicleSpeedVSOSig`，
  故 `-030`／`-031` 之 Vehicle Model 加勾 `VF(ProMaster)637`，
  `specification_reference` 加第二行 `SYS-RA-VF551_V42-656` 之 anchor。
  V42 無速度退出條文（只有 reset 語意），reasoning 註明「以 V33 條文 ＋ V42 常數承載」。
  `-009`／`-010`（`c_VEHSPD_MAX = 8 mph`）因而只涵蓋 HDCC27／DT27／376。
```

### R-CAM14(c)（修訂，2026-09-23，Pei 裁：CAM-06 審閱 §二-2）

```text
R-CAM14(c)  訊息名以 DBC 為準（R-17）。
  376 之速度訊號寫 `STATUS_CCAN3.VehicleSpeedVSOSig`，不寫 `BRAKE1`；
  R-CAM3(e) 之 CAN source 行因而為兩分支而非三分支：
    `CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)`
  `BRAKE1` 為 VF551_V3 之文面名，留 reasoning 互參，不入工作簿任何欄。
  取代 R-CAM14 原文之「`BRAKE1` 376」一句。
```

### R-CAM10(b)（增補，2026-09-23，Pei 裁：CAM-06 審閱 §二-4）

```text
R-CAM10(b)  同一行為之 IF 來源與 THEN 來源分屬兩承接列時，合為一個 TC。
  `specification_reference` 以多行承載兩錨（selfcheck 第 1 項逐行反查，兩錨各須通過）；
  該 TC 歸 **SWE ID 較小之承接列**（req_id 取小者），
  另一列於 plan 與 reasoning 註明「委派 SWE-CAM-nnn」，不另出 TC。
  本段為 R-CAM10 之例外而非推翻：R-CAM10 管「同一來源不得兩列共錨」，
  本段管「同一行為之兩個來源不得拆成兩個半截 TC」。
  合一後之 verbatim 逾 50 token 且無法以保序子序列兼顧兩來源者，回退為兩 TC 並回報。
```

### R-CAM15 — Atl-Mi 三平台之車型歸屬判準（Pei 裁，2026-09-23：CAM-07 審閱 §一-5）

```text
R-CAM15  Atl-Mi 車型歸屬 —— V3 之母體為 376（`P363` anchor，R-CAM11）。
  同一驗證點上：
  (a) V42（637）與 V33（2261）皆無對應條文時，V3 列承 637／2261／376 三平台；
  (b) V42／V33 有對應條文時，V3 列只承 376，該兩平台各由其本之列承接；
  (c) V42 有而 V33 無時，V42 列承 637、V3 列承 376（2261 由該驗證點之 V33 列或不承）。
  文面即上繳包 CAM-07 §4-4 之三句。
```

**執行層落實（CAM-07 §3／CAM-08 §3）**：本條為既有作法之明文化，非新規 ——
batch01 之 `-012`／`-014`／`-016` 與 batch02a 之 `-050`（(c)：637 ＋ 376）、
`-054`／`-055`（(b)：只 376）、`-071`／`-072`（(a)：三平台）皆已依此。
自 batch02b 起為落檔前之逐列判準。


### R-CAM16 — 全來源委派之 SWE 列，其零 TC 非缺口（Pei 裁，2026-09-23：CAM-09 審閱 §一-3）

```text
R-CAM16  SWE 列之所有來源依 R-CAM10（含 (b)）委派他列者，其 TC 數為 0 而**非覆蓋缺口**。
  該列於 `features/camera/data/coverage.tsv` 記一行：
    disposition = `No TC — all sources delegated to SWE-CAM-nnn (R-CAM10)`，`tc_count = 0`。
  與 Heading 列之零 TC（`No TC — Heading; refer to child IDs`，R-BLM2／R-POP5 前例）
  並列為**兩種**零 TC 形制，不可混記：前者之行為已由承接列驗證，後者之行為在其子列。
```

**執行層落實（CAM-10 §1）**：A 本現有兩列適用 ——
`SWE-CAM-007`（唯一來源 `SYS-RA-VF551_V42-216` 委派 `SWE-CAM-006`）與
`SWE-CAM-013`（三個來源全數委派 `SWE-CAM-004`）。
`coverage.tsv` 於本輪新建（A 本 25 列全量），兩列依本條記載。


### R-CAM16(b)（增補，2026-09-23，Pei 裁：CAM-16 審閱 §一-1）

```text
R-CAM16(b)  零 TC 之**第三種形制**：來源列之 `Description` **自陳無需求**
  （`N/A`／`Not applicable`／空）者，其 TC 數為 0 而非覆蓋缺口。
  該列於 `coverage`（A 本 `coverage.tsv`／B 本 `coverage_b.tsv`）記一行：
    disposition = `No TC — source states N/A (A-CAnn)`，`tc_count = 0`。
  **不得**與 R-CAM16 之委派形制或 Heading 形制混記 —— 三者之成因相異：
    委派：行為已由承接列驗證；Heading：行為在其子列；**自陳 N/A：來源明言無此需求**。
  同時登 RDF，指出 037 不應將該列列為 leaf（`Categorization` 應為 Heading 或 Out of scope）。
```

**原條 R-CAM16 之逐字不動**（R-TM13／GCB-06：修訂段以同級錨自立）。

**執行層落實（CAM-16／CAM-17）**：B 本 `SWE1-RVC-069`（SYS1 §27.3.2，`NRL-188058`）——
其 Description 全文 4 token `First surface needs: N/A`（依 profile §7.7 取全文實測）。
`coverage_b.tsv` 依本款記載；**RDF-12** 同時登。

### R-CAM17 — 量測主張須附證據（Pei 裁，2026-09-23：CAM-12 審閱 §二-1）

```text
R-CAM17  上繳包中任何「查無／零命中／全等／逐字相符」之主張，須附四項：
  (a) 掃描字串（逐字，含是否分大小寫）；
  (b) 母體之檔名或目錄（含本數）；
  (c) 所用之命令或工具；
  (d) 命中數。
  無上述證據之主張**視同未量測**，審閱不採。
  分析層每包隨機複驗至少一項。
  立條之由：CAM-11 上繳 §3-3／§4-2 之「Atl-Hi 三本 PROXI 掃描零命中」為未執行之量測，
  CAM-12 重掃即查得（`Steering_Ratio_Rack_Pinion_Type`，byte 88 bit 0–1，三本 row 410）。
```

**執行層落實（CAM-13）**：本包所有「查無」主張逐項附證據，見上繳包 §5。
併登 `GC_BACKLOG.md` **GCB-08**，提請入全域 ledger。


### R-CAM18 — B 本之 `Vehicle Model` 七欄以「可佈性」判（Pei 裁，2026-09-23：CAM-14 審閱 §一-5）

```text
R-CAM18  B 本（SYS1 HMI）之條文不帶平台維度（無 `PHDCC27`／`P637MCA` 之類之錨），
  故 R-CAM3 之車型軸於 B 本改由**可佈性**判：
  (a) 預設 —— 五款已出資平台（HDCC27、DT27、637、2261、376）皆 `1`；
  (b) 該列之 PROXI 前提所用之 byte 於該平台之 PROXI 本**不存在** -> 該欄 `0`；
  (c) 該列之觸發訊號於該平台之 DBC **不存在**（沿 A 本已定之 message 對照，R-CAM1(b)）
      -> 該欄 `0`；
  (d) (b)／(c) 判 `0` 者，該列之 reasoning 須**具名證據**（掃描字串、母體本數、命令、
      命中數；R-CAM17）；
  (e) `Commander (598)`／`Regengade (5210)` 恆 `0`（R-CAM2 不變）。
  A 本不受本條影響 —— 其車型軸仍由 SYS2 之平台錨直接判（R-CAM3）。
```

**執行層落實（CAM-14／CAM-15）**：B01a 22 列中 19 列五款全 `1`；3 列
（`NR1L-RVCHMI-008`／`-012`／`-014`）因 `Toro_ATL_MI` 之 2019 本缺 byte 177
（`Surround_View_Camera`／`Forward_Facing_Camera`，**DR-CAM-l**）而 `Toro(2261)` = `0`。
DECISIONS **6-51** 由 `[PROPOSED]` 轉 `[DECIDED]`。

---

## 平台 ↔ VF ↔ PROXI 對照（下放包 §2 附表，分析層實測 `forms/proxi/` 六本）

| Vehicle Model 欄 | forms/proxi | VF551 | EE |
|---|---|---|---|
| HDCC27 Atl-Hi | `HDCC28_ATL_HI`／`HDCC27_initial` | V2 (`PHDCC27` anchor)／V4 | Atl-Hi |
| DT27 Atl-Hi | `DT28_ATL_HI` | V2 (`PDT27` anchor) | Atl-Hi |
| 637 Atl-Mi | `Promaster_ATL_MI` | V42 | Atl-Mi |
| 2261 Atl-Mi | `Toro_ATL_MI` | V33 | Atl-Mi |
| 376 Atl-Mi | `Fastback_ATL_MI` | V3 | Atl-Mi |
| 598／5210 | 無 | 無 | 一律 0 |

## 執行層回報（CAM-02，2026-09-16）

- R-G23 取號現查：本檔現有 `### R-CAM1`～`R-CAM3`，全 repo 無 `R-CAM4` 以上；
  `docs/fw036/RULINGS.sha.tsv` 無 `R-CAM` 列（該表未重生）。`{live}` = 4 成立。
  下放包 CAM-02 §1 之五條實際號為 **R-CAM4／R-CAM5／R-CAM6／R-CAM7／R-CAM8**；
  同 §1 末之「Out of Scope 來源之處置」條下放包未給 `{live+n}` 佔位，
  執行層依落檔順序取 **R-CAM9**（下放包 §1 五個 code block 之後、
  「裁定 6／9／10 為 DECISIONS 項」之前，故列為第六條）。
- **R-CAM4(a) 取代 CAM-01 之 Layer 1 提案**：Test Group 由 `Camera` 改為
  `Rear View Camera`，兩本同值。CAM-01 DECISIONS §6-1／§6-2 之提案作廢。

## 執行層回報（CAM-01，2026-09-16）

- R-G23 取號現查：`grep -rn "R-CAM"` 於全 repo（排除本包下放檔）無命中；
  `docs/fw036/RULINGS.sha.tsv` 之 prefix 清單為 `R-AM R-C R-DD R-G R-ICS R-PH
  R-PMH R-POP R-TM R-U R-VF R-VL R-VS R-VT`，無 `R-CAM`。`{live}` = 1 成立，
  三條實際號為 **R-CAM1／R-CAM2／R-CAM3**。
