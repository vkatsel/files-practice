import json

with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-ca.json", "w", encoding="utf-8") as file2:
    data = json.load(file)
    list_ca = [i for i in data if i["state"] == "California"]
    json.dump(list_ca, file2, indent=4 )
    print(f"The amount of California is {len(list_ca)}, out of {len(data)} ")