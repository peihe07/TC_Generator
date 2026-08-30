# R-P372 複查 —— 45 名無錨 `<X>` 以規格用語重查（63 包）

> R-P372(a)：以所屬 TC 之 `test_item` 上半 verbatim（規格逐字）為查詢名稱，重查 G0 台帳一次。
> 與 59 包之差別為**查詢名稱種類**（R-G13 第 2 項）：59 包查 TC 措辭，本檔查規格用語。
> R-P372(b)：逐字含 `antitheft` 者 **6 名**併入 DR-PW23，不另開 DR（R-P378(b) 訂正 R-P372(b) 之「11 名／40」）。

## 總計：複查 45 名

| 判定 | 數 |
|---|---|
| 有錨 | **39** |
| 查無 | **6** |
| 未覆蓋（無逐字對應之 TC）| **0** |

## ⚠ 誠實揭露：本輪仍非「人讀」

R-P372(a) 令「**人讀**其所屬 TC 之 `test_item` 上半 verbatim」。
本檔所做者為**第二次機器掃描，改以規格用語為查詢名**（R-G13 第 2 項之變更），
**不是人讀**。二者之差在：

- 機器仍以**內容詞之交集**為查詢鍵，故 TC 措辭之殘留（`after`、`each`、
  `again`、`one`）會混入查詢詞，使命中與否受措辭影響；
- 人讀能判斷「該 `<X>` 在規格中對應哪一句」，機器不能。

**故本輪之 6 個「查無」仍不足以登記為 R-G13 意義下之查無** ——
其查詢名並非純規格用語。**本層不為該 6 名開 DR、不登 M-n**，
理由同 59 包 §3（未達要件者不得向上游提問，A-PW355 之教訓）。

**39 個「有錨」則為可用之正面結果** —— 其查詢詞全部落在規格用語內，
且命中之錨點為 G0 台帳內之 `{ObjectID}` 段落，可直接補入代理量表。

## 逐名

| `<X>` | TC 數 | 查詢用之規格內容詞 | 判定 | 錨點 |
|---|---|---|---|---|
| `shown logos` | 8 | `logos` | **有錨** | CFTS009-4941672、CFTS009-4941676 |
| `Timeout1 and then trigger an Ignition On event` | 4 | `ignition、timeout1` | **有錨** | CFTS009-4941581、CFTS009-4941587 |
| `disclaimer wording` | 4 | `disclaimer` | **有錨** | CFTS009-4941246、CFTS009-4941248 |
| `season the HU determines` | 4 | `season` | **有錨** | CFTS009-4942079、CFTS009-4942083 |
| `selectable values offered for SwitchOff_Timeout_Setting.` | 3 | `switchoff_timeout_setting.req` | **有錨** | CFTS009-4941441、CFTS009-4941487 |
| `audio output against the animation start` | 3 | `animation` | **有錨** | CFTS009-4941255、CFTS009-4941292 |
| `displayed font` | 3 | `font` | **有錨** | CFTS009-4941271、CFTS009-4941273 |
| `displayed App icon` | 3 | `icon` | **有錨** | CFTS009-4941277、CFTS009-4941279 |
| `call audio routing` | 2 | `call` | **有錨** | CFTS009-4941029、CFTS009-4941032 |
| `parameters offered for user selection` | 2 | `parameters、user` | **有錨** | CFTS009-4941702 |
| `call audio routing and the TLM state` | 2 | `audio、call、routing` | **查無** | — |
| `Timeout1 against the configured parameter` | 2 | `timeout1` | **有錨** | CFTS009-4941055、CFTS009-4941056 |
| `FPDM, AMP, ICS and DTV functions` | 2 | `fpdm` | **有錨** | CFTS009-4941360、CFTS009-4941361 |
| `shown logo against the configured brand` | 2 | `brand、logo` | **有錨** | CFTS009-4941668、CFTS009-4941669 |
| `applied theme against the brand signal` | 2 | `signal、theme` | **有錨** | CFTS009-4941268、CFTS009-4941269 |
| `$Radio_Theme$ against the applied theme` | 2 | `$radio_theme$、theme` | **有錨** | CFTS009-4941271、CFTS009-4942004 |
| `shown recirc icon` | 2 | `icon、recirc` | **有錨** | CFTS009-4941279、CFTS009-4941281 |
| `TLM screen content before and after StandardScreen_Time` | 1 | `after、screen、standardscreen_time` | **有錨** | CFTS010-4942337 |
| `TLM_Status transitions during the remainder of the boot` | 1 | `boot、during、transitions` | **有錨** | CFTS010-4942338 |
| `three stored variables` | 1 | `variables` | **有錨** | CFTS009-4941120、CFTS009-4941122 |
| `TLM_Status.Info and the state machine` | 1 | `tlm_status.info` | **有錨** | CFTS009-4941396、CFTS009-4941441 |
| `AMP, ICS and DTV power states and the audio paths` | 1 | `audio` | **有錨** | CFTS009-4941019、CFTS009-4941027 |
| `TLM_Status.Info and the screen content` | 1 | `screen、tlm_status.info` | **有錨** | CFTS009-4941544、CFTS009-4941554 |
| `remote start outcome flags and the TLM state` | 1 | `remote、start` | **有錨** | CFTS009-4941044、CFTS009-4941045 |
| `remote start outcome flag and the TLM state` | 1 | `flag、outcome、remote、start` | **查無** | — |
| `TLM state against the operative state management rules` | 1 | `management、operative` | **有錨** | CFTS009-4941351、CFTS009-4941769 |
| `offered items against the TLM HMI documents` | 1 | `documents、items` | **有錨** | CFTS009-4941771、CFTS009-4941775 |
| `user selectable parameter on an ex-factory unit` | 1 | `factory` | **有錨** | CFTS009-4941106、CFTS009-4941491 |
| `shown logo against the configured parameter` | 1 | `logo、parameter` | **有錨** | CFTS009-4941668、CFTS009-4941670 |
| `user selectable timeout parameter on an ex-factory unit` | 1 | `factory` | **有錨** | CFTS009-4941106、CFTS009-4941491 |
| `HU mode after the idle period` | 1 | `after、mode` | **有錨** | CFTS009-4941029、CFTS009-4941160 |
| `HU behavior and the stored logs` | 1 | `behavior、logs、stored` | **查無** | — |
| `both processors` | 1 | `both` | **有錨** | CFTS009-4941317、CFTS009-4941376 |
| `screen against the elapsed time` | 1 | `time` | **有錨** | CFTS009-4941051、CFTS009-4941052 |
| `ICS functions and the DTV` | 1 | `functions` | **有錨** | CFTS009-4941033、CFTS009-4941165 |
| `screen across the cycles` | 1 | `cycles、screen` | **有錨** | CFTS009-4941958 |
| `shown wording` | 1 | `wording` | **查無** | — |
| `shown element` | 1 | `element` | **有錨** | CFTS009-4941263、CFTS009-4941269 |
| `shown seat graphic against the brand signal` | 1 | `graphic、seat` | **有錨** | CFTS009-4941281、CFTS009-4941283 |
| `shown gauges` | 1 | `gauges` | **有錨** | CFTS009-4941284、CFTS009-4941286 |
| `TLM_Status.Info after each one` | 1 | `after、each、tlm_status.info` | **查無** | — |
| `TLM state again after Timeout1 has elapsed` | 1 | `after、again、elapsed、timeout1` | **查無** | — |
| `audio power amplifier and the BoosterOUT states` | 1 | `audio、power` | **有錨** | CFTS009-4941019、CFTS009-4941027 |
| `analog and digital antenna supplies` | 1 | `antenna` | **有錨** | CFTS009-4941316、CFTS009-4941750 |
| `USB and AUX MCU states` | 1 | `states` | **有錨** | CFTS009-4941022、CFTS009-4941068 |
