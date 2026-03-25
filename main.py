import csv

with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
    reader = list(csv.DictReader(file))
    total_amount = 0
    sum = 0
    for price in reader:
        total_amount += 1
        sum += int(price['Price'])
    print(round(sum/total_amount, 2))
prices = [int(row["Price"]) for row in reader]
print(max(prices))
print()


# print(f"The total value is {price}")

