# 下放包 04 —— priority 對映草案（待裁）、profile 草案（待裁）、T9 訊號寫法前置

- 日期：2026-08-27
- 方向：分析層 → Pei（§一、§二 待裁）＋ 執行層（T9）
- 前一包：`03_review_close.md`（framework 鎖定已准）
- 依據素材：037 28 leaf 全文、HMI spec p3–p7（Standard Lockout Popup、
  Fullscreen Lockout 流程、Driver Lockout Tables 與 R1L 適用性註記）
- 落檔註記：本包首次寫入於 MCP 逾時中失敗（get_file_info 驗 ENOENT），
  本檔為重寫，內容與首寫同稿

---

## 一、priority 對映草案（IN §10.2；037 為 28/28 High，須落 P0–P3）

### 判準（規則式，非逐列心證）

```
PR-a  進鎖方向之常態路徑（RESTRICTED 之施加或其 HMI 強制，常態輸入）→ P0
      理由：其失效 = 行駛/非停妥狀態下受禁 feature 可操作，即本 feature
      之危害本體（IN §10.2 P0「safety」）。
PR-b  fail-safe 例外路徑（輸入失效 → RESTRICTED）→ P1
      理由：安全向失效補位，屬 major operational logic；其常態前提
      （PR-a 各列）已為 P0。
PR-c  解鎖方向常態、初始化、監看能力 → P1
      理由：失效方向為過度鎖定（可用性損失），非危害。
本 feature 無 P2/P3 —— 全域屬法規安全域，037 全 High 與此一致。
```

### 逐 leaf 表

| P | leaf | 內容 |
|---|---|---|
| **P0**(8) | 007 | ≥5MPH → RESTRICTED |
| | 009 | RESTRICTED 下存取受阻 |
| | 011 | 使用中轉 RESTRICTED → lockout 通知 |
| | 013, 015 | Lockout Table L/O 逐項施加（-120/-121） |
| | 019 | HK 自排非 P → RESTRICTED |
| | 023 | HK 手排手煞 OFF → RESTRICTED |
| | 025 | 速度 ≥5MPH → RESTRICTED（**凍結中**，priority 先掛草案值） |
| **P1**(20) | 004, 006, 008, 010, 012, 014, 016 | fail-safe（訊號失效 → RESTRICTED） |
| | 018, 020, 022, 024, 026, 028 | HK/市場 fail-safe（026/028 凍結中） |
| | 001, 002 | Body OFF 初始化（NOT_RESTRICTED） |
| | 003 | 監看能力（5/3 規則之整合面；轉移本體由 115/116 各自持有） |
| | 005 | ≤3MPH → NOT_RESTRICTED |
| | 017, 021 | HK 解鎖常態（P 檔／手煞 ON） |
| | 027 | ≤3MPH → NOT_RESTRICTED（凍結中） |

閉合：8 + 20 = 28 ✅

---

## 二、profile 草案（`docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md`；准後落檔）

### §1 spec_reference（IN §10.7(a)，無 override）

`CFTS022-{ObjectID}`，一行一 ObjectID、同 TC 內升冪。雙引 leaf
（-017~-028）：閘 `CFTS022-4915120` 一行 ＋ 條文 ObjectID 一行。

### §2 R-DD3 細則（ER 之 HMI 錨）

**觀察面 A（主）—— 存取阻擋**：對 Lockout Table 標 `L/O` 之 feature
發起存取，ER 斷言「該 feature 未被開啟／存取被阻」。
feature 之取樣以 HMI spec p7 `Driver Lockout Tables` 為準，並受其
R1L 註記拘束：黃標項不適用 R1L、Embedded NAV 僅 LATAM、VR/TTS
僅隨 Embedded NAV。**取樣 feature 於 TC 內具名**（如
`Destination Entry`、`Pairing (1st time)`），不得寫「some restricted feature」。

**觀察面 B —— lockout 通知**：leaf 011 之 notification 斷言錨定
`Standard Lockout Popup`，其字串逐字取 spec p4：
`Feature not available while the vehicle is in motion.`
引用時 `"..."` 雙引號（IN §11）。

**降階規則（R-DD3(b) 之落地）**：
- `notifies the subscribed Listener` / `DD Service outputs RESTRICTED`
  等軟體層敘述**不入 ER**；ER 以觀察面 A/B 之 HMI 反應斷言。
- `RESTRICTED` / `NOT_RESTRICTED` / `Locked` / `Unlocked` 四詞
  **均不出現於 ER**（A-DD3 已結）；test_item 上半 verbatim 照 037，不改字。

**§8.4.2 界線（硬）**：HMI spec 之 PC1–PC4（安全帶、乘客偵測）、
乘客確認 popup 流程（`Are you the passenger?` 分支、UF1/UF2 解鎖）、
Level 3 ADAS 分支 —— **皆非本 28 leaf 所有**，TC 不得引入其邏輯、
不得以其為 Pre-Condition。Fullscreen Lockout 畫面僅得作
reaction presence 錨（「lockout 畫面出現」），不得斷言其分支決策。

### §3 訊號施加寫法（IN §8.7.5；LID 對應自上繳包 01 T6）

| 037 之 `$…$` | 施加路徑 | 寫法 |
|---|---|---|
| `$Speedometer$` | CAN：LID r1738 → `GW_C1.VEH_SPEED`（CAN-B） | `Send the signal $GW_C1.VEH_SPEED$ = <raw> (<label>)`，raw/label 待 T9 對 DBC 實測 |
| `$VC_Trans_Equipped$` | CAN：LID r421 → `VehCfg7.VC_Trans_Equipped` | 同上，待 T9 |
| `$PresentGear$` | CAN：LID r1397 → `GW_C1.Gr` | 同上，待 T9 |
| `$PARK_BRK_EGD$` | **DR-DD2 未結** —— 保留來源名，步驟依 §8.7.5(d) 寫 `Drive PARK_BRK_EGD from <值> to <值>` 形式 | 定名後改 CAN 寫法 |
| `$Country_Code$` | PROXI：LID r43 → `Car_Configuration_16.Country_Code` | `PROXI Country_Code = <HK 值>`，HK 列舉值待 T9 |

5/3 MPH 為 spec 值（§8.7.1 具名門檻）；**raw 編碼一律 T9 查得，
不得換算臆填**（§8.4.1）。

### §4 pilot 提案

pilot 批 = **組 3 `Lockout Enforcement`（leaf 009–012，4 leaf）**。
理由：同時演練訊號施加（signal simulation）、觀察面 A/B、
fail-safe 形態 —— R-DD3 全部細則在此一組內受檢。

---

## 三、T9（執行層；priority/profile 裁定不阻此）

| # | 任務 |
|---|---|
| T9a | 對四庫之 DBC（R-DD5 綁定件）查 `GW_C1.VEH_SPEED`、`VehCfg7.VC_Trans_Equipped`、`GW_C1.Gr`、`STATUS_BH_BCM1.ParkBrakeSts`／`BCM_FD_9.ParkBrakeSts`（A-DD2 之候選對應，僅查證不採用）：逐訊號輸出 BO_ 歸屬、位長、scaling、`VAL_` 列舉逐字。查無者列表 |
| T9b | PROXI 檔查 `Country_Code` 值域，輸出 Hong Kong 之列舉值（查無 → 列 DR 候選，分析層擬 DR-DD3） |
| T9c | 5/3 MPH 對 `GW_C1.VEH_SPEED` 之 raw 換算**只列 DBC factor/offset 原值**，換算式與結果由分析層覆核後入 profile —— 執行層不逕填 TC 值 |

## 四、待 Pei 裁

1. §一 priority 表（規則 PR-a/b/c ＋ 28 列配置）
2. §二 profile 草案（准後分析層落 `docs/runtime/profiles/FW036_R1L_DriverDistraction_Profile.md`）
3. §二 §4 pilot = 組 3

## 五、上繳包要求（`docs/upstream/03_signal_binding.md`）

T9a–c 原始輸出、未結 DR 清單、獨立自評、量測條件揭露（R-G8）。
