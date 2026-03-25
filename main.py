#Task1
#import csv
#
# total=0
# with open("data/products-1000.csv","r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     next(file)
#     for row in reader:
#         if row[11]=="in_stock":
#             price = float(row[5])
#             stock= int(row[7])
#             total= total+price*stock
# print(f"The total value is: {total}")
#
# total=0
# with open("data/products-1000.csv","r", encoding="utf-8") as file:
#     reader = list(csv.DictReader(file))
#     for row in reader:
#         print(f"{row["Index"]} {row["Name"]}")
#
# print(f"The total value is: {total}")
import json

#Task2
# import csv
# with open("data/products-1000.csv","r", encoding="utf-8") as file:
#       reader = list(csv.reader(file))
#       prices=[]
#       quant=[]
#       for row in reader:
#           if row[11]=="in-stock":
#               prices.append(float(row[5]))
#               quant.append(float(row[5]))
#       print(total/sum(quant), max(prices))

#Task3
# import json
# total=0
# with open("data/data.json", "r", encoding="utf-8") as file:
#     user_data = json.load(file)
#     for el in user_data:
#         if el["state"]== "California":
#             total+=1
#       dictionary= [i for i in user_data if i["stste"] == "California"]
#       print(list_ca)
#     print(f"The amount of Californians {total}, out of {len(user_data)}")

#Task4
# from tkinter import filedialog
# filepath=filedialog.asksaveasfilename()
# with open("data/data.json", "r", encoding="utf-8") as file, \
#     open("data/data.json", "w", encoding="utf-8") as dest:
#     user_data = json.load(file)
#     list_ca=[i for i in user_data if i["state"]=="California"]
#     json.dump(list_ca, dest, indent=4)
#     print(list_ca)
#     print(f"The amount of California users is {len(list_ca)}")
