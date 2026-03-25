import csv
import json
total=0

# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader=csv.reader(file)
#     next(file)
#     for row in reader:
#         if row[11] == "in_stock":
#             price = float(row[5])
#             stock = int(row[7])
#             total += price*stock

# print(f'The total value is: {total}')

# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader1=list(csv.DictReader(file))
#     for row in reader1:
#         print(f'{row["Index"]} {row["Name"]}')

# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader2=csv.reader(file)
#     prices = []
#     total1=0
#     for row in reader2:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             total1+= float(row[5])
#     print(f'Average is {total1/len(prices)}, max value is {max(prices)}')


# JSON
from tkinter import filedialog
filepath = filedialog.asksaveasfilename()
print(filepath)

with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-ca.json", "w", encoding="utf-8") as dest:
    user_data=json.load(file)
    for el in user_data:
        if el["state"]=='California':
            total+=1
    list = [i for i in user_data if i['state'] == "California"]
    json.dump(list, dest, indent=4)
    print(list)
    print(f'The amount of californians {total}, out of {len(user_data)}')

