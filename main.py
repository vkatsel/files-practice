import csv
total_price = 0
with open("data/products-1000.csv", "r", encoding="utf-8") as file:
    reader = list(csv.DictReader(file))
    for row in reader:
        print(f"{row["Index"]} {row["Name"]}")
