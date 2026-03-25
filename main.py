import csv
import json

# with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
#     reader = list(csv.DictReader(file))
#     total_amount = 0
#     sum = 0
#     for price in reader:
#         total_amount += 1
#         sum += int(price['Price'])
#     print(round(sum/total_amount, 2))
# prices = [int(row["Price"]) for row in reader]
# print(max(prices))
# print()
# print(f"The total value is {price}")
    # list_ca = [i for i in user_data if i['state'] == "Calisfornia"]
    # print(f"The amount of Californians: {total}, out of {len(user_data)}")
total = 0
with open("data/data.json", "r", encoding="UTF-8") as file, \
        open("data/data-ca.json", "w", encoding="UTF-8") as dest:
        user_data = json.load(file)
        list_oa = [i for i in user_data if i['state'] == "California"]
        json.dump(list_oa, dest, indent=4)
        print(list_oa)


