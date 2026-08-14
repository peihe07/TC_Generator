# 03 — Comfort HMI / 上繳包 01 覆核 ＋ Phase 2 指示

- 產出層：分析層
- 日期：2026-08-14
- 對象：執行層
- 覆核對象：`features/comfort/docs/upstream/01_phase0_intake.md`

---

## 1. 覆核結論：**PASS**

三個指定 assertion 全 PASS，且以 PASS/FAIL + 實測值形式輸出。反向驗證
（期望值改 402 → FAIL、不寫 `DECISIONS.md`、非零離開；`sys1_export` 為 null
記為 FAIL 而非靜默通過）確認 assertion 在該階段確實可能失敗，符合
「檢查項須確認其在該階段確實可能失敗；不可能失敗者標未實測而非 PASS」。

自加之第三 assertion（相異 citation stem 集合 **恰等於** `[SR24]`，而非
「SR24 是否在其中」）採納為正確作法：通過條件寫成「與參照對象在所有可讀
屬性上一致」，而非「已知的幾項正確」。此形態列為往後 assertion 之預設寫法。

`feature.yaml` 之 spec 路徑寫全名而非 `SYS1_HMI_Comfort_*`：採納。同目錄
存在 SR25，萬用字元會使 R-C1 之遵守取決於命名運氣。此為 R19-3 意義下的
機械強制，非紀律。

`new_feature.py` 原本不產 `RULINGS.md`／`DATA_REQUESTS.md` —— 此發現接受，
且其診斷（檔案不存在則無處提醒任何人去寫，為 AMFM／Projection「裁決只存在
於聊天」之結構成因）成立。修補對後續 feature 生效，不回溯既有 feature。

---

## 2. 分析層自身之訂正

```
R-C4-1  R-C4 之量測母體補標（訂正 R-C4，不取代）

R-C4 原文「共 92 列具此形態」未標母體，違反 §5a「標明量測條件」。訂正：

  母體 = 全部資料列 498（含 95 列 Heading）→ 多行 citation 儲存格 92 列
  母體 = leaves 403（Functional Requirement）→ 多行 citation 儲存格 57 列

兩數皆經執行層獨立實測復現，不衝突。R-C4 之實質規則（取第一行、相異
section 數 assert == 129）不變。

凡條文載有計數者，一律同時載明母體；未載母體之計數視為未完成之陳述。
```

`docs/handoff/01_phase0_intake.md` §2、§3（R-C4 條文）與 §5 之數字均為 498
母體，執行層對齊說明正確，01 不改寫（已被取用）。

---

## 3. 新發現：基線**內**的覆蓋缺口（上繳包未提出處置）

上繳包 §7.2 為佐證 A-CF01 之不可複測，列出執行層可獨立實測者：

```
SR24 export outline 節數      180
037 引用                      129
未被 037 引用                  51
```

**這 51 節是 R-C1 基線之內的未引用節，性質與 R-C5 所處置之 SR25 新增內容
完全不同，且重要得多。** R-C5 處理的是 out-of-scope 文件；這 51 節在
in-scope 文件裡。

上繳包將其列為「A-CF01 之對照數字」，未提出處置 —— 此為本次覆核唯一之
缺口。不責執行層（下放包未指示），但須補。

### 指示（Phase 2 併同執行，分析層自裁之量測定義，非範圍擴張）

產出 51 節之分類清單，寫入 `features/comfort/data/sr24_uncited_sections.tsv`
與 `RECON.md` 之新段，欄位：`outline`｜`polarion_id`｜`description 前 80 字`
｜`分類`。分類取以下四值之一，判準寫入該段開頭：

- `container` —— 章級容器標題，其下層節已被引用
- `assumption` —— 1.x 類範圍聲明，非可驗證需求
- `figure` —— 內容僅為 image 參照，無行為敘述
- `substantive` —— 含行為敘述（含 `shall`／`will`／編號條款前綴如
  `C1.)`、`ICE2.)`）而未被 037 引用

**只分類，不做任何 TC 處置。** 不產 TC、不入 coverage 分母、不列 BLOCKED、
不自行補 RD 項目（§8.2、§8.4.2）。`substantive` 一類之後續處置（是否進
RD-1）屬 Pei 裁定，於清單產出後另裁。

登記 `A-CF08`（OPEN）：SR24 基線內 51 節未被 037 引用，分類待產。

---

## 4. 待 Pei 裁定（本包不自裁）

| # | 事項 | 分析層建議 |
|---|---|---|
| D-C8 | 既有 feature 是否重跑 recon（Privacy `DECISIONS.md` 已簽） | **不重跑**。Privacy 之 diff 經實測全為增益（新增 assertion 段、outline map 段誠實回報無 Outline 欄、`[RULED]` tc_id、兩處措辭修正），**無數字更正**，已簽結論之事實基礎未變。重跑之唯一效果是覆蓋簽署狀態，代價大於收益 |
| D-C9 | `recon.py` 全檔重寫已簽 `DECISIONS.md` 之結構性風險 | 立條文：偵測到簽署標記時**拒絕覆寫**，改寫 `DECISIONS.new.md` 並非零離開。此風險非本次引入，但既已察覺，屬 R16 同類（工具靜默破壞已簽產物），須機械強制而非紀律（R19-3） |
| D-C10 | 51 節中 `substantive` 一類之處置 | 待 §3 清單產出後另裁 |

---

## 5. 不阻塞、確認接受之項目

- **A-CF02**（交付夾 SR25）：執行層本 session 檔案系統不可達，照登未驗 ——
  處置正確。該量測為分析層所作，交付夾實測值以分析層紀錄為準；P7 決定是否
  回填 SR24 時於可觸及時重測。
- **A-CF01**（SR25 節清單）**刻意不驗**：正確。複測需載入 SR25，R-C1 禁止其
  作為查得依據；180/129/51 與 187/58 為不同文件之統計，不得互推。此判斷
  本身即為 §5a「不以自身先前輸出為來源」之正確應用。
- **A-CF06**（`pymupdf` 未裝）：不阻塞。spec_mode A 之文字權威為 SYS1
  export。惟「PDF 具 text layer」目前**不可陳述**，不得在任何文件中假定。
- **A-CF04**（intake spec_mode 提案偏低）：已知限制，recon 之獨立提案為準。
- **A-CF07**（空白範本第 10–11 列樣本殘留）：Phase 1 不改素材，正確。
  **但須於 Phase 3 profile 明文定其寫回時之處置**（覆寫或先清除），
  不得留到 write-back 當下臨時決定 —— BLANK 型之 write-back 為
  「append from first data row」，殘留列會位移首資料列。

---

## 6. 下一步

Phase 2（`DECISIONS.md` [PROPOSED] 覆核簽署）併同 §3 之 51 節分類。
兩者完成後進 Phase 3 framework。

Phase 3 之預告，供執行層預留：403 leaves 中章 2 佔 92、章 16 佔 99，
合計 47%。Layer 2 Test Set 之granularity 成敗集中於此二章之切分
（§4.1.3 兩種失敗形態：過細使 Test Set 淪為 TC ID 副本、過粗產生
Misc 桶）。屆時需 spec 章節結構與 037 分組之交集，兩者皆已在手。

---

## 7. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C4-1 計數須載明母體 | ✅ §2 | 分析層自裁，即時生效 |
| D-C8 / D-C9 / D-C10 | ✅ §4（表列） | 待 Pei 裁定 |

R-C4-1 須貼入 `features/comfort/RULINGS.md`，置於 R-C4 之後（R19-2）。
D-C8～D-C10 未裁定前不得入 RULINGS.md。
