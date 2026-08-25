"""VF230 量產第 1 組：batch 1–3（W-VF69 §5）。

seq 268–417，50 條／批，依 R-VS58 選池序。
書寫式**全數取自 pilot #1 v4／pilot #2 之已核可模板**，不新創形態。

**不臆造之三道關**：
  1. 事實抽不出者不生成（`vf230_wvf69_facts.py`，逐條具名其缺何項）
  2. 標題套不進 canon §4.3 之 2–14 字者不生成（逐式試，皆不合即棄）
  3. `test_item` 取條文**逐字子字串**，不改寫（A-VS161 之教訓）
"""
import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FEAT / "scripts"))
import vf230_wvf45_priority as PR      # noqa: E402
import vf230_wvf61_pilot as P1         # noqa: E402
import vf230_wvf69_facts as FACTS      # noqa: E402

EP = "等價劃分 (Equivalence Partitioning, EP)"
FULLOP = "The HU is in the Full-Operation state"
BUS = "FD-CAN8 is connected to the bus simulator with signal tracing enabled"
MENU = "Open the Vehicle Settings menu and wait until it is fully rendered"
SEQ0, PER_BATCH, N_BATCH = 268, 50, 3
# **W-VF71 第 7 項：第 2 組（3 批 150 條）**。組別以 `--group` 指定，
# 其 seq 與批號自第 1 組續接，**不重疊**：
#   第 1 組 batch01–03 seq 268–417   第 2 組 batch04–06 seq 418–567
# 組別只決定「自選池序之第幾條起取」，**選池序本身不變**（R-VS58）。
GROUP = int(next((a.split("=")[1] for a in sys.argv[1:]
                  if a.startswith("--group=")), "1"))
assert GROUP >= 1, "--group 須 >= 1"
SKIP = PER_BATCH * N_BATCH * (GROUP - 1)      # 前組已取之條數
SEQ0 += SKIP
BATCH0 = N_BATCH * (GROUP - 1)                # 批號之偏移


def n(xs: list[str]) -> str:
    return "\n".join(f"{i}. {x}" for i, x in enumerate(xs, 1))


def pick_title(cands: list[str]) -> str | None:
    """canon §4.3：2–14 字。逐式試，取首個合者；皆不合則 None。"""
    return next((t for t in cands if 2 <= len(t.split()) <= 14), None)


# 管路句 —— 其主語為 Android／VHAL 之中介層，不述需求之觸發或結果。
# **只刪句、不改字**（A-VS161：不得改其文字）。
PLUMBING = re.compile(
    r"^\s*(?:CarPropertyService|CarPropertyManager|The Vehicle HAL|Vehicle HAL|VHAL"
    r"|VehicleConfigManager|VehicleConfigService|SystemProperties"
    r"|The response shall be returned|The configuration response shall be returned"
    r"|HW supplier shall process|The HMI layer shall send a request to"
    # ---- W-VF73 §5-1：W-VF71 第 4 項所測之 4 個漏列句型（**現准修**）----
    # #1 述訊號**如何送達** Android 層（傳輸路徑本身），非需求之觸發或結果
    r"|The HW supplier shall provide the \S+ signal to the Android Automotive"
    # #2 述中介層之處理動作，無可觀察之結果
    r"|The HMI/LTM/ETM layer shall process"
    # #3／#4 為現行列舉之近變體 —— 其漏列非概念之遺漏，
    # 而是**逐字列舉對措辭變體不具韌性**（R-VF95 二所指之「列舉之不完整」）
    r"|HW supplier shall notify"
    r"|The retrieved configuration response shall be returned"
    r")", re.I)


def clause_tail(text: str, anchor: re.Pattern) -> str:
    """自條文取 test_item —— **逐句挑選，句內逐字**。

    首版取「自結論句之錨至文末」，而多數條文之錨即第一句，
    遂 117／150 退為條文全文（中位數 698 字元，含實作層管路）。
    改為逐句挑：刪主語為中介層之管路句，其餘**逐字保留**。
    一句都不剩者退為全文（其數逐輪回報）。
    """
    sents = re.split(r"(?<=\.)\s+", text.strip())
    keep = [x for x in sents if x.strip() and not PLUMBING.match(x)]
    return " ".join(keep).strip() if keep else text.strip()


# ---- 條文自身矛盾之偵測（A-VF18 之同型，依 V23 §4.2 處置）----
# `chooses to enable …` 而其值為 Off／`chooses to disable …` 而其值為 Enable。
# **以結論句為準，於 Remarks 具名其不一致與 DR 編號，不自行調和。**
POLAR_ON = {"on", "enable", "enabled", "enableled", "enableledchime",
            "present", "true", "requested"}
POLAR_OFF = {"off", "disable", "disabled", "notenable", "zero", "absent",
             "false", "notrequest"}
CHOOSE_VERB = re.compile(r"chooses to (enable|disable)\b", re.I)


def polarity(label: str) -> str | None:
    k = re.sub(r"[^a-z0-9]", "", label.lower())
    return "ON" if k in POLAR_ON else ("OFF" if k in POLAR_OFF else None)


def contradiction_remark(text: str, label: str) -> str:
    """條文之動作動詞與其值極性相反者，回其具名文字；否則回空字串。"""
    m = CHOOSE_VERB.search(text)
    if not m:
        return ""
    want = "ON" if m.group(1).lower() == "enable" else "OFF"
    got = polarity(label)
    if not got or got == want:
        return ""
    return (f"⚠ **條文自身不一致**：其動作句為 `chooses to {m.group(1)}`，"
            f"而其 `value` 與結論句皆為 `{label}`（極性相反）。"
            "依 **V23 §4.2**（A-VF18 之處置）**以結論句為準**，本條驗 "
            f"`{label}`；**不自行調和二者**。已開 **DR-38**。")


SENT_PROXI = re.compile(r"(If [A-Za-z0-9_ ()/]+?=\s*\[|When the HMI receives the value)")
SENT_SIG = re.compile(r"(When the customer chooses|The HMI layer shall capture"
                      r"|HW supplier shall|The HW supplier shall|When the LTM or ETM)")



# ---- R-VF97：`tc_title` 之參數名形態 —— **以 PROXI 表為準，不以形態猜** ----
# R-VF97 乙令「節點／參數之別名移除」。**實測其對本組不成立**：
#   `CAN node 82 (PTGM)`  PROXI 表內**逐字如此**；`CAN node 82` 與 `PTGM` 皆不在表內
#                          → 移除別名反使標題所指之參數不存在
#   `SVC_SK_PRSNT (Surround_View_Camera)`  表內只有**括號內**者
#                          → 該保留者為括號內，非括號外
#   `(SRT)`／`(Utility_Lighting)`  表內有其括號內之名 → 剝括號即得
# 故判準改為：**取「在 PROXI 表內」之形態**（原樣／括號內／剝殼後），
# 三者皆不在表內者維持條文逐字並具名。**其依據為資料，非形態。**
_PROXI_NAMES = None


def proxi_names() -> set[str]:
    """PROXI 表之全部文字（正規化形）。**直讀 XML，不經 `proxi_known()`**
    —— 後者限於 `Format` 分頁前六欄，而別名式之名未必落於該範圍（R-VF92 一）。"""
    global _PROXI_NAMES
    if _PROXI_NAMES is None:
        import zipfile
        z = zipfile.ZipFile(FEAT / "inputs" / "PROXI_HDCC27_R3_20250424.xlsx")
        ts = re.findall(r"<t[^>]*>(.*?)</t>",
                        z.read("xl/sharedStrings.xml").decode("utf-8"), re.S)
        _PROXI_NAMES = {pnorm(t) for t in ts}
        globals()["_PROXI_RAW"] = {t.strip() for t in ts if t.strip()}
    return _PROXI_NAMES


def proxi_names_raw() -> set[str]:
    proxi_names()
    return globals().get("_PROXI_RAW", set())


def pnorm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def title_param(raw: str) -> tuple[str, str]:
    """回 (標題用之參數名, 依據)。逐式試，取**首個在 PROXI 表內**者。"""
    names = proxi_names()
    names_raw = proxi_names_raw()
    raw = raw.strip()
    # **候選之序：剝殼形態先於原樣。**
    # `pnorm()` 會吸收括號（`pnorm("(SRT)") == pnorm("SRT")`），
    # 故原樣若排在前，`(SRT)` 會被判為「表內有此形態」而把括號留在標題內
    # —— **正規化掩蓋了形態差異**（R-VF92 一所警告之「因正規化吸收」）。
    cands = []
    m = re.match(r"^\[\s*(.+?)\s*\]$", raw)
    if m:
        cands.append((m.group(1), "剝方括號"))
    m = re.match(r"^(.*?)\s*\(([^)]+)\)$", raw)
    if m:
        if m.group(1).strip():
            cands.append((m.group(1).strip(), "取括號外之主體"))
        cands.append((m.group(2).strip(), "取括號內之名（表內僅此形態）"))
    cands.append((raw, "條文逐字 —— 剝殼形態皆不在表內，而原樣在"))
    for c, why in cands:
        if pnorm(c) in names:
            return c, why
    # ---- W-VF82：**前綴唯一匹配**（表內較長之形態）----
    # 實測 9 條之條文**省略了表內名之別名段**或以 `or` 代 `/`：
    #   `CAN node 95`              表內 `CAN node 95 (ITBM/ITCM)`
    #   `CAN node 97`              表內 `CAN node 97 (PSSM)`
    #   `CAN Node 27 (ASM or ASCM)` 剝殼後 `CAN Node 27` → 表內 `CAN node 27 (ASM/ASCM)`
    # **其非「改取他標的」**（R-VF92 二）—— 二者為**同一參數之完整名與省略名**，
    # 非另一參數；且**要求其前綴匹配為唯一**，多於一者不取。
    # **其剩餘部分須以空白或 `(` 起首** —— 即表內名為「條文名 ＋ 獨立之別名段」，
    # 而非續字。**缺此守衛則 `Greeting_Light` 會命中 `Greeting_Lights_Menu`**
    # （剩餘為 `s_Menu`，續字），**而該二者正是 DR-34 所問、
    # 且 R-VF92 二明令「不得以名近推定其對應」者** —— 本判準若無此守衛，
    # 恰好造出該條所禁之推定。**本守衛即為其對治。**
    for c, _ in cands:
        if not c:
            continue
        pre = [t for t in names_raw
               if t.lower().startswith(c.lower())
               and len(t) > len(c)
               and t[len(c):len(c) + 1] in (" ", "(")]
        if len(pre) == 1:
            return pre[0], f"前綴唯一匹配（條文 `{c}` → 表內 `{pre[0]}`；其別名段獨立）"
    for c, why in cands:
        if pnorm(c) in names:
            return c, why
    return raw, "**三式皆不在 PROXI 表內** —— 維持條文逐字並具名"


# R-VF101 二：`reasoning` 之必要句（增分句後之逐字形）。缺之即 FAIL（自檢項 12）。
NEED_SENTENCE = (
    "條文未指定所收之值；值域取自 DBC；本條驗其代表值，"
    "該值為 DBC VAL_ 列舉之書寫序首項，非依 raw 大小、非條文指定。")



# ---- R-VF118：`test_item` 之括號下半 ＋ 摘句（W-VF82 全量施行）----
# canon §4.3.1 逐字：「缺括號下半 = FAIL，不得出貨」。實測 0/440 具之。
# **格式**：`<條文上半（摘句）>` ⏎（空行）`(<procedure 末步，首字小寫> -> <ER 末項>)`
# **下半之二端逐字取自該 TC 之 `test_procedure` 末步與 `expected_result` 末項**
#   —— R-VF118 一：不另創語句，其為「已寫之物之投影」。
# **上半以與括號下半之測試目的直接相關之句為限**（canon §4.3.1），
#   **只刪句不改字**（A-VS161）—— 故上半恆為條文之某一整句，不截斷。
_CONCL = re.compile(r"shall (?:not )?display|shall send|shall be sent|is displayed|"
                    r"receives the value|shall maintain/update|shall update|"
                    r"shall allow|shall prevent|= *\[", re.I)


def _sents(x: str) -> list[str]:
    return [t.strip() for t in re.split(r"(?<=\.)\s+", x.strip()) if t.strip()]


# ---- R-VF125：摘句之排除層（W-VF83）----
# **評分只能排序，不能排除**（V53 §3 逐字）—— 伴隨句同時滿足「含結論動詞」與
# 「與 `tc_title` 重疊」二條件，故評分式判準反而優先選中它。
# **實測 174／438（39.7%）之上半為伴隨句**，其上半在講「無效值之處置」
# 而下半在驗「設定之顯示」，**與 canon §4.3.1 之「直接相關」相反**。
#
# **本清單為已知集合，非全集**（R-VF95 二）—— 新形態由人讀補入並具名其輪次。
EXCLUDE_UPPER = [
    # (a) 無主詞指涉本 TC 之驗證對象者。
    #     **其變體須一併收**：V53 所報之 174 未含 `Any invalid **signal** value …`
    #     （2 條），本層實測補之 —— 收窄之判準若逐字寫死，其變體即漏。
    (re.compile(r"^Any invalid\b.{0,40}?shall be considered invalid", re.I),
     "(a) 無主詞指涉本 TC 之驗證對象"),
    # (b) 泛稱之維持／更新句。
    (re.compile(r"^The HMI layer shall maintain/update the displayed setting", re.I),
     "(b) 泛稱之維持／更新句"),
]


def excluded_upper(sent: str) -> str | None:
    for rx, why in EXCLUDE_UPPER:
        if rx.match(sent.strip()):
            return why
    return None


def summarise(item: str, title: str) -> tuple[str, str]:
    """上半：取與測試目的直接相關之句。回 (句, 依據)。

    **「取末句」為錯之規則** —— 實測 440 條中 **230 條之末句為伴隨句
    （`Any invalid value shall be considered invalid by HMI.`）或無結論動詞**，
    其與測試目的無關。故改取「含結論動詞且與 `tc_title` 之關鍵詞重疊最多」者。
    """
    ss = _sents(item)
    key = set(re.findall(r"[A-Za-z0-9_]{4,}", title))
    # **第一層：排除，先行** —— 於評分之前剔除，故評分無從再選中它。
    ss_ok = [x for x in ss if not excluded_upper(x)]
    pool = ss_ok or ss          # 全數被排除者，退回原集合再由評分處理
    cand = [x for x in pool if _CONCL.search(x)]
    if cand:
        best = max(cand, key=lambda x: (len(key & set(re.findall(r"[A-Za-z0-9_]{4,}", x))),
                                        cand.index(x)))
        return best, "結論句"
    # 二層皆無候選 → 退回末句（**排除後之末句**，非原末句）並具名
    return pool[-1], "**無結論句，退回末句**"


def bracket(proc: str, er: str) -> str:
    """下半 —— 逐字取 procedure 末步與 ER 末項，首字小寫，不另創。"""
    p = re.sub(r"^\d+\.\s*", "", [x for x in proc.split("\n") if x.strip()][-1]).strip()
    e = re.sub(r"^\d+\.\s*", "", [x for x in er.split("\n") if x.strip()][-1]).strip()
    return f"({p[:1].lower()}{p[1:]} -> {e})"




def build(f: dict, seq: int, wr: dict, refs: dict, lv: dict,
          famsize: dict | None = None,
          vcvm: dict | None = None) -> tuple[dict | None, str]:
    """`famsize`：leaf 家族 → 其可生成之條數。

    **R-VF98 之射程逐字為「同一 leaf 家族之**二條以上** TC」** ——
    家族僅一條者，無手足可與之混淆，**無條件子句之標題為合法**。
    故退化式（`<S> is not displayed`）**僅對單條家族開放**。
    缺此區分則長設定名 ＋ 長 value 之條無式可用（實測 11 條），
    而其在 W-VF71 版本中係以該退化式生成 —— 即 V35 Defect 1 所攔者。
    """
    S, form = f["setting"], f["form"]
    # ---- canon §4.3（≤14 字）與 R-VF98 二（多條家族須帶區辨）之衝突 ----
    # 實測 11 條：長設定名 ＋ 長 value（`Full Speed Forward Collision Warning
    # with Mitigation` 7 字、另一條 25 字），**任何帶 value 之式皆逾 14 字**。
    # **canon §4.3 為 canon 層之硬限制，R-VF98 二為專案層之預防性判準** ——
    # 二者衝突時 canon 優先；而 canon §4.3 之**實質**要求（手足不得逐字相同）
    # 仍由自檢項 13 守住。
    # **其區辨由正負向承擔**：`<S> is not displayed` 與
    # `<S> is displayed and modifiable` 逐字不同，非可互換。
    # 故退化式恢復為**最後手段**，而其使用**逐條具名於 `reasoning`**，
    # 並由自檢項 14 回報其數 —— **不得靜默退化**。
    degraded = False
    itd = "NA"          # R-VF91 二之佔位式覆寫之；其餘形態維持 NA
    w = wr[f["leaf_id"]]
    ref = refs.get(lv[f["leaf_id"]]["src_ref"], "")
    if not ref:
        return None, "spec_reference 未由 R-VF68 之錨鏈解出"

    if f.get("pilot3") == "預設值型":
        # ---- pilot #3（W-VF73 §4 二）----
        # **書寫式取自既有交付範例**（R-VF74 一，非自創）：
        #   `Rear camera setting defaults to off`（vehicle_setting 交付本）
        #     pre  1. The HU has been reset to factory settings
        #     proc 1. Power cycle the HU after the factory reset
        #          2. Open the … screen and check that the … setting is <V>
        #     ER   1. The HU completes start-up
        #          2. The … setting is <V>
        # **不送任何 CAN 值** —— 其所驗者為預設值，送值即改驗上行型之行為。
        msg, sig, raw, lab = f["msg"], f["sig"], f["raw"], f["label"]
        item = clause_tail(f["text"], SENT_SIG)
        title = pick_title([f"{S} defaults to {lab}",
                            f"The {S} setting defaults to {lab}"])
        pre = [FULLOP, "The HU has been reset to factory settings"]
        proc = ["Power cycle the HU after the factory reset", MENU,
                f'Read the Vehicle Settings menu and check that the {S} setting '
                f"is displayed as {lab}"]
        er = ["The HU completes start-up", "The Vehicle Settings menu is displayed",
              f"The {S} setting is displayed as {lab}"]
        remark = ""
        vsrc, reason = "2-DBC", (
            f"值域來源 **2-DBC** —— 條文逐字指名預設值 `{lab}`，"
            f"其於 `{sig}` 之 DBC 值域內為 raw {raw}（唯一命中）。"
            f"**書寫式取自既有交付範例**「Rear camera setting defaults to off」"
            f"（R-VF74 一，非自創）：factory reset ＋ power cycle ＋ 讀初始顯示。"
            f"**不送任何 CAN 值** —— 送值即改驗上行型之行為，非本條之需求。")

    elif form == "PROXI 型":
        p, v, neg = f["param"], f["value"], f["negative"]
        # R-VF97：標題用之參數名以 PROXI 表定之；
        # **`pre_conditions` 仍用條文逐字 `p`**（R-VF78 二），二者不混。
        pt, pt_why = title_param(p)
        item = clause_tail(f["text"], SENT_PROXI)
        pre = [FULLOP, f'PROXI ${p}$ is set to "{v}"']
        if neg:
            title = pick_title([
                f'{S} is not displayed when {pt} is "{v}"',
                f'{S} is not displayed when the PROXI value is "{v}"',
                # R-VF98：退化為無條件子句之式前，先試僅帶值之區辨式 ——
                # 無條件式對同家族之任兩條皆適用，不得單獨作為標題。
                f'{S} is not displayed when set to "{v}"']
                + [f'{S} is not displayed'])
            proc = ["Power cycle the HU", MENU,
                    f'Read the Vehicle Settings menu and check that the "{S}" '
                    "customer setting is not displayed"]
            er = ["The HU completes start-up", "The Vehicle Settings menu is displayed",
                  f'The "{S}" customer setting is not displayed']
        else:
            title = pick_title([
                f'{S} is displayed and modifiable when {pt} is "{v}"',
                f'{S} is displayed and modifiable when the PROXI value is "{v}"',
                f'{S} is displayed and modifiable when set to "{v}"']
                + [f'{S} is displayed and modifiable'])
            proc = ["Power cycle the HU", MENU,
                    f'Read the Vehicle Settings menu and check that the "{S}" '
                    "customer setting is displayed",
                    f'Select the "{S}" customer setting and check that its value '
                    "can be changed"]
            er = ["The HU completes start-up", "The Vehicle Settings menu is displayed",
                  f'The "{S}" customer setting is displayed',
                  f'The value of the "{S}" customer setting can be changed']
        remark = ""
        vsrc, reason = "0-CLAUSE", (
            f"值域來源 **0-CLAUSE**（R-VF13／R-VF60）—— 條文逐字帶出 `{v}`。"
            f"PROXI 參數名於 `pre_conditions` 取條文逐字 `{p}`（R-VF78 二）；"
            f"`tc_title` 取 `{pt}`（R-VF97，{pt_why}）。")

    elif form == "訊號送出型":
        msg, sig, raw, lab = f["msg"], f["sig"], f["raw"], f["label"]
        oth = f["other_label"]
        item = clause_tail(f["text"], SENT_SIG)
        title = pick_title([
            f"{msg}.{sig} is sent as {raw} ({lab}) when {S} is {lab}",
            f"{msg}.{sig} is sent as {raw} ({lab})",
            f"{sig} is sent as {raw} ({lab})"])
        pre = [FULLOP, BUS, f'The "{S}" customer setting is set to {oth}']
        proc = [MENU,
                f'Set the "{S}" customer setting to {lab} and check that '
                f"{msg}.{sig} = {raw} ({lab}) is transmitted",
                f'Read the Vehicle Settings menu and check that the {S} setting '
                f"is displayed as {lab}"]
        er = ["The Vehicle Settings menu is displayed",
              f"{msg}.{sig} = {raw} ({lab}) is sent",
              f"The {S} setting is displayed as {lab}"]
        remark = contradiction_remark(f["text"], lab)
        vsrc, reason = "2-DBC", (
            f"值域來源 **2-DBC**（R-VF13）—— `{sig}` 之 `VAL_` 內 raw {raw} = `{lab}`"
            + ("；條文逐字指名該值。" if f["value_named"] else
               "；**條文未指名值**，取 DBC 值域之最大 raw 為被驗分區，"
               f"其對偶分區 raw {f['other_raw']} = `{oth}` 置於前置。"))

    elif form == "訊號上行型":
        msg, sig, raw, lab = f["msg"], f["sig"], f["raw"], f["label"]
        oraw, olab = f["other_raw"], f["other_label"]
        item = clause_tail(f["text"], SENT_SIG)
        # R-VF98：**有區辨之式須排在無區辨之式之前**。
        # 原序將 `{S} is displayed as {lab}`（無區辨）排在第 2，
        # 致長設定名之條退化至該式而與同家族者不可分辨（實測 seq 458）。
        title = pick_title([
            f"{S} is displayed as {lab} when {sig} is {raw} ({lab})",
            f"{sig} = {raw} ({lab}) updates the {S} setting",
            f"{S} is displayed as {lab} when {sig} is {raw}",
            f"{S} is displayed as {lab}"])
        pre = [FULLOP, BUS, "The Vehicle Settings menu is open"]
        proc = [f"Send CAN: {msg}.{sig} = {oraw} ({olab})",
                f"Send CAN: {msg}.{sig} = {raw} ({lab})",
                f'Read the Vehicle Settings menu and check that the {S} setting '
                f"is displayed as {lab}"]
        er = [f"{msg}.{sig} = {oraw} ({olab}) is sent",
              f"{msg}.{sig} = {raw} ({lab}) is sent",
              f"The {S} setting is displayed as {lab}"]
        remark = contradiction_remark(f["text"], lab)
        if f.get("placeholder"):
            # ---- R-VF91 二：canon §8.4.1 之佔位形式 ----
            # `input_test_data` 列 DBC 有效值域**全集**，`test_procedure` 取其首值。
            # **末句為必要句**（R-VF91 二末）—— 缺之即為造值，自檢列 FAIL。
            # 欄內為交付語料，**全英文**（canon §8.4.1 之佔位式本身即英文）。
            dom = ", ".join(f"{r} ({l})" for r, l in
                            zip(f["domain_raw"], f["domain"]))
            # R-VF101 一：書寫序與 raw 大小序若同，須具名（否則被誤讀為依大小取值）
            same_order = f["domain_raw"] == sorted(f["domain_raw"], key=int)
            itd = f"{msg}.{sig} = one of [{dom}]"
            vsrc, reason = "2-DBC", (
                f"值域來源 **2-DBC**（R-VF91 二）—— `{sig}` 之 DBC 有效值域全集為 "
                f"{{{dom}}}"
                + (f"（已排除保留值 {'、'.join(f['excluded'])}）"
                   if f.get("excluded") else "")
                + f"，`input_test_data` 逐字列之；取列舉之首值 raw {raw} = `{lab}` "
                  f"為代表值，其次值 raw {oraw} = `{olab}` 置於 procedure 第 1 步。"
                + ("**本訊號之書寫序與 raw 大小序恰同**（R-VF101 一所令之具名）—— "
                   "取值之依據為書寫序，非大小序。" if same_order else
                   "本訊號之書寫序與 raw 大小序**不同**，取值依書寫序。")
                + NEED_SENTENCE)
        else:
            itd = "NA"
            vsrc, reason = "2-DBC", (
                f"值域來源 **2-DBC** —— `{sig}` 之 `VAL_` 內 raw {raw} = `{lab}`"
                + ("；條文逐字指名該值。" if f["value_named"] else
                   "；**條文未指名值**，依 R-VF81 一之語意側取值"
                   f"（{f.get('pick_why') or '見 facts'}），"
                   f"其對偶 raw {oraw} = `{olab}` 置於 procedure 第 1 步。"))

    elif form == "設定顯示與修改型":
        item = f["text"]
        title = pick_title([
            f"{S} customer setting is displayed and modifiable on the LTM screen",
            f"{S} customer setting is displayed and modifiable",
            f"{S} is displayed and modifiable"])
        pre = [FULLOP]
        proc = [MENU,
                f'Read the Vehicle Settings menu and check that the "{S}" customer '
                "setting is displayed",
                f'Select the "{S}" customer setting and check that its options '
                "are displayed",
                f'Select an option other than the current one and check that the '
                f'"{S}" customer setting is changed to the selected option']
        er = ["The Vehicle Settings menu is displayed",
              f'The "{S}" customer setting is displayed',
              f'The options of the "{S}" customer setting are displayed',
              f'The "{S}" customer setting is changed to the selected option']
        remark = ""
        vsrc, reason = "", (
            "本條無訊號亦無 PROXI，值域來源欄留白（非未查，而是條文本無值）。"
            "書寫式沿用 pilot #1 v4 之正向式（W-VF68 §2.1 第 3 項之回退，已核可）。")
    else:
        return None, f"形態 `{form}` 無模板"

    if not title:
        return None, f"標題逐式皆逾 canon §4.3 之 2–14 字（設定名 `{S}`）"
    # 退化＝所選之式不含區辨 token（` when `／`as|is|= <raw> (`／`as <Label>`）
    degraded = not re.search(r" when |(?:\bas|\bis|=) \d+ \(|\bas [A-Z][A-Za-z0-9_]*\b",
                             title)
    if degraded:
        fam = re.sub(r"-?\d+$", "", f["leaf_id"])
        reason += (f" **標題退化為無條件式**：帶區辨之逐式皆逾 canon §4.3 之 14 字"
                   f"（設定名 `{S}` {len(S.split())} 字）。canon §4.3 為硬限制而"
                   f"R-VF98 二為預防性判準，衝突時 canon 優先；本條與同家族"
                   f"（`{fam}`，{(famsize or {}).get(fam, 1)} 條）之區辨由正負向承擔，"
                   f"其逐字唯一性由自檢項 13 驗證。")

    title3 = lv[f["leaf_id"]]["title"].replace("\\n", " ")
    text = re.sub(r"\s+", " ", lv[f["leaf_id"]]["desc"])
    if title3 in PR.P0A:
        pri, cls = "P0", "P0(a)"
    elif title3 in PR.P0_SAFETY:
        pri, cls = "P0", "P0(c)"
    elif title3 in PR.P1_SAFETY_PRESENTATION:
        pri, cls = "P1", "P1"
    elif PR.P2_PAT.search(text):
        pri, cls = "P2", "P2"
    else:
        pri, cls = "P1", "P1"

    pending = "PENDING" in (w.get("value_source") or "")
    if pending:
        pre[1] = pre[1] + " (PENDING: DR-34)"

    # ---- R-VF111：`not clear` 之逐字轉錄補入 `remarks`（AH 欄）----
    # `R-VF15` 令「於該 TC 之 Remarks 逐字記 `Upstream Verification Criteria: …`」，
    # `R-VF26` 二令其「於 **TC 書寫時**作為 TC 內容之一部分產出」。
    # **W-VF77 之 dry-run 查出其從未履行**（67 條該有而 0 條有），
    # 而工作簿當時全空 —— **故此處補記即為「書寫時」，非回溯編輯**（R-VF111）。
    # **取逐字，不取定型句**：67 條之 `vc` 有 **34 種** distinct 值，
    # 定型句所載等同於一個旗標，而該旗標已在 `writability.tsv` 之 `vcvm_not_clear`。
    nc = (vcvm or {}).get(f["leaf_id"])
    if nc:
        lines = []
        if "not clear" in nc.get("vc", "").lower():
            lines.append(f"Upstream Verification Criteria: {nc['vc']}")
        if "not clear" in nc.get("vm", "").lower():
            lines.append(f"Upstream Verification Method: {nc['vm']}")
        if lines:
            # **既有 remark 不覆蓋**（實測標的中 0 條已有 remark，此為防未來）。
            remark = (remark + "\n" if remark else "") + "\n".join(lines)

    # R-VF118：上半（摘句）＋ 空行 ＋ 括號下半
    _up, _why = summarise(item, title)
    item = f"{_up}\n\n{bracket(n(proc), n(er))}"
    reason += f" `test_item` 之上半取{_why}（R-VF118；canon §4.3.1）。"

    return {
        "leaf_id": f["leaf_id"], "seq": seq, "test_set": w["test_set"],
        "layer3": title3, "tc_title": title, "test_item": item,
        "pre_conditions": n(pre), "input_test_data": itd,
        "test_procedure": n(proc), "expected_result": n(er),
        "specification_reference": ref, "priority": pri, "priority_class": cls,
        "design_method": EP, "writable": w["writable"],
        "dr_dependent": "DR-34" if pending else "",
        "remarks": remark, "value_source": vsrc, "clause_form": form,
        "reasoning": reason,
    }, ""


def main() -> None:
    facts, skipped = FACTS.load_all()
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    refs = P1.spec_refs()
    # R-VF111：037 之 `vc`／`vm` 逐字（僅 `not clear` 者用之）
    import vf230_wvf44_writability as WR
    vcvm = WR.vcvm()

    # R-VF98 之家族計數 —— **以 facts 全集計**（非本組），
    # 蓋家族之成員可能落於他組，只算本組會把跨組之手足誤判為單條。
    famsize: dict[str, int] = {}
    for x in facts:
        if not x.get("pending") and not x.get("pilot3"):
            k = re.sub(r"-?\d+$", "", x["leaf_id"])
            famsize[k] = famsize.get(k, 0) + 1

    # ---- 可執行內容逐字相同者之去重（W-VF74，2026-08-24）----
    # **成因**：上游有二條需求以不同措辭描述**同一可測行為**
    # （如 `SWITCH1PowerMode-005` 之 Android 屬性層寫法 與 `-030` 之顧客動作寫法，
    #  src_ref 各為 `SYS-RA-VF230_V1-2262`／`-2211`）。
    # **其產出之 TC 除 `test_item`（條文節錄）外，
    #  `pre_conditions`／`test_procedure`／`expected_result`／`input_test_data`
    #  逐字相同** —— 執行二者即做同一件事，且 `tc_title` 亦相同（canon §4.3 FAIL）。
    # **判準為機械且不涉語意推測**：可執行四欄之逐字相同。
    # **不造假區辨**（R-VF92 二）；保留首條、其餘登記並回報，開 DR。
    # **指紋於 SKIP 階段即開始累積** —— 否則跨組之重複偵測不到。
    import hashlib
    EXEC_KEYS = ("pre_conditions", "test_procedure", "expected_result",
                 "input_test_data")

    def _fp(t):
        return hashlib.sha1("\u0000".join(t[k] for k in EXEC_KEYS)
                            .encode()).hexdigest()

    seen_fp: dict[str, str] = {}
    dup_exec: list[dict] = []

    tcs, rejected, seq, taken = [], [], SEQ0, 0
    for f in facts:
        if f.get("pending"):
            continue          # R-VF81 三 —— 已隔離，見 data/vf230_isolated.tsv
        if f.get("pilot3"):
            continue          # pilot #3 之條另檔產出（seq 901–），不入量產號段
        # 前組已取者跳過 —— **以「可生成之條」計數，非以 facts 之索引計**，
        # 否則模板套不上而被 reject 者會使兩組之邊界錯位。
        if taken < SKIP:
            t0, _ = build(f, 0, wr, refs, lv, famsize, vcvm)
            if t0 is not None:
                fp = _fp(t0)
                if fp in seen_fp:
                    continue          # 前組已去重者，不計入 taken
                seen_fp[fp] = f["leaf_id"]
                taken += 1
            continue
        if len(tcs) >= PER_BATCH * N_BATCH:
            break
        t, why = build(f, seq, wr, refs, lv, famsize, vcvm)
        if t is None:
            rejected.append({"leaf_id": f["leaf_id"], "form": f["form"], "why": why})
            continue
        fp = _fp(t)
        if fp in seen_fp:
            dup_exec.append({"leaf_id": f["leaf_id"], "form": f["form"],
                             "same_as": seen_fp[fp],
                             "why": ("可執行四欄（pre／procedure／ER／input）與 "
                                     f"`{seen_fp[fp]}` **逐字相同** —— "
                                     "上游二需求描述同一可測行為，執行二者即做同一件事；"
                                     "**不造假區辨**（R-VF92 二），保留首條，本條登記待 DR")})
            continue
        seen_fp[fp] = f["leaf_id"]
        tcs.append(t)
        seq += 1

    from collections import Counter
    # ---- R-VS83：selection 欄記**算式**（各項之出處與運算），不得只記結果數 ----
    # 其成因（25 上繳 §七-2）：手算值 `574（620 − pilot 20 − 隔離 26）` 之
    # 620 在 repo 內查無落檔，故該欄之「不符」無法歸因於任一側。
    # **本欄之每一項皆自本輪實測得，不寫死。**
    pool_n = len({k for k, v in wr.items() if v["writable"] in ("W0", "W1")})
    pilot_n = len({t["leaf_id"] for f in
                   ("generated/vf230_pilot1.json", "generated/vf230_pilot2.json")
                   for t in json.loads((FEAT / f).read_text())["tcs"]})
    iso_pending = sum(1 for f in facts if f.get("pending"))
    iso_skipped = len(skipped)
    body_n = pool_n - pilot_n - iso_pending - iso_skipped
    SELECTION_FORMULA = (
        f"R-VS58 選池序。量產母體之算式（各項皆本輪實測，R-VS83）："
        f"選池 {pool_n}（`docs/reports/vf230_writability.tsv` 之 writable ∈ "
        f"{{W0,W1}}）− pilot {pilot_n}（`generated/vf230_pilot1.json` ＋ "
        f"`pilot2.json` 之 leaf_id 去重）− 隔離 {iso_pending + iso_skipped}"
        f"（其中 R-VF81 三之訊號送出型 {iso_pending}、事實抽不出 {iso_skipped}；"
        f"逐條列於 `data/vf230_isolated.tsv`）= **{body_n}**。"
        f"本組為第 {GROUP} 組，自該母體之選池序第 {SKIP + 1}–{SKIP + len(tcs)} 條取"
    )
    print(f"生成 {len(tcs)} 條，seq {SEQ0}–{seq - 1}")
    print(f"  事實抽不出而跳過（母體 574 中）：{len(skipped)}")
    print(f"  模板套不上而跳過：{len(rejected)}")
    print(f"  可執行內容與前條逐字相同而去重：{len(dup_exec)}")
    for r in dup_exec:
        print(f"    {r['leaf_id'][:42]:44} 同 {r['same_as']}")
    for r in rejected:
        print(f"    {r['leaf_id'][:44]:46} {r['why']}")

    for i in range(N_BATCH):
        part = tcs[i * PER_BATCH:(i + 1) * PER_BATCH]
        # **尾批不足額或無條時跳過** —— 末組之條數未必為 PER_BATCH 之倍數
        # （W-VF74 之末組為 22 條）。無此守衛則空批於 `part[0]` 拋錯。
        if not part:
            continue
        dist = Counter(t["priority_class"] for t in part)
        forms = Counter(t["clause_form"] for t in part)
        doc = {
            "batch": f"vf230_batch{BATCH0 + i + 1:02d}", "line": "VF230",
            "feature": "vehicle_setting / VF230", "test_group": "Vehicle Setting",
            "handoff": "docs/handoff/V29_production_start.md"
                       "（sha256 ff86f0c6242f6ac2…，7015 bytes）",
            "work_order": "W-VF69",
            "selection": SELECTION_FORMULA + "。事實抽不出者跳過並具名。"
                         "priority 分布（逐條實測）："
                         + "；".join(f"{k} {v}" for k, v in sorted(dist.items())) + "。",
            "form_distribution": dict(forms),
            "signal_notation": 'R-1 v2／R-VS52：Send CAN: MESSAGE.Signal = <raw> '
                               '(<Label>)；ER「… is sent」；procedure「… is '
                               'transmitted」；PROXI $Param$ = "值"（參數名取條文逐字，'
                               'R-VF78 二）；Input Test Data 為 NA',
            "bus": "FD-CAN8（R-VF78 一；Part 1 交付本內 `FD-CAN` 之逐字形實測 0 命中）",
            "spec_reference_source": "R-VF68：037 `Source Requirement ID` → 035 SYSRA "
                                     "`Basic Report` 之「來源需求項目 ID」",
            "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
            "templates": "pilot #1 v4（PROXI 型正負二式、設定顯示與修改型）／"
                         "pilot #2（訊號送出型、訊號上行型），皆已核可，未新創形態",
            "write_back": "**未寫回**（R-VF26）。`seq` 僅記於產出。",
            "tcs": part,
        }
        p = FEAT / f"generated/vf230_batch{BATCH0 + i + 1:02d}.json"
        p.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  batch{BATCH0 + i + 1:02d}  {len(part)} 條  seq {part[0]['seq']}–"
              f"{part[-1]['seq']}  {dict(forms)}  {dict(dist)}")

    (FEAT / f"data/_vf230_wvf69_skipped{'' if GROUP == 1 else f'_g{GROUP}'}.json").write_text(
        json.dumps({"facts_missing": skipped, "template_rejected": rejected,
                    "exec_duplicate": dup_exec},
                   ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
