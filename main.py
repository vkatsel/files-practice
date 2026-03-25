import csv
import json

with open("data/products-1000.csv", "r") as file:
    reader = csv.reader(file)
   # next(file)
    total = 0
    # for row in reader:
    #     if row[11] == "in_stock":
    #         price = float(row[5])
    #         stock = int(row[7])
    #         total += price * stock
    #
    # print(total)

    # reader = list(csv.DictReader(file))
    # for row in reader:
    #     print(row["Index"], row["Name"])
    #
    # prices = [int(row["Price"]) for row in reader]
    # print(f"Average_Price: {sum(prices)/len(prices)}")
    # print(f"Expensive: {max(prices)}")
    #

total = 0
from tkinter import filedialog
filepath = filedialog.asksaveasfilename()

with open("data/data.json", "r", encoding="utf-8") as file, \
        open(filepath, "w") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == "California":
    #         total += 1
    list_ca = [i for i in user_data if i["state"] == 'California']
    print(f"The amount of californians: {total}")
    json.dump(list_ca, dest, indent = 4)

