import csv
total_price = 0
with open("data/products-1000.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    prices = []
    quant = []
    next(file)
    for row in reader:
        if row[11] == "in_stock":
            price = float(row[5])
            stock = int(row[7])
            total_price += price * stock
            prices.append(price)
            quant.append(stock)



print(f"The total value is {total_price}, average is {sum(prices)/len(prices)}, maximum value is {max(prices)}, minimum value is {min(prices)}")