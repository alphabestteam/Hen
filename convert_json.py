import json


f = open('detials_of_person.json')

data = json.load(f)

data["name"] = "hen"
data["age"] = 21
data["city"] = "ganey tiqua"

print(data)

new_f = open("after_change.json","a")
new_f.write(json.dumps(data))
f.close()

