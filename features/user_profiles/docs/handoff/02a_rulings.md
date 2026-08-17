# 02a 下放包 — User Profiles 裁決條文（Pei 2026-08-17 裁定，逐字）

承 `docs/upstream/01_intake.md` 之覆核。**01 輪已核可，不退回。**

```text
R-U8  Recon 閘值與判準（取代 01b_tasks.md 作業項 3 之預期值）
      三個閘一律以 Categorization 欄之逐列計數為單位：
        functional_requirement_count == 180
        heading_count == 25（欄值等於 "Heading" 者，非 len(headings)=27）
        out_of_scope_count == 2
      葉節點 182 之 ID 前綴形態值降為對照輸出，不作閘。
      依據：Comfort R-C3 逐字禁止以 ID 形態判定 leaf，
      recon.py:568 已將其標為 "the heuristic that the ruling BANS"；
      canon §5a 第 17 條「既有政策優先」。
      生成母體維持 180，不變。
      **本條之成因為下放包之誤**：01b 同時寫入「leaf = Categorization
      以 Functional 起始」與「葉節點 182、扣 2 得 180」，兩者單位不同，
      在該判準下 182 不可能量得。A-UP07 判定成立，執行層停下為正確。

R-U9  Pop Up List 來源
      以 features/comfort/inputs/Pop Up List HMI R1 SR24 Post 2A
      (Dec 15, 2023).xlsx（SHA b0827f02…，見 Comfort BASELINE.sha256）
      為候選，先驗本 feature 引用之 20 個 PU id 之涵蓋率再採用。
      採用後比照 Comfort R-C11 移入 spec-index/ 作單一來源，
      不在各 feature inputs/ 各留一份。涵蓋不全才轉 DR 索取。
      A-UP06 之處置以本條為準：素材未必缺，先驗再說。

R-G3  framework.md §Workbook sync 之範例程式碼（全域）
      該節範例為 openpyxl + wb.save()，對 rev C 工作簿會摧毀 R 欄
      x14 dataValidation（A-UP09 實測：節點 1→0、zip members 48→47、
      而 P／T–Z／AF 三條 legacy DV 存活，表面像無害重封裝）。
      須於該節加禁用警示，並將範例改寫為 xlsx_surgical splice。
      屬跨 feature 缺陷，非 User Profiles 專屬。

R-U10 A-UP08 —— 採 (b)
      rev C 起 `Test Case Framework` 分頁不列為交付要求；
      framework.md §Workbook sync 之該項改標「rev A/B only」。
      理由：rev C 為現行官方表單且無該分頁，該分頁係 Media 時期
      工作流產物，非 STLA 表單要求。不因此產生新 DR。

R-U11 A-UP05 —— 結案為「歷史記載失效」
      20260816_ext 之 mtime 2026-08-17 09:45:54，15 秒後另存為
      20260817_ext；容量擴充（B 欄 601→1411）發生於 FORMS.md 記載之後，
      故原記載之量測對象已不存在。FORMS.md 維持雙欄並列，原記載留為歷史。
      **記載限制**：本條依 Pei 裁定結案，**非經成因查證確認**。
      兩者不同，不得日後被引為「成因已查明」。

R-U12 歸檔三檔之雜湊保護
      於 archive/forms_superseded/ 建 BASELINE.sha256，涵蓋三檔。
      理由：R-G2 保住了檔案，雜湊卻只記於 FORMS.md；
      而 R-U6 之 style authority（Home 225 列工作簿）正倚賴其中一份。
      保住檔案與保住雜湊是兩件事。
```

## 分析層自陳之錯誤（一併留檔）

1. **01b 之預期值 182** —— 見 R-U8。違反既有政策查核義務。
2. **037 素材從未落 repo** —— 分析層整輪以 Project 附件作業，
   下放包卻點名該檔，形成空指（A-UP04）。DR #1 因此產生。
3. **bytes 由 KB 顯示值反推而報為實測** —— 聊天中曾報
   `20260121 = 65,822`、`Home_20260809 = 119,890`，實測為 **65,823**／
   **119,885**。SHA256 兩者皆相符，內容無誤。repo 內記載由執行層以
   `stat` 實測寫入，未受污染；本項僅為分析層陳述之更正。

## 本包產生之新條文清單（自檢）

- R-U8 ✓　R-U9 ✓　R-G3 ✓　R-U10 ✓　R-U11 ✓　R-U12 ✓（皆以區塊形式出現）
