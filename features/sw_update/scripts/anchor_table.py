#!/usr/bin/env python3
"""T20a–e —— 錨表建置（下放包 07 §三）。

**只建候選表與分級，不定錨、不分群、不命名**（R-SU12(c)）。

軸依 **R-SU12(a)**：037 列之 `Requirement Description` 全文
× CFTS_57 之 487 個需求物件全文。章節歸屬由需求物件之母章導出。

**自我檢定為結構前提**（R-SU13、PLAYBOOK §7.1）：
`main()` 先跑 T20e，任一項不通過即非零碼退出且**不跑全母體**。

Usage:
    python3 scripts/anchor_table.py            # 自檢 → 全母體
    python3 scripts/anchor_table.py --selftest # 只跑自檢
"""
import argparse
import math
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
A03 = ROOT / "inputs/SoftwareUpdate_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx"
CFTS = ROOT / "inputs/R1LR_Atl-H_25PI4.5 Dec Release-xOTA_CFTS_57 Reflash_20251202-2111.docx"

C_ID, C_SRC, C_TITLE, C_DESC, C_CAT, C_SUB = 0, 1, 2, 3, 5, 6
IN_SCOPE = ("Functional Requirement", "Non Functional Requirement")

# 停用詞 —— 沿 framework_survey 之 13 字，另加長文本常見之功能詞。
# **本表與 framework_survey.STOP 不同，且刻意如此**：那裡比對標題（短），
# 這裡比對需求句全文（長）。長文本若不去 shall/must/system 之類，
# 每一對都會共享它們而使分數趨同 —— 判別力降低。
# 二者不共用，故**不得聲稱參數一致**（下放包 06 之拘束只及於 T18d／T19）。
STOP = set("""the a an of and for to in on is are be shall must will with
that this these those it its as at by from or if then when where which
be being been has have had not no all any each such other same than
system vehicle requirement requirements support supported provide provided
""".split())


def norm_tokens(s):
    ws = re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).split()
    return [w for w in ws if w not in STOP and len(w) > 2]


# ── T20a —— CFTS_57 需求物件全文 ──────────────────────────────────────
def cfts_objects():
    """487 個需求物件：ObjectID、母章號、全文（逐字，不摘要）。

    抽取法沿 `ANCHOR_POOL.md` 之既定判準（下放包 03 T12）：
    heading style 1–4 之 `{7位}` 為章節；其後之 7 位數若右鄰
    `: [Artifact Type:Subsystem Functional Requirement]` 宣告者為需求物件。
    **全文 = 該宣告之後至同段落結束之文字**（逐字）。
    """
    raw = zipfile.ZipFile(CFTS).read("word/document.xml").decode("utf8", "replace")
    paras = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", raw, re.S):
        m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        paras.append(((m.group(1) if m else ""), re.sub(r"<[^>]+>", "", p)))
    HEAD, TOC = {"1", "2", "3", "4", "5"}, {"10", "20", "30", "40", "50"}
    DECL = re.compile(r"^\s*(\d{7}):\s*\[Artifact Type:Subsystem Functional Requirement\]")
    # **需求句在宣告段之「後一段」起** —— 宣告段本身只有 `{oid}: [k:v]…` 之屬性串。
    # 初版誤以為同段，致 487 個全文皆空（見上繳包 06 §2.1）。
    # 全文 = 宣告段之後至**下一個宣告段或標題段**之前的全部段落，逐字串接。
    idx = []
    for i, (st, t) in enumerate(paras):
        if st in TOC:
            continue
        if st in HEAD:
            m = re.search(r"^\s*([\d.]+)\s+(.*?)\s*\{(\d{7})\}", t)
            if m:
                idx.append(("H", i, m.group(1), m.group(2)))
                continue
        m = DECL.match(t)
        if m:
            idx.append(("R", i, m.group(1), None))
    objs, fail, cur = [], [], None
    for k, (kind, i, a, b) in enumerate(idx):
        if kind == "H":
            cur = {"num": a, "title": b}
            continue
        stop = idx[k + 1][1] if k + 1 < len(idx) else len(paras)
        body = " ".join(paras[j][1].strip() for j in range(i + 1, stop)
                        if paras[j][0] not in TOC and paras[j][1].strip())
        body = re.sub(r"\s+", " ", body).strip()
        if any(o["oid"] == a for o in objs):
            continue
        if not body:
            fail.append((a, cur["num"] if cur else "?", "宣告段之後至下一宣告／標題之間無文字"))
            continue
        objs.append({"oid": a, "chap": cur["num"] if cur else "?",
                     "chap_title": cur["title"] if cur else "?", "text": body})
    return objs, fail


# ── T20b —— 路徑 A：TF-IDF cosine ────────────────────────────────────
class TfIdf:
    """TF-IDF cosine。**選它而非 Jaccard 之理由**：Jaccard 對長文本之
    判別力低（長度差異主導聯集），且不加權罕見詞 —— 上繳包 05 §0 之
    92% 未達門檻即其在標題上之表現。TF-IDF 以 idf 加權罕見詞，
    對「需求句 × 需求句」這種同體例長文本較合適。

    **已知偏差方向**：偏好共享罕見詞者。若二列共用一個罕見專名
    （如 `OMA-DM`）而語意無關，其分數會偏高 —— 故 R-SU13 之路徑 B
    為必要之獨立第二路，不得以本路單獨定錨。
    """

    def __init__(self, docs):
        self.docs = docs
        df = Counter()
        self.tf = []
        for d in docs:
            c = Counter(norm_tokens(d))
            self.tf.append(c)
            df.update(c.keys())
        n = len(docs)
        self.idf = {w: math.log((n + 1) / (k + 1)) + 1 for w, k in df.items()}
        self.vecs = [self._vec(c) for c in self.tf]

    def _vec(self, c):
        v = {w: (1 + math.log(f)) * self.idf.get(w, math.log(len(self.docs) + 1) + 1)
             for w, f in c.items()}
        nrm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {w: x / nrm for w, x in v.items()}

    def query(self, text, top=3):
        q = self._vec(Counter(norm_tokens(text)))
        sc = []
        for i, v in enumerate(self.vecs):
            s = sum(q[w] * v[w] for w in q.keys() & v.keys())
            if s > 0:
                sc.append((s, i))
        sc.sort(reverse=True)
        return sc[:top]


def a03_rows():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    return [r for r in wb["AnalysisReport_FULL"].iter_rows(min_row=8, values_only=True)
            if r[C_ID] not in (None, "") and r[C_CAT] in IN_SCOPE]


def rid_num(r):
    return int(re.search(r"(\d+)$", str(r[C_ID])).group(1))


# ── T20c —— 路徑 B：SYS-RA 序號之連續段 ──────────────────────────────
def sysra_num(r):
    m = re.search(r"SYS-RA-FOTA-(\d+)", str(r[C_SRC] or ""))
    return int(m.group(1)) if m else None


def segments(rows):
    """`Source Requirement ID` 之連續遞增／遞減段。

    段之定義：相鄰二列之 SYS-RA 號差為 +1 或 -1 且方向不變。
    無 SYS-RA 號者中斷該段並自成「不可解」。
    """
    segs, cur = [], None
    for r in rows:
        n = sysra_num(r)
        if n is None:
            if cur:
                segs.append(cur)
                cur = None
            segs.append({"rows": [r], "dir": 0, "unresolved": True})
            continue
        if cur and cur["dir"] in (0, n - cur["last"]) and abs(n - cur["last"]) == 1:
            cur["rows"].append(r)
            cur["dir"] = n - cur["last"]
            cur["last"] = n
        else:
            if cur:
                segs.append(cur)
            cur = {"rows": [r], "dir": 0, "last": n, "unresolved": False}
    if cur:
        segs.append(cur)
    return segs


def seg_block(seg, objs, tfidf):
    """段之區塊落點：段內各列之路徑 A 首選章之眾數。

    **路徑 B 之獨立性須說清楚**：本函式用到 A 之結果，故**不是**
    完全獨立於 A。真正獨立之部分是**分段本身**（純以 SYS-RA 序號切，
    不看文字）；落點則以段為單位彙總 A 之逐列結果。
    其獨立性在於：**A 之單列噪音被段內多數決壓過** ——
    一列被罕見詞誤導，整段不會。這是區塊級證據之來源。
    **若段長為 1，本路等於 A，無獨立性** —— 該類段一律標為不可判。
    """
    if seg.get("unresolved") or len(seg["rows"]) < 2:
        return None, "段長 < 2 或無 SYS-RA 號 —— 本路不可判"
    votes = Counter()
    for r in seg["rows"]:
        hits = tfidf.query(str(r[C_DESC] or ""), top=1)
        if hits:
            votes[objs[hits[0][1]]["chap"]] += 1
    if not votes:
        return None, "段內無任一列產生候選"
    top, k = votes.most_common(1)[0]
    return top, f"段長 {len(seg['rows'])}，{k} 列投向 {top}（分布 {dict(votes)}）"


# ── T20e —— 自我檢定（R-SU13；跑全母體前執行）────────────────────────
def self_test(rows, objs, tfidf):
    print("## T20e —— 自我檢定（R-SU13；未通過即不跑全母體）\n")
    ok = True
    by_id = {str(r[C_ID]).strip(): r for r in rows}

    print("### (i) 已知標的探針\n")
    probes = [
        ("SWE1-FOTA-351", "4.10.2",
         "分析層於下放包 06 §3.1 之 T19d 表列：其標題 `Server-Initiated "
         "Session Flow` 對 CFTS `4.10.2` 之詞集重疊比為 **1.00**（完全重疊）"),
        ("SWE1-FOTA-337", "4.10.5",
         "同表列，`Deployment Flow Initiation` → `4.10.5 Deployment Flow` "
         "分 0.67，為該表中次高者"),
        ("SWE1-FOTA-258", "4.9.1",
         "同表列，`Update Agent Bootloader Integration` → "
         "`4.9.1 Update Agent Requirements` 分 0.50"),
    ]
    print("| # | 037 列 | 期望章 | A 首選章 | 分 | 前 3 候選 | 判 |")
    print("|---|---|---|---|---:|---|---|")
    for i, (rid, want, why) in enumerate(probes, 1):
        r = by_id.get(rid)
        if r is None:
            print(f"| {i} | `{rid}` | {want} | **列不存在** | — | — | **FAIL** |")
            ok = False
            continue
        hits = tfidf.query(str(r[C_DESC] or ""), top=3)
        got = objs[hits[0][1]]["chap"] if hits else None
        cand = "；".join(f"{objs[j]['chap']}(`{objs[j]['oid']}`, {s:.3f})"
                         for s, j in hits) or "無"
        hit = got == want
        ok &= hit
        print(f"| {i} | `{rid}` | {want} | {got or '—'} | "
              f"{hits[0][0]:.3f} | {cand} | {'PASS' if hit else '**FAIL**'} |")
    print("\n**探針之「已知」依據**（逐一說明，非自選為便）：")
    for i, (rid, want, why) in enumerate(probes, 1):
        print(f"{i}. `{rid}` → `{want}` —— {why}")
    print("\n> ⚠ 三例皆源自 **T19d 之字面比對**，而 R-SU12(b) 已將該路降為輔助訊號。"
          "\n> 故此三例為**弱已知**：它們是「字面上高度重合」而非「經人裁定之對應」。"
          "\n> **本檢定能證明管線會動，不能證明它對。**")

    print("\n### (ii) 反向輸入 —— 與 SW Update 無關之文字\n")
    negs = [
        ("vehicle_category §11.2",
         "Selecting yes to restoring defaults will reset their settings to "
         "default. Once settings are restored a pop-up will be shown stating "
         "Settings reset to default."),
        ("vehicle_category §4.1",
         "The Glove Box screen shall display a Lock control which the user "
         "presses to lock or unlock the glove box compartment."),
        ("audio_mgmt CFTS019",
         "When HU needs to activate audio on at least one loudspeaker "
         "according to the table above, HU shall store the current audio mode "
         "settings volume tone controls Fade and Balance controls."),
    ]
    # 母體之分數分布 —— 「高分」須有基準，否則 0.3 是高是低無從說起
    import random
    random.seed(0)
    base = []
    for r in random.sample(rows, min(40, len(rows))):
        h = tfidf.query(str(r[C_DESC] or ""), top=1)
        if h:
            base.append(h[0][0])
    base.sort()
    p50 = base[len(base) // 2] if base else 0
    p10 = base[max(0, len(base) // 10)] if base else 0
    print(f"**基準**（母體 40 列隨機取樣之首選分數）：中位數 **{p50:.3f}**、"
          f"第 10 百分位 **{p10:.3f}**、最低 {base[0]:.3f}、最高 {base[-1]:.3f}")
    print(f"\n**判準**：反向輸入之首選分數須 **低於母體第 10 百分位（{p10:.3f}）**。")
    print("\n| # | 來源 | 首選章 | 分 | 判 |")
    print("|---|---|---|---:|---|")
    for i, (src, txt) in enumerate(negs, 1):
        h = tfidf.query(txt, top=1)
        s = h[0][0] if h else 0.0
        c = objs[h[0][1]]["chap"] if h else "—"
        good = s < p10
        ok &= good
        print(f"| {i} | {src} | {c} | {s:.3f} | {'PASS' if good else '**FAIL**'} |")
    print("\n> **本項之判準是相對的，不是絕對的** —— 「不產生高分候選」若不給基準，"
          "\n> 任何分數都可被說成低。故以母體分布之第 10 百分位為線。")
    # ── (iii) 自引探針 —— **真地面真值**（執行層增設，下放包未列）
    print("\n### (iii) 自引探針 —— 真地面真值（執行層增設）\n")
    print("037 之 `Requirement Description` 內**直接引用 CFTS ObjectID** 者，"
          "其對應**由 037 自己寫出**\n—— 獨立於路徑 A（文字）與路徑 B（序號）。"
          "全 311 列掃描得 **2 筆**。\n")
    print("**比對前先剔除 Description 中之 `490xxxx` 數字串** —— "
          "否則「命中」只是因為兩邊都有那串數字，\n那不是文字相似，是抄號碼。\n")
    gt = [("SWE1-FOTA-313", "4.12"), ("SWE1-FOTA-327", "4.12.1")]
    print("| 037 列 | 自引所指之章 | A 首選章 | 分 | 前 3 候選 | 判 |")
    print("|---|---|---|---:|---|---|")
    gt_ok = True
    for rid, want in gt:
        r = by_id.get(rid)
        desc = re.sub(r"(?<!\d)490\d{4}(?!\d)", " ", str(r[C_DESC] or "")) if r else ""
        hits = tfidf.query(desc, top=3)
        got = objs[hits[0][1]]["chap"] if hits else None
        cand = "；".join(f"{objs[j]['chap']}({s:.3f})" for s, j in hits)
        good = got == want
        gt_ok &= good
        print(f"| `{rid}` | **{want}** | {got} | {hits[0][0]:.3f} | {cand} "
              f"| {'PASS' if good else '**FAIL**'} |")
    print(f"\n**(iii) {'全過' if gt_ok else '**未過**'}**")

    print(f"\n**自我檢定（依 R-SU13 之三項）：{'全過' if ok else '**未過**'}**")
    if not ok and gt_ok:
        print("\n> ⚠ **(i) 未過而 (iii) 全過** —— 二者指向相反。")
        print("> (i) 之三個探針源自 T19d 之**字面標題比對**，"
              "而 R-SU12(b) 已將該路降為輔助訊號；")
        print("> (iii) 之二筆為 037 **自己寫出**之對應。")
        print("> **證據較強者說管線是對的；較弱者說它是錯的。**")
        print("> 依 R-SU13「任一項不通過即停」，**仍停**——"
              "探針之效力由分析層裁，不由執行層自換。")
    return ok


# ── T20d —— 雙路合議與分級 ───────────────────────────────────────────
def grade(a_hits, objs, b_chap):
    """R-SU13 之信度分級。

    「明顯差距」須有數字，否則 H 與 M 之界線由讀者自填。
    **本檔取 A 首選與次選之分差 ≥ 0.05 為「明顯」** ——
    該值為本檔自訂，**非裁定**，其選定理由見上繳包之揭露。
    """
    if not a_hits:
        return "L", "A 無候選", None, 0.0, 0.0
    a_chap = objs[a_hits[0][1]]["chap"]
    s1 = a_hits[0][0]
    s2 = a_hits[1][0] if len(a_hits) > 1 else 0.0
    gap = s1 - s2
    if b_chap is None:
        return "M", "僅 A 一路可判", a_chap, s1, gap
    if a_chap != b_chap:
        return "L", f"A={a_chap} 與 B={b_chap} 不同章", a_chap, s1, gap
    return ("H", "A、B 同章且首次選分差 ≥ 0.05", a_chap, s1, gap) if gap >= 0.05 \
        else ("M", "A、B 同章但首次選分差 < 0.05", a_chap, s1, gap)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    rows = a03_rows()
    objs, fail = cfts_objects()
    print(f"## T20a —— CFTS_57 需求物件全文抽取\n")
    print(f"- 抽得 **{len(objs)}** 個需求物件（應 487 —— "
          f"{'閉合 ✅' if len(objs) == 487 else '**不閉合 ❌**'}）")
    print(f"- 抽取失敗 **{len(fail)}** 個" + (f"：{fail}" if fail else "（無）"))
    lens = sorted(len(o["text"]) for o in objs)
    print(f"- 全文長度：中位數 {lens[len(lens)//2]}、最短 {lens[0]}、最長 {lens[-1]} 字元")
    print(f"- 037 in-scope 列 **{len(rows)}**（應 311 —— "
          f"{'閉合 ✅' if len(rows) == 311 else '**不閉合 ❌**'}）\n")

    tfidf = TfIdf([o["text"] for o in objs])
    if not self_test(rows, objs, tfidf):
        print("\n**自我檢定未通過 —— 不跑全母體，非零碼退出**（R-SU13）")
        return 2
    if args.selftest:
        return 0

    # ── 路徑 B
    segs = segments(rows)
    print(f"\n## T20c —— 路徑 B：`Source Requirement ID` 之連續段\n")
    print(f"- 分段 **{len(segs)}** 段；不可解（無 SYS-RA 號）"
          f"**{sum(1 for s in segs if s.get('unresolved'))}** 段")
    print(f"- 段長分布：{dict(Counter(len(s['rows']) for s in segs))}\n")
    print("| # | 037 列區間 | SYS-RA 區間 | 段長 | 落點章 | 依據 |")
    print("|---:|---|---|---:|---|---|")
    seg_of = {}
    for i, sg in enumerate(segs, 1):
        b_chap, why = seg_block(sg, objs, tfidf)
        for r in sg["rows"]:
            seg_of[str(r[C_ID]).strip()] = (i, b_chap, why)
        ids = [rid_num(r) for r in sg["rows"]]
        ns = [sysra_num(r) for r in sg["rows"] if sysra_num(r) is not None]
        print(f"| {i} | {ids[0]}–{ids[-1]} | "
              f"{(str(ns[0]) + '–' + str(ns[-1])) if ns else '—'} | "
              f"{len(sg['rows'])} | {b_chap or '**不可判**'} | {why} |")

    # ── T20d
    print(f"\n## T20d —— 雙路合議與分級\n")
    out, cnt = [], Counter()
    for r in rows:
        rid = str(r[C_ID]).strip()
        hits = tfidf.query(str(r[C_DESC] or ""), top=3)
        _, b_chap, _ = seg_of.get(rid, (None, None, ""))
        g, why, a_chap, s1, gap = grade(hits, objs, b_chap)
        cnt[g] += 1
        out.append({"rid": rid, "title": str(r[C_TITLE] or ""), "grade": g,
                    "why": why, "a_chap": a_chap, "b_chap": b_chap,
                    "s1": s1, "gap": gap,
                    "cands": [(objs[j]["oid"], objs[j]["chap"], s)
                              for s, j in hits]})
    print(f"| 級 | 列數 | 佔比 |\n|---|---:|---:|")
    for g in ("H", "M", "L"):
        print(f"| **{g}** | {cnt[g]} | {cnt[g]/len(rows)*100:.1f}% |")
    print(f"\n**閉合**：{cnt['H']} + {cnt['M']} + {cnt['L']} = {sum(cnt.values())}"
          f"（應 311 —— {'✅' if sum(cnt.values()) == 311 else '**❌**'}）\n")
    print("### L 級全清單（R-SU13：不得列入錨表）\n")
    print("| 037 列 | 標題 | A 首選章 | B 落點章 | A 分 | 分差 | 理由 |")
    print("|---|---|---|---|---:|---:|---|")
    for o in out:
        if o["grade"] == "L":
            print(f"| `{o['rid']}` | {o['title'][:42]} | {o['a_chap'] or '—'} | "
                  f"{o['b_chap'] or '—'} | {o['s1']:.3f} | {o['gap']:.3f} | {o['why']} |")

    # ── ANCHOR_TABLE.md
    L = ["# ANCHOR_TABLE — SW Update 逐列候選表（T20，下放包 07）\n",
         "> **候選，非結論**（R-SU12(c)）。任何一列之最終錨點須經 R-SU13 之",
         "> 雙路檢定並由**分析層裁定**；執行層不得逕定。",
         "> **L 級不得列入錨表**（R-SU13）—— 本表仍列出以供裁定，其 `grade` 欄標 L。\n",
         f"- 母體 311 列；H {cnt['H']}／M {cnt['M']}／L {cnt['L']}",
         "- 路徑 A：TF-IDF cosine，037 `Requirement Description` 全文 × "
         "CFTS_57 487 需求物件全文",
         "- 路徑 B：`Source Requirement ID` 連續段之區塊落點（段長 < 2 者不可判）\n",
         "| 037 列 | 標題 | grade | A 首選（ObjectID／章／分） | 次選 | 第三 | B 落點章 | 分差 |",
         "|---|---|---|---|---|---|---|---:|"]
    for o in out:
        c = o["cands"] + [("—", "—", 0.0)] * 3
        L.append(f"| `{o['rid']}` | {o['title'][:40]} | **{o['grade']}** | "
                 f"`{c[0][0]}` {c[0][1]} {c[0][2]:.3f} | "
                 f"`{c[1][0]}` {c[1][1]} {c[1][2]:.3f} | "
                 f"`{c[2][0]}` {c[2][1]} {c[2][2]:.3f} | "
                 f"{o['b_chap'] or '—'} | {o['gap']:.3f} |")
    (ROOT / "ANCHOR_TABLE.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\n→ `ANCHOR_TABLE.md` 已寫出（311 列全列）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
