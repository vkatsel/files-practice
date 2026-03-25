import json

with open("data/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    total = 0
    for item in data:
        if item["state"] == "California":
            total += 1
    print(f" The amount of californians {total}, out of {len(data)}")