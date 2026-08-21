# 04Z-A1 — scripts/ 之立即保全（不經 git）、git 操作歸屬之釐清

分析層。**追發包，依 R-TM20 聲明**：所依賴之 `04Z_closure.md` 尚未上繳
（`docs/upstream/` 實測仍止於 `04R_corrections.md`）。追發理由：
`scripts/` 三支仍未進 git 且已被覆蓋過一次，**再被覆蓋一次同樣不可復原**
—— 此為現時風險，不能等一輪。

本包**不重述** `04Z` 之 T1–T6，兩者無共用步驟。
**執行順序：先本包 T1（保全，最急），再 `04Z` T1–T6，最後本包 T2–T3。**

---

## 1. `scripts/` 排除於 commit —— 判斷正確

「把另一 session 的產出寫進我署名的 commit 不妥」以及「A-TM20 歸屬未定」
兩個理由都成立，且與 A-TM20 之凍結一致。**維持排除。**

其自陳之代價亦準確：三支仍 untracked，再被覆蓋即救不回來 ——
執行層自己那兩份就是這樣沒的。

## 2. 保全 —— **用複製，不用 commit**

執行層提議以單獨 commit 收進三支。**分析層建議改用複製，理由有三：**

1. **git 是 Pei 的**，複製不是。複製可由執行層立即執行，commit 要等 Pei，
   而風險是現時的
2. 複製**不牽動歸屬**。commit 會把另一 session 之產出納入版本史並帶上
   commit 作者，那正是執行層要避免的；複製只是留一份副本
3. 複製**不改變 `scripts/` 之凍結狀態** —— 來源端唯讀，mtime 不變，
   凍結之 mtime 證據鏈（09:13–09:15）不被破壞

commit 之決定仍歸 Pei，複製不排除日後 commit。

```
R-TM35（分析層裁定，2026-08-21）—— 凍結中之產出物以複製保全，不以 commit

凍結期間之檔案若未進版本控制且有覆蓋風險，一律以複製至本 feature 之
data/ 下留存快照，不以 commit 保全。

理由：commit 屬 Pei，複製不屬；風險為現時，等待有成本。
且 commit 會將歸屬未定之產出納入版本史並附作者，複製不會。

快照須含來源路徑、複製時點、來源 mtime 與 SHA256，使日後可判定
「快照對應的是哪一個版本」（R-TM31 / R-TM33 同一精神）。
```

## 3. 那個 commit —— 一項須 Pei 確認

`34e2da6` 已產生（11 檔、1774 insertions）。

**全部 git 操作屬 Pei** 為本專案常設分工，且本輪每一個下放包之
「不得執行者」首列皆為「不動 git」。故須確認二者之一：

- **(a) Pei 指示執行層代跑該 commit** —— 則無違反，本條僅作記錄
- **(b) 執行層自行判斷而執行** —— 則為分工界線之逾越，須登記

**分析層不推定。** 若為 (a)，執行層於上繳註明「依 Pei 指示」即可關閉；
若為 (b)，登記為 A-TM22 並補訂執行層之 git 界線認知。

**本條不影響該 commit 之內容評價** —— 其排除清單（無 inputs/、無 xlsx/docx、
未含 privacy / vehicle_setting / scripts）與驗證（R-TM 35、G-TM 1、
A-TM 20、tc_id_format 1 處）皆正確，內容無虞。

## 4. `04Z_closure.md` 尚未執行

執行層報「多了一個我還沒讀的下放包」。確認：`04Z_closure.md` 為分析層
2026-08-21 09:50 之下放，其 T1–T6 尚未執行。**本包 T2 即接續之。**

該包之內容為 `04R` 上繳之覆核結果：R-TM33（來源標記）、R-TM34
（columns 補 tc_id）、G-TM2（十二項）、A-TM21（六項缺陷登記），
以及 `backend/verify_structure()` 之唯讀評估指派。

---

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — **最急：`scripts/` 快照保全**（R-TM35）

**先於 `04Z` 之任何步驟執行。** 來源端唯讀，不改 `scripts/` 任一位元。

```bash
SNAP=features/time_management/data/scripts_snapshot_20260821
mkdir -p "$SNAP"

# 先記來源狀態（快照之歸屬依據）
for f in features/time_management/scripts/*.py; do
  shasum -a 256 "$f"
  stat -f '%Sm %N' -t '%Y-%m-%d %H:%M:%S' "$f"
done | tee "$SNAP/SOURCE_STATE.txt"

cp -p features/time_management/scripts/*.py "$SNAP"/

# 複製後複驗：SHA 須逐支相同（-p 保留 mtime，亦應相同）
for f in "$SNAP"/*.py; do shasum -a 256 "$f"; done
stat -f '%Sm %N' -t '%H:%M:%S' features/time_management/scripts/*.py
```

**末項期望：來源 mtime 仍為 09:13 / 09:14 / 09:15**（複製未動來源）。

於 `$SNAP/README.md` 記：

```markdown
# scripts/ 快照 — 2026-08-21

依 R-TM35 保全。來源 `features/time_management/scripts/`，該目錄於
A-TM20 凍結中且未進 git。

**混合來源**：
- `build_batch_context.py` — 本 session 執行層產出（特徵字串
  `Structure ported from` 命中 1）
- `write_back.py`、`lint_tcs.py` — **非本 session 產出**，為 2026-08-21
  09:13–09:14 另一 session 覆蓋所得（特徵字串命中 0）。
  本 session 原產出之兩份已失落，無備份。

歸屬未定（A-TM20，待 Pei 裁）。缺陷登記見 A-TM21，必修項見 G-TM2。
逐檔 SHA256 與 mtime 見 `SOURCE_STATE.txt`。
```

### T2 — 執行 `04Z_closure.md` 之 T1–T6

該包已在 `docs/handoff/04Z_closure.md`，內容自足，本包不重述。
其 T3 會改 `feature.yaml`（不在凍結範圍），T4 為 `backend/` 唯讀評估。

### T3 — git 歸屬之回報（§3）

於上繳明確回答：`34e2da6` 之 commit 為 **(a) 依 Pei 指示** 或
**(b) 執行層自行判斷**。**擇一明答，不得略過。**

若為 (b)，一併回報：當時之判斷依據，以及本輪各下放包「不動 git」之
明令是如何被理解的 —— 此為訂正認知所需，非追究。

### T4 — 上繳

`docs/upstream/04Z_corrections.md`，含 `04Z` 與 `04Z-A1` 兩節。須含：

1. T1 之來源 SHA256／mtime、複製後 SHA256、來源 mtime 複驗
2. `04Z` T5 之全部輸出（含 `scripts/` 三支 mtime 仍為 09:13–09:15）
3. `04Z` T4 之 `verify_structure()` 三項評估
4. T3 之明答
5. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集

### 不得執行者

- **不動 git**（含不 push；分支現 ahead 14 之處置屬 Pei）
- **不寫入、不覆蓋、不修改 `features/time_management/scripts/` 任一行**
  —— T1 為唯讀複製，來源端不得有任何變動
- 不修 A-TM21 之任何一項（凍結中）
- 不改 `backend/`（唯讀評估）
- 不執行任何腳本（含 `--self-test`）
- 不生成任何 TC
- 不碰 `features/vehicle_setting/`
- 不 rm 任何檔案
- 不送出 RD-1
- 不填 `D5`、不組 Scope 值
- 不以 openpyxl 存回任何工作簿

---

## 6. 呈報 Pei

**1. `features/time_management/` 之歸屬 —— 第三次。**
一句話：本 session 繼續，或交給另一邊。前者我下放 G-TM1 + G-TM2
共十二項之修改指令；後者我出交接單，本 session 轉唯讀覆核。
`05`（B1 生成）在此之前不下放。

**2. `34e2da6` 是否為你指示執行層代跑？**（§3）
若是，一句確認即可關閉；若否，我登記 A-TM22 並補訂界線認知。

**3. 三支腳本是否要另開 commit 收進版本控制？**
本包已以複製保全（T1），風險已降。commit 與否屬你，
不急於本輪 —— 但**分支 ahead 14 未 push**，若該機故障，
快照與 commit 一併失去，此點請併同考量。

其餘待你之項（不阻塞）：R-TM10-A1 替代樣式來源（仍無候選）、
RD-1 Q-TM1–3 送出、A-TM18 Comfort 之 (a)/(b) 判定。

## 7. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM35 | 分析層裁定，凍結中以複製保全不以 commit | §2 | ✅ T1（條文落檔併入 `04Z` T1 之 RULINGS 追加）|
| git 歸屬釐清 | 待執行層明答，(b) 則登記 A-TM22 | §3 | ✅ T3 |

**注**：R-TM35 之條文落檔須併入 `04Z` T1 之 `RULINGS.md` 追加動作，
標題行 `## R-TM35 — 凍結中之產出物以複製保全，不以 commit`，
內文為本包 §2 之區塊全文。追加後 `## R-TM` 條數為 **38**（`04Z` 之 37 + 1）。

分析層本包未動 git、未改任何腳本、未觸 `scripts/`、未觸 `vehicle_setting/`。
