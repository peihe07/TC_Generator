# spec_reference 交付語料調查（2026-08-21）

量測條件：讀取 10_Reviewing/00_TestCase 下 7 本已交付 036 之
「Specification Reference 規格參考」欄（唯讀，openpyxl 沙箱副本），
逐 cell 逐行分類；區分大小寫；行=以換行切分後之單元。
樣本：BT 20260729 / DealerMode 20260417(done) / HFP 20260316(Refine) /
Media 20260625 / Projection 20260623 / Home 20260809 / AMFM 20260810，
共 2,489 資料列。

## 一、既有軌道 = 兩大格式家族，按 spec 型態分流（非偏離）

| 家族 | 格式 | 使用者 |
|---|---|---|
| A. CFTS 母文件 | `CFTS{nnn}-{ObjectID 7位}` | DealerMode(全) HFP(全) BT(主) AMFM(全) Projection(混) |
| B. HMI Logic 文件 | `{檔名}_{章節號}` | Home(全) Media(主) Projection(混) |

ObjectID 即 CFTS 文件各物件之大括號號碼（Polarion object ID）。
BT/Projection 另有 `SYS3_*` 與 `SYS-RA-*` 前綴，屬 SYS3/SYS-RA 追溯來源。

## 二、偏離點（實測）

1. **分隔符**：AMFM 32 列用 `; `（僅 PeiPYHsu 列）；其餘全語料
   多來源慣例 = 一來源文件一行（newline），同文件多 ID 以 `, ` 續列
   且前綴敘明一次（Projection 121x `..._NRL-154418, NRL-154724` 型）。
2. **排序**：同 cell 內多 CFTS ObjectID 升冪/亂序混雜
   （BT asc=44 / mixed=51；HFP 4 列全反序）。無穩定升冪慣例；
   實際語意近「主要驗證對象在前」。canon §10.7「lowest section first」
   與語料不符。
3. **檔名 token 化**：Home 216 行檔名帶空格；Media 644 行 + Projection
   175 行帶底線。canon §10.7 兩個範例各示一種，自身歧義。
4. **同檔名拼寫漂移**：Pop Up List 於 Media 出現三種
   （`(Dec_15,_2023)` / `(Dec_15_2023)` / 無括號），Projection 統一
   `(Dec_15_2023)` 34 行。
5. **短號混入**：非 7 位 ObjectID 之 CFTS 需求號散見
   （AMFM: CFTS019-718、CFTS024-605、CFTS024-707、CFTS004-1316 各 1；
   Projection: CFTS025-4660 ×7）— 兩套 ID 制混用未標明。

## 三、對 canon §10.7 之判定

§10.7 僅成文了家族 B（filename_section），家族 A 佔語料多數卻無條文；
排序條文與語料不符；檔名 token 化未定一制。**需增補與修訂。**
提議條文見聊天（待 Pei 裁定後回寫 canon 與 feature profiles）。

## 四、對進行中 feature 之直接影響

- **Time Management**（CFTS015 母文件）：spec_reference 應採家族 A
  `CFTS015-{ObjectID}`（例 `CFTS015-4813920`），非 filename_section。
- **Vehicle Setting**（CFTS044）：同上，與既有錨鏈
  （SYS-RA → SYS2 → Polarion 7 位 → CFTS 章節）一致。
