import pandas as pd
import random
from math import ceil

table_1 = pd.read_excel("original_data.xlsx", sheet_name=0)
table_2 = pd.read_excel("original_data.xlsx", sheet_name=1)
table_3 = pd.read_excel("original_data.xlsx", sheet_name=2)

# 5)

table_2.insert(1, "Apellido", str())

def split_names(row):
    [name, last_name] = row["Representante"].split()
    row["Representante"] = name
    row["Apellido"] = last_name
    return row


table_2 = table_2.apply(split_names, axis=1)

# 4)

table_3.insert(2, "PrecioVenta", 0)
table_3.insert(3, "CostoProducción", 0)


def define_prices(row):
    match row["Descripción"][0]:
        case "A":
            base_price = 1000
        case "S":
            base_price = 500
        case "L", "M", "H":
            base_price = 300
        case "B":
            base_price = 200
        case _:
            base_price = 150
    msrp = ceil(base_price * random.random() * 1000)
    cost = ceil((msrp * random.random()) / 2)

    row["PrecioVenta"] = msrp
    row["CostoProducción"] = cost
    return row


table_3 = table_3.apply(define_prices, axis=1)
