import csv

total = 0
with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[11] == "in_stock":
            price=float(row[5])
            stock = int(row[7])
            total += price * stock


print(f"The total value is {total}")