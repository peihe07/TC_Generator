# 04a 下放包 — 積欠五條之裁定（Pei 2026-08-17 全數裁定，逐字）

此五條於 02／03 輪之聊天提出，本輪首次落檔。

```text
R-U13 .gitignore 之 archive/forms_superseded/BASELINE.sha256 例外
      —— 追認（內容成立），程序補正。
      追認範圍僅限本次已作之單行例外與其註解改寫，不及其他。
      明訂：版控政策一律先裁後改；執行層不得以「某條裁決之必然結果」
      推導出對 .gitignore／入庫範圍／tag 之授權。
      成因兼含分析層起草不全（R-U12 未處理追蹤狀態），一併留檔。

R-U14 A-UP09 之解除條件
      文字修補不構成 RESOLVED。解除條件 = 機器檢查存在且實跑：
      對產出檔驗 x14:dataValidation 節點數與 zip member 集合，
      比對來源母本（可借 Comfort write_back §3.3 之同型 assertion）。
      **該 gate 立起並實跑前，本 feature 之寫回實作不得開工。**
      A-UP09 維持 PENDING。

R-U15 DR #4（PU1087／PU1088）之阻斷範圍
      非 Phase 1 阻斷，recon 與 framework 不受其擋。
      阻斷範圍限於 spec 4.1.1（Profile Setup）之 popup 引用：
      該章相關 TC 於 DR #4 到齊前不生成，不得以鄰近 PU id 推定內容
      （§8.4.1 禁止捏造）。
      索取標的：載有 PU1087／PU1088 之 Pop Up List 版本。
      現有 SR24 Post 2A (Dec 15, 2023) 已驗為正確文件家族、
      兩缺者落在編號區間內（PU0001–PU1578，空號 248）——
      即「不是版本不對，是這一版沒有這兩列」。

R-U16 037 採認
      inputs/ 之 037（SHA 9d176dde…）為本 feature 之權威需求來源。
      Phase 0 之全部 037 側數字係分析層於 Project 附件副本上量得，
      未與本檔比對雜湊，一律重測不沿用。
      BASELINE.sha256 依 R-C20 比照更新，涵蓋 inputs/ 全部檔案。
      （執行層 03 輪已完成，6/6 OK。）

R-U17 inputs/ 之 spec 副本處置
      兩份 R1L-R 已驗為逐位元組相同（SHA 368d5874…）。
      依 Comfort R-C11 單一來源原則：由 Pei 刪除 inputs/ 副本，
      spec 引用路徑維持 spec-index/。刪除屬不可逆，執行層不得代勞。
      **反對意見已記錄**：執行層於 03 包 §5 主張兩份各自受檢
      正是日後任一份被改動時會出聲的機制，合併會關掉該能力。
      該意見未被採納；若日後改採雙份併存，須以新條文取代本條，
      不得以「當時有人反對過」為由逕行回退。
```

## 本包產生之新條文清單（自檢）

- R-U13 ✓　R-U14 ✓　R-U15 ✓　R-U16 ✓　R-U17 ✓（皆以區塊形式出現）
