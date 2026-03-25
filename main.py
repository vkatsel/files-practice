import csv
#
# total = 0
# price = 0
# count = 0
# max = -10
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         if int(row["Stock"]) != 0:
#             price += float(row["Price"])
#             count +=1
#         if max < int(row["Price"]):
#             max = int(row["Price"])
#         if int(row["Price"]) == 999:
#             i = row["Name"]
# print(float((price/count)))
# print(max)
# print(i)
#

# print(f"The total value is {total}")
#     reader = csv.reader(file)
#     next(file)
#     for row in reader:
#         if row[11] == "in_stock":
#             price = float(row[5])
#             stock = int(row[7])
#             total += price * stock
#
#
# print(f"The total value is {total}")
import json
total = 0
with open("data/data.json", "r", encoding="utf-8") as file, \
    open("data/data-ca.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == 'California':
    #         total +=1
    list_ca = [i for i in user_data if i['state'] == "California"]
    json.dump(list_ca, dest, indent=4)

    print(f"The amount of Californians {len(list_ca)}, out of {len(user_data)}")
    print(list_ca)
