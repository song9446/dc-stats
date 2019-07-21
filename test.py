import dc_api
import datetime
import pickle

month = datetime.timedelta(days=30)
today = datetime.datetime.now()
month_ago = today-month

docs = []
for doc in dc_api.board(board_id="programming"):
    doc["comments"] = [comm for comm in doc["comments"]]
    for i in doc["comments"]:
        i["time"] = datetime.datetime.strptime(i["time"], "%m.%d %H:%M").replace(year=today.year)
    doc["time"] = datetime.datetime.strptime(doc["time"], "%Y.%m.%d %H:%M")
    if doc["time"] < month_ago:
        break
    print("process:", doc["time"])
    docs.append(doc)


with open('data.pickle', 'wb') as f:
    pickle.dump(docs, f)
