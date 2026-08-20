# 56 下放包 — 第二段之資訊量（最後一項）與 ENTRY 004

**本包無裁決條文。** 55 輪上繳**核可**。ENTRY 003 成立。

## 一、覆核結案

**`TC-165` 本輪讀畢，缺陷 0。**
**189 / 189 全部經第二人逐條讀畢，分析層之覆核義務結清。**

`TC-165` 之 ER4 理由紮實：只驗 ER2（遙控起動期間不清除），
**一個根本沒有 30 秒計時之實作會通過**；ER4 證明計時仍在，只是排除了該段時間。

## 二、AD-1（defect）第二段有一部分僅為第一段之改寫

`TI-2` 驗「非僅重複第一段」，**而其比對為字面** ——
換句話說即通過，故 189／189 全綠而問題仍在。

**實例**（分析層於 `55_review_pack_33a` 逐條讀出）：

| tc_id | 第一段 | 第二段 | 移除第二段是否損失資訊 |
|---|---|---|---|
| `168` | New Profile Setup starts from the All Profiles tab | Verifies that the New Profile Setup starts from the All Profiles tab | **否** |
| `173` | The same username can be used by two Driver Profiles | Verifies that the same username can be used by more than one Driver Profile | **否** |
| `166` | Valet Mode welcome popup clears like the other popups | Verifies that the Valet Mode welcome popup clears in the same way as the other welcome popups | **否** |

**對照，寫得對者**：

| tc_id | 第二段所帶進之新資訊 |
|---|---|
| `165` | `30-second **dismissal timer**` —— 點出被排除者為哪一個計時器 |
| `164` | `**stays away for the session**` —— 補上 ER2 之那一半 |
| `167` | `**never launches the account login**` —— 補上 ER4 之缺席斷言 |

### 判準（可測之代理 ＋ 人工判讀）

**代理判準**：去除 `Verifies that` 與停用詞後，
第二段之實詞集合 ⊆ 第一段之實詞集合（或重疊率 ≥ 門檻）→ **列待判**。

**不自動轉紅** —— 「有沒有帶進新資訊」是語意判斷，
與 AB-1（兩端是否指同一件事）同類，機械判不了（55 輪 §7-3 已具名此類）。

**判讀後之處置**：第二段改寫，帶進該條 ER 所斷言而第一段未載之具體內容
（來源仍為 `reasoning` 之驗證目標句，不另行構思）。

**須附**：
- 代理判準之**門檻選定依據**（不得先看結果再定門檻 —— Q-1 之教訓）
- 其**盲區**（R-G11）：以同義詞改寫而實詞不重疊者抓不到
- **G-K**：報命中數前，先證明它對 `168`／`173`／`166` 三條會叫

## 三、ENTRY 004

1. AD-1 之改寫（待判清單經人工判讀後）
2. **`TC-167` 之 `specification_reference`** —— 若 Tutorials L&F 之 PDF
   已落 `inputs/`（G-L）；未落則維持具名缺口，**不再列為待辦**
3. 重跑 18 支閘；`DELIVERY.sha256` ENTRY 004
4. 四份 review pack 重出（`test_item` 變動）

## 四、本 feature 之最後一項

**AD-1 處置完成後，分析層無任何未結項。** 其後僅餘 Pei 之：

1. **交付** —— `output/` 之 ENTRY 004
2. **git** —— 指令清單（帶 pathspec）
3. **`R-U17`** —— 刪 `inputs/` 之 spec 副本
4. **Tutorials L&F 之 PDF 落 `inputs/`**（若欲補 `TC-167` 之引用欄）
5. **RD v2 ＋ #8 ＋ A-UP14** —— 交付後寄出亦可

## 五、值得記入 profile 之一句（本 feature 之最後一課）

55 輪 §7-4：

> **閘只能守住已知的規格，守不住沒有人寫下來的期待。**

AD-1 是它的下一層：

> **規格寫下來之後，閘守住的仍只是它可測的那一面。**
> `TI-2` 忠實地執行了「非僅重複第一段」——
> 它只是不知道「換句話說」也是重複。

## 六、不在本包授權範圍

- 交付、git、RD 寄出 —— 屬 Pei
- 第二段之內容自行創作（來源仍為 `reasoning` 之驗證目標句）

## 七、上繳

`docs/upstream/56_second_segment.md`，更新 `docs/INDEX.md`，附獨立判斷。
