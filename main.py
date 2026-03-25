import csv

with open("data/products-1000.csv", "r", encoding="UTF-8") as file:
    reader = list(csv.DictReader(file))
    for row in reader:
        print(f"{row['Index']} {row['Name']}")

print(f"The total value is {total}")

