import json

f = open("config.json","r")

data = json.load(f)

upper_letter = data["data"].upper()

if(data["silent"]):
    print(upper_letter)

data["data"] = upper_letter
f= open("config.json","w")
f.write(json.dumps(data))

