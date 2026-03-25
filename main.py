import csv
import json
#
# total =0
# with open("data/products-1000.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     prices = []
#     next(file)
#     for row in reader:
#         if row[11]=="in_stock":
#             price = float(row[5])
#             # stock = int(row[7])
#             # total += price * stock
#             total += price
#             prices.append(float(row[5]))
#
#     # reader = list(csv.DictReader(file))
#     # print(reader)  окремооооо
#     # for row in reader:
#     #     print(f"{row["Index"]} {row["Name"]}")
# print(f"the total value is {total}")
# print(f"average is {total/len(prices)}, max value is {max(prices)}")

# total =0
# with open("data/data.json", "r", encoding="utf-8") as file:
#     user_data = json.load(file)
#     # for el in user_data:
#     #     if el["state"] == "California":
#     #         total +=1
#     list_ca = [i for i in user_data if i["state"]=="California"]
#     # print(f"the amount of californians {total}, out of {len(user_data)}")
#     print(list_ca)
#     print(f"the amount of california {len(list_ca)}, out of {len(user_data)}")


# from tkinter import  filedialog об назву через окно вбить і місце тедж
# filepath = filedialog.askopenfilename()


total =0
with open("data/data.json", "r", encoding="utf-8") as file, \
        open("data/data-ca.json", "w", encoding="utf-8") as dest:
    user_data = json.load(file)
    # for el in user_data:
    #     if el["state"] == "California":
    #         total +=1
    list_ca = [i for i in user_data if i["state"]=="California"]
    json.dump(list_ca, dest, indent =4)
    # print(f"the amount of californians {total}, out of {len(user_data)}")
    print(list_ca)
    print(f"the amount of california {len(list_ca)}, out of {len(user_data)}")