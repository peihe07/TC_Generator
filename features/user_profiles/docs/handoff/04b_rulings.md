# 04b 下放包 — 03 輪覆核所生六條（Pei 2026-08-17 裁定，逐字）

03 輪上繳包**核可**，作業 1–6 全數通過。以下六條為覆核所生。

```text
R-U18 A-UP04 → RESOLVED
      037 已落 inputs/，SHA 9d176dde… 入 BASELINE，
      三閘 180／25／2 相符，表頭列實得 row 7。
      **記載限制（永久）**：Project 附件副本不在 repo，
      其與 inputs/ 這份之同源性永不可證。
      故 Phase 0 之 037 側數字非「被複驗」，是「被取代」；
      日後不得以「Phase 0 已驗過」為由跳過重測。

R-U19 135 / 133 分立
      data/expected_cited_sections.tsv 維持 135 列
      （記「037 引用了哪些」，該記載正確，不改）。
      另立生成集合 133（扣 4.7、5.11 —— 該二 outline 之唯一引用者
      為 R-U4 排除之 PROF-017／035），作為覆蓋率分母與 batch 排程依據。
      兩數不得互相取代；引用時一律具名是哪一個。
      R-U3 之證據行「135 個 section id 缺漏 0」仍為真，
      但它不是覆蓋率的分子。

R-U20 Layer 2 定案 —— 採 B 案，8 個 Test Set
      Preference Storage (ch4, 28)
      Profile List        (ch5, 40)
      Defaults            (ch6, 11)
      Welcome Flow        (ch7, 14)
      Setup Flow          (ch8, 25)
      Editing             (ch9+ch10, 25)
      Connected Account   (ch11, 6)
      Valet Mode          (ch12+ch13+ch14, 31)
      合計 180。
      **命名判準**（解執行層自陳之不一致）：§4.2 禁止的是重複
      Test Group 之「整體」—— 即不得出現 "User Profiles xxx"；
      單一詞 Profile 在承載能力語義時允許。
      故 Profile List 成立；ch6 取 Defaults、ch7 取 Welcome Flow
      （去 Screen／Popup 之 UI widget 名）。

R-G4  recon.py 之輸出檔名歸屬（全域）
      recon.py 之 leaf→section 產物一律寫
      data/recon_leaf_to_section.tsv；不得寫 spec_id_to_outline.tsv
      （後者歸 build_outline_map.py，內容為 spec 側索引，兩者不同物）。
      並加前置檢查：腳本不得無聲覆寫既存之 tracked 檔，
      偵測到即中止並報告，不自行備份、不自行還原。
      **改動 recon.py 前**須先查 features/home 之 lint_tcs.py 與
      make_batch_context.py 實際讀的是哪一種內容，確認後才動。
      成因：本 feature 先建 spec 側索引才跑 recon，順序與
      home／comfort 相反，後者遂無聲覆蓋前者，git status 僅顯示 M。

R-G5  git 禁令之正面條款（全域，重申並擴充）
      「全部 git 操作屬 Pei」包含還原、回退、checkout、restore、
      stash、clean。
      追認 03 輪已作之 git checkout（結果正確，被丟棄者已另存為
      data/recon_leaf_to_section.tsv）；追認範圍僅限本次單一檔案。
      **遇覆寫事故之正確作法**：兩版皆保留（改名並存）、上報、停手，
      不自行還原。理由：checkout 丟棄工作區變更且不可救回，
      執行層無從確知該檔是否另有未提交之他人變更。
      本條與 R-U13 為同一失效模式之第二次發生（前次為 .gitignore）：
      以「某條裁決之必然結果」自推授權。

R-G6  上繳包之記載一致性
      03 包 §7.1 記「git checkout 還原」而 §8 記「git 未執行」，
      同份文件互相矛盾。§8「本包所動之檔」須含 git 動作，據實更正。
      往後「未執行 git」一語須與全文動作清單逐項對得起來；
      摘要與內文不符者退回，不予核可。
```

## 本包產生之新條文清單（自檢）

- R-U18 ✓　R-U19 ✓　R-U20 ✓　R-G4 ✓　R-G5 ✓　R-G6 ✓（皆以區塊形式出現）
