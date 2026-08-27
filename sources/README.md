# `sources/` —— 共用來源文件（R-G27）

```
sources/
  raw/<doc_id>/          原檔（xlsx／pdf／dbc）—— **全 repo 一份**
  extracted/<doc_id>/    intake 抽取之文字形（逐 sheet tsv／md）
  MANIFEST.tsv           doc_id、檔名、sha256、版本、使用 feature
```

* `raw/` 為權威。`extracted/` 為衍生物，二者不符時**一律以 `raw/` 為準**
  （FO §8.6）；抽取工具改版後 `extracted/` 得重產，`raw/` 不得。
* **版控**（Pei 裁，2026-08-27）：`raw/` **不入 git**（同
  `features/*/inputs/`、`forms/*` 之政策，客戶文件本體不入庫）；
  `extracted/` 與 `MANIFEST.tsv` **入**。raw 之身分由 MANIFEST 之 sha256
  與各抽取物首列之 `source_sha256` 兩處釘住 —— 檔案在磁碟，身分在 git。
* feature 端不再存原檔副本，`feature.yaml` 以 `doc_id` 引用。
  **既有 feature 之舊副本不搬**，新 feature 一律走本目錄。
* 抽取以 `scripts/extract_source.py` 為之；其對每個 sheet 自驗
  行數與非空儲存格數，不符即停（27 包 §F-6）。

`_intake/{Feature_Name}/` 仍為**暫存投遞區**（R-G24 附記）；
投遞後之原檔落點為 `sources/raw/<doc_id>/`。
