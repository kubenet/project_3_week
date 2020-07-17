import json
from data import goals, teachers

lst =[]
lst.append(goals)
lst.append(teachers)

with open("data.json", "w") as f:
   json.dump(lst, f)
f.close

#
# f = open('data.json', 'r')
# teachers = json.loads(f.read())
# f.close

