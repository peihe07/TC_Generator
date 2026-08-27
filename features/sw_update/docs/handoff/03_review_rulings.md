# 下放包 03 —— 上繳包 01 審結、A-SU2/A-SU3 處分、R-SU5 v2／R-SU7

- 日期：2026-08-27
- 方向：分析層 → 執行層
- 前一包：`02_asu1_rulings.md`；對應上繳：`docs/upstream/02_pending_closeout.md`
- 裁定狀態：R-SU5 v2、R-SU7、A-SU3 處分 —— 即裁；
  A-SU2 之第三家族問題 —— 待 T11 量測後提 Pei

---

## 一、上繳包 01 審查判定

**收。** 判定依據：

- T4' 比對 36 項中 33 `=`；3 項 `≠` 皆屬下放包側量測法缺陷
  （first-id 靜默丟棄、TOC 行數與 brace 總命中混同），非 repo 複本
  與素材不一致，成因全部閉合可重現
- 六條裁決抄錄為程式回讀逐字元比對，OK
- T10 之結構判準（`w:pStyle` + Artifact Type 宣告）有
  「章節物件 87 = TOC PAGEREF 87」交叉驗證，方法採認
- T5' 對 `PU971` 拒絕靜默正規化並登 A-SU3 —— **處置正確**，
  id 認定屬 Tier 2，本包 §二收
- 自評三項如實 —— #1（spec_mode）、#3（PU971 目視）本包轉為任務／
  已由分析層代行；#2（母體 311 無機器保證）維持逐包揭露

T0b 之 `SW UpdateHMI/`（含空格）照 vehicle_category 前例保留，採認。
T9 之 DBC 不綁裁定（vehicle property 非 CAN frame + grep 0 命中雙證）採認。

---

## 二、裁決與處分

### 2.1 R-SU5 v2（抄入 RULINGS.md，逐字；沿革以引用代抄）

```
R-SU5 v2（037 之 Source Requirement ID 欄 —— 依 A-SU2 更正形態陳述）

037 之 `Source Requirement ID` 欄 383 列**全部非空**，實測三形態：

(i)   `SYS-RA-FOTA-{n}` 純形態 —— 370 格
(ii)  `SYS-RA-FOTA-{a}/SYS-RA-FOTA-{b}` 併記 —— 3 格：
      SWE1-FOTA-171（336/334）、175（360/361）、216（506/507）
(iii) `SYS-RA-VF747_V2-{n}`（7 格：225, 226, 227, 228, 230, 239, 240）
      與 `SYS-RA-VF747_V6-{n}`（3 格：241, 242, 243）—— 計 10 格

v1 之「非空 373／unique 364」為 first-id-only 抽取條件下之正確值
（上繳包 01 §三 3.3 已閉合重現）；全集之 FOTA id unique 數由
執行層量測入台帳（T11），後續引用以台帳為準。

拘束照舊：
(a) `spec_reference` 不得取本欄。FOTA 族（i)(ii)：其 SYS-RA 母體
    無對應規格檔可查，理由不變。VF747 族（iii)：v1 之理由**不成立**
    —— 手上有 `Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx`；
    惟引用版本為 V2／V6、在手文件為 V1_R3（版本落差），且其
    物件結構未經 repo 原件實測（A-SU1 之教訓：不得以附件複本
    斷原件）。故 (a) 對 (iii) **暫行維持**，是否為該 10 列另立
    第三錨點家族，待 T11 量測後提 Pei 裁。
(b) 本欄僅作 037 內部追溯保留，不進入任何 TC 欄位（不變）。
(c) SYSAD 分配表三項錯位觀察不立案不再提（不變，Q5）。

沿革：v1 見下放包 01 §二；形態更正依據 A-SU2（2026-08-27）。
```

### 2.2 R-SU7（新條，抄入 RULINGS.md，逐字）

```
R-SU7（CFTS_57 之 Description 物件 —— 不入錨點池）

上繳包 01 T10 實測：CFTS_57 原件含 `[Artifact Type:Description]`
物件 135 個，為結構可驗證之 Polarion 物件，但既非章節亦非需求。

裁定：**不入錨點池**（池維持 565 = 章節 87 + 需求 478）。

理由：TC 之錨指向其驗證之需求單元（IN §10.7(a)、§8.2 需求單元
由上游定義）；Description 為需求之從屬說明內容，以之為錨會使
追溯碎裂於單元之下。

配套：Description 內容於 TC 撰寫中被取用時，**錨落其所屬之
需求／章節物件**。為此 `ANCHOR_POOL.md` 須補「Description →
所屬物件」對照（T12）；對照不可解者列表回報，其內容在對照
落地前不得作為 TC 之依據（IN §8.4.1）。
```

### 2.3 A-SU3 處分（RESOLVED；處分文入 ANOMALIES.md）

```
A-SU3 處分（2026-08-27，分析層裁）：`PU971`（p.46，全文件僅 1 見，
FOTAFU4 段）認定為 `PU0971` 之**原文筆誤**，非文字層抽取漏字。

證據：
(i)  分析層目視 p.46 頁面 render：原文自身印作 `PU971` ——
     同頁同段落三處（頁題「Forced Update Available 2 (PU0971)
     for EMEA」、FOTAFU4、FOTAFU4.1）以 `PU0971` 指同一彈窗
     「ROV Forced Update Available 2」，`PU971` 所指亦為同名彈窗
(ii) `PU971` 不在 Pop Up List 之 1,341 個 unique PU 內；
     3 位數形態逸出全清單之編號型態
(iii) 量測出處：附件頁圖 46.jpeg（分析層）；repo 側複證交 T14

處置：
- `lint.popup_ids` 維持 51（`PU0971` 已在內），不新增 id
- 任何 TC 欄位引用該彈窗一律作 `PU0971`
- 例外：test_item 上半之 verbatim 摘句若含該句，逐字保留 `PU971`
  （R-4 之 verbatim 紀律；IN §11 例外同型 —— lint 對引文段之
  保留 token 對來源驗證，不作 ban）
- 不改規格、不發 DR —— 觀察記錄即止
```

A-SU2：形態陳述面以 R-SU5 v2 結案；**第三家族問題保持 PENDING**，
掛 T11。

---

## 三、任務（本輪 T11–T14）

| # | 任務 | 說明 |
|---|---|---|
| T11 | **VF747 repo 原件結構探測**：`word/document.xml` 之 (i) Artifact Type 宣告有無與分布；(ii) 7 位 ObjectID 有無（brace／裸／bookmark 屬性皆查）；(iii) `SYS-RA-VF747`、`V2`、`V6` 字樣及 id 值 `1061, 1062, 1063, 1064, 1066, 1067, 1348, 175, 183, 184` 之可解性（任何形態之對應段落）。**只量測回報，不裁** —— 第三家族由 Pei 據此裁。併帶：037 Source ID 欄全集 FOTA id unique 數入台帳（R-SU5 v2） | A-SU2 |
| T12 | `ANCHOR_POOL.md` 補「Description（135）→ 所屬需求／章節物件」對照節：id、所屬物件 id、判定脈絡（相鄰結構）；不可解者列表 | R-SU7 |
| T13 | `spec_mode: A` 之 FO §3 **逐條核對**：對五種模式之定義逐條比對本 feature 素材組成，回報逐條判定；不符即停 | 自評 #1 |
| T14 | A-SU3 之 repo 側複證：自 `inputs/` 之 PDF render p.46（或等效逐字元抽取該段），確認 `PU971` 字面在 repo 原件同位存在，證據（方法 + 摘句）附入 A-SU3 RESOLVED 記錄 | 證據鏈閉合 |
| T-抄 | RULINGS.md 追加 R-SU5 v2、R-SU7（逐字；R-SU5 v1 不刪不改，v2 append，沿革行引用即可）；ANOMALIES.md：A-SU3 → RESOLVED（處分文逐字）、A-SU2 → 部分結案註記（形態面 R-SU5 v2，家族面 PENDING 掛 T11） | — |

**不在本輪**：framework、錨定協定、TC、寫回、git。逸出即停照舊。

---

## 四、上繳包要求（`docs/upstream/02_pending_closeout.md`）

1. T11–T14 逐項結果（實際指令 + 原始輸出）
2. T-抄 之逐字核對結果（程式回讀比對法照 01）
3. T11 之量測表 —— 供 Pei 裁第三家族（分析層將附提案）
4. 未結 DR 清單（應仍空）
5. 獨立自評（每包必答）
6. 量測條件揭露（R-G8）
