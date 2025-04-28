# joaquin.soler.1979@gmail.com
# Experto responsable de generar las consultas específicas para los INSERT en la BD

def getConsultaOrders(order_id, customer_id, order_date, promised_delivery_time, actual_delivery_time, delivery_status, total_order, payment_method, deliver_partner_id, store_id):

    consulta = f"""INSERT INTO orders (order_id, 
                                        customer_id, 
                                        order_date, 
                                        promised_delivery_time, 
                                        actual_delivery_time, 
                                        delivery_status, 
                                        total_order, 
                                        payment_method, 
                                        deliver_partner_id, 
                                        store_id)
                                VALUES ({order_id},
                                        {customer_id},
                                        '{order_date}',
                                        '{promised_delivery_time}',
                                        '{actual_delivery_time}',
                                        '{delivery_status}',
                                        {total_order},
                                        '{payment_method}',
                                        {deliver_partner_id},
                                        {store_id}                                
                                )"""

    return consulta

def getConsultaProductos(product_id,product_name,category,brand,price,mrp,margin_percentage,shelf_life_days,min_stock_level,max_stock_level):

    consulta = f"""INSERT INTO products (product_id,
                                        product_name,
                                        category,
                                        brand,
                                        price,
                                        mrp,
                                        margin_percentage,
                                        shelf_life_days,
                                        min_stock_level,
                                        max_stock_level)
                                VALUES ({product_id},
                                        '{product_name}',
                                        '{category}',
                                        '{brand}',
                                        {price},
                                        {mrp},
                                        {margin_percentage},
                                        {shelf_life_days},
                                        {min_stock_level},
                                        {max_stock_level}                                
                                )"""
    
    return consulta

def getConsultaOrdenItem(order_id, product_id, quantity, unit_price):

    consulta = f"""INSERT INTO order_items (order_id,
                                        product_id,
                                        quantity,
                                        unit_price)
                                VALUES ({order_id},
                                        {product_id},
                                        {quantity},
                                        {unit_price}
                                )"""
    
    return consulta