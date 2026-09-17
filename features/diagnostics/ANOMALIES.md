# ANOMALIES — FW036 Diagnostics HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-DIAGnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

| 標記 | layer | 事由 | 出處 | 型 | 狀態 |
|---|---|---|---|---|---|
| `[A-DIAG01]` | execution | R-DIAG5(c) 之 NRC／SID 適用空白：230 列 negative／unsupported 中 205 列（89%）CFTS004 與 037 皆無 NRC 值；I/O Control SID `0x2F` CFTS004 零命中、SYSAD 零命中、僅 037 之 24 列明載 | 本包實測 `data/nrc_coverage.tsv`、`data/sysad_uds_tables.md` | 條文適用空白 | **RESOLVED**（R-DIAG5(amend)，Pei 2026-09-17）—— 226 列中 223 列已解（CFTS004 5／037 20／ISO 198），殘 3 列轉 DR-DIAG-1（非阻斷）|
| `[A-DIAG02]` | execution | `R-DIAG` 四字母前綴不被 `scripts/ruling_anchor.py` 之 `RE_ANCHOR`（`R-[A-Z]{0,3}\d+`）接受，九條無法進 `RULINGS.sha.tsv`，R-G52 引用制對本 feature 失效 | `rulings_hash.py --target` 回報 0 錨點 | 全域工具 | **RESOLVED**（R-G73，Pei 2026-09-17）—— 正則放寬為 `{0,4}`；回歸實測既有 788 id 之 sha8 零變動 |
| `[A-DIAG03]` | execution | SYSAD 無 UDS 位元組序列表與 NRC 表；唯一序列表為 DTC 流程，而 037 之 DTC 提及列 = 0 | `data/sysad_uds_tables.md` §2 | 來源缺件 | **PENDING** — 不阻斷；DR-DIAG-2 維持 |
| `[A-DIAG04]` | execution | 598／5210 之前例衝突：R-DIAG7(b) 引 R-CAM2(b)「一律 0」，而已交付之 SWC 0708 工作簿 285 列中 202 列填 `1` | SWC 0708 `Test Case Specification` T..Z 欄實測 | 前例衝突 | **RESOLVED**（R-G74，Pei 2026-09-17）—— R-CAM2(b) 升為全域，598／5210 一律 0；SWC 0708 依 R-G72 不回修 |
| `[A-DIAG05]` | execution | SWC 0708 自身欄位錯位：10 列之作者名 `PeiPYHsu` 落入 `T` 欄（HDCC27 Atl-Hi），車型七欄整體右移一格 | 同上 | 外部工作簿瑕疵 | **記錄** — 非本 feature 產物，不修；供 SWC 線參考 |
| `[A-DIAG06]` | analysis | 下放包 CDD-01 §4(b) 以合併列書寫 8 列實為 11 檔，「必投遞」數不可直接對帳（審閱 A1）| `down/20260917_CDD-01.md` §4(b) | 下放包形式 | **RESOLVED** — 後續下放包投遞表一檔一列 |
| `[A-DIAG07]` | analysis | 下放包 CDD-01 §5 稱 `-057` 歸 #11；實測歸 #10 `$1801`。分析層以標題「Audio Output Settings」推定，未查 L3（審閱 A2）| 同上 §5 | 未查即斷言 | **RESOLVED** — R-DIAG3(amend) 落字；framework.md Part II 記明 |
| `[A-DIAG08]` | analysis | 下放包 CDD-01 §5 只點名 `$5000` 跨母節；實為 6 個（審閱 A3）| 同上 §5 | 漏列 | **RESOLVED** — R-DIAG9(amend)(c) 落字 |
| `[A-DIAG09]` | analysis | 選定 `R-DIAG` 四字母前綴前未查 `ruling_anchor.py` 正則（審閱 A4）| 同上 §2 | 未查即命名 | **RESOLVED** — R-G73；前綴為全域命名空間，其可行性由全域工具定義 |
| `[A-DIAG10]` | analysis | 下放包 CDD-01 §7 斷言「無阻斷性 DR」，未先量測 NRC 值之來源覆蓋率（審閱 A5）| 同上 §7 | 違「先量測後斷言」| **RESOLVED** — 審閱撤回該句；CDD-01 §8.1 已更正為阻斷性 |
| `[A-DIAG11]` | analysis | 下放包以 V1 (2) 為母體發包；V1 (3) 已在同目錄（審閱 A6）| 同上 §1 | 非預見性 | **RESOLVED** — R-DIAG8(amend)；記事實，非責任 |
| `[A-DIAG12]` | analysis | R-DIAG9(c) 條文書「43 個」實為 42（`$5007` 未引用計入，審閱 A7）| `features/diagnostics/RULINGS.md` R-DIAG9 | 條文與實測不符 | **RESOLVED** — 條文不改（R-TM13），R-DIAG9(amend)(a) 記 42 |
| `[A-DIAG13]` | execution | `Toro_ATL_MI` 之 PROXI `Market_Area`（byte 160）Type 欄記為 `Not Used`，其餘五本為 `Table`；值 `2` 仍存在 | `forms/proxi/Toro_ATL_MI/…XLSM` `PROXI Write!F682` | 證據強度 | **記錄** — R-DIAG7(amend) 明文「不影響填法」|
| `[A-DIAG14]` | execution | 下放包 CDD-01_A T4 書 `$XXXX` 白名單「27 種」，該數為 CDD-01 3-5 之 037 token 種數；依其自身定義（`layer3_assign.tsv` 之 DID 集合）實測為 **36 種** | `down/20260917_CDD-01_A.md` §3 T4 | 數字引用錯置 | **RESOLVED** — 依定義實作 36 種，見上繳包 §4 |
| `[A-DIAG15]` | execution | `docs/fw036/RULINGS.sha.tsv` 表頭自稱「單一全域檔，重生一律掃描全部 canon 與各 feature」，實際只含 `features/security/RULINGS.md` 32 列；全 repo 重生為 837 錨點。`rulings_hash.py --check` 因而 FAIL —— **本包動工前即 FAIL**，非本包造成 | `docs/fw036/RULINGS.sha.tsv` | 全域檔過期 | **PENDING** — 非本 feature 所能決；全域待辦 |
| `[A-DIAG16]` | execution | CDD-01 上繳包 §2.2 之表標題書 `body sha8`，其值實為 `rulings_hash.py` 之 `sha8`（section_sha）欄；且 `R-DIAG9` 自算值 `802f0427` 與工具 `cc7b5200` 不符（手算未複製工具對章節尾界之處置）| `up/20260917_CDD-01.md` §2.2 | 自算代替工具 | **RESOLVED** — 本包以工具實跑取代自算，全表見上繳包 §3 |

## Assumption markers

None yet（本包未產 TC）。Inline format in generated JSON reasoning: `[ASSUMPTION A-DIAGnn]`.
