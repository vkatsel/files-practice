# import csv
#
# tot = 0
# total = 0
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = csv.reader(file)
#     prices = []
#     for row in reader:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             total += float(row[5])
#             price = float(row[5])
#             stock = int(row[7])
#             tot += price * stock
#
# print(f"the tot {tot}")
# print(f"average is {total/ len(prices)}, max is {max(prices)}")
#
# tot_price = 0
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         print(f"{row["Index"]} {row["Name"]}")

import json

# filepath = filedialog.askopenfilename()

total = 0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-ca.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == "California":
    #         total += 1
    list_ca = [i for i in user_data if i["state"] == "California"]
    json.dump(list_ca, dest , indent=4)
    print(list_ca)
    print(f"amount of caf {len(list_ca)}, out of {len(user_data)}")
    print(f"amount of caf {total}, out of {len(user_data)}")

