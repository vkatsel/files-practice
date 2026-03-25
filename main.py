import csv

total_price = 0

with open("data/products-1000.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    prices = []
    for row in reader:
        if row[11] == "in_stock":
            prices.append(float(row[5]))
    print(f"Average price is {round(sum(prices)/len(prices), 2)}, maximum price is {max(prices)}")



