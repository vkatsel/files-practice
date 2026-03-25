import csv

total_price = 0

with open("data/products-1000.csv", "r", encoding="utf-8") as file:
    reader = list(csv.DictReader(file))
    for row in reader:
        print(f"{row['Index']}{row['Name']}")
    # next(file)
    # for row in reader:
    #     if row[11] == 'in_stock':
    #         price = float(row[5])
    #         stock = int(row[7])
    #         total_price += price * stock
