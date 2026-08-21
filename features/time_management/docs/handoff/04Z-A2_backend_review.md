# 04Z-A2 — A-TM21(b) 降級、G-TM2 訂正、git 授權界線、backend 續讀

分析層 → 執行層。覆核對象：`docs/upstream/04Z_corrections.md`（兩節）。
**全部受理。** `04` 往返結案。

`scripts/` 仍凍結（A-TM20 第三次呈報未獲答覆），本包**仍不下放修改腳本
之指令**；本包全部動作為條文與 `backend/` 唯讀。

---

## 1. §5 `verify_structure()` 評估 —— 受理，G-TM2 項 2 訂正

三層比對之拆解正確，第三層之判定尤其關鍵：

```python
differing = sorted(m for m in src_members if a.read(m) != b.read(m))
unexpected = [m for m in differing if m not in patched]
```

**`a.read(m) != b.read(m)` 為逐 member 位元組比對，且限定只有
`patched` 之 member 得有差異** —— 這比 `check_other_sheets()` 之 docstring
所承諾者（「目標分頁以外逐位元相同」）更嚴格，因它連目標分頁以外
**任何** 未預期之內容變動都攔。

且 `run()` 之呼叫順序使前者通過與否不影響後者執行。**A-TM21(b) 降級成立。**

### 1.1 處置：移除 `check_other_sheets()`，非只改 docstring

執行層提兩案（改 docstring / 移除）。分析層取**移除**，並採其理由：

> 其存在使讀者誤以為有第二道獨立檢查。

一個功能被完全涵蓋、且比涵蓋者更弱的檢查，留著只有兩種作用：讓人以為
防護有兩層，或讓人在 `verify_structure` 出問題時誤以為還有備援。
**兩者都是假保證**，正是本 feature 一路在防的形態。

```
G-TM2 項 2 訂正（2026-08-21，依 04Z 上繳 §5.3）

原文：「A-TM21 (b) —— check_other_sheets() 同上處置（實作 docstring
所述之保護，或改寫 docstring 使其與實作相符）」

訂正為：

  2. A-TM21 (b) —— **移除 check_other_sheets()**，並於 run() 之該處
     加一行註解指向 backend/xlsx_surgical.py:268-275 之 verify_structure
     第三層。

     理由：該函式之功能已被 verify_structure 完全涵蓋且後者更嚴格
     （逐 member 位元組比對，且限定僅 patched 者得異）。保留一個
     更弱且被完全涵蓋之檢查，只會製造「有兩道獨立防護」之假象。

     若持有者堅持保留，則須改寫 docstring 使其誠實描述「僅比對 member
     名稱集合」，且不得再使用「逐位元相同」字樣。
     **不得留下承諾與實作不符之狀態** —— 此點與原文相同。

G-TM2 項 1（A-TM21(a)）**不變**。其 resolve_columns() 之欄位對映無任何
其他機制涵蓋：verify_structure 保護檔案結構，不驗欄位對映是否取對；
寫入落在錯欄時，錯欄仍在目標分頁內屬 patched，結構檢查全綠。
執行層 §5.4 之區辨正確。
```

## 2. §2 git 歸屬 —— 明答 (a)，界線理解正確，立為條文

執行層之二分正確且我未曾明文寫過：

| 來源 | 效力 |
|---|---|
| 下放包「不得執行者」之「不動 git」 | 分析層之指令**不授權**執行層動 git |
| Pei 於聊天層之直接輸入 | **git 操作之唯一授權來源** |

**下放包無權授權 git 操作，亦無權撤銷 Pei 之直接指示** —— 這句把
「不動 git」從一條禁令還原成它本來的意思：**分析層沒有這個權限可以給**。
四次 commit 皆在 Pei 直接輸入後、且從未 push，符合。

**無 A-TM22 之登記需要。**

```
R-TM36（分析層自裁，2026-08-21）—— git 授權之唯一來源

下放包「不得執行者」所列之「不動 git」，其意義為
**分析層之指令不授權執行層執行任何 git 寫入操作**，
非「執行層在任何情況下不得執行 git」。

git 操作之唯一授權來源為 Pei 於聊天層之直接指示。下放包無權授權，
亦無權撤銷該指示。

執行層收到 Pei 之直接 git 指示時逕行執行，並於上繳完整回報
（指令、commit hash、變更檔數、排除清單、是否 push）。

依據：04Z 上繳 §2.1 之二分。本條為既有分工之明文化，非新規則。
```

### 2.1 §2.2 commit message —— 草擬屬執行層，但數字須實測

```
R-TM37（分析層自裁，2026-08-21）—— commit message 之草擬與其查證義務

commit message 之草擬屬執行層自裁（Pei 之指示為「執行 commit」，
不含逐字審閱 message），現行作法（執行層草擬、回報中完整呈現、
Pei 事後可要求改寫）確認為所期。

但 message 內之任何數字或狀態陳述受與其他斷言相同之查證義務
（canon §5a）：`rulings 35, anomalies 20` 一類必須為**實測值**，
不得取自下放包之期望值或前次回報。message 是會被日後引用的記載，
其錯誤與文件內之錯誤同級。

未 push 前 message 可重寫，故錯誤可逆 —— 但可逆不免除查證義務。
```

## 3. 三項未讀之 `backend/` —— 本包指派兩項

執行層列三項未讀且**不代為聲稱**，正確。其中 §6.3(2) 之自我修正尤其準確：

> 該句應讀為「此處是 DV 保護之所在」而非「該保護經確認有效」。

**這是本包最該學的一句話。** 「找到了保護的所在」與「確認保護有效」是
兩件事，前者常被當成後者用 —— 與 docstring 承諾／實作缺失同一形態，
只是發生在讀者這一側。

指派 `_dv_counts()` 與 `patch_sheet_xml()`：前者是 R-G3（母本 x14 下拉）
之實際執行點，後者是 `surgical_save` 之核心寫入者。**兩者皆為交付件
不可逆風險之所在**，在 B1 生成前應讀完。

`verify_structure` 之三層若有一層名實不符，其後果落在交付件上。

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM36 / R-TM37，並訂正 G-TM2 項 2

標題行 `## R-TM36 — git 授權之唯一來源`、
`## R-TM37 — commit message 之草擬與其查證義務`，內文為 §2 / §2.1 之區塊。

G-TM2 項 2 依 §1.1 之區塊訂正 —— **原文加刪除線保留，訂正文置於其下並
註明依據包**（R-TM13），不整段換掉。

追加後 `## R-TM` 條數應為 **40**；`## G-TM` 仍為 **2**。

### T2 — `ANOMALIES.md`：A-TM21(b) 降級註記

於 A-TM21 條文末尾追加，逐字：

```markdown
**(b) 降級（2026-08-21，依 04Z 上繳 §5 之 verify_structure 評估）**

check_other_sheets() 所指之保護**實際存在**，由
backend/xlsx_surgical.py:268-275 之 verify_structure 第三層提供，
且較 docstring 所承諾者更嚴格（逐 member 位元組比對 `a.read(m) !=
b.read(m)`，且限定僅 patched 之 member 得有差異）。

故 (b) 由「保護缺失」降為「docstring 與實作不符」。
處置隨之由「補實作」改為「移除該函式」（G-TM2 項 2 訂正）。

**(a) 不隨之降級** —— resolve_columns() 之欄位對映無任何其他機制涵蓋：
verify_structure 保護檔案結構，不驗欄位對映是否取對。寫入落在錯欄時，
錯欄仍在目標分頁內屬 patched，結構檢查全綠。
```

**A-TM21 條數不變（21）。**

### T3 — `backend/` 續讀（唯讀，兩項）

**只讀，不改，不執行。** 依 R-TM31 附程式碼位置與片段，不只結論。

**(1) `_dv_counts()`** —— 回報：

- 其如何區分 classic DV 與 x14 擴充 DV（讀哪個 XML 節點／namespace）
- 母本之 x14 下拉（R 欄 design_method）在該函式下計為幾
- 若 openpyxl 存回丟棄 x14，該計數是否確實由 1 變 0 —— **能否僅由讀碼
  判定？若不能，明說「須實跑方能確認」，不得以讀碼推得當作已驗**
- 是否有 classic 與 x14 皆為 0 之退化情形會使比對恆真

**(2) `patch_sheet_xml()`** —— 回報：

- 其寫入之粒度（整個 sheet XML／逐 cell 節點）
- 對未被指定之 cell 是否保證不動（**依據為何：程式碼保證，或僅為
  當前輸入之偶然結果**）
- 對共用字串表（`sharedStrings.xml`）之處理 —— 若新增字串，該 member
  必然變動，其是否在 `members_patched` 之列。**此點直接決定
  verify_structure 第三層會不會誤報**
- 對 x14 擴充節點（`<extLst>`）之處理

### T4 — canon §10.3 之獨立複驗（§6.5）

執行層記「分析層補驗 canon 原文，執行層未獨立複驗，依 R-TM4 雙向適用
仍為單方」。**提請成立。**

讀 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 之 §10.3，回報原文，
並就 R-TM32 之三項確認逐項判定支持／不支持：

1. `NR1L-TimeAndDate-{n:03d}` 符合 `{project}-{abbr}-{NNN}`
2. `TimeAndDate` 符合「alphanumeric module abbreviation」，條文未限長度
3. 「序號跨批連續不重設」符合「monotonically increasing within the same
   `{project}-{abbr}` group」

**任一項不支持即回報並停** —— tc_id 已入 `feature.yaml`，若形式有誤
須在 B1 生成前改。

### T5 — 驗證（依 R-TM31，列明細）

```bash
grep -n '^## R-TM3[67]' features/time_management/RULINGS.md
grep -n '項 2 訂正'      features/time_management/RULINGS.md
grep -n '降級'           features/time_management/ANOMALIES.md
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 40
grep -c '^## G-TM' features/time_management/RULINGS.md      # 期望 2
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 21
stat -f '%Sm %N' -t '%H:%M:%S' features/time_management/scripts/*.py
```

末項期望仍為 **09:13:36 / 09:14:32 / 09:15:18**（凍結未破）。

### T6 — 上繳

`docs/upstream/04Z-A2_corrections.md`。須含 T5 全部輸出、T3 兩項之
逐項回報（附位置與片段）、T4 之原文與三項判定、
**本包是否仍有該驗而未驗者之獨立判斷**（明列全集）。

### 不得執行者

- **不動 git**（除非 Pei 於聊天層直接指示 —— R-TM36）
- **不寫入、不覆蓋、不修改 `features/time_management/scripts/` 任一行**（A-TM20）
- 不修 A-TM21 之任何一項（凍結中）
- **不改 `backend/` 任何檔**（T3 唯讀）
- 不執行任何腳本（含 `--self-test`）
- 不生成任何 TC
- 不碰 `features/vehicle_setting/`
- 不 rm 任何檔案
- 不送出 RD-1
- 不填 `D5`、不組 Scope 值
- 不以 openpyxl 存回任何工作簿

---

## 5. 呈報 Pei

**1. `features/time_management/` 之歸屬 —— 第四次，一句話即可。**
本 session 繼續（我下放 G-TM1 + G-TM2 十二項之修改指令），
或交給另一邊（我出交接單，本 session 轉唯讀覆核）。
`05`（B1 生成）在此之前不下放。

**2. 分支 ahead 14 未 push。** 快照與 commit 同在該機，機器故障則一併失去。

其餘不阻塞：R-TM10-A1 替代樣式來源（仍無候選）、RD-1 Q-TM1–3 送出、
A-TM18 Comfort 之 (a)/(b) 判定。

## 6. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM36 | 分析層自裁，git 授權來源 | §2 | ✅ T1 |
| R-TM37 | 分析層自裁，commit message 查證義務 | §2.1 | ✅ T1 |
| G-TM2 項 2 訂正 | 依 R-TM13 加註保留 | §1.1 | ✅ T1 |
| A-TM21(b) 降級 | anomaly 註記，條數不變 | §1 | ✅ T2 |

分析層本包未動 git、未改任何腳本、未觸 `scripts/`、未改 `backend/`。
