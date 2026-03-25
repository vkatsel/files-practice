import json
import csv

# total = 0
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = csv.reader(file)
# #    reader = list(csv.DictReader(reader))
#     next(file)
#     for row in reader:
#         if row[11] == "in_stock":
#             price = float(row[5])
#             stock = int(row[7])
#             total += price * stock
#
# print(total)
# amount = 0
# sum_price = 0
# max_price = -1
# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         price = float(row["Price"])
#         if price > max_price:
#             max_price = price
#         if row["Availability"] == "in_stock":
#             amount += 1
#             sum_price += price
# print(f"Maximum price is {max_price}. The average price is {round(sum_price / amount, 2)}")

amount_cal = 0

with open("data/data.json", "r", encoding="UTF-8") as file, \
        open('data/data_cal.json', 'w', encoding="UTF-8") as dest:
    user_data = json.load(file)
    # for user in user_data:
    #     if user['state'] == "California":
    #         amount_cal += 1
    list_ca = [user for user in user_data if user['state'] == "California"]
    json.dump(list_ca, dest, indent=4)

print(f"The amount of california users is {amount_cal} out of {len(user_data)}.")



