#!/usr/bin/env python3
"""T58 —— pilot 收斂條件之驗證（下放包 10 §四，十項）。

第 3–8 項可機械化者一律機械化；第 2、9、10 項含人工判斷成分，
本腳本只驗其**可機械化之部分**，其餘於上繳包標明主觀範圍。

母體標註（R-VC15）：本輪 TC 數 12，其 leaf 取自 **117 leaf 母體**之
Test Set `Glove Box`（12 leaf）。
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
J = json.loads((ROOT / "generated" / "pilot_glovebox.json").read_text("utf-8"))
TCS = J["tcs"]

REQ_KEYS = ["tc_title", "pre_conditions", "input_test_data", "test_procedure",
            "expected_result", "specification_reference", "design_method",
            "priority", "split_flag", "split_reason"]
FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
          "expected_result"]

res = []


def chk(n, name, ok, detail):
    res.append((n, name, ok, detail))


# 1 —— 10 個必要 key（IN §10.1）
missing = {t["leaf_id"]: [k for k in REQ_KEYS if k not in t] for t in TCS}
bad = {k: v for k, v in missing.items() if v}
chk(1, "12 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）",
    len(TCS) == 12 and not bad,
    f"TC 數 {len(TCS)}；缺 key {bad or '無'}")

# 2 —— IN §9 十七項：見上繳包逐項；此處只驗可機械化之子項
chk(2, "IN §9 十七項自檢（機械化子項見第 3–8、11、12 項；全項見上繳包）",
    True, "本腳本不代替逐項判讀，見上繳包 10 §4.2")


# 11 —— §4.4 之三類禁項（下放包 12 §四.1）。
# ⚠ 前一輪之第 3 項人工判讀**只驗了三類中的一類**（feature under test as
# premise），漏掉 system defaults 與 step-controlled state，
# 導致 12/12 帶錯往下走。判準太鬆之漏檢，與前三件「太嚴而誤報」方向相反。
PC_DEFAULT = re.compile(
    r"\b(head unit|HU)\b.*\b(powered on|booted|on)\b|\bignition is on\b",
    re.I)
PC_PREMISE = re.compile(
    r"\b(is accessible|is available|can be reached)\b", re.I)
# 第三類最難機械化：「該狀態是否步驟可達成」需語意判斷。
# 可機械化之近似 —— 該 pre_condition 之文字若與任一 procedure 步驟之標的
# 重疊（共用一個引號標的），即列為候選並人工判讀。
QUOTED = re.compile(r'"([^"]+)"')
c11 = {"default": [], "premise": [], "step_overlap": []}
for t in TCS:
    for ln in t["pre_conditions"].split("\n"):
        s = re.sub(r"^\d+\.\s*", "", ln).strip()
        if not s:
            continue
        if PC_DEFAULT.search(s):
            c11["default"].append(f"{t['leaf_id']}: {s[:56]}")
        if PC_PREMISE.search(s):
            c11["premise"].append(f"{t['leaf_id']}: {s[:56]}")
        pcq = set(QUOTED.findall(s))
        prq = set(QUOTED.findall(t["test_procedure"]))
        if pcq & prq:
            c11["step_overlap"].append(
                f"{t['leaf_id']}: 共用標的 {sorted(pcq & prq)}")
chk(11, "pre_conditions 無 §4.4 三類禁項（system defaults／premise／step-controlled）",
    not any(c11.values()),
    "；".join(f"{k} {len(v)}" for k, v in c11.items())
    + (f" -- {sum(c11.values(), [])[:3]}" if any(c11.values()) else ""))

# 12 —— 對他筆之值的隱性依賴（下放包 12 §五）
RE_CROSSREF = re.compile(
    r"\b(comparable|corresponding|similar|equivalent)\b[^.]{0,40}"
    r"\b(ceiling|threshold|limit|count|timeout|duration|interval)\b", re.I)
c12 = []
for t in TCS:
    for f in ("test_procedure", "expected_result", "pre_conditions",
              "input_test_data", "test_item"):
        for m in RE_CROSSREF.finditer(t[f]):
            c12.append(f"{t['leaf_id']}/{f}: {m.group(0)[:50]}")
chk(12, "無對他筆之值的隱性依賴（comparable/corresponding/... ＋ 門檻類名詞）",
    not c12, f"命中 {len(c12)} 處 {c12 or '無'}")

# 3 —— test_item 括號下半 12 筆兩兩不同
low = {}
nobracket = []
for t in TCS:
    m = re.search(r"\(([^()]*)\)\s*$", t["test_item"].strip())
    if not m:
        nobracket.append(t["leaf_id"])
    else:
        low.setdefault(m.group(1).strip(), []).append(t["leaf_id"])
dup = {k: v for k, v in low.items() if len(v) > 1}
chk(3, "test_item 括號下半 12 筆兩兩不同（機械）",
    not nobracket and not dup and len(low) == 12,
    f"缺括號 {nobracket or '無'}；重複 {dup or '無'}；相異 {len(low)}")

# 3b —— 下半一律英文（R-S4 / R-PMH153）
cjk = [t["leaf_id"] for t in TCS
       if re.search(r"[一-鿿]",
                    re.search(r"\(([^()]*)\)\s*$",
                              t["test_item"].strip()).group(1))]
chk("3b", "test_item 括號下半無中文（R-S4）", not cjk, f"含中文 {cjk or '無'}")

# 4 —— specification_reference 與 recon_leaf_to_section.tsv 逐字相符
ref = {r[0]: r[3] for r in csv.reader(
    (ROOT / "data" / "recon_leaf_to_section.tsv").open(encoding="utf-8"),
    delimiter="\t")}
bad4 = [(t["leaf_id"], t["specification_reference"], ref.get(t["leaf_id"]))
        for t in TCS if t["specification_reference"] != ref.get(t["leaf_id"])]
chk(4, "specification_reference 12 筆與 recon_leaf_to_section.tsv 逐字相符",
    not bad4, f"不符 {len(bad4)} 筆 {bad4 or ''}")

# 5 —— priority 與 priority_final.tsv 逐字相符
pf = {r["req_id"]: r["final_p"] for r in csv.DictReader(
    (ROOT / "data" / "priority_final.tsv").open(encoding="utf-8"),
    delimiter="\t")}
bad5 = [(t["leaf_id"], t["priority"], pf.get(t["leaf_id"]))
        for t in TCS if t["priority"] != pf.get(t["leaf_id"])]
chk(5, "priority 12 筆與 priority_final.tsv 逐字相符",
    not bad5, f"不符 {len(bad5)} 筆 {bad5 or ''}")

# 6 —— Test Set 皆為 Glove Box，無變體
ts = {t["test_set"] for t in TCS}
tg = {t["test_group"] for t in TCS}
chk(6, "Test Set 12 筆皆為 `Glove Box`，Test Group 皆為 `Vehicle Category`",
    ts == {"Glove Box"} and tg == {"Vehicle Category"},
    f"test_set={sorted(ts)}；test_group={sorted(tg)}")

# 7 —— 尾句號、引號規則
trail, sq, br, ws = [], [], [], []
for t in TCS:
    for f in FIELDS:
        for ln in t[f].split("\n"):
            s = ln.rstrip()
            if s and re.match(r"^\s*(\d+\.|[a-c]\.)", s) and s.endswith((".", "。")):
                trail.append(f"{t['leaf_id']}/{f}: {s[-40:]}")
            if ln != ln.strip():
                ws.append(f"{t['leaf_id']}/{f}")
    for f in FIELDS + ["tc_title"]:
        if re.search(r"\[[^\]]+\]|<[^>]+>", t[f]):
            br.append(f"{t['leaf_id']}/{f}")
        if re.search(r"(?<![A-Za-z])'[^']+'(?![A-Za-z])", t[f]):
            sq.append(f"{t['leaf_id']}/{f}")
chk(7, "尾句號／方括號／單引號／行首尾空白（IN §11，作者欄位）",
    not trail and not sq and not br and not ws,
    f"尾句號 {len(trail)}；單引號 {len(sq)}；方括號角括號 {len(br)}；"
    f"空白 {len(ws)}" + (f" -- {trail[:2]}{sq[:2]}{br[:2]}" if (trail or sq or br) else ""))

# 7b —— test_item 上半之來源記法。
# ⚠ 本項之判準已由「禁止」改為「驗證來源」—— **不是為了讓結果變綠**，
# 是其前提改變了：R-VC19 落條、profile
# `docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md` §1 已啟動
# IN §11 之例外。該例外之啟動條件為「when the feature profile says so」，
# 前一輪 profile 不存在故例外未啟動、本項判「禁止」；
# 現在 profile 存在且明文，故依 R-VC19(c)「lint 之職責由禁止改為驗證其來源」
# 改判。**判準改變之依據是裁決，不是結果。**
SRC = {}
try:
    import openpyxl
    _wb = openpyxl.load_workbook(
        ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx",
        read_only=True, data_only=True)
    for r in list(_wb["Analysis Report"].iter_rows(values_only=True))[7:]:
        if r[0] not in (None, ""):
            SRC[str(r[0]).strip()] = (str(r[3]).strip(), str(r[4]).strip())
except Exception as e:                      # noqa: BLE001
    SRC = {}
    print(f"（警告：037 不可讀，7b 退化為僅計數：{e}）", file=sys.stderr)

TOKEN = re.compile(r"«[^»]*»|(?<![A-Za-z])'[^']+'(?![A-Za-z])")
kept, unsourced = [], []
for t in TCS:
    for tok in TOKEN.findall(t["test_item"].split("\n\n")[0]):
        kept.append((t["leaf_id"], tok))
        ti, de = SRC.get(t["leaf_id"], ("", ""))
        if tok not in ti and tok not in de:
            unsourced.append((t["leaf_id"], tok))
chk("7b", "test_item 上半保留之來源記法對得上其來源列（R-VC19(c)）",
    bool(SRC) and not unsourced,
    f"保留 token {len(kept)} 個；未對上來源 {len(unsourced)} 個 "
    f"{unsourced or ''}"
    + ("" if SRC else "；**037 不可讀，本項未實測**"))

# 8 —— VC-033-01 帶且僅帶一處 PENDING
pat = "PENDING: DR-VC8 Glove Box lockout threshold"
cnt = {t["leaf_id"]: json.dumps(t, ensure_ascii=False).count("PENDING:")
       for t in TCS}
others = {k: v for k, v in cnt.items() if k != "SWE1-HMI-VC-033-01" and v}
one = cnt.get("SWE1-HMI-VC-033-01") == 1
exact = pat in TCS[10]["test_procedure"]
chk(8, "`VC-033-01` 帶且僅帶一處 PENDING，字串逐字相符",
    one and exact and not others,
    f"033-01 之 PENDING 數 {cnt.get('SWE1-HMI-VC-033-01')}；"
    f"字串相符 {exact}；他筆帶 PENDING {others or '無'}")

# 9 —— 流程區分（機械部分：括號下半須含 activation / deactivation）
f9 = []
for lid in ("SWE1-HMI-VC-028-02", "SWE1-HMI-VC-033-01"):
    t = next(x for x in TCS if x["leaf_id"] == lid)
    b = re.search(r"\(([^()]*)\)\s*$", t["test_item"].strip()).group(1).lower()
    if "activation" not in b and "deactivation" not in b:
        f9.append(lid)
chk(9, "`028-02`／`033-01` 之括號下半明載其流程（機械：含 activation/deactivation）",
    not f9, f"未載者 {f9 or '無'}")

# 10 —— VC-021 委派載於各 TC 之 reasoning
f10 = [t["leaf_id"] for t in TCS if "VC-021" not in t.get("reasoning", "")]
chk(10, "`VC-021` 之委派載於全部 12 筆之 reasoning（§8.2.1）",
    not f10, f"未載者 {f10 or '無'}")

# 另：test_procedure ≥ 2 步、Procedure ↔ ER 1:1、ER 無 modal
p2 = [t["leaf_id"] for t in TCS
      if len(t["test_procedure"].split("\n")) < 2]
mism = [(t["leaf_id"], len(t["test_procedure"].split("\n")),
         len(t["expected_result"].split("\n")))
        for t in TCS
        if len(t["test_procedure"].split("\n")) != len(t["expected_result"].split("\n"))]
# modal 之檢查須**排除引號內之 UI 文字** —— 彈窗原文
# "PIN must be 4 digits / OK" 之 must 是規格所載之畫面文字，
# 不是作者之 modal。初版未排除，誤報 VC-033-02（見上繳包 10 §4.3）。
def _unquoted(s):
    return re.sub(r'"[^"]*"', " ", s)


modal = [t["leaf_id"] for t in TCS
         if re.search(r"\b(shall|will|should|must)\b",
                      _unquoted(t["expected_result"]), re.I)]
verb = [t["leaf_id"] for t in TCS
        if re.search(r"^\d+\.\s*(observe|verify|check that)\b",
                     t["test_procedure"], re.I | re.M)]
chk("A", "Procedure ≥2 步 ∧ Procedure↔ER 1:1 ∧ ER 無 modal ∧ 步驟無 observe/verify 起首",
    not p2 and not mism and not modal and not verb,
    f"步數不足 {p2 or '無'}；1:1 不符 {mism or '無'}；"
    f"ER 含 modal {modal or '無'}；禁用起首動詞 {verb or '無'}")

print("verify_pilot — Glove Box pilot（R-VC18，下放包 10 §四）")
print(f"{'#':>3}  {'條件':<62} 判")
print("-" * 96)
failed = 0
for n, name, ok, detail in res:
    if not ok:
        failed += 1
    print(f"{str(n):>3}  {name:<62} {'PASS' if ok else '**FAIL**'}")
    print(f"     {detail}")
print("-" * 96)
print(f"{len(res)} checked / {failed} failed")
sys.exit(1 if failed else 0)
