import csv
import json
#
# numb_in_stock=0
# total_in_stock=0
# prices=[]
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         print(f"{row["Index"]} {row["Name"]}")
#         if row["Availability"] == "in_stock" or row["Availability"] == "limited_stock":
#             numb_in_stock +=1
#             total_in_stock += float(row["Price"])
#             prices.append(row["Price"])
#
#
# print(f"The average price of items in stock {total_in_stock/numb_in_stock}")
# print(f"The total value is {total_in_stock}")
# print(f"The maximum price is {max(prices)}")

total=0
with open("data/data.json", "r", encoding="utf-8") as file:
        open("data/data-ca.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    list_ca = [i for i in user_data if i["state"] == "California"]
    # for el in user_data:
    #     if el["state"] == "California":
    #         total += 1

    print(f"The amount of Californians {total} out of {len(user_data)}")