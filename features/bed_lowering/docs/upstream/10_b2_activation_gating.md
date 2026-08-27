# 上繳包 10 — Bed Lowering Mode：B2 批（Activation Gating，28 leaf）

日期：2026-08-27
對應下放包：`features/bed_lowering/docs/handoff/10_b2_activation_gating.md`
（sha256 `9891bfa1cd4a93cc856fec3d50f822630464876d16f738a9fcf802a759aaac3c`）
執行層：Tier 1

**結論：B2 二十八條生成完成，26 條寫回（列 29–54），2 條依 IN §8.4.3 保留。
機檢與交付 lint（全簿 45 列）皆 clean。§〇 B1 收尾已做。
一項須具名交審：006／020 兩對之步驟逐字相同（037 本身之重複，未製造差異）。**

---

## 〇、B1 收尾

`b1_tcs.json` 批次層 `reasoning` 第二句已改為 HU 按鍵入口之描述，
與九條現行內容一致。TC 本文未動，未重驗全批。

- `b1_tcs.json` → `2033c81b44b450bd32e3038f0c26a3594538f6d746715562c0de621a006b8fc1`
- `B1/manifest.json` → `7b8787a4b0b342b9416c3d98b547f7a30c043a33bc7b505d1a56616ad92276b8`（含 `reasoning_corrected` 留痕）

---

## 一、範圍

`Activation Gating`，母號 005／006／007／020／024／042，
**28 leaf（Service 21／HMI 7）**，以 `test_set_map.tsv` 整組取用，未手挑。
機器複核：批內 28 個 req_id 與 context 之 28 leaf **集合完全一致**（assert）。

母號分佈實測：005×4、006×5、007×4、020×5、024×7、042×3 = 28。

**042 不是 Telematics/遠端類**（下放包 §二-4 之條件性提醒未觸發）——
實讀其三條皆為 ignition 完全 OFF 之可及性，走 HMI 與 ignition 訊號即可。

---

## 二、DR-1 命中 —— **實測 2 條，估算消掉 2 條**

下放包要求「逐列確認實際命中數」。結果：

| leaf | 速度語彙 | 判定 |
|---|---|---|
| 007-03 | `upper vehicle-speed threshold` | **PENDING** |
| 007-04 | `defined XX MPH threshold` | **PENDING** |
| 007-01 | 檔位條件，無速度 | 不需 |
| 007-02 | 監看行為，無門檻值 | 不需 |
| 006-03／006-05／020-03／020-05／024-04 | `0 MPH` | **具體值，不需 DR** |

DR-1 影響清單原載 `BLM-007-01~04`（4 條），**實測命中 2 條**。
`0 MPH` 是規格給定之具體值，不是缺件 —— 兩者都寫「MPH」，
但一個有值一個沒有，逐列讀才分得出來。

含 PENDING 之二條**不入寫回**（IN §8.4.3），`--skip-pending` 顯式回報：

```
IN §8.4.3 保留不寫回 2 條: ['SWE1-HMI-BLM-007-03', 'SWE1-HMI-BLM-007-04']
```

---

## 三、訊號預查 —— 全部查有

依 B1 教訓先自 LID 英文描述查，再回 DBC 定實名：

| 訊號 | 訊息 | tx | 列舉（節錄）|
|---|---|---|---|
| `$BCM_FD_2.OperationalModeSts$` | 0x100 | SGW | `1 Ignition_Off_WithoutKey`／`2 Ignition_Off`／`4 Ignition_On`／`8 Ignition_On_EngOn` |
| `$ENGINE_FD_2.EngineSts_W$` | 0x106 | SGW | `0 Engine_Off`／`1 Engine_Cranking`／`2 Engine_On` |
| `$TRANSM_FD_4.GearEngaged$` | 0x5AA | SGW | `0 Neutral`／`1..9 ForwardGear_n`／`13 Parking`／`14 ReverseGear` |
| `$BRAKE_FD_2.VehicleSpeedVSOSig$` | 0x102 | SGW | 物理值，單位 Km/h（沿 B1）|
| `$ASCM_FD_2.BDL_Enbl$` | 0x5A5 | SGW | `0 FALSE`／`1 TRUE` —— **僅觀察，不注入** |

**`OperationalModeSts` 一支訊號同時給出四個本批需要的狀態**，
這件事直接決定了 §四之兩處 trigger 區分能否成立 —— 若只有「ignition on/off」
兩態，005-03 與 042-01 就分不開，得退回 R-BLM13(a)。

### 入口紀律（B1 教訓，全批適用）

28 條**無一條注入 `$ASCM_FD_2.BDL_Enbl$`**。進入與觸發一律走：
ignition／速度／檔位訊號（他節點，可注入）→ HU 按鍵 → 觀察 `BDL_Enbl`。
已機器複核：批內無任何 `Send the signal $ASCM_FD_2.BDL_Enbl$`。

---

## 四、R-BLM13 之適用 —— (c) 兩處成立，(a) 三處

| leaf | 分支 | 依據 |
|---|---|---|
| 005-03 | **(c)** | trigger = `OperationalModeSts` **2 (Ignition_Off)**，鑰匙在位之熄火 |
| 042-01 | **(c)** | trigger = **1 (Ignition_Off_WithoutKey)**，完全斷電 |
| 005-04 | **(c)** | trigger = **4 (Ignition_On)** 且 `EngineSts_W` = 0，與 005-03 之 ignition 本身 OFF 可分 |
| 042-02 | (a) | 與 042-01 同 trigger。042-01 斷言「入口不存在」，本條斷言「按下去也不啟用」|
| 042-03 | (a) | 同 trigger，觀察面錯開：042-01 看 Controls tab，本條看 Apps menu 清單 |
| 007-03 | (a) | 與 007-04 同 trigger（速度達門檻）。本條斷言值「有變化」，不斷言終態 |

**(c) 能成立完全靠 DBC 列舉分得出四個 ignition 狀態** ——
若列舉只有 on/off，005-03 與 042-01 就只能用 (a)。
這是「先查訊號再定界」帶來的實際好處，記於此。

---

## 五、**須具名交審：006／020 兩對步驟逐字相同**

全批 28 條括號下半**相異數 28**，唯一性成立。但逐對比對高風險組時：

| 對 | 下半 | Final 步 | Procedure |
|---|---|---|---|
| 006-03 vs 020-03 | 不同 | **相同** | **逐字相同** |
| 006-05 vs 020-05 | 不同 | **相同** | **逐字相同** |
| 006-02 vs 020-02 | 不同 | 相同 | 不同 |
| 006-04 vs 020-04 | 不同 | 相同 | 不同 |
| 006-01 vs 020-01 | 不同 | 相同 | 不同（檔位取值不同）|

**成因是上游**：037 之 006 群（`Bed Lowering request`）與 020 群
（`Bed Lowering Mode enable request`）在「靜止／0 MPH／任意檔位」三條件上
逐條對應，是 037 自身之重複，不是本批之切分問題。

**處置：未合併，亦未製造差異。**

- 未合併：IN §8.2.1 尊重上游分解，合併等於替上游決定兩條 leaf 是一條。
- **未製造差異**：我可以讓 020-03 改用 2 Km/h 而非 1 Km/h，自查就會全綠 ——
  但那等於憑空造出上游沒有的區分，讓一份「看起來有兩種覆蓋」的交付本
  掩蓋「其實測的是同一件事」。**為了讓自查變綠而改測試值，
  正是這個專案一路在防的那種「看起來合理、不會自曝」的形態。**

交由分析層裁：保留兩對、合併、或以不同邊界值換取實際覆蓋增益（後者為裁定，非執行層可自取）。

---

## 六、機檢與寫回

```
TC 數 28
N 欄相異值數 1  (R-BLM5 預期 1)
priority 分布 {'P1': 25, 'P2': 3}
design_method 分布 {'Negative / Invalid': 10, 'Boundary Value Analysis': 5,
                    'Functional Based': 5, 'Decision Table': 4,
                    'Equivalence Partitioning': 2, 'State Transition': 2}
Input Test Data == NA 之比例 28/28
機檢項全數 PASS
§5.2 長度／§5.1 主動詞／ER 1:1 全批 PASS
```

寫回：

| 項 | 值 |
|---|---|
| 輸出 | `workbook/bed_lowering_05.xlsx` sha256 `c6593bb061be1815a47e4765f5716f75d419deaca9542512c56b90e8133caf74` |
| 列 | 29–54（26 條）|
| TC ID | `newR1L-BLM-020` … `newR1L-BLM-045` |
| patched 儲存格 | 364（26 × 14）|
| round-trip | 26 列 × 14 欄，**差異 0** |
| 保全計數 | zip 48／sheet 9／legacy DV 4／**x14 DV 1**／extLst 3 —— 全等 |
| 交付 lint | **全簿 45 列 clean — 0 findings** |

S／AB 兩欄未回填（`CONST` 空字典，R-BLM16(2)(3)），欄數 14 而非 16。

工作簿鏈：`00 起建 → 01 pilot → 02 B1 → 03 清兩欄 → 04 B1 修訂 → 05 B2`（現行）

---

## 七、執行層自陳

1. **B2 之 completion 仍非模型產出**（第三次記載）。組裝以腳本為之
   （`/tmp/gen_b2.py`），但每條之 Procedure／ER 文字為逐條撰寫。
   下放包 08 §二-1 所要之「模型 vs session 品質對比」仍給不出來。
2. **非零車速之具體值（1／2／10／15 Km/h）是我選的**，037 只寫
   「非 0 MPH」「moving」。已登記於 manifest `provisional_inputs`，
   **複驗義務掛於 DR-1 結案** —— 門檻回覆後若任一值 >= 門檻，
   該條語意會由「未達門檻仍不受理」變成「已超門檻」，須逐條複驗。
3. **007-03 是定義型需求**（"shall define an upper threshold"）。
   其可測性完全繫於 DR-1 之值：沒有值就只能驗「行為在某個未知點改變」。
   已於 per-TC reasoning 明記。**若 Pei 認為此條本質不可驗，
   它是 coverage gap disclosure 之候選，非本包可裁。**
4. **台架可執行性未驗**（第七次記載）。本批新增之 ignition 狀態注入
   （`OperationalModeSts` 四態切換）與檔位注入，對台架之要求高於前兩批。
5. **024 三入口（Apps menu／Controls tab／Home Screen）之實際 UI 位置未查證**。
   037 只給名稱，規格 PDF 有 concept screens 但依 R-BLM7 不入語料。
   TC 以名稱書寫，**實際導航路徑須由執行者依實機補**。
6. **未跑 recon**：本批未改 `feature.yaml` 之 `recon_assertions`，
   母體亦未變（仍 176 leaf），故無重跑必要。

---

## 八、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行。本批新增 007-03／007-04 兩條以 PENDING 承接，未寫回；另 13 條之暫定車速值複驗義務亦掛於其結案 |

---

## 九、停點

**已停。** 交分析層複審。

R-G14 計數：本批為第 1 批候選。**執行層不自評** —— §五之
006／020 兩對是否構成 A 類項，由分析層裁。
