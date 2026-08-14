# 上繳包 03 — R24 貼入、A-PV14 平台 diff

執行層 → 分析層。2026-08-13。回應 `docs/handoff/03_platform_baseline.md` §5。

**執行順序**：依 Pei 指示先跑 04 包（profile 草案為下一個 chat 觸點）再跑本包。
兩包無相互依賴。

**依 Pei 指示跳過兩項**：
- §2.2（先執行 02 包 R23 八條）—— **已於稍早完成**，結果見
  `docs/upstream/02_template_rulings.md`。故 §5.1 之「第 2 項完整執行結果」
  不在本包重述。
- §2.4（建 `inputs/BASELINE.sha256`）—— **已由 R26-2 取代**，落點改為
  feature 根 `features/privacy/BASELINE.sha256`，已建立並納入版控。
  §5.3 因此改記為「以新落點完成」。

---

## 1. 完成狀態

| # | 作業 | 狀態 |
|---|---|---|
| 1 | R24 貼入 `RULINGS.md` | ✅ 置於 R25 之前，維持編號順序 |
| 2 | 先執行 02 包 | ⏭ 跳過（已完成）|
| 3 | R24-2 diff 與換檔 | ⚠️ **diff 完成、換檔未執行** —— 見 §2 |
| 4 | 建 `inputs/BASELINE.sha256` | ⏭ 跳過（R26-2 取代）|
| 5 | A-PV14 狀態更新 | ✅ 依實際結果，維持 PENDING |
| 6 | `PLAYBOOK.md` §6 同步 | ✅ |

停手條件：第 1 項（02 包觸發停手）—— 02 包確曾觸發其停手條件 1
（`RULINGS.md` 已存在），但該包 §3.1 之處置為「停止新建，改為附加，
**續行第 2–6 項**」，非全包停止，故本包第 3–6 項照行。
第 2 項（SCV/AMP 有差異）**未觸發**。第 3 項（`.gitignore` 排除）不適用。

---

## 2. §5.2 —— R24-2 diff 輸出與結論

### 2.1 量測條件

- 全程唯讀。以 `python-docx` 抽出段落文字＋表格儲存格文字，去空行後逐行
  `difflib.SequenceMatcher` 比對
- 條款範圍依 R24-2(1)：`CTRL_AMP.*`、`$VolumeSCV$`、`Acustic_Configuration`
  （併測 `Acoustic_` 拼法）、`Audio_System_Type`、`amplifier` / `AMP `
  之 present / not present 敘述

### 2.2 結果

| | HDCC28 副本 | `inputs/` 現存 |
|---|---|---|
| SHA256 | `e20ba7a4f8f7…` | `49dd3c31405f…` |
| bytes | 177,388 | 184,808 |
| 非空行 | 404 | 403 |
| 差異 hunk | — | **9** |
| SCV/AMP 相關行數 | **33** | **33** |
| **落在 SCV/AMP 條款之差異 hunk** | — | **0** |

### 2.3 九個 hunk 逐條（皆不在條款範圍內）

| # | 類型 | 內容 |
|---|---|---|
| 1 | 作者 | `Keerthi Kambala` → `Abhishek Dwivedi` |
| 2 | 適用 VF | `VF610` → `VF672` / `VF505` / `VF508` |
| 3 | 訊號表 | 少 `ENGINE_FD_2.EngineSts_W` |
| 4 | 訊號表 | 少 `BCM_FD_9.PowerModeSts` |
| 5 | 訊號表 | 多 `TBM_FD_1.SOSCallType` |
| 6 | 訊號表 | 少 `VSIM_FD_1.AudioMuteRq`（Audio mute request）|
| 7 | SGW gating | `B-CAN` → `BCAN`（同一 gating，寫法不同）|
| 8 | 修訂履歷 | 見 §2.4 |
| 9 | 空白 | `MdsActforANC` 後空格數 |

### 2.4 平台來源之獨立佐證

```
HDCC28 −  Initial release derived from VF651_V6_R1_PHDCCMCA
inputs +  Initial release Derived from VF651_V6_R1_PDT26
```

稽核原本是以**檔案路徑**推得平台歸屬（`28DT_2A_LTM/DT28_split` vs
`HDCC28_Split`）。hunk 8 讓同一結論在**文件內文**獲得獨立佐證：
`PHDCCMCA` 對 `PDT26`。A-PV14 的事實面至此無疑義 ——
這正是 R24-2 §5a 所立「『檔案在正確的交付夾裡』不蘊含『檔案來自正確的
平台樹』」的完整實例。

### 2.5 條件判定：R24-2(2) 成立

SCV/AMP 條款零差異 → 適用 (2)「換入 HDCC28 版，記為『平台標籤更正，
實質內容無影響』，不回溯任何已簽裁決」。**(3) 停手回報之條件未觸發。**

### 2.6 ⚠️ 但換檔未執行 —— 權限攔阻

覆寫 `features/privacy/inputs/` 之該檔的動作被 Claude Code 之權限分類器
**攔下兩次**（先以 Python `shutil.copyfile`，再以 `cp`，皆遭拒）。
**執行層停止嘗試，未以任何其他方式繞過。**

待辦（需 Pei 執行或授權）：

```bash
cp "/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/VF/VF_Split document/HDCC28_Split/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx" \\
   "features/privacy/inputs/Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx"
```

**換檔完成後尚須連動三處，目前皆維持換檔前狀態**：

1. `BASELINE.sha256` 該行 → `e20ba7a4f8f7…`，檔頭記「依 R24-2(2) 換版」
   （BASELINE 的更新規則要求連同裁決編號）
2. `ANOMALIES.md` A-PV14 → RESOLVED
3. framework Part VI 注 3 與 profile §6 之「A-PV14 未結案前不得引用 V6_R2」
   解除；Part VI 批次計畫表之 B2 依賴欄改為無

**在換檔完成前，V6_R2 仍不得列為 `specification_reference`**。
B1（pilot）不受影響 —— 其五片葉子刻意避開 AMP-present 分支。

---

## 3. §5.3 —— `BASELINE.sha256` 建立結果

**已建立，落點為 R26-2 指定之 feature 根**（非本包 §2.4 所寫的 `inputs/`
之下）：`features/privacy/BASELINE.sha256`，8 檔，已納入版控。
`shasum -a 256 -c` 實測 8 OK、exit 0、零警告。全文見
`docs/upstream/04_framework.md` §3。

另註：若照本包原路徑建於 `inputs/` 之下，會踩到本包停手條件 3 ——
`features/privacy/.gitignore:2` 的 `inputs/` 會把它整個排除，進不了版控。
新落點無此問題。

**本檔目前記錄的 V6_R2 為 `49dd3c31…`（DT26 版）**，換檔後須同步更新。

---

## 4. §5.4 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。**

1. **條款範圍是 R24-2 給定的，我沒有質疑它，但其中一條差異值得分析層再看。**
   hunk 6 顯示 HDCC28 版有 `VSIM_FD_1.AudioMuteRq`（Audio mute request）
   而 `inputs/` 版沒有。它不在 R24-2(1) 所列的五個詞集內，故依規則不計入
   「SCV/AMP 條款差異」—— 但它是**音訊路徑訊號**。同理 hunk 3/4/5 的三個
   訊號差異也都在音訊/電源域。
   我依 R22-5 **未把它們重新分類**（分類會承載因果假設），照實列出全部九個
   hunk 供裁定。若分析層認為 mute 屬 SCV/AMP 範圍，(2) 之結論須重審。

2. **diff 只比對文字，未比對圖與嵌入物件。** `python-docx` 抽的是段落與
   表格文字；兩份的圖片、圖表、頁首頁尾、註解**未比對**。
   兩份 size 差 7,420 bytes 而文字幾乎相同，差額可能就在這些非文字部分。
   R24-2(1) 說「全文 diff」，我做的是全文**文字** diff —— 這是限縮，須說明。

3. **換檔後的連動三處，我只列了清單，沒有預先驗證。** 特別是第 3 項
   （framework 注 3 與 profile §6 解除）牽涉兩份已寫好的文件，
   實際改動時要確認措辭不會留下矛盾（例如 profile §8 說「A-PV14 blocks B2」
   也要一併改）。**目前 profile 仍是草案未核可**，若在核可前換檔，
   兩者要一起改。

4. **R24-1 所立之 §5a（不可逆範圍決定不得依單次量測）尚未回頭檢查
   既有決定。** 該條追溯性地否定了「08 包作廢」的理由。但 repo 內是否還有
   其他依單次量測做出的不可逆決定，**未盤點**。本包範圍限 Privacy，
   且 Pei 已裁示專注 Privacy，故未查 —— 但這條規則是通則。

<!-- UPSTREAM-COVERS: 03 -->
