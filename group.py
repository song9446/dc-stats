import itertools
import pickle

with open('data.pickle', 'rb') as f:
    docs = pickle.load(f)

print("num: %d" % len(docs))

get_author = lambda x: x["author"]
get_author = lambda x: x["author"]

corpuses = []
for doc in docs:
    corpuses.append({
        "type": "doc",
        "text": (doc["title"] + " " + doc["contents"]).replace("- dc App", "").replace("- dc official App", "").strip(),
        "time": doc["time"],
        "dccon": None,
        "author": doc["author"],
        })
    for comm in doc["comments"]:
        corpuses.append({
            "type": "comm",
            "text": comm["contents"].replace("- dc App", "").replace("- dc official App", "").strip(),
            "time": comm["time"],
            "dccon": comm["dccon"],
            "author": comm["author"],
            })


corpuses = sorted(corpuses, key=get_author)
grouped = itertools.groupby(corpuses, key=get_author)
grouped = sorted([(i,list(j)) for i,j in grouped], key=lambda x: len(x[1]), reverse=True)

with open("grouped.pickle", "wb") as f:
    pickle.dump(grouped, f)
