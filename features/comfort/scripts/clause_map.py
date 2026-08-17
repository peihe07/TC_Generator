"""leaf → 條文原句之對齊。

IDF 詞彙重疊為主（短句之逐字相似度不可靠），另加兩項修補：
  - 切句時把過短之碎片併回前句（`5. Windshield).` 之類為列舉物，非句）
  - 低分之 leaf 若其前後鄰葉同指一句，從眾（037 之相鄰 leaf 多出自同一句）
**不加單調性**：3.2 之 037 leaf 順序與條文順序不一致（`024-07` 為第 4 句、
`024-08` 為第 3 句），單調性在該節會把兩者一起推錯。
"""
import json, re, csv, math, collections, sys
from pathlib import Path
F=Path("/Users/peihe/Work_Projects/TC_Generator/features/comfort")
sq=lambda t: " ".join(str(t).split())
docs=[json.loads(p.read_text(encoding="utf-8")) for p in sorted((F/"generated").glob("*.json"))]

def sents(t):
    raw=[sq(x) for x in re.split(r"(?<=[.;])\s+(?=[A-Z(«0-9])", t or "") if sq(x)]
    out=[]
    for s in raw:
        merge = bool(out) and (
            len(s) < 28                          # 列舉碎片（`5. Windshield).`）
            or re.match(r"^\d+[.)]", s)
            or re.search(r"\b(e\.g|i\.e|etc|vs)\.$", out[-1])   # 縮寫非句末
        )
        # 曾以「括號未閉」為併句條件，**在 7.4 上把 9 句併成 4 句** ——
        # 該節之 `((hold longer that 500 ms))` 使其後全部被吸進同一句。
        # 括號在本語料裡不是可靠的句界訊號，故不用。
        if merge: out[-1] = out[-1] + " " + s
        else: out.append(s)
    return out

tok=lambda s:[w.lower() for w in re.findall(r"[A-Za-z0-9/']+", s) if len(w)>1]
STOP=set("the a an of to in on and or is are be will shall for with that this it as at by not if when".split())
allsent=[s for d in docs for s in sents(d["source_clause"])]
df=collections.Counter()
for s in allsent: df.update(set(tok(s))-STOP)
N=len(allsent); idf=lambda w: math.log(N/(1+df.get(w,0)))

def score(item, sent):
    a=set(tok(item))-STOP; b=set(tok(sent))-STOP
    if not a or not b: return 0.0
    # F1（recall 與 precision 之調和平均）。三者實測過：
    #   cosine 之長度正規化**懲罰長句** —— 16.13 之 119-06「turns on Sync」
    #     被推去短句「Pressing AUTO…」；
    #   純 recall **獎勵長句** —— 3.2 之 024-04「Pressing A/C」被吸進
    #     那句最長的列舉句；
    #   F1 兩者皆不偏。
    inter=sum(idf(w) for w in a&b)
    if inter <= 0: return 0.0
    rec=inter/(sum(idf(w) for w in a)+1e-9)
    pre=inter/(sum(idf(w) for w in b)+1e-9)
    return 2*rec*pre/(rec+pre)

def recall(item, sent):
    a=set(tok(item))-STOP; b=set(tok(sent))-STOP
    if not a: return 0.0
    return sum(idf(w) for w in a&b)/(sum(idf(w) for w in a)+1e-9)


# 讀過條文後逐條具名之訂正（分數救不了者）。鍵為 (節, leaf)，值為句序。
OVERRIDES = {
    ("16.8", "SWE1-HVAC-113-02"): 0,   # fan speed 7/7 在 ICE7 之列舉句內
    ("16.8", "SWE1-HVAC-113-04"): 0,   # RECIRC open (LED off) 同上
    ("16.8", "SWE1-HVAC-113-05"): 0,   # turns on Sync 同上
    ("16.8", "SWE1-HVAC-113-06"): 0,   # 「activates the REAR DEFROST」在列舉句尾
    ("7.6",  "SWE1-HVAC-034-01"): 2,   # REAR CLIMATE OFF 畫面在該句，不在末句
    ("7.4",  "SWE1-HVAC-032-01"): 2,   # current degree / HI / LO
    ("7.4",  "SWE1-HVAC-032-02"): 3,   # TEMP pop-up next to slider when touching
    ("7.4",  "SWE1-HVAC-032-03"): 7,   # Metric → half degree increments
    ("7.4",  "SWE1-HVAC-032-04"): 6,   # SYNC on：調駕駛側影響乘客側
}


def leafkey(r):
    m=re.match(r"SWE1-HVAC-(\d+)(?:-(\d+))?$", r); return (int(m.group(1)), int(m.group(2) or 0))

def build():
    rows=[]
    for d in docs:
        S=sents(d["source_clause"])
        if not S: continue
        rep={}
        for tc in d["tcs"]:
            rep.setdefault(tc["req_id"], re.sub(r"\s*\([^)]*\)\s*$","",sq(tc["test_item"])))
        leaves=sorted(rep, key=leafkey)
        pick={}; best={}
        for l in leaves:
            sc=[score(rep[l],s) for s in S]
            j=max(range(len(S)), key=lambda i: sc[i])
            pick[l]=j; best[l]=sc[j]
        # 低分之修補：F1 在短 item 上不穩（其詞太少），故把候選限縮為
        # {自己之 argmax, 前一葉之句, 後一葉之句}，再以 **recall** 定奪 ——
        # 此時長度已不是變因（三者皆為該節之句），recall 問的是
        # 「這個 item 的詞，哪一句涵蓋得最全」。
        for i,l in enumerate(leaves):
            if best[l] >= 0.40: continue
            # 候選只取 {自己之 argmax, 前後鄰葉之句}。曾試過「低分即全節取
            # recall 最高者」，**在 16.8 上更糟**：短句（`Change in fan speed
            # doesn't break MAX DEF.`）以兩個高 IDF 詞就贏過那句真正的列舉句。
            # 分數救不了的，交給 §OVERRIDES 逐條具名。
            cand={pick[l]} | {pick[leaves[k]] for k in (i-1,i+1) if 0<=k<len(leaves)}
            pick[l]=max(cand, key=lambda j: (recall(rep[l], S[j]), -j))
        for l in list(pick):
            if (d["outline"], l) in OVERRIDES:
                pick[l]=OVERRIDES[(d["outline"], l)]
        for tc in d["tcs"]:
            j=pick[tc["req_id"]]
            rows.append([tc["tc_id"], tc["req_id"], d["outline"],
                         f"{score(rep[tc['req_id']],S[j]):.2f}", str(j), S[j]])
    return rows

if __name__ == "__main__":
    rows=build()
    p=F/"data/leaf_clause_sentence.tsv"
    with p.open("w",encoding="utf-8",newline="") as fh:
        w=csv.writer(fh,delimiter="\t",lineterminator="\n")
        w.writerow(["tc_id","req_id","outline","score","sent_idx","clause_verbatim"]); w.writerows(rows)
    print("rows:", len(rows))
    for o in sys.argv[1:]:
        print(f"\n=== {o} ===")
        seen=set()
        for r in rows:
            if r[2]==o and r[1] not in seen:
                seen.add(r[1]); print(f"  {r[1]:22} idx={r[4]} s={r[3]}  {r[5][:80]}")
