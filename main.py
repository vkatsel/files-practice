import csv
import json

# total = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.reader(file))
#     prices = []
#     for row in reader:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             total += float(row[5])
#     print(f'Average is {total / len(prices)}, max value is {max(prices)}')

# print(f"The total value is {total}")
#
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader2=csv.reader(file)
#     prices = []
#     quant = []
#     for row in reader2:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             quant.append(int(row[7]))
#     print(f'Average is {total/sum(quant)}, max value is {max(prices)}')

from tkinter import  filedialog

filepath = filedialog.asksaveasfilename()
print(filepath)

total = 0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open(filepath, "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    list_ca = [i for i in user_data if i['state'] == "California"]

    json.dump(list_ca, dest, indent=4)

    print(list_ca)
    print(f"The amount of Californians {len(list_ca)}, out of {len(user_data)}")



