import csv

# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # print(row[5])
#         if row[11] == "in_stock":
#             price = float(row[5])
#             stock = int(row[7])
#             total = price * stock
#             print(total)

# total = 0

# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         print(f"{row["Index"]} {row["Name"]}")
#     next(file)
#     for row in reader:
#         if row[11] == "in_stock":
#             price = float(row[5])
#             stock = int(row[7])
#             total += price * stock
#
# print(f"The total value is {total}")


# total = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.DictReader(file))
#     amount = len(reader)
#     for row in reader:
#         print(f"{row["Index"]} {row["Name"]}")
#
# print(f"The total value is {total}")

# total = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.reader(file))
#     prices = []
#     # quant = []
#     for row in reader:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             # quant.append(int(row[7]))
#             total += float(row[5])
#     print(f"Average is {total / len(prices)}, max value is {max(prices)}")
import json
from tkinter import filedialog
filepath = filedialog.asksaveasfilename()

total = 0
with open("data/data.json", "r", encoding="utf-8") as file,  \
        open("data/total.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == "California":
    #         total += 1
    list_cal = [i for i in user_data if i["state"] == "California"]
    json.dump(list_cal, dest, indent=4)
    print(list_cal)
    print(f"the amount of pendosu {len(list_cal)}, out of {len(user_data)}")


