# AMFM — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-13（下放包 01 §2.7）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| — | 2026-08-09 ~ 08-12 | P0 ~ P7 全程（R1 ~ R13） | **未落檔** ‡ | **未落檔** ‡ | R1 ~ R13 † | A-AM01 ~ A-AM16 † | — ‡ |
| 01 | 2026-08-13 | AMFM close-out（R14 全項簽署） | [handoff/01_closeout.md](handoff/01_closeout.md) | [upstream/01_closeout.md](upstream/01_closeout.md) | R14-C1 ~ R14-C7 | A-AM17 | PASS |

---

## 2. 註記

### ‡ 01 以前之往返全部未落檔

AMFM 於 2026-08-09 至 08-12 走完 P0–P7，**期間之下放包與上繳包全數只存在於
聊天**，`features/amfm/docs/handoff/` 目錄本身直到 2026-08-13 寫入下放包 01
時才由分析層建立。

與 Projection `INDEX.md` 所記之 01–09 缺口**同類**：
- 下放包未落檔 → Projection 登記為 **A-PJ62**
- 上繳包未落檔 → Projection 以 **R-P95** 補正

**編號說明**：本包編為 `01` 係因本目錄之第一份落檔，**不代表 AMFM 之往返序**。
實際往返次數遠多於一次，其序無從還原。

### 內容之權威在哪裡

未落檔的是**往返包**，不是內容。該期間之裁決與異常，其實質內容已落於：

| 檔案 | 內容 |
|---|---|
| `features/amfm/RULINGS.md` | R1 ~ R14 逐字 |
| `features/amfm/DECISIONS.md` | Phase 1 決策表 |
| `features/amfm/ANOMALIES.md` | A-AM01 ~ A-AM17 |
| `features/amfm/DATA_REQUESTS.md` | #1 ~ #5（含 1b / 2b / 2c） |
| `features/amfm/RUNBOOK.md` | feature 事實之權威 |
| `features/amfm/PLAYBOOK.md` §6 | 狀態板（自 RUNBOOK 維護） |

**以上六處為權威。** 缺的是逐包歸屬，不是內容。

### † 推得之範圍

首列之「產生之裁決／異常」欄填 `R1 ~ R13` 與 `A-AM01 ~ A-AM16`，
係以 `RULINGS.md` 與 `ANOMALIES.md` 之現行編號全集扣除本包（01）所產生者
（R14-C1 ~ R14-C7、A-AM17）推得，**非逐包實錄**。

量測條件：對 `features/amfm/RULINGS.md` 之 `^## R[0-9]+` 標題與
`features/amfm/ANOMALIES.md` 之 `A-AM[0-9]+` 出現處掃描，區分大小寫，
去重後取編號範圍。此推導**不具權威性**，僅為索引用途。

**不重建歷史往返包**——重建即為以記憶產出文件，違反 canon §5a 第十五條。

---

## 3. 目錄

```
features/amfm/docs/
├── INDEX.md                        ← 本檔
├── handoff/                        01，共 1 檔（01 以前未落檔）
│   └── 01_closeout.md
├── upstream/                       01，共 1 檔（01 以前未落檔）
│   └── 01_closeout.md
├── batches-amfm.md                 批次記錄
├── family_overlap.md / .json       RD-1 附件（Q-AM1 family-overlap 表）
└── tag-annotation-regen-v1.txt     tag annotation 副本
```

**`reports/` 尚未建立**——AMFM 之報告類文件目前散在 `docs/` 根層
（`batches-amfm.md`）與 `RUNBOOK.md`。是否比照 Projection 之
`handoff/ upstream/ reports/` 三分結構重整，屬版控與檔案佈局政策，
**未在下放包 01 之授權範圍內，未執行**。
