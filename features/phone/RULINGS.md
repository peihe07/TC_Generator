# RULINGS — Phone (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Phone 之裁決權威；
跨 feature 條文承接時註明來源包。

取號依 R-G23 落檔當下現查：本檔由下放包 PH-01 §任務 1 之 `new_feature.py`
於 2026-09-07 產生，落檔前掃描本檔無任何既存 `### R-PH`，故 `{live}` = **1**，
三條依序取 **R-PH1／R-PH2／R-PH3**（與下放包 §2「期望值為 1」相符）。

來源：`docs/fw036/handoff/down/20260907_PH-01.md` §2
（Pei 2026-09-07「用Phone，然後以整份037為主，最後判斷需要增加的再說，
HFP是HFP，可以互相參考，但不可以因為HFP寫到了這裡就沒也寫」）。

---

### R-PH1 — Test Group（Pei 裁，2026-09-07，下放包 PH-01 §2）

```text
R-PH1  Test Group = `Phone`
  本 feature 之工作簿 Test Group 欄一律為 `Phone`（不帶 HMI 尾綴，同 `Media`／`Home` 之既例）。
  R-G42 第三項「037 report 之 feature 全名」於本 feature 之適用結果即 `Phone`
  （037 標題 `SWE1-Phone-HMI` 之 feature 名為 Phone；HMI 為文件類別尾綴，非 feature 名之一部分）。
  TC ID 之 ABBR（R-G42 第二項）由 recon 自 037 req_id 提候選，Pei 於 DECISIONS.md 裁一次。
```

> **執行層回報（2026-09-07）**：`feature.yaml` `test_group: "Phone"` 已落。
> ABBR 候選見 `DECISIONS.md` §1 —— 037 之 req_id 為 `SWE1-HMI-{nnn}`，其
> feature token 為 `HMI`（文件類別，非 feature 名），故 R-G42 第二項之
> 「037 req_id 之 feature 縮寫 token」在本 feature **取不到可用值**；
> 此為 R-G42 二所稱「req_id 無縮寫或有歧義者，由 Pei 裁一次後登 feature.yaml」
> 之情形。`feature.yaml` `tc_id.abbr` 暫為 `null`，不自定。

### R-PH2 — 範圍（Pei 裁，2026-09-07，下放包 PH-01 §2）

```text
R-PH2  範圍 = 整份 037（911 列），增補後議
  TC 生成之母體為 037 `SWE1-Phone-HMI-V0.1` Analysis Report 全部 911 資料列
  （213 parent `SYS-HMI-RA-PHONE-016`～`271` ＋ 698 child），不以資料夾名稱
  「Multiple Phones Paired Simultaneously」或 Multiphone 關鍵字做子集篩選。
  037 未載而 26PI 變更日誌所列之新增項（MPA11、MPA12）**不併入本輪**；
  其處置（登 DR 要求上游補 037，或另開增補包）於 911 列走完後由 Pei 另裁。
```

> **執行層回報（2026-09-07）**：911／213／698 三數實測相符（RECON.md、
> 上繳包 §3）。惟 **FO §5「Every leaf gets a row」之 leaf 判準為
> `Categorization == Functional Requirement`**，實測 754 列（另 157 列為
> `Heading`）；`recon.py` 據此定 `leaves=754`、`regen targets=754`。
> 「911 列」與「754 leaf」不衝突 —— 前者為資料列總數（本條之母體界定），
> 後者為出 TC 之列。Heading 之台帳處置沿 `R-POP5` 之形態，於 DECISIONS.md
> §3 列為 [PROPOSED]，待 Pei 裁。MPA11／MPA12 原文已抽至
> `docs/26pi_delta.md`，本輪不併入。

### R-PH3 — HFP 與 Phone 各為獨立 feature（Pei 裁，2026-09-07，下放包 PH-01 §2）

```text
R-PH3  HFP 與 Phone 各為獨立 feature；可互參，不得互相省略
  (a) HFP（CFTS026）之既有 TC 得作為 Phone 之寫法參考（步驟句式、通話情境之 setup 型態）。
  (b) Phone 之任一 037 列，不得因 HFP 已有語意相近之 TC 而不寫；覆蓋完整性以本 feature
      之 037 為唯一判準（FO §5「Every leaf gets a row」）。
  (c) 反向亦同：本 feature 不回頭改 HFP。
  (d) 互參時只參考寫法，不複製其 spec_reference —— 追溯各歸各母體（IN §8.4.2）。
```

> **執行層回報（2026-09-07）**：HFP 交付本
> `…_CFTS026_HandsFreePhone_20260316(Refine).xlsx` 實測 136 TC 列、13 個
> Test Set、Test Group 一律 `HandsFreePhone`、TC ID 前綴一律 `newR1L`
> （R-G42 生效前之本，不回歸）、`Specification Reference` 136/136 為
> `CFTS026-*`。與本 feature 之 `{檔名}_{章節號}` 形制**無交集**，
> (d) 之「不複製 spec_reference」在形制上即自然成立。清單見上繳包 §4-4。
