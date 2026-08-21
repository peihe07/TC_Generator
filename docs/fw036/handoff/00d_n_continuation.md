# 下放包 00d：N 續行豁免撤除（1 行差額裁定）

承 00c。裁定 1 之目標值 6,704 有獨立實測來源（分析層零豁免掃描），
非算術估值，故基準不因實作結果反推修改。「以重跑實測為準」一語
係限制 10,700 該類推估值之引用，不及於已實測之 N 基準。

## 裁定：採 (b)，撤除續行豁免。N = 6,704，總違規 10,659

**證據（HFP row 15，er 欄全文）**：
```
1. The device is successfully paired and connected to the HU.
2. The duplicate contact is successfully created on the device.
3. Phonebook synchronization/update starts successfully.
4. Phonebook synchronization/update completes successfully without error.
5. The Phonebook screen opens successfully and remains usable.
6. The HU phonebook entry count remains 4,999 and no additional
   duplicate contact entry is created.        ← 續行，item 6 之末行
```
該欄 6 個 numbered item 全部以句號結尾。現行豁免使 1–5 命中、
item 6 漏報 —— 同欄內部不一致，此即漏報之證。

**理由**：canon §11 之規制單位為 numbered item（"Applies to every
numbered item"），非物理行。item 之尾句號落在續行上時，該 item
仍以句號結尾，屬違規。續行豁免誤將物理行當作規制單位。

**副作用評估（實測）**：續行中段行本就不以 `[.。]$` 結尾，撤除
豁免僅會新增「以句號結尾之續行」= item 末行 = 真違規。分析層
零豁免掃描得 6,704，與撤除後預期值相等，可交叉驗證。

**維持不動**：`$` 指令行豁免保留（§5.4 命令列非 item 敘述；
8 本中無帶句號之 `$` 行，數值不受影響）。全域 NUMBERED_LINE
定義維持不動，E 錨值不得變 —— 此為本次修改之外溢紅線。

## 執行

```bash
cd /Users/peihe/Work_Projects/TC_Generator
# 1. n_exempt() 移除續行豁免；$ 指令行豁免保留
# 2. 測試：新增 HFP row15 型「續行帶尾句號」正例；
#    保留「續行中段不誤報」反例；
#    保留 test_numbered_lines_helper_excludes_lettered_substeps
pytest tests/test_lint036.py -q
python3 scripts/lint036.py <8 本> --report-dir docs/fw036/lint_reports
```

## 驗收錨（三項同時成立方為通過）

- N = 6,704；總違規 = 10,659
- E 逐本 = BT1 DM1 HFP5 Media1 PM0 Proj5 AMFM0 Home0（不得變）
- Media 14 項 = A0 B0 C1 D0 E1 F0 G0 H0 I2 J0 K0 L0 M0 **N=3**
  （Media 原 N=2，撤除續行豁免後是否 +1 由實測定；若仍為 2 則
  Media 無續行型違規，屬正常，記錄實測值即可，勿反改他項）

## 上繳

併入 `docs/fw036/upstream/00c_lint_final.md`（勿另立 00d 上繳），
增列本裁定之前後對照與 HFP row15 證據。lint 至此定版。
新規 0 條。
