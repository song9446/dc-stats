import pickle

def mean(it):
    return sum(it)/len(it) if len(it) else 0

def max_(it, key):
    return max(it, key=key) if len(it) else ""

with open('grouped.pickle', 'rb') as f:
    grouped = pickle.load(f)

stats  = [(i[0], {
    "작성 문서 수": len([j for j in i[1] if j["type"] == "doc"]),
    "작성 댓글 수": len([j for j in i[1] if j["type"] == "comm"]),
    "작성 디시콘 수": len([j for j in i[1] if j["type"] == "comm" and j["dccon"] is not None]),
    "평균 문서 길이": mean([len(j["text"]) for j in i[1] if j["type"] == "doc"]),
    "평균 댓글 길이": mean([len(j["text"]) for j in i[1] if j["type"] == "comm" and j["dccon"] is None]),
    #"가장 많이 사용한 디시콘": max_([j["dccon"] for j in i[1] if j["type"] == "comm" and j["dccon"]], key=lambda x: len(x)),
    }) for i in grouped[:50]]
for i in stats:
    print("<p>")
    print("<b>%s</b><br>"%i[0])
    for j in i[1]:
        print("%s: %d<br>"%(j, i[1][j]))
    print("</p><br>")
