# 下放包 12 — vsm_v43：b2-1 生成 —— Forward Collision Warning（15 leaf，R-VT25(d)）

日期：2026-09-02　取號：`docs/handoff/` 實測有 00–11，取 12
台帳不重生；DR 不代發；不寫工作簿；已凍 b1 不動。

## 〇、首項

framework v2 表之「待 Pei 准」標籤改「鎖定 (R-VT24)」（R-VT25(a)，一行）。

## 一、契約

生成規約沿用 vsm_v42 05／11 包契約＋兩線全部教訓之固定自檢（E56 型逐字全等斷言對 `title_source_description`；bus-error 式限測試員送出步；回饋型先建請求態；VAL_ 缺值揭露；UI 名取規格具名註來源；詞界比對；發起態入 Procedure）。V43 專屬：D 欄 Sys-RA 實名＋Remarks 逐列 `Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1)`；spec_reference 雙錨（spec 前 Sys-RA 後，R-VT22(c)：`spec_section` 欄直取，`direct`／`segment_map` 皆可用，`none` 者只寫 Sys-RA 錨）；spec 錨前綴逐字 `Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_{節號}`（實際檔名 token 化，首列回報所用前綴供覆核）。

## 二、本批

1. 母體：v2 之 `test_set = Forward Collision Warning` 且 `status = active`，**15 列**（chapter .06，含解得 12）。
2. 規格節：`spec_section` 應為 `1.11.1.1.6`（segment_map Δ0 區）——切出該節全文為行為佐證；test_item 上半仍取 SYSRA Description 逐字。
3. 訊號：v5＋val_tables_v43（FSFCWPlus 族解得有 VAL_）；內部 `FSCWPlus_Setting.Req`／`TLM_Vehicle_Setup_Menu.Info` 依 b1 先例逐一實測 UI 面（規格具名／HMI 錨），可走則走、否則 `PENDING: DR-VT4 <名>`——**不得沿用 b1 之 0 PENDING 結論（R-VT20(d) 防推廣）**。
4. 規格拼字（`Forward Collision Warinig` 等）verbatim 保留，佐證入 DR-VT2 清單。
5. 輸出 `generated/b2_fcw/`（json＋md＋INDEX），E 判準沿 E38–E45／E51／E56 型（15/15）。

## 三、順做（R-VT25(c)，K-14 新法）

`1.14.1` 表列解析 ID↔參數名 → 參數名逐字對 `1.14.2.1.NN` 節文 → 命中者於 `leaves_interim_v2.tsv` 補 `spec_section`；補列數與仍 none 數上繳（E87）。

## 四、上繳（`docs/upstream/12_b2_fcw.md`）

同 05 包上繳結構；E 逐項＋E87；PENDING 清單；§K；獨立判斷；gate_all 歸因。**綠色通道計數第一批。**
