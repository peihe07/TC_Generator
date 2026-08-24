#!/usr/bin/env python3
"""R-PMH51 之未套用側 —— 指定章之**雙向**逐句複驗（17 包步驟 3）。

R-PMH51 明文：A-PMH03 之其餘三則（8、9.1、11.1）須以雙向法複驗，
**未複驗前其標題結論不得引用**。11.1 已於 13 包方向二覆蓋、9.1 查出新漏 2，
**而 outline `8` 至今未做** —— 本檔補之，並使其可對任一章重跑。

方向一：SYS1 之每一句是否出現於 PDF（01 包已對全簿做過）
方向二：**PDF 之每一句是否出現於 SYS1** —— 漏句只在此方向顯示

用法:
    python scripts/chapter_bidirectional.py 8
"""
import argparse
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
PDF_TXT = ROOT / "sandbox" / "spec.txt"
SYS1 = ROOT / "inputs" / "SYS1_HMI_Power_Moding_HMI_Logic_and_Flow_R1_SR24_2A.xlsx"

# 各章於 PDF 全文之**起錨**（逐字取自 PDF，非推算）。
# 章之範圍 = [本章起錨, **下一章起錨**) —— 訖錨不另指定，
# 使相鄰兩章之邊界**必然共用同一個字串**，區間**不可能重疊或留縫**
# （17 §12 第 1 項：「錨之外的第 7 個 marker」之藏身處，由 `partition()` 逐段列出）。
STARTS = {
    7:  "7 Startup Notes:",
    8:  "R1Low Only",
    9:  "8 Power Moding Please refer to Power Moding State Matrix",
    10: "9 Power Moding Additional Power Moding Behavior Notes:",
    11: "VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS:",
    12: "10 Power Moding - Off Road+",
}

# --- R-PMH66(c)：殘餘之逐句人讀結論。**每一殘餘句皆須在此具名** ---
# 「逐字未命中」者一律進殘餘；**殘餘不得由門檻自動判為「非漏」** ——
# 門檻只決定人讀之優先順序，不決定結論。未具名之殘餘句 → **FAIL**。
# 鍵為該句之前 60 字元（正規化後）。
RESIDUE_VERDICT: dict[str, str] = {
    "Charge Now - XEV key off-Pop-ups Charge Now/Summary; Precond":
        "非漏 —— 其散文 `3. XEV key off-Pop-ups Charge Now/Summary; Preconditioning.` 於 SYS1 9.1 逐字存在；句首之 `Charge Now -` 為前一條列項之尾，屬 `-layout` 之切分",
    "Fully functional for 60 seconds up to 2.5 minutes to display":
        "**部分漏 —— A-PMH16(1)**：`Fully functional` 為矩陣格（漏，屬新漏 2）；散文側 PDF 作 `should 'stay awake' for 60 seconds up to 2.5 minutes`，**SYS1 作 `should 'stay awake up to 2.5 minutes`** —— `' for 60 seconds` 整段缺失",
    "HVAC Knobs: HVAC Knobs: Maximum time the radio can 'stay awa":
        "非漏（散文側）—— `Maximum time the radio can 'stay awake' because of these popups is 10 minutes.` 於 SYS1 逐字存在；`HVAC Knobs:`／`KEY OFF OFF OFF` 為矩陣格，屬新漏 2",
    "OFF Forced OFF Headunit: If user chooses to dismiss Wi-Fi co":
        "非漏（散文側）—— `If user chooses to dismiss Wi-Fi configuration popup, display Charge Now (if applicable).` 於 SYS1 逐字存在；其餘為矩陣格，屬新漏 2",
    "FOTA update available - OFF Full on, some limited functional":
        "非漏（散文側）—— FOTA 條列三句於 SYS1 9.1 逐字存在；`OFF`／`Full on, some limited functionality`／`ICS Hard Controls:` 為矩陣格，屬新漏 2",
    "(No ACC Climate GUI: Climate GUI: position) OFF Forced OFF T":
        "非漏（散文側）—— `The priority of the popups which occur at IGN OFF are as follows:` 於 SYS1 逐字存在；`(No ACC position)`／`Climate GUI:`／`Forced OFF` 為矩陣格，屬新漏 2",
    "[CR22412] OFF be functional (See CTS009) (DCR19385) Full on,":
        "非漏（散文側）—— `If the user interacts with the FOTA [CR22412] popup the radio shall 'stay awake' until the user has not interacted with the popup for 60 seconds.` 於 SYS1 逐字存在；`VR HK to activate SIRI…(See CTS009)` 等為矩陣格，屬新漏 2",
    "FOTA via Wi-Fi configuration - OFF OFF position If user choo":
        "非漏（散文側）—— `2. FOTA via Wi-Fi configuration` 之兩句於 SYS1 逐字存在；矩陣格屬新漏 2",
    "Fully functional ENGINE ON Climate GUI: Climate GUI: Not Vis":
        "**部分漏** —— `PM1) In the event that there are popups to show at IGN OFF but the user has set Power Accessory Delay to 0 seconds, the head unit should 'stay awake` 之散文於 SYS1 存在（惟見 A-PMH16(1)）；`KEY ON ENGINE ON`／`ENGINE OFF`／`Climate GUI:`／`Headunit:`／`ICS Hard Controls:`／`Fully functional`／`Not Visibile due to power off` 全為矩陣格 —— **漏，屬新漏 2**",
    "Shut the radio down if user dismisses Charge Now XEV key off":
        "非漏（散文側）—— SYS1 作 `Shut the radio down if user dismisses XEV key off Pop-ups.`，逐字存在；句中之 `Charge Now` 為前一條列項之尾，屬切分",
    "If the user does not (ACC or Climate GUI: Climate GUI: RUN) ":
        "**部分漏 —— A-PMH16(2)(3)(4)**：PDF 作 `within 60 seconds the timeout defined in pop-up list, the radio should shut Off the popup should close aofnd if no other popups…`；**SYS1 作 `within 60 the timeout defined in pop-up list, the popup should close if no other popups…`** —— 缺 `seconds`、缺 `the radio should shut Off the`、`aofnd` 被逕改為 `if`。其餘 `(ACC or RUN)`／`Climate GUI:` 為矩陣格，屬新漏 2",
    "8 Power Moding Please refer to Power Moding State Matrix for":
        "**漏 —— 屬新漏 2 之範圍，惟 A-PMH14 未具名此句**：`Please refer to Power Moding State Matrix for further specifications.` 為章 9 之首句（指標句），SYS1 全 52 則探針 `Please refer to Power Moding State Matrix` 命中 **0**。與新漏 3（p10 之 `POWER MODING STATE MATRIX:` 段）同一形態、不同位置",
    "HEADUNIT POWER HEADUNIT POWER OFF ON ICS Hard Controls : ICS":
        "**漏 —— 新漏 2**：狀態矩陣之表頭（`HEADUNIT POWER OFF`／`ON` × `ICS Hard Controls`／`HVAC Knobs`）。探針 `HEADUNIT POWER`／`ICS Hard Controls`／`HVAC Knobs` 於 SYS1 全簿命中皆 0",
    "KEY OFF accessory delay expires Only headunit-related contro":
        "**漏 —— 新漏 2**：矩陣之 `KEY OFF (ACC)` 列（`accessory delay expires`／`Only headunit-related controls functional`）",
    "OFF OFF after power accessory delay expires 3.":
        "**漏 —— 新漏 2**：矩陣之 `KEY OFF (No ACC)` 列（`after power accessory delay expires`）；句末之 `3.` 為條列編號被切分所併入",
    "VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS: VRLP1: VR ":
        "非漏 —— SYS1 之 outline `11` 逐字為 `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS`（無尾冒號），`11.1` 逐字為 `VRLP1: VR hard key to…`。逐字未命中之因為 PDF 之節標題帶尾冒號、且切分於 `(eg.` 處斷開",
    "Radio status after interaction with SIRI depends on outcome ":
        "非漏 —— 切分假象：句切於 `(i.e.` 處；其全句於 SYS1 11.1 逐字存在",
    "radio back to off), Screen ON and Audio OFF, Screen Off, and":
        "非漏 —— **條列再流**（A-PMH03 原記之形態，A-PMH14 已以方向二確認）：SYS1 11.1 作 `- Screen Off and Audio OFF (i.e. radio back to off), - Screen ON and Audio OFF, …`，僅條列符號不同，四個 outcome 全在",
    "(DCR19385) POWER MODING STATE MATRIX: Power Moding behavior ":
        "**漏 —— A-PMH14 新漏 3（既有，非新）**：`POWER MODING STATE MATRIX:` 段於 SYS1 全簿命中 0。句首之 `(DCR19385)` 屬前一句（VRLP1）之尾，SYS1 11.1 有之",
    "If this document is not available, please request a copy fro":
        "**漏 —— A-PMH14 新漏 3 之第二句（既有，非新）**",
}
MIN_SENT = 25          # 最短比對單位（字元），比照 13 包
GRAM = 6               # 6-gram 覆蓋率，比照 13 包
GRAM_THRESHOLD = 0.30  # < 30% 者為真漏候選


# --- R-PMH52 之擴及（17 包步驟 4）---
# 本檢查於輸出末尾具名其限度。
sys.path.insert(0, str(Path(__file__).resolve().parent))

LIMITS = [
    "**`STARTS` 之起錨為人工指定** —— 錨取錯則整章之範圍隨之錯；`--partition` 只能查未覆蓋段，查不出「錨落在章內某處」之情形",
    "只比對 PDF **文字層**；**圖表不看** —— p9 之狀態矩陣即以圖呈現（A-PMH14 新漏 2）",
    "比對單位為句（>= 25 字元）；**短於 25 字元之句一律不入母體**，章 8 之標題 `Starup R1Low Only` 即屬之",
    "6-gram 覆蓋率**不再參與判定**（R-PMH66）—— 只決定殘餘人讀之優先順序；其門檻值本身未經重驗，故亦不再被倚賴",
    "`RESIDUE_VERDICT` 之人讀結論**由人寫入，本檢查不驗其正確性** —— 只驗其存在",
    "**只驗字之有無，不驗語意** —— 同義改寫會被判為漏句，改寫錯誤會被判為命中",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for _x in LIMITS:
        print(f"  - {_x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


def norm(t: str) -> str:
    t = str(t).replace("_x000D_", " ")
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'),
                 ("”", '"'), ("…", "..."), ("–", "-"),
                 ("—", "-")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def sentences(t: str) -> list[str]:
    """句號後空白切分，保留 >= MIN_SENT 者（比照 13 包之比對單位）。"""
    return [s.strip() for s in re.split(r"(?<=\.)\s+", t)
            if len(s.strip()) >= MIN_SENT]


def grams(t: str) -> set[str]:
    w = re.findall(r"[a-z0-9]+", t.lower())
    return {" ".join(w[i:i + GRAM]) for i in range(max(0, len(w) - GRAM + 1))}


def coverage(s: str, hay: str) -> float:
    g = grams(s)
    return len(g & grams(hay)) / len(g) if g else 1.0


def bounds(pdf: str) -> list[tuple[int, int, int]]:
    """回傳 [(章, 起, 訖)]，訖 = 下一章之起；末章訖 = 全文末。

    起錨於全文中之命中數須恰 1（R-PMH41 —— 驗命中數）；不為 1 即 raise。
    """
    pos = []
    for ch, a in STARTS.items():
        n = pdf.count(a)
        if n != 1:
            raise SystemExit(f"章 {ch} 之起錨 `{a}` 命中 {n} 次（須恰 1）—— R-PMH41")
        pos.append((pdf.index(a), ch))
    pos.sort()
    out = []
    for k, (i, ch) in enumerate(pos):
        j = pos[k + 1][0] if k + 1 < len(pos) else len(pdf)
        out.append((ch, i, j))
    return out


def pdf_chapter(ch: int, pdf: str) -> str:
    for c, i, j in bounds(pdf):
        if c == ch:
            return pdf[i:j].strip()
    raise SystemExit(f"章 {ch} 未建錨")


def partition(pdf: str) -> int:
    """17 §12 第 1 項 —— 章區間之覆蓋／重疊檢查。

    區間由「下一章之起」界定，**重疊與縫隙在構造上即不可能**；
    真正待查者為**首章之前**與**末章之後**之未覆蓋文字，及其是否含 marker。
    """
    import importlib
    mc = importlib.import_module("marker_coverage")
    bs = bounds(pdf)
    print("\n=== 章區間之分割檢查（17 §12 第 1 項）===")
    print(f"{'章':>3}  {'起':>6} {'訖':>6} {'字元':>6}  起錨")
    for ch, i, j in bs:
        print(f"{ch:>3}  {i:>6} {j:>6} {j-i:>6}  {STARTS[ch][:52]}")
    gaps = [("首章之前", 0, bs[0][1]), ("末章之後", bs[-1][2], len(pdf))]
    total = sum(j - i for _, i, j in bs)
    print(f"\n  已覆蓋 {total} / {len(pdf)} 字元"
          f"（{total/len(pdf):.1%}）；重疊 **0**（構造上不可能）")
    bad = 0
    cnt, _ = mc.prefix_scan(pdf)
    reqs, _ = mc.req_prefixes(cnt)
    for name, i, j in gaps:
        seg = pdf[i:j]
        ms = mc.enumerate_markers(seg, reqs) if seg.strip() else []
        print(f"\n  未覆蓋段【{name}】{j-i} 字元；**其中之 marker：{ms or '無'}**")
        if seg.strip():
            print(f"    首 120 字元：{seg[:120]}")
            print(f"    末 120 字元：{seg[-120:]}")
        if ms:
            bad += 1
            print("    ← **停止條件 8 觸發** —— 未覆蓋段含 marker")
    if not bad:
        print("\n  **未覆蓋段皆不含 marker —— 停止條件 8 未觸發。**")
        print("  （首章之前為 p1–p7 之封面與五張流程圖頁，A-PMH04 已知之圖片佔位）")
    return bad


def sys1_chapter(ch: int) -> list[tuple[str, str]]:
    ws = openpyxl.load_workbook(SYS1, data_only=True)["Basic Report"]
    out = []
    for r in range(2, ws.max_row + 1):
        o = str(ws.cell(r, 3).value or "").strip()
        if re.fullmatch(rf"{ch}(\.\d+)*", o):
            out.append((o, norm(ws.cell(r, 4).value or "")))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("chapter", type=int, nargs="?")
    ap.add_argument("--partition", action="store_true",
                    help="17 §12 第 1 項 —— 章區間之覆蓋／重疊檢查")
    a = ap.parse_args()
    if a.partition:
        pdf_all = norm(PDF_TXT.read_text(errors="replace"))
        rc = partition(pdf_all)
        print_limits()
        sys.exit(1 if rc else 0)
    if a.chapter is None:
        raise SystemExit("須給章號，或用 --partition")
    ch = a.chapter
    pdf_all = norm(PDF_TXT.read_text(errors="replace"))
    pdf_ch = pdf_chapter(ch, pdf_all)
    rows = sys1_chapter(ch)
    sys_ch = " ".join(d for _, d in rows)

    print(f"=== 章 {ch} 之雙向複驗（R-PMH51）===")
    print(f"PDF 段：{len(pdf_ch)} 字元；SYS1：{len(rows)} 則、{len(sys_ch)} 字元")
    print(f"PDF 段起錨 `{STARTS[ch]}`（訖 = 下一章之起錨）")
    import importlib
    _mc = importlib.import_module("marker_coverage")
    _cnt, _ = _mc.prefix_scan(pdf_all)
    _reqs, _ = _mc.req_prefixes(_cnt)
    mk = _mc.enumerate_markers(pdf_ch, _reqs)
    print(f"PDF 段內 marker：{len(mk)} 個 —— {mk}")

    # --- 方向一：SYS1 → PDF ---
    print(f"\n--- 方向一（SYS1 → PDF）：SYS1 之字是否出現於 PDF ---")
    print(f"{'outline':<8} {'字數':>5}  {'逐字命中':<8} 覆蓋率")
    d1_miss = []
    for o, d in rows:
        hit = d in pdf_all
        cov = coverage(d, pdf_all)
        print(f"{o:<8} {len(d):>5}  {'是' if hit else '**否**':<8} {cov:6.1%}")
        if not hit:
            d1_miss.append((o, d, cov))

    # --- 方向二：PDF → SYS1（漏句只在此方向顯示）---
    print(f"\n--- 方向二（PDF → SYS1）：PDF 之字是否出現於 SYS1 ---")
    sents = sentences(pdf_ch)
    print(f"PDF 段切出 {len(sents)} 句（>= {MIN_SENT} 字元）")
    print(f"{'#':>3}  {'逐字命中':<8} {'覆蓋率':>7}  句首")
    residue = []
    for i, s in enumerate(sents, 1):
        hit = s in sys_ch
        cov = coverage(s, sys_ch)
        print(f"{i:>3}  {'是' if hit else '**否**':<8} {cov:6.1%}  {s[:58]}")
        if not hit:
            residue.append(s)   # R-PMH66(b)：逐字未命中者一律進殘餘

    print(f"\n=== 結果（R-PMH66 —— 判定為二值，門檻只分流殘餘）===")
    print(f"  方向一未逐字命中：{len(d1_miss)} 則")
    for o, d, cov in d1_miss:
        print(f"    outline {o}（覆蓋 {cov:.1%}）：{d[:90]}")
    print(f"\n  方向二逐字命中 {len(sents)-len(residue)}/{len(sents)}；"
          f"**殘餘 {len(residue)} 句**")
    print("  **殘餘不得由門檻自動判為「非漏」** —— 逐句須有人讀之具名結論；"
          "\n  覆蓋率只決定人讀之優先順序（高者先看），不決定結論。")
    unnamed = []
    for s in sorted(residue, key=lambda x: -coverage(x, sys_ch)):
        k = s[:60]
        v = RESIDUE_VERDICT.get(k)
        print(f"\n    [覆蓋 {coverage(s, sys_ch):5.1%}] {s}")
        if v:
            print(f"      人讀結論：{v}")
        else:
            print("      **人讀結論：未具名 ← FAIL（R-PMH66(c)）**")
            unnamed.append(k)
    print(f"\n  殘餘未具名結論者：**{len(unnamed)}**"
          f"{'' if not unnamed else ' ← **FAIL**'}")
    print_limits()
    sys.exit(1 if unnamed else 0)


if __name__ == "__main__":
    main()
