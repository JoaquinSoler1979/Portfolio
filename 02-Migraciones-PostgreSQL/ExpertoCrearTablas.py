#joaquin.soler.1979@gmail.com
# Experto creación de estructura de datos en la base de datos

from FachadaPersistencia import ejecutarConsultaSinResultado

def crearTablas():

    print("creando tablas")

    consulta =  """CREATE TABLE products(
                                        product_id INT PRIMARY KEY,
                                        product_name VARCHAR(15),
                                        category VARCHAR(25),
                                        brand VARCHAR(45),
                                        price FLOAT,
                                        mrp FLOAT,
                                        margin_percentage FLOAT,
                                        shelf_life_days INT,
                                        min_stock_level INT,
                                        max_stock_level INT
                                        )"""
    
    ejecutarConsultaSinResultado(consulta)

    consulta = """CREATE TABLE orders (order_id BIGINT PRIMARY KEY,
                                       customer_id BIGINT,
                                       order_date DATETIME,
                                       promised_delivery_time DATETIME,
                                       actual_delivery_time DATETIME,
                                       delivery_status VARCHAR(20),
                                       total_order FLOAT,
                                       payment_method VARCHAR(10),
                                       deliver_partner_id INT,
                                       store_id INT
                )"""
    
    ejecutarConsultaSinResultado(consulta)

    consulta = """CREATE TABLE order_items (order_id BIGINT,
                                            product_id INT,
                                            quantity INT NOT NULL,
                                            unit_price FLOAT NOT NULL,
                                            FOREIGN KEY (order_id) REFERENCES orders(order_id),
                                            FOREIGN KEY (product_id) REFERENCES products(product_id)    
                )"""
    
    ejecutarConsultaSinResultado(consulta)    
    print("tablas creadas")