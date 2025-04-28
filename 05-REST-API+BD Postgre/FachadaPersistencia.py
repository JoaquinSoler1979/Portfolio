import psycopg2, sqlite3
from Expediente.models import Expediente

def ejecutar_consulta_con_resultado(consulta):
    conexion = getConexionPostgreSQL()
    cursor = conexion.cursor()
    cursor.execute(consulta)
    
    resultado = cursor.fetchall()

    conexion.commit()
    conexion.close()
    return resultado

def ejecutar_consulta_sin_resultado(consulta):
    conexion = getConexionSQLite()
    cursor = conexion.cursor()
    
    cursor.execute(consulta)
    
    conexion.commit()
    conexion.close()

def getConexionPostgreSQL():
    
    return  psycopg2.connect(
            host="10.20.253.72",        # Dirección del servidor (puede ser IP o 'localhost') .72 es testing .75 producción
            port=5432,               # Puerto de conexión (5432 es el predeterminado)
            database="iurix",  # Nombre de la base de datos
            user="jsoler",       # Usuario de la base de datos
            password="T4nh4us3r" # Contraseña del usuario
        )

def getConexionSQLite():

    return sqlite3.connect(
            database="C:/Users/jsoler/Downloads/Python/RESTO/db.sqlite3"
    )

def actualizarDB():

    consulta = """SELECT e.exp_id AS id,
                    o.org_descr AS "Organismo",
		            CONCAT(e.exp_numero,'-',e.exp_anio) AS "Nro.Expte",
		            e.exp_carat AS "Carátula",
		            DATE(m.mov_fecha) AS "Fecha ult. mov."
                FROM iurix.exp e
                JOIN iurix.org o ON o.org_id = e.org_id
                JOIN iurix.mov m ON m.mov_id = e.exp_ultmov
                WHERE e.exp_anio = 2020"""        
    
    resultados = ejecutar_consulta_con_resultado(consulta)    

    indice = 1
    for r in resultados:      
        print(indice)
        indice = indice + 1
        try:
            exp = Expediente.objects.get(exp_id = f"{r[0]}")
        except Exception as e:
            exp = Expediente.objects.create(
                                        exp_id = f"{r[0]}",
                                        organismo = f"{r[1]}",
                                        numero = f"{r[2]}",
                                        caratula = f"{r[3]}",
                                        fechaultmov = f"{r[4]}"
            )