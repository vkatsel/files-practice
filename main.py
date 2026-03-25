import csv

# total = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.DictReader(file))
#     # reader = csv.reader(file)
#     # next(file)
#     # for row in reader:
#     #     if row[11] == "in_stock":
#     #         price = float(row[5])
#     #         stock = int(row[7])
#     #         total = price*stock
#     for row in reader:
#         print(f"{row["Index"]} {row["Name"]}")
#
# print(f"The total value is {total}")
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.DictReader(file))
#     prices = []
#     for row in reader:
#         if row[11] == "in_stock":
#             prices.append(float(row[5]))
#             total += float(row[5])
# print(f"Average is {total/len(prices)} \nMax value is {max(prices)}")
import json

total = 0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-ca.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for vadym in user_data:
    #     if vadym["state"] == 'California':
    #         total += 1
    hotel_california = [i for i in user_data if i['state'] == "California"]
    # print(f"The amount of Californians is {total}, out of {len(user_data)}")

    json.dump(hotel_california, dest, indent=4)

    print(hotel_california)
    print(f"The amount of Californians is {len(hotel_california)}, out of {len(user_data)}")
