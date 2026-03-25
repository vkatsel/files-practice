# import csv
#
# total = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     # reader = list(csv.DictReader(file))
#     # next(file)
#     prices = []
#     for row in reader:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             total += float(row[5])
#             # quant.append(int(row[5]))
#     #         price = float(row[5])
#     #         stock = int(row[7])
#     #         total += price * stock
# #         print(f"{row["Index"]} {row["Name"]}")
# #
# # print(f"the total value is {total}")
# # with open("data/products-1000.csv", "r", encoding="utf-8") as file:
# #     prices = []
# #     quant = []
# #     for row in reader:
# #         if row[11] == "in_stock":
# #             prices.append(float(row[5]))
# #             quant.append(int(row[7]))
#     print(f'avarege is {total / len(prices)}, max value is {max(prices)}')
#
import json
from tkinter import filedialog

filepath = filedialog.asksaveasfilename()
total =0
with open("data/data.json", "r", encoding="utf-8") as file, \
    open(filepath, "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if (el["state"] == 'California'):
    #         total += 1
    list_ca = [i for i in user_data if i['state']=="California"]
    json.dump(list_ca, dest, indent=4)
    print(list_ca)
    print(f"the amount of californians {len(list_ca)}, out of {len(user_data) }")