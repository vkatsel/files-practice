import csv

with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    next(file)
    for row in reader:
        if row[1] in reader:
            price = float(row[5])
            stock = int(row[7])
            total = price*stock

print(f"The total value is {total}")
