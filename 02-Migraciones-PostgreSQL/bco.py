import pandas as pd

ruta = 'C:/Users/casa/Downloads/python/01-Migraciones-MariaDB/db/'
# archivos "blinkit_orders.csv", "blinkit_order_items.csv", "blinkit_products.csv"

# DataFrame para las ordenes
dfOrders = pd.read_csv(f'{ruta}blinkit_orders.csv')

print(dfOrders)