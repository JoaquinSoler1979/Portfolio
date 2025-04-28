#joaquin.soler.1979@gmail.com
#Controlador que organiza las tareas a realizar
import ExpertoCrearTablas as ect
import ExpertoGeneradorDeConsultas as egc
import FachadaPersistencia as fp
import pandas as pd


# 1) Crear tablas
# ect.crearTablas()

# 2) Abrir la fuente de datos (archivo csv), llenar dataframe 
ruta = 'C:/Users/casa/Downloads/python/01-Migraciones-MariaDB/db/'
# archivos "blinkit_orders.csv", "blinkit_order_items.csv", "blinkit_products.csv"

# DataFrame para las ordenes
dfOrders = pd.read_csv(f'{ruta}blinkit_orders.csv')

# DataFrame para los productos
dfProducts = pd.read_csv(f'{ruta}blinkit_products.csv')

# DataFrame para las relaciones entre las órdenes y los productos
dfOrderItems = pd.read_csv(f'{ruta}blinkit_order_items.csv')

# 3) Guardar el dataframe en la base de datos
# guardar las ordenes

print("Inicializando carga de órdenes")
for i, registro in dfOrders.iterrows():
    consulta = egc.getConsultaOrders(registro[0],
                                     registro[1],
                                     registro[2],
                                     registro[3],
                                     registro[4],
                                     registro[5],
                                     registro[6],
                                     registro[7],
                                     registro[8],
                                     registro[9]
                                     )        
    fp.ejecutarConsultaSinResultado(consulta)

print("Finalizada carga de órdenes")


# guardar productos
# product_id,product_name,category,brand,price,mrp,margin_percentage,shelf_life_days,min_stock_level,max_stock_level
print("inicio carga de productos")
for i, registro in dfProducts.iterrows():
    consulta = egc.getConsultaProductos(registro[0],
                                     registro[1],
                                     registro[2],
                                     registro[3],
                                     registro[4],
                                     registro[5],
                                     registro[6],
                                     registro[7],
                                     registro[8],
                                     registro[9]
                                     )        
    fp.ejecutarConsultaSinResultado(consulta)

print("fin carga de productos")


# guardar datos de la orden/item(producto), tabla intermedia
# order_id,product_id,quantity,unit_price
print("inicio carga de ordenes/productos")
for i, registro in dfOrderItems.iterrows():
    consulta = egc.getConsultaOrdenItem(registro[0],
                                     registro[1],
                                     registro[2],
                                     registro[3]
                                     )        
    fp.ejecutarConsultaSinResultado(consulta)

print("fin carga de ordenes/productos")


    