# 上繳包 01 — AMFM close-out（R14 全項簽署）

> 交付對象：分析層（Claude Project）
> 對應下放包：[`handoff/01_closeout.md`](../handoff/01_closeout.md)
> 日期：2026-08-13
> 結果：**PASS** —— §2.1–§2.7 全數完成；三項停手條件全部檢查，
> 第 3 項觸發（**A-AM17** 已登記，依 §3.3 繼續其餘作業）；另一項排版衝突見 §7.2

---

## 0. 執行摘要

| § | 作業 | 結果 |
|---|---|---|
| 2.1 | `RULINGS.md` 貼入 R14 | 完成，區塊逐字元相同 `b43a75f4…` |
| 2.2 | `PLAYBOOK.md` §6 P7 補登 | 完成，`[ ]` → `[x]`，七項數值全載 |
| 2.3 | `PLAYBOOK.md` §6 Open PENDING 改寫 | 完成，四項全做 |
| 2.4 | `ANOMALIES.md` A-AM08 disposition | 完成，另登記 A-AM17 |
| 2.5 | `DATA_REQUESTS.md` #4 關列、#2b 拆列 | 完成，`#2b` / `#2c` 兩列 |
| 2.6 | RD-1 Q-AM2 增補 | 完成，兩檔同步，區塊逐字元相同 `53e7fa7d…` |
| 2.7 | `features/amfm/docs/` 往返結構 | 完成，`INDEX.md` + `upstream/` 建立 |

**停手條件三項**：第 1 項未觸發（R14 未占用）、第 2 項未觸發（各值全相符）、
**第 3 項觸發** → A-AM17 登記後繼續，依 §3.3 之明文。

**未執行任何 git 操作。** commit message 見 §5。

---

## 1. §2.2 各數值之獨立重驗（§4 第 2 項）

**這是本包最要緊的一項**——下放包 §2.2 明令「若獨立重測與此處不符，停手回報，
不得自行調和」。故**全部七項各自重算，未沿用下放包所載、亦未沿用 tag annotation**。

**量測條件**：
- 對象為 `output/…_Radio_20260129.xlsx` **實際路徑之檔案**，非沙箱副本
- bytes 以 `stat -f%z`；SHA256 以 `write_back.sha256_file`（同 script 之定義）
- legacy hash 以 `write_back.ordered_content_hash(rows, cfg["done_region"]["author_value"])`
  重算，**openpyxl 重新開檔讀取**，非讀取任何既有 report
- 列數以 `write_back.load_rows` 後依 author 欄分割
- lint 讀 `features/amfm/lint_report.json` 現行內容
- leaf 數以 `features/amfm/generated/**/*.json` 實際檔數計

| # | 項目 | 下放包 §2.2 所載 | 獨立重測 | 判定 |
|---|---|---|---|---|
| 1 | bytes | 171,631 | **171,631** | 相符 |
| 2 | SHA256 | `da18b5b0ca9ee5794b67a31ddd317b4a23decf9e0e88380a3717f823e45f3f22` | 同左，逐字元 | 相符 |
| 3 | legacy done-region hash | `30d9e4c0719a2929` | `30d9e4c0719a2929` | 相符 |
| 4 | rows preserved | 158 | **158**（列 10–167） | 相符 |
| 5 | rows regen | 143 (0 placeholder) | **143**（列 168–310） | 相符 |
| 6 | rows total | 301 | **301** | 相符 |
| 7 | lint | PASS, 143 TCs, 102 leaf files, 0 findings | `{"tcs": 143, "files": 102, "findings": []}` | 相符 |

**不符項目：無。** 七項全部相符，停手條件第 2 項未觸發。

### 1.1 兩項加驗（下放包未要求）

| 加驗項 | 結果 |
|---|---|
| legacy hash 全長 | `30d9e4c0719a29292ff50123ead1003262652fbb8f301e93bf974fd2ee17f30a` —— annotation 所載 16 字元為前綴截斷，非另一雜湊 |
| coverage 102/102 | regen 區之 distinct `req_id` = **102**；`generated/` 檔數 = **102**；兩者相等 |
| segment 連續性 | `LEGACY 10–167` + `REGEN 168–310` 兩段，無交錯、無空隙 |

### 1.2 三方比對之來源獨立性

下放包 §1 稱「sidecar / tag annotation / 實測三方逐字元相同」。本層複驗時
**三個來源各自獨立取得**：

| 來源 | 取得方式 |
|---|---|
| sidecar | `cat output/…_Radio_20260129.sha256` |
| tag annotation | `git tag -l -n99 fw036-amfm-regen-v1` |
| 實測 | 對 `output/` 內實檔重算 SHA256 |

三者同為 `da18b5b0…`。sidecar 之檔名欄與實檔名亦逐字相同。

---

## 2. §2.1–§2.7 逐項完成狀態與 diff 摘要（§4 第 1 項）

`git diff --numstat`：

```
11   0   docs/fw036/RD1_amfm_submission.md
12   0   docs/fw036/RD1_questions_amfm.md
75   0   features/amfm/ANOMALIES.md
 3   2   features/amfm/DATA_REQUESTS.md
59  27   features/amfm/PLAYBOOK.md
77   0   features/amfm/RULINGS.md
```

新增未追蹤：`features/amfm/docs/INDEX.md`、`features/amfm/docs/upstream/01_closeout.md`。

### 2.1 `RULINGS.md` — R14 貼入

**停手條件 1 檢查**：既有標題為 `## R1` ~ `## R13`，**R14 未被占用**，
檔案末節為 R13。未觸發。

貼入方式：以 `sed -n '19,85p'` 自下放包 §1 之 ```` ```text ```` fence 擷取後
附加，**未經轉錄**。

| 比對 | SHA256（前 16） |
|---|---|
| `RULINGS.md` L294–358（`[RULING] R14` 至 fence 前） | `b43a75f4…` |
| 下放包 L20–84（同範圍） | `b43a75f4…` |

**逐字元相同。**

**一處依「維持既有格式與編號慣例」所加**：本檔慣例為 `## Rn — <題> (Pei, <日>)`
標題，而 §1 之區塊本身無標題。故於 fence 之上加 `## R14 — AMFM close-out
(Pei, 2026-08-13)` 標題與三行前言（含 R-PV02 未簽署之聲明），
**fence 內文字一字未動**。若分析層認為應純貼無標題，回覆即改。

### 2.2 `PLAYBOOK.md` §6 — P7 補登

`[ ]` → `[x]`，內文改為已完成式。七項數值全數載入，**檔案大小以 bytes 表示**
（R14-C7），並註明 sidecar 未入庫、digest 權威副本在 tag annotation、
與 Projection R-P94 及 `FEATURE_ONBOARDING` §6 一致。

尾段「Pending: Pei approval → commit → `--write` → tag …」整段移除，
改為「**RD-1 送出待 Pei（Tier 3）**」。

### 2.3 `PLAYBOOK.md` §6 Open PENDING — 改寫

| 指示 | 執行 |
|---|---|
| A-AM09 條目刪除，改記一行 | 完成，逐字照 §2.3 所給文字 |
| 087/094、089/095 改寫為裁定結果 | 完成，兩對分列，載明 C4-a 之 value-class 軸與 C4-b 之上游根因 |
| 090/096 移出，改列 RD-1 之下（FYI） | 完成，移入 Q-AM2 條目內，標明「非待裁」 |
| A-AM11–14 加註轉換條件，**現在不得改狀態** | 完成，四條均加註「PENDING → AWAITING_UPSTREAM on the day RD-1 is sent (R14-C5)…Not to be changed before Pei confirms the send」。**狀態未改。** |

### 2.4 `ANOMALIES.md`

- A-AM08 追加「Per-pair disposition — RULED (R14-C4)」段：三對之裁定表 +
  逐對理由；明載 residual 收斂為 087/094（CLOSED）與 089/095（deferred）
- 090/096 自 A-AM08 之待裁範圍移出，改為上游觀察
- **A-AM11–14 狀態未動**（下放包 §2.4 明令）
- 新增 **A-AM17**（見 §3）

### 2.5 `DATA_REQUESTS.md`

- **#4**：Status 改為「✅ 已入 `inputs/`；範圍裁決 R8 stands（R14-C2,
  2026-08-13）—— 關列」，Urgency `Medium（裁決）` → `—`，
  說明欄之「仍待 Pei 裁」改為「經 R8 裁定不進本 workbook」
- **#2b**：主檔標已入 `inputs/`（37,376 bytes，SHA256 `55666213…`），
  Urgency → `—`，並就地標註 A-AM17
- **#2c 新列**：其餘 12 件 O 附件，Status「⚠️ 未入 `inputs/`」，Urgency `Low`，
  Batch impact 欄逐字寫「audit 舉證用，不阻塞任何批次（Diagnostics 批
  097–104 已生成、lint green、零 placeholder）」

### 2.6 RD-1 Q-AM2 增補

`docs/fw036/RD1_amfm_submission.md` 之增補段與下放包 §2.6 所給區塊
**逐字元相同**（`53e7fa7d…`，以 `sed` 範圍雜湊比對）。

`docs/fw036/RD1_questions_amfm.md` 同步追加為 item 5。該檔為問題清單、
非送件稿，格式與縮排不同，故**依該檔既有體例改寫縮排並加註
「(added per R14-C4-d, 2026-08-13)」**，內容之事實與請求逐項一致
（三個 id、兩葉 vs 一葉、深度不一、未改交付簿、v2 統一）。

**排版衝突一項，見 §7.2。**

### 2.7 `features/amfm/docs/` 往返結構

- `features/amfm/docs/upstream/` 建立（先前不存在）
- `features/amfm/docs/INDEX.md` 建立，依 Projection 體例
- 誠實標示 **01 以前之往返全部未落檔**，並指明內容之權威在
  `RULINGS.md` / `DECISIONS.md` / `ANOMALIES.md` / `DATA_REQUESTS.md` /
  `RUNBOOK.md` / `PLAYBOOK.md §6` 六處
- **未重建任何歷史往返包**
- 首列之編號範圍（R1~R13、A-AM01~A-AM16）標為 **†推得**，並載明推導方法與
  量測條件、明示不具權威性
- 本包（01）與本上繳包（01）已登入

**一項未執行並註明**：`reports/` 未建立。AMFM 之報告類文件現散在
`docs/` 根層（`batches-amfm.md`）與 `RUNBOOK.md`；是否比照 Projection 三分結構
重整屬檔案佈局政策，**不在下放包 01 授權範圍內**，已於 `INDEX.md` §3 註明。

---

## 3. `4874049-` / `4874050-` 兩檔之緣由（§4 第 3 項）—— **無法說明，登記 A-AM17**

**實測**（對 `features/amfm/inputs/` 實際路徑，非沙箱副本）：

| 檔名 | bytes | SHA256（前 16） |
|---|---|---|
| `4874050- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls` | 37,376 | `55666213fdbef997` |
| `4874049- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls` | 37,376 | `3fd31f9482b7d660` |

**大小完全相同，雜湊相異。**（下放包述 36.50 KB —— 37,376 bytes = 36.50 KiB，相符。）

**既有記載搜尋**：對 `features/amfm/` 與 `docs/fw036/` 全文掃描 `4874049`，
**除本次新增之記載外零命中**。`DATA_REQUESTS.md` #2b 與 `A-AM07` 之 residual
註記**皆只提 `4874050`**。

**結論：無法自既有記載說明。** 依下放包 §3.3 登記 **A-AM17** 後繼續其餘作業。

**為何不當作無害**：兩檔共用檔名主體與精確位元組數，表面上像「同一份附件被
兩個需求引用」；但雜湊相異，故**不是同一份**。**大小相同而內容不同，正是
「同模板不同資料」之特徵**——也正是「以檔名選檔會選錯」的那一類。此即 AMFM/SXM
既有之標準規則：「檔名相同」不足以證明「內容相同」。

**今日之曝險**：R14-C3 將 #2b（`4874050` DTC 定義表）標為已入 `inputs/` 並關列。
若 Diagnostics 批實際引用的是 `4874049` 那份，該關列即掛在錯的檔案上。
**已生成之內容不受影響**——Diagnostics 批 097–104 已生成、lint green、
零 placeholder，且**兩檔皆未被任何 script 讀取**；曝險在稽核軌跡，不在語料。

**未處置**：何者為需求所引、另一份去留，屬 scope／source 問題（Tier 2/3）。
執行層僅登記與回報。

---

## 4. `INDEX.md` 之建立結果（§4 第 5 項）

見 §2.7。表列兩列：未落檔期（`—`）與本包（`01`）。

**與 Projection `INDEX.md` 之差異**：Projection 之未落檔期為 01–09 共九列
（因其 §2 表已給出各包 slug），AMFM 之未落檔期**併為單一列**——
因 AMFM 無任何來源指出各次往返之主題或序，**逐次拆列即為以記憶產出結構**。
併列是唯一不違反 canon §5a 第十五條的表示法。

---

## 5. 為 Pei 準備之 commit message（§4 第 4 項）—— **不執行**

工作區現有變更全部屬本包，可單一 commit：

```
docs(amfm): record R14 close-out rulings, ack P7, and add handoff index

- RULINGS.md: R14-C1..C7 verbatim (P7 ack, R8 stands, #2b split,
  duplicate_of per-pair, AWAITING_UPSTREAM condition, RD-1 send, bytes)
- PLAYBOOK.md: P7 marked done with delivered artefact measurements;
  Open PENDING rewritten per R14-C2/C4/C5
- ANOMALIES.md: A-AM08 per-pair disposition; A-AM17 opened for the
  4874049/4874050 same-name same-size different-hash pair in inputs/
- DATA_REQUESTS.md: #4 closed under R8; #2b/#2c split
- RD1_amfm_submission.md / RD1_questions_amfm.md: Q-AM2 per-band leaf
  allocation asymmetry (R14-C4-d)
- features/amfm/docs/: INDEX.md and upstream/ created; rounds before 01
  recorded as unfiled
```

**未執行 `git add`、`git commit`、`git tag` 或任何 git 寫入操作。**
本包全程僅用 `status` / `diff` / `tag -l` / `ls-files` 等讀取型指令。

---

## 6. §2.8「不做的事」之確認

| 明令 | 確認 |
|---|---|
| 不修改 `features/amfm/generated/` | 未動，僅以 `rglob` 計檔數（唯讀） |
| 不修改 `output/`、不重跑 `write_back.py` | 未動。**未以 CLI 執行該 script**；僅 `import` 其 `load_rows` / `ordered_content_hash` / `sha256_file` 三個純函式對交付檔**唯讀**重算——§4 第 2 項所要求之獨立重測需要此定義。若分析層認為此已逾「不重跑」之界，請明示，本層改以另寫獨立實作重算 |
| 不建立／移動／刪除 git tag | 未動 |
| 不執行任何 git 操作 | 未執行，見 §5 |
| 不改 A-AM11–14 狀態 | 未改，僅加註轉換條件 |
| 不處理 R-PV02 | 未處理，並於 `RULINGS.md` R14 前言明載其未簽署 |

---

## 7. 本包是否仍有該驗而未驗者（§4 第 6 項，不得省略）

三項。第一項須裁，第二項為下放包內部排版衝突，第三項為觀察。

### 7.1 A-AM17 —— 已登記，須 Pei 裁定

見 §3。**須裁**：兩檔何者為需求所引？另一份去留？
在此之前，`DATA_REQUESTS.md` #2b 之關列掛在 `4874050` 上，此為下放包所指定。

### 7.2 下放包 §2.6 之落點與區塊自身編號衝突

| 出處 | 所指位置 |
|---|---|
| §1 R14-C4-d | 「併入 Q-AM2 **item 3**」 |
| §2.6 指示 | 「在 **item 3** 現有內容後追加」 |
| §2.6 所給區塊自身 | 開頭為 `   5. **Per-band leaf allocation asymmetry.**` |

Q-AM2 現有 item 1–4。若照「item 3 之後」插入，序列即成 **1, 2, 3, 5, 4**。

**處置：依區塊自身之編號放為 item 5（item 4 之後），區塊內文一字未改。**

理由：這是排版位置衝突，非數值或事實不符，故不適用「停手不調和」；
而在兩個相互矛盾的指示之間，**區塊自身所帶的編號是分析層最後寫下的意圖**，
且唯一能產生自洽文件的選擇。已於 `PLAYBOOK.md` 與 `ANOMALIES.md` 之引用處
一併寫為「Q-AM2 item 5」。

**若分析層原意確為 item 3 之子項（如 3.5 或併入 item 3 段內），回覆即改**——
本層不預設。

### 7.3 R14-C4-b 之「不動 v1」在 PLAYBOOK 中之狀態表示

C4-b 裁「維持現況，不動 v1」，待上游答覆後再決定 v2。本層在 `PLAYBOOK.md`
§6 Open PENDING 中將 089/095 標為 **deferred to upstream, not pending here**，
而非留在 PENDING 清單。

**理由**：留在 PENDING 會使該清單同時混有「待 Pei 裁」與「待上游答」兩種，
而 §6 該節之開頭明載「Nothing here may be disposed of in Claude Code — all
are Tier 2/3」，語意是待裁。089/095 已裁完，只是結果為延後。

**但 C4-b 未明言其在 §6 之表示方式**，此為本層之判斷。若分析層希望它仍列
PENDING，回覆即改。

### 7.4 已驗且無異常者

- R14 未占用（R1–R13 為既有全集）
- R14 區塊逐字元相同 `b43a75f4…`
- §2.2 七項數值獨立重測全數相符，另加驗三項
- Q-AM2 增補區塊逐字元相同 `53e7fa7d…`
- A-AM17 編號未占用（既有最大為 A-AM16）
- `#2c` 為新列，未與既有編號衝突
- A-AM11–14 狀態未動
- `generated/` / `output/` / tag 未動
- 未執行任何 git 寫入操作
- `INDEX.md` 未重建任何歷史往返包

---

## 8. 本包產生之新條文清單

**本包為上繳包，未立新裁決條文。**

| 編號 | 動作 | 位置 |
|---|---|---|
| R14-C1 ~ R14-C7 | 落檔（逐字） | `features/amfm/RULINGS.md` |
| A-AM17 | **新登記**（執行層開，依下放包 §3.3 之條件性授權） | `features/amfm/ANOMALIES.md` |
| A-AM08 | 三對裁定，residual 收斂為兩對 | `features/amfm/ANOMALIES.md` |
| A-AM09 | CLOSED（R8 stands, R14-C2） | `PLAYBOOK.md` §6 / `DATA_REQUESTS.md` #4 |
| A-AM11 ~ A-AM14 | 加註轉換條件，**狀態未改** | `PLAYBOOK.md` §6 |
| R-PV02 | **未簽署，未執行** | 於 `RULINGS.md` R14 前言明載 |

**不 commit。**
