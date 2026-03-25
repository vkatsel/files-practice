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
#
# print(f"The total value is {total}")
# print(f"Average is {total/len(prices)}, max value is {max(prices)}")

from tkinter import  filedialog

filepath = filedialog.askopenfilename()
print(filepath)

total = 0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == 'California':
    #         total +=1
    list_ca = [i for i in user_data if i['state'] == 'California']
    json.dump(list_ca, dest, indent=4)
    print(list_ca)
    print(f"The amount of Californians {len(list_ca)}, out of {len(user_data)}")



