# 03 上繳 — DBC↔LID 逐屬性交叉、Comfort 重疊、餘數驗證

執行層寫入。往返 NN = 03。
**本輪未生成任何 TC，未寫回任何工作簿。** git 僅於 R-VS24 之窄口內執行一次。

> 依 R-VS18 於開工第一個動作建立，六節先留空，逐項完成即填。
> `docs/reports/` 為**附件**，非本檔之替代。

## 本輪作業清單

| # | 作業 | 狀態 |
|---|---|---|
| W-25 | 版控追蹤現況查證（唯讀，不佔順位） | ✅ **判定 (a)**，見 §0 |
| W-15b′ | DBC ↔ LID 表逐屬性交叉 | ✅ 附件 `reports/w15b_dbc_lid_crosscheck.md` |
| W-17 | LID 列數差 6；`TRUNCATED_ENUM` 其他形態 | ❌ **未執行** |
| W-9 | Comfort 逐條對照（母體 237） | ❌ **未執行** |
| W-22 | 值域抽取之餘數驗證 | ❌ **未執行** |
| W-23 | 歸因判準化 C1–C5 | ❌ **未執行** |
| W-24 | `IGN_OFF` 兩處條文是否落在 237 內 | ❌ **未執行** |
| W-26 | 改寫 A-VS19 措辭 | ✅ |
| — | 附錄 A 之入庫（R-VS24 窄口） | ⬜ |

---

## 0. W-25 —— 版控追蹤現況（**判定 (a)**，兩種結果皆回報）

### 實測

```
$ git ls-files features/vehicle_setting/ | wc -l
51
$ git log --oneline -- features/vehicle_setting | head -10
2c6c9b3 feat(vehicle_setting): rounds 00-02 intake, recon, rulings R-VS1..R-VS21
554079e feat(vehicle_setting): rounds 02-03 — rulings filed, value domains ...
52de5a6 docs(vehicle_setting): round 01 upstream + W-8 three-source variable comparison
21ba4d6 docs(vehicle_setting): file handoff 02 — coverage baseline correction
039b42f feat(vehicle_setting): round 01 partial — leaf universe resolved ...
c780d5d feat(vehicle_setting): round 00 — intake, recon, anchor chain, LID and DBC baselines
```

**判定 = (a)**：`features/vehicle_setting/` 之 **51 檔已被追蹤**，
分佈於 **6 個 commit**，最早者 `c780d5d`（00 輪，30 檔）。
`2c6c9b3` 之 7 檔為**增量**，非全部。

（(b) 之情形不成立：並非「只有 2c6c9b3 之 7 檔被追蹤」，故無須追因 `git add` 未生效。）

### 更正

07 包 §7 逐字載「**P2 不做，00～02 三輪之產物全部不在版控中 ——
若工作區出事，三輪工作沒有備份**」；09 包沿用同一陳述。**該陳述為誤。**

實際上自 00 輪 `c780d5d` 起，每輪產物皆已入庫；
真正未入庫者僅 `inputs/INPUTS.sha256`（受 `.gitignore` 之 `inputs/` 全目錄排除，
已於 `2c6c9b3` 隨 R-VS16 之例外解決）與少數中介檔。

### ⚠ 執行層亦有責，不只分析層

**本執行層在 02 輪上繳與回報中原樣重述了該陳述**（「P2 積了六輪 ——
00～02 三輪產物全部不在版控中」），**而那六個 commit 正是本執行層自己跑的**。
即：手上有直接證據而未查，照抄了上游的推測。

→ **A-VS25 之描述須涵蓋兩層**，不得只記分析層。

---

## 1. 預期 vs 實測（相符者亦列出）

| 項 | 預期 | 實測 | 判定 |
|---|---|---|---|
| W-25 追蹤檔數 | 未給（判定 (a)/(b)） | **51 檔／6 commit** → **(a)** | 見 §0 |
| W-26 空白目錄 | 已不存在（P1 已關閉） | `ls -d`／`find` 無輸出、`git ls-files` 未匹配 | **符** |
| DBC BHCAN message／signal | 155／883 | **155／883** | 符 |
| DBC FDCAN8 message／signal | 323／1755 | **323／1755** | 符 |
| DBC VAL_ 表數 | 未給 | BHCAN **650**／FDCAN8 **1512** | 新測 |
| W-15b′ 八屬性全符 | 未給 | **14 / 58** | 新測 |

---

## 2. 不符項目（不自行調和）

### 2.1 W-15b′ 之三項（**升級條件「LID 表與 DBC 之屬性矛盾」命中**）

| # | 項 | 內容 | 登記 |
|---|---|---|---|
| 1 | **message 歸屬矛盾** | `$ESS_ENG_ST$`：LID 載於 `ENGINE_FD_2`，DBC 實際於 **`STATUS_CCAN3`** | **A-VS26**，待判 |
| 2 | **signal 名大小寫不符** | LID `HSW_STATSts`／`HSW_STATFailSts` vs DBC `HSW_StatSts`／`HSW_StatFailSts` | **A-VS27** —— **推翻 00G §2 之「LID 表與 DBC 一致」** |
| 3 | **8 支按鍵請求類訊號不在基線 DBC** | `FL_HS_Cmd_Tlm_Req`／`HSW_Cmd_Tlm`／`HeatLeftSeatTgl` 等 | **A-VS28**，待判 |

**皆未調和。** 第 2 項之後果最直接：依 R-VS9(1)，訊號逐字名以 LID 表為第一權威，
照 LID 寫入 TC 即寫出匯流排上不存在之名 —— 與 R-VS9(5) 所防者同型，**惟此次錯的是第一權威本身**。

### 2.2 W-25 之陳述更正

07 §7／09 包之「00–02 三輪產物不在版控」為誤（§0）。**A-VS25**，兩層皆有責。

### 2.3 我方之配對缺陷（先報自己的錯）

W-15b′ 首版將 LID 儲存格之**第一個** message 名與該 signal 在 DBC 之**每一個**
出現處交叉配對，得 `MISMATCH` **13**；改為逐 (message, signal) 對配後 **13 → 1**。
**12 / 13 為我方缺陷** —— 與 W-8 之 33 → 1 同型。

---

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | A-VS19 措辭改寫（W-26）；W-15b′ 之配對式由交叉配改為逐對配；07／09 包「不在版控」之陳述更正 |
| **核實無誤** | DBC 之 message／signal 計數與 00H 一致；W-26 之 P1 關閉依據（三種查法皆無輸出） |
| **正確地不動** | A-VS26／A-VS27／A-VS28 皆**登記待判，未自行調和**；未依 R-VS9(1) 逕採 LID 之大小寫，亦未逕採 DBC —— 該衝突屬裁決層 |

---

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| DBC 解析 | `^BO_ (\d+) (\w+)\s*:\s*(\d+)\s+(\w+)` 取 message（id／dlc／tx）；<br>`^\s*SG_ (\w+)\s*:\s*(\d+)\|(\d+)@(\d)([+-])\s*\(f,o\)\s*\[min\|max\]\s*"unit"` 取 signal 全屬性；<br>`^VAL_ (\d+) (\w+) …;` 取值表 |
| LID signal 抽取 | 先以 `([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)` 取 **(message, signal) 對**；無點號者退回裸名 `[A-Za-z0-9_]{4,}` 並過濾停用詞 |
| **配對** | **逐 (message, signal) 對配** —— LID 給了 message 名者，只與 message 相符之 DBC 出現處比對。**非交叉配**（首版之缺陷，見 §2.3） |
| signal 名比對 | **首版區分大小寫**；`NOT_IN_DBC` 者再以**不分大小寫**重掃，以分離「大小寫差異」與「真不存在」。<br>⚠ **若只跑不分大小寫，A-VS27 之三筆會被吸收而看不見** |
| VAL_ ↔ Format | 值字串 `\s+`／`_` 併為單一空格、轉小寫後作集合比較 |
| W-25 | `git ls-files`／`git log --oneline`（唯讀） |
| W-26 | `ls -d`／`find features -maxdepth 1 -name 'vehicle setting'`／`git ls-files 'features/vehicle setting*'` 三法 |

---

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS25** | —（流程類） | 「三輪產物不在版控」為誤；**分析層推測、執行層照抄未查** |
| **A-VS26** | **DR-13（新）** | `$ESS_ENG_ST$` 之 message 歸屬矛盾（LID `ENGINE_FD_2` vs DBC `STATUS_CCAN3`） |
| **A-VS27** | —（我方以 DBC 為準即可，惟需 R-VS9 定案） | LID signal 名大小寫與 DBC 不符 |
| **A-VS28** | **DR-14（新）** | 8 支按鍵請求類訊號不在基線 DBC |
| A-VS19 | — | 措辭改寫（W-26），P1 關閉 |

**DR-13**：`ESS_ENG_ST` 究竟位於哪個 message？LID 與基線 DBC 給出不同答案。Urgency **Medium**（1 token）。
**DR-14**：8 支按鍵請求訊號（`*_Cmd_Tlm*`／`Heat*SeatTgl`／`CmdIgn_FailSts`／`HDRstRelRq_3rdRow`）
於基線 DBC 不存在 —— 是否另有網段之 DBC 未入庫？Urgency **High**（procedure 之操作步驟需要它們）。

---

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，五項**

### 6.1 本輪未執行之作業（具名）

**W-17／W-9／W-22／W-23/W-24 五項全未執行。** 其中：

- **W-22** 為 W-20 之驗證補強 —— 02 上繳 §6.2-3 自陳「三式已窮盡未經驗證」，
  該弱點**本輪未收**，且 W-15b′ 又新增了對 LID 表之依賴
- **W-9** 為 R-VS7 委派句之來源表，framework 階段需要它
- **W-23** 之 C3（我方 `Format` 解析殘缺）**為我方缺陷**，09 包明令「判準化同時修正解析式，
  不得長期以分類遮蓋」—— 未做即等於繼續遮蓋

### 6.2 W-15b′ 自身之界線

1. **`ALL_ATTR_MATCH` 之 14 筆，其「所有可讀屬性」只及於我解析出來的八項。**
   DBC 之 `BA_`（屬性）、`CM_`（註解）、multiplexor 未納入比對 ——
   **「所有可讀」是相對於我的解析器，不是相對於 DBC 格式。**
2. **LID 側只取了 `Atlantis High` 與 `Atlantis(&High)` 兩欄組**，
   其餘四欄組（Powernet／CUSW／Compact）未比對；若某 token 之 Atlantis High 欄
   本身抄錯而他欄正確，本輪看不出來。
3. **21 筆 `NOT_IN_DBC` 中，PROXI 類與「形似 CAN 訊號」之分類為人讀**，
   未寫成判準；下輪重跑會再次全部列出。
