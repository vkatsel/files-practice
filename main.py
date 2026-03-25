# import csv
#
# total_price = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     next(file)
#     for row in reader:
#         if row[11]=="in_stock":
#             price=float(row[5])
#             stock=int(row[7])
#             total_price+=price*stock
# print(f"The total value is {total_price}")
# #
#
#
#
# # import csv
# #
# # total_price = 0
# # with open("data/products-1000.csv", "r", encoding="utf-8") as file:
# #     reader = list(csv.DictReader(file))
# #     for row in reader:
# #         print(f"{row["Index"]} {row["Name"]}")
# #
# # print(f"The total value is {total_price}")
#
# import csv
#
# total_price = 0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = list(csv.reader(file))
#     prices=[]
#     quant=[]
#     for row in reader:
#         if row[11]=="in_stock":
#             prices.append(float(row[5]))
#             quant.append(int(row[7]))
#             total_price+=float(row[7])
#     print(total_price/len(prices), max(prices))



#
# import json
# total=0
# with open("data/data.json", "r", encoding="utf-8") as file:
#     user_data = json.load(file)
#     # for el in user_data:
#     #     if el["state"]=="California":
#     #         total+=1
#     list=[i for i in user_data if i["state"]=="California"]
#     print(list)
#     print(f"The amount of Californians {total}, out of {len(user_data)}")

from tkinter import filedialog
filepath=filedialog.askopenfilename()
print(filepath)

import json
total=0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open(filepath, "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"]=="California":
    #         total+=1
    list=[i for i in user_data if i["state"]=="California"]
    json.dump(list, dest, indent=4)
    print(list)
    print(f"The amount of Californians {total}, out of {len(user_data)}")