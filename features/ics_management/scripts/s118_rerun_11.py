#!/usr/bin/env python3
"""下放包 11 作業 B —— NBSP 正規化重跑（R-ICS38(c)；A-ICS66）。

**後繼腳本**：不回改 `s118_compare_08.py`、不回改 `s118_gap_09.py`（R-ICS38(c)：
08 之報告與腳本不回改）。本檔重新實作二者之量測面，唯一差異為**比對前之正規化**。

**零寫入保證**：對 `generated/**`（TC JSON）只讀不寫；對 `RULINGS.md`／
`ANOMALIES.md`／`DATA_REQUESTS.md`／`docs/handoff/**` 不觸碰。
`cfts020_probe.py` 以 `importlib` 唯讀載入，不修改。
本檔不執行任何 git 指令。

量測四項
--------
A. 不可見／非 ASCII 字元普查（正規化清單之實測依據）
B. 09 之覆蓋清點重跑（機械層 token 命中）—— 原始 vs 正規化二數並報
C. 08 之「§1.18 有無行為對應」重跑 —— 錨層／TC 層二數並報
D. 依 R-ICS39(c) 之並列雙錨集合：逐條列出應加之 §1.18 錨（**只列不加**）

用法：
  python3 features/ics_management/scripts/s118_rerun_11.py            # 全部
  python3 features/ics_management/scripts/s118_rerun_11.py --census   # 只做 A
  python3 features/ics_management/scripts/s118_rerun_11.py --coverage # 只做 B
  python3 features/ics_management/scripts/s118_rerun_11.py --counterpart  # 只做 C
  python3 features/ics_management/scripts/s118_rerun_11.py --anchors  # 只做 D
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "scripts" / "cfts020_probe.py"
GEN = ROOT / "generated"

# 08 之交辦基準批次（b01~b05 = 25 條）。b06 為 08 成文後之產出。
BASE_BATCHES = ("b01", "b02", "b03", "b04", "b05")
# 下放包 11 所指之 27 條母數 = b01~b06。b07 於本作業執行期間由並行 session 新增（見報告 §0-3）。
B11_BATCHES = ("b01", "b02", "b03", "b04", "b05", "b06")


# --------------------------------------------------------------------------
# §A 正規化
# --------------------------------------------------------------------------
# 正規化對照表（逐項實測後決定，見報告 §0-1）
NORM_MAP = {
    " ": " ",   # NO-BREAK SPACE —— A-ICS66 之主因
    " ": " ",   # FIGURE SPACE
    " ": " ",   # THIN SPACE
    " ": " ",   # NARROW NO-BREAK SPACE
    "​": "",    # ZERO WIDTH SPACE
    "‌": "",    # ZERO WIDTH NON-JOINER
    "‍": "",    # ZERO WIDTH JOINER
    "﻿": "",    # ZERO WIDTH NO-BREAK SPACE (BOM)
    "­": "",    # SOFT HYPHEN
    "‘": "'",   # LEFT SINGLE QUOTATION MARK
    "’": "'",   # RIGHT SINGLE QUOTATION MARK
    "“": '"',   # LEFT DOUBLE QUOTATION MARK
    "”": '"',   # RIGHT DOUBLE QUOTATION MARK
    "–": "-",   # EN DASH
    "—": "-",   # EM DASH
    "−": "-",   # MINUS SIGN
    "▪": " ",   # BLACK SMALL SQUARE（項目符號）
    "•": " ",   # BULLET
    "\t": " ",
    "\r": "\n",
}


def normalize(text: str) -> str:
    """比對前正規化。R-ICS38(c) 之最小要求為 U+00A0；本表為實測後之擴充。

    注意：本正規化**只用於比對**，不寫回任何檔；
    亦**不及 test_item 上半之 verbatim**（R-ICS31(b) 不變，那是逐字）。
    """
    for src, dst in NORM_MAP.items():
        text = text.replace(src, dst)
    # 折疊連續空白（不跨行）
    text = re.sub(r"[ ]{2,}", " ", text)
    return text


def load_probe():
    spec = importlib.util.spec_from_file_location("cfts020_probe", PROBE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def census(objs) -> None:
    """A：不可見／非 ASCII 字元普查（全文件 + §1.18/§1.8 分列）。"""
    def count(pool):
        c: collections.Counter = collections.Counter()
        for o in pool:
            for ch in o["text"]:
                if ord(ch) > 126 or (ord(ch) < 32 and ch != "\n"):
                    c[ch] += 1
        return c

    s118 = [o for o in objs if o["section_no"].startswith("1.18")]
    s18 = [o for o in objs if o["section_no"].startswith("1.8")
           and not o["section_no"].startswith("1.18")]
    for label, pool in (("全文件", objs), ("§1.18", s118), ("§1.8", s18)):
        c = count(pool)
        print(f"\n-- {label}（{len(pool)} 物件）--")
        if not c:
            print("   （無）")
        for ch, n in c.most_common():
            nm = unicodedata.name(ch, "?")
            covered = "已正規化" if ch in NORM_MAP else "未列入"
            print(f"   U+{ord(ch):04X}  {nm:34}  {n:6}  {covered}")
    # 含 NBSP 之判適用物件數
    for label, pool in (("§1.18", s118), ("§1.8", s18)):
        ap = [o for o in pool if o["verdict"] == "適用"]
        n = sum(1 for o in ap if " " in o["text"])
        print(f"\n{label} 判適用 {len(ap)} 個，其中含 NBSP 者 {n} 個")


# --------------------------------------------------------------------------
# §B 09 之覆蓋清點重跑（沿用 09 §0-3 之判準，只換正規化）
# --------------------------------------------------------------------------
STOP = {
    "CFTS", "ICS", "TLM", "HMI", "LIDS", "CSTACK", "BHCAN", "CLIMATIC",
    "PANEL", "PLEASE", "SHALL", "SIGNAL", "SIGNALS", "SCREEN", "SCREENS",
}

TOK_PATTERNS = [
    re.compile(r"\$[A-Za-z0-9_<>]+\$"),
    re.compile(r"\b[A-Z][A-Z0-9_]{4,}\b"),
    re.compile(r'"([^"]+)"'),
    re.compile(r"\bT[A-Za-z][A-Za-z0-9_]{3,}\b"),
]


def tokens(text: str) -> set[str]:
    out: set[str] = set()
    for pat in TOK_PATTERNS:
        for m in pat.finditer(text):
            tok = m.group(1) if m.lastindex else m.group(0)
            if tok.upper().strip("$_") in STOP:
                continue
            out.add(tok)
    return out


def tnorm(sig: str) -> str:
    """訊號符號之比對正規化（同 09：去 `$`、去 `<n>`、去非英數、轉小寫）。"""
    s = sig.strip("$").replace("<n>", "").replace("<N>", "")
    return re.sub(r"[^a-z0-9]", "", s.lower())


def load_tcs(batches=None) -> list[dict]:
    tcs = []
    for f in sorted(GEN.glob("b0*/b0*_tcs.json")):
        data = json.loads(f.read_text(encoding="utf8"))
        if batches is not None and data["batch"] not in batches:
            continue
        for i, t in enumerate(data["tcs"], 1):
            tcs.append({
                "batch": data["batch"],
                "no": f'{data["batch"]}-{i:02d}',
                "req_id": t["req_id"],
                "title": t.get("tc_title", ""),
                "anchors": [a.strip() for a in
                            str(t.get("specification_reference", "")).split("\n") if a.strip()],
                "verify_text": "\n".join([
                    t.get("test_item", ""),
                    t.get("test_procedure", ""),
                    t.get("expected_result", ""),
                ]),
            })
    return tcs


def hits(obj_toks: set[str], tcs: list[dict]) -> dict[str, list[str]]:
    res = {}
    for tok in sorted(obj_toks):
        n = tnorm(tok)
        if len(n) < 4:
            continue
        res[tok] = [t["no"] for t in tcs if n in tnorm(t["verify_text"])]
    return res


def coverage(objs, tcs) -> None:
    """B：逐物件之機械層 token 命中 —— 原始 vs 正規化二數並報。"""
    ap = [o for o in objs if o["section_no"].startswith("1.18") and o["verdict"] == "適用"]
    print(f"\n判適用 §1.18 物件 {len(ap)} 個；TC 母數 {len(tcs)} 條")
    print("\n| ObjectID | § | 原始 token 數 | 正規化 token 數 | 原始全中 TC | 正規化全中 TC | 差異 |")
    print("|---|---|---|---|---|---|---|")
    changed = []
    for o in sorted(ap, key=lambda x: x["id"]):
        raw_t = tokens(o["text"])
        nrm_t = tokens(normalize(o["text"]))
        raw_h = hits(raw_t, tcs)
        nrm_h = hits(nrm_t, tcs)

        def full(h):
            if not h:
                return []
            return [t["no"] for t in tcs if all(t["no"] in v for v in h.values())]

        rf, nf = full(raw_h), full(nrm_h)
        diff = "—" if (raw_t == nrm_t and rf == nf) else "**變**"
        if diff != "—":
            changed.append((o["id"], sorted(nrm_t - raw_t), sorted(raw_t - nrm_t), rf, nf))
        print(f'| `{o["id"]}` | {o["section_no"]} | {len(raw_t)} | {len(nrm_t)} | '
              f'{len(rf)} | {len(nf)} | {diff} |')
    print(f"\n正規化後 token 集合或全中集合改變者：{len(changed)} 個")
    for oid, added, removed, rf, nf in changed:
        print(f"\n  {oid}")
        print(f"    正規化後新增 token：{added}")
        print(f"    正規化後消失 token：{removed}")
        print(f"    全中 TC：{rf}  ->  {nf}")


# --------------------------------------------------------------------------
# §C 08 之行為對應重跑（錨層／TC 層）
# --------------------------------------------------------------------------
ACT_ICS = r"\bICS (?:shall|will|has to|determines|is )"
ACT_HU = r"\bHU (?:shall|will|has to|receives|determines|sees|is |transitions)"
ACT_TLM = r"\bTLM (?:shall|has to|receives|is |determines)"

BEHAVIORS: list[tuple[str, str | None, str, str]] = [
    ("按鍵資料傳送（ICS 側送出）", ACT_ICS, r"button", "主詞 ICS ∧ 本文含 button"),
    ("按鍵資料傳送（HU／TLM 側接收）", f"(?:{ACT_HU}|{ACT_TLM})", r"[Bb]utton",
     "主詞 HU 或 TLM ∧ 本文含 button"),
    ("旋鈕資料傳送（ICS 側送出）", ACT_ICS, r"[Kk]nob|KNOB", "主詞 ICS ∧ 本文含 knob/KNOB"),
    ("旋鈕資料傳送（HU／TLM 側接收）", f"(?:{ACT_HU}|{ACT_TLM})", r"[Kk]nob|KNOB",
     "主詞 HU 或 TLM ∧ 本文含 knob/KNOB"),
    ("按壓事件 short/long press", None,
     r"short press|long press|Short Press|Long Press|Tpress|button press event",
     "本文含 short/long press、Tpress 或 button press event"),
    ("顯示狀態 $TGW_DISP_STAT$", None, r"\$TGW_DISP_STAT\$", "本文含 $TGW_DISP_STAT$"),
    ("顯示狀態 $RQ_DISP_INTS$", None, r"\$RQ_DISP_INTS\$", "本文含 $RQ_DISP_INTS$"),
    ("顯示狀態 $DCSD_DISP_STAT$", None, r"\$DCSD_DISP_STAT\$", "本文含 $DCSD_DISP_STAT$"),
    ("stuck button", None, r"[Ss]tuck|Tstuck_button", "本文含 stuck 或 Tstuck_button"),
    ("POWER 硬鍵行為", None, r"POWER hardkey|\$ICSPowerButton\$|PowerModeSts_CStack",
     "本文含 POWER hardkey 或 $ICSPowerButton$ 或 PowerModeSts_CStack"),
    ("SCREEN OFF 硬鍵行為", None,
     r"SCREEN OFF hardkey|\$ICSScreenOffButton\$|Screen Off|Screen On",
     "本文含 SCREEN OFF hardkey / $ICSScreenOffButton$ / Screen Off / Screen On"),
    ("Enter 按鍵行為", None, r"\$Enter_Button\$", "本文含 $Enter_Button$"),
    ("Back 按鍵行為", None, r"\$Back_Button\$", "本文含 $Back_Button$"),
    ("點名 CLIMATIC_PANEL 訊息", None, r"CLIMATIC_PANEL", "本文含 CLIMATIC_PANEL"),
    ("時間變數之定值", None, r"msec|= 1\.5 sec|120 sec", "本文含 msec 或具體秒值"),
    ("Mute 行為", None, r"\$ICSMuteButton\$|Mute", "本文含 $ICSMuteButton$ 或 Mute"),
    ("Logistic／Power Mode 狀態回報", None, r"[Ll]ogistic", "本文含 logistic"),
]


def tags(text: str, norm: bool = True) -> list[str]:
    if norm:
        text = normalize(text)
    out = []
    for name, actor, topic, _ in BEHAVIORS:
        if actor is not None and not re.search(actor, text):
            continue
        if re.search(topic, text):
            out.append(name)
    return out


def counterpart_run(objs, tcs, norm: bool, verbose: bool = False):
    """回傳 (a020, hit, miss, tc_with_020, tc_all_hit, tc_part, by_id, s118_ap)。"""
    by_id = {o["id"]: o for o in objs}
    s118_ap = [o for o in objs
               if o["section_no"].startswith("1.18") and o["verdict"] == "適用"]

    def has_counterpart(ref: str) -> bool:
        o = by_id.get(ref.split("-", 1)[1])
        if o is None:
            return False
        t = set(tags(o["text"], norm))
        return bool(t) and any(t & set(tags(c["text"], norm)) for c in s118_ap)

    anchors: dict[str, list[str]] = {}
    for t in tcs:
        for r in t["anchors"]:
            anchors.setdefault(r, []).append(t["no"])
    a020 = [k for k in anchors if k.startswith("CFTS020-")]
    hit = sorted(k for k in a020 if has_counterpart(k))
    miss = sorted(k for k in a020 if not has_counterpart(k))
    tc_with = [t for t in tcs if any(r.startswith("CFTS020-") for r in t["anchors"])]
    tc_all = [t for t in tc_with
              if all(has_counterpart(r) for r in t["anchors"] if r.startswith("CFTS020-"))]
    tc_part = [t for t in tc_with
               if any(not has_counterpart(r) for r in t["anchors"] if r.startswith("CFTS020-"))]
    return a020, hit, miss, tc_with, tc_all, tc_part, has_counterpart


def counterpart(objs) -> None:
    """C：錨層／TC 層之原始 vs 正規化二數，且分 b01~b05（08 基準）與 b01~b06。"""
    for label, batches in (("b01~b05（08 之交辦基準，25 條）", BASE_BATCHES),
                           ("b01~b06（下放包 11 所指之 27 條母數）", B11_BATCHES),
                           ("全批次（含執行期間新增者）", None)):
        tcs = load_tcs(batches)
        print(f"\n===== {label} —— TC 母數 {len(tcs)} =====")
        for norm in (False, True):
            a020, hit, miss, tc_with, tc_all, tc_part, _ = counterpart_run(objs, tcs, norm)
            tag = "正規化後" if norm else "原始（08 算法）"
            print(f"\n  [{tag}]")
            print(f"    相異 CFTS020 錨 {len(a020)}：有對應 {len(hit)} / 無對應 {len(miss)}")
            print(f"      有對應：{', '.join(hit)}")
            print(f"      無對應：{', '.join(miss)}")
            print(f"    含 CFTS020 錨之 TC {len(tc_with)}："
                  f"全錨有對應 {len(tc_all)} / 至少一錨無對應 {len(tc_part)}")
            print(f"      全錨有對應：{', '.join(t['no'] for t in tc_all)}")
            print(f"      部分無對應：{', '.join(t['no'] for t in tc_part)}")


# --------------------------------------------------------------------------
# §D 加錨集合（R-ICS39(c)：並列雙錨，不擇一）——**只列不加**
# --------------------------------------------------------------------------
def anchor_plan(objs) -> None:
    """D：逐條列出 27 條中應加之 §1.18 錨（ObjectID）與加錨後之完整錨行。

    判準：對每一條 TC 之每一個 `CFTS020-<id>`（§1.8 側）錨，取其行為標籤集，
    於 §1.18 之 29 個判適用物件中找標籤交集非空者 —— 該物件即為同一行為面
    之 §1.18 母條，依 R-ICS39(c) 應**並列**加錨（不取代原錨）。
    排序依 IN §10.7：一 ObjectID 一行、ID 升序、前綴逐行重述。
    """
    tcs = load_tcs(B11_BATCHES)
    by_id = {o["id"]: o for o in objs}
    s118_ap = sorted([o for o in objs
                      if o["section_no"].startswith("1.18") and o["verdict"] == "適用"],
                     key=lambda x: x["id"])
    print(f"\nTC 母數 {len(tcs)}；§1.18 判適用候選母條 {len(s118_ap)}")
    total_new = 0
    covered_tc = 0
    for t in tcs:
        adds: dict[str, set[str]] = {}
        for r in t["anchors"]:
            if not r.startswith("CFTS020-"):
                continue
            o = by_id.get(r.split("-", 1)[1])
            if o is None:
                continue
            st = set(tags(o["text"]))
            if not st:
                continue
            for c in s118_ap:
                inter = st & set(tags(c["text"]))
                if inter:
                    adds.setdefault(c["id"], set()).update(inter)
        new = sorted(i for i in adds if f"CFTS020-{i}" not in t["anchors"])
        if not new:
            print(f'\n{t["no"]}  {t["title"]}\n  現有錨：{t["anchors"]}\n  應加：（無）')
            continue
        covered_tc += 1
        total_new += len(new)
        final = sorted(set(t["anchors"]) | {f"CFTS020-{i}" for i in new})
        print(f'\n{t["no"]}  {t["title"]}')
        print(f'  現有錨：{" + ".join(t["anchors"])}')
        for i in new:
            print(f'  應加 CFTS020-{i}  依據行為面：{sorted(adds[i])}')
        print("  加錨後完整錨行（IN §10.7 排序）：")
        for a in final:
            print(f"    {a}")
    print(f"\n== 合計：{covered_tc} 條 TC 需加錨，共加 {total_new} 個錨（**只列不加**，R-ICS39(d)）==")
    print("   （此為機械層之上界，粒度過粗 —— 見 anchor_plan_adjudicated()）")


# 判讀層之對應表：**逐字取自 `docs/reports/09_s118_coverage_gap.md` §1**
# 之「有覆蓋／部分覆蓋」欄（該欄依 09 §0-3 之 C1/C2/C3 判準人工判定）。
# 本輪已複驗其機械層輸入（§B：正規化前後 0 物件改變），故該判讀結論之
# 輸入未變，判定沿用。**本表不由本腳本推導，係引用**，可逐條回 09 §1 覆核。
ADJUDICATED: dict[str, tuple[str, list[str]]] = {
    "4821693": ("部分覆蓋", ["b04-01", "b04-02", "b04-03", "b04-04", "b04-05"]),
    "4821694": ("有覆蓋", ["b04-03", "b04-04"]),
    "4821695": ("有覆蓋", ["b04-05"]),
    "4821696": ("有覆蓋", ["b04-01", "b04-02", "b04-05"]),
    "4821697": ("有覆蓋", ["b04-04"]),
    "4821698": ("有覆蓋", ["b04-04"]),
    "4821701": ("部分覆蓋", ["b01-06"]),
    "4821702": ("有覆蓋", ["b04-06", "b05-01", "b05-02"]),
    "4821703": ("有覆蓋", ["b04-03"]),
    "4821704": ("部分覆蓋", ["b04-07"]),
    "4821705": ("有覆蓋", ["b03-08"]),
    "4821706": ("有覆蓋", ["b03-05", "b03-07"]),
    "4821709": ("部分覆蓋", ["b06-01", "b06-02"]),
}


def sort_anchors(refs) -> list[str]:
    """IN §10.7：一 ObjectID 一行、ID 升序、前綴逐行重述。"""
    return sorted(set(refs), key=lambda r: int(r.rsplit("-", 1)[1]))


def anchor_plan_adjudicated(objs) -> None:
    """D-2：b12 可直接執行之逐條加錨指示表（判讀層，窄集合）。

    R-ICS39(c)：同一行為二節皆有母條時 → **並列雙錨，不擇一**。
    「同一行為」之認定取 09 §1 已判之行為等值覆蓋（C1∧C2 對位者），
    非取 08 之節層粗標籤（後者只為「二節有無同面」之比較而設，
    用於逐條加錨會產生假性擴張，見 anchor_plan()）。
    """
    tcs = {t["no"]: t for t in load_tcs(B11_BATCHES)}
    by_id = {o["id"]: o for o in objs}
    per_tc: dict[str, list[tuple[str, str]]] = {}
    for oid, (verdict, tc_list) in ADJUDICATED.items():
        for no in tc_list:
            per_tc.setdefault(no, []).append((oid, verdict))

    total = 0
    print("\n| # | TC | tc_title | 現有錨 | 應加之錨（ObjectID） | 依據行為面 |")
    print("|---|---|---|---|---|---|")
    for i, no in enumerate(sorted(per_tc), 1):
        t = tcs[no]
        adds = sorted(per_tc[no], key=lambda x: int(x[0]))
        new = [f"CFTS020-{o}" for o, _ in adds if f"CFTS020-{o}" not in t["anchors"]]
        total += len(new)
        why = "；".join(f'{o}（{v}）' for o, v in adds)
        print(f'| {i} | {no} | {t["title"]} | {" + ".join(sort_anchors(t["anchors"]))} | '
              f'{" + ".join(new) if new else "（無）"} | {why} |')
    print(f"\n合計：{len(per_tc)} 條 TC，共加 {total} 個錨")

    print("\n### 加錨後之完整錨行（依 IN §10.7；b12 逐條照抄）\n")
    for no in sorted(per_tc):
        t = tcs[no]
        final = sort_anchors(list(t["anchors"]) + [f"CFTS020-{o}" for o, _ in per_tc[no]])
        print(f'**{no}** —— {t["title"]}')
        print("```")
        for a in final:
            print(a)
        print("```")
        for oid, v in sorted(per_tc[no], key=lambda x: int(x[0])):
            o = by_id[oid]
            print(f'- `{oid}` §{o["section_no"]}（{v}）：{normalize(o["text"])[:140]}')
        print()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--census", action="store_true")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--counterpart", action="store_true")
    ap.add_argument("--anchors", action="store_true")
    args = ap.parse_args()
    run_all = not any([args.census, args.coverage, args.counterpart, args.anchors])

    probe = load_probe()
    objs = probe.parse()

    if run_all or args.census:
        print("\n########## §A 不可見／非 ASCII 字元普查 ##########")
        census(objs)
    if run_all or args.coverage:
        print("\n########## §B 09 覆蓋清點重跑（機械層） ##########")
        coverage(objs, load_tcs(B11_BATCHES))
    if run_all or args.counterpart:
        print("\n########## §C 08 行為對應重跑（錨層／TC 層） ##########")
        counterpart(objs)
    if run_all or args.anchors:
        print("\n########## §D-1 加錨集合（機械層上界，只列不加） ##########")
        anchor_plan(objs)
        print("\n########## §D-2 加錨指示表（判讀層，b12 直接執行） ##########")
        anchor_plan_adjudicated(objs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
