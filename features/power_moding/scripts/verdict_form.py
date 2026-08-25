#!/usr/bin/env python3
"""R-PMH91 —— 對照結論須以**四詞之一**作結（取代攔截式列舉）。

**取代 `wording_sample.py`**（其形態為攔截式列舉，攔「無矛盾」「非牴觸」二詞；
兩層抽樣之偽陰率 10% → **20%，未見收斂**，且漏網者「**非漏**」正是
`RESIDUE_VERDICT` 20 條中最常用之起首詞 —— 23 包 §7.2）。

**本檢查為正向**：驗每一對照結論**是否以四詞之一作結**，
**不驗其是否含某些禁用詞**。

  四詞：`牴觸`／`印證`／`未對照`（R-PMH79）＋ `待定義`（R-PMH85）
  另允 `—`：該項**本身即比對之一造**，不入判定（非結論）。

**母體非列舉** —— 其為各檢查之**判定表**（`VERDICT`／`RESIDUE_VERDICT`／
`ER_VERDICT`／`LINE_VERDICT` 等），**其每一項依構造即為一個對照結論**；
不必掃描散文去猜哪一行是結論。**R-PMH67 之抽樣義務於本檢查不適用**
（無列舉即無偽陰可估）。

用法:
    python scripts/verdict_form.py
    python scripts/verdict_form.py --must-hit
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

FOUR = ("牴觸", "印證", "未對照", "待定義")
NON_PARTY = "—"

# R-PMH92 —— 本檢查之 must-hit 註冊。**總表之結果欄由此決定，手寫不採認。**
HAS_MUST_HIT = True
MUST_HIT_NOTE = '`--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體）'

LIMITS = [
    "**只驗『以四詞之一作結』，不驗該詞是否判對** —— 一個判錯之「未對照」照樣通過",
    "母體為**判定表之項**；**散文中之對照結論不入母體** —— 上繳包正文若以他詞作結，本檢查看不見",
    "`—`（本身即一造）為允許值 —— **其濫用即可繞過本檢查**，本檢查不判其是否恰當",
    "**「作結」之位置本檢查取『起首』** —— 條文之措詞為「以四詞之一作結」，"
    "而本 repo 之判定表一律將記法置於首；**該解讀已具名，若條文原意為句末則本檢查取錯了位置**",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def collect() -> list[tuple[str, str, str]]:
    """回傳 [(來源, 鍵, 記法之字串)]。"""
    out = []
    import chapter_bidirectional as cb
    for k, v in cb.RESIDUE_VERDICT.items():
        out.append(("chapter_bidirectional.RESIDUE_VERDICT", k, v))
    import matrix_vs_chapter as mvc
    for k, v in mvc.VERDICT.items():
        out.append(("matrix_vs_chapter.VERDICT", str(k), v[0]))
    import batch_er_vs_matrix as bem
    # ⚠ 26 包：`ER_VERDICT` 之值由 (記法, 謂詞, 依據) 改為
    # **(類, 記法, 謂詞, 依據)**（R-PMH97 之二分）—— 記法自 `v[0]` 移至 `v[1]`。
    # **本檔於改造當輪即以 23 項全 FAIL 攔下該不同步**（26 包 §7）。
    for k, v in bem.ER_VERDICT.items():
        out.append(("batch_er_vs_matrix.ER_VERDICT", str(k), v[1]))
    import spec_assertion_scan as sas
    # 29 包（R-PMH107）：`ANIM_LINE_VERDICT` 為新資料，其納入為**既有檢查之適用**。
    for name in ("LINE_VERDICT", "AUDIO_LINE_VERDICT", "ANN_LINE_VERDICT",
                 "AFTER_LINE_VERDICT", "AUDIO_CELL_VERDICT", "ANIM_LINE_VERDICT"):
        for k, v in getattr(sas, name).items():
            out.append((f"spec_assertion_scan.{name}", str(k), v[0]))
    # R-PMH100（27 包）—— **矩陣側 174 格全部入母體**（× 四斷言），
    # 「落選」類別已消滅，故其判定與入選者同列於此。
    for a in sorted(sas.ASSERTION_DOMAIN):
        for key, kind, _pred, _why in sas.cell_verdicts(a):
            out.append((f"spec_assertion_scan.cell_verdicts[{a}]", key, kind))
    return out


def judge(text: str) -> str:
    if text.startswith(NON_PARTY):
        return NON_PARTY
    for w in FOUR:
        if text.startswith(w):
            return w
    return ""


def run(extra: list[tuple[str, str, str]] | None = None, quiet: bool = False) -> tuple[int, dict, list]:
    items = collect() + (extra or [])
    counts, bad = {}, []
    for src, key, text in items:
        w = judge(text)
        if not w:
            bad.append((src, key, text[:70]))
        else:
            counts[w] = counts.get(w, 0) + 1
    if not quiet:
        print(f"=== 對照結論之記法（R-PMH91）===")
        print(f"母體：各檢查之判定表，共 **{len(items)}** 項\n")
        for src in sorted({s for s, _, _ in items}):
            sub = [x for x in items if x[0] == src]
            c = {}
            for _, _, t in sub:
                c[judge(t) or "**未以四詞作結**"] = c.get(judge(t) or "**未以四詞作結**", 0) + 1
            print(f"  {src:<44} {len(sub):>3} 項  {c}")
        print(f"\n  合計：{counts}；**未以四詞之一作結 = {len(bad)}**")
        for src, key, text in bad:
            print(f"    **FAIL** {src} [{key}] :: {text}")
    return len(bad), counts, bad


def must_hit() -> int:
    """R-PMH92／24 包步驟 2 之三項錨點。"""
    print("=== R-PMH91 之 must-hit（24 包步驟 2）===\n")
    base, _, _ = run(quiet=True)
    print(f"  基線（現況）之 FAIL 數 = {base}")

    a = [("**測試替身**", "must-hit(a)", "非漏 —— 其散文於 SYS1 逐字存在")]
    n_a, _, bad_a = run(a, quiet=True)
    ok_a = n_a == base + 1 and any(k == "must-hit(a)" for _, k, _ in bad_a)
    print(f"\n  (a) 注入以「**非漏**」作結之對照結論 → FAIL 數 {base} → {n_a}；"
          f"其在 FAIL 清單內：{ok_a}")

    b = [("**測試替身**", "must-hit(b)", "未對照 —— 素材無對應列")]
    n_b, _, _ = run(b, quiet=True)
    ok_b = n_b == base
    print(f"  (b) 注入以「**未對照**」作結者 → FAIL 數 {base} → {n_b}；未被攔下：{ok_b}")

    # (c) 非對照結論之行**不進母體** —— 母體為判定表，散文行依構造即不在其中
    items = collect()
    ok_c = not any("write_back.test_group_value 與 test_group 一致" in t
                   for _, _, t in items)
    print(f"  (c) 非對照結論之散文行（如同值查核 `… 與 … 一致 : True`）"
          f"**不進母體**：{ok_c}")
    print("      —— 其成立之理由不是「被過濾掉」，是**母體為判定表而非散文**。")

    print("\n" + "=" * 66)
    print(f"(a) 非漏 → FAIL: {ok_a}；(b) 未對照 → PASS: {ok_b}；(c) 散文不進母體: {ok_c}")
    return 0 if (ok_a and ok_b and ok_c) else 1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--must-hit", action="store_true")
    a = ap.parse_args()
    if a.must_hit:
        rc = must_hit()
        print_limits()
        sys.exit(rc)
    n, _, _ = run()
    print_limits()
    sys.exit(1 if n else 0)


if __name__ == "__main__":
    main()
