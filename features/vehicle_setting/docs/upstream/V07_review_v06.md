# 上繳 V07 —— 4 leaf 轉 W0、158/160 結案、619 逐句判別、錨點自身之盲點

執行層寫入。依據：`docs/handoff/V07_review_v06.md` §6（3 項工單）＋ §2 之 R-VF17。
canon §8.2 六節。

**本輪未生成 TC、未寫回工作簿。** 唯一之產物變更為 R-VF17 所令之 4 leaf 分級
（W2→W0），其範圍受限、可重跑、有快照。

---

## 1. 交付總表

| 項 | 狀態 | 產物 |
|---|---|---|
| R-VF17 4 leaf 轉 W0 | **已施行** | `scripts/vf230_rvf17_apply.py`、`writability.tsv`／`generatable.tsv`、快照二份 |
| W-VF18 158 vs 160 | **完成（結案）** | `scripts/vf230_wvf18_rd1.py`、`docs/reports/wvf18_rd1_delta.md` |
| W-VF19 三套 upstream diff | **完成（無須合併）** | 本檔 §3 |
| W-VF20 619 逐句判別 | **完成（只判不改）** | `scripts/vf230_wvf20_619.py`、`docs/reports/wvf20_619_triage.md` |
| 條文落檔 | **完成** | `RULINGS.md` +R-VF17／18／19；`PLAYBOOK.md` +錨點檢查表 |
| anomaly | **完成** | +A-VF3（結案）／**A-VF4（新，錨點自身之盲點）** |

---

## 2. R-VF17 —— 已施行

```
SWE1-VC-HeatedSteeringWheelManagement-029  W2/B6-value-absent → W0   reqid 4859496
SWE1-VC-HeatedSteeringWheelManagement-030  W2/B6-value-absent → W0   reqid 4859497
SWE1-VC-HeatedSteeringWheelManagement-033  W2/B6-value-absent → W0   reqid 4859500
SWE1-VC-HeatedSteeringWheelManagement-034  W2/B6-value-absent → W0   reqid 4859501
```

`evidence_note` 逐筆記：來源欄為 037 之 `Verification Method`、reqid、
**逐字來源行**（`* verify that TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm = "ON"` 等）、
解出值域 `{ON, OFF}`。`generatable.tsv` 之 `writable` 同步。
快照：`writability_pre_rvf17.tsv`／`generatable_pre_rvf17.tsv`。

**錨點（R-VF11）**：必命中 = 4 leaf 施行前皆 `W2`／`B6-value-absent`（實測符）；
必不命中 = `HeatedSteeringWheelManagement-031` 前後皆 `W0` 不變（實測符）。
腳本可重跑，第二次執行報「已為 W0，無須再施行」。

### 2.1 ⚠ 本變更不具持久性 —— 須寫入 driver

`writability.tsv`／`generatable.tsv` 由 `scripts/writability_driver.py --write`
產生。其 `value_sourced()`（§262 之 B6 判定所依）**尚未認 037 之 VC/VM
為值域來源**。

→ **driver 若重跑，該 4 leaf 會被回復為 W2／`B6-value-absent`。**

**本層未改 driver** —— 其為 Part 1 之產物，且併行線本輪正在修改
（`writability_driver.py`／`selfcheck_*.py` 於 `942f0d7` 有變更）。
**請示**：R-VF13 之來源是否寫入 driver 之 `value_sourced()`；
若是，該修改屬 Part 1 之 W 號序列，非 VF230 線。

---

## 3. W-VF19 —— 三套 upstream：**無分歧，無須合併**

**實測時之現況已與 V07 §5.2 所列不同** —— `61_vf230_intake.md` 與
`62_vf230_recon.md` **均已不存在**，二者皆由併行線於
`7a7747e`／`942f0d7` 搬入 `docs/upstream/vf230/`。故現存為兩套，非三套。

**逐位元 diff（對 git 歷史）**：

| 舊路徑 | 新路徑 | 行數 | 結果 |
|---|---|---:|---|
| `upstream/61_vf230_intake.md`（`7a7747e^`） | `upstream/vf230/00_intake.md` | 368 / 368 | **逐位元相同** |
| `upstream/62_vf230_recon.md`（`942f0d7^`） | `upstream/vf230/01_recon.md` | 247 / 247 | **逐位元相同** |

→ **純搬移，內容零損失，無獨有段落，無矛盾之數字或裁決引用。
V07 §5.2 所慮之「互有獨有內容則須合併」不發生。**

**現存之不一致僅剩一項**：本線之 `docs/upstream/V06_scope_close.md` 與
`docs/upstream/V07_review_v06.md`（本檔）採 R-VF10 之 `V{NN}_` 平鋪，
而 `vf230/` 子目錄採 `{NN}_`。**二者擇一即可，本層不偏好；
惟 repo 現況已收斂於 `vf230/`（4 檔對 2 檔）。**

**請裁**：採 `vf230/{NN}_` 抑或 `V{NN}_` 平鋪。若採前者，本檔與 V06
須移入 `vf230/` 並改號為 `02_`／`03_`。**本層未動任何檔名。**

---

## 4. W-VF18 —— 158 vs 160 結案：**(iii) 二者定義本不相同**

**實質判準**：RD-1 之標的逐字為 `Heated Seat`（88）與 `Vented Seat`（72）——
**二者為 Layer 2（Test Set）之名**，成員以 `framework.md` 之
Layer 2 → Layer 3 對照表為準。自 `writability.tsv` 重算：

```
Heated Seat   88     ThreeStagesHeatedSeat 22 ／ TwoStagesHeatedSeat 20 ／
                     LeftFrontHeatedSeat 15 ／ RightFrontHeatedSeat 15 ／
                     OneStageHeatedSeat 14 ／ CrossZone Common 2
Vented Seat   72     ThreeStagesVentedSeatsManagement 22 ／
                     TwoStagesVentedSeatsManagement 20 ／
                     LeftFrontVentedSeat 15 ／ RightFrontVentedSeat 15
合計         160     ← 與 RD-1 自述完全相符
```

**差額 2** = `LeftFrontHeatedSeat-004`／`-011`，其 `layer3` 為
**`CrossZone Common`** —— `framework.md` 明列之 Heated Seat 之 Layer 3，
惟其名不帶族名字串，故 W-VF16 之字串型代理判準漏之。

- **非 (i)**：`writability.tsv` 無遺漏，該 2 leaf 在其內且值正確
- **非 (ii)**：RD-1 之 160 無計數誤
- **是 (iii)**：代理判準與實質判準之定義不同

**A-VF3 所慮之「`writability.tsv` 非該範圍之全集」不成立** —— 其為全集，
是取用方式錯了。**W-VF16 之判準 (c) 應以 160 為準；此更正不改變其結論**
（A-VS118 之 4 leaf 於 158 與 160 兩版皆判「未交付」）。

---

## 5. W-VF20 —— 619 之逐句判別（只判不改）

`\b619\b` 全庫命中 **97 處／22 檔**（**詞界必要**：`data/lid_pairs.tsv`
有 `1619`／`2619`／列號 `619`，首版未加詞界混入 4 筆偽陽性）。

```
須改     2
不改    95
待人工   0
```

**須改（現行有效之陳述，本輪未改）**：

| 檔:行 | 逐字 |
|---|---|
| `feature.yaml:29` | `# leaf 全集以 data/vf230_leaves.tsv 為準（619 leaf）。` |
| `scripts/vf230_layer2.py:113` | `assert tot_leaf == 619 or True` |

**R-VF18 之「同一檔內可能兼有兩類」已具體發生**：`feature.yaml:118`
（`388/619`）雖位於現行有效之設定檔，其為 **Test Group 裁定當時之證據**
（該裁定已由 R-VF9 結案），非後續據以行動之值 —— **逐行覆寫判為不改**。
覆寫及其理由列於報告 §1，不隱形。

**錨點（R-VF11）**：必為「須改」= `feature.yaml:29`；
必為「不改」= `docs/upstream/vf230/00_intake.md` 任一行。二者皆符。

---

## 6. A-VF4（新）—— **錨點本身可以選錯，且其失效與通過不可分辨**

本輪兩次施行皆於首版選了**不在被掃描集合內**之錨點：

| 處 | 首版錨點 | 何以無效 |
|---|---|---|
| W-VF18 | `LeftFrontHeatedSeat-001` | 不在 `writability.tsv` 之 237 列內（`leaves.tsv` 有 271，差 34）→ 必命中錨點實測失敗而停 |
| R-VF17 施行 | `HeatedSteeringWheelManagement-023` | 同不在檔內 → 取值恆為 `None`，**施行前後皆 `None`，「錨點通過」與「錨點不存在」不可分辨** |

**R-VF11／R-VF19 之盲點**：二條文令「附必命中／必不命中錨點」，
**未令「先驗錨點存在於被掃描之集合內」**。
一個不存在之必不命中錨點**恆為通過**，其提供之保證為零。

**與 A-VS106 同型** —— 驗證機制自身之失效與其通過不可分辨。

**已改正**：W-VF18 改用 `LeftFrontHeatedSeat-003`，並另加**鑑別錨點**
`LeftFrontHeatedSeat-004`（實質須命中、代理須不命中 —— 即差額本身，
其存在使兩判準之定義差異在落筆時即可見）；R-VF17 改用 `-031`，
並於錨點不在檔內時 `raise SystemExit`。
**已寫入 PLAYBOOK 檢查表第 3 項。**

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

1. **R-VF17 之效果不具持久性**（§2.1）。driver 一重跑即回復。
   **本輪之產物變更是四個 tsv 儲存格，其存續繫於「沒有人跑 driver」** ——
   這不是一個可依賴之狀態。**此為本輪最須處置者。**

2. **R-VF15 之 AH 欄轉錄仍未施行**，其與 R-VF14(1) 之交集仍未裁
   （V06 §6 第 1 項、V07 §5.1 皆已列，本輪無新進展）。
   V07 §5.1 指出 `docs/handoff/66_writeback_procedure.md` 已存在，
   **一旦寫回，判準 (a) 即不再為 0** —— 該裁定之時窗正在關閉。

3. **W-VF20 之「須改 2」未改**（V07 §6.4 令只判不改）。惟
   `scripts/vf230_layer2.py:113` 之 `assert tot_leaf == 619 or True`
   **因 `or True` 而恆真，本即無效之斷言** —— 其為「須改」不僅因數字，
   更因其為一個不會失敗之檢查（A-VS106 同型）。本輪未改。

4. **本輪未複驗 R-VF13 之全文**。R-VF17 引 R-VF13 之第 3、5 項，
   而 R-VF13 落於 V05 包，**本層未曾落檔 R-VF10–R-VF13**（V04／V05 之
   執行層工作未做）。本輪係依 V07 §2 所引之轉述施行，
   **未讀 R-VF13 逐字**。若其另有本層未知之限制，本輪之施行可能逾越。
   **建議下輪先補落 R-VF10–R-VF13。**
