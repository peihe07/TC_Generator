# `REGEN_ORDER.md` —— 各批之重製順序（W-161，56 輪）

依 `docs/handoff/84_delivery.md` §4 之裁定。

**R-VS53 之弱化，具名於此**：早批之產物**不可自單一 driver 重製** ——
`batchNN_vM.json` 為「原生成器之輸出 ＋ 依序疊加之修正腳本」。
重製須**按下表之順序**執行，跳過任一層其結果即不同。

**分析層／稽核之可重現性由此鏈滿足，非由單一 driver 滿足。**

| 批 | 原生成器 | 修正層（依序） | 層 | 現行版本 | sha256（前 16） | 凍結點 | `frozen_sha256`（前 16） |
|---|---|---|---:|---|---|---|---|
| `batch01` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` → `**D-3（48 輪） 之腳本或作業不在 repo**` → `split_exec_w143.py` → `**W-157 之腳本或作業不在 repo**` → `**W-160 之腳本或作業不在 repo**` | 6 | `batch01_v9.json` | `34f551be0e3b850a` | `batch01.json` | `cf1e5510232a5158` |
| `batch02` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` → `**D-3（48 輪） 之腳本或作業不在 repo**` → `split_exec_w143.py` → `**W-157 之腳本或作業不在 repo**` → `**W-160 之腳本或作業不在 repo**` | 6 | `batch02_v7.json` | `45f32fc651724852` | `batch02.json` | `6b6f45d5473d27ed` |
| `batch03` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` → `**W-160 之腳本或作業不在 repo**` | 3 | `batch03_v6.json` | `3e6e6eddc6db7286` | `batch03.json` | `207fd0f8c7706682` |
| `batch04` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` | 2 | `batch04_v6.json` | `94540d4f762244b4` | `batch04.json` | `8843b891c5503373` |
| `batch05` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` | 2 | `batch05_v4.json` | `5bd88bfacaa4ce55` | `batch05.json` | `c13574c86736e45d` |
| `batch06` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` → `pilot_fix_w130.py` → `split_exec_w143.py` | 4 | `batch06_v6.json` | `e0cca54927ae429f` | `batch06.json` | `e14897d1099897d5` |
| `batch07` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` → `pilot_fix_w130.py` → `**W-157 之腳本或作業不在 repo**` → `**W-160 之腳本或作業不在 repo**` | 5 | `batch07_v7.json` | `85462b3aedb5a688` | `batch07.json` | `c494bb31a4a00e95` |
| `batch08` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` | 2 | `batch08_v5.json` | `8f3d3565f752576c` | `batch08.json` | `5b0070a0b1ee0551` |
| `batch10` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` → `pilot_fix_w130.py` → `**W-160 之腳本或作業不在 repo**` | 4 | `batch10_v6.json` | `96cf32046b0a9796` | `batch10.json` | `268a31a3d7ac4868` |
| `batch11` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` | 2 | `batch11_v4.json` | `314bb2c9a37d2ec2` | `batch11.json` | `cffe83b367b9bd68` |
| `batch12` | `**首版生成器未入庫；其產物以 sha256 凍結為基準**` | `record_rewrite_w95.py` → `priority_and_style_w101.py` | 2 | `batch12_v4.json` | `d0fab7fa4f14ead5` | `batch12.json` | `fb7cfac7481b7e98` |
| `batch13` | `batch13_w100.py` | `sibling_fix_w105.py` → `pilot_fix_w130.py` → `signal_rewrite_w131.py` → `impl_gap_w133.py` | 4 | `batch13_v5.json` | `d7080276032bc6c1` | — | — |
| `batch14` | `batch14_w105.py` | `**D-4（38 輪） 之腳本或作業不在 repo**` → `pilot_fix_w130.py` → `signal_rewrite_w131.py` → `impl_gap_w133.py` | 4 | `batch14_v5.json` | `510d80f88526c040` | — | — |
| `batch15` | `batch15_w108.py` | `pilot_fix_w130.py` → `signal_rewrite_w131.py` → `impl_gap_w133.py` | 3 | `batch15_v4.json` | `ff8f979d8b0abcc2` | — | — |
| `batch16` | `batch16_w113.py` | `pilot_fix_w130.py` → `screen_layer_w132.py` → `popup_weakest_w135.py` → `**D-3（48 輪） 之腳本或作業不在 repo**` | 4 | `batch16_v4.json` | `763cca763bb0202c` | — | — |
| `batch17` | `batch17_w116.py` | `pilot_fix_w130.py` → `signal_rewrite_w131.py` → `screen_layer_w132.py` → `impl_gap_w133.py` → `**D-3（48 輪） 之腳本或作業不在 repo**` → `**W-157 之腳本或作業不在 repo**` | 6 | `batch17_v6.json` | `e4f094ec44dff012` | — | — |
| `batch18` | `batch18_w119.py` | `pilot_fix_w130.py` → `signal_rewrite_w131.py` → `impl_gap_w133.py` → `**D-3（48 輪） 之腳本或作業不在 repo**` → `**W-157 之腳本或作業不在 repo**` | 5 | `batch18_v5.json` | `d3d1f9a7b0e6da7c` | — | — |
| `batch19` | `batch19_w122.py` | `pilot_fix_w130.py` → `signal_rewrite_w131.py` → `impl_gap_w133.py` | 3 | `batch19_v4.json` | `cc47d18045ad4d50` | — | — |
| `batch20` | `batch20_w143.py` | — | 0 | `batch20.json` | `feb5ef8ece767038` | — | — |
| `batch21_probe` | `batch21_probe_w146.py` | `**W-149 之腳本或作業不在 repo**` → `**W-157 之腳本或作業不在 repo**` | 2 | `batch21_probe_v2.json` | `868da48b133950af` | — | — |
| `batch22` | `batch22_w150.py` | — | 0 | `batch22.json` | `fe0c2c2822b8e105` | — | — |
| `batch23` | `batch23_w152.py` | `**W-157 之腳本或作業不在 repo**` | 1 | `batch23_v2.json` | `c74c457dbebe3824` | — | — |

**鏈長最長者：`batch01`，6 層。**

### 原生成器未入庫者 —— **11 批**，其 R-VS53 以**雜湊凍結**滿足（86 包 §3）

| 批 | 凍結點（現存最早版） | 其 TC | `frozen_sha256` |
|---|---|---:|---|
| `batch01` | `batch01.json` | 10 | `cf1e5510232a5158ce7f03538f2451d64f2d37fc87fa0115c9ae737e7bb5e1ad` |
| `batch02` | `batch02.json` | 6 | `6b6f45d5473d27ed08e400716ddc205227a1c76736693ff340470cf84f35f8f5` |
| `batch03` | `batch03.json` | 10 | `207fd0f8c770668206b5631eb4b457671c3c286517f389df701a55175def1083` |
| `batch04` | `batch04.json` | 10 | `8843b891c550337339f0a3d70b099d6d10c14135036a97592567cfbf6911600c` |
| `batch05` | `batch05.json` | 8 | `c13574c86736e45d72e0ebb24997fa1d2cb34dea4673bdb455eb5822b4fbfcb4` |
| `batch06` | `batch06.json` | 9 | `e14897d1099897d5ccd6e7ba39f612dc21194e6a272acb829dd8ef504bccce26` |
| `batch07` | `batch07.json` | 7 | `c494bb31a4a00e95adc4ad8b49efade5496e636e51324a26c19777d24234c619` |
| `batch08` | `batch08.json` | 7 | `5b0070a0b1ee0551292229d4771613d4bc71d387ccbcf5b4b0c2b5cd1685c17a` |
| `batch10` | `batch10.json` | 10 | `268a31a3d7ac4868f6cbc9c2aede51022cac21cbebab64df4d7b6d230204ff46` |
| `batch11` | `batch11.json` | 1 | `cffe83b367b9bd688655c8fc4d197adbcdef3c6556fc61f400dcb9c8055123f5` |
| `batch12` | `batch12.json` | 0 | `fb7cfac7481b7e987e4105463576df233635218c812b65aa7cd0379557ee95ca` |
| **合計** | | **78** | |

**其意涵**（86 包 §3，須具名不得以「可重製」一語涵蓋）：

　該 11 批（**78 條**）之**首版生成過程不可重放** —— 現存腳本中無任何一支寫出其首版。
　其後之**每一層修正皆有腳本且順序已記於上表**，故其變更歷程可稽核。

　**可稽核之範圍為「自凍結點起之變更」，非「自需求起之產出」。**
升級門檻為「> 3 則重製之可行性須另議」——**逾**。

## 重製之執行順序

```
cd features/vehicle_setting
python3 scripts/<原生成器>.py          # 產 batchNN.json
python3 scripts/<修正層 1>.py          # 產 batchNN_v2.json
python3 scripts/<修正層 2>.py          # 產 batchNN_v3.json …
```

**各修正腳本皆掃全母體並自產下一版**，故其執行為「跑一次即處理所有批」，
非逐批呼叫。上表之「修正層」為該批**實際被觸及**之層。

## 驗證

```
python3 scripts/selfcheck_w53.py generated/<現行版本>   # §9 十七項
python3 scripts/selfcheck_anchored.py                   # 固定錨點 20 項
python3 scripts/defect_scan_w157.py                     # 五項 defect
python3 scripts/backscan_w160.py                        # R-VS77 全母體回掃
python3 scripts/completeness_w154.py                    # R-VS76 完整性
```

### ⚠ 已入庫後之**就地改動**（R-VS80 所禁；A-VS162）

判準為 **git 可驗者**：該版本檔之 commit 數 > 1，即其入庫後另有 commit 改其內容。
**不以 `revision` 之標記推斷** —— `batch14_v2` 之首標記為 `D-4（38 輪）`，其為該版之產出者而非就地改動。

| 版本檔 | 改動之 commit | 所改之欄位（條數） |
|---|---|---|
| `batch01_v3.json` | `baeb58a` | `dr15_exposed` 8 |
| `batch01_v6.json` | `70b75d0` | `screen_pending` 8 |
| `batch01_v6.json` | `100d1e0` | `screen_pending` 2 |
| `batch02.json` | `baeb58a` | `dr15_exposed` 6 |
| `batch02_v4.json` | `70b75d0` | `screen_pending` 6 |
| `batch02_v4.json` | `100d1e0` | `screen_pending` 1 |
| `batch03.json` | `baeb58a` | `dr15_exposed` 10 |
| `batch03_v5.json` | `70b75d0` | `screen_pending` 10 |
| `batch04_v6.json` | `70b75d0` | `screen_pending` 10 |
| `batch05_v4.json` | `70b75d0` | `screen_pending` 8 |
| `batch06_v4.json` | `70b75d0` | `screen_pending` 9 |
| `batch07_v4.json` | `70b75d0` | `screen_pending` 7 |
| `batch08_v5.json` | `70b75d0` | `screen_pending` 7 |
| `batch10_v4.json` | `70b75d0` | `screen_pending` 10 |
| `batch11_v4.json` | `70b75d0` | `screen_pending` 1 |
| `batch13_v2.json` | `70b75d0` | `screen_pending` 10 |
| `batch14_v2.json` | `70b75d0` | `screen_pending` 10 |
| `batch15.json` | `70b75d0` | `screen_pending` 13 |
| `batch16.json` | `70b75d0` | `screen_pending` 10 |
| `batch16_v4.json` | `100d1e0` | `screen_pending` 10 |
| `batch17.json` | `70b75d0` | `screen_pending` 10 |
| `batch17_v5.json` | `100d1e0` | `screen_pending` 8 |
| `batch18.json` | `70b75d0` | `screen_pending` 10 |
| `batch18_v4.json` | `100d1e0` | `screen_pending` 5 |
| `batch21_probe.json` | `a8b5bb1` | `expected_result` 2／`test_procedure` 2／`reasoning` 2／`remarks` 1／`pre_conditions` 1／`split_reason` 1／`distinguishing_axis` 1／`tc_title` 1／`split_flag` 1 |
| `batch23.json` | `cc66602` | `pre_conditions` 9／`test_procedure` 8／`expected_result` 7／`remarks` 5 |
| **合計** | **5 個 commit** ／ **26 檔次** | |

**該層皆不在鏈上** —— 其無腳本，亦不產新版；
**其記錄僅存於上表之 git commit**。若該次未入庫，其缺口即永久不可見。

**48 輪之就地改動（A-VS162）—— 其手段不可考，以 git commit `100d1e0` 為其記錄。**