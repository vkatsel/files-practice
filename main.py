import csv
import json

 # with open("data/products-1000.csv", "r", encoding="utf-8") as file:
 #     reader = csv.reader(file)
 #     next(file)
 #     for row in reader:
 #         if row[11] == "in_stock":
 #             price = float(row[5])
 #             stock = int(row[7])
 #             total += price*stock
 #             av = total / 1000
#
# print(f"the total value is {total}")

#reader = list(csv.DictReader(file)
#------------------------------------
# total = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.reader(file))
#     prices = []
#     for row in reader:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             total += float(row[5])
#     print(f"Average price: {total/len(prices)}, max price: {max(prices)}")
#------------------------------------
total = 0
with open("data/data.json", "r", encoding="utf-8") as file:
    user_data = json.load(file)
    for el in user_data:
        if el["state"] == "California":
            total = total + 1
#print(f"The amount of California users is {total}, out of {len(user_data)}")
#-----------------------------------
total = 0
with open("data/data.json", "r", encoding="utf-8") as file:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == "California":
    #         total = total + 1
    list_ca = [i for i in user_data if i["state"] == "California"]
    print(list_ca)
#print(f"The amount of California users is {len(list_ca)}, out of {len(user_data)}")
#-----------------------------------

from tkinter import filedialog

filepath = filedialog.asksaveasfilename()

with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-ca.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    list_ca = [i for i in user_data if i["state"] == "California"]

    json.dump(list_ca, dest, indent=4) #

    print(list_ca)
    print(f"The amount of California users is {len(list_ca)}, out of {len(user_data)}")