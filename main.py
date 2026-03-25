import json

with open("data/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    list_ca = [i for i in data if i["state"] == "California"]
    print(f"The amount of California is {len(list_ca)}, out of {len(data)} ")