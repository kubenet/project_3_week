import json
from data import goals, teachers

lst =[]
lst.append(goals)
lst.append(teachers)

with open("data.json", "w") as f:
   json.dump(lst, f)
f.close


