import csv
import json
# #reader - це спеціальний тип даних. Клас в csv, який нагадує json.
# total = 0
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = csv.reader(file)
#     next(file) #пропустити рядок (в нашому випадку перший рядок, бо ми з іншими не працювали)
#     for row in reader:
#         if (row[11]) == "in_stock":
#             price = float(row[5])
#             stock = int(row[7])
#             total += price*stock
# print(f"The total value is {total}")
# #reader = list(csv.DictReader(file)) працює з автоматично створюваними словничками, де
# import csv
#reader - це спеціальний тип даних. Клас в csv, який нагадує json.
# total = 0
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         print(f"{row["Index"]} {row["Name"]}")
# #створюємо список із словничків і row - це словник
# total_sum = 0
# counter = 0
#
# def maximum(dict):
#     max = 0
#     for el in dict:
#         if int(el["Price"]) > max:
#             max = int(el["Price"])
#     return max
#
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         if row["Availability"] == "in_stock":
#             total_sum += float(row["Price"])
#             counter += 1
#     avr = total_sum/counter
# print(f"The average is {avr} and the most expensive product costs {maximum(reader)}$")
# total = 0
from tkinter import filedialog

filepath = filedialog.asksaveasfilename()

with open("data/data.json", "r", encoding = "utf-8") as file, \
        open(filepath, "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == "California":
    #         total += 1
    list_ca = [i for i in user_data if i["state"] == 'California']

    json.dump(list_ca, dest, indent=4)

    print(list_ca)
    print(f"The amount of californians is {len(list_ca)}, out of {len(user_data)}")




