# DATA REQUESTS — Power (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/power/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

來源：下放包 01 §G、下放包 02 §G。撤回列不刪、不重編號，保留作為裁決跡證。

| DR | Urgency | 內容 | 阻斷何物 | Anomaly |
|---|---|---|---|---|
| DR-PW1 | **High（live）** | `SWE-PM-089` 之真實上游來源為何？（`SWE1-PM-ANT-008` 非 SYS2 id） | 該 leaf 之 TC 及其 `specification_reference` | A-PW01 |
| DR-PW2 | **撤回** | SYS2 匯出之**收錄規則**為何？—— 包含（a）CFTS009 `Sys-RA-PM-0197`–`0206` 連續十條缺失；（b）CFTS009 本文 904 條需求中未被引用之 547 條內，有 **140 個需求錨點**標 `EE Architecture: Atlantis High/Mid`（`Atlantis High, Atlantis Mid` 73 + `Atlantis Mid, Atlantis High` 67，二者為同一集合之不同排序寫法），似不應被濾掉。**（R-P7 撤回：範圍 = 037 之 115 leaf）** | 已解除 | — |
| DR-PW3 | **Medium（live）** | `Sys-RA-PM-0334` 引用之 `4942087` 屬何文件？ | A-PW02 | A-PW02 |
| DR-PW4 | **撤回** | 037 `Priority` 之 `High`/`Medium` 如何映射至 FW036 `P0`–`P3`？**（R-P8 撤回：priority 依 TC 測項判定）** | 已解除 | — |

**本表現存 live 項僅 DR-PW1 與 DR-PW3。** 02 包無新增 DR。

> 註（02 包）：DR-PW3 之證據描述已於 ANOMALIES A-PW02 訂正 ——
> `Sys-RA-PM-0334` 之 `4942087` **可被 `\d{6,8}` 正常解析**，
> 其缺口在於該 item id 無法解析至任一 CFTS 章節，非 token 缺失。
> DR 本身之問題（`4942087` 屬何文件）不變，仍為 live。
>
> **DR-PW1 / DR-PW3 皆不阻斷 framework 定版；當前阻斷 framework 者為 §E
> leaf 分布之重裁，屬裁決事項而非資料事項，故不列入本表。**
