# 上繳 18（B、C）— 第二批取樣清單與承前確認

- 產出層：執行層｜2026-08-18｜對象：分析層
- **未生成** —— 取樣清單先回報（18 包作業 B 明文）
- **本輪未執行任何 git**；**未寫回工作簿**

---

## 1. 範圍：ch12 → ch13 → ch14，**29 leaf**

| 章 | Test Set | 總 leaf | pilot 已生成 | 本批 | 批後 |
|---|---|---|---|---|---|
| 12 | Valet Mode | 25 | 1（`128-01`）| 24 | 完成 |
| 13 | Valet Mode | 4 | 1（`132-02`）| 3 | 完成 |
| 14 | Valet Mode | 2 | 0 | 2 | 完成 |
| | **合計** | **31** | **2** | **29** | **Valet Mode 100%** |

**批界同第一批之原則**：本批做完，`Valet Mode` 這個 Test Set 收乾淨，
不留零頭跨批。**做完後 180 leaf 之覆蓋為 16＋27＋29＝72，餘 108。**

## 2. 條數估計：**約 34 條**（**未逾 40，故不提分批**）

| 項 | 數 | 依據 |
|---|---|---|
| leaf | 29 | 一葉一 TC（§8.2.1）之下限 |
| **可能之拆分** | ＋2 | `113`（12.1 儲存／重設為兩觸發）、`129`（12.10 未滿 4 碼變灰／按下發 bonk 為兩觸發）—— §5.7 |
| **§7 負向配對** | ＋3 | `125-02`（Projection／HFP／VR）、`126-01`（特定選單區）、`126-02`（狀態列限制）—— 三者皆為**列舉式支援項**，canon §7 明文須配至少一條反面 |
| 估計 | **≈ 34** | |

**未逾 40，故不提分批建議。**
惟若覆核時認為下列任一成立，條數會過 40，屆時應以 **ch12 / ch13＋14** 切兩批
（12.1–12.10 為 PIN 與鎖定之完整邏輯，13–14 為 SPAAK 與 welcome popup，
**切在 12/13 之間不會切斷任何一組邏輯**）：

1. `125-01`～`125-04`、`126-01`～`126-03` 各自再需負向配對（＋4）
2. `117`／`118` 之 PIN 啟用與停用各需正反兩條（＋2）
3. `128-02`／`128-03` 之 30 分鐘鎖定需時間邊界前後各一（＋2）

## 2.1 取樣清單（29 leaf，依章節連續排序）

| # | req_id | sec | Sub | 037 Prio | 標題 | 註 |
|---|---|---|---|---|---|---|
| 1 | `SWE1-HMI-PROF-113` | 12.1 | HMI | High | Valet Mode Preferences Store and Reset Logic | **可能拆 2**（儲存與重設為兩個觸發） |
| 2 | `SWE1-HMI-PROF-114` | 12.1.1 | HMI | Medium | Restore Default Status Bar in Valet Mode | — |
| 3 | `SWE1-HMI-PROF-115` | 12.2 | HMI | High | Activate Valet Mode Only via All Profiles Tab | — |
| 4 | `SWE1-HMI-PROF-116` | 12.2.1 | HMI | High | Disable Valet Mode Activation in Motion | — |
| 5 | `SWE1-HMI-PROF-117` | 12.3 | HMI | High | 4-Digit PIN Required to Activate Valet Mode | 與 118 為啟用／停用之配對 |
| 6 | `SWE1-HMI-PROF-118` | 12.3.1 | HMI | High | Same 4-Digit PIN to Deactivate Valet Mode | 與 117 之配對；PIN 相同為其斷言 |
| 7 | `SWE1-HMI-PROF-119` | 12.3.2 | Service | Medium | Disconnecting Battery Resets Valet Mode | `Service` 群 —— 斷電後之重設，需 key cycle 級操作 |
| 8 | `SWE1-HMI-PROF-120` | 12.3.3 | HMI | High | Return to Previous Profile After Valet Mode Exit | — |
| 9 | `SWE1-HMI-PROF-121` | 12.4 | HMI | Low | Press Elsewhere to Cancel Valet PIN Entry | — |
| 10 | `SWE1-HMI-PROF-122` | 12.5 | HMI | High | Status Bar Shows Lock Icon for Valet Mode | — |
| 11 | `SWE1-HMI-PROF-123` | 12.6 | HMI | Medium | Prompt to Deactivate on Valet Icon Press | — |
| 12 | `SWE1-HMI-PROF-124` | 12.7 | Service | High | Seat Buttons Change Pos. but Don't Load Profile in Valet Mode | `Service` 群 |
| 13 | `SWE1-HMI-PROF-125-01` | 12.8 | HMI | High | Device Manager Disabled in Valet Mode | — |
| 14 | `SWE1-HMI-PROF-125-02` | 12.8 | HMI | High | Disable Projection, HFP, and VR in Valet Mode | **列舉式**（Projection／HFP／VR）→ §7 需負向配對 |
| 15 | `SWE1-HMI-PROF-125-03` | 12.8 | HMI | High | Glove Box Lock Prompt on Valet Mode Entry | — |
| 16 | `SWE1-HMI-PROF-125-04` | 12.8 | HMI | Medium | Glove Box Lock Button Greyed Out in Valet Mode | — |
| 17 | `SWE1-HMI-PROF-126-01` | 12.8.1 | HMI | Medium | Lock Out Specific Menu Areas in Valet Mode | **列舉式**（特定選單區）→ §7 需負向配對 |
| 18 | `SWE1-HMI-PROF-126-02` | 12.8.1 | HMI | Medium | Status Bar Restrictions and Grey Out in Valet Mode | **列舉式**（狀態列限制）→ §7 需負向配對 |
| 19 | `SWE1-HMI-PROF-126-03` | 12.8.1 | HMI | Medium | Electronic Glove Box Lock Logic in Valet Mode | — |
| 20 | `SWE1-HMI-PROF-127` | 12.8.2 | Service | Medium | Restore Glove Box State on Valet Mode Deactivation | `Service` 群 |
| 21 | `SWE1-HMI-PROF-128-02` | 12.9 | HMI | High | PIN Entry Blocked During 30-Minute Lockout | 與 pilot 之 015（12.9 第 10 次）同節；鎖定中 |
| 22 | `SWE1-HMI-PROF-128-03` | 12.9 | HMI | High | Restore PIN Entry After 30-Minute Lockout | 同上；鎖定解除 |
| 23 | `SWE1-HMI-PROF-129` | 12.10 | HMI | Medium | Grey Out Go Button Until 4 Digits & Bonk on Press | **可能拆 2**（未滿 4 碼變灰／按下發 bonk 為兩觸發） |
| 24 | `SWE1-HMI-PROF-130` | 12.10.1 | HMI | Low | Grey Out Numeric Buttons After 4 Digits Entered | — |
| 25 | `SWE1-HMI-PROF-131` | 13.1 | Service | High | (SPAAK) Auto-Activate Valet Mode Without PIN | SPAAK 群；與 132-01／133 同組 |
| 26 | `SWE1-HMI-PROF-132-01` | 13.2 | HMI | High | (SPAAK) Block All Head Unit Valet Exit Options | 與 pilot 之 016（13.2）同節之另一 leaf |
| 27 | `SWE1-HMI-PROF-133` | 13.3 | HMI | Medium | (SPAAK) PU1573 on Valet Profile Icon Press | — |
| 28 | `SWE1-HMI-PROF-134` | 14.1 | HMI | High | Welcome Popup Shows Valet Mode and Deactivate Button | **R-U51 口徑之受測對象**（`Exit Valet Mode process above`） |
| 29 | `SWE1-HMI-PROF-135` | 14.2 | HMI | High | Cannot Deactivate Valet Mode While in Motion | — |

## 3. 三項必含之確認（比照前例具名）

### 3.1 must_carry 待追蹤項 —— **現況確為 0**（已實測，非推定）

```
9.8    已覆蓋 TC-012
9.3.2  已覆蓋 TC-011, TC-023
9.1    已覆蓋 TC-017
11.4   已覆蓋 TC-013, TC-044
11.5   已覆蓋 TC-014, TC-042, TC-043
p17    已覆蓋 TC-013, TC-014, TC-042, TC-043, TC-044
p14    已覆蓋 TC-017
待追蹤 = 0
```

**七條全數已被實際注入**（非「掛得上」，是「某條 TC 真的帶了它」）。
**本批無 must_carry** —— `must_carry_for()` 對 ch12–14 各節皆回傳空。

### 3.2 §7 列舉配對 —— **三處，已列於清單之註欄**

`125-02`（Projection／HFP／VR）、`126-01`（特定選單區）、`126-02`（狀態列限制）
三者皆為「列舉受限項目」之形態，依 canon §7
「Enumerated supported items → ALWAYS pair with at least one unsupported negative」
須各配一條反面（**在 Valet Mode 下仍可用之項目**）。

**本批之列舉配對可自足**：不需跨批，反面之對象就在同節之條文裡。

### 3.3 R-U51／R-U46 口徑之受測對象

- **R-U51（位置指涉）**：`134`（14.1）之條文為
  `…will initiate the Exit Valet Mode process **above**` ——
  11 輪盲區掃描之 17 條命中之一，當時判為「指向 14.x 之流程，非 PLP 表」。
  **本批將首次以 TC 檢驗該判讀之後果**。
- **R-U46（PLP 併列）**：ch12–14 **無** PLP leaf（`PLP_LEAVES` 六條皆在 ch4／ch5），
  故本批**無 3.x 併列**。

## 4. 本批之已知風險（生成前須知）

| # | 事項 | 說明 |
|---|---|---|
| 1 | **`Service` 群三條**（`119`／`124`／`127`）| 需 key cycle 級或斷電級操作。`119`（斷電重設 Valet Mode）之觀察點將再次落入 **R-U21 之「裁決來源」**（同 `ignition cycle`）—— 生成時須依 J-4 標示 |
| 2 | **30 分鐘鎖定**（`128-02`／`128-03`）| 其驗證需實際等待 30 分鐘。`128-03`（鎖定解除）**無法在合理時間內執行** —— 建議生成時於 remarks 具名其執行成本，或提請以縮時手段替代（屬 Pei 之裁定範圍）|
| 3 | **PIN 為安全機制** | `117`／`118`／`128-02` 之失效後果為 **Valet Mode 可被繞過** → 依 D-UP16-01 判 **P0**。本批之 P0 比例會顯著高於前兩批 |
| 4 | **SPAAK 群**（`131`／`132-01`／`133`）| 與 pilot 之 `016`（13.2）同組。`132-01` 與 `016` 同節不同 leaf —— **sibling tc_title 不得雷同**（G5）|
| 5 | **12.8／12.8.1 之七個 sub-id** | `125-01`～`-04`、`126-01`～`-03` 語意相近（皆為「Valet Mode 下某功能被禁」）—— **§8.3 sibling 軸辨識之最大壓力點**，G5 會擋雷同標題 |
| 6 | **R-U5 之 rubric 無安全帶**（17 輪 §4 第 1 項之待裁）| 本批幾乎每一條都涉「行車安全／防盜」之後果，**該待裁項在本批之影響遠大於第一批**。建議在本批生成前裁 |

## 5. 作業 C —— 承前確認

### 5.1 兩份清單之一致性檢查 —— **已有**

`gen_batch01.build()` 於生成前比對 `data/batch01_sample.tsv` 與 `TCS` 之鍵，
不一致即 `SystemExit` 並列出兩向差集：

```python
ids = sample()
if sorted(ids) != sorted(TCS):
    raise SystemExit(f"取樣清單與內容不一致：TSV {len(ids)} vs TCS {len(TCS)}\n"
                     f"  TSV 有而 TCS 無：…\n  TCS 有而 TSV 無：…")
```

與 `gen_pilot` 之作法相同（該處比對 `pilot_sample.tsv` 與 `SAMPLE_IDS`）。
**兩者之差別**：pilot 比對之對象為**順序敏感**（`tsv != SAMPLE_IDS`），
batch01 為**集合**（`sorted(ids) != sorted(TCS)`）——
因 batch01 之 tc_id 依 TSV 之列序指派，而內容以 dict 承載，**集合一致即可**。

### 5.2 16 輪 §6.5 風險④⑤⑥ —— 已於上繳 17 §3.4 回報

| # | 事項 | 結果（17 輪 §3.4）|
|---|---|---|
| ④ | `112-02`／`-03` 與 `112-01` 之列舉完整性 | 三條齊備，G5 未觸發，pre-condition 互斥 |
| ⑤ | `PROF-085` 之 must_carry 兩條是否真注入 | **是**（9.1 ＋ p14），T-1／T-2 於第一批首次成立 |
| ⑥ | ch12–14 未納入 | 維持，即本批 |

---

## 6. 獨立判斷

| # | 項 | 說明 |
|---|---|---|
| 1 | **`128-03` 之 30 分鐘等待** | 這條 TC 寫得出來，但**跑不動**。寫一條沒人會執行的 TC 與寫一條錯的 TC，代價不同但都不是零 —— **建議在生成前裁其處置**（照寫並註明成本／改以縮時／不生成並登記）|
| 2 | **P0 比例將顯著上升** | 依 D-UP16-01 之 tie-break，PIN 與鎖定類皆為「核心能力被繞過」。**若 29 條裡有一半是 P0，那個 rubric 的分辨力就要重新檢視** —— 這是估計，生成後才有實數 |
| 3 | **R-U5 無安全帶之待裁在本批放大** | 見 §4 第 6 項。第一批只有 `089` 一條受影響，本批可能十條以上 |
| 4 | **本批估計 34 條為推估** | §2 之「可能拆分」與「§7 配對」皆為生成前之判斷，**實數以生成時之切分為準**（16 輪估 28–34、實得 28，該次偏高）|
| 5 | **`134` 之 R-U51 判讀將首次受檢** | 11 輪判「above 指 14.x 之流程」，該判讀至今未被任何 TC 檢驗過 |
