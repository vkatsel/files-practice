import json
total = 0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-california.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == "California":
    #         total+=1
    list_ca = [i for i in user_data if i['state'] == 'California']
    json.dump(list_ca, dest, indent=4)

    print(dest)
    print(f"The amount of Californians {len(list_ca)}, out of {len(user_data)}")

