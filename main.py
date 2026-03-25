import json
#
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = csv.reader(file)
#     total = 0
#     t_stock = 0
#     t_price = 0
#     p = []
#     a = []
#     for row in reader:
#         if row[11] == "in_stock":
#             price = float(row[5])
#             stock = int(row[7])
#             total += price * stock
#             t_stock += stock
#             t_price += price
#             a.append(price)
#             p.append(price)
#     print(max(a))
#     print(t_price / len(p))
#     print(f"The total value is {total}")

with open("data/data.json", "r", encoding="UTF-8") as file, \
        open("data/data-ca.json", "w", encoding="UTF-8") as dest:
    total_s = 0
    total_e = 0
    user_data = json.load(file)
    for i in user_data:
        if i["state"] == "California":
            total_s += 1
        if i["email"].endswith("com"):
            total_e += 1
    list_ca = [i for i in user_data if i["state"] == "California"]
    json.dump(list_ca, dest, indent=4)
    print(f"The amount of CALifornians {total_s}, out of {len(user_data)}")
    print(f"The amount of com emails {total_e / len(user_data) * 100}%")