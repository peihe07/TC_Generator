#!/usr/bin/env python3
"""R-PMH35 —— Layer 2 之 granularity 判準（G1–G5），含 must-hit 錨點之實跑。

門檻**寫死於程式**（R-PMH35(a)：「約等於」「過半」不構成門檻）：

  G1 過細 —— 組數相對 leaf 數      : 組數 / leaf 數 <= 1/3（平均組規模 >= 3）
  G2 過細 —— 最小組                : min(組規模) >= 2
  G3 過粗 —— 收容簇                : 組名不得命中收容簇清單（大小寫不敏感、全字）
  G4 過粗 —— 最大組佔比            : max(組規模) / leaf 數 <= 0.5
  G5 決策測試 —— 組規模之區間      : 全部組規模 ∈ [2, floor(leaf 數 / 2)]

**未經 must-hit 實跑者不得標 PASS**（R-PMH35(c)）—— 故 `--self-test`
為採用本判準之前提，非可選項。

用法：
    python scripts/check_granularity.py --feature .            # 現行提案
    python scripts/check_granularity.py --feature . --self-test
"""

# R-PMH92 —— 本檢查之 must-hit 註冊。**總表之結果欄由此決定，手寫不採認。**
HAS_MUST_HIT = True
MUST_HIT_NOTE = '`--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗'


import argparse
import csv
import hashlib
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# G3 之收容簇清單。全字比對、大小寫不敏感 —— `Other` 命中而
# `Power Off Behavior` 不命中（其含 `Off` 而非 `Other`，且比對單位為整詞）。
CATCH_ALL = {"misc", "general", "unclassified", "other", "雜項"}

# ---------------------------------------------------------------- 門檻
# **R-PMH40 —— 判準門檻之唯一來源即此處。**
# 文件中之門檻數值一律由 `--emit-thresholds` 產生後貼入，不得另行維護副本。
THRESHOLDS = {
    "G1": ("組數 / leaf", "<=", 1.0 / 3.0, "1/3",
           "canon §4.1.3 決策測試之平均意義：平均每組不足 3 個 leaf 時，"
           "過濾結果多為 1–2 列，索引價值與逐條列舉無異（R-PMH39）"),
    "G2": ("min(組規模)", ">=", 2, "2",
           "canon §4.1.3「不是一條」之單組下限 —— 至少兩個才成組"),
    "G3": ("組名命中收容簇清單之數", "==", 0, "0",
           f"收容簇清單 {sorted(CATCH_ALL)}；全字比對、大小寫不敏感"),
    "G4": ("max(組規模) / leaf", "<=", 0.5, "1/2",
           "canon §4.1.3「不是整本」—— 單組不得吃掉過半"),
    "G5": ("逸出 [2, floor(leaf/2)] 之組規模數", "==", 0, "0",
           "G2 之下限與 G4 之上限所夾之區間，逐組適用"),
}


# --- R-PMH52 之擴及（17 包步驟 4）---
# R-PMH52 之措詞為「**任何** lint 之輸出須具名其未涵蓋之範圍」，
# 而 16 包 §5.3 查出該條實際只施行於 `lint_batch.py` —— 單向套用。
# 本檢查自此於輸出末尾具名其限度。**內容須為本檢查之限度，
# 不得寫成一般性免責。**
LIMITS = [
    "G1–G5 五項**只看組數與組員數之分布**；**不看任何組之內容** —— 一組 3 個 leaf 是否真屬同一能力，本檢查不判",
    "Layer 2 之**組名**（字面、大小寫、是否與 Test Group 重複）不看 —— 該屬 R-PMH13／R-PMH36／canon §4.2",
    "**分母 `n_leaf` 為外部給定**（現行 **46** —— R-PMH72 排除 `-028`、**R-PMH117 排除 `-002`**）；其是否正確不由本檢查驗",
    "leaf 到組之**指派**不看 —— 只要分布合格，指派錯誤仍全綠",
    "`--check-doc-sync` 只驗門檻表與程式同源；**不驗該門檻本身是否恰當**",
    "**R-PMH68 之殘餘盲區**：doc-sync 之錨為**門檻表輸出**之 SHA256，守的是**值**而非**產生該值之邏輯** —— 改 `evaluate()` 之計算方式而門檻值不變者，本檢查不會察覺",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for _x in LIMITS:
        print(f"  - {_x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def self_sha256() -> str:
    """本程式檔之 SHA256。

    **R-PMH68（18 包）起不再作為 doc-sync 之錨** —— 以整支程式為錨者，
    任何編輯（含純註解、含與門檻無關之常數）皆使文件失效而門檻一字未動；
    該誤報會訓練出「重跑 emit 再貼上」之反射，**而該反射正是使本檢查
    失效之途徑**（17 包 §12 第 5 項）。保留本函式供追溯。
    """
    return hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()


def thresholds_sha256() -> str:
    """**門檻表本身**之 SHA256 —— R-PMH68 之錨。

    取 `emit_thresholds()` 之輸出（門檻表之正規形式）為錨，
    故加註解、加 `LIMITS` 等與門檻無關之編輯**不再使文件失效**。

    **殘餘盲區（已寫入 `LIMITS`）**：本錨守的是**值**，
    不是**產生該值之邏輯** —— 改計算方式而值不變者，本檢查不會察覺。
    """
    return hashlib.sha256(emit_thresholds().encode("utf-8")).hexdigest()


DOC = ROOT / "framework.md"
DOC_SHA_RE = re.compile(r"門檻表 SHA256：`([0-9a-f]{64})`")


TBL_RE = re.compile(r"(\| id \| 量 \| 關係 \| 門檻 \| 來源 \|\n(?:\|[^\n]*\|\n)+)")


def _norm_tbl(s: str) -> list[str]:
    """表格之正規化：去行首尾空白、摺疊 cell 內之對齊空白。"""
    out = []
    for line in s.strip().splitlines():
        cells = [re.sub(r"\s+", " ", c).strip() for c in line.strip().strip("|").split("|")]
        out.append("|".join(cells))
    return out


def check_doc_sync(doc: Path = None, prog_sha: str = None,
                   doc_text: str = None) -> tuple[bool, str]:
    """R-PMH42 —— 門檻單一來源之**可執行檢查**。

    **11 包步驟 4 之強化**：原僅比對程式 SHA256，而**雜湊是代理量** ——
    手改文件中之門檻數值而不動雜湊行，檢查會 PASS。
    現改為**兩項並驗**：
      (1) 程式 SHA256 之記載與程式現值相符（命中須恰 1 —— R-PMH41）；
      (2) **文件之門檻表與 `emit_thresholds()` 之輸出正規化後逐字相同**。

    `prog_sha` / `doc_text` 僅供自測注入。
    """
    doc = doc or DOC
    cur = prog_sha or thresholds_sha256()
    if doc_text is None:
        if not doc.exists():
            return False, f"文件不存在：{doc}"
        doc_text = doc.read_text(encoding="utf-8")

    hits = DOC_SHA_RE.findall(doc_text)
    if len(hits) != 1:
        return False, (f"文件中之 `門檻表 SHA256：` 記載數 = {len(hits)}（預期恰 1）"
                       f" —— R-PMH41：驗命中數")
    if hits[0] != cur:
        return False, (f"**門檻表已與程式分岔（雜湊）** —— 文件記 `{hits[0][:16]}…`，"
                       f"門檻表現值 `{cur[:16]}…`。"
                       f"請重跑 `--emit-thresholds` 並重貼門檻節。")

    tbls = TBL_RE.findall(doc_text)
    if len(tbls) != 1:
        return False, (f"文件中之門檻表數 = {len(tbls)}（預期恰 1）—— R-PMH41")
    want, got = _norm_tbl(emit_thresholds()), _norm_tbl(tbls[0])
    if want != got:
        diff = next((f"L{i+1}: 文件 {g!r} vs 程式 {w!r}"
                     for i, (w, g) in enumerate(zip(want, got)) if w != g),
                    f"行數 文件 {len(got)} vs 程式 {len(want)}")
        return False, (f"**門檻表之內容已與程式分岔** —— {diff}。"
                       f"（雜湊相符但表被手改 —— 雜湊是代理量，故此項另驗）")
    return True, (f"文件與程式同源 —— 門檻表 SHA256 `{cur[:16]}…`（命中 1 處）"
                  f"＋ 門檻表 {len(got)} 列逐字相同")


def emit_thresholds() -> str:
    """R-PMH40 —— 門檻表之機器產出，供文件貼入。"""
    L = ["| id | 量 | 關係 | 門檻 | 來源 |", "|---|---|:--:|---|---|"]
    for k, (q, op, _v, disp, why) in THRESHOLDS.items():
        L.append(f"| **{k}** | {q} | `{op}` | **`{disp}`** | {why} |")
    return "\n".join(L)

# 06 §5.2 之逐 leaf 分配。Test Set #2 之名依 **R-PMH36**（Pei 2026-08-24 裁
# 「甲」）為 `Disclaimer Screen` —— Layer 2 已定版 8 組。
PROPOSAL = {
    "Splash Screen": ["001-01", "001-02", "011"],
    "Disclaimer Screen": ["001-03", "001-04", "001-05", "003", "004", "005", "022-02"],
    "Startup Animation": ["006-01", "006-02", "006-03", "007", "008-01", "008-02",
                          "009-01", "009-02", "010"],
    "Startup Sounds": ["012", "013", "014", "015", "016", "017"],
    # R-PMH117（Pei 2026-08-25「核可」）：`002`（7.1.1，`SU1.1)`）判 out of scope、
    # 不寫入交付工作簿，比照 R-PMH72 對 `028` 之處置（canon §8.4.2 三項判準同型）。
    # 其列保留於 `layer3_sections.tsv` 與 `outline_map.json`
    # （標 `EXCLUDED-BY-R-PMH117`）作為內部台帳。
    # **有 TC 之 leaf 因而由 47 降為 46**，granularity 之分母隨之改變。
    # ⚠ `023` **留在本組** —— 其為「停手待 DR-PMH5」（R-PMH111），
    # **非 out of scope**；二者不同，不得合併處置。
    "Power Transitions": ["018-01", "018-02", "018-03", "018-04", "018-05",
                          "023"],
    "Power Off Behavior": ["019", "020", "021", "022-01", "024-01", "024-02",
                           "024-03", "025"],
    "Voice Assistant Key": ["026-01", "026-02", "026-03", "026-04", "026-05"],
    # R-PMH72（Pei 2026-08-24「DR-PMH1 拿掉」）：`028` 不寫入交付工作簿、
    # 不產出 TC，故**不入 Layer 2 之分組**。其列保留於 `layer3_sections.tsv`
    # 與 `outline_map.json`（標 `EXCLUDED-BY-R-PMH72`）作為內部台帳。
    # **有 TC 之 leaf 因而由 48 降為 47**，granularity 之分母隨之改變。
    "Off Road Plus": ["027", "029"],
}

# 有 TC 之 leaf 數 —— granularity 之分母（R-PMH72 ＋ **R-PMH117**）
N_LEAF = 46


def evaluate(groups: dict[str, list], n_leaf: int) -> dict[str, tuple[bool, str]]:
    """回傳 {判準 id: (是否 PASS, 實測值之說明)}。"""
    sizes = [len(v) for v in groups.values()]
    n_grp = len(groups)
    hi = math.floor(n_leaf / 2)
    r1 = n_grp / n_leaf
    r4 = max(sizes) / n_leaf
    hits = sorted(n for n in groups
                  if any(w == t for t in n.lower().replace("/", " ").split()
                         for w in CATCH_ALL))
    out_of_band = sorted(s for s in sizes if not (2 <= s <= hi))
    t1, t2, t4 = THRESHOLDS["G1"][2], THRESHOLDS["G2"][2], THRESHOLDS["G4"][2]
    return {
        "G1": (r1 <= t1, f"組數/leaf = {n_grp}/{n_leaf} = {r1:.4f} "
                         f"(門檻 <= {THRESHOLDS['G1'][3]} = {t1:.4f})"),
        "G2": (min(sizes) >= t2, f"min(組規模) = {min(sizes)} (門檻 >= {t2})"),
        "G3": (not hits, f"收容簇命中 = {hits or '無'} (門檻 = 零命中)"),
        "G4": (r4 <= t4, f"max/leaf = {max(sizes)}/{n_leaf} = {r4:.4f} "
                         f"(門檻 <= {THRESHOLDS['G4'][3]} = {t4})"),
        "G5": (not out_of_band,
               f"逸出 [2, {hi}] 之組規模 = {out_of_band or '無'} "
               f"(實測區間 [{min(sizes)}, {max(sizes)}])"),
    }


def structural_collateral(groups: dict, n_leaf: int) -> dict[str, str]:
    """R-PMH38 —— 以**算式**判定哪些連帶 FAIL 為結構性，不以文字論述代替。

    鴿籠：n 個 leaf 分 k 組，若每組規模 >= 2 則須 n >= 2k。
    故 k > floor(n/2) 時**必有**單 leaf 組 —— G2 必然 FAIL，
    且該單 leaf 組必逸出 [2, floor(n/2)] —— G5 亦必然 FAIL。
    """
    k, hi = len(groups), math.floor(n_leaf / 2)
    out = {}
    if k > hi:
        why = (f"鴿籠：k={k} > floor(n/2)={hi} ⇒ 每組規模 >= 2 須 n >= 2k = {2*k} "
               f"> n = {n_leaf}，故必有單 leaf 組")
        out["G2"] = why
        out["G5"] = why + "；該單 leaf 組必逸出 [2, %d]" % hi
    return out


def report(title: str, groups: dict, n_leaf: int, expect_fail: set = frozenset(),
           collateral: str = "") -> bool:
    """回傳「指定判準是否全部如期 FAIL」（錨點）或「是否全 PASS」（範圍向）。

    **連帶 FAIL 不使錨點失敗** —— must-hit 之職責是證明「該判準會 FAIL」，
    其他判準一併 FAIL 不否定此事。惟連帶須具名，因其影響**隔離度**：
    一個同時觸發三個判準之錨點，不足以單獨證明其中任一個有效。
    """
    res = evaluate(groups, n_leaf)
    struct = structural_collateral(groups, n_leaf)
    print(f"\n--- {title} ---")
    ok = True
    coll = []
    for k in ("G1", "G2", "G3", "G4", "G5"):
        p, why = res[k]
        mark = "PASS" if p else "**FAIL**"
        want = ""
        if expect_fail:
            if k in expect_fail:
                want = "  ← 指定 FAIL " + ("✅" if not p else "❌ **未 FAIL**")
                ok &= not p
            elif not p:
                if k in struct:
                    want = "  ← **結構性連帶**（算式可推）"
                else:
                    want = "  ← 連帶 FAIL（未隔離）"
                coll.append(k)
        print(f"    {k} {mark:9s} {why}{want}")
    if expect_fail:
        if not coll:
            print("    隔離度：**隔離**（僅指定判準 FAIL）")
        elif all(k in struct for k in coll):
            print(f"    隔離度：**結構性連帶** {coll}")
            for k in coll:
                print(f"        {k} 之算式：{struct[k]}")
        else:
            bad = [k for k in coll if k not in struct]
            print(f"    隔離度：**未隔離** —— {bad} 無算式可推 ❌")
            ok = False
    else:
        ok = all(p for p, _ in res.values())
    return ok


def self_test() -> int:
    n = N_LEAF
    print("=== R-PMH35(c) —— must-hit 錨點之實跑（五個，各須 FAIL 其指定判準）===")
    anchors = []

    # A1：每個 outline 各成一組（29 組）
    rows = [r for r in csv.DictReader((ROOT / "data" / "layer3_sections.tsv")
                                      .open(encoding="utf-8"), delimiter="\t")
            if not r.get("excluded_by")]          # R-PMH72 —— `-028` 不入分母
    by_outline: dict[str, list] = {}
    for r in rows:
        by_outline.setdefault(r["outline_number"], []).append(r["swe_requirement_id"])
    anchors.append(("A1 每個 outline 各成一組", by_outline, {"G1"},
                    f"**構造本質使然**：{len(by_outline)} 個 outline 分 {n} leaf，"
                    "必有單 leaf 組，"
                    "故 G2／G5 必然一併 FAIL —— 無法隔離"))

    # A2：每個 leaf 各成一組（46 組，R-PMH117 之後）
    anchors.append(("A2 每個 leaf 各成一組",
                    {r["swe_requirement_id"]: [r["swe_requirement_id"]] for r in rows},
                    {"G1", "G2"},
                    "**構造本質使然**：全部組規模為 1，G5 必然一併 FAIL —— 無法隔離"))

    # A3：`Off Road Plus` 拆為單 leaf 組（其現為 2 leaf，故得 9 組）
    g3 = {k: v for k, v in PROPOSAL.items() if k != "Off Road Plus"}
    for x in PROPOSAL["Off Road Plus"]:
        g3[f"Off Road Plus {x}"] = [x]
    anchors.append(("A3 Off Road Plus 拆為三個單 leaf 組", g3, {"G2", "G5"},
                    ""))

    # A4：新增一組名為 `Misc`（自 Startup Animation 移一個 leaf 過去，維持 48）
    # A4 之 `Misc` 取 **2** 個 leaf（非 1）—— 取 1 會連帶觸發 G2／G5，
    # 使本錨點無法單獨證明 G3。取 2 即隔離。
    g4 = {k: list(v) for k, v in PROPOSAL.items()}
    g4["Misc"] = [g4["Startup Animation"].pop(), g4["Startup Animation"].pop()]
    anchors.append(("A4 新增一組名為 Misc（2 leaf，以隔離 G3）", g4, {"G3"}, ""))

    # A5：八組併為一組
    anchors.append(("A5 八組併為一組",
                    {"All": [x for v in PROPOSAL.values() for x in v]}, {"G4", "G5"}, ""))

    # A6（R-PMH39）：G1 之**隔離**錨點 —— **46 leaf 分 16 組（14×3 + 2×2）**。
    # G2 min=2 ✅／G4 max=3/46 ✅／G5 全落 [2,23] ✅／G3 組名無收容簇 ✅，
    # 僅 G1 = 16/46 = 0.3478 > 1/3 FAIL。此組態即 R-PMH39 所述
    # 「G2/G4/G5 全通過而仍過細」者，證明 G1 不可省。
    #
    # **分母由 47 改 46 後本錨點已重算（R-PMH117）** ——
    # 原式 `15×3 + 1×2` 於 46 會得 `15×3 + 1×1`，**其 min=1 使 G2／G5 一併 FAIL，
    # 隔離即失效**（本錨點須只 FAIL G1）。故改為 `14×3 + 2×2 = 46`。
    # **此即「不得沿用舊組態」之實例** —— 舊式在新分母下仍會跑，只是不再隔離。
    leaves = [x for v in PROPOSAL.values() for x in v]
    assert len(leaves) == n, (len(leaves), n)
    g6, i = {}, 0
    for j in range(14):
        g6[f"Set{j+1:02d}"] = leaves[i:i+3]; i += 3
    g6["Set15"] = leaves[i:i+2]; i += 2
    g6["Set16"] = leaves[i:]
    assert sum(len(v) for v in g6.values()) == n and len(g6) == 16, (g6, n)
    assert min(len(v) for v in g6.values()) == 2, "隔離失效：出現單 leaf 組"
    anchors.append((f"A6 {n} leaf 分 16 組（14×3 + 2×2）—— G1 之隔離錨點",
                    g6, {"G1"}, ""))

    all_ok = True
    for title, groups, exp, coll in anchors:
        all_ok &= report(f"{title}（{len(groups)} 組）", groups, n, exp, coll)

    print("\n=== 範圍向（R-G9）—— 現行 8 組須 G1–G5 全 PASS ===")
    scope_ok = report("現行提案（8 組）", PROPOSAL, n)
    print(f"    範圍向 {'PASS ✅' if scope_ok else 'FAIL ❌'}")

    print("\n=== Q11 三案之試算（R-PMH35 末段 / R-PMH14 鑑別力）===")
    cases = {"（甲）Disclaimer Screen ← **R-PMH36 已採**": "Disclaimer Screen",
             "（乙）Acceptance Screen": "Acceptance Screen"}
    verdicts = {}
    for label, name in cases.items():
        g = {(name if k == "Disclaimer Screen" else k): v for k, v in PROPOSAL.items()}
        verdicts[label] = report(f"{label}（{len(g)} 組）", g, n)
    g_bing = {k: list(v) for k, v in PROPOSAL.items() if k != "Disclaimer Screen"}
    g_bing["Splash Screen"] = g_bing["Splash Screen"] + PROPOSAL["Disclaimer Screen"]
    verdicts["（丙）併入 Splash Screen"] = report(
        f"（丙）併入 Splash Screen（{len(g_bing)} 組）", g_bing, n)

    print("\n" + "=" * 72)
    if len(set(verdicts.values())) == 1:
        print("本判準對 Q11 之三案無鑑別力 —— 三案於 G1–G5 之結果完全相同"
              f"（皆 {'PASS' if all(verdicts.values()) else 'FAIL'}），"
              "依 R-PMH14 不得被引為支持任一案之理由。")
    else:
        print("本判準對 Q11 有鑑別力：" + str(verdicts))
    print("=" * 72)

    print("\n=== R-PMH42 —— doc-sync 檢查之故意失敗與還原 ===")
    real = self_sha256()
    fake = "0" * 64
    bad_ok, bad_why = check_doc_sync(prog_sha=fake)
    print(f"\n  [故意失敗] 注入假雜湊（模擬程式已改而文件未重貼）")
    print(f"    doc-sync {'PASS ❌ **未攔下**' if bad_ok else '**FAIL** 攔下 ✅'} — {bad_why}")
    good_ok, good_why = check_doc_sync()
    print(f"\n  [還原] 用程式實際雜湊")
    print(f"    doc-sync {'PASS ✅' if good_ok else '**FAIL** ❌'} — {good_why}")

    # 11 包步驟 4：第二項故意失敗 —— 雜湊相符而**表被手改**
    tampered = DOC.read_text(encoding="utf-8").replace("**`1/3`**", "**`0.35`**", 1)
    tam_ok, tam_why = check_doc_sync(doc_text=tampered)
    print(f"\n  [故意失敗 2] 手改文件之門檻值 `1/3` → `0.35`（雜湊行不動）")
    print(f"    doc-sync {'PASS ❌ **未攔下**' if tam_ok else '**FAIL** 攔下 ✅'} — {tam_why}")

    sync_ok = (not bad_ok) and good_ok and (not tam_ok)

    print(f"\nmust-hit 五錨點全部如期 FAIL: {all_ok}；範圍向 PASS: {scope_ok}；"
          f"doc-sync 故意失敗被攔下且還原後 PASS: {sync_ok}")
    return 0 if (all_ok and scope_ok and sync_ok) else 1


def doc_sync_must_hit() -> int:
    """R-PMH68 之兩項故意失敗（18 包步驟 5）。

    (a) **改門檻值而不重貼文件 → 須 FAIL**（真報仍在）
    (b) **加一行純註解 → 須 PASS**（誤報已消除）

    (b) 以**實際複本＋子行程**為之：把本檔複製為 `scripts/_docsync_probe.py`
    並在其中加一行純註解，跑其 `--check-doc-sync`。複本置於 `scripts/` 下，
    使其 `ROOT` 與本檔相同。跑畢即刪。
    """
    import shutil
    import subprocess
    ok_a = ok_b = False

    print("=== R-PMH68 must-hit (a) —— 改門檻值而不重貼文件 → 須 FAIL ===")
    saved = THRESHOLDS["G2"]
    THRESHOLDS["G2"] = (saved[0], saved[1], 3, "3", saved[4])
    try:
        ok, why = check_doc_sync()
        ok_a = not ok
        print(f"  改 G2 之門檻為 3 後：{'**FAIL**' if not ok else 'PASS'} — {why[:150]}")
    finally:
        THRESHOLDS["G2"] = saved
    print(f"  攔下：{ok_a}")

    print("\n=== R-PMH68 must-hit (b) —— 加一行純註解 → 須 PASS ===")
    src = Path(__file__).resolve()
    probe = src.parent / "_docsync_probe.py"
    try:
        text = src.read_text(encoding="utf-8")
        text = text.replace('"""', '"""\n# 純註解 —— R-PMH68 must-hit (b) 之測試替身\n', 1)
        probe.write_text(text, encoding="utf-8")
        r = subprocess.run([sys.executable, str(probe), "--check-doc-sync"],
                           capture_output=True, text=True)
        ok_b = r.returncode == 0
        print(f"  複本之 SHA256 與本檔不同："
              f"{hashlib.sha256(probe.read_bytes()).hexdigest() != self_sha256()}")
        print(f"  複本之 --check-doc-sync 退出碼 = {r.returncode}"
              f"（0 = PASS）：{ok_b}")
        print(f"  {r.stdout.splitlines()[0] if r.stdout else r.stderr[:120]}")
    finally:
        probe.unlink(missing_ok=True)
    print(f"  誤報已消除：{ok_b}")

    print("\n" + "=" * 66)
    print(f"(a) 改門檻值 → FAIL: {ok_a}；(b) 加純註解 → PASS: {ok_b}")
    print("**若改用舊錨（整支程式之 SHA256），(b) 必然 FAIL** —— "
          "\n  該誤報即 17 §12 第 5 項所述之「訓練出重貼反射」之來源。")
    return 0 if (ok_a and ok_b) else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--feature", default=".")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--emit-thresholds", action="store_true",
                    help="R-PMH40 —— 輸出門檻表（Markdown），供文件貼入")
    ap.add_argument("--check-doc-sync", action="store_true",
                    help="R-PMH42／R-PMH68 —— 驗 framework.md 之門檻節與門檻表同源")
    ap.add_argument("--doc-sync-must-hit", action="store_true",
                    help="R-PMH68 —— 兩項故意失敗（改門檻值 FAIL／加註解 PASS）")
    args = ap.parse_args()
    if args.emit_thresholds:
        print(emit_thresholds())
        print(f"\n> 門檻表 SHA256：`{thresholds_sha256()}`")
        print("> 重新產生：`python scripts/check_granularity.py --emit-thresholds`")
        sys.exit(0)
    if args.doc_sync_must_hit:
        rc = doc_sync_must_hit()
        print_limits()
        sys.exit(rc)
    if args.check_doc_sync:
        ok, why = check_doc_sync()
        print(f"doc-sync {'PASS' if ok else '**FAIL**'} — {why}")
        print_limits()
        sys.exit(0 if ok else 1)
    if args.self_test:
        rc = self_test()
        print_limits()
        sys.exit(rc)
    ok = report("現行提案（8 組）", PROPOSAL, N_LEAF)
    print(f"\n結果：{'PASS' if ok else 'FAIL'}")
    print("⚠ 依 R-PMH35(c)，未跑 --self-test 者不得將本結果標為 PASS。")
    print_limits()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
