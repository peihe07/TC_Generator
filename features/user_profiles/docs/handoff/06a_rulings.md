# 06a 下放包 — 05 輪覆核所生七條（Pei 2026-08-17 裁定，逐字）

05 輪上繳包**核可**，作業 1–6 全數通過。

```text
R-U25 spec 基線之修訂 —— xlsx 為結構、PDF 為內文
      R-U3 之證據（Source ID namespace 一致、135 id 缺漏 0）證明的是
      **結構完整**，非**內文完整**。兩者當時被合為一件，於此分開。
      spec 基線改為：xlsx 提供 outline 結構與 Source ID，
      PDF 提供條文內文與圖形內容；兩者為同一基線之兩面，
      皆已在 BASELINE.sha256 內。
      **前置作業（優先於 framework 定稿）**：對 169 條逐節比對
      xlsx Description 與 PDF 文字層，量出 export 之掉句率與形態。
      若為系統性掉句，outline_map.json 須以 PDF 重建，
      且 04／05 輪之全部判讀須標示其依據面。
      成因：05 輪 §7 第 2 項自陳——PDF 之條文比 xlsx export 完整，
      而本 feature 自 recon 至 framework 之全部判斷皆建於 xlsx 側。

R-U26 spec_popup_ids 之擴充
      由 20 擴為 32，加 `source` 欄標 `xlsx_text`／`pdf_only`。
      原 20 列之記載不刪 —— 它記的是「xlsx Description 欄掃得者」，
      該記載正確，只是涵蓋範圍小於其類別。
      12 個 pdf_only id（PU0575–0579、0586、0587、0609、0612、0614、
      1497、1511）須逐一定位其所屬 section；05 輪只比了集合差。

R-U27 R-U15 之阻斷範圍收窄
      spec PDF p6 已載 PU1087／PU1088 之觸發條件，
      DR #4 所缺者僅為 Pop Up List 中該二列之 popup **內文**。
      故 4.1.1 相關 TC **得以生成**：觸發條件、顯示與否、流程分支皆可驗；
      **僅 popup 內文之逐字 ER 不寫**，該處以 spec 原文之描述為據，
      不推定內容（§8.4.1）。
      PROF-002-03 據此解除阻斷。DR #4 降為 MEDIUM，不再擋章節。

R-U28 A-UP02 / DR #3 之性質重估
      3.1–3.5 有內容且可讀 → A-UP02 非「內容不存在」，
      而是「spec 有而 SWE 未涵蓋」，形態同 Comfort R-C16。
      處置分兩支：
        3.1–3.5      依 R-U22 得作為 PROF-001-01 之 in-scope 依據，
                     不另生成獨立 TC（我方不自造需求）
        10.1/11.1/11.2  變體覆寫條款且無任何 SWE 需求，不生成 TC，
                     列 RD-1 之上游覆蓋缺口
      DR #3 仍送出，性質改為「上游覆蓋缺口」而非「索取缺件」。

R-U29 PLP3（Memory Seat Module）再試一次
      p5 有 11 張點陣圖，PLP3 之列項可能在點陣圖內而非向量文字層。
      以 pdfimages 抽該頁圖後視覺判讀，再定可讀與否；
      仍不可讀才進 DR。
      理由：Memory Seat 連動屬 R-U21 之 B 群測法，
      該清單缺項會直接影響 PROF-001-01 之 ER 範圍。

R-G4-1 R-G4 之修訂 —— 讀者為三個
      `spec_id_to_outline.tsv` 之讀者除 `lint_tcs.py`、
      `make_batch_context.py` 外，尚有
      `features/home/scripts/extract_exemplars.py:97`，
      其用法同 make_batch_context（load_outline_to_chapter → chapter_of），
      受同一危害。原條文之「兩個讀者」為漏數，據實更正。

R-U30 comfort 孤兒檔之處置 —— 延後，登記不動手
      R-G4 生效後 comfort 若重跑 recon，產物將落新名，
      而其 RUNBOOK／INDEX／RULINGS／DECISIONS 四處仍指舊名。
      comfort 已交付，實務上不會重跑，故不於本輪動它。
      登記為跨 feature note，待 Comfort 下次開輪次一併清。
      **本 feature 不得寫入 comfort 任何檔。**
```

## 本包產生之新條文清單（自檢）

- R-U25 ✓　R-U26 ✓　R-U27 ✓　R-U28 ✓　R-U29 ✓　R-G4-1 ✓　R-U30 ✓
  （皆以區塊形式出現）
